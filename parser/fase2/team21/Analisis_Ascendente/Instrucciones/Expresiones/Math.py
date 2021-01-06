import  math
import random
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import *
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.expresion import *
import  tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica as  Trigonometrica
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion as Expresion
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.IdAsId as IdAsId
import hashlib
class Math_(Instruccion):
    def __init__(self, nombre, E1, E2,fila,columna):
        self.nombre = nombre
        self.E1 = E1
        self.E2 = E2
        self.fila = fila
        self.columna = columna


    def Resolver(mathe,ts, Consola,exceptions):

        #Consola.append('E1 -- ' + mathe.nombre + '\n')
        #Consola.append('E2 -- ' + type(mathe.E2).__name__ + '\n')


        if isinstance(mathe,Math_):
            if mathe.E1 == None and mathe.E2 == None:
                if mathe.nombre == 'PI':
                    return math.pi
                elif mathe.nombre == 'RANDOM':
                    return random.random()
            else:


                if mathe.E2 == None: # operaciones de un valor
                    num1 = Math_.Resolver(mathe.E1,ts,Consola,exceptions)
                    if mathe.nombre == 'LN' or mathe.nombre == 'LOG':
                        return math.log(float(num1))
                    elif mathe.nombre == 'ABS':
                        return  abs(num1)
                    elif mathe.nombre == 'CBRT':
                        return num1 ** (1/3)
                    elif mathe.nombre == 'CEIL' or mathe.nombre == 'CEILING':
                        return math.ceil(num1)
                    elif mathe.nombre == 'DEGREES':
                        return  math.degrees(num1)
                    elif mathe.nombre == 'EXP':
                        return math.exp(num1)
                    elif mathe.nombre == 'FACTORIAL':
                        return math.factorial(int(num1))
                    elif mathe.nombre == 'FLOOR':
                        return  math.floor(num1)
                    elif mathe.nombre == 'LOG10':
                        return  math.log10(num1)
                    elif mathe.nombre == 'RADIANS':
                        return  math.radians(num1)
                    elif mathe.nombre == 'ROUND':
                        return  round(num1)
                    elif mathe.nombre == 'SIGN':
                        if num1 >= 0:
                            return 1
                        else:
                            return  -1
                    elif mathe.nombre == 'SQRT':
                        return  math.sqrt(num1)
                    elif mathe.nombre == 'TRUNC':
                        return  math.trunc(num1)
                    elif mathe.nombre == 'SUM':
                         return math.fsum(num1)
                    elif mathe.nombre == 'MD5':
                        return hashlib.md5(str(num1).encode("utf-8")).hexdigest()
                    elif mathe.nombre == 'WIDTH_BUCKET':
                        print("whidth bucket")
                        print(mathe.E1)
                        elementos = mathe.E1

                        valor = elementos[0].valor
                        min = elementos[1].valor
                        max = elementos[2].valor
                        count = elementos[3].valor


                        temp = (max - min) / count
                        contador = float(min)
                        cubo = 0
                        if float(valor) == contador:
                            return 1
                        while contador < float(max):
                            if float(valor) < contador:
                                return cubo

                            contador += temp
                            cubo += 1

                        return cubo + 1


                else:
                    num1 = Math_.Resolver(mathe.E1,ts,Consola,exceptions)
                    num2 = Math_.Resolver(mathe.E2,ts,Consola,exceptions)
                    if mathe.nombre == 'DIV':
                        return num1/num2
                    elif mathe.nombre == 'GCD':
                        return math.gcd(num1,num2)
                    elif mathe.nombre == 'MOD':
                        return num1 % num2
                    elif mathe.nombre == 'POWER':
                        return  num1 ** num2
        elif isinstance(mathe, Trigonometrica.Trigonometrica):
            return Trigonometrica.Trigonometrica.Resolver(mathe,ts,Consola,exceptions)
        elif isinstance(mathe,Math_):
            return Math_.Resolver(mathe,ts,Consola,exceptions)
        elif isinstance(mathe, Primitivo):
            return  mathe.valor
        elif isinstance(mathe, Expresion.Expresion):
            return Expresion.Expresion.Resolver(mathe,ts,Consola,exceptions)
        elif isinstance(mathe, Unario):
            return Expresion.Expresion.Resolver(mathe,ts,Consola,exceptions)


    def obtenerCadenaEntrada(mathe,condicion):
        if isinstance(mathe,Math_):
            if mathe.E1 == None and mathe.E2 == None:
                if mathe.nombre == 'PI':
                    return 'PI() '
                elif mathe.nombre == 'RANDOM':
                    return 'RANDOM() '
            else:

                if mathe.E2 == None:  # operaciones de un valor
                    if isinstance(mathe.E1,Unario):
                        num1 = Expresion.Expresion.ObtenerCadenaEntrada(mathe.E1,condicion)
                        return mathe.nombre + '(' + str(num1) + ') '
                    else:
                        num1 = Math_.obtenerCadenaEntrada(mathe.E1, condicion)
                        return mathe.nombre + '(' + str(num1) + ') '
                else:
                    if isinstance(mathe.E1, Unario) and isinstance(mathe.E2, Unario):
                        num1 = Expresion.Expresion.ObtenerCadenaEntrada(mathe.E1,condicion)
                        num2 = Expresion.Expresion.ObtenerCadenaEntrada(mathe.E2,condicion)
                        return mathe.nombre + '(' + str(num1) + ',' + str(num2) + ') '
                    elif isinstance(mathe.E1, Unario):
                        num1 = Expresion.Expresion.ObtenerCadenaEntrada(mathe.E1,condicion)
                        num2 = Math_.obtenerCadenaEntrada(mathe.E2, condicion)
                        return mathe.nombre + '(' + str(num1) + ',' + str(num2) + ') '
                    elif isinstance(mathe.E2, Unario):
                        num1 = Math_.obtenerCadenaEntrada(mathe.E1, condicion)
                        num2 = Expresion.Expresion.ObtenerCadenaEntrada(mathe.E2,condicion)
                        return mathe.nombre + '(' + str(num1) + ',' + str(num2) + ') '
                    else:
                        num1 = Math_.obtenerCadenaEntrada(mathe.E1,condicion)
                        num2 = Math_.obtenerCadenaEntrada(mathe.E2,condicion)
                        return mathe.nombre+'('+ str(num1)+','+str(num2)+') '
        elif isinstance(mathe, Trigonometrica.Trigonometrica):
            return str(Trigonometrica.Trigonometrica.obtenerCadenaEntrada(mathe,condicion))
        elif isinstance(mathe,Math_):
            return str(Math_.obtenerCadenaEntrada(mathe,condicion))
        elif isinstance(mathe, Primitivo):
            return  str(Primitivo.ObtenerCadenaEntrada(mathe))
        elif isinstance(mathe, Expresion.Expresion):
            expresion = str(Expresion.Expresion.ObtenerCadenaEntrada(mathe,condicion))
            return expresion
        elif isinstance(mathe,list):
            valores=''
            cont=0
            for val in mathe:
                if isinstance(val,Primitivo):
                    valores+=Primitivo.ObtenerCadenaEntrada(val)+' '
                cont += 1
                if cont < len(mathe):
                    valores += ', '
                else:
                    valores += ' '
            return valores
        elif isinstance(mathe,Id):
            return str(mathe.id)
        elif isinstance(mathe,IdId):
            return str(IdId.ObtenerCadenaEntrada(mathe))
        elif isinstance(mathe, IdAsId.IdAsId):
            return str(IdAsId.IdAsId.ObtenerCadenaEntrada(mathe))



    def traducir(mathe, ts, consola, exception, tv, regla, antes, optimizado, ID):
        if mathe.E1 == None and mathe.E2 == None:
            if mathe.nombre == 'PI':
                temp = tv.Temp()
                consola.append(f'\t{temp} = math.pi\n')
                return temp
            elif mathe.nombre == 'RANDOM':
                temp = tv.Temp()
                consola.append(f'\t{temp} = random.random()\n')
                return temp
        else:
            if mathe.E2 == None:  # operaciones de un valor
                num1 = Expresion.Expresion.traducir(mathe.E1, ts, consola, exception, tv, regla, antes, optimizado, ID)
                if mathe.nombre == 'LN' or mathe.nombre == 'LOG':
                    temp1 = tv.Temp()
                    consola.append(f'\t{temp1} = float({num1})\n')
                    temp2 = tv.Temp()
                    consola.append(f'\t{temp2} = math.log({temp1})\n')
                    return temp2
                elif mathe.nombre == 'ABS':
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = abs({num1})\n')
                    return temp
                elif mathe.nombre == 'CBRT': #========================
                    return num1 ** (1 / 3)
                elif mathe.nombre == 'CEIL' or mathe.nombre == 'CEILING':
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = math.ceil({num1})\n')
                    return temp
                elif mathe.nombre == 'DEGREES':
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = math.degrees({num1})\n')
                    return temp
                elif mathe.nombre == 'EXP':
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = math.exp({num1})\n')
                    return temp
                elif mathe.nombre == 'FACTORIAL':
                    temp1 = tv.Temp()
                    consola.append(f'\t{temp1} = int({num1})\n')
                    temp2 = tv.Temp()
                    consola.append(f'\t{temp2} = math.factorial({temp1})\n')
                    return temp2
                elif mathe.nombre == 'FLOOR':
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = math.floor({num1})\n')
                    return temp
                elif mathe.nombre == 'LOG10':
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = math.log10({num1})\n')
                    return temp
                elif mathe.nombre == 'RADIANS':
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = math.radians({num1})\n')
                    return temp
                elif mathe.nombre == 'ROUND':
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = round({num1})\n')
                    return temp
                elif mathe.nombre == 'SIGN':
                    if num1 >= 0:
                        return 1
                    else:
                        return -1
                elif mathe.nombre == 'SQRT':
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = math.sqrt({num1})\n')
                    return temp
                elif mathe.nombre == 'TRUNC':
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = math.trunc({num1})\n')
                    return temp
                elif mathe.nombre == 'SUM':
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = math.fsum({num1})\n')
                    return temp
                elif mathe.nombre == 'MD5':
                    temp1 = tv.Temp()
                    consola.append(f'\t{temp1} = str({num1})\n')
                    temp2 = tv.Temp()
                    consola.append(f'\t{temp2} = {temp1}.encode("utf-8")\n')
                    temp3 = tv.Temp()
                    consola.append(f'\t{temp3} = hashlib.md5({temp2})\n')
                    temp4 = tv.Temp()
                    consola.append(f'\t{temp4} = {temp3}.hexdigest()\n')
                    return temp4
                elif mathe.nombre == 'WIDTH_BUCKET':
                    print("whidth bucket")
                    consola.append('\t#whidth bucket\n')
                    print(mathe.E1)
                    elementos = mathe.E1

                    valor = elementos[0].valor
                    min = elementos[1].valor
                    max = elementos[2].valor
                    count = elementos[3].valor
                    #---------
                    tvalor = tv.Temp()
                    consola.append(f'\t{tvalor} = {valor}\n')
                    tmin = tv.Temp()
                    consola.append(f'\t{tmin} = {min}\n')
                    tmax = tv.Temp()
                    consola.append(f'\t{tmax} = {max}\n')
                    tcount = tv.Temp()
                    consola.append(f'\t{tcount} = {count}\n')

                    temp = (max - min) / count
                    #-----------
                    resta = tv.Temp()
                    consola.append(f'\t{resta} = {tmax} - {tmin}\n')
                    division = tv.Temp()
                    consola.append(f'\t{division} = {resta} / {tcount}\n')

                    contador = float(min)
                    cubo = 0
                    #-----------
                    tcontador = tv.Temp()
                    consola.append(f'\t{tcontador} = float({tmin})\n')
                    tcubo = tv.Temp()
                    consola.append(f'\t{tcubo} = 0\n')
                    #-------------- primer if
                    casteo = tv.Temp()
                    consola.append(f'\t{casteo} = float({tvalor})\n')
                    condicion = tv.Temp()
                    consola.append(f'\t{condicion} = {casteo} == {tcontador}\n')
                    tresultado = tv.Temp()
                    consola.append(f'\t{tresultado} = 1\n')
                    verdadero = tv.Et()
                    falso = tv.Et()
                    consola.append('\tif ' + condicion + ':\n\t\t goto .' + verdadero + '\n')
                    consola.append(f'\telse:\n\t\tgoto .{falso}\n')
                    consola.append(f'\tlabel .{verdadero}\n')
                    consola.append(f'\t{tresultado} = 1\n')
                    #saltarse el while
                    inicial = tv.Et()
                    verdadero2 = tv.Et()
                    falso2 = tv.Et()
                    consola.append(f'\tgoto .{falso2}\n')
                    consola.append(f'\tlabel .{falso}\n')
                    #if float(valor) == contador:
                    #    return 1
                    #-----------------------while
                    casteo2 = tv.Temp()
                    consola.append(f'\t{casteo2} = float({tmax})\n')
                    condicion2 = tv.Temp()
                    consola.append(f'\tlabel .{inicial}\n')
                    consola.append(f'\t{condicion2} = {tcontador} < {casteo2}\n')
                    consola.append('\tif ' + condicion2 + ':\n\t\t goto .' + verdadero2 + '\n')
                    consola.append(f'\telse:\n\t\tgoto .{falso2}\n')
                    consola.append(f'\tlabel .{verdadero2}\n')
                    #otro if
                    condicion3 = tv.Temp()
                    consola.append(f'\t{condicion3} = {casteo} < {tcontador}\n')
                    verdadero3 = tv.Et()
                    falso3 = tv.Et()
                    consola.append('\tif ' + condicion3 + ':\n\t\t goto .' + verdadero3 + '\n')
                    consola.append(f'\telse:\n\t\tgoto .{falso3}\n')
                    consola.append(f'\tlabel .{verdadero3}\n')

                    consola.append(f'\t{tresultado} = {tcubo}\n')
                    #salir de while
                    consola.append(f'\tgoto .{falso2}\n')
                    consola.append(f'\tlabel .{falso3}\n')
                    consola.append(f'\t{tcontador} = {tcontador} + {division}\n')
                    consola.append(f'\t{tcubo} = {tcubo} + 1\n')
                    consola.append(f'\tgoto .{inicial}\n')
                    consola.append(f'\tlabel .{falso2}\n')

                    #while contador < float(max):
                    #    if float(valor) < contador:
                    #        return cubo

                    #    contador += temp
                    #    cubo += 1

                    #return cubo + 1 #eso para que es?

                    return tresultado

            else:
                num1 = Expresion.Expresion.traducir(mathe.E1, ts, consola, exception, tv, regla, antes, optimizado, ID)
                num2 = Expresion.Expresion.traducir(mathe.E2, ts, consola, exception, tv, regla, antes, optimizado, ID)
                if mathe.nombre == 'DIV':
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = {num1} / {num2}\n')
                    return temp
                elif mathe.nombre == 'GCD':
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = math.gcd({num1}, {num2})\n')
                    return temp
                elif mathe.nombre == 'MOD':
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = {num1} % {num2}\n')
                    return temp
                elif mathe.nombre == 'POWER':
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = {num1} ** {num2}\n')
                    return temp

