from .AST.expression import *
from .AST.symbol import *
from .AST.error import * 
from .executeValue import executeValue

import math
import random
import hashlib

from datetime import datetime

def executeExpression(self, expression):
            s = Symbol('', 1, 1, 0, 0)
            if isinstance(expression, Value):
                return executeValue(self,expression)
            # EXPRESIONES ARITMETICAS
            if isinstance(expression, Arithmetic):
                e1 = executeExpression(self,expression.value1)
                e2 = executeExpression(self,expression.value2)
                if isinstance(e1, Error):
                    return e1
                elif isinstance(e2, Error):
                    return e2
                else:
                    try:
                        if(expression.type == '+'):
                            # SUMAS
                            if(e1.type == 1 and e2.type == 1):
                                s.value = int(e1.value) + int(e2.value)
                                s.type = 1
                                return s
                            elif(e1.type == 2 and e2.type == 2):
                                s.value = float(e1.value) + float(e2.value)
                                s.type = 2
                                return s

                            elif((e1.type == 1 and e2.type == 2) or (e1.type == 2 and e2.type == 1)):
                                s.value = float(e1.value) + float(e2.value)
                                s.type = 2
                                return s

                            elif(e1.type == 3 and e2.type == 3):
                                s.value = str(e1.value) + str(e2.value)
                                s.type = 3
                                return s
                            else:
                                return Error('Semantico', 'No se pueden sumar los types ' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)

                        elif(expression.type == '-'):
                            # RESTA
                            if(e1.type == 1 and e2.type == 1):
                                s.value = int(e1.value) - int(e2.value)
                                s.type = 1
                                return s
                            elif(e1.type == 2 and e2.type == 2):
                                s.value = float(e1.value) - float(e2.value)
                                s.type = 2
                                return s
                            
                            elif((e1.type == 1 and e2.type == 2) or (e1.type == 2 and e2.type == 1)):
                                s.value = float(e1.value) - float(e2.value)
                                s.type = 2
                                return s

                            else:
                                return Error('Semantico', 'No se pueden restar los types ' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)
                        elif(expression.type == '*'):
                            # MULT
                            if(e1.type == 1 and e2.type == 1):
                                s.value = int(e1.value) * int(e2.value)
                                s.type = 1
                                return s
                            elif(e1.type == 2 and e2.type == 2):
                                s.value = float(e1.value) * float(e2.value)
                                s.type = 2
                                return s
                            elif((e1.type == 1 and e2.type == 2) or (e1.type == 2 and e2.type == 1)):
                                s.value = float(e1.value) * float(e2.value)
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se pueden multiplicar los types ' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)
                        elif(expression.type == '/'):
                            # DIV
                            if(e1.type == 1 and e2.type == 1):
                                s.value = int(int(e1.value) / int(e2.value))
                                s.type = 1
                                return s
                            elif(e1.type == 2 and e2.type == 2):
                                s.value = float(e1.value) / float(e2.value)
                                s.type = 2
                                return s
                            elif((e1.type == 1 and e2.type == 2) or (e1.type == 2 and e2.type == 1)):
                                s.value = float(e1.value) /  float(e2.value)
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se pueden dividir los types ' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)
                        elif(expression.type == '%'):
                            # MOD
                            if(e1.type == 1 and e2.type == 1):
                                s.value = int(int(e1.value) % int(e2.value))
                                s.type = 1
                                return s
                            elif(e1.type == 2 and e2.type == 2):
                                s.value = float(e1.value) % float(e2.value)
                                s.type = 2
                                return s

                            elif((e1.type == 1 and e2.type == 2) or (e1.type == 2 and e2.type == 1)):
                                s.value = float(e1.value) % float(e2.value)
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar modulo con los types ' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)
                    except Exception as e:
                        return Error('Semantico', 'Error : ' + str(e), 0, 0)

            # EXPRESIONES LOGICAS
            elif isinstance(expression, Logical):
                e1 = executeExpression(self,expression.value1)
                e2 = executeExpression(self,expression.value2)
                if isinstance(e1, Error):
                    return e1
                elif isinstance(e2, Error):
                    return e2
                else:
                    try:
                        if(expression.type == 'AND'):
                            # AND
                            if(e1.type == 1 and e2.type == 1):
                                if((e1.value == 1 or e1.value == 0) and (e2.value == 1 or e2.value == 0)):
                                    s.value = int(e1.value) & int(e2.value)
                                    s.type = 1
                                    return s
                                else:
                                    return Error('Semantico', 'No se puede hacer un AND LOGICO entre los valuees ' + str(e1.value) + ' y ' + str(e2.value), 0, 0)
                            else:
                                return Error('Semantico', 'No se puede hacer un AND LOGICO entre los types ' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)

                        elif(expression.type == 'OR'):
                            # OR
                            if(e1.type == 1 and e2.type == 1):
                                if((e1.value == 1 or e1.value == 0) and (e2.value == 1 or e2.value == 0)):
                                    s.value = int(e1.value) | int(e2.value)
                                    s.type = 1
                                    return s
                                else:
                                    return Error('Semantico', 'No se puede hacer un OR LOGICO entre los valuees ' + str(e1.value) + ' y ' + str(e2.value), 0, 0)
                            else:
                                return Error('Semantico', 'No se puede hacer un OR LOGICO entre los types ' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)
                    except Exception as e:
                        return Error('Semantico', 'Error : ' + str(e), 0, 0)
            # EXPRESIONES RELACIONALES
            elif isinstance(expression, Relational):
                e1 = executeExpression(self,expression.value1)
                e2 = executeExpression(self,expression.value2)
                if isinstance(e1, Error):
                    return e1
                elif isinstance(e2, Error):
                    return e2
                else:
                    if(e1.type!=4):
                        try:
                            if(expression.type == '='):
                                # IGUAL IGUAL
                                if(e1.type == 1 and e2.type == 1):
                                    s.value = int(int(e1.value) == int(e2.value))
                                    s.type = 1
                                    return s
                                elif(e1.type == 2 and e2.type == 2):
                                    s.value = int(float(e1.value) == float(e2.value))
                                    s.type = 1
                                    return s

                                elif((e1.type == 1 and e2.type == 2) or (e1.type == 2 and e2.type == 1)):
                                    s.value = int(float(e1.value) == float(e2.value))
                                    s.type = 1
                                    return s

                                elif(e1.type == 3 and e2.type == 3):
                                    s.value = int(str(e1.value) == str(e2.value))
                                    s.type = 1
                                    return s
                                else:
                                    return Error('Semantico', 'No se pueden comparar los types ' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)

                            elif(expression.type == '!=' or expression.type == '<>'):
                                # DIFERENTE
                                if(e1.type == 1 and e2.type == 1):
                                    s.value = int(int(e1.value) != int(e2.value))
                                    s.type = 1
                                    return s
                                elif(e1.type == 2 and e2.type == 2):
                                    s.value = int(float(e1.value) != float(e2.value))
                                    s.type = 1
                                    return s

                                elif((e1.type == 1 and e2.type == 2) or (e1.type == 2 and e2.type == 1)):
                                    s.value = int(float(e1.value) != float(e2.value))
                                    s.type = 1
                                    return s

                                elif(e1.type == 3 and e2.type == 3):
                                    s.value = int(str(e1.value) != str(e2.value))
                                    s.type = 1
                                    return s
                                else:
                                    return Error('Semantico', 'No se pueden comparar los types ' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)
                            elif(expression.type == '>='):
                                # MAYOR IGUAL
                                if(e1.type == 1 and e2.type == 1):
                                    s.value = int(int(e1.value) >= int(e2.value))
                                    s.type = 1
                                    return s
                                elif(e1.type == 2 and e2.type == 2):
                                    s.value = int(float(e1.value) >= float(e2.value))
                                    s.type = 1
                                    return s

                                elif((e1.type == 1 and e2.type == 2) or (e1.type == 2 and e2.type == 1)):
                                    s.value = int(float(e1.value) >= float(e2.value))
                                    s.type = 1
                                    return s

                                elif(e1.type == 3 and e2.type == 3):
                                    s.value = int(str(e1.value) >= str(e2.value))
                                    s.type = 1
                                    return s
                                else:
                                    return Error('Semantico', 'No se pueden comparar los types ' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)
                            elif(expression.type == '<='):
                                # MENO IGUAL
                                if(e1.type == 1 and e2.type == 1):
                                    s.value = int(int(e1.value) <= int(e2.value))
                                    s.type = 1
                                    return s
                                elif(e1.type == 2 and e2.type == 2):
                                    s.value = int(float(e1.value) <= float(e2.value))
                                    s.type = 1
                                    return s

                                elif((e1.type == 1 and e2.type == 2) or (e1.type == 2 and e2.type == 1)):
                                    s.value = int(float(e1.value) <= float(e2.value))
                                    s.type = 1
                                    return s

                                elif(e1.type == 3 and e2.type == 3):
                                    s.value = int(str(e1.value) <= str(e2.value))
                                    s.type = 1
                                    return s
                                else:
                                    return Error('Semantico', 'No se pueden comparar los types ' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)

                            elif(expression.type == '>'):
                                # MAYOR
                                if(e1.type == 1 and e2.type == 1):
                                    s.value = int(int(e1.value) > int(e2.value))
                                    s.type = 1
                                    return s
                                elif(e1.type == 2 and e2.type == 2):
                                    s.value = int(float(e1.value) > float(e2.value))
                                    s.type = 1
                                    return s

                                elif((e1.type == 1 and e2.type == 2) or (e1.type == 2 and e2.type == 1)):
                                    s.value = int(float(e1.value) > float(e2.value))
                                    s.type = 1
                                    return s

                                elif(e1.type == 3 and e2.type == 3):
                                    s.value = int(str(e1.value) > str(e2.value))
                                    s.type = 1
                                    return s
                                else:
                                    return Error('Semantico', 'No se pueden comparar los types ' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)

                            elif(expression.type == '<'):
                                # MENOR
                                if(e1.type == 1 and e2.type == 1):
                                    s.value = int(int(e1.value) < int(e2.value))
                                    s.type = 1
                                    return s
                                elif(e1.type == 2 and e2.type == 2):
                                    s.value = int(float(e1.value) < float(e2.value))
                                    s.type = 1
                                    return s

                                elif((e1.type == 1 and e2.type == 2) or (e1.type == 2 and e2.type == 1)):
                                    s.value = int(float(e1.value) < float(e2.value))
                                    s.type = 1
                                    return s

                                elif(e1.type == 3 and e2.type == 3):
                                    s.value = int(str(e1.value) < str(e2.value))
                                    s.type = 1
                                    return s
                                else:
                                    return Error('Semantico', 'No se pueden comparar los types ' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)

                        except Exception as e:
                            return Error('Semantico', 'Error : ' + str(e), 0, 0)
                    else:
                        s.value=e2.value
                        s.op = expression.type
                        s.type=e2.type
                        s.id=e1.value
                        return s
            
            # EXPRESIONES UNARIAS
            elif isinstance(expression, Unary):
                e = executeExpression(self,expression.value)
                if isinstance(e, Error):
                    return e
                else:
                    try:
                        if(expression.type == '-'):
                            # NEGATIVO
                            if(e.type == 1):
                                s.value = -1 * int(e.value)
                                s.type = 1
                                return s
                            elif(e.type == 2):
                                s.value = -1 * float(e.value)
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar negativo del type ' + self.types[e.type], 0, 0)

                        elif(expression.type == 'NOT'):
                            # NEGACION
                            if(e.type == 1):
                                if (e.value == 0 or e.value == 1):
                                    s.value = int(abs(1-e.value))
                                    s.type = 1
                                    return s
                                else:
                                    return Error('Semantico', 'Solo se pueden negar valuees enteros 0 o 1', 0, 0)
                            else:
                                return Error('Semantico', 'No se pueden hacer una NEGACION del type ' + self.types[e.type], 0, 0)

                        elif(expression.type == '+'):
                            # NEGATIVO
                            if(e.type == 1):
                                s.value = int(e.value)
                                s.type = 1
                                return s
                            elif(e.type == 2):
                                s.value = float(e.value)
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar positivo del type ' + self.types[e.type], 0, 0)

                    except Exception as e:
                        return Error('Semantico', 'Error : ' + str(e), 0, 0)
            # FUNCIONES MATEMATICAS
            elif isinstance(expression, MathFunction):
                e = 0
                if(expression.function != 'PI' or expression.function != 'RANDOM' or expression.function != 'NOW' or expression.function != 'CURRENT_DATE' or expression.function != 'CURRENT_TIME'): e = executeExpression(self,expression.expression)
                if isinstance(e, Error):
                    return e
                else:
                    try:
                        if(expression.function == 'ABS'):
                            # ABSOLUTO
                            if(e.type == 1):
                                s.value = abs(int(e.value))
                                s.type = 1
                                return s
                            elif(e.type == 2):
                                s.value = abs(float(e.value))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar el absoluto del type ' + self.types[e.type], 0, 0)
                        elif(expression.function == 'CBRT'):
                            # RAIZ CUBICA
                            if(e.type == 1):
                                s.value = float(e.value**(1/3))
                                s.type = 2
                                return s
                            elif(e.type == 2):
                                s.value = float(e.value**(1/3))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar la raiz cubica del type ' + self.types[e.type], 0, 0)
                        elif(expression.function == 'CEIL'):
                            # REDONDEAR 
                            if(e.type == 1 or e.type == 2):
                                s.value = int(math.ceil(e.value))
                                s.type = 1
                                return s
                            else:
                                return Error('Semantico', 'No se puede redondear del type ' + self.types[e.type], 0, 0)
                        elif(expression.function == 'CEILING'):
                            # REDONDEAR
                            if(e.type == 1 or e.type == 2):
                                s.value = int(math.ceil(e.value))
                                s.type = 1
                                return s
                            else:
                                return Error('Semantico', 'No se puede redondear del type ' + self.types[e.type], 0, 0)
                        elif(expression.function == 'DEGREES'):
                            # DE RADIANES A GRADOS
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.degrees(e.value))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede convertir a grados del type ' + self.types[e.type], 0, 0)
                        elif(expression.function == 'EXP'):
                            # EXPONENCIACION
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.exp(e.value))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar la exponenciacion del type ' + self.types[e.type], 0, 0)
                        elif(expression.function == 'FACTORIAL'):
                            # FACTORIAL
                            if(e.type == 1):
                                s.value = int(math.factorial(e.value))
                                s.type = 1
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar el factorial del type ' + self.types[e.type], 0, 0)
                        elif(expression.function == 'FLOOR'):
                            # REDONDEAR
                            if(e.type == 1 or e.type == 2):
                                s.value =int(math.floor(e.value))
                                s.type = 1
                                return s
                            else:
                                return Error('Semantico', 'No se puede redondear del type ' + self.types[e.type], 0, 0)
                        elif(expression.function == 'LN'):
                            # LOGARITMO NATURAL
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.log(e.value))
                                if((s.value - int(s.value)) == 0):
                                    s.type = 1
                                else:
                                    s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar el logaritmo natural del type ' + self.types[e.type], 0, 0)
                        elif(expression.function == 'LOG'):
                            # LOGARITMO BASE 10
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.log10(e.value))
                                if((s.value - int(s.value)) == 0):
                                    s.type = 1
                                else:
                                    s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar el logaritmo base 10 del type ' + self.types[e.type], 0, 0)
                        elif(expression.function == 'PI'):
                            # VALOR DE PI
                            s.value = float(math.pi)
                            if((s.value - int(s.value)) == 0):
                                s.type = 1
                            else:
                                s.type = 2
                            return s
                        elif(expression.function == 'RADIANS'):
                            # DE GRADOS A RADIANES
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.radians(e.value))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede convertir a radianes del type ' + self.types[e.type], 0, 0)
                        elif(expression.function == 'SIGN'):
                            # DEVOLVER EL SIGNO
                            value = float(e.value)
                            if(e.type == 1 or e.type == 2):
                                if(value < 0):
                                    s.value = -1
                                else:
                                    s.value = 1
                                s.type = 1
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar el signo del type ' + self.types[e.type], 0, 0)
                        elif(expression.function == 'SQRT'):
                            # RAIZ CUADRADA
                            if(e.type == 1):
                                s.value = int(e.value**(1/2))
                                s.type = 1
                                return s
                            elif(e.type == 2):
                                s.value = float(e.value**(1/2))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar la raiz cuadrada del type ' + self.types[e.type], 0, 0)
                        elif(expression.function == 'RANDOM'):
                            # DEVOLVER NUMERO ENTRE 0 Y 1
                            s.value = float(random.uniform(0,1))
                            s.type = 2
                            return s
                        elif(expression.function == 'NOW'):
                            now = datetime.now()
                            Date_and_Time = str(now.date()) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
                            s.value = str(Date_and_Time)
                            s.type = 3
                            return s
                        elif(expression.function == 'CURRENT_DATE'):
                            now = datetime.now()
                            Date_ = str(now.date())
                            s.value = str(Date_)
                            s.type = 3
                            return s
                        elif(expression.function == 'CURRENT_TIME'):
                            now = datetime.now()
                            Time_ = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
                            s.value = str(Time_)
                            s.type = 3
                            return s
                        elif(expression.function == 'MD5'):
                            s.value = hashlib.md5(e.value.encode('utf-8')).hexdigest()
                            s.type = 3
                            return s
                    except Exception as e:
                        return Error('Semantico', 'Error : ' + str(e), 0, 0)
                    
            # FUNCIONES TRIGONOMETRICAS
            elif isinstance(expression, TrigonometricFunction):
                e = executeExpression(self,expression.expression)
                if isinstance(e, Error):
                    return e
                else:
                    try:
                        if(expression.function == 'ACOS'):
                            # COSENO INVERSO
                            if(e.type == 1 or e.type == 2):
                                if(e.value>= -1 and e.value<=1):
                                    s.value = float(math.acos(e.value))
                                    s.type = 2
                                    return s
                                else:
                                    return Error('Semantico', 'Error en el dominio de coseno inverso ', 0, 0)  
                            else:
                                return Error('Semantico', 'No se puede sacar el coseno inverso del type ' + self.types[e.type], 0, 0)
                        elif(expression.function == 'ACOSD'):
                            # COSENO INVERSO MEDIDO EN GRADOS, SALIDA SE CONVIERTE A GRADOS
                            if(e.type == 1 or e.type == 2):
                                if(e.value>= -1 and e.value<=1):
                                    s.value = float(math.degrees(math.acos(e.value)))
                                    s.type = 2
                                    return s
                                else:
                                    return Error('Semantico', 'Error en el dominio de coseno inverso medido en grados ', 0, 0)  
                            else:
                                return Error('Semantico', 'No se puede sacar el coseno inverso medido en grados del type ' + self.types[e.type], 0, 0) 
                        elif(expression.function == 'ASIN'):
                            # SENO INVERSO
                            if(e.type == 1 or e.type == 2):
                                if(e.value>= -1 and e.value<=1):
                                    s.value = float(math.asin(e.value))
                                    s.type = 2
                                    return s
                                else:
                                    return Error('Semantico', 'Error en el dominio de seno inverso', 0, 0)  
                            else:
                                return Error('Semantico', 'No se puede sacar el seno inverso del type ' + self.types[e.type], 0, 0) 
                        elif(expression.function == 'ASIND'):
                            # SENO INVERSO MEDIDO EN GRADOS, SALIDA SE CONVIERTE A GRADOS
                            if(e.type == 1 or e.type == 2):
                                if(e.value>= -1 and e.value<=1):
                                    s.value = float(math.degrees(math.asin(e.value)))
                                    s.type = 2
                                    return s
                                else:
                                    return Error('Semantico', 'Error en el dominio de seno inverso medido en grados', 0, 0)  
                            else:
                                return Error('Semantico', 'No se puede sacar el seno inverso medido en grados del type ' + self.types[e.type], 0, 0)   
                        elif(expression.function == 'ATAN'):
                            # TANGENTE INVERSO
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.atan(e.value))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar la tangente inversa del type ' + self.types[e.type], 0, 0) 
                        elif(expression.function == 'ATAND'):
                            # TANGENTE INVERSO MEDIDO EN GRADOS, SALIDA SE CONVIERTE A GRADOS
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.degrees(math.atan(e.value)))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar la tangente inversa medido en grados del type ' + self.types[e.type], 0, 0)   
                        elif(expression.function == 'COS'):
                            # COSENO
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.cos(e.value))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar el coseno del type ' + self.types[e.type], 0, 0) 
                        elif(expression.function == 'COSD'):
                            # COSENO MEDIDO EN GRADOS, ENTRADA EN GRADOS
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.cos(math.radians(e.value)))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar el coseno en grados del type ' + self.types[e.type], 0, 0)   
                        elif(expression.function == 'COT'):
                            # COTANGENTE
                            if(e.type == 1 or e.type == 2):
                                if((e.value % math.pi) != 0):
                                    s.value = float(math.cos(e.value)/math.sin(e.value))
                                    s.type = 2
                                    return s
                                else:
                                    return Error('Semantico', 'Error en el dominio de cotangente', 0, 0)  
                            else:
                                return Error('Semantico', 'No se puede sacar cotangente del type ' + self.types[e.type], 0, 0) 
                        elif(expression.function == 'COTD'):
                            # COTANGENTE MEDIDO EN GRADOS, ENTRADA EN GRADOS
                            if(e.type == 1 or e.type == 2):
                                if((e.value % math.pi) != 0):
                                    s.value =float(math.cos(math.radians(e.value))/math.sin(math.radians(e.value)))
                                    s.type = 2
                                    return s
                                else:
                                    return Error('Semantico', 'Error en el dominio de cotangente medido en grados', 0, 0)  
                            else:
                                return Error('Semantico', 'No se puede sacar cotangente en grados del type ' + self.types[e.type], 0, 0)   
                        elif(expression.function == 'SIN'):
                            # SENO
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.sin(e.value))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar seno del type ' + self.types[e.type], 0, 0) 
                        elif(expression.function == 'SIND'):
                            # SENO MEDIDO EN GRADOS, ENTRADA EN GRADOS
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.sin(math.radians(e.value)))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar seno en grados del type ' + self.types[e.type], 0, 0)   
                        elif(expression.function == 'TAN'):
                            # TANGENTE
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.tan(e.value))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar la tangente inversa del type ' + self.types[e.type], 0, 0) 
                        elif(expression.function == 'TAND'):
                            # TANGENTE MEDIDO EN GRADOS, ENTRADA EN GRADOS
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.tan(math.radians(e.value)))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar la tangente inversa en grados del type ' + self.types[e.type], 0, 0)   
                        elif(expression.function == 'SINH'):
                            # SENO HIPERBOLICO
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.sinh(e.value))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar el seno hiperbolico del type ' + self.types[e.type], 0, 0) 
                        elif(expression.function == 'COSH'):
                            # COSENO HIPERBOLICO
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.cosh(e.value))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar el coseno hiperbolico del type ' + self.types[e.type], 0, 0) 
                        elif(expression.function == 'TANH'):
                            # TANGENTE HIPERBOLICO
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.tanh(e.value))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar la tangente hiperbolico del type ' + self.types[e.type], 0, 0) 
                        elif(expression.function == 'ASINH'):
                            # SENO INVERSO HIPERBOLICO
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.asinh(e.value))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar el seno inverso hiperbolico del type ' + self.types[e.type], 0, 0) 
                        elif(expression.function == 'ACOSH'):
                            # COSENO INVERSO HIPERBOLICO
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.acosh(e.value))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar el coseno inverso hiperbolico del type ' + self.types[e.type], 0, 0) 
                        elif(expression.function == 'ATANH'):
                            # TANGENTE INVERSO HIPERBOLICO
                            if(e.type == 1 or e.type == 2):
                                s.value = float(math.atanh(e.value))
                                s.type = 2
                                return s
                            else:
                                return Error('Semantico', 'No se puede sacar la tangente inversa hiperbolico del type ' + self.types[e.type], 0, 0) 
                    except Exception as e:
                        return Error('Semantico', 'Error : ' + str(e), 0, 0)

            # FUNCIONES MATEMATICAS Y TRIGONOMETRICAS CON UNA LISTA DE EXPRESIONES
            elif isinstance(expression, ArgumentListFunction):
                if(len(expression.expressions) == 1):
                    e1 = executeExpression(self,expression.expressions[0])
                    if isinstance(e1, Error):
                        return e1
                    else:
                        try:
                            if(expression.function == 'ROUND'):
                                # REDONDEAR
                                if(e1.type == 1 or e1.type == 2):
                                    s.value = round(e1.value)
                                    s.type = 1
                                    return s
                                else:
                                    return Error('Semantico', 'Error en los argumentos para redondear un numero de los types' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)
                            elif(expression.function == 'TRUNC'):
                                # REDONDEAR
                                if(e1.type == 1 or e1.type == 2):
                                    s.value = math.trunc(e1.value)
                                    s.type = 1
                                    return s
                                else:
                                    return Error('Semantico', 'Error en los argumentos para redondear un numero de los types' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)
                        except Exception as e:
                            return Error('Semantico', 'Error : ' + str(e), 0, 0)
                elif(len(expression.expressions) != 2):
                    return Error('Semantico', 'No se puede sacar la funcion porque la cantidad de argumentos es incorrecta', 0, 0)
                else:
                    e1 = executeExpression(self,expression.expressions[0])
                    e2 = executeExpression(self,expression.expressions[1])
                    if isinstance(e1, Error):
                        return e1
                    elif isinstance(e2, Error):
                        return e2
                    else:
                        try:
                            if(expression.function == 'DIV'):
                                # DIVISION
                                if((e1.type == 1 or e1.type == 2) and (e2.type == 1 or e2.type == 2)):
                                    s.value = float(e1.value) / float(e2.value)
                                    s.type = 2
                                    return s
                                else:
                                    return Error('Semantico', 'No se pueden dividir los types ' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)
                            elif(expression.function == 'GCD'):
                                # MAXIMO COMUN DIVISOR
                                if(e1.type == 1 and e2.type == 1):
                                    s.value = int(math.gcd((e1.value),(e2.value)))
                                    s.type = 1
                                    return s
                                else:
                                    return Error('Semantico', 'No se puede sacar el maximo comun divisor de los types ' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)
                            elif(expression.function == 'MOD'):
                                if((e1.type == 1 or e1.type == 2) and (e2.type == 1 or e2.type == 2)):
                                    s.value = float(math.fmod(e1.value,e2.value))
                                    s.type = 2
                                    return s
                                else:
                                    return Error('Semantico', 'No se puede sacar el modulo de la division de los types ' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)
                            elif(expression.function == 'POWER'):
                                # ELEVAR UN NUMERO 
                                if((e1.type == 1 or e1.type == 2) and (e2.type == 1 or e2.type == 2)):
                                    s.value = float(math.pow(e1.value,e2.value))
                                    s.type = 2
                                    return s
                                else:
                                    return Error('Semantico', 'Error en los argumentos para elevar un numero de los types' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)
                            elif(expression.function == 'ROUND'):
                                # REDONDEAR
                                if((e1.type == 1 or e1.type == 2) and (e2.type == 1)):
                                    s.value = float(round(e1.value,e2.value))
                                    s.type = 2
                                    return s
                                else:
                                    return Error('Semantico', 'Error en los argumentos para redondear un numero con argumentos de los types' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)
                            elif(expression.function == 'TRUNC'):
                                # TRUNCAR NUMERO
                                if((e1.type == 1 or e1.type == 2) and (e2.type == 1)):
                                    stepper = 10.0 ** e2.value
                                    s.value = float(math.trunc(stepper*e1.value)/stepper)
                                    s.type = 2
                                    return s
                                else:
                                    return Error('Semantico', 'Error en los argumentos para truncar un numero con argumentos de los types' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)
                            elif(expression.function == 'ATAN2'):
                                # ARCOTANGENTE
                                if((e1.type == 1 or e1.type == 2) and (e2.type == 1 or e2.type == 2)):
                                    s.value = float(math.atan2(e1.value,e2.value))
                                    s.type = 2
                                    return s
                                else:
                                    return Error('Semantico', 'Error en los argumentos sacar el arcotangente un numero con argumentos de los types' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)
                            elif(expression.function == 'ATAN2D'):
                                # ARCOTANGENTE, ENTRADA EN GRADOS
                                if((e1.type == 1 or e1.type == 2) and (e2.type == 1 or e2.type == 2)):
                                    s.value = float(math.degrees(math.atan2(e1.value,e2.value)))
                                    s.type = 2
                                    return s
                                else:
                                    return Error('Semantico', 'Error en los argumentos sacar el arcotangente medido en grados con argumentos de los types' + self.types[e1.type] + ' y ' + self.types[e2.type], 0, 0)
                        except Exception as e:
                            return Error('Semantico', 'Error : ' + str(e), 0, 0)
                        #Falta funcion matematica width_bucket


            # EXTRACT
            elif isinstance(expression, ExtractFunction):
                e = executeExpression(self,expression.expression)
                if isinstance(e, Error):
                    return e
                else:
                    try:
                        if(expression.function == 'HOUR'):
                            s.value = e.value[11:13]
                            s.type = 3
                            return s
                        elif(expression.function == 'MINUTE'):
                            s.value = e.value[14:16]
                            s.type = 3
                            return s
                        if(expression.function == 'SECOND'):
                            s.value = e.value[17:19]
                            s.type = 3
                            return s
                        if(expression.function == 'YEAR'):
                            s.value = e.value[0:4]
                            s.type = 3
                            return s
                        if(expression.function == 'MONTH'):
                            s.value = e.value[5:7]
                            s.type = 3
                            return s
                        if(expression.function == 'DAY'):
                            s.value = e.value[8:10]
                            s.type = 3
                            return s
                    except Exception as e:
                        return Error('Semantico', 'Error : ' + str(e), 0, 0) 

            # DATE PARTE
            elif isinstance(expression, DatePartFunction):
                e = executeExpression(self,expression.expression)
                if isinstance(e, Error):
                    return e
                else:
                    try:
                        if(expression.function.type == 3):
                            typeTime = expression.function.value
                            cadena = str(e.value).strip().split(' ')

                            value = 0
                            for i in cadena:
                                if (typeTime == i) or (str(typeTime + 'S') == i): 
                                    s.value = value
                                    s.type = 1
                                    return s
                                if i.isnumeric():
                                    value = i
                        else:
                            return Error('Semantico', 'Error : Error en los argumentos para sacar date_part', 0, 0) 
                    except Exception as e:
                        return Error('Semantico', 'Error : ' + str(e), 0, 0)