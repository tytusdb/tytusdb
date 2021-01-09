from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class LoopPL(InstruccionPL):
    def __init__(self, InstruccionPL, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.InstruccionPL = InstruccionPL
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        print('trduccion')