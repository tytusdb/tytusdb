from models.instructions.shared import Instruction
from models.instructions.DDL.table_inst import CreateTB
from models.instructions.DML.special_functions import loop_list
from controllers.type_checker import TypeChecker
from controllers.symbol_table import SymbolTable
from controllers.error_controller import ErrorController
from controllers.data_controller import DataController
from models.instructions.shared import Where
import pandas as pd
from storageManager import jsonMode as j
'''
    Lenguaje de Manipulación de Datos (DML) =======================================================================================================================
'''
class Insert(Instruction):
    '''
        INSERT recibe tres parametros: 
            1. tabla a insertar
            2. columnas donde insertar (puede estar vacio (se inserta en todas))
            3. valores a insertar
    '''
    def __init__(self,  table, arr_columns, arr_values, line, column) :
        self.table = table
        self.arr_columns = arr_columns
        self.arr_values = arr_values

        self.line = line
        self.column = column

    def __repr__(self):
        return str(vars(self))
        
    def process(self, instruction):
        if self.arr_columns == None:
        #Solo nos dieron los valores, tienen que venir todos ---> Espino ya valida longitud? ---> CREO QUE SI -- TEST -- 
            vals_insert = []
            for column in self.arr_values:
                val = column.process(instruction)
                vals_insert.append(val.value)
            # print(vals_insert)
            if self.validateValues(vals_insert):
                pass
            else:
                return
            DataController().insert(self.table.alias, vals_insert, self.line, self.column)
        else:
            if len(self.arr_columns) == len(self.arr_values):
                dic = {}
                for i in range(len(self.arr_columns)):
                    id_col = self.arr_columns[i].alias
                    if id_col in dic:
                        print("CLAVE REPETIDA")
                        return None
                    else:
                        dic[id_col] = self.arr_values[i].process(instruction).value

                #Pidiendo tabla
                database_id = SymbolTable().useDatabase
                table_tp = TypeChecker().searchTable(database_id, self.table.alias)
                headers = TypeChecker().searchColumnHeadings(table_tp)
                checker = CreateTB(None, None, None)
                #validando nombres de columnas ingresados
                for key in dic:
                    if not key in headers:
                        print("Nombre de columna invalido, " + key)
                        return None
                for name_col in headers:
                    column = TypeChecker().searchColumn(table_tp, name_col).__dict__
                    if not name_col in dic: #Valor Nulo --> ver si se puede
                        if column['_notNull'] == True:
                            print(f'Columna {name_col} no puede ser null')
                            return None
                        else:
                            dic[name_col] = None
                    else: #validar valor
                        is_correct = checker.validateType(column['_dataType'], dic.get(name_col), False)
                        if not is_correct:
                            print(f'Valor no valido para la columna {name_col}')
                            return None
                        #VALIDAR CHECK
                        if not realizeCheck(column, dic):
                            return None

                #TODO: METER EL WHERE, VALIDAR UNIQUE Y VALIDAR CHECK
                ordered_vals = []
                for name_col in headers:
                    ordered_vals.append(dic.get(name_col))
                print(ordered_vals)
                DataController().insert(self.table.alias, ordered_vals,0,1) # Enviar numero de fila y columna
            else:
                print("Error Datos incompletos")
        return None
        
    def validateValues(self, array_values:[]):
        database_id = SymbolTable().useDatabase
        table_tp = TypeChecker().searchTable(database_id, self.table.alias)
        headers = TypeChecker().searchColumnHeadings(table_tp)
        if len(headers) != len(array_values):
            print("Cantidad de datos incorrecta")
            return False

        checker = CreateTB(None, None, None)
        dic =  dict(zip(headers, array_values))
        for index, name_col in enumerate(headers):
            column = TypeChecker().searchColumn(table_tp, name_col).__dict__
            is_correct = checker.validateType(column['_dataType'], array_values[index], False)
            if not is_correct:
                print(f'Valor no valido para la columna {name_col}')
                return False
            if not realizeCheck(column, dic):
                return False
        return True

