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

class Add_Constraint(Querie):
    def __init__(self, columnName,constraintVal, row, column):
        Querie.__init__(self, row, column)
        self.columnName = columnName
        self.constraintVal = constraintVal

   # constraintVal es un diccionario {'type': 'unique', 'name':nombre,'value': campo_unico}
    def execute(self, environment,tableName):
        if not isinstance(self.columnName,str):
            return {'Error': 'El nombre indicado de la columna no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        if not isinstance(tableName,str):
            return {'Error': 'El nombre indicado de la tabla no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        
        db_name = environment.getActualDataBase()
        database = environment.readDataBase(db_name)
        table = database.getTable(tableName)

        repetido = False
        for item in table.constraint:
            if item['name'] == self.constraintVal['name']:
                repetido = True
                break
        if repetido == True:
             return {'Error': 'ya existe una restriccion con el mismo nombre', 'Fila':self.row, 'Columna': self.column }
        
        #columna a la que hace referencia menos el check
        if self.constraintVal['type'] != 'check':
            reference = False
            for item in table.column:
                if item.name == self.constraintVal['value']:
                    reference = True
                    break
            if reference == False:
                return {'Error': 'La columna a la que hace referencia la restriccion no existe en la tabla: '+tableName, 'Fila':self.row, 'Columna': self.column }
        
        if self.constraintVal['type'] == 'primary':
            for item in table.constraint:
                if item['value'] == self.constraintVal['value']
                    if item['type'] == 'primary':
                        return 'la columna: '+self.columnName +' ya tiene la restriccionde llave primaria'
            result = admin.extractTable(db_name, tableName)
            if isinstance(result,list):
                if len(result) > 0:
                    return {'Error': 'No se puede agregar la llave primaria a la tabla: '+tableName+' porque la tabla ya contiene valores.', 'Fila':self.row, 'Columna': self.column }
            for item in table.constraint:
                if item['type'] == 'primary':
                    self.constraintVal = {'type':self.constraintVal['type'],'name':item['name'],'value':self.constraintVal['value']}
        table.createConstraint(self.constraintVal)

        return 'la restriccion fue insertada en la tabla: '+tableName+' con exito.'




