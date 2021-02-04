import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\AST\\')
sys.path.append(nodo_dir)

storage_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\storageManager\\')
sys.path.append(storage_dir)

c3d_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..')) + '\\C3D\\')
sys.path.append(c3d_dir)

from Temporal import *
from Label import *
from Nodo import Nodo
from jsonMode import showDatabases

class Update(Nodo):
    def __init__(self, nombreNodo,fila = -1 ,columna = -1 ,valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)

    def execute(self,enviroment = None):
        print('Llamar al update')
        
    def compile(self):
        tmp = instanceTemporal.getTemporal()
        dir = f"{tmp} = '{self.getText()}'\n"
        dir += f'display[p] = {tmp}\n'
        dir += 'p = p + 1'
        return dir
    
    def getText(self):
        table_ =  self.hijos[0].valor.upper()
        valores_= ""
        for h in self.hijos[2].hijos:
            valores_ += h.valor + ','
        valores_[0:-1]
        
        print('valores_', valores_)
        if len(self.hijos) < 4:
            return f"UPDATE {table_} SET {valores_}"
        else:
            exp =  self.hijos[3].hijos[0].getText()
            where_body = f" WHERE {exp};"
            return f"UPDATE {table_} SET {valores_} {where_body}"
        
        
    
            