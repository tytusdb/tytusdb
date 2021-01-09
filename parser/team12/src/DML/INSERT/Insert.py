import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\AST\\')
sys.path.append(nodo_dir)

storage_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\storageManager\\')
sys.path.append(storage_dir)

from Nodo import Nodo
from jsonMode import showDatabases

class Insert(Nodo):
    def __init__(self, nombreNodo,fila = -1 ,columna = -1 ,valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)
        
    def compile(self):
        tmp = instanceTemporal.getTemporal()
        dir = f"{tmp} = '{self.getText()}'\n"
        dir += f'display[p] = {tmp}\n'
        dir += 'p = p + 1'
    
    def getText(self):
        table_ =  self.hijos[0].valor.upper()
        if len(self.hijos) < 3:
            return f"INSERT INTO {table_} VALUES ();"
        else:
            return f"INSERT INTO {table_} LVAL VALUES ();"

    def execute(self,enviroment = None):
        print('Llamar al insert')
