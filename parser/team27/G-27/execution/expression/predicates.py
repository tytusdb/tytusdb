from execution.abstract.expression import *
from execution.symbol.typ import *
from execution.expression.literal import *
from execution.expression.id import *
from TypeChecker.checker import *

class Predicates(Expression):
    # si es el oprando not mandar un None como operador right
    def __init__(self, operator1, operator2,operator3,tipoPredicate, row, column):
        Expression.__init__(self, row, column)
        self.operator1 = operator1
        self.operator2 = operator2
        self.operator3 = operator3
        self.tipoPredicate= tipoPredicate

    def execute(self, environment):
        op2 = self.operator2
        op3 = self.operator3
        if op2 != None:
            op2 = op2.execute(environment)
        if op3 != None:
            op3 = op3.execute(environment)
        
        if self.tipoPredicate =='BETWEEN':
            op1 = self.operator3.execute(environment)
            if 'Error' in op1:
                return {'Error':'El id indicado no existe en la tabla ', 'Linea':self.row, 'Columna': self.column }
            #TODO verificar tipos de los 3 operandos
            if op1['typ']!= op2['typ'] or op2['typ'] != op3['typ']:
                return {'Error':'El tipo de dato de la columna es diferente al tipo de dato a comparar ', 'Linea':self.row, 'Columna': self.column }
            if op2['value'] >= op3['value']:
                return {'Error':'El valor 1 es mayor o igual que el valor 2', 'Linea':self.row, 'Columna': self.column }
            if op1['value'] > op2['value'] and op1['value'] < op3['value']:
                return {'value':True,'typ':Type.BOOLEAN}
            else:
                return {'value':False,'typ':Type.BOOLEAN}

        elif self.tipoPredicate =='NOT BETWEEN':
            op1 = self.operator3.execute(environment)
            if 'Error' in op1:
                return {'Error':'El id indicado no existe en la tabla ', 'Linea':self.row, 'Columna': self.column }
            #TODO verificar tipos de los 3 operandos
            if op1['typ']!= op2['typ'] or op2['typ'] != op3['typ']:
                return {'Error':'El tipo de dato de la columna es diferente al tipo de dato a comparar ', 'Linea':self.row, 'Columna': self.column }
            if op2['value'] > op3['value']:
                return {'Error':'El valor 1 es mayor o igual que el valor 2', 'Linea':self.row, 'Columna': self.column }
            if op1['value'] < op2['value'] or op1['value'] > op3['value']:
                return {'value':True,'typ':Type.BOOLEAN}
            else:
                return {'value':False,'typ':Type.BOOLEAN}
        
        elif self.tipoPredicate =='BETWEEN SYMMETRIC':
            op1 = self.operator3.execute(environment)
            if 'Error' in op1:
                return {'Error':'El id indicado no existe en la tabla ', 'Linea':self.row, 'Columna': self.column }
            #TODO verificar tipos de los 3 operandos
            if op1['typ']!= op2['typ'] or op2['typ'] != op3['typ']:
                return {'Error':'El tipo de dato de la columna es diferente al tipo de dato a comparar ', 'Linea':self.row, 'Columna': self.column }
            if op2['value'] >= op3['value']:
                return {'Error':'El valor 1 es igual que el valor 2 por lo que no hay rango', 'Linea':self.row, 'Columna': self.column }

            if op2['value'] < op3['value']:
                if op1['value'] < op2['value'] or op1['value'] > op3['value']:
                    return {'value':True,'typ':Type.BOOLEAN}
                else:
                    return {'value':False,'typ':Type.BOOLEAN}
            else:
                if op1['value'] < op3['value'] or op1['value'] > op2['value']:
                    return {'value':True,'typ':Type.BOOLEAN}
                else:
                    return {'value':False,'typ':Type.BOOLEAN}
  
        elif self.tipoPredicate =='NOT BETWEEN SYMMETRIC':
            op1 = self.operator3.execute(environment)
            if 'Error' in op1:
                return {'Error':'El id indicado no existe en la tabla ', 'Linea':self.row, 'Columna': self.column }
            #TODO verificar tipos de los 3 operandos
            if op1['typ']!= op2['typ'] or op2['typ'] != op3['typ']:
                return {'Error':'El tipo de dato de la columna es diferente al tipo de dato a comparar ', 'Linea':self.row, 'Columna': self.column }
            if op2['value'] >= op3['value']:
                return {'Error':'El valor 1 es igual que el valor 2 por lo que no hay rango', 'Linea':self.row, 'Columna': self.column }

            if op2['value'] < op3['value']:
                if op1['value'] < op2['value'] or op1['value'] > op3['value']:
                    return {'value':True,'typ':Type.BOOLEAN}
                else:
                    return {'value':False,'typ':Type.BOOLEAN}
            else:
                if op1['value'] < op3['value'] or op1['value'] > op2['value']:
                    return {'value':True,'typ':Type.BOOLEAN}
                else:
                    return {'value':False,'typ':Type.BOOLEAN}
        
        elif self.tipoPredicate =='DISTINCT':
            op1 = self.operator3.execute(environment)
            if 'Error' in op1:
                return {'Error':'El id indicado no existe en la tabla ', 'Linea':self.row, 'Columna': self.column }            
            if op1['typ']!= op2['typ']:
                return {'Error':'El tipo de dato de la columna es diferente al tipo de dato a comparar ', 'Linea':self.row, 'Columna': self.column }        
            if op1['value'] != op2['value']:
                return {'value':True,'typ':Type.BOOLEAN}
            else:
                return {'value':False,'typ':Type.BOOLEAN}
        elif self.tipoPredicate =='NOT DISTINCT':
            op1 = self.operator3.execute(environment)
            if 'Error' in op1:
                return {'Error':'El id indicado no existe en la tabla ', 'Linea':self.row, 'Columna': self.column }            
            if op1['typ']!= op2['typ']:
                return {'Error':'El tipo de dato de la columna es diferente al tipo de dato a comparar ', 'Linea':self.row, 'Columna': self.column }        
            if op1['value'] == op2['value']:
                return {'value':True,'typ':Type.BOOLEAN}
            else:
                return {'value':False,'typ':Type.BOOLEAN}

        elif self.tipoPredicate =='IS NULL':
            op1 = self.operator3.execute(environment)
            if 'Error' in op1:
                return {'Error':'El id indicado no existe en la tabla ', 'Linea':self.row, 'Columna': self.column }            
            if op1['typ'] == Type.NULL:
                return {'value':True,'typ':Type.BOOLEAN}
            elif op1['value'] == 'null':
                return {'value':True,'typ':Type.BOOLEAN}
            else:
                return {'value':False,'typ':Type.BOOLEAN}

        elif self.tipoPredicate =='IS NOT NULL':
            op1 = self.operator3.execute(environment)
            if 'Error' in op1:
                return {'Error':'El id indicado no existe en la tabla ', 'Linea':self.row, 'Columna': self.column }            
            if op1['typ'] == Type.NULL:
                return {'value':False,'typ':Type.BOOLEAN}
            elif op1['value'] == 'null':
                return {'value':False,'typ':Type.BOOLEAN}
            else:
                return {'value':True,'typ':Type.BOOLEAN}

        elif self.tipoPredicate =='ISNULL':
            op1 = self.operator3.execute(environment)
            if 'Error' in op1:
                return {'Error':'El id indicado no existe en la tabla ', 'Linea':self.row, 'Columna': self.column }            
            if op1['typ'] == Type.NULL:
                return {'value':True,'typ':Type.BOOLEAN}
            elif op1['value'] == 'null':
                return {'value':True,'typ':Type.BOOLEAN}
            else:
                return {'value':False,'typ':Type.BOOLEAN}

        elif self.tipoPredicate =='NOTNULL':
            op1 = self.operator3.execute(environment)
            if 'Error' in op1:
                return {'Error':'El id indicado no existe en la tabla ', 'Linea':self.row, 'Columna': self.column }            
            if op1['typ'] == Type.NULL:
                return {'value':False,'typ':Type.BOOLEAN}
            elif op1['value'] == 'null':
                return {'value':False,'typ':Type.BOOLEAN}
            else:
                return {'value':True,'typ':Type.BOOLEAN}

        elif self.tipoPredicate =='IS TRUE':
            op1 = self.operator3.execute(environment)
            if 'Error' in op1:
                return {'Error':'El id indicado no existe en la tabla ', 'Linea':self.row, 'Columna': self.column }            
            if op1['typ'] == Type.NULL:
                return {'value':False,'typ':Type.BOOLEAN}
            elif op1['value'] == 'null':
                return {'value':False,'typ':Type.BOOLEAN}
            elif op1['typ'] == Type.BOOLEAN:
                if op1['value'] == True:
                    return {'value':True,'typ':Type.BOOLEAN}
                else:
                    return {'value':False,'typ':Type.BOOLEAN}
            else:
                return {'value':False,'typ':Type.BOOLEAN}
        
        elif self.tipoPredicate =='IS NOT TRUE':
            op1 = self.operator3.execute(environment)
            if 'Error' in op1:
                return {'Error':'El id indicado no existe en la tabla ', 'Linea':self.row, 'Columna': self.column }            
            if op1['typ'] == Type.NULL:
                return {'value':True,'typ':Type.BOOLEAN}
            elif op1['value'] == 'null':
                return {'value':True,'typ':Type.BOOLEAN}
            elif op1['typ'] == Type.BOOLEAN:
                if op1['value'] == True:
                    return {'value':False,'typ':Type.BOOLEAN}
                else:
                    return {'value':True,'typ':Type.BOOLEAN}
            else:
                return {'value':True,'typ':Type.BOOLEAN}
        
        elif self.tipoPredicate =='IS FALSE':
            op1 = self.operator3.execute(environment)
            if 'Error' in op1:
                return {'Error':'El id indicado no existe en la tabla ', 'Linea':self.row, 'Columna': self.column }            
            if op1['typ'] == Type.NULL:
                return {'value':True,'typ':Type.BOOLEAN}
            elif op1['value'] == 'null':
                return {'value':True,'typ':Type.BOOLEAN}
            elif op1['typ'] == Type.BOOLEAN:
                if op1['value'] == True:
                    return {'value':False,'typ':Type.BOOLEAN}
                else:
                    return {'value':True,'typ':Type.BOOLEAN}
            else:
                return {'value':False,'typ':Type.BOOLEAN}
        
        elif self.tipoPredicate =='IS NOT FALSE':
            op1 = self.operator3.execute(environment)
            if 'Error' in op1:
                return {'Error':'El id indicado no existe en la tabla ', 'Linea':self.row, 'Columna': self.column }            
            if op1['typ'] == Type.NULL:
                return {'value':False,'typ':Type.BOOLEAN}
            elif op1['value'] == 'null':
                return {'value':False,'typ':Type.BOOLEAN}
            elif op1['typ'] == Type.BOOLEAN:
                if op1['value'] == True:
                    return {'value':True,'typ':Type.BOOLEAN}
                else:
                    return {'value':False,'typ':Type.BOOLEAN}
            else:
                return {'value':True,'typ':Type.BOOLEAN}
        #unknow revisar
        elif self.tipoPredicate =='IS UNKNOWN':
            op1 = self.operator3.execute(environment)
            if 'Error' in op1:
                return {'Error':'El id indicado no existe en la tabla ', 'Linea':self.row, 'Columna': self.column }            
            if op1['typ'] == Type.NULL:
                return {'value':True,'typ':Type.BOOLEAN}
            elif op1['value'] == 'null':
                return {'value':True,'typ':Type.BOOLEAN}
            else:
                return {'value':False,'typ':Type.BOOLEAN}

        elif self.tipoPredicate =='IS NOT UNKNOWN':
            op1 = self.operator3.execute(environment)
            if 'Error' in op1:
                return {'Error':'El id indicado no existe en la tabla ', 'Linea':self.row, 'Columna': self.column }            
            if op1['typ'] == Type.NULL:
                return {'value':False,'typ':Type.BOOLEAN}
            elif op1['value'] == 'null':
                return {'value':False,'typ':Type.BOOLEAN}
            else:
                return {'value':True,'typ':Type.BOOLEAN}
        
            
     