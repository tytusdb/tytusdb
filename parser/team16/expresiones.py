from enum import Enum

class OPERACION_ARITMETICA(Enum) :
    MAS = 1
    MENOS = 2
    MULTI = 3
    DIVIDIDO = 4
    RESIDUO = 5
    POTENCIA = 6
    CUADRATICA = 7
    CUBICA = 8

class OPERACION_LOGICA(Enum) :
    AND = 1
    OR = 2
    XOR = 3
    #nuevas logias Edilson
    BETWEEN = 4
    NOT_BETWEEN = 5
    IS_DISTINCT = 6
    IS_NOT_DISTINCT = 7
    IS_NULL= 8
    IS_NOT_NULL = 9
    IS_TRUE= 10
    IS_NOT_TRUE= 11
    IS_FALSE= 12
    IS_NOT_FALSE= 13
    IS_UNKNOWN= 14
    IS_NOT_UNKNOWN= 15
    IN = 16
    NOT_IN = 17
    EXISTS = 18
    NOT_EXISTS=19
    NOT = 20

class OPERACION_RELACIONAL(Enum) :
    IGUALQUE = 1
    DISTINTO = 2
    MAYORIGUAL = 3
    MENORIGUAL = 4
    MAYORQUE = 5
    MENORQUE = 6

class OPERACION_BIT_A_BIT(Enum) :
    AND = 1
    OR = 2
    XOR = 3
    SHIFT_IZQ = 4
    SHIFT_DER = 5
    COMPLEMENTO = 6
    
class TIPO_VARIABLE(Enum) :
    TEMPORAL = 1 
    PARAMETRO = 2
    VALOR_DEV_FUN = 3
    RA = 4
    STACK = 5
    SP = 6

class TIPO_DATO(Enum) :
    ENTERO = 1
    FLOTANTE = 2
    CADENA = 3
    ARREGLO = 4
    CHAR = 5

class FUNCION_NATIVA(Enum):
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
    SIGN = 18
    SQRT = 19
    WIDTH_BUCKET = 20
    TRUNC = 21
    RANDOM = 22
    ACOS = 23
    ACOSD = 24
    ASIN = 25
    ASIND = 26
    ATAN = 27
    ATAND = 28
    ATAN2 = 29
    ATAN2D = 30
    COS = 31
    COSD = 32
    COT = 33
    COTD = 34
    SIN = 35
    SIND = 36
    TAN = 37
    TAND = 38
    SINH = 39
    COSH = 40
    TANH = 41
    ASINH = 42
    ACOSH = 43
    ATANH = 44
    LENGTH = 45
    SUBSTRING = 46
    TRIM = 47
    MD5 = 48
    SHA256 = 49
    SUBSTR = 50
    GET_BYTE = 51
    SET_BYTE = 52
    CONVERT = 53
    ENCODE = 54
    DECODE = 55
    NOW = 56
    EXTRACT = 57
    DATE_PART = 58


class CONDICIONAL_SUBQUERY(Enum):
    ALL = 1
    ANY = 2
    SOME = 3


class UNIDAD_TIEMPO(Enum):
    YEAR = 1
    MONTH = 2
    DAY = 3
    HOUR = 4
    MINUTE = 5
    SECOND = 6

class CONSTANTES(Enum):
    CURRENT_DATE = 1
    CURRENT_TIME = 2

#------------------------------------------------------------------------

class Casteo() :
    def __init__(self,tipo_dato,variable) :
        self.tipo_dato = tipo_dato
        self.variable = variable

#------------------------------------------------------------------------

class UnitariaNegAritmetica() :
    def __init__(self, exp) :
        self.exp = exp

class UnitariaLogicaNOT() :
    def __init__(self, expresion):
        self.expresion=expresion


#Objeto exist
class UnitariaLogicaEXIST() :
    def __init__(self, expresion):
        self.expresion=expresion



class UnitariaNotBB() :
    def __init__(self, expresion):
        self.expresion=expresion

