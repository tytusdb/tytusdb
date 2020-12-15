from .instruccionAbstracta import InstruccionAbstracta

class InsertTable(InstruccionAbstracta):

    def __init__(self, nombreTabla, listaColumnas = [], listaExpresiones=[], defaultValues = False):
        self.nombreTabla = nombreTabla
        self.listaColumnas = listaColumnas
        self.listaExpresiones = listaExpresiones
        self.defaultValues = defaultValues


    

    def ejecutar(self, tabalSimbolos, listaErrores):
         
        pass   

