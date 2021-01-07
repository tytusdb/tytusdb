

from Expresion.Binaria import Binaria
from Entorno import Entorno
from Tipo import Tipo
from Expresion.Terminal import Terminal
from Expresion.Id import Identificador
import math
from tkinter import *
from Expresion.variablesestaticas import *
from reportes import *
class Aritmetica(Binaria):
    def __init__(self, exp1, exp2, operador):
        'Se usan los valores de las clases padres'
        Binaria.__init__(self,exp1,exp2,operador)
        self.stringsql+= str(exp1.stringsql) +' '
        self.stringsql+= self.operador +' '
        self.stringsql+= str(exp2.stringsql)+' 

    def getval(self,entorno):

        if isinstance(self.exp1,Identificador) and isinstance(self.exp2,Identificador):
            return self


        valizq=self.exp1.getval(entorno)
        valder=self.exp2.getval(entorno)
        valizq=valizq.valor
        valder=valder.valor



        if type(valizq) not in (int, float, complex) or type(valder) not in (int, float, complex) :
            reporteerrores.append(Lerrores("Error Semantico",
                                           "Error los valores de los operandos deben ser numericos",
                                           0, 0))
            variables.consola.insert(INSERT,
                                     "Error los valores de los operandos deben ser numericos")

        if self.operador == '+':
            self.valor = valizq+valder
        elif self.operador == '-':
            self.valor = valizq - valder
        elif self.operador ==  '*':
            self.valor = valizq * valder
        elif self.operador == '/':
            self.valor = valizq / valder
        elif self.operador == '%':
            self.valor = valizq % valder
        elif self.operador == '^':
            self.valor = valizq ** valder

        tipo= Tipo(self.valor,'decimal')
        self.tipo=tipo
        return self

    def traducir(self,entorno):
        ''
        if str(self.operador).lower() == '%':
            ''
        elif str(self.operador).lower() == '^':
            ''
        else:
            self.temp = entorno.newtemp()
            nt=self.temp
            exp1=self.exp1.traducir(entorno)
            exp2=self.exp2.traducir(entorno)
            cad = exp1.codigo3d
            cad += exp2.codigo3d
            cad += nt + '=' + str(exp1.temp) + ' ' + self.operador + ' ' + str(exp2.temp) + '\n'
            self.codigo3d=cad

        return self

    
