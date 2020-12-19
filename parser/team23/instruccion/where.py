from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *

class where(instruccion):
    def __init__(self,expresiones, line, column, num_nodo):
        super().__init__(line,column)
        self.expresiones=expresiones
        self.nodo = nodo_AST('WHERE',num_nodo)
        print(expresiones)
        if expresiones != None:
            print('-- 1')
            for element in expresiones:
                print('-- 2')
                if element != None:
                    print('-- 3')
                    self.nodo.hijos.append(element.nodo)
         
        
    def ejecutar(self):
        pass 