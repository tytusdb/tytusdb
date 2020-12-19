from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *
from storage import jsonMode as funciones
from error.errores import *

class update_st (instruccion):

    def __init__(self, id1, id2, dato, where, line, column, num_nodo):

        super().__init__(line, column)
        self.id1 = id1
        self.id2 = id2
        self.dato = dato
        self.where = where

        #Nodo AST UPDATE

        self.nodo = nodo_AST('UPDATE', num_nodo)
        self.nodo.hijos.append(nodo_AST('UPDATE', num_nodo + 1))
        self.nodo.hijos.append(nodo_AST(id1, num_nodo + 2))
        self.nodo.hijos.append(nodo_AST('SET', num_nodo + 3))
        self.nodo.hijos.append(nodo_AST(id2, num_nodo + 4))
        self.nodo.hijos.append(nodo_AST('=', num_nodo + 5))
        self.nodo.hijos.append(nodo_AST(dato, num_nodo + 6))

        if where != None:
            self.nodo.hijos.append(where.nodo)


 # Gramatica
        self.grammar_ = "<TR><TD>INSTRUCCION ::= UPDATE ID SET ID = op_val where; </TD><TD>INSTRUCCION = falta poner accicon;</TD></TR>"
        if where != None:
            self.grammar_ += where.grammar_

    def ejecutar(self):
        pass