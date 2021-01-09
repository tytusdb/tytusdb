from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
class ReturnsNext(InstruccionPL):
    def __init__(self, OperacionLogica, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.OperacionLogica = OperacionLogica
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        print('trduccion')