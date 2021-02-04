from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
class MoveFrom(InstruccionPL):
    def __init__(self, direction,id, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id =  id
        self.direction = direction

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        print('trduccion')