from Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
from Analisis_Ascendente.Instrucciones.PLPGSQL.CasePL import CasePL
from Analisis_Ascendente.Instrucciones.PLPGSQL.Declaracion import Declaracion
from Analisis_Ascendente.Instrucciones.PLPGSQL.Ifpl import Ifpl
from Analisis_Ascendente.Instrucciones.PLPGSQL.Return import Return
from Analisis_Ascendente.Instrucciones.PLPGSQL.SelectCount import SelectCount
from Analisis_Ascendente.Instrucciones.PLPGSQL.plasignacion import Plasignacion
from Analisis_Ascendente.Instrucciones.Select import SelectDist, selectInst
from Analisis_Ascendente.Instrucciones.Select.Select2 import Selectp3
import Analisis_Ascendente.Instrucciones.Select.Select3 as Select3
from Analisis_Ascendente.Instrucciones.Select.select import Select
from Analisis_Ascendente.Instrucciones.Select.select1 import selectTime
from Analisis_Ascendente.Instrucciones.Time import Time
from Analisis_Ascendente.Instrucciones.expresion import *
import Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica as Trigonometrica
import Analisis_Ascendente.Instrucciones.Expresiones.Math as Math
from Analisis_Ascendente.Instrucciones.Expresiones.Binario import Binario
from Analisis_Ascendente.storageManager.jsonMode import extractTable


#PARA DEJAR VACIA LA FUNCION PARA SU PROXIMA EJECUCION
def limpiarFuncion(expr,tsglobal):
    if isinstance(expr, Funcion):
        bdactual = tsglobal.buscar_sim("usedatabase1234")
        BD = tsglobal.buscar_sim(bdactual.valor)
        entornoBD = BD.Entorno
        try:
            if entornoBD.validar_sim(expr.id) == 1:  # Verificamos si el nombre de la función existe en la DB
                simboloFuncion = entornoBD.buscar_sim(expr.id)
                vaciarFuncion(simboloFuncion)
        except:
            None

def vaciarFuncion(simboloFuncion):
    entornoFN = simboloFuncion.Entorno
    for simbolo in entornoFN.simbolos.values():
        if simbolo.categoria == TS.TIPO_DATO.PARAMETRO:
            simbolo.valor = None
        elif simbolo.categoria == TS.TIPO_DATO.DECLARACION:
            entornoFN.eliminar_sim(simbolo.id)
    simboloFuncion.valor = None



#PARA RESOLVER UNA FUNCION EN UN INSERT
def ResolverFuncion(expr,tsglobal,Consola,exception):
    if isinstance(expr, Funcion):
        return ejecutarFuncion(expr,tsglobal,Consola,exception)

def ejecutarFuncion(expr,tsglobal,consola,expection):
        bdactual = tsglobal.buscar_sim("usedatabase1234")
        BD = tsglobal.buscar_sim(bdactual.valor)
        entornoBD = BD.Entorno
        try:
            if entornoBD.validar_sim(expr.id) == 1:             #Verificamos si el nombre de la función existe en la DB
                simboloFuncion = entornoBD.buscar_sim(expr.id)
                if expr.listaexpresiones == None:
                        ejecutarSentencias(tsglobal,simboloFuncion,consola,expection)
                        return simboloFuncion.valor
                else:
                    correcto = asignarArgumentos(simboloFuncion,expr.listaexpresiones,tsglobal,consola,expection)  #ASIGNAMOS VALORES A LOS PARAMETROS
                    if correcto:
                        ejecutarSentencias(tsglobal,simboloFuncion,consola,expection)
                        return simboloFuncion.valor
                    else:
                        return "Parametros incorrectos"
            else:
                return "No existe esa función"
        except:
            return "Error en ejecutar la Funcion"

