from enum import  Enum

class MODE(Enum):
    '''
        STRING: usa el metodo execute pero solo reconstruye la sentencia
        C3D    : usa el metodo execute y lo traduce
    '''
    STRING = 0
    C3D = 1