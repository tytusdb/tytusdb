import sys, os.path

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

class Function_Cbrt(Expresion):

    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)    
    
    def execute(self, enviroment):
        hijo = self.hijos[0]
        res = hijo.execute(enviroment)

        if hijo.tipo.data_type == Data_Type.numeric :

            if res > -1 :
                self.tipo = Type_Expresion(Data_Type.numeric)
                self.valorExpresion = res ** (1. / 3.)
                return self.valorExpresion
            else :
                self.valorExpresion = None
                self.tipo = Type_Expresion(Data_Type.error)
                return self.valorExpresion
                
        else :
            self.tipo = Type_Expresion(Data_Type.error)
            self.valorExpresion = None
            # Reportar Error
            return self.valorExpresion

    def compile(self, enviroment):
        hijo = self.hijos[0]
        res = hijo.compile(enviroment)

        self.tipo = Type_Expresion(Data_Type.numeric)
        self.dir = instanceTemporal.getTemporal()
        self.cod = res
        self.cod += self.dir + ' = ' + hijo.dir + ' ** ( 1. / 3. )\n'
        return self.cod
        

    
    def getText(self):
        exp = self.hijos[0]
        stringReturn = 'cbrt('+ exp.getText() +')'
        return stringReturn