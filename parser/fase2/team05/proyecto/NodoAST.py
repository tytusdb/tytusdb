class NodoAST:
    def __init__(self, contenido):
        self._contenido = contenido
        self._hijos = []
    
    def getContenido(self):
        return self._contenido

    def getHijos(self):
        return self._hijos

    def setHijo(self, hijo):
        self._hijos.append(hijo)