import  math

from tytus.parser.team21.Analisis_Ascendente.Instrucciones.Expresiones.Binario import Binario
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion,IdId
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.Time import Time
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.expresion import *

import tytus.parser.team21.Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica as Trigonometrica
import tytus.parser.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math as  Math

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

