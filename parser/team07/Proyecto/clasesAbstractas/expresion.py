from .instruccionAbstracta import InstruccionAbstracta



class Expresion(InstruccionAbstracta):


    def __init__(self):   
        pass

    def valorPrimitivo(self,valor,tipo):
        self.valor = valor
        self.tipoOperacion = tipo
        self.opIzquierdo = None
        self.opDerecho = None
    
    def operacionUnaria(self,opIzquierdo,tipoOperacion):
        self.valor = None
        self.tipoOperacion = tipoOperacion
        self.opIzquierdo = opIzquierdo
        self.opDerecho = None
    
    def operacionBinaria(self,opIzquierdo,opDerecho,tipoOperacion):
        self.valor = None
        self.tipoOperacion = tipoOperacion
        self.opIzquierdo = opIzquierdo
        self.opDerecho = opDerecho   
    

    def ejecutar(self, tabalSimbolos, listaErrores):
         
        pass   

