from .instruccionAbstracta import InstruccionAbstracta

class createDatabase(InstruccionAbstracta):
    '''
        Esta clase representa la instrucción crear database.
        La instrucción crear database tiene un ID y una posible lista de owner y mode
    '''
    def __init__(self, identificador, opciones=[]):
        self.identificador = identificador
        self.opciones = opciones


    def ejecutar(self, tabalSimbolos, listaErrores):        
        pass 