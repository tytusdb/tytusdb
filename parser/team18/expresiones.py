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


class OPERACION_MATH(Enum):
    ABS = 1
    CBRT = 2
    CEIL = 3
    CEILING = 4
    DEGREES = 5
    DIV = 6
    EXP = 7
    FACTORIAL = 8
    FLOOR = 9
    GCD = 10
    LN = 11
    LOG = 12
    MOD = 13
    PI = 14
    POWER = 15
    RADIANS = 16
    ROUND = 17
    MIN_SCALE =18
    SCALE = 19
    SIGN = 20
    SQRT = 21
    TRIM = 22
    TRUNC =  23
    RANDOM =  24
    SETSEED = 25
    #trigonometric functions
    ACOS = 26
    ACOSD = 27
    ASIN = 28
    ASIND = 29
    ATAN = 30
    ATAND = 31
    ATAN2 = 32
    ATAN2D = 33
    COS = 34
    COSD = 35
    COT = 36
    COTD = 37
    SIN = 38
    SIND = 39
    TAN = 40
    TAND = 41
    SINH = 42
    COSH = 43
    TANH = 44
    ASINH = 45
    ACOSH = 46
    ATANH = 47

    WIDTH_BUCKET = 48


class OPERACION_BINARY_STRING(Enum):
    LENGTH = 1
    SUBSTRING = 2
    TTRIM = 3
    MD5 = 4
    SHA256 = 5
    DECODE = 6
    ENCODE = 7
    GET_BYTE = 8
    SET_BYTE = 9
    SUBSTR =  10
    CONVERT = 11

class OPERACION_PATRONES(Enum):
    BETWEEN = 1
    NOT_BETWEEN = 2
    IN = 3
    NOT_IN = 4
    LIKE = 5
    NOT_LIKE = 6
    ILIKE = 7
    NOT_ILIKE = 8
    SIMILAR = 9
    NOT_SIMILAR = 10

class FUNCIONES_SELECT(Enum):
    COUNT = 1
    SUM = 2
    AVG = 3
    MIN = 4
    MAX = 5
    
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

class Operando_ID_Columna(Expresion):
    '''
        Esta clase representa un id con acceso a columnas
    '''
    def __init__(self, nombre, columna):
        self.nombre=nombre
        self.columna=columna

class Operacion_NOW(Expresion):
    '''
        Esta clase representa la operacion NOW
    '''

class Operacion_CURRENT(Expresion):
    '''
        Esta clase representa la operacion CURRENT_TIME o CURRENT_DATE
    '''
    def __init__(self, tipo):
        self.tipo=tipo

class Operacion_TIMESTAMP(Expresion):
    '''
        Esta clase representa la operaciion TIMESTAMP
    '''
    def __init__(self, valor):
        self.valor=valor

class Operando_EXTRACT(Expresion):
    '''
        Esta clase representa la operacion EXTRACT
    '''
    def __init__(self, medida, valores):
        self.medida=medida
        self.valores=valores

class Operacion_DATE_PART(Expresion):
    '''
        Esta clase representa la operacion DATE_PART
    '''
    def __init__(self, val1, val2):
        self.val1=val1
        self.val2=val2

class Operacion_Great_Least(Expresion):
    '''
        Esta clase representa la operacion greatnes y leastnes
    '''
    def __init__(self, tipo, expresion):
        self.tipo=tipo
        self.expresion=expresion


class Operacion_Math_Unaria(Expresion):
    '''
        Esta clase representa la expresion matematica con un solo argumento
        Esta clase recibe el nombre de la funcion y una sola expresion
    '''
    def __init__(self,op,operador):
        self.op = op
        self.operador  = operador

class Operacion_Math_Binaria(Expresion):
    '''
        Esta clase representa la expresion matematica con un dos argumentos
        Esta clase recibe el operador y 2 expresiones
    '''
    def __init__(self,op1,op2,operador):
        self.op1 = op1
        self.op2 = op2
        self.operador  = operador

class Operacion_Definida(Expresion):
    '''
        Esta clase representa la constante pi y random 
    '''
    def __init__(self,operador):
        self.operador = operador

class Operacion_Strings(Expresion):
    '''
        Esta clase representa las operaciones unarias que se pueden realizar con strings
    '''
    def __init__(self,cadena, operador):
        self.cadena = cadena
        self.operador =  operador

class Operacion_String_Binaria(Expresion):
    '''
        Esta clase representa las operaciones compuestas que se pueden realizar con string
    '''
    def __init__(self,op1,op2,operador):
        self.op1 = op1
        self.op2 = op2
        self.operador = operador

class Operacion_String_Compuesta(Expresion):
    '''
        Esta clase representa las operaciones compuestas que se pueden realizar con string
    '''
    def __init__(self,op1,op2,op3,operador):
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.operador = operador

class Operacion_Patron(Expresion):
    '''
        Esta clase representa las operaciones de patron
    '''
    def __init__(self,op1,op2,operador):
        self.op1=op1
        self.op2=op2
        self.operador=operador

class Funcion_select(Expresion):
    '''
        Esta clase representa una funcion select count, sum, avg, min, max
    '''
    def __init__(self,op,operador):
        self.op=op
        self.operador=operador

class Operacion__Cubos(Expresion):
    '''
        Esta clase representa la funcion de width bucket la cual recibe 4 parametros
        y un operador
    '''
    def __init__(self,op1,op2,op3,op4,operador):
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.op4 = op4
        self.operador = operador