import sys, os.path

nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\AST\\')
sys.path.append(nodo_dir)

from Nodo import Nodo

class Operator(Nodo):
    
    def __init__(self, nombreNodo, fila, columna, valor):
        Nodo.__init__(self, nombreNodo, fila, columna, valor)

    def execute(self, enviropment):
        print("f")
    
    def compile(self, enviropment):
        print("compile")
    
    def getText(self):
        return str(self.nombreNodo)