from Instrucciones.Excepcion import Excepcion
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Asignacion(Instruccion):
    def __init__(self, nombre, expresion, query, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.nombre = nombre
        self.expresion = expresion
        self.query = query

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)

    def traducir(self, tabla, controlador, arbol):
        self.ejecutar(tabla, arbol)
        codigo = ''
