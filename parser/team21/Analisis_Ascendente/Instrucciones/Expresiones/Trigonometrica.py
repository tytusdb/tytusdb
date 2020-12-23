import  math
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion,IdId
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.expresion import *
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math import *
import Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion as Expresion

class Trigonometrica(Instruccion):
    def __init__(self, trig, E,fila,columna):
        self.trig = trig
        self.E = E
        self.fila = fila
        self.columna = columna


    def Resolver(Trigo,ts,Consola,exceptions):
        #print('TRIGONOMETRICA -- '+Trigo.trig+'----' + type(Trigo).__name__ + '\n')


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
                    return math.atan(math.radians(num))
                elif (str(Trigo.trig).upper() == 'ATAN2'):
                    return 0.1111
                elif (str(Trigo.trig).upper() == 'atan2d'):
                    return 0.1111
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
