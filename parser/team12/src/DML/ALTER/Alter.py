import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\AST\\')
sys.path.append(nodo_dir)

storage_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\storageManager\\')
sys.path.append(storage_dir)

from Nodo import Nodo
from jsonMode import showDatabases

class Alter(Nodo):
    def __init__(self, nombreNodo,fila = -1 ,columna = -1 ,valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)

    def execute(self,enviroment = None):
        print('Llamar al Alter')
        
    def compile(self):
        tmp = instanceTemporal.getTemporal()
        dir = f"{tmp} = '{self.getText()}'\n"
        dir += f'display[p] = {tmp}\n'
        dir += 'p = p + 1'

    def getText(self):
        if self.hijos[1].nombreNodo == "DATABASE":
            table_ =  self.hijos[1].valor.upper()
            return f"ALTER DATABASE {table_};"
        elif self.hijos[0].nombreNodo == "TABLE":
            table_ =  self.hijos[0].valor.upper()
            #exp =  self.hijos[3].hijos[0].getText()
            #where_body = f" WHERE {exp};"
            return f"ALTER TABLE {table_}"
