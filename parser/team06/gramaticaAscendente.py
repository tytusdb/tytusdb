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
    'truc':'TRUC',
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
    'symmetric':'SYMMETRIC'


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
     r'[a-zA-Z]+[a-zA-_Z0-9]*'
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
    h.reporteGramatical1 +="query     ::=      opcion\n"
    h.reporteGramatical2 +="t[0]=t[1]\n"
    t[0]=t[1]
 
                    # derivando cada produccion a cosas como el create, insert, select; funciones como avg, sum, substring irian como otra produccion 
                    #dentro del select (consulta)


# empiezan las producciones de las operaciones finales
#la englobacion de las operaciones

#-----------------------------------------------------CREATE DB--------------------------------------------------------------------

def p_crearBaseDatos_1(t):
    'crearBD    : CREATE DATABASE ID PUNTOYCOMA'
    h.reporteGramatical1 +="crearBD    ::=        CREATE DATABASE ID PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateDatabases(t[3])\n"
    t[0] = CreateDatabases(t[3])


def p_crearBaseDatos_2(t):
    'crearBD    : CREATE OR REPLACE DATABASE ID PUNTOYCOMA'
    h.reporteGramatical1 +="crearBD    ::=        CREATE OR REPLACE DATABASE ID PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateDatabases(t[5])\n"
    t[0] = CreateDatabases(t[5])

def p_crearBaseDatos_3(t):
    'crearBD    : CREATE OR REPLACE DATABASE ID parametrosCrearBD PUNTOYCOMA'
    h.reporteGramatical1 +="crearBD    ::=        CREATE OR REPLACE DATABASE ID parametrosCrearBD PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateDatabaseswithParameters(t[5],t[6])\n"
    t[0] = CreateDatabaseswithParameters(t[5],t[6])

def p_crearBaseDatos_4(t):
    'crearBD    : CREATE  DATABASE ID parametrosCrearBD PUNTOYCOMA'
    h.reporteGramatical1 +="crearBD    ::=        CREATE  DATABASE ID parametrosCrearBD PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0] = CreateDatabaseswithParameters(t[3],t[4])\n"
    t[0] = CreateDatabaseswithParameters(t[3],t[4])


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
        t[0]=VariantesAt(t[1],t[2])
    elif t[1].upper()=="ALTER":
        h.reporteGramatical1 +="variantesAt    ::=        ALTER listaContAlter\n"
        t[0]=VariantesAt(t[1],t[2])
    elif t[1].upper()=="DROP":
        h.reporteGramatical1 +="variantesAt    ::=         DROP contDrop\n"
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
        t[0]=contAlter(t[2],t[3],t[4])
    elif t[3].upper()=="TYPE":
        h.reporteGramatical1 +="contAlter    ::=         COLUMN ID  TYPE  tipo\n"
        t[0]=contAlter(t[2],t[3],t[4])


def p_contAdd(t):
    '''
    contAdd     :   COLUMN ID tipo 
                |   CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                |   FOREIGN KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA REFERENCES ID
                |   CONSTRAINT ID UNIQUE PARENTESISIZQUIERDA listaid PARENTESISDERECHA
    '''
    if t[1].upper()=="COLUMN":
        h.reporteGramatical1 +="contAdd    ::=         COLUMN ID tipo\n"
        t[0]=contAdd(t[1],t[3],t[2],None,None)
    elif t[1].upper()=="CHECK":
        h.reporteGramatical1 +="contAdd    ::=         CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        t[0]=contAdd(t[1],None,None,None,t[3])
    elif t[1].upper()=="FOREIGN":
        h.reporteGramatical1 +="contAdd    ::=        FOREIGN KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA REFERENCES ID\n"
        t[0]=contAdd(t[1],None,t[4],t[7],None)
    elif t[1].upper()=="CONSTRAINT":
        h.reporteGramatical1 +="contAdd    ::=         CONSTRAINT ID UNIQUE PARENTESISIZQUIERDA listaid PARENTESISDERECHA\n"
        t[0]=contAdd(t[1],None,t[2],None,t[5])


