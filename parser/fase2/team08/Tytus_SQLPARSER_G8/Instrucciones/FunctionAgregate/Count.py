from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
import numpy as np 

class Count(Instruccion):
    def __init__(self, valor, tipo, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.INTEGER),linea,columna, strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.valor.ejecutar(tabla, arbol)
        if isinstance(resultado, Excepcion):
            return resultado
        resultado = len(resultado)
        return np.array([[resultado]])

    def analizar(self, tabla, arbol):
        super().analizar(tabla, arbol)
        pass

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        cadena = "COUNT("
        cadena += self.valor.concatenar(tabla,arbol)
        cadena += ")"
        return cadena
