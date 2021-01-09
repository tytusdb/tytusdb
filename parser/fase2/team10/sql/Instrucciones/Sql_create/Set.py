from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Set(Instruccion):
    def __init__(self, id, tipo, id2, strGram,linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = id
        self.id2 = id2

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))
'''
instruccion = Use("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''