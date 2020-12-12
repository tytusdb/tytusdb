from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class CreateType(Instruccion):
    def __init__(self, id, tipo, listaExpre, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = id
        self.listaExpre = listaExpre

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))
'''
instruccion = CreateType("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''