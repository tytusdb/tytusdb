import re
from queries import *
from expresiones import *
# -----------------------------------------------------------------------------
# Grupo 6
#
# Universidad de San Carlos de Guatemala
# Facultad de Ingenieria
# Escuela de Ciencias y Sistemas
# Organizacion de Lenguajes y Compiladores 2
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
#                       INICIA ANALIZADOR LEXICO
# -----------------------------------------------------------------------------
#palabras reservadas del lenguaje
reservadas = {
    #   PALABRAS RESERVADAS POR SQL
    'show' : 'SHOW',
    'databases' : 'DATABASES',
    'database' : 'DATABASE',
    'tables' : 'TABLES',
    'columns' : 'COLUMNS',
    'from' : 'FROM',
    'select' : 'SELECT',
    'distinct' : 'DISTINCT',
    'limit' : 'LIMIT',
    'offset' : 'OFFSET',
    'of':'OF',
    'order' : 'ORDER',
    'by' : 'BY',
    'where' : 'WHERE',
    'and' : 'AND',
    'or' : 'OR',
    'not' : 'NOT',
    'in' : 'IN',
    'concat' : 'CONCAT',
    'only':'ONLY',
    'as' : 'AS',
    'sqrt' : 'SQRT',
    'avg' : 'AVG',
    'sum' : 'SUM',
    'cont' :'CONT',
    'desc' : 'DESC',
    'asc' : 'ASC',
    'like' : 'LIKE',
    'min' : 'MIN',
    'max' : 'MAX',
    'abs' : 'ABS',
    'on' : 'ON',
    'union' : 'UNION',
    'all' : 'ALL',
    'insert' : 'INSERT',
    'into' : 'INTO',
    'values' : 'VALUES',
    'update' : 'UPDATE',
    'set' : 'SET',
    'delete' : 'DELETE',
    'create' : 'CREATE',
    'primary' : 'PRIMARY',
    'key' : 'KEY',
    'null' : 'NULL',
    'nulls':'NULLS',

    'unique' : 'UNIQUE',
    'check' : 'CHECK',
    'cbrt' : 'CBRT',
    'ceil' : 'CEIL',
    'ceiling' : 'CEILING',
    'degrees' : 'DEGREES',
    'div':'DIV',
    'exp':'EXP',
    'factorial':'FACTORIAL',
    'floor':'FLOOR',
    'gcd':'GCD',
    'lcm':'LCM',
    'ln':'LN',
    'log':'LOG',
    'log10':'LOG10',
    #'current':'CURRENT',
    'default' : 'DEFAULT',
    'auto_increment' : 'AUTO_INCREMENT',
    'alter' : 'ALTER',
    'table' : 'TABLE',
    'add' : 'ADD',
    'drop' : 'DROP',
    'column' : 'COLUMN',
    'rename' : 'RENAME',
    'to' : 'TO',
    'replace' : 'REPLACE',
    'type' : 'TYPE',
    'enum' : 'ENUM',
    'if' : 'IF',
    'exists' : 'EXISTS',
    'min_scale':'MIN_SCALE',
    'mod':'MOD',
    'pi':'PI',
    'power':'POWER',
    'radians':'RADIANS',
    'round':'ROUND',
    'scale':'SCALE',
    'sign':'SIGN',
    'mode' : 'MODE',
    'owner' : 'OWNER',
    'constraint' : 'CONSTRAINT',
    'foreign' : 'FOREIGN',
    'references' : 'REFERENCES',
    'inherits' : 'INHERITS',
    'group' : 'GROUP',
    'having' : 'HAVING',
    'inner' : 'INNER',
    'outer' : 'OUTER',
    'trim_scale':'TRIM_SCALE',
    'trunc':'TRUNC',
    'width_bucket':'WIDTH_BUCKET',
    'random':'RANDOM',
    'setseed':'SETSEED',
    'acos':'ACOS',
    'acosd':'ACOSD',
    'asin':'ASIN',
    'asind':'ASIND',
    'atan':'ATAN',
    'atan2':'ATAN2',
    'cos':'COS',
    'cosd':'COSD',
    'cot':'COT',
    'cotd':'COTD',
    'sin':'SIN',
    'sind':'SIND',
    'tan':'TAN',
    'tand':'TAND',
    'atand':'ATAND',
    'atan2d':'ATAN2D',
    'sinh':'SINH',
    'cosh':'COSH',
    'tanh':'TANH',
    'asinh':'ASINH',
    'acosh':'ACOSH',
    'atanh':'ATANH',
    'length':'LENGTH',
    'substring':'SUBSTRING',
    'trim':'TRIM',
    'get_byte':'GET_BYTE',
    'md5':'MD5',
    'set_byte':'SET_BYTE',
    'sha256':'SHA256',
    'substr':'SUBSTR',
    'convert':'CONVERT',
    'encode':'ENCODE',
    'decode':'DECODE',
    'escape':'ESCAPE',
    'any':'ANY',
    'some':'SOME',
    'using':'USING',
    'first':'FIRST',
    'last':'LAST',
    'current_user':'CURRENT_USER',
    'session_user':'SESSION_USER',
    'symmetric':'SYMMETRIC',
    'left' : 'LEFT',
    'right' : 'RIGHT',
    'full' : 'FULL',
    'join' : 'JOIN',
    'natural' : 'NATURAL',
    'case' : 'CASE',
    'then' : 'THEN',
    'begin' : 'BEGIN',
    'end' : 'END',
    'else' : 'ELSE',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    'intersect' : 'INTERSECT',
    'except' : 'EXCEPT',
    #  tipos de datos permitidos
    'smallint' : 'SMALLINT',
    'integer' : 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'double' : 'DOUBLE',
    'precision' : 'PRECISION',
    'money' : 'MONEY',
    'varying' : 'VARYING',
    'varchar' : 'VARCHAR',
    'character' : 'CHARACTER',
    'char' : 'CHAR',
    'text' : 'TEXT',
    'boolean' : 'BOOLEAN',
    'timestamp':'TIMESTAMP',
    'time':'TIME',
    'date':'DATE',
    'interval':'INTERVAL',
    'year':'YEAR',
    'month':'MONTH',
    'day':'DAY',
    'hour':'HOUR',
    'minute':'MINUTE',
    'second':'SECOND',
    'to':'TO',
    'true':'TRUE',
    'false':'FALSE',
    'declare' : 'DECLARE',
    'function' : 'FUNCTION',
    'returns' : 'RETURNS',
    'returning':'RETURNING',
    'exec':'EXEC',
    'execute':'EXECUTE',
    'between' : 'BETWEEN',
    'ilike' : 'ILIKE',
    'is':'IS',
    'isnull':'ISNULL',
    'notnull':'NOTNULL',
    #enums
    'type':'TYPE',
    'ENUM':'ENUM',

    #para trim
    'leading':'LEADING',
    'trailing':'TRAILING',
    'both':'BOTH',
    'for':'FOR',
    'symmetric':'SYMMETRIC',
    'use' : 'USE',
    'now' : 'NOW',
    'extract' : 'EXTRACT',
    'date_part' : 'DATE_PART',
    'current_date' : 'CURRENT_DATE',
    'current_time' : 'CURRENT_TIME',
    # INDEX
    'index':'INDEX',
    'hash':'HASH',
    'perform' : 'PERFORM',

    'procedure' : 'PROCEDURE',
    'out' : 'OUT',
    'language' : 'LANGUAGE',
    'plpgsql' : 'PLPGSQL',
    'rowtype' : 'ROWTYPE',
    'alias' : 'ALIAS'
# revisar funciones de tiempo y fechas
}

# listado de tokens que manejara el lenguaje (solo la forma en la que los llamare  en las producciones)
tokens  = [
    'PUNTOYCOMA',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'DOSPUNTOS',
    'PUNTO',
    'TYPECAST',
    'CORCHETEIZQ',
    'CORCHETEDER',
    'POTENCIA',
    'RESIDUO',
    'MAYOR',
    'MENOR',
    'IGUAL',
    'MAYORIGUAL',
    'MENORIGUAL',
    'DIFERENTE',
    'IGUALIGUAL',
    'PARENTESISIZQUIERDA',
    'PARENTESISDERECHA',

    'COMA',
    'NOTEQUAL',
    'SIMBOLOOR',
    'SIMBOLOAND',
    'SIMBOLOAND2',
    'SIMBOLOOR2',
    'NUMERAL',
    'COLOCHO',
    'DESPLAZAMIENTODERECHA',
    'DESPLAZAMIENTOIZQUIERDA',
    'DOLAR',


#tokens que si devuelven valor
    'DECIMALTOKEN',
    'ENTERO',
    'CADENA',
    'ETIQUETA',
    'ID'
] + list(reservadas.values())

# Tokens y la forma en la que se usaran en el lenguaje
t_PUNTOYCOMA                            = r';'
t_MAS                                   = r'\+'
t_MENOS                                 = r'-'
t_POR                                   = r'\*'
t_DIV                                   = r'/'
t_DOSPUNTOS                             = r':'
t_PUNTO                                 = r'\.'
t_TYPECAST                              = r'::'
t_CORCHETEDER                           = r']'
t_CORCHETEIZQ                           = r'\['
t_POTENCIA                              = r'\^'
t_RESIDUO                               = r'%'
t_MAYOR                                 = r'<'
t_MENOR                                 = r'>'
t_IGUAL                                 = r'='
t_MAYORIGUAL                            = r'>='
t_MENORIGUAL                            = r'<='
t_DIFERENTE                             = r'<>'
t_IGUALIGUAL                            = r'=='
t_PARENTESISIZQUIERDA                   = r'\('
t_PARENTESISDERECHA                     = r'\)'
t_COMA                                  = r','
t_NOTEQUAL                              = r'!='
t_SIMBOLOOR                             = r'\|\|' #esto va a concatenar cadenas 
t_SIMBOLOAND                            = r'&&'
t_SIMBOLOAND2                           = r'\&'
t_SIMBOLOOR2                            = r'\|'
t_NUMERAL                               = r'\#' #REVISAR
t_COLOCHO                               = r'~'  #REVISAR
t_DESPLAZAMIENTODERECHA                 = r'>>'
t_DESPLAZAMIENTOIZQUIERDA               = r'<<'
t_DOLAR                                 = r'\$'


#definife la estructura de los decimales
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("El valor decimal es muy largo %d", t.value)
        t.value = 0
    return t
#definife la estructura de los enteros
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("El valor del entero es muy grande %d", t.value)
        t.value = 0
    return t

#definife la estructura de las cadenas
def t_CADENA(t):
    r'[\'|\"].*?[\'|\"]'
    t.value = t.value[1:-1] # quito las comillas del inicio y final de la cadena
    return t 


#definife la estructura de las etiquetas, por el momento las tomo unicamente como letras y numeros
def t_ETIQUETA(t):
     r'[a-zA-Z_]+[a-zA-Z0-9_]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     print("ALV:",t)
     print("ALV:",t.type)
     return t

# Comentario simple # ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1

def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n|)*?\*/'
    t.lexer.lineno += t.value.count("\n")
# ----------------------- Caracteres ignorados -----------------------
# caracter equivalente a un tab
t_ignore = " \t"
#caracter equivalente a salto de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    x=caden.splitlines()
    filas=len(x)-1
    print("filas que no cambian: ",filas) 
    if h.filapivote>0:
        fila=(t.lineno-1)-h.filapivote*filas
    else:
        fila=(t.lineno-1)
    h.filapivote+=1
    print("Caracter lexico no permitido ==> '%s'" % t.value)
    h.errores+=  "<tr><td>"+str(t.value[0])+"</td><td>"+str(fila)+"</td><td>"+str(find_column(caden,t))+"</td><td>LEXICO</td><td>token no pertenece al lenguaje</td></tr>\n"
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


# -----------------------------------------------------------------------------
#                       INICIA ANALIZADOR SINTACTICO
# -----------------------------------------------------------------------------

# Asociación de operadores y precedencia
precedence = (
    ('left','TYPECAST'),
    ('right','UMINUS'),
    ('right','UNOT'),
    ('left','MAS','MENOS'),
    ('left','POTENCIA'),
    ('left','POR','DIV','RESIDUO'),
    ('left','AND','OR','SIMBOLOOR2','SIMBOLOOR','SIMBOLOAND2'),
    ('left','DESPLAZAMIENTOIZQUIERDA','DESPLAZAMIENTODERECHA'),
    )

#IMPORTACION DE CLASES ALTERNAS
import reportes as h





# estructura de mi gramatica
#-----------------------------------------------------INICIO--------------------------------------------------------------------
def p_inicio_1(t) :
    'inicio               : queries' 
    h.reporteGramatical1 +="inicio     ::=      queries \n"
    t[0]=t[1]
    p=t[0]
    h.insertarSimbolos(p)
    
def p_queries_1(t) :
    'queries               : queries query'
    h.reporteGramatical1 +="queries     ::=      queries query\n"
    t[1].append(t[2])
    t[0]=t[1]

def p_queries_2(t) :
    'queries               : query'    
    h.reporteGramatical1 +="queries     ::=      query\n"
    t[0]=[t[1]]
 
#-----------------------------------------------------LISTA DE FUNCIONES--------------------------------------------------------------------

def p_query(t):
    '''query        : mostrarBD
                    | crearBD
                    | alterBD
                    | dropBD
                    | useBD
                    | operacion
                    | insertinBD
                    | updateinBD
                    | deleteinBD
                    | createTable
                    | inheritsBD
                    | dropTable
                    | alterTable
                    | variantesAt
                    | contAdd
                    | contDrop
                    | contAlter                    
                    | selectData PUNTOYCOMA
                    | tipos
                    | createIndex
                    | alterIndex
                    | dropIndex
                    | combinacionSelects PUNTOYCOMA
                    | execFunction
    '''
    h.reporteGramatical1 +="query     ::=      opcion\n"
    h.reporteGramatical2 +="t[0]=t[1]\n"
    t[0]=t[1]
 
                    # derivando cada produccion a cosas como el create, insert, select; funciones como avg, sum, substring irian como otra produccion 
                    #dentro del select (consulta)


