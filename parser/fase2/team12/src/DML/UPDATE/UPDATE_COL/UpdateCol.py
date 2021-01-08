import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\AST\\')
sys.path.append(nodo_dir)

storage_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\storageManager\\')
sys.path.append(storage_dir)

from Nodo import Nodo
from jsonMode import showDatabases

class UpdateCol(Nodo):
    def __init__(self, nombreNodo,fila,columna,valor):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)

    def execute(self,enviroment = None):
        print('Llamar al update')

    def addChild(self, node):
        self.hijos.append(node)
                 
    def compile(self):
        tmp = instanceTemporal.getTemporal()
        dir = f"{tmp} = \"{self.getText()}\"\n"
        dir += f'display[p] = {tmp}\n'
        dir += 'p = p + 1'
    
    def getText(self):
        table_ =  self.hijos[0].valor.upper()
        exp =  self.hijos[1].hijos[0].getText()
        return f"{table_} = {exp}"
          