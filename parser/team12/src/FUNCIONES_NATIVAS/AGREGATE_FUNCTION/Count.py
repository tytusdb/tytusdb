import sys, os.path
import math

dir_nodo = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\EXPRESION\\EXPRESION\\')
sys.path.append(dir_nodo)

ent_nodo = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\ENTORNO\\')
sys.path.append(ent_nodo)

variable_nodo = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
sys.path.append(variable_nodo)

from Expresion import Expresion
from Tipo import Data_Type
from Tipo_Expresion import Type_Expresion
from VariablesGlobales import * 

class FunctionCount(Expresion):

    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)    
    
    def execute(self, enviroment):
        self.hijos[0].execute(enviroment)
        self.tipo = Type_Expresion(Data_Type.numeric)
        self.valorExpresion = 1
        global selectAgregate
        selectAgregate.pop(-1)
        selectAgregate.append("COUNT")
        return 1
    
    def compile(self, enviroment):
        self.tipo = Type_Expresion(Data_Type.error)
        self.valorExpresion = None
        return self.valorExpresion 

    
    def getText(self):
        texto = "count("+ self.hijos[0].getText() +")"
        return texto