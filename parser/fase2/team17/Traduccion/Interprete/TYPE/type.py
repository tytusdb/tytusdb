from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.Primitivos.TIPO import TIPO
from Interprete.SELECT.indexador_auxiliar import indexador_auxiliar
from Interprete.SELECT.indexador_auxiliar import IAT
from Interprete.simbolo import Simbolo

class type(NodoArbol):

    def __init__(self, indentificador, ListaTipos, line, coliumn):
        super().__init__(line, coliumn)
        self.indentificador = indentificador
        self.ListaTipos = ListaTipos

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        indentificador = self.indentificador
        value:Valor = Valor(TIPO.LISTA, indentificador)
        lista = []
        for i in self.ListaTipos:
            val:Valor = i.execute(entorno, arbol)
            value.insert_tipo_toType(str(val.data))
            lista.append(str(val.data))
        simbol:Simbolo = Simbolo(indentificador, TIPO.LISTA, value)
        entorno.insertar_variable(simbol)
        arbol.console.append("\n" + "Type: " + indentificador + " --> Valores: "+ str(lista) + "\n")
        return