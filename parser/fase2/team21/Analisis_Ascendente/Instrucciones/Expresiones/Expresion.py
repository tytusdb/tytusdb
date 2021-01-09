import  math

from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Binario import Binario
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion,IdId, Parametro
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Time import Time
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.expresion import *

import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica as Trigonometrica
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math as  Math
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Function.Llamada import Llamada
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Where as Where
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select.select as Select
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select.selectInst as SelectInst
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select.Select2 as Selectp3
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select.Select3 as Selectp4
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Function.Function as Function
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Procedure.Procedure as Procedure

class Expresion(Exp):
    def __init__(self, iz, dr, operador,fila,columna):
        self.iz = iz
        self.dr = dr
        self.operador = operador
        self.fila = fila
        self.columna = columna

    def Resolver(expr,ts,Consola,exception):

        if isinstance(expr,Expresion):
            exp1 = Expresion.Resolver(expr.iz,ts,Consola,exception)
            exp2 = Expresion.Resolver(expr.dr,ts,Consola,exception)

            if expr.operador == '=':
                return exp1 == exp2
            elif expr.operador == '*':

                # id = expresion
                # id = (x < 9 )
                if (isinstance(exp1,float) and isinstance(exp2,float)) or (isinstance(exp1,int) and isinstance(exp2,int)) or (isinstance(exp1,float) and isinstance(exp2,int))  or (isinstance(exp1,int) and isinstance(exp2,float)) :
                    return exp1 * exp2
                return 'error'
            elif expr.operador == '/':
                if (isinstance(exp1,float) and isinstance(exp2,float)) or (isinstance(exp1,int) and isinstance(exp2,int)) or (isinstance(exp1,float) and isinstance(exp2,int))  or (isinstance(exp1,int) and isinstance(exp2,float)) :
                    return exp1 /  exp2
                return 'error'
            elif expr.operador == '+':
                if (isinstance(exp1,float) and isinstance(exp2,float)) or (isinstance(exp1,int) and isinstance(exp2,int)) or (isinstance(exp1,float) and isinstance(exp2,int))  or (isinstance(exp1,int) and isinstance(exp2,float)):
                    return exp1 +  exp2
                return 'error'
            elif expr.operador == '-':
                if (isinstance(exp1,float) and isinstance(exp2,float)) or (isinstance(exp1,int) and isinstance(exp2,int)) or (isinstance(exp1,float) and isinstance(exp2,int))  or (isinstance(exp1,int) and isinstance(exp2,float)):
                    return exp1 -  exp2
                return 'error'
            elif expr.operador == '^':
                if (isinstance(exp1,float) and isinstance(exp2,float)) or (isinstance(exp1,int) and isinstance(exp2,int)) or (isinstance(exp1,float) and isinstance(exp2,int))  or (isinstance(exp1,int) and isinstance(exp2,float)):
                    return exp1 **  exp2
                return 'error'
            elif expr.operador == '%':
                if (isinstance(exp1,float) and isinstance(exp2,float)) or (isinstance(exp1,int) and isinstance(exp2,int)) or (isinstance(exp1,float) and isinstance(exp2,int))  or (isinstance(exp1,int) and isinstance(exp2,float)):
                    return exp1 %  exp2
                return 'error'
            elif expr.operador == '==': #comparacion---------------------------------------
                boole= exp1 == exp2
                return  boole
            elif expr.operador == '<>':
                boole = exp1 != exp2
                return boole
            elif expr.operador == '>':
                boole = exp1 > exp2
                return boole
            elif expr.operador == '<':

                boole = exp1 < exp2
                return boole
            elif expr.operador == '!=':
                boole = exp1 != exp2
                return boole
            elif expr.operador == '>=':
                boole = exp1 >= exp2
                return boole
            elif expr.operador == '<=':
                boole = exp1 <= exp2
                return boole
        elif isinstance(expr,Id):
            if ts.validar_sim(expr.id) == 1:
                return expr.id
            else:
                return 'holamundo'

        elif isinstance(expr, Primitivo):
            return expr.valor
        elif isinstance(expr, Trigonometrica.Trigonometrica):
            return Trigonometrica.Trigonometrica.Resolver(expr,ts,Consola,exception)
        elif isinstance(expr, Math.Math_):
            print("estoy llegango")
            return  Math.Math_.Resolver(expr,ts,Consola,exception)
        elif isinstance(expr,Time):
            return Time.resolverTime(expr)
        elif isinstance(expr,Binario):
            return Binario.Resolver(expr,ts,Consola,exception)
        elif isinstance(expr, Unario):
            exp1 = Expresion.Resolver(expr.op,ts,Consola,exception)
            if expr.operador == '-':
                if isinstance(exp1, int) or isinstance(exp1, float):
                    return exp1 * -1
            elif expr.operador == '+':
                if isinstance(exp1, int) or isinstance(exp1, float):
                    return exp1
            elif expr.operador == '!':
                    return not exp1

    #obtener la cadena de una expresion--------------------------------------------------
    def ObtenerCadenaEntrada(expr,condicion):

        if isinstance(expr,Expresion):

            exp1 = Expresion.ObtenerCadenaEntrada(expr.iz,condicion)
            exp2 = Expresion.ObtenerCadenaEntrada(expr.dr,condicion)
            if condicion:
                expresion = '('+exp1+" "+ str(expr.operador)+" " + exp2 +') '
            else:
                expresion = exp1 + " " + str(expr.operador) + " " + exp2
            return expresion
        elif isinstance(expr,Id):
            expresion = expr.id
            return str(expresion)
        elif isinstance(expr, Primitivo):
            expresion = Primitivo.ObtenerCadenaEntrada(expr)
            return str(expresion)
        elif isinstance(expr, Trigonometrica.Trigonometrica):
            expresion = Trigonometrica.Trigonometrica.obtenerCadenaEntrada(expr,condicion)
            return str(expresion)
        elif isinstance(expr, Math.Math_):
            expresion = Math.Math_.obtenerCadenaEntrada(expr,condicion)
            return str(expresion)
        elif isinstance(expr,Time):
            return  Time.ObtenerCadenaEntrada(expr)
        elif isinstance(expr,Binario):
            return str(Binario.ObtenerCadenaEntrada(expr,condicion))
        elif isinstance(expr, Unario):
            exp1 = Expresion.ObtenerCadenaEntrada(expr.op,condicion)
            return str(expr.operador)+exp1
        elif isinstance(expr, Llamada):
            llamada = Llamada.obtenerCadena(expr,condicion)
            return llamada
        elif isinstance(expr, IdId):
            idid= IdId.ObtenerCadenaEntrada(expr)
            return str(idid)
        elif isinstance(expr,Where.Where):
            wherwcad= Where.Where.ObtenerCadenaEntrada(expr)
            return  str(wherwcad)


    def ObtenerCadenaEntradaWhere(expr,lista_funcionesProcedimientos):

        if isinstance(expr,Expresion):

            exp1 = Expresion.ObtenerCadenaEntradaWhere(expr.iz,lista_funcionesProcedimientos)
            exp2 = Expresion.ObtenerCadenaEntradaWhere(expr.dr,lista_funcionesProcedimientos)

            expresion = exp1 + " " + str(expr.operador) + " " + exp2
            print('expre2'+str(exp2))
            return expresion
        elif isinstance(expr,Id):
            expresion = expr.id
            if lista_funcionesProcedimientos == None:
                return str(expresion)
            else:
                for func in lista_funcionesProcedimientos:
                    for param in func.parametros:
                        if isinstance(param,Parametro):
                            if param.id == expresion:
                                return ' {'+str(expresion)+'} '
            return str(expresion)
        elif isinstance(expr, Primitivo):
            expresion = Primitivo.ObtenerCadenaEntrada(expr)
            return str(expresion)
        elif isinstance(expr, Trigonometrica.Trigonometrica):
            expresion = Trigonometrica.Trigonometrica.obtenerCadenaEntrada(expr,False)
            return str(expresion)
        elif isinstance(expr, Math.Math_):
            expresion = Math.Math_.obtenerCadenaEntrada(expr,False)
            return str(expresion)
        elif isinstance(expr,Time):
            return  Time.ObtenerCadenaEntrada(expr)
        elif isinstance(expr,Binario):
            return str(Binario.ObtenerCadenaEntrada(expr,False))
        elif isinstance(expr, Unario):
            exp1 = Expresion.ObtenerCadenaEntradaWhere(expr.op,lista_funcionesProcedimientos)
            return str(expr.operador)+exp1
        elif isinstance(expr, Llamada):
            llamada = Llamada.obtenerCadena(expr,False)
            return llamada
        elif isinstance(expr, IdId):
            idid= IdId.ObtenerCadenaEntrada(expr)
            return str(idid)
        elif isinstance(expr,Where.Where):
            wherwcad= Where.Where.ObtenerCadenaEntrada(expr, lista_funcionesProcedimientos)

            print('CADENA WHERE'+wherwcad)
            return  str(wherwcad)




    def traducir(expre, ts, consola, exception, tv, regla, antes, optimizado, ID):
        #consola.append('\ten expresion\n')
        if isinstance(expre, Primitivo):
            if expre.cadena:
                #devolver cadenas con comillas
                return '\'' + str(expre.valor) + '\''
            elif str(expre.valor) == 'FALSE':
                return 'False'
            elif str(expre.valor) == 'TRUE':
                return 'True'
            else:
                return str(expre.valor)
        elif isinstance(expre, Id):
                return str(expre.id) #por el momento
        elif isinstance(expre, Llamada):
                print("aqui estoy")
                print(expre.listaE)
                print(expre.caso)
                concatena = ""
                if  len(expre.listaE) == 0:
                    concatena += Llamada.obtenerCadena(expre,2)
                else:
                    concatena += Llamada.obtenerCadena(expre,1)

                return str(f"{concatena}")
        elif isinstance(expre, Expresion):
            expre1 = Expresion.traducir(expre.iz, ts, consola, exception, tv, regla, antes, optimizado, ID)
            expre2 = Expresion.traducir(expre.dr, ts, consola, exception, tv, regla, antes, optimizado, ID)
            #pruebas de optimizacion
            bandera = True
            if expre.operador == '/':
                #regla 18   x = 0 / y -> x = 0
                if expre1 == '0':
                    bandera = False
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = 0\n')
                    regla.append('18')
                    antes.append(f'{temp} = 0 / {expre2}')
                    optimizado.append(f'{temp} = 0')
                    return temp
                elif expre2 == '0':
                    return 0
                elif expre2 == '1':
                    #var = v / 1
                    if ID != None and ID != 'IF': #asignacion o declaracion
                        if ID == expre1:
                            #regla 11 x = x / 1
                            regla.append('11')
                            antes.append(f'{ID} = {expre1} / 1')
                            optimizado.append('#Se elimina la instruccion')
                        else:
                            #regla 15 x = y / 1 -> x = y
                            regla.append('15')
                            antes.append(f'{ID} = {expre1} / 1')
                            optimizado.append(f'{ID} = {expre1}')
                            ####
                            temp = tv.Temp()
                            consola.append(f'\t{temp} = {expre1}\n')
                            return temp

            elif expre.operador == '*':
                #regla 17 x = y * 0 -> x = 0
                if expre1 == '0' or expre2 == '0':
                    bandera = False
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = 0\n')
                    regla.append('17')
                    antes.append(f'{temp} = {expre1} * {expre2}')
                    optimizado.append(f'{temp} = 0')
                    return temp
                #regla 16 x = y * 2 -> x = y + y
                elif expre1 == '2':
                    bandera = False
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = {expre2} + {expre2}\n')
                    regla.append('16')
                    antes.append(f'{temp} = {expre1} * {expre2}')
                    optimizado.append(f'{temp} = {expre2} + {expre2}')
                    return temp
                elif expre2 == '2':
                    bandera = False
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = {expre1} + {expre1}\n')
                    regla.append('16')
                    antes.append(f'{temp} = {expre1} * {expre2}')
                    optimizado.append(f'{temp} = {expre1} + {expre1}')
                    return temp
                elif expre2 == '1':
                    #var = v * 1
                    if ID != None and ID != 'IF': #es de asignacion o declaracion
                        if ID == expre1:
                            #regla 10 x = x * 1 -> se elimina
                            regla.append('10')
                            antes.append(f'{ID} = {expre1} * 1')
                            optimizado.append('#Se elimina la instruccion')
                        else:
                            #regla 14 x = y * 1 -> x = y
                            regla.append('14')
                            antes.append(f'{ID} = {expre1} * 1')
                            optimizado.append(f'{ID} = {expre1}')
                            temp = tv.Temp()
                            consola.append(f'\t{temp} = {expre1}\n')
                            return temp
                elif expre1 == '1':
                    #var = 1 * v
                    if ID != None and ID != 'IF': #asignacion o declaracion
                        if ID == expre2:
                            #regla 10 x = 1 * x -> se elimina
                            regla.append('10')
                            antes.append(f'{ID} = 1 * {expre2}')
                            optimizado.append('#Se elimina la instruccion')
                        else:
                            #regla 14 x = 1 * y -> x = y
                            regla.append('14')
                            antes.append(f'{ID} = 1 * {expre2}')
                            optimizado.append(f'{ID} = {expre2}')
                            temp = tv.Temp()
                            consola.append(f'\t{temp} = {expre2}\n')
                            return temp

            elif expre.operador == '+':
                #var = v + 0
                if expre2 == '0':
                    if ID != None and ID != 'IF': #es de asignacion o declaracion
                        if ID == expre1:
                            #regla 8 x = x + 0 -> se elimina
                            regla.append('8')
                            antes.append(f'{ID} = {expre1} + 0')
                            optimizado.append('#Se elimina la instruccion')
                        else:
                            #regla 12 x = y + 0 -> x = y
                            regla.append('12')
                            antes.append(f'{ID} = {expre1} + 0')
                            optimizado.append(f'{ID} = {expre1}')
                            temp = tv.Temp()
                            consola.append(f'\t{temp} = {expre1}\n')
                            return temp
                #var = 0 + v
                elif expre1 == '0':
                    if ID != None and ID != 'IF': #es de asignacion o declaracion
                        if ID == expre2:
                            #regla 8 x = 0 + x -> se elimina
                            regla.append('8')
                            antes.append(f'{ID} = 0 + {expre2}')
                            optimizado.append('#Se elimina la instruccion')
                        else:
                            #regla 12 x = 0 + y -> x = y
                            regla.append('12')
                            antes.append(f'{ID} = 0 + {expre2}')
                            optimizado.append(f'{ID} = {expre2}')
                            temp = tv.Temp()
                            consola.append(f'\t{temp} = {expre2}\n')
                            return temp

            elif expre.operador == '-':
                #var = v + 0
                if expre2 == '0':
                    if ID != None and ID != 'IF': #es de asignacion o declaracion
                        if ID == expre1:
                            #regla 9 x = x - 0 -> se elimina
                            regla.append('9')
                            antes.append(f'{expre1} = {expre1} - 0')
                            optimizado.append('#Se elimina la instruccion')
                        else:
                            #regla 13 x = y - 0 -> x = y
                            regla.append('13')
                            antes.append(f'{ID} = {expre1} - 0')
                            optimizado.append(f'{ID} = {expre1}')
                            temp = tv.Temp()
                            consola.append(f'\t{temp} = {expre1}\n')
                            return temp

            #booleanos
            elif expre.operador == '<' or expre.operador == '<=' or expre.operador == '>' or expre.operador == '>=' or expre.operador == '==' or expre.operador == '!=' or expre.operador == '=':
                if ID == 'IF':
                    if Expresion.esNumero(expre1) and Expresion.esNumero(expre2):
                        print('REGLA 4 o 5')
                        verdadero = False
                        if expre.operador == '<':
                            verdadero = expre1 < expre2
                        elif expre.operador == '<=':
                            verdadero = expre1 <= expre2
                        elif expre.operador == '>':
                            verdadero = expre1 > expre2
                        elif expre.operador == '>=':
                            verdadero = expre1 >= expre2
                        elif expre.operador == '==':
                            verdadero = expre1 == expre2
                        elif expre.operador == '!=':
                            verdadero = expre1 != expre2
                        elif expre.operador == '=':
                            verdadero = expre1 == expre2
                        if verdadero:
                            #regla 4
                            print('regla 4')
                            prim = tv.SiguienteEt()
                            v1 = prim[1:]
                            v1 = int(v1)
                            regla.append('4')
                            antes.append(f'if {tv.SiguienteTemp()}:<br> &nbsp goto .{prim}<br>else:<br> &nbsp goto .L{v1 + 1}')
                            optimizado.append(f'goto .{prim}')
                        else:
                            #regla 5
                            print('regla 5')
                            prim = tv.SiguienteEt()
                            v1 = prim[1:]
                            v1 = int(v1)
                            regla.append('5')
                            antes.append(f'if {tv.SiguienteTemp()}:<br> &nbsp goto .{prim}<br>else:<br> &nbsp goto .L{v1 + 1}')
                            optimizado.append(f'goto .L{v1 + 1}')
                    else:
                        print('No SON NUMEROS')


            if bandera:
                temp = tv.Temp()
                if expre.operador == '=':
                    expre.operador = '=='
                consola.append(f'\t{temp} = {expre1} {expre.operador} {expre2}\n')
                return temp
        elif isinstance(expre, Unario):
            expre1 = Expresion.traducir(expre.op, ts, consola, exception, tv, regla, antes, optimizado, ID)
            temp = tv.Temp()
            operador = expre.operador
            if expre.operador == '!':
                operador = 'not'
            consola.append(f'\t{temp} = {operador}{expre1}\n')
            return temp
        elif isinstance(expre, Math.Math_):
            return  Math.Math_.traducir(expre, ts, consola, exception, tv, regla, antes, optimizado, ID)
        elif isinstance(expre, Binario):
            return Binario.traducir(expre, ts, consola, exception, tv, regla, antes, optimizado, ID)
        elif isinstance(expre, Trigonometrica.Trigonometrica):
            return Trigonometrica.Trigonometrica.traducir(expre, ts, consola, exception, tv, regla, antes, optimizado, ID)
        elif isinstance(expre, Select.Select):
            print('ES UN SELECT ')
            val=''

            if (expre.caso == 1):
                a = Time.resolverTime(expre.time)
                val = str(a)
                print('caso<3---')
                print(str(expre.caso))
                return a
            elif (expre.caso == 3):
                variable = SelectInst.Select_inst()
                trash = []
                a = SelectInst.Select_inst.ejecutar(variable, expre, ts, trash, exception)
                print("-------------------------------------------------------")
                print("\n")


                print("valor", a)

                print("----------------------------------------------------------")
                for val in a:
                    try:
                        print('valor' + str(val[0]))
                        return str(val[0])
                    except:
                        return 0

            elif (expre.caso == 4):
                print(expre)
                a = Selectp3.Selectp3.ejecutar(expre, ts, consola, exception, False)
                print("veamos")
                print(a)
                for val in a[1]:
                    print('valor' + str(val))
                    return str(val)

            elif (expre.caso == 5):
                a = Selectp4.Selectp4.ejecutar(expre, ts, consola, exception, False)
                print('ACAAAAAAA')
                for val in a[1]:
                    print('valor'+str(val[0]))
                    return str(val[0])
        elif isinstance(expre, Time):
            print('traduciendo time')
            return Time.traducir(expre, ts, consola, exception, tv)


    def esNumero(valor) -> bool:
        try:
            int(valor)
            return True
        except:
            try:
                float(valor)
                return True
            except:
                return False