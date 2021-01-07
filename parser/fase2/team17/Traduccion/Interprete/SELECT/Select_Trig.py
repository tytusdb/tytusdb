
from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.Primitivos.TIPO import TIPO
from Interprete.SELECT.indexador_auxiliar import indexador_auxiliar
from Interprete.SELECT.indexador_auxiliar import IAT
from Interprete.simbolo import Simbolo
import traceback


import math

class Select_Trig(NodoArbol):

    def __init__(self, exp, tipo, line, coliumn):
        super().__init__(line, coliumn)
        self.exp = exp
        self.tipo = tipo

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):

        if self.tipo == "acos":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                acos   = math.acos(degree)
                retorno: Valor = Valor(TIPO.DECIMAL,acos)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "acosd":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                acos   = math.acos(math.radians(degree))
                retorno: Valor = Valor(TIPO.DECIMAL,acos)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "asin":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                acos = math.asin(degree)
                retorno: Valor = Valor(TIPO.DECIMAL, acos)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "asind":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                asin = math.asin(math.radians(degree))
                retorno: Valor = Valor(TIPO.DECIMAL, asin)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "atan":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                acos = math.atan(degree)
                retorno: Valor = Valor(TIPO.DECIMAL, acos)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "atan2":
            try:
                value1: Valor = self.exp[0].execute(entorno, arbol)  # <--- parametro1
                value2: Valor = self.exp[1].execute(entorno, arbol)  # <--- parametro2

                par1= float(str(value1.data))
                par2 = float(str(value1.data))

                acos = math.atan2(par1,par2)
                retorno: Valor = Valor(TIPO.DECIMAL, acos)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "atan2d":
            try:
                value1: Valor = self.exp[0].execute(entorno, arbol)  # <--- parametro1
                value2: Valor = self.exp[1].execute(entorno, arbol)  # <--- parametro2

                par1= float(str(value1.data))
                par2 = float(str(value1.data))

                acos = math.atan2(math.radians(par1),math.radians(par2))
                retorno: Valor = Valor(TIPO.DECIMAL, acos)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "cos":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                acos = math.cos(degree)
                retorno: Valor = Valor(TIPO.DECIMAL, acos)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "cosd":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                cos = math.cos(math.radians(degree))
                retorno: Valor = Valor(TIPO.DECIMAL, cos)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "cot":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                cos = math.cos(degree)
                sin = math.sin(degree)
                cot = cos/sin
                retorno: Valor = Valor(TIPO.DECIMAL, cot)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "cotd":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                cos = math.cos(math.radians(degree))
                sin = math.sin(math.radians(degree))
                cot = cos/sin
                retorno: Valor = Valor(TIPO.DECIMAL, cot)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "sin":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                sin = math.sin(degree)
                retorno: Valor = Valor(TIPO.DECIMAL,sin)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "sind":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                sin = math.sin(math.radians(degree))
                retorno: Valor = Valor(TIPO.DECIMAL,sin)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "tan":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                tan = math.tan(degree)
                retorno: Valor = Valor(TIPO.DECIMAL,tan)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "tand":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                tan = math.tan(math.radians(degree))
                retorno: Valor = Valor(TIPO.DECIMAL,tan)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "sinh":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                sinh = math.sinh(degree)
                retorno: Valor = Valor(TIPO.DECIMAL,sinh)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "cosh":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                cosh = math.cosh(degree)
                retorno: Valor = Valor(TIPO.DECIMAL, cosh)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "tanh":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                tanh = math.tanh(degree)
                retorno: Valor = Valor(TIPO.DECIMAL,tanh)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "asinh":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                asinh = math.asinh(degree)
                retorno: Valor = Valor(TIPO.DECIMAL,asinh)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "acosh":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                acosh = math.acosh(degree)
                retorno: Valor = Valor(TIPO.DECIMAL,acosh)
                return retorno
            except:
                print(traceback)
        elif self.tipo == "atanh":
            try:
                expresion: Valor = self.exp.execute(entorno, arbol)  # <--- numero
                degree = float(str(expresion.data))
                atanh = math.atanh(degree)
                retorno: Valor = Valor(TIPO.DECIMAL,atanh)
                return retorno
            except:
                print(traceback)
