from enum import Enum


class arit(Enum):
    MAS = 1
    RES = 2
    POR = 3
    DIV = 4
    PORC = 5
    BETWEENS= 6



class valoresCampo(Enum):
    notNUll = 1  
    NUll = 2
    PRIMARY = 3 
    FOREIGN = 4
    HASCHECK = 5
    IDENTITY = 6
    CONSTRAINT = 7
    UNKNOWN = 100

class logic(Enum):
    NOT = 1
    AND = 2
    OR = 3
    XOR = 4


class relac(Enum):
    II = 1
    NI = 2
    MENI = 3
    MAYI = 4
    MAYOR = 5
    MENOR = 6


class ESP(Enum):
    isTrue = 0
    isNotTrue = 1
    isFalse = 2 
    isNotFalse = 3
    isNotNull = 4
    isNull = 5

class DIST(Enum):
    isNotDistinct = 0
    isDistinct = 1


class tipod(Enum):
    INT = 1
    CHA = 2
    SMALLINT = 3
    BIGINT = 4
    DECIMAL = 5
    NUMERIC = 6
    REAL = 7
    DOUBLE = 8
    MONEY = 9
    VARYING = 10
    TEXT = 11
    DATE = 12
    BOOLEAN = 13
    CHARACTER = 14
    VARCHAR = 15




class Expresion:
    '''
        je je
    '''

class distinct(Expresion):
    def __init__(self, oper1, oper2 , operacion):
        self.op1 = oper1
        self.op2 = oper2
        self.operacion = operacion

class raiz(Expresion):
    def __init__(self, oper1):
        self.op1 = oper1

class potencia(Expresion):
    def __init__(self, oper,pot):
        self.op1 = oper
        self.pot = pot

class avg(Expresion):
    def __init__(self, oper):
        self.op1 = oper

class SUM(Expresion):
    def __init__(self, oper):
        self.op1 = oper

class pi(Expresion):
    def __init__(self, oper):
        self.op1 = oper

class MAX(Expresion):
    def __init__(self, oper):
        self.op1 = oper


class aritmetica(Expresion):
    def __init__(self, op1, op2, operacion):
        self.op1 = op1
        self.op2 = op2
        self.operacion = operacion

class aritmeticaNegativa(Expresion):
    def __init__(self, operacion):
        self.operacion = operacion
    
class aritmeticaESP(Expresion):
    def __init__(self, op1 , oper):
        self.op1 = op1
        self.operacion = oper


class logica(Expresion):
    def __init__(self, op1, op2, operacion):
        self.op1 = op1
        self.op2 = op2
        self.operacion = operacion


class relacional(Expresion):
    def __init__(self, op1, op2, operacion):
        self.op1 = op1
        self.op2 = op2
        self.operacion = operacion


class tipo(Expresion):
    def __init__(self, tipo):
        self.tipo = tipo


class casteo(Expresion):
    def __init__(self, tipo, valor, id):
        self.id = id
        self.tipo = tipo
        self.valor = valor

class numero(Expresion):
    def __init__(self, numero):
        self.numero = numero
class numeroM(Expresion):
    def __init__(self, numero):
        self.numero = numero

class cadena(Expresion):
    def __init__(self, cad):
        self.cad =cad

class cadenaCaracter(Expresion):
    def __init__(self, cadC):
        self.cadC = cadC

class numDecimal(Expresion):
    def __init__(self, numDec):
        self.numDec = numDec

class numDecimalM(Expresion):
    def __init__(self, numDec):
        self.numDec = numDec




class ids(Expresion):
    def __init__(self, ids):
        self.ids = ids

#Funciones EXTRAS 
class aritmetica2(Expresion):
    def __init__(self, operacion):
        self.operacion = operacion

class funcionextra(Expresion): 
    def __init__(self,funcion):
        self.funcion = funcion
class funcionextra2(Expresion): 
    def __init__(self,funcion):
        self.funcion = funcion
class funcionextra3(Expresion): 
    def __init__(self,funcion):
        self.funcion = funcion

class mathfunctions(Expresion): 
    def __init__(self,funcion,op1):
        self.funcion =funcion
        self.op1=op1

class mathfunctions2(Expresion): 
    def __init__(self,funcion,op1,op2):
        self.funcion =funcion
        self.op1=op1
        self.op2=op2
#width_bucket
class mathfunctions3(Expresion): 
    def __init__(self,op1,op2,op3,op4):
        self.op1=op1
        self.op2=op2
        self.op3=op3
        self.op4=op4

class randomclass(Expresion): 
    def __init__(self):
        print('random()')
    


class trigonometricas(Expresion): 
    def __init__(self,funcion,op1):
        self.funcion = funcion
        self.op1=op1

class binarystring(Expresion): 
    def __init__(self,funcion):
        self.funcion=funcion

class binarystring2(Expresion): 
    def __init__(self,funcion,operacion):
        self.funcion=funcion
        self.operacion=operacion

class binarystring3(Expresion): 
    def __init__(self,op1,op2,op3):
        self.op1=op1
        self.op2=op2
        self.op3=op3

class binarystring4(Expresion): 
    def __init__(self,funcion,op2,op3):
        self.op1=funcion
        self.op2=op2
        self.op3=op3

class binarystring5(Expresion): 
    def __init__(self,op1,op2,op3):
        self.op1=op1
        self.op2=op2
        self.op3=op3

class binarystring6(Expresion): 
    def __init__(self,op1,op2):
        self.op1=op1
        self.op2=op2
        
class binarystring7(Expresion): 
    def __init__(self,op1,op2):
        self.op1=op1
        self.op2=op2


