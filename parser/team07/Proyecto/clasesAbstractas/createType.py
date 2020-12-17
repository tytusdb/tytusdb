from .instruccionAbstracta import InstruccionAbstracta

class createType(InstruccionAbstracta):

    def __init__(self, nombre, listaExpresiones=[]):
        self.nombre = nombre
        self.listaExpresiones = listaExpresiones

    

    def ejecutar(self, tabalSimbolos, listaErrores):        
        pass   

