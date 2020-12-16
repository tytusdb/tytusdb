from Expresion.Binaria import Binaria
from Entorno import Entorno

class Relacional(Binaria):
    def __init__(self, exp1, exp2, operador):
        'Se usan los valores de las clases padres'
        Binaria.__init__(self, exp1, exp2, operador)


    def getval(self,entorno):
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
            elif self.operador == '==':
                self.val = valizq == valder;
            print(self.val)
            return self.val
        except :
             return 'Los tipos que se estan comparando no coinciden'

