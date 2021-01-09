from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class DeclaracionesPL(InstruccionPL):
    def __init__(self, id, Tipo, tipo, linea, columna, strGram ):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id = id
        self.Tipo = Tipo


    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)


    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        
