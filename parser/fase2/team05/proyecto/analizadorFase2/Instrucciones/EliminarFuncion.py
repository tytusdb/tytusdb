from analizadorFase2.Abstractas.Instruccion import Instruccion

class EliminarFuncion(Instruccion):
    def __init__(self, id):
        self.id = id