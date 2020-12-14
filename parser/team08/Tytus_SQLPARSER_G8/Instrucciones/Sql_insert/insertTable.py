from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class insertTable(Instruccion):
    def __init__(self, id, tipo, lcol, lexpre, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = id
        self.lcol = lcol
        self.lexpre = lexpre

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))
'''
instruccion = insertTable("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''