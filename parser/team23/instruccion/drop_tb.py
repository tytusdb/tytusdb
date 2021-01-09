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
                add_text("M-00000 successful completion: The table with the following ID -> " + self.id + " -> has been removed from the database: " + actual_db + "\n")
            elif (drop_aux == 1):
                errores.append(nodo_error(self.line, self.column, 'E-22005 error_in_assignment: Cannot delete the table ' + self.id, 'Semántico'))
                add_text('E-22005 error_in_assignment: Cannot delete the table ' + self.id +'\n')
            elif (drop_aux == 2):
                errores.append(nodo_error(self.line, self.column, 'E-22005 error in assignment: the database with the following ID does not exist -> ' + actual_db, 'Semántico'))
                add_text('E-22005 error in assignment: the database with the following ID does not exist -> ' + actual_db + '\n')
            elif (drop_aux == 3):
                errores.append(nodo_error(self.line, self.column, 'E-42P01 undefined table: The table with the following ID does not exist ->  ' + self.id, 'Semántico'))
                add_text('E-42P01 undefined table: The table with the following ID does not exist -> ' + self.id + '\n')
        except:
            errores.append(nodo_error(self.line, self.column, 'E-22005 error_in_assignment: Drop Table could not be launched', 'Semántico'))
            add_text('E-22005 error_in_assignment: Drop Table could not be launched ' + self.id + '\n')