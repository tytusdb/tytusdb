from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class DropIndiceIf(InstruccionPL):
    def __init__(self, nombre, opcionDropProcedure, tipo, linea, columna, strGram ):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)
        self.nombre = nombre
        self.opcionDropProcedure = opcionDropProcedure

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)
        if isinstance(self.nombre, str):
            arbol.eliminarIndice(nombre)
        else:
            for id in self.nombre:
                arbol.eliminarIndice(id.id)

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)