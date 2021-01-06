from abstract.instruccion import *
from tools.tabla_tipos import *
from error.errores import *
from tools.console_text import *
from instruccion.P_Key import *
from instruccion.F_Key import *
from instruccion.unique_simple import *
from instruccion.condicion_simple import *
from storage import jsonMode as funciones

class alter_add_col(instruccion):
    def __init__(self, id_col, type_col, condiciones, line, column, num_nodo):
        super().__init__(line, column)
        self.id_col = id_col
        self.type_col = type_col
        self.condiciones = condiciones

        #Nodo AST Alter Add Column
        self.nodo = nodo_AST('ADD COLUMN', num_nodo)
        self.nodo.hijos.append(nodo_AST('ADD COLUMN', num_nodo + 1))
        self.nodo.hijos.append(nodo_AST(id_col, num_nodo + 2))
        self.nodo.hijos.append(nodo_AST(self.get_str_tipo(type_col), num_nodo + 3))
        if condiciones != None:
        #    for condicion in condiciones:
            self.nodo.hijos.append(condiciones.nodo)

        #Gramatica
        self.grammar_ = '<TR><TD> ALTER_OP ::= ADD COLUMN ' + id_col + ' TYPE_COLUMN CONDITION_COLUMN </TD><TD> ALTER_OP = new alter_add_col(' + id_col + ', TYPE_COLUMN, CONDITION_COLUMN); </TD></TR>\n'

    def ejecutar(self, id_tb):
        id_db = get_actual_use()

        #Validar si existe columna con dicho nombre
        if ts.existe_col(id_db, id_tb, self.id_col) == True:
            errores.append(nodo_error(self.line, self.column, 'ERROR - Ya existe una columna llamada ' + self.id_col, 'Semántico'))
            add_text('ERROR - Ya existe una columna llamada ' + self.id_col + '\n')
            return 

        #Validar condición para ver que insertar en los registros de la columna
        val_insert = 'NULL'

        registros = funciones.extractTable(id_db, id_tb)
        if len(registros) > 0:
            if isinstance(self.condiciones, P_Key):
                errores.append(nodo_error(self.line, self.column, 'ERROR - No puedes agregar una llave primaria en una tabla con registros', 'Semántico'))
                add_text('ERROR - No puedes agregar una llave primaria en una tabla con registros\n')
                return
                
            if isinstance(self.condiciones, F_key):
                errores.append(nodo_error(self.line, self.column, 'ERROR - No puedes agregar una foranea primaria en una tabla con registros', 'Semántico'))
                add_text('ERROR - No puedes agregar una llave foranea en una tabla con registros\n')
                return

            if isinstance(self.condiciones, condicion_simple):
                if self.condiciones.comando.lower() == 'default':
                    val_insert == self.condiciones.expresion.ejecutar([])
                else:
                    errores.append(nodo_error(self.line, self.column, 'ERROR - No puedes agregar una columna con restricción not null en una tabla con registros', 'Semántico'))
                    add_text('ERROR - No puedes agregar una columna con restricción not null en una tabla con registros\n')
                    return

        add_col_return = funciones.alterAddColumn(id_db, id_tb, val_insert)
        # Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente.

        if add_col_return == 0:
            size = 0
            tipo = self.type_col
            if isinstance(self.type_col, tuple):
                size = self.type_col[1]
                tipo = self.type_col[0]

            list_condiciones = None
            if self.condiciones != None:
                list_condiciones = [self.condiciones]

            nodo_col = symbol_col(self.id_col, size, tipo, list_condiciones)
            ts.add_col(id_db, id_tb, nodo_col)

             #Agregar restricciones
            if list_condiciones != None:
                count_restricciones = 0
                for restriccion in list_condiciones:
                    if isinstance(restriccion, P_Key):
                        if len(restriccion.dato) == 0:
                            restriccion.dato.append(self.id_col)

                        restriccion.ejecutar(id_tb)
                        
                    if isinstance(restriccion, F_key):
                        if len(restriccion.dato1) == 0:
                            restriccion.dato1.append(self.id_col)

                        restriccion.ejecutar(id_tb)

                    if isinstance(restriccion, unique_simple):
                        if len(restriccion.dato) == 0:
                            restriccion.dato.append(self.id_col)

                    count_restricciones += 1

            add_text('Columna ' + self.id_col + ' agregada.\n')
        elif add_col_return == 1:
            errores.append(nodo_error(self.line, self.column, 'ERROR - No se puede agregar la columna', 'Semántico'))
            add_text('ERROR - No se puede agregar la columna\n')
        elif add_col_return == 2:
            errores.append(nodo_error(self.line, self.column, 'ERROR - No se encuentra la base de datos', 'Semántico'))
            add_text('ERROR - No se encuentra la base de datos\n')
        elif add_col_return == 3:
            errores.append(nodo_error(self.line, self.column, 'ERROR - No existe la tabla: ' + id_tb, 'Semántico'))
            add_text('ERROR - No existe la tabla: ' + id_tb + '\n')
    
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
