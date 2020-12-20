import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/parser/team27/G-27/execution/querie')
sys.path.append('../tytus/storage')
from querie import * 
from environment import *
from table import *
from column import *
from typ import *
from storageManager import jsonMode as admin

class Alter_Column(Querie):
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

    