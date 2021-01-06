import PLSQL.tsPLSQL as TS
import PLSQL.tfPLSQL as TF
from PLSQL.instruccionesPLSQL import *
from PLSQL.expresionesPLSQL import *
import PLSQL.gramaticaPLSQL as g

temporalT = 0
temporalA = 0
temporalV = 0
temporalE = 0
ts = TS.TablaDeSimbolos()
tf = TF.TablaDeFunciones()
cadenaTraduccion = ""
cadenaManejador = ""
cadenaFunciones = ""
contadorLlamadas = 0
gram = []
tablaSimbolos = []
tablaELexicos = []
tablaESintacticos = []
tablaOptimizacion = []

cadenaFuncionIntermedia = ""
numFuncionSQL = 0

def getGramatica():
    global gram
    return gram

def getELexicos():
    global tablaELexicos
    return tablaELexicos

def getOptimizacion():
    global tablaOptimizacion
    return tablaOptimizacion

def getESintacticos():
    global tablaESintacticos
    return tablaESintacticos

def runC3D(codigoC):
    global gram, tablaELexicos, tablaESintacticos
    gram = g.listaGramatica
    tablaELexicos = g.listaErroresLexicos
    tablaESintacticos = g.listaErroresSintacticos
    instrucciones = g.parse(codigoC)
    return instrucciones

def generarTemporalT():
    global temporalT
    temporalT = temporalT + 1
    return 't' + str(temporalT - 1)

def resetTemporalT():
    global temporalT
    temporalT = 0

def generarTemporalEtiqueta():
    global temporalE
    temporalE = temporalE + 1
    return 'L' + str(temporalE - 1)

def resetTemporalEtiqueta():
    global temporalE
    temporalE = 0

def generarTemporalA():
    global temporalA
    temporalA = temporalA + 1
    return 'ta' + str(temporalA - 1)

def resetTemporalA():
    global temporalA
    temporalA = 0

