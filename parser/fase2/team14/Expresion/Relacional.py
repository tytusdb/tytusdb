from Expresion.Binaria import Binaria

from Expresion.variablesestaticas import *
from Tipo import Tipo
from reportes import *

class Relacional(Binaria):
    def __init__(self, exp1, exp2, operador):
        'Se usan los valores de las clases padres'
        Binaria.__init__(self, exp1, exp2, operador)
        self.exp1 = exp1
        self.exp2 = exp2




    def getval(self, entorno):

        valizq = self.exp1.getval(entorno)
        valder = self.exp2.getval(entorno)
        if valizq == None or valder == None:
            return self

        valizq = valizq.valor
        valder = valder.valor

        try:
            if self.operador == '>':
                self.valor = valizq > valder
            elif self.operador == '<':
                self.valor = valizq < valder
            elif self.operador == '>=':
                self.valor = valizq >= valder
            elif self.operador == '<=':
                self.valor = valizq <= valder
            elif self.operador == '<>':
                self.valor = valizq != valder
            elif self.operador == '=':
                self.valor = valizq == valder
            elif self.operador == 'like':
                self.valor = self.like(valizq, valder)
            elif self.operador == 'ilike':
                self.valor = self.ilike(valizq, valder)

            self.tipo = 'boolean'
            return self
        except:
            reporteerrores.append(Lerrores("Error Semantico",
                                           'Los tipos que se estan comparando no coinciden',
                                           0, 0))
            variables.consola.insert(INSERT,
                                     'Los tipos que se estan comparando no coinciden\n')
            return

    def like(self, valizq, valder):
        valorder = valder.replace('%', '')
        if valorder in valizq:
            return True
        return False

    def ilike(self, valizq, valder):
        valizq = valizq.lower()
        valder = valder.lower()
        return self.like(valizq, valder)

    def traducir(self, entorno):
        exp1 = self.exp1.traducir(entorno)
        exp2 = self.exp2.traducir(entorno)
        if (self.operador == 'not like'):
            stringsql = exp1.stringsql + ' '
            stringsql +=' not like '
            stringsql += exp2.stringsql
            if self.stringsql == '()':
                self.stringsql = '(' + stringsql + ')'
            else:
                self.stringsql = stringsql
        else:
            stringsql = exp1.stringsql + ' '
            stringsql += ' '+self.operador+' '
            stringsql += exp2.stringsql
            if self.stringsql == '()':
                self.stringsql = '(' + stringsql + ')'
            else:
                self.stringsql = stringsql
        #------------------------------------------------------------------------------------------------------------
        if self.operador == '<>':
            self.operador = '!='
        if self.operador == '=':
            self.operador = '=='


        self.temp = entorno.newtemp()
        nt = self.temp

        cad = exp1.codigo3d
        cad += exp2.codigo3d
        cad += nt + '=' + str(exp1.temp) + ' ' + self.operador + ' ' + str(exp2.temp) + '\n'
        self.codigo3d = cad


        return self