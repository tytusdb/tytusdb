from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Undefined(Instruccion):
    def __init__(self, tipo, valor, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.tipo = tipo
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)
        if self.valor != None:
            self.valor = self.tipo + self.valor
        return self.valor

    def traducir(self, tabla, controlador, arbol):
        codigo = 'Undefined.Undefined("' + self.tipo + '", '
        if self.valor is None:
            codigo += 'None'
        else:
            codigo += '"' + self.valor + '"'
        codigo += ', "' + self.strGram + '", ' + str(self.linea) + ', ' + str(self.columna) + ')'
        return codigo
