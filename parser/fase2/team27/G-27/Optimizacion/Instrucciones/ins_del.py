from Optimizacion.Instrucciones.instruccion import *
class Ins_Del(Instruccion):
    def __init__(self, func, params):
        Instruccion.__init__(self, func, params)
    
    def execute(self):
        return {'ins': self.ins, 'params': self.params}

    def toString(self,tab):
        return '\n'+'\t'*tab +'del ' + self.params