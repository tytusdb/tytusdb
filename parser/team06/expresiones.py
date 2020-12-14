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

class OPERACION_RESTRICCION_COLUMNA(Enum):
    CHECK_SIMPLE = 1
    CHECK_CONSTRAINT = 2
    UNIQUE_COLUMNA = 3    
    UNIQUE_SIMPLE = 4
    UNIQUE_CONSTAINT = 5
    PRIMARY_KEY = 6
    FOREIGN_KEY = 7
    NULL = 8
    NOT_NULL = 9
    DEFAULT = 10
    COLUMNASINRESTRICCION=11
    COLUMNACONRESTRICCION=12

class RestriccionTabla:
    '''
        Esta clase representa las restricciones en la tabla
    '''

class RestriccionPrimaryKeyColumn(RestriccionTabla):
    '''Esta clase representa la restricion de una columna
        como tipo primary key
    '''
    def __init__(self,primary):
        self.primary=primary

class RestriccionPrimaryKey(RestriccionTabla):
    '''
        Esta clase representa la restriccion de llave 
        primaria de una o varis columnas
    '''
    def __init__(self,listColumn=[]):
        self.listColumn=listColumn

class RestriccionForeingkey(RestriccionTabla):
    '''
        Esta clase representa la restriccion de que
        columna es una llave foranea
    ''' 
    def __init__(self,idForanea,idTable,idLlaveF):
        self.idForanea=idForanea
        self.idTable=idTable
        self.idLlaveF=idLlaveF

class RestriccionConstraintCheck(RestriccionTabla):
    '''
        Esta clase representa la restriccion de check
        con su contraint en la columna
    '''
    def __init__(self,idConstraint,condChek):
        self.idConstraint = idConstraint
        self.condCheck = condChek

class RestriccionCheck(RestriccionTabla):
    '''
        Esta clase representa la restriccion de check
        de una columna
    '''
    def __init__(self,condCheck):
        self.condCheck=condCheck

class RestriccionUniqueSimple(RestriccionTabla):
    '''
        Esta clase representa la restricion de unique
        que es definido en la columna
    '''
    def __init__(self,var):
        self.var=var

class RestriccionConstraintUnique(RestriccionTabla):
    '''
        Esta clase representa la restriccion de unique
        con su respectivo contraint
    '''
    def __init__(self,idUnique):
        self.idUnique=idUnique
        

class RestriccionUnique(RestriccionTabla):
    '''
        Esta clase represetna las restriciones que tendran
        las columnas de forma unique
    '''
    def __init__(self,listColumn=[]):
        self.listColumn=listColumn

class RestriccionNull(RestriccionTabla):
    '''
        Esta clase representa que la columna podra ser nula
    '''
    def __init__(self,var):
        self.var = var

class RestriccionNotNull(RestriccionTabla):
    '''
        Esta clase representa que la columna simpre debe de tener
        se le debe de ingresar un valor, al insertar datos a la tabla
    '''
    def __init__(self,var):
        self.var = var

class RestriccionDefaul(RestriccionTabla):
    '''
        Esta clase representa que la columna de le asigna un valor por
        default al crear la tabla
    '''
    def __init__(self,valor):
        self.valor = valor

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
