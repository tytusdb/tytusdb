from .instruccionAbstracta import InstruccionAbstracta

class funcionCase(InstruccionAbstracta):

    '''Clase que representa un select simple el cual lleva como atributos'''

    def __init__(self, ListadoWhen, SentenciaElse):
        self.ListadoWhen = ListadoWhen
        self.SentenciaElse = SentenciaElse

    def ejecutar(self, tabalSimbolos, listaErrores):
         
        pass  