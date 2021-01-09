from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
class UpadteOper(InstruccionPL):
    def __init__(self, id, InstruSet, OperacionLogica, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id =  id
        self.InstruSet = InstruSet
        self.OperacionLogica = OperacionLogica
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        print('UpdateOper _> pendiente de considerar : Crear MEtodo')