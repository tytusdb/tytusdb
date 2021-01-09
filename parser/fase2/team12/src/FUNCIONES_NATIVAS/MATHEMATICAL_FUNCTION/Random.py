import sys, os.path
import math
import random

dir_nodo = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\EXPRESION\\EXPRESION\\')
sys.path.append(dir_nodo)

ent_nodo = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\ENTORNO\\')
sys.path.append(ent_nodo)

c3d_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\C3D\\')
sys.path.append(c3d_dir)

from Expresion import Expresion
from Tipo import Data_Type
from Tipo_Expresion import Type_Expresion
from Label import *
from Temporal import *

class Function_Random(Expresion):

    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)    
    
    def execute(self, enviroment):

        self.tipo = Type_Expresion(Data_Type.numeric)
        self.valorExpresion = random.random()
        return self.valorExpresion
    
    def compile(self, enviroment):
        self.tipo = Type_Expresion(Data_Type.numeric)
        self.dir = 'random.random()'
        self.cod = ''
        return self.cod
    
    def getText(self):
        stringReturn = 'random()'
        return stringReturn