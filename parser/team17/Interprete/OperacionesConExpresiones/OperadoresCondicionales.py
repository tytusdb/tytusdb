from Interprete.NodoAST import NodoArbol

class OperadoresCondicionales():

    def __init__(self, izq, der, tipoOperaRelacional):
        self.izq = izq
        self.der = der
        self.tipoOperaRelacional = tipoOperaRelacional

    def getIzq(self):
        return self.izq

    def getDer(self):
        return self.der

    def getTipoOperaRelacional(self):
        return self.tipoOperaRelacional
