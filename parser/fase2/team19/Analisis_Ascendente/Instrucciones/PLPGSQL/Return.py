from Analisis_Ascendente.Instrucciones.instruccion import Instruccion


class Return(Instruccion):
    def __init__(self,expresion):
        self.expr = expresion

    def get_quemado(self):
        return 'return %s' % self.expr.get_quemado()