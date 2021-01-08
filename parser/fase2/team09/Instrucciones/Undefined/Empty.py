from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Empty(Instruccion):
    def __init__(self, tipo, valor, strGram, linea, columna):
        self.valor = None

    def ejecutar(self, tabla, arbol):
        return None
