from webbrowser import Elinks

from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.Primitivos.TIPO import TIPO
from Interprete.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos
from Interprete.Manejo_errores.ErroresSemanticos import ErroresSemanticos

class SUMA(NodoArbol):

    def __init__(self, izq: NodoArbol, der: NodoArbol, line, coliumn):
        super().__init__(line, coliumn)
        self.izq = izq
        self.der = der

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        izquierdo: Valor = self.izq.execute(entorno, arbol)
        derecho: Valor = self.der.execute(entorno, arbol)

        if derecho==0:
            Error:ErroresSemanticos = ErroresSemanticos("Error semantico no se puede dividir entre 0", self.linea, self.columna, "DIVISION")
            arbol.ErroresSemanticos.append(Error)
        else:
            tipoRes = COMPROBADOR_deTipos(izquierdo.tipo, derecho.tipo, "/")
            if tipoRes == 0:
                newValor:Valor = Valor(tipoRes, izquierdo.data / derecho.data)
                return newValor;

            
        
        