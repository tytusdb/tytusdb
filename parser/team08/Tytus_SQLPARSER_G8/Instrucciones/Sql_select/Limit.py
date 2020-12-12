from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Limit(Instruccion):
    def __init__(self, listaExpre, tipo, expre, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.listaExpre = listaExpre
        self.expre = expre

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.listaExpre + " linea: " + str(self.linea) + " columna: " + str(self.columna))

'''
instruccion = Limit("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''