def p_contDrop(t):
    '''
    contDrop    : COLUMN ID 
                | CONSTRAINT ID
    '''
    if t[1].upper()=="COLUMN":
        h.reporteGramatical1 +="contDrop    ::=         COLUMN ID \n"
        t[0]=contDrop(t[1],t[2])
    elif t[1].upper()=="CONSTRAINT":
        h.reporteGramatical1 +="contDrop    ::=         CONSTRAINT ID\n"
        t[0]=contDrop(t[1],t[2])

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
    h.reporteGramatical1 +="dropBD    ::=        DROP DATABASE  "+str(t[3])+" PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0]= DropDB(t[3])\n"
    t[0]= DropDB(t[3])


def p_dropBD_2(t):
    'dropBD    : DROP DATABASE IF EXISTS ID PUNTOYCOMA'
    h.reporteGramatical1 +="dropBD    ::=        DROP DATABASE IF EXISTS  "+str(t[5])+" PUNTOYCOMA\n"
    h.reporteGramatical2 +="t[0]= DropDBIF(t[5])\n"
    t[0]= DropDBIF(t[5])
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
    'operacion : MENOS ENTERO  %prec UMINUS'
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
                        | DIV PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | EXP PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | FACTORIAL PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | FLOOR PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | GCD PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | LCM PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | LN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | LOG PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | LOG10 PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                    


                        | MIN_SCALE PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | MOD PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | POWER PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | RADIANS PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SCALE ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SIGN ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SQRT ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TRIM_SCALE ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TRUC ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | WIDTH_BUCKET PARENTESISIZQUIERDA operacion COMA operacion COMA operacion COMA operacion PARENTESISDERECHA
                        | RANDOM PARENTESISIZQUIERDA PARENTESISDERECHA
                        | SETSEED PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ACOS  PARENTESISIZQUIERDA operacion PARENTESISDERECHA



                        | ACOSD PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ASIN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ASIND PARENTESISIZQUIERDA operacion PARENTESISDERECHA                
                        | ATAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ATAN2 PARENTESISIZQUIERDA operacion PARENTESISDERECHA
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
    if t[1]=="ABS":
        h.reporteGramatical1 +="funcionBasica    ::=      ABS PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="CBRT":
        h.reporteGramatical1 +="funcionBasica    ::=      CBRT PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="CEIL":
        h.reporteGramatical1 +="funcionBasica    ::=      CEIL PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="CEILING":
        h.reporteGramatical1 +="funcionBasica    ::=      CEILING PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="DEGREES":
        h.reporteGramatical1 +="funcionBasica    ::=      DEGREES PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="DIV":
        h.reporteGramatical1 +="funcionBasica    ::=      DIV PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="EXP":
        h.reporteGramatical1 +="funcionBasica    ::=      EXP PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="FACTORIAL":
        h.reporteGramatical1 +="funcionBasica    ::=      FACTORIAL PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="FLOOR":
        h.reporteGramatical1 +="funcionBasica    ::=      FLOOR PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="GCD":
        h.reporteGramatical1 +="funcionBasica    ::=      GCD PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="LCM":
        h.reporteGramatical1 +="funcionBasica    ::=      LCM PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="LN":
        h.reporteGramatical1 +="funcionBasica    ::=      LN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="LOG":
        h.reporteGramatical1 +="funcionBasica    ::=      LOG PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="LOG10":
        h.reporteGramatical1 +="funcionBasica    ::=      LOG10 PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"    
    elif t[1]=="MIN_SCALE":
        h.reporteGramatical1 +="funcionBasica    ::=      MIN_SCALE PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"   
    elif t[1]=="MOD":
        h.reporteGramatical1 +="funcionBasica    ::=      MOD PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA\n"   
    elif t[1]=="POWER":
        h.reporteGramatical1 +="funcionBasica    ::=      POWER PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA\n"
    elif t[1]=="RADIANS":
        h.reporteGramatical1 +="funcionBasica    ::=      RADIANS PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"    
    elif t[1]=="ROUND":
        h.reporteGramatical1 +="funcionBasica    ::=      ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="SCALE":
        h.reporteGramatical1 +="funcionBasica    ::=      SCALE ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="SIGN":
        h.reporteGramatical1 +="funcionBasica    ::=      SIGN ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"    
    elif t[1]=="SQRT":
        h.reporteGramatical1 +="funcionBasica    ::=      SQRT ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="TRIM_SCALE":
        h.reporteGramatical1 +="funcionBasica    ::=      TRIM_SCALE ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="TRUC":
        h.reporteGramatical1 +="funcionBasica    ::=      TRUC ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="WIDTH_BUCKET":
        h.reporteGramatical1 +="funcionBasica    ::=      WIDTH_BUCKET PARENTESISIZQUIERDA operacion COMA operacion COMA operacion COMA operacion PARENTESISDERECHA\n"
    elif t[1]=="RANDOM":
        h.reporteGramatical1 +="funcionBasica    ::=      RANDOM PARENTESISIZQUIERDA  PARENTESISDERECHA\n"
    elif t[1]=="SETSEED":
        h.reporteGramatical1 +="funcionBasica    ::=      SETSEED PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="ACOS":
        h.reporteGramatical1 +="funcionBasica    ::=      ACOS PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="ACOSD":
        h.reporteGramatical1 +="funcionBasica    ::=      ACOSD PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="ASIN":
        h.reporteGramatical1 +="funcionBasica    ::=      ASIN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="ASIND":
        h.reporteGramatical1 +="funcionBasica    ::=      ASIND PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="ATAN":
        h.reporteGramatical1 +="funcionBasica    ::=      ATAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="ATAN2":
        h.reporteGramatical1 +="funcionBasica    ::=      ATAN2 PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="COS":
        h.reporteGramatical1 +="funcionBasica    ::=      COS PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="COSD":
        h.reporteGramatical1 +="funcionBasica    ::=      COSD PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="COT":
        h.reporteGramatical1 +="funcionBasica    ::=      COT PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="COTD":
        h.reporteGramatical1 +="funcionBasica    ::=      COTD PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="SIN":
        h.reporteGramatical1 +="funcionBasica    ::=      SIN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="SIND":
        h.reporteGramatical1 +="funcionBasica    ::=      SIND PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="TAN":
        h.reporteGramatical1 +="funcionBasica    ::=      TAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="TAND":
        h.reporteGramatical1 +="funcionBasica    ::=      TAND PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="SINH":
        h.reporteGramatical1 +="funcionBasica    ::=      SINH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="COSH":
        h.reporteGramatical1 +="funcionBasica    ::=      COSH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="TANH":
        h.reporteGramatical1 +="funcionBasica    ::=      TANH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="ASINH":
        h.reporteGramatical1 +="funcionBasica    ::=      ASINH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="ACOSH":
        h.reporteGramatical1 +="funcionBasica    ::=      ACOSH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="ATANH":
        h.reporteGramatical1 +="funcionBasica    ::=      ATANH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="LENGTH":
        h.reporteGramatical1 +="funcionBasica    ::=      LENGTH PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        
    elif t[1]=="TRIM":
        h.reporteGramatical1 +="funcionBasica    ::=      TRIM PARENTESISIZQUIERDA opcionTrim operacion FROM operacion PARENTESISDERECHA\n"
    elif t[1]=="GET_BYTE":
        h.reporteGramatical1 +="funcionBasica    ::=      GET_BYTE PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA\n"
    elif t[1]=="MD5":
        h.reporteGramatical1 +="funcionBasica    ::=      MD5 PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="SET_BYTE":
        h.reporteGramatical1 +="funcionBasica    ::=      SET_BYTE PARENTESISIZQUIERDA operacion COMA operacion COMA operacion PARENTESISDERECHA\n"
    elif t[1]=="SHA256":
        h.reporteGramatical1 +="funcionBasica    ::=      SHA256 PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="SUBSTR":
        h.reporteGramatical1 +="funcionBasica    ::=      SUBSTR PARENTESISIZQUIERDA operacion  COMA operacion COMA operacion PARENTESISDERECHA\n"
    elif t[1]=="CONVERT":
        h.reporteGramatical1 +="funcionBasica    ::=      CONVERT PARENTESISIZQUIERDA operacion  COMA operacion COMA operacion PARENTESISDERECHA\n"
    elif t[1]=="ENCODE":
        h.reporteGramatical1 +="funcionBasica    ::=      ENCODE  PARENTESISIZQUIERDA operacion  COMA operacion  PARENTESISDERECHA\n"
    elif t[1]=="DECODE":
        h.reporteGramatical1 +="funcionBasica    ::=      DECODE  PARENTESISIZQUIERDA operacion  COMA operacion  PARENTESISDERECHA\n"
    elif t[1]=="AVG":
        h.reporteGramatical1 +="funcionBasica    ::=      AVG PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    elif t[1]=="SUM":
        h.reporteGramatical1 +="funcionBasica    ::=      SUM PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
    




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
    t[0] = ExpresionInvocacion(t[1],t[3])
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
    t[0] = InsertinDataBases(t[3],t[6])
    h.reporteGramatical1 +="insertinBD    ::=      INSERT INTO ID VALUES PARENTESISIZQUIERDA listaParam PARENTESISDERECHA PUNTOYCOMA\n"