def ejecutarSentencias(tsglobal,simboloFuncion,consola,exceptions):
        #Ejecutamos el bloque de las declaraciones
        simbolodeclare = simboloFuncion.Entorno.buscar_sim('DECLARE')
        if simbolodeclare is not None:
            declaraciones = simbolodeclare.valor                                #List de objetos: Declaracion
            for declaracion in declaraciones:
                if isinstance(declaracion,Declaracion):
                    ejecutarDeclaracion(declaracion,simboloFuncion,tsglobal,consola,exceptions)
        #Ejecutamos el bloque begin
        simbolobegin = simboloFuncion.Entorno.buscar_sim('BEGIN')           #List de objetos: cualquier instruccion
        instrucciones = simbolobegin.valor
        for instr in instrucciones:
            if isinstance(instr,Plasignacion):
                ejecutarPlasignacion(instr,tsglobal,simboloFuncion,consola,exceptions)
            elif isinstance(instr,Return):
                ejecutarReturn(instr,tsglobal,simboloFuncion,consola,exceptions)
            elif isinstance(instr, Select):
                if instr.caso == 1:
                    consola.append('caso 1')
                    selectTime.ejecutar(instr, tsglobal, consola, exceptions, True)
                elif instr.caso == 2:
                    consola.append('caso 2')
                    variable = SelectDist.Select_Dist()
                    SelectDist.Select_Dist.ejecutar(variable, instr, tsglobal, consola, exceptions)
                elif instr.caso == 3:
                    consola.append('caso 3')
                    variable = selectInst.Select_inst()
                    selectInst.Select_inst.ejecutar(variable, instr, tsglobal, consola, exceptions)
                elif instr.caso == 4:
                    consola.append('caso 4')
                    Selectp3.ejecutar(instr, tsglobal, consola, exceptions, True)
            elif isinstance(instr, Ifpl):
                Ifpl.ejecutar(instr,tsglobal,simboloFuncion.Entorno,consola,exceptions)
            elif isinstance(instr, CasePL):
                CasePL.ejecutar(instr,simboloFuncion.Entorno, consola, exceptions)

def ejecutarDeclaracion(declaracion,simboloFuncion,ts,consola,exception):
    entornoFN = simboloFuncion.Entorno
    nuevosimbolo = None
    if declaracion.asignacion == None:
        nuevosimbolo = TS.Simbolo(TS.TIPO_DATO.DECLARE, declaracion.id, declaracion.tipo, None, None)
    else:
        expre = Expresion.Resolver(declaracion.asignacion,ts,consola,exception)
        nuevosimbolo = TS.Simbolo(TS.TIPO_DATO.DECLARE, declaracion.id, declaracion.tipo, expre, None)
    entornoFN.agregar_sim(nuevosimbolo)

def ejecutarPlasignacion(plasignacion,ts,simboloFuncion,consola,exception):
    #Validamos que la variable exista en la función
    entornoFN =  simboloFuncion.Entorno
    if entornoFN.validar_sim(plasignacion.id) == 1:
        simvariable = entornoFN.buscar_sim(plasignacion.id)
        if isinstance(plasignacion.expresion,SelectCount):
            valorRetorno = resolverSelectCount(plasignacion.expresion,ts)
        elif isinstance(plasignacion.expresion,Select):
            valorRetorno = resolverSelectGlobal(plasignacion.expresion,ts,consola,exception)
        else:
            valorRetorno = ResolverReturn(plasignacion.expresion,ts,entornoFN,consola,exception)
        #verifico que concuerde el tipo de la expresion con el tipo de la variable
        correcto = verificarRetorno(valorRetorno,simvariable.tipo.tipo)
        if correcto:
            simvariable.valor = valorRetorno
        else:
            consola.append(f"Error: El valor a asignar a la variable: {simvariable.id} no coincide con su tipo")
    else:
        consola.append(f"Error: No existe la variable: {plasignacion.id} en la función: {simboloFuncion.id}")

def ejecutarPlasignacionIf(plasignacion,ts,consola,exception,tsglobal):
    #Validamos que la variable exista en la función
    entornoFN = ts
    if entornoFN.validar_sim(plasignacion.id) == 1:
        simvariable = entornoFN.buscar_sim(plasignacion.id)
        if isinstance(plasignacion.expresion,SelectCount):
            valorRetorno = resolverSelectCount(plasignacion.expresion,tsglobal)
        else:
            valorRetorno = ResolverReturn(plasignacion.expresion,ts,entornoFN,consola,exception)
        #verifico que concuerde el tipo de la expresion con el tipo de la variable
        correcto = verificarRetorno(valorRetorno,simvariable.tipo.tipo)
        if correcto:
            simvariable.valor = valorRetorno
        else:
            consola.append(f"Error: El valor a asignar a la variable: {simvariable.id} no coincide con su tipo")
    else:
        consola.append(f"Error: No existe la variable: {plasignacion.id} ")


def resolverSelectCount(expresion,ts):
    bdactual = ts.buscar_sim("usedatabase1234")
    BD = ts.buscar_sim(bdactual.valor)
    entornoBD = BD.Entorno
    count = 0
    try:
        if entornoBD.validar_sim(expresion.idtabla) == 1:
            simtabla = entornoBD.buscar_sim(expresion.idtabla)
            registros = extractTable(BD.id,simtabla.id)
            count = len(registros)
            return count
        else:
            return count
    except:
        return count


