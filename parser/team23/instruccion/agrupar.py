from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *
from abstract.retorno import *
import math as m
import decimal as d
import random as r
class agrupar(instruccion):
    def __init__(self,agrupacion, expresiones,expresiones1, line, column, num_nodo):
        super().__init__(line,column)
        self.valor = expresiones.valor
        self.tipo = expresiones.tipo
        self.expresiones=expresiones
        self.expresiones1 = expresiones1
        self.agrupacion=agrupacion
        self.nodo = nodo_AST(agrupacion,num_nodo)
        self.nodo.hijos.append(expresiones.nodo)
        if self.expresiones1 != None:
            self.nodo.hijos.append(expresiones1.nodo)        
        
    def ejecutar(self):
        aux = 0
        numero = self.expresiones.valor
        numero1 = 0
        if self.expresiones1 != None:
            numero1 = self.expresiones1.valor
        print(self.agrupacion)
        print(self.valor)

        if str(self.agrupacion).lower() == "factorial":
            aux = m.factorial(numero)
        elif str(self.agrupacion).lower() == "cbrt":
            aux = round(numero**(1/3))
        elif str(self.agrupacion).lower() == "ceil":
            aux = int(numero+1)
        elif str(self.agrupacion).lower() == "ceiling":
            aux = int(numero+1)
        elif str(self.agrupacion).lower() == "degrees":
            aux = numero*(180/m.pi)
        elif str(self.agrupacion).lower() == "div":
            aux = int(numero/numero1)
        elif str(self.agrupacion).lower() == "exp":
            aux = m.exp(numero)
        elif str(self.agrupacion).lower() == "floor":
            aux = int(numero)
        elif str(self.agrupacion).lower() == "gcd":
            aux = m.gcd(numero,numero1)
        elif str(self.agrupacion).lower() == "ln":
            aux = m.log(numero,m.e)
        elif str(self.agrupacion).lower() == "log":
            aux = m.log10(numero)
        elif str(self.agrupacion).lower() == "mod":
            aux = numero%numero1
        elif str(self.agrupacion).lower() == "pi":
            aux = m.pi
        elif str(self.agrupacion).lower() == "power":
            aux = numero ** numero1
        elif str(self.agrupacion).lower() == "radians":
            aux = m.radians(numero)
        elif str(self.agrupacion).lower() == "round":
            aux = round(numero)
        elif str(self.agrupacion).lower() == "sing":
            aux = -1 if numero < 0 else 1
        elif str(self.agrupacion).lower() == "sqrt":
            aux = m.sqrt(numero)
        elif str(self.agrupacion).lower() == "width_bucket":
            aux = r.randint(1,3)
        elif str(self.agrupacion).lower() == "trunc":
            aux = int(numero)
        elif str(self.agrupacion).lower() == "random":
            aux = r.random()
        elif str(self.agrupacion).lower() == "acos":
            aux = m.acos(numero)
        elif str(self.agrupacion).lower() == "acosd":
            aux = m.degrees(acos(numero))   
        elif str(self.agrupacion).lower() == "asin":
            aux = m.asin(numero)
        elif str(self.agrupacion).lower() == "asind":
            aux = m.degrees(asin(numero))
        elif str(self.agrupacion).lower() == "atan":
            aux = m.atan(numero)
        elif str(self.agrupacion).lower() == "atand":
            aux = m.degrees(atan(numero))
        elif str(self.agrupacion).lower() == "atan2":
            aux = m.atan2(numero,numero1)
        elif str(self.agrupacion).lower() == "atan2d":
            aux = m.degrees(atan2(numero,numero1))
        elif str(self.agrupacion).lower() == "cos":
            aux = m.cos(numero)
        elif str(self.agrupacion).lower() == "cosd":
            aux = m.degrees(cos(numero))
        elif str(self.agrupacion).lower() == "cot":
            aux = (m.cos(numero)/m.sin(numero))
        elif str(self.agrupacion).lower() == "cotd":
            aux = m.degrees(cot(numero))
        elif str(self.agrupacion).lower() == "sin":
            aux = m.sin(numero)
        elif str(self.agrupacion).lower() == "sind":
            aux = m.degrees(sin(numero))
        elif str(self.agrupacion).lower() == "tan":
            aux = m.tan(numero)
        elif str(self.agrupacion).lower() == "tand":
            aux = m.degrees(tan(numero))
        elif str(self.agrupacion).lower() == "sinh":
            aux = m.sinh(numero)
        elif str(self.agrupacion).lower() == "cosh":
            aux = m.cosh(numero)
        elif str(self.agrupacion).lower() == "tanh":
            aux = m.tanh(numero)
        elif str(self.agrupacion).lower() == "asinh":
            aux = m.asinh(numero)
        elif str(self.agrupacion).lower() == "acosh":
            aux = m.acosh(numero)
        elif str(self.agrupacion).lower() == "atanh":
            aux = m.atanh(numero)

        self.valor = aux
        print(self.valor)
        return retorno(self.valor, self.tipo)