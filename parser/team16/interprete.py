from Instruccion import *
from graphviz import Graph
from graphviz import escape
from expresiones import *
from Ast2 import *
from six import string_types
import ts as TS
from errores import *
import Gramatica as g
import jsonMode as Master
import math
from random import random
from datetime import datetime
import re
import IntervalParser
import hashlib
from dateutil.relativedelta import relativedelta

##------------------------------------------
# TABLA DE SIMBOLOS GLOBAL
ts_global = TS.TablaDeSimbolos()
# TABLA DE ERRORES GLOBAL
LisErr = TablaError([])
# ===========================
instrucciones = []
editor = None
consola = None
content = ''

baseInterprete = baseActual


# INICIALIZACION DE MAIN==============================================
# ========================================================================
def limpiarValores():
    global ts_global, instrucciones, indice, tag, LisErr
    ts_global = TS.TablaDeSimbolos
    instrucciones = []
    indice = 0
    tag = ''
    LisErr = TablaError([])


def inicializarEjecucionAscendente(contenido):
    global LisErr, instrucciones, ts_global
    ts_global = TS.TablaDeSimbolos()
    instrucciones = g.parse(contenido, LisErr)
   # reporte_errores()


def inicializarTS():
    global instrucciones, ts_global, tag
    # save_main('main',ts_global,1)
    # fill_tags(instrucciones,ts_global)
    # consola.insert('end',"\n>> ********  Start  ******** \n>>")
    # tag='main'
    # if not comprobarMain(instrucciones):
    # consola.insert('end',">>Error: Verifique errores lexicos y sintacticos\n>>")


# ========================================================================
# ========================================================================

# EJECUTANDO EXPRESIONES============================
# VERIFICANDO QUE TIPO DE EXPRESION ES
def procesar_expresion(expresiones, ts):

    if isinstance(expresiones, ExpresionAritmetica):
        return procesar_aritmetica(expresiones, ts)
    elif isinstance(expresiones, ExpresionRelacional):
        return procesar_relacional(expresiones, ts)
    elif isinstance(expresiones, ExpresionLogica):
        return procesar_logica(expresiones, ts)
    elif isinstance(expresiones, UnitariaNegAritmetica):
        return procesar_negAritmetica(expresiones, ts)
    elif isinstance(expresiones, UnitariaLogicaNOT):
        return procesar_logicaNOT(expresiones, ts)
    elif isinstance(expresiones, UnitariaNotBB):
        return procesar_NotBB(expresiones, ts)
    elif isinstance(expresiones, ExpresionValor):
        return expresiones.val
    elif isinstance(expresiones, Variable):
        return procesar_variable(expresiones, ts)
    elif isinstance(expresiones, UnitariaAritmetica):
        return procesar_unitaria_aritmetica(expresiones, ts)
    elif isinstance(expresiones, ExpresionFuncion):
        return procesar_funcion(expresiones, ts)
    elif isinstance(expresiones, ExpresionTiempo):
        return procesar_unidad_tiempo(expresiones, ts)
    elif isinstance(expresiones, ExpresionConstante):
        return procesar_constante(expresiones, ts)
    elif isinstance(expresiones, Absoluto):
        try:
            return procesar_expresion(expresiones.variable, ts)
        # return abs(procesar_expresion(expresiones.variable,ts))
        except:
            print('Error no se puede aplicar abs() por el tipo de dato')
            # consola.insert('end','>>Error: No se puede aplicar abs() al tipo de dato\n>>')
            # newErr=ErrorRep('Semantico','No se puede aplicar abs() al tipo de dato ',indice)
            # LisErr.agregar(newErr)
            return None
    else:
        print(expresiones)
        print('Error:Expresion no reconocida')


