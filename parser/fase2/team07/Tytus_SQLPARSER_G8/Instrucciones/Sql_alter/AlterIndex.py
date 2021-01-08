from Instrucciones.TablaSimbolos.Instruccion import *

class AlterIndex(Instruccion):
    def __init__(self, nombre, tipo, actual, reemplazo, strGram, linea, columna, strSent):
        Instruccion.__init__(self,tipo,linea,columna, strGram, strSent)
        self.nombre= nombre
        self.actual = actual
        self.reemplazo = reemplazo        

    def ejecutar(self, tabla, arbol):
        #super().ejecutar(tabla,arbol)
        tabla.alterIndice(self, arbol)
    
    def traducir(self,tabla,arbol,cadenaTraducida):
        temporal = arbol.generaTemporal()
        codigo = "\t" + temporal + " = " + "\"" + self.strSent + "\"\n"
        codigo += "\tFuncionesPara3D.ejecutarsentecia(" + temporal + ")\n\n"
        return codigo