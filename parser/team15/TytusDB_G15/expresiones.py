from enum import Enum

class ExpresionNumerica:
    '''
        Esta clase representa una expresión numérica
    '''
class ExpresionIdentificador(ExpresionNumerica) :
    def __init__(self, id = "") :
        self.id = id

class ExpresionNumero(ExpresionNumerica) :
    def __init__(self, val = 0) :
        self.val = val