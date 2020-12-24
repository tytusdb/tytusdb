# LEXICO 
import re
from reporteErrores.errorReport import ErrorReport 
from reporteErrores.instance import listaErrores
palabrasReservadas = {
    'insert':'INSERT',
    'varchar':'VARCHAR',
    'columns':'COLUMNS', 
    'column':'COLUMN',
    'natural':'NATURAL',
    'outer':'OUTER',
    'bytea':'BYTEA',
    'sign':'SIGN',               
    'rename':'RENAME',
    'asc':'ASC',
    'desc':'DESC',
    'add':'ADD',
    'current':'CURRENT',
    'current_time':'CURRENT_TIME',
    'returning':'RETURNING',
    'distinct':'DISTINCT',
    'symmetric':'SYMMETRIC',
    'unknown':'UNKNOWN',
    'create':'CREATE',
    'replace':'REPLACE',
    'declare':'DECLARE',
    'database':'DATABASE',
    'show':'SHOW',
    'databases':'DATABASES',
    'if':'IF',
    'else':'ELSE',
    'case':'CASE',
    'when':'WHEN',
    'then':'THEN',
    'null':'NULL',
    'first':'FIRST',
    'last':'LAST',
    'union':'UNION',
    'intersect':'INTERSECT',
    'except':'EXCEPT',
    'limit':'LIMIT',
    'offset':'OFFSET',
    'constraint':'CONSTRAINT',
    'unique':'UNIQUE',
    'check':'CHECK',
    'default':'DEFAULT',
    'primary':'PRIMARY',
    'references':'REFERENCES',
    'table':'TABLE',
    'foreign':'FOREIGN',
    'key':'KEY',
    'inherits':'INHERITS',
    'use':'USE',
    # VARIABLES DE ADMIN 
    'current_user':'CURRENT_USER',
    'session_user':'SESSION_USER',    
    'owner':'OWNER',
    'mode':'MODE',
    'group':'GROUP',
    'by':'BY',
    'having':'HAVING',
    'alter':'ALTER',
    'drop':'DROP',
    'select':'SELECT',
    'from':'FROM',
    'where':'WHERE',
    'as':'AS',
    'inner':'INNER',
    'into': 'INTO',
    'update': 'UPDATE',
    'delete': 'DELETE',
    'on':'ON',
    'values': 'VALUES',
    'join':'JOIN',
    'in': 'IN',
    'set': 'SET',
    'exists':'EXISTS',
    'between':'BETWEEN',
    'in':'IN',
    'like':'LIKE',
    'ilike':'ILIKE',
    'similar':'SIMILAR',
    'is':'IS',
    'isnull':'ISNULL',
    'notnull':'NOTNULL',
    # operadores logicos
    'or': 'OR',
    'and':'AND',
    'not': 'NOT',
    'left': 'LEFT',
    'right': 'RIGHT',
    'full' : 'FULL',
    'using':'USING',
    'all':'ALL',
    'some':'SOME',
    # TIPOS NUMERICOS
    'smallint':'SMALLINT',
    'integer':'INTEGER',
    'bigint': 'BIGINT',
    'numeric':'NUMERIC',
    'decimal':'DECIMAL',
    'real': 'REAL',
    'double':'DOUBLE','precision': 'PRECISION',
    'money':'MONEY',
    # TIPOS DE CARACTER
    'character':'CHARACTER', 'varying':'VARYING',
    'char':'CHAR',
    'text':'TEXT',
    #TIPOS DATA/TIME
    'timestamp':'TIMESTAMP',
    'time':'TIME',
    'data':'DATA',
    'with':'WITH',
    'zone':'ZONE',
    'interval':'INTERVAL',
    # fields - de tiempo 
    'year':'YEAR',
    'month':'MONTH',
    'day':'DAY',
    'hour':'HOUR',
    'minute':'MINUTE',
    'second':'SECOND',
    'to':'TO',
    # tipo Booleano
    'boolean':'BOOLEAN',
    'false':'FALSE',
    'true':'TRUE',
    # ENUMERATED TYPE
    'type':'TYPE',
    'enum':'ENUM',
    # FUNCIONES DE AGREGACION 
    'sum':'SUM',
    'now':'NOW',
    'date':'DATE',
    'avg':'AVG',
    'max':'MAX',
    'min':'MIN',
    'abs':'ABS',
    'cbrt':'CBRT',
    'ceil':'CEIL',
    'ceiling':'CEILING',
    'degrees':'DEGREES',
    'div':'DIV',
    'exp':'EXP',
    'factorial':'FACTORIAL',
    'floor':'FLOOR',
    'gcd':'GCD',
    'ln':'LN',
    'log':'LOG',
    'mod':'MOD',
    'pi':'PI',
    'power':'POWER',
    'radians':'RADIANS',
    'round':'ROUND',
    'sing':'SING',
    'sqrt':'SQRT',
    'width_bucket':'WIDTH_BUCKET',
    'trunc':'TRUNC',
    'random':'RANDOM',
    'acos':'ACOS',
    'acosd':'ACOSD',
    'asin':'ASIN',
    'asind':'ASIND',
    'atan':'ATAN',
    'atand':'ATAND',
    'atan2':'ATAN2',
    'atan2d':'ATAN2D',
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
    'md5':'MD5',
    'sha256':'SHA256',
    'substr':'SUBSTR',
    'get_byte':'GET_BYTE',
    'set_byte':'SET_BYTE',
    'convert':'CONVERT',
    'encode':'ENCODE',
    'decode':'DECODE',
    'order':'ORDER',
    'nulls':'NULLS',
    'count':'COUNT',
    'end':'END',
    'greatest':'GREATEST',
    'least':'LEAST',
    'extract':'EXTRACT',
    'date_part':'DATE_PART',
    'current_date':'CURRENT_DATE',
    'current_timestamp':'CURRENT_TIMESTAMP',

}
tokens = [
    # corchetes no porque dijo el aux que no venia
    'ID',
    'REGEX',
    'NUMERO',
    'PUNTO',
    'DECIMAL_LITERAL',
    'CADENA',
    'PTCOMA',
    'IGUAL',
    'MAYOR',
    'MENOR',
    'DIFERENTE',
    'DIFERENTE2',
    'MAYORIGUAL',
    'MENORIGUAL', 
    'MAS',
    'MENOS',
    'ASTERISCO',
    'DIVISION',
    'PABRE',
    'PCIERRA',
    'COMA',
    'TYPECAST',
    'EXPONENT',
    'MODULO',
    'PIPE',
    'DOBLE_PIPE',
     # Binary string funcions - operators: 
    'AMPERSAND',
    'NUMERAL',
    'BITWISE_NOT',
    'CORRIMIENTO_DER',
    'CORRIMIENTO_IZQ',
    'NOTBETWEEN',
    'CADENA_DATE',
    'CADENA_NOW',
    'CADENA_INTERVAL',
    'DOBLE_PUNTO',
    'NOT_IN'
] + list(palabrasReservadas.values())


