from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class DropPL(InstruccionPL):
    def __init__(self, id, ListId, OpcionDropProcedure, tipo, linea, columna, strGram ):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)
        self.id = id
        self.ListId = ListId
        self.OpcionDropProcedure = OpcionDropProcedure

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)