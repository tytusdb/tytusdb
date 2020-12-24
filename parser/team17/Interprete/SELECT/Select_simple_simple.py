from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.SELECT.indexador_auxiliar import indexador_auxiliar
from Interprete.SELECT.indexador_auxiliar import IAT
from Interprete.Primitivos.TIPO import TIPO
from Interprete.simbolo import Simbolo
from Interprete.OperacionesConExpresiones.OperadoresCondicionales import OperadoresCondicionales
from StoreManager import jsonMode as j
from prettytable import PrettyTable
from Interprete.Meta import Meta
from Interprete.SELECT.indexador_auxiliar import indexador_auxiliar

class select_simple_simple(NodoArbol):

    def __init__(self, lista_exp, line, column):
        super().__init__(line, column)
        self.lista_exp = lista_exp

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):

        tabla:Valor = Valor(TIPO.MATRIZ, "Select simple simple")
        tabla.inicializarMatrix_boring(2,len(self.lista_exp))
        indexM = 0 # V_TablaSelect.matriz[m][index] = lista[m]

        for i in self.lista_exp:
            if isinstance(i, indexador_auxiliar):
                indexador:indexador_auxiliar = i
                expresion: Valor = indexador.origen.execute(entorno, arbol)
                tabla.matriz[0][indexM] = Valor(TIPO.CADENA, indexador.referencia)
                tabla.matriz[1][indexM] = expresion
                indexM = indexM + 1
                #arbol.console.append("\n" + "tytus > [" + indexador.referencia + "] : " + str(expresion.data) + "\n")
                pass
            else:
                expresion: Valor = i.execute(entorno, arbol)
                tabla.matriz[0][indexM] = "Funcion"
                tabla.matriz[1][indexM] = expresion
                #arbol.console.append("\n" + "tytus > [Funcion] : " + str(expresion.data) + "\n")
        arbol.console.append("\n" + tabla.inicializarPrettybabe() + "\n")
        return
