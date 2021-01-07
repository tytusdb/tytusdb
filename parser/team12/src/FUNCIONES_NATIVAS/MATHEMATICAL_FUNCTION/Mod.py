import sys, os.path
import math

dir_nodo = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\EXPRESION\\EXPRESION\\')
sys.path.append(dir_nodo)

ent_nodo = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\ENTORNO\\')
sys.path.append(ent_nodo)

from Expresion import Expresion
from Tipo import Data_Type
from Tipo_Expresion import Type_Expresion

class Function_Mod(Expresion):

    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)    
    
    def execute(self, enviroment):
        hijo = self.hijos[0]
        hijo2 = self.hijos[1]
        res = hijo.execute(enviroment)
        res2 = hijo2.execute(enviroment)


        if hijo.tipo.data_type == Data_Type.numeric and hijo2.tipo.data_type == Data_Type.numeric:
            
            if res2 == 0 :

                self.tipo = Type_Expresion(Data_Type.error)
                self.valorExpresion = None
                return self.valorExpresion
            
            else :

                self.tipo = Type_Expresion(Data_Type.numeric)
                self.valorExpresion = res % res2
                return self.valorExpresion
            
        else :
            self.tipo = Type_Expresion(Data_Type.error)
            self.valorExpresion = None
            return self.valorExpresion
    
    def compile(self, enviroment):
        print("compile")
    
    def getText(self):
        exp = self.hijos[0]
        exp2 = self.hijos[1]
        stringReturn = 'mod('+ exp.getText() + ',' + exp2.getText() +')'
        return stringReturn