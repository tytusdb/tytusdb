import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/storage')
from querie import * 
from storageManager import jsonMode as admin
from prettytable import PrettyTable

class drop_database(Querie):
    '''
     row = numero de fila(int)
     column = numero de columna(int)
    '''
    def __init__(self,column,row):
        Querie.__init__(self,column, row)
    #Valor de retorno: lista de strings con los nombres de las bases de datos, si ocurrió un error o no hay bases de datos devuelve una lista vacía [].
    def execute(self, environment):              
        result = showDatabases()  #<---------------------------
        
        if not isinstance(result,list):
            return {'Error': 'La funcion showdatabase(), no retorna un objeto lista', 'Fila':self.row, 'Columna': self.column }
        
        
        if len(result) == 0:
            #Se elimino correctamente la base de datos
            return 'No hay bases de datos para mostrar, ya sea porque no existe ninguna base de datos o porque ocurrio un error desconocido'
        else:
            x = PrettyTable()
            x.add_column("bases",result)
            #print(x.get_string())
            return x.get_string()