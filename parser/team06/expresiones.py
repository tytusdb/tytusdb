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

