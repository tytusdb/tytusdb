from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *
from abstract.retorno import *
import math as m
import decimal as d
import random as r
from datetime import date
from datetime import datetime
import hashlib
class agrupar(instruccion):
    def __init__(self,agrupacion, expresiones,expresiones1, line, column, num_nodo):
        super().__init__(line,column)
        self.alias = None
        self.valor = expresiones.valor
        self.tipo = expresiones.tipo
        self.expresiones=expresiones
        self.expresiones1 = expresiones1
        self.agrupacion=agrupacion
        self.nodo = nodo_AST(agrupacion,num_nodo)
        self.nodo.hijos.append(expresiones.nodo)
        if self.expresiones1 != None:
            self.nodo.hijos.append(expresiones1.nodo)        
        
    def ejecutar(self, list_db):
        today = date.today()
        now = datetime.now()
        aux = 0
        numero = self.expresiones.valor
        numero1 = 0
        if self.expresiones1 != None:
            numero1 = self.expresiones1.valor

        if self.alias == None:
            self.alias = "Resultado"
        print(self.agrupacion)
        if str(self.agrupacion).lower() == "factorial":
            aux = m.factorial(numero)
        elif str(self.agrupacion).lower() == "cbrt":
            aux = round(numero**(1/3))
        elif str(self.agrupacion).lower() == "abs":
            aux = abs(numero)
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
        elif str(self.agrupacion).lower() == "now":
            aux = now.strftime("%Y-%m-%d %H:%M:%S")
        elif str(self.agrupacion).lower() == "timestamp":
            aux = now.strftime("%Y-%m-%d %H:%M:%S")
        elif str(self.agrupacion).lower() == "current_date":
            aux = now.strftime("%Y-%m-%d")
        elif str(self.agrupacion).lower() == "current_time":
            aux = now.strftime("%H:%M:%S")
        elif str(self.agrupacion).lower() == "date_part":
            aux = now.strftime("%H:%M:%S")
            if numero == "hour" or numero == "hours":
                aux_time = str(numero1).split()
                aux = aux_time[0]
            elif numero == "minutes" or numero == "minute":
                aux_time = str(numero1).split()
                aux = aux_time[2]
            elif numero == "seconds" or numero == "second":
                aux_time = str(numero1).split()
                aux = aux_time[4]
            else:
                aux = "No se encontro"
        elif str(self.agrupacion).lower() == "extract":
            x_time = str(numero1).split()
            y_time = x_time[0].split("-")
            z_time = x_time[1].split(":")
            if numero == "year":
                aux = y_time[0]
            elif numero == "month":
                aux = y_time[1]
            elif numero == "day":
                aux = y_time[2]
            elif numero == "hour":
                aux = z_time[0]
            elif numero == "minute":
                aux = z_time[1]
            elif numero == "second":
                aux = z_time[2]
        elif str(self.agrupacion).lower() == "substring" or str(self.agrupacion).lower() == "substr":
            aux_sub = ""
            for x in range(numero1):
                aux_sub += numero[x] 
            aux = aux_sub
        elif str(self.agrupacion).lower() == "length":
            aux = len(numero)
        elif str(self.agrupacion).lower() == "trim":
            aux = str(numero).strip()
        elif str(self.agrupacion).lower() == "md5":
            aux = hashlib.md5(numero.encode()).hexdigest()
        elif str(self.agrupacion).lower() == "sha256":
            aux = hashlib.sha256(numero.encode()).hexdigest()
        elif str(self.agrupacion).lower() == "decode":
            aux = numero  
        elif str(self.agrupacion).lower() == "encode":
            aux = numero
        elif str(self.agrupacion).lower() == "get_byte":
            aux = ord(str(numero[numero1]))
        elif str(self.agrupacion).lower() == "set_byte":
            aux = numero
        elif str(self.agrupacion).lower() == "convert":
            aux = numero
            

        self.valor = aux
        print(self.valor)
        return retorno(self.valor, self.tipo , self.alias)