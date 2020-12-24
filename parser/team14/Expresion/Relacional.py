from Expresion.Binaria import Binaria
from Expresion.Aritmetica import Aritmetica
from Expresion.Unaria import Unaria
from Expresion.Aritmetica import Aritmetica
from Expresion.Logica import Logica
from Expresion.FuncionesNativas import  FuncionesNativas
from Entorno import Entorno
from Tipo import Tipo
from Expresion.Terminal import Terminal
from tkinter import *
from Expresion.variablesestaticas import *
from reportes import *

class Relacional(Binaria):
    def __init__(self, exp1, exp2, operador):
        'Se usan los valores de las clases padres'
        Binaria.__init__(self, exp1, exp2, operador)


    def getval(self,entorno):
        if isinstance(self.exp1,Terminal) and isinstance(self.exp2,Terminal):
            if (self.exp1.tipo.tipo == 'identificador' or self.exp2.tipo.tipo == 'identificador'):
                return self

        valizq=self.exp1.getval(entorno);
        valder=self.exp2.getval(entorno);
        valizq=valizq.valor
        valder=valder.valor

        try:
            if self.operador == '>':
                self.valor = valizq > valder;
            elif self.operador == '<':
                self.valor = valizq < valder;
            elif self.operador == '>=':
                self.valor = valizq >= valder;
            elif self.operador == '<=':
                self.valor = valizq <= valder;
            elif self.operador == '<>':
                self.valor = valizq != valder;
            elif self.operador == '=':
                self.valor = valizq == valder;

            self.tipo = 'boolean'
            return self
        except :
            reporteerrores.append(Lerrores("Error Semantico",
                                           'Los tipos que se estan comparando no coinciden',
                                           0, 0))
            variables.consola.insert(INSERT,
                                     'Los tipos que se estan comparando no coinciden\n')
            return

