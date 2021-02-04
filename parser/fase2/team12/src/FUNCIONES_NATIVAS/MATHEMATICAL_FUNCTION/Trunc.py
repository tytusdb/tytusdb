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

class Function_Trunc(Expresion):


    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)    
    
    def execute(self, enviroment):
        
        cantExp = len(self.hijos)        

        if cantExp == 1 :

            exp = self.hijos[0]
            expValue = exp.execute(enviroment)

            if exp.tipo.data_type == Data_Type.numeric :

                self.tipo = Type_Expresion(Data_Type.numeric)
                self.valorExpresion = math.trunc(expValue)
                return self.valorExpresion
            
            else :

                self.tipo = Type_Expresion(Data_Type.error)
                self.valorExpresion = None
                return self.valorExpresion

        else:

            exp = self.hijos[0]
            exp2 = self.hijos[1]

            expValue = exp.execute(enviroment)
            exp2Value = exp2.execute(enviroment)

            if exp.tipo.data_type == Data_Type.numeric and exp2.tipo.data_type == Data_Type.numeric :
                
                try :

                    valor2 = int(exp2Value)
                    factor = 10.0 ** valor2
                    self.tipo = Type_Expresion(Data_Type.numeric)
                    self.valorExpresion = math.trunc(expValue * factor) / factor
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
        cantExp = len(self.hijos)        

        if cantExp == 1 :

            exp = self.hijos[0]
            expValue = exp.compile(enviroment)

            self.tipo = Type_Expresion(Data_Type.numeric)
            self.dir = instanceTemporal.getTemporal()
            self.cod = expValue
            self.cod += self.dir + ' = math.trunc(' + exp.dir + ')\n' 
            return self.cod

        else:

            exp = self.hijos[0]
            exp2 = self.hijos[1]

            expValue = exp.compile(enviroment)
            exp2Value = exp2.compile(enviroment)

            valor2 = str(instanceTemporal.getTemporal())
            factor = str(instanceTemporal.getTemporal())

            self.tipo = Type_Expresion(Data_Type.numeric)
            self.cod = expValue + exp2Value
            self.cod += valor2 + ' = int(' + exp2.dir + ')\n'                
            self.cod += factor + ' = 10.0 ** ' + valor2 + '\n'
            self.dir = instanceTemporal.getTemporal()
            self.cod += self.dir + ' = math.trunc(' + exp.dir + ' * ' + factor + ') / ' + factor + '\n'
            return self.cod
    
    def getText(self):
        
        cantExp = len(self.hijos)        

        if cantExp == 1 :

            exp = self.hijos[0]
            stringReturn = 'trunc(' + exp.getText() + ')'
            return stringReturn
        
        else:

            exp = self.hijos[0]
            exp2 = self.hijos[1]
            stringReturn = 'trunc(' + exp.getText() + ',' + exp2.getText() + ')'
            return stringReturn