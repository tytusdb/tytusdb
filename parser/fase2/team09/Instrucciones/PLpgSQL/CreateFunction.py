from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class CreateFunction(Instruccion):
    def __init__(self, nombre, tipo, parametros, declaraciones, instrucciones, strGram, linea, columna):
        Instruccion.__init__(self, tipo, linea, columna, strGram)
        self.nombre = nombre
        self.parametros = parametros
        self.declaraciones = declaraciones
        self.instrucciones = instrucciones

    def ejecutar(self, tabla, arbol):
        #super().ejecutar(tabla,arbol)
        #Aqui vamos a guardar la funcion
        tabla.setFuncion(self)

'''
instruccion = CreateFunction("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''