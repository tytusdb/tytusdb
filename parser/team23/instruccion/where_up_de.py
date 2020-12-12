from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *
from storage import jsonMode as funciones
from error.errores import *

class where_up_de(instruccion):
    def __init__(self, id, dato, line, column, num_nodo):
        super().__init__(line, column)
        self.id = id
        self.dato = dato


        #Nodo del Where
        self.nodo = nodo_AST('WHERE', num_nodo)
        self.nodo.hijos.append(nodo_AST('WHERE', num_nodo + 1))
        self.nodo.hijos.append(nodo_AST(id, num_nodo + 2))
        self.nodo.hijos.append(nodo_AST('=', num_nodo + 3))
        self.nodo.hijos.append(nodo_AST(dato, num_nodo + 4))

        # Gramatica
        self.grammar_ = "<TR><TD>WHERE ::= WHERE ID IGUAL op_val </TD><TD>WHERE = falta poner accicon;</TD></TR>"

    def ejecutar(self):
        pass