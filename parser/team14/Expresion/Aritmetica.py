

from Expresion.Binaria import Binaria
from Entorno import Entorno
import math

class Aritmetica(Binaria):
    def __init__(self, exp1, exp2, operador):
        'Se usan los valores de las clases padres'
        Binaria.__init__(self,exp1,exp2,operador)

    def getval(self,entorno):
        valizq=self.exp1.getval(entorno);
        valder=self.exp2.getval(entorno);


        if type(valizq) not in (int, float, complex) or type(valder) not in (int, float, complex) :
            return 'Error ambos operandos deben ser numericos'

        if self.operador == '+':
            self.val = valizq+valder;
        elif self.operador == '-':
            self.val = valizq - valder;
        elif self.operador ==  '*':
            self.val = valizq * valder;
        elif self.operador == '/':
            self.val = valizq / valder;
        elif self.operador == '%':
            self.val = valizq % valder;
        elif self.operador == '^':
            self.val = valizq ^ valder;

        return self.val