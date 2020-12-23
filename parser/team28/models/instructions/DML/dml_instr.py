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
    def __init__(self,  table, arr_columns, arr_values) :
        self.table = table
        self.arr_columns = arr_columns
        self.arr_values = arr_values

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
            DataController().insert(self.table.id, vals_insert,0,1) # Enviar numero de fila y columna
        else:
            if len(self.arr_columns) == len(self.arr_values):
                dic = {}
                for i in range(len(self.arr_columns)):
                    id_col = self.arr_columns[i].alias
                    if id_col in dic:
                        print("CLAVE REPETIDA")
                        return
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
        table_tp = TypeChecker().searchTable(database_id, self.table.id)
        headers = TypeChecker().searchColumnHeadings(table_tp)
        checker = CreateTB(None, None, None)
        for index, name_col in enumerate(headers):
            column = TypeChecker().searchColumn(table_tp, name_col).__dict__
            print(column)
            is_correct = checker.validateType(column['_dataType'], array_values[index], False)
            if not is_correct:
                print(f'Valor no valido para la columna {name_col}')
                return False
        return True

class Update(Instruction):
    '''
        UPDATE recibe tres parametros: 
            1. tabla a insertar
            2. array de columnas con el valor a insertar (ColumnVal[])
            3. recibe un array con todas los parametros OPCIONALES
    '''
    def __init__(self,  table, arr_columns_vals, params) :
        self.table = table
        self.arr_columns_vals = arr_columns_vals
        self.params = params
    
    def __repr__(self):
        return str(vars(self))
    
    def process(self, instruction):
        #Obteniendo tabla de la cual voy a hacer el update
        database_id = SymbolTable().useDatabase
        table_tp = TypeChecker().searchTable(database_id, self.table)
        table_cont = DataController().extractTable(self.table,0,0)
        headers = TypeChecker().searchColumnHeadings(table_tp)
        table_update = pd.DataFrame(table_cont)
        table_update.columns = headers

        tuplas = [] #t[0] = nombre columna, t[1] = valor a cambiar

        for column in self.arr_columns_vals:
            tuplas.append(column.process(instruction))
        d = {}
        for t in tuplas:
            if not t[0] in headers:
                print("Columna no existe --- ERROR")
                break
            else:
                d[ headers.index(t[0]) ] = t[1].value
        print("DICTIONARY")
        print(d)
        #validando nombres de columnas ingresados
        for key in d:
            if not key in headers:
                print("Nombre de columna invalido, " + key)
                return None
        
        #validando tipo de valores para las columnas
        checker = CreateTB(None, None, None)
        for name_col in headers:
                column = TypeChecker().searchColumn(table_tp, name_col).__dict__
                if not name_col in d: #Valor Nulo --> ver si se puede
                    if column['_notNull'] == True:
                        print(f'Columna {name_col} no puede ser null')
                        return None
                    else:
                        d[name_col] = None
                else: #validar valor
                    is_correct = checker.validateType(column['_dataType'], d.get(name_col), False)
                    if not is_correct:
                        print(f'Valor no valido para la columna {name_col}')
                        return None 
        if self.params == None: #CAMBIAR TODOS LOS REGISTROS DE LA TABLA
            pk_col_name = TypeChecker().searchColPrimaryKey(table_tp).name
            pk_list = table_update[[pk_col_name]].to_numpy()
            print(pk_list)

            for pk in pk_list:
                print(self.table, d, pk)
                DataController().update(self.table, d, pk, 0 , 0)
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
    def __init__(self,  table, params) :
        self.table = table
        self.params = params
    
    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        #Obteniendo tabla de la cual voy a borrar
        database_id = SymbolTable().useDatabase
        table_tp = TypeChecker().searchTable(database_id, self.table)
        table_cont = DataController().extractTable(self.table,0,0)
        headers = TypeChecker().searchColumnHeadings(table_tp)
        table_delete = pd.DataFrame(table_cont)
        table_delete.columns = headers

        if self.params == None: #BORRAR TODOS LOS REGISTROS DE LA TABLA
            pk_col_name = TypeChecker().searchColPrimaryKey(table_tp).name
            pk_list = table_delete[[pk_col_name]].to_numpy()
            print(pk_list)

            for pk in pk_list:
                DataController().delete(self.table, pk, 0,0)
        else:
            for option in self.params:
                if isinstance(option, Where):
                    table_delete.query(option.condition.alias)
                    break
        return None
    