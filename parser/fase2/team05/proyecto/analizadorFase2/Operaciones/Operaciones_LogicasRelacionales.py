from analizadorFase2.Abstractas.Expresion import Expresion
from analizadorFase2.Operaciones.TiposOperacionesLR import TiposOperacionesLR

class OperacionesLogicasRelacionales(Expresion):
    def __init__(self, tipo : TiposOperacionesLR, izquierdo, derecho):
        Expresion.__init__(self)
        self.tipo = tipo
        self.izquierdo = izquierdo
        self.derecho = derecho