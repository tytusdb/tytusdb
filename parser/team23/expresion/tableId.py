from abstract.expresion import * 
from tools.tabla_tipos import *
from abstract.retorno import *
from storage import jsonMode as funciones
from tools.console_text import *

class tableId(expresion):
    def __init__(self, valor, line, column, tipo, num_nodo):
        super().__init__(line, column)
        self.valor = valor
        self.tipo = tipo

        #Nodo AST 
        self.nodo = nodo_AST('ID', num_nodo)
        self.nodo.hijos.append(nodo_AST(str(valor), num_nodo+1))

        #Gramatica
        self.grammar_ = '<TR><TD> ID ::= ' + str(valor) +' </TD><TD> ID = new ID(' + str(valor) + '); </TD></TR>'

    def ejecutar(self):
        actualDB = get_actual_use()
        getdata=funciones.extractTable(actualDB,self.valor)
        return retorno(getdata, self.tipo)