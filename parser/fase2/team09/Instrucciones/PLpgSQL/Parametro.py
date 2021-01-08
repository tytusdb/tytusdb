from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Parametro(Instruccion):
    def __init__(self, nombre, tipo, valor, alias, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.nombre = nombre
        self.tipo = tipo
        self.valor = valor
        self.alias = alias

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)
