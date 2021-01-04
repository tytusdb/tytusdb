from analizadorFase2.Abstractas.Instruccion import Instruccion

class Declaracion(Instruccion):
    def __init__(self, id):
        self.id = id