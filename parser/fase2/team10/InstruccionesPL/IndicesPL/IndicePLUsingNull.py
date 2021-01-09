from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class IndicePLUsingNull(InstruccionPL):
    def __init__(self, nombreIndice ,nombreTabla , nombreOperacion, orden, OrdenPosicion,tipo, strGram, linea, columna):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.nombreIndice = nombreIndice
        self.nombreTabla = nombreTabla
        self.nombreOperacion = nombreOperacion
        self.orden = orden
        self.OrdenPosicion =OrdenPosicion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion
        arbol.setListaIndice(self)
    def traducir(self, tabla, arbol):
        print('trduccion')