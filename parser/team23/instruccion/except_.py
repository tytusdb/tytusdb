from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *
from prettytable import PrettyTable


class except_(instruccion):
    def __init__(self, izquierda, derecha, line, column, num_nodo):
        super().__init__(line, column)
        self.izquierda = izquierda
        self.derecha = derecha

        # AST
        self.nodo = nodo_AST('EXCEPT', num_nodo)
        self.nodo.hijos.append(nodo_AST('(', num_nodo + 1))
        self.nodo.hijos.append(izquierda.nodo)
        self.nodo.hijos.append(nodo_AST(')', num_nodo + 2))
        self.nodo.hijos.append(nodo_AST('EXCEPT', num_nodo + 3))
        self.nodo.hijos.append(nodo_AST('(', num_nodo + 4))
        self.nodo.hijos.append(derecha.nodo)
        self.nodo.hijos.append(nodo_AST(')', num_nodo + 5))

        # Gramatica
        self.grammar_ = '<TR><TD> except ::= (seleccionar) EXCEPT (seleccionar); </TD><TD> except = new except_(izquierda,derecha); </TD></TR>\n'
        self.grammar_ += izquierda.grammar_
        self.grammar_ += derecha.grammar_

    def ejecutar(self):
        izquierdaA = self.izquierda.ejecutar(True)
        derechaA = self.derecha.ejecutar(True)
        aux1 = []
        resultado = []
        tabla1 = izquierdaA.query
        tabla2 = derechaA.query
        salidaTabla = PrettyTable()
        salidaTabla.field_names = izquierdaA.tipo

        for m in tabla2:
            for n in tabla1:
                if m == n:
                    aux1.append(n)


        for n in tabla1:
            if self.metodo_Pegre(n,aux1):
                resultado.append(n)
                print(n)


        salidaTabla.add_rows(resultado)

        add_text('\n')
        add_text(salidaTabla)
        add_text('\n')

    def metodo_Pegre(self,dato,lista):
        aux = lista
        bandera = True

        for recorrido in aux:
            if(recorrido!=dato):
                bandera = True
            else:
                bandera = False
                break;

        return bandera