from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *

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
        if replace_ != None:
            self.nodo.hijos.append(nodo_AST('OR REPLACE', num_nodo+3))
        if if_exists != None:
            self.nodo.hijos.append(nodo_AST('IF NOT EXISTS', num_nodo+4))
        self.nodo.hijos.append(nodo_AST(id_db, num_nodo+2))
        if owner != None:
            self.nodo.hijos.append(owner.nodo)
        if mode != None:
            self.nodo.hijos.append(mode.nodo)
    
    def ejecutar(self):
        pass