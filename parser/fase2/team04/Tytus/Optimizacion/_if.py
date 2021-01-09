from Optimizacion.instruccion import Instruccion

class _If(Instruccion):
    def __init__(self, expresion, id, linea):
        self.expresion = expresion
        self.id = id
        self.linea = linea
        
    def toString(self):
        codigo = f"if {self.expresion.toString()}: goto .{self.id}\n"
        return codigo