# empiezan las producciones de las operaciones finales
#la englobacion de las operaciones
#-----------------------------------------------------CREATE INDEX--------------------------------------------------------------------
def p_createIndex(t):
    'createIndex    : CREATE INDEX ID ON ID PARENTESISIZQUIERDA listaid PARENTESISDERECHA PUNTOYCOMA'
    h.reporteGramatical1 +="createIndex    ::=        CREATE INDEX ID ON ID PARENTESISIZQUIERDA listaid PARENTESISDERECHA PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateIndex(INDEX,t[3],t[5],t[7]) \n"
    t[0] = CreateIndex("INDEX",t[3],t[5],t[7])

def p_createIndex_5(t):
    'createIndex    : CREATE INDEX ID ON ID PARENTESISIZQUIERDA lower PARENTESISDERECHA PUNTOYCOMA'
    h.reporteGramatical1 +="createIndex    ::=        CREATE INDEX ID ON ID PARENTESISIZQUIERDA listaid PARENTESISDERECHA PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateIndex(t[3],t[5],t[7]) \n"
    t[0] = CreateIndexLow("INDEX",t[3],t[5],t[7])  

def p_createIndex_1_1(t):
    'createIndex    : CREATE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA PUNTOYCOMA'
    h.reporteGramatical1 +="createIndex    ::=        CREATE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateIndexParams(INDEX,t[3],t[5],t[7],t[8])\n"
    t[0] = CreateIndexParams("INDEX",t[3],t[5],t[7],t[8])

def p_createIndex_1_2(t):
    'createIndex    : CREATE INDEX ID ON ID PARENTESISIZQUIERDA listaid PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA'
    h.reporteGramatical1 +="createIndex    ::=        CREATE INDEX ID ON ID PARENTESISIZQUIERDA listaid PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateIndexWhere(INDEX,t[3],t[5],t[7],t[10])\n"
    t[0] = CreateIndexWhere("INDEX",t[3],t[5],t[7],t[10]) 

def p_createIndex_1_1_2(t):
    'createIndex    : CREATE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA WHERE whereOptions  PUNTOYCOMA'
    h.reporteGramatical1 +="createIndex    ::=        CREATE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateIndexParamsWhere(INDEX,t[3],t[5],t[7],t[8],t[11]) \n"
    t[0] = CreateIndexParamsWhere("INDEX",t[3],t[5],t[7],t[8],t[11]) 

def p_createIndex_2(t):
    'createIndex    : CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA listaid PARENTESISDERECHA PUNTOYCOMA'
    h.reporteGramatical1 +="createIndex    ::=        CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA listaid PARENTESISDERECHA PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = t[0] = CreateIndex(INDEX USING HASHt[3],t[5],t[9]) \n"
    t[0] = CreateIndex("INDEX USING HASH",t[3],t[5],t[9]) 

def p_createIndex_2_1(t):
    'createIndex    : CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA PUNTOYCOMA'
    h.reporteGramatical1 +="createIndex    ::=        CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateIndexParams(INDEX USING HASH,t[3],t[5],t[9],t[10])\n"
    t[0] = CreateIndexParams("INDEX USING HASH",t[3],t[5],t[9],t[10])

def p_createIndex_2_2(t):
    'createIndex    : CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA listaid PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA'
    h.reporteGramatical1 +="createIndex    ::=        CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA listaid PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateIndexWhere(INDEX USING HASH,t[3],t[5],t[9],t[12])\n"
    t[0] = CreateIndexWhere("INDEX USING HASH",t[3],t[5],t[9],t[12]) 

def p_createIndex_2_1_2(t):
    'createIndex    : CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA'
    h.reporteGramatical1 +="createIndex    ::=        CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateIndexParamsWhere(INDEX USING HASH,t[3],t[5],t[9],t[10],t[13])\n"
    t[0] = CreateIndexParamsWhere("INDEX USING HASH",t[3],t[5],t[9],t[10],t[13]) 

def p_createIndex_3(t):
    'createIndex    : CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA listaid PARENTESISDERECHA PUNTOYCOMA'
    h.reporteGramatical1 +="createIndex    ::=        CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA listaid PARENTESISDERECHA PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = t[0] = CreateIndex(UNIQUE,t[4],t[6],t[8]\n"
    t[0] = CreateIndex("UNIQUE",t[4],t[6],t[8]) 

def p_createIndex_3_1(t):
    'createIndex    : CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA PUNTOYCOMA'
    h.reporteGramatical1 +="createIndex    ::=        CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateIndexParams(UNIQUE,t[4],t[6],t[8],t[9])\n"
    t[0] = CreateIndexParams("UNIQUE",t[4],t[6],t[8],t[9])

def p_createIndex_3_2(t):
    'createIndex    : CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA listaid PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA'
    h.reporteGramatical1 +="createIndex    ::=        CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA listaid PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateIndexWhere(UNIQUE,t[4],t[6],t[8],t[11])\n"
    t[0] = CreateIndexWhere("UNIQUE",t[4],t[6],t[8],t[11]) 

def p_createIndex_3_1_2(t):
    'createIndex    : CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA'
    h.reporteGramatical1 +="createIndex    ::=        CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateIndexParamsWhere(UNIQUE,t[4],t[6],t[8],t[9],t[12])\n"
    t[0] = CreateIndexParamsWhere("UNIQUE",t[4],t[6],t[8],t[9],t[12])
# -------------------------------------------------------------DROP INDEX--------------------------------------------------------
def p_dropIndex(t):
    'dropIndex    : DROP INDEX ID PUNTOYCOMA'
    h.reporteGramatical1 +="dropIndex    ::=        DROP INDEX ID PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = DropIndex(t[3]) \n"
    t[0] = DropIndex(t[3])

def p_dropIndex_1(t):
    'dropIndex    : DROP INDEX IF EXISTS ID PUNTOYCOMA'
    h.reporteGramatical1 +="dropIndex    ::=        DROP INDEX IF EXISTS ID PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = DropIndex(t[5]) \n"
    t[0] = DropIndex(t[5])  
# ------------------------------------------------------------ALTER INDEX---------------------------------------------------------
def p_alterIndex(t):
    'alterIndex    : ALTER INDEX ID RENAME TO ID PUNTOYCOMA'
    h.reporteGramatical1 +="alterIndex    ::=        ALTER INDEX ID RENAME TO ID PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = AlterIndex(t[3],t[6]) \n"
    t[0] = AlterIndex(t[3],t[6])

def p_alterIndex_1(t):
    'alterIndex    : ALTER INDEX IF EXISTS ID RENAME TO ID PUNTOYCOMA'
    h.reporteGramatical1 +="alterIndex    ::=        ALTER INDEX IF EXISTS ID RENAME TO ID PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = AlterIndex(t[5],t[8]) \n"
    t[0] = AlterIndex(t[5],t[8]) 
# ------------------------------------------------------ALTER INDEX COLUMN ----------------------------------------------------
def p_alterIndex_2(t):
    'alterIndex    : ALTER INDEX ID ALTER final PUNTOYCOMA'
    h.reporteGramatical1 +="alterIndex    ::=        ALTER INDEX ID ALTER final PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = AlterIndex(t[5],t[8]) \n"
    t[0] = AlterColumnIndex(t[3],t[5])  

def p_alterIndex_3(t):
    'alterIndex    : ALTER INDEX ID ALTER COLUMN final PUNTOYCOMA'
    h.reporteGramatical1 +="alterIndex    ::=        ALTER INDEX ID ALTER COLUMN final PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = AlterIndex(t[5],t[8]) \n"
    t[0] = AlterColumnIndex(t[3],t[6])

def p_alterIndex_4(t):
    'alterIndex    : ALTER INDEX IF EXISTS ID ALTER final PUNTOYCOMA'
    h.reporteGramatical1 +="alterIndex    ::=        ALTER INDEX IF EXISTS ID ALTER final PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = AlterIndex(t[5],t[8]) \n"
    t[0] = AlterColumnIndex(t[5],t[7])  

def p_alterIndex_5(t):
    'alterIndex    : ALTER INDEX IF EXISTS ID ALTER COLUMN final PUNTOYCOMA'
    h.reporteGramatical1 +="alterIndex    ::=        ALTER INDEX IF EXISTS ID ALTER COLUMN final PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = AlterIndex(t[5],t[8]) \n"
    t[0] = AlterColumnIndex(t[5],t[8])     
# --------------------------------------------------------------------------------------------------------------------------------
def p_indexParams(t):
    'indexParams    : sort'
    h.reporteGramatical1 +="indexParams    ::=        sort\n"
    h.reporteGramatical2 +="t[0] = t[1]\n"
    t[0] = t[1]

def p_whereOptions_1(t):
    'whereOptions    : asignaciones'
    h.reporteGramatical1 +="whereOptions    ::=        asignaciones\n"
    h.reporteGramatical2 +="t[0] = t[1]\n"
    t[0] = t[1]

def p_whereOptions_2(t):
    'whereOptions    : operacion'
    h.reporteGramatical1 +="whereOptions    ::=        operacion\n"
    h.reporteGramatical2 +="t[0] = t[1]\n"
    t[0] = t[1]

def p_whereOptions_3(t):
    'whereOptions    : search_condition'
    h.reporteGramatical1 +="whereOptions    ::=        search_condition\n"
    h.reporteGramatical2 +="t[0] = t[1]\n"
    t[0] = t[1]

def p_sortOptions_1(t):
    'sort    : NULLS FIRST'
    h.reporteGramatical1 +="sort    ::=        NULLS FIRST\n"
    h.reporteGramatical2 +="t[0] = t[2]\n"
    t[0] = t[2]

def p_sortOptions_1_1(t):
    'sort    : DESC NULLS FIRST'
    h.reporteGramatical1 +="sort    ::=        DESC NULLS FIRST\n"
    h.reporteGramatical2 +="t[0] = t[3]\n"
    t[0] = SortOptions(t[1],t[3])

def p_sortOptions_1_2(t):
    'sort    : ASC NULLS FIRST'
    h.reporteGramatical1 +="sort    ::=        ASC NULLS FIRST\n"
    h.reporteGramatical2 +="t[0] = t[3]\n"
    t[0] = SortOptions(t[1],t[3])

def p_sortOptions_2(t):
    'sort    : NULLS LAST'
    h.reporteGramatical1 +="sort    ::=        NULLS LAST\n"
    h.reporteGramatical2 +="t[0] = t[2]\n"
    t[0] = t[2]

def p_sortOptions_2_1(t):
    'sort    : DESC NULLS LAST'
    h.reporteGramatical1 +="sort    ::=        DESC NULLS LAST\n"
    h.reporteGramatical2 +="t[0] = t[3]\n"
    t[0] = SortOptions(t[1],t[3])

def p_sortOptions_2_2(t):
    'sort    : ASC NULLS LAST'
    h.reporteGramatical1 +="sort    ::=        ASC NULLS LAST\n"
    h.reporteGramatical2 +="t[0] = t[3]\n"
    t[0] = SortOptions(t[1],t[3])

def p_lower(t):
    'lower    : ID PARENTESISIZQUIERDA ID PARENTESISDERECHA'
    h.reporteGramatical1 +="sort    ::=        ASC NULLS LAST\n"
    h.reporteGramatical2 +="t[0] = t[3]\n"
    t[0] = SortOptions(t[1],t[3])
#-----------------------------------------------------CREATE DB--------------------------------------------------------------------

def p_crearBaseDatos_1(t):
    'crearBD    : CREATE DATABASE ID PUNTOYCOMA'
    h.reporteGramatical1 +="crearBD    ::=        CREATE DATABASE ID PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateDatabases(t[3])\n"
    t[0] = CreateDatabases(t[3])

def p_crearBaseDatos_2(t):
    'crearBD    : CREATE DATABASE IF NOT EXISTS ID PUNTOYCOMA'
    h.reporteGramatical1 +="crearBD    ::=        CREATE DATABASE IF NOT EXISTS ID PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = Create_IF_Databases(t[3],t[6])\n"
    t[0] = Create_IF_Databases(t[3],t[6])

def p_crear_replace_BaseDatos_1(t):
    'crearBD    : CREATE OR REPLACE DATABASE ID PUNTOYCOMA'
    h.reporteGramatical1 +="crearBD    ::=        CREATE OR REPLACE DATABASE ID PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateDatabases(t[5])\n"
    t[0] = Create_Replace_Databases(t[3],t[5])

def p_crear_replace_BaseDatos_2(t):
    'crearBD    : CREATE OR REPLACE DATABASE IF NOT EXISTS ID PUNTOYCOMA'
    h.reporteGramatical1 +="crearBD    ::=        CREATE OR REPLACE DATABASE ID PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateDatabases(t[5])\n"
    t[0] = Create_Replace_IF_Databases(t[3],t[5],t[8])

def p_crear_param_BaseDatos_1(t):
    'crearBD    : CREATE  DATABASE ID parametrosCrearBD PUNTOYCOMA'
    h.reporteGramatical1 +="crearBD    ::=        CREATE  DATABASE ID parametrosCrearBD PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateDatabaseswithParameters(t[3],t[4])\n"
    t[0] = CreateDatabaseswithParameters(t[3],t[4])

