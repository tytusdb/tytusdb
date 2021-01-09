from Optimizacion.instruccion import Instruccion

class _Import(Instruccion):
    def __init__(self, id, linea):
        self.id = id
        self.linea = linea
        
    def toString(self):
        codigo = f"import {self.id}\n"
        return codigo