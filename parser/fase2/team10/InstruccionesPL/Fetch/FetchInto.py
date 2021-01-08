from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
class FetchInto(InstruccionPL):
    def __init__(self, id, ListId, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id =  id
        self.ListId = ListId
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        print('Fetch _> pendiente de considerar : Crear MEtodo')