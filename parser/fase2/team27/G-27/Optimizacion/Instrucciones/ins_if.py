from Optimizacion.Instrucciones.instruccion import *
from Optimizacion.Asignaciones.asignacion import *
class Ins_if(Instruccion):
    def __init__(self, ins, params, goto):
        Instruccion.__init__(self, ins, params)
        self.goto = goto

    def execute(self):
        return {'ins': self.ins, 'params': self.params, 'goto': self.goto}
    
    def toString(self,tab):
        if isinstance(self.params,Asignacion):
            return '\t'*tab + 'if ' + self.params.toString() + ':\n' + '\t'*(tab+1) + 'goto .' + self.goto
        else:
            return '\t'*tab + 'if ' + self.params+ ':\n' + '\t'*(tab+1) + 'goto .' + self.goto  

    def setGoto(self,goto):
        self.goto = goto
    def getGoto(self):
        return self.goto