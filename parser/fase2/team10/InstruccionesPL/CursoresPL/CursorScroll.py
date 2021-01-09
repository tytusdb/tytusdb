from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class CursorScroll(InstruccionPL):
    def __init__(self,id, ListId, cadena , tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id = id
        self.ListId = ListId
        self.cadena =  cadena
        

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)