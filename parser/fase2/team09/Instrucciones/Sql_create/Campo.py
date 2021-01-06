from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Campo(Instruccion):
    def __init__(self, nombre, lower, orden, null, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.nombre = nombre
        self.lower = lower
        self.orden = orden
        self.null = null
        self.existe = False
        self.dupli = False

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)
        restricciones = ""
        if self.lower:
            restricciones = ".lower()"
        else:
            self.lower = None
        self.orden = self.orden.ejecutar(tabla, arbol)
        if self.orden is not None:
            if self.lower is not None:
                restricciones = restricciones + ", "
            else:
                restricciones = restricciones + " "
            restricciones = restricciones + self.orden
        self.null = self.null.ejecutar(tabla, arbol)
        if self.null is not None:
            if self.orden is not None:
                restricciones = restricciones + " "
            elif self.lower is not None:
                restricciones = restricciones + ", "
            else:
                restricciones = restricciones + " "
            restricciones = restricciones + self.null
        return restricciones + "; "