def p_insertBD_2(t):
    'insertinBD           : INSERT INTO ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA VALUES PARENTESISIZQUIERDA listaParam PARENTESISDERECHA PUNTOYCOMA'
    h.reporteGramatical1 +="insertinBD    ::=     INSERT INTO ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA VALUES PARENTESISIZQUIERDA listaParam PARENTESISDERECHA PUNTOYCOMA\n"

# SE SEPARO LA LISTA EN 2 METODOS PARA MANEJAR DATOS
def p_listaParam(t):
    '''listaParam         : listaParam COMA final
    '''
    t[1].append(t[3])
    t[0] = t[1]
    h.reporteGramatical1 +="insertinBD    ::=      listaParam COMA final\n"

def p_listaParam_2(t):
    '''listaParam         : final
    '''
    t[0] = [t[1]]
    h.reporteGramatical1 +="insertinBD    ::=      final\n"

#-----------------------------------------------------UPDATE BD--------------------------------------------------------------------
def p_updateBD(t):
    'updateinBD           : UPDATE ID SET asignaciones WHERE asignaciones PUNTOYCOMA'
    t[0]= UpdateinDataBase(t[2],t[4],t[6])
    h.reporteGramatical1 +="updateinBD    ::=      UPDATE ID SET asignaciones WHERE asignaciones PUNTOYCOMA\n"


