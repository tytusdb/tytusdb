from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
class IndicePLUnique(InstruccionPL):
    def __init__(self, nombreIndice, nombreTabla, columnas,tipo, strGram, linea, columna):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.nombreIndice = nombreIndice
        self.nombreTabla = nombreTabla
        self.columnas = columnas
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion
        arbol.setListaIndice(self)

    def traducir(self, tabla, arbol):
        print('trduccion')