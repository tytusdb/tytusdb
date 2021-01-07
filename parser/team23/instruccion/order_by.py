from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *
from abstract.retorno import *

class order_by(instruccion):
    def __init__(self,expresiones, asc_desc, nulls_f_l, line, column, num_nodo):
        super().__init__(line,column)
        self.expresiones = expresiones
        self.asc_desc = asc_desc
        self.nulls_f_l = nulls_f_l

        self.nodo = nodo_AST('ORDER BY',num_nodo)
        self.nodo.hijos.append(nodo_AST('ORDER BY',num_nodo+1))

        self.nodo.hijos.append(nodo_AST(str(expresiones), num_nodo + 2))

        self.nodo.hijos.append(nodo_AST(asc_desc, num_nodo+3))

        if nulls_f_l != None:
            self.nodo.hijos.append(nodo_AST(nulls_f_l,num_nodo+4))
        
        #Gramatica
        self.grammar_ = '<TR><TD> order_by ::= ORDER BY list_id '+ asc_desc +' nulls_f_l </TD><TD> order_by = new order_by(expresiones); </TD></TR>\n'
        self.grammar_ += '<TR><TD> list_id ::=  list_id  </TD><TD> list_id = [] </TD></TR>\n'

    def ejecutar(self):
        return retorno(self.expresiones,self.asc_desc)