from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.SELECT.indexador_auxiliar import indexador_auxiliar

class select(NodoArbol):

    def __init__(self, listavalores, ID, listawhere, line, column):
        super().__init__(line, column)
        self.listavalores = listavalores
        self.ID = ID
        self.listawhere = listawhere

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        #for item in self.listavalores:
            #item_:Valor = item.execute(entorno, arbol)
            #print(item_.data)
        #pass
        print(self.ID)
        for item in self.listawhere:
            item_:Valor = item.execute(entorno, arbol)
            print(item_.data)
        pass
        valor_:Valor = Valor(0, 7)
        value:Valor = Valor(666, "Matrix")
        value.inicializarMatrix_boring(5,5)
        value.consola_imprimirMatriz_NERY()
        encabezados:list = ['1ra', '2da', '3ra', '4ta', '5ta']
        value.establecer_encabezados(encabezados)
        value.ingresar_aMatriz_boring(valor_, 1, 1)
        value.ingresar_aMatriz_boring(valor_, 3, 1)
        value.consola_imprimirMatriz_NERY()

        columna1:list = value.obtenerColumna_enBase_aIndice(1)
        value_columna1:Valor = Valor(667, "lista")
        value_columna1.inicizalizar_lista(columna1)
        value_columna1.imprimir_lista()

        columna2: list = value.obtenerColumna_enBase_aEncabezado('2da')
        value_columna2: Valor = Valor(667, "lista")
        value_columna2.inicizalizar_lista(columna2)
        value_columna2.imprimir_lista()