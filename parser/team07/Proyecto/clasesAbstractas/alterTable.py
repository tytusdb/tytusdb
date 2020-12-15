from .instruccionAbstracta import InstruccionAbstracta

class alterTable(InstruccionAbstracta):

    def __init__(self, nombre, instrucciones = []):
        self.nombre = nombre
        self.instrucciones = instrucciones
    

    def ejecutar(self, tabalSimbolos, listaErrores):        
        pass   