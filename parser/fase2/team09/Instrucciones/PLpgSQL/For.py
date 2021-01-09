from Instrucciones.Excepcion import Excepcion
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.PLpgSQL import Exit

class For(Instruccion):
    def __init__(self, indice, reverse, rango, cambio, sentencias, label, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.indice = indice
        self.reverse = reverse
        self.rango = rango
        self.cambio = cambio
        self.sentencias = sentencias
        self.label = label

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)
        if self.label is not None:
            if self.label[0] == self.label[1]:
                self.label = (self.label[0])[2:-2]
            else:
                error = Excepcion("FOR00", "Semántico", "Los labels de inicio y fin no coinciden.", self.linea, self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
        mayor = 0
        menor = 0
        if self.reverse:
            mayor = self.rango[0]
            menor = self.rango[1]
        else:
            menor = self.rango[0]
            mayor = self.rango[1]
        if menor > mayor:
            error = Excepcion("FOR01", "Semántico", "Error en el orden de los índices (rango invertido).", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
        if self.cambio < 1:
            error = Excepcion("FOR02", "Semántico", "Error en el cambio del índice (cláusula BY).", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
        for s in self.sentencias:
            if isinstance(s, Exit):
                if s.label is not None and self.label != s.label:
                    error = Excepcion("FOR03", "Semántico", "El label de Exit no coincide con el del For.", s.linea, s.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())

    def traducir(self, tabla, controlador, arbol):
        self.ejecutar(tabla, arbol)
        codigo = ''
