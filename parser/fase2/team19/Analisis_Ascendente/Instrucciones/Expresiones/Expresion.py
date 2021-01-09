from Analisis_Ascendente.Instrucciones.Expresiones.Binario import Binario
from Analisis_Ascendente.Instrucciones.Time import Time
from Analisis_Ascendente.Instrucciones.expresion import *
import Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica as Trigonometrica
import Analisis_Ascendente.Instrucciones.Expresiones.Math as Math
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
from Analisis_Ascendente.Instrucciones.PLPGSQL.Declaracion import Declaracion
from Analisis_Ascendente.Instrucciones.PLPGSQL.Return import Return
from Analisis_Ascendente.Instrucciones.PLPGSQL.plasignacion import Plasignacion
from Analisis_Ascendente.reportes import Reportes
from C3D import GeneradorTemporales

class Expresion(Exp):
    def __init__(self, iz, dr, operador,fila,columna):
        self.iz = iz
        self.dr = dr
        self.operador = operador
        self.fila = fila
        self.columna = columna

    def getC3D(self, listop):
        codigo = {}
        etq = GeneradorTemporales.nuevo_temporal()
        code = '    %s = ' % etq
        nodo = self
        while isinstance(nodo, Expresion):
            if isinstance(nodo.iz, Id):
                code += nodo.iz.id + ' '
                if nodo.operador == '+':
                    if isinstance(nodo.dr, Primitivo):
                        if nodo.dr.valor == 0:
                            optimizacion1 = Reportes.ListaOptimizacion(nodo.iz.id + nodo.operador + '0', "Se elimino la instrucción",
                                    Reportes.TipoOptimizacion.REGLA8)
                            listop.append(optimizacion1)
                            break
                elif nodo.operador == '-':
                    if isinstance(nodo.dr, Primitivo):
                        if nodo.dr.valor == 0:
                            optimizacion1 = Reportes.ListaOptimizacion(nodo.iz.id + nodo.operador + '0', "Se elimino la instrucción",
                                    Reportes.TipoOptimizacion.REGLA9)
                            listop.append(optimizacion1)
                            break
                elif nodo.operador == '/':
                    if isinstance(nodo.dr, Primitivo):
                        if nodo.dr.valor == 1:
                            optimizacion1 = Reportes.ListaOptimizacion(nodo.iz.id + nodo.operador + '1', "Se elimino la instrucción",
                                    Reportes.TipoOptimizacion.REGLA10)
                            listop.append(optimizacion1)
                            break
                elif nodo.operador == '-':
                    if isinstance(nodo.dr, Primitivo):
                        if nodo.dr.valor == 1:
                            optimizacion1 = Reportes.ListaOptimizacion(nodo.iz.id + nodo.operador + '1', "Se elimino la instrucción",
                                    Reportes.TipoOptimizacion.REGLA11)
                            listop.append(optimizacion1)
                            break
                else:
                    code += nodo.operador + ''
            elif isinstance(nodo.iz, Primitivo):
                if isinstance(nodo.iz.valor, str):
                    code += '\''+nodo.dr.valor + '\' '
                else:
                    code += str(nodo.iz.valor)
                code += nodo.operador + ' '
            elif isinstance(nodo.iz, Expresion):
                dicto = nodo.iz.getC3D(listop)
                code = '\n'+dicto["code"] + '\n'
            if isinstance(nodo.dr, Primitivo):
                if isinstance(nodo.dr.valor, str):
                    code += '\''+nodo.dr.valor + '\''
                else:
                    code += str(nodo.dr.valor)
            elif isinstance(nodo.dr, Time):
                code += nodo.dr.getC3D()
            elif isinstance(nodo.dr, Trigonometrica.Trigonometrica):
                code += nodo.dr.getC3D()
            elif isinstance(nodo.dr, Math.Math_):
                code += nodo.dr.getC3D()
            elif isinstance(nodo.dr, Expresion):
                dicto = nodo.dr.getC3D(listop)
                code += '\n'+dicto["code"] + '\n'
            nodo = nodo.dr
        code += ''
        codigo = {
            "code": code,
            "tmp": etq
        }
        return codigo

    def get_quemado(self):
        return '%s %s %s' % (self.iz.get_quemado(), self.operador, self.dr.get_quemado())

    def limpiarFuncion(expr,tsglobal):
        if isinstance(expr,Funcion):
            bdactual = tsglobal.buscar_sim("usedatabase1234")
            BD = tsglobal.buscar_sim(bdactual.valor)
            entornoBD = BD.Entorno
            try:
                if entornoBD.validar_sim(expr.id) == 1:  # Verificamos si el nombre de la función existe en la DB
                    simboloFuncion = entornoBD.buscar_sim(expr.id)
                    Expresion.vaciarFuncion(simboloFuncion)
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

    def ResolverFuncion(expr,tsglobal,tstabla,Consola,exception):
        if isinstance(expr, Funcion):
            return Expresion.ejecutarFuncion(expr,tsglobal,tstabla,Consola,exception)

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
            elif expr.operador == '==':
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
                simvariable = ts.buscar_sim(expr.id)
                return simvariable.valor
            else:
                return 'holamundo' #No deberia de pasar
        elif isinstance(expr, Primitivo):
            if expr.valor == 'TRUE':
                return True
            elif expr.valor == 'FALSE':
                return False
            else:
                return expr.valor
        elif isinstance(expr, Trigonometrica.Trigonometrica):
            return Trigonometrica.Trigonometrica.Resolver(expr,ts,Consola,exception)
        elif isinstance(expr, Math.Math_):
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

    def ejecutarFuncion(expr,tsglobal,ts,consola,expection):
        bdactual = tsglobal.buscar_sim("usedatabase1234")
        BD = tsglobal.buscar_sim(bdactual.valor)
        entornoBD = BD.Entorno
        try:
            if entornoBD.validar_sim(expr.id) == 1:             #Verificamos si el nombre de la función existe en la DB
                simboloFuncion = entornoBD.buscar_sim(expr.id)
                if expr.listaexpresiones == None:
                        Expresion.ejecutarSentencias(ts,simboloFuncion,consola,expection)
                        return simboloFuncion.valor
                else:
                    correcto = Expresion.asignarArgumentos(simboloFuncion,expr.listaexpresiones,ts,consola,expection)  #ASIGNAMOS VALORES A LOS PARAMETROS
                    if correcto:
                        Expresion.ejecutarSentencias(ts,simboloFuncion,consola,expection)
                        return simboloFuncion.valor
                    else:
                        return "Parametros incorrectos"
            else:
                return "No existe esa función"
        except:
            return "Error en ejecutar la Funcion"

    def asignarArgumentos(simboloFuncion,listaExpresiones,ts,consola,exception):
        #VERFICAMOS CADA EXPRESION CON EL TIPO DE DATO DE CADA PARAMETRO
        argumentoscorrectos = True
        for expresion in listaExpresiones:
            expresuelta = Expresion.Resolver(expresion,ts,consola,exception)
            entornoFN = simboloFuncion.Entorno
            for simbolo in entornoFN.simbolos.values():  #simbolo = una variable
                if simbolo.categoria == TS.TIPO_DATO.PARAMETRO and simbolo.valor == None:
                    correcto = Expresion.verificarArgumento(expresuelta,simbolo.tipo)
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

    def ejecutarSentencias(ts,simboloFuncion,consola,exception):
        #Ejecutamos el bloque de las declaraciones
        simbolodeclare = simboloFuncion.Entorno.buscar_sim('DECLARE')
        if simbolodeclare is not None:
            declaraciones = simbolodeclare.valor                                #List de objetos: Declaracion
            for declaracion in declaraciones:
                if isinstance(declaracion,Declaracion):
                    ejecutarDeclaracion(declaracion,simboloFuncion,ts,consola,exception)
        #Ejecutamos el bloque begin
        simbolobegin = simboloFuncion.Entorno.buscar_sim('BEGIN')           #List de objetos: cualquier instruccion
        instrucciones = simbolobegin.valor
        for instr in instrucciones:
            if isinstance(instr,Plasignacion):
                ejecutarPlasignacion(instr,ts,simboloFuncion,consola,exception)
            elif isinstance(instr,Return):
                ejecutarReturn(instr,ts,simboloFuncion,consola,exception)


