from abstract.instruccion import *
from tools.tabla_tipos import *

class rename_owner_db(instruccion):
    def __init__(self, comando, dato, line, column, num_nodo):

        super().__init__(line, column)
        self.dato = dato
        self.comando = comando

        #Nodo AST Rename Owner
        if(comando.lower()=='rename'):
            self.nodo = nodo_AST('RENAME', num_nodo)
            self.nodo.hijos.append(nodo_AST('RENAME TO', num_nodo+1))
            self.nodo.hijos.append(nodo_AST(dato, num_nodo + 2))
        else:
            self.nodo = nodo_AST('OWNER', num_nodo)
            self.nodo.hijos.append(nodo_AST('OWNER TO', num_nodo + 1))
            self.nodo.hijos.append(nodo_AST('\{', num_nodo + 2))
            self.nodo.hijos.append(nodo_AST(dato, num_nodo + 3))
            self.nodo.hijos.append(nodo_AST('\}', num_nodo + 4))

        #Gramatica 
        self.grammar_ = '<TR><TD> OWNER_RENAME ::= RENAME TO ' + dato + ' </TD><TD> OWNER_RENAME = new rename_owner_db(RENAME, ' + dato +'); </TD></TR> '
        self.grammar_ += '<TR><TD> OWNER_RENAME ::= OWNER TO { ' + dato + ' } </TD><TD> OWNER_RENAME = new rename_owner_db(OWNER, ' + dato + '); </TD></TR> '

    def ejecutar(self):
        pass