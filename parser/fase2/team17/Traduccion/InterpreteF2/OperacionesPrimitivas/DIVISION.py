from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos
from InterpreteF2.Reporteria.ErroresSemanticos import ErroresSemanticos

class DIVISION(NodoArbol):

    def __init__(self, izq: NodoArbol, der: NodoArbol, line, coliumn):
        super().__init__(line, coliumn)
        self.izq = izq
        self.der = der

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        tipoRes = COMPROBADOR_deTipos(self.izq.analizar_semanticamente(entorno, arbol),
                                      self.der.analizar_semanticamente(entorno, arbol), "+")
        if tipoRes != -1:
            print(tipoRes.getTipoResultante())
            return tipoRes.getTipoResultante()
        else:
            # ERROR SEMANTICO de tipo
            pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):

        try:
            if self.esNecesarioOptimizar(entorno, arbol):
                return self.traducir_optimizado(entorno, arbol)

            izquierdo = self.izq.traducir(entorno, arbol)  # <-- tiene un temporal
            derecho = self.der.traducir(entorno, arbol)  # <-- tiene un temporal

            if derecho == 0:
                # Error de tipos
                desc = 'Parametro derecho de DIVISION es cero'
                reportero = ErroresSemanticos(desc, str(self.linea), str(self.columna), 'DIVISION')
                arbol.ErroresSemanticos.append(reportero)
                # -------------------------------------------------------------
                tmp = arbol.getTemp()
                arbol.addC3D(tmp + " = 0")
                return tmp

            else:
                if self.analizar_semanticamente(entorno, arbol) == 0:
                    tmp = arbol.getTemp()
                    arbol.addC3D(tmp + " = int(" + izquierdo + ") / int(" + derecho + ")")
                    return tmp
                elif self.analizar_semanticamente(entorno, arbol) == 1:
                    tmp = arbol.getTemp()
                    arbol.addC3D(tmp + " = float(" + izquierdo + ") / float(" + derecho + ")")
                    return tmp
                else:
                    # Error de tipos
                    desc = 'Parametros no validos en DIVISION'
                    reportero = ErroresSemanticos(desc, str(self.linea), str(self.columna), 'DIVISION')
                    arbol.ErroresSemanticos.append(reportero)
                    # -------------------------------------------------------------
                    tmp = arbol.getTemp()
                    arbol.addC3D(tmp + " = 0")
                    return tmp
        except:
            tmp = arbol.getTemp()
            arbol.addC3D(tmp + " = 0")
            return tmp


    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol) -> str:
        cadena: str = self.izq.getString(entorno, arbol) + str(" / ") + self.der.getString(entorno, arbol)
        return cadena

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        izquierdo: Valor = self.izq.getValueAbstract(entorno, arbol)  # <-- tiene un temporal
        derecho: Valor = self.der.getValueAbstract(entorno, arbol)  # <-- tiene un temporal
        if self.analizar_semanticamente(entorno, arbol) == 0:
            newVal: Valor = Valor(TIPO.ENTERO, int(str(izquierdo.data)) / int(str(derecho.data)))
            return newVal
        elif self.analizar_semanticamente(entorno, arbol) == 1:
            newVal: Valor = Valor(TIPO.DECIMAL, float(str(izquierdo.data)) / float(str(derecho.data)))
            return newVal
        elif self.analizar_semanticamente(entorno, arbol) == 2:
            #newVal: Valor = Valor(TIPO.CADENA, str(str(izquierdo.data)) / str(derecho.data))
            # ERROR SEMANTICO DE TIPOS NO SE PUEDEN OPERAR TIPOS CADENA
            return None

    def esNecesarioOptimizar(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        if str(self.izq.getString(entorno, arbol)) == '1':
            return True
        elif str(self.der.getString(entorno, arbol)) == '1':
            return True
        elif str(self.izq.getString(entorno, arbol)) == '0':
            return True
        return False

    def traducir_optimizado(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        try:
            if str(self.izq.getString(entorno, arbol)) == '1':
                derecho = []
                derecho.append(self.der.traducir(entorno, arbol))
                derecho.append('11-15')
                return derecho
            elif str(self.der.getString(entorno, arbol)) == '1':
                izquierdo = []
                izquierdo.append(self.izq.traducir(entorno, arbol))
                izquierdo.append('11-15')
                return izquierdo
            if str(self.izq.getString(entorno, arbol)) == '0':
                derecho = []
                derecho.append(self.der.traducir(entorno, arbol))
                derecho.append('18')
                return derecho
        except:
            tmp = arbol.getTemp()
            arbol.addC3D(tmp + " = 0")
            return tmp