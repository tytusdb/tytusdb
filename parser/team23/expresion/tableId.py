from abstract.expresion import * 
from tools.tabla_tipos import *
from tools.tabla_simbolos import *
from abstract.retorno import *
from storage import jsonMode as funciones
from tools.console_text import *
from error.errores import *
from tools.tabla_simbolos import *

class tableId(expresion):
    def __init__(self, valor, line, column, tipo, num_nodo):
        super().__init__(line, column)
        self.valor = valor

        #Nodo AST 
        self.nodo = nodo_AST('ID', num_nodo)
        self.nodo.hijos.append(nodo_AST(str(valor), num_nodo+1))

        #Gramatica
        self.grammar_ = '<TR><TD> ID ::= ' + str(valor) +' </TD><TD> ID = new ID(' + str(valor) + '); </TD></TR>'

    def ejecutar(self, list_tb):
        actualDB = get_actual_use()

        #RETORNAR LA TABLA COMPLETA CON INDICE DE COLUMNA
        for item in list_tb:
            col_item = ts.get_col(actualDB, item, self.valor)

            if col_item != None:
                encabezados=ts.field_names(actualDB,item)
                getdata = funciones.extractTable(actualDB,item)
                index_col = ts.get_pos_col(actualDB, item, self.valor)                
                return retorno(getdata, col_item.tipo, True, index_col,encabezados)

        #BUSCAR LA TABLA POR ALIAS
        alias_tb = ts.get_alias(self.valor)
        if alias_tb != None:
            encabezados = ts.field_names(actualDB, alias_tb)
            getdata = funciones.extractTable(actualDB, alias_tb)
            return retorno(getdata, tipo_primitivo.TABLA, True, encabezados)
            
        
        #RETORNAR LA TABLA COMPLETA SIN INDICE DE COLUMNA
        extract_tb = ts.get_tb(actualDB, self.valor)
        if extract_tb != None:
            encabezados=ts.field_names(actualDB,self.valor)
            getdata = funciones.extractTable(actualDB,self.valor)
            return retorno(getdata, tipo_primitivo.TABLA, True, encabezados)

        errores.append(nodo_error(self.line, self.column, 'ERROR - No se puede extraer la data del id ' + self.valor, 'Semántico'))
        add_text('ERROR - No se puede extraer la data del id ' + self.valor + '\n')
        return retorno(-1, tipo_primitivo.ERROR)