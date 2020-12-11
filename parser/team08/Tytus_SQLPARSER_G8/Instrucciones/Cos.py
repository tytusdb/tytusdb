from Instruccion import Instruccion
from TablaSimbolo import *

class Cos(Instruccion):
    def __init__(self, valor, linea, columna):
        Instruccion.__init__(self,None,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        # Valor se vuelve un objeto el cual va a traer un tipo y un resultado
        valor = self.valor.ejecutar(tabla,arbol)
        #if isinstance(valor, Excepcion) 

        if (valor.tipo != Tipo_Dato.BIGINT or valor.tipo != Tipo_Dato.SMALLINT or valor.tipo != Tipo_Dato.INTEGER or valor.tipo != Tipo_Dato.DECIMAL || valor.tipo != Tipo_Dato.DOUBLE_PRECISION || valor.tipo != Tipo_Dato.NUMERIC):
            error = Excepcion("Semantico","No se puede realizar la operación COS con el tipo: "+valor.tipo,str(self.linea),str(self.columna))

        resultado.valor = cos(valor)
        resultado.tipo = valor.tipo
        return resultado        
        #print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))

instruccion = Cos("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)