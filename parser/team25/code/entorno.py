
class Simbolo:
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo

class Entorno:
    def __init__(self, anterior = None):
        self.anterior = anterior
        self.ts = {}
    
    def agregarSimbolo(self,key,valor,tipo) -> bool:
        if key in self.ts: #error de existir
            return False
        else:
            self.ts[key] = Simbolo(valor,tipo)
            return True

    def modificarSimbolo(self,key,valor) -> int:
        if not(key in self.ts): #Error de no existir
            return 2
        else:
            if self.__comprobarTipo(valor, self.ts[key].tipo): #Comprobamos que basado en el tipo, el valor sea valido
                self.ts[key].valor = valor
                return 0
            else:
                return 1

    def buscarSimbolo(self,key) -> Simbolo:
        if not(key in self.ts):
            if self.anterior != None:
                return self.anterior.buscarSimbolo(key)
            else:
                return None
        else:
            return self.ts[key]

    def __comprobarTipo(valor, tipo) -> bool:
        if isinstance(valor, int) and tipo == __VARIABLE_TYPE.INTEGER.value:
            return True
        elif (isinstance(valor, float) or isinstance(valor, int)) and tipo == __VARIABLE_TYPE.DECIMAL.value:
            return True
        elif isinstance(valor, str) and tipo == __VARIABLE_TYPE.STRING.value:
            return True
        elif isinstance(valor, bool) and tipo == __VARIABLE_TYPE.BOOLEAN.value:
            return True
        elif isinstance(valor, str) and tipo == __VARIABLE_TYPE.ENUM.value:
            return True
        return False

    
# Clase de tipo de valor para una variable
from enum import Enum
class __VARIABLE_TYPE(Enum):
    INTEGER = 'INTEGER'
    DECIMAL = 'DECIMAL'
    STRING = 'STRING'
    BOOLEAN = 'BOOLEAN'
    ENUM = 'ENUM'

#Metodo para la conversion de columnas del type reference a tipos en la tabla de simbolos
def toEnviroment(columns : list, env: Entorno) -> Entorno:
    # Por cada columna se verifica el tipo 
    for col in columns:
        #Dependiendo del tipo de columna, se establecera un tipo de variable especial
        tipo = __VARIABLE_TYPE.ENUM.value
        if col['Type'] == 'SMALLINT' \
        or col['Type'] == 'BIGINT' \
        or col['Type'] == 'INTEGER':
            tipo = __VARIABLE_TYPE.INTEGER.value
        elif col['Type'] == 'DECIMAL' \
        or col['Type'] == 'NUMERIC' \
        or col['Type'] == 'REAL' \
        or col['Type'] == 'DOUBLE_PRECISION' \
        or col['Type'] == 'MONEY':
            tipo = __VARIABLE_TYPE.DECIMAL.value
        elif col['Type'] == 'CHAR' \
        or col['Type'] == 'VARCHAR' \
        or col['Type'] == 'TEXT':
            tipo = __VARIABLE_TYPE.STRING.value
        elif col['Text'] == 'BOOLEAN':
            tipo = __VARIABLE_TYPE.BOOLEAN.value
        #Asignamos el valor de la columna en la tabla como nulo
        env.agregarSimbolo(col, None, tipo)

    return env