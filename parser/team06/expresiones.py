from enum import Enum

class OPERACION_ARITMETICA(Enum) :
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    RESIDUO = 5
#faltan algunas creo yo

class OPERACION_LOGICA(Enum) :
    NOT  = 1
    AND = 2
    OR = 3


class OPERACION_BIT(Enum):
    NOT = 1
    AND = 2
    OR = 3
    XOR= 4
    DESPLAZAMIENTO_IZQUIERDA = 5
    DESPLAZAMIENTO_DERECHA = 6

class OPERACION_RELACIONAL(Enum):
    IGUAL_IGUAL = 1
    NO_IGUAL = 2
    MAYOR_IGUAL = 3
    MENOR_IGUAL = 4
    MAYOR = 5
    MENOR = 6

class OPERACION_FUNCION_DEFINIDA(Enum):
    OPERACION_ABS=1
    #FALTA EL MONTON


class ExpresionNumerica:
    '''
        Esta clase representa una expresión numérica
    '''
class ExpresionNegativo(ExpresionNumerica) :
    '''
        Esta clase representa la Expresión Aritmética Negativa
        Esta clase recibe la expresion
    '''
    def __init__(self, id) :
        self.id = id

class ExpresionNumero(ExpresionNumerica) :
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self, id = 0) :
        self.id = id

class ExpresionIdentificador(ExpresionNumerica) :
    '''
        Esta clase representa un identificador.
    '''

    def __init__(self, id = "") :
        self.id = id



class ExpresionFuncionBasica(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, id) :
        self.id = id

class ExpresionCadena :
    '''
        Esta clase representa una Expresión de tipo cadena.
    '''


class ExpresionCadenas(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas simples.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, id) :
        self.id = id

# ---------------------------------------------------------------------------------------------------------------------
#                                EXPRESIONES DE LAS OPERACIONES BASICAS PARA EL SELECT
# ---------------------------------------------------------------------------------------------------------------------

class ExpresionABS(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionCBRT(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionCEIL(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionCEILING(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionDEGREES(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionDIV(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1,exp2) :
        self.exp1 = exp1
        self.exp2 = exp2

class ExpresionEXP(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionFACTORIAL(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionFLOOR(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionGCD(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1,exp2) :
        self.exp1 = exp1
        self.exp2 = exp2

class ExpresionLN(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionLOG(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionMOD(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1,exp2) :
        self.exp1 = exp1
        self.exp2 = exp2

class ExpresionPI(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp


class ExpresionPOWER(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1,exp2) :
        self.exp1 = exp1
        self.exp2 = exp2


class ExpresionRADIANS(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionROUND(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionSIGN(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionSQRT(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionTRUNC(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionRANDOM(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionWIDTHBUCKET(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1,exp2,exp3,exp4) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.exp4 = exp4

# ----------------------------------------------------------------
#           EMPIEZAN LAS TRIGONOMETRICAS

class ExpresionACOS(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionACOSD(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionASIN(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionASIND(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionATAN(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionATAND(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionATAN2(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1,exp2) :
        self.exp1 = exp1
        self.exp2 = exp2


class ExpresionATAN2D(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1,exp2) :
        self.exp1 = exp1
        self.exp2 = exp2



class ExpresionCOS(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionCOSD(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionCOT(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionCOTD(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionSIN(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionSIND(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionTAN(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionTAND(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionSINH(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionCOSH(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp


class ExpresionTANH(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionASINH(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionACOSH(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionATANH(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

# ----------------------------------------------------------------
#               BINARY STRING FUNCTIONS
