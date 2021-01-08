from Optimizacion.expresion import Expresion

class Literal(Expresion): 
    def __init__(self, valor, linea):
        self.valor = valor
        self.linea = linea
        
    def toString(self):
        codigo = f"{self.valor}"
        return codigo