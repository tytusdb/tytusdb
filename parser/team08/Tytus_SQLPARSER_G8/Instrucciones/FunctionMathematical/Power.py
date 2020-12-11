
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Power(Instruccion):
    def __init__(self, valor, exp, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor
        self.exp = exp

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("POWER")
        print(math.pow(self.valor,self.exp))
        resultado = math.pow(self.valor,self.exp)
        return resultado
        
instruccion = Power(1,2,None, 1,2)
instruccion.ejecutar(None,None)