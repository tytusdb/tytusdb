
from Instrucciones.Instruccion import Instruccion

class Return(Instruccion):
    def __init__(self,exp):
        self.exp=exp

    def ejecutar(self, ent):
        'ejecutar return'
        return self.exp.getval(ent)

    def traducir(self, ent):
        'ejecutar return'
        self.codigo3d='stack[0]= '+self.exp.traducir(ent).temp +'\n'
        self.stringsql = 'return ' + self.exp.stringsql+';'
        return self
