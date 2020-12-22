from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.tabla_simbolos import *
from error.errores import *
from storage import jsonMode as funciones
from tools.console_text import *

class P_Key(instruccion):
    def __init__(self, dato, constraint, line, column, num_nodo):
        super().__init__(line, column)
        self.dato = dato
        self.constraint = constraint

        #Nodo Primary key
        if constraint != None:
            self.nodo.hijos.append(constrain.nodo)
        self.nodo = nodo_AST('PRIMARY KEY', num_nodo)
        self.nodo.hijos.append(nodo_AST('PRIMARY KEY', num_nodo + 1))
        if len(dato) > 0:
            self.nodo.hijos.append(nodo_AST('(', num_nodo + 2))
            count_ids = 4
            for aux in dato:
                self.nodo.hijos.append(nodo_AST(aux, num_nodo + count_ids))
                count_ids += 1
            self.nodo.hijos.append(nodo_AST(')', num_nodo + 3))

        #Gramatica
        self.grammar_ = '<TR><TD> CONDICIONES ::= CONSTRAINT PRIMARY KEY '
        if len(dato) > 0:
            self.grammar_ += '('
            for aux in dato:
                self.grammar_ += aux
            self.grammar_ += ')'
        self.grammar_ += '</TD><TD> CONDICIONES ::= new P_Key(ID, CONSTRAINT); </TD></TR>\n'

        if constraint != None:
            self.grammar_ += '<TR><TD> CONSTRAINT ::= CONSTRAINT ID </TD><TD> CONSTRAINT = new constraint(ID); </TD></TR>\n'
        else:
            self.grammar_ += '<TR><TD> CONSTRAINT ::= EPSILON </TD><TD> CONSTRAINT = None; </TD></TR>\n'

    def ejecutar(self, id_tb):
        try:
            id_db = get_actual_use()

            list_cols = []
            for id_col in self.dato:
                pos_col = ts.get_pos_col(id_db, id_tb, id_col)
                list_cols.append(pos_col)

            add_pk = funciones.alterAddPK(id_db, id_tb, list_cols)
            # Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave primaria existente, 5 columnas fuera de límites.

            if add_pk == 0:
                pass
            elif add_pk == 1:
                errores.append(nodo_error(self.line, self.column, 'ERROR - No se pudo asignar como llave primaria: ' + self.dato, 'Semántico'))
                add_text('ERROR - No se pudo asignar como llave primaria: ' + self.dato + '\n')
            elif add_pk == 2:
                errores.append(nodo_error(self.line, self.column, 'ERROR - No existe la base de datos: ' + id_db, 'Semántico'))
                add_text('ERROR - No existe la base de datos: ' + id_db + '\n')
            elif add_pk == 3:
                errores.append(nodo_error(self.line, self.column, 'ERROR - No existe la tabla: ' + id_tb, 'Semántico'))
                add_text('ERROR - No existe la tabla: ' + id_tb + '\n')
            elif add_pk == 4:
                errores.append(nodo_error(self.line, self.column, 'ERROR - Ya existe una llave primaria', 'Semántico'))
                add_text('ERROR - Ya existe una llave primaria\n')
            elif add_pk == 5:
                errores.append(nodo_error(self.line, self.column, 'ERROR - Limite de columnas para llave primaria excedido.', 'Semántico'))
                add_text('ERROR - Limite de columnas para llave primaria excedido.\n')
                
        except:
            errores.append(nodo_error(self.line, self.column, 'ERROR - No se pudo restringir llave primaria en tabla: ' + id_tb, 'Semántico'))
            add_text('ERROR - No se pudo restringir llave primaria en tabla: ' + id_tb + '\n')