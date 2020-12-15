from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *

class create_table(instruccion):
    def __init__(self, id_table, columnas, line, column, num_nodo):
        super().__init__(line, column)
        self.id_table = id_table
        self.columnas = columnas

        #Nodo AST Create Table
        self.nodo = nodo_AST('CREATE TABLE', num_nodo)
        self.nodo.hijos.append(nodo_AST('CREATE TABLE', num_nodo+1))
        self.nodo.hijos.append(nodo_AST(id_table, num_nodo+2))
        self.nodo.hijos.append(nodo_AST('(', num_nodo+3))
        for columna in columnas:
            self.nodo.hijos.append(columna.nodo)
        self.nodo.hijos.append(nodo_AST(')', num_nodo+4)) 
    
    def ejecutar(self):
        pass