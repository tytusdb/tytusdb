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

class Function_Gsd(Expresion):

    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)    
    
    def execute(self, enviroment):
        hijo = self.hijos[0]
        hijo2 = self.hijos[1]
        res = hijo.execute(enviroment)
        res2 = hijo2.execute(enviroment)

        if hijo.tipo.data_type == Data_Type.numeric and hijo2.tipo.data_type == Data_Type.numeric :

            try :
                self.tipo = Type_Expresion(Data_Type.numeric)
                self.valorExpresion = math.gcd(res,res2)
                return self.valorExpresion

            except:
                self.tipo = Type_Expresion(Data_Type.error)
                self.valorExpresion = None
                return self.valorExpresion

        else :

            self.tipo = Type_Expresion(Data_Type.error)
            self.valorExpresion = None
            return self.valorExpresion
    
    def compile(self, enviroment):
        hijo = self.hijos[0]
        hijo2 = self.hijos[1]
        res = hijo.compile(enviroment)
        res2 = hijo2.compile(enviroment)

        self.tipo = Type_Expresion(Data_Type.numeric)
        self.dir = instanceTemporal.getTemporal()
        self.cod = res
        self.cod += res2
        self.cod += self.dir + ' = math.gcd(' + hijo.dir + ',' + hijo2.dir + ')\n'
        return self.cod
    
    def getText(self):
        exp = self.hijos[0]
        exp2 = self.hijos[1]
        stringReturn = 'gcd('+ exp.getText() + ',' + exp2.getText() +')'
        return stringReturn