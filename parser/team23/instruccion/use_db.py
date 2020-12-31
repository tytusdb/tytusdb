from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *
from tools.tabla_simbolos import *
from storage import jsonMode as funciones
from error.errores import *

class use_db(instruccion):
    def __init__(self, id_db, line, column, num_nodo):
        super().__init__(line, column)
        self.id_db = id_db

        #Nodo AST Use DB
        self.nodo = nodo_AST('USE ', num_nodo)
        self.nodo.hijos.append(nodo_AST('USE ', num_nodo+1))
        self.nodo.hijos.append(nodo_AST(id_db, num_nodo+2))

        #Gramatica
        self.grammar_ = '<TR><TD> INSTRUCCION ::= USE ' + id_db + '; </TD><TD> INSTRUCCION = new use_db(' + id_db + '); </TD></TR>\n'

    def ejecutar(self):
        try:
            existe_db = ts.get_db(self.id_db)
            update_use_db(self.id_db)            
            add_text('M-00000 successful completion: You are using the following database: ' + self.id_db +'\n')
        except:
            errores.append(nodo_error(self.line, self.column, 'E-42602 invalid name: A database with the following name was not found ' + self.id_db, 'Semántico'))
            add_text('E-42602 invalid name: A database with the following name was not found ' + self.id_db + '\n')