from .instruccionAbstracta import InstruccionAbstracta

class dropDatabase(InstruccionAbstracta):

    def __init__(self, nombre):
        self.nombre = nombre
    

    def ejecutar(self, tabalSimbolos, listaErrores):        
        pass   