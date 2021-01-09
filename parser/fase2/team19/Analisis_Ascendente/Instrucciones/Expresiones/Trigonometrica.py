import  math
from Analisis_Ascendente.Instrucciones.instruccion import Instruccion,IdId
from Analisis_Ascendente.Instrucciones.expresion import *
from Analisis_Ascendente.Instrucciones.Expresiones.Math import *
import Analisis_Ascendente.Instrucciones.Expresiones.Expresion as Expresion

class Trigonometrica(Instruccion):
    def __init__(self, trig, E, E2,fila,columna):
        self.trig = trig
        self.E = E
        self.E2 = E2
        self.fila = fila
        self.columna = columna

    def getC3D(self):
        code = ''
        code += self.trig + '('
        if self.E is not None:
            code += str(self.E.valor)
        if self.E2 is not None:
            code += ',' + str(self.E2.valor)
        code += ')'
        return code


    def Resolver(Trigo,ts,Consola,exceptions):
        if isinstance(Trigo,Trigonometrica):
            num= Trigonometrica.Resolver(Trigo.E,ts,Consola,exceptions)
            if isinstance(num,float) or isinstance(num,int):
                if (str(Trigo.trig).upper() == 'ACOS'):
                    rad = math.acos(num)
                    return rad
                elif (str(Trigo.trig).upper() == 'ACOSD'):
                    return math.acos(math.radians(num))
                elif (str(Trigo.trig).upper() == 'ASIN'):
                    rad = math.asin(num)
                    return rad
                elif (str(Trigo.trig).upper() == 'ASIND'):
                    return math.asin(math.radians(num))
                elif (str(Trigo.trig).upper() == 'ATAN'):
                    rad = math.atan(num)
                    return rad
                elif (str(Trigo.trig).upper() == 'ATAND'):
                    return math.degrees(math.atan((num)))
                elif (str(Trigo.trig).upper() == 'ATAN2'):
                    num1 = Trigonometrica.Resolver(Trigo.E,ts,Consola,exceptions)
                    num2 = Trigonometrica.Resolver(Trigo.E2,ts,Consola,exceptions)

                    if isinstance(num1,int) or isinstance(num1,float):
                        if isinstance(num2,int) or isinstance(num2,float):
                            arg = num1 /  num2
                            return math.atan(float(arg))
                        else:
                            return 'error'
                    else:
                        return 'error'
                elif (str(Trigo.trig).upper() == 'ATAN2D'):
                    num1 = Trigonometrica.Resolver(Trigo.E,ts,Consola,exceptions)
                    num2 = Trigonometrica.Resolver(Trigo.E2,ts,Consola,exceptions)

                    if isinstance(num1, int) or isinstance(num1, float):
                        if isinstance(num2, int) or isinstance(num2, float):
                            arg = num1 / num2
                            return math.degrees(math.atan(float((arg))))
                        else:
                            return 'error'
                    else:
                        return 'error'
                elif (str(Trigo.trig).upper() == 'COS'):
                    rad = math.cos(num)
                    return rad
                elif (str(Trigo.trig).upper() == 'COSD'):
                    return math.cos(math.radians(num))
                elif (str(Trigo.trig).upper() == 'COT'):
                    tan = math.tan(num)
                    cot = 1 / tan
                    return cot
                elif (str(Trigo.trig).upper() == 'COTD'):
                    tan = math.tan(math.radians(num))
                    cot = 1 / tan
                    return cot
                elif (str(Trigo.trig).upper() == 'SIN'):
                    rad = math.sin(num)
                    return rad
                elif (str(Trigo.trig).upper() == 'SIND'):
                    return math.sin(math.radians(num))
                elif (str(Trigo.trig).upper() == 'TAN'):
                    return math.tan(num)
                elif (str(Trigo.trig).upper() == 'TAND'):
                    return math.tan(math.radians(num))
                elif (str(Trigo.trig).upper() == 'SINH'):
                    rad = math.sinh(num)
                    return rad
                elif (str(Trigo.trig).upper() == 'COSH'):
                    rad = math.cosh(num)
                    return rad
                elif (str(Trigo.trig).upper() == 'TANH'):
                    rad = math.tanh(num)
                    return rad
                elif (str(Trigo.trig).upper() == 'ASINH'):
                    rad = math.asinh(num)
                    return rad
                elif (str(Trigo.trig).upper() == 'ACOSH'):
                    rad = math.acosh(num)
                    return rad
                elif (str(Trigo.trig).upper() == 'ATANH'):
                    rad = math.atanh(num)
                    return rad

        elif isinstance(Trigo,Primitivo):
            return Trigo.valor
        elif isinstance(Trigo,Trigonometrica):
            return Trigonometrica.Resolver(Trigo,ts,Consola,exceptions)
        elif isinstance(Trigo, Math_):
            return Math_.Resolver(Trigo,ts,Consola,exceptions)
        elif isinstance(Trigo,Expresion.Expresion):
            return Expresion.Expresion.Resolver(Trigo ,ts,Consola,exceptions)
        elif isinstance(Trigo, Id):
            return Trigo.id
        elif isinstance(Trigo, IdId):
            return [Trigo.id1,Trigo.id2]
