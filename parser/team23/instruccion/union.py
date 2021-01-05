from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *
from prettytable import PrettyTable

class union(instruccion):
    def __init__(self,izquierda,derecha, line, column, num_nodo):
        super().__init__(line,column)
        self.izquierda=izquierda
        self.derecha=derecha


        #AST
        self.nodo = nodo_AST('UNION',num_nodo)
        self.nodo.hijos.append(nodo_AST('(', num_nodo + 1))
        self.nodo.hijos.append(izquierda.nodo)
        self.nodo.hijos.append(nodo_AST(')', num_nodo + 2))
        self.nodo.hijos.append(nodo_AST('UNION',num_nodo + 3))
        self.nodo.hijos.append(nodo_AST('(', num_nodo + 4))
        self.nodo.hijos.append(derecha.nodo)
        self.nodo.hijos.append(nodo_AST(')', num_nodo + 5))

        #Gramatica
        self.grammar_ = '<TR><TD> union ::= (seleccionar) UNION (seleccionar); </TD><TD> union = new union(izquierda,derecha); </TD></TR>\n'
        self.grammar_ += izquierda.grammar_
        self.grammar_ += derecha.grammar_
        
    def ejecutar(self):
        izquierdaA=self.izquierda.ejecutar(True)
        derechaA=self.derecha.ejecutar(True)
        salidaTabla = PrettyTable()
        salidaTabla.field_names = izquierdaA.tipo
        salidaTabla.add_rows(izquierdaA.query)
        salidaTabla.add_rows(derechaA.query)

        add_text('\n')
        add_text(salidaTabla)
        add_text('\n')