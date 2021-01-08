from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Execute(Instruccion):
    def __init__(self, nombre, parametros, strGram, linea, columna):
        self.nombre = nombre
        self.parametros = parametros

    def ejecutar(self, tabla, arbol):
        print("Execute", self.nombre, self.parametros)
