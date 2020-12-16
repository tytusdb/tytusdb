from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Declare(Instruccion):
    def __init__(self, id, operacion, id2, linea, columna):
        Instruccion.__init__(self,None,linea,columna)
        self.valor = id
        self.id2 = id2
        self.operacion = operacion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))

'''
instruccion = Declare("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''