from Expresion.Binaria import Binaria
from Entorno import Entorno

class Relacional(Binaria):
    def __init__(self, exp1, exp2, operador):
        'Se usan los valores de las clases padres'
        Binaria.__init__(self, exp1, exp2, operador)


    def getval(self,entorno):
        if (self.exp1.tipo.tipo == 'identificador' or self.exp2.tipo.tipo == 'identificador'):
            return self

        valizq = self.exp1.getval(entorno);
        valder = self.exp2.getval(entorno);
        try:
            if self.operador == '>':
                self.val = valizq > valder;
            elif self.operador == '<':
                self.val = valizq < valder;
            elif self.operador == '>=':
                self.val = valizq >= valder;
            elif self.operador == '<=':
                self.val = valizq <= valder;
            elif self.operador == '<>':
                self.val = valizq != valder;
            elif self.operador == '=':
                self.val = valizq == valder;

            self.tipo = 'boolean'
            return self.val
        except :
             return 'Los tipos que se estan comparando no coinciden'


