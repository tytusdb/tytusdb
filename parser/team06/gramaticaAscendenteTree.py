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
    'upper' : 'UPPER',
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
    'unknown':'UNKNOWN',
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
    'view' : 'VIEW',
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
    'izquierda' : 'LEFT',
    'derecha' : 'RIGHT',
    'full' : 'FULL',
    'join' : 'JOIN',
    'natural' : 'NATURAL',
    'case' : 'CASE',
    'when' : 'WHEN',
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
    'now':'NOW'


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
    nodeFather.token = 'inicio'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] =nodeFather
    gramaticaAscendenteTree.tree.root = t[0]
    
def p_queries_1(t) :
    'queries               : queries query'
    nodeFather = nodeAst()
    nodeFather.token = 'queries'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather

def p_queries_2(t) :
    'queries               : query'    
    nodeFather = nodeAst()
    nodeFather.token = 'queries'

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
                    | listaid
                    | tipoAlter                    
                    | selectData
    '''
    nodeFather = nodeAst()
    nodeFather.token = 'query'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)
    t[0] = nodeFather
 
                    # derivando cada produccion a cosas como el create, insert, select; funciones como avg, sum, substring irian como otra produccion 
                    #dentro del select (consulta)


# empiezan las producciones de las operaciones finales
#la englobacion de las operaciones

#-----------------------------------------------------CREATE DB--------------------------------------------------------------------
def p_crearBaseDatos_1(t):
    'crearBD    : CREATE DATABASE ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREARBD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    print(t[1])
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
    'crearBD    : CREATE OR REPLACE DATABASE ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREARBD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    print(t[1])
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

def p_crearBaseDatos_3(t):
    'crearBD    : CREATE OR REPLACE DATABASE ID parametrosCrearBD PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREARBD'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CREATE'
    print(t[1])
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

def p_crearBaseDatos_4(t):
    'crearBD    : CREATE  DATABASE ID parametrosCrearBD PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'CREARBD'

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


def p_parametrosCrearBD_1(t):
    'parametrosCrearBD : parametrosCrearBD parametroCrearBD'
    nodeFather = nodeAst()
    nodeFather.token = 'parametrosCrearBD'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)
    t[0] = nodeFather

def p_parametrosCrearBD_2(t):
    'parametrosCrearBD :  parametroCrearBD'
    nodeFather = nodeAst()
    nodeFather.token = 'parametrosCrearBD'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)
    
    t[0] = nodeFather

def p_parametroCrearBD(t):
    '''parametroCrearBD :  OWNER IGUAL final
                        |  MODE IGUAL final
    '''    
    if t[1] == "OWNER":
        nodeFather = nodeAst()
        nodeFather.token = 'parametroCrearBD'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'OWNER'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon3 = t[3]
        nodeFather.son.append(nodeSon3)
    
        t[0] = nodeFather
    elif t[1] == "MODE":
        nodeFather = nodeAst()
        nodeFather.token = 'parametroCrearBD'

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
    nodeFather.token = 'USEBD'

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
    nodeFather.token = 'SHOWDB'

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
    nodeFather.token = 'ALTERDB'

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
    nodeFather.token = 'ALTERDB'

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
    nodeFather.token = 'parametroAlterUser'

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
    nodeFather.token = 'parametroAlterUser'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'SESSION_USER'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)
    
    t[0] = nodeFather


def p_parametroAlterUser_3(t):
    '''parametroAlterUser : final    '''
    nodeFather = nodeAst()
    nodeFather.token = 'parametroAlterUser'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)
    
    t[0] = nodeFather
#-----------------------------------------------------DROP TABLE-----------------------------------------------------------------
def p_dropTable(t) :
    'dropTable  : DROP TABLE ID PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'DROP TABLE'
    nodeFather.lexeme = 'DROP'
    nodeSon2 = nodeAst()
    nodeSon2.token = 'ID'
    nodeSon2.lexeme = t[3]
    nodeFather.son.append(nodeSon2)
    t[0]=nodeFather
#-----------------------------------------------------ALTER TABLE-----------------------------------------------------------------
def p_alterTable(t):
    '''
    alterTable  : ALTER TABLE ID variantesAt PUNTOYCOMA

    '''
    nodeFather = nodeAst()
    nodeFather.token = 'ALTER TABLE'
    nodeSon2 = nodeAst()
    nodeSon2.token = 'ID'
    nodeSon2.lexeme = t[3]
    nodeFather.son.append(nodeSon2)
    nodeSon3 = t[4]
    nodeFather.son.append(nodeSon3)
    t[0]=nodeFather

   

#---------------------------------------------------TIPOS------------------------------------------------------------------------
def p_variantesAt(t):
    '''
    variantesAt :   ADD contAdd
                |   ALTER contAlter
                |   DROP contDrop
    '''
    nodeFather = nodeAst()
    nodeFather.token = t[1]

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)
    t[0]=nodeFather
    
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
        nodeFather.token = 'contALTER'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'COLUMN'
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'ID'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'SET NOT NULL'
        nodeFather.son.append(nodeSon3)

        t[0]=nodeFather
    elif t[3].upper()=="TYPE":
        nodeFather = nodeAst()
        nodeFather.token = 'contALTER'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'COLUMN TYPE'
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'ID'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = t[4]
        nodeFather.son.append(nodeSon3)
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
    nodeFather.token = "contAdd"
    
    if t[1].upper()=="COLUMN":
        nodeSon2 = nodeAst()
        nodeSon2.token = 'COLUMN'
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'ID'
        nodeSon3.lexeme = t[2]
        nodeFather.son.append(nodeSon3)
    
        nodeSon4 = t[3]
        nodeFather.son.append(nodeSon4)
        t[0]=nodeFather

    elif t[1].upper()=="CHECK":
        #CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA
        nodeSon2 = nodeAst()
        nodeSon2.token = 'CHECK'
        nodeFather.son.append(nodeSon2)
        nodeSon3 = nodeAst()
        nodeSon3.token = '('
        nodeFather.son.append(nodeSon3)
        nodeSon1 = t[3]
        nodeFather.son.append(nodeSon1)
        nodeSon4 = nodeAst()
        nodeSon4.token = ')'
        nodeFather.son.append(nodeSon4)
        t[0]=nodeFather

    elif t[1].upper()=="FOREIGN":
        nodeSon2 = nodeAst()
        nodeSon2.token = 'FOREIGN KEY'
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = '('
        nodeFather.son.append(nodeSon3)
    
        nodeSon1 = nodeAst()
        nodeSon1.token = "ID"
        nodeSon1.lexeme = t[4]
        nodeFather.son.append(nodeSon1)

        nodeSon4 = nodeAst()
        nodeSon4.token = ')'
        nodeFather.son.append(nodeSon4)

        nodeSon5 = nodeAst()
        nodeSon5.token = 'REFERENCES'
        nodeSon5.lexeme = t[6]
        nodeFather.son.append(nodeSon5)
        t[0]=nodeFather
    elif t[1].upper()=="PRIMARY":
        nodeSon2 = nodeAst()
        nodeSon2.token = 'PRIMARY KEY'
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = '('
        nodeFather.son.append(nodeSon3)
    
        nodeSon1 = nodeAst()
        nodeSon1.token = "ID"
        nodeSon1.lexeme = t[4]
        nodeFather.son.append(nodeSon1)

        nodeSon4 = nodeAst()
        nodeSon4.token = ')'
        nodeFather.son.append(nodeSon4)
        t[0]=nodeFather
    elif t[1].upper()=="CONSTRAINT":
        #CONSTRAINT ID FOREIGN KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA REFERENCES ID PARENTESISIZQUIERDA ID PARENTESISDERECHA
        #CONSTRAINT ID PRIMARY KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA
        #CONSTRAINT ID UNIQUE PARENTESISIZQUIERDA ID PARENTESISDERECHA
        
        nodeSon2 = nodeAst()
        nodeSon2.token = 'CONSTRAINT'
        nodeFather.son.append(nodeSon2)

        if t[3].upper()=="PRIMARY":
            nodeSon2 = nodeAst()
            nodeSon2.token = 'PRIMARY KEY'
            nodeFather.son.append(nodeSon2)

            nodeSon7 = nodeAst()
            nodeSon7.token = 'ID'
            nodeSon7.lexeme = t[2]
            nodeFather.son.append(nodeSon7)

            nodeSon3 = nodeAst()
            nodeSon3.token = '('
            nodeFather.son.append(nodeSon3)
    
            nodeSon1 = nodeAst()
            nodeSon1.token = "ID"
            nodeSon1.lexeme = t[6]
            nodeFather.son.append(nodeSon1)

            nodeSon4 = nodeAst()
            nodeSon4.token = ')'
            nodeFather.son.append(nodeSon4)
            t[0]=nodeFather
        elif t[3].upper()=="FOREIGN":
            #CONSTRAINT ID FOREIGN KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA REFERENCES ID PARENTESISIZQUIERDA ID PARENTESISDERECHA
            nodeSon2 = nodeAst()
            nodeSon2.token = 'FOREIGN KEY'
            nodeFather.son.append(nodeSon2)

            nodeSon7 = nodeAst()
            nodeSon7.token = 'ID'
            nodeSon7.lexeme = t[2]
            nodeFather.son.append(nodeSon7)

            nodeSon3 = nodeAst()
            nodeSon3.token = '('
            nodeFather.son.append(nodeSon3)
    
            nodeSon1 = nodeAst()
            nodeSon1.token = "ID"
            nodeSon1.lexeme = t[6]
            nodeFather.son.append(nodeSon1)

            nodeSon4 = nodeAst()
            nodeSon4.token = ')'
            nodeFather.son.append(nodeSon4)

            nodeSon12 = nodeAst()
            nodeSon12.token = "REFERENCES ID"
            nodeSon12.lexeme = t[9]
            nodeFather.son.append(nodeSon12)

            nodeSon13 = nodeAst()
            nodeSon13.token = "REFERENCES"
            nodeSon13.lexeme = t[11]
            nodeFather.son.append(nodeSon13)
            t[0]=nodeFather
        else:
            nodeSon2 = nodeAst()
            nodeSon2.token = 'UNIQUE'
            nodeFather.son.append(nodeSon2)

            nodeSon7 = nodeAst()
            nodeSon7.token = 'ID'
            nodeSon7.lexeme = t[2]
            nodeFather.son.append(nodeSon7)

            nodeSon3 = nodeAst()
            nodeSon3.token = '('
            nodeFather.son.append(nodeSon3)
    
            nodeSon1 = nodeAst()
            nodeSon1.token = "ID"
            nodeSon1.lexeme = t[6]
            nodeFather.son.append(nodeSon1)

            nodeSon4 = nodeAst()
            nodeSon4.token = ')'
            nodeFather.son.append(nodeSon4)
            t[0]=nodeFather
        


def p_contDrop(t):
    '''
    contDrop    : COLUMN ID 
                | CONSTRAINT ID
                | PRIMARY KEY
    '''
    if t[1].upper()=="COLUMN":

        nodeFather = nodeAst()
        nodeFather.token = 'contDROP'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'COLUMN'
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'ID'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)
        t[0]=nodeFather
    elif t[1].upper()=="CONSTRAINT":
        nodeFather = nodeAst()
        nodeFather.token = 'contDROP'
        
        nodeSon1 = nodeAst()
        nodeSon1.token = 'CONSTRAINT'
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'ID'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)
        t[0]=nodeFather
    elif t[1].upper()=="PRIMARY":
        nodeFather = nodeAst()
        nodeFather.token = 'contDROP'
        
        nodeSon1 = nodeAst()
        nodeSon1.token = 'PRIMARY KEY'
        nodeFather.son.append(nodeSon1)
        t[0]=nodeFather

# SE SEPARO LA LISTA PARA PODER MANIPULAR DATOS
def p_listaID(t):
    '''
    listaid     :   listaid COMA ID
    '''
    h.reporteGramatical1 +="listaid    ::=         listaid COMA ID\n"
    h.reporteGramatical2 +="t[1].append(t[3])\nt[0]=t[1]\n"
    t[1].append(t[3])
    t[0]=t[1]

def p_listaID_2(t):
    '''
    listaid     :   ID
    '''
    h.reporteGramatical1 +="listaid    ::=          ID\n"
    h.reporteGramatical2 +="t[0]=[t[1]]"
    t[0]=ExpresionIdentificador(t[1])
    
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
    nodeFather.token = 'DROPDB'

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
    nodeFather.token = 'DROPDB'

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
                          '''                          
