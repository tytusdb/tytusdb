from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class VariablePL(InstruccionPL):
    def __init__(self, id, Tipo, tipo, linea, columna, strGram ):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)
        self.id = id
        self.Tipo = Tipo

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)

        val = self.Tipo.traducir(tabla,arbol)
        res = '{0} = {1} \n'.format(self.id, val)

        arbol.add3D([self.id, 0])
        arbol.agregarTripleta(0, '=', self.id, val)
        arbol.agregarGeneral(0, '=', self.id, val)
            
        return res