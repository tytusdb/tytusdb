from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor

class Opera_Relacionales(NodoArbol):

    def __init__(self, izq:NodoArbol, der:NodoArbol, tipoOperaRelacional, line, coliumn):
        super().__init__(line, coliumn)
        self.izq = izq
        self.der = der
        self.tipoOperaRelacional = tipoOperaRelacional

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        izquierdo:Valor = self.izq.execute(entorno, arbol)
        derecho:Valor = self.der.execute(entorno, arbol)

        if self.tipoOperaRelacional == "=":
            retorno:Valor
            if izquierdo.data == derecho.data:
                retorno = Valor(3, True);
                return  retorno;
            else:
                retorno = Valor(3, False);
                return retorno;

        elif self.tipoOperaRelacional == "u:=":
            return {izquierdo.data: self.der}
