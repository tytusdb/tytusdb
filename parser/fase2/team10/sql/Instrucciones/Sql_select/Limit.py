from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Limit(Instruccion):
    def __init__(self, listaExpre, expre, strGram, linea, columna):
        Instruccion.__init__(self, None, linea,columna,strGram)
        self.listaExpre = listaExpre
        self.expre = expre

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if isinstance(self.listaExpre, Instruccion):
            res = self.listaExpre.ejecutar(tabla,arbol)
        else:
            res = self.listaExpre
        #print(self.listaExpre + " linea: " + str(self.linea) + " columna: " + str(self.columna))
        return res
'''
instruccion = Limit("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''