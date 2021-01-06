from Expresion.Binaria import Binaria
from Expresion.Aritmetica import Aritmetica
from Expresion.Unaria import Unaria
from Expresion.Aritmetica import Aritmetica
from Expresion.Logica import Logica
from Expresion.FuncionesNativas import  FuncionesNativas
from Entorno import Entorno
from Tipo import Tipo
from Expresion.Id import Identificador
from tkinter import *
from Expresion.variablesestaticas import *
from reportes import *

class Relacional(Binaria):
    def __init__(self, exp1, exp2, operador):
        'Se usan los valores de las clases padres'
        Binaria.__init__(self, exp1, exp2, operador)
        self.exp1=exp1
        self.exp2=exp2
        if(self.operador=='not like'):
            self.stringsql+=exp1.stringsql+' not like ' +exp2.stringsql
            self.operador= 'like'
            operador='like'
        else:
            self.stringsql+=exp1.stringsql+' ' 
            self.stringsql+= operador+' '
            self.stringsql +=  exp2.stringsql
        



    def getval(self,entorno):
        if isinstance(self.exp1,Identificador) and isinstance(self.exp2,Identificador):
            return self


        valizq=self.exp1.getval(entorno)
        valder=self.exp2.getval(entorno)
        valizq=valizq.valor
        valder=valder.valor

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
            elif self.operador=='like':
                self.valor=self.like(valizq,valder)
            elif self.operador=='ilike':
                 self.valor=self.ilike(valizq,valder)

            self.tipo = 'boolean'
            return self
        except :
            reporteerrores.append(Lerrores("Error Semantico",
                                           'Los tipos que se estan comparando no coinciden',
                                           0, 0))
            variables.consola.insert(INSERT,
                                     'Los tipos que se estan comparando no coinciden\n')
            return

    def like(self,valizq,valder):
        valorder=valder.replace('%','')
        if valorder in valizq:
            return True
        return False

    def ilike(self, valizq, valder):
        valizq=valizq.lower()
        valder=valder.lower()
        return self.like(valizq,valder)

    def traducir(self,entorno):
        if self.operador=='<>':
            self.operador='!='
        if self.operador=='=':
            self.operador='=='
        self.temp = entorno.newtemp()
        nt=self.temp
        exp1=self.exp1.traducir(entorno)
        exp2=self.exp2.traducir(entorno)
        cad = exp1.codigo3d
        cad += exp2.codigo3d
        cad += nt + '=' + str(exp1.temp) + ' ' + self.operador + ' ' + str(exp2.temp) + '\n'
        self.codigo3d=cad

        return self
