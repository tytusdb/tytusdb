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

label_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))+"\\C3D\\")
sys.path.append(label_dir)

from Nodo import Nodo
from Tipo_Expresion import Type_Expresion
from Tipo import Data_Type
from Expresion_Logica import *
from Expresion_Aritmetica import *
from Expresion_Relacional import * 
from Label import *
from Temporal import *

class Expresion(Nodo):

    def __init__(self, nombreNodo, fila, columna, valor):
        Nodo.__init__(self, nombreNodo, fila, columna, valor)
        self.tipo = Type_Expresion(Data_Type.non)
        self.valorExpresion = None
        self.dir = ''
        self.cod = ''

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

    def compile(self, enviroment):

        cantHijos = len(self.hijos)

        if cantHijos == 3 :
            
            exp = self.hijos[0]
            op = self.hijos[1]
            exp2 = self.hijos[2]

            if op.nombreNodo == '+' :

                cod1 = exp.compile(enviroment)
                cod2 = exp2.compile(enviroment)

                self.dir = instanceTemporal.getTemporal()
                self.cod = cod1 + cod2 + self.dir + ' = ' + exp.dir + '+' + exp2.dir + '\n'
                self.tipo = Type_Expresion(Data_Type.numeric)
                return self.cod
            
            elif op.nombreNodo == '-':

                cod1 = exp.compile(enviroment)
                cod2 = exp2.compile(enviroment)

                self.dir = instanceTemporal.getTemporal()
                self.cod = cod1 + cod2 + self.dir + ' = ' + exp.dir + '-' + exp2.dir + '\n'
                self.tipo = Type_Expresion(Data_Type.numeric)
                return self.cod            
            
            elif op.nombreNodo == '*':

                cod1 = exp.compile(enviroment)
                cod2 = exp2.compile(enviroment)

                self.dir = instanceTemporal.getTemporal()
                self.cod = cod1 + cod2 + self.dir + ' = ' + exp.dir + '*' + exp2.dir + '\n'
                self.tipo = Type_Expresion(Data_Type.numeric)
                return self.cod
            
            elif op.nombreNodo == '/':

                cod1 = exp.compile(enviroment)
                cod2 = exp2.compile(enviroment)

                self.dir = instanceTemporal.getTemporal()                    
                self.cod = cod1 + cod2 + self.dir + ' = ' + exp.dir + '/' + exp2.dir + '\n'
                self.tipo = Type_Expresion(Data_Type.numeric)
                return self.cod
            
            elif op.nombreNodo == '^':

                cod1 = exp.compile(enviroment)
                cod2 = exp2.compile(enviroment)

                self.dir = instanceTemporal.getTemporal()
                self.cod = cod1 + cod2 + self.dir + ' = ' + exp.dir + '**' + exp2.dir + '\n'
                self.tipo = Type_Expresion(Data_Type.numeric)
                return self.cod
            
            elif op.nombreNodo == '%':

                cod1 = exp.compile(enviroment)
                cod2 = exp2.compile(enviroment)

                self.dir = instanceTemporal.getTemporal()
                self.cod = cod1 + cod2 + self.dir + ' = ' + exp.dir + '%' + exp2.dir + '\n'
                self.tipo = Type_Expresion(Data_Type.numeric)
                return self.cod
            
            elif op.nombreNodo == '<=':

                cod1 = exp.compile(enviroment)
                cod2 = exp2.compile(enviroment)

                self.tipo = Type_Expresion(Data_Type.boolean)

                # Generando Temporal
                self.dir = instanceTemporal.getTemporal()

                # Generando Etiqueta 1
                e1 = instanceLabel.getLabel()

                # Generando Etiqueta 2
                e2 = instanceLabel.getLabel()

                # Generando Etiqueta 3
                e3 = instanceLabel.getLabel()
                self.cod = cod1 + cod2 + 'if ' + exp.dir + ' <= ' + exp2.dir + ' :\n'
                self.cod += '\tgoto ' + e1 + '\n'
                self.cod += 'goto ' + e2
                self.cod += '\n'
                self.cod +=  'label ' + e1 + '\n'
                #self.cod += '\t' + self.dir + ' = 1\n'
                #self.cod += '\t' + 'goto ' + e3 + '\n'
                #self.cod += 'label ' + e2 + '\n'
                #self.cod += '\t' + self.dir + ' = 0\n'
                self.cod += self.dir + ' = 1\n'
                self.cod += 'goto ' + e3 + '\n'
                self.cod += 'label ' + e2 + '\n'
                self.cod += self.dir + ' = 0\n'
                self.cod += 'label ' + e3 + '\n'
                return self.cod                
            
            elif op.nombreNodo == '<':

                cod1 = exp.compile(enviroment)
                cod2 = exp2.compile(enviroment)

                self.tipo = Type_Expresion(Data_Type.boolean)

                # Generando Temporal
                self.dir = instanceTemporal.getTemporal()

                # Generando Etiqueta 1
                e1 = instanceLabel.getLabel()

                # Generando Etiqueta 2
                e2 = instanceLabel.getLabel()

                # Generando Etiqueta 3
                e3 = instanceLabel.getLabel()

                self.cod = cod1 + cod2 + 'if ' + exp.dir + ' < ' + exp2.dir + ' :\n'
                self.cod += '\tgoto ' + e1 + '\n'
                self.cod += 'goto ' + e2
                self.cod += '\n'
                self.cod +=  'label ' + e1 + '\n'
                #self.cod += '\t' + self.dir + ' = 1\n'
                #self.cod += '\t' + 'goto ' + e3 + '\n'
                #self.cod += 'label ' + e2 + '\n'
                #self.cod += '\t' + self.dir + ' = 0\n'
                self.cod += self.dir + ' = 1\n'
                self.cod += 'goto ' + e3 + '\n'
                self.cod += 'label ' + e2 + '\n'
                self.cod += self.dir + ' = 0\n'
                self.cod += 'label ' + e3 + '\n'
                return self.cod                
            
            elif op.nombreNodo == '>=':

                cod1 = exp.compile(enviroment)
                cod2 = exp2.compile(enviroment)

                self.tipo = Type_Expresion(Data_Type.boolean)

                # Generando Temporal
                self.dir = instanceTemporal.getTemporal()

                # Generando Etiqueta 1
                e1 = instanceLabel.getLabel()

                # Generando Etiqueta 2
                e2 = instanceLabel.getLabel()

                # Generando Etiqueta 3
                e3 = instanceLabel.getLabel()

                self.cod = cod1 + cod2 + 'if ' + exp.dir + ' >= ' + exp2.dir + ' :\n'
                self.cod += '\tgoto ' + e1 + '\n'
                self.cod += 'goto ' + e2
                self.cod += '\n'
                self.cod +=  'label ' + e1 + '\n'
                #self.cod += '\t' + self.dir + ' = 1\n'
                #self.cod += '\t' + 'goto ' + e3 + '\n'
                #self.cod += 'label ' + e2 + '\n'
                #self.cod += '\t' + self.dir + ' = 0\n'
                self.cod +=  self.dir + ' = 1\n'
                self.cod +=  'goto ' + e3 + '\n'
                self.cod += 'label ' + e2 + '\n'
                self.cod +=  self.dir + ' = 0\n'
                self.cod += 'label ' + e3 + '\n'
                return self.cod
            
            elif op.nombreNodo == '>':

                cod1 = exp.compile(enviroment)
                cod2 = exp2.compile(enviroment)

                self.tipo = Type_Expresion(Data_Type.boolean)

                # Generando Temporal
                self.dir = instanceTemporal.getTemporal()

                # Generando Etiqueta 1
                e1 = instanceLabel.getLabel()

                # Generando Etiqueta 2
                e2 = instanceLabel.getLabel()

                # Generando Etiqueta 3
                e3 = instanceLabel.getLabel()

                self.cod = cod1 + cod2 + 'if ' + exp.dir + ' > ' + exp2.dir + ' :\n'
                self.cod += '\tgoto ' + e1 + '\n'
                self.cod += 'goto ' + e2
                self.cod += '\n'
                self.cod +=  'label ' + e1 + '\n'
                #self.cod += '\t' + self.dir + ' = 1\n'
                #self.cod += '\t' + 'goto ' + e3 + '\n'
                #self.cod += 'label ' + e2 + '\n'
                #self.cod += '\t' + self.dir + ' = 0\n'
                self.cod += self.dir + ' = 1\n'
                self.cod +='goto ' + e3 + '\n'
                self.cod += 'label ' + e2 + '\n'
                self.cod +=self.dir + ' = 0\n'
                self.cod += 'label ' + e3 + '\n'
                return self.cod                
            
            elif op.nombreNodo == '<>':

                cod1 = exp.compile(enviroment)
                cod2 = exp2.compile(enviroment)

                self.tipo = Type_Expresion(Data_Type.boolean)

                # Generando Temporal
                self.dir = instanceTemporal.getTemporal()

                # Generando Etiqueta 1
                e1 = instanceLabel.getLabel()

                # Generando Etiqueta 2
                e2 = instanceLabel.getLabel()

                # Generando Etiqueta 3
                e3 = instanceLabel.getLabel()

                self.cod = cod1 + cod2 + 'if ' + exp.dir + ' != ' + exp2.dir + ' :\n'
                self.cod += '\tgoto ' + e1 + '\n'
                self.cod += 'goto ' + e2
                self.cod += '\n'
                self.cod +=  'label ' + e1 + '\n'
                #self.cod += '\t' + self.dir + ' = 1\n'
                #self.cod += '\t' + 'goto ' + e3 + '\n'
                #self.cod += 'label ' + e2 + '\n'
                #self.cod += '\t' + self.dir + ' = 0\n'
                self.cod +=  self.dir + ' = 1\n'
                self.cod += 'goto ' + e3 + '\n'
                self.cod += 'label '+ e2 + '\n'
                self.cod += self.dir + ' = 0\n'
                self.cod += 'label ' + e3 + '\n'
                return self.cod                
            
            elif op.nombreNodo == '=':

                cod1 = exp.compile(enviroment)
                cod2 = exp2.compile(enviroment)

                self.tipo = Type_Expresion(Data_Type.boolean)

                # Generando Temporal
                self.dir = instanceTemporal.getTemporal()

                # Generando Etiqueta 1
                e1 = instanceLabel.getLabel()

                # Generando Etiqueta 2
                e2 = instanceLabel.getLabel()

                # Generando Etiqueta 3
                e3 = instanceLabel.getLabel()

                self.cod = cod1 + cod2 + 'if ' + exp.dir + ' == ' + exp2.dir + ' :\n'
                self.cod += '\tgoto ' + e1 + '\n'
                self.cod += 'goto ' + e2
                self.cod += '\n'
                self.cod +=  'label ' + e1 + '\n'
                #self.cod += '\t' + self.dir + ' = 1\n'
                #self.cod += '\t' + 'goto ' + e3 + '\n'
                #self.cod += 'label ' + e2 + '\n'
                #self.cod += '\t' + self.dir + ' = 0\n'
                self.cod += self.dir + ' = 1\n'
                self.cod += 'goto ' + e3 + '\n'
                self.cod += 'label ' + e2 + '\n'
                self.cod += self.dir + ' = 0\n'
                self.cod += 'label ' + e3 + '\n'
                return self.cod                
            
            elif op.nombreNodo == 'AND':

                cod1 = exp.compile(enviroment)
                cod2 = exp2.compile(enviroment)

                self.tipo = Type_Expresion(Data_Type.boolean)

                # Generando Temporal
                self.dir = instanceTemporal.getTemporal()

                # Generando Etiqueta 1
                e1 = instanceLabel.getLabel()

                # Generando Etiqueta 2
                e2 = instanceLabel.getLabel()

                # Generando Etiqueta 3
                e3 = instanceLabel.getLabel()

                # Generando Etiqueta 4
                e4 = instanceLabel.getLabel()

                self.cod = cod1
                self.cod += 'if ' + exp.dir + ' ==  1 :\n'
                self.cod += '\tgoto ' + e1 + '\n'
                self.cod += 'goto ' + e2 + '\n'
                self.cod += 'label ' + e1 + '\n'
                self.cod += cod2
                self.cod += 'if ' + exp2.dir + ' ==  1 :\n'
                self.cod += '\tgoto ' + e3 + '\n'
                self.cod += 'goto ' + e2 + '\n'
                self.cod += 'label ' + e3 + '\n'
                self.cod += self.dir + ' = 1 \n'
                self.cod += 'goto ' + e4 + '\n'
                self.cod += 'label ' + e2
                self.cod += self.dir + ' = 0 \n'
                self.cod += 'label ' + e4 + '\n'
                return self.cod            

            elif op.nombreNodo == 'OR':

                cod1 = exp.compile(enviroment)
                cod2 = exp2.compile(enviroment)

                self.tipo = Type_Expresion(Data_Type.boolean)

                # Generando Temporal
                self.dir = instanceTemporal.getTemporal()

                # Generando Etiqueta 1
                e1 = instanceLabel.getLabel()

                # Generando Etiqueta 2
                e4 = instanceLabel.getLabel()

                # Generando Etiqueta 3
                e5 = instanceLabel.getLabel()

                self.cod = cod1
                self.cod += 'if ' + exp.dir + ' ==  1 :\n'
                self.cod += '\tgoto ' + e1 + '\n'
                self.cod += cod2
                self.cod += 'if ' + exp2.dir + ' ==  1 :\n'
                self.cod += '\tgoto ' + e1 + '\n'
                self.cod += 'goto ' + e4 + '\n'
                self.cod += 'label ' + e1 + '\n'
                self.cod += self.dir + ' = 1 \n'
                self.cod += 'goto ' + e5 + '\n'
                self.cod += 'label ' + e4 + '\n'
                self.cod += self.dir + ' = 0 \n'
                self.cod += 'label ' + e5 + '\n'
                return self.cod                                            
            
        elif cantHijos == 2 :

            op = self.hijos[0]
            exp = self.hijos[1]

            if op.nombreNodo == '!':
                
                cod = exp.compile(enviroment)

                # Etiqueta 1
                e1 = instanceLabel.getLabel()                    

                # Etiqueta 2
                e2 = instanceLabel.getLabel()

                # Etiqueta Salida
                e3 = instanceLabel.getLabel()

                # Temporal
                self.dir = instanceTemporal.getTemporal()
                self.cod += cod
                self.cod += 'if ' + exp.dir + ' == 1 :\n'
                self.cod += '\tgoto ' + e1 + '\n'
                self.cod += 'goto ' + e2 + '\n'
                self.cod += 'label ' + e1 + '\n'
                self.cod += self.dir + ' = 0 \n'
                self.cod += 'goto ' + e3 + '\n'
                self.cod += 'label ' + e2 + '\n'
                self.cod += self.dir + ' = 1 \n'
                self.cod += 'label ' + e3 + '\n'
                return self.cod

            elif op.nombreNodo == '-':
                
                cod = exp.compile(enviroment)
                self.tipo = Type_Expresion(Data_Type.numeric)
                self.dir = instanceTemporal.getTemporal()
                self.cod = cod
                self.cod += self.dir + ' = ' + exp.dir + ' * -1' + '\n'
                return self.cod

            pass
        elif cantHijos == 1 :
            
            exp = self.hijos[0]
            codExp = exp.compile(enviroment)
            self.dir = exp.dir
            self.cod = codExp
            return self.cod
    
    def getText(self):
        cantHijos = len(self.hijos)

        if cantHijos == 3 :

            op = self.hijos[1]
            exp1 = self.hijos[0]
            exp2 = self.hijos[2]
            
            stringRespuesta = '('+'('+exp1.getText()+')'+op.getText()+'('+exp2.getText()+')'+')'
            return stringRespuesta

        elif cantHijos == 2:

            op = self.hijos[0]
            exp = self.hijos[1]

            stringRespuesta = op.getText() + '(' + exp.getText() + ')'
            return stringRespuesta

        elif cantHijos == 1:

            exp = self.hijos[0]
            val = exp.getText()
            return val