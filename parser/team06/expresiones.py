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