def p_crear_param_BaseDatos_2(t):
    'crearBD    : CREATE  DATABASE IF NOT EXISTS ID parametrosCrearBD PUNTOYCOMA'
    h.reporteGramatical1 +="crearBD    ::=        CREATE  DATABASE ID parametrosCrearBD PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateDatabaseswithParameters(t[3],t[4])\n"
    t[0] = Create_Databases_IFwithParameters(t[3],t[6],t[7])

def p_crear_replace_param_BaseDatos_1(t):
    'crearBD    : CREATE OR REPLACE DATABASE ID parametrosCrearBD PUNTOYCOMA'
    h.reporteGramatical1 +="crearBD    ::=        CREATE OR REPLACE DATABASE ID parametrosCrearBD PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateDatabaseswithParameters(t[5],t[6])\n"
    t[0] = Create_Replace_DatabaseswithParameters(t[3],t[5],t[6])

def p_crear_replace_param_BaseDatos_2(t):
    'crearBD    : CREATE OR REPLACE DATABASE IF NOT EXISTS ID parametrosCrearBD PUNTOYCOMA'
    h.reporteGramatical1 +="crearBD    ::=        CREATE OR REPLACE DATABASE ID parametrosCrearBD PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateDatabaseswithParameters(t[5],t[6])\n"
    t[0] = Create_Replace_Databases_IFwithParameters(t[3],t[5],t[8],t[9])

def p_parametrosCrearBD_1(t):
    'parametrosCrearBD : parametrosCrearBD parametroCrearBD'
    h.reporteGramatical1 +="parametrosCrearBD    ::=        parametrosCrearBD parametroCrearBD\n"
    h.reporteGramatical2 +="t[1].append(t[2])\n t[0]=t[1]\n"
    t[1].append(t[2])
    t[0]=t[1]

def p_parametrosCrearBD_2(t):
    'parametrosCrearBD :  parametroCrearBD'
    h.reporteGramatical1 +="parametrosCrearBD    ::=        parametroCrearBD\n"
    h.reporteGramatical2 +="t[0]=[t[1]]\n"
    t[0]=[t[1]]

def p_parametroCrearBD(t):
    '''parametroCrearBD :  OWNER IGUAL final
                        |  MODE IGUAL final
    '''
    h.reporteGramatical1 +="parametroCrearBD    ::=        "+str(t[1])+"   IGUAL  "+str(t[3])+"\n"
    
    if t[1] == "OWNER":
        h.reporteGramatical2 +="t[0]=ExpresionOwner(t[1],t[3])\n"
        t[0]=ExpresionOwner(t[1],t[3])
    elif t[1] == "MODE":
        h.reporteGramatical2 +="t[0]=ExpresionMode(t[1],t[3])\n"
        t[0]=ExpresionMode(t[1],t[3])
#-----------------------------------------------------SHOW DB--------------------------------------------------------------------
def p_mostrarBD(t):
    'mostrarBD  : SHOW DATABASES PUNTOYCOMA'
    h.reporteGramatical1 +="mostrarBD    ::=        SHOW DATABASES PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0]=ShowDatabases(1)\n"
    t[0]=ShowDatabases(1)

def p_usarBaseDatos(t):
    'useBD    : USE ID PUNTOYCOMA'
    h.reporteGramatical1 +="useBD    ::=        USE ID PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0]=UseDatabases(t[2])\n"
    t[0]=UseDatabases(t[2])
    print("t[0]:",t[0])
#-----------------------------------------------------ALTER BD--------------------------------------------------------------------
def p_alterBD_1(t):
    'alterBD    : ALTER DATABASE ID RENAME TO ID PUNTOYCOMA'
    h.reporteGramatical1 +="alterBD    ::=       ALTER DATABASE "+str(t[3])+" RENAME TO "+str(t[6])+" PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = AlterDB(t[3],t[6])\n"
    t[0] = AlterDB(t[3],t[6])

def p_alterBD_2(t):
    'alterBD    : ALTER DATABASE ID OWNER TO parametroAlterUser PUNTOYCOMA'
    h.reporteGramatical1 +="alterBD    ::=       ALTER DATABASE "+str(t[3])+" OWNER TO "+str(t[6])+" PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = AlterOwner(t[3],t[4],t[6])\n"
    t[0] = AlterOwner(t[3],t[4],t[6])

def p_parametroAlterUser(t):
   
    '''parametroAlterUser : CURRENT_USER
                        |   SESSION_USER
                        |   final
    '''
    h.reporteGramatical1 +="parametroAlterUser    ::=        "+str(t[1])+" \n"
    h.reporteGramatical2 +="t[0] = t[1]\n"
    t[0] = t[1]
#-----------------------------------------------------DROP TABLE-----------------------------------------------------------------
def p_dropTable(t) :
    'dropTable  : DROP TABLE ID PUNTOYCOMA'
    h.reporteGramatical1 +="dropTable    ::=        DROP TABLE ID PUNTOYCOMA\n"
    t[0]=DropTable(t[3])
#-----------------------------------------------------ALTER TABLE-----------------------------------------------------------------
def p_alterTable(t):
    '''
    alterTable  : ALTER TABLE ID variantesAt PUNTOYCOMA

    '''
    h.reporteGramatical1 +="alterTable    ::=        ALTER TABLE ID variantesAt PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = AlterTable(t[3],t[4])"
    t[0] = AlterTable(t[3],t[4])

#---------------------------------------------------TIPOS------------------------------------------------------------------------
def p_variantesAt(t):
    '''
    variantesAt :   ADD contAdd
                |   ALTER contAlter
                |   DROP contDrop
    '''
    if t[1].upper()=="ADD": 
        h.reporteGramatical1 +="variantesAt    ::=        ADD contAdd\n"
        h.reporteGramatical2 +="t[0]=VariantesAt(t[1],t[2])"  
        t[0]=VariantesAt(t[1],t[2])
    elif t[1].upper()=="ALTER":
        h.reporteGramatical1 +="variantesAt    ::=        ALTER listaContAlter\n"
        h.reporteGramatical2 +="t[0]=VariantesAt(t[1],t[2])"
        t[0]=VariantesAt(t[1],t[2])
    elif t[1].upper()=="DROP":
        h.reporteGramatical1 +="variantesAt    ::=         DROP contDrop\n"
        h.reporteGramatical2 +="t[0]=VariantesAt(t[1],t[2])"
        t[0]=VariantesAt(t[1],t[2])
    
# SE SEPARO LA LISTA PARA PODER MANIPULAR DATOS
def p_listaContAlter(t):
    '''
    listaContAlter  : listaContAlter COMA contAlter 
    '''
    h.reporteGramatical1 +="listaContAlter    ::=         listaContAlter COMA contAlter\n"

def p_listaContAlter_2(t):
    '''
    listaContAlter  : contAlter
    '''
    h.reporteGramatical1 +="listaContAlter    ::=         contAlter\n"


def p_contAlter(t):
    '''
    contAlter   : COLUMN ID SET NOT NULL 
                | COLUMN ID TYPE tipo
    '''
    if t[3].upper()=="SET":
        h.reporteGramatical1 +="contAlter    ::=         COLUMN ID   SET  NOT NULL\n"
        h.reporteGramatical2 +="t[0]=contAlter(t[2],t[3],t[4])"
        t[0]=contAlter(t[2],t[3],t[4])
    elif t[3].upper()=="TYPE":
        h.reporteGramatical1 +="contAlter    ::=         COLUMN ID  TYPE  tipo\n"
        h.reporteGramatical2 +="t[0]=contAlter(t[2],t[3],t[4])"
        t[0]=contAlter(t[2],t[3],t[4])


def p_contAdd(t):
    '''
    contAdd     :   COLUMN ID tipo 
                |   CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                |   FOREIGN KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA REFERENCES ID 
                |   PRIMARY KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA
                |   CONSTRAINT ID FOREIGN KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA REFERENCES ID PARENTESISIZQUIERDA ID PARENTESISDERECHA
                |   CONSTRAINT ID PRIMARY KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA
                |   CONSTRAINT ID UNIQUE PARENTESISIZQUIERDA ID PARENTESISDERECHA
    '''
    if t[1].upper()=="COLUMN":
        h.reporteGramatical1 +="contAdd    ::=         COLUMN ID tipo\n"
        h.reporteGramatical2 +="t[0]=contAdd(t[1],t[3],t[2],None,None,None,None)"
        t[0]=contAdd(t[1],t[3],t[2],None,None,None,None)
    elif t[1].upper()=="CHECK":
        h.reporteGramatical1 +="contAdd    ::=         CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=contAdd(t[1],None,None,None,None,None,t[3])"
        t[0]=contAdd(t[1],None,None,None,None,None,t[3])
    elif t[1].upper()=="FOREIGN":
        h.reporteGramatical1 +="contAdd    ::=        FOREIGN KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA REFERENCES ID\n"
        h.reporteGramatical2 +="t[0]=contAdd(t[1],None,t[4],t[7],None,None,None)"
        t[0]=contAdd(t[1],None,t[4],t[7],None,None,None)
    elif t[1].upper()=="PRIMARY":
        h.reporteGramatical1 +="contAdd    ::=        PRIMARY KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=contAdd(t[1],None,t[4],None,None,None,None)"
        t[0]=contAdd(t[1],None,t[4],None,None,None,None)
    elif t[1].upper()=="CONSTRAINT":
        if t[3].upper()=="PRIMARY":
            h.reporteGramatical1 +="contAdd     ::= CONSTRAINT ID PRIMARY KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA\n"
            h.reporteGramatical2 +="t[0]=contAdd(t[1],t[3],t[2],t[6],None,None,None)"
            t[0]=contAdd(t[1],t[3],t[2],t[6],None,None,None)
        elif t[3].upper()=="FOREIGN":
            h.reporteGramatical1 +="contAdd     ::= CONSTRAINT ID FOREIGN KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA REFERENCES ID PARENTESISIZQUIERDA ID PARENTESISDERECHA\n"
            h.reporteGramatical2 +="t[0]=contAdd(t[1],t[3],t[2],t[6],t[9],t[11],None)"
            t[0]=contAdd(t[1],t[3],t[2],t[6],t[9],t[11],None)
        else:
            h.reporteGramatical1 +="contAdd    ::=         CONSTRAINT ID UNIQUE PARENTESISIZQUIERDA ID PARENTESISDERECHA\n"
            h.reporteGramatical2 +="t[0]=contAdd(t[1],None,t[2],None,None,None,t[5])"
            t[0]=contAdd(t[1],t[3],t[2],None,None,None,t[5])


def p_contDrop(t):
    '''
    contDrop    : COLUMN ID 
                | CONSTRAINT ID
                | PRIMARY KEY
    '''
    if t[1].upper()=="COLUMN":
        h.reporteGramatical1 +="contDrop    ::=         COLUMN ID \n"
        h.reporteGramatical2 +="t[0]=contDrop(t[1],t[2])"
        t[0]=contDrop(t[1],t[2])
    elif t[1].upper()=="CONSTRAINT":
        h.reporteGramatical1 +="contDrop    ::=         CONSTRAINT ID\n"
        h.reporteGramatical2 +="t[0]=contDrop(t[1],t[2])"
        t[0]=contDrop(t[1],t[2])
    elif t[1].upper()=="PRIMARY":
        h.reporteGramatical1 +="contDrop    ::=         PRIMARY KEY\n"
        h.reporteGramatical2 +="t[0]=contDrop(t[1],None)"
        t[0]=contDrop(t[1],None)
# SE SEPARO LA LISTA PARA PODER MANIPULAR DATOS
def p_listaID(t):
    '''
    listaid     :   listaid COMA final
    '''
    h.reporteGramatical1 +="listaid    ::=         listaid COMA final\n"
    h.reporteGramatical2 +="t[1].append(t[3])\nt[0]=t[1]\n"
    t[1].append(t[3])
    t[0]=t[1]

def p_listaID_2(t):
    '''
    listaid     :   final
    '''
    h.reporteGramatical1 +="listaid    ::=          final\n"
    h.reporteGramatical2 +="t[0]=[t[1]]"
    t[0]=[t[1]]
    
#-----------------------------------------------------DROP BD--------------------------------------------------------------------


def p_dropBD_1(t):
    'dropBD    : DROP DATABASE ID PUNTOYCOMA'
    h.reporteGramatical1 +="dropBD    ::=        DROP DATABASE  "+str(t[3])+" PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0]= DropDB(t[3])\n"
    t[0]= DropDB(t[3])


def p_dropBD_2(t):
    'dropBD    : DROP DATABASE IF EXISTS ID PUNTOYCOMA'
    h.reporteGramatical1 +="dropBD    ::=        DROP DATABASE IF EXISTS  "+str(t[5])+" PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0]= DropDBIF(t[3],t[5])\n"
    t[0]= DropDBIF(t[3],t[5])
#-----------------------------------------------------OPERACIONES Y EXPRESIONES--------------------------------------------------------------------
def p_operacion(t):
    '''operacion          : operacion MAS operacion
                          | operacion MENOS operacion
                          | operacion POR operacion
                          | operacion DIV operacion
                          | operacion RESIDUO operacion
                          | operacion POTENCIA operacion
                          | operacion AND operacion
                          | operacion OR operacion
                          | operacion SIMBOLOOR2 operacion
                          | operacion SIMBOLOOR operacion
                          | operacion SIMBOLOAND2 operacion
                          | operacion DESPLAZAMIENTOIZQUIERDA operacion
                          | operacion DESPLAZAMIENTODERECHA operacion
                          | operacion IGUAL operacion
                          | operacion IGUALIGUAL operacion
                          | operacion NOTEQUAL operacion
                          | operacion MAYORIGUAL operacion
                          | operacion MENORIGUAL operacion
                          | operacion MAYOR operacion
                          | operacion MENOR operacion
                          | operacion DIFERENTE operacion
                          | PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                          | PARENTESISIZQUIERDA listaid PARENTESISDERECHA                             
                          '''
