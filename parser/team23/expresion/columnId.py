from abstract.expresion import * 
from tools.tabla_tipos import *
from abstract.retorno import *
from storage import jsonMode as funciones
from tools.console_text import *

class tableId(expresion):
    def __init__(self, table, column, line, column, tipo, num_nodo):
        super().__init__(line, column)
        self.table = table
        self.column = column

        #Nodo AST 
        self.nodo = nodo_AST('ID', num_nodo)
        self.nodo.hijos.append(nodo_AST(str(table), num_nodo+1))
        self.nodo.hijos.append(nodo_AST(str('.'), num_nodo+1))
        self.nodo.hijos.append(nodo_AST(str(column), num_nodo+1))

        #Gramatica
        self.grammar_ = '<TR><TD> ID ::= ' + str(table) +'.' + str(column) +' </TD><TD> ID = new ID(' + str(table) +', ' + str(column) + '); </TD></TR>'

    def ejecutar(self, list_tb):
        actualDB = get_actual_use()
        getdata = funciones.extractTable(actualDB,self.table)

        index_col = ts.get_pos_col(actualDB, self.table, self.column)
        col_item = ts.get_col(actualDB, self.table, self.column)
        encabezados=ts.field_names(actualDB,self.table)
        return retorno(getdata, col_item.tipo, True, col_item,encabezados=encabezados)