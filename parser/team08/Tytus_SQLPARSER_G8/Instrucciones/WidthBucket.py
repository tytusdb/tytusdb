from Instruccion import Instruccion

class WidthBucket(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))

instruccion = WidthBucket("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)