# --------------------------------------------------------------------------------------------------------------                          
    if t[2]=='+':
        h.reporteGramatical1 +="operacion    ::=       operacion MAS operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionAritmetica(t[1],t[3],OPERACION_ARITMETICA.MAS)\n"
        t[0]=ExpresionAritmetica(t[1],t[3],OPERACION_ARITMETICA.MAS)
# --------------------------------------------------------------------------------------------------------------                                  
    elif t[2]=='-':
        h.reporteGramatical1 +="operacion    ::=       operacion MENOS operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionAritmetica(t[1],t[3],OPERACION_ARITMETICA.MENOS)\n"
        t[0]=ExpresionAritmetica(t[1],t[3],OPERACION_ARITMETICA.MENOS)
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='*':
        h.reporteGramatical1 +="operacion    ::=       operacion POR operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionAritmetica(t[1],t[3],OPERACION_ARITMETICA.POR)\n"
        t[0]=ExpresionAritmetica(t[1],t[3],OPERACION_ARITMETICA.POR)
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='/':
        h.reporteGramatical1 +="operacion    ::=      operacion DIV operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionAritmetica(t[1],t[3],OPERACION_ARITMETICA.DIVIDIDO)\n"
        t[0]=ExpresionAritmetica(t[1],t[3],OPERACION_ARITMETICA.DIVIDIDO)
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='%':
        h.reporteGramatical1 +="operacion    ::=      operacion RESIDUO operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionAritmetica(t[1],t[3],OPERACION_ARITMETICA.MODULO)\n"
        t[0]=ExpresionAritmetica(t[1],t[3],OPERACION_ARITMETICA.MODULO)
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='^':
        print("entra a la potencia")
        h.reporteGramatical1 +="operacion    ::=      operacion POTENCIA operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionAritmetica(t[1],t[3],OPERACION_ARITMETICA.POTENCIA)\n"
        t[0]=ExpresionAritmetica(t[1],t[3],OPERACION_ARITMETICA.POTENCIA)
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=="AND":
        h.reporteGramatical1 +="operacion    ::=      operacion AND operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionLogica(t[1],t[3],OPERACION_LOGICA.AND)\n"
        t[0]=ExpresionLogica(t[1],t[3],OPERACION_LOGICA.AND)
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=="OR":
        h.reporteGramatical1 +="operacion    ::=      operacion OR operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionLogica(t[1],t[3],OPERACION_LOGICA.OR)\n"
        t[0]=ExpresionLogica(t[1],t[3],OPERACION_LOGICA.OR)
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='|':
        h.reporteGramatical1 +="operacion    ::=      operacion | operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionLogica(t[1],t[3],OPERACION_LOGICA.OR)\n"
        t[0]=ExpresionLogica(t[1],t[3],OPERACION_LOGICA.OR)
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='||':
        h.reporteGramatical1 +="operacion    ::=      operacion || operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionLogica(t[1],t[3],OPERACION_LOGICA.OR)\n"
        t[0]=ExpresionLogica(t[1],t[3],OPERACION_LOGICA.OR)
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='&':
        h.reporteGramatical1 +="operacion    ::=      operacion & operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionLogica(t[1],t[3],OPERACION_LOGICA.AND)\n"
        t[0]=ExpresionLogica(t[1],t[3],OPERACION_LOGICA.AND)
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='<<':
        print(t[2])
        h.reporteGramatical1 +="operacion    ::=      operacion DESPLAZAMIENTOIZQUIERDA operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionBIT(t[1],t[3],OPERACION_BIT.DESPLAZAMIENTO_IZQUIERDA)\n"
        t[0]=ExpresionBIT(t[1],t[3],OPERACION_BIT.DESPLAZAMIENTO_IZQUIERDA)
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='>>':
        h.reporteGramatical1 +="operacion    ::=      operacion DESPLAZAMIENTODERECHA operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionBIT(t[1],t[3],OPERACION_BIT.DESPLAZAMIENTO_DERECHA)\n"
        t[0]=ExpresionBIT(t[1],t[3],OPERACION_BIT.DESPLAZAMIENTO_DERECHA)
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='=':
        t[0]=ExpresionIgualdad(t[1],t[3])
        #t[0]=operacionDelete(t[1],t[3],t[2])
        h.reporteGramatical1 +="operacion    ::=      operacion IGUAL operacion\n"
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='==':
        h.reporteGramatical1 +="operacion    ::=      operacion IGUALIGUAL operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.IGUAL_IGUAL)\n"
        t[0]=ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.IGUAL_IGUAL)
# --------------------------------------------------------------------------------------------------------------                            
    elif t[2]=='!=':
        h.reporteGramatical1 +="operacion    ::=      operacion NOTEQUAL operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.NO_IGUAL)\n"
        t[0]=ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.NO_IGUAL)
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='>=':
        h.reporteGramatical1 +="operacion    ::=      operacion MAYORIGUAL operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MAYOR_IGUAL)\n"
        t[0]=ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MAYOR_IGUAL)
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='<=':
        h.reporteGramatical1 +="operacion    ::=      operacion MENORIGUAL operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MENOR_IGUAL)\n"
        t[0]=ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MENOR_IGUAL)
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='>':
        h.reporteGramatical1 +="operacion    ::=      operacion MAYOR operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MAYOR)\n"
        t[0]=ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MAYOR)
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='<':
        h.reporteGramatical1 +="operacion    ::=      operacion MENOR operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MENOR)\n"
        t[0]=ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MENOR)
# --------------------------------------------------------------------------------------------------------------                                  
    elif t[2]=='<>':
        h.reporteGramatical1 +="operacion    ::=      operacion DIFERENTE operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.DIFERENTE)\n"
        t[0]=ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.DIFERENTE)
# --------------------------------------------------------------------------------------------------------------                          
    else:
        h.reporteGramatical1 +="operacion    ::=      PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        t[0]=t[2]
# --------------------------------------------------------------------------------------------------------------                              
def p_operacion_menos_unario(t):
    '''operacion : MENOS ENTERO  %prec UMINUS
                | MENOS DECIMAL  %prec UMINUS
    
    ''' 
    h.reporteGramatical1 +="operacion    ::=      MENOS operacion  %prec UMINUS\n"
    h.reporteGramatical2 +="t[0]=ExpresionNegativo(t[2])\n"
    t[0]=ExpresionNegativo(t[2]) 
# --------------------------------------------------------------------------------------------------------------                          
def p_operacion_not_unario(t):
    'operacion : NOT operacion %prec UNOT'
    h.reporteGramatical1 +="operacion    ::=      NOT operacion  %prec UNOT\n"
    h.reporteGramatical2 +="t[0]=ExpresionNOT(t[2])\n"
    t[0]=ExpresionNOT(t[2])
# --------------------------------------------------------------------------------------------------------------                          
def p_operacion_funcion(t):
    'operacion  : funcionBasica'
    h.reporteGramatical1 +="operacion    ::=      funcionBasica\n"
    h.reporteGramatical2 +="t[0]=t[1]\n"
    t[0]=t[1]
# --------------------------------------------------------------------------------------------------------------                          
def p_operacion_final(t):
    'operacion :     final'
    t[0] = t[1]
    h.reporteGramatical1 +="operacion    ::=      final\n"
    h.reporteGramatical2 +="t[0]=t[1]\n"
    t[0]=t[1]
