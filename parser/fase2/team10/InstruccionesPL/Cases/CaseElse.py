from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
from InstruccionesPL.Ends import Ends

class CaseElse(InstruccionPL):
    def __init__(self, InstruccionPL12, ContCase, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.InstruccionPL12 = InstruccionPL12
        self.ContCase = ContCase

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        if type(self.InstruccionPL12)==list:
            if self.InstruccionPL12!=None:
                for ins in self.InstruccionPL12:
                    ins.traducir(tabla,arbol)

        if (isinstance(self.ContCase, Ends.Ends) == False) and (self.ContCase!=None):         
            res = self.ContCase.traducir(tabla, arbol)
       
                