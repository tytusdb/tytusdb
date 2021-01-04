from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.tabla_simbolos import *
from error.errores import *
from storage import jsonMode as funciones
from tools.console_text import *

class unique_simple(instruccion):
    def __init__(self, constraint, dato, line, column, num_nodo):
        super().__init__(line,column)
        self.constraint = constraint
        self.dato = dato

        self.nodo = nodo_AST('condition_column',num_nodo)
        if constraint != None:
            self.nodo.hijos.append(constraint.nodo)
        self.nodo.hijos.append(nodo_AST('UNIQUE',num_nodo+1))
        if len(dato) > 0:
            self.nodo.hijos.append(nodo_AST('(', num_nodo + 2))
            count_dato = 4
            for aux in dato:
                self.nodo.hijos.append(nodo_AST(aux, count_dato + num_nodo))
                count_dato += 1
            self.nodo.hijos.append(nodo_AST(')', num_nodo + 3))

        self.grammar_ = '<TR><TD> CONDICION ::= constraint UNIQUE op_unique </TD><TD> CONDICION = new unique_simple(constraint, op_unique); </TD></TR>'

    def ejecutar(self, tb_id, dato, pos_col):
        try:
            id_db = get_actual_use()

            #Extraer registros en dicha columna
            tabla = funciones.extractTable(id_db, tb_id)

            #Validar si existe un registro igual
            for registro in tabla:
                if dato == registro[pos_col]:
                    return nodo_error(self.line, self.column, 'ERROR - Restricción UNIQUE violada, no se puede insertar duplicado: ' + str(dato), 'Semántico')
            
            return None
        except:
            return nodo_error(self.line, self.column, 'E-22005 error in assignment: Unable to validate UNIQUE constraint', 'Semántico')

    def cargar_unique(self, tb_id):
        try:
            id_db = get_actual_use()

            for col in self.dato:
                columna = ts.get_col(id_db, tb_id, col)
                columna.condiciones = [] 
                columna.condiciones.append(unique_simple(self.constraint, col, self.line, self.column, 0))
        except:
            errores.append(nodo_error(self.line, self.column, 'E-22005 error in assignment: Unable to validate UNIQUE constraint', 'Semántico'))
            add_text('E-22005 error in assignment: Unable to validate UNIQUE constraint\n')

