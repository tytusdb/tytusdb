
from .instruccionAbstracta import InstruccionAbstracta

class   BetweenIn(InstruccionAbstracta):

    def __init__(self):
        self.valorComparar = None
        self.valorInicio = None
        self.valorFin = None
        self.listaIn = None
        self.tipoOperacion = None
        self.subQuery = None

    def between(self,valorCom,valInicio,valFin,tipoOp):
        self.valorComparar = valorCom
        self.valorInicio = valInicio
        self.valorFin = valFin
        self.tipoOperacion = tipoOp
    

    def inn(self,valorCom,listaIn,tipoOp):
        self.valorComparar = valorCom
        self.listaIn = listaIn
        self.tipoOperacion = tipoOp
    
    def innSubquery(self,valorCom,subquery,tipoOp):
        self.valorComparar = valorCom
        self.subQuery = subquery
        self.tipoOperacion = tipoOp

    

    def ejecutar(self, tabalSimbolos, listaErrores):
         

        pass   

