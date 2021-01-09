from Expresion.Expresion import Expresion
from Entorno import Entorno
from Tipo import Tipo
from Expresion.Terminal import Terminal

class Extract(Expresion):
    'This is an abstract class'

    def __init__(self,field=None,timestamp=None):
        self.field=field
        self.timestamp=timestamp
        self.stringsql = 'EXTRACT( ' + field + ' from timestamp \'' + timestamp + '\') '

    def getval(self,entorno):
        'spliteo el timestamp'
        splited=self.timestamp.split(' ')
        fecha= splited[0]
        hora = splited[1]
        splitedfecha= fecha.split('-')
        splitedhora = hora.split(':')
        if self.field=='year':
            tipo=Tipo('integer',None,-1,-1)
            return Terminal(tipo,splitedfecha[0])
        elif self.field=='month':
            tipo = Tipo('integer', None, -1, -1)
            return Terminal(tipo,splitedfecha[1])
        elif self.field == 'day':
            tipo = Tipo('integer', None, -1, -1)
            return Terminal(tipo,splitedfecha[2])
        elif self.field=='hour':
            tipo = Tipo('integer', None, -1, -1)
            return Terminal(tipo,splitedhora[0])
        elif self.field=='minute':
            tipo = Tipo('integer', None, -1, -1)
            return Terminal(tipo,splitedhora[1])
        elif self.field == 'second':
            tipo = Tipo('integer', None, -1, -1)
            return Terminal(tipo,splitedhora[2])


    def traducir(self,entorno):
        self.temp=self.getval(entorno).valor
        return self