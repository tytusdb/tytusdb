from analizadorFase2.Abstractas.Expresion import Expresion
from analizadorFase2.Abstractas.Expresion import Tipos


class Primitivo(Expresion):
    def __init__(self, type : Tipos, valor):
        Expresion.__init__(self)
        self.tipo = type
        self.valor = valor