# SE SEPARO LA LISTA EN 2 METODOS PARA MANEJAR DATOS
def p_asignaciones(t):
    '''asignaciones       : asignaciones COMA asigna
    '''
    t[1].append(t[3])
    t[0] = t[1]
    h.reporteGramatical1 +="asignaciones    ::=      asignaciones COMA asigna\n"

def p_asignaciones_2(t):
    '''asignaciones       : asigna
    '''
    t[0] = [t[1]]
    h.reporteGramatical1 +="asignaciones    ::=      asigna\n"

def p_asigna(t):
    'asigna             : ID IGUAL operacion'
    t[0] = AsignacioninTable(t[1],t[3])
    h.reporteGramatical1 +="asigna    ::=      ID IGUAL operacion\n"

#-----------------------------------------------------DELETE IN BD--------------------------------------------------------------------
def p_deleteinBD_1(t):
    'deleteinBD         : DELETE FROM ID PUNTOYCOMA'
    h.reporteGramatical1 +="deleteinBD    ::=      DELETE FROM ID PUNTOYCOMA\n"

def p_deleteinBD_2(t):
    'deleteinBD         : DELETE FROM ID WHERE operacion PUNTOYCOMA'
    t[0] = DeleteinDataBases(t[3],t[5])
    h.reporteGramatical1 +="deleteinBD    ::=      DELETE FROM ID WHERE operacion PUNTOYCOMA\n"

