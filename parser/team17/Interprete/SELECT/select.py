from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor

class select(NodoArbol):

    def __init__(self, listavalores, ID, listawhere, line, column):
        super().__init__(line, column)
        self.listavalores = listavalores
        self.ID = ID
        self.listawhere = listawhere

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        for item in self.listavalores:
            item_:Valor = item.execute(entorno, arbol)
            print(item_.data)
        pass
        print(self.ID)
        for item in self.listawhere:
            item_:Valor = item.execute(entorno, arbol)
            print(item_.data)
        pass