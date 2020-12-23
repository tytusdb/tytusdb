from Expresion.Expresion import Expresion
from Expresion.Terminal import Terminal
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
        if (self.exp1.tipo.tipo == 'identificador'):
            return self

        valexp=self.exp1.getval(entorno)
        if isinstance(valexp, Terminal):
            valexp = valexp.getval(entorno)

        if self.operador == '+':
            self.tipo=self.exp1.tipo
            self.tipo= valexp
        elif self.operador == '-':
            self.tipo=self.exp1.tipo
            self.valor = valexp*-1
        elif self.operador == 'not':
            self.tipo='boolean'
            self.valor =  not valexp

        print(self.valor)
        return self.valor


