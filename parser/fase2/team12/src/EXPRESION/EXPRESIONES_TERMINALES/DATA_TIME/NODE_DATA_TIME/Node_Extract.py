import sys, os

nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..')) + '\\EXPRESION\\')
sys.path.append(nodo_dir)

nodo_ast = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..','..')) + '\\ENTORNO\\')
sys.path.append(nodo_ast)

from Expresion import Expresion
from Tipo import Data_Type
from Tipo_Expresion import Type_Expresion

class Extract_Expresion(Expresion):
    
    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)
        self.tipo = Data_Type.non
    
    def execute(self, eviroment):
        print("")
    
    def compile(self, eviroment):
        print("text")

    def getText(self):
        time = self.hijos[0]
        cadenaTexto2 = self.hijos[1]
        return "EXTRACT("+ time.nombreNodo + ' FROM TIMESTAMP ' + '\'' + cadenaTexto2.valor + '\''  +")"