#-----------------------------------------------------CREATE TABLE--------------------------------------------------------------------
def p_createTable(t):
    'createTable        : CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA PUNTOYCOMA'
    t[0]= CreateTable(t[3],t[5])
    h.reporteGramatical1 +="createTable    ::=      CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA PUNTOYCOMA\n"



def p_inheritsBD(t):
    'inheritsBD         : CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA  INHERITS PARENTESISIZQUIERDA ID PARENTESISDERECHA PUNTOYCOMA'
    h.reporteGramatical1 +="inheritsBD    ::=      CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA  INHERITS PARENTESISIZQUIERDA ID PARENTESISDERECHA PUNTOYCOMA\n"

# SE SEPARO LA LISTA EN 2 METODOS PARA MANEJAR DATOS
def p_creaColumna(t):
    '''creaColumnas        : creaColumnas COMA Columna 
    '''
    t[1].append(t[3])
    t[0] = t[1]
    h.reporteGramatical1 +="creaColumnas    ::=      creaColumnas COMA Columna\n"

def p_creaColumna_2(t):
    '''creaColumnas        : Columna 
    '''
    t[0]=[t[1]]
    h.reporteGramatical1 +="createTable    ::=      Columna\n"

def p_columna_1(t):
    'Columna            : ID tipo'
    t[0]=ColumnasTable(t[1],t[2],None)
    h.reporteGramatical1 +="Columna    ::=      ID tipo\n"

def p_columna_2(t):
    'Columna            : ID tipo paramOpcional'
    #print(t[3])
    t[0]=ColumnasTable(t[1],t[2],t[3])
    h.reporteGramatical1+="Columna      ::=     ID tipo paramOpcional"

def p_columna_3(t):
    'Columna            : uniqueinColumn'
    h.reporteGramatical+="Columna       ::=     uniqueinColumn"

def p_columna_4(t):
    '''Columna          : constraintinColumn 
                        | checkinColumn
                        | primaryKey
                        | foreignKey
    '''
    t[0] = t[1]
    h.reporteGramatical1 +="Columna    ::=      Un parametro de columna\n"

def p_paramOpcional(t):
    '''paramOpcional    : paramOpcional paramopc
    '''
    t[1].append(t[2])
    t[0] = t[1]
    h.reporteGramatical1 +="paramOpcional    ::=      paramOpcional paramopc\n"
    print("parametro-----")
    

def p_paramOpcional_1(t):
    '''paramOpcional    : paramopc
    '''
    t[0] = [t[1]]
    print("parametro++++")
    print(t[0])
    h.reporteGramatical1 +="paramOpcional    ::=      paramopc\n"

def p_paramopc_1(t):
    '''paramopc         : DEFAULT final
                        | NULL
                        | NOT NULL
                        | UNIQUE
                        | PRIMARY KEY
    '''
    if t[1].upper() == "DEFAULT":
        
        t[0] = TipoRestriccion(RestriccionDefaul(t[2]),OPERACION_RESTRICCION_COLUMNA.DEFAULT)
        print("entro default " ,t[0])
    #elif t[1].upper() == "NULL":
    #    t[0] = TipoRestriccion(RestriccionNull(1),OPERACION_RESTRICCION_COLUMNA.NULL)
    #elif t[1] == "NOT":
    #    t[0] = TipoRestriccion(RestriccionNotNull(1),OPERACION_RESTRICCION_COLUMNA.NOT_NULL)
    #elif t[1] == "UNIQUE":
    #    print(t[1])
    #    t[0] = TipoRestriccion(RestriccionUniqueSimple(1),OPERACION_RESTRICCION_COLUMNA.UNIQUE_COLUMNA)
    #elif t[1] == "PRIMARY":
    #    t[0] = TipoRestriccion(RestriccionPrimaryKeyColumn(1),OPERACION_RESTRICCION_COLUMNA.PRIMARY_KEY)
    else:
        print("FFFFF")
    
    h.reporteGramatical1 +="paramopc    ::=      paramopc\n"
    #print(t[0])
    