#-----------------------------------------------------FUNCIONES MATEMATICAS--------------------------------------------------------------------
def p_funcion_basica(t):
    '''funcionBasica    : ABS PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | CBRT PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | CEIL PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | CEILING PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | DEGREES PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | DIV PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | EXP PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | FACTORIAL PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | FLOOR PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | GCD PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | LCM PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | LN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | LOG PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | MOD PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | PI PARENTESISIZQUIERDA  PARENTESISDERECHA
                        | POWER PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | RADIANS PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA                      
                        | SIGN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SQRT PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TRIM_SCALE PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TRUNC  PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | WIDTH_BUCKET PARENTESISIZQUIERDA operacion COMA operacion COMA operacion COMA operacion PARENTESISDERECHA
                        | RANDOM PARENTESISIZQUIERDA PARENTESISDERECHA
                        
                        
                        | ACOS  PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ACOSD PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ASIN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ASIND PARENTESISIZQUIERDA operacion PARENTESISDERECHA                
                        | ATAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ATAND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ATAN2 PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | ATAN2D PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        

                        | COS PARENTESISIZQUIERDA operacion PARENTESISDERECHA
			            | COSD  PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | COT PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | COTD PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SIN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SIND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TAND  PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SINH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | GREATEST PARENTESISIZQUIERDA select_list PARENTESISDERECHA
                        | LEAST PARENTESISIZQUIERDA select_list PARENTESISDERECHA
                        | NOW PARENTESISIZQUIERDA  PARENTESISDERECHA


                        | COSH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TANH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ASINH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ACOSH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ATANH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | LENGTH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TRIM PARENTESISIZQUIERDA opcionTrim operacion FROM operacion PARENTESISDERECHA
                        | GET_BYTE PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | MD5 PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SET_BYTE PARENTESISIZQUIERDA operacion COMA operacion COMA operacion PARENTESISDERECHA
                        | SHA256 PARENTESISIZQUIERDA operacion PARENTESISDERECHA                       
                        | SUBSTR PARENTESISIZQUIERDA operacion  COMA operacion COMA operacion PARENTESISDERECHA
                        | CONVERT PARENTESISIZQUIERDA operacion  COMA operacion COMA operacion PARENTESISDERECHA
                        | ENCODE PARENTESISIZQUIERDA operacion  COMA operacion  PARENTESISDERECHA
                        | DECODE PARENTESISIZQUIERDA operacion  COMA operacion  PARENTESISDERECHA
                        | AVG PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SUM PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | EXTRACT PARENTESISIZQUIERDA opcionTiempo FROM TIMESTAMP operacion PARENTESISDERECHA
                        | ID PARENTESISIZQUIERDA operacion COMA INTERVAL operacion PARENTESISDERECHA
                        | CURRENT_TIME 
                        | CURRENT_DATE
    '''
    if t[1].upper()=="ABS":
        h.reporteGramatical1 +="funcionBasica    ::=      ABS PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionABS(t[3])\n"
        t[0]=ExpresionABS(t[3])
    elif t[1].upper()=="CBRT":
        h.reporteGramatical1 +="funcionBasica    ::=      CBRT PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionCBRT(t[3])\n"
        t[0]=ExpresionCBRT(t[3])
    elif t[1].upper()=="CEIL":
        h.reporteGramatical1 +="funcionBasica    ::=      CEIL PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionCEIL(t[3])\n"
        t[0]=ExpresionCEIL(t[3])
    elif t[1].upper()=="CEILING":
        h.reporteGramatical1 +="funcionBasica    ::=      CEILING PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionCEILING(t[3])\n"
        t[0]=ExpresionCEILING(t[3])
    elif t[1].upper()=="DEGREES":
        t[0]=ExpresionDEGREES(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      DEGREES PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionDEGREES(t[3])\n"
    elif t[1].upper()=="DIV":
        print("entra a DIV++++++++++++")
        t[0]=ExpresionDIV(t[3],t[5])
        h.reporteGramatical1 +="funcionBasica    ::=      DIV PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionDIV(t[3],t[5])\n"
    elif t[1].upper()=="EXP":
        t[0]=ExpresionEXP(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      EXP PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionEXP(t[3])\n"
    elif t[1].upper()=="FACTORIAL":
        t[0]=ExpresionFACTORIAL(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      FACTORIAL PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionFACTORIAL(t[3])\n"
    elif t[1].upper()=="FLOOR":
        t[0]=ExpresionFLOOR(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      FLOOR PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionFLOOR(t[3])\n"
    elif t[1].upper()=="GCD":
        t[0]=ExpresionGCD(t[3],t[5])
        h.reporteGramatical1 +="funcionBasica    ::=      GCD PARENTESISIZQUIERDA operacion COMA operacion  PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionGCD(t[3],t[5])\n"
    elif t[1].upper()=="LN":
        t[0]=ExpresionLN(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      LN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionLN(t[3])\n"
    elif t[1].upper()=="LOG":
        t[0]=ExpresionLOG(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      LOG PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionLOG(t[3])\n"
    elif t[1].upper()=="MOD":
        t[0]=ExpresionMOD(t[3],t[5])
        h.reporteGramatical1 +="funcionBasica    ::=      MOD PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA\n" 
        h.reporteGramatical2 +="t[0]=ExpresionMOD(t[3],t[5])\n"  
    elif t[1].upper()=="PI":
        t[0]=ExpresionPI(1)
        h.reporteGramatical1 +="funcionBasica    ::=      PI PARENTESISIZQUIERDA   PARENTESISDERECHA\n"   
        h.reporteGramatical2 +="t[0]=ExpresionPI(1)\n"
    elif t[1].upper()=="POWER":
        t[0]=ExpresionPOWER(t[3],t[5])
        h.reporteGramatical1 +="funcionBasica    ::=      POWER PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA\n" 
        h.reporteGramatical2 +="t[0]=ExpresionPOWER(t[3],t[5])\n"
    elif t[1].upper()=="RADIANS":
        t[0]=ExpresionRADIANS(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      RADIANS PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n" 
        h.reporteGramatical2 +="t[0]=ExpresionRADIANS(t[3])\n"   
    elif t[1].upper()=="ROUND":
        t[0]=ExpresionROUND(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionROUND(t[3])\n"
    elif t[1].upper()=="SIGN":
        t[0]=ExpresionSIGN(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      SIGN  PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"  
        h.reporteGramatical2 +="t[0]=ExpresionSIGN(t[3])\n"  
    elif t[1].upper()=="SQRT":
        t[0]=ExpresionSQRT(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      SQRT  PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionSQRT(t[3])\n"
    elif t[1].upper()=="TRUNC":
        t[0]=ExpresionTRUNC(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      TRUNC  PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="[0]=ExpresionTRUNC(t[3])\n"
    elif t[1].upper()=="WIDTH_BUCKET":
        t[0]=ExpresionWIDTHBUCKET(t[3],t[5],t[7],t[9])
        h.reporteGramatical1 +="funcionBasica    ::=      WIDTH_BUCKET PARENTESISIZQUIERDA operacion COMA operacion COMA operacion COMA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionWIDTHBUCKET(t[3],t[5],t[7],t[9])\n"
    elif t[1].upper()=="RANDOM":
        t[0]=ExpresionRANDOM(1)
        h.reporteGramatical1 +="funcionBasica    ::=      RANDOM PARENTESISIZQUIERDA  PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionRANDOM(1)\n"
    elif t[1].upper()=="ACOS":
        t[0]=ExpresionACOS(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ACOS PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionACOS(t[3])\n"
    elif t[1].upper()=="ACOSD":
        t[0]=ExpresionACOSD(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ACOSD PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionACOSD(t[3])\n"
    elif t[1].upper()=="ASIN":
        t[0]=ExpresionASIN(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ASIN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="tt[0]=ExpresionASIN(t[3])\n"
    elif t[1].upper()=="ASIND":
        t[0]=ExpresionASIND(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ASIND PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionASIND(t[3])\n"
    elif t[1].upper()=="ATAN":
        t[0]=ExpresionATAN(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ATAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionATAN(t[3])\n"
    elif t[1].upper()=="ATAND":
        t[0]=ExpresionATAND(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ATAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n" 
        h.reporteGramatical2 +="t[0]=ExpresionATAND(t[3])\n"
    elif t[1].upper()=="ATAN2":
        t[0]=ExpresionATAN2(t[3],t[5])
        h.reporteGramatical1 +="funcionBasica    ::=      ATAN2 PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionATAN2(t[3],t[5])\n"
    elif t[1].upper()=="ATAN2D":
        t[0]=ExpresionATAN2D(t[3],t[5])
        h.reporteGramatical1 +="funcionBasica    ::=      ATAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionATAN2D(t[3],t[5])\n"
    elif t[1].upper()=="COS":
        t[0]=ExpresionCOS(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      COS PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionCOS(t[3])\n"
    elif t[1].upper()=="COSD":
        t[0]=ExpresionCOSD(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      COSD PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionCOSD(t[3])\n"
    elif t[1].upper()=="COT":
        t[0]=ExpresionCOT(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      COT PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionCOT(t[3])\n"
    elif t[1].upper()=="COTD":
        t[0]=ExpresionCOTD(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      COTD PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionCOTD(t[3])\n"
    elif t[1].upper()=="SIN":
        t[0]=ExpresionSIN(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      SIN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionSIN(t[3])\n"
    

    
    elif t[1].upper()=="SIND":
        t[0]=ExpresionSIND(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      SIND PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionSIND(t[3])\n"
    elif t[1].upper()=="TAN":
        t[0]=ExpresionTAN(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      TAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionTAN(t[3])\n"
    elif t[1].upper()=="TAND":
        t[0]=ExpresionTAND(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      TAND PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionTAND(t[3])\n"
    elif t[1].upper()=="SINH":
        t[0]=ExpresionSINH(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      SINH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionSINH(t[3])\n"
    elif t[1].upper()=="COSH":
        t[0]=ExpresionCOSH(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      COSH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionCOSH(t[3])\n"
    
    elif t[1].upper()=="TANH":
        t[0]=ExpresionTANH(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      TANH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionTANH(t[3])\n"
    elif t[1].upper()=="ASINH":
        t[0]=ExpresionASINH(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ASINH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionASINH(t[3])\n"
    elif t[1].upper()=="ACOSH":
        t[0]=ExpresionACOSH(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ACOSH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionACOSH(t[3])\n"
    elif t[1].upper()=="ATANH":
        t[0]=ExpresionATANH(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ATANH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionATANH(t[3])\n"
    elif t[1].upper()=="GREATEST":
        t[0]=ExpresionGREATEST(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      GREATEST PARENTESISIZQUIERDA select_list PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionGREATEST(t[3])\n"
    elif t[1].upper()=="LEAST":
        t[0]=ExpresionLEAST(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      LEAST PARENTESISIZQUIERDA select_list PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionLEAST(t[3])\n"
    elif t[1].upper()=="NOW":
        t[0]=ExpresionNOW(1)
        h.reporteGramatical1 +="funcionBasica    ::=      NOW PARENTESISIZQUIERDA  PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionNOW(1)\n"
   


    elif t[1].upper()=="LENGTH":
        h.reporteGramatical1 +="funcionBasica    ::=      LENGTH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionLENGTH(t[3])\n"
        t[0]=ExpresionLENGTH(t[3])
    elif t[1].upper()=="TRIM":
        h.reporteGramatical1 +="funcionBasica    ::=      TRIM PARENTESISIZQUIERDA opcionTrim operacion FROM operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionTRIM(t[3],t[4],t[6])\n"
        t[0]=ExpresionTRIM(t[3],t[4],t[6])
    elif t[1].upper()=="GET_BYTE":
        h.reporteGramatical1 +="funcionBasica    ::=      GET_BYTE PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="MD5":
        h.reporteGramatical1 +="funcionBasica    ::=      MD5 PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionMD5(t[3])\n"
        t[0]=ExpresionMD5(t[3])
    elif t[1].upper()=="SET_BYTE":
        h.reporteGramatical1 +="funcionBasica    ::=      SET_BYTE PARENTESISIZQUIERDA operacion COMA operacion COMA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="SHA256":
        h.reporteGramatical1 +="funcionBasica    ::=      SHA256 PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionSHA256(t[3])\n"
        t[0]=ExpresionSHA256(t[3])
    elif t[1].upper()=="SUBSTR":
        h.reporteGramatical1 +="funcionBasica    ::=      SUBSTR PARENTESISIZQUIERDA operacion  COMA operacion COMA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionSUBSTR(t[3],t[5],t[7])\n"
        t[0]=ExpresionSUBSTR(t[3],t[5],t[7])
    elif t[1].upper()=="CONVERT":
        h.reporteGramatical1 +="funcionBasica    ::=      CONVERT PARENTESISIZQUIERDA operacion  COMA operacion COMA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="ENCODE":
        h.reporteGramatical1 +="funcionBasica    ::=      ENCODE  PARENTESISIZQUIERDA operacion  COMA operacion  PARENTESISDERECHA\n"
    elif t[1].upper()=="DECODE":
        h.reporteGramatical1 +="funcionBasica    ::=      DECODE  PARENTESISIZQUIERDA operacion  COMA operacion  PARENTESISDERECHA\n"
    elif t[1].upper()=="AVG":
        h.reporteGramatical1 +="funcionBasica    ::=      AVG PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="SUM":
        h.reporteGramatical1 +="funcionBasica    ::=      SUM PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
  
    elif t[1].upper()=="EXTRACT":
        h.reporteGramatical1 +="funcionBasica    ::=     EXTRACT  PARENTESISIZQUIERDA opcionTiempo FROM TIMESTAMP operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=ExpresionEXTRACT(t[3],t[6])\n"
        t[0]=ExpresionEXTRACT(t[3],t[6])
    elif t[1].upper()=="DATE_PART":
        h.reporteGramatical1 +="funcionBasica    ::=      DATE_PART PARENTESISIZQUIERDA operacion COMA INTERVAL operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="CURRENT_DATE":
        h.reporteGramatical1 +="funcionBasica    ::=      CURRENT_DATE \n"
        h.reporteGramatical2 +="t[0]=ExpresionCurrentDate(1)\n"
        t[0]=ExpresionCurrentDate(1)
    elif t[1].upper()=="CURRENT_TIME":
        h.reporteGramatical1 +="funcionBasica    ::=      CURRENT_TIME\n"
        h.reporteGramatical2 +="t[0]=ExpresionCurrentTime(1)\n"
        t[0]=ExpresionCurrentTime(1)
    else:
        print("no entra a ninguna en funcionBasica")



def p_funcion_basica_1(t):
    'funcionBasica   : SUBSTRING PARENTESISIZQUIERDA operacion FROM operacion FOR operacion PARENTESISDERECHA'
    h.reporteGramatical1 +="funcionBasica    ::=      SUBSTRING PARENTESISIZQUIERDA operacion FROM operacion FOR operacion PARENTESISDERECHA\n"
    h.reporteGramatical2 +="t[0]=ExpresionSUBSTRINGA(t[3],t[5],t[7])\n"
    t[0]=ExpresionSUBSTRINGA(t[3],t[5],t[7])
def p_funcion_basica_2(t):
    'funcionBasica   : SUBSTRING PARENTESISIZQUIERDA operacion FROM operacion PARENTESISDERECHA'
    h.reporteGramatical1 +="funcionBasica    ::=      SUBSTRING PARENTESISIZQUIERDA operacion FROM operacion PARENTESISDERECHA\n"
    h.reporteGramatical2 +="t[0]=ExpresionSUBSTRINGB(t[3],t[5])\n"
    t[0]=ExpresionSUBSTRINGB(t[3],t[5])
def p_funcion_basica_3(t):
    'funcionBasica   : SUBSTRING PARENTESISIZQUIERDA operacion FOR operacion PARENTESISDERECHA'
    h.reporteGramatical1 +="funcionBasica    ::=      SUBSTRING PARENTESISIZQUIERDA operacion FOR operacion PARENTESISDERECHA\n"
    h.reporteGramatical2 +="t[0]=ExpresionSUBSTRINGC(t[3],t[5])\n"
    t[0]=ExpresionSUBSTRINGC(t[3],t[5])
 
def p_opcionTrim(t):
    ''' opcionTrim  : LEADING
                    | TRAILING
                    | BOTH
    '''    
    h.reporteGramatical1 +="opcionTrim     ::=     "+str(t[1])+"\n"
    # falta mandar a las funciones de fechas y dates y todo eso
    if t[1].upper()=="LEADING":
        h.reporteGramatical1 +="funcioopcionTrimnBasica    ::=      LEADING\n"
        h.reporteGramatical2 +="t[0]=ExpresionCadenas(1)\n"
        t[0]=ExpresionCadenas("1")
    elif t[1].upper()=="TRAILING":
        h.reporteGramatical1 +="opcionTrim    ::=      TRAILING\n"
        h.reporteGramatical2 +="t[0]=ExpresionCadenas(2)\n"
        t[0]=ExpresionCadenas("2")
    elif t[1].upper()=="BOTH":
        h.reporteGramatical1 +="opcionTrim    ::=      BOTH\n"
        h.reporteGramatical2 +="t[0]=ExpresionCadenas(3)\n"
        t[0]=ExpresionCadenas("3")
    
def p_opcionTiempo(t):
    '''opcionTiempo     :   YEAR
                        |   MONTH
                        |   DAY
                        |   HOUR
                        |   MINUTE
                        |   SECOND
    '''
    if t[1].upper()=="YEAR":
        h.reporteGramatical1 +="opcionTiempo    ::=      YEAR\n"
        h.reporteGramatical2 +="t[0]=ExpresionCadenas(1)\n"
        t[0]=ExpresionCadenas("1")
    elif t[1].upper()=="MONTH":
        h.reporteGramatical1 +="opcionTiempo    ::=      MONTH\n"
        h.reporteGramatical2 +="t[0]=ExpresionCadenas(2)\n"
        t[0]=ExpresionCadenas("2")
    elif t[1].upper()=="DAY":
        h.reporteGramatical1 +="opcionTiempo    ::=      DAY\n"
        h.reporteGramatical2 +="t[0]=ExpresionCadenas(3)\n"
        t[0]=ExpresionCadenas("3")
    elif t[1].upper()=="HOUR":
        h.reporteGramatical1 +="opcionTiempo    ::=      HOUR\n"
        h.reporteGramatical2 +="t[0]=ExpresionCadenas(4)\n"
        t[0]=ExpresionCadenas("4")
    elif t[1].upper()=="MINUTE":
        h.reporteGramatical1 +="opcionTiempo    ::=      MINUTE\n"
        h.reporteGramatical2 +="t[0]=ExpresionCadenas(5)\n"
        t[0]=ExpresionCadenas("5")
    elif t[1].upper()=="SECOND":
        h.reporteGramatical1 +="opcionTiempo    ::=      SECOND\n"
        h.reporteGramatical2 +="t[0]=ExpresionCadenas(6)\n"
        t[0]=ExpresionCadenas("6")
    

#-----------------------------------------------------PRODUCCIONES TERMINALES--------------------------------------------------------------------
def p_final(t):
    '''final        : DECIMAL
                    | ENTERO'''
    h.reporteGramatical1 +="final    ::=      Numero("+str(t[1])+")\n"
    h.reporteGramatical2 +="t[0]=ExpresionNumero(t[1])\n"
    t[0]=ExpresionNumero(t[1])


def p_final_id(t):
    'final          : ID'
    t[0] = t[1]
    h.reporteGramatical1 +="final    ::=      ID("+str(t[1])+")\n"
    h.reporteGramatical2 +="t[0]=ExpresionIdentificador(t[1])\n"
    t[0]=ExpresionIdentificador(t[1])

def p_final_invocacion(t):
    'final          : ID PUNTO ID'
    h.reporteGramatical1 +="final    ::=      ID("+str(t[1])+") . ID("+str(t[3])+")\n"
    h.reporteGramatical2 +="t[0] = ExpresionInvocacion(t[1],t[3])\n"
    t[0] = ExpresionLlamame(t[1],t[3])

def p_final_invocacion_2(t):
    'final          : ID PUNTO POR'
    h.reporteGramatical1 +="final    ::=      ID("+str(t[1])+") . ID("+str(t[3])+")\n"
    h.reporteGramatical2 +="t[0] = ExpresionInvocacion(t[1],t[3])\n"
    t[0] = ExpresionLlamame(t[1],t[3])

def p_final_cadena(t):
    'final          : CADENA'
    t[0] = t[1]
    h.reporteGramatical1 +="final     ::=     CADENA ("+t[1]+")\n"
    h.reporteGramatical2 +="t[0]=ExpresionCadenas(t[1])\n"
    t[0]=ExpresionCadenas(t[1])

#-----------------------------------------------------INSERT BD--------------------------------------------------------------------
def p_insertBD_1(t):
    'insertinBD           : INSERT INTO ID VALUES PARENTESISIZQUIERDA listaParam PARENTESISDERECHA PUNTOYCOMA'
    #print(t[3],t[6])
    t[0] = InsertinDataBases(t[3],None,t[6])
    h.reporteGramatical1 +="insertinBD    ::=      INSERT INTO ID VALUES PARENTESISIZQUIERDA listaParam PARENTESISDERECHA PUNTOYCOMA\n"
    h.reporteGramatical2 += "InsertinDabaBases(t[3],t[6])\n"

def p_insertBD_2(t):
    'insertinBD           : INSERT INTO ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA VALUES PARENTESISIZQUIERDA listaParam PARENTESISDERECHA PUNTOYCOMA'
    print(t[9])
    t[0] = InsertinDataBases(t[3],t[5],t[9])
    h.reporteGramatical1 +="insertinBD    ::=     INSERT INTO ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA VALUES PARENTESISIZQUIERDA listaParam PARENTESISDERECHA PUNTOYCOMA\n"
    h.reporteGramatical2 += "t[0] = InsertinDataBases(t[3],t[5],t[9])\n"

# SE SEPARO LA LISTA EN 2 METODOS PARA MANEJAR DATOS
def p_listaParam(t):
    '''listaParam         : listaParam COMA listaP
    '''
    t[1].append(t[3])
    t[0] = t[1]
    h.reporteGramatical1 +="insertinBD    ::=      listaParam COMA operacion\n"
    h.reporteGramatical2 +="t[0]=t[1]\n"

def p_listaParam_2(t):
    '''listaParam           : listaP
    '''
    t[0] = [t[1]]
    h.reporteGramatical1 +="listaParam    ::=      operacion\n"
    h.reporteGramatical2 +="t[0]=[t[1]]\n"

def p_listaP_1(t):
    'listaP                 : operacion'
    print("---------------",t[1])
    t[0] = t[1]

def p_listaP_2(t):
    'listaP             : ID operacion'
    t[0] = t[1]
    print(t[0])

def p_listaP_3(t):
    'listaP             : ID PARENTESISIZQUIERDA PARENTESISDERECHA'
    t[0] = t[1]+"()"
    print(t[0])


#-----------------------------------------------------UPDATE BD--------------------------------------------------------------------
def p_updateBD(t):
    'updateinBD           : UPDATE ID SET asignaciones WHERE operacion PUNTOYCOMA'
    t[0]= UpdateinDataBase(t[2],t[4],t[6])
    h.reporteGramatical1 +="updateinBD    ::=      UPDATE ID SET asignacion WHERE operacion PUNTOYCOMA\n"
    h.reporteGramatical1 +="t[0]=UpdateinDabaBase(t[2].t[4],t[6])\n"


# SE SEPARO LA LISTA EN 2 METODOS PARA MANEJAR DATOS
def p_asignaciones(t):
    '''asignaciones       : asignaciones COMA operacion
    '''
    t[1].append(t[3])
    t[0] = t[1]
    h.reporteGramatical1 +="asignaciones    ::=      asignaciones COMA operacion\n"
    h.reporteGramatical2 +="t[0]=t[1]\n"

def p_asignaciones_2(t):
    '''asignaciones       : operacion
    '''
    t[0] = [t[1]]
    h.reporteGramatical1 +="asignaciones    ::=      asigna\n"
    h.reporteGramatical2 +="t[0]=[t[1]]\n"

#-----------------------------------------------------DELETE IN BD--------------------------------------------------------------------
def p_deleteinBD_1(t):
    'deleteinBD         : DELETE FROM ID PUNTOYCOMA'
    t[0] = t[3]
    h.reporteGramatical1 +="deleteinBD    ::=      DELETE FROM ID PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0]=t[3]\n"

def p_deleteinBD_2(t):
    'deleteinBD         : DELETE FROM ID WHERE operacion PUNTOYCOMA'
    t[0] = DeleteinDataBases(t[3],t[5])
    h.reporteGramatical1 +="deleteinBD    ::=      DELETE FROM ID WHERE operacion PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0]=DeleteinDataBases(t[3],t[5])\n"


#-----------------------------------------------------CREATE TABLE CON INHERITS-------------------------------------------------------
def p_inheritsBD(t):
    'inheritsBD         : CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA  INHERITS PARENTESISIZQUIERDA ID PARENTESISDERECHA PUNTOYCOMA'
    t[0]=InheritsBD(t[3],t[9],t[5])
    h.reporteGramatical1 +="inheritsBD    ::=      CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA  INHERITS PARENTESISIZQUIERDA ID PARENTESISDERECHA PUNTOYCOMA\n"    
    h.reporteGramatical2 +="t[0]=InheritsBD(t[3],t[9],t[5])\n"

#-----------------------------------------------------CREATE TABLE--------------------------------------------------------------------
def p_createTable(t):
    'createTable        : CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA PUNTOYCOMA'
    t[0]= CreateTable(t[3],t[5])
    h.reporteGramatical1 +="createTable    ::=      CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA PUNTOYCOMA\n"
    h.reporteGramatical2 += "t[0]= CreateTable(t[3],t[5])\n"


# -------------------------------------------------------------------------------------------------------------- 
# SE SEPARO LA LISTA EN 2 METODOS PARA MANEJAR DATOS
def p_creaColumna(t):
    '''creaColumnas        : creaColumnas COMA Columna 
    '''
    t[1].append(t[3])
    t[0] = t[1]
    #print(t[0])
    h.reporteGramatical1 +="creaColumnas    ::=      creaColumnas COMA Columna\n"
    h.reporteGramatical2 +="t[1]\n"

def p_creaColumna_2(t):
    '''creaColumnas        : Columna 
    '''
    t[0]=[t[1]]
    h.reporteGramatical1 +="createTable    ::=      Columna\n"
    h.reporteGramatical2 +="[t[1]]\n"

# -------------------------------------------------------------------------------------------------------------- 
#INICIA LAS PRODUCCIONES DE COLUMNAS
def p_columna_1(t):
    'Columna            : ID tipo'
    t[0]=TipoAtributoTable(ColumnasTable(t[1],t[2],None),OPERACION_RESTRICCION_COLUMNA.COLUMNASINRESTRICCION)
    h.reporteGramatical1 +="Columna    ::=      ID tipo\n"
    h.reporteGramatical2 +="t[0]=TipoAtributoTable(ColumnasTable(t[1],t[2],None),OPERACION_RESTRICCION_COLUMNA.COLUMNASINRESTRICCION)"

def p_columna_2(t):
    'Columna            : ID tipo paramOpcional'
    t[0]=TipoAtributoTable(ColumnasTable(t[1],t[2],t[3]),OPERACION_RESTRICCION_COLUMNA.COLUMNACONRESTRICCION)
    h.reporteGramatical1 +="Columna      ::=     ID tipo paramOpcional"
    h.reporteGramatical2 +="t[0]=TipoAtributoTable(ColumnasTable(t[1],t[2],t[3]),OPERACION_RESTRICCION_COLUMNA.COLUMNACONRESTRICCION)\n"

def p_columna_3(t):
    'Columna            : UNIQUE PARENTESISIZQUIERDA listaParam PARENTESISDERECHA'
    t[0]=TipoAtributoTable(RestriccionUnique(t[3]),OPERACION_RESTRICCION_COLUMNA.UNIQUE_ATRIBUTO)
    h.reporteGramatical1 +="Columna            : UNIQUE PARENTESISIZQUIERDA listaParam PARENTESISDERECHA\n"
    h.reporteGramatical2 +="t[0]=TipoAtributoTable(RestriccionUnique(t[3]),OPERACION_RESTRICCION_COLUMNA.UNIQUE_ATRIBUTO)\n"

def p_columna_4(t):
    '''Columna          : constraintcheck
    '''
    t[0]=TipoAtributoTable(t[1],OPERACION_RESTRICCION_COLUMNA.CHECK_CONSTRAINT)
    h.reporteGramatical1 +="Columna    ::=      constraintcheck\n"
    h.reporteGramatical2 +="t[0]=TipoAtributoTable(t[1],OPERACION_RESTRICCION_COLUMNA.CHECK_CONSTRAINT)\n"

def p_columna_5(t):
    'Columna            : checkinColumn'
    t[0]=TipoAtributoTable(t[1],OPERACION_RESTRICCION_COLUMNA.CHECK_SIMPLE)
    h.reporteGramatical1 +="Columna    ::=      checkinColumn\n"
    h.reporteGramatical2 +="t[0]=TipoAtributoTable(t[1],OPERACION_RESTRICCION_COLUMNA.CHECK_SIMPLE)\n"

def p_columna_6(t):
    'Columna            : primaryKey'
    t[0]=TipoAtributoTable(t[1],OPERACION_RESTRICCION_COLUMNA.PRIMARY_KEY)
    h.reporteGramatical1 +="Columna    ::=      primaryKey\n"
    h.reporteGramatical2 +="t[0]=TipoAtributoTable(t[1],OPERACION_RESTRICCION_COLUMNA.PRIMARY_KEY)\n"

def p_columna_7(t):
    'Columna            : foreignKey'
    t[0]=TipoAtributoTable(t[1],OPERACION_RESTRICCION_COLUMNA.FOREIGN_KEY)
    h.reporteGramatical1 +="Columna    ::=       foreingKey\n"
    h.reporteGramatical2 += "t[0]=TipoAtributoTable(t[1],OPERACION_RESTRICCION_COLUMNA.FOREIGN_KEY)\n"


# -------------------------------------------------------------------------------------------------------------- 
#INICIA LA LISTA DE RESTRICCIONES OPCIONALES EN LAS COLUMNAS
def p_paramOpcional(t):
    '''paramOpcional    : paramOpcional paramopc
    '''
    t[1].append(t[2])
    t[0] = t[1]
    h.reporteGramatical1 +="paramOpcional    ::=      paramOpcional paramopc\n"
    h.reporteGramatical2 +="t[0]=t[1]\n"
    

def p_paramOpcional_1(t):
    '''paramOpcional    : paramopc
    '''
    t[0] = [t[1]]
    h.reporteGramatical1 +="paramOpcional    ::=      paramopc\n"
    h.reporteGramatical2 +="t[0]=[t[1]]\n"



# -------------------------------------------------------------------------------------------------------------- 
#INICIA LAS RESTRICCIONES EN LAS COLUMNAS
def p_paramopc_1(t):
    '''paramopc         : DEFAULT final
                        | NULL
                        | NOT NULL
                        | UNIQUE
                        | PRIMARY KEY
    '''
    if t[1].upper() == "DEFAULT":
        t[0] = TipoRestriccion(RestriccionDefaul(t[2]),OPERACION_RESTRICCION_COLUMNA.DEFAULT)
        h.reporteGramatical1 +="paramopc    ::=      DEFAULT final\n"
        h.reporteGramatical2 +="TipoRestriccion(RestriccionDefaul(t[2]),OPERACION_RESTRICCION_COLUMNA.DEFAULT)\n"
    
    elif t[1].upper() == "NULL":
        t[0] = TipoRestriccion(RestriccionNull(1),OPERACION_RESTRICCION_COLUMNA.NULL)
        h.reporteGramatical1 +="paramopc    ::=      NULL\n"
        h.reporteGramatical2 +="TipoRestriccion(RestriccionNull(1),OPERACION_RESTRICCION_COLUMNA.NULL)\n"
    
    elif t[1].upper() == "NOT":
        t[0] = TipoRestriccion(RestriccionNotNull(1),OPERACION_RESTRICCION_COLUMNA.NOT_NULL)
        h.reporteGramatical1 +="paramopc    ::=      NOT NULL\n"
        h.reporteGramatical2 +="t[0] = TipoRestriccion(RestriccionNotNull(1),OPERACION_RESTRICCION_COLUMNA.NOT_NULL)\n"
    
    elif t[1].upper() == "UNIQUE":
        t[0] = TipoRestriccion(RestriccionUniqueSimple(1),OPERACION_RESTRICCION_COLUMNA.UNIQUE_COLUMNA)
        h.reporteGramatical1 +="paramopc    ::=      UNIQUE\n"
        h.reporteGramatical2 +="TipoRestriccion(RestriccionUniqueSimple(1),OPERACION_RESTRICCION_COLUMNA.UNIQUE_COLUMNA)\n"
    
    elif t[1].upper() == "PRIMARY" and t[2].upper()=="KEY":
        t[0] = TipoRestriccion(RestriccionPrimaryKeyColumn(1),OPERACION_RESTRICCION_COLUMNA.PRIMARY_KEY)
        h.reporteGramatical1 +="paramopc    ::=      PRIMARY KEY\n"
        h.reporteGramatical2 +="TipoRestriccion(RestriccionPrimaryKeyColumn(1),OPERACION_RESTRICCION_COLUMNA.PRIMARY_KEY)\n"
    
    else:
        print("FFFFF")
    

# -------------------------------------------------------------------------------------------------------------- 
#LLAMADA A LAS RESTRICCION CHECK
def p_paramopc_2(t):
    'paramopc           : constraintcheck'
    t[0] = TipoRestriccion(t[1],OPERACION_RESTRICCION_COLUMNA.CHECK_CONSTRAINT)
    h.reporteGramatical1 +="paramopc    ::=      constraintcheck\n"
    h.reporteGramatical2 +="t[0] = TipoRestriccion(t[1],OPERACION_RESTRICCION_COLUMNA.CHECK_CONSTRAINT)\n"
    
def p_paramopc_3(t):
    'paramopc           : checkinColumn'
    t[0]=TipoRestriccion(t[1],OPERACION_RESTRICCION_COLUMNA.CHECK_SIMPLE)
    h.reporteGramatical1 +="paramopc    ::=      checkinColumn\n"
    h.reporteGramatical2 +="t[0]=TipoRestriccion(t[1],OPERACION_RESTRICCION_COLUMNA.CHECK_SIMPLE)\n"

# -------------------------------------------------------------------------------------------------------------- 
#RESTRICCION UNIQUE
def p_paramopc_4(t):
    'paramopc           : CONSTRAINT ID UNIQUE'
    t[0] = TipoRestriccion(RestriccionConstraintUnique(t[2]),OPERACION_RESTRICCION_COLUMNA.UNIQUE_CONSTAINT)
    h.reporteGramatical1 +="paramopc    ::=      CONSTRAINT   ID   UNIQUE\n"
    h.reporteGramatical2 +="t[0] = TipoRestriccion(RestriccionConstraintUnique(t[2]),OPERACION_RESTRICCION_COLUMNA.UNIQUE_CONSTAINT)\n"


# -------------------------------------------------------------------------------------------------------------- 
#RESTRICION CHECK 
def p_checkcolumna(t):
    'checkinColumn      :  CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA'
    t[0]=RestriccionCheck(t[3])
    h.reporteGramatical1 +="checkinColumn     ::=     CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    h.reporteGramatical2 +="t[0]=RestriccionCheck(t[3])\n"

def p_constraintcheck(t):
    'constraintcheck    : CONSTRAINT ID CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA'
    t[0]=RestriccionConstraintCheck(t[2],t[5])
    h.reporteGramatical1 +="constraintcheck    : CONSTRAINT ID CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    h.reporteGramatical2 +="t[0]=RestriccionConstraintCheck(t[2],t[5])\n"




def p_primaryKey(t):
    'primaryKey         : PRIMARY KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA'
    t[0]=RestriccionPrimaryKey(t[4])
    h.reporteGramatical1 +="primaryKey    ::=      PRIMARY KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA\n"
    h.reporteGramatical2 +="t[0]=RestriccionPrimaryKey(t[4])\n"


def p_foreingkey(t):
    'foreignKey         : FOREIGN KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA REFERENCES ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA' 
    t[0]=RestriccionForeingkey(t[7],t[4],t[9])
    h.reporteGramatical1 +="foreignKey    ::=      FOREIGN KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA REFERENCES ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA\n"
    h.reporteGramatical2 +="t[0]=RestriccionForeingkey(t[7],t[4],t[9])\n"

#-----------------------------------------------------TIPOS DE DATOS--------------------------------------------------------------------

def p_tipo(t):
    '''tipo            :  SMALLINT
                        | INTEGER
                        | BIGINT
                        
                        | NUMERIC
                        | REAL
                        | DOUBLE PRECISION
                        | MONEY
                        | VARCHAR PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA
                        | CHARACTER VARYING PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA
                        | CHARACTER PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA
                        | CHAR PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA
                        | TEXT
                        | BOOLEAN
                        | TIMESTAMP
                        | TIME
                        | INTERVAL
                        | DATE
                        | YEAR
                        | MONTH 
                        | DAY
                        | HOUR 
                        | MINUTE
                        | SECOND
    '''
    # -------------------------------------------------------------------------------------------------------------- 
    if t[1].upper()=="SMALLINT":
        t[0] = TipoDatoColumna(t[1],None) 
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="INTEGER":
        t[0] = TipoDatoColumna(t[1],None)
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="BIGINT":
        t[0]=TipoDatoColumna(t[1],None)
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

    # -------------------------------------------------------------------------------------------------------------- 
    

    
    

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="NUMERIC":
        t[0]=TipoDatoColumna(t[1],None)
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="REAL":
        t[0]=TipoDatoColumna(t[1],None)
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="DOUBLE":
        t[0]=TipoDatoColumna(t[1],None)
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="MONEY":
        t[0]=TipoDatoColumna(t[1],None)
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="CHARACTER" and t[2].upper()=="VARYING":
        t[0]=TipoDatoColumna(t[2],t[4])
        h.reporteGramatical1 +="tipo    ::=      CHARACTER VARYING PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],t[4])\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="VARCHAR":
        t[0]=TipoDatoColumna(t[1],t[3])
        h.reporteGramatical1 +="tipo    ::=      VARCHAR PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],t[3])\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="CHARACTER":
        t[0]=TipoDatoColumna(t[1],t[3])
        h.reporteGramatical1 +="tipo    ::=      CHARACTER PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],t[3])\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="CHAR":
        t[0]=TipoDatoColumna(t[1],t[3])
        h.reporteGramatical1 +="tipo    ::=      CHAR PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],t[3])\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="TEXT":
        t[0]=TipoDatoColumna(t[1],None)
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="BOOLEAN":
        t[0]=TipoDatoColumna(t[1],None)
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="TIMESTAMP":
        t[0]=TipoDatoColumna(t[1],None)
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="TIME":
        t[0]=TipoDatoColumna(t[1],None)
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="INTERVAL":
        t[0]=TipoDatoColumna(t[1],None)
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="DATE":
        t[0]=TipoDatoColumna(t[1],None)
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="YEAR":
        t[0]=TipoDatoColumna(t[1],None)
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="MONT":
        t[0]=TipoDatoColumna(t[1],None)
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="HOUR":
        t[0]=TipoDatoColumna(t[1],None)
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="MINUT":
        t[0]=TipoDatoColumna(t[1],None)
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="SECOND":
        t[0]=TipoDatoColumna(t[1],None)
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
        h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

# -------------------------------------------------------------------------------------------------------------- 
def p_tipo_2(t):
    'tipo               : DECIMAL'
    t[0]=TipoDatoColumna(t[1],None)
    h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
    h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],None)\n"

# -------------------------------------------------------------------------------------------------------------- 
def p_tipo_3(t):
    'tipo               : DECIMAL PARENTESISIZQUIERDA ENTERO COMA ENTERO PARENTESISDERECHA '
    val = str(t[3])+","+str(t[5])
    t[0]=TipoDatoColumna(t[1],val)
    h.reporteGramatical1 +"tipo     ::=     "+str(t[1])+"("+str(t[3])+","+str(t[5])+")\n"
    h.reporteGramatical2 +="t[0]=TipoDatoColumna(t[1],val)"



#--------------------------------------------------- SENTENCIA SELECT --------------------------------------------------------------
def p_select(t):
    '''selectData       : SELECT select_list FROM select_list WHERE search_condition opcionesSelect 
                        | SELECT POR FROM select_list WHERE search_condition opcionesSelect 
    '''
    if t[2]=='*':
        h.reporteGramatical1 +="selectData    ::=     SELECT POR FROM select_list WHERE search_condition opcionesSelect \n"
        print("/////////////////// SELECT CON ASTERISCO ////////////////////////")
        print("Columnas: ",t[2])
        print("Tablas: ",t[4])
        print("Where: ",QueryWhere(t[6]))
        print("Extras: ",t[7])
        t[0]=Select5(t[2],t[4],QueryWhere(t[6]),t[7])
    else:
        h.reporteGramatical1 +="selectData    ::=      SELECT select_list FROM select_list WHERE search_condition opcionesSelect \n"
        print("/////////////////// SELECT SIN ASTERISCO ////////////////////////")
        print("Columnas: ",t[2])
        print("Tablas: ",t[4])
        print("Where: ",QueryWhere(t[6]))
        print("Extras: ",t[7])
        t[0]=Select5(t[2],t[4],QueryWhere(t[6]),t[7])
     


def p_select_1(t):
    '''selectData       : SELECT select_list FROM select_list WHERE search_condition  
                        | SELECT POR FROM select_list WHERE search_condition  
    '''
    if t[2]=='*':
        h.reporteGramatical1 +="selectData    ::=     SELECT POR FROM select_list WHERE search_condition  \n"
        h.reporteGramatical2 +="t[0]=Select3(t[4],QueryWhere(t[6]))\n"
        print("entra al select con where y asterisco/////////////////")
        t[0]=Select3(t[4],QueryWhere(t[6]))
        print("el objeto que sube")
        print(t[0])
    else:
        h.reporteGramatical1 +="selectData    ::=     SELECT select_list FROM select_list WHERE search_condition  \n"
        h.reporteGramatical2 +=" t[0]=Select4(t[2],t[4],QueryWhere(t[6]))\n"
        print("entra al select con where y campos /////////////////")
        print(t[2])
        print(t[4])
        print(t[6])
        t[0]=Select4(t[2],t[4],QueryWhere(t[6]))
        print(t[0])



# esta full
def p_select_2(t):
    '''selectData       : SELECT select_list FROM select_list  
                        | SELECT POR FROM select_list  
    ''' 
    if t[2]=='*':
        h.reporteGramatical1 +="selectData    ::=      SELECT POR FROM select_list  \n"
        h.reporteGramatical2 +=" t[0]=Select(1,t[4])\n"
        print("entra a select_2 A")
        #se le agrega como segundo parametro el 2 que significa que venia asterirsco o todas las tablas
        t[0]=Select(1,2,t[4])
    
    else:
        # select tipo 4
        h.reporteGramatical1 +="selectData    ::=     SELECT select_list FROM select_list  \n"
        h.reporteGramatical2 +=" t[0]=Select2(2,t[2],t[4])\n"
        print("entra a select_2  B")
        print(t[2])
        print(t[4])
        t[0]=Select2(2,t[2],t[4])

# esta full
def p_select_3(t):
    '''selectData       : SELECT select_list   
    '''
    h.reporteGramatical1 +="selectData    ::=      SELECT select_list   \n"
    h.reporteGramatical2 +=" t[0]=Select(1,t[2])\n"
    #se le agrega el 2do 1 si solo vienen datos y no tablas
    t[0]=Select(1,1,t[2])



def p_opcionesSelect_1(t):
    '''opcionesSelect   : opcionesSelect opcionSelect
    '''
    h.reporteGramatical1 +="opcionesSelect    ::=      opcionesSelect opcionSelect\n"
    print(t[1])
    t[1].append(t[2])
    t[0]=t[1]

def p_opcionesSelect_2(t):
    '''opcionesSelect   : opcionSelect
    '''
    h.reporteGramatical1 +="opcionesSelect    ::=      opcionSelect\n"
    print(t[1])
    t[0]=[t[1]]


def p_opcionesSelect_3(t):
    '''opcionSelect     : LIMIT operacion
                        | GROUP BY select_list
                        | HAVING select_list
                        | ORDER BY select_list 
    '''
    if t[1].upper()=="LIMIT":
        h.reporteGramatical1 +="opcionSelect    ::=      LIMIT operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionLimit(t[2])\n"
        t[0]=ExpresionLimit(t[2])
    elif t[1].upper()=="GROUP":
        h.reporteGramatical1 +="opcionSelect    ::=      GROUP BY select_list\n"
        h.reporteGramatical2 +="t[0]=ExpresionGroup(t[3])\n"
        t[0]=ExpresionGroup(t[3])
    elif t[1].upper()=="HAVING":
        h.reporteGramatical1 +="opcionSelect    ::=      HAVING select_list\n"
        h.reporteGramatical2 +="t[0]=ExpresionHaving(t[2])\n"
        t[0]=ExpresionHaving(t[2])
    elif t[1].upper()=="ORDER":
        h.reporteGramatical1 +="opcionSelect    ::=      ORDER BY select_list\n"
        h.reporteGramatical2 +="t[0]=ExpresionOrder(t[3],'ASC')\n"
        t[0]=ExpresionOrder(t[3],'ASC')


def p_opcionesSelect_4(t):
    '''opcionSelect     : LIMIT operacion OFFSET operacion
                        | ORDER BY select_list ordenamiento                     
    '''
    if t[1].upper()=="LIMIT":
        h.reporteGramatical1 +="opcionSelect    ::=      LIMIT operacion OFFSET operacion\n"
        h.reporteGramatical2 +="t[0]=ExpresionLimitOffset(t[2],t[4])\n"
        t[0]=ExpresionLimitOffset(t[2],t[4])
    elif t[1].upper()=="ORDER":
        h.reporteGramatical1 +="opcionSelect    ::=      ORDER BY select_list ordenamiento\n"
        h.reporteGramatical2 +="t[0]=ExpresionOrder(t[3],t[4])\n"
        t[0]=ExpresionOrder(t[3],t[4])



def p_ordenamiento(t):
    '''ordenamiento     : ASC
                        | DESC '''
    h.reporteGramatical1 +="ordenamiento    ::=      "+str(t[1])+"\n"
    h.reporteGramatical2 +=" t[0]=str(t[1])\n"
    t[0]=str(t[1])



def p_search_condition_2(t):
    'search_condition   : final NOT IN PARENTESISIZQUIERDA selectData PARENTESISDERECHA'
    h.reporteGramatical1 +="search_condition    ::=       NOT search_condition\n"
    print("esta condicion es del not con operacion******************")
    print(t[1])
    print(t[5])
    t[0]=ExpresionNotIn(t[1],t[5])

#agregar eeste al arbol y 3D
def p_search_condition_5(t):
    'search_condition   : NOT EXISTS PARENTESISIZQUIERDA selectData PARENTESISDERECHA'
    h.reporteGramatical1 +="search_condition    ::=       NOT search_condition\n"
    print("esta condicion es del not con operacion******************")
    print(t[4])
    t[0]=ExpresionNotExists(t[4])

#agregar eeste al arbol y 3D
def p_search_condition_6(t):
    'search_condition   : EXISTS PARENTESISIZQUIERDA selectData PARENTESISDERECHA'
    h.reporteGramatical1 +="search_condition    ::=       NOT search_condition\n"
    print("esta condicion es del not con operacion******************")
    print(t[3])
    t[0]=ExpresionExists(t[3])

#agregar eeste al arbol y 3D
def p_search_condition_7(t):
    'search_condition   : final  IN PARENTESISIZQUIERDA selectData PARENTESISDERECHA'
    h.reporteGramatical1 +="search_condition    ::=       NOT search_condition\n"
    print("esta condicion es del not con operacion******************")
    print(t[1])
    print(t[4])
    t[0]=ExpresionIn(t[1],t[4])

# PARA ABAJO YA ESTA
def p_search_condition_3(t):
    'search_condition   : operacion'
    h.reporteGramatical1 +="search_condition    ::=       operacion\n"
    h.reporteGramatical2 +=" t[0]=t[1]\n"
    print("entra a la operacion del seach_condition++++++++++++++++++++++++++++++++++++++++")
    print(t[1])
    t[0]=t[1]

def p_search_condition_4(t):
    'search_condition   : PARENTESISIZQUIERDA search_condition PARENTESISDERECHA'
    h.reporteGramatical1 +="search_condition    ::=     PARENTESISIZQUIERDA search_condition PARENTESISDERECHA\n"
    h.reporteGramatical2 +=" t[0]=t[2]\n"
    print("entra a la condicion con el parentesis")
    print(t[2])
    t[0]=t[2]





def p_select_list_1(t):
    ' select_list   : select_list COMA operacion'
    h.reporteGramatical1 +="select_list    ::=      select_list COMA operacion\n"
    h.reporteGramatical2 +=" t[1].append(t[3])\nt[0]=t[1]\n"
    print("Entra a select list COMA operacion****************************************")
    t[1].append(t[3])
    print(t[1])
    t[0]=t[1]
    

 
def p_select_list_6(t):
    ' select_list   : select_list COMA asignacion'
    h.reporteGramatical1 +="select_list    ::=      select_list COMA asignacion\n"
    h.reporteGramatical2 +=" t[0]=Asignacion(t[1],t[3])\n"
    print(" entra al select_list COMA operacion-------------")
    t[1].append(t[3])
    t[0]=t[1]
    print(t[0])
 
def p_select_list_7(t):
    ' select_list   :  asignacion'
    h.reporteGramatical1 +="select_list    ::=      asignacion\n"
    h.reporteGramatical2 +=" t[0]=t[1]\n"
    print(" entra al select_list: asignacion-------------")
    print(t[1])
    t[0]=[t[1]]


def p_select_list_2(t):
    'select_list    : operacion'
    h.reporteGramatical1 +="select_list    ::=      operacion\n"
    h.reporteGramatical2 +=" t[0]=[ExpresionFuncionBasica(t[1])]\n"
    print("select_list+++++++++++++++++++++++++")
    print(t[1])
    t[0]=[ExpresionFuncionBasica(t[1])]

def p_asignacion_1(t):
    ' asignacion   : operacion AS  operacion' 
    h.reporteGramatical1 +="select_list    ::=      select_list AS  operacion\n"
    h.reporteGramatical2 +=" t[0]=[Asignacion(t[1],t[3])]\n"
    print("entra a asignacion: operacion AS operacion")
    t[0]=Asignacion(t[1],t[3])

def p_asignacion_2(t):
    ' asignacion   : final final'
    h.reporteGramatical1 +="select_list    ::=      final final\n"
    h.reporteGramatical2 +=" t[0]=[Asignacion(t[1],t[2])]\n"
    print(" entra al select_list de 2 finales-------------")
    t[0]=Asignacion(t[1],t[2])
    print(t[0])

def p_funcion_basica_4(t):
    'funcionBasica   : operacion BETWEEN operacion '
    h.reporteGramatical1 +="funcionBasica    ::=      operacion BETWEEN operacion AND operacion\n"
    h.reporteGramatical2 +="t[0]=ExpresionBetween(t[1],t[3])\n"
    print("entra al between con sus operaciones")
    print(t[1])
    print(t[3])
    t[0]=ExpresionBetween(t[1],t[3])




def p_funcion_basica_7(t):
    'funcionBasica   : operacion NOT BETWEEN operacion'
    h.reporteGramatical1 +="funcionBasica    ::=      operacion NOT BETWEEN operacion AND operacion\n"
    h.reporteGramatical2 +="t[0]=ExpresionNotBetween(t[1],t[4])\n"
    print("entra al NOT between con sus operaciones")
    print(t[1])
    print(t[3])
    t[0]=ExpresionNotBetween(t[1],t[4])


def p_funcion_basica_8(t):
    'funcionBasica   : operacion  BETWEEN SYMMETRIC operacion '
    h.reporteGramatical1 +="funcionBasica    ::=      operacion  BETWEEN SYMMETRIC operacion AND operacion\n"
    h.reporteGramatical2 +="t[0]=ExpresionBetweenSymmetric(t[1],t[4])\n"
    t[0]=ExpresionBetweenSymmetric(t[1],t[4])

def p_funcion_basica_9(t):
    'funcionBasica   : operacion NOT BETWEEN SYMMETRIC operacion '
    h.reporteGramatical1 +="funcionBasica    ::=      operacion NOT BETWEEN SYMMETRIC operacion AND operacion\n"
    h.reporteGramatical2 +="t[0]=ExpresionNotBetweenSymmetric(t[1],t[5])\n"
    t[0]=ExpresionNotBetweenSymmetric(t[1],t[5])


def p_funcion_basica_10(t):
    '''funcionBasica : operacion IS DISTINCT FROM operacion                            
    '''
    h.reporteGramatical1 +="funcionBasica    ::=      operacion IS DISTINCT FROM operacion\n"
    h.reporteGramatical2 +="t[0]=ExpresionIsDistinct(t[1],t[5])\n"
    print("entra al IS DISTINCT ++++++++++++++++++")
    t[0]=ExpresionIsDistinct(t[1],t[5])

def p_funcion_basica_11(t):
    '''funcionBasica : operacion IS NOT DISTINCT  FROM operacion'''
    h.reporteGramatical1 +="funcionBasica    ::=     operacion IS NOT DISTINCT  FROM operacion\n"
    h.reporteGramatical2 +="t[0]=ExpresionIsNotDistinct(t[1],t[6])\n"
    print("entra al IS NOT DISTINCT ++++++++++++++++++")
    t[0]=ExpresionIsNotDistinct(t[1],t[6])

def p_tipos(t):
    '''tipos : CREATE TYPE final AS ENUM PARENTESISIZQUIERDA select_list PARENTESISDERECHA PUNTOYCOMA'''
    print("entra al enum++++++++++++++++++++++++++++++++")
    h.reporteGramatical1 +="tipos    ::=     CREATE TYPE final AS ENUM PARENTESISIZQUIERDA select_list PARENTESISDERECHA PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0]=Tipo(t[3],t[7])\n"
    print(t[3])
    print(t[7])
    t[0]=Tipo(t[3],t[7])

#debo agregar estos al arbol y a la 3D
#--------------------------------------------------------------------------------------------------------------------
#                                           AGREGACION DEL UNION
def p_combinacionSelects(t):
    '''combinacionSelects  : selectData UNION selectData
                            | selectData INTERSECT selectData
                            | selectData EXCEPT selectData
     
    '''
    print("*************************Entra a procesar el UNION********************")
    if t[2].upper()=="UNION":
        t[0]=QueryUnion(t[1],t[3])
    elif t[2].upper()=="INTERSECT":
        t[0]=QueryIntersect(t[1],t[3])
    elif t[2].upper()=="EXCEPT":
        t[0]=QueryExcept(t[1],t[3])


def p_select_4(t):
    '''selectData       : SELECT select_list FROM   tipoJoin
                        | SELECT POR FROM  tipoJoin
    '''
    if t[2]=='*':
       print("entro al select * tipo join ++++++++++++++++++++++++++++++")
       print(t[2])
       t[0]=Select6(t[2],t[4])
    else:
        print("entro al select lista tipo join ++++++++++++++++++++++++++++++")
        print(t[2])
        t[0]=Select6(t[2],t[4])
        


def p_tipoJoin_1(t):
    '''tipoJoin   :   select_list  INNER JOIN select_list ON operacion
                  |   select_list NATURAL INNER JOIN select_list 
     '''
    if t[2].upper()=="INNER":
        print("entro al tipoJoin1 INNER----------------------------------------------------")
        print(t[1])
        print(t[2])
        print(t[4])
        print(t[6])
        t[0]=ExpresionJoinA(t[1],t[2],t[4],t[6])
    elif t[2].upper()=="NATURAL":
        print("entro al NATURAL ----------------------------------------------------")
        print(t[1])
        print(t[2])
        print(t[3])
        print(t[5])    
        t[0]=ExpresionJoinB(t[1],t[2],t[3],t[5])


def p_tipoJoin_2(t):
    '''tipoJoin   :  select_list  otroTipoJoin OUTER JOIN select_list ON operacion
                  |  select_list  NATURAL otroTipoJoin OUTER JOIN select_list
    '''
    if t[2].upper()=="NATURAL":
        print("entro al tipoJoin2 NATURAL ----------------------------------------------------")
        print(t[1])
        print(t[2])
        print(t[3])
        print(t[4])
        print(t[6])
        t[0]=ExpresionJoinC(t[1],t[2],t[3],t[4],t[6])
    else:
        print("entro al tipoJoin2 ELSE ----------------------------------------------------")
        print(t[1])
        print(t[2])
        print(t[3])
        print(t[5])
        print(t[7])
        t[0]=ExpresionJoinD(t[1],t[2],t[3],t[5],t[7])
    


def p_otroTipoJoin(t):
    ''' otroTipoJoin    :   LEFT
                        |   RIGHT
                        |   FULL
    '''
    print("entra al otro tipo de join para su condicion")
    t[0]=t[1]
    
def p_execFunction(t):
    'execFunction    : execOption ID PUNTOYCOMA'
    h.reporteGramatical1 +="execFunction ::= execOption ID PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0]=execFunction(t[2])\n"
    t[0]=execFunction(t[2])

def p_execFunction_1(t):
    'execFunction    : execOption ID PARENTESISIZQUIERDA listaid PARENTESISDERECHA PUNTOYCOMA'
    h.reporteGramatical1 +="execFunction    ::=     execOption ID PARENTESISIZQUIERDA listaid PARENTESISDERECHA PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0]=execFunctionParams(t[2],t[4])\n"
    t[0]=execFunctionParams(t[2],t[4])

def p_execFunction_2(t):
    'execFunction    : execOption ID PARENTESISIZQUIERDA PARENTESISDERECHA PUNTOYCOMA'
    h.reporteGramatical1 +="execFunction    ::=     execOption ID PARENTESISIZQUIERDA PARENTESISDERECHA PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0]=execFunction(t[2])\n"
    t[0]=execFunction(t[2])

def p_execOption_1(t):
    'execOption : EXEC'
    t[0] = t[1]
def p_execOption_2(t):
    'execOption : EXECUTE'
    t[0] = t[1]

#para manejar los errores sintacticos
#def p_error(t): #en modo panico :v
  #  print("token error: ",t)
   # print("Error sintáctico en '%s'" % t.value[0])
   # print("Error sintáctico en '%s'" % t.value[1])
    

#def p_error(t): #en modo panico :v
#   while True:
#        tok=parser.token()
#        if not tok or tok.type==';':break
#    parser.errok()
#    return tok
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    print((token.lexpos - line_start) +1 )
    return (token.lexpos - line_start) 


def p_error(t):
     print("token: '%s'" %t)
     print("Error sintáctico en '%s' " % t.value)
     #h.filapivote+=1
     x=caden.splitlines()
     filas=len(x)-1
     print("filas que no cambian: ",filas)
     
     if h.filapivote>0:
         fila=(t.lineno-1)-h.filapivote*filas
     else:
         fila=(t.lineno-1)
     h.filapivote+=1
     h.errores+=  "<tr><td>"+str(t.value)+"</td><td>"+str(fila)+"</td><td>"+str(find_column(caden,t))+"</td><td>SINTACTICO</td><td>el token no va aqui</td></tr>\n"
     print("Error sintáctico fila '%s'" % fila)
     print("Error sintáctico col '%s'" % find_column(caden,t))
     if not t:
         print("End of File!")
         return
     # Read ahead looking for a closing '}'
     while True:
         tok = parser.token()             # Get the next token
         if not tok or tok.type == 'PUNTOYCOMA': 
             break
     parser.restart()
     
import ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    global caden
    caden=""
    caden=input
    return parser.parse(input)