class Update(Instruction):
    '''
        UPDATE recibe tres parametros: 
            1. tabla a insertar
            2. array de columnas con el valor a insertar (ColumnVal[])
            3. recibe un array con todas los parametros OPCIONALES
    '''
    def __init__(self,  table, arr_columns_vals, params, line, column) :
        self.table = table
        self.arr_columns_vals = arr_columns_vals
        self.params = params

        self.line = line
        self.column = column

    def __repr__(self):
        return str(vars(self))
    
    def process(self, instruction):
        #Obteniendo tabla de la cual voy a hacer el update
        database_id = SymbolTable().useDatabase
        table_tp = TypeChecker().searchTable(database_id, self.table)
        table_cont = DataController().extractTable(self.table,self.line, self.column)
        headers = TypeChecker().searchColumnHeadings(table_tp)
        table_update = pd.DataFrame(table_cont)

        tuplas = [] #t[0] = nombre columna, t[1] = valor a cambiar

        for column in self.arr_columns_vals:
            tuplas.append(column.process(instruction))
        d = {}
        d_col_names = {}
        #validando nombres de columnas ingresados
        for t in tuplas:
            if not t[0] in headers:
                print("Columna no existe --- ERROR")
                return None
            else:
                d[ headers.index(t[0]) ] = t[1].value
                d_col_names[t[0]] = t[1].value
        
        #validando tipo de valores para las columnas
        print(d_col_names)
        checker = CreateTB(None, None, None)
        for key in list(d_col_names.keys()):
                column = TypeChecker().searchColumn(table_tp, key).__dict__
                is_correct = checker.validateType(column['_dataType'], d_col_names.get(key), False)
                if not is_correct:
                    print(f'Valor no valido para la columna {key}')
                    return None 
                if not realizeCheck(column, d_col_names):
                    return None
        #CAMBIAR TODOS LOS REGISTROS DE LA TABLA
        if self.params == None: 
            
            pk_col_name = TypeChecker().searchColPrimaryKey(table_tp)
            if pk_col_name is None: #NO HAY LLAVE PRIMARIA
                pk_list = range(len(table_update.index))
                for pk in pk_list:
                    pk = str(pk)
                    DataController().update(self.table, d, [pk], 0 , 0)
            else:
                table_update.columns = headers
                pk_list = table_update[pk_col_name.name].tolist()
                for pk in pk_list:
                    pk = str(pk) + "|"
                    DataController().update(self.table, d, [pk], 0 , 0)
            print(pk_list)
  
        else:
            for option in self.params:
                if isinstance(option, Where):
                    table_update.query(option.condition.alias)
                    break
        return None
class ColumnVal(Instruction):
    '''
        ColumnVal recibe dos parametros: 
            1. nombre del campo a insertar
            2. valor a poner
    '''
    def __init__(self,  column, value) :
        self.column = column
        self.value = value
    
    def __repr__(self):
        return str(vars(self))
    
    def process(self, instruction):

        id_col = self.column.alias
        val = self.value.process(instruction)

        return [id_col, val]
    

class Opt1(Instruction):
    '''
        Recibe si se ha introducido un ALIAS y un asterisco (true || false)
    '''
    def __init__(self, isAsterisco, alias) :
        self.isAsterisco = isAsterisco
        self.alias = alias
    
    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        pass

class Delete(Instruction):
    '''
        DELETE recibe la tabla donde tiene que borrar y recibe un array con todas los parametros OPCIONALES
        Las opciones disponibles en un array del DELETE
        opt1 = ASTERISK SQLALIAS || ASTERISK || SQLALIAS
        opt2 = USING
        opt3 = WHERE
        opt4 = RETURNING
    '''
    def __init__(self,  table, params, line, column ) :
        self.table = table
        self.params = params
    
        self.line = line
        self.column = column

    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        #Obteniendo tabla de la cual voy a borrar
        database_id = SymbolTable().useDatabase
        table_tp = TypeChecker().searchTable(database_id, self.table)
        table_cont = DataController().extractTable(self.table,self.line, self.column)
        headers = TypeChecker().searchColumnHeadings(table_tp)
        table_delete = pd.DataFrame(table_cont)

        if self.params == None: 
            
            pk_col_name = TypeChecker().searchColPrimaryKey(table_tp)
            if pk_col_name is None: #NO HAY LLAVE PRIMARIA
                pk_list = range(len(table_delete.index))
                for pk in pk_list:
                    pk = str(pk)
                    DataController().delete(self.table, pk, self.line, self.column)

            else:
                table_delete.columns = headers
                pk_list = table_delete[pk_col_name.name].tolist()
                for pk in pk_list:
                    pk = str(pk) + "|"
                    DataController().delete(self.table, pk, self.line, self.column)
            print(pk_list)
  
        else:
            for option in self.params:
                if isinstance(option, Where):
                    table_delete.query(option.condition.alias)
                    break
        return None

def realizeCheck(column: dict, dic:dict):
        #VALIDAR CHECK
        if column['_check'] == []:
            print("NO tiene check")
            #no tiene check
        else:
            print("tiene check")
            condition = column['_check']['_condition_check']
            print(condition)
            val = eval(condition, dic)
            print(val)
            if not val:
                print("NO cumple el check: " + condition)
                return False
        return True