from Optimizacion.instruccion import Instruccion

class Asignacion(Instruccion):
    def __init__(self, izquierda, derecha, linea):
        self.izquierda = izquierda
        self.derecha = derecha
        self.linea = linea
        
    def toString(self):
        codigo = f"{self.izquierda.toString()} = {self.derecha.toString()}\n"
        return codigo