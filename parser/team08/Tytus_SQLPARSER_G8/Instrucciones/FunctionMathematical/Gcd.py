
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Gcd(Instruccion):
    def __init__(self, op1, op2, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.op1 = op1
        self.op2 = op2

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("gcd")
        print(math.gcd(self.op1,self.op2))
        return math.gcd(self.op1,self.op2)

#find the  the greatest common divisor of the two integers
'''
instruccion = Gcd(10,5,None, 1,2)

instruccion.ejecutar(None,None)
'''