def generarC3D(instrucciones, ts_global):
    global contadorLlamadas, tablaSimbolos, ts
    global cadenaTraduccion, tf, cadenaManejador
    global cadenaFuncionIntermedia,numFuncionSQL
    cadenaTraduccion = ""
    cadenaFuncionIntermedia = ""
    contadorLlamadas = 0
    numFuncionSQL = 0
    cadenaManejador = ""
    resetTemporalA()
    resetTemporalT()
    resetTemporalEtiqueta()
    tf = TF.TablaDeFunciones()

    cadenaFuncionIntermedia += "\nfrom gramatica import parse"
    cadenaFuncionIntermedia += "\nfrom principal import * "
    cadenaFuncionIntermedia += "\nimport ts as TS"
    cadenaFuncionIntermedia += "\nfrom expresiones import *"
    cadenaFuncionIntermedia += "\nfrom instrucciones import *"
    cadenaFuncionIntermedia += "\nfrom report_ast import *"
    cadenaFuncionIntermedia += "\nfrom report_tc import *"
    cadenaFuncionIntermedia += "\nfrom report_ts import *"
    cadenaFuncionIntermedia += "\nfrom report_errores import *\n\n"
    cadenaFuncionIntermedia += "\nclass Intermedio():"
    cadenaFuncionIntermedia += "\n\tinstrucciones_Global = []"
    cadenaFuncionIntermedia += "\n\ttc_global1 = []"
    cadenaFuncionIntermedia += "\n\tts_global1 = []\n"
    cadenaFuncionIntermedia += "\n\tdef __init__(self):"
    cadenaFuncionIntermedia += "\n\t\t''' Funcion Intermedia '''\n\n"

    cadenaTraduccion += "from FuncionInter import * " + "\n"
    cadenaTraduccion += "from goto import with_goto" + "\n\n"
    cadenaTraduccion += "inter = Intermedio()" + "\n\n"
    cadenaTraduccion += "@with_goto  # Decorador necesario." + "\n"
    cadenaTraduccion += "def main():" + "\n"
    cadenaTraduccion += "\tSra = -1" + "\n"
    cadenaTraduccion += "\tSs0 = [0] * 10000" + "\n"
    indice = 0
    ts = ts_global
    while indice < len(instrucciones):
        instruccion = instrucciones[indice]
        if isinstance(instruccion, ListaDeclaraciones):
            generarListaDeclaraciones(instruccion, ts)
        elif isinstance(instruccion, LlamadaFuncion):
            generarLlamadaFuncion(instruccion, ts)
        elif isinstance(instruccion, Principal):
            generarPrincipal(instruccion, ts)
            cadenaTraduccion += '\t\n'
            cadenaTraduccion += '\tgoto. end'
        elif isinstance(instruccion, Funcion):
            guardarFuncion(instruccion, ts)
        elif isinstance(instruccion, CreateDatabase):
            cadenaTraduccion += "\n\tprint(inter.procesar_funcion"+str(numFuncionSQL)+"())"
            cadenaFuncionIntermedia += createDatabaseFuncion(instruccion, ts)
        elif isinstance(instruccion, ShowDatabases):
            cadenaTraduccion += "\n\tprint(inter.procesar_funcion"+str(numFuncionSQL)+"())"
            cadenaFuncionIntermedia += createShowDatabasesFuncion(instruccion, ts)
        elif isinstance(instruccion, UseDatabase):
            cadenaTraduccion += "\n\tprint(inter.procesar_funcion"+str(numFuncionSQL)+"())"
            cadenaFuncionIntermedia += createUseDatabaseFuncion(instruccion, ts)
        elif isinstance(instruccion, ShowTables):
            cadenaTraduccion += "\n\tprint(inter.procesar_funcion"+str(numFuncionSQL)+"())"
            cadenaFuncionIntermedia += createShowTablesFuncion(instruccion, ts)
        elif isinstance(instruccion, DropDatabase):
            cadenaTraduccion += "\n\tprint(inter.procesar_funcion"+str(numFuncionSQL)+"())"
            cadenaFuncionIntermedia += createDropDatabaseFuncion(instruccion, ts)
            
            
        indice = indice + 1
    tablaSimbolos = ts
    
    cadenaTraduccion += '\t\n'
    cadenaTraduccion += '\tgoto. end'
    agregarFunciones()
    agregarRetorno()
    cadenaTraduccion += "\n\n\tlabel .end" + "\n"
    cadenaTraduccion += "\treturn" + "\n"
    cadenaTraduccion += "\nmain()" + "\n"

    salidaFuncionIntermedia = open("./FuncionInter.py", "w")
    salidaFuncionIntermedia.write(cadenaFuncionIntermedia)
    salidaFuncionIntermedia.close()

    return cadenaTraduccion

def generarPrincipal(instruccion, ts):
    global cadenaTraduccion
    indice = 0
    instrucciones = instruccion.instrucciones
    while indice < len(instrucciones):
        instruccion = instrucciones[indice]
        if isinstance(instruccion, ListaDeclaraciones):
            generarListaDeclaraciones(instruccion, ts)
        elif isinstance(instruccion, Asignacion):
            generarAsignacion(instruccion, ts)
        elif isinstance(instruccion, Impresion):
            generarImpresion(instruccion, ts)
        elif isinstance(instruccion, SentenciaIf):
            generarSentenciaIf(instruccion, ts, None)
        elif isinstance(instruccion, SentenciaCase):
            generarSentenciaCase(instruccion, ts)
        elif isinstance(instruccion, LlamadaFuncion):
            generarLlamadaFuncion(instruccion, ts)
        elif isinstance(instruccion, Etiqueta):
            generarEtiqueta(instruccion, ts)
        elif isinstance(instruccion, Salto):
            generarSalto(instruccion,ts)
        indice = indice + 1

