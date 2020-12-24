from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *
from storage import jsonMode as funciones
from error.errores import * 
from tools.tabla_simbolos import *

class alter_db(instruccion):
    def __init__(self, id_db, owner, line, column, num_nodo):
        super().__init__(line, column)
        self.id_db = id_db
        self.owner = owner

        #Nodo AST Alter DB
        self.nodo = nodo_AST('ALTER DATABASE', num_nodo)
        self.nodo.hijos.append(nodo_AST('ALTER DATABASE', num_nodo + 1))
        self.nodo.hijos.append(nodo_AST(id_db, num_nodo + 2))
        self.nodo.hijos.append(owner.nodo)
        self.nodo.hijos.append(nodo_AST(owner.dato, num_nodo+3))

        #Gramatica
        self.grammar_ = '<TR><TD> INSTRUCCION ::= ALTER DATABASE ' + id_db + ' rename_owner </TD><TD> INSTRUCCION = new alter_db(' + self.id_db + ', OWNER_RENAME); </TD></TR>\n'
        self.grammar_ += owner.grammar_

    def ejecutar(self):
        try:
            if self.owner.comando.lower() != 'owner':
                alterar = funciones.alterDatabase(self.id_db, self.owner.dato)
                # Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 databaseOld no existente, 3 databaseNew existente.

                if(alterar == 0):
                    new_db = ts.get_db(self.id_db)
                    new_db.id_ = self.owner.dato
                    ts.update_db(self.id_db, new_db)
                    add_text("M-00000 successful completion: \n The database has been altered: \n Previous ID: " + self.id_db + " New ID: " + self.owner.dato + "\n")
                elif(alterar == 1):
                    errores.append(nodo_error(self.line, self.column, 'E-22005 error in assignment: The Database could not be altered', 'Semántico'))
                    add_text("E-22005 error in assignment: The Database could not be altered.\n")
                elif(alterar == 2):
                    errores.append(nodo_error(self.line, self.column, 'E-42602 invalid name: The database with this ID \"" + self.id_db + "\" does not exist.', 'Semántico'))
                    add_text("E-42602 invalid name: The database with this ID ->" + self.id_db + "<- does not exist.\n")
                elif(alterar == 3):
                    errores.append(nodo_error(self.line, self.column, 'Error 42P04 duplicate_database: A database already exists with the following id ' + self.owner.dato, 'Semántico'))
                    add_text("Error 42P04 duplicate_database: A database already exists with the following id " + self.owner.dato + "\n")
                else:
                    errores.append(nodo_error(self.line, self.column, 'E-22005 error in assignment: The Database could not be altered.', 'Semántico'))
                    add_text("E-22005 error in assignment: The Database could not be altered.\n")
            else:
                add_text("No se ha implementado ALTER OWNER")
        except:
            errores.append(nodo_error(self.line, self.column, 'E-22005 error in assignment: The Database could not be altered.', 'Semántico'))
            add_text("E-22005 error in assignment: The Database could not be altered..\n")