from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo

class Enum(Instruccion):
    def __init__(self, id, tipo, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.TIPOENUM),linea,columna,"")
        self.id = id
        self.listaValores = []

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        return self.valor

    def analizar(self, tabla, arbol):
        return super().analizar(tabla, arbol)
    
    def traducir(self, tabla, arbol):
        return super().traducir(tabla, arbol)
    
    def buscarTipo(self, nombre):
        for x in range(0, len(self.listaValores)):
            if self.listaValores[x] == nombre:
                return nombre
        
        return None