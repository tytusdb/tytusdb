from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
from InstruccionesPL.Ends import Ends
class Elses(InstruccionPL):
    def __init__(self,InstrucionesPL, ContIf, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.InstruccionesPL = InstrucionesPL
        self.ContIf = ContIf

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        res = ''
        if type(self.InstruccionesPL)== list:
            if self.InstruccionesPL!=None:
                for ins in self.InstruccionesPL:
                    ins.traducir(tabla, arbol)
        
        if isinstance(self.ContIf, Ends.Ends) == False:
            res = self.ContIf.traducir(tabla, arbol)
       
        return res

