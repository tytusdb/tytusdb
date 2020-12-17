from .instruccionAbstracta import InstruccionAbstracta

class dropTable(InstruccionAbstracta):

    def __init__(self, nombre):
        self.nombre = nombre
    

    def ejecutar(self, tabalSimbolos, listaErrores):        
        pass   