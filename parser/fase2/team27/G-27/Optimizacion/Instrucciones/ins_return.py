from Optimizacion.Instrucciones.instruccion import *
class Ins_return(Instruccion):
    def __init__(self, ins, params):
        Instruccion.__init__(self, ins, params)
    
    def execute(self):
        return {'ins': self.ins, 'params': self.params}
    
    def toString(self,tab):
        return '\t'*tab + 'return ' + str(self.params)