def resolverSelectGlobal(instr,ts,consola,exceptions):
    valorselect = None
    if instr.caso == 1:
        valorselect = selectTime.ejecutar(instr, ts, consola, exceptions, True)
    elif instr.caso == 2:
        variable = SelectDist.Select_Dist()
        valorselect = SelectDist.Select_Dist.ejecutar(variable, instr, ts, consola, exceptions)
    elif instr.caso == 3:
        variable = selectInst.Select_inst()
        valorselect = selectInst.Select_inst.ejecutar(variable, instr, ts, consola, exceptions)
    elif instr.caso == 4:
        valorselect = Selectp3.ejecutar(instr, ts, consola, exceptions, True)
    elif instr.caso == 5:
        valorselect = Select3.Selectp4.ejecutar(instr, ts, consola, exceptions, True)
    #Convertimos a un int si se puede
    try:
        valor = int(valorselect)
        return valor
    except:
        return valorselect

def ejecutarReturn(Retu,ts,simfuncion,Consola,exception):
    valorRetorno = ResolverReturn(Retu.expr,ts,simfuncion.Entorno,Consola,exception)
    if valorRetorno == 'TRUE':
        valorRetorno = True
    elif valorRetorno == 'FALSE':
        valorRetorno = False
    #VERIFICAMOS SI EL VALOR DE RETORNO CON CUERDA CON EL RETURNS DE LA FUNCION
    correcto = verificarRetorno(valorRetorno,simfuncion.tipo)
    if correcto:
        simfuncion.valor = valorRetorno
        Consola.append(f"Se realizo el return de la función {simfuncion.id} con exito")
    else:
        simfuncion.valor = None
        Consola.append(f"El tipo de dato a retornar no concuerda con el tipo de returns de la función")

def ResolverReturn(expr, ts, entornoFuncion, Consola, exception):
        if isinstance(expr, Expresion):
            exp1 = ResolverReturn(expr.iz, ts, entornoFuncion, Consola, exception)
            exp2 = ResolverReturn(expr.dr, ts, entornoFuncion, Consola, exception)
            if expr.operador == '=':
                return exp1 == exp2
            elif expr.operador == '*':
                # id = expresion
                # id = (x < 9)
                if (isinstance(exp1, float) and isinstance(exp2, float)) or (
                        isinstance(exp1, int) and isinstance(exp2, int)) or (
                        isinstance(exp1, float) and isinstance(exp2, int)) or (
                        isinstance(exp1, int) and isinstance(exp2, float)):
                    return exp1 * exp2
                return 'error'
            elif expr.operador == '/':
                if (isinstance(exp1, float) and isinstance(exp2, float)) or (
                        isinstance(exp1, int) and isinstance(exp2, int)) or (
                        isinstance(exp1, float) and isinstance(exp2, int)) or (
                        isinstance(exp1, int) and isinstance(exp2, float)):
                    return exp1 / exp2
                return 'error'
            elif expr.operador == '+':
                if (isinstance(exp1, float) and isinstance(exp2, float)) or (
                        isinstance(exp1, int) and isinstance(exp2, int)) or (
                        isinstance(exp1, float) and isinstance(exp2, int)) or (
                        isinstance(exp1, int) and isinstance(exp2, float)):
                    return exp1 + exp2
                return 'error'
            elif expr.operador == '-':
                if (isinstance(exp1, float) and isinstance(exp2, float)) or (
                        isinstance(exp1, int) and isinstance(exp2, int)) or (
                        isinstance(exp1, float) and isinstance(exp2, int)) or (
                        isinstance(exp1, int) and isinstance(exp2, float)):
                    return exp1 - exp2
                return 'error'
            elif expr.operador == '^':
                if (isinstance(exp1, float) and isinstance(exp2, float)) or (
                        isinstance(exp1, int) and isinstance(exp2, int)) or (
                        isinstance(exp1, float) and isinstance(exp2, int)) or (
                        isinstance(exp1, int) and isinstance(exp2, float)):
                    return exp1 ** exp2
                return 'error'
            elif expr.operador == '%':
                if (isinstance(exp1, float) and isinstance(exp2, float)) or (
                        isinstance(exp1, int) and isinstance(exp2, int)) or (
                        isinstance(exp1, float) and isinstance(exp2, int)) or (
                        isinstance(exp1, int) and isinstance(exp2, float)):
                    return exp1 % exp2
                return 'error'
            elif expr.operador == '==':  # comparacion---------------------------------------
                boole = exp1 == exp2
                return boole
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
        elif isinstance(expr, Id):
            #VERIFICAMOS SI ES UNA VARIABLE DE LA FUNCION
            if ts.validar_sim(expr.id) == 1:
                simbolo = ts.buscar_sim(expr.id)
                return simbolo.valor
            else:
                if entornoFuncion.validar_sim(expr.id) == 1:
                    simbolo = entornoFuncion.buscar_sim(expr.id)
                    return simbolo.valor
        elif isinstance(expr, Primitivo):
            if expr.valor == 'TRUE':
                return True
            elif expr.valor == 'FALSE':
                return False
            else:
                return expr.valor
        elif isinstance(expr, Trigonometrica.Trigonometrica):
            return Trigonometrica.Trigonometrica.Resolver(expr, ts, Consola, exception)
        elif isinstance(expr, Math.Math_):
            # print("estoy llegango")
            return Math.Math_.Resolver(expr, ts, Consola, exception)
        elif isinstance(expr, Time):
            return Time.resolverTime(expr)
        elif isinstance(expr, Binario):
            return Binario.Resolver(expr, ts, Consola, exception)
        elif isinstance(expr, Unario):
            exp1 = Expresion.Resolver(expr.op, ts, Consola, exception)
            if expr.operador == '-':
                if isinstance(exp1, int) or isinstance(exp1, float):
                    return exp1 * -1
            elif expr.operador == '+':
                if isinstance(exp1, int) or isinstance(exp1, float):
                    return exp1
            elif expr.operador == '!':
                return not exp1

