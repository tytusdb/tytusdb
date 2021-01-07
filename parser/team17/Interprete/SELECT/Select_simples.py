from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.Primitivos.TIPO import TIPO
from Interprete.SELECT.indexador_auxiliar import indexador_auxiliar
from Interprete.SELECT.indexador_auxiliar import IAT
from Interprete.simbolo import Simbolo
import math
import random

class Select_simples(NodoArbol):

    def __init__(self, exp, tipo, line, coliumn):
        super().__init__(line, coliumn)
        self.exp = exp
        self.tipo = tipo

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):

        if self.tipo == "FACTORIAL":
            expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
            retorno:Valor = Valor(TIPO.DECIMAL, math.factorial( int(str(expresion.data)) ))
            return retorno
        elif self.tipo == "FLOOR":
            expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
            retorno: Valor = Valor(TIPO.DECIMAL, math.floor(float(str(expresion.data))))
            return retorno
        elif self.tipo == "GCD":
            expresion1: Valor = self.exp[0].execute(entorno, arbol)  # <--- numero
            expresion2: Valor = self.exp[1].execute(entorno, arbol)  # <--- numero
            retorno: Valor = Valor(TIPO.DECIMAL, math.gcd(int(str(expresion1.data)), int(str(expresion2.data))))
            return retorno
        elif self.tipo == "LN":
            expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
            retorno: Valor = Valor(TIPO.DECIMAL, math.log10(float(str(expresion.data))))
            return retorno
        elif self.tipo == "LOG":
            expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
            retorno: Valor = Valor(TIPO.DECIMAL, math.log(float(str(expresion.data))))
            return retorno
        elif self.tipo == "MOD":
            expresion1: Valor = self.exp[0].execute(entorno, arbol)  # <--- numero
            expresion2: Valor = self.exp[1].execute(entorno, arbol)  # <--- numero
            v = int(str(expresion1.data)) % int(str(expresion2.data))
            retorno: Valor = Valor(TIPO.DECIMAL, v)
            return retorno
        elif self.tipo == "PI":
            retorno: Valor = Valor(TIPO.DECIMAL, math.pi)
            return retorno
        elif self.tipo == "POWER":
            expresion1: Valor = self.exp[0].execute(entorno, arbol)  # <--- numero
            expresion2: Valor = self.exp[1].execute(entorno, arbol)  # <--- numero
            v = int(str(expresion1.data)) ** int(str(expresion2.data))
            retorno: Valor = Valor(TIPO.DECIMAL, v)
            return retorno
        elif self.tipo == "RADIANS":
            expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
            retorno: Valor = Valor(TIPO.DECIMAL, math.radians(float(str(expresion.data))))
            return retorno
        elif self.tipo == "ROUND":
            expresion1: Valor = self.exp[0].execute(entorno, arbol)  # <--- numero
            expresion2: Valor = self.exp[1].execute(entorno, arbol)  # <--- numero
            retorno: Valor = Valor(TIPO.DECIMAL, round(float(str(expresion1.data)) , int(str(expresion2.data))))
            return retorno
        elif self.tipo == "SIGN":
            expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
            v = 0
            if float(str(expresion.data)) > 0:
                v = 1
            else:
                v = -1
            retorno: Valor = Valor(TIPO.DECIMAL, v)
            return retorno
        elif self.tipo == "SQRT":
            expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
            retorno: Valor = Valor(TIPO.DECIMAL, math.sqrt(float(str(expresion.data))))
            return retorno
        elif self.tipo == "TRUNC":
            expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
            retorno: Valor = Valor(TIPO.DECIMAL, math.trunc(float(str(expresion.data))))
            return retorno
        elif self.tipo == "RANDOM":
            retorno: Valor = Valor(TIPO.DECIMAL, random.randrange(1024))
            return retorno
        elif self.tipo == "CBRT":
            expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
            retorno: Valor = Valor(TIPO.DECIMAL, self.CBRT(float(str(expresion.data))))
            return retorno
        elif self.tipo == "CEIL":
            expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
            retorno: Valor = Valor(TIPO.DECIMAL, math.ceil(float(str(expresion.data))))
            return retorno
        elif self.tipo == "DEGREES":
            expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
            retorno: Valor = Valor(TIPO.DECIMAL, math.degrees(float(str(expresion.data))))
            return retorno
        elif self.tipo == "DIV":
            expresion1: Valor = self.exp[0].execute(entorno, arbol)  # <--- numero
            expresion2: Valor = self.exp[1].execute(entorno, arbol)  # <--- numero
            v = int(str(expresion1.data)) / int(str(expresion2.data))
            retorno: Valor = Valor(TIPO.DECIMAL, int(v))
            return retorno
        elif self.tipo == "EXP":
            expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
            retorno: Valor = Valor(TIPO.DECIMAL, math.exp(float(str(expresion.data))))
            return retorno

    def CBRT(self, n):
        return n ** (1./3.)