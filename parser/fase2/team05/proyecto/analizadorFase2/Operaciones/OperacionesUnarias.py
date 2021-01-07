from analizadorFase2.Operaciones.TiposOperacionesA import TiposOperaciones
from analizadorFase2.Abstractas.Expresion import Expresion


class OperacionesUnarias(Expresion):
    def __init__(self, tipoOp : TiposOperaciones, valor):
        self.tipoop = tipoOp
        self.valor = valor