from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *

class Isnull(instruccion):
    def __init__(self,agrupacion, expresiones,noot, line, column, num_nodo):
        super().__init__(line,column)
        self.expresiones=expresiones
        self.agrupacion=agrupacion
        self.noot=noot
        self.nodo = nodo_AST(agrupacion+' '+noot,num_nodo)
        print(expresiones)
        self.nodo.hijos.append(expresiones.nodo)         
        print('Si jala isnull 2')

    def ejecutar(self):
        pass 