from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *
from storage import jsonMode as funciones
from error.errores import *

class drop(instruccion):

    def __init__(self,id,if_exists,line,column,num_nodo):

        super().__init__(line,column)
        self.id = id
        self.if_exists = if_exists

        #Nodo DROP
        self.nodo=nodo_AST('DROP',num_nodo)
        self.nodo.hijos.append(nodo_AST('DROP',num_nodo+1))
        self.nodo.hijos.append(nodo_AST('DATABASE', num_nodo + 2))
        if if_exists != None:
            self.nodo.hijos.append(if_exists.nodo)
        self.nodo.hijos.append(nodo_AST(id, num_nodo + 3))

        # Gramatica
        self.grammar_ = "<TR><TD>INSTRUCCION ::= drop_statement; </TD><TD>INSTRUCCION = falta poner accicon;</TD></TR>"
        if if_exists != None:
            self.grammar_ = if_exists.grammar_

    def ejecutar(self):
        pass