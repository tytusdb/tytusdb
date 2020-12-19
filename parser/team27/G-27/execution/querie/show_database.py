import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/storage')
from querie import * 
from storageManager import jsonMode as admin
from texttable import Texttable

class drop_database(Querie):
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
            listaTabla=[]
            listaTabla.append(["bases de datos"])
            for item in result:
                listaTabla.append([item])
            t = Texttable()
            t.add_rows(listaTabla)
            newTabla = str(t.draw())
            return newTabla