# --------------------------------------------------------------------------------------------------------------                          
    if t[2]=='+':
        nodeFather = nodeAst()
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        h.reporteGramatical1 +="operacion    ::=      operacion IGUAL operacion\n"
# --------------------------------------------------------------------------------------------------------------                          
    elif t[2]=='==':
        nodeFather = nodeAst()
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        nodeFather.token = 'operacion'

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
        h.reporteGramatical1 +="operacion    ::=      PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        nodeFather = nodeAst()
        nodeFather.token = 'operacion'

        nodeSon2 = t[2]
        nodeFather.son.append(nodeSon2)
    
        t[0] = nodeFather
# --------------------------------------------------------------------------------------------------------------                              
def p_operacion_menos_unario_entero(t):
    '''operacion : MENOS ENTERO  %prec UMINUS'''
    nodeFather = nodeAst()
    nodeFather.token = 'operacion'

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
    nodeFather.token = 'operacion'

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
    nodeFather.token = 'operacion'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'NOT'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)
    
    t[0] = nodeFather
	
	
	
	
def p_operacion_final(t):
    'operacion :     final'
    nodeFather = nodeAst()
    nodeFather.token = 'operacion'

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
                        | GREATEST PARENTESISIZQUIERDA select_list PARENTESISDERECHA
                        | LEAST PARENTESISIZQUIERDA select_list PARENTESISDERECHA
                        | NOW PARENTESISIZQUIERDA  PARENTESISDERECHA
                        
                        
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
    '''
#BYRON    
    if t[1].upper()=="ABS":
        h.reporteGramatical1 +="funcionBasica    ::=      ABS PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        t[0]=ExpresionABS(t[3])
    elif t[1].upper()=="CBRT":
        h.reporteGramatical1 +="funcionBasica    ::=      CBRT PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        t[0]=ExpresionCBRT(t[3])
    elif t[1].upper()=="CEIL":
        h.reporteGramatical1 +="funcionBasica    ::=      CEIL PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        t[0]=ExpresionCEIL(t[3])
    elif t[1].upper()=="CEILING":
        h.reporteGramatical1 +="funcionBasica    ::=      CEILING PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        t[0]=ExpresionCEILING(t[3])
    elif t[1].upper()=="DEGREES":
        t[0]=ExpresionDEGREES(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      DEGREES PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="DIV":
        print("entra a DIV++++++++++++")
        t[0]=ExpresionDIV(t[3],t[5])
        h.reporteGramatical1 +="funcionBasica    ::=      DIV PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="EXP":
        t[0]=ExpresionEXP(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      EXP PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="FACTORIAL":
        t[0]=ExpresionFACTORIAL(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      FACTORIAL PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="FLOOR":
        t[0]=ExpresionFLOOR(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      FLOOR PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="GCD":
        t[0]=ExpresionGCD(t[3],t[5])
        h.reporteGramatical1 +="funcionBasica    ::=      GCD PARENTESISIZQUIERDA operacion COMA operacion  PARENTESISDERECHA\n"
    elif t[1].upper()=="LN":
        t[0]=ExpresionLN(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      LN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="LOG":
        t[0]=ExpresionLOG(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      LOG PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="MOD":
        t[0]=ExpresionMOD(t[3],t[5])
        h.reporteGramatical1 +="funcionBasica    ::=      MOD PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA\n"   
    elif t[1].upper()=="PI":
        t[0]=ExpresionPI(1)
        h.reporteGramatical1 +="funcionBasica    ::=      PI PARENTESISIZQUIERDA   PARENTESISDERECHA\n"   
    elif t[1].upper()=="POWER":
        t[0]=ExpresionPOWER(t[3],t[5])
        h.reporteGramatical1 +="funcionBasica    ::=      POWER PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA\n" 
    elif t[1].upper()=="RADIANS":
        t[0]=ExpresionRADIANS(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      RADIANS PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"    
    elif t[1].upper()=="ROUND":
        t[0]=ExpresionROUND(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="SIGN":
        t[0]=ExpresionSIGN(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      SIGN  PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"    
    elif t[1].upper()=="SQRT":
        t[0]=ExpresionSQRT(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      SQRT  PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="TRUNC":
        t[0]=ExpresionTRUNC(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      TRUNC  PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
#HAYRTON
    elif t[1].upper()=="WIDTH_BUCKET":
        t[0]=ExpresionWIDTHBUCKET(t[3],t[5],t[7],t[9])
        h.reporteGramatical1 +="funcionBasica    ::=      WIDTH_BUCKET PARENTESISIZQUIERDA operacion COMA operacion COMA operacion COMA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="RANDOM":
        t[0]=ExpresionRANDOM(1)
        h.reporteGramatical1 +="funcionBasica    ::=      RANDOM PARENTESISIZQUIERDA  PARENTESISDERECHA\n"
    elif t[1].upper()=="ACOS":
        t[0]=ExpresionACOS(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ACOS PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="ACOSD":
        t[0]=ExpresionACOSD(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ACOSD PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="ASIN":
        t[0]=ExpresionASIN(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ASIN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="ASIND":
        t[0]=ExpresionASIND(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ASIND PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="ATAN":
        t[0]=ExpresionATAN(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ATAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="ATAND":
        t[0]=ExpresionATAND(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ATAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n" 
    elif t[1].upper()=="ATAN2":
        t[0]=ExpresionATAN2(t[3],t[5])
        h.reporteGramatical1 +="funcionBasica    ::=      ATAN2 PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="ATAN2D":
        t[0]=ExpresionATAN2D(t[3],t[5])
        h.reporteGramatical1 +="funcionBasica    ::=      ATAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="COS":
        t[0]=ExpresionCOS(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      COS PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="COSD":
        t[0]=ExpresionCOSD(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      COSD PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="COT":
        t[0]=ExpresionCOT(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      COT PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="COTD":
        t[0]=ExpresionCOTD(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      COTD PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="SIN":
        t[0]=ExpresionSIN(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      SIN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    

    
    elif t[1].upper()=="SIND":
        t[0]=ExpresionSIND(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      SIND PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="TAN":
        t[0]=ExpresionTAN(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      TAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="TAND":
        t[0]=ExpresionTAND(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      TAND PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="SINH":
        t[0]=ExpresionSINH(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      SINH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="COSH":
        t[0]=ExpresionCOSH(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      COSH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
#JPI    
    elif t[1].upper()=="TANH":
        t[0]=ExpresionTANH(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      TANH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="ASINH":
        t[0]=ExpresionASINH(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ASINH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="ACOSH":
        t[0]=ExpresionACOSH(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ACOSH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="ATANH":
        t[0]=ExpresionATANH(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      ATANH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
   
   


    elif t[1].upper()=="LENGTH":
        h.reporteGramatical1 +="funcionBasica    ::=      LENGTH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="TRIM":
        h.reporteGramatical1 +="funcionBasica    ::=      TRIM PARENTESISIZQUIERDA opcionTrim operacion FROM operacion PARENTESISDERECHA\n"
    elif t[1]=="GET_BYTE":
        h.reporteGramatical1 +="funcionBasica    ::=      GET_BYTE PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="MD5":
        h.reporteGramatical1 +="funcionBasica    ::=      MD5 PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="SET_BYTE":
        h.reporteGramatical1 +="funcionBasica    ::=      SET_BYTE PARENTESISIZQUIERDA operacion COMA operacion COMA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="SHA256":
        h.reporteGramatical1 +="funcionBasica    ::=      SHA256 PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1].upper()=="SUBSTR":
        h.reporteGramatical1 +="funcionBasica    ::=      SUBSTR PARENTESISIZQUIERDA operacion  COMA operacion COMA operacion PARENTESISDERECHA\n"
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

    elif t[1].upper()=="GREATEST":
        t[0]=ExpresionGREATEST(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      GREATEST PARENTESISIZQUIERDA select_list PARENTESISDERECHA\n"
    elif t[1].upper()=="LEAST":
        t[0]=ExpresionLEAST(t[3])
        h.reporteGramatical1 +="funcionBasica    ::=      LEAST PARENTESISIZQUIERDA select_list PARENTESISDERECHA\n"
    elif t[1].upper()=="NOW":
        t[0]=ExpresionNOW(1)
        h.reporteGramatical1 +="funcionBasica    ::=      NOW PARENTESISIZQUIERDA  PARENTESISDERECHA\n"
   
    else:
        print("no entra a ninguna en funcionBasica")
#JPI



def p_funcion_basica_1(t):
    'funcionBasica   : SUBSTRING PARENTESISIZQUIERDA operacion FROM operacion FOR operacion PARENTESISDERECHA'
    h.reporteGramatical1 +="funcionBasica    ::=      SUBSTRING PARENTESISIZQUIERDA operacion FROM operacion FOR operacion PARENTESISDERECHA\n"

def p_funcion_basica_2(t):
    'funcionBasica   : SUBSTRING PARENTESISIZQUIERDA operacion FROM operacion PARENTESISDERECHA'
    h.reporteGramatical1 +="funcionBasica    ::=      SUBSTRING PARENTESISIZQUIERDA operacion FROM operacion PARENTESISDERECHA\n"
   
def p_funcion_basica_3(t):
    'funcionBasica   : SUBSTRING PARENTESISIZQUIERDA operacion FOR operacion PARENTESISDERECHA'
    h.reporteGramatical1 +="funcionBasica    ::=      SUBSTRING PARENTESISIZQUIERDA operacion FOR operacion PARENTESISDERECHA\n"

 
def p_opcionTrim(t):
    ''' opcionTrim  : LEADING
                    | TRAILING
                    | BOTH
    '''    
    h.reporteGramatical1 +="opcionTrim     ::=     "+str(t[1])+"\n"
    # falta mandar a las funciones de fechas y dates y todo eso

#-----------------------------------------------------PRODUCCIONES TERMINALES--------------------------------------------------------------------
def p_final_decimal(t):
    '''final        : DECIMAL'''
    nodeFather = nodeAst()
    nodeFather.token = 'final'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'DECIMAL'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)
    
    t[0] = nodeFather

def p_final_entero(t):
    '''final        : ENTERO'''
    nodeFather = nodeAst()
    nodeFather.token = 'final'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ENTERO'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)
    
    t[0] = nodeFather

def p_final_id(t):
    'final          : ID'
    nodeFather = nodeAst()
    nodeFather.token = 'final'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ID'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)
    
    t[0] = nodeFather

def p_final_invocacion(t):
    'final          : ID PUNTO ID'
    nodeFather = nodeAst()
    nodeFather.token = 'final'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ID'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon3 = nodeAst()
    nodeSon3.token = 'ID'
    nodeSon3.lexeme = t[3]
    nodeFather.son.append(nodeSon3)
    
    t[0] = nodeFather
def p_final_cadena(t):
    'final          : CADENA'
    nodeFather = nodeAst()
    nodeFather.token = 'final'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CADENA'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)
    
    t[0] = nodeFather

#-----------------------------------------------------INSERT BD--------------------------------------------------------------------
def p_insertBD_1(t):
    'insertinBD           : INSERT INTO ID VALUES PARENTESISIZQUIERDA listaParam PARENTESISDERECHA PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'insertinBD'

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

    nodeSon5 = t[6]
    nodeFather.son.append(nodeSon5)

    t[0] = nodeFather

def p_insertBD_2(t):
    'insertinBD           : INSERT INTO ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA VALUES PARENTESISIZQUIERDA listaParam PARENTESISDERECHA PUNTOYCOMA'
    #pendiente

# SE SEPARO LA LISTA EN 2 METODOS PARA MANEJAR DATOS
def p_listaParam(t):
    'listaParam           : listaParam COMA final'
    nodeFather = nodeAst()
    nodeFather.token = 'listaParam'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[3]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather
    

def p_listaParam_2(t):
    'listaParam           : final'
    nodeFather = nodeAst()
    nodeFather.token = 'listaParam'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather

#-----------------------------------------------------UPDATE BD--------------------------------------------------------------------
def p_updateBD(t):
    'updateinBD           : UPDATE ID SET asignaciones WHERE asignaciones PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'insertinBD'

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
    'asignaciones         : asignaciones COMA asigna'
    nodeFather = nodeAst()
    nodeFather.token = 'asignaciones'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather


def p_asignaciones_2(t):
    'asignaciones         : asigna'
    nodeFather = nodeAst()
    nodeFather.token = 'asignaciones'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather


def p_asigna(t):
    'asigna               : ID IGUAL operacion'
    nodeFather = nodeAst()
    nodeFather.token = 'asigna'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'ID'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[3]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather

#-----------------------------------------------------DELETE IN BD--------------------------------------------------------------------
def p_deleteinBD_1(t):
    'deleteinBD         : DELETE FROM ID PUNTOYCOMA'
    #no especificado en enunciado

def p_deleteinBD_2(t):
    'deleteinBD         : DELETE FROM ID WHERE operacion PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'deleteinBD'

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
    nodeSon4.token = 'FROM'
    nodeSon4.lexeme = t[4]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = t[5]
    nodeFather.son.append(nodeSon5)

    t[0] = nodeFather


#-----------------------------------------------------CREATE TABLE CON INHERITS-------------------------------------------------------
def p_inheritsBD(t):
    'inheritsBD         : CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA  INHERITS PARENTESISIZQUIERDA ID PARENTESISDERECHA PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'inheritsBD'

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

    nodeSon4 = t[5]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'INHERITS'
    nodeSon5.lexeme = t[7]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = t[9]
    nodeFather.son.append(nodeSon6)

    t[0] = nodeFather

#-----------------------------------------------------CREATE TABLE--------------------------------------------------------------------
def p_createTable(t):
    'createTable        : CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA PUNTOYCOMA'
    nodeFather = nodeAst()
    nodeFather.token = 'createTable'

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

    nodeSon4 = t[5]
    nodeFather.son.append(nodeSon4)

    t[0] = nodeFather

# -------------------------------------------------------------------------------------------------------------- 
# SE SEPARO LA LISTA EN 2 METODOS PARA MANEJAR DATOS
def p_creaColumna(t):
    'creaColumnas          : creaColumnas COMA Columna'
    nodeFather = nodeAst()
    nodeFather.token = 'creaColumnas'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[3]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather

def p_creaColumna_2(t):
    'creaColumnas          : Columna'
    nodeFather = nodeAst()
    nodeFather.token = 'creaColumnas'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather

# -------------------------------------------------------------------------------------------------------------- 
#INICIA LAS PRODUCCIONES DE COLUMNAS
def p_columna_1(t):
    'Columna            : ID tipo'
    nodeFather = nodeAst()
    nodeFather.token = 'Columna'

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
    nodeFather.token = 'Columna'

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
    nodeFather.token = 'Columna'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'UNIQUE'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[3]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather

def p_columna_4(t):
    'Columna            : constraintcheck'
    nodeFather = nodeAst()
    nodeFather.token = 'Columna'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather

def p_columna_5(t):
    'Columna            : checkinColumn'
    nodeFather = nodeAst()
    nodeFather.token = 'Columna'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather

def p_columna_6(t):
    'Columna            : primaryKey'
    nodeFather = nodeAst()
    nodeFather.token = 'Columna'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather

def p_columna_7(t):
    'Columna            : foreignKey'
    nodeFather = nodeAst()
    nodeFather.token = 'Columna'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather


# -------------------------------------------------------------------------------------------------------------- 
#INICIA LA LISTA DE RESTRICCIONES OPCIONALES EN LAS COLUMNAS
def p_paramOpcional(t):
    'paramOpcional      : paramOpcional paramopc'
    nodeFather = nodeAst()
    nodeFather.token = 'paramOpcional'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[2]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather

def p_paramOpcional_1(t):
    'paramOpcional      : paramopc'
    nodeFather = nodeAst()
    nodeFather.token = 'ParamOpcional'

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
        nodeFather.token = 'paramopc'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'DEFAULT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = t[2]
        nodeFather.son.append(nodeSon2)

        t[0] = nodeFather
        
    elif t[1].upper() == "NULL":
        nodeFather = nodeAst()
        nodeFather.token = 'paramopc'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'NULL'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    elif t[1].upper() == "NOT":
        nodeFather = nodeAst()
        nodeFather.token = 'paramopc'

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
        nodeFather.token = 'paramopc'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'UNIQUE'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    elif t[1].upper() == "PRIMARY":
        nodeFather = nodeAst()
        nodeFather.token = 'paramopc'

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
        print("FFFFF")
    

# -------------------------------------------------------------------------------------------------------------- 
#LLAMADA A LAS RESTRICCION CHECK
def p_paramopc_2(t):
    'paramopc           : constraintcheck'
    nodeFather = nodeAst()
    nodeFather.token = 'paramopc'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather
    
def p_paramopc_3(t):
    'paramopc           : checkinColumn'
    nodeFather = nodeAst()
    nodeFather.token = 'paramopc'

    nodeSon1 = t[1]
    nodeFather.son.append(nodeSon1)

    t[0] = nodeFather


# -------------------------------------------------------------------------------------------------------------- 
#RESTRICCION UNIQUE
def p_paramopc_4(t):
    'paramopc           : CONSTRAINT ID UNIQUE'
    nodeFather = nodeAst()
    nodeFather.token = 'paramopc'

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
    nodeFather.token = 'checkinColumn'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'CHECK'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = t[3]
    nodeFather.son.append(nodeSon2)

    t[0] = nodeFather
    

def p_constraintcheck(t):
    'constraintcheck    : CONSTRAINT ID CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA'
    nodeFather = nodeAst()
    nodeFather.token = 'constraintcheck'

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

    nodeSon4 = t[5]
    nodeFather.son.append(nodeSon4)

    t[0] = nodeFather


def p_primaryKey(t):
    'primaryKey         : PRIMARY KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA'
    nodeFather = nodeAst()
    nodeFather.token = 'primaryKey'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'PRIMARY'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'KEY'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = t[4]
    nodeFather.son.append(nodeSon3)

    t[0] = nodeFather

def p_foreingkey(t):
    'foreignKey         : FOREIGN KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA REFERENCES ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA' 
    nodeFather = nodeAst()
    nodeFather.token = 'foreignKey'

    nodeSon1 = nodeAst()
    nodeSon1.token = 'FOREIGN'
    nodeSon1.lexeme = t[1]
    nodeFather.son.append(nodeSon1)

    nodeSon2 = nodeAst()
    nodeSon2.token = 'KEY'
    nodeSon2.lexeme = t[2]
    nodeFather.son.append(nodeSon2)

    nodeSon3 = t[4]
    nodeFather.son.append(nodeSon3)

    nodeSon4 = nodeAst()
    nodeSon4.token = 'REFERENCES'
    nodeSon4.lexeme = t[6]
    nodeFather.son.append(nodeSon4)

    nodeSon5 = nodeAst()
    nodeSon5.token = 'ID'
    nodeSon5.lexeme = t[7]
    nodeFather.son.append(nodeSon5)

    nodeSon6 = t[9]
    nodeFather.son.append(nodeSon6)

    t[0] = nodeFather

#-----------------------------------------------------TIPOS DE DATOS--------------------------------------------------------------------

def p_tipo(t):
    '''tipo            :  SMALLINT
                        | INTEGER
                        | BIGINT
                        | DECIMAL
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
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SMALLINT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="INTEGER":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'INTEGER'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="BEGIN":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'BEGIN'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="DECIMAL":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'DECIMAL'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="NUMERIC":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'NUMERIC'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="REAL":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'REAL'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="DOUBLE":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

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
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'MONEY'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="CHARACTER" and t[2].upper()=="VARING":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'CHARACTER'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2.token = 'VARING'
        nodeSon2.lexeme = t[2]
        nodeFather.son.append(nodeSon2)

        nodeSon3 = nodeAst()
        nodeSon3.token = 'ENTERO'
        nodeSon3.lexeme = t[4]
        nodeFather.son.append(nodeSon3)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="VARCHAR":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'VARCHAR'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'ENTERO'
        nodeSon2.lexeme = t[3]
        nodeFather.son.append(nodeSon2)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="CHARACTER":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'CHARACTER'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'ENTERO'
        nodeSon2.lexeme = t[3]
        nodeFather.son.append(nodeSon2)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="CHAR":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'CHAR'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        nodeSon2 = nodeAst()
        nodeSon2.token = 'ENTERO'
        nodeSon2.lexeme = t[3]
        nodeFather.son.append(nodeSon2)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="TEXT":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'TEXT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="BOOLEAN":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'BOOLEAN'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="TIMESTAMP":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'TIMESTAMP'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="TIME":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'TIME'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="INTERVAL":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'INTERVAL'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="DATE":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'DATE'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="YEAR":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'YEAR'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="MONT":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'MONT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="HOUR":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'HOUR'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="MINUT":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'MINUT'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="SECOND":
        nodeFather = nodeAst()
        nodeFather.token = 'tipo'

        nodeSon1 = nodeAst()
        nodeSon1.token = 'SECOND'
        nodeSon1.lexeme = t[1]
        nodeFather.son.append(nodeSon1)

        t[0] = nodeFather

    
