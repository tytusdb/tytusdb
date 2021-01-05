from execution.abstract.querie import * 
from execution.symbol.environment import *
from execution.symbol.typ import *
from execution.querie.add_column import *
from execution.querie.drop_column import *


class Alter_Table(Querie):
    ''' 
     row = numero de fila
     column = numero de columna
     tableName = nombre de la tabla a la que le haremos el alter (cadena)
     operacion = puede ser un objeto o lista de objetos. los objetos pueden ser de tipo:
                 alter_column,alter_constraint,drop_column,drop_constraint y alter_column                 
    '''
    def __init__(self, tableName,operacion, row, column):
        Querie.__init__(self, row, column)
        self.tableName = tableName
        self.operacion = operacion

    def execute(self, environment):
        if not isinstance(self.tableName,str):
            return {'Error': 'El nombre indicado de la tabla no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        
        if isinstance(self.operacion,list):
            arreglo = []
            for item in self.operacion:
                strVar = item.execute(environment, self.tableName)
                arreglo.append(strVar)
            return arreglo
        else:   
            return self.operacion.execute(environment,self.tableName)