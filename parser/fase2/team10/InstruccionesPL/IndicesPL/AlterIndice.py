from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL
from InstruccionesPL.IndicesPL import IndicePL1,  IndicePL7, IndicePL8, IndicePL9, IndicePLUnique, IndicePLUsing, IndicePLUsingNull
from InstruccionesPL.Expresiones import PrimitivoPL

class AlterIndice(InstruccionPL):
    def __init__(self, nombre, columnaActual, columnaNueva, tipo, linea, columna, strGram ):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)
        self.nombre = nombre
        self.columnaActual = columnaActual
        self.columnaNueva =columnaNueva

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)
        arbol.modificarIndice(self.nombre, self.columnaActual, self.columnaNueva)


    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)