from abstract.instruccion import *
from tools.tabla_tipos import *

class drop_tb(instruccion):

    def __init__(self,id,line,column,num_nodo):
        super().__init__(line,column)
        self.id = id

        #Nodo DROP TABLE
        self.nodo = nodo_AST('DROP', num_nodo)
        self.nodo.hijos.append(nodo_AST('DROP', num_nodo + 1))
        self.nodo.hijos.append(nodo_AST('TABLE', num_nodo + 2))
        self.nodo.hijos.append(nodo_AST(id, num_nodo + 3))

        # Gramatica
        self.grammar_ = "<TR><TD>INSTRUCCION ::= drop_statement; </TD><TD>INSTRUCCION = new drop_tb(ID);</TD></TR>"

    def ejecutar(self):
        pass