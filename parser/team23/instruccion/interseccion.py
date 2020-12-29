from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *
from prettytable import PrettyTable


class interseccion(instruccion):
    def __init__(self, izquierda, derecha, line, column, num_nodo):
        super().__init__(line, column)
        self.izquierda = izquierda
        self.derecha = derecha

        # AST
        self.nodo = nodo_AST('INTERSECT', num_nodo)
        self.nodo.hijos.append(nodo_AST('(', num_nodo + 1))
        self.nodo.hijos.append(izquierda.nodo)
        self.nodo.hijos.append(nodo_AST(')', num_nodo + 2))
        self.nodo.hijos.append(nodo_AST('INTERSECT', num_nodo + 3))
        self.nodo.hijos.append(nodo_AST('(', num_nodo + 4))
        self.nodo.hijos.append(derecha.nodo)
        self.nodo.hijos.append(nodo_AST(')', num_nodo + 5))

        # Gramatica
        self.grammar_ = '<TR><TD> intersect ::= (seleccionar) INTERSECT (seleccionar); </TD><TD> intersect = new interseccion(izquierda,derecha); </TD></TR>\n'
        self.grammar_ += izquierda.grammar_
        self.grammar_ += derecha.grammar_

    def ejecutar(self):
        izquierdaA = self.izquierda.ejecutar(True)
        derechaA = self.derecha.ejecutar(True)
        resultado = []
        tabla1 = izquierdaA.query
        tabla2 = derechaA.query
        salidaTabla = PrettyTable()
        salidaTabla.field_names = izquierdaA.tipo

        for m in tabla1:
            for n in tabla2:
                if m == n:
                    resultado.append(m)
                    print(m)

        salidaTabla.add_rows(resultado)

        add_text('\n')
        add_text(salidaTabla)
        add_text('\n')