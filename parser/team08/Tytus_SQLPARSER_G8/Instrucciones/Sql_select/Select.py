from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Select(Instruccion):
    #dist  tipo  lcol  lcol  linners where lrows
    def __init__(self, dist, tipo, lcol, lcol2, linners, where, lrows, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.dist = dist
        self.lcol = lcol
        self.lcol2 = lcol2
        self.linners = linners
        self.where = where
        self.lrows = lrows

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.dist + " linea: " + str(self.linea) + " columna: " + str(self.columna))

'''
instruccion = Select("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''