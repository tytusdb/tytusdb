from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Body(Instruccion):
    def __init__(self, declaraciones, sentencias, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.declaraciones = declaraciones
        self.sentencias = sentencias

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)
