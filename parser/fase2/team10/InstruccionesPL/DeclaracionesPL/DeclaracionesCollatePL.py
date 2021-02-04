from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class DeclaracionesCollatePL(InstruccionPL):
    def __init__(self, id, Tipo,constant, tipo, id2, OperacionLogica, linea, columna, strGram ):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id = id
        self.Tipo = Tipo
        self.id2 = id2
        self.constant = constant
        self.OperacionLogica = OperacionLogica
        


    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)


    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)