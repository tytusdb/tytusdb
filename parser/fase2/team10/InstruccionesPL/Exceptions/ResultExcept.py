from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class ResultExcept(InstruccionPL):
    def __init__(self, cadenacaracter, id, tipo,  linea, columna, strGram ):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.cadenacaracter = cadenacaracter
        self.id = id
        

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)

        arbol.agregarTripleta(0, 'Exception', self.cadenacaracter, self.id)
        arbol.agregarGeneral(0, 'Exception', self.cadenacaracter, self.id)
        arbol.add3D(['Exception', self.cadenacaracter])