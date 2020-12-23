from execution.abstract.querie import * 
from execution.symbol.environment import *
from execution.symbol.table import *
from execution.symbol.column import *
from execution.symbol.typ import *
from storageManager import jsonMode as admin

class Add_Column(Querie):
    ''' 
     columnName = espera un nombre de columna debe de ser una cadena
     row = numero de fila
     column = numero de columna
     columnType = espera un tipo de dato esto seria un dicionario con la siguiente sintaxis:
                  {'type':, 'length':, debe ser int, 'default':'' mandamos un valor por defecto del tipo de dato }
                   valor_type: aqui mandamos un type de la clase Database_Types
                   valor_length: si el valor_type es igual a Varchar(numero), mandar el numero, osea el tamaño del varchar, si no es varchar mandar un -1
                   valor_default: mandar un valor por defecto segun el tipo de dato(valor_type), ejemplo -> varchar(10) default -> ''(cadena vacia)
                   ejemplos diccionario:
                    {'type':DBType.numeric, 'length': -1, 'default':0 }, {'type':DBType.varchar, 'length': 20, 'default':'' }
                    
    '''
    def __init__(self, columnName,columnType, row, column):
        Querie.__init__(self, row, column)
        self.columnName = columnName
        self.columnType = columnType

    # columnType es un diccionario {'type':text, 'length':-1, 'default':''}
    def execute(self, environment,tableName):
        if not isinstance(self.columnName,str):
            return {'Error': 'El nombre indicado de la columna no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        if not isinstance(tableName,str):
            return {'Error': 'El nombre indicado de la tabla no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        
        # creo una nueva columna, agregar el length
        newColumn = Column(self.columnName,self.columnType['type'],self.columnType['default'],self.columnType['length'])

        db_name = environment.getActualDataBase()
        database = environment.readDataBase(db_name)
        table = database.getTable(tableName)

        if table == None:
            return {'Error': 'la tabla: '+ tableName +'no existe en la base de datos: '+db_name, 'Fila':self.row, 'Columna': self.column }
        
        table.createColumn(newColumn)

        result = admin.alterAddColumn(db_name,tableName,self.columnType['default'])

        if result == 0:
            return 'se inserto correctamente la columna: '+self.columnName+' en la tabla: '+tableName
        elif result == 1:
            return {'Error': 'Error al ejecutar la operacion add column', 'Fila':self.row, 'Columna': self.column }
        elif result == 2:
            return {'Error': 'La base de datos a la que hace referencia no existe', 'Fila':self.row, 'Columna': self.column }
        elif result == 3:
            return {'Error': 'La tabla: '+tableName+' no existe', 'Fila':self.row, 'Columna': self.column }
        else:
            return {'Error': 'Error desconocido en el add column', 'Fila':self.row, 'Columna': self.column }