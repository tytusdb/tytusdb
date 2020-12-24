

from Expresion.Binaria import Binaria
from Entorno import Entorno
from Tipo import Tipo
from Expresion.Terminal import Terminal
import math
from tkinter import *
from Expresion.variablesestaticas import *
from reportes import *
class Aritmetica(Binaria):
    def __init__(self, exp1, exp2, operador):
        'Se usan los valores de las clases padres'
        Binaria.__init__(self,exp1,exp2,operador)

    def getval(self,entorno):

        if (self.exp1.tipo.tipo == 'identificador' or self.exp2.tipo.tipo == 'identificador'):
            return self


        valizq=self.exp1.getval(entorno);
        valder=self.exp2.getval(entorno);
        valizq=valizq.valor
        valder=valder.valor



        if type(valizq) not in (int, float, complex) or type(valder) not in (int, float, complex) :
            reporteerrores.append(Lerrores("Error Semantico",
                                           "Error los valores de los operandos deben ser numericos",
                                           0, 0))
            variables.consola.insert(INSERT,
                                     "Error los valores de los operandos deben ser numericos")

        if self.operador == '+':
            self.valor = valizq+valder;
        elif self.operador == '-':
            self.valor = valizq - valder;
        elif self.operador ==  '*':
            self.valor = valizq * valder;
        elif self.operador == '/':
            self.valor = valizq / valder;
        elif self.operador == '%':
            self.valor = valizq % valder;
        elif self.operador == '^':
            self.valor = valizq ** valder;

        tipo= Tipo(self.valor,'decimal')
        self.tipo=tipo
        return self