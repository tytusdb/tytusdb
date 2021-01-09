from Optimizacion.instruccion import Instruccion

class Label(Instruccion):
    def __init__(self, id, linea):
        self.id = id
        self.linea = linea
        
    def toString(self):
        codigo = f"label .{self.id}\n"
        return codigo