def ejecutarPlasignacion(plasignacion,ts,simboloFuncion,consola,exception):
    #Validamos que la variable exista en la función
    entornoFN =  simboloFuncion.Entorno
    if entornoFN.validar_sim(plasignacion.id) == 1:
        simvariable = entornoFN.buscar_sim(plasignacion.id)
        valorRetorno = ResolverReturn(plasignacion.expresion,ts,entornoFN,consola,exception)
        if valorRetorno == 'TRUE':
            valorRetorno = True
        elif valorRetorno == 'FALSE':
            valorRetorno = False
        #verifico que concuerde el tipo de la expresion con el tipo de la variable
        correcto = verificarRetorno(valorRetorno,simvariable.tipo.tipo)
        if correcto:
            simvariable.valor = valorRetorno
        else:
            consola.append(f"Error: El valor a asignar a la variable: {simvariable.id} no coincide con su tipo")
    else:
        consola.append(f"Error: No existe la variable: {plasignacion.id} en la función: {simboloFuncion.id}")


def ejecutarDeclaracion(declaracion,simboloFuncion,ts,consola,exception):
    entornoFN = simboloFuncion.Entorno
    nuevosimbolo = None
    if declaracion.asignacion == None:
        nuevosimbolo = TS.Simbolo(TS.TIPO_DATO.DECLARE, declaracion.id, declaracion.tipo, None, None)
    else:
        expre = Expresion.Resolver(declaracion.asignacion,ts,consola,exception)
        nuevosimbolo = TS.Simbolo(TS.TIPO_DATO.DECLARE, declaracion.id, declaracion.tipo, expre, None)
    entornoFN.agregar_sim(nuevosimbolo)

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

