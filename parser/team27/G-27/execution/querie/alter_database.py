import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/storage')
from querie import * 
from storageManager import jsonMode as admin

class alter_database(Querie):
    def __init__(self,oldName,newName, column,row):
        Querie.__init__(self,column, row)
        self.oldName= oldName
        self.newName = newName
    
    def execute(self, environment):
        
        if not isinstance(self.newName,str):
            return {'Error': 'El nombre indicado de la base de datos no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        if not isinstance(self.oldName,str):
            return {'Error': 'El nombre indicado de la base de datos no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        result = 4
        result = admin.alterDatabase(self.oldName, self.newName)  #<---------------------------
        if result == 0:
            #Se cambio correctamente el nombre a la base de datos.
            return 'Se cambio el nombre de:' + self.oldName + ' a : '+self.newName 
        elif result == 1:
            #Error al crear
            return {'Error':'Ocurrió un error en el storage manager. No se pudo cambiar el nombre de :' + self.oldName + ' a: '+self.newName, 'Fila':self.row, 'Columna':self.column}
        elif result == 2:
            #Base de datos:oldName no existe
            return {'Error':'No existe la base de datos con el nombre: ' + self.oldName, 'Fila':self.row, 'Columna':self.column}
         elif result == 3:
            #Base de datos:oldName no existe
            return {'Error':'Ya existe una base de datos con el nombre: ' + self.newName, 'Fila':self.row, 'Columna':self.column}
        else:
            return {'Error': "Error desconocido en el storage manager.", 'Fila': self.row, 'Columna': self.column}