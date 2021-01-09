from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Columna(Instruccion):
    def __init__(self, id, tipo, strGram ,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.id = id
        self.tipo = tipo

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        
    def getCodigo(self, tabla, arbol):
        id = f"{self.id}"
        tipo = f"{self.tipo.toString()}"
       
        
        column = f"{id} {tipo}"
        
        return column

    def getCodigoTipo(self, tabla, arbol):
        return self.tipo.toString()