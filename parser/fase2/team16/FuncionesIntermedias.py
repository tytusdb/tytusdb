import Gramatica as Gram
import interprete as Inter
from Instruccion import *
from Instruccion import heap as hp
heap = hp

def ejecutarSQL():
    cadena = heap[-1]

    nueva = str(cadena).upper()
    #print(nueva)
    Inter.inicializarEjecucionAscendente(cadena)
    #Inter.Ejecucion():
    # if len(Lista) > 0:
    #     self.consola.insert('insert', Lista[0])
    # else:
    #     return


def funcionNativa():
    idfuncion = heap[-1]

    if idfuncion == FUNCION_NATIVA.PI.value:
        return Inter.procesar_expresion(ExpresionFuncion(None, None, None, None, FUNCION_NATIVA.PI), None)
    elif idfuncion == FUNCION_NATIVA.RANDOM.value:
        return Inter.procesar_expresion(ExpresionFuncion(None, None, None, None, FUNCION_NATIVA.RANDOM), None)
    elif idfuncion == FUNCION_NATIVA.NOW.value:
        return Inter.procesar_expresion(ExpresionFuncion(None, None, None, None, FUNCION_NATIVA.NOW), None)

    val = heap[-2]
    exp1 = ExpresionValor(val)
    if idfuncion == FUNCION_NATIVA.ABS.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.ABS), None)
    
    elif idfuncion == FUNCION_NATIVA.CBRT.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.CBRT), None)

    elif idfuncion == FUNCION_NATIVA.CEIL.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.CEIL), None)

    elif idfuncion == FUNCION_NATIVA.CEILING.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.CEILING), None)

    elif idfuncion == FUNCION_NATIVA.DEGREES.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.DEGREES), None)

    elif idfuncion == FUNCION_NATIVA.EXP.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.EXP), None)

    elif idfuncion == FUNCION_NATIVA.FACTORIAL.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.FACTORIAL), None)

    elif idfuncion == FUNCION_NATIVA.FLOOR.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.FLOOR), None)

    elif idfuncion == FUNCION_NATIVA.LN.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.LN), None)

    elif idfuncion == FUNCION_NATIVA.LOG.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.LOG), None)

    elif idfuncion == FUNCION_NATIVA.RADIANS.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.RADIANS), None)

    elif idfuncion == FUNCION_NATIVA.SIGN.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.SIGN), None)

    elif idfuncion == FUNCION_NATIVA.SQRT.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.SQRT), None)

    elif idfuncion == FUNCION_NATIVA.ACOS.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.ACOS), None)

    elif idfuncion == FUNCION_NATIVA.ACOSD.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.ACOSD), None)

    elif idfuncion == FUNCION_NATIVA.ASIN.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.ASIN), None)

    elif idfuncion == FUNCION_NATIVA.ASIND.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.ASIND), None)

    elif idfuncion == FUNCION_NATIVA.ATAN.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.ATAN), None)

    elif idfuncion == FUNCION_NATIVA.ATAND.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.ATAND), None)

    elif idfuncion == FUNCION_NATIVA.COS.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.COS), None)

    elif idfuncion == FUNCION_NATIVA.COSD.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.COSD), None)

    elif idfuncion == FUNCION_NATIVA.COT.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.COT), None)

    elif idfuncion == FUNCION_NATIVA.COTD.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.COTD), None)

    elif idfuncion == FUNCION_NATIVA.SIN.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.SIN), None)

    elif idfuncion == FUNCION_NATIVA.SIND.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.SIND), None)

    elif idfuncion == FUNCION_NATIVA.TAN.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.TAN), None)

    elif idfuncion == FUNCION_NATIVA.TAND.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.TAND), None)

    elif idfuncion == FUNCION_NATIVA.SINH.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.SINH), None)

    elif idfuncion == FUNCION_NATIVA.COSH.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.COSH), None)

    elif idfuncion == FUNCION_NATIVA.TANH.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.TANH), None)

    elif idfuncion == FUNCION_NATIVA.ASINH.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.ASINH), None)

    elif idfuncion == FUNCION_NATIVA.ACOSH.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.ACOSH), None)

    elif idfuncion == FUNCION_NATIVA.ATANH.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.ATANH), None)

    elif idfuncion == FUNCION_NATIVA.ROUND.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.ROUND), None)

    elif idfuncion == FUNCION_NATIVA.LENGTH.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.LENGTH), None)

    elif idfuncion == FUNCION_NATIVA.MD5.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.MD5), None)

    elif idfuncion == FUNCION_NATIVA.SHA256.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, None, None, None, FUNCION_NATIVA.SHA256), None)

    val = heap[-3]
    exp2 = ExpresionValor(val)

    if idfuncion == FUNCION_NATIVA.DIV.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, exp2, None, None, FUNCION_NATIVA.DIV), None)

    elif idfuncion == FUNCION_NATIVA.GCD.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, exp2, None, None, FUNCION_NATIVA.GCD), None)

    elif idfuncion == FUNCION_NATIVA.MOD.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, exp2, None, None, FUNCION_NATIVA.MOD), None)

    elif idfuncion == FUNCION_NATIVA.POWER.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, exp2, None, None, FUNCION_NATIVA.POWER), None)

    elif idfuncion == FUNCION_NATIVA.TRUNC.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, exp2, None, None, FUNCION_NATIVA.TRUNC), None)

    elif idfuncion == FUNCION_NATIVA.ATAN2.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, exp2, None, None, FUNCION_NATIVA.ATAN2), None)

    elif idfuncion == FUNCION_NATIVA.ATAN2D.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, exp2, None, None, FUNCION_NATIVA.ATAN2D), None)

    elif idfuncion == FUNCION_NATIVA.EXTRACT.value:
        val2 = heap[-3]
        time = None
        if val2 == "HOUR":
            time = UNIDAD_TIEMPO.HOUR
        elif val2 == "MINUTE":
            time = UNIDAD_TIEMPO.MINUTE
        elif val2 == "SECOND":
            time = UNIDAD_TIEMPO.SECOND
        elif val2 == "YEAR":
            time = UNIDAD_TIEMPO.YEAR
        elif val2 == "MONTH":
            time = UNIDAD_TIEMPO.MONTH
        elif val2 == "DAY":
            time = UNIDAD_TIEMPO.DAY

        exp2 = ExpresionTiempo(val, time)
        return Inter.procesar_expresion(ExpresionFuncion(exp1, exp2, None, None, FUNCION_NATIVA.EXTRACT), None)

    elif idfuncion == FUNCION_NATIVA.DATE_PART.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, exp2, None, None, FUNCION_NATIVA.DATE_PART), None)

    elif idfuncion == FUNCION_NATIVA.TRIM.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, exp2, None, None, FUNCION_NATIVA.TRIM), None)

    val = heap[-4]
    exp3 = ExpresionValor(val)
    
    if idfuncion == FUNCION_NATIVA.SUBSTRING.value or idfuncion == FUNCION_NATIVA.SUBSTR.value:
        return Inter.procesar_expresion(ExpresionFuncion(exp1, exp2, exp3, None, FUNCION_NATIVA.SUBSTRING), None)

def insert():
    id_tabla = [ExpresionValor(heap[-1])]
    nval = heap[-2]
    inval = 1
    valores = []

    while inval <= nval:
        valores.append(ExpresionValor(heap[-2 - inval]))
        inval += 1

    insertDatos = Insert_Datos(id_tabla, valores)
    insertDatos.Ejecutar()





