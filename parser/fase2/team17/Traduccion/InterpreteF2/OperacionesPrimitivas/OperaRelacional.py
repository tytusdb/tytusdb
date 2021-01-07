from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos
from InterpreteF2.Reporteria.ErroresSemanticos import ErroresSemanticos

class OperaRelacional(NodoArbol):

    def __init__(self, izq, der, tipoOperaRelacional, line, coliumn):
        super().__init__(line, coliumn)
        self.izq = izq
        self.der = der
        self.tipoOperaRelacional = tipoOperaRelacional
        self.Isvalidador_Regla4 = False

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        tipoRes = COMPROBADOR_deTipos(self.izq.analizar_semanticamente(entorno, arbol), self.der.analizar_semanticamente(entorno, arbol), "+")
        if tipoRes != -1:
            return tipoRes.getTipoResultante()
        else:
            # ERROR SEMANTICO de tipo
            pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        try:
            izquierdo = self.izq.traducir(entorno, arbol)  # <-- tiene un temporal
            derecho = self.der.traducir(entorno, arbol)  # <-- tiene un temporal

            if str(izquierdo) == 'None' or str(izquierdo) == '':
                descripcion = 'El nodo izquierdo no es valido en operacion relacional/Logica'
                reportero = ErroresSemanticos(descripcion, str(self.linea), str(self.columna), 'OperacionesRelaciones')
                arbol.ErroresSemanticos.append(reportero)
                return 'False'
            elif str(derecho) == 'None' or str(derecho) == '':
                descripcion = 'El nodo derecho no es valido en operacion relacional/Logica'
                reportero = ErroresSemanticos(descripcion, str(self.linea), str(self.columna), 'OperacionesRelaciones')
                arbol.ErroresSemanticos.append(reportero)
                return 'False'
            else:
                pass

            tmp = str(izquierdo) + " " + str(self.tipoOperaRelacional) + " " + str(derecho)
            return tmp
        except:
            return 'False'

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def validador_Regla4(self, entorno: Tabla_de_simbolos, arbol:Arbol):


        try:
            izquierdo: Valor = self.izq.getValueAbstract(entorno, arbol)  # <-- tiene un temporal
            derecho: Valor = self.der.getValueAbstract(entorno, arbol)  # <-- tiene un temporal
            if str(izquierdo.data) == str(derecho.data):
                return True
        except:
            pass
        return False

    def validador_Regla5(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        try:
            if str(self.tipoOperaRelacional) == '==':
                izquierdo: Valor = self.izq.getValueAbstract(entorno, arbol)  # <-- tiene un temporal
                derecho: Valor = self.der.getValueAbstract(entorno, arbol)  # <-- tiene un temporal
                if str(izquierdo.data) != str(derecho.data):
                    return True
        except:
            pass
        return False

