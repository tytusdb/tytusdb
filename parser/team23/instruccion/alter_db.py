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
        self.grammar_ = '<TR><TD> INSTRUCCION ::= ALTER DATABASE ' + id_db + ' OWNER_RENAME </TD><TD> INSTRUCCION = new alter_db(' + self.id_db + ', OWNER_RENAME); </TD></TR>\n'
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
                    add_text("Base de datos se ha alterado: ID Anterior: " + self.id_db + " ID Nuevo: " + self.owner.dato + "\n")
                elif(alterar == 1):
                    errores.append(nodo_error(self.line, self.column, 'Error en alter database', 'Semántico'))
                    add_text("ERROR - Base de datos no pudo ser alterada.\n")
                elif(alterar == 2):
                    errores.append(nodo_error(self.line, self.column, 'Base de datos con id ' + self.id_db + ' no existe.', 'Semántico'))
                    add_text("ERROR - La base de datos " + self.id_db + " no existe.\n")
                elif(alterar == 3):
                    errores.append(nodo_error(self.line, self.column, 'Ya existe una base de datos con el id ' + self.owner.dato, 'Semántico'))
                    add_text("ERROR - Ya existe una base de datos con el id " + self.owner.dato + "\n")
                else:
                    errores.append(nodo_error(self.line, self.column, 'Error al alterar database', 'Semántico'))
                    add_text("Base de datos no puedo ser alterada.\n")
            else:
                add_text("No se ha implementado ALTER OWNER")
        except:
            errores.append(nodo_error(self.line, self.column, 'Error al realizar cambios en la base de datos', 'Semántico'))
            add_text("ERROR - Base de datos no pudo ser alterada.\n")