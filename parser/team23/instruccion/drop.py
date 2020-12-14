from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *
from storage import jsonMode as funciones
from error.errores import *
from storage.jsonMode import *

class drop(instruccion):

    def __init__(self,id,if_exists,line,column,num_nodo):

        super().__init__(line,column)
        self.id = id
        self.if_exists = if_exists

        #Nodo DROP
        self.nodo=nodo_AST('DROP',num_nodo)
        self.nodo.hijos.append(nodo_AST('DROP',num_nodo+1))
        self.nodo.hijos.append(nodo_AST('DATABASE', num_nodo + 2))
        if if_exists != None:
            self.nodo.hijos.append(nodo_AST('IF EXISTS', num_nodo + 3))
            self.nodo.hijos.append(nodo_AST(id, num_nodo + 4))
        else:
            self.nodo.hijos.append(nodo_AST(id, num_nodo + 3))

        # Gramatica
        self.grammar_ = "<TR><TD>INSTRUCCION ::= drop_statement; </TD><TD>INSTRUCCION = falta poner accicon;</TD></TR>"


    def ejecutar(self):
        try:
            drop_aux = funciones.dropDatabase(self.id)

            if (drop_aux == 2):
                add_text("Base de datos no existe, con nombre "+ self.id)
            elif (drop_aux == 0):
                add_text("Base de datos eliminada, con nombre "+ self.id)
            else:
                add_text("Base de datos no se pudo eliminar, con nombre "+ self.id)
        except:
            errores.append(nodo_error(self.line,self.column,'Error en drop DataBase','Semantico'))
        pass