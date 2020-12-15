from Expresion.Expresion import Expresion
from Entorno import Entorno

class Binaria(Expresion) :
    '''
        Esta clase representa la Expresión Binaria.
        Esta clase recibe los operandos y el operador
    '''
    def __init__(self, exp1, exp2, operador) :
        Expresion.__init__(self)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
