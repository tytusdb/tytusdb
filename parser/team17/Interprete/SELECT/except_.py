from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.Primitivos.TIPO import TIPO
from Interprete.SELECT.indexador_auxiliar import indexador_auxiliar
from Interprete.SELECT.indexador_auxiliar import IAT
from Interprete.simbolo import Simbolo

class except_(NodoArbol):

    def __init__(self, select_1, select_2, line, coliumn):
        super().__init__(line, coliumn)
        self.select_1 = select_1
        self.select_2 = select_2

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):

        TV_select1: Valor = self.select_1.execute(entorno, arbol)
        TV_select2: Valor = self.select_2.execute(entorno, arbol)

        TV_select2_columna: Valor = Valor(TIPO.LISTA, "COMPARADOR")
        TV_select2_columna.inicizalizar_lista(TV_select2.obtenerColumna_enBase_aIndice(0))
        lista_TV_select2 = TV_select2_columna.getLista_sinPareas()

        TV_select1.inicializarPrettybabe()
        valEncabezado:Valor = TV_select1.matriz[0][0]
        encabezado =  str(valEncabezado.data)
        for i in lista_TV_select2:
            TV_select1.filtrarWhere_experimental("=", encabezado, str(i.data))

        arbol.console.append("\n" + "Except ---> GO" + "\n")
        arbol.console.append(TV_select1.inicializarPrettybabe_experimental_invertido())
        arbol.console.append("\n" + "Except ---> END" + "\n")
        return

