
from .instruccionAbstracta import InstruccionAbstracta

class UpdateColumna(InstruccionAbstracta):

    def __init__(self, nombreColumna, valorActualizar):
        self.nombreColumna = nombreColumna
        self.valorActualizar = valorActualizar


    

    def ejecutar(self, tabalSimbolos, listaErrores):
         
        pass   

