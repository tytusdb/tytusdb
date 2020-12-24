from execution.abstract.querie import * 
from execution.symbol.environment import * 

class Use(Querie):
    '''
     database = nombre de la base de datos que deseamos utilizar (cadena)
     row = numero de fila(int)
     column = numero de columna(int)
    '''
    def  __init__(self, database, row, column):
        Querie.__init__(self, row, column)
        self.database = database
    
    def execute(self, environment):
        if not isinstance(self.database, str):
            return {'Error': 'El argumento no es un id, por favor verifique la sintaxis.', 'Linea': self.row, 'Columna': self.column}
        environment.setActualDataBase(self.database)
        return 'Se ha referenciado la base de datos ' +  self.database 