def p_paramopc_2(t):
    'paramopc           : constraintinColumn'
    h.reporteGramatical1 +="paramopc    ::=      "+str(t[1])+"\n"

def p_paramopc_3(t):
    'paramopc           : checkinColumn'
    t[0] = TipoRestriccion(t[1],OPERACION_RESTRICCION_COLUMNA.CHECK_SIMPLE)
    h.reporteGramatical1+="paramopc     ::=     "+str(t[1])+"\n"

def p_paramopc_4(t):
    'paramopc           : CONSTRAINT ID UNIQUE'
    t[0] = TipoRestriccion(RestriccionConstraintUnique(t[2]),OPERACION_RESTRICCION_COLUMNA.UNIQUE_CONSTAINT)
    h.reporteGramatical1 +="constraintinColumn    ::=      CONSTRAINT   ID   UNIQUE"

def p_constraintinColumn_1(t):
    '''constraintinColumn   : CONSTRAINT ID checkinColumn
    '''
    t[0]=RestriccionConstraintCheck(t[2],t[3])
    h.reporteGramatical1 +="constraintinColumn    ::=      CONSTRAINT   ID   "+str(t[3])+"\n"


def p_constraintinColumn_2(t):
    'ConstraintinColumn     : CONSTRAINT ID uniqueinColumn'
    t[0]=RestriccionConstraintUnique(t[2],t[3])
    h.reporteGramatical1 +="constraintinColumn    ::=      CONSTRAINT   ID   "+str(t[3])+"\n"

def p_checkinColumn(t):
    'checkinColumn      : CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA'
    t[0]=RestriccionCheck(t[3])
    h.reporteGramatical1 +="checkinColumn    ::=      CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"


def p_uniqueinColumn(t):
    'uniqueinColumn     : UNIQUE PARENTESISIZQUIERDA listaParam PARENTESISDERECHA'
    t[0]=RestriccionUnique(t[3])
    h.reporteGramatical1 +="uniqueinColumn    ::=      UNIQUE PARENTESISIZQUIERDA listaParam PARENTESISDERECHA\n"


def p_primaryKey(t):
    'primaryKey         : PRIMARY KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA'
    t[0]=RestriccionPrimaryKey(t[4])
    h.reporteGramatical1 +="primaryKey    ::=      PRIMARY KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA\n"


def p_foreingkey(t):
    'foreignKey         : FOREIGN KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA REFERENCES ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA' 
    t[0]=RestriccionForeingkey(t[4],t[7],t[9])
    h.reporteGramatical1 +="foreignKey    ::=      FOREIGN KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA REFERENCES ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA\n"

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
    if t[1]=="SMALLINT":
        t[0] = t[1] 
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"
    elif t[1]=="INTEGER":
        t[0] = t[1]
        h.reporteGramatical1 +="tipo    ::=      "+str(t[1])+"\n"

    
#--------------------------------------------------- SENTENCIA SELECT --------------------------------------------------------------
def p_select(t):
    '''selectData       : SELECT select_list FROM select_list WHERE search_condition opcionesSelect PUNTOYCOMA
                        | SELECT POR FROM select_list WHERE search_condition opcionesSelect PUNTOYCOMA
    '''
    if t[2]=='*':
        h.reporteGramatical1 +="selectData    ::=     SELECT POR FROM select_list WHERE search_condition opcionesSelect PUNTOYCOMA\n"
    else:
        h.reporteGramatical1 +="selectData    ::=      SELECT select_list FROM select_list WHERE search_condition opcionesSelect PUNTOYCOMA\n"


