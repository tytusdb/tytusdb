from Expresion.Expresion import Expresion
from datetime import date
from datetime import datetime
from Entorno import Entorno

class Terminal(Expresion) :
    '''
        Esta clase representa un terminal.
    '''
    def __init__(self,tipo,valor) :
       Expresion.__init__(self)
       self.tipo=tipo
       self.valor=valor

    def getval(self,entorno):

        if self.tipo=='identificador':
            'buscar columna'

        if self.valor == 'CURRENT_DATE':
            return date.today()
        elif self.valor== 'CURRENT_TIME' or (self.valor=='now' and self.tipo=='timestamp without time zone'):
            return datetime.now()

        return self.valor

