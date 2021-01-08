import sys, os.path

nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..')) + '\\EXPRESION\\')
sys.path.append(nodo_dir)

nodo_ast = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..','..')) + '\\ENTORNO\\')
sys.path.append(nodo_ast)

from Expresion import Expresion
from Tipo import Data_Type
from Tipo_Expresion import Type_Expresion

class Char_Expresion(Expresion):
    
    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)
    
    def execute(self, enviroment):
        
        self.tipo = Type_Expresion(Data_Type.character)
        newString = self.valor.replace('\\b','\b')
        newString = newString.replace('\\f','\f')
        newString = newString.replace('\\n','\n')
        newString = newString.replace('\\t','\t')
        newString = newString.replace('\\r','\r')
        self.valorExpresion = newString
        return self.valorExpresion
    
    def compile(self, enviroment):
        self.tipo = Type_Expresion(Data_Type.character)
        self.dir = '\'' + self.valor + '\''
        self.cod = ''
        return self.cod
    
    def getText(self):
        return '\''+str(self.valor)+'\''