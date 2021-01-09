from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
class Returns(InstruccionPL):
    def __init__(self, OperacionLogica, tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.OperacionLogica = OperacionLogica
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        result = self.OperacionLogica.traducir(tabla,arbol)
        arbol.agregarTripleta(0, 'RETURN', 'return', result)
        arbol.agregarGeneral(0, 'RETURN', 'return', result)
        arbol.add3D(['Return',result])
        