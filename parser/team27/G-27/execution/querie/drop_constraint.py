from execution.abstract.querie import * 
from execution.symbol.environment import *
from execution.symbol.table import *
from execution.symbol.column import *
from execution.symbol.typ import *
from storageManager import jsonMode as admin

class Drop_Constraint(Querie):
    '''
     constName = nombre del constraint que deseamos eliminar(cadena)
     row = numero de fila(int)
     column = numero de columna(int)
    '''
    def __init__(self,constName, row, column):
        Querie.__init__(self, row, column)
        self.constName = constName

    def execute(self, environment,tableName):
        if not isinstance(self.constName,str):
            return {'Error': 'El nombre indicado del constraint no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        if not isinstance(tableName,str):
            return {'Error': 'El nombre indicado de la tabla no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        
        db_name = environment.getActualDataBase()
        database = environment.readDataBase(db_name)
        table = database.getTable(tableName)
        if table == None:
            return {'Error': 'la tabla: '+ tableName +'no existe en la base de datos: '+db_name, 'Fila':self.row, 'Columna': self.column }
        

        constDelete = readConstraint(self.constName)
        if constDelete == None:            
            return {'Error': 'la tabla: '+ tableName +' no contiene ninguna restriccion con el nombre: '+self.constName, 'Fila':self.row, 'Columna': self.column }
        
        borrarPrymari = False
        if constDelete['type'] == 'primary':
            borrarPrymari = True

        cons = table.eliminar_Constraint(self.constName)                      
        if cons == False:            
            return {'Error': 'la tabla: '+ tableName +' no contiene ninguna restriccion con el nombre: '+self.constName, 'Fila':self.row, 'Columna': self.column }
        while cons == True: 
            cons = table.eliminar_Constraint(self.constName) 

        if borrarPrymari == True:
            result = admin.alterDropPK(db_name,tableName)
            if result == 0:
                cons = table.eliminar_Constraint(self.constName)                 
                if cons == False:            
                    return {'Error': 'la tabla: '+ tableName +' no contiene ninguna restriccion con el nombre: '+self.constName, 'Fila':self.row, 'Columna': self.column }
                return 'se elimino la restriccion: '+self.constName+' de la tabla: '+tableName
            elif result == 1:
                return {'Error': 'Error en la operacion DROP CONSTRAINT ', 'Fila':self.row, 'Columna': self.column }
            elif result == 2:
                return {'Error': 'la base de datos a la que hace referencia no existe', 'Fila':self.row, 'Columna': self.column }
            elif result == 3:
                return {'Error': 'La tabla: '+tableName+' no existe en la base de datos', 'Fila':self.row, 'Columna': self.column }
            elif result == 4:
                return {'Error': 'llave primaria no existente.', 'Fila':self.row, 'Columna': self.column }
            else:
                return {'Error': 'Error desconocido en la instruccion Drop Constraint ', 'Fila':self.row, 'Columna': self.column }

        return 'se elimino la restriccion: '+self.constName+' de la tabla: '+tableName
    