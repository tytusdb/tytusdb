from Optimizacion.instruccion import Instruccion

class _From(Instruccion):
    def __init__(self, id_list, id, linea):
        self.id_list = id_list
        self.id = id
        self.linea = linea
        
    def toString(self):
        codigo = f"from {'.'.join(self.id_list)} import {self.id}\n"
        return codigo