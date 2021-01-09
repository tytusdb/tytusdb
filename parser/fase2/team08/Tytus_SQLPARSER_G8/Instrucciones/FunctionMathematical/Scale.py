import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Expresiones.Aritmetica import Aritmetica
from Instrucciones.Expresiones.Primitivo import Primitivo

class Scale(Instruccion):
    def __init__(self, valor, strGram,tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        arbol.consola.append('Función en proceso...')

    def analizar(self, tabla, arbol):
        return super().analizar(tabla, arbol)

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        if isinstance(self.valor, Primitivo):
            return f"SCALE({self.valor.traducir(tabla,arbol).temporalAnterior})"
        elif isinstance(self.valor, Aritmetica):
            return f"SCALE({self.valor.concatenar(tabla,arbol)})"
        return f"SCALE({self.valor.traducir(tabla,arbol)})"