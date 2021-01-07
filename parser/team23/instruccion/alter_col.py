from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *
from error.errores import *
from tools.tabla_simbolos import *
from instruccion.condicion_simple import *

class alter_col(instruccion):
    def __init__(self, comando, ID, line, column, num_nodo):

        super().__init__(line, column)
        self.comando = comando
        self.ID = ID

        #Nodo opcion alter
        if comando.lower() == 'not':
            self.nodo = nodo_AST('alter_col_op', num_nodo)
            self.nodo.hijos.append(nodo_AST('SET', num_nodo+1))
            self.nodo.hijos.append(nodo_AST('NOT', num_nodo + 2))
            self.nodo.hijos.append(nodo_AST('NULL', num_nodo + 3))
        elif comando.lower() == 'default':
            self.nodo = nodo_AST('alter_col_op', num_nodo)
            self.nodo.hijos.append(nodo_AST('SET', num_nodo+1))
            self.nodo.hijos.append(nodo_AST('DEFAULT', num_nodo + 2))
            self.nodo.hijos.append(ID.nodo)
        elif comando.lower() == 'type':
            self.nodo = nodo_AST('alter_col_op', num_nodo)
            self.nodo.hijos.append(nodo_AST('TYPE', num_nodo + 1))
            self.nodo.hijos.append(nodo_AST(ID, num_nodo + 2))

        #Gramatica
        self.grammar_ = '<TR><TD> ALTER_OP ::= '
        if comando.lower() == 'not':
            self.grammar_ += 'SET NOT NULL </TD><TD> ALTER_OP = new alter_col(NOT, None); </TD></TR>\n'
        elif comando.lower() == 'default':
            self.grammar_ += 'SET DEFAULT EXPRESSION </TD><TD> ALTER_OP = new alter_col(DEFAULT, EXPRESSION); </TD></TR>\n'
            self.grammar_ += ID.grammar_
        elif comando.lower() == 'type':
            self.grammar_ += 'TYPE TYPE_COLUMN </TD><TD> ALTER_OP = new alter_col(TYPE, TYPE_COLUMN); </TD></TR>\n'

    def ejecutar(self, tb_id, id_col):
        id_db = get_actual_use()

        if self.comando.lower() == 'not':
            nodo_simbolo = ts.get_col(id_db, tb_id, id_col)
            nodo_simbolo.condiciones.append(condicion_simple(self.comando, self.ID, self.line, self.column, self.num_nodo+10000000))
            ts.update_col(id_db, tb_id, id_col, nodo_simbolo)

            add_text('Se agrego la condición NOT NULL\n')
        elif self.comando.lower() == 'default':
            nodo_simbolo = ts.get_col(id_db, tb_id, id_col)
            nodo_simbolo.condiciones.append(condicion_simple(self.comando, self.ID, self.line, self.column, self.num_nodo+10000000))
            ts.update_col(id_db, tb_id, id_col, nodo_simbolo)

            add_text('Se agrego la condición DEFAULT\n')
        elif self.comando.lower() == 'type':
            size = 0
            tipo = self.ID
            if isinstance(self.ID, tuple):
                size = self.ID[1]
                tipo = self.ID[0]

            nodo_simbolo = ts.get_col(id_db, tb_id, id_col)
            tipo_dominante = tipos_tabla[tipo.value][nodo_simbolo.tipo.value]

            if tipo_dominante != tipo:
                errores.append(nodo_error(self.line, self.column, 'ERROR - No puedes cambiar tipo de dato: ' + self.get_str_tipo(nodo_simbolo.tipo) + ' por: ' + self.get_str_tipo(tipo), 'Semántico'))
                add_text('ERROR - No puedes cambiar tipo de dato: ' + self.get_str_tipo(nodo_simbolo.tipo) + ' por: ' + self.get_str_tipo(tipo) + '\n')
                return

            nodo_simbolo.size = size
            nodo_simbolo.tipo = tipo
            ts.update_col(id_db, tb_id, id_col, nodo_simbolo)

            add_text('Se cambió el tipo de dato de la columna ' + id_col + '\n')

    def get_str_tipo(self, tipo):
        if tipo == tipo_primitivo.SMALLINT:
            return "SMALLINT"
        elif tipo == tipo_primitivo.INTEGER:
            return "INTEGER"
        elif tipo == tipo_primitivo.BIGINT:
            return "BIGINT"
        elif tipo == tipo_primitivo.DECIMAL:
            return "DECIMAL"
        elif tipo == tipo_primitivo.REAL:
            return "REAL"
        elif tipo == tipo_primitivo.DOUBLE_PRECISION:
            return "DOUBLE PRECISION"
        elif tipo == tipo_primitivo.MONEY:
            return "MONEY"
        elif tipo == tipo_primitivo.VARCHAR:
            return "VARCHAR"
        elif tipo == tipo_primitivo.CHAR:
            return "CHAR"
        elif tipo == tipo_primitivo.TEXT:
            return "TEXT"
        elif tipo == tipo_primitivo.TIMESTAMP:
            return "TIMESTAMP"
        elif tipo == tipo_primitivo.DATE:
            return "DATE"
        elif tipo == tipo_primitivo.TIME:
            return "TIME"
        elif tipo == tipo_primitivo.INTERVAL:
            return "INTERVAL"
        elif tipo == tipo_primitivo.BOOLEAN:
            return "BOOLEAN"

