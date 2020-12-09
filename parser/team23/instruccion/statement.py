from abstract.instruccion import *
from tools.environment import *

class statement_(instruccion):
    def __init__(self, instrucciones, line, column):
        super().__init__(line, column)
        self.instrucciones = instrucciones

    def ejecutar(self, ambiente):
        try:
            nuevo_entorno = environment(ambiente)

            for instruccion_ in self.instrucciones:
                instruccion_.ejecutar(ambiente)
        except:
           print("error statement")