class Retorno:
    def __init__(self, instruccion, nodo):
        self._instruccion = instruccion
        self._nodo = nodo

    def getInstruccion(self):
        return self._instruccion

    def getNodo(self):
        return self._nodo