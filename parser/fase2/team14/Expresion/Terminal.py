from Expresion.Expresion import Expresion
from datetime import date
from datetime import datetime
from Entorno import Entorno
import random as rn
from Tipo import  Tipo
import math

class Terminal(Expresion) :
    '''
        Esta clase representa un terminal.
    '''
    def __init__(self,tipo,valor) :
       Expresion.__init__(self)
       self.tipo=tipo
       self.valor=valor


    def getval(self,entorno):

        if self.tipo.tipo=='identificador':
            'buscar columna'

        if self.valor == 'CURRENT_DATE':
            self.tipo = Tipo('date', None, -1, -1)
            self.valor=str(date.today())
            return self
        elif self.valor == 'CURRENT_TIME':
            'retornar solo  la hora'
            now = datetime.now()
            self.tipo=Tipo('time without time zone',None,-1,-1)
            self.valor=str(now.hour)
            return self
        elif self.valor=='now' and self.tipo.tipo=='timestamp without time zone':
            self.valor=str(datetime.now())
            return self


        elif(self.valor=='random'):
                value = rn.uniform(0,1)
                self.tipo=Tipo('double',None,-1,-1)
                self.valor= value
                return self
        elif (self.valor=="pi"):

                self.valor =math.pi
                self.tipo = Tipo('numeric', None, len(str(self.valor)), -1)
                return self
        else:
            if str(self.valor).count('-')==2 and str(self.valor).count(':')==2:
                if len(str(self.valor))>10:
                    self.tipo = Tipo('timestamp without time zone', None, -1, -1)
            elif str(self.valor).count('-')==2:
                if len(str(self.valor))==10:
                    self.tipo=Tipo('date',None,-1,-1)
            elif str(self.valor).count(':') == 2:
                if len(str(self.valor)) >= 8:
                    self.tipo = Tipo('time without time zone', None, -1, -1)
            return self

    def traducir(self,entorno):

        self.temp=self.getval(entorno).valor
        if self.tipo.tipo=='varchar':
            self.temp='\''+self.temp+'\''

        if str(self.temp).lower()=='true':
            self.temp='1'
        elif str(self.temp).lower()=='false':
            self.temp='0'
        return self
