from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class CreateOrReplace(Instruccion):
    def __init__(self, id, tipo, id2, exp, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = id
        self.id2 = id2
        self.exp = exp

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))

'''
instruccion = CreateOrReplace("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''