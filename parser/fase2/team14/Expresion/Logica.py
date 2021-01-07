from Expresion.Binaria import Binaria
from Entorno import Entorno
from Expresion.Terminal import Terminal
from Expresion.Id import Identificador
from tkinter import *
from Expresion.variablesestaticas import *
from reportes import *

class Logica(Binaria):
    def __init__(self, exp1, exp2, operador):
        'Se usan los valores de las clases padres'
        Binaria.__init__(self, exp1, exp2, operador)
        self.operador =operador
        self.exp2=exp2
        self.exp1=exp1

        self.stringsql +=exp1.stringsql+ ' '
        self.stringsql+= operador +' ' 
        self.stringsql += exp2.stringsql

        



    def getval(self, entorno):
        if isinstance(self.exp1, Identificador) and isinstance(self.exp2, Identificador):
            return self

        valizq=self.exp1.getval(entorno)
        valder=self.exp2.getval(entorno)
        valizq=valizq.valor
        valder=valder.valor

        if str(valizq).lower() not in('true','false') or str(valder).lower() not in('true','false') :
            reporteerrores.append(Lerrores("Error Semantico",
                                           'Error los operandos deben ser booleanos \n',
                                           0, 0))
            variables.consola.insert(INSERT,
                                     'Error los operandos deben ser booleanos \n')

            return

        if self.operador == 'and':
            self.valor = valizq and valder;
        elif self.operador == 'or':
            self.valor = valizq or valder;

        self.tipo='boolean'
        return self

    def traducir(self,entorno):
        self.temp = entorno.newtemp()
        nt=self.temp
        exp1=self.exp1.traducir(entorno)
        exp2=self.exp2.traducir(entorno)
        cad = exp1.codigo3d
        cad += exp2.codigo3d
        cad += nt + '=' + str(exp1.temp) + ' ' + self.operador + ' ' + str(exp2.temp) + '\n'
        self.codigo3d=cad

        return self

