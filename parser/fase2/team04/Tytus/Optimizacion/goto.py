from Optimizacion.instruccion import Instruccion

class Goto(Instruccion):
    def __init__(self, id, linea):
        self.id = id
        self.linea = linea
        
    def toString(self):
        codigo = f"goto .{self.id}\n"
        return codigo