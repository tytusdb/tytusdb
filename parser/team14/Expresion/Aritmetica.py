

from Expresion.Binaria import Binaria
from Entorno import Entorno
from Tipo import Tipo
from Expresion import Expresion
import math

class Aritmetica(Binaria):
    def __init__(self, exp1, exp2, operador):
        'Se usan los valores de las clases padres'
        Binaria.__init__(self,exp1,exp2,operador)

    def getval(self,entorno):

        if (self.exp1.tipo.tipo == 'identificador' or self.exp2.tipo.tipo == 'identificador'):
            return self


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
            self.val = valizq ** valder;

        tipo= Tipo(self.val,'decimal')
        self.tipo=tipo
        return self.val