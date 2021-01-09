from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class IndicePL(InstruccionPL):
    def __init__(self, id,id1 , id2,id3,descs,orindice,claseoperador,tipo, strGram, linea, columna):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id = id
        self.id1 = id1
        self.id2 = id2
        self.id3 = id3 
        self.descs = descs
        self.orindice = orindice
        self.claseoperador = claseoperador
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        print('trduccion')