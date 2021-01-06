from Analisis_Ascendente.Instrucciones.instruccion import Instruccion


class Return(Instruccion):
    def __init__(self,expresion):
        self.expr = expresion