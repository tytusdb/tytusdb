import sys, os.path

nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..')) + '\\EXPRESION\\')
sys.path.append(nodo_dir)

nodo_ast = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..','..')) + '\\ENTORNO\\')
sys.path.append(nodo_ast)

label_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..','..'))+"\\C3D\\")
sys.path.append(label_dir)

from Expresion import Expresion
from Tipo import Data_Type
from Tipo_Expresion import Type_Expresion
from Label import *
from Temporal import *

class Numeric_Expresion(Expresion):
    
    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)
        self.tipo = Data_Type.numeric

    def execute(self, enviroment):
        self.tipo = Type_Expresion(Data_Type.numeric)
        self.valorExpresion = self.valor
        return self.valorExpresion

    def compile(self, enviroment):
        self.tipo = Type_Expresion(Data_Type.numeric)
        self.dir = str(self.valor)
        self.cod = ''
        return self.cod

    def getText(self):
        return str(self.valor)