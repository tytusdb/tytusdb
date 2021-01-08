from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
import numpy as np
class Sum(Instruccion):
    def __init__(self, valor, tipo, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.valor.ejecutar(tabla, arbol)
        if isinstance(resultado, Excepcion):
            return resultado

        suma = 0
        for x in range(0, len(resultado)):
            #print(f"posicion {x}")
            #print(f"valor {resultado[x][0]}")
            if str.isnumeric(str(resultado[x][0])):
                suma += int(resultado[x][0])
            elif str.isdecimal(str(resultado[x][0])):
                suma += float(resultado[x][0])
            else:
                error = Excepcion("22023", "Semantico", "Parametro de evaluacion invalido", self.linea, self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error

        return np.array([[suma]])


    def analizar(self, tabla, arbol):
        return super().analizar(tabla, arbol)
        
    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        cadena = "SUM("
        cadena += self.valor.concatenar(tabla,arbol)
        cadena += ")"
        return cadena

