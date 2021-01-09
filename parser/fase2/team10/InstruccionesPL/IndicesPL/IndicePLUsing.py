from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class IndicePLUsing(InstruccionPL):
    def __init__(self, nombreIndice, nombreTabla , opracion, nombreCampo,tipo, strGram, linea, columna):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.nombreIndice= nombreIndice
        self.nombreTabla = nombreTabla
        self.opracion = opracion
        self.nombreCampo = nombreCampo 


    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        arbol.setListaIndice(self)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        print('trduccion')