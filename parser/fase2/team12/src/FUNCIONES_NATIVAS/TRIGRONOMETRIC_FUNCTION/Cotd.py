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

class Function_Cotd(Expresion):

    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)    
    
    def execute(self, enviroment):
        exp = self.hijos[0]
        valueExp = exp.execute(enviroment)

        if exp.tipo.data_type == Data_Type.numeric :

            try:

                self.tipo = Type_Expresion(Data_Type.numeric)
                self.valorExpresion = ( 1. / math.tan(valueExp * (math.pi / 180) ) ) 
                return self.valorExpresion

            except :

                self.tipo = Type_Expresion(Data_Type.error)
                self.valorExpresion = None
                return self.valorExpresion
        
        else :

            self.tipo = Type_Expresion(Data_Type.error)
            self.valorExpresion = None
            return self.valorExpresion

    def compile(self, enviroment):
        exp = self.hijos[0]
        valueExp = exp.compile(enviroment)

        if exp.tipo.data_type == Data_Type.numeric :

            self.tipo = Type_Expresion(Data_Type.numeric)
            self.dir = instanceTemporal.getTemporal()
            self.cod = valueExp
            self.cod += self.dir + ' =  1. / math.tan(' + exp.dir + '* (math.pi / 180))\n'
            return self.cod
        
        else :

            self.tipo = Type_Expresion(Data_Type.error)
            self.cod = ''
            self.dir = ''
            return self.cod
    
    def getText(self):
        exp = self.hijos[0]
        stringReturn = 'cotd('+ exp.getText() +')'
        return stringReturn