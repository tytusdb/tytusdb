from Instrucciones.Excepcion import Excepcion
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Continue(Instruccion):
    def __init__(self, label, condicion, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.label = label
        self.condicion = condicion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)

    def traducir(self, tabla, controlador, arbol):
        self.ejecutar(tabla, arbol)
        codigo = ''
