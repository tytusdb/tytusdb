from .instruccionAbstracta import InstruccionAbstracta

class columnaCampoAlias(InstruccionAbstracta):

    '''Declaracion de referencia a una tabla con su campo y un alias'''

    def __init__(self, Tabla, Campo, Alias):
        self.Tabla = Tabla
        self.Campo = Campo
        self.Alias = Alias

    def ejecutar(self, tabalSimbolos, listaErrores):        
        pass 

