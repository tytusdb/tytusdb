import sys, os.path

nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\AST\\')
sys.path.append(nodo_dir)

nodo_tipo = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\ENTORNO\\')
sys.path.append(nodo_tipo)

from Nodo import Nodo
from Tipo_Expresion import Type_Expresion
from Tipo import Data_Type

class Expresion(Nodo):
    def __init__(self, nombreNodo, fila, columna, valor):
        Nodo.__init__(self, nombreNodo, fila, columna, valor)
        self.tipo = Type_Expresion(Data_Type.non)


    def execute(self, enviroment):
        print(self.nombreNodo)