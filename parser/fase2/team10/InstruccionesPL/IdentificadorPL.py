from InstruccionesPL.TablaSimbolosPL.TipoPL import  TipoPL, Tipo_DatoPL
from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class IdentificadorPL(InstruccionPL):
    def __init__(self, id, strGram, linea, columna):
        InstruccionPL.__init__(self,TipoPL(Tipo_DatoPL.ID), linea, columna,strGram)
        self.id = id
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)
        print('aca sebe de ejecutarse')

    def traducir(self, tabla, arbol):
        super().traducir(tabla,arbol)
       
        return self.id






