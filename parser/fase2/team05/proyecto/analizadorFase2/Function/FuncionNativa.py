from analizadorFase2.Abstractas.Expresion import Expresion
from analizadorFase2.Abstractas.Instruccion import Instruccion
from analizadorFase2.Function.TipoFunNativa import TipoFunNativa


class FuncionNativa(Instruccion):
    def __init__(self, tipo : TipoFunNativa, parametros):
        self.tipo = tipo
        self.parametros = parametros
        if parametros is None:
            self.numparametros = 0
        elif isinstance(parametros, list):
            self.numparametros = len(parametros)
        else:
            self.numparametros = 1

#class Funcion(Expresion):
#    def __init__(self, id, parametros, declaraciones, cuerpo):
#        self.id = id
#        self.declaraciones = declaraciones
#        self.parametros = parametros
#        self.cuerpo = cuerpo
#        if parametros is None:
#            self.numparametros = 0
#        else:
#            self.numparametros = len(parametros)