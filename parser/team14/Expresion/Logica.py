from Expresion.Binaria import Binaria
from Entorno import Entorno
from Expresion.Terminal import Terminal
from tkinter import *
from Expresion.variablesestaticas import *
from reportes import *

class Logica(Binaria):
    def __init__(self, exp1, exp2, operador):
        'Se usan los valores de las clases padres'
        Binaria.__init__(self, exp1, exp2, operador)


    def getval(self, entorno):
        if (self.exp1.tipo.tipo == 'identificador' or self.exp2.tipo.tipo == 'identificador'):
            return self

        valizq = self.exp1.getval(entorno);
        valder = self.exp2.getval(entorno);
        if (isinstance(valizq, Terminal)):
            valizq = valizq.getval(entorno)
        if (isinstance(valder, Terminal)):
            valder = valder.getval(entorno)

        if valizq not in('true','false') or valder not in('true','false') :
            reporteerrores.append(Lerrores("Error Semantico",
                                           'Error los operandos deben ser booleanos \n',
                                           0, 0))
            variables.consola.insert(INSERT,
                                     'Error los operandos deben ser booleanos \n')

            return

        if self.operador == 'and':
            self.val = valizq and valder;
        elif self.operador == 'or':
            self.val = valizq or valder;

        self.tipo='boolean'
        return self.val
