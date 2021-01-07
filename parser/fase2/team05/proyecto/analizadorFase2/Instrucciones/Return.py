from analizadorFase2.Abstractas.Instruccion import Instruccion

class Return_inst(Instruccion):
    def __init__(self, valor):
        self.valor = valor