#--------------------------------------------------- SENTENCIA SELECT --------------------------------------------------------------
#BYRON
def p_select(t):
    '''selectData       : SELECT select_list FROM select_list WHERE search_condition opcionesSelect PUNTOYCOMA
                        | SELECT POR FROM select_list WHERE search_condition opcionesSelect PUNTOYCOMA
    '''
    if t[2]=='*':
        h.reporteGramatical1 +="selectData    ::=     SELECT POR FROM select_list WHERE search_condition opcionesSelect PUNTOYCOMA\n"
        print("/////////////////// SELECT CON ASTERISCO ////////////////////////")
        print("Columnas: ",t[2])
        print("Tablas: ",t[4])
        print("Where: ",QueryWhere(t[6]))
        print("Extras: ",t[7])
        t[0]=Select5(t[2],t[4],QueryWhere(t[6]),t[7])
    else:
        h.reporteGramatical1 +="selectData    ::=      SELECT select_list FROM select_list WHERE search_condition opcionesSelect PUNTOYCOMA\n"
        print("/////////////////// SELECT SIN ASTERISCO ////////////////////////")
        print("Columnas: ",t[2])
        print("Tablas: ",t[4])
        print("Where: ",QueryWhere(t[6]))
        print("Extras: ",t[7])
        t[0]=Select5(t[2],t[4],QueryWhere(t[6]),t[7])
     


