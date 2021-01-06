from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.tabla_simbolos import *
from error.errores import *
from storage import jsonMode as funciones
from tools.console_text import *

class F_key(instruccion):
    def __init__(self, dato1, ID, dato2, constraint, line, column, num_nodo):
        super().__init__(line,column)
        self.dato1 = dato1
        self.dato2 = dato2
        self.ID = ID
        self.constraint = constraint

        #Nodo FOREIGN
        if constraint != None:
            self.nodo.hijos.append(constrain.nodo)
        count_ids = 8
        self.nodo = nodo_AST('FOREIGN KEY', num_nodo)
        self.nodo.hijos.append(nodo_AST('FOREIGN KEY', num_nodo + 1))
        if len(dato1) > 0:
            self.nodo.hijos.append(nodo_AST('(', num_nodo + 2))
            for aux in dato1:
                self.nodo.hijos.append(nodo_AST(aux, num_nodo + count_ids))
                count_ids += 1
            self.nodo.hijos.append(nodo_AST(')', num_nodo + 3))

        self.nodo.hijos.append(nodo_AST('REFERENCES', num_nodo + 4))
        self.nodo.hijos.append(nodo_AST(ID, num_nodo + 5))

        if len(dato2) > 0:
            self.nodo.hijos.append(nodo_AST('(', num_nodo + 6))
            for aux in dato2:
                self.nodo.hijos.append(nodo_AST(aux, num_nodo + count_ids))
                count_ids += 1
            self.nodo.hijos.append(nodo_AST(')', num_nodo + 7))

        #Gramatica
        self.grammar_ = '<TR><TD> CONDICIONES ::= CONSTRAINT FOREIGN KEY '
        if len(dato1) > 0:
            self.grammar_ += '('
            for aux in dato1:
                self.grammar_ += aux + ','
            self.grammar_ += ') '
        self.grammar_ += 'REFERENCES ' + ID
        if len(dato2) > 0:
            self.grammar_ += '('
            for aux in dato2:
                self.grammar_ += aux + ','
            self.grammar_ += ')'
        self.grammar_ += '</TD><TD> CONDICIONES = new F_Key(LISTA_ID, ' + ID + ', LISTA_ID2, CONSTRAINT); </TD></TR>\n'

        if constraint != None:
            self.grammar_ += '<TR><TD> CONSTRAINT ::= CONSTRAINT ID </TD><TD> CONSTRAINT = new constraint(ID); </TD></TR>\n'
        else:
            self.grammar_ += '<TR><TD> CONSTRAINT ::= EPSILON </TD><TD> CONSTRAINT = None; </TD></TR>\n'

    def ejecutar(self, id_tb):
        pass