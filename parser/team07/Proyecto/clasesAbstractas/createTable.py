from .instruccionAbstracta import InstruccionAbstracta

class createTable(InstruccionAbstracta):
    '''
        Esta clase representa la instrucción crear tabla.
        La instrucción crear tabla tiene un ID y una lista de columnas y una posible herencia de otra tabla
    '''
    def __init__(self, identificador, herencia, columnas=[]):
        self.identificador = identificador
        self.columnas = columnas
        self.herencia = herencia


    def ejecutar(self, tabalSimbolos, listaErrores):        
        pass 
