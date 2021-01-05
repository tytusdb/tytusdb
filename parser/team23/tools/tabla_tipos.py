from enum import Enum

class tipo_primitivo(Enum): 
    #NUMERIC TYPES
    SMALLINT = 0
    INTEGER = 1
    BIGINT = 2
    DECIMAL = 3
    REAL = 4
    DOUBLE_PRECISION = 5
    MONEY = 6

    #CHARACTER TYPES
    VARCHAR = 7
    CHAR = 8
    TEXT = 9

    #DATE/TIME TYPES
    TIMESTAMP = 10
    DATE = 11
    TIME = 12
    INTERVAL = 13

    #BOOLEAN TYPES
    BOOLEAN = 14

    #ENUMERATED TYPES
    ENUMERATED = 15

    NULL = 16
    ERROR = 17

    TABLA = 18
      

class nodo_AST:
    def __init__(self, valor, num):
        self.valor = str(valor)
        self.num = str(num)
        self.hijos = []

tipos_tabla = [
    [tipo_primitivo.SMALLINT, tipo_primitivo.INTEGER, tipo_primitivo.BIGINT, tipo_primitivo.DECIMAL, tipo_primitivo.REAL, tipo_primitivo.DOUBLE_PRECISION, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.SMALLINT],
    [tipo_primitivo.INTEGER, tipo_primitivo.INTEGER, tipo_primitivo.BIGINT, tipo_primitivo.DECIMAL, tipo_primitivo.REAL, tipo_primitivo.DOUBLE_PRECISION, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.INTEGER],
    [tipo_primitivo.BIGINT, tipo_primitivo.BIGINT, tipo_primitivo.BIGINT, tipo_primitivo.DECIMAL, tipo_primitivo.REAL, tipo_primitivo.DOUBLE_PRECISION, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.BIGINT],
    [tipo_primitivo.DECIMAL, tipo_primitivo.DECIMAL, tipo_primitivo.DECIMAL, tipo_primitivo.DECIMAL, tipo_primitivo.REAL, tipo_primitivo.DOUBLE_PRECISION, tipo_primitivo.MONEY, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.DECIMAL],
    [tipo_primitivo.REAL, tipo_primitivo.REAL, tipo_primitivo.REAL, tipo_primitivo.REAL, tipo_primitivo.REAL, tipo_primitivo.DOUBLE_PRECISION, tipo_primitivo.MONEY, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.REAL],
    [tipo_primitivo.DOUBLE_PRECISION, tipo_primitivo.DOUBLE_PRECISION, tipo_primitivo.DOUBLE_PRECISION, tipo_primitivo.DOUBLE_PRECISION, tipo_primitivo.DOUBLE_PRECISION, tipo_primitivo.DOUBLE_PRECISION, tipo_primitivo.MONEY, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.DOUBLE_PRECISION],
    [tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.MONEY, tipo_primitivo.MONEY, tipo_primitivo.MONEY, tipo_primitivo.MONEY, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.MONEY], 
    [tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.VARCHAR, tipo_primitivo.VARCHAR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.VARCHAR],
    [tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.VARCHAR, tipo_primitivo.CHAR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.CHAR],
    [tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.TEXT, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.TEXT],
    [tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.TIMESTAMP, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.TIMESTAMP],
    [tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.DATE, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.DATE],
    [tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.TIME, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.TIME],
    [tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.INTERVAL, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.INTERVAL],
    [tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.BOOLEAN, tipo_primitivo.ERROR, tipo_primitivo.BOOLEAN],
    [tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ENUMERATED, tipo_primitivo.ENUMERATED],
    [tipo_primitivo.SMALLINT, tipo_primitivo.INTEGER, tipo_primitivo.BIGINT, tipo_primitivo.DECIMAL, tipo_primitivo.REAL, tipo_primitivo.DOUBLE_PRECISION, tipo_primitivo.MONEY, tipo_primitivo.VARCHAR, tipo_primitivo.CHAR, tipo_primitivo.TEXT, tipo_primitivo.TIMESTAMP, tipo_primitivo.DATE, tipo_primitivo.TIME, tipo_primitivo.INTERVAL, tipo_primitivo.BOOLEAN, tipo_primitivo.ENUMERATED, tipo_primitivo.NULL],
]

#  SMALLINT  -  INTEGER  -  BIGINT  -  DECIMAL  -  REAL   -  DOUBLE_P  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR
#  INTEGER   -  INTEGER  -  BIGINT  -  DECIMAL  -  REAL   -  DOUBLE_P  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  
#  BIGINT    -  BIGINT   -  BIGINT  -  DECIMAL  -  REAL   -  DOUBLE_P  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR    
#  DECIMAL   -  DECIMAL  -  DECIMAL -  DECIMAL  -  REAL   -  DOUBLE_P  -  MONEY  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  
#  REAL      -   REAL    -   REAL   -    REAL   -  REAL   -  DOUBLE_P  -  MONEY  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR 
#  DOUBLE_P  -  DOUBLE_P - DOUBLE_P - DOUBLE_P  - DOUBLE_P-  DOUBLE_P  -  MONEY  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR   
#  ERROR     -    ERROR  -   ERROR  -  MONEY    -   MONEY -    MONEY   -  MONEY  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  
#  ERROR     -    ERROR  -   ERROR  -  ERROR    -   ERROR -    ERROR   -  ERROR  - VARCHAR -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  
#  ERROR     -    ERROR  -   ERROR  -  ERROR    -  ERROR  -  ERROR     -  ERROR  -  ERROR  -   CHAR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  
#  ERROR     -   ERROR   -   ERROR  -   ERROR   -  ERROR  -   ERROR    -  ERROR  -  ERROR  -  ERROR  -  TEXT   -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  
#  ERROR     -   ERROR   -   ERROR  -   ERROR   -  ERROR  -   ERROR    -  ERROR  -  ERROR  -  ERROR  -  ERROR  -TIMESTAMP-  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR
#  ERROR     -   ERROR   -   ERROR  -   ERROR   -  ERROR  -   ERROR    -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  DATE   -  ERROR  -  ERROR  -  ERROR  -  ERROR 
#  ERROR     -   ERROR   -   ERROR  -   ERROR   -  ERROR  -   ERROR    -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -   TIME  -  ERROR  -  ERROR  -  ERROR 
#  ERROR     -   ERROR   -   ERROR  -   ERROR   -  ERROR  -   ERROR    -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  - INTERVAL-  ERROR  -  ERROR  
#  ERROR     -   ERROR   -   ERROR  -   ERROR   -  ERROR  -   ERROR    -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  - BOOLEAN -  ERROR 
#  ERROR     -   ERROR   -   ERROR  -   ERROR   -  ERROR  -   ERROR    -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ERROR  -  ENUM 