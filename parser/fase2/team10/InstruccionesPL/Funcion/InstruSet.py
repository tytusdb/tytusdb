from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class InstruSet(InstruccionPL):
    def __init__(self, operacionlogica ,tipo, strGram, linea, columna):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.operacionlogica = operacionlogica
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        print('trduccion')