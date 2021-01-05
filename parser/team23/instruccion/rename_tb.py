from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *
from storage import jsonMode as funciones
from error.errores import *
from tools.tabla_simbolos import *

class rename_tb(instruccion):
    def __init__(self, new_id, line, column, num_nodo):
        super().__init__(line, column)
        self.new_id = new_id
        
        #Nodo AST rename_tb
        self.nodo = nodo_AST('RENAME TO', num_nodo)
        self.nodo.hijos.append(nodo_AST('RENAME TO', num_nodo+1))
        self.nodo.hijos.append(nodo_AST(new_id, num_nodo+2))

        #Gramatica
        self.grammar_ = '<TR><TD> ALTER_OP ::= RENAME TO ' + new_id + ' </TD><TD> ALTER_OP = new rename_tb(' + new_id + '); </TD></TR>\n'

    def ejecutar(self, id_tb):
        try:
            id_db = get_actual_use()
            rename_table = funciones.alterTable(id_db, id_tb, self.new_id)
            # Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 tableOld no existente, 4 tableNew existente.

            if rename_table == 0:
                ts.update_tb(id_db, id_tb, self.new_id)
                add_text('Se ha renombrado la tabla correctamente, nuevo id: ' + self.new_id + ' id anterior: ' + id_tb + '\n')
            elif rename_table == 1:
                errores.append(nodo_error(self.line, self.column, 'ERROR - No se pudo cambiar el nombre de la tabla', 'Semántico'))
                add_text('ERROR - No se pudo cambiar el nombre de la tabla\n')
            elif rename_table == 2:
                errores.append(nodo_error(self.line, self.column, 'ERROR - No se encontro la base de datos: ' + id_db, 'Semántico'))
                add_text('ERROR - No se encontro la base de datos: ' + id_db + '\n')
            elif rename_table == 3:
                errores.append(nodo_error(self.line, self.column, 'ERROR - No existe la tabla ' + id_tb + ' para cambiar nombre.', 'Semántico'))
                add_text('ERROR - No existe la tabla ' + id_tb + ' para cambiar nombre.\n')
            elif rename_table == 4:
                errores.append(nodo_error(self.line, self.column, 'ERROR - Ya existe una tabla llamada ' + self.new_id, 'Semántico'))
                add_text('ERROR - Ya existe una tabla llamada ' + self.new_id + '\n')
        except:
            errores.append(nodo_error(self.line, self.column, 'ERROR - No se puede renombrar la tabla' + id_tb, 'Semántico'))
            add_text('ERROR - No se puede renombrar la tabla ' + id_tb + '\n')
            