from execution.abstract.querie import * 
from execution.symbol.environment import *
from execution.symbol.table import *
from execution.symbol.column import *
from execution.symbol.typ import *
from storageManager import jsonMode as admin

class Alter_Column(Querie):
    ''' 
     columnName = espera un nombre de columna debe de ser una cadena
     row = numero de fila
     column = numero de columna
     alterType = puede ser una cadena -> 'SET NOT NULL' o 'TYPE', depende la instruccion
     columnType =  si el parametro alterType = 'SET NOT NULL' este parametro se le envia un None
                   si el parametro alterType = 'TYPE :
                   espera un tipo de dato esto seria un dicionario con la siguiente sintaxis:
                   {'type':, 'length':, debe ser int, 'default':'' mandamos un valor por defecto del tipo de dato }
                   valor_type: aqui mandamos un type de la clase Database_Types
                   valor_length: si el valor_type es igual a Varchar(numero), mandar el numero, osea el tamaño del varchar, si no es varchar mandar un -1
                   valor_default: mandar un valor por defecto segun el tipo de dato(valor_type), ejemplo -> varchar(10) default -> ''(cadena vacia)
                   ejemplos diccionario:
                    {'type':DBType.numeric, 'length': -1, 'default':0 }, {'type':DBType.varchar, 'length': 20, 'default':'' }
                    
    '''
    def __init__(self,columnName,alterType,columnType, row, column):
        Querie.__init__(self, row, column)
        self.columnName = columnName
        self.alterType = alterType
        self.columnType = columnType
# columnType es un diccionario {'type':text, 'length':-1, 'default':''}
    def execute(self, environment,tableName):
        if not isinstance(self.columnName,str):
            return {'Error': 'El nombre indicado de la columna no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        if not isinstance(tableName,str):
            return {'Error': 'El nombre indicado de la tabla no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        
        db_name = environment.getActualDataBase()
        database = environment.readDataBase(db_name)
        table = database.getTable(tableName)
        if table == None:
            return {'Error': 'la tabla: '+ tableName +' no existe en la base de datos: '+db_name, 'Fila':self.row, 'Columna': self.column }
       
        columnAlter = table.readColumn(self.columnName)
        if columnAlter == None:
            return {'Error': 'la columna: '+ self.columnName +' no existe en la tabla: '+tableName, 'Fila':self.row, 'Columna': self.column }
        
        if self.alterType == 'SET NOT NULL':
            bandera = False
            for item in table.constraint:
                if item['type'] == 'not null':
                    if item['value'] == self.columnName:
                        bandera = True

            if bandera == True:            
                return 'la columna: '+self.columnName + ' ya contaba con la restriccion not_null'

            nombrenn = 'nn'+self.columnName
            notnull_constraint = {'type': 'not null', 'name':nombrenn, 'value': self.columnName}
            table.createConstraint(notnull_constraint)
            return 'se agrego la resticcion not null a la columna: '+self.columnName+' de la tabla: '+tableName
        elif self.alterType == 'TYPE':
            #poner el tipo
            if self.columnType == None:
                 return {'Error': 'El tipo al que hace refrencia no existe o esta mal escrito ', 'Fila':self.row, 'Columna': self.column }
            columnAlter.setTipo(self.columnType['type'])
            columnAlter.setLenght(self.columnType['length'])
            return 'se cambio correctamente el tipo de dato a la columna: '+self.columnName

        else:
            return {'Error': 'Error desconocido en la instruccion ALTER COLUMN', 'Fila':self.row, 'Columna': self.column }

    