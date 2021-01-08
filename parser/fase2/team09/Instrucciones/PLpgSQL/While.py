from Instrucciones.Excepcion import Excepcion
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.PLpgSQL import Exit

class While():
    def __init__(self, condicion, sentencias, label, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.condicion = condicion
        self.sentencias = sentencias
        self.label = label

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)
        if self.label is not None:
            if self.label[0] == self.label[1]:
                self.label = (self.label[0])[2:-2]
            else:
                error = Excepcion("WHL00", "Semántico", "Los labels de inicio y fin no coinciden.", self.linea, self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return
        for s in self.sentencias:
            if isinstance(s, Exit):
                if s.label is not None and self.label != s.label:
                    error = Excepcion("WHL01", "Semántico", "El label de Exit no coincide con el del While.", s.linea, s.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())

    def traducir(self, tabla, controlador, arbol):
        self.ejecutar(tabla, arbol)
        codigo = ''
