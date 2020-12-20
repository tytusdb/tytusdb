from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *
from storage import jsonMode as funciones
from error.errores import *
from tools.tabla_simbolos import *

class drop_tb(instruccion):

    def __init__(self,id,line,column,num_nodo):
        super().__init__(line,column)
        self.id = id

        #Nodo DROP TABLE
        self.nodo = nodo_AST('DROP TABLE', num_nodo)
        self.nodo.hijos.append(nodo_AST('DROP', num_nodo + 1))
        self.nodo.hijos.append(nodo_AST('TABLE', num_nodo + 2))
        self.nodo.hijos.append(nodo_AST(id, num_nodo + 3))

        # Gramatica
        self.grammar_ = "<TR><TD>INSTRUCCION ::= DROP TABLE " + id + "; </TD><TD>INSTRUCCION = new drop_tb(" + id + ");</TD></TR>"

    def ejecutar(self):
        try:
            actual_db = get_actual_use()
            drop_aux = funciones.dropTable(actual_db, self.id)
            # Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente.

            if(drop_aux == 0):
                ts.delete_tb(actual_db, self.id)
                add_text("Tabla - " + self.id + " - a sido eliminada de la base de datos: " + actual_db + "\n")
            elif (drop_aux == 1):
                errores.append(nodo_error(self.line, self.column, 'ERROR - No se puede eliminar table ' + self.id, 'Semántico'))
                add_text('ERROR - No se puede eliminar table ' + self.id +'\n')
            elif (drop_aux == 2):
                errores.append(nodo_error(self.line, self.column, 'ERROR - No existe la base de datos: ' + actual_db, 'Semántico'))
                add_text('ERROR - No existe la base de datos: ' + actual_db + '\n')
            elif (drop_aux == 3):
                errores.append(nodo_error(self.line, self.column, 'ERROR - No existe la tabla: ' + self.id, 'Semántico'))
                add_text('ERROR - No existe la tabla: ' + self.id + '\n')
        except:
            errores.append(nodo_error(self.line, self.column, 'ERROR - No se pudo ejecutar Drop Table', 'Semántico'))
            add_text('ERROR - No se pudo ejecutar Drop Table ' + self.id + '\n')