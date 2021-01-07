from Optimizacion.Instrucciones.instruccion import Instruccion
class Funcion(Instruccion):
    def __init__(self, ins, params, func):
        Instruccion.__init__(self, ins, params)
        self.func = func

    def execute(self):
        return {'ins': self.ins, 'params': self.params, 'func': self.func}


print('funcion')