def p_select_1(t):
    '''selectData       : SELECT select_list FROM select_list WHERE search_condition  PUNTOYCOMA
                        | SELECT POR FROM select_list WHERE search_condition  PUNTOYCOMA
    '''
    if t[2]=='*':
        h.reporteGramatical1 +="selectData    ::=     SELECT POR FROM select_list WHERE search_condition  PUNTOYCOMA\n"
        h.reporteGramatical2 +="t[0]=Select3(t[4],QueryWhere(t[6]))\n"
        print("entra al select con where y asterisco/////////////////")
        t[0]=Select3(t[4],QueryWhere(t[6]))
        print("el objeto que sube")
        print(t[0])
    else:
        h.reporteGramatical1 +="selectData    ::=     SELECT select_list FROM select_list WHERE search_condition  PUNTOYCOMA\n"
        h.reporteGramatical2 +=" t[0]=Select4(t[2],t[4],QueryWhere(t[6]))\n"
        print("entra al select con where y campos /////////////////")
        print(t[2])
        print(t[4])
        print(t[6])
        t[0]=Select4(t[2],t[4],QueryWhere(t[6]))
        print(t[0])



# esta full
def p_select_2(t):
    '''selectData       : SELECT select_list FROM select_list  PUNTOYCOMA
                        | SELECT POR FROM select_list  PUNTOYCOMA
    ''' 
    if t[2]=='*':
        h.reporteGramatical1 +="selectData    ::=      SELECT POR FROM select_list  PUNTOYCOMA\n"
        h.reporteGramatical2 +=" t[0]=Select(1,t[4])\n"
        print("entra a select_2 A")
        t[0]=Select(1,t[4])
    
    else:
        # select tipo 4
        h.reporteGramatical1 +="selectData    ::=     SELECT select_list FROM select_list  PUNTOYCOMA\n"
        h.reporteGramatical2 +=" t[0]=Select2(2,t[2],t[4])\n"
        print("entra a select_2  B")
        t[0]=Select2(2,t[2],t[4])

