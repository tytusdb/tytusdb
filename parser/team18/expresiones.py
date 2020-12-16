from enum import Enum

class OPERACION_ARITMETICA(Enum) :
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    POTENCIA =  5
    MODULO = 6

class OPERACION_RELACIONAL(Enum) :
    IGUAL = 1
    DIFERENTE = 2
    MAYORIGUALQUE = 3
    MENORIGUALQUE = 4
    MAYOR_QUE = 5
    MENOR_QUE = 6

class OPERACION_LOGICA(Enum):
    AND = 1
    OR = 2

class OPERACION_ESPECIAL(Enum):
    SQRT2 = 1
    CBRT2 = 2
    AND2 = 3
    OR2 = 4
    NOT2 = 5
    XOR = 6
    DEPIZQ = 7
    DEPDER = 8
    
class Expresion:
    '''
        Esta clase representa una expresión numérica
    '''

class Operacion_Aritmetica(Expresion) :
    '''
        Esta clase representa una operacion aritmetica entre dos expresiones y un operando
    '''

    def __init__(self, op1, op2, operador) :
        self.op1 = op1
        self.op2 = op2
        self.operador = operador

class Operacion_Relacional(Expresion):
    '''
        Esta clase representa una operacion relacional 
    '''

    def __init__(self, op1, op2, operador):
        self.op1 = op1
        self.op2 = op2
        self.operador = operador

class Operacion_Logica_Binaria(Expresion):
    '''
        Esta clase representa una operacion logica binaria
    '''

    def __init__(self, op1, op2, operador):
        self.op1 = op1
        self.op2 = op2
        self.operador = operador

class Operacion_Logica_Unaria(Expresion):
    '''
        Esta clase representa una operacion logica unaria
    '''

    def __init__(self,op):
        self.op = op

class Operacion_Especial_Binaria(Expresion):
    '''
        Esta clase representa una operacion especial binaria
    '''

    def __init__(self, op1, op2, operador):
        self.op1 = op1
        self.op2 = op2
        self.operador = operador

class Operacion_Especial_Unaria(Expresion):
    '''
        Esta clase representa una operacion especial unaria
    '''

    def __init__(self, op, operador):
        self.op = op
        self.operador = operador

class Negacion_Unaria(Expresion):
    '''
        Esta clase representa una negacion unaria para un operador
    '''

    def __init__(self,op):
        self.op=op

class Operando_Numerico(Expresion):
    '''
        Esta clase representa un operando del tipo numerico el cual puede ser entero o decimal
    '''
    
    def __init__(self,valor=0):
        self.valor=valor

class Operando_ID(Expresion):
    '''
        Esta clase represnta un operando del tipo identificador
    '''

    def __init__(self,id=""):
        self.id=id

class Operando_Cadena(Expresion):
    '''
        Esta clase representa un operando de tipo cadena
    '''

    def __init__(self,valor=""):
        self.valor=valor

class Operando_Booleano(Expresion):
    '''
        Esta clase representa un operando de tipo booleano
    '''

    def __init__(self,valor=False):
        self.valor=valor