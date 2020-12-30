from execution.abstract.querie import * 
from execution.symbol.environment import *
from execution.symbol.table import *
from storageManager import jsonMode as admin

class Drop_Table(Querie):
    '''
     tableName = nombre de la tabla que deseamos eliminar(cadena)
     row = numero de fila(int)
     column = numero de columna(int)
    '''
    def __init__(self,tableName, row, column):
        Querie.__init__(self, row, column)
        self.tableName = tableName

    def execute(self, environment):
        if not isinstance(self.tableName,str):
            return {'Error': 'El nombre indicado de la tabla no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        name = environment.getActualDataBase()
        result = 4
        result = admin.dropTable(name, self.tableName)
        if result == 0:            
            database = environment.readDataBase(name)
          
            table = database.getTable(self.tableName)
            if table == None:
                return {'Error':'Ocurrió un error en la metadata, la tabla' + self.tableName + ' no pudo ser Eliminada.', 'Fila':self.row, 'Columna':self.column}
            database.deleteTable(self.tableName)
            #metodo para verificar si existe la tabla en la base de datos
            # si existe la tabla, metodo para verificar que la tabla no sea llave foranea de otra tabla
            # si no es llave foranea, elimnar la tabla
            return 'La Tabla ' + self.tableName + ' ha sido eliminada con éxito.' 
        elif result == 1:
            #Error al crear
            return {'Error':'Ocurrió un error en el storage manager Tabla' + self.tableName + ' no pudo ser Eliminada.', 'Fila':self.row, 'Columna':self.column}
        elif result == 2:
            #Error al crear
            return {'Error':'Base de datos' + name + ' no existe.', 'Fila':self.row, 'Columna':self.column}
        elif result == 3:
            #Error al crear
            return {'Error':'La tabla: ' + self.tableName + ' no existe en la base de datos: '+name, 'Fila':self.row, 'Columna':self.column}     
        elif result == 4:
            #Error al crear
            return {'Error':'Error desconocido al intentar eliminar la tabla: '+self.tableName, 'Fila':self.row, 'Columna':self.column}