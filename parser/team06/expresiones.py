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

    def __init__(self, mode, final) :
        self.mode = mode
        self.final = final
# ---------------------------------------------------------------------------------------------------------------- 
#                                             CLASE Y CONSTRUCTORES DE LAS DIFERENTES EXPRESIONES
# ----------------------------------------------------------------------------------------------------------------
