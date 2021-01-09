from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class IfElse(Instruccion):
    def __init__(self, cond, sent, elss, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.cond = cond
        self.sent = sent
        self.elss = elss

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)

    def traducir(self, tabla, controlador):
        codigo = ''
