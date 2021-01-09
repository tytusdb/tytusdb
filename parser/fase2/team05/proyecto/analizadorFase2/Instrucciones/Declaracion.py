from analizadorFase2.Abstractas.Instruccion import Instruccion

class Declaracion(Instruccion):
    def __init__(self, id,tipo):
        self.id = id
        self.tipo = tipo