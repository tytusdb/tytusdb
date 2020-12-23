from abstract.expresion import * 
from tools.tabla_tipos import *
from tools.tabla_simbolos import *
from abstract.retorno import *
from storage import jsonMode as funciones
from tools.console_text import *
from tools.tabla_simbolos import *

class tableId(expresion):
    def __init__(self, valor, line, column, tipo, num_nodo):
        super().__init__(line, column)
        self.valor = valor
        self.tipo = tipo_primitivo.TABLA

        #Nodo AST 
        self.nodo = nodo_AST('ID', num_nodo)
        self.nodo.hijos.append(nodo_AST(str(valor), num_nodo+1))

        #Gramatica
        self.grammar_ = '<TR><TD> ID ::= ' + str(valor) +' </TD><TD> ID = new ID(' + str(valor) + '); </TD></TR>'

    def ejecutar(self, list_tb):
        actualDB = get_actual_use()
        encabezados = ts.field_names(actualDB, self.valor)

        extract_tb = ts.get_tb(actualDB, self.valor)
        if extract_tb == None:
            for item in list_tb:
                extract_col = ts.existe_col(actualDB, item, self.valor)

                if extract_col == True:
                    getdata = funciones.extractTable(actualDB,item)
                    index_col = ts.get_pos_col(actualDB, item, self.valor)
                    return retorno(getdata, self.tipo, True, index_col)

        getdata = funciones.extractTable(actualDB,self.valor)
        return retorno(getdata, self.tipo, True)