def generarEtiqueta(instruccion, ts):
    global cadenaTraduccion
    cadenaTraduccion += '\t\n'
    cadenaTraduccion += '\t' + 'label. ' + str(instruccion.id)

def generarSalto(instruccion, ts):
    global cadenaTraduccion
    cadenaTraduccion += '\t\n'
    cadenaTraduccion += '\tgoto. '+ str(instruccion.id) + ''

def agregarFunciones():
    global tf, cadenaTraduccion
    for funcion in tf.funciones:
        instruccion = tf.obtener(funcion)
        tsTemp = TS.TablaDeSimbolos()
        if instruccion.parametros[0] != None:
            contador = 0
            for parametro in instruccion.parametros:
                simbolo = TS.Simbolo(parametro.id, parametro.tipo, getEmpty(parametro.tipo), instruccion.temporales[contador])
                tsTemp.agregar(simbolo)
                contador = contador + 1
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\t' + 'label. ' + str(instruccion.id)
        generarPrincipal(instruccion.instrucciones, tsTemp)
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tgoto. retorno'

def agregarRetorno():
    global cadenaTraduccion
    cadenaTraduccion += '\t\n'
    cadenaTraduccion += '\t\n'
    cadenaTraduccion += '\tlabel. retorno'
    cadenaTraduccion += '\t\n'
    cadenaTraduccion += '\tSsp = Ss0[Sra]'
    cadenaTraduccion += '\t\n'
    cadenaTraduccion += '\tSra = Sra - 1'
    cadenaTraduccion += cadenaManejador

def guardarFuncion(instruccion, ts):
    global tf
    tempParametros = []
    if instruccion.parametros[0] != None:
        for parametro in instruccion.parametros:
            parametroTemp = generarTemporalA()
            tempParametros.append(parametroTemp)

    funcion = TF.Funcion(instruccion.id, instruccion.tipo, instruccion.parametros, tempParametros, instruccion.instrucciones)
    tf.agregar(funcion)

def generarLlamadaFuncion(instruccion, ts):
    global cadenaTraduccion, contadorLlamadas, cadenaManejador, tf
    contadorLlamadas = contadorLlamadas + 1
    if instruccion.parametros[0] is None:
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tSra = Sra + 1'
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tSs0[Sra] = ' + str(contadorLlamadas) + ''
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tgoto. ' + instruccion.id + ''
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tlabel. retorno' + str(contadorLlamadas)
    else:
        funcion = tf.obtener(instruccion.id)
        contador = 0
        for parametro in instruccion.parametros:
            exp = generarExpresion(parametro, ts)
            cadenaTraduccion += '\t\n'
            cadenaTraduccion += '\t' + str(funcion.temporales[contador]) + ' = ' + str(exp) + ''
            contador = contador + 1
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tSra = Sra + 1'
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tSs0[Sra] = ' + str(contadorLlamadas) + ''
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tgoto. ' + instruccion.id + ''
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tlabel. retorno' + str(contadorLlamadas)
    cadenaManejador += '\t\n'
    cadenaManejador += '\tif Ssp == '+ str(contadorLlamadas) + ': goto. retorno' + str(contadorLlamadas) + ''

def generarListaDeclaraciones(instruccion, ts):
    global cadenaTraduccion
    tipo = instruccion.tipo
    for declaracion in instruccion.declaraciones:
        if declaracion.exp is None:
            temporal = generarTemporalT()
            simbolo = TS.Simbolo(declaracion.id, getTipo(tipo), getEmpty(tipo), temporal)
            ts.agregar(simbolo)
            cadenaTraduccion += '\t\n'
            cadenaTraduccion += '\t' + str(temporal) + " = " + str(getEmpty(tipo)) + ''
        else:
            temporal1 = generarExpresion(declaracion.exp, ts)
            temporal2 = generarTemporalT()
            simbolo = TS.Simbolo(declaracion.id, getTipo(tipo), temporal1, temporal2)
            ts.agregar(simbolo)
            cadenaTraduccion += '\t\n'
            cadenaTraduccion += '\t' + str(temporal2) + " = " + str(temporal1) + ''

