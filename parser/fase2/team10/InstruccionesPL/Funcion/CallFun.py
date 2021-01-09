from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class CallFun(InstruccionPL):
    def __init__(self, id , op,tipo, strGram, linea, columna):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id = id
        self.op = op
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        print('trduccion')