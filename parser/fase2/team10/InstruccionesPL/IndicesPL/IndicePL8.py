from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class IndicePL8(InstruccionPL):
    def __init__(self, nombreIndice, nombreTabla, nombreCampo, operacionlogica,tipo, strGram, linea, columna):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.nombreIndice = nombreIndice
        self.nombreTabla = nombreTabla
        self.nombreCampo = nombreCampo
        self.operacionlogica = operacionlogica
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        arbol.setListaIndice(self)
 
    def traducir(self, tabla, arbol):
        print('trduccion')