from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
class Columna(Instruccion):
    def __init__(self, nombre, tipo, constraint, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.nombre = nombre
        self.tipo = tipo
        self.constraint=constraint
    
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
    
    def analizar(self, tabla, arbol):
        pass
    
    def traducir(self, tabla, arbol):
        cadena = self.nombre
        if(self.tipo.tipo != None):
            cadena += " "+self.tipo.traducir(tabla, arbol)
        
        if(self.constraint != None):
            for x in range(0, len(self.constraint)):
                cadena += self.constraint[x].traducir(tabla,arbol)
        
        return cadena