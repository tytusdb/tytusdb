from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.tabla_simbolos import *

class alias_item(instruccion):
    def __init__(self, alias, id_, line, column, num_nodo):
        self.alias
        self.id

        #Nodo AST Alias
        self.nodo = nodo_AST('ALIAS', num_nodo)
        self.nodo.hijos.append(nodo_AST(alias, num_nodo + 1))
        self.nodo.hijos.append(nodo_AST('AS', num_nodo + 2))
        self.nodo.hijos.append(nodo_AST(id_, num_nodo + 3))

        #Gramatica
        self.grammar_ = '<TR><TD> EXPRESSION ::= ID AS ID </TD><TD> EXPRESSION = new alias_item(' + alias + ',' + id_ + '); </TD></TR>\n'

    def ejecutar(self, list_id):
        ts.add_alias(self.alias, self.id_)