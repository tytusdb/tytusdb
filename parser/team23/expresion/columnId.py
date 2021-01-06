from abstract.expresion import * 
from tools.tabla_tipos import *
from abstract.retorno import *
from storage import jsonMode as funciones
from tools.console_text import *
from tools.tabla_simbolos import *

class columnId(expresion):
    def __init__(self, table, columna, line, column, num_nodo):
        super().__init__(line, column)
        self.table = table
        self.column = columna

        #Nodo AST 
        self.nodo = nodo_AST('ID', num_nodo)
        self.nodo.hijos.append(nodo_AST(str(table), num_nodo+1))
        self.nodo.hijos.append(nodo_AST(str('.'), num_nodo+1))
        self.nodo.hijos.append(nodo_AST(str(column), num_nodo+1))

        #Gramatica
        self.grammar_ = '<TR><TD> ID ::= ' + str(table) +'.' + str(column) +' </TD><TD> ID = new ID(' + str(table) +', ' + str(column) + '); </TD></TR>'

    def ejecutar(self, list_tb):
        #RETORNAR TABLA COMPLETA CON INDICE DE TABLA 
        actualDB = get_actual_use()

        #BUSCAR TABLA CON COLUMNA
        col_item = ts.get_col(actualDB, self.table, self.columna)
        if col_item != None:
            getdata = funciones.extractTable(actualDB,self.table)
            index_col = ts.get_pos_col(actualDB, self.table, self.columna)
            encabezados=ts.field_names(actualDB,self.table)
            return retorno(getdata, col_item.tipo, True, index_col,encabezados=encabezados)
        
        #BUSCAR TABLA CON ALIAS
        alias_tb = ts.get_alias(self.table)
        if alias_tb != None:
            item_col = ts.get_col(actualDB, alias_tb, self.columna)
            getdata = funciones.extractTable(actualDB, alias_tb)
            index_col = ts.get_pos_col(actualDB, alias_tb, self.columna)
            encabezados = ts.field_names(actualDB, alias_tb)
            return retorno(getdata, item_col.tipo, True, index_col, encabezados)

        errores.append(nodo_error(self.line, self.column, 'ERROR - No se puede extraer la data de ' + self.table + '.' + self.columna, 'Semántico'))
        add_text('ERROR - No se puede extraer la data de ' + self.table + '.' + self.columna + '\n')
