from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Llamada(Instruccion):
    def __init__(self, nombre, parametros, strGram, linea, columna):
        self.nombre = nombre
        self.parametros = parametros

    def ejecutar(self, tabla, arbol):
        print("Llamada", self.nombre, self.parametros)