# expresiones regulares
t_CORRIMIENTO_DER = r'>>'
t_CORRIMIENTO_IZQ = r'<<'
t_BITWISE_NOT = r'~'
t_AMPERSAND = r'&'
t_NUMERAL = r'\#'
t_PIPE = r'\|'
t_DOBLE_PIPE =  r'\|\|'
t_MODULO = r'%'
t_EXPONENT = r'\^'
t_TYPECAST =r'[:][:]'
t_PTCOMA = r';'
t_IGUAL  = r'='
t_DIFERENTE2 = r'[!][=]'
t_MAYOR  = r'>'
t_MENOR  = r'<'
t_MAS = r'\+'
t_MENOS = r'-'
t_PUNTO = r'\.'
t_ASTERISCO = r'\*'
t_DIVISION = r'/'
t_DIFERENTE = r'[<][>]'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_PABRE = r'\('
t_PCIERRA = r'\)'
t_COMA = r','
t_DOBLE_PUNTO= r'[:][:]'


def t_NOTBETWEEN(t):
    r'[Nn][Oo][tT][ ]+[Bb][eE][tT][wW][eE][eE][nN]'
    t.type = 'NOTBETWEEN'
    return t
def t_NOT_IN(t):
    r'[Nn][Oo][tT][ ]+[iI][nN]'
    t.type = 'NOT_IN'
    return t
# funcion para id, aca tambien se reconocen las palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palabrasReservadas.get(t.value.lower(),'ID')
    return t # se retorna para puede que se cambie el type del token

