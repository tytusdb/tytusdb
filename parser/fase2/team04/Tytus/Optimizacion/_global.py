from Optimizacion.instruccion import Instruccion

class Global(Instruccion):
    def __init__(self, id, linea):
        self.id = id
        self.linea = linea
        
    def toString(self):
        codigo = f"global {self.id}\n"
        return codigo