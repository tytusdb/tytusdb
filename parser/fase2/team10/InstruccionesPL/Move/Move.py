from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
class Move(InstruccionPL):
    def __init__(self,id, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id =  id
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        print('Move _> pendiente de considerar : Crear MEtodo')