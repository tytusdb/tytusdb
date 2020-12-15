
from .instruccionAbstracta import InstruccionAbstracta

class UpdateTable(InstruccionAbstracta):

    def __init__(self, nombreTabla, listaUpdates, condicion):
        self.nombreTabla = nombreTabla
        self.condicion = condicion
        self.listaUpdates = listaUpdates


    

    def ejecutar(self, tabalSimbolos, listaErrores):
         
        pass   

