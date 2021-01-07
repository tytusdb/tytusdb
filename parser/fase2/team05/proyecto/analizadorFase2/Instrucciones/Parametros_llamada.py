from analizadorFase2.Abstractas.Instruccion import Instruccion

class Parametro_llamada(Instruccion):
    def __init__(self, valor):
        self.valor = valor