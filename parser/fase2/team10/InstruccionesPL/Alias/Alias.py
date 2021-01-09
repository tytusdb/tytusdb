from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class Alias(InstruccionPL):
    def __init__(self, id,id2 ,tipo ,lineas, columna, strGram):
        InstruccionPL.__init__(self, tipo, lineas, columna, strGram)        
        self.id =  id
        self.id2 = id2
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        print('Alias _> pendiente de considerar : Crear MEtodo')

    