from Optimizacion.expresion import Expresion

class Operacion(Expresion): 
    def __init__(self, izquierda, operador, derecha, linea):
        self.izquierda = izquierda
        self.operador = operador
        self.derecha = derecha
        self.linea = linea
        
    def toString(self):
        operador = self.operador if self.operador == '.' else f" {self.operador} "
        codigo = f"{self.izquierda.toString()}{operador}{self.derecha.toString()}"
        return codigo