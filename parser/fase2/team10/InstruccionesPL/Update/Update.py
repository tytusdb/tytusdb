from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
class Upadte(InstruccionPL):
    def __init__(self, id, InstruSet, currentId, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.id =  id
        self.Instruset = InstruSet
        self.currentId = currentId
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        print('Update _> pendiente de considerar : Crear MEtodo')