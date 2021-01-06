import  math
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion,IdId
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.expresion import *
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math import *
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math  as Math
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion as Expresion

class Trigonometrica(Instruccion):
    def __init__(self, trig, E, E2,fila,columna):
        self.trig = trig
        self.E = E
        self.E2 = E2
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
        elif isinstance(Trigo, Math.Math_):
            return Math.Math_.Resolver(Trigo,ts,Consola,exceptions)
        elif isinstance(Trigo,Expresion.Expresion):
            return Expresion.Expresion.Resolver(Trigo ,ts,Consola,exceptions)
        elif isinstance(Trigo, Id):
            return Trigo.id
        elif isinstance(Trigo, IdId):
            return [Trigo.id1,Trigo.id2]
        elif isinstance(Trigo, Unario):
            return Expresion.Expresion.Resolver(Trigo,ts,Consola,exceptions)


    def traducir(trig, ts, consola, exception, tv, regla, antes, optimizado, ID):
        num = Expresion.Expresion.traducir(trig.E, ts, consola, exception, tv, regla, antes, optimizado, ID)
        if (str(trig.trig).upper() == 'ACOS'):
            temp = tv.Temp()
            consola.append(f'\t{temp} = math.acos({num})\n')
            return temp
        elif (str(trig.trig).upper() == 'ACOSD'):
            temp1 = tv.Temp()
            consola.append(f'\t{temp1} = math.radians({num})\n')
            temp2 = tv.Temp()
            consola.append(f'\t{temp2} = math.acos({temp1})\n')
            return temp2
        elif (str(trig.trig).upper() == 'ASIN'):
            temp = tv.Temp()
            consola.append(f'\t{temp} = math.asin({num})\n')
            return temp
        elif (str(trig.trig).upper() == 'ASIND'):
            temp1 = tv.Temp()
            consola.append(f'\t{temp1} = math.radians({num})\n')
            temp2 = tv.Temp()
            consola.append(f'\t{temp2} = math.asin({temp1})\n')
            return temp2
        elif (str(trig.trig).upper() == 'ATAN'):
            temp = tv.Temp()
            consola.append(f'\t{temp} = math.atan({num})\n')
            return temp
        elif (str(trig.trig).upper() == 'ATAND'):
            temp1 = tv.Temp()
            consola.append(f'\t{temp1} = math.atan({num})\n')
            temp2 = tv.Temp()
            consola.append(f'\t{temp2} = math.degrees({temp1})\n')
            return temp2
        elif (str(trig.trig).upper() == 'ATAN2'):
            num2 = Expresion.Expresion.traducir (trig.E2, ts, consola, exception, tv, regla, antes, optimizado, ID)
            #omito validaciones
            arg = tv.Temp()
            consola.append(f'\t{arg} = {num} / {num2}\n')
            casteo = tv.Temp()
            consola.append(f'\t{casteo} = float({arg})\n')
            atanm = tv.Temp()
            consola.append(f'\t{atanm} = math.atan({casteo})\n')
            return atanm
        elif (str(trig.trig).upper() == 'ATAN2D'):
            num2 = Expresion.Expresion.traducir (trig.E2, ts, consola, exception, tv, regla, antes, optimizado, ID)
            #omito validaciones
            arg = tv.Temp()
            consola.append(f'\t{arg} = {num} / {num2}\n')
            casteo = tv.Temp()
            consola.append(f'\t{casteo} = float({arg})\n')
            atanm = tv.Temp()
            consola.append(f'\t{atanm} = math.atan({casteo})\n')
            temp = tv.Temp()
            consola.append(f'\t{temp} = math.degrees({atanm})\n')
        elif (str(trig.trig).upper() == 'COS'):
            temp = tv.Temp()
            consola.append(f'\t{temp} = math.cos({num})\n')
            return temp
        elif (str(trig.trig).upper() == 'COSD'):
            temp1 = tv.Temp()
            consola.append(f'\t{temp1} = math.radians({num})\n')
            temp2 = tv.Temp()
            consola.append(f'\t{temp2} = math.cos({temp1})\n')
            return temp2
        elif (str(trig.trig).upper() == 'COT'):
            temp1 = tv.Temp()
            consola.append(f'\t{temp1} = math.tan({num})\n')
            temp2 = tv.Temp()
            consola.append(f'\t{temp2} = 1 / {temp1}\n')
            return temp2
        elif (str(trig.trig).upper() == 'COTD'):
            temp1 = tv.Temp()
            consola.append(f'\t{temp1} = math.radians({num})\n')
            temp2 = tv.Temp()
            consola.append(f'\t{temp2} = math.tan({temp1})\n')
            temp3 = tv.Temp()
            consola.append(f'\t{temp3} = 1 / {temp2}\n')
            return temp3
        elif (str(trig.trig).upper() == 'SIN'):
            temp = tv.Temp()
            consola.append(f'\t{temp} = math.sin({num})\n')
            return temp
        elif (str(trig.trig).upper() == 'SIND'):
            temp1 = tv.Temp()
            consola.append(f'\t{temp1} = math.radians({num})\n')
            temp2 = tv.Temp()
            consola.append(f'\t{temp2} = math.sin({temp1})\n')
            return temp2
        elif (str(trig.trig).upper() == 'TAN'):
            temp = tv.Temp()
            consola.append(f'\t{temp} = math.tan({num})\n')
            return temp
        elif (str(trig.trig).upper() == 'TAND'):
            temp1 = tv.Temp()
            consola.append(f'\t{temp1} = math.radians({num})\n')
            temp2 = tv.Temp()
            consola.append(f'\t{temp2} = math.tan({temp1})\n')
            return temp2
        elif (str(trig.trig).upper() == 'SINH'):
            temp = tv.Temp()
            consola.append(f'\t{temp} = math.sinh({num})\n')
            return temp
        elif (str(trig.trig).upper() == 'COSH'):
            temp = tv.Temp()
            consola.append(f'\t{temp} = math.cosh({num})\n')
            return temp
        elif (str(trig.trig).upper() == 'TANH'):
            temp = tv.Temp()
            consola.append(f'\t{temp} = math.tanh({num})\n')
            return temp
        elif (str(trig.trig).upper() == 'ASINH'):
            temp = tv.Temp()
            consola.append(f'\t{temp} = math.asinh({num})\n')
            return temp
        elif (str(trig.trig).upper() == 'ACOSH'):
            temp = tv.Temp()
            consola.append(f'\t{temp} = math.acosh({num})\n')
            return temp
        elif (str(trig.trig).upper() == 'ATANH'):
            temp = tv.Temp()
            consola.append(f'\t{temp} = math.atanh({num})\n')
            return temp




    def obtenerCadenaEntrada(Trigo,condicion):
        #print('TRIGONOMETRICA -- '+Trigo.trig+'----' + type(Trigo).__name__ + '\n')


        if isinstance(Trigo,Trigonometrica):
            if Trigo.E2 == None:
                if isinstance(Trigo.E,Unario):
                    num = Expresion.Expresion.ObtenerCadenaEntrada(Trigo.E, condicion)
                    cadena = Trigo.trig + '(' + num + ') '
                else:
                    num= Trigonometrica.obtenerCadenaEntrada(Trigo.E,condicion)
                    cadena = Trigo.trig + '('+num+') '
            else:
                if isinstance(Trigo.E,Unario) and isinstance(Trigo.E2,Unario):
                    num1 = Expresion.Expresion.ObtenerCadenaEntrada(Trigo.E, condicion)
                    num2 = Expresion.Expresion.ObtenerCadenaEntrada(Trigo.E2, condicion)
                    cadena = Trigo.trig + '(' + num1 + ',' + num2 + ') '
                elif isinstance(Trigo.E,Unario):
                    num1 = Expresion.Expresion.ObtenerCadenaEntrada(Trigo.E, condicion)
                    num2 = Trigonometrica.obtenerCadenaEntrada(Trigo.E2,condicion)
                    cadena = Trigo.trig + '(' + num1 + ',' + num2 + ') '
                elif isinstance(Trigo.E2,Unario):
                    num1 = Trigonometrica.obtenerCadenaEntrada(Trigo.E,condicion)
                    num2 = Expresion.Expresion.ObtenerCadenaEntrada(Trigo.E2, condicion)
                    cadena = Trigo.trig + '(' + num1 + ',' + num2 + ') '
                else:
                    num1 = Trigonometrica.obtenerCadenaEntrada(Trigo.E,condicion)
                    num2 = Trigonometrica.obtenerCadenaEntrada(Trigo.E2,condicion)
                    cadena = Trigo.trig + '(' + num1+','+num2+ ') '

            return cadena


        elif isinstance(Trigo,Primitivo):
            return str(Primitivo.ObtenerCadenaEntrada(Trigo))
        elif isinstance(Trigo,Trigonometrica):
            return str(Trigonometrica.obtenerCadenaEntrada(Trigo,condicion))+' '
        elif isinstance(Trigo, Math.Math_):
            return str(Math.Math_.obtenerCadenaEntrada(Trigo,condicion))+' '
        elif isinstance(Trigo,Expresion.Expresion):
            return str(Expresion.Expresion.ObtenerCadenaEntrada(Trigo,condicion))
        elif isinstance(Trigo, Id):
            return str(Trigo.id)+' '
        elif isinstance(Trigo, IdId):
            return str(IdId.ObtenerCadenaEntrada(Trigo))

