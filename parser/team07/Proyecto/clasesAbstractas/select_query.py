from .instruccionAbstracta import InstruccionAbstracta

class select_query(InstruccionAbstracta):

    '''Esta es la instruccion general de un query que puede unir varios select
    esta tiene los 2 querys que se unen y el tipo de union'''

    def __init__(self, query1, query2, tipoUnion):
        self.query1 = query1
        self.query2 = query2
        self.tipoUnion = tipoUnion


    def ejecutar(self, tabalSimbolos, listaErrores):    
        if self.query2 is None:
            self.query1.ejecutar(tabalSimbolos, listaErrores)
        else:
            print("Vienen 2 querys")
        pass 

