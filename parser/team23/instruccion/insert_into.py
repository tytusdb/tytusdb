from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *
from storage import jsonMode as funciones
from error.errores import *

class insert_into  (instruccion):

    def __init__(self,dato,lista,line,column,num_nodo):
        super().__init__(line, column)
        self.dato = dato
        self.lista = lista

        #Nodo AST INSERT INTO
        self.nodo = nodo_AST('INSERT INTO', num_nodo)
        self.nodo.hijos.append(nodo_AST('INSERT INTO',num_nodo+1))
        self.nodo.hijos.append(nodo_AST(dato, num_nodo + 2))
        self.nodo.hijos.append(nodo_AST('VALUES', num_nodo + 3))
        self.nodo.hijos.append(nodo_AST('(', num_nodo + 4))
        self.nodo.hijos.append(nodo_AST(lista, num_nodo + 5))
        self.nodo.hijos.append(nodo_AST(')', num_nodo + 6))

        # Gramatica
        self.grammar_ = "<TR><TD>INSTRUCCION ::= INSERT INTO ID VALUE (list_val); </TD><TD>INSTRUCCION = falta poner accicon;</TD></TR>"

    def ejecutar(self):
        pass