# esta full
def p_select_3(t):
    '''selectData       : SELECT select_list   PUNTOYCOMA
    '''
    h.reporteGramatical1 +="selectData    ::=      SELECT select_list   PUNTOYCOMA\n"
    h.reporteGramatical2 +=" t[0]=Select(1,t[2])\n"
    t[0]=Select(1,t[2])



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
    'search_condition   : NOT search_condition'
    h.reporteGramatical1 +="search_condition    ::=       NOT search_condition\n"
    print("esta condicion es del not con operacion******************")
    print(t[2])

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
#HAYRTON




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
    t[0]=t[1]


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
    t[0]=[Asignacion(t[1],t[3])]

def p_asignacion_2(t):
    ' asignacion   : final final'
    h.reporteGramatical1 +="select_list    ::=      final final\n"
    h.reporteGramatical2 +=" t[0]=[Asignacion(t[1],t[2])]\n"
    print(" entra al select_list de 2 finales-------------")
    t[0]=[Asignacion(t[1],t[2])]
    print(t[0])

def p_funcion_basica_4(t):
    'funcionBasica   : operacion BETWEEN operacion '
    h.reporteGramatical1 +="funcionBasica    ::=      operacion BETWEEN operacion AND operacion\n"
    h.reporteGramatical2 +="t[0]=ExpresionBetween(t[1],t[3])\n"
    print("entra al between con sus operaciones")
    print(t[1])
    print(t[3])
    t[0]=ExpresionBetween(t[1],t[3])

def p_funcion_basica_5(t):
    'funcionBasica   :  operacion LIKE CADENA'
    h.reporteGramatical1 +="funcionBasica    ::=      operacion LIKE CADENA\n"

def p_funcion_basica_6(t):
    'funcionBasica   : operacion  IN PARENTESISIZQUIERDA select_list PARENTESISDERECHA '
    h.reporteGramatical1 +="funcionBasica    ::=      operacion  IN PARENTESISIZQUIERDA select_list PARENTESISDERECHA\n"

#JPI
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
#JPI 


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