def asignarArgumentos(simboloFuncion,listaExpresiones,ts,consola,exception):
        #VERFICAMOS CADA EXPRESION CON EL TIPO DE DATO DE CADA PARAMETRO
        argumentoscorrectos = True
        for expresion in listaExpresiones:
            expresuelta = Expresion.Resolver(expresion,ts,consola,exception)
            entornoFN = simboloFuncion.Entorno
            for simbolo in entornoFN.simbolos.values():  #simbolo = una variable
                if simbolo.categoria == TS.TIPO_DATO.PARAMETRO and simbolo.valor == None:
                    correcto = verificarArgumento(expresuelta,simbolo.tipo)
                    if correcto:
                        simbolo.valor = expresuelta
                    else:
                        argumentoscorrectos = False
                    break
            if not argumentoscorrectos:
                for simbolo in entornoFN.simbolos:
                    if simbolo.categoria == TS.TIPO_DATO.PARAMETRO:
                        simbolo.valor = None
                break
        return argumentoscorrectos

def verificarArgumento(tipoargumento,tipoparametro):
        correcto = False
        if isinstance(tipoargumento,int) and (tipoparametro=='SMALLINT' or tipoparametro=='INTEGER' or tipoparametro=='BIGINT' or tipoparametro=='NUMERIC' or tipoparametro=='SERIAL'):
            correcto = True
        elif isinstance(tipoargumento,float) and (tipoparametro=='REAL' or tipoparametro=='DOUBLE' or tipoparametro=='MONEY'or tipoparametro.startswith('DECIMAL')):
            correcto = True
        elif isinstance(tipoargumento,bool) and tipoparametro=='BOOLEAN':
            correcto = True
        elif isinstance(tipoargumento,str) and (tipoparametro=='TEXT' or tipoparametro.startswith('CHARACTER') or tipoparametro.startswith('VARCHAR') or tipoparametro.startswith('CHAR')):
            correcto = True
        elif tipoparametro == 'TIMESTAMP' or tipoparametro=='DATE' or tipoparametro =='TIME' or tipoparametro=='INTERVAL':
            correcto = True
        return correcto

def verificarRetorno(valorRetorno, tipoFuncion) -> bool:
    correcto = False
    if isinstance(valorRetorno, int) and (tipoFuncion == 'SMALLINT' or tipoFuncion == 'INTEGER' or tipoFuncion == 'BIGINT' or tipoFuncion == 'NUMERIC' or tipoFuncion == 'SERIAL'):
        correcto = True
    elif isinstance(valorRetorno, float) and (tipoFuncion == 'REAL' or tipoFuncion == 'DOUBLE' or tipoFuncion == 'MONEY' or tipoFuncion.startswith('DECIMAL')):
        correcto = True
    elif isinstance(valorRetorno, bool) and tipoFuncion == 'BOOLEAN':
        correcto = True
    elif isinstance(valorRetorno, str) and (tipoFuncion == 'TEXT' or tipoFuncion.startswith('CHARACTER') or tipoFuncion.startswith('VARCHAR') or tipoFuncion.startswith('CHAR')):
        correcto = True
    elif tipoFuncion == 'TIMESTAMP' or tipoFuncion == 'DATE' or tipoFuncion == 'TIME' or tipoFuncion == 'INTERVAL':
        correcto = True
    return correcto

