from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class Exits(InstruccionPL):
    def __init__(self, ContInstru, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.ContInstru = ContInstru
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)