def generarExpresion(expresion, ts):
    global cadenaTraduccion
    if isinstance(expresion, ExpresionCadena):
        return "\'" + expresion.val + "\'"
    elif isinstance(expresion, ExpresionNumero):
        return expresion.val
    elif isinstance(expresion, ExpresionBooleana):
        boool = False
        if expresion.val.upper() == 'TRUE':
            boool = True
        elif expresion.val.upper() == 'FALSE':
            boool = False
        return boool
    elif isinstance(expresion, ExpresionNegativo):
        exp = generarExpresion(expresion.exp, ts)
        return "-" + str(exp)
    elif isinstance(expresion, ExpresionIdentificador):
        return ts.obtener(expresion.id).temporal
    elif isinstance(expresion, ExpresionNOT):
        exp = generarExpresion(expresion.exp, ts)
        return "!" + str(exp)
    elif isinstance(expresion, ExpresionNOTBIN):
        exp = generarExpresion(expresion.exp, ts)
        return "~" + str(exp)
    elif isinstance(expresion, ExpresionBinaria):
        global tablaOptimizacion
        # Revisar optimización
        exp1 = generarExpresion(expresion.exp1, ts)
        exp2 = generarExpresion(expresion.exp2, ts)
        operador = getOperador(expresion.operador)
        if operador == '+' and exp2 == 0:
            # Regla 8 | 12
            print("Regla 8 | 12")
            cadenaTraduccion += '\n\t# REGLA 8 - OPTIMIZACION POR MIRILLA'
            tablaOptimizacion.append(Optimizacion('Regla 8|12', str(exp1) + " " + str(operador) + " " + str(exp2)))
            return exp1
        elif operador == '-' and exp2 == 0:
            # Regla 9 | 13
            print("Regla 9 | 13")
            tablaOptimizacion.append(Optimizacion('Regla 9|13', str(exp1) + " " + str(operador) + " " + str(exp2)))
            return exp1
        elif operador == '*' and exp2 == 1:
            # Regla 10 | 14
            print("Regla 10 | 14")
            tablaOptimizacion.append(Optimizacion('Regla 10|14', str(exp1) + " " + str(operador) + " " + str(exp2)))
            return exp1
        elif operador == '/' and exp2 == 1:
            # Regla 11 | 15
            print("Regla 11 | 15")
            tablaOptimizacion.append(Optimizacion('Regla 11|15', str(exp1) + " " + str(operador) + " " + str(exp2)))
            return exp1
        elif operador == '*' and exp2 == 2:
            # Regla 16
            print("Regla 16")
            tablaOptimizacion.append(Optimizacion('Regla 16', str(exp1) + " " + str(operador) + " " + str(exp2)))
            cadena = str(exp1) + " + " + str(exp1) + ''
            return cadena
        elif operador == '*' and exp2 == 0:
            # Regla 17
            print("Regla 17")
            tablaOptimizacion.append(Optimizacion('Regla 17', str(exp1) + " " + str(operador) + " " + str(exp2)))
            cadena = str(0)
            return cadena
        elif operador == '/' and exp1 == 0:
            # Regla 18
            print("Regla 18")
            tablaOptimizacion.append(Optimizacion('Regla 18', str(exp1) + " " + str(operador) + " " + str(exp2)))
            cadena = str(0)
            return cadena
        else:
            temporal = generarTemporalT()
            cadena = '\t' + str(temporal) + " = " + str(exp1) + " " + operador + " " + str(exp2) + ''
            cadenaTraduccion += '\t\n'
            cadenaTraduccion += cadena
            return temporal


