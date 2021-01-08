from analizadorFase2.Abstractas.Instruccion import Instruccion

class Llamada(Instruccion):
    def __init__(self, id, parametros):
        self.id = id
        self.parametros = parametros
        if parametros is None:
            self.numparametros = 0
        else:
            self.numparametros = len(parametros)

    def setInstruccion3d(self, instruccion):
        self.instruccion3d = instruccion

    def setInstruccion(self, instruccion):
        self.instruccion = instruccion

    def getInstruccion(self):
        return self.instruccion