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
        print('Error:Expresion no reconocida')


def procesar_aritmetica(expresion, ts):
    val = procesar_expresion(expresion.exp1, ts)
    val2 = procesar_expresion(expresion.exp2, ts)
    if expresion.operador == OPERACION_ARITMETICA.MAS:
        if isinstance(val, string_types) and isinstance(val2, string_types):
            return val + val2
        elif ((isinstance(val, int) or isinstance(val, float))
              and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val + val2
        else:
            # consola.insert('end','>>Error: tipos no pueden sumarse \n>>')
            # newErr=ErrorRep('Semantico','Tipos no puden sumarse ',indice)
            # LisErr.agregar(newErr)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.MENOS:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val - val2
        else:
            # consola.insert('end','>>Error: tipos no pueden restarse \n>>')
            # newErr=ErrorRep('Semantico','Tipos no puden restarse ',indice)
            # LisErr.agregar(newErr)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.MULTI:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val * val2
        else:
            # consola.insert('end','>>Error: tipos no pueden multiplicarse \n>>')
            # newErr=ErrorRep('Semantico','Tipos no puden multiplicarse ',indice)
            # LisErr.agregar(newErr)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.DIVIDIDO:
        if val2 == 0:
            print('Error: No se puede dividir entre 0')
            # consola.insert('end','>>Error: No se puede dividir entre cero'+str(val)+' '+str(val2)+'\n>>')
            # newErr=ErrorRep('Semantico','No se puede dividir entre cero '+str(val)+' '+str(val2),indice)
            # LisErr.agregar(newErr)
            return None
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val / val2
        else:
            print('Error: Tipos no pueden dividirse')
            # consola.insert('end','>>Error: tipos no pueden dividires \n>>')
            # newErr=ErrorRep('Semantico','Tipos no puden dividirse ',indice)
            # LisErr.agregar(newErr)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.RESIDUO:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return val % val2
        else:
            print('Error: Tipos no pueden operarse %')
            # consola.insert('end','>>Error: tipos no pueden operarse por residuo \n>>')
            # newErr=ErrorRep('Semantico','Tipos no puden operarse por residuo ',indice)
            # LisErr.agregar(newErr)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.POTENCIA:
        if ((isinstance(val, int) or isinstance(val, float))
                and ((isinstance(val2, int) or isinstance(val2, float)))):
            return pow(val, val2)
        else:
            print('Error: Tipos no pueden operarse %')
            # consola.insert('end','>>Error: tipos no pueden operarse por residuo \n>>')
            # newErr=ErrorRep('Semantico','Tipos no puden operarse por residuo ',indice)
            # LisErr.agregar(newErr)
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
        '''
    elif isinstance(val, int) and isinstance(val2[0], DatoInsert):
        if expresion.operador == OPERACION_RELACIONAL.IGUALQUE:
            listaV = []
            for v in val2:
                Vd:DatoInsert = v
                if int(Vd.valor) == val2:
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.DISTINTO:
            listaV = []
            for v in val2:
                Vd:DatoInsert = v
                if int(Vd.valor) != val2:
                    listaV.append(Vd)
            return listaV
        elif expresion.operador == OPERACION_RELACIONAL.MAYORIGUAL:
            listaV = []
            for v in val:
                Vd:DatoInsert = v
                if  val >= int(Vd.valor):
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
            return listaV'''
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
    global  ListaTablasG
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
        if isinstance(val, string_types):
            if(val.isdecimal()):
                return float(val) * float(val)
            elif(val.isnumeric()):
                return int(val) * int(val)
            else:
                return None

        elif isinstance(val, int) or isinstance(val, float):
            return val * val
        else:
            # consola.insert('end','>>Error: tipo no pueden elevarse al cuadrado \n>>')
            # newErr=ErrorRep('Semantico','Tipo no pude elevarse al cuadrado ',indice)
            # LisErr.agregar(newErr)
            return None
    elif expresion.operador == OPERACION_ARITMETICA.CUBICA:
        if isinstance(val, string_types):
            if (val.isdecimal()):
                return pow(float(val), 3)
            elif (val.isnumeric()):
                return pow(int(val), 3)
            else:
                return None

        elif isinstance(val, int) or isinstance(val, float):
            return val * val
        else:
            # consola.insert('end','>>Error: tipo no pueden elevarse al cuadrado \n>>')
            # newErr=ErrorRep('Semantico','Tipo no pude elevarse al cuadrado ',indice)
            # LisErr.agregar(newErr)
            return None
