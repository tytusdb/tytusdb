from enum import Enum

class OPCIONESCREATE_TABLE(Enum):
    PRIMARIA = 1
    FORANEA = 2
    REFERENCES = 3
    NOT_NULL = 4
    NULL = 5
    PRIMARIA_SOLA = 6
    CONSTRAINT = 7
    UNIQUE = 8

class OPCIONES_UNIONES(Enum):
    UNION = 1
    INTERSECT = 2
    EXCEPTS = 3

class OPERACION_TIEMPO(Enum):
    YEAR = 1
    DAY = 2
    MOUNTH = 3
    HOUR = 4
    MINUTE = 5
    SECOND = 6

class OPCIONES_CONSTRAINT(Enum):
    CHECK = 1
    UNIQUE = 2
    FOREIGN = 3
    NULL = 4
    NOT_NULL = 5
    DEFAULT = 6
    PRIMARY = 7

class OPERACION_ARITMETICA(Enum):
    MAS = 1
    MENOS = 2
    ASTERISCO = 3
    DIVIDIDO = 4
    MODULO = 5
    MAYMAY = 6
    MENMEN = 7
    CEJILLA = 8
    HASTAG = 9
    S_OR = 9
    D_OR = 10
    AMPERSON = 11
    NOT_LIKE = 12
    BETWEEN = 13
    IN = 14
    NOT_IN = 15
    AVG = 16
    MAX = 17
    MIN = 18
    SIN_SOME_ANY = 19
    ALL = 20
    SOME = 21
    NOW = 22
    ANYS = 23
    ABS = 24
    LENGTH = 25
    CBRT = 26
    CEIL = 27
    CEILING = 28
    DEGREES = 29
    E_DIV = 30
    EXP = 31
    FACTORIAL = 32
    FLOOR = 33
    GCD = 34
    LN = 35
    LOG = 36
    MOD = 37
    PI = 38
    POWER = 39
    RADIANS = 40
    ROUND = 41
    SIGN = 42
    SQRT = 43
    WIDTH_BUCKET = 44
    TRUNC = 45
    RANDOM = 46
    ACOS = 47
    ASIND = 48
    ATAN = 49
    ATAND = 50
    ATAN2 = 51
    ATAN2D = 52
    COS = 53
    COT = 54
    COTD = 55
    SIN = 56
    SIND = 57
    TAN = 58
    TAND = 59
    SINH = 60
    COSH = 61
    TANH = 62
    ASINH = 63
    ATANH = 64
    COSD = 65
    ACOSH = 66
    ASIN = 67
    ACOSD = 68
    S_TRUNC = 69

class OPERACION_RELACIONAL(Enum):
    MAYQUE = 1
    MENQUE = 2
    MAYIGQUE = 3
    MENIGQUE = 4
    DOBLEIGUAL = 5
    NOIG   = 6
    DIFERENTE = 7
    IGUAL = 8
    NOT_LIKE = 9
    BETWEEN = 10
    N_IN = 11
    NOT_IN = 12

class OPERACION_LOGICA(Enum):
    AND = 1
    OR = 2
    NOT = 3
    TRUE = 4
    FALSE = 5
    THEN = 6
    
class TIPO_DE_DATOS(Enum):
    text_ = 1
    float_ = 2
    integer_ = 3
    smallint_ = 4
    money = 5
    bigint = 6
    real = 7
    double = 8
    interval = 9
    time = 10
    timestamp = 11
    date = 12
    varying = 13
    varchar = 14
    char = 15
    character = 16
    decimal = 17
    numeric = 18
    double_precision = 19
    current_time = 20
    current_date = 21
    now = 22
    date_part = 23
    extract = 24
    boolean = 25

class SELECT_TIME(Enum):
    EXTRACT = 1
    DATE_PART = 2
    NOW = 3
    CURRENT_DATE = 4
    CURRENT_TIME = 5
    TIMESTAMP = 6

class TIPO_VALOR(Enum):
    IDENTIFICADOR = 1
    NUMERO = 2
    DOBLE = 3
    ASTERISCO = 4
    NEGATIVO = 5
    AS_ID = 6
    ID_ASTERISCO = 7
    CADENA = 8

class TIPO_INSERT(Enum):
    CON_PARAMETROS = 1
    SIN_PARAMETROS = 2

class TIPO_LOGICA(Enum):
    AND = 1
    OR = 2
    NOT = 3

class TIPO_ALTER_TABLE(Enum):
    DROP_CONSTRAINT = 1
    RENAME_COLUMN = 2
    ADD_COLUMN = 3
    ADD_CHECK = 4
    ADD_FOREIGN = 5
    ADD_CONSTRAINT_CHECK = 6
    ADD_CONSTRAINT_UNIQUE = 7
    ADD_CONSTRAINT_FOREIGN = 8
    ALTER_COLUMN = 9
    DROP_COLUMN = 10
    NOT_NULL = 11
    ALTER_COLUMN_NULL = 12
    ALTER_COLUMN_NOT_NULL = 13


