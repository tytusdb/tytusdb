from enum import Enum

class TipoRetornoInstruccion(Enum):
    RETORNO = 1
    ROMBER = 2
    CONTINUE = 3
    NORMAL = 4
    ERROR = 5



class RetornoInstruccion():

    def __init__(self, tipoRetorno,Simbolo = None):
        self.tipoRetornoInstruccion = tipoRetorno
        self.SimboloRetornar = Simbolo