def ResolverReturn(expr,ts,entornoFuncion,Consola,exception):
        if isinstance(expr,Expresion):
            exp1 = ResolverReturn(expr.iz,ts,entornoFuncion,Consola,exception)
            exp2 = ResolverReturn(expr.dr,ts,entornoFuncion,Consola,exception)
            if expr.operador == '=':
                return exp1 == exp2
            elif expr.operador == '*':
                # id = expresion
                # id = (x < 9)
                if (isinstance(exp1,float) and isinstance(exp2,float)) or (isinstance(exp1,int) and isinstance(exp2,int)) or (isinstance(exp1,float) and isinstance(exp2,int))  or (isinstance(exp1,int) and isinstance(exp2,float)) :
                    return exp1 * exp2
                return 'error'
            elif expr.operador == '/':
                if (isinstance(exp1,float) and isinstance(exp2,float)) or (isinstance(exp1,int) and isinstance(exp2,int)) or (isinstance(exp1,float) and isinstance(exp2,int))  or (isinstance(exp1,int) and isinstance(exp2,float)) :
                    return exp1 / exp2
                return 'error'
            elif expr.operador == '+':
                if (isinstance(exp1,float) and isinstance(exp2,float)) or (isinstance(exp1,int) and isinstance(exp2,int)) or (isinstance(exp1,float) and isinstance(exp2,int))  or (isinstance(exp1,int) and isinstance(exp2,float)):
                    return exp1 + exp2
                return 'error'
            elif expr.operador == '-':
                if (isinstance(exp1,float) and isinstance(exp2,float)) or (isinstance(exp1,int) and isinstance(exp2,int)) or (isinstance(exp1,float) and isinstance(exp2,int))  or (isinstance(exp1,int) and isinstance(exp2,float)):
                    return exp1 - exp2
                return 'error'
            elif expr.operador == '^':
                if (isinstance(exp1,float) and isinstance(exp2,float)) or (isinstance(exp1,int) and isinstance(exp2,int)) or (isinstance(exp1,float) and isinstance(exp2,int))  or (isinstance(exp1,int) and isinstance(exp2,float)):
                    return exp1 ** exp2
                return 'error'
            elif expr.operador == '%':
                if (isinstance(exp1,float) and isinstance(exp2,float)) or (isinstance(exp1,int) and isinstance(exp2,int)) or (isinstance(exp1,float) and isinstance(exp2,int))  or (isinstance(exp1,int) and isinstance(exp2,float)):
                    return exp1 % exp2
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
            if ts.validar_sim(expr.id) == 1:       #Esta opción no debería de ejecutarse normalmente
                simbolo = ts.buscar_sim(expr.id)
                return simbolo.valor
            else:
                #VERIFICAMOS SI ES UNA VARIABLE DE LA FUNCION
                if entornoFuncion.validar_sim(expr.id) == 1:
                    simbolo = entornoFuncion.buscar_sim(expr.id)
                    return simbolo.valor
        elif isinstance(expr, Primitivo):
            return expr.valor
        elif isinstance(expr, Trigonometrica.Trigonometrica):
            return Trigonometrica.Trigonometrica.Resolver(expr,ts,Consola,exception)
        elif isinstance(expr, Math.Math_):
            #print("estoy llegango")
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

def verificarRetorno(valorRetorno, tipoFuncion) -> bool:
    correcto = False
    if isinstance(valorRetorno, int) and (
            tipoFuncion == 'SMALLINT' or tipoFuncion == 'INTEGER' or tipoFuncion == 'BIGINT' or tipoFuncion == 'NUMERIC' or tipoFuncion == 'SERIAL'):
        correcto = True
    elif isinstance(valorRetorno, float) and (
            tipoFuncion == 'REAL' or tipoFuncion == 'DOUBLE' or tipoFuncion == 'MONEY' or tipoFuncion.startswith(
            'DECIMAL')):
        correcto = True
    elif isinstance(valorRetorno, bool) and tipoFuncion == 'BOOLEAN':
        correcto = True
    elif isinstance(valorRetorno, str) and (
            tipoFuncion == 'TEXT' or tipoFuncion.startswith('CHARACTER') or tipoFuncion.startswith(
            'VARCHAR') or tipoFuncion.startswith('CHAR')):
        correcto = True
    elif tipoFuncion == 'TIMESTAMP' or tipoFuncion == 'DATE' or tipoFuncion == 'TIME' or tipoFuncion == 'INTERVAL':
        correcto = True
    return correcto

