from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos

class RESTA(NodoArbol):

    def __init__(self, izq: NodoArbol, der: NodoArbol, line, coliumn):
        super().__init__(line, coliumn)
        self.izq = izq
        self.der = der

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        tipoRes = COMPROBADOR_deTipos(self.izq.analizar_semanticamente(entorno, arbol),
                                      self.der.analizar_semanticamente(entorno, arbol), "-")
        if tipoRes != -1:
            print(tipoRes.getTipoResultante())
            return tipoRes.getTipoResultante()
        else:
            # ERROR SEMANTICO de tipo
            pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        izquierdo = self.izq.traducir(entorno, arbol)  # <-- tiene un temporal
        derecho = self.der.traducir(entorno, arbol)  # <-- tiene un temporal
        if self.analizar_semanticamente(entorno, arbol) == 0:
            tmp = arbol.getTemp()
            arbol.addC3D(tmp + " = int(" + izquierdo + ") - int(" + derecho + ")")
            return tmp
        elif self.analizar_semanticamente(entorno, arbol) == 1:
            tmp = arbol.getTemp()
            arbol.addC3D(tmp + " = float(" + izquierdo + ") - float(" + derecho + ")")
            return tmp
        elif self.analizar_semanticamente(entorno, arbol) == 2:
            tmp = arbol.getTemp()
            #ERROR SEMANTICO DE TIPOS NO SE PUEDEN RESTAR TIPOS CADENA
            return tmp

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol) -> str:
        cadena: str = self.izq.getString(entorno, arbol) + str(" - ") + self.der.getString(entorno, arbol)
        return cadena

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        izquierdo: Valor = self.izq.getValueAbstract(entorno, arbol)  # <-- tiene un temporal
        derecho: Valor = self.der.getValueAbstract(entorno, arbol)  # <-- tiene un temporal
        if self.analizar_semanticamente(entorno, arbol) == 0:
            newVal: Valor = Valor(TIPO.ENTERO, int(str(izquierdo.data)) - int(str(derecho.data)))
            return newVal
        elif self.analizar_semanticamente(entorno, arbol) == 1:
            newVal: Valor = Valor(TIPO.DECIMAL, float(str(izquierdo.data)) - float(str(derecho.data)))
            return newVal
        elif self.analizar_semanticamente(entorno, arbol) == 2:
            #newVal: Valor = Valor(TIPO.CADENA, str(str(izquierdo.data)) - str(derecho.data))
            # ERROR SEMANTICO DE TIPOS NO SE PUEDEN RESTAR TIPOS CADENA
            return None
