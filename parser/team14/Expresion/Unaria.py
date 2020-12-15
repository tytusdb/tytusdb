from Expresion.Expresion import Expresion
from Entorno import Entorno

class Unaria(Expresion) :
    '''
        Esta clase representa la Expresión Binaria.
        Esta clase recibe los operandos y el operador
    '''
    def __init__(self, exp1,operador) :
        Expresion.__init__(self)
        self.exp1 = exp1
        self.operador = operador

    def getval(self,entorno):
        valexp=self.exp1.getval(entorno)
        if self.operador == '+':
            self.valor= valexp
        elif self.operador == '-':
            self.valor = valexp*-1
        elif self.operador == 'not':
            self.valor =  not valexp

        print(self.valor)
        return self.valor


