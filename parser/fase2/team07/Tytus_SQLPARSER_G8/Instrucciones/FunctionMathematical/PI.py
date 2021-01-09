import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from Instrucciones.TablaSimbolos.Simbolo3D import Simbolo3d

class PI(Instruccion):
    def __init__(self, strGram, linea, columna, strSent):
        Instruccion.__init__(self,Tipo("",Tipo_Dato.DOUBLE_PRECISION),linea,columna,strGram,strSent)

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        self.tipo = Tipo("",Tipo_Dato.NUMERIC)
        return math.pi
    
    def traducir(self, tabla, arbol, cadenaTraducida):
        resultado = self.ejecutar(tabla, arbol)
        if isinstance(resultado,Excepcion):
            return resultado        
        codigo = ""
        temporal = arbol.generaTemporal()
        codigo += "\t" + temporal + " = " + str(resultado) + "\n"
        nuevo = Simbolo3d(self.tipo, temporal, codigo, None, None)
        return nuevo
