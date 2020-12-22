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
            return str(date.today())
        elif self.valor== 'CURRENT_TIME':
            'retornar solo  la hora'
            now = datetime.now()
            return str(now.hour)
        elif self.valor=='now' and self.tipo.tipo=='timestamp without time zone':
            return str(datetime.now())

        elif(self.valor=='random'):
                value = rn.uniform(0,1)
                return value
        elif (self.valor=="pi"):
                return math.pi
        else:
            if str(self.valor).count('-')==2 and self.valor.count(':')==2:
                if len(str(self.valor))>10:
                    self.tipo = Tipo('timestamp without time zone', None, -1, -1)
            elif str(self.valor).count('-')==2:
                if len(str(self.valor))==10:
                    self.tipo=Tipo('date',None,-1,-1)
            elif str(self.valor).count(':') == 2:
                if len(str(self.valor)) >= 8:
                    self.tipo = Tipo('time without time zone', None, -1, -1)
            return self.valor