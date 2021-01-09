from Expresion.Expresion import Expresion
from Expresion.Terminal import Terminal
from Expresion.Id import Identificador
from Entorno import Entorno

class Unaria(Expresion) :
    '''
        Esta clase representa la Expresión Binaria.
        Esta clase recibe los operandos y el operador
    '''
    def __init__(self, exp1,operador) :
        Expresion.__init__(self)
        self.exp1 = exp1
        self.operador = operador



    def getval(self,entorno):

        valexp=self.exp1.getval(entorno)
        if valexp == None:
            return self

        valexp=valexp.valor
        if isinstance(valexp, Terminal):
            valexp = valexp.getval(entorno)

        if self.operador == '+':
            self.tipo=self.exp1.tipo
            self.tipo= valexp
        elif self.operador == '-':
            self.tipo=self.exp1.tipo
            self.valor = valexp*-1
        elif self.operador == 'not':
            self.tipo='boolean'
            self.valor =  not valexp


        return self


    def traducir(self,entorno):
        self.temp = entorno.newtemp()
        nt=self.temp
        exp1=self.exp1.traducir(entorno)
        cad = exp1.codigo3d
        cad += nt + '='  + self.operador + ' ' + str(exp1.temp) + '\n'
        self.codigo3d=cad

        stringsql = self.operador+' ' +str(exp1.stringsql) +' '
        if self.stringsql == '()':
            self.stringsql = '(' + stringsql + ')'
        else:
            self.stringsql = stringsql

        return self