from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Set(Instruccion):
    def __init__(self, id, tipo, id2, strGram,linea, columna, strSent):
        Instruccion.__init__(self,tipo,linea,columna, strGram, strSent)
        self.valor = id
        self.id2 = id2

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))

    def traducir(self,tabla,arbol,cadenaTraducida):
        temporal = arbol.generaTemporal()
        codigo = "\t" + temporal + " = " + "\"" + self.strSent + "\"\n"
        codigo += "\tFuncionesPara3D.ejecutarsentecia(" + temporal + ")\n\n"
        return codigo
'''
instruccion = Use("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''