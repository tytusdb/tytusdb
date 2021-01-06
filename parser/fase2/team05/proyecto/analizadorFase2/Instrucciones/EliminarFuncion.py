from analizadorFase2.Abstractas.Instruccion import Instruccion

class EliminarFuncion(Instruccion):
    def __init__(self, id, instruccion3d):
        self.id = id
        self.instruccion3d = instruccion3d