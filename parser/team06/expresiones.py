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


# ---------------------------------------------------------------------------------------------------------------- 
class ExpresionInvocacion(ExpresionNumerica) :
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self, id = "",id1 = "") :
        self.id = id
        self.id1 = id1
# ---------------------------------------------------------------------------------------------------------------- 


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


# ---------------------------------------------------------------------------------------------------------------- 
#clases para los tipos de dato
class DataType:
    '''
        Esta clase representa las limitaciones en un
        tipo de dato, que se le asignara a la columna
        en una tabla
    '''
class TipoDatoColumna(DataType):
    '''
        Esta clase representa las limitaciones que tendra
        el tipo de dato en una columna, que es creada en la 
        tabla
    '''
    def __init__(self,id,longitud):
        self.id=id
        self.longitud=longitud


# ---------------------------------------------------------------------------------------------------------------- 
#clases para restricciones
class OPERACION_RESTRICCION_COLUMNA(Enum):
    CHECK_SIMPLE = 1
    CHECK_CONSTRAINT = 2
    UNIQUE_COLUMNA = 3    #<--- Cuando se declara en la columna
    UNIQUE_ATRIBUTO = 4   #<--- Cuando se declara como atributo   
    UNIQUE_CONSTAINT = 5  #<--- Cuando se declara con constraint
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
    def __init__(self,idTable,idForanea=[],idLlaveF=[]):
        self.idForanea=idForanea
        self.idTable=idTable
        self.idLlaveF=idLlaveF

class RestriccionConstraintCheck(RestriccionTabla):
    '''
        Esta clase representa la restriccion de check
        con su contraint en la columna
    '''
    def __init__(self,idConstraint,condCheck):
        self.idConstraint = idConstraint
        self.condCheck = condCheck

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

class CondicionDelete:
    '''
        Esta clase representa la condicon que se le dara para poder
        eliminar un registro en una tabla
    '''
class operacionDelete(CondicionDelete):
    '''
        Esta clase representa los valores que se validaran para poder
        eliminar un registro
    '''
    def __init__(self,exp1,exp2,operador):
        self.exp1=exp1
        self.exp2=exp2
        self.operador=operador

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
class ExpresionMode(ExpresionQueries) :
    '''
        Esta clase representa la Expresión Aritmética.
        Esta clase recibe los operandos y el operador
    '''
    def __init__(self, mode, final) :
        self.mode = mode
        self.final = final
# ---------------------------------------------------------------------------------------------------------------- 
#                                             CLASE Y CONSTRUCTORES DE LAS DIFERENTES EXPRESIONES
# ----------------------------------------------------------------------------------------------------------------

class ExpresionGREATEST(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionLEAST(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionNOW(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, id) :
        self.id = id

# mis expresiones para el where
class ExpresionCondicionAND(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

class ExpresionCondicionOR(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

class ExpresionBetween(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    
class ExpresionNotBetween(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

class ExpresionBetweenSymmetric(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

class ExpresionNotBetweenSymmetric(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

class ExpresionIsDistinct(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

class ExpresionIsNotDistinct(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2


class ExpresionIgualdad(ExpresionNumerica):
    '''
        Esta clase representa que valor sera actualizado en una
        columna, o la condicion que debe cumplir la columna para 
        poder actulizar
    '''
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2

#---------- expresiones complementarias del where--------------
class ExpresionLimit(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, valor1):
        self.valor1 = valor1

class ExpresionLimitOffset(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

class ExpresionGroup(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, valor1):
        self.valor1 = valor1

class ExpresionHaving(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, valor1):
        self.valor1 = valor1

class ExpresionOrder(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

class ExpresionNotIn(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, valor1,valor2):
        self.valor1 = valor1
        self.valor2 = valor2

class ExpresionIn(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, valor1,valor2):
        self.valor1 = valor1
        self.valor2 = valor2

class ExpresionNotExists(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, valor1):
        self.valor1 = valor1

class ExpresionExists(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, valor1):
        self.valor1 = valor1

class ExpresionLlamame(ExpresionNumerica) :
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self, id = "",id1 = "") :
        self.id = id
        self.id1 = id1

class ExpresionLENGTH(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1) :
        self.exp1 = exp1

class ExpresionSUBSTR(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1,exp2,exp3) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3

class ExpresionSHA256(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1) :
        self.exp1 = exp1

class ExpresionMD5(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1) :
        self.exp1 = exp1

class ExpresionSUBSTRINGA(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1,exp2,exp3) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3

class ExpresionSUBSTRINGB(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1,exp2) :
        self.exp1 = exp1
        self.exp2 = exp2

class ExpresionSUBSTRINGC(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1,exp2) :
        self.exp1 = exp1
        self.exp2 = exp2

class ExpresionTRIM(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1,exp2,exp3) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3

class ExpresionCurrentTime(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1) :
        self.exp1 = exp1

class ExpresionCurrentDate(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1) :
        self.exp1 = exp1

class ExpresionEXTRACT(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, exp1,exp2) :
        self.exp1 = exp1
        self.exp2 = exp2

# -----------------------------------------------------------------------------------------------------
#                       EXPRESIONES PARA JOINS

class ExpresionJoinA(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, tabla1,tipo,tabla2,condicion) :
        self.tabla1=tabla1
        self.tipo=tipo
        self.tabla2=tabla2
        self.condicion=condicion

class ExpresionJoinB(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, tabla1,natural,tipo,tabla2) :
        self.tabla1=tabla1
        self.natural=natural
        self.tipo=tipo
        self.tabla2=tabla2

class ExpresionJoinC(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, tabla1,natural,auxiliar,tipo,tabla2) :
        self.tabla1=tabla1
        self.natural=natural
        self.auxiliar=auxiliar
        self.tipo=tipo
        self.tabla2=tabla2


class ExpresionJoinD(ExpresionNumerica):
    '''
        Esta clase representa la expresión para castear datos.
        Esta clase recibe un tipo a convertir y el dato
    '''
    def __init__(self, tabla1,auxiliar,tipo,tabla2,operacion) :
        self.tabla1=tabla1
        self.auxiliar=auxiliar
        self.tipo=tipo
        self.tabla2=tabla2
        self.operacion=operacion
        
class SortOptions(ExpresionNumerica):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, sort, option):
        self.sort = sort
        self.option = option
