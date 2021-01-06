
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
        if not key in self.ts:
            if self.anterior != None:
                return self.anterior.buscarSimbolo(key)
            else:
                return None
        else:
            return self.ts[key]

    def __comprobarTipo(self ,valor, tipo) -> bool:
        if isinstance(valor, int) and tipo == VARIABLE_TYPE.INTEGER.value:
            return True
        elif (isinstance(valor, float) or isinstance(valor, int)) and tipo == VARIABLE_TYPE.DECIMAL.value:
            return True
        elif isinstance(valor, str) and tipo == VARIABLE_TYPE.STRING.value:
            return True
        elif isinstance(valor, bool) and tipo == VARIABLE_TYPE.BOOLEAN.value:
            return True
        elif isinstance(valor, str) and tipo == VARIABLE_TYPE.ENUM.value:
            return True
        return False

    
# Clase de tipo de valor para una variable
from enum import Enum
class VARIABLE_TYPE(Enum):
    INTEGER = 'INTEGER'
    DECIMAL = 'DECIMAL'
    STRING = 'STRING'
    BOOLEAN = 'BOOLEAN'
    ENUM = 'ENUM'
    DATE = 'DATE'

#Metodo para la conversion de columnas del type reference a tipos en la tabla de simbolos
def toEnviroment(columns : dict, env: Entorno) -> Entorno:
    # Por cada columna se verifica el tipo 
    for col in columns:
        #Dependiendo del tipo de columna, se establecera un tipo de variable especial
        tipo = VARIABLE_TYPE.STRING.value
        if columns[col]['Type'] == 'SMALLINT' \
        or columns[col]['Type'] == 'BIGINT' \
        or columns[col]['Type'] == 'INTEGER':
            tipo = VARIABLE_TYPE.INTEGER.value
        elif columns[col]['Type'] == 'DECIMAL' \
        or columns[col]['Type'] == 'NUMERIC' \
        or columns[col]['Type'] == 'REAL' \
        or columns[col]['Type'] == 'DOUBLE_PRECISION' \
        or columns[col]['Type'] == 'MONEY':
            tipo = VARIABLE_TYPE.DECIMAL.value
        elif columns[col]['Type'] == 'CHAR' \
        or columns[col]['Type'] == 'VARCHAR' \
        or columns[col]['Type'] == 'TEXT':
            tipo = VARIABLE_TYPE.STRING.value
        elif columns[col]['Type'] == 'BOOLEAN':
            tipo = VARIABLE_TYPE.BOOLEAN.value
        elif columns[col]['Type'] == 'DATE':
            tipo = VARIABLE_TYPE.DATE.value
        #Asignamos el valor de la columna en la tabla como nulo
        env.agregarSimbolo(col, None, tipo)

    return env