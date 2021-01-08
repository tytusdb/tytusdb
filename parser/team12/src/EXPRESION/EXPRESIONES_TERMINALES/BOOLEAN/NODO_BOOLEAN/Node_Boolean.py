import sys, os.path

nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..')) + '\\EXPRESION\\')
sys.path.append(nodo_dir)

nodo_ast = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..','..')) + '\\ENTORNO\\')
sys.path.append(nodo_ast)

from Expresion import Expresion
from Tipo import Data_Type
from Tipo_Expresion import Type_Expresion

class Boolean_Expresion(Expresion):
    
    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)    
    
    def execute(self, enviroment):
        
        self.tipo = Type_Expresion(Data_Type.boolean)

        if self.valor.lower() == 'true':
            self.valorExpresion = True
        else:
            self.valorExpresion = False
        
        return self.valorExpresion

    def compile(self, enviroment):
        self.tipo = Type_Expresion(Data_Type.boolean)
        self.cod = ''

        if self.valor.lower() == 'true':
            self.dir = str(1)
            return self.cod
        else:
            self.dir = str(0)
            return self.cod
    
    def getText(self):
        return str(self.valor.lower())