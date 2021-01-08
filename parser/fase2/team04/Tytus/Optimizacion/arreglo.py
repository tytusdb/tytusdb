from Optimizacion.expresion import Expresion

class Arreglo(Expresion): 
    def __init__(self, id, expresion, linea):
        self.id = id
        self.expresion = expresion
        self.linea = linea
        
    def toString(self):
        id = self.id if self.id else ""
        codigo = f"{id}[{self.expresion.toString()}]"
        return codigo