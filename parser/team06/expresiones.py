from enum import Enum
# ---------------------------------------------------------------------------------------------------------------- 
#                                             ENUMS
# ----------------------------------------------------------------------------------------------------------------

class OPERACION_ARITMETICA(Enum) :
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    MODULO = 5
    POTENCIA = 6
#faltan algunas creo yo

class OPERACION_LOGICA(Enum) :
    NOT  = 1
    AND = 2
    OR = 3


class OPERACION_BIT(Enum):
    DESPLAZAMIENTO_IZQUIERDA = 1
    DESPLAZAMIENTO_DERECHA = 2

class OPERACION_RELACIONAL(Enum):
    IGUAL_IGUAL = 1
    NO_IGUAL = 2
    MAYOR_IGUAL = 3
    MENOR_IGUAL = 4
    MAYOR = 5
    MENOR = 6
    DIFERENTE = 7

class OPERACION_FUNCION_DEFINIDA(Enum):
    OPERACION_ABS=1
    #FALTA EL MONTON
# ---------------------------------------------------------------------------------------------------------------- 
#                                             ENUMS
# ----------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------- 
#                                             CLASE Y CONSTRUCTORES DE LAS DIFERENTES EXPRESIONES
# ----------------------------------------------------------------------------------------------------------------

class ExpresionNumerica:
    '''
        Esta clase representa una expresión numérica
    '''

class ExpresionAritmetica(ExpresionNumerica) :
    '''
        Esta clase representa la Expresión Aritmética.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
# ---------------------------------------------------------------------------------------------------------------- 

class ExpresionLogica(ExpresionNumerica) :
    '''
        Esta clase representa la Expresión Logica.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
# ---------------------------------------------------------------------------------------------------------------- 

class ExpresionBIT(ExpresionNumerica) :
    '''
        Esta clase representa la Expresión Logica.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
# ---------------------------------------------------------------------------------------------------------------- 

class ExpresionRelacional(ExpresionNumerica) :
    '''
        Esta clase representa la Expresión Logica.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
 # ---------------------------------------------------------------------------------------------------------------- 
   
class ExpresionNOT(ExpresionNumerica):
    '''
        Esta clase representa la expresión lógica para el not.
        Esta clase recibe un operando y el operador !
    '''
    def __init__(self, exp) :
        self.exp = exp
# ---------------------------------------------------------------------------------------------------------------- 

class ExpresionNegativo(ExpresionNumerica):
    '''
        Esta clase representa la expresión lógica para el not.
        Esta clase recibe un operando y el operador !
    '''
    def __init__(self, exp) :
        self.exp = exp
# ---------------------------------------------------------------------------------------------------------------- 

class ExpresionNumero(ExpresionNumerica) :
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self, val = 0) :
        self.val = val
# ---------------------------------------------------------------------------------------------------------------- 
class ExpresionIdentificador(ExpresionNumerica) :
    '''
        Esta clase representa un identificador.
    '''

    def __init__(self, id = "") :
        self.id = id
# ---------------------------------------------------------------------------------------------------------------- 
class ExpresionInvocacion(ExpresionNumerica) :
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self, id = "",id1 = "") :
        self.id = id
        self.id1 = id1
# ---------------------------------------------------------------------------------------------------------------- 
class ExpresionCadena :
    '''
        Esta clase representa una Expresión de tipo cadena.
    '''


class ExpresionCadenas(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas simples.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, val) :
        self.val = val

# ---------------------------------------------------------------------------------------------------------------- 

class ExpresionQueries:
    '''
        Esta clase representa una expresión numérica
    '''
class ExpresionOwner(ExpresionQueries) :
    '''
        Esta clase representa la Expresión Aritmética.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, owner, final) :
        self.owner = owner
        self.final = final

class ExpresionMode(ExpresionQueries) :
    '''
        Esta clase representa la Expresión Aritmética.
        Esta clase recibe los operandos y el operador
    '''
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

    def __init__(self, mode, final) :
        self.mode = mode
        self.final = final
# ---------------------------------------------------------------------------------------------------------------- 
#                                             CLASE Y CONSTRUCTORES DE LAS DIFERENTES EXPRESIONES
# ----------------------------------------------------------------------------------------------------------------
