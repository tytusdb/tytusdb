from analizadorFase2.Operaciones.TiposOperacionesA import TiposOperaciones
from analizadorFase2.Abstractas.Expresion import Expresion


class Operaciones_Aritmeticas(Expresion):
    def __init__(self, tipo : TiposOperaciones, izquierdo, derecho):
        self.tipo = tipo
        self.izquierdo = izquierdo
        self.derecho = derecho