from .AST.expression import *
from .AST.symbol import *
from .AST.error import * 
def executeExpression(self, expression):
            s = Symbol('', 1, 1, 0, 0)
            if isinstance(expression, Value):
                return self.executeValue(expression)
            # EXPRESIONES ARITMETICAS
            if isinstance(expression, Arithmetic):
                e1 = self.executeExpression(expression.value1)
                e2 = self.executeExpression(expression.value2)
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
                e1 = self.executeExpression(expression.value1)
                e2 = self.executeExpression(expression.value2)
                if isinstance(e1, Error):
                    return e1
                elif isinstance(e2, Error):
                    return e2
                else:
                    try:
                        if(expression.type == '&&'):
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

                        elif(expression.type == '||'):
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
                e1 = self.executeExpression(expression.value1)
                e2 = self.executeExpression(expression.value2)
                if isinstance(e1, Error):
                    return e1
                elif isinstance(e2, Error):
                    return e2
                else:
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
            
            # EXPRESIONES UNARIAS
            elif isinstance(expression, Unary):
                e = self.executeExpression(expression.value)
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
    