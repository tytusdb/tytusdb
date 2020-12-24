from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *
from abstract.retorno import *

class where(instruccion):
    def __init__(self,expresiones, line, column, num_nodo):
        super().__init__(line,column)
        self.expresiones=expresiones
        self.nodo = nodo_AST('WHERE',num_nodo)
        #print(expresiones)
        self.nodo.hijos.append(nodo_AST('WHERE',num_nodo+1))
        self.nodo.hijos.append(expresiones.nodo)

        #Gramatica
        self.grammar_ = '<TR><TD> donde ::= WHERE expression  </TD><TD> donde = new where(); </TD></TR>\n'
        self.grammar_ += expresiones.grammar_

    def ejecutar(self, lista_id):
        return self.expresiones.ejecutar(lista_id)