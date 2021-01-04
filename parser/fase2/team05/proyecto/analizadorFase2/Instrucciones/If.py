from analizadorFase2.Abstractas.Instruccion import Instruccion

class If_inst(Instruccion):
    def __init__(self, condicion, cuerpo, elsest):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.elsest = elsest