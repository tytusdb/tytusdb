from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *
from storage import jsonMode as funciones
from error.errores import * 
from tools.tabla_simbolos import *

class alter_db(instruccion):
    def __init__(self, id_db, new_id, owner, line, column, num_nodo):
        super().__init__(line, column)
        self.id_db = id_db
        self.new_id = new_id
        self.owner = owner

        #Nodo AST Alter DB
        self.nodo = nodo_AST('ALTER DATABASE', num_nodo)
        self.nodo.hijos.append(nodo_AST('ALTER DATABASE', num_nodo + 1))
        self.nodo.hijos.append(nodo_AST(id_db, num_nodo + 2))
        if owner == True:
            self.nodo.hijos.append(nodo_AST('OWNER TO', num_nodo+3))
        else:   
            self.nodo.hijos.append(nodo_AST('RENAME TO', num_nodo+4))
        self.nodo.hijos.append(nodo_AST(new_id, num_nodo+5))

        #Gramatica
        self.grammar_ = '<TR><TD> INSTRUCCION ::= ALTER DATABASE ' + id_db
        if owner != True:
            self.grammar_ += ' RENAME TO '
        else:
            self.grammar_ += ' OWNER TO '
        self.grammar_ += new_id + ' </TD><TD> INSTRUCCION = new alter_db(' + self.id_db + ',' + self.new_id
        if owner != True:
            self.grammar_ +=  ', False); </TD></TR>'
        else:
            self.grammar_ +=  ', True); </TD></TR>'

    def ejecutar(self):
        try:
            if owner != True:
                alterar = funciones.alterDatabase(self.id_db, self.new_id)
                # Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 databaseOld no existente, 3 databaseNew existente.

                if(alterar == 0):
                    new_db = ts.get_db(self.id_db)
                    new_db.id_ = self.new_id
                    ts.update_db(self.id_db, new_db)
                    add_text("Base de datos se ha alterado: ID Anterior: " + self.id_db + " ID Nuevo: " + self.new_id + "\n")
                elif(alterar == 1):
                    errores.append(nodo_error(self.line, self.column, 'Error en alter database', 'Semántico'))
                    add_text("ERROR - Base de datos no pudo ser alterada.\n")
                elif(alterar == 2):
                    errores.append(self.line, self.column, 'Base de datos con id ' + self.id_db + ' no existe.', 'Semántico')
                    add_text("ERROR - La base de datos " + self.id_db + " no existe.\n")
                elif(alterar == 3):
                    errores.append(self.line, self.column, 'Ya existe una base de datos con el id ' + self.new_id, 'Semántico')
                    add_text("ERROR - Ya existe una base de datos con el id " + self.new_id + "\n")
                else:
                    errores.append(nodo_error(self.line, self.column, 'Error al alterar database', 'Semántico'))
                    add_text("Base de datos no puedo ser alterada.\n")
            else:
                add_text("No se ha implementado ALTER OWNER")

        except:
            errores.append(nodo_error(self.line, self.column, 'Error al realizar cambios en la base de datos', 'Semántico'))
            add_text("ERROR - Base de datos no pudo ser alterada.\n")