def t_DECIMAL_LITERAL(t): # primer se verifica que sea un decimal , sino es solo un numero
    r'\d+[.]\d+'
    t.value = float(t.value)
    return t

def t_NUMERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print('ese numero entero es muy grande')
        t.value = 0
    return t



def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_COMENTARIO_DE_UNA_LINEA(t):
    r'[-][-].*\n'
    t.lexer.lineno +=1
    
def t_COMENTARIO_MULTI(t):
    r'/\*(.|\n)*?\*/' # falta reconocer comentario adentro de comentario 
    t.lexer.lineno += t.value.count('\n')
 
def t_REGEX(t): # primero verifico , si es un regex
    r'[\'][%].*[%][\']'
    t.value = t.value[1:-1]
    return t 
def t_REGEX2(t): # primero verifico , si es un regex
    r'[\"][%].*[%][\"]'
    t.value = t.value[1:-1]
    t.type = 'REGEX'
    return t
def t_CADENA_NOW(t):
    r'\'[Nn][oO][wW]\''
    t.value =  t.value[1:-1]
    t.type = "CADENA_NOW"
    return t 
def t_CADENA_INTERVAL(t):
    r'\'[ ]*([\d][\d]?[ ]+hours|[\d][\d]?[ ]+seconds|[\d][\d]?[ ]+minutes)([ ]+([\d][\d]?[ ]+hours|[\d][\d]?[ ]+seconds|[\d][\d]?[ ]+minutes))?([ ]([\d][\d]?[ ]+hours|[\d][\d]?[ ]+seconds|[\d][\d]?[ ]+minutes))?[ ]*\''
    t.value =  t.value[1:-1]
    t.type = "CADENA_INTERVAL"
    return t

def t_CADENA_DATE4(t):# HORA Y MINUTOS 
    r'\'[ ]*[\d][\d]?[:][\d][\d]?[ ]*\''
    t.value =  t.value[1:-1]
    t.type = "CADENA_DATE"
    return t

def t_CADENA_DATE3(t): # HORA MIN , SEG 
    r'\'[ ]*[\d][\d]?[:][\d][\d]?[:][\d][\d]?[ ]*\''
    t.value =  t.value[1:-1]
    t.type = "CADENA_DATE"
    return t

def t_CADENA_DATE2(t):
    r'\'[ ]*[\d][\d][\d][\d][-][\d][\d]?[-][\d][\d]?[ ]+[\d][\d]?[:][\d][\d]?[:][\d][\d]?[ ]*\''
    t.value =  t.value[1:-1]
    t.type = "CADENA_DATE"
    return t
def t_CADENA_DATE(t):
    r'\'[ ]*[\d][\d][\d][\d][-][\d][\d]?[-][\d][\d]?[ ]*\''
    t.value =  t.value[1:-1]
    t.type = "CADENA_DATE"
    return t
# comillas simples y dobles ambos se reconocen como token tipo CADENA
def t_CADENA(t):
    r'\"[^"]*\"'
    t.value = t.value[1:-1] # quitando las comillas dobles al inicio y al final
    return t
def t_CADENA2(t):
    r'\'[^\']*\''
    t.value = t.value[1:-1] # quitando las comillas dobles al inicio y al final
    t.type = "CADENA"
    return t

#ignorando espacios    
t_ignore = ' \t'

def t_error(t):
    print(f'Error lexico: {t.value[0]}')
    error = ErrorReport('lexico', f'error lexico con {t.value[0]}', t.lineno)
    listaErrores.addError(error)
    t.lexer.skip(1)





# construyendo el lexico
import ply.lex as lex
lexer = lex.lex(reflags = re.IGNORECASE)

#para debugger los nuevos tokens
# lexer.input('''
# SELECT date_part('minutes', INTERVAL '4 houRs 3 miNutes');
# SELECT date_part('minutes', INTERVAL '4 hours 3 minutes');
# SELECT date_part('seconds', INTERVAL '4 hours 3 minutes 15 seconds');
# ''')
# while not False:
#     token = lexer.token()
#     if not token:
#         break
#     print(f'tipo: {token.type} valor: {token.value}  linea:{token.lineno} col:{token.lexpos}')