def generarSentenciaCase(instruccion, ts):
    global cadenaTraduccion
    exp = generarExpresion(instruccion.exp, ts)
    etiquetaFinal = generarTemporalEtiqueta()
    for caso in instruccion.casos:
        if(caso.exp == None):
            ts_local = TS.TablaDeSimbolos(ts.simbolos)
            generarPrincipal(caso.sentencias, ts_local)
        else:
            exp2 = generarExpresion(caso.exp, ts)
            etiquetaFalso = generarTemporalEtiqueta()
            temporal = generarTemporalT()
            cadenaTraduccion += '\t\n'
            cadenaTraduccion += '\t' + str(temporal) + " = " + str(exp) + " != " + str(exp2) + ''
            cadenaTraduccion += '\t\n'
            cadenaTraduccion += '\tif ' + str(temporal) + ': goto. ' + str(etiquetaFalso) + ''
            ts_local = TS.TablaDeSimbolos(ts.simbolos)
            generarPrincipal(caso.sentencias, ts_local)
            cadenaTraduccion += '\t\n'
            cadenaTraduccion += '\tgoto. ' + etiquetaFinal + ''
            cadenaTraduccion += '\t\n'
            cadenaTraduccion += '\tlabel. ' + etiquetaFalso
    cadenaTraduccion += '\t\n'
    cadenaTraduccion += '\tlabel. ' + etiquetaFinal

def generarSentenciaIf(instruccion, ts, etiquetaFinal):
    global cadenaTraduccion
    temporal = generarExpresion(instruccion.exp,ts)
    etiquetaSi = generarTemporalEtiqueta()
    etiquetaSino = generarTemporalEtiqueta()
    if etiquetaFinal == None:
        etiquetaFinal = generarTemporalEtiqueta()
    cadenaTraduccion += '\t\n'
    cadenaTraduccion += '\tif  ' + str(temporal) + ' : goto. ' + str(etiquetaSi) + ''
    cadenaTraduccion += '\t\n'
    cadenaTraduccion += '\tgoto. ' + etiquetaSino + ''
    if isinstance(instruccion.sino, SentenciaIf):
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tlabel. ' + etiquetaSi
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        generarPrincipal(instruccion.si, ts_local)
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tgoto. ' + etiquetaFinal + ''
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tlabel. ' + etiquetaSino
        generarSentenciaIf(instruccion.sino, ts, etiquetaFinal)
    elif (instruccion.sino == None):
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tlabel. ' + etiquetaSi
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        generarPrincipal(instruccion.si, ts_local)
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tlabel. ' +  etiquetaSino
    else:
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tlabel. ' +  etiquetaSi
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        generarPrincipal(instruccion.si, ts_local)
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tgoto. ' + etiquetaFinal + ''
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tlabel. ' + etiquetaSino
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        generarPrincipal(instruccion.sino, ts_local)
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\tlabel. ' + etiquetaFinal

