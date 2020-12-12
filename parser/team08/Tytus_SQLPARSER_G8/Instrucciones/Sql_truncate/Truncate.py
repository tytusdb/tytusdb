from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Truncate(Instruccion):
    def __init__(self, id, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = id

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))
'''
instruccion = DropDatabase("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''