from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
from InstruccionesPL.TablaSimbolosPL.TipoPL import TipoPL, Tipo_DatoPL
class PrimitivoPL(InstruccionPL):
    def __init__(self, valor, tipo, strGram, linea, columna):
        InstruccionPL.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor
        
    def ejecutar(self):
        print('ejecutar')
        

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        return self.valor