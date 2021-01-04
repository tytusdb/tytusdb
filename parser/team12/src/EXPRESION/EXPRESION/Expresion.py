import sys, os.path

nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\AST\\')
sys.path.append(nodo_dir)

nodo_tipo = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\ENTORNO\\')
sys.path.append(nodo_tipo)

exp_logica = (os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))+"\\EXPRESION_LOGICA\\")
sys.path.append(exp_logica)

exp_aritmetica = (os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))+"\\EXPRESION_ARITMETICA\\")
sys.path.append(exp_aritmetica)

exp_relacional = (os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))+"\\EXPRESION_RELACIONAL\\")
sys.path.append(exp_relacional)


from Nodo import Nodo
from Tipo_Expresion import Type_Expresion
from Tipo import Data_Type
from Expresion_Logica import *
from Expresion_Aritmetica import *
from Expresion_Relacional import * 

class Expresion(Nodo):

    def __init__(self, nombreNodo, fila, columna, valor):
        Nodo.__init__(self, nombreNodo, fila, columna, valor)
        self.tipo = Type_Expresion(Data_Type.non)
        self.valorExpresion = None

    def execute(self, enviroment):

        cantHijos = len(self.hijos)

        if cantHijos == 3 :

            op = self.hijos[1]
            exp1 = self.hijos[0]
            exp2 = self.hijos[2]
            expRes = Expresion("E",-1,-1,None)
            
            # VERIFICACION DE OPERACIONES LÓGICAS
            if op.nombreNodo == "AND":
                
                x = AND(exp1, exp2, expRes, enviroment)
                self.tipo = expRes.tipo
                self.valorExpresion = expRes.valorExpresion
                return self.valorExpresion
            
            elif op.nombreNodo == 'OR':

                x = OR(exp1, exp2, expRes, enviroment)
                self.tipo = expRes.tipo
                self.valorExpresion = expRes.valorExpresion
                return self.valorExpresion

            # VERIFICACION DE OPERACIONES RELACIONALES
            elif op.nombreNodo == "<>":

                x = diferente(exp1, exp2, expRes, enviroment)
                self.tipo = expRes.tipo
                self.valorExpresion = expRes.valorExpresion
                return self.valorExpresion

            elif op.nombreNodo == "=":

                x = igualdad(exp1, exp2, expRes, enviroment)
                self.tipo = expRes.tipo
                self.valorExpresion = expRes.valorExpresion
                return self.valorExpresion
            
            elif op.nombreNodo == ">":

                x = mayor(exp1, exp2, expRes, enviroment)
                self.tipo = expRes.tipo
                self.valorExpresion = expRes.valorExpresion
                return self.valorExpresion

            elif op.nombreNodo == ">=":

                x = mayorigual(exp1, exp2, expRes, enviroment)
                self.tipo = expRes.tipo
                self.valorExpresion = expRes.valorExpresion
                return self.valorExpresion

            elif op.nombreNodo == "<":

                x = menor(exp1, exp2, expRes, enviroment)
                self.tipo = expRes.tipo
                self.valorExpresion = expRes.valorExpresion
                return self.valorExpresion

            elif op.nombreNodo == "<=":

                x = menorigual(exp1, exp2, expRes, enviroment)
                self.tipo = expRes.tipo
                self.valorExpresion = expRes.valorExpresion
                return self.valorExpresion

            # VERIFICACION DE OPERACIONES ARITMETICAS
            elif op.nombreNodo == '^':

                x = pot(exp1, exp2, expRes, enviroment)
                self.tipo = expRes.tipo
                self.valorExpresion = expRes.valorExpresion
                return self.valorExpresion

            elif op.nombreNodo == '%':

                x = mod(exp1, exp2, expRes, enviroment)
                self.tipo = expRes.tipo
                self.valorExpresion = expRes.valorExpresion
                return self.valorExpresion
                
            if op.nombreNodo == '+':

                x = suma(exp1, exp2, expRes, enviroment)
                self.tipo = expRes.tipo
                self.valorExpresion = expRes.valorExpresion
                return self.valorExpresion

            elif op.nombreNodo == '-':

                x = resta(exp1, exp2, expRes, enviroment)
                self.tipo = expRes.tipo
                self.valorExpresion = expRes.valorExpresion
                return self.valorExpresion

            elif op.nombreNodo == '*':

                x = mult(exp1, exp2, expRes, enviroment)
                self.tipo = expRes.tipo
                self.valorExpresion = expRes.valorExpresion
                return self.valorExpresion

            elif op.nombreNodo == '/':

                x = div(exp1, exp2, expRes, enviroment)
                self.tipo = expRes.tipo
                self.valorExpresion = expRes.valorExpresion
                return self.valorExpresion

        elif cantHijos == 2:

            op = self.hijos[0]
            exp = self.hijos[1]
            print(exp.nombreNodo)            
            expValue = Expresion("E",-1,-1,None)

            if op.nombreNodo == 'NOT':                                

                x = NOT(exp,expValue,enviroment)
                self.tipo = expValue.tipo
                self.valorExpresion = expValue.valorExpresion
                return self.valorExpresion

            elif op.nombreNodo == '-':
                
                x = numNeg(exp, expValue, enviroment)
                self.tipo = expValue.tipo
                self.valorExpresion = expValue.valorExpresion
                return self.valorExpresion

        elif cantHijos == 1:

            exp = self.hijos[0]
            val = exp.execute(enviroment)
            self.tipo = exp.tipo
            self.valorExpresion = exp.valorExpresion
            return self.valorExpresion
        