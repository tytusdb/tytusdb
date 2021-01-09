from InstruccionesPL.TablaSimbolosPL.TipoPL import  TipoPL, Tipo_DatoPL
from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class InOutIdentificador(InstruccionPL):
    def __init__(self, id,tipo, strGram, linea, columna):
        InstruccionPL.__init__(self,TipoPL(Tipo_DatoPL.ID), linea, columna,strGram)
        self.id = id
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        print('trduccion')