def p_select_1(t):
    '''selectData       : SELECT select_list FROM select_list WHERE search_condition  PUNTOYCOMA
                        | SELECT POR FROM select_list WHERE search_condition  PUNTOYCOMA
    '''
    if t[2]=='*':
        h.reporteGramatical1 +="selectData    ::=     SELECT POR FROM select_list WHERE search_condition  PUNTOYCOMA\n"
    else:
        h.reporteGramatical1 +="selectData    ::=     SELECT select_list FROM select_list WHERE search_condition  PUNTOYCOMA\n"

def p_select_2(t):
    '''selectData       : SELECT select_list FROM select_list  PUNTOYCOMA
                        | SELECT POR FROM select_list  PUNTOYCOMA
    '''
    if t[2]=='*':
        h.reporteGramatical1 +="selectData    ::=     SELECT select_list FROM select_list  PUNTOYCOMA\n"
    else:
        h.reporteGramatical1 +="selectData    ::=      SELECT POR FROM select_list  PUNTOYCOMA\n"

def p_select_3(t):
    '''selectData       : SELECT select_list   PUNTOYCOMA
    '''
    h.reporteGramatical1 +="selectData    ::=      SELECT select_list   PUNTOYCOMA\n"

def p_opcionesSelect_1(t):
    '''opcionesSelect   : opcionesSelect opcionSelect
    '''
    h.reporteGramatical1 +="opcionesSelect    ::=      opcionesSelect opcionSelect\n"

def p_opcionesSelect_2(t):
    '''opcionesSelect   : opcionSelect
    '''
    h.reporteGramatical1 +="opcionesSelect    ::=      opcionSelect\n"


def p_opcionesSelect_3(t):
    '''opcionSelect     : LIMIT operacion
                        | GROUP BY select_list
                        | HAVING select_list
                        | ORDER BY select_list 
    '''
    if t[1]=="LIMIT":
        h.reporteGramatical1 +="opcionSelect    ::=      LIMIT operacion\n"
    elif t[1]=="GROUP":
        h.reporteGramatical1 +="opcionSelect    ::=      GROUP BY select_list\n"
    elif t[1]=="HAVING":
        h.reporteGramatical1 +="opcionSelect    ::=      HAVING select_list\n"
    elif t[1]=="ORDER":
        h.reporteGramatical1 +="opcionSelect    ::=      ORDER BY select_list\n"

def p_opcionesSelect_4(t):
    '''opcionSelect     : LIMIT operacion OFFSET operacion
                        | ORDER BY select_list ordenamiento                     
    '''
    if t[1]=="LIMIT":
        h.reporteGramatical1 +="opcionSelect    ::=      LIMIT operacion OFFSET operacion\n"
    elif t[1]=="ORDER":
        h.reporteGramatical1 +="opcionSelect    ::=      ORDER BY select_list ordenamiento\n"



def p_ordenamiento(t):
    '''ordenamiento     : ASC
                        | DESC '''
    h.reporteGramatical1 +="ordenamiento    ::=      "+str(t[1])+"\n"

def p_search_condition_1(t):
    '''search_condition   : search_condition AND search_condition
                          | search_condition OR search_condition                         
    '''
    h.reporteGramatical1 +="search_condition    ::=     search_condition     "+str(t[2])+"    search_condition\n"

def p_search_condition_2(t):
    'search_condition   : NOT search_condition'
    h.reporteGramatical1 +="search_condition    ::=      condicion_select   operacion\n"

def p_search_condition_3(t):
    'search_condition   : operacion'
    h.reporteGramatical1 +="search_condition    ::=       operacion\n"