def procesar_aritmetica(expresion, ts):
    global LisErr
    val = procesar_expresion(expresion.exp1, ts)
    val2 = procesar_expresion(expresion.exp2, ts)

    if expresion.operador == OPERACION_ARITMETICA.MAS:
        if ((isinstance(val, int) or isinstance(val, float))
              and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val + val2
        else:
            agregarErrorDatosOperacion(val, val2, "+", "numerico", 0,0)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.MENOS:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val - val2
        else:
            agregarErrorDatosOperacion(val, val2, "-", "numerico", 0,0)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.MULTI:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val * val2
        else:
            agregarErrorDatosOperacion(val, val2, "*", "numerico", 0,0)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.DIVIDIDO:
        if val2 == 0:
            agregarErrorDatosOperacion(val, val2, "/", "numerico diferente de 0 en el segundo parametro", 0, 0)
            return None
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val / val2
        else:
            agregarErrorDatosOperacion(val, val2, "/", "numerico", 0,0)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.RESIDUO:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val % val2
        else:
            agregarErrorDatosOperacion(val, val2, "/", "numerico", 0,0)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.POTENCIA:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return pow(val, val2)
        else:
            agregarErrorDatosOperacion(val, val2, "%", "numerico", 0,0)
            return None
    elif expresion.operador == OPERACION_BIT_A_BIT.AND:
        if isinstance(val, int) and isinstance(val2, int):
            return val & val2
        else:
            agregarErrorDatosOperacion(val, val2, "&", "entero", 0,0)
            return None
    elif expresion.operador == OPERACION_BIT_A_BIT.OR:
        if isinstance(val, int) and isinstance(val2, int):
            return val | val2
        else:
            agregarErrorDatosOperacion(val, val2, "|", "entero", 0,0)
            return None
    elif expresion.operador == OPERACION_BIT_A_BIT.XOR:
        if isinstance(val, int) and isinstance(val2, int):
            return val ^ val2
        else:
            agregarErrorDatosOperacion(val, val2, "#", "entero", 0,0)
            return None
    elif expresion.operador == OPERACION_BIT_A_BIT.SHIFT_DER:
        if isinstance(val, int) and isinstance(val2, int):
            return val >> val2
        else:
            agregarErrorDatosOperacion(val, val2, ">>", "entero", 0,0)
            return None
    elif expresion.operador == OPERACION_BIT_A_BIT.SHIFT_IZQ:
        if isinstance(val, int) and isinstance(val2, int):
            return val << val2
        else:
            agregarErrorDatosOperacion(val, val2, "<<", "entero", 0,0)
            return None

def procesar_relacional(expresion, ts):
    val = procesar_expresion(expresion.exp1, ts)
    val2 = procesar_expresion(expresion.exp2, ts)

    if (isinstance(val, int) and isinstance(val2, float)
            or isinstance(val, float) and isinstance(val2, int)
            or isinstance(val, float) and isinstance(val2, float)
            or isinstance(val, int) and isinstance(val2, int)):
        if expresion.operador == OPERACION_RELACIONAL.IGUALQUE:
            return 1 if (val == val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.DISTINTO:
            return 1 if (val != val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MAYORIGUAL:
            return 1 if (val >= val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MENORIGUAL:
            return 1 if (val <= val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MAYORQUE:
            return 1 if (val > val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MENORQUE:
            return 1 if (val < val2) else 0
    elif isinstance(val, string_types) and isinstance(val2, string_types):
        if expresion.operador == OPERACION_RELACIONAL.IGUALQUE:
            return 1 if (val == val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.DISTINTO:
            return 1 if (val != val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MAYORIGUAL:
            return 1 if (val >= val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MENORIGUAL:
            return 1 if (val <= val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MAYORQUE:
            return 1 if (val > val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MENORQUE:
            return 1 if (val < val2) else 0
    elif (isinstance(val[0], DatoInsert) and isinstance(val2, int)
          or isinstance(val[0], DatoInsert) and isinstance(val2, int)
          or isinstance(val[0], DatoInsert) and isinstance(val2, float)
          or isinstance(val[0], DatoInsert) and isinstance(val2, int) ):

        if expresion.operador == OPERACION_RELACIONAL.IGUALQUE:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if int(Vd.valor) == val2:
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.DISTINTO:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if int(Vd.valor) != val2:
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MAYORIGUAL:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if int(Vd.valor) >= val2:
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MENORIGUAL:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if int(Vd.valor) <= val2:
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MAYORQUE:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if int(Vd.valor) > val2:
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MENORQUE:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if int(Vd.valor) < val2:
                    listaV.append(Vd)
            return listaV
    elif isinstance(val[0], DatoInsert) and isinstance(val2, string_types):
        if expresion.operador == OPERACION_RELACIONAL.IGUALQUE:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if str(Vd.valor) == val2:
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.DISTINTO:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if str(Vd.valor) != val2:
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MAYORIGUAL:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if str(Vd.valor) >= val2:
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MENORIGUAL:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if str(Vd.valor) <= val2:
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MAYORQUE:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if str(Vd.valor) > val2:
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MENORQUE:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if str(Vd.valor) < val2:
                    listaV.append(Vd)
            return listaV
    else:
        print('Error: Expresion relacional con tipos incompatibls')
        # consola.insert('end','>>Error: Expresion relacional con tipos incompatibles'+str(expresion.operador)+'\n>>')
        # newErr=ErrorRep('Semantico','Expresion relacional con tipos incompatibles '+str(expresion.operador),indice)
        # LisErr.agregar(newErr)
        return None


def procesar_logica(expresion, ts):
    print("Logica en LOGICA")
    val = procesar_expresion(expresion.exp1, ts)
    val2 = procesar_expresion(expresion.exp2, ts)

    if ((isinstance(val, int) or isinstance(val, float))
            and ((isinstance(val2, int) or isinstance(val2, float)))):
        if expresion.operador == OPERACION_LOGICA.AND:
            return 1 if (val and val2) else 0
        elif expresion.operador == OPERACION_LOGICA.OR:
            return 1 if (val or val2) else 0
        elif expresion.operador ==OPERACION_LOGICA.IS_DISTINCT:
            return 1 if (val != val2) else 0
        elif expresion.operador == OPERACION_LOGICA.IS_NOT_DISTINCT:
            return 1 if (val == val2) else 0
    elif (isinstance(val[0], DatoInsert) and isinstance(val2[0], DatoInsert)):
        if expresion.operador == OPERACION_LOGICA.OR:
            print( "Logica en OR")
            listaP = []
            for v in val:
                vv: DatoInsert = v
                listaP.append(vv)
            for v2 in val2:
                vv2: DatoInsert = v2
                listaP.append(vv2)
            return listaP

        elif expresion.operador == OPERACION_LOGICA.AND:
            listaP = []
            for v in val:
                vv: DatoInsert = v
                for v2 in val2:
                    vv2: DatoInsert = v2
                    if vv2.fila == vv.fila:
                        listaP.append(vv2)

            return listaP

        elif expresion.operador ==OPERACION_LOGICA.IS_DISTINCT:
            listaP = []
            for v in val:
                vv: DatoInsert = v
                for v2 in val2:
                    vv2: DatoInsert = v2
                    if vv2.fila != vv.fila:
                        listaP.append(vv2)

            return listaP

        elif expresion.operador ==OPERACION_LOGICA.IS_NOT_DISTINCT:
            listaP = []
            for v in val:
                vv: DatoInsert = v
                for v2 in val2:
                    vv2: DatoInsert = v2
                    if vv2.fila == vv.fila:
                        listaP.append(vv2)

            return listaP
    elif ((val == None) and isinstance(val2[0], DatoInsert)):
        if expresion.operador == OPERACION_LOGICA.OR:
            print( "Logica en OR")
            listaP = []
            for v2 in val2:
                vv2: DatoInsert = v2
                listaP.append(vv2)

            return listaP

        elif expresion.operador == OPERACION_LOGICA.AND:
            listaP = []
            for v2 in val2:
                vv2: DatoInsert = v2
                listaP.append(vv2)

            return listaP

        elif expresion.operador ==OPERACION_LOGICA.IS_DISTINCT:
            listaP = []
            for v2 in val2:
                vv2: DatoInsert = v2
                listaP.append(vv2)

            return listaP

        elif expresion.operador ==OPERACION_LOGICA.IS_NOT_DISTINCT:
            listaP = []
            for v2 in val2:
                vv2: DatoInsert = v2
                listaP.append(vv2)

            return listaP

    elif (isinstance(val[0], DatoInsert) and val2 == None):
        if expresion.operador == OPERACION_LOGICA.OR:
            print( "Logica en OR")
            listaP = []
            for v in val:
                vv: DatoInsert = v
                listaP.append(vv)

            return listaP

        elif expresion.operador == OPERACION_LOGICA.AND:
            listaP = []
            for v in val:
                vv: DatoInsert = v
                listaP.append(vv)

            return listaP

        elif expresion.operador ==OPERACION_LOGICA.IS_DISTINCT:
            listaP = []
            for v in val:
                listaP.append(v)

            return listaP

        elif expresion.operador ==OPERACION_LOGICA.IS_NOT_DISTINCT:
            listaP = []
            for v in val:
                listaP.append(v)

            return listaP
    else:
        print('Error: No se puede realizar la op. logica')
        # consola.insert('end','>>Error: Expresion logica con tipos incompatibles'+str(expresion.operador)+'\n>>')
        # newErr=ErrorRep('Semantico','Expresion logica con tipos incompatibles '+str(expresion.operador),indice)
        # LisErr.agregar(newErr)




def procesar_negAritmetica(expresion, ts):
    try:
        return -1 * procesar_expresion(expresion.exp, ts)
    except:
        print('Error:tipo de dato no se puede multiplicar por -1')
        # consola.insert('end','>>Error: No se pudo realizar la neg aritmetica\n>>')
        # newErr=ErrorRep('Semantico','No se pudo realizar la neg aritmetica ',indice)
        # LisErr.agregar(newErr)
        return None


def procesar_logicaNOT(instr, ts):
    try:
        val = procesar_expresion(instr.expresion, ts)
        return 0 if (val == 1) else 1
    except:
        print('Error no se puede aplicar Neg Logica')
        # consola.insert('end','>>Error: No se puede aplicar Neg Logica\n>>')
        # newErr=ErrorRep('Semantico','No se puede aplicar Neg Logica ',indice)
        # LisErr.agregar(newErr)
        return None


#aqui viene expresion de subquery
def procesar_logicaEXIST(instr, ts):
    try:
        val = procesar_expresion(instr.expresion, ts)
        return 0 if (val == 1) else 1

    except:
        print('Error no se puede aplicar Neg Logica')
        # consola.insert('end','>>Error: No se puede aplicar Neg Logica\n>>')
        # newErr=ErrorRep('Semantico','No se puede aplicar Neg Logica ',indice)
        # LisErr.agregar(newErr)
        return None







def procesar_NotBB(instr, ts):
    try:
        val = procesar_expresion(instr.expresion, ts)
        if isinstance(val, int):
            binario = ~int(val)
            return int(binario)
        else:
            print('Error: no compatible para aplicar neg binario')
            # consola.insert('end','>>Error: No compatible para aplicar neg binario\n>>')
            # newErr=ErrorRep('Semantico','No compatible para aplicar neg binario ',indice)
        # LisErr.agregar(newErr)
        return None
    except:
        print('Error no compatible para aplicar neg binario')
        # consola.insert('end','>>Error: No compatible para aplicar neg binario\n>>')
        # newErr=ErrorRep('Semantico','No compatible para aplicar neg binario ',indice)
        # LisErr.agregar(newErr)
        return None


def procesar_variable(tV, ts):
    global  ListaTablasG, baseN
    listaRes = []
    for item in ts.Datos:
        v:DatoInsert = ts.obtenerDato(item)
        if str(v.columna) == str(tV.id) and str(v.bd) == str(baseN[0]) and str(v.tabla) == str(ListaTablasG[0]):
            print(" <> En listar: " + str(v.valor))
            listaRes.append(v)
    print(" <><>")
    if listaRes.__len__() == 0:
        print(" >>> No hay datos para esta validación.")
        return None
    else:
        return listaRes



def procesar_unitaria_aritmetica(expresion, ts):
    val = procesar_expresion(expresion.exp1, ts)
    if expresion.operador == OPERACION_ARITMETICA.CUADRATICA:
        # if isinstance(val, string_types):
        #     if(val.isdecimal()):
        #         return float(val) * float(val)
        #     elif(val.isnumeric()):
        #         return int(val) * int(val)
        #     else:
        #         return None

        if isinstance(val, int) or isinstance(val, float):
            return val * val
        else:
            agregarErrorDatosOperacion(val, "", "|", "numerico", 0,0)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.CUBICA:
        # if isinstance(val, string_types):
        #     if (val.isdecimal()):
        #         return pow(float(val), 3)
        #     elif (val.isnumeric()):
        #         return pow(int(val), 3)
        #     else:
        #         return None

        if isinstance(val, int) or isinstance(val, float):
            return val * val * val
        else:
            agregarErrorDatosOperacion(val, "", "||", "numerico", 0, 0)
            return None
    elif expresion.operador == OPERACION_BIT_A_BIT.COMPLEMENTO:

        if isinstance(val, int):
            return ~val
        else:
            agregarErrorDatosOperacion(val, "", "~", "entero", 0, 0)
            return None


def procesar_funcion(expresion, ts):

    if expresion.exp1 is None:
        if expresion.id_funcion == FUNCION_NATIVA.PI:
            return math.pi
        elif expresion.id_funcion == FUNCION_NATIVA.RANDOM:
            return random()
        elif expresion.id_funcion == FUNCION_NATIVA.NOW:
            fecha = datetime.today()
            fechaString = '{:%Y-%m-%d %H:%M:%S}'.format(fecha)
            return fechaString

    if expresion.exp1 is not None:
        val1 = procesar_expresion(expresion.exp1, ts)

        if expresion.id_funcion == FUNCION_NATIVA.ABS:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return abs(float(val1))
            #     elif val1.isnumeric():
            #         return abs(int(val1))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return abs(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "ABS", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.CBRT:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return float(val1)**(1/3)
            #     elif val1.isnumeric():
            #         return int(val1)**(1/3)
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return val1 ** (1/3)
            else:
                agregarErrorFuncion(val1, None,None, None, "CBRT", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.CEIL:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.ceil(float(val1)**(1/3))
            #     elif val1.isnumeric():
            #         return math.ceil(int(val1)**(1/3))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.ceil(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "CEIL", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.CEILING:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         if float(val1) > 0:
            #             return int(float(val1)) + 1
            #         else:
            #             return int(float(val1))
            #     elif val1.isnumeric():
            #         return val1
            #     else:
            #         return None

            if isinstance(val1, float):
                if val1 > 0:
                    return int(val1) + 1
                else:
                    return int(val1)
            elif isinstance(val1, int):
                return val1
            else:
                agregarErrorFuncion(val1, None,None, None, "CEILING", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.DEGREES:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.degrees(float(val1))
            #     elif val1.isnumeric():
            #         return math.degrees(int(val1))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.degrees(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "DEGREES", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.EXP:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.exp(float(val1))
            #     elif val1.isnumeric():
            #         return math.exp(int(val1))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.exp(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "EXP", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.FACTORIAL:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return None
            #     elif val1.isnumeric():
            #         return math.factorial(int(val1))
            #     else:
            #         return None

            if isinstance(val1, int):
                return math.factorial(val1)
            elif isinstance(val1, float):
                return None
            else:
                agregarErrorFuncion(val1, None,None, None, "FACTORIAL", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.FLOOR:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.floor(float(val1)**(1/3))
            #     elif val1.isnumeric():
            #         return math.floor(int(val1)**(1/3))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.floor(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "FLOOR", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.LN:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.log(float(val1))
            #     elif val1.isnumeric():
            #         return math.log(int(val1))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.log(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "LN", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.LOG:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.log10(float(val1))
            #     elif val1.isnumeric():
            #         return math.log10(int(val1))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.log10(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "LN", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.RADIANS:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.radians(float(val1))
            #     elif val1.isnumeric():
            #         return math.radians(int(val1))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.radians(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "RADIANS", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.SIGN:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         if float(val1) > 0:
            #             return 1
            #         else:
            #             return -1
            #     elif val1.isnumeric():
            #         if int(val1) > 0:
            #             return 1
            #         else:
            #             return -1
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                if val1 > 0:
                    return 1
                else:
                    return -1
            else:
                agregarErrorFuncion(val1, None,None, None, "SIGN", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.SQRT:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         if float(val1) > 0:
            #             return math.sqrt(float(val1))
            #         else:
            #             return None
            #     elif val1.isnumeric():
            #         if int(val1) > 0:
            #             return math.sqrt(int(val1))
            #         else:
            #             return None
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                if val1 > 0:
                    return math.sqrt(val1)
                else:
                    return None
            else:
                agregarErrorFuncion(val1, None,None, None, "SQRT", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ACOS:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         if -1 <= float(val1) <= 1:
            #             return math.acos(float(val1))
            #         else:
            #             return None
            #     elif val1.isnumeric():
            #         if -1 <= int(val1) <= 1:
            #             return math.acos(int(val1))
            #         else:
            #             return None
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                if -1 <= val1 <= 1:
                    return math.acos(val1)
                else:
                    return None
            else:
                agregarErrorFuncion(val1, None,None, None, "ACOS", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ACOSD:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         if -1 <= float(val1) <= 1:
            #             return math.degrees(math.acos(float(val1)))
            #         else:
            #             return None
            #     elif val1.isnumeric():
            #         if -1 <= int(val1) <= 1:
            #             return math.degrees(math.acos(int(val1)))
            #         else:
            #             return None
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                if -1 <= val1 <= 1:
                    return math.degrees(math.acos(val1))
                else:
                    return None
            else:
                agregarErrorFuncion(val1, None,None, None, "ACOSD", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ASIN:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         if -1 <= float(val1) <= 1:
            #             return math.asin(float(val1))
            #         else:
            #             return None
            #     elif val1.isnumeric():
            #         if -1 <= int(val1) <= 1:
            #             return math.asin(int(val1))
            #         else:
            #             return None
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                if -1 <= val1 <= 1:
                    return math.asin(val1)
                else:
                    return None
            else:
                agregarErrorFuncion(val1, None, None, None, "ASIN", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ASIND:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         if -1 <= float(val1) <= 1:
            #             return math.degrees(math.asin(float(val1)))
            #         else:
            #             return None
            #     elif val1.isnumeric():
            #         if -1 <= int(val1) <= 1:
            #             return math.degrees(math.asin(int(val1)))
            #         else:
            #             return None
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                if -1 <= val1 <= 1:
                    return math.degrees(math.asin(val1))
                else:
                    return None
            else:
                agregarErrorFuncion(val1, None, None, None, "ASIND", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ATAN:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.atan(float(val1))
            #     elif val1.isnumeric():
            #         return math.atan(int(val1))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.atan(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "ATAN", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ATAND:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.degrees(math.atan(float(val1)))
            #     elif val1.isnumeric():
            #         return math.degrees(math.atan(int(val1)))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.degrees(math.atan(val1))
            else:
                agregarErrorFuncion(val1, None, None, None, "ATAND", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.COS:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.cos(float(val1))
            #     elif val1.isnumeric():
            #         return math.cos(int(val1))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.cos(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "COS", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.COSD:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.degrees(math.cos(float(val1)))
            #     elif val1.isnumeric():
            #         return math.degrees(math.cos(int(val1)))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.degrees(math.cos(val1))
            else:
                agregarErrorFuncion(val1, None, None, None, "COSD", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.COT:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return 1 / math.tan(float(val1))
            #     elif val1.isnumeric():
            #         return 1 / math.tan(int(val1))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return 1 / math.tan(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "COT", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.COTD:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.degrees(1 / math.tan(float(val1)))
            #     elif val1.isnumeric():
            #         return math.degrees(1 / math.tan(int(val1)))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.degrees(1 / math.tan(val1))
            else:
                agregarErrorFuncion(val1, None, None, None, "COTD", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.SIN:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.sin(float(val1))
            #     elif val1.isnumeric():
            #         return math.sin(int(val1))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.sin(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "SIN", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.SIND:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.degrees(math.sin(float(val1)))
            #     elif val1.isnumeric():
            #         return math.degrees(math.sin(int(val1)))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.degrees(math.sin(val1))
            else:
                agregarErrorFuncion(val1, None, None, None, "SIND", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.TAN:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.tan(float(val1))
            #     elif val1.isnumeric():
            #         return math.tan(int(val1))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.tan(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "TAN", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.TAND:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.degrees(math.tan(float(val1)))
            #     elif val1.isnumeric():
            #         return math.degrees(math.tan(int(val1)))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.degrees(math.tan(val1))
            else:
                agregarErrorFuncion(val1, None, None, None, "TAND", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.SINH:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.sinh(float(val1))
            #     elif val1.isnumeric():
            #         return math.sinh(int(val1))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.sinh(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "SINH", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.COSH:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.cosh(float(val1))
            #     elif val1.isnumeric():
            #         return math.cosh(int(val1))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.cosh(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "COSH", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.TANH:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.tanh(float(val1))
            #     elif val1.isnumeric():
            #         return math.tanh(int(val1))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.tanh(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "TANH", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ASINH:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return math.tanh(float(val1))
            #     elif val1.isnumeric():
            #         return math.tanh(int(val1))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return math.tanh(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "ASINH", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ACOSH:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         if float(val1) >= 1:
            #             return math.acosh(float(val1))
            #         else:
            #             return None
            #     elif val1.isnumeric():
            #         if int(val1) >= 1:
            #             return math.acosh(int(val1))
            #         else:
            #             return None
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                if val1 >= 1:
                    return math.acosh(val1)
                else:
                    agregarErrorFuncion(val1, None, None, None, "ACOSH", "numerico >= 1", 0, 0)
                    return None
            else:
                agregarErrorFuncion(val1, None, None, None, "ACOSH", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ATANH:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         if -1 < float(val1) < 1:
            #             return math.atanh(float(val1))
            #         else:
            #             return None
            #     elif val1.isnumeric():
            #         if -1 < int(val1) < 1:
            #             return math.atanh(int(val1))
            #         else:
            #             return None
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                if -1 < val1 < 1:
                    return math.atanh(val1)
                else:
                    agregarErrorFuncion(val1, None, None, None, "ATANH", "numerico entre -1 y 1", 0, 0)
                    return None
            else:
                agregarErrorFuncion(val1, None, None, None, "ATANH", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ROUND:
            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         return round(float(val1) ** (1 / 3))
            #     elif val1.isnumeric():
            #         return round(int(val1) ** (1 / 3))
            #     else:
            #         return None

            if isinstance(val1, int) or isinstance(val1, float):
                return round(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "ROUND", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.LENGTH:
            if isinstance(val1, string_types):
                return len(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "LENGTH", "string", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.MD5:
            if isinstance(val1, string_types):
                return str(hashlib.md5(val1.encode()).hexdigest())
            else:
                agregarErrorFuncion(val1, None, None, None, "MD5", "string", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.SHA256:
            if isinstance(val1, string_types):
                return str(hashlib.sha256(val1.encode()).hexdigest())
            else:
                agregarErrorFuncion(val1, None, None, None, "MD5", "string", 0, 0)
                return None

    if expresion.exp2 is not None:
        val1 = procesar_expresion(expresion.exp1, ts)
        val2 = procesar_expresion(expresion.exp2, ts)

        if expresion.id_funcion == FUNCION_NATIVA.DIV:
            parametro1 = None
            parametro2 = None

            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         parametro1 = float(val1)
            #     elif val1.isnumeric():
            #         parametro1 = int(val1)
            if isinstance(val1, int) or isinstance(val1, float):
                parametro1 = val1

            # if isinstance(val2, string_types):
            #     if val2.isdecimal():
            #         parametro2 = float(val2)
            #     elif val2.isnumeric():
            #         parametro2 = int(val2)
            if isinstance(val2, int) or isinstance(val2, float):
                parametro2 = val2

            if parametro1 is not None and parametro2 is not None:
                if parametro2 != 0:
                    return parametro1 / parametro2
                else:
                    agregarErrorFuncion(val2, None, None, None, "DIV", "numerico diferentes de 0 en el dividendo", 0, 0)

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "DIV", "numerico", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "DIV", "numerico", 0, 0)

            return None

        elif expresion.id_funcion == FUNCION_NATIVA.GCD:
            parametro1 = None
            parametro2 = None

            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         parametro1 = float(val1)
            #     elif val1.isnumeric():
            #         parametro1 = int(val1)
            if isinstance(val1, int):
                parametro1 = val1

            # if isinstance(val2, string_types):
            #     if val2.isdecimal():
            #         parametro2 = float(val2)
            #     elif val2.isnumeric():
            #         parametro2 = int(val2)
            if isinstance(val2, int):
                parametro2 = val2

            if parametro1 is not None and parametro2 is not None:
                return math.gcd(parametro1, parametro2)

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "GCD", "entero", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "GCD", "entero", 0, 0)

            return None

        elif expresion.id_funcion == FUNCION_NATIVA.MOD:
            parametro1 = None
            parametro2 = None

            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         parametro1 = float(val1)
            #     elif val1.isnumeric():
            #         parametro1 = int(val1)
            if isinstance(val1, int) or isinstance(val1, float):
                parametro1 = val1

            # if isinstance(val2, string_types):
            #     if val2.isdecimal():
            #         parametro2 = float(val2)
            #     elif val2.isnumeric():
            #         parametro2 = int(val2)
            if isinstance(val2, int) or isinstance(val2, float):
                parametro2 = val2

            if parametro1 is not None and parametro2 is not None:

                if parametro2 != 0:
                    return parametro1 % parametro2
                else:
                    agregarErrorFuncion(val2, None, None, None, "MOD", "numerico diferente de 0", 0, 0)

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "MOD", "numerico", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "MOD", "numerico", 0, 0)

            return None

        elif expresion.id_funcion == FUNCION_NATIVA.POWER:
            parametro1 = None
            parametro2 = None

            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         parametro1 = float(val1)
            #     elif val1.isnumeric():
            #         parametro1 = int(val1)
            if isinstance(val1, int) or isinstance(val1, float):
                parametro1 = val1

            # if isinstance(val2, string_types):
            #     if val2.isdecimal():
            #         parametro2 = float(val2)
            #     elif val2.isnumeric():
            #         parametro2 = int(val2)
            if isinstance(val2, int) or isinstance(val2, float):
                parametro2 = val2

            if parametro1 is not None and parametro2 is not None:
                return parametro1 ** parametro2

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "POWER", "numerico", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "POWER", "numerico", 0, 0)

            return None

        elif expresion.id_funcion == FUNCION_NATIVA.TRUNC:
            parametro1 = None
            parametro2 = None

            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         parametro1 = float(val1)
            #     elif val1.isnumeric():
            #         parametro1 = int(val1)
            if isinstance(val1, int) or isinstance(val1, float):
                parametro1 = val1

            # if isinstance(val2, string_types):
            #     if val2.isdecimal():
            #         # Agregar error semantico
            #         print('Error se espera un entero no un decimal')
            #     elif val2.isnumeric():
            #         parametro2 = int(val2)
            if isinstance(val2, int):
                parametro2 = val2
            elif  isinstance(val2, float):
                # Agregar error semantico
                agregarErrorFuncion(val2, None, None, None, "TRUNC", "numerico entero como segundo parametro", 0, 0)

            if parametro1 is not None and parametro2 is not None:
                return round(parametro1, parametro2)

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "TRUNC", "numerico", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "TRUNC", "numerico", 0, 0)

            return None

        elif expresion.id_funcion == FUNCION_NATIVA.ATAN2:
            parametro1 = None
            parametro2 = None

            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         parametro1 = float(val1)
            #     elif val1.isnumeric():
            #         parametro1 = int(val1)
            if isinstance(val1, int) or isinstance(val1, float):
                parametro1 = val1

            # if isinstance(val2, string_types):
            #     if val2.isdecimal():
            #         parametro2 = float(val2)
            #     elif val2.isnumeric():
            #         parametro2 = int(val2)
            if isinstance(val2, int) or isinstance(val2, float):
                parametro2 = val2

            if parametro1 is not None and parametro2 is not None:
                return math.atan2(parametro1, parametro2)

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "ATAN2", "numerico", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "ATAN2", "numerico", 0, 0)

            return None

        elif expresion.id_funcion == FUNCION_NATIVA.ATAN2D:
            parametro1 = None
            parametro2 = None

            # if isinstance(val1, string_types):
            #     if val1.isdecimal():
            #         parametro1 = float(val1)
            #     elif val1.isnumeric():
            #         parametro1 = int(val1)
            if isinstance(val1, int) or isinstance(val1, float):
                parametro1 = val1

            # if isinstance(val2, string_types):
            #     if val2.isdecimal():
            #         parametro2 = float(val2)
            #     elif val2.isnumeric():
            #         parametro2 = int(val2)
            if isinstance(val2, int) or isinstance(val2, float):
                parametro2 = val2

            if parametro1 is not None and parametro2 is not None:
                return math.degrees(math.atan2(parametro1, parametro2))

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "ATAN2D", "numerico", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "ATAN2D", "numerico", 0, 0)

            return None
        elif expresion.id_funcion == FUNCION_NATIVA.EXTRACT:
            parametro1 = None
            parametro2 = None

            if isinstance(val1, string_types):
                parametro1 = val1

            if isinstance(val2, string_types):
                try:
                    if re.compile("^\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01])$").match(val2):
                        print('Es una fecha sin hora')
                        print(val2 + " 00:00:00")
                        parametro2 = datetime.strptime(val2 + " 00:00:00", '%Y-%m-%d %H:%M:%S')
                    elif re.compile("^\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01])[ ]+(00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9])$").match(val2):
                        parametro2 = datetime.strptime(val2, '%Y-%m-%d %H:%M:%S')

                except ValueError:
                    # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
                    agregarErrorFuncion(val2, None, None, None, "EXTRACT", "string con formato de fecha", 0, 0)

            if parametro1 is not None and parametro2 is not None:
                if parametro1 == 'YEAR':
                    return parametro2.year
                elif parametro1 == 'MONTH':
                    return parametro2.month
                elif parametro1 == 'DAY':
                    return parametro2.day
                elif parametro1 == 'HOUR':
                    return parametro2.hour
                elif parametro1 == 'MINUTE':
                    return parametro2.minute
                elif parametro1 == 'SECOND':
                    return parametro2.second

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "EXTRACT", "unidad de tiempo", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "EXTRACT", "string", 0, 0)

            return None

        elif expresion.id_funcion == FUNCION_NATIVA.DATE_PART:
            parametro1 = None
            parametro2 = None

            if isinstance(val1, string_types):
                parametro1 = val1

            if isinstance(val2, string_types):
                try:
                    parametro2 = IntervalParser.parse(val2)

                except ValueError:
                    # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
                    agregarErrorFuncion(val2, None, None, None, "DATE_PART", "string con sintaxys de intervalo de tiempo", 0, 0)
                    print('ERROR AL CONVERTIR CADENA EN OBJETO DATETIME')

            if parametro1 is not None and parametro2 is not None:
                if parametro1 == 'year' or parametro1 == 'years':
                    return parametro2.years
                elif parametro1 == 'month' or parametro1 == 'months':
                    return parametro2.months
                elif parametro1 == 'day' or parametro1 == 'days':
                    return parametro2.days
                elif parametro1 == 'hour' or parametro1 == 'hours':
                    return parametro2.hours
                elif parametro1 == 'minute' or parametro1 == 'minutes':
                    return parametro2.minutes
                elif parametro1 == 'second' or parametro1 == 'seconds':
                    return parametro2.seconds

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "DATE_PART", "string de unidad de tiempo", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "DATE_PART", "string con sintaxys de intervalo de tiempo", 0, 0)

            return None

        elif expresion.id_funcion == FUNCION_NATIVA.TRIM:
            parametro1 = None
            parametro2 = None

            if isinstance(val1, string_types):
                parametro1 = val1

            if isinstance(val2, string_types):
                parametro2 = val2

            if parametro1 is not None and parametro2 is not None:
                if parametro1 != "":
                    return parametro2.strip(parametro1)
                else:
                    agregarErrorFuncion(val1, None, None, None, "TRIM", "string con una longitud mayor a 0", 0, 0)

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "TRIM", "string", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "TRIM", "string", 0, 0)

            return None


    if expresion.exp3 is not None:
        val1 = procesar_expresion(expresion.exp1, ts)
        val2 = procesar_expresion(expresion.exp2, ts)
        val3 = procesar_expresion(expresion.exp3, ts)

        if expresion.id_funcion == FUNCION_NATIVA.SUBSTRING or expresion.id_funcion == FUNCION_NATIVA.SUBSTR:
            parametro1 = None
            parametro2 = None
            parametro3 = None

            if isinstance(val1, string_types):
                parametro1 = val1

            # if isinstance(val2, string_types):
            #     if val2.isnumeric():
            #         parametro2 = int(val2)

            if isinstance(val2, int):
                parametro2 = val2

            # if isinstance(val3, string_types):
            #     if val3.isnumeric():
            #         parametro3 = int(val3)
            if isinstance(val3, int):
                parametro3 = val3

            if parametro1 is not None and parametro2 is not None and parametro3 is not None:
                if parametro2 <= len(parametro1) and parametro3 <= len(parametro1):
                    if parametro2 <= parametro3:
                        return parametro1[parametro2:parametro3]
                    else:
                        agregarErrorFuncion(val2, None, None, None, "SUBSTRING", "entero menor o igual tercer parametro", 0, 0)
                else:
                    agregarErrorFuncion(val1, val2, None, None, "SUBSTRING", "entero dentro de la longitud de la cadena", 0, 0)

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "SUBSTRING", "string", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "SUBSTRING", "entero como segundo parametro", 0, 0)
            if parametro3 is None:
                agregarErrorFuncion(val3, None, None, None, "SUBSTRING", "entero como tercer parametro", 0, 0)

            return None

    return None


def procesar_unidad_tiempo(expresion, ts):
    return expresion.nombre


def procesar_constante(expresion, ts):
    if expresion.id_constate == CONSTANTES.CURRENT_TIME:
        fecha = datetime.now().time()
        fechaString = '{:%H:%M:%S}'.format(fecha)
        return fechaString
    if expresion.id_constate == CONSTANTES.CURRENT_DATE:
        fecha = datetime.now()
        fechaString = '{:%Y-%m-%d}'.format(fecha)
        return fechaString



# -------------------------------------------------------------------------------------------------
# --------------------------------- EJECUCION -----------------------------------------------------

from Instruccion import *
from expresiones import *


class interprete2:

    def __init__(self, sentencias):
        self.i = 0
        self.sentencias = sentencias

    def inc(self):
        global i
        self.i += 1

    def ejecucion(self):
        self.recorrerInstrucciones(self.sentencias)

    def recorrerInstrucciones(self, sente):
        global ts_global
        for i in sente:
            if isinstance(i, CreateDataBase):
                i.Ejecutar()
            elif isinstance(i, ShowDatabases):
                i.Ejecutar()
            elif isinstance(i, AlterDataBase):
                i.Ejecutar()
            elif isinstance(i, DropDataBase):
                i.Ejecutar()
            elif isinstance(i, CreateTable):
                i.Ejecutar()
            elif isinstance(i, Insert_Datos):
                i.Ejecutar()
            elif isinstance(i, DropTable):
                i.Ejecutar()
            elif isinstance(i,Alter_Table_AddColumn):
                i.Ejecutar()
            elif isinstance(i,Alter_Table_Drop_Column):
                i.Ejecutar()
            elif isinstance(i,Alter_Table_Rename_Column):
                i.Ejecutar()
            elif isinstance(i,Alter_Table_Drop_Constraint):
                i.Ejecutar()
            elif isinstance(i,Alter_table_Add_Foreign_Key):
                i.Ejecutar()
            elif isinstance(i,Alter_Table_Add_Constraint):
                i.Ejecutar()
            elif isinstance(i, Delete_Datos):
                i.Ejecutar()
            elif isinstance(i, Update_Datos):
                i.Ejecutar()
            elif isinstance(i,Alter_COLUMN):
                i.Ejecutar()
            elif isinstance(i,Select):
                i.Ejecutar()
            elif isinstance(i,Select2):
                i.Ejecutar()
            elif isinstance(i,Select3):
                i.Ejecutar()
            elif isinstance(i, SelectExpresion):
                i.Ejecutar()
            elif isinstance(i,CreacionEnum):
                i.Ejecutar()
            elif isinstance(i,Select4):
                i.Ejecutar()
            elif isinstance(i,SubSelect):
                i.Ejecutar()
            elif isinstance(i,SubSelect2):
                i.Ejecutar()
            elif isinstance(i,SubSelect3):
                i.Ejecutar()
            elif isinstance(i,SubSelect4):
                i.Ejecutar()
            elif isinstance(i, Alter_table_Alter_Column_Set):
                i.Ejecutar()
            elif isinstance(i, useClase):
                i.Ejecutar()
            else:
                print("NO ejecuta")

'''
    def i_CreateDataBase(self, DataBase: CreateDataBase):
        global ts_global
        r = ts_global.obtenerCreateDateBase(DataBase.idBase)
        if r == None:
            print("No encontre la base de datos.")
            rM = Master.createDatabase(str(DataBase.idBase))
            if rM == 0:
                print("> Base de datos creada con exito!")
            elif rM == 1 or rM == 2:
                print("> Base de datos con conflicto.")
        else:
            print("Si encontre la base de datos.")
            for i in ts_global.createDataBase:
                x:CreateDataBase = ts_global.obtenerCreateDateBase(i)
                print(x.Modo)'''


#REPORTE DE ERRORES..................
def reporte_errores():
    print("ejecutando errores...........")
    Rep = Graph('g', filename='berrores.gv', format='png',node_attr={'shape': 'plaintext', 'height': '.1'})
    cadena=''
    i=1
    for item in LisErr.errores:
        cadena+='<TR><TD>'+str(i)+'</TD><TD>'+str(item.tipo)+'</TD>'+'<TD>'+str(item.descripcion)+'</TD>'+'<TD>'+str(item.linea)+'</TD></TR>'
        i+=1
    Rep.node('structs','''<<TABLE> <TR> <TD>Numero</TD><TD>Tipo-Clase Error</TD><TD>Descripcion Error</TD><TD>Linea</TD></TR>'''+cadena+'</TABLE>>')
    Rep.render('g', format='png', view=True)
    print('Hecho')

def agregarErrorDatosOperacion(val1, val2, op, tipoEsperado, linea, columna):
    global LisErr
    er = ErrorRep('Semantico',
                  'Los datos ingresados: "' + str(val1) + '", "' + str(val2)
                  + '"; No se pueden operar con "' + str(op) + '", se esperaban datos de tipo ' + str(tipoEsperado), linea)
    LisErr.agregar(er)

def agregarErrorFuncion(val1, val2, val3, val4,funcion, tipoEsperado, linea, columna):
    global LisErr
    datos = ""
    if val1 is not None:
        datos = '"' + str(val1) + '"'
    if val2 is not None:
        datos = datos + ", " + '"' + str(val2) + '"'
    if val3 is not None:
        datos = datos + ", " + '"' + str(val3) + '"'
    if val4 is not None:
        datos = datos + ", " + '"' + str(val4) + '"'

    er = ErrorRep('Semantico',
                  'Los datos ingresados: ' + datos + '; No se pueden usar en la funcion "'
                  + str(funcion) + '", se esperaban datos de tipo '+ str(tipoEsperado), linea)
    LisErr.agregar(er)

## PROCESAR SELECT -----------------------------------------------------------------------------------------------------

# ========================================================================
# ========================================================================

# EJECUTANDO EXPRESIONES============================
# VERIFICANDO QUE TIPO DE EXPRESION ES
def procesar_expresion_select(expresiones, ts):
    print("---------------------------------------"+str(expresiones))

    if isinstance(expresiones, ExpresionAritmetica):
        return procesar_aritmetica_select(expresiones, ts)

    elif isinstance(expresiones, ExpresionRelacional):
        return procesar_relacional_select(expresiones, ts)

    elif isinstance(expresiones, ExpresionLogica):
        return procesar_logica_select(expresiones, ts)

    elif isinstance(expresiones, UnitariaNegAritmetica):
        return procesar_negAritmetica_select(expresiones, ts)

    elif isinstance(expresiones, UnitariaLogicaNOT):
        return procesar_logicaNOT_select(expresiones, ts)

    elif isinstance(expresiones, UnitariaNotBB):
        return procesar_NotBB_select(expresiones, ts)

    elif isinstance(expresiones, ExpresionValor):
        return expresiones.val

    elif isinstance(expresiones, CAMPO_TABLA_ID_PUNTO_ID):   #  WHERE Profesional.Id = Trabajo.Codigo
        return procesar_variable_select(expresiones, ts)

    elif isinstance(expresiones, Variable):
        return procesar_variable(expresiones, ts)

    elif isinstance(expresiones, UnitariaAritmetica):
        return procesar_unitaria_aritmetica_select(expresiones, ts)
    elif isinstance(expresiones, ExpresionFuncion):
        return procesar_funcion_select(expresiones, ts)

#exist
    elif isinstance(expresiones, UnitariaLogicaEXIST):
        result = ProcesoSub(expresiones.expresion, ts_global)

        if(len(result)>0):
            return True
        else:
            return False

        # return ProcesoSub(expresiones.expresion, ts_global)



    elif isinstance(expresiones, AccesoSubConsultas):
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ENtre sub where")
        return ProcesoSub(expresiones,ts_global)


    elif isinstance(expresiones, Absoluto):
        try:
            return procesar_expresion_select(expresiones.variable, ts)
        except:
            print('Error no se puede aplicar abs() por el tipo de dato')
            return None

    elif isinstance(expresiones, ExpresionTiempo):
        return procesar_unidad_tiempo(expresiones, ts)
    else:
        print('<<<<<<<<><<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>a')
        print(expresiones)
        print('Error:Expresion no reconocida')


def procesar_aritmetica_select(expresion, ts):
    val = procesar_expresion_select(expresion.exp1, ts)
    val2 = procesar_expresion_select(expresion.exp2, ts)

    if expresion.operador == OPERACION_ARITMETICA.MAS:
        if ((isinstance(val, int) or isinstance(val, float))
              and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val + val2
        else:
            agregarErrorDatosOperacion(val, val2, "+", "numerico", 0,0)
            return None

    elif expresion.operador == OPERACION_ARITMETICA.MENOS:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val - val2
        else:
            agregarErrorDatosOperacion(val, val2, "-", "numerico", 0,0)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.MULTI:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val * val2
        else:
            agregarErrorDatosOperacion(val, val2, "*", "numerico", 0,0)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.DIVIDIDO:
        if val2 == 0:
            agregarErrorDatosOperacion(val, val2, "/", "numerico diferente de 0 en el segundo operador", 0, 0)
            return None
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val / val2
        else:
            agregarErrorDatosOperacion(val, val2, "/", "numerico", 0, 0)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.RESIDUO:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val % val2
        else:
            agregarErrorDatosOperacion(val, val2, "%", "numerico", 0, 0)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.POTENCIA:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return pow(val, val2)
        else:
            agregarErrorDatosOperacion(val, val2, "*", "numerico", 0, 0)
            return None
    elif expresion.operador == OPERACION_BIT_A_BIT.AND:
        if isinstance(val, int) and isinstance(val2, int):
            return val & val2
        else:
            agregarErrorDatosOperacion(val, val2, "&", "entero", 0,0)
            return None
    elif expresion.operador == OPERACION_BIT_A_BIT.OR:
        if isinstance(val, int) and isinstance(val2, int):
            return val | val2
        else:
            agregarErrorDatosOperacion(val, val2, "|", "entero", 0,0)
            return None
    elif expresion.operador == OPERACION_BIT_A_BIT.XOR:
        if isinstance(val, int) and isinstance(val2, int):
            return val ^ val2
        else:
            agregarErrorDatosOperacion(val, val2, "#", "entero", 0,0)
            return None
    elif expresion.operador == OPERACION_BIT_A_BIT.SHIFT_DER:
        if isinstance(val, int) and isinstance(val2, int):
            return val << val2
        else:
            agregarErrorDatosOperacion(val, val2, ">>", "entero", 0,0)
            return None
    elif expresion.operador == OPERACION_BIT_A_BIT.SHIFT_DER:
        if isinstance(val, int) and isinstance(val2, int):
            return val >> val2
        else:
            agregarErrorDatosOperacion(val, val2, "<<", "entero", 0,0)
            return None


def procesar_relacional_select(expresion, ts):
    val = procesar_expresion_select(expresion.exp1, ts)
    val2 = procesar_expresion_select(expresion.exp2, ts)

    if (isinstance(val, int) and isinstance(val2, float)
            or isinstance(val, float) and isinstance(val2, int)
            or isinstance(val, float) and isinstance(val2, float)
            or isinstance(val, int) and isinstance(val2, int)):
        if expresion.operador == OPERACION_RELACIONAL.IGUALQUE:
            return 1 if (val == val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.DISTINTO:
            return 1 if (val != val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MAYORIGUAL:
            return 1 if (val >= val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MENORIGUAL:
            return 1 if (val <= val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MAYORQUE:
            return 1 if (val > val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MENORQUE:
            return 1 if (val < val2) else 0

    elif isinstance(val, string_types) and isinstance(val2, string_types):
        if expresion.operador == OPERACION_RELACIONAL.IGUALQUE:
            return 1 if (val == val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.DISTINTO:
            return 1 if (val != val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MAYORIGUAL:
            return 1 if (val >= val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MENORIGUAL:
            return 1 if (val <= val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MAYORQUE:
            return 1 if (val > val2) else 0
        elif expresion.operador == OPERACION_RELACIONAL.MENORQUE:
            return 1 if (val < val2) else 0
    elif (isinstance(val,list) and isinstance(val2, int)
          or isinstance(val,list) and isinstance(val2, int)
          or isinstance(val,list) and isinstance(val2, float)
          or isinstance(val,list) and isinstance(val2, int) ):

        if expresion.operador == OPERACION_RELACIONAL.IGUALQUE:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if int(Vd.calculado) == val2:
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.DISTINTO:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if int(Vd.calculado) != val2:
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MAYORIGUAL:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if int(Vd.calculado) >= val2:
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MENORIGUAL:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if int(Vd.calculado) <= val2:
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MAYORQUE:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if int(Vd.calculado) > val2:
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MENORQUE:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if int(Vd.calculado) < val2:
                    listaV.append(Vd)
            return listaV

    elif isinstance(val,list) and isinstance(val2[0], DatoInsert):
        if expresion.operador == OPERACION_RELACIONAL.IGUALQUE:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                for v2 in val2:
                    Vd2:DatoInsert = v2
                    if str(Vd.calculado) == str(Vd2.calculado):
                        listaV.append(Vd)
                        listaV.append(Vd2)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.DISTINTO:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                for v2 in val:
                    Vd2:DatoInsert = v2
                    if str(Vd.calculado) != str(Vd2.calculado):
                        listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MAYORIGUAL:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                for v2 in val:
                    Vd2:DatoInsert = v2
                    if int(Vd.calculado) >= int(Vd2.calculado):
                        listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MENORIGUAL:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                for v2 in val:
                    Vd2:DatoInsert = v2
                    if int(Vd.calculado) <= int(Vd2.calculado):
                        listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MAYORQUE:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                for v2 in val:
                    Vd2:DatoInsert = v2
                    if int(Vd.calculado) > int(Vd2.calculado):
                        listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MENORQUE:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                for v2 in val:
                    Vd2:DatoInsert = v2
                    if int(Vd.calculado) < int(Vd2.calculado):
                        listaV.append(Vd)
            return listaV
    elif isinstance(val[0], DatoInsert) and isinstance(val2, string_types):
        if expresion.operador == OPERACION_RELACIONAL.IGUALQUE:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if str(Vd.calculado) == str(val2):
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.DISTINTO:
            listaV = []
            for v in val:
                Vd: DatoInsert = v
                if str(Vd.calculado) != str(val2):
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MAYORIGUAL:
            # error semantico
            listaV = []
            for v in val:
                Vd: DatoInsert = v
                if str(Vd.calculado) >= str(val2):
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MENORIGUAL:
            listaV = []
            for v in val:
                Vd: DatoInsert = v
                if str(Vd.calculado) <= str(val2):
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MAYORQUE:
            listaV = []
            for v in val:
                Vd: DatoInsert = v
                if str(Vd.calculado) > str(val2):
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MENORQUE:
            listaV = []
            for v in val:
                Vd: DatoInsert = v
                if str(Vd.calculado) < str(val2):
                    listaV.append(Vd)
            return listaV
    else:
        print('Error: Expresion relacional con tipos incompatibls')
        # consola.insert('end','>>Error: Expresion relacional con tipos incompatibles'+str(expresion.operador)+'\n>>')
        # newErr=ErrorRep('Semantico','Expresion relacional con tipos incompatibles '+str(expresion.operador),indice)
        # LisErr.agregar(newErr)
        return None


def procesar_logica_select(expresion, ts):
    print("Logica en LOGICA")
    val = procesar_expresion_select(expresion.exp1, ts)
    val2 = procesar_expresion_select(expresion.exp2, ts)

    if ((isinstance(val, int) or isinstance(val, float))
        and ((isinstance(val2, int) or isinstance(val2, float)))):

        if expresion.operador == OPERACION_LOGICA.AND:
            return 1 if (val and val2) else 0
        elif expresion.operador == OPERACION_LOGICA.OR:
            return 1 if (val or val2) else 0
    elif (isinstance(val[0], DatoInsert) and isinstance(val2[0], DatoInsert)):
        if expresion.operador == OPERACION_LOGICA.OR:
            listaP = []
            for v in val:
                vv: DatoInsert = v
                listaP.append(vv)
            for v2 in val2:
                vv2: DatoInsert = v2
                listaP.append(vv2)

            return listaP
        elif expresion.operador == OPERACION_LOGICA.AND:
            listaP = []
            for v in val2:
                vv: DatoInsert = v
                for v2 in val:
                    vv2: DatoInsert = v2
                    if str(vv2.fila) == str(vv.fila):
                        listaP.append(vv2)
            return listaP


#==========  AQU VIENEN NOT IN

        elif expresion.operador == OPERACION_LOGICA.NOT_IN:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   estoy entrando x2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            listaP = []
            for v in val2:
                vv: DatoInsert = v
                for v2 in val:
                    vv2: DatoInsert = v2

                    if str(vv2.fila) != str(vv.fila):
                        listaP.append(vv2)
            return listaP


# ========== VIENE UN IN

        elif expresion.operador == OPERACION_LOGICA.IN:
            listaP = []
            for v in val2:
                vv: DatoInsert = v
                for v2 in val:
                    vv2: DatoInsert = v2
                    if str(vv2.fila) == str(vv.fila):
                        listaP.append(vv2)
            return listaP




        elif expresion.operador == OPERACION_LOGICA.IS_DISTINCT:
            listaP = []
            for v in val:
                vv: DatoInsert = v
                for v2 in val2:
                    vv2: DatoInsert = v2
                    if vv2.fila != vv.fila:
                        listaP.append(vv2)
            return listaP

        elif expresion.operador == OPERACION_LOGICA.IS_NOT_DISTINCT:
            listaP = []
            for v in val:
                vv: DatoInsert = v
                for v2 in val2:
                    vv2: DatoInsert = v2
                    if vv2.fila == vv.fila:
                        listaP.append(vv2)
            return listaP
    elif ((val == None) and isinstance(val2[0], DatoInsert)):
        if expresion.operador == OPERACION_LOGICA.OR:
            print( "Logica en OR")
            listaP = []
            for v2 in val2:
                vv2: DatoInsert = v2
                listaP.append(vv2)

            return listaP

        elif expresion.operador == OPERACION_LOGICA.AND:
            listaP = []
            for v2 in val2:
                vv2: DatoInsert = v2
                listaP.append(vv2)

            return listaP
        elif expresion.operador ==OPERACION_LOGICA.IS_DISTINCT:

            return val2

        elif expresion.operador ==OPERACION_LOGICA.IS_NOT_DISTINCT:

            return val2

    elif (isinstance(val[0], DatoInsert) and val2 == None):
        if expresion.operador == OPERACION_LOGICA.OR:
            print( "Logica en OR")
            listaP = []
            for v in val:
                vv: DatoInsert = v
                listaP.append(vv)

            return listaP

        elif expresion.operador == OPERACION_LOGICA.AND:
            listaP = []
            for v in val:
                vv: DatoInsert = v
                listaP.append(vv)
            return listaP

        elif expresion.operador ==OPERACION_LOGICA.IS_DISTINCT:

            return val

        elif expresion.operador ==OPERACION_LOGICA.IS_NOT_DISTINCT:

            return val
    else:
        print('Error: No se puede realizar la op. logica')
        agregarErrorDatosOperacion(val, val2, 'Operadores Logicos', "", 0, 0)
        return None

def procesar_negAritmetica_select(expresion, ts):
    try:
        return -1 * procesar_expresion_select(expresion.exp, ts)
    except:
        print('Error:tipo de dato no se puede multiplicar por -1')
        # consola.insert('end','>>Error: No se pudo realizar la neg aritmetica\n>>')
        # newErr=ErrorRep('Semantico','No se pudo realizar la neg aritmetica ',indice)
        # LisErr.agregar(newErr)
        return None


def procesar_logicaNOT_select(instr, ts):
    try:
        val = procesar_expresion_select(instr.expresion, ts)
        return 0 if (val == 1) else 1
    except:
        print('Error no se puede aplicar Neg Logica')
        # consola.insert('end','>>Error: No se puede aplicar Neg Logica\n>>')
        # newErr=ErrorRep('Semantico','No se puede aplicar Neg Logica ',indice)
        # LisErr.agregar(newErr)
        return None


def procesar_NotBB_select(instr, ts):
    try:
        val = procesar_expresion_select(instr.expresion, ts)
        if isinstance(val, int):
            binario = ~int(val)
            return int(binario)
        else:
            print('Error: no compatible para aplicar neg binario')
            # consola.insert('end','>>Error: No compatible para aplicar neg binario\n>>')
            # newErr=ErrorRep('Semantico','No compatible para aplicar neg binario ',indice)
        # LisErr.agregar(newErr)
        return None
    except:
        print('Error no compatible para aplicar neg binario')
        # consola.insert('end','>>Error: No compatible para aplicar neg binario\n>>')
        # newErr=ErrorRep('Semantico','No compatible para aplicar neg binario ',indice)
        # LisErr.agregar(newErr)
        return None


def procesar_variable_select(tV, ts):
    global  ListaTablasG, baseN
    variable: CAMPO_TABLA_ID_PUNTO_ID = tV
    listaRes = []
    for item in ts.Datos:
        v:DatoInsert = ts.obtenerDato(item)
        # Se obtienen los datos de la columna.
        if str(v.columna) == str(variable.campoid) and str(v.bd) == str(baseN[0]) and str(v.tabla) == str(variable.tablaid):
            print(" <> En listar: " + str(v.valor))
            listaRes.append(DatoInsert(v.bd, v.tabla, v.columna, v.valor, v.fila))
    print(" <><>")
    if listaRes.__len__() == 0:
        print(" >>> No hay datos para esta validación.")
        return None
    else:
        return listaRes



def procesar_unitaria_aritmetica_select(expresion, ts):
    val = procesar_expresion_select(expresion.exp1, ts)
    if expresion.operador == OPERACION_ARITMETICA.CUADRATICA:
        # if isinstance(val, string_types):
        #     if(val.isdecimal()):
        #         return float(val) * float(val)
        #     elif(val.isnumeric()):
        #         return int(val) * int(val)
        #     else:
        #         return None

        if isinstance(val, int) or isinstance(val, float):
            return val * val
        else:
            agregarErrorDatosOperacion(val, "", "|", "numerico", 0,0)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.CUBICA:
        # if isinstance(val, string_types):
        #     if (val.isdecimal()):
        #         return pow(float(val), 3)
        #     elif (val.isnumeric()):
        #         return pow(int(val), 3)
        #     else:
        #         return None

        if isinstance(val, int) or isinstance(val, float):
            return val * val * val
        else:
            agregarErrorDatosOperacion(val, "", "||", "numerico", 0,0)
            return None


def procesar_funcion_select(expresion, ts):

    if expresion.exp1 is None:
        if expresion.id_funcion == FUNCION_NATIVA.PI:
            return math.pi
        elif expresion.id_funcion == FUNCION_NATIVA.RANDOM:
            return random()
        elif expresion.id_funcion == FUNCION_NATIVA.NOW:
            fecha = datetime.today()
            fechaString = '{:%Y-%m-%d %H:%M:%S}'.format(fecha)
            return fechaString


    if expresion.exp1 is not None:
        val1 = procesar_expresion_select(expresion.exp1, ts)


        if expresion.id_funcion == FUNCION_NATIVA.ABS:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v.calculado, int) or isinstance(v.calculado, float):
                        v.calculado = abs(v.calculado)
                        result.append(v)
                    else:
                        v.calculado = 0
                        result.append(v)
                        agregarErrorFuncion(v, None,None, None, "ABS", "numerico", 0, 0)
                return result

            if isinstance(val1, int) or isinstance(val1, float):
                return abs(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "ABS", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.CBRT:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v.calculado, int) or isinstance(v.calculado, float):
                        v.calculado =  v.calculado ** (1/3)
                        result.append(v)
                    else:
                        v.calculado = 0
                        result.append(v)
                        agregarErrorFuncion(v, None, None, None, "CBRT", "numerico", 0, 0)
                return result

            if isinstance(val1, int) or isinstance(val1, float):
                return val1 ** (1/3)
            else:
                agregarErrorFuncion(val1, None,None, None, "CBRT", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.CEIL:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v.calculado, int) or isinstance(v.calculado, float):
                        v.calculado = math.ceil(v.calculado)
                        result.append(v)
                    else:
                        v.calculado = 0
                        result.append(v)
                        agregarErrorFuncion(v, None, None, None, "CEIL", "numerico", 0, 0)
                return result

            if isinstance(val1, int) or isinstance(val1, float):
                return math.ceil(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "CEIL", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.CEILING:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v.calculado, float):
                        if val1 > 0:
                           v.calculado = int(v.calculado) + 1
                        else:
                            v.calculado = int(v.calculado)
                    elif isinstance(v.calculado, int):
                        v.calculado = v.calculado
                    else:
                        v.calculado = 0
                        agregarErrorFuncion(v, None, None, None, "CEILING", "numerico", 0, 0)
                    result.append(v)
                return result

            if isinstance(val1, float):
                if val1 > 0:
                    return int(val1) + 1
                else:
                    return int(val1)
            elif isinstance(val1, int):
                return val1
            else:
                agregarErrorFuncion(val1, None,None, None, "CEILING", "numerico", 0, 0)
                return None

        elif expresion.id_funcion == FUNCION_NATIVA.LENGTH:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v.calculado, string_types):
                        v.calculado = len(v.calculado)
                        result.append(v)
                    else:
                        v.calculado = 0
                        result.append(v)
                        agregarErrorFuncion(v, None, None, None, "LENGTH", "string", 0, 0)
                return result
            if isinstance(val1, string_types):
                return len(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "LENGTH", "string", 0, 0)
                return None


    if expresion.exp2 is not None:
        val1 = procesar_expresion_select(expresion.exp1, ts)
        val2 = procesar_expresion_select(expresion.exp2, ts)

        if expresion.id_funcion == FUNCION_NATIVA.TRIM:
            parametro1 = None
            parametro2 = None

            if isinstance(val1, string_types):
                parametro1 = val1

            if isinstance(val2, string_types) or isinstance(val2, list):
                parametro2 = val2

            if parametro1 is not None and parametro2 is not None:
                if isinstance(parametro2, list):
                    result = []
                    for v in parametro2:
                        if isinstance(v.calculado, string_types):
                            if v.calculado != "":
                                v.calculado = v.calculado.strip(parametro1)
                            else:
                                v.calculado = ""
                                agregarErrorFuncion(v, None, None, None, "TRIM", "string con una longitud mayor a 0", 0, 0)
                            result.append(v)
                        else:
                            agregarErrorFuncion(val1, None, None, None, "TRIM", "string", 0, 0)
                    return result
                elif isinstance(parametro2, string_types):
                    if parametro1 != "":
                        return parametro2.strip(parametro1)
                    else:
                        agregarErrorFuncion(val1, None, None, None, "TRIM", "string con una longitud mayor a 0", 0, 0)

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "TRIM", "string", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "TRIM", "string", 0, 0)

            return None
        elif expresion.id_funcion == FUNCION_NATIVA.EXTRACT:
            parametro1 = None
            parametro2 = None

            if isinstance(val1, string_types):
                parametro1 = val1

            if isinstance(val2, string_types):
                try:
                    if re.compile("^\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01])$").match(val2):
                        print('Es una fecha sin hora')
                        print(val2 + " 00:00:00")
                        parametro2 = datetime.strptime(val2 + " 00:00:00", '%Y-%m-%d %H:%M:%S')
                    elif re.compile("^\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01])[ ]+(00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9])$").match(val2):
                        parametro2 = datetime.strptime(val2, '%Y-%m-%d %H:%M:%S')

                except ValueError:
                    # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
                    agregarErrorFuncion(val2, None, None, None, "EXTRACT", "string con formato de fecha", 0, 0)

            if isinstance(val2, list):
                try:
                    parametro2 = []
                    for v in val2:
                        if isinstance(v.calculado, string_types):
                            if re.compile("^\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01])$").match(v.calculado):
                                print('Es una fecha sin hora')
                                print(v.calculado + " 00:00:00")
                                v.calculado = datetime.strptime(v.calculado + " 00:00:00", '%Y-%m-%d %H:%M:%S')
                                parametro2.append(v)
                            elif re.compile(
                                    "^\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01])[ ]+(00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9])$").match(
                                    v.calculado):
                                v.calculado = datetime.strptime(v.calculado, '%Y-%m-%d %H:%M:%S')
                                parametro2.append(v)
                            else:
                                v.calculado = datetime.strptime("1990-01-01 01:01:01", '%Y-%m-%d %H:%M:%S')
                                parametro2.append(v)
                                agregarErrorFuncion(v.calculado, None, None, None, "EXTRACT", "string con formato de fecha", 0, 0)

                except ValueError:
                    agregarErrorFuncion(val2, None, None, None, "EXTRACT", "string con formato de fecha", 0, 0)

            if parametro1 is not None and parametro2 is not None:
                if isinstance(parametro2, list):
                    result = []

                    for v in parametro2:
                        if parametro1 == 'YEAR':
                            v.calculado = v.calculado.year
                            result.append(v)
                        elif parametro1 == 'MONTH':
                            v.calculado = v.calculado.month
                            result.append(v)
                        elif parametro1 == 'DAY':
                            v.calculado = v.calculado.day
                            result.append(v)
                        elif parametro1 == 'HOUR':
                            v.calculado = v.calculado.hour
                            result.append(v)
                        elif parametro1 == 'MINUTE':
                            v.calculado = v.calculado.minute
                            result.append(v)
                        elif parametro1 == 'SECOND':
                            v.calculado = v.calculado.second
                            result.append(v)
                        else:
                            v.calculado = 0
                            result.append(v)
                            agregarErrorFuncion(val1, None, None, None, "EXTRACT", "unidad de tiempo", 0, 0)
                    return result
                else:

                    if parametro1 == 'YEAR':
                        return parametro2.year
                    elif parametro1 == 'MONTH':
                        return parametro2.month
                    elif parametro1 == 'DAY':
                        return parametro2.day
                    elif parametro1 == 'HOUR':
                        return parametro2.hour
                    elif parametro1 == 'MINUTE':
                        return parametro2.minute
                    elif parametro1 == 'SECOND':
                        return parametro2.second

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "EXTRACT", "unidad de tiempo", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "EXTRACT", "string", 0, 0)

            return None

        elif expresion.id_funcion == FUNCION_NATIVA.DATE_PART:
            parametro1 = None
            parametro2 = None

            if isinstance(val1, string_types):
                parametro1 = val1

            if isinstance(val2, string_types):
                try:
                    parametro2 = IntervalParser.parse(val2)

                except ValueError:
                    # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
                    agregarErrorFuncion(val2, None, None, None, "DATE_PART", "string con sintaxys de intervalo de tiempo", 0, 0)
                    print('ERROR AL CONVERTIR CADENA EN OBJETO DATETIME')

            if isinstance(val2, list):
                try:
                    parametro2 = []
                    for v in val2:
                        if isinstance(v.calculado, string_types):
                            v.calculado = IntervalParser.parse(v.calculado)
                            parametro2.append(v)
                        else:
                            v.calculado = IntervalParser.parse("1 years")
                            parametro2.append(v)
                            agregarErrorFuncion(v.calculado, None, None, None, "DATE_PART",
                                                "string con sintaxys de intervalo de tiempo", 0, 0)

                except ValueError:
                    # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
                    agregarErrorFuncion(val2, None, None, None, "DATE_PART", "string con sintaxys de intervalo de tiempo", 0, 0)
                    print('ERROR AL CONVERTIR CADENA EN OBJETO DATETIME')


            if parametro1 is not None and parametro2 is not None:

                if isinstance(parametro2, list):
                    result = []
                    for v in parametro2:
                        if isinstance(v.calculado, relativedelta):
                            if parametro1 == 'year' or parametro1 == 'years':
                                v.calculado = v.calculado.years
                                result.append(v)
                            elif parametro1 == 'month' or parametro1 == 'months':
                                v.calculado = v.calculado.months
                                result.append(v)
                            elif parametro1 == 'day' or parametro1 == 'days':
                                v.calculado = v.calculado.days
                                result.append(v)
                            elif parametro1 == 'hour' or parametro1 == 'hours':
                                v.calculado = v.calculado.hours
                                result.append(v)
                            elif parametro1 == 'minute' or parametro1 == 'minutes':
                                v.calculado = v.calculado.minutes
                                result.append(v)
                            elif parametro1 == 'second' or parametro1 == 'seconds':
                                v.calculado = v.calculado.seconds
                                result.append(v)
                        else:
                            v.calculado = 0
                            result.append(v)
                            agregarErrorFuncion(v.calculado, None, None, None, "DATE_PART", "relativedelta, error en conversion", 0, 0)

                    return result

                elif isinstance(parametro2, relativedelta):
                    if parametro1 == 'year' or parametro1 == 'years':
                        return parametro2.years
                    elif parametro1 == 'month' or parametro1 == 'months':
                        return parametro2.months
                    elif parametro1 == 'day' or parametro1 == 'days':
                        return parametro2.days
                    elif parametro1 == 'hour' or parametro1 == 'hours':
                        return parametro2.hours
                    elif parametro1 == 'minute' or parametro1 == 'minutes':
                        return parametro2.minutes
                    elif parametro1 == 'second' or parametro1 == 'seconds':
                        return parametro2.seconds

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "DATE_PART", "string de unidad de tiempo", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "DATE_PART", "string con sintaxys de intervalo de tiempo", 0, 0)

            return None


    if expresion.exp3 is not None:
        val1 = procesar_expresion_select(expresion.exp1, ts)
        val2 = procesar_expresion_select(expresion.exp2, ts)
        val3 = procesar_expresion_select(expresion.exp3, ts)

        if expresion.id_funcion == FUNCION_NATIVA.SUBSTRING or expresion.id_funcion == FUNCION_NATIVA.SUBSTR:
            parametro1 = None
            parametro2 = None
            parametro3 = None

            if isinstance(val1, string_types) or isinstance(val1, list):
                parametro1 = val1

            if isinstance(val2, int):
                parametro2 = val2

            if isinstance(val3, int):
                parametro3 = val3

            if parametro1 is not None and parametro2 is not None and parametro3 is not None:
                if isinstance(parametro1, list):
                    result = []
                    for v in parametro1:
                        if isinstance(v.calculado, string_types):
                            if parametro2 <= len(v.calculado) and parametro3 <= len(v.calculado):
                                if parametro2 <= parametro3:
                                    v.calculado = v.calculado[parametro2:parametro3]
                                else:
                                    agregarErrorFuncion(val2, None, None, None, "SUBSTRING",
                                                        "entero menor o igual tercer parametro", 0, 0)
                            else:
                                agregarErrorFuncion(val2, val3, None, None, "SUBSTRING",
                                                    "entero dentro de la longitud de la cadena", 0, 0)
                        else:
                            agregarErrorFuncion(v, None, None, None, "SUBSTRING", "string", 0, 0)
                        result.append(v)
                    return result

                elif isinstance(parametro1, string_types):
                    if parametro2 <= len(parametro1) and parametro3 <= len(parametro1):
                        if parametro2 <= parametro3:
                            return parametro1[parametro2:parametro3]
                        else:
                            agregarErrorFuncion(val2, None, None, None, "SUBSTRING", "entero menor o igual tercer parametro", 0, 0)
                    else:
                        agregarErrorFuncion(val1, val2, None, None, "SUBSTRING", "entero dentro de la longitud de la cadena", 0, 0)

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "SUBSTRING", "string", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "SUBSTRING", "entero como segundo parametro", 0, 0)
            if parametro3 is None:
                agregarErrorFuncion(val3, None, None, None, "SUBSTRING", "entero como tercer parametro", 0, 0)

            return None

def procesar_expresion_columna(expresiones, ts):

    if isinstance(expresiones, ExpresionAritmetica):
        result = procesar_aritmetica_columna(expresiones, ts)
        if isinstance(result, list):
            return result.copy()
        return result
    # elif isinstance(expresiones, ExpresionRelacional):
    #     return procesar_relacional(expresiones, ts)
    # elif isinstance(expresiones, ExpresionLogica):
    #     return procesar_logica(expresiones, ts)
    elif isinstance(expresiones, UnitariaNegAritmetica):
        return procesar_negAritmetica_columna(expresiones, ts)
    # elif isinstance(expresiones, UnitariaLogicaNOT):
    #     return procesar_logicaNOT(expresiones, ts)
    # elif isinstance(expresiones, UnitariaNotBB):
    #     return procesar_NotBB(expresiones, ts)
    elif isinstance(expresiones, ExpresionValor):
        return expresiones.val
    elif isinstance(expresiones, CAMPO_TABLA_ID_PUNTO_ID):   #  WHERE Profesional.Id = Trabajo.Codigo
        return procesar_variable_columna2(expresiones, ts)
    elif isinstance(expresiones, Variable):
        return procesar_variable_columna(expresiones, ts)
    elif isinstance(expresiones, UnitariaAritmetica):
        return procesar_unitaria_aritmetica_columna(expresiones, ts)
    elif isinstance(expresiones, ExpresionFuncion):
        return procesar_funcion_columna(expresiones, ts)
    elif isinstance(expresiones, ExpresionTiempo):
        return procesar_unidad_tiempo(expresiones, ts)
    # elif isinstance(expresiones, ExpresionConstante):
    #     return procesar_constante(expresiones, ts)
    elif isinstance(expresiones, Absoluto):
        try:
            return procesar_expresion_columna(expresiones.variable, ts)
        # return abs(procesar_expresion(expresiones.variable,ts))
        except:
            print('Error no se puede aplicar abs() por el tipo de dato')
            # consola.insert('end','>>Error: No se puede aplicar abs() al tipo de dato\n>>')
            # newErr=ErrorRep('Semantico','No se puede aplicar abs() al tipo de dato ',indice)
            # LisErr.agregar(newErr)
            return None
    # else:
    #     print('Error:Expresion no reconocida')

def procesar_negAritmetica_columna(expresion, ts):
    try:
        val = procesar_expresion_columna(expresion.exp, ts)
        if isinstance(val, list):
            result = []
            for v in val:
                if isinstance(v, int) or isinstance(v, float):
                    result.append(-1 * v)
                else:
                    result.append(0)
                    agregarErrorDatosOperacion(v, "", "-", "numerico", 0, 0)
            return result.copy()

        return -1 * val
    except:
        print('Error:tipo de dato no se puede multiplicar por -1')
        # consola.insert('end','>>Error: No se pudo realizar la neg aritmetica\n>>')
        # newErr=ErrorRep('Semantico','No se pudo realizar la neg aritmetica ',indice)
        # LisErr.agregar(newErr)
        return None

def procesar_variable_columna2(tV, ts):
    global  ListaTablasG, baseN
    variable: CAMPO_TABLA_ID_PUNTO_ID = tV
    listaRes = []
    for item in ts.Datos:
        v: DatoInsert = ts.obtenerDato(item)
        # Se obtienen los datos de la columna.
        if str(v.columna) == str(variable.campoid) and str(v.bd) == str(baseN[0]) and str(v.tabla) == str(
                variable.tablaid):
            print(" <> En listar: " + str(v.valor))
            listaRes.append(v.valor)
    print(" <><>")
    if listaRes.__len__() == 0:
        print(" >>> No hay datos para esta validación.")
        return None
    else:
        return listaRes


def procesar_variable_columna(tV, ts):
    global ListaTablasG, baseN
    variable = tV
    listaRes = []

    print('valores de arreglos')
    print(len(ListaTablasG))
    print(len(baseN))
    for item in ts.Datos:
        v: DatoInsert = ts.obtenerDato(item)

        # Se obtienen los datos de la columna.
        if str(v.columna) == str(variable.id) and str(v.bd) == str(baseN[0]) and str(v.tabla) == str(ListaTablasG[0]):
            print(" <> En listar: " + str(v.valor))
            listaRes.append(v.valor)
    print(" <><>")
    if listaRes.__len__() == 0:
        print(" >>> No hay datos para esta validación.")
        return None
    else:
        return listaRes

def procesar_unitaria_aritmetica_columna(expresion, ts):
    val = procesar_expresion_columna(expresion.exp1, ts)
    if expresion.operador == OPERACION_ARITMETICA.CUADRATICA:
        if isinstance(val, list):
            result = []
            for v in val:
                if isinstance(v, int) or isinstance(v, float):
                    result.append(v*v)
                else:
                    result.append(0)
                    agregarErrorDatosOperacion(v, "", "|", "numerico", 0, 0)
            return result.copy()

        if isinstance(val, int) or isinstance(val, float):
            return val * val
        else:
            agregarErrorDatosOperacion(val, "", "|", "numerico", 0, 0)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.CUBICA:
        if isinstance(val, list):
            result = []
            for v in val:
                if isinstance(v, int) or isinstance(v, float):
                    result.append(v * v * v)
                else:
                    result.append(0)
                    agregarErrorDatosOperacion(v, "", "||", "numerico", 0, 0)
            return result.copy()

        if isinstance(val, int) or isinstance(val, float):
            return val * val * val
        else:
            agregarErrorDatosOperacion(val, "", "||", "numerico", 0, 0)
            return None


def procesar_aritmetica_columna(expresion, ts):
    global LisErr
    val = procesar_expresion_columna(expresion.exp1, ts)
    val2 = procesar_expresion_columna(expresion.exp2, ts)

    if expresion.operador == OPERACION_ARITMETICA.MAS:
        if ((isinstance(val, int) or isinstance(val, float))
              and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val + val2
        elif (isinstance(val, int) or isinstance(val, float)) and isinstance(val2, list):
            result = []
            for item in val2:
                if isinstance(item, int) or isinstance(item, float):
                    result.append(item + val)
                else:
                    agregarErrorDatosOperacion(val, item, "+", "numerico", 0, 0)
                    result.append(0)

            return result.copy()
        elif (isinstance(val2, int) or isinstance(val2, float)) and isinstance(val, list):
            result = []
            for item in val:
                if isinstance(item, int) or isinstance(item, float):
                    result.append(item + val2)
                else:
                    agregarErrorDatosOperacion(val, item, "+", "numerico", 0, 0)
                    result.append(0)

            return result.copy()
        elif isinstance(val2, list) and isinstance(val, list):
            if len(val2) == len(val):
                result = []
                for i, v in enumerate(val):
                    result.append(v + val2[i])
                return result.copy()
            else:
                agregarErrorDatosOperacion(val, val2, "+", "arreglos numericos de la misma longitud", 0, 0)
        else:
            agregarErrorDatosOperacion(val, val2, "+", "numerico", 0,0)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.MENOS:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val - val2
        elif (isinstance(val, int) or isinstance(val, float)) and isinstance(val2, list):
            result = []
            for item in val2:
                if isinstance(item, int) or isinstance(item, float):
                    result.append(val - item)
                else:
                    agregarErrorDatosOperacion(val, item, "-", "numerico", 0, 0)
                    result.append(0)

            return result.copy()
        elif (isinstance(val2, int) or isinstance(val2, float)) and isinstance(val, list):
            result = []
            for item in val:
                if isinstance(item, int) or isinstance(item, float):
                    result.append(item - val2)
                else:
                    agregarErrorDatosOperacion(val, item, "-", "numerico", 0, 0)
                    result.append(0)

            return result.copy()
        elif isinstance(val2, list) and isinstance(val, list):
            if len(val2) == len(val):
                result = []
                for i, v in enumerate(val):
                    result.append(v - val2[i])
                return result.copy()
            else:
                agregarErrorDatosOperacion(val, val2, "-", "arreglos numericos de la misma longitud", 0, 0)
        else:
            print(val)
            print(val2)
            agregarErrorDatosOperacion(val, val2, "-", "numerico", 0, 0)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.MULTI:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val * val2
        elif (isinstance(val, int) or isinstance(val, float)) and isinstance(val2, list):
            result = []
            for item in val2:
                if isinstance(item, int) or isinstance(item, float):
                    result.append(item * val)
                else:
                    agregarErrorDatosOperacion(val, item, "*", "numerico", 0, 0)
                    result.append(0)

            return result.copy()
        elif (isinstance(val2, int) or isinstance(val2, float)) and isinstance(val, list):
            result = []
            for item in val:
                if isinstance(item, int) or isinstance(item, float):
                    result.append(item * val2)
                else:
                    agregarErrorDatosOperacion(val, item, "*", "numerico", 0, 0)
                    result.append(0)

            return result.copy()
        elif isinstance(val2, list) and isinstance(val, list):
            if len(val2) == len(val):
                result = []
                for i, v in enumerate(val):
                    result.append(v * val2[i])
                return result.copy()
            else:
                agregarErrorDatosOperacion(val, val2, "", "arreglos numericos de la misma longitud", 0, 0)
        else:
            agregarErrorDatosOperacion(val, val2, "*", "numerico", 0, 0)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.DIVIDIDO:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val / val2
        elif (isinstance(val, int) or isinstance(val, float)) and isinstance(val2, list):
            result = []
            for item in val2:
                if isinstance(item, int) or isinstance(item, float):
                    result.append(val / item)
                else:
                    agregarErrorDatosOperacion(val, item, "/", "numerico", 0, 0)
                    result.append(0)

            return result.copy()
        elif (isinstance(val2, int) or isinstance(val2, float)) and isinstance(val, list):
            result = []
            for item in val:
                if isinstance(item, int) or isinstance(item, float):
                    result.append(item/val2)
                else:
                    agregarErrorDatosOperacion(val, item, "/", "numerico", 0, 0)
                    result.append(0)

            return result.copy()
        elif isinstance(val2, list) and isinstance(val, list):
            if len(val2) == len(val):
                result = []
                for i, v in enumerate(val):
                    result.append(v / val2[i])
                return result.copy()
            else:
                agregarErrorDatosOperacion(val, val2, "/", "arreglos numericos de la misma longitud", 0, 0)
        else:
            agregarErrorDatosOperacion(val, val2, "/", "numerico", 0, 0)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.RESIDUO:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val % val2
        elif (isinstance(val, int) or isinstance(val, float)) and isinstance(val2, list):
            result = []
            for item in val2:
                if isinstance(item, int) or isinstance(item, float):
                    result.append(val % item)
                else:
                    agregarErrorDatosOperacion(val, item, "%", "numerico", 0, 0)
                    result.append(0)

            return result.copy()
        elif (isinstance(val2, int) or isinstance(val2, float)) and isinstance(val, list):
            result = []
            for item in val:
                if isinstance(item, int) or isinstance(item, float):
                    result.append(item % val2)
                else:
                    agregarErrorDatosOperacion(val, item, "%", "numerico", 0, 0)
                    result.append(0)

            return result.copy()
        elif isinstance(val2, list) and isinstance(val, list):
            if len(val2) == len(val):
                result = []
                for i, v in enumerate(val):
                    result.append(v % val2[i])
                return result.copy()
            else:
                agregarErrorDatosOperacion(val, val2, "%", "arreglos numericos de la misma longitud", 0, 0)
        else:
            agregarErrorDatosOperacion(val, val2, "%", "numerico", 0, 0)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.POTENCIA:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val ** val2
        elif (isinstance(val, int) or isinstance(val, float)) and isinstance(val2, list):
            result = []
            for item in val2:
                if isinstance(item, int) or isinstance(item, float):
                    result.append(val ** item)
                else:
                    agregarErrorDatosOperacion(val, item, "^", "numerico", 0, 0)
                    result.append(0)

            return result.copy()
        elif (isinstance(val2, int) or isinstance(val2, float)) and isinstance(val, list):
            result = []
            for item in val:
                if isinstance(item, int) or isinstance(item, float):
                    result.append(item ** val2)
                else:
                    agregarErrorDatosOperacion(val, item, "^", "numerico", 0, 0)
                    result.append(0)

            return result.copy()
        elif isinstance(val2, list) and isinstance(val, list):
            if len(val2) == len(val):
                result = []
                for i, v in enumerate(val):
                    result.append(v ** val2[i])
                return result.copy()
            else:
                agregarErrorDatosOperacion(val, val2, "^", "arreglos numericos de la misma longitud", 0, 0)
        else:
            agregarErrorDatosOperacion(val, val2, "^", "numerico", 0, 0)
            return None
    elif expresion.operador == OPERACION_BIT_A_BIT.AND:
        if (isinstance(val, int) and isinstance(val2, int)):
            return val & val2
        elif isinstance(val, int) and isinstance(val2, list):
            result = []
            for item in val2:
                if isinstance(item, int):
                    result.append(val & item)
                else:
                    agregarErrorDatosOperacion(val, item, "&", "entero", 0, 0)
                    result.append(0)

            return result.copy()
        elif isinstance(val2, int) and isinstance(val, list):
            result = []
            for item in val:
                if isinstance(item, int):
                    result.append(item & val2)
                else:
                    agregarErrorDatosOperacion(val, item, "&", "entero", 0, 0)
                    result.append(0)

            return result.copy()
        elif isinstance(val2, list) and isinstance(val, list):
            if len(val2) == len(val):
                result = []
                for i, v in enumerate(val):
                    result.append(v & val2[i])
                return result.copy()
            else:
                agregarErrorDatosOperacion(val, val2, "&", "arreglos de enteros de la misma longitud", 0, 0)
        else:
            agregarErrorDatosOperacion(val, val2, "&", "entero", 0, 0)
            return None

    elif expresion.operador == OPERACION_BIT_A_BIT.OR:
        if (isinstance(val, int) and isinstance(val2, int)):
            return val | val2
        elif isinstance(val, int) and isinstance(val2, list):
            result = []
            for item in val2:
                if isinstance(item, int):
                    result.append(val | item)
                else:
                    agregarErrorDatosOperacion(val, item, "|", "entero", 0, 0)
                    result.append(0)

            return result.copy()
        elif isinstance(val2, int) and isinstance(val, list):
            result = []
            for item in val:
                if isinstance(item, int):
                    result.append(item | val2)
                else:
                    agregarErrorDatosOperacion(val, item, "|", "entero", 0, 0)
                    result.append(0)

            return result.copy()
        elif isinstance(val2, list) and isinstance(val, list):
            if len(val2) == len(val):
                result = []
                for i, v in enumerate(val):
                    result.append(v | val2[i])
                return result.copy()
            else:
                agregarErrorDatosOperacion(val, val2, "|", "arreglos de enteros de la misma longitud", 0, 0)
        else:
            agregarErrorDatosOperacion(val, val2, "|", "entero", 0, 0)
            return None

    elif expresion.operador == OPERACION_BIT_A_BIT.XOR:
        if (isinstance(val, int) and isinstance(val2, int)):
            return val ^ val2
        elif isinstance(val, int) and isinstance(val2, list):
            result = []
            for item in val2:
                if isinstance(item, int):
                    result.append(val ^ item)
                else:
                    agregarErrorDatosOperacion(val, item, "#", "entero", 0, 0)
                    result.append(0)

            return result.copy()
        elif isinstance(val2, int) and isinstance(val, list):
            result = []
            for item in val:
                if isinstance(item, int):
                    result.append(item ^ val2)
                else:
                    agregarErrorDatosOperacion(val, item, "#", "entero", 0, 0)
                    result.append(0)

            return result.copy()
        elif isinstance(val2, list) and isinstance(val, list):
            if len(val2) == len(val):
                result = []
                for i, v in enumerate(val):
                    result.append(v ^ val2[i])
                return result.copy()
            else:
                agregarErrorDatosOperacion(val, val2, "#", "arreglos de enteros de la misma longitud", 0, 0)
        else:
            agregarErrorDatosOperacion(val, val2, "#", "entero", 0, 0)
            return None

    elif expresion.operador == OPERACION_BIT_A_BIT.SHIFT_DER:
        if (isinstance(val, int) and isinstance(val2, int)):
            return val >> val2
        elif isinstance(val, int) and isinstance(val2, list):
            result = []
            for item in val2:
                if isinstance(item, int):
                    result.append(val >> item)
                else:
                    agregarErrorDatosOperacion(val, item, ">>", "entero", 0, 0)
                    result.append(0)

            return result.copy()
        elif isinstance(val2, int) and isinstance(val, list):
            result = []
            for item in val:
                if isinstance(item, int):
                    result.append(item >> val2)
                else:
                    agregarErrorDatosOperacion(val, item, ">>", "entero", 0, 0)
                    result.append(0)

            return result.copy()
        elif isinstance(val2, list) and isinstance(val, list):
            if len(val2) == len(val):
                result = []
                for i, v in enumerate(val):
                    result.append(v >> val2[i])
                return result.copy()
            else:
                agregarErrorDatosOperacion(val, val2, ">>", "arreglos de enteros de la misma longitud", 0, 0)
        else:
            agregarErrorDatosOperacion(val, val2, ">>", "entero", 0, 0)
            return None
    elif expresion.operador == OPERACION_BIT_A_BIT.SHIFT_IZQ:
        if isinstance(val, int) and isinstance(val2, int):
            return val << val2
        elif isinstance(val, int) and isinstance(val2, list):
            result = []
            for item in val2:
                if isinstance(item, int):
                    result.append(val << item)
                else:
                    agregarErrorDatosOperacion(val, item, "<<", "entero", 0, 0)
                    result.append(0)

            return result.copy()
        elif isinstance(val2, int) and isinstance(val, list):
            result = []
            for item in val:
                if isinstance(item, int):
                    result.append(item << val2)
                else:
                    agregarErrorDatosOperacion(val, item, "<<", "entero", 0, 0)
                    result.append(0)

            return result.copy()
        elif isinstance(val2, list) and isinstance(val, list):
            if len(val2) == len(val):
                result = []
                for i, v in enumerate(val):
                    result.append(v << val2[i])
                return result.copy()
            else:
                agregarErrorDatosOperacion(val, val2, "<<", "arreglos de enteros de la misma longitud", 0, 0)
        else:
            agregarErrorDatosOperacion(val, val2, "<<", "entero", 0, 0)
            return None

def procesar_funcion_columna(expresion, ts):

    if expresion.exp1 is None:
        if expresion.id_funcion == FUNCION_NATIVA.PI:
            return math.pi
        elif expresion.id_funcion == FUNCION_NATIVA.RANDOM:
            return random()
        elif expresion.id_funcion == FUNCION_NATIVA.NOW:
            fecha = datetime.today()
            fechaString = '{:%Y-%m-%d %H:%M:%S}'.format(fecha)
            return fechaString

    if expresion.exp1 is not None:
        val1 = procesar_expresion_columna(expresion.exp1, ts)

        if expresion.id_funcion == FUNCION_NATIVA.ABS:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(abs(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None,None, None, "ABS", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return abs(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "ABS", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.CBRT:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(v ** (1/3))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "CBRT", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return val1 ** (1/3)
            else:
                agregarErrorFuncion(val1, None,None, None, "CBRT", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.CEIL:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.ceil(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "CEIL", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.ceil(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "CEIL", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.CEILING:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, float):
                        if val1 > 0:
                            result.append(int(v) + 1)
                        else:
                            result.append(int(v))
                    elif isinstance(v, int):
                        result.append(v)
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "CEILING", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, float):
                if val1 > 0:
                    return int(val1) + 1
                else:
                    return int(val1)
            elif isinstance(val1, int):
                return val1
            else:
                agregarErrorFuncion(val1, None,None, None, "CEILING", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.DEGREES:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.degrees(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "DEGREES", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.degrees(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "DEGREES", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.EXP:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.exp(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "EXP", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.exp(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "EXP", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.FACTORIAL:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.factorial(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "FACTORIAL", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int):
                return math.factorial(val1)
            elif isinstance(val1, float):
                return None
            else:
                agregarErrorFuncion(val1, None,None, None, "FACTORIAL", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.FLOOR:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.floor(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "FLOOR", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.floor(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "FLOOR", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.LN:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.log(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "LN", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.log(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "LN", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.LOG:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.log10(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "LN", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.log10(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "LOG", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.RADIANS:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.radians(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "RADIANS", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.radians(val1)
            else:
                agregarErrorFuncion(val1, None,None, None, "RADIANS", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.SIGN:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        if v > 0:
                            result.append(1)
                        else:
                            result.append(-1)

                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "SIGN", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                if val1 > 0:
                    return 1
                else:
                    return -1
            else:
                agregarErrorFuncion(val1, None,None, None, "SIGN", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.SQRT:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        if v >= 0:
                            result.append(math.sqrt(v))
                        else:
                            result.append(0)
                            agregarErrorFuncion(v, None, None, None, "SQRT", "numerico mayor a 0", 0, 0)
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "SQRT", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                if val1 >= 0:
                    return math.sqrt(val1)
                else:
                    return None
            else:
                agregarErrorFuncion(val1, None,None, None, "SQRT", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ACOS:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        if -1 <= v <= 1:
                            result.append(math.acos(v))
                        else:
                            result.append(0)
                            agregarErrorFuncion(v, None, None, None, "ACOS", "numerico entre -1 y 1", 0, 0)
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "ACOS", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                if -1 <= val1 <= 1:
                    return math.acos(val1)
                else:
                    agregarErrorFuncion(val1, None, None, None, "ACOS", "numerico entre -1 y 1", 0, 0)
                    return None
            else:
                agregarErrorFuncion(val1, None,None, None, "ACOS", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ACOSD:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        if -1 <= v <= 1:
                            result.append(math.degrees(math.acos(v)))
                        else:
                            result.append(0)
                            agregarErrorFuncion(v, None, None, None, "ACOSD", "numerico entre -1 y 1", 0, 0)
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "ACOSD", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                if -1 <= val1 <= 1:
                    return math.degrees(math.acos(val1))
                else:
                    agregarErrorFuncion(val1, None, None, None, "ACOSD", "numerico", 0, 0)
                    return None
            else:
                agregarErrorFuncion(val1, None,None, None, "ACOSD", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ASIN:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        if -1 <= v <= 1:
                            result.append(math.asin(v))
                        else:
                            result.append(0)
                            agregarErrorFuncion(v, None, None, None, "ASIN", "numerico entre -1 y 1", 0, 0)
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "ASIN", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                if -1 <= val1 <= 1:
                    return math.asin(val1)
                else:
                    agregarErrorFuncion(val1, None, None, None, "ASIN", "numerico entre -1 y 1", 0, 0)
                    return None
            else:
                agregarErrorFuncion(val1, None, None, None, "ASIN", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ASIND:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        if -1 <= v <= 1:
                            result.append(math.degrees(math.asin(v)))
                        else:
                            result.append(0)
                            agregarErrorFuncion(v, None, None, None, "ASIND", "numerico entre -1 y 1", 0, 0)
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "ASIND", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                if -1 <= val1 <= 1:
                    return math.degrees(math.asin(val1))
                else:
                    return None
            else:
                agregarErrorFuncion(val1, None, None, None, "ASIND", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ATAN:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.atan(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "ATAN", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.atan(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "ATAN", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ATAND:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.degrees(math.atan(v)))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "ATAND", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.degrees(math.atan(val1))
            else:
                agregarErrorFuncion(val1, None, None, None, "ATAND", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.COS:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.cos(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "COS", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.cos(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "COS", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.COSD:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.degrees(math.cos(v)))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "COSD", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.degrees(math.cos(val1))
            else:
                agregarErrorFuncion(val1, None, None, None, "COSD", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.COT:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(1 / math.tan(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "COT", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return 1 / math.tan(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "COT", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.COTD:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(1 / math.tan(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "COTD", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.degrees(1 / math.tan(val1))
            else:
                agregarErrorFuncion(val1, None, None, None, "COTD", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.SIN:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.sin(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "SIN", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.sin(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "SIN", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.SIND:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.degrees(math.sin(v)))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "SIND", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.degrees(math.sin(val1))
            else:
                agregarErrorFuncion(val1, None, None, None, "SIND", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.TAN:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.tan(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "TAN", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.tan(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "TAN", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.TAND:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.degrees(math.tan(v)))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "TAND", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.degrees(math.tan(val1))
            else:
                agregarErrorFuncion(val1, None, None, None, "TAND", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.SINH:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.sinh(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "SINH", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.sinh(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "SINH", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.COSH:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.cosh(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "COSH", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.cosh(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "COSH", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.TANH:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.tanh(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "TANH", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.tanh(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "TANH", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ASINH:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(math.tanh(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "ASINH", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return math.tanh(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "ASINH", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ACOSH:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        if v >= 1:
                            result.append(math.acosh(v))
                        else:
                            result.append(0)
                            agregarErrorFuncion(v, None, None, None, "ACOSH", "numerico >= 1", 0, 0)
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "ACOSH", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                if val1 >= 1:
                    return math.acosh(val1)
                else:
                    agregarErrorFuncion(val1, None, None, None, "ACOSH", "numerico >= 1", 0, 0)
                    return None
            else:
                agregarErrorFuncion(val1, None, None, None, "ACOSH", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ATANH:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        if -1 < v < 1:
                            result.append(math.atanh(v))
                        else:
                            result.append(0)
                            agregarErrorFuncion(v, None, None, None, "ATANH", "numerico entre -1 y 1", 0, 0)
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "ATANH", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                if -1 < val1 < 1:
                    return math.atanh(val1)
                else:
                    agregarErrorFuncion(val1, None, None, None, "ATANH", "numerico entre -1 y 1", 0, 0)
                    return None
            else:
                agregarErrorFuncion(val1, None, None, None, "ATANH", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.ROUND:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, int) or isinstance(v, float):
                        result.append(round(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "ROUND", "numerico", 0, 0)
                return result.copy()

            if isinstance(val1, int) or isinstance(val1, float):
                return round(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "ROUND", "numerico", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.LENGTH:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, string_types):
                        result.append(len(v))
                    else:
                        result.append(0)
                        agregarErrorFuncion(v, None, None, None, "LENGTH", "string", 0, 0)
                return result.copy()
            if isinstance(val1, string_types):
                return len(val1)
            else:
                agregarErrorFuncion(val1, None, None, None, "LENGTH", "string", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.MD5:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, string_types):
                        result.append(str(hashlib.md5(v.encode()).hexdigest()))
                    else:
                        result.append("")
                        agregarErrorFuncion(v, None, None, None, "MD5", "string", 0, 0)
                return result.copy()
            if isinstance(val1, string_types):
                return str(hashlib.md5(val1.encode()).hexdigest())
            else:
                agregarErrorFuncion(val1, None, None, None, "MD5", "string", 0, 0)
                return None
        elif expresion.id_funcion == FUNCION_NATIVA.SHA256:
            if isinstance(val1, list):
                result = []
                for v in val1:
                    if isinstance(v, string_types):
                        result.append(str(hashlib.sha256(v.encode()).hexdigest()))
                    else:
                        result.append("")
                        agregarErrorFuncion(v, None, None, None, "SHA256", "string", 0, 0)
                return result.copy()
            if isinstance(val1, string_types):
                return str(hashlib.sha256(val1.encode()).hexdigest())
            else:
                agregarErrorFuncion(val1, None, None, None, "SHA256", "string", 0, 0)
                return None

    if expresion.exp2 is not None:
        val1 = procesar_expresion_columna(expresion.exp1, ts)
        val2 = procesar_expresion_columna(expresion.exp2, ts)

        if expresion.id_funcion == FUNCION_NATIVA.DIV:
            parametro1 = None
            parametro2 = None

            if isinstance(val1, int) or isinstance(val1, float) or isinstance(val1, list):
                parametro1 = val1

            if isinstance(val2, int) or isinstance(val2, float) or isinstance(val2, list):
                parametro2 = val2

            if parametro1 is not None and parametro2 is not None:
                if isinstance(parametro1, list) and (isinstance(parametro2, int) or isinstance(parametro2, float)):
                    if parametro2 != 0:
                        result = []
                        for v in parametro1:
                            result.append(v/parametro2)
                        return result
                    else:
                        agregarErrorFuncion(val2, None, None, None, "DIV", "numerico diferente de 0", 0, 0)
                elif (isinstance(parametro1, int) or isinstance(parametro1, float)) and isinstance(parametro2, list):
                    result = []
                    for v in parametro2:
                        if v != 0:
                            result.append(parametro1 / v)
                        else:
                            result.append(0)
                            agregarErrorFuncion(v, None, None, None, "DIV","numerico diferentes de 0 en el dividendo", 0, 0)
                    return result
                elif isinstance(parametro1, list) and isinstance(parametro2, list):
                    if len(parametro1) == len(parametro2):
                        result = []
                        for i, v in enumerate(parametro1):
                            if (isinstance(v, int) or isinstance(v, float)) and (isinstance(parametro2[i], int) or isinstance(parametro2[i], float)):
                                if parametro2[i] != 0:
                                    result.append(v/parametro2[i])
                                else:
                                    result.append(0)
                                    agregarErrorFuncion(parametro2[i], None, None, None, "DIV", "numerico diferentes de 0 en el dividendo", 0, 0)
                            else:
                                result.append(0)
                                agregarErrorFuncion(v, parametro2[i], None, None, "DIV", "numericos", 0, 0)
                        return result
                    else:
                        agregarErrorFuncion(val1, val2, None, None, "DIV", "arreglo de la misma longitud", 0, 0)
                elif (isinstance(parametro1, int) or isinstance(parametro1, float)) and (isinstance(parametro2, int) or isinstance(parametro2, float)):
                    if parametro2 != 0:
                        return parametro1 / parametro2
                    else:
                        agregarErrorFuncion(val2, None, None, None, "DIV", "numerico diferentes de 0 en el dividendo", 0, 0)


            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "DIV", "numerico", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "DIV", "numerico", 0, 0)

            return None

        elif expresion.id_funcion == FUNCION_NATIVA.GCD:
            parametro1 = None
            parametro2 = None

            if isinstance(val1, int) or isinstance(val1, list):
                parametro1 = val1

            if isinstance(val2, int) or isinstance(val2, list):
                parametro2 = val2

            if parametro1 is not None and parametro2 is not None:
                if isinstance(parametro1, list) and isinstance(parametro2, int):
                    result = []
                    for v in parametro1:
                        if isinstance(v, int):
                            result.append(math.gcd(v, parametro2))
                        else:
                            agregarErrorFuncion(v, None, None, None, "GCD", "entero", 0, 0)
                    return result

                elif isinstance(parametro1, int) and isinstance(parametro2, list):
                    result = []
                    for v in parametro2:
                        if isinstance(v, int):
                            result.append(math.gcd(parametro1, v))
                        else:
                            result.append(0)
                            agregarErrorFuncion(v, None, None, None, "GCD", "entero", 0, 0)
                    return result
                elif isinstance(parametro1, list) and isinstance(parametro2, list):
                    if len(parametro1) == len(parametro2):
                        result = []
                        for i, v in enumerate(parametro1):
                            if isinstance(v, int) and isinstance(parametro2[i], int):
                                result.append(math.gcd(v, parametro2[i]))

                            else:
                                result.append(0)
                                agregarErrorFuncion(v, parametro2[i], None, None, "GCD", "entero", 0, 0)
                        return result
                    else:
                        agregarErrorFuncion(val1, val2, None, None, "GCD", "arreglo de la misma longitud", 0, 0)
                elif isinstance(parametro1, int) and isinstance(parametro2, int):
                    return math.gcd(parametro1, parametro2)


            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "GCD", "entero", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "GCD", "entero", 0, 0)

            return None

        elif expresion.id_funcion == FUNCION_NATIVA.MOD:
            parametro1 = None
            parametro2 = None

            if isinstance(val1, int) or isinstance(val1, float) or isinstance(val1, list):
                parametro1 = val1

            if isinstance(val2, int) or isinstance(val2, float) or isinstance(val2, list):
                parametro2 = val2

            if parametro1 is not None and parametro2 is not None:
                if isinstance(parametro1, list) and (isinstance(parametro2, int) or isinstance(parametro2, float)):
                    if parametro2 != 0:
                        result = []
                        for v in parametro1:
                            result.append(v % parametro2)
                        return result
                    else:
                        agregarErrorFuncion(val2, None, None, None, "MOD", "numerico diferente de 0", 0, 0)
                elif (isinstance(parametro1, int) or isinstance(parametro1, float)) and isinstance(parametro2, list):
                    result = []
                    for v in parametro2:
                        if v != 0:
                            result.append(parametro1 % v)
                        else:
                            result.append(0)
                            agregarErrorFuncion(v, None, None, None, "MOD", "numerico diferentes de 0 en el dividendo",
                                                0, 0)
                    return result
                elif isinstance(parametro1, list) and isinstance(parametro2, list):
                    if len(parametro1) == len(parametro2):
                        result = []
                        for i, v in enumerate(parametro1):
                            if (isinstance(v, int) or isinstance(v, float)) and (
                                    isinstance(parametro2[i], int) or isinstance(parametro2[i], float)):
                                if parametro2[i] != 0:
                                    result.append(v % parametro2[i])
                                else:
                                    result.append(0)
                                    agregarErrorFuncion(parametro2[i], None, None, None, "MOD",
                                                        "numerico diferentes de 0 en el dividendo", 0, 0)
                            else:
                                result.append(0)
                                agregarErrorFuncion(v, parametro2[i], None, None, "MOD", "numericos", 0, 0)
                        return result
                    else:
                        agregarErrorFuncion(val1, val2, None, None, "MOD", "arreglo de la misma longitud", 0, 0)
                elif (isinstance(parametro1, int) or isinstance(parametro1, float)) and (
                        isinstance(parametro2, int) or isinstance(parametro2, float)):
                    if parametro2 != 0:
                        return parametro1 % parametro2
                    else:
                        agregarErrorFuncion(val2, None, None, None, "MOD", "numerico diferentes de 0 en el dividendo",
                                            0, 0)

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "MOD", "numerico", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "MOD", "numerico", 0, 0)

            return None

        elif expresion.id_funcion == FUNCION_NATIVA.POWER:
            parametro1 = None
            parametro2 = None

            if isinstance(val1, int) or isinstance(val1, float) or isinstance(val1, list):
                parametro1 = val1

            if isinstance(val2, int) or isinstance(val2, float) or isinstance(val2, list):
                parametro2 = val2

            if parametro1 is not None and parametro2 is not None:
                if isinstance(parametro1, list) and (isinstance(parametro2, int) or isinstance(parametro2, float)):
                    result = []
                    for v in parametro1:
                        if isinstance(v, int) or isinstance(v, float):
                            result.append(v ** parametro2)
                        else:
                            agregarErrorFuncion(v, None, None, None, "TRUNC", "numerico", 0, 0)

                    return result


                elif (isinstance(parametro1, int) or isinstance(parametro1, float)) and isinstance(parametro2, list):
                    result = []
                    for v in parametro2:
                        if isinstance(v, int) or isinstance(v, float):
                            result.append(parametro1 ** v)
                        else:
                            result.append(0)
                            agregarErrorFuncion(v, None, None, None, "POWER","numerico", 0, 0)
                    return result
                elif isinstance(parametro1, list) and isinstance(parametro2, list):
                    if len(parametro1) == len(parametro2):
                        result = []
                        for i, v in enumerate(parametro1):
                            if (isinstance(v, int) or isinstance(v, float)) and (isinstance(parametro2[i], int) or isinstance(parametro2[i], float)):
                                    result.append(v**parametro2[i])
                            else:
                                result.append(0)
                                agregarErrorFuncion(v, parametro2[i], None, None, "POWER", "numericos", 0, 0)
                        return result
                    else:
                        agregarErrorFuncion(val1, val2, None, None, "POWER", "arreglo de la misma longitud", 0, 0)
                elif (isinstance(parametro1, int) or isinstance(parametro1, float)) and (isinstance(parametro2, int) or isinstance(parametro2, float)):
                    return parametro1 ** parametro2


            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "POWER", "numerico", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "TRUNC", "numerico", 0, 0)

            return None

        elif expresion.id_funcion == FUNCION_NATIVA.TRUNC:
            parametro1 = None
            parametro2 = None

            if isinstance(val1, int) or isinstance(val1, float) or isinstance(val1, list):
                parametro1 = val1

            if isinstance(val2, int) or isinstance(val2, float) or isinstance(val2, list):
                parametro2 = val2

            if parametro1 is not None and parametro2 is not None:
                if isinstance(parametro1, list) and (isinstance(parametro2, int) or isinstance(parametro2, float)):
                    result = []
                    for v in parametro1:
                        if isinstance(v, int) or isinstance(v, float):
                            result.append(round(v, parametro2))
                        else:
                            agregarErrorFuncion(v, None, None, None, "TRUNC", "numerico", 0, 0)

                    return result


                elif (isinstance(parametro1, int) or isinstance(parametro1, float)) and isinstance(parametro2, list):
                    result = []
                    for v in parametro2:
                        if isinstance(v, int) or isinstance(v, float):
                            result.append(round(parametro1, v))
                        else:
                            result.append(0)
                            agregarErrorFuncion(v, None, None, None, "TRUNC", "numerico", 0, 0)
                    return result
                elif isinstance(parametro1, list) and isinstance(parametro2, list):
                    if len(parametro1) == len(parametro2):
                        result = []
                        for i, v in enumerate(parametro1):
                            if (isinstance(v, int) or isinstance(v, float)) and (
                                    isinstance(parametro2[i], int) or isinstance(parametro2[i], float)):
                                result.append(round(v, parametro2[i]))
                            else:
                                result.append(0)
                                agregarErrorFuncion(v, parametro2[i], None, None, "TRUNC", "numericos", 0, 0)
                        return result
                    else:
                        agregarErrorFuncion(val1, val2, None, None, "TRUNC", "arreglo de la misma longitud", 0, 0)
                elif (isinstance(parametro1, int) or isinstance(parametro1, float)) and (isinstance(parametro2, int) or isinstance(parametro2, float)):
                    return round(parametro1, parametro2)

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "TRUNC", "numerico", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "TRUNC", "numerico", 0, 0)

            return None

        elif expresion.id_funcion == FUNCION_NATIVA.ATAN2:
            parametro1 = None
            parametro2 = None

            if isinstance(val1, int) or isinstance(val1, float) or isinstance(val1, list):
                parametro1 = val1

            if isinstance(val2, int) or isinstance(val2, float) or isinstance(val2, list):
                parametro2 = val2

            if parametro1 is not None and parametro2 is not None:
                if isinstance(parametro1, list) and (isinstance(parametro2, int) or isinstance(parametro2, float)):
                    result = []
                    for v in parametro1:
                        if isinstance(v, int) or isinstance(v, float):
                            result.append(math.atan2(v, parametro2))
                        else:
                            agregarErrorFuncion(v, None, None, None, "ATAN2", "numerico", 0, 0)

                    return result


                elif (isinstance(parametro1, int) or isinstance(parametro1, float)) and isinstance(parametro2, list):
                    result = []
                    for v in parametro2:
                        if isinstance(v, int) or isinstance(v, float):
                            result.append(math.atan2(parametro1, v))
                        else:
                            result.append(0)
                            agregarErrorFuncion(v, None, None, None, "ATAN2", "numerico", 0, 0)
                    return result
                elif isinstance(parametro1, list) and isinstance(parametro2, list):
                    if len(parametro1) == len(parametro2):
                        result = []
                        for i, v in enumerate(parametro1):
                            if (isinstance(v, int) or isinstance(v, float)) and (
                                    isinstance(parametro2[i], int) or isinstance(parametro2[i], float)):
                                result.append(math.atan2(v, parametro2[i]))
                            else:
                                result.append(0)
                                agregarErrorFuncion(v, parametro2[i], None, None, "ATAN2", "numericos", 0, 0)
                        return result
                    else:
                        agregarErrorFuncion(val1, val2, None, None, "ATAN2", "arreglo de la misma longitud", 0, 0)
                elif (isinstance(parametro1, int) or isinstance(parametro1, float)) and (
                        isinstance(parametro2, int) or isinstance(parametro2, float)):
                    return math.atan2(parametro1, parametro2)


            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "ATAN2", "numerico", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "ATAN2", "numerico", 0, 0)

            return None

        elif expresion.id_funcion == FUNCION_NATIVA.ATAN2D:
            parametro1 = None
            parametro2 = None

            if isinstance(val1, int) or isinstance(val1, float) or isinstance(val1, list):
                parametro1 = val1

            if isinstance(val2, int) or isinstance(val2, float) or isinstance(val2, list):
                parametro2 = val2

            if parametro1 is not None and parametro2 is not None:
                if isinstance(parametro1, list) and (isinstance(parametro2, int) or isinstance(parametro2, float)):
                    result = []
                    for v in parametro1:
                        if isinstance(v, int) or isinstance(v, float):
                            result.append(math.degrees(math.atan2(v, parametro2)))
                        else:
                            agregarErrorFuncion(v, None, None, None, "ATAN2", "numerico", 0, 0)

                    return result


                elif (isinstance(parametro1, int) or isinstance(parametro1, float)) and isinstance(parametro2, list):
                    result = []
                    for v in parametro2:
                        if isinstance(v, int) or isinstance(v, float):
                            result.append(math.degrees(math.atan2(parametro1, v)))
                        else:
                            result.append(0)
                            agregarErrorFuncion(v, None, None, None, "ATAN2", "numerico", 0, 0)
                    return result
                elif isinstance(parametro1, list) and isinstance(parametro2, list):
                    if len(parametro1) == len(parametro2):
                        result = []
                        for i, v in enumerate(parametro1):
                            if (isinstance(v, int) or isinstance(v, float)) and (
                                    isinstance(parametro2[i], int) or isinstance(parametro2[i], float)):
                                result.append(math.degrees(math.atan2(v, parametro2[i])))
                            else:
                                result.append(0)
                                agregarErrorFuncion(v, parametro2[i], None, None, "ATAN2", "numericos", 0, 0)
                        return result
                    else:
                        agregarErrorFuncion(val1, val2, None, None, "ATAN2", "arreglo de la misma longitud", 0, 0)
                elif (isinstance(parametro1, int) or isinstance(parametro1, float)) and (
                        isinstance(parametro2, int) or isinstance(parametro2, float)):
                    return math.degrees(math.atan2(parametro1, parametro2))


            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "ATAN2D", "numerico", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "ATAN2D", "numerico", 0, 0)

            return None
        elif expresion.id_funcion == FUNCION_NATIVA.EXTRACT:
            parametro1 = None
            parametro2 = None

            if isinstance(val1, string_types):
                parametro1 = val1

            if isinstance(val2, string_types):
                try:
                    if re.compile("^\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01])$").match(val2):
                        print('Es una fecha sin hora')
                        print(val2 + " 00:00:00")
                        parametro2 = datetime.strptime(val2 + " 00:00:00", '%Y-%m-%d %H:%M:%S')
                    elif re.compile("^\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01])[ ]+(00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9])$").match(val2):
                        parametro2 = datetime.strptime(val2, '%Y-%m-%d %H:%M:%S')

                except ValueError:
                    # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
                    agregarErrorFuncion(val2, None, None, None, "EXTRACT", "string con formato de fecha", 0, 0)

            if isinstance(val2, list):
                try:
                    parametro2 = []
                    for v in val2:
                        if isinstance(v, string_types):
                            if re.compile("^\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01])$").match(v):
                                print('Es una fecha sin hora')
                                print(v + " 00:00:00")
                                parametro2.append(datetime.strptime(v + " 00:00:00", '%Y-%m-%d %H:%M:%S'))
                            elif re.compile(
                                    "^\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01])[ ]+(00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9])$").match(
                                    v):
                                parametro2.append(datetime.strptime(v, '%Y-%m-%d %H:%M:%S'))
                            else:
                                parametro2.append(datetime.strptime("1990-01-01 01:01:01", '%Y-%m-%d %H:%M:%S'))
                                agregarErrorFuncion(v, None, None, None, "EXTRACT", "string con formato de fecha", 0, 0)

                except ValueError:
                    agregarErrorFuncion(val2, None, None, None, "EXTRACT", "string con formato de fecha", 0, 0)

            if parametro1 is not None and parametro2 is not None:
                if isinstance(parametro2, list):
                    result = []

                    for v in parametro2:
                        if parametro1 == 'YEAR':
                            result.append(v.year)
                        elif parametro1 == 'MONTH':
                            result.append(v.month)
                        elif parametro1 == 'DAY':
                            result.append(v.day)
                        elif parametro1 == 'HOUR':
                            result.append(v.hour)
                        elif parametro1 == 'MINUTE':
                            result.append(v.minute)
                        elif parametro1 == 'SECOND':
                            result.append(v.second)
                        else:
                            result.append(0)
                            agregarErrorFuncion(val1, None, None, None, "EXTRACT", "unidad de tiempo", 0, 0)
                    return result
                elif isinstance(parametro2, string_types):

                    if parametro1 == 'YEAR':
                        return parametro2.year
                    elif parametro1 == 'MONTH':
                        return parametro2.month
                    elif parametro1 == 'DAY':
                        return parametro2.day
                    elif parametro1 == 'HOUR':
                        return parametro2.hour
                    elif parametro1 == 'MINUTE':
                        return parametro2.minute
                    elif parametro1 == 'SECOND':
                        return parametro2.second

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "EXTRACT", "unidad de tiempo", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "EXTRACT", "string", 0, 0)

            return None

        elif expresion.id_funcion == FUNCION_NATIVA.DATE_PART:
            parametro1 = None
            parametro2 = None

            if isinstance(val1, string_types):
                parametro1 = val1

            if isinstance(val2, string_types):
                try:
                    parametro2 = IntervalParser.parse(val2)

                except ValueError:
                    # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
                    agregarErrorFuncion(val2, None, None, None, "DATE_PART", "string con sintaxys de intervalo de tiempo", 0, 0)
                    print('ERROR AL CONVERTIR CADENA EN OBJETO DATETIME')

            if isinstance(val2, list):
                try:
                    parametro2 = []
                    for v in val2:
                        if isinstance(v, string_types):
                            parametro2.append(IntervalParser.parse(v))
                        else:
                            parametro2.append(IntervalParser.parse("1 years"))
                            agregarErrorFuncion(v, None, None, None, "DATE_PART",
                                                "string con sintaxys de intervalo de tiempo", 0, 0)

                except ValueError:
                    # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
                    agregarErrorFuncion(val2, None, None, None, "DATE_PART", "string con sintaxys de intervalo de tiempo", 0, 0)
                    print('ERROR AL CONVERTIR CADENA EN OBJETO DATETIME')


            if parametro1 is not None and parametro2 is not None:

                if isinstance(parametro2, list):
                    result = []
                    for v in parametro2:
                        if isinstance(v, relativedelta):
                            if parametro1 == 'year' or parametro1 == 'years':
                                result.append(v.years)
                            elif parametro1 == 'month' or parametro1 == 'months':
                                result.append(v.months)
                            elif parametro1 == 'day' or parametro1 == 'days':
                                result.append(v.days)
                            elif parametro1 == 'hour' or parametro1 == 'hours':
                                result.append(v.hours)
                            elif parametro1 == 'minute' or parametro1 == 'minutes':
                                result.append(v.minutes)
                            elif parametro1 == 'second' or parametro1 == 'seconds':
                                result.append(v.seconds)
                        else:
                            result.append(0)
                            agregarErrorFuncion(v, None, None, None, "DATE_PART", "relativedelta, error en conversion", 0, 0)

                    return result

                elif isinstance(parametro2, relativedelta):
                    if parametro1 == 'year' or parametro1 == 'years':
                        return parametro2.years
                    elif parametro1 == 'month' or parametro1 == 'months':
                        return parametro2.months
                    elif parametro1 == 'day' or parametro1 == 'days':
                        return parametro2.days
                    elif parametro1 == 'hour' or parametro1 == 'hours':
                        return parametro2.hours
                    elif parametro1 == 'minute' or parametro1 == 'minutes':
                        return parametro2.minutes
                    elif parametro1 == 'second' or parametro1 == 'seconds':
                        return parametro2.seconds

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "DATE_PART", "string de unidad de tiempo", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "DATE_PART", "string con sintaxys de intervalo de tiempo", 0, 0)

            return None

        elif expresion.id_funcion == FUNCION_NATIVA.TRIM:
            parametro1 = None
            parametro2 = None

            if isinstance(val1, string_types):
                parametro1 = val1

            if isinstance(val2, string_types) or isinstance(val2, list):
                parametro2 = val2

            if parametro1 is not None and parametro2 is not None:
                if isinstance(parametro2, list):
                    result = []
                    for v in parametro2:
                        if isinstance(v, string_types):
                            if v != "":
                                result.append(v.strip(parametro1))
                            else:
                                result.append("")
                                agregarErrorFuncion(v, None, None, None, "TRIM", "string con una longitud mayor a 0", 0, 0)
                        else:
                            agregarErrorFuncion(val1, None, None, None, "TRIM", "string", 0, 0)
                    return result
                elif isinstance(parametro2, string_types):
                    if parametro1 != "":
                        return parametro2.strip(parametro1)
                    else:
                        agregarErrorFuncion(val1, None, None, None, "TRIM", "string con una longitud mayor a 0", 0, 0)

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "TRIM", "string", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "TRIM", "string", 0, 0)

            return None


    if expresion.exp3 is not None:
        val1 = procesar_expresion_columna(expresion.exp1, ts)
        val2 = procesar_expresion_columna(expresion.exp2, ts)
        val3 = procesar_expresion_columna(expresion.exp3, ts)

        if expresion.id_funcion == FUNCION_NATIVA.SUBSTRING or expresion.id_funcion == FUNCION_NATIVA.SUBSTR:
            parametro1 = None
            parametro2 = None
            parametro3 = None

            if isinstance(val1, string_types) or isinstance(val1, list):
                parametro1 = val1

            if isinstance(val2, int):
                parametro2 = val2

            if isinstance(val3, int):
                parametro3 = val3

            if parametro1 is not None and parametro2 is not None and parametro3 is not None:
                if isinstance(parametro1, list):
                    result = []
                    for v in parametro1:
                        if isinstance(v, string_types):
                            if parametro2 <= len(v) and parametro3 <= len(v):
                                if parametro2 <= parametro3:
                                    result.append(v[parametro2:parametro3])
                                else:
                                    agregarErrorFuncion(val2, None, None, None, "SUBSTRING",
                                                        "entero menor o igual tercer parametro", 0, 0)
                            else:
                                agregarErrorFuncion(val2, val3, None, None, "SUBSTRING",
                                                    "entero dentro de la longitud de la cadena", 0, 0)
                        else:
                            agregarErrorFuncion(v, None, None, None, "SUBSTRING", "string", 0, 0)
                    return result

                elif isinstance(parametro1, string_types):
                    if parametro2 <= len(parametro1) and parametro3 <= len(parametro1):
                        if parametro2 <= parametro3:
                            return parametro1[parametro2:parametro3]
                        else:
                            agregarErrorFuncion(val2, None, None, None, "SUBSTRING", "entero menor o igual tercer parametro", 0, 0)
                    else:
                        agregarErrorFuncion(val1, val2, None, None, "SUBSTRING", "entero dentro de la longitud de la cadena", 0, 0)

            if parametro1 is None:
                agregarErrorFuncion(val1, None, None, None, "SUBSTRING", "string", 0, 0)
            if parametro2 is None:
                agregarErrorFuncion(val2, None, None, None, "SUBSTRING", "entero como segundo parametro", 0, 0)
            if parametro3 is None:
                agregarErrorFuncion(val3, None, None, None, "SUBSTRING", "entero como tercer parametro", 0, 0)

            return None

    return None
