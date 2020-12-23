from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *
from abstract.retorno import *

class where(instruccion):
    def __init__(self,expresiones, line, column, num_nodo):
        super().__init__(line,column)
        self.expresiones=expresiones
        self.nodo = nodo_AST('WHERE',num_nodo)
        print(expresiones)
       # if expresiones != None:
        #    for element in expresiones:
         #       if element != None:
          #          self.nodo.hijos.append(element.nodo)
         
        self.grammar_=''
        
    def ejecutar(self, lista_id):
        return self.expresiones.ejecutar(lista_id)