from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *

class group_by(instruccion):
    def __init__(self,expresiones, line, column, num_nodo):
        super().__init__(line,column)
        self.expresiones=expresiones

        #AST
        self.nodo = nodo_AST('GROUP BY',num_nodo)
        self.nodo.hijos.append(nodo_AST('GROUP BY',num_nodo+1))
        self.nodo.hijos.append(nodo_AST(str(expresiones), num_nodo + 2))

        #Gramatica
        self.grammar_ = '<TR><TD> group_by ::= GROUP BY list_id </TD><TD> group_by = new group_by(); </TD></TR>\n'
        self.grammar_ += '<TR><TD> list_id ::= list_id </TD><TD> list_id = [] </TD></TR>\n'


    def ejecutar(self):
        return self.expresiones
