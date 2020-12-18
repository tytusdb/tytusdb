from .instruccionAbstracta import InstruccionAbstracta

class selectSimple(InstruccionAbstracta):

    '''Clase que representa un select simple el cual lleva como atributos'''

    def __init__(self, selectColumnas, selectTablas, selectCondiciones):
        self.selectColumnas = selectColumnas
        self.selectTablas = selectTablas
        self.selectCondiciones = selectCondiciones


    def ejecutar(self, tabalSimbolos, listaErrores):        
        pass 

