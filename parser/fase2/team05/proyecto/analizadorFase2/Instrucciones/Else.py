from analizadorFase2.Abstractas.Instruccion import Instruccion

class Else_inst(Instruccion):
    def __init__(self, cuerpoelse):
        self.cuerpoelse = cuerpoelse
