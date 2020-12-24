
from .instruccionAbstracta import InstruccionAbstracta

class DeleteTable(InstruccionAbstracta):

    def __init__(self, nombreTabla, condicion): #nombreColuna > 1
        self.nombreTabla = nombreTabla
        self.condicion = condicion


    

    def ejecutar(self, tabalSimbolos, listaErrores):
         
         


        pass   

