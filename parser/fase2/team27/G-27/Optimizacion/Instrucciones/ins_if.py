from Optimizacion.Instrucciones.instruccion import *
class Ins_if(Instruccion):
    def __init__(self, ins, params, goto):
        Instruccion.__init__(self, ins, params)
        self.goto = goto

    def execute(self):
        return {'ins': self.ins, 'params': self.params, 'goto': self.goto}