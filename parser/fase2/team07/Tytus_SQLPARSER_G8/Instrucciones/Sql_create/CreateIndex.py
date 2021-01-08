from Instrucciones.TablaSimbolos.Instruccion import *

class CreateIndex(Instruccion):
    def __init__(self, nombre, tipo, tabla, columnas, strGram, linea, columna, strSent):
        Instruccion.__init__(self,tipo,linea,columna, strGram, strSent)
        self.nombre= nombre
        self.tipo = tipo
        self.tabla = tabla        
        self.columnas = columnas        

    def ejecutar(self, tabla, arbol):
        #super().ejecutar(tabla,arbol)
        tabla.setIndice(self, arbol)
    
    def traducir(self,tabla,arbol,cadenaTraducida):
        temporal = arbol.generaTemporal()
        codigo = "\t" + temporal + " = " + "\"" + self.strSent + "\"\n"
        codigo += "\tFuncionesPara3D.ejecutarsentecia(" + temporal + ")\n\n"
        return codigo