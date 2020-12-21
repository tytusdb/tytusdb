from abstract.instruccion import *
from tools.tabla_tipos import *

class delete_from (instruccion):
    def __init__(self,ID1, ID2, OP_VAL, line, column, num_nodo):

        super().__init__(line,column)
        self.ID1 = ID1
        self.ID2 = ID2
        self.OP_VAL = OP_VAL

        #Nodo DELETE FROM
        self.nodo = nodo_AST('DELETE', num_nodo)
        self.nodo.hijos.append(nodo_AST('DELETE', num_nodo+1))
        self.nodo.hijos.append(nodo_AST('FROM', num_nodo + 2))
        self.nodo.hijos.append(nodo_AST(ID1, num_nodo + 3))
        self.nodo.hijos.append(nodo_AST('WHERE', num_nodo + 4))
        self.nodo.hijos.append(nodo_AST(ID2, num_nodo + 5))
        self.nodo.hijos.append(nodo_AST('=', num_nodo + 6))
        self.nodo.hijos.append(nodo_AST(OP_VAL, num_nodo + 7))

        #Grammar
        self.grammar_ = "<TR><TD>INSTRUCCION ::= DELETE FROM ID WHERE ID = op_val ;''' </TD><TD>INSTRUCCION = falta poner accicon;</TD></TR>"

    def ejecutar(self):
        pass