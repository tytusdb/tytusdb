from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class CaseWhen(Instruccion):
    def __init__(self, when, sent, othe, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.when = when
        self.sent = sent
        self.othe = othe

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)

    def traducir(self, tabla, controlador):
        codigo = ''