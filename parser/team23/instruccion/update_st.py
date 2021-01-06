from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *
from storage import jsonMode as funciones
from error.errores import *
from tools.tabla_simbolos import *

class update_st (instruccion):

    def __init__(self, id1, id2, dato, where, line, column, num_nodo):

        super().__init__(line, column)
        self.id1 = id1
        self.id2 = id2
        self.dato = dato
        self.where = where

        #Nodo AST UPDATE

        self.nodo = nodo_AST('UPDATE', num_nodo)
        self.nodo.hijos.append(nodo_AST('UPDATE', num_nodo + 1))
        self.nodo.hijos.append(nodo_AST(id1, num_nodo + 2))
        self.nodo.hijos.append(nodo_AST('SET', num_nodo + 3))
        self.nodo.hijos.append(nodo_AST(id2, num_nodo + 4))
        self.nodo.hijos.append(nodo_AST('=', num_nodo + 5))
        self.nodo.hijos.append(nodo_AST(dato, num_nodo + 6))

        if where != None:
            self.nodo.hijos.append(where.nodo)

        # Gramatica
        self.grammar_ = "<TR><TD>INSTRUCCION ::= UPDATE ID SET ID = op_val where; </TD><TD>INSTRUCCION = falta poner accicon;</TD></TR>"
        if where != None:
            self.grammar_ += where.grammar_

    def ejecutar(self):
        id_db = get_actual_use()

        if self.where != None:
            list_id = [self.id1]
            val_return = self.where.ejecutar(list_id)
            dato_val = self.dato.ejecutar(list_id)

            index_col = ts.get_pos_col(id_db, self.id1, self.id2)
            index_pk = ts.get_index_pk(id_db, self.id1)

            for item in val_return.valor:                

                dict_registro = {}

                count_col = 0
                for col in item:
                    if count_col == index_col:
                        dict_registro[count_col] = dato_val.valor
                    else:
                        dict_registro[count_col] = col
                    count_col += 1

                list_pk = []
                for id_pk in index_pk:
                    list_pk.append(item[id_pk])

                resultado = funciones.update(id_db, self.id1, dict_registro, list_pk)                
                # Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave primaria no existe.

                if resultado == 1:
                    errores.append(nodo_error(self.line, self.column, 'ERROR - No se pudo realizar el update', 'Semántico'))
                    add_text('ERROR - No se pudo realizar el update\n')
                elif resultado == 2:
                    errores.append(nodo_error(self.line, self.column, 'ERROR - No se encontró la base de datos', 'Semántico'))
                    add_text('ERROR - No se encontró la base de datos\n')
                elif resultado == 3:
                    errores.append(nodo_error(self.line, self.column, 'ERROR - No se encontro la tabla ' + self.id1, 'Semántico'))
                    add_text('ERROR - No se encontro la tabla ' + self.id1 + '\n')
                elif resultado == 4:
                    errores.append(nodo_error(self.line, self.column, 'ERROR - No existe la llave primaria', 'Semántico'))
                    add_text('ERROR - No existe la llave primaria\n')

            add_text('Se actualizadon los registros\n')
        else:   
            pass