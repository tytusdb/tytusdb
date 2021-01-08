from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Variable(Instruccion):
    def __init__(self, nombre, const, tipo, nulo, valor, alias, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.nombre = nombre
        self.const = const
        self.tipo = tipo
        self.nulo = nulo
        self.valor = valor
        self.alias = alias

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)
