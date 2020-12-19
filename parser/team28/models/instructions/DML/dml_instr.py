from models.instructions.shared import Instruction
from controllers.type_checker import TypeChecker
from controllers.symbol_table import SymbolTable
from controllers.error_controller import ErrorController
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
        print("EJECUTANDO INSERT")
        #Jalando Base de Datos
        # database_id = SymbolTable().useDatabase
        database_id = 'world'
        
        # if not database_id:
        #     desc = f": Database not selected"
        #     ErrorController().addExecutionError(4, 'Execution', desc, 0, 1)#manejar linea y columna
        #     return None
        # #Base de datos existe --> Obtener tabla
        # database = TypeChecker().searchDatabase(database_id)
        # table_tp = TypeChecker().searchTable(database, self.table.value)
        # if not table_tp:
        #     desc = f": Table does not exists"
        #     ErrorController().addExecutionError(4, 'Execution', desc, 0, 1)#manejar linea y columna
        #     return None
        #Obtenida la tabla ---> TODO: VALIDAR TIPOS
        # for column in table_tp.columns:
        #     if column.
        if self.arr_columns == None:
        #Solo nos dieron los valores, tienen que venir todos ---> Espino ya valida longitud?
            vals_insert = []
            for column in self.arr_values:
                val = column.process(instruction)
                vals_insert.append(val.value)
            print(vals_insert)
            j.insert(database_id, self.table.value, vals_insert)
        else:
            if len(self.arr_columns) == len(self.arr_values):
                pass
            else:
                print("Error Datos incompletos")
        

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
    
    def process(self, instrucction):
        pass

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
    
    def process(self, instrucction):
        pass
    

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
        pass