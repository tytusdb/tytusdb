import re
from queries import *
from expresiones import *
from nodeAst import nodeAst


class gramaticaAscendenteTree:
    text = ""
    textInput = ""
    errorList = {}
    tree = nodeAst()
    symbolTable = {}
    gramReport = {}
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
    'alias' : 'ALIAS',
    'return' : 'RETURN'
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
    nodeFather = nodeAst()
    nodeFather.token = 'INICIO'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] =nodeFather
    gramaticaAscendenteTree.tree.root = t[0]
    
def p_queries_1(t) :
    'queries               : queries query'
    nodeFather = nodeAst()
    nodeFather.token = 'QUERIES'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather

def p_queries_2(t) :
    'queries               : query'    
    nodeFather = nodeAst()
    nodeFather.token = 'QUERIES'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)
    t[0] = nodeFather
 
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
                    | tipoAlter                    
                    | selectData PUNTOYCOMA
                    | tipos
                    | createIndex
                    | alterIndex
                    | dropIndex
                    | combinacionSelects PUNTOYCOMA
                    | execFunction
                    | if
                    
                    
    '''
    nodeFather = nodeAst()
    nodeFather.token = 'QUERY'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)
    t[0] = nodeFather
#-----------------------------------------------------CREATE INDEX--------------------------------------------------------------------
def p_createIndex_1(t):
    'createIndex    : CREATE INDEX ID ON ID PARENTESISIZQUIERDA lower PARENTESISDERECHA PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREATE_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INDEX'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'ON'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ID'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon7 = t[7]
    nodeFather.son.append(nodeSon7)

    t[0] = nodeFather



def p_createIndex_1_1(t):
    'createIndex    : CREATE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREATE_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INDEX'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'ON'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ID'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon7 = nodeAst()
    nodeSon7.token = 'ID'
    nodeSon7.lexeme = t[7]
    nodeFather.son.append(nodeSon7)

    nodeSon8 = t[8]
    nodeFather.son.append(nodeSon8)

    t[0] = nodeFather

def p_createIndex_1_2(t):
    'createIndex    : CREATE INDEX ID ON ID PARENTESISIZQUIERDA lower PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREATE_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INDEX'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'ON'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ID'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon7 = t[7]
    nodeFather.son.append(nodeSon7)

    nodeSon9 = nodeAst()
    nodeSon9.token = 'WHERE'
    nodeSon9.lexeme = t[9]
    nodeFather.son.append(nodeSon9)

    nodeSon10 = t[10]
    nodeFather.son.append(nodeSon10)

    t[0] = nodeFather

def p_createIndex_1_1_2(t):
    'createIndex    : CREATE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA WHERE whereOptions  PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREATE_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INDEX'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'ON'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ID'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon7 = nodeAst()
    nodeSon7.token = 'ID'
    nodeSon7.lexeme = t[7]
    nodeFather.son.append(nodeSon7)

    nodeSon8 = t[8]
    nodeFather.son.append(nodeSon8)

    nodeSon10 = nodeAst()
    nodeSon10.token = 'WHERE'
    nodeSon10.lexeme = t[10]
    nodeFather.son.append(nodeSon10)

    nodeSon11 = t[11]
    nodeFather.son.append(nodeSon11)

    t[0] = nodeFather

def p_createIndex_2(t):
    'createIndex    : CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA lower PARENTESISDERECHA PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREATE_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INDEX'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'ON'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ID'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'USING'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon7 = nodeAst()
    nodeSon7.token = 'HASH'
    nodeSon7.lexeme = t[7]
    nodeFather.son.append(nodeSon7)

    nodeSon9 = t[9]
    nodeFather.son.append(nodeSon9)

    t[0] = nodeFather

def p_createIndex_2_1(t):
    'createIndex    : CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREATE_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INDEX'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'ON'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ID'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'USING'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon7 = nodeAst()
    nodeSon7.token = 'HASH'
    nodeSon7.lexeme = t[7]
    nodeFather.son.append(nodeSon7)

    nodeSon9 = nodeAst()
    nodeSon9.token = 'ID'
    nodeSon9.lexeme = t[9]
    nodeFather.son.append(nodeSon9)

    nodeSon10 = t[10]
    nodeFather.son.append(nodeSon10)

    t[0] = nodeFather

def p_createIndex_2_2(t):
    'createIndex    : CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA lower PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREATE_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INDEX'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'ON'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ID'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'USING'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon7 = nodeAst()
    nodeSon7.token = 'HASH'
    nodeSon7.lexeme = t[7]
    nodeFather.son.append(nodeSon7)

    nodeSon9 = t[9]
    nodeFather.son.append(nodeSon9)

    nodeSon11 = nodeAst()
    nodeSon11.token = 'WHERE'
    nodeSon11.lexeme = t[11]
    nodeFather.son.append(nodeSon11)

    nodeSon12 = t[12]
    nodeFather.son.append(nodeSon12)

    t[0] = nodeFather

def p_createIndex_2_1_2(t):
    'createIndex    : CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREATE_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INDEX'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'ON'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ID'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'USING'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon7 = nodeAst()
    nodeSon7.token = 'HASH'
    nodeSon7.lexeme = t[7]
    nodeFather.son.append(nodeSon7)

    nodeSon9 = nodeAst()
    nodeSon9.token = 'ID'
    nodeSon9.lexeme = t[9]
    nodeFather.son.append(nodeSon9)

    nodeSon10 = t[10]
    nodeFather.son.append(nodeSon10)

    nodeSon12 = nodeAst()
    nodeSon12.token = 'WHERE'
    nodeSon12.lexeme = t[12]
    nodeFather.son.append(nodeSon12)

    nodeSon13 = t[13]
    nodeFather.son.append(nodeSon13)

    t[0] = nodeFather

def p_createIndex_3(t):
    'createIndex    : CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA lower PARENTESISDERECHA PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREATE_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'UNIQUE'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'INDEX'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'ID'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ON'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'ID'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon8 = t[8]
    nodeFather.son.append(nodeSon8)

    t[0] = nodeFather

def p_createIndex_3_1(t):
    'createIndex    : CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREATE_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'UNIQUE'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'INDEX'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'ID'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ON'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'ID'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon8 = nodeAst()
    nodeSon8.token = 'ID'
    nodeSon8.lexeme = t[8]
    nodeFather.son.append(nodeSon8)

    nodeSon9 = t[9]
    nodeFather.son.append(nodeSon9)

    t[0] = nodeFather

def p_createIndex_3_2(t):
    'createIndex    : CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA lower PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREATE_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'UNIQUE'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'INDEX'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'ID'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ON'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'ID'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon8 = t[8]
    nodeFather.son.append(nodeSon8)

    nodeSon10 = nodeAst()
    nodeSon10.token = 'WHERE'
    nodeSon10.lexeme = t[10]
    nodeFather.son.append(nodeSon10)

    nodeSon11 = t[11]
    nodeFather.son.append(nodeSon11)

    t[0] = nodeFather

def p_createIndex_3_1_2(t):
    'createIndex    : CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREATE_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'UNIQUE'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'INDEX'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'ID'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ON'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'ID'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon8 = nodeAst()
    nodeSon8.token = 'ID'
    nodeSon8.lexeme = t[8]
    nodeFather.son.append(nodeSon8)

    nodeSon9 = t[9]
    nodeFather.son.append(nodeSon9)

    nodeSon11 = nodeAst()
    nodeSon11.token = 'WHERE'
    nodeSon11.lexeme = t[11]
    nodeFather.son.append(nodeSon11)

    nodeSon12 = t[12]
    nodeFather.son.append(nodeSon12)

    t[0] = nodeFather

# -------------------------------------------------------------DROP INDEX--------------------------------------------------------
def p_dropIndex(t):
    'dropIndex    : DROP INDEX ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'DROP_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'DROP'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INDEX'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather

def p_dropIndex_1(t):
    'dropIndex    : DROP INDEX IF EXISTS ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'DROP_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'DROP'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INDEX'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'IF'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'EXISTS'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ID'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    t[0] = nodeFather

# ------------------------------------------------------------ALTER INDEX---------------------------------------------------------
def p_alterIndex(t):
    'alterIndex    : ALTER INDEX ID RENAME TO ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'ALTER_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ALTER'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INDEX'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'RENAME'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'TO'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'ID'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    t[0] = nodeFather

def p_alterIndex_1(t):
    'alterIndex    : ALTER INDEX IF EXISTS ID RENAME TO ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'ALTER_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ALTER'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INDEX'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'IF'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'EXISTS'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ID'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'RENAME'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon7 = nodeAst()
    nodeSon7.token = 'TO'
    nodeSon7.lexeme = t[7]
    nodeFather.son.append(nodeSon7)

    nodeSon8 = nodeAst()
    nodeSon8.token = 'ID'
    nodeSon8.lexeme = t[8]
    nodeFather.son.append(nodeSon8)

    t[0] = nodeFather
# ------------------------------------------------------ALTER INDEX COLUMN ----------------------------------------------------
def p_alterIndex_2(t):
    'alterIndex    : ALTER INDEX ID ALTER ID final PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'ALTER_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ALTER'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INDEX'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'ALTER'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ID'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = t[6]
    nodeFather.son.append(nodeSon6)

    t[0] = nodeFather

def p_alterIndex_3(t):
    'alterIndex    : ALTER INDEX ID ALTER COLUMN ID final PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'ALTER_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ALTER'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INDEX'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'ALTER'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'COLUMN'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'ID'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon7 = t[7]
    nodeFather.son.append(nodeSon7)

    t[0] = nodeFather

def p_alterIndex_4(t):
    'alterIndex    : ALTER INDEX IF EXISTS ID ALTER ID final PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'ALTER_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ALTER'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INDEX'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'IF'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'EXISTS'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ID'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'ALTER'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon7 = nodeAst()
    nodeSon7.token = 'ID'
    nodeSon7.lexeme = t[7]
    nodeFather.son.append(nodeSon7)

    nodeSon8 = t[8]
    nodeFather.son.append(nodeSon8)

    t[0] = nodeFather

def p_alterIndex_5(t):
    'alterIndex    : ALTER INDEX IF EXISTS ID ALTER COLUMN ID final PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'ALTER_INDEX'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ALTER'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INDEX'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'IF'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'EXISTS'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ID'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'ALTER'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon7 = nodeAst()
    nodeSon7.token = 'COLUMN'
    nodeSon7.lexeme = t[7]
    nodeFather.son.append(nodeSon7)

    nodeSon8 = nodeAst()
    nodeSon8.token = 'ID'
    nodeSon8.lexeme = t[8]
    nodeFather.son.append(nodeSon8)


    nodeSon9 = t[9]
    nodeFather.son.append(nodeSon9)

    t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------------------------
def p_indexParams(t):
    'indexParams    : sort'
    nodeFather = nodeAst()
    nodeFather.token = 'INDEX_PARAMS'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather
def p_whereOptions_1(t):
    'whereOptions    : asignaciones'
    nodeFather = nodeAst()
    nodeFather.token = 'WHERE_OPTIONS'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather
def p_whereOptions_2(t):
    'whereOptions    : operacion'
    nodeFather = nodeAst()
    nodeFather.token = 'WHERE_OPTIONS'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather
def p_whereOptions_3(t):
    'whereOptions    : search_condition'
    nodeFather = nodeAst()
    nodeFather.token = 'WHERE_OPTIONS'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather
def p_sortOptions_1(t):
    'sort    : NULLS FIRST'
    nodeFather = nodeAst()
    nodeFather.token = 'SORT'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'NULLS'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'FIRST'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather

def p_sortOptions_1_1(t):
    'sort    : DESC NULLS FIRST'
    nodeFather = nodeAst()
    nodeFather.token = 'SORT'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'DESC'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'NULLS'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'FIRST'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather

def p_sortOptions_1_2(t):
    'sort    : ASC NULLS FIRST'
    nodeFather = nodeAst()
    nodeFather.token = 'SORT'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ASC'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'NULLS'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'FIRST'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather

def p_sortOptions_2(t):
    'sort    : NULLS LAST'
    nodeFather = nodeAst()
    nodeFather.token = 'SORT'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'NULLS'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'LAST'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather

def p_sortOptions_2_1(t):
    'sort    : DESC NULLS LAST'
    nodeFather = nodeAst()
    nodeFather.token = 'SORT'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'DESC'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'NULLS'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'LAST'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather

def p_sortOptions_2_2(t):
    'sort    : ASC NULLS LAST'
    nodeFather = nodeAst()
    nodeFather.token = 'SORT'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ASC'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'NULLS'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'LAST'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather

def p_lower(t):
    'lower    : lower COMA low'
    nodeFather = nodeAst()
    nodeFather.token = 'LISTA_ID'
        
    nodeSon1  = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon3 = t[3]
    nodeFather.son.append(nodeSon3)

    t[0]=nodeFather

def p_lower_1(t):
    'lower    : low'
    nodeFather = nodeAst()
    nodeFather.token = 'LISTA_ID'
        
    nodeSon1  = t[1]
    nodeFather.son.append(nodeSon1)

    t[0]=nodeFather


def p_low(t):
    'low    : ID PARENTESISIZQUIERDA ID PARENTESISDERECHA'
    nodeFather = nodeAst()
    nodeFather.token = 'IDS'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ID'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather

def p_low_1(t):
    'low    : ID'
    nodeFather = nodeAst()
    nodeFather.token = 'IDS'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ID'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather
#-----------------------------------------------------CREATE DB--------------------------------------------------------------------
def p_crearBaseDatos_1(t):
    'crearBD    : CREATE DATABASE ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREAR_BD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'DATABASE'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather

def p_crearBaseDatos_2(t):
    'crearBD    : CREATE DATABASE IF NOT EXISTS ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREAR_BD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'DATABASE'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'IF'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'NOT'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'EXISTS'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'ID'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    t[0] = nodeFather   
def p_crear_replace_BaseDatos_1(t):
    'crearBD    : CREATE OR REPLACE DATABASE ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREAR_BD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'OR'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'REPLACE'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'DATABASE'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ID'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    t[0] = nodeFather

def p_crear_replace_BaseDatos_2(t):
    'crearBD    : CREATE OR REPLACE DATABASE IF NOT EXISTS ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREAR_BD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'OR'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'REPLACE'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'DATABASE'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'IF'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'NOT'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon7 = nodeAst()
    nodeSon7.token = 'EXISTS'
    nodeSon7.lexeme = t[7]
    nodeFather.son.append(nodeSon7)

    nodeSon8 = nodeAst()
    nodeSon8.token = 'ID'
    nodeSon8.lexeme = t[8]
    nodeFather.son.append(nodeSon8)

    t[0] = nodeFather

def p_crear_param_BaseDatos_1(t):
    'crearBD    : CREATE  DATABASE ID parametrosCrearBD PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREAR_BD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'DATABASE'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = t[4]
    nodeFather.son.append(nodeSon4)

    t[0] = nodeFather

def p_crear_param_BaseDatos_2(t):
    'crearBD    : CREATE  DATABASE IF NOT EXISTS ID parametrosCrearBD PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREAR_BD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'DATABASE'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'IF'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'NOT'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'EXISTS'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'ID'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon7 = t[7]
    nodeFather.son.append(nodeSon7)

    t[0] = nodeFather

def p_crear_replace_param_BaseDatos_1(t):
    'crearBD    : CREATE OR REPLACE DATABASE ID parametrosCrearBD PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREAR_BD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'OR'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'REPLACE'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'DATABASE'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ID'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = t[6]
    nodeFather.son.append(nodeSon6)

    t[0] = nodeFather

def p_crear_replace_param_BaseDatos_2(t):
    'crearBD    : CREATE OR REPLACE DATABASE IF NOT EXISTS ID parametrosCrearBD PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREARBD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'OR'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'REPLACE'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'DATABASE'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'IF'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'NOT'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon7 = nodeAst()
    nodeSon7.token = 'EXISTS'
    nodeSon7.lexeme = t[7]
    nodeFather.son.append(nodeSon7)

    nodeSon8 = nodeAst()
    nodeSon8.token = 'ID'
    nodeSon8.lexeme = t[8]
    nodeFather.son.append(nodeSon8)


    nodeSon9 = t[9]
    nodeFather.son.append(nodeSon9)

    t[0] = nodeFather
def p_parametrosCrearBD_1(t):
    'parametrosCrearBD : parametrosCrearBD parametroCrearBD'
    nodeFather = nodeAst()
    nodeFather.token = 'PARAMETROS_CREAR_BD'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)
    t[0] = nodeFather

def p_parametrosCrearBD_2(t):
    'parametrosCrearBD :  parametroCrearBD'
    nodeFather = nodeAst()
    nodeFather.token = 'PARAMETROS_CREAR_BD'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)
    
    t[0] = nodeFather

def p_parametroCrearBD(t):
    '''parametroCrearBD :  OWNER IGUAL final
                        |  MODE IGUAL final
    '''    
    if t[1] == "OWNER":
        nodeFather = nodeAst()
        nodeFather.token = 'PARAMETRO_CREAR_BD'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'OWNER'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
    elif t[1] == "MODE":
        nodeFather = nodeAst()
        nodeFather.token = 'PARAMETRO_CREAR_BD'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'MODE'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
#-----------------------------------------------------SHOW DB--------------------------------------------------------------------
def p_usarBaseDatos(t):
    'useBD    : USE ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'USE_BD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'USE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'ID'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)
    
    t[0] = nodeFather
#-----------------------------------------------------SHOW DB--------------------------------------------------------------------
def p_mostrarBD(t):
    'mostrarBD  : SHOW DATABASES PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'SHOW_DB'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'SHOW'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'DATABASES'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)
    
    t[0] = nodeFather
#-----------------------------------------------------ALTER BD--------------------------------------------------------------------
def p_alterBD_1(t):
    'alterBD    : ALTER DATABASE ID RENAME TO ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'ALTER_DB'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ALTER'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'DATABASE'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'RENAME'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'TO'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'ID'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)
    
    t[0] = nodeFather

def p_alterBD_2(t):
    'alterBD    : ALTER DATABASE ID OWNER TO parametroAlterUser PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'ALTER_DB'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ALTER'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'DATABASE'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'OWNER'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'TO'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = t[6]
    nodeFather.son.append(nodeSon6)
    
    t[0] = nodeFather

def p_parametroAlterUser_1(t):   
    
    ' parametroAlterUser : CURRENT_USER '
    nodeFather = nodeAst()
    nodeFather.token = 'PARAMETRO_ALTER_USER'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CURRENT_USER'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)
    
    t[0] = nodeFather

def p_parametroAlterUser_2(t):
    '''
    parametroAlterUser : SESSION_USER
    '''
    nodeFather = nodeAst()
    nodeFather.token = 'PARAMETRO_ALTER_USER'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'SESSION_USER'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)
    
    t[0] = nodeFather


def p_parametroAlterUser_3(t):
    '''parametroAlterUser : final    '''
    nodeFather = nodeAst()
    nodeFather.token = 'PARAMETRO_ALTER_USER'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)
    
    t[0] = nodeFather
#-----------------------------------------------------DROP TABLE-----------------------------------------------------------------
def p_dropTable(t) :
    'dropTable  : DROP TABLE ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'DROP_TABLE'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'DROP'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'TABLE'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    t[0]=nodeFather
#-----------------------------------------------------ALTER TABLE-----------------------------------------------------------------
def p_alterTable(t):
    '''
    alterTable  : ALTER TABLE ID variantesAt PUNTOYCOMA

    '''
    nodeFather = nodeAst()
    nodeFather.token = 'ALTER_TABLE'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ALTER'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)
 
    nodeSon2 = nodeAst()
    nodeSon2.token = 'TABLE'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = t[4]
    nodeFather.son.append(nodeSon4)

    t[0]=nodeFather

   

#---------------------------------------------------TIPOS------------------------------------------------------------------------
def p_variantesAt_1(t):
    '''
    variantesAt :   ADD contAdd
    '''
    nodeFather = nodeAst()
    nodeFather.token = 'VARIANTES_AT'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ADD'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)
 
    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)

    t[0]=nodeFather

def p_variantesAt_2(t):
    '''
    variantesAt :   ALTER contAlter
    '''
    nodeFather = nodeAst()
    nodeFather.token = 'VARIANTES_AT'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ALTER'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)
 
    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)

    t[0]=nodeFather

def p_variantesAt_3(t):
    '''
    variantesAt : DROP contDrop
    '''
    nodeFather = nodeAst()
    nodeFather.token = 'VARIANTES_AT'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'DROP'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)
 
    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)

    t[0]=nodeFather

#---------------------------------------------STATEMENT IF -------------------------------------------------------

#---------------------------------------------TERMINAN STATEMENTS BYRON ------------------------------------------    
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
        nodeFather = nodeAst()
        nodeFather.token = 'CONT_ALTER'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'COLUMN'
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'ID'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'SET'
        nodeSon3.lexeme = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = nodeAst()
        nodeSon4.token = 'NOT'
        nodeSon4.lexeme = t[4]
        nodeFather.son.append(nodeSon4)

        nodeSon5 = nodeAst()
        nodeSon5.token = 'NULL'
        nodeSon5.lexeme = t[5]
        nodeFather.son.append(nodeSon5)

        t[0]=nodeFather

    elif t[3].upper()=="TYPE":
        nodeFather = nodeAst()
        nodeFather.token = 'CONT_ALTER'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'COLUMN'
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'ID'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'TYPE'
        nodeSon3.lexeme = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = t[4]
        nodeFather.son.append(nodeSon4)

        t[0]=nodeFather


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
    nodeFather = nodeAst()
    nodeFather.token = "CONT_ADD"
    
    if t[1].upper()=="COLUMN":

        nodeSon1 = nodeAst()
        nodeSon1.token = 'COLUMN'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'ID'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)
    
        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0]=nodeFather

    elif t[1].upper()=="CHECK":
        nodeSon1 = nodeAst()
        nodeSon1.token = 'CHECK'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0]=nodeFather

    elif t[1].upper()=="FOREIGN":

        nodeSon1 = nodeAst()
        nodeSon1.token = 'FOREIGN'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'KEY'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon4 = nodeAst()
        nodeSon4.token = 'ID'
        nodeSon4.lexeme = t[4]
        nodeFather.son.append(nodeSon4)
    
        nodeSon6 = nodeAst()
        nodeSon6.token = 'REFERENCES'
        nodeSon6.lexeme = t[6]
        nodeFather.son.append(nodeSon6)

        nodeSon7 = nodeAst()
        nodeSon7.token = 'ID'
        nodeSon7.lexeme = t[7]
        nodeFather.son.append(nodeSon7)

        t[0]=nodeFather

    elif t[1].upper()=="PRIMARY":

        nodeSon1 = nodeAst()
        nodeSon1.token = 'PRIMARY'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'KEY'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon4 = nodeAst()
        nodeSon4.token = "ID"
        nodeSon4.lexeme = t[4]
        nodeFather.son.append(nodeSon4)

        t[0]=nodeFather

    elif t[1].upper()=="CONSTRAINT":
        
        nodeSon1 = nodeAst()
        nodeSon1.token = 'CONSTRAINT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'ID'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        if t[3].upper()=="PRIMARY":

            nodeSon3 = nodeAst()
            nodeSon3.token = 'PRIMARY'
            nodeSon3.lexeme = t[3]
            nodeFather.son.append(nodeSon3)

            nodeSon4 = nodeAst()
            nodeSon4.token = 'KEY'
            nodeSon4.lexeme = t[4]
            nodeFather.son.append(nodeSon4)
    
            nodeSon6 = nodeAst()
            nodeSon6.token = "ID"
            nodeSon6.lexeme = t[6]
            nodeFather.son.append(nodeSon6)

            t[0]=nodeFather

        elif t[3].upper()=="FOREIGN":

            nodeSon3 = nodeAst()
            nodeSon3.token = 'FOREIGN'
            nodeSon3.lexeme = t[3]
            nodeFather.son.append(nodeSon3)

            nodeSon4 = nodeAst()
            nodeSon4.token = 'KEY'
            nodeSon4.lexeme = t[4]
            nodeFather.son.append(nodeSon4)
    
            nodeSon6 = nodeAst()
            nodeSon6.token = "ID"
            nodeSon6.lexeme = t[6]
            nodeFather.son.append(nodeSon6)

            nodeSon8 = nodeAst()
            nodeSon8.token = "REFERENCES"
            nodeSon8.lexeme = t[8]
            nodeFather.son.append(nodeSon8)

            nodeSon9 = nodeAst()
            nodeSon9.token = "ID"
            nodeSon9.lexeme = t[9]
            nodeFather.son.append(nodeSon9)

            nodeSon11 = nodeAst()
            nodeSon11.token = "ID"
            nodeSon11.lexeme = t[11]
            nodeFather.son.append(nodeSon11)

            t[0]=nodeFather
        else:
            nodeSon3 = nodeAst()
            nodeSon3.token = 'UNIQUE'
            nodeSon3.lexeme = t[3]
            nodeFather.son.append(nodeSon3)

            nodeSon5 = nodeAst()
            nodeSon5.token = 'ID'
            nodeSon5.lexeme = t[5]
            nodeFather.son.append(nodeSon5)
    
            t[0]=nodeFather
        
def p_contDrop(t):
    '''
    contDrop    : COLUMN ID 
                | CONSTRAINT ID
                | PRIMARY KEY
    '''
    if t[1].upper()=="COLUMN":

        nodeFather = nodeAst()
        nodeFather.token = 'CONT_DROP'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'COLUMN'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'ID'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        t[0]=nodeFather
        
    elif t[1].upper()=="CONSTRAINT":
        nodeFather = nodeAst()
        nodeFather.token = 'CONT_DROP'
        
        nodeSon1 = nodeAst()
        nodeSon1.token = 'CONSTRAINT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'ID'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        t[0]=nodeFather

    elif t[1].upper()=="PRIMARY":
        nodeFather = nodeAst()
        nodeFather.token = 'CONT_DROP'
        
        nodeSon1 = nodeAst()
        nodeSon1.token = 'PRIMARY'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'KEY'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        t[0]=nodeFather
#---------------------------------------------- STATEMENT IF -----------------------------------------------
def p_if_1(t):
    '''
    if          :  IF  operacion THEN operacion END IF PUNTOYCOMA
    ''' 
    nodeFather = nodeAst()
    nodeFather.token = 'IF'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'IF'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'THEN'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'END'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'IF'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon7 = nodeAst()
    nodeSon7.token = ';'
    nodeSon7.lexeme = t[7]
    nodeFather.son.append(nodeSon7)

    t[0]=nodeFather
def p_if_2(t):
    '''
    if          : IF operacion THEN operacion ELSE if 
    '''
    nodeFather = nodeAst()
    nodeFather.token = 'IF'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'IF'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'THEN'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ELSE'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = t[6]
    nodeFather.son.append(nodeSon6)
    t[0] = nodeFather

def p_if_3(t):
    '''
    if          : IF operacion THEN operacion ELSE operacion END IF PUNTOYCOMA
    '''
    nodeFather = nodeAst()
    nodeFather.token = 'IF'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'IF'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'THEN'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ELSE'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = t[6]
    nodeFather.son.append(nodeSon6)
    
    nodeSon51 = nodeAst()
    nodeSon51.token = 'END'
    nodeSon51.lexeme = t[7]
    nodeFather.son.append(nodeSon51)

    nodeSon61 = nodeAst()
    nodeSon61.token = 'IF'
    nodeSon61.lexeme = t[8]
    nodeFather.son.append(nodeSon61)

    nodeSon7 = nodeAst()
    nodeSon7.token = ';'
    nodeSon7.lexeme = t[9]
    nodeFather.son.append(nodeSon7)

    t[0]= nodeFather
#---------------------------------------------- STATEMENT IF TERMINA ---------------------------------------
#-----------------------------------------------------STATEMENT CASE--------------------------------------------------------------------

#-----------------------------------------------------STATEMENT CASE TERMINA--------------------------------------------------------------------
# SE SEPARO LA LISTA PARA PODER MANIPULAR DATOS
def p_listaID(t):
    '''
    listaid     :   listaid COMA final
    '''
    nodeFather = nodeAst()
    nodeFather.token = 'LISTA_ID'
        
    nodeSon1  = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon3 = t[3]
    nodeFather.son.append(nodeSon3)

    t[0]=nodeFather

def p_listaID_2(t):
    '''
    listaid     :   final
    '''
    nodeFather = nodeAst()
    nodeFather.token = 'LISTA_ID'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0]=nodeFather
#-----------------------------------------------------STATEMENT CASE--------------------------------------------------------------------    
#-----------------------------------------------------DROP BD--------------------------------------------------------------------
def p_tipoAlter(t):
    '''
    tipoAlter   :   ADD 
                |   DROP
    '''
    h.reporteGramatical1 +="operacion    ::=       final\n"
#-----------------------------------------------------Tipo Alter--------------------------------------------------------------------
def p_dropBD_1(t):
    'dropBD    : DROP DATABASE ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'DROP_DB'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'DROP'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'DATABASE'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)
    
    t[0] = nodeFather


def p_dropBD_2(t):
    'dropBD    : DROP DATABASE IF EXISTS ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'DROP_DB'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'DROP'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'DATABASE'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'IF'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'EXISTS'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ID'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)
    
    t[0] = nodeFather
#-----------------------------------------------------OPERACIONES Y EXPRESIONES--------------------------------------------------------------------
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
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'MAS'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                                  
    elif t[2]=='-':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'MENOS'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='*':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'POR'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='/':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'DIV'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='%':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'MOD'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='^':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'POW'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=="AND":
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'AND'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=="OR":
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'OR'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='|':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'OR'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='||':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'OR'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='&':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'AND'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='<<':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'L_SHIFT'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='>>':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'R_SHIFT'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='=':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'IGUAL'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather        
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='==':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'EQUAL'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                            
    elif t[2]=='!=':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'NOT_EQ'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='>=':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'MAY_IQ'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='<=':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'MEN_IQ'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='>':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'MAY_Q'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='<':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'MEN_Q'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                                  
    elif t[2]=='<>':
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'DIF'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                          
    else:
        nodeFather = nodeAst()
        nodeFather.token = 'OPERACION'

        nodeSon2 = t[2]
        nodeFather.son.append(nodeSon2)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                              
def p_operacion_menos_unario_entero(t):
    '''operacion : MENOS ENTERO  %prec UMINUS'''
    nodeFather = nodeAst()
    nodeFather.token = 'OPERACION'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'MENOS'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'ENTERO'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)
    
    t[0] = nodeFather 
def p_operacion_menos_unario_decimal(t):
    '''operacion : MENOS DECIMAL  %prec UMINUS''' 
    nodeFather = nodeAst()
    nodeFather.token = 'OPERACION'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'MENOS'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'DECIMAL'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)
    
    t[0] = nodeFather
	
	
	
def p_operacion_not_unario(t):
    'operacion : NOT operacion %prec UNOT'
    nodeFather = nodeAst()
    nodeFather.token = 'OPERACION'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'NOT'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)
    
    t[0] = nodeFather
	
def p_operacion_funcion(t):
    'operacion  : funcionBasica'
    nodeFather = nodeAst()
    nodeFather.token = 'OPERACION'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather
	
	
def p_operacion_final(t):
    'operacion :     final'
    nodeFather = nodeAst()
    nodeFather.token = 'OPERACION'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather
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
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'ABS'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
        
        t[0] = nodeFather 
    elif t[1].upper()=="CBRT":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'CBRT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
        
        t[0] = nodeFather 
    elif t[1].upper()=="CEIL":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'CEIL'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
        
        t[0] = nodeFather 
    elif t[1].upper()=="CEILING":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'CEILING'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
        
        t[0] = nodeFather 
    elif t[1].upper()=="DEGREES":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'DEGREES'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon5 = t[5]
        nodeFather.son.append(nodeSon5)

        t[0] = nodeFather 
    elif t[1].upper()=="DIV":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'DIV'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
        
        t[0] = nodeFather 
    elif t[1].upper()=="EXP":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'EXP'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
        
        t[0] = nodeFather 
    elif t[1].upper()=="FACTORIAL":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'FACTORIAL'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
        
        t[0] = nodeFather 
    elif t[1].upper()=="FLOOR":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'FLOOR'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather 
    elif t[1].upper()=="GCD":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'GCD'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon5 = t[5]
        nodeFather.son.append(nodeSon5)

        t[0] = nodeFather 
    elif t[1].upper()=="LN":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'LN'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="LOG":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'LOG'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather  
    elif t[1].upper()=="MOD":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'MOD'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon5 = t[5]
        nodeFather.son.append(nodeSon5)

        t[0] = nodeFather 
    elif t[1].upper()=="PI":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'PI'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather 
    elif t[1].upper()=="POWER":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'POWER'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon5 = t[5]
        nodeFather.son.append(nodeSon5)

        t[0] = nodeFather 
    elif t[1].upper()=="RADIANS":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'RADIANS'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather  
    elif t[1].upper()=="ROUND":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'ROUND'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather 
    elif t[1].upper()=="SIGN":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SIGN'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather 
    elif t[1].upper()=="SQRT":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SQRT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="TRUNC":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'TRUNC'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="WIDTH_BUCKET":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'WIDTH_BUCKET'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon5 = t[5]
        nodeFather.son.append(nodeSon5)

        nodeSon7 = t[7]
        nodeFather.son.append(nodeSon7)

        nodeSon9 = t[9]
        nodeFather.son.append(nodeSon9)

        t[0] = nodeFather
    elif t[1].upper()=="RANDOM":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'RANDOM'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather
    elif t[1].upper()=="ACOS":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'ACOS'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="ACOSD":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'ACOSD'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="ASIN":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'ASIN'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="ASIND":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'ASIND'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="ATAN":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'ATAN'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="ATAND":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'ATAND'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="ATAN2":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'ATAN2'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="ATAN2D":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'ATAN2D'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="COS":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'COS'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="COSD":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'COSD'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="COT":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'COT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="COTD":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'COTD'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    
    elif t[1].upper()=="SIN":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SIN'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
       
    elif t[1].upper()=="SIND":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SIND'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="TAN":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'TAN'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="TAND":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'TAND'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="SINH":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SINH'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="COSH":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'COSH'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    
    elif t[1].upper()=="TANH":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'TANH'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="ASINH":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'ASINH'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="ACOSH":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'ACOSH'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="ATANH":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'ATANH'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="GREATEST":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'GREATEST'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="LEAST":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'LEAST'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="NOW":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'NOW'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather
    elif t[1].upper()=="LENGTH":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'LENGTH'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="TRIM":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'TRIM'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = t[4]
        nodeFather.son.append(nodeSon4)

        nodeSon5 = nodeAst()
        nodeSon5.token = 'FROM'
        nodeSon5.lexeme = t[5]
        nodeFather.son.append(nodeSon5)

        nodeSon6 = t[6]
        nodeFather.son.append(nodeSon6)

        t[0] = nodeFather
    elif t[1].upper()=="GET_BYTE":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'GET_BYTE'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon5 = t[5]
        nodeFather.son.append(nodeSon5)

        t[0] = nodeFather
    elif t[1].upper()=="MD5":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'MD5'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="SET_BYTE":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SET_BYTE'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon5 = t[5]
        nodeFather.son.append(nodeSon5)

        nodeSon7 = t[7]
        nodeFather.son.append(nodeSon7)

        t[0] = nodeFather
    elif t[1].upper()=="SHA256":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SHA256'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[1].upper()=="SUBSTR":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SUBSTR'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon5 = t[5]
        nodeFather.son.append(nodeSon5)

        nodeSon7 = t[7]
        nodeFather.son.append(nodeSon7)

        t[0] = nodeFather
    elif t[1].upper()=="CONVERT":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'CONVERT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon5 = t[5]
        nodeFather.son.append(nodeSon5)

        nodeSon7 = t[7]
        nodeFather.son.append(nodeSon7)

        t[0] = nodeFather
    elif t[1].upper()=="ENCODE":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'ENCODE'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon5 = t[5]
        nodeFather.son.append(nodeSon5)

        t[0] = nodeFather
    elif t[1].upper()=="DECODE":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'DECODE'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon5 = t[5]
        nodeFather.son.append(nodeSon5)

        t[0] = nodeFather
    elif t[1].upper()=="AVG":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'AVG'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather  
    elif t[1].upper()=="SUM":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SUM'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather  
    elif t[1].upper()=="EXTRACT":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'EXTRACT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = nodeAst()
        nodeSon4.token = 'FROM'
        nodeSon4.lexeme = t[4]
        nodeFather.son.append(nodeSon4)

        nodeSon5 = nodeAst()
        nodeSon5.token = 'TIMESTAMP'
        nodeSon5.lexeme = t[5]
        nodeFather.son.append(nodeSon5)

        nodeSon6 = t[6]
        nodeFather.son.append(nodeSon6)

        t[0] = nodeFather
    elif t[1].upper()=="DATE_PART":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'DATE_PART'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon5 = nodeAst()
        nodeSon5.token = 'INTERVAL'
        nodeSon5.lexeme = t[5]
        nodeFather.son.append(nodeSon5)

        nodeSon6 = t[6]
        nodeFather.son.append(nodeSon6)

        t[0] = nodeFather
    elif t[1].upper()=="CURRENT_DATE":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'CURRENT_DATE'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather
    elif t[1].upper()=="CURRENT_TIME":
        nodeFather = nodeAst()
        nodeFather.token = 'FUNCION_BASICA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'CURRENT_TIME'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather
    else:
        print("no entra a ninguna en funcionBasica")
#JPI



def p_funcion_basica_1(t):
    'funcionBasica   : SUBSTRING PARENTESISIZQUIERDA operacion FROM operacion FOR operacion PARENTESISDERECHA'
    nodeFather = nodeAst()
    nodeFather.token = 'FUNCION_BASICA'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'SUBSTRING'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon3 = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'FROM'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'FOR'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon7 = t[7]
    nodeFather.son.append(nodeSon7)

    t[0] = nodeFather
def p_funcion_basica_2(t):
    'funcionBasica   : SUBSTRING PARENTESISIZQUIERDA operacion FROM operacion PARENTESISDERECHA'
    nodeFather = nodeAst()
    nodeFather.token = 'FUNCION_BASICA'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'SUBSTRING'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon3 = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'FROM'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = t[5]
    nodeFather.son.append(nodeSon5)

    t[0] = nodeFather
def p_funcion_basica_3(t):
    'funcionBasica   : SUBSTRING PARENTESISIZQUIERDA operacion FOR operacion PARENTESISDERECHA'
    nodeFather = nodeAst()
    nodeFather.token = 'FUNCION_BASICA'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'SUBSTRING'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon3 = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'FOR'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = t[5]
    nodeFather.son.append(nodeSon5)

    t[0] = nodeFather
 
def p_opcionTrim(t):
    ''' opcionTrim  : LEADING
                    | TRAILING
                    | BOTH
    '''    
    if t[1].upper()=="LEADING":
        nodeFather = nodeAst()
        nodeFather.token = 'OPCION_TRIM'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'LEADING'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather
    elif t[1].upper()=="TRAILING":
        nodeFather = nodeAst()
        nodeFather.token = 'OPCION_TIEMPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'TRAILING'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather
    elif t[1].upper()=="BOTH":
        nodeFather = nodeAst()
        nodeFather.token = 'OPCION_TIEMPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'BOTH'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

def p_opcionTiempo(t):
    '''opcionTiempo     :   YEAR
                        |   MONTH
                        |   DAY
                        |   HOUR
                        |   MINUTE
                        |   SECOND
    '''
    if t[1].upper()=="YEAR":
        nodeFather = nodeAst()
        nodeFather.token = 'OPCION_TIEMPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'YEAR'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    elif t[1].upper()=="MONTH":
        nodeFather = nodeAst()
        nodeFather.token = 'OPCION_TIEMPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'MONTH'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather
    elif t[1].upper()=="DAY":
        nodeFather = nodeAst()
        nodeFather.token = 'OPCION_TIEMPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'DAY'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather
    elif t[1].upper()=="HOUR":
        nodeFather = nodeAst()
        nodeFather.token = 'OPCION_TIEMPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'HOUR'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather
    elif t[1].upper()=="MINUTE":
        nodeFather = nodeAst()
        nodeFather.token = 'OPCION_TIEMPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'MINUTE'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather
    elif t[1].upper()=="SECOND":
        nodeFather = nodeAst()
        nodeFather.token = 'OPCION_TIEMPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SECOND'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

#-----------------------------------------------------PRODUCCIONES TERMINALES--------------------------------------------------------------------
def p_final_decimal(t):
    '''final        : DECIMAL'''
    nodeFather = nodeAst()
    nodeFather.token = 'FINAL'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'DECIMAL'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)
    
    t[0] = nodeFather

def p_final_entero(t):
    '''final        : ENTERO'''
    nodeFather = nodeAst()
    nodeFather.token = 'FINAL'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ENTERO'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)
    
    t[0] = nodeFather

def p_final_id(t):
    'final          : ID'
    nodeFather = nodeAst()
    nodeFather.token = 'FINAL'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ID'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)
    
    t[0] = nodeFather

def p_final_invocacion(t):
    'final          : ID PUNTO ID'
    nodeFather = nodeAst()
    nodeFather.token = 'FINAL'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ID'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)
    
    t[0] = nodeFather
def p_final_invocacion_2(t):
    'final          : ID PUNTO POR'
    nodeFather = nodeAst()
    nodeFather.token = 'FINAL'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ID'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'POR'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)
    
    t[0] = nodeFather


def p_final_cadena(t):
    'final          : CADENA'
    nodeFather = nodeAst()
    nodeFather.token = 'FINAL'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CADENA'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)
    
    t[0] = nodeFather

#-----------------------------------------------------INSERT BD--------------------------------------------------------------------
def p_insertBD_1(t):
    'insertinBD           : INSERT INTO ID VALUES PARENTESISIZQUIERDA listaParam PARENTESISDERECHA PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'INSERT_IN_BD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'INSERT'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INTO'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'VALUES'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon6 = t[6]
    nodeFather.son.append(nodeSon6)

    t[0] = nodeFather

def p_insertBD_2(t):
    'insertinBD           : INSERT INTO ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA VALUES PARENTESISIZQUIERDA listaParam PARENTESISDERECHA PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'INSERT_IN_BD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'INSERT'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'INTO'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = t[5]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'VALUES'
    nodeSon5.lexeme = t[7]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = t[9]
    nodeFather.son.append(nodeSon6)

    t[0] = nodeFather

# SE SEPARO LA LISTA EN 2 METODOS PARA MANEJAR DATOS
def p_listaParam(t):
    '''listaParam         : listaParam COMA listaP
    '''
    nodeFather = nodeAst()
    nodeFather.token = 'listaParam'
    
    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[3]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather

def p_listaParam_2(t):
    '''listaParam           : listaP
    '''
    nodeFather = nodeAst()
    nodeFather.token = 'listaParam'
    
    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather

def p_listaP_1(t):
    'listaP                 : operacion'
    nodeFather = nodeAst()
    nodeFather.token = 'listaP'
    
    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)
    
    t[0] = nodeFather

def p_listaP_2(t):
    'listaP             : ID operacion'
    nodeFather = nodeAst()
    nodeFather.token = 'listaP'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ID'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)
    
    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)
    
    t[0] = nodeFather
    

def p_listaP_3(t):
    'listaP             : ID PARENTESISIZQUIERDA PARENTESISDERECHA'
    nodeFather = nodeAst()
    nodeFather.token = 'listaP'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ID'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)
    
    t[0] = nodeFather

#-----------------------------------------------------UPDATE BD--------------------------------------------------------------------
def p_updateBD(t):
    'updateinBD           : UPDATE ID SET asignaciones WHERE operacion PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'UPDATE_IN_BD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'UPDATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'ID'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'SET'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'WHERE'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = t[6]
    nodeFather.son.append(nodeSon6)

    t[0] = nodeFather

# SE SEPARO LA LISTA EN 2 METODOS PARA MANEJAR DATOS
def p_asignaciones(t):
    'asignaciones         : asignaciones COMA operacion'
    nodeFather = nodeAst()
    nodeFather.token = 'ASIGNACIONES'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon3 = t[3]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather


def p_asignaciones_2(t):
    'asignaciones         : operacion'
    nodeFather = nodeAst()
    nodeFather.token = 'ASIGNACIONES'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather

#-----------------------------------------------------DELETE IN BD--------------------------------------------------------------------
def p_deleteinBD_1(t):
    'deleteinBD         : DELETE FROM ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'DELETE_IN_BD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'DELETE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'FROM'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)
    
    t[0] = nodeFather

def p_deleteinBD_2(t):
    'deleteinBD         : DELETE FROM ID WHERE operacion PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'DELETE_IN_BD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'DELETE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'FROM'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'WHERE'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = t[5]
    nodeFather.son.append(nodeSon5)

    t[0] = nodeFather


#-----------------------------------------------------CREATE TABLE CON INHERITS-------------------------------------------------------
def p_inheritsBD(t):
    'inheritsBD         : CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA  INHERITS PARENTESISIZQUIERDA ID PARENTESISDERECHA PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'INHERITS_BD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'TABLE'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon5 = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon7 = nodeAst()
    nodeSon7.token = 'INHERITS'
    nodeSon7.lexeme = t[7]
    nodeFather.son.append(nodeSon7)

    nodeSon9 = t[9]
    nodeFather.son.append(nodeSon9)

    t[0] = nodeFather

#-----------------------------------------------------CREATE TABLE--------------------------------------------------------------------
def p_createTable(t):
    'createTable        : CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREATE_TABLE'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = "TABLE"
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon5 = t[5]
    nodeFather.son.append(nodeSon5)

    t[0] = nodeFather

# -------------------------------------------------------------------------------------------------------------- 
# SE SEPARO LA LISTA EN 2 METODOS PARA MANEJAR DATOS
def p_creaColumna(t):
    'creaColumnas          : creaColumnas COMA Columna'
    nodeFather = nodeAst()
    nodeFather.token = 'CREA_COLUMNAS'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon3 = t[3]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather

def p_creaColumna_2(t):
    'creaColumnas          : Columna'
    nodeFather = nodeAst()
    nodeFather.token = 'CREA_COLUMNAS'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather

# -------------------------------------------------------------------------------------------------------------- 
#INICIA LAS PRODUCCIONES DE COLUMNAS
def p_columna_1(t):
    'Columna            : ID tipo'
    nodeFather = nodeAst()
    nodeFather.token = 'COLUMNA'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ID'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather

def p_columna_2(t):
    'Columna            : ID tipo paramOpcional'
    nodeFather = nodeAst()
    nodeFather.token = 'COLUMNA'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ID'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = t[3]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather

def p_columna_3(t):
    'Columna            : UNIQUE PARENTESISIZQUIERDA listaParam PARENTESISDERECHA'
    nodeFather = nodeAst()
    nodeFather.token = 'COLUMNA'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'UNIQUE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon3 = t[3]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather

def p_columna_4(t):
    'Columna            : constraintcheck'
    nodeFather = nodeAst()
    nodeFather.token = 'COLUMNA'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather

def p_columna_5(t):
    'Columna            : checkinColumn'
    nodeFather = nodeAst()
    nodeFather.token = 'COLUMNA'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather

def p_columna_6(t):
    'Columna            : primaryKey'
    nodeFather = nodeAst()
    nodeFather.token = 'COLUMNA'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather

def p_columna_7(t):
    'Columna            : foreignKey'
    nodeFather = nodeAst()
    nodeFather.token = 'COLUMNA'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather


# -------------------------------------------------------------------------------------------------------------- 
#INICIA LA LISTA DE RESTRICCIONES OPCIONALES EN LAS COLUMNAS
def p_paramOpcional(t):
    'paramOpcional      : paramOpcional paramopc'
    nodeFather = nodeAst()
    nodeFather.token = 'PARAM_OPCIONAL'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather

def p_paramOpcional_1(t):
    'paramOpcional      : paramopc'
    nodeFather = nodeAst()
    nodeFather.token = 'PARAM_OPCIONAL'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather

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
        nodeFather = nodeAst()
        nodeFather.token = 'PARAM_OPC'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'DEFAULT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = t[2]
        nodeFather.son.append(nodeSon2)

        t[0] = nodeFather
        
    elif t[1].upper() == "NULL":
        nodeFather = nodeAst()
        nodeFather.token = 'PARAM_OPC'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'NULL'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    elif t[1].upper() == "NOT":
        nodeFather = nodeAst()
        nodeFather.token = 'PARAM_OPC'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'NOT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'NULL'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        t[0] = nodeFather

    elif t[1].upper() == "UNIQUE":
        nodeFather = nodeAst()
        nodeFather.token = 'PARAM_OPC'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'UNIQUE'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    elif t[1].upper() == "PRIMARY":
        nodeFather = nodeAst()
        nodeFather.token = 'PARAM_OPC'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'PRIMARY'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'KEY'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        t[0] = nodeFather

    else:
        print("NO SE ENCUENTRA NINGUN PARAMETRO OPCIONAL")
    

# -------------------------------------------------------------------------------------------------------------- 
#LLAMADA A LAS RESTRICCION CHECK
def p_paramopc_2(t):
    'paramopc           : constraintcheck'
    nodeFather = nodeAst()
    nodeFather.token = 'PARAM_OPC'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather
    
def p_paramopc_3(t):
    'paramopc           : checkinColumn'
    nodeFather = nodeAst()
    nodeFather.token = 'PARAM_OPC'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather


# -------------------------------------------------------------------------------------------------------------- 
#RESTRICCION UNIQUE
def p_paramopc_4(t):
    'paramopc           : CONSTRAINT ID UNIQUE'
    nodeFather = nodeAst()
    nodeFather.token = 'PARAM_OPC'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CONSTRAINT'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'ID'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'UNIQUE'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather


# -------------------------------------------------------------------------------------------------------------- 
#RESTRICION CHECK 
def p_checkcolumna(t):
    'checkinColumn      :  CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA'
    nodeFather = nodeAst()
    nodeFather.token = 'CHECK_IN_COLUMN'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CHECK'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon3 = t[3]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather
    

def p_constraintcheck(t):
    'constraintcheck    : CONSTRAINT ID CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA'
    nodeFather = nodeAst()
    nodeFather.token = 'CONSTRAINT_CHECK'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CONSTRAINT'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'ID'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'CHECK'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon5 = t[5]
    nodeFather.son.append(nodeSon5)

    t[0] = nodeFather


def p_primaryKey(t):
    'primaryKey         : PRIMARY KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA'
    nodeFather = nodeAst()
    nodeFather.token = 'PRIMARY_KEY'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'PRIMARY'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'KEY'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon4 = t[4]
    nodeFather.son.append(nodeSon4)

    t[0] = nodeFather

def p_foreingkey(t):
    'foreignKey         : FOREIGN KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA REFERENCES ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA' 
    nodeFather = nodeAst()
    nodeFather.token = 'FOREIGN_KEY'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'FOREIGN'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'KEY'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon4 = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon6 = nodeAst()
    nodeSon6.token = 'REFERENCES'
    nodeSon6.lexeme = t[6]
    nodeFather.son.append(nodeSon6)

    nodeSon7 = nodeAst()
    nodeSon7.token = 'ID'
    nodeSon7.lexeme = t[7]
    nodeFather.son.append(nodeSon7)

    nodeSon9 = t[9]
    nodeFather.son.append(nodeSon9)

    t[0] = nodeFather

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
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SMALLINT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="INTEGER":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'INTEGER'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper() =="BIGINT":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'BEGIN'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    
    
    

    

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="NUMERIC":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'NUMERIC'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="REAL":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'REAL'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="DOUBLE":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'DOUBLE'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'PRECISION'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="MONEY":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'MONEY'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="CHARACTER" and t[2].upper()=="VARING":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'CHARACTER'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'VARING'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon4 = nodeAst()
        nodeSon4.token = 'ENTERO'
        nodeSon4.lexeme = t[4]
        nodeFather.son.append(nodeSon4)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="VARCHAR":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'VARCHAR'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'ENTERO'
        nodeSon3.lexeme = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="CHARACTER":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'CHARACTER'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'ENTERO'
        nodeSon3.lexeme = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="CHAR":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'CHAR'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'ENTERO'
        nodeSon3.lexeme = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="TEXT":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'TEXT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="BOOLEAN":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'BOOLEAN'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="TIMESTAMP":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'TIMESTAMP'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="TIME":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'TIME'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="INTERVAL":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'INTERVAL'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="DATE":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'DATE'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="YEAR":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'YEAR'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="MONT":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'MONT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="HOUR":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'HOUR'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="MINUT":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'MINUT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="SECOND":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SECOND'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather


def p_tipo_2(t):
    'tipo               : DECIMAL'
    nodeFather = nodeAst()
    nodeFather.token = 'TIPO'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'DECIMAL'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather

def p_tipo_3(t):
    'tipo               : DECIMAL PARENTESISIZQUIERDA ENTERO COMA ENTERO PARENTESISDERECHA '
    nodeFather = nodeAst()
    nodeFather.token = 'tipo'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'DECIMAL'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ENTERO'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ENTERO'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    t[0] = nodeFather
    

    
#--------------------------------------------------- SENTENCIA SELECT --------------------------------------------------------------
#BYRON
def p_select(t):
    '''selectData       : SELECT select_list FROM select_list WHERE search_condition opcionesSelect 
                        | SELECT POR FROM select_list WHERE search_condition opcionesSelect 
    '''
    if t[2]=='*':
        nodeFather = nodeAst()
        nodeFather.token = 'SELECT_DATA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SELECT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'POR'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'FROM'
        nodeSon3.lexeme = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = t[4]
        nodeFather.son.append(nodeSon4)

        nodeSon5 = nodeAst()
        nodeSon5.token = 'WHERE'
        nodeSon5.lexeme = t[5]
        nodeFather.son.append(nodeSon5)

        nodeSon6 = t[6]
        nodeFather.son.append(nodeSon6)
        
        nodeSon7 = t[7]
        nodeFather.son.append(nodeSon7)

        t[0] = nodeFather


    else:
        nodeFather = nodeAst()
        nodeFather.token = 'SELECT_DATA'
    
        nodeSon1 = nodeAst()
        nodeSon1.token = 'SELECT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'FROM'
        nodeSon3.lexeme = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = t[4]
        nodeFather.son.append(nodeSon4)

        nodeSon5 = nodeAst()
        nodeSon5.token = 'WHERE'
        nodeSon5.lexeme = t[5]
        nodeFather.son.append(nodeSon5)

        nodeSon6 = t[6]
        nodeFather.son.append(nodeSon6)

        nodeSon7 = t[7]
        nodeFather.son.append(nodeSon7)

        t[0] = nodeFather



def p_select_1(t):
    '''selectData       : SELECT select_list FROM select_list WHERE search_condition  
                        | SELECT POR FROM select_list WHERE search_condition  
    '''
    if t[2]=='*':
        nodeFather = nodeAst()
        nodeFather.token = 'SELECT_DATA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SELECT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'POR'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'FROM'
        nodeSon3.lexeme = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = t[4]
        nodeFather.son.append(nodeSon4)

        nodeSon5 = nodeAst()
        nodeSon5.token = 'WHERE'
        nodeSon5.lexeme = t[5]
        nodeFather.son.append(nodeSon5)

        nodeSon6 = t[6]
        nodeFather.son.append(nodeSon6)

        t[0] = nodeFather
        
    else:
        nodeFather = nodeAst()
        nodeFather.token = 'SELECT_DATA'
    
        nodeSon1 = nodeAst()
        nodeSon1.token = 'SELECT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'FROM'
        nodeSon3.lexeme = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = t[4]
        nodeFather.son.append(nodeSon4)

        nodeSon5 = nodeAst()
        nodeSon5.token = 'WHERE'
        nodeSon5.lexeme = t[5]
        nodeFather.son.append(nodeSon5)

        nodeSon6 = t[6]
        nodeFather.son.append(nodeSon6)

        t[0] = nodeFather


# esta full
def p_select_2(t):
    '''selectData       : SELECT select_list FROM select_list  
                        | SELECT POR FROM select_list  
    ''' 
    if t[2]=='*':
        nodeFather = nodeAst()
        nodeFather.token = 'SELECT_DATA'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SELECT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'POR'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'FROM'
        nodeSon3.lexeme = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = t[4]
        nodeFather.son.append(nodeSon4)

        t[0] = nodeFather

    else:
        nodeFather = nodeAst()
        nodeFather.token = 'SELECT_DATA'
    
        nodeSon1 = nodeAst()
        nodeSon1.token = 'SELECT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'FROM'
        nodeSon3.lexeme = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = t[4]
        nodeFather.son.append(nodeSon4)

        t[0] = nodeFather
        

# esta full
def p_select_3(t):
    '''selectData       : SELECT select_list   
    '''
    nodeFather = nodeAst()
    nodeFather.token = 'SELECT_DATA'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'SELECT'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)


    t[0] = nodeFather

def p_opcionesSelect_1(t):
    '''opcionesSelect   : opcionesSelect opcionSelect
    '''
    nodeFather = nodeAst()
    nodeFather.token = 'OPCIONES_SELECT'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather

def p_opcionesSelect_2(t):
    '''opcionesSelect   : opcionSelect
    '''
    nodeFather = nodeAst()
    nodeFather.token = 'OPCIONES_SELECT'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather


def p_opcionesSelect_3(t):
    '''opcionSelect     : LIMIT operacion
                        | GROUP BY select_list
                        | HAVING select_list
                        | ORDER BY select_list 
    '''
    if t[1].upper()=="LIMIT":

        nodeFather = nodeAst()
        nodeFather.token = 'OPCION_SELECT'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'LIMIT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = t[2]
        nodeFather.son.append(nodeSon2)

        t[0] = nodeFather

    elif t[1].upper()=="GROUP":
        nodeFather = nodeAst()
        nodeFather.token = 'OPCION_SELECT'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'GROUP'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'BY'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather

    elif t[1].upper()=="HAVING":

        nodeFather = nodeAst()
        nodeFather.token = 'OPCION_SELECT'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'HAVING'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = t[2]
        nodeFather.son.append(nodeSon2)

        t[0] = nodeFather

    elif t[1].upper()=="ORDER":
        nodeFather = nodeAst()
        nodeFather.token = 'OPCION_SELECT'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'ORDER'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'BY'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather

def p_opcionesSelect_4(t):
    '''opcionSelect     : LIMIT operacion OFFSET operacion
                        | ORDER BY select_list ordenamiento                     
    '''
    if t[1].upper()=="LIMIT":
        nodeFather = nodeAst()
        nodeFather.token = 'OPCION_SELECT'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'LIMIT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'OFFSET'
        nodeSon3.lexeme = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = t[4]
        nodeFather.son.append(nodeSon4)

        t[0] = nodeFather

    elif t[1].upper()=="ORDER":
        nodeFather = nodeAst()
        nodeFather.token = 'OPCION_SELECT'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'ORDER'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'BY'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = t[4]
        nodeFather.son.append(nodeSon4)

        t[0] = nodeFather
        



def p_ordenamiento(t):
    '''ordenamiento     : ASC
                        | DESC '''

    if t[1] == "ASC":
        nodeFather = nodeAst()
        nodeFather.token = 'ORDENAMIENTO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'ASC'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather
    elif t[1] == "DESC":
        nodeFather = nodeAst()
        nodeFather.token = 'ORDENAMIENTO'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'DESC'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather
    



def p_search_condition_2(t):
    'search_condition   : final NOT IN PARENTESISIZQUIERDA selectData PARENTESISDERECHA'
    nodeFather = nodeAst()
    nodeFather.token = 'SEARCH_CONDITION'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'NOT'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'IN'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)


    nodeSon5 = t[5]
    nodeFather.son.append(nodeSon5)

    t[0] = nodeFather

# PARA ABAJO YA ESTA
def p_search_condition_3(t):
    'search_condition   : operacion'
    nodeFather = nodeAst()
    nodeFather.token = 'SEARCH_CONDITION'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather

def p_search_condition_4(t):
    'search_condition   : PARENTESISIZQUIERDA search_condition PARENTESISDERECHA'
    nodeFather = nodeAst()
    nodeFather.token = 'SEARCH_CONDITION'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'PARENTESISIZQUIERDA'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'PARENTESISDERECHA'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather    
#HAYRTON




def p_select_list_1(t):
    ' select_list   : select_list COMA operacion'
    nodeFather = nodeAst()
    nodeFather.token = '  select_list'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[3]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather

 
def p_select_list_6(t):
    ' select_list   : select_list COMA asignacion'
    nodeFather = nodeAst()
    nodeFather.token = '  select_list'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[3]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather
 
def p_select_list_7(t):
    ' select_list   :  asignacion'
    nodeFather = nodeAst()
    nodeFather.token = '  select_list'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather


def p_select_list_2(t):
    'select_list    : operacion'
    nodeFather = nodeAst()
    nodeFather.token = '  select_list'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather

def p_asignacion_1(t):
    ' asignacion   : operacion AS  operacion' 
    nodeFather = nodeAst()
    nodeFather.token = '  asignacion'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = '  AS'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = t[3]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather

def p_asignacion_2(t):
    ' asignacion   : final final'
    nodeFather = nodeAst()
    nodeFather.token = '  asignacion'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather

def p_funcion_basica_4(t):
    'funcionBasica   : operacion BETWEEN operacion '
    nodeFather = nodeAst()
    nodeFather.token = '  funcionBasica'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = '  BETWEEN'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = t[3]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather

def p_funcion_basica_5(t):
    'funcionBasica   :  operacion LIKE CADENA'
    nodeFather = nodeAst()
    nodeFather.token = '  funcionBasica'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'LIKE'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'CADENA'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather

def p_funcion_basica_6(t):
    'funcionBasica   : operacion IN PARENTESISIZQUIERDA select_list PARENTESISDERECHA '
    nodeFather = nodeAst()
    nodeFather.token = '  funcionBasica'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'IN'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = t[4]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather

#JPI
def p_funcion_basica_7(t):
    'funcionBasica   : operacion NOT BETWEEN operacion'
    nodeFather = nodeAst()
    nodeFather.token = 'funcionBasica'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'NOT'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'BETWEEN'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = t[4]
    nodeFather.son.append(nodeSon4)

    t[0] = nodeFather


def p_funcion_basica_8(t):
    'funcionBasica   : operacion  BETWEEN SYMMETRIC operacion '
    nodeFather = nodeAst()
    nodeFather.token = 'funcionBasica'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'BETWEEN'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'SYMMETRIC'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = t[4]
    nodeFather.son.append(nodeSon4)

    t[0] = nodeFather

def p_funcion_basica_9(t):
    'funcionBasica   : operacion NOT BETWEEN SYMMETRIC operacion '
    nodeFather = nodeAst()
    nodeFather.token = 'funcionBasica'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'NOT'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'BETWEEN'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'SYMMETRIC'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = t[5]
    nodeFather.son.append(nodeSon5)

    t[0] = nodeFather

def p_funcion_basica_10(t):
    '''funcionBasica : operacion IS DISTINCT FROM operacion '''
    nodeFather = nodeAst()
    nodeFather.token = 'funcionBasica'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'IS'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'DISTINCT'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'FROM'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = t[5]
    nodeFather.son.append(nodeSon5)

    t[0] = nodeFather

def p_funcion_basica_11(t):
    '''funcionBasica : operacion IS NOT DISTINCT  FROM operacion'''
    nodeFather = nodeAst()
    nodeFather.token = 'funcionBasica'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'IS'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'NOT'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'DISTINCT'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'FROM'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = t[6]
    nodeFather.son.append(nodeSon6)

    t[0] = nodeFather

def p_tipos(t):
    '''tipos : CREATE TYPE final AS ENUM PARENTESISIZQUIERDA select_list PARENTESISDERECHA PUNTOYCOMA'''
    nodeFather = nodeAst()
    nodeFather.token = 'tipos'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'TYPE'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = t[3]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'AS'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ENUM'
    nodeSon5.lexeme = t[5]
    nodeFather.son.append(nodeSon5)

    nodeSon7 = t[7]
    nodeFather.son.append(nodeSon7)

    t[0] = nodeFather
#JPI 


# ESTO ES NUEVO POR LOS JOIN******************************************************************************

#agregar eeste al arbol y 3D
def p_search_condition_5(t):
    'search_condition   : NOT EXISTS PARENTESISIZQUIERDA selectData PARENTESISDERECHA'
    nodeFather = nodeAst()
    nodeFather.token = 'SEARCH_CONDITION'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'NOT'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'EXISTS'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon4 = t[4]
    nodeFather.son.append(nodeSon4)

    t[0] = nodeFather

def p_search_condition_6(t):
    'search_condition   : EXISTS PARENTESISIZQUIERDA selectData PARENTESISDERECHA'
    nodeFather = nodeAst()
    nodeFather.token = 'SEARCH_CONDITION'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'EXISTS'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon3 = t[3]
    nodeFather.son.append(nodeSon3)
    
    t[0] = nodeFather

#agregar eeste al arbol y 3D
def p_search_condition_7(t):
    'search_condition   : final  IN PARENTESISIZQUIERDA selectData PARENTESISDERECHA'
    nodeFather = nodeAst()
    nodeFather.token = 'SEARCH_CONDITION'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'IN'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon4 = t[4]
    nodeFather.son.append(nodeSon4)

    t[0] = nodeFather

# PARA ABAJO YA ESTA
def p_search_condition_3(t):
    'search_condition   : operacion'
    nodeFather = nodeAst()
    nodeFather.token = 'SEARCH_CONDITION'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather

def p_combinacionSelects(t):
    '''combinacionSelects  : selectData UNION selectData
                            | selectData INTERSECT selectData
                            | selectData EXCEPT selectData
     
    '''
    print("*************************Entra a procesar el UNION********************")
    if t[2].upper()=="UNION":
        nodeFather = nodeAst()
        nodeFather.token = 'COMBINATION_SELECTS'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'UNION'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[2].upper()=="INTERSECT":
        nodeFather = nodeAst()
        nodeFather.token = 'COMBINATION_SELECTS'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'INTERSECT'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather
    elif t[2].upper()=="EXCEPT":
        nodeFather = nodeAst()
        nodeFather.token = 'COMBINATION_SELECTS'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'UNION'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather


def p_select_4(t):
    '''selectData       : SELECT select_list FROM   tipoJoin
                        | SELECT POR FROM  tipoJoin
    '''
    if t[2]=='*':
        nodeFather = nodeAst()
        nodeFather.token = 'SELECT'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SELECT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'POR'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'FROM'
        nodeSon3.lexeme = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = t[4]
        nodeFather.son.append(nodeSon4)
    
        t[0] = nodeFather
    else:
        nodeFather = nodeAst()
        nodeFather.token = 'SELECT'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SELECT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'FROM'
        nodeSon3.lexeme = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = t[4]
        nodeFather.son.append(nodeSon4)
    
        t[0] = nodeFather
        
def p_tipoJoin_1(t):
    '''tipoJoin   :   select_list  INNER JOIN select_list ON operacion
                  |   select_list NATURAL INNER JOIN select_list 
     '''
    if t[2].upper()=="INNER":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO_JOIN'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'INNER'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'JOIN'
        nodeSon3.lexeme = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = t[4]
        nodeFather.son.append(nodeSon4)

        nodeSon5 = nodeAst()
        nodeSon5.token = 'ON'
        nodeSon5.lexeme = t[5]
        nodeFather.son.append(nodeSon5)

        nodeSon6 = t[6]
        nodeFather.son.append(nodeSon6)
    
        t[0] = nodeFather
    elif t[2].upper()=="NATURAL":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO_JOIN'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'NATURAL'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'INNER'
        nodeSon3.lexeme = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = nodeAst()
        nodeSon4.token = 'JOIN'
        nodeSon4.lexeme = t[4]
        nodeFather.son.append(nodeSon4)

        nodeSon5 = t[5]
        nodeFather.son.append(nodeSon5)
    
        t[0] = nodeFather


def p_tipoJoin_2(t):
    '''tipoJoin   :  select_list  otroTipoJoin OUTER JOIN select_list ON operacion
                  |  select_list  NATURAL otroTipoJoin OUTER JOIN select_list
    '''
    if t[2].upper()=="NATURAL":
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO_JOIN'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'NATURAL'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = nodeAst()
        nodeSon4.token = 'OUTER'
        nodeSon4.lexeme = t[4]
        nodeFather.son.append(nodeSon4)

        nodeSon5 = nodeAst()
        nodeSon5.token = 'JOIN'
        nodeSon5.lexeme = t[5]
        nodeFather.son.append(nodeSon5)

        nodeSon6 = t[6]
        nodeFather.son.append(nodeSon6)
    
        t[0] = nodeFather
    else:
        nodeFather = nodeAst()
        nodeFather.token = 'TIPO_JOIN'

        nodeSon1 = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'OUTER'
        nodeSon3.lexeme = t[3]
        nodeFather.son.append(nodeSon3)

        nodeSon4 = nodeAst()
        nodeSon4.token = 'JOIN'
        nodeSon4.lexeme = t[4]
        nodeFather.son.append(nodeSon4)

        nodeSon5 = t[5]
        nodeFather.son.append(nodeSon5)

        nodeSon6 = nodeAst()
        nodeSon6.token = 'ON'
        nodeSon6.lexeme = t[6]
        nodeFather.son.append(nodeSon6)

        nodeSon7 = t[7]
        nodeFather.son.append(nodeSon7)
    
        t[0] = nodeFather
    


def p_otroTipoJoin(t):
    ''' otroTipoJoin    :   LEFT
                        |   RIGHT
                        |   FULL
    '''
    if t[1].upper() == "LEFT":
        nodeFather = nodeAst()
        nodeFather.token = 'OTRO_TIPO_JOIN'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'LEFT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather
    elif t[1].upper() == "RIGHT":
        nodeFather = nodeAst()
        nodeFather.token = 'OTRO_TIPO_JOIN'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'RIGHT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather
    elif t[1].upper() == "FULL":
        nodeFather = nodeAst()
        nodeFather.token = 'OTRO_TIPO_JOIN'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'FULL'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather
    
def p_execFunction(t):
    'execFunction    : execOption ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'EXEC_FUNCTION'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'ID'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather

def p_execFunction_1(t):
    'execFunction    : execOption ID PARENTESISIZQUIERDA listaid PARENTESISDERECHA PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'EXEC_FUNCTION'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'ID'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon4 = t[4]
    nodeFather.son.append(nodeSon4)

    t[0] = nodeFather

def p_execFunction_2(t):
    'execFunction    : execOption ID PARENTESISIZQUIERDA PARENTESISDERECHA PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'EXEC_FUNCTION'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'ID'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather

def p_execOption_1(t):
    'execOption : EXEC'
    nodeFather = nodeAst()
    nodeFather.token = 'EXEC_OPTION'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'EXEC'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather

def p_execOption_2(t):
    'execOption : EXECUTE'
    nodeFather = nodeAst()
    nodeFather.token = 'EXEC_OPTION'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'EXECUTE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather



    



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
