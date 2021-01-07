from Optimizacion.Instrucciones.instruccion import *
class Ins_parse(Instruccion):
    def __init__(self, func, params):
        Instruccion.__init__(self, func, params)
    
    def execute(self):
        return {'fun': Instruccion.func, 'params': self.params, 'ins': self.ins}