from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *
from storage import jsonMode as funciones
from error.errores import *
from tools.tabla_simbolos import *

class create_db(instruccion):
    def __init__(self, id_db, replace_, if_exists, owner, mode, line, column, num_nodo):
        super().__init__(line, column)
        self.id_db = id_db
        self.replace_ = replace_
        self.if_exists = if_exists
        self.owner = owner
        self.mode = mode

        #Nodo AST Create DB
        self.nodo = nodo_AST('CREATE DATABASE', num_nodo)
        self.nodo.hijos.append(nodo_AST('CREATE DATABASE', num_nodo+1))        
        if replace_ != False:
            self.nodo.hijos.append(nodo_AST('OR REPLACE', num_nodo+3))
        if if_exists != False:
            self.nodo.hijos.append(nodo_AST('IF NOT EXISTS', num_nodo+4))
        self.nodo.hijos.append(nodo_AST(id_db, num_nodo+2))
        if owner != None:
            self.nodo.hijos.append(owner.nodo)
        if mode != None:
            self.nodo.hijos.append(mode.nodo)

        #Gramatica
        self.grammar_ = '<TR><TD>INSTRUCCION ::= CREATE'
        if replace_ != False:
            self.grammar_ += ' OR REPLACE'
        self.grammar_ += ' DATABASE '
        if if_exists != False:
            self.grammar_ += ' IF NOT EXISTS ' 
        self.grammar_ += id_db
        if owner != None:
            self.grammar_ += ' OWNER '
        if mode != None:
            self.grammar_ += ' MODE '
        self.grammar_ += '</TD><TD>INSTRUCCION = new create_db(ID,  REPLACE, IF_EXISTS, OWNER, MODE);</TD></TR>'

        if owner != None:
            self.grammar_ += '<TR><TD> OWNER ::= OWNER </TD><TD> OWNER = True; </TD></TR>'
        if mode != None:
            self.grammar_ += '<TR><TD> MODE ::= MODE </TD><TD> MODE = True; </TD></TR>'

    def ejecutar(self):
        try:       
            crear = funciones.createDatabase(self.id_db)
            # Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 base de datos existente

            if(crear == 0): # Exitoso
                new_db = symbol_db(self.id_db)  # Nuevo nodo de Base de datos
                ts.add_db(new_db)   # Agregar Base de datos a la tabla de simbolos
                add_text("M-00000	successful completion: Database created successfully with name - " + self.id_db + " -\n")
            elif(crear == 1): # Error en operacion
                errores.append(nodo_error(self.line, self.column, 'E-22005 error in assignment: Database could not be created', 'Semántico'))
                add_text("E-22005 error in assignment: Database could not be created.\n")
            elif(crear == 2): # Base ya existe
                if self.if_exists == False:
                    if self.replace_ == True:   # Remplazar
                        delete = funciones.dropDatabase(self.id_db)
                        replace_db = funciones.createDatabase(self.id_db)

                        if(replace_db == 0):
                            new_db = symbol_db(self.id_db)  # Nuevo nodo de Base de datos
                            ts.update_db(self.id_db, new_db)   # Agregar Base de datos a la tabla de simbolos
                            add_text("M-00000	successful completion: Database successfully replaced with name - " + self.id_db + " -\n")
                        elif(replace_db == 2):
                            add_text("E-42P04 duplicate database: Database already exists - " + self.id_db + " - \n")
                        else:
                            errores.append(nodo_error(self.line, self.column, 'E-22005 error in assignment: Database could not be replaced.', 'Semántico'))
                            add_text("E-22005 error in assignment: Database could not be replaced.\n")
                    else:
                        add_text("E-42P04 duplicate database: Database already exists - " + self.id_db + " - \n")
                else:
                    add_text("E-42P04 duplicate database: Database already exists  - " + self.id_db + " - \n")
            else:
                errores.append(nodo_error(self.line, self.column, 'E-22005 error in assignment: Database could not be created', 'Semántico'))
                add_text("E-22005 error in assignment: Database could not be created.\n")

        except:
            errores.append(nodo_error(self.line, self.column, 'E-22005 error in assignment: Database could not be created', 'Semántico'))
            add_text("E-22005 error in assignment: Database could not be created.\n")