class TIPO_DELETE(Enum):
    DELETE_NORMAL = 1
    DELETE_RETURNING = 2
    DELETE_EXIST = 3
    DELETE_CONDIFION = 4
    DELETE_USING = 5
    DELETE_EXIST_RETURNING = 6
    DELETE_CONDICION_RETURNING = 7
    DELETE_USING_returnin = 8

class OPCIONES_DATOS(Enum):
    TRIM = 1
    SUBSTR = 2
    SUBSTRING = 3
    EXTRACT = 4
    SOME = 5
    ANY = 6

class OPCIONES_SELECT(Enum):
    DISTINCT = 1
    CASE = 2
    SUBCONSULTA = 3
    EXPRESION = 4
    FUNCIONES = 5
    GREATEST = 6
    LEAST = 7
    WHERE = 8
    GROUP_BY = 9
    HAVING = 10
    ORDER_BY = 11
    LIMIT = 12
    OFFSET = 13
    SELECT = 14

class OPCION_VERIFICAR(Enum):
    NULL = 1
    N_NULL = 2
    ISNULL = 3
    NOTNULL = 4
    TRUE = 5
    FALSE = 6
    N_TRUE = 7
    N_FALSE = 8
    UNKNOWN = 9
    N_UNKNOWN = 10  
    BETWEEN = 11
    NOT_IN = 12
    ISDISTINCT = 13
    NOT_DISTINCT = 14
    LIKE = 15
    NOT_LIKE = 16
    INN = 17
    NOT_EXISTS = 18 
    N_BETWEEN = 19
    BETWEEN_SYMETRIC = 20
    NOT_BETWEEN_SYMETRIC = 21
    EXTRACT = 22
    DATE_PART = 23
    NOW = 24
    CURRENT_DATE = 25
    CURRENT_TIME = 26
    TIMESTAMP = 27
    BETWEEN_1 = 28
    BETWEEN_2 = 29

class CADENA_BINARIA(Enum):
    LENGTH = 1
    SUBSTRING = 2
    TRIM = 3
    SUBSTR = 4
    GET_BYTE = 5
    SET_BYTE = 6
    SHA256 = 7
    ENCODE = 8
    DECODE = 9
    CONVERT = 10

class INSERT_EXCLUSIVA(Enum):
    SUBSTRING = 1
    MD5 = 2
    TRIM = 3
    NOW = 5

class ExpresionNumerica:
    '''
        Esta clase representa una expresión numérica
    '''

class ExpresionEntero(ExpresionNumerica) :
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self,etiqueta, val = 0) :
        self.val = val
        self.etiqueta = etiqueta


class ExpresionBinaria(ExpresionNumerica) :
    '''
        Esta clase representa la Expresión Aritmética Binaria.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionIdentificador(ExpresionNumerica) :
    def __init__(self,etiqueta, val = "") :
        self.etiqueta = etiqueta
        self.val = val ##Cambio

class ExpresionIdentificadorDoble(ExpresionNumerica) :
    def __init__(self,etiqueta, val = "", val1 = ""):
        self.etiqueta = etiqueta
        self.val = val ##Cambio
        self.val1 = val1 ##Cambio


class ExpresionNegativo(ExpresionNumerica) :
    '''
        Esta clase representa la Expresión Aritmética Negativa.
        Esta clase recibe la expresion
    '''
    def __init__(self,etiqueta, exp) :
        self.etiqueta = etiqueta
        self.exp = exp

class ExpresionRelacional() :
    '''
        Esta clase representa la expresión lógica.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionCadena :
    '''
        Esta clase representa una Expresión de tipo cadena.
    '''

class ExpresionComillaSimple(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas doble.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, operador,val):
        self.val = val
        self.operador = operador

class ExpresionLogica() :
    '''
        Esta clase representa la expresión lógica.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class Expresiondatos():
    def __init__(self,operador,exp1,exp2,exp3,exp4):
        self.operador = operador
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.exp4 = exp4

class ExpresionBooleana():
    def __init__(self,etiqueta,val):
        self.etiqueta = etiqueta
        self.val = val

class ExpresionNumero(ExpresionNumerica) :
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self, etiqueta ,val = 0, val1 = 0) :
        self.val = val
        self.val1 = val1
        self.etiqueta = etiqueta

class ExpresionNumeroSimple(ExpresionNumerica) :
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self, val = 0) :
        self.val = val


class Expresion_Caracter(ExpresionNumero):

    def __init__(self, etiqueta, val = 0):
        self.etiqueta = etiqueta
        self.val = val

class ExpresionTiempo():
    def __init__(self, operador):
        self.operador = operador



