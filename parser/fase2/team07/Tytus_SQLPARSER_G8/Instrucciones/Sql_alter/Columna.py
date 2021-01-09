from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Columna(Instruccion):
    def __init__(self, id, tipo, strGram ,linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna,strGram,strSent)
        self.id = id
        self.tipo = tipo

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        