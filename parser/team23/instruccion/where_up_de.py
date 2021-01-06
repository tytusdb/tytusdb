from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *
from storage import jsonMode as funciones
from error.errores import *

class where_up_de(instruccion):
    def __init__(self, dato, line, column, num_nodo):
        super().__init__(line, column)
        self.dato = dato

        #Nodo del Where
        self.nodo = nodo_AST('WHERE', num_nodo)
        self.nodo.hijos.append(nodo_AST('WHERE', num_nodo + 1))
        self.nodo.hijos.append(dato.nodo)

        # Gramatica
        self.grammar_ = "<TR><TD>WHERE ::= WHERE expression </TD><TD>WHERE = new where_up_de(expression); </TD></TR>"

    def ejecutar(self, list_tb):
        return self.dato.ejecutar(list_tb)