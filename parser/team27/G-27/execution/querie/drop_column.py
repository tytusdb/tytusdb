from execution.abstract.querie import * 
from execution.symbol.environment import *
from execution.symbol.table import *
from execution.symbol.column import *
from execution.symbol.typ import *
from storageManager import jsonMode as admin

class Drop_Column(Querie):
    '''
     columnName = nombre de la columna que deseamos eliminar(cadena)
     row = numero de fila(int)
     column = numero de columna(int)
    '''
    def __init__(self, columnName, row, column):
        Querie.__init__(self, row, column)
        self.columnName = columnName

    def execute(self, environment,tableName):
        if not isinstance(self.columnName,str):
            return {'Error': 'El nombre indicado de la columna no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        if not isinstance(tableName,str):
            return {'Error': 'El nombre indicado de la tabla no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        
        db_name = environment.getActualDataBase()
        database = environment.readDataBase(db_name)
        table = database.getTable(tableName)
        
        if table == None:
            return {'Error': 'la tabla: '+ tableName +'no existe en la base de datos: '+db_name, 'Fila':self.row, 'Columna': self.column }
        
        index = -1
        for i in range(len(table.columns)):
            if table.columns[i].name == self.columnName:
                index = i
                break
        if index == -1:
             return {'Error': 'la columna: '+ self.columnName +'no existe en la tabla: '+tableName, 'Fila':self.row, 'Columna': self.column }
        
        result = admin.alterDropColumn(db_name, tableName, index)

        if result == 0:
            for item in table.constraint:
                if item['type'] == 'primary':
                    if item['value'] == self.columnName:
                        return {'Error': 'la columna: '+ self.columnName +'no puede eliminarse ya que es una llave primaria de la tabla', 'Fila':self.row, 'Columna': self.column }
              
            columnDelete = table.deleteConstraint(self.columnName)      
            while columnDelete == True:
                columnDelete = table.deleteConstraint(self.columnName)              

            table.deleteColumn(self.columnName)
            #falta borrar los checks
            return 'se elimino correctamente la columna: '+self.columnName+' en la tabla: '+tableName
        elif result == 1:
            return {'Error': 'Error al ejecutar la operacion drop column', 'Fila':self.row, 'Columna': self.column }
        elif result == 2:
            return {'Error': 'La base de datos a la que hace referencia no existe', 'Fila':self.row, 'Columna': self.column }
        elif result == 3:
            return {'Error': 'La tabla: '+tableName+' no existe', 'Fila':self.row, 'Columna': self.column }
        elif result == 4:
             return {'Error': 'Llave no puede eliminarse o tabla quedarse sin columnas', 'Fila':self.row, 'Columna': self.column }
        elif result == 5:
            return {'Error': 'Columna fuera de limites', 'Fila':self.row, 'Columna': self.column }
        else:
            return {'Error': 'Error desconocido en el drop column', 'Fila':self.row, 'Columna': self.column }