def generarImpresion(instruccion, ts):
    global cadenaTraduccion
    tamaño = len(instruccion.impresiones)
    if tamaño == 1:
        cadena = generarExpresion(instruccion.impresiones[0], ts)
        if(cadena[1:-1] == '\n'):
            cadenaTraduccion += '\t\n'
            cadenaTraduccion += "\tprint(\'\\n\')"
        elif(cadena[0] == '\'' or cadena[0] == '"'):
            cadena = cadena[1:-1]
            cadena = cadena.replace('\\n', ' \\n ')
            cadenas = cadena.split()
            tempCadena = ''
            for elemento in cadenas:
                if elemento == '\\n':
                    cadenaTraduccion += '\t\n'
                    cadenaTraduccion += "\tprint(\'" + tempCadena + " \')"
                    tempCadena = ''
                    cadenaTraduccion += '\t\n'
                    cadenaTraduccion += "\tprint(\'\\n\')"
                else:
                    tempCadena += elemento + " "
            if tempCadena != '':
                cadenaTraduccion += '\t\n'
                cadenaTraduccion += "\tprint(\'" + tempCadena + " \')"
                tempCadena = ''
        else:
            cadenaTraduccion += '\t\n'
            cadenaTraduccion += "\tprint(" + cadena + " )"
    else:
        cadena = generarExpresion(instruccion.impresiones.pop(0), ts)
        cadena = cadena[1:-1]
        cadena = cadena.replace('%', ' % ')
        cadena = cadena.replace('\\n', ' \\n')
        cadenas = cadena.split()
        tempCadena = ''
        for elemento in cadenas:
            if elemento == '%':
                cadenaTraduccion += '\t\n'
                cadenaTraduccion += "\tprint(\'" + tempCadena + " \')"
                tempCadena = ''
                cadenaTraduccion += '\t\n'
                temp = generarExpresion(instruccion.impresiones.pop(0), ts)
                cadenaTraduccion += '\t\n'
                cadenaTraduccion += "\tprint(" + temp + ")"
            elif elemento == '\\n':
                cadenaTraduccion += '\t\n'
                cadenaTraduccion += "\tprint(\'" + tempCadena + " \')"
                tempCadena = ''
                cadenaTraduccion += '\t\n'
                cadenaTraduccion += "\tprint(\'\\n\')"
            else:
                tempCadena += elemento + " "
        if tempCadena != '':
            cadenaTraduccion += '\t\n'
            cadenaTraduccion += "\tprint(\'" + tempCadena + " \')"
            tempCadena = ''

def generarAsignacion(instruccion, ts):
    global cadenaTraduccion
    temporal1 = generarExpresion(instruccion.exp, ts)
    simboloTemporal = ts.obtener(instruccion.id)
    temporal2 = simboloTemporal.temporal
    if temporal1 != temporal2:
        simbolo = TS.Simbolo(instruccion.id, simboloTemporal.tipo, temporal1, temporal2)
        ts.agregar(simbolo)
        cadenaTraduccion += '\t\n'
        cadenaTraduccion += '\t' + str(temporal2) + " = " + str(temporal1) + ""

def getTipo(tipo):
    if tipo == TIPO_DATO.INT:
        return TS.TIPO_DATO.ENTERO
    elif tipo == TIPO_DATO.CHAR:
        return TS.TIPO_DATO.CHARACTER
    elif tipo == TIPO_DATO.DOUBLE:
        return TS.TIPO_DATO.FLOTANTE
    elif tipo == TIPO_DATO.FLOAT:
        return TS.TIPO_DATO.FLOTANTE
    elif tipo == TIPO_DATO.STRING:
        return TS.TIPO_DATO.STRING
    elif tipo == TIPO_DATO.BOOLEAN:
        return TS.TIPO_DATO.BOOLEAN

def getEmpty(tipo):
    if tipo == TIPO_DATO.INT:
        return 0
    elif tipo == TIPO_DATO.CHAR:
        return "\'\'"
    elif tipo == TIPO_DATO.DOUBLE:
        return 0
    elif tipo == TIPO_DATO.FLOAT:
        return 0
    elif tipo == TIPO_DATO.STRING:
        return "\'\'"
    elif tipo == TIPO_DATO.BOOLEAN:
        return False

def getOperador(operador):
    if operador == OPERADOR.MAS:
        return "+"
    elif operador == OPERADOR.MENOS:
        return "-"
    elif operador == OPERADOR.POR:
        return "*"
    elif operador == OPERADOR.DIVIDIDO:
        return "/"
    elif operador == OPERADOR.NOT:
        return "!"
    elif operador == OPERADOR.AND:
        return "&&"
    elif operador == OPERADOR.OR:
        return "||"
    elif operador == OPERADOR.XOR:
        return "xor"
    elif operador == OPERADOR.NOTB:
        return "~"
    elif operador == OPERADOR.ANDB:
        return "&"
    elif operador == OPERADOR.ORB:
        return "|"
    elif operador == OPERADOR.XORB:
        return "^"
    elif operador == OPERADOR.SHIFTD:
        return ">>"
    elif operador == OPERADOR.SHIFTI:
        return "<<"
    elif operador == OPERADOR.IGUAL:
        return "=="
    elif operador == OPERADOR.DIFERENTE:
        return "!="
    elif operador == OPERADOR.MAYORIGUAL:
        return ">="
    elif operador == OPERADOR.MENORIGUAL:
        return "<="
    elif operador == OPERADOR.MAYOR:
        return ">"
    elif operador == OPERADOR.MENOR:
        return "<"
    elif operador == OPERADOR.MOD:
        return "%"

def createDatabaseFuncion(instruccion, ts):
    global numFuncionSQL
    print(instruccion.cadena)
    cadenaSQL = generarFuncionesSQL(instruccion.cadena,numFuncionSQL)
    return cadenaSQL

def createShowDatabasesFuncion(instruccion, ts):
    global numFuncionSQL
    print(instruccion.cadena)
    cadenaSQL = generarFuncionesSQL(instruccion.cadena,numFuncionSQL)
    return cadenaSQL


def createUseDatabaseFuncion(instruccion, ts):
    global numFuncionSQL
    print(instruccion.cadena)
    cadenaSQL = generarFuncionesSQL(instruccion.cadena,numFuncionSQL)
    return cadenaSQL

def createDropDatabaseFuncion(instruccion, ts):
    global numFuncionSQL
    print(instruccion.cadena)
    cadenaSQL = generarFuncionesSQL(instruccion.cadena,numFuncionSQL)
    return cadenaSQL

def createShowTablesFuncion(instruccion, ts):
    global numFuncionSQL
    print(instruccion.cadena)
    cadenaSQL = generarFuncionesSQL(instruccion.cadena,numFuncionSQL)
    return cadenaSQL

def generarFuncionesSQL(instruccionSQL,numero):
    global numFuncionSQL
    cadenaFuncionSQL = ""
    cadenaFuncionSQL += "\n\tdef procesar_funcion"+str(numero)+"(self):"
    cadenaFuncionSQL += "\n\t\tglobal instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss"
    cadenaFuncionSQL += "\n\t\tinstrucciones = g.parse('"+instruccionSQL+"')"
    cadenaFuncionSQL += "\n\t\terroressss = ErrorHTML()"
    cadenaFuncionSQL += "\n\t\tif  erroressss.getList()== []:"
    cadenaFuncionSQL += "\n\t\t\tinstrucciones_Global = instrucciones"
    cadenaFuncionSQL += "\n\t\t\tts_global = TS.TablaDeSimbolos()"
    cadenaFuncionSQL += "\n\t\t\ttc_global = TC.TablaDeTipos()"
    cadenaFuncionSQL += "\n\t\t\ttc_global1 = tc_global"
    cadenaFuncionSQL += "\n\t\t\tts_global1 = ts_global"
    cadenaFuncionSQL += "\n\t\t\tsalida = procesar_instrucciones(instrucciones, ts_global,tc_global)"
    cadenaFuncionSQL += "\n\t\t\treturn salida"
    cadenaFuncionSQL += "\n\t\telse:"
    cadenaFuncionSQL += "\n\t\t\treturn 'Parser Error'\n\n"
    numFuncionSQL += 1
    return cadenaFuncionSQL

'''f = open("./entrada.txt", "r")
input = f.read()
instrucciones = runC3D(input)
instrucciones_Global = instrucciones
ts_global = TS.TablaDeSimbolos()
codigo3D = generarC3D(instrucciones, ts_global)
salida = open("./salida3D.py", "w")
salida.write(codigo3D)
salida.close()'''

'''if len(ts.simbolos) > 0:
    for simb in ts_global.simbolos.values():
        print(simb.id,simb.tipo,simb.valor,simb.temporal)
    
if len(tf.funciones) > 0:
    for simb in tf.funciones.values():
        for ins in simb.instrucciones.instrucciones:
            print(simb.id,simb.tipo,simb.parametros,simb.temporales,ins)'''
