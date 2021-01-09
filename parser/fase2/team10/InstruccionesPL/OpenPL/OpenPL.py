from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
class OpenPL(InstruccionPL):
    def __init__(self, id, scroll, ContenidoBegin, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id =  id
        self.scroll = scroll
        self.ContenidoBegin = ContenidoBegin

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        print('Pendiente de definir Cursosres : Crear Metodo para realizar acciones')