from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
from Analisis_Ascendente.Instrucciones.expresion import *
from Analisis_Ascendente.Instrucciones.instruccion import *


class Ifpl(Instruccion):
    ''' #1 If
        #2 If elif else
        #3 If else '''
    global consola
    global exceptions

    def __init__(self, caso,e_if,s_if,elif_s,s_else, fila, columna):
        self.caso = caso
        self.e_if = e_if
        self.s_if = s_if
        self.elif_s = elif_s
        self.s_else = s_else
        self.fila = fila
        self.columna = columna

    def ejecutar(If, ts, consola, exceptions):
            if If.caso == 1:
                resultado = Expresion.Resolver(If.e_if, ts, consola, exceptions)
                if resultado == True:
                    for x in range(0, len(If.s_if)):
                       print(If.s_if[x])
                        #ejecutar sentencias
                else:
                    pass
            elif If.caso == 2:
                print('hola')
            else:
                resultado = Expresion.Resolver(If.e_if, ts, consola, exceptions)
                if resultado == True:
                    print('state')
                else:
                    print('state')
                    print('else')
                    print(If.e_if)
                    print(If.s_if)
                    print(If.s_else)
                    print(If.caso)