class UnariaReferencia() :
    def __init__(self,tipoVar):
        self.tipoVar=tipoVar




#NUEVAS UNITARIAS
class UnitariaLogicaIS_NOT_NULL() :
    def __init__(self, expresion):
        self.expresion=expresion

class UnitariaLogicaIS_NOT_TRUE() :
    def __init__(self, expresion):
        self.expresion=expresion

class UnitariaLogicaIS_NOT_FALSE() :
    def __init__(self, expresion):
        self.expresion=expresion

class UnitariaLogicaIS_NOT_UNKNOWN() :
    def __init__(self, expresion):
        self.expresion=expresion

class UnitariaLogicaIS_IS_NULL() :
    def __init__(self, expresion):
        self.expresion=expresion

class UnitariaLogicaIS_IS_TRUE() :
    def __init__(self, expresion):
        self.expresion=expresion

class UnitariaLogicaIS_IS_FALSE() :
    def __init__(self, expresion):
        self.expresion=expresion

class UnitariaLogicaIS__UNKNOWN() :
    def __init__(self, expresion):
        self.expresion=expresion
#------------------------------------------------------------------------

class Expresion:
    '''Clase abstracta'''

class Parametro(Expresion) :
    def __init__(self, expresion) :
        self.expresion=expresion

'''
class Variable(Expresion) :
    def __init__(self, id, tipoVar):
        self.id=id
        self.tipoVar=tipoVar'''

class ExpresionValor(Expresion):
    def __init__(self, val):
        self.val = val

class AccesoArray(Expresion) :
    def __init__(self, tipoVar, params=[]) :
        self.tipoVar=tipoVar
        self.params=params
#------------------------------------------------------

class ExpresionAritmetica(Expresion) :
   
    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

#------------------------------------------------------

class ExpresionLogica(Expresion) :
    
    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

#------------------------------------------------------
class ExpresionRelacional(Expresion) :

    def __init__(self,exp1,exp2,operador) :
        self.exp1=exp1
        self.exp2=exp2
        self.operador=operador

#------------------------------------------------------
class ExpresionBitABit(Expresion) :

    def __init__(self,exp1,exp2,operador) :
        self.exp1=exp1
        self.exp2=exp2
        self.operador=operador

# ------------------------------------------------------
class valorTipo(Expresion):
    def __init__(self, valor, expresion):
        self.valor = valor
        self.expresion = expresion


#-----------------------------------------------------------

#CLASES EDILSON
class UnitariaArismeticaABS() :
    def __init__(self, expresion):
        self.expresion=expresion

#-----------------------------------------------------------------
class ExpresionValor2(Expresion) :
    def __init__(self, val ,tipo ):
        self.val = val
        self.tipo = tipo


class ExpresionCondicionalSubquery(Expresion):
    def __init__(self, val):
        self.val = val

# ================================================================0000000
class Variable(Expresion) :
    def __init__(self,id ,tipo_var):
        self.id = id
        self.tipo_var = tipo_var


class ExpresionFuncion(Expresion):
    def __init__(self, exp1, exp2, exp3, exp4, id_funcion):
        self.id_funcion = id_funcion
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.exp4 = exp4

class ExpresionBinaria(Expresion):
    def __init__(self, exp1, exp2, exp3, exp4, id_funcion):
        self.id_funcion = id_funcion
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.exp4 = exp4

class UnitariaAritmetica(Expresion):
    def __init__(self, exp1, operador):
        self.exp1 = exp1
        self.operador = operador

class CAMPO_TABLA_ID_PUNTO_ID(Expresion):
    def __init__(self, tablaid, campoid,tipovariable):
        self.tablaid = tablaid
        self.campoid = campoid
        self.tipovariable = tipovariable

class ExpresionTiempo(Expresion):
    def __init__(self, nombre, id_tiempo):
        self.nombre = nombre
        self.id_tiempo = id_tiempo

class ExpresionConstante(Expresion):
    def __init__(self, nombre, id_constate):
        self.nombre = nombre
        self.id_constate = id_constate