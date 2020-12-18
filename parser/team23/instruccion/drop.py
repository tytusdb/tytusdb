from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *
from storage import jsonMode as funciones
from error.errores import *
from tools.tabla_simbolos import *

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
        self.grammar_ = "<TR><TD> INSTRUCCION ::= DROP DATABASE IF_EXISTS " + id + " </TD><TD>INSTRUCCION = new drop(" + id + ", IF_EXISTS); </TD></TR>\n"
        if if_exists != None:
            self.grammar_ += "<TR><TD> IF_EXISTS ::= IF EXISTS </TD><TD> IF_EXISTS =  True; </TD></TR>\n"
        else:
            self.grammar_ += "<TR><TD> IF_EXISTS ::= Epsilon </TD><TD> IF_EXISTS =  None; </TD></TR>\n"

    def ejecutar(self):
        try:
            drop_aux = funciones.dropDatabase(self.id)
            # Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 base de datos no existente.

            if (drop_aux == 2):
                add_text("Base de datos no existe, con nombre "+ self.id + "\n")
            elif (drop_aux == 0):
                ts.delete_db(self.id)
                add_text("Base de datos eliminada, con nombre "+ self.id + "\n")
            else:
                add_text("ERROR - Base de datos no se pudo eliminar, con nombre "+ self.id + "\n")
                errores.append(nodo_error(self.line,self.column,'Error en drop DataBase','Semantico'))
        except:
            errores.append(nodo_error(self.line,self.column,'ERROR - No se pudo ejecutar drop DataBase','Semantico'))
            add_text("ERROR - Base de datos no se pudo eliminar, con nombre "+ self.id + "\n")