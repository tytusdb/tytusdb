import sys, os.path
import math

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

class Function_Round(Expresion):

    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)    
    
    def execute(self, enviroment):
        op1 = self.hijos[0]
        op2 = self.hijos[1]
        res1 = op1.execute(enviroment)
        res2 = op2.execute(enviroment)

        if op1.tipo.data_type == Data_Type.numeric and op2.tipo.data_type == Data_Type.numeric :

            self.tipo = Type_Expresion(Data_Type.numeric)
            self.valorExpresion = round(res1,res2)
            return self.valorExpresion

        else :

            self.tipo = Type_Expresion(Data_Type.error)
            self.valorExpresion = None
            return self.valorExpresion
    
    def compile(self, enviroment):
        op1 = self.hijos[0]
        op2 = self.hijos[1]
        res1 = op1.compile(enviroment)
        res2 = op2.compile(enviroment)

        self.tipo = Type_Expresion(Data_Type.numeric)
        self.dir = instanceTemporal.getTemporal()
        self.cod = res1 + res2
        self.cod += self.dir + ' = round(' + op1.dir + ',' + op2.dir + ')\n'
        return self.cod
    
    def getText(self):
        exp = self.hijos[0]
        exp2 = self.hijos[1]
        stringReturn = 'round('+ exp.getText() + ',' + exp2.getText() +')'
        return stringReturn