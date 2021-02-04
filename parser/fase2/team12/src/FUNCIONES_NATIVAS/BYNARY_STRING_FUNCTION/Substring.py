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

class Function_Substring(Expresion):

    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)    
    
    def execute(self, enviroment):
        exp = self.hijos[0]
        exp2 = self.hijos[1]
        exp3 = self.hijos[2]
        
        valueExp = exp.execute(enviroment)
        valueExp2 = exp2.execute(enviroment)
        valueExp3 = exp3.execute(enviroment)

        if exp.tipo.data_type == Data_Type.character :
            
            if exp2.tipo.data_type == Data_Type.numeric and exp3.tipo.data_type == Data_Type.numeric :

                try :
                    
                    rango = slice(valueExp2-1, valueExp3)
                    self.tipo = Type_Expresion(Data_Type.character)
                    self.valorExpresion = valueExp[rango]
                    return self.valorExpresion

                except :
                    
                    self.tipo = Type_Expresion(Data_Type.error)
                    self.valorExpresion = None
                    return self.valorExpresion

            else :

                self.tipo = Type_Expresion(Data_Type.error)
                self.valorExpresion = None
                return self.valorExpresion

        else :

            self.tipo = Type_Expresion(Data_Type.error)
            self.valorExpresion = None
            return self.valorExpresion
    
    def compile(self, enviroment):
        exp = self.hijos[0]
        exp2 = self.hijos[1]
        exp3 = self.hijos[2]
        
        valueExp = exp.execute(enviroment)
        valueExp2 = exp2.execute(enviroment)
        valueExp3 = exp3.execute(enviroment)

        rango = instanceTemporal.getTemporal()
        self.cod = valueExp + valueExp2 + valueExp3
        self.cod += rango + ' = slice(' + exp2.dir + '-1, ' + exp3.dir + ')\n'
        self.dir = instanceTemporal.getTemporal()
        self.cod += self.dir + ' = ' + exp.dir + '[' + rango + ']\n'
        return self.cod
    
    def getText(self):

        exp = self.hijos[0]
        exp2 = self.hijos[1]
        exp3 = self.hijos[2]

        stringReturn = 'substring(' + exp.getText() + ',' + exp2.getText() + ',' + exp3.getText() + ')'
        return stringReturn