from analizadorFase2.Abstractas.Instruccion import Instruccion

class Funcion(Instruccion):
    def __init__(self, id, parametros, declaraciones, cuerpo):
        self.id = id
        self.declaraciones = declaraciones
        self.parametros = parametros
        self.cuerpo = cuerpo
        if parametros is None:
            self.numparametros = 0
        else:
            self.numparametros = len(parametros)