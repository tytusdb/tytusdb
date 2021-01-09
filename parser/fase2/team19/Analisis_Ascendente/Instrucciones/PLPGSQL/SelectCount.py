from Analisis_Ascendente.Instrucciones.instruccion import Instruccion

class SelectCount(Instruccion):
    def __init__(self,idtabla):
        self.idtabla = idtabla

    def get_quemado(self):
        return 'select count(*) from %s' % self.idtabla