def p_search_condition_4(t):
    'search_condition   : PARENTESISIZQUIERDA search_condition PARENTESISDERECHA'
    h.reporteGramatical1 +="search_condition    ::=     PARENTESISIZQUIERDA search_condition PARENTESISDERECHA\n"


def p_select_list_1(t):
    ' select_list   : select_list COMA operacion'
    h.reporteGramatical1 +="select_list    ::=      select_list COMA operacion\n"
    


def p_select_list_2(t):
    'select_list    : operacion'
    h.reporteGramatical1 +="select_list    ::=      operacion\n"

def p_select_list_3(t):
    ' select_list   : select_list condicion_select operacion COMA operacion' 
    h.reporteGramatical1 +="select_list    ::=      select_list condicion_select operacion COMA operacion\n"

def p_select_list_4(t):
    ' select_list   : condicion_select   operacion' 
    h.reporteGramatical1 +="select_list    ::=      condicion_select   operacion\n"

def p_select_list_5(t):
    ' select_list   : select_list AS  operacion' 
    h.reporteGramatical1 +="select_list    ::=      select_list AS  operacion\n"

def p_condicion_select(t):
    '''condicion_select : DISTINCT FROM                 
    '''
    h.reporteGramatical1 +="condicion_select    ::=      DISTINCT FROM\n"

def p_condicion_select_2(t):
    '''condicion_select : IS DISTINCT FROM                             
    '''
    h.reporteGramatical1 +="condicion_select    ::=      IS DISTINCT FROM\n"


def p_condicion_select_3(t):
    '''condicion_select : IS NOT DISTINCT  FROM'''
    h.reporteGramatical1 +="condicion_select    ::=     IS NOT DISTINCT  FROM\n"

def p_condicion_select_4(t):
    '''condicion_select : DISTINCT '''
    h.reporteGramatical1 +="condicion_select    ::=      DISTINCT \n"

def p_condicion_select_5(t):
    '''condicion_select :  IS DISTINCT                 
    '''
    h.reporteGramatical1 +="condicion_select    ::=      IS DISTINCT\n"

def p_condicion_select_6(t):
    '''condicion_select : IS NOT DISTINCT                 
    '''
    h.reporteGramatical1 +="condicion_select    ::=     IS NOT DISTINCT\n"

def p_funcion_basica_4(t):
    'funcionBasica   : operacion BETWEEN operacion AND operacion'
    h.reporteGramatical1 +="funcionBasica    ::=      operacion BETWEEN operacion AND operacion\n"

def p_funcion_basica_5(t):
    'funcionBasica   :  operacion LIKE CADENA'
    h.reporteGramatical1 +="funcionBasica    ::=      operacion LIKE CADENA\n"

def p_funcion_basica_6(t):
    'funcionBasica   : operacion  IN PARENTESISIZQUIERDA select_list PARENTESISDERECHA '
    h.reporteGramatical1 +="funcionBasica    ::=      operacion  IN PARENTESISIZQUIERDA select_list PARENTESISDERECHA\n"

def p_funcion_basica_7(t):
    'funcionBasica   : operacion NOT BETWEEN operacion AND operacion '
    h.reporteGramatical1 +="funcionBasica    ::=      operacion NOT BETWEEN operacion AND operacion\n"

def p_funcion_basica_8(t):
    'funcionBasica   : operacion  BETWEEN SYMMETRIC operacion AND operacion'
    h.reporteGramatical1 +="funcionBasica    ::=      operacion  BETWEEN SYMMETRIC operacion AND operacion\n"

def p_funcion_basica_9(t):
    'funcionBasica   : operacion NOT BETWEEN SYMMETRIC operacion AND operacion'
    h.reporteGramatical1 +="funcionBasica    ::=      operacion NOT BETWEEN SYMMETRIC operacion AND operacion\n"


def p_funcion_basica_10(t):
    'funcionBasica   : operacion condicion_select operacion'
    h.reporteGramatical1 +="funcionBasica    ::=      operacion condicion_select operacion\n"

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