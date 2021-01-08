from analizadorFase2.Abstractas.Instruccion import Instruccion

class Asignacion(Instruccion):
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor