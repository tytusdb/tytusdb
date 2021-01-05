from Instrucciones.TablaSimbolos.Instruccion import *

class CreateIndex(Instruccion):
    def __init__(self, nombre, tipo, orden, consi, columnas, strGram, linea, columna, strSent):
        Instruccion.__init__(self,tipo,linea,columna, strGram, strSent)
        self.nombre= nombre
        self.tipo = tipo
        self.orden = orden
        self.columnas = columnas
        self.consi = consi

    def ejecutar(self, tabla, arbol):
        #super().ejecutar(tabla,arbol)
        tabla.setIndice(self)        
