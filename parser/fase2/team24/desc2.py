import time

# Parte lexica en ply

reservadas = {
    'smallint': 'SMARLLINT',
    'integer': 'INTEGER',
    'bigint': 'BIGINT',
    'decimal': 'DECIMAL',
    'numeric': 'NUMERIC',
    'real': 'REAL',
    'double': 'DOUBLE',
    'precision': 'PRECISION',
    'character': 'CHARACTER',
    'varying': 'VARYING',
    'text': 'TEXT',
    'timestamp': 'TIMESTAMP',
    'select': 'SELECT',
    'extract': 'EXTRACT',
    'year': 'YEAR',
    'day': 'DAY',
    'hour': 'HOUR',
    'minute': 'MINUTE',
    'second': 'SECOND',
    'month': 'MONTH',
    'date_part': 'DATE_PART',
    'from': 'FROM',
    'current_date': 'CURRENT_DATE',
    'current_time': 'CURRENT_TIME',
    'boolean': 'BOOLEAN',
    'create': 'CREATE',
    'type': 'TYPE',
    'as': 'AS',
    'between': 'BETWEEN',
    'is': 'IS',
    'like': 'LIKE',
    'in': 'IN',
    'null': 'NULL',
    'not': 'NOT',
    'and': 'AND',
    'or': 'OR',
    'replace': 'REPLACE',
    'database': 'DATABASE',
    'if': 'IF',
    'owner': 'OWNER',
    'alter': 'ALTER',
    'rename': 'RENAME',
    'to': 'TO',
    'current_user': 'CURRENT_USER',
    'session_user': 'SESSION_USER',
    'drop': 'DROP',
    'exists': 'EXISTS',
    'table': 'TABLE',
    'constraint': 'CONSTRAINT',
    'unique': 'UNIQUE',
    'check': 'CHECK',
    'key': 'KEY',
    'primary': 'PRIMARY',
    'references': 'REFERENCES',
    'foreign': 'FOREIGN',
    'set': 'SET',
    'column': 'COLUMN',
    'inherits': 'INHERITS',
    'insert': 'INSERT',
    'into': 'INTO',
    'update': 'UPDATE',
    'delete': 'DELETE',
    'where': 'WHERE',
    'values': 'VALUES',
    'by': 'BY',
    'having': 'HAVING',
    'abs': 'ABS',
    'cbrt': 'CBRT',
    'ceil': 'CEIL',
    'ceiling': 'CEILING',
    'degrees': 'DEGREES',
    'div': 'DIV',
    'exp': 'EXP',
    'factorial': 'FACTORIAL',
    'floor': 'FLOOR',
    'gcd': 'GCD',
    'lcm': 'LCM',
    'ln': 'LN',
    'log': 'LOG',
    'log10': 'LOG10',
    'min_scale': 'MIN_SCALE',
    'mod': 'MOD',
    'pi': 'PI',
    'power': 'POWER',
    'radians': 'RADIANS',
    'round': 'ROUND',
    'scale': 'SCALE',
    'sign': 'SIGN',
    'sqrt': 'SQRT',
    'trim_scale': 'TRIM_SCALE',
    'truc': 'TRUC',
    'width_bucket': 'WIDTH_BUCKET',
    'random': 'RANDOM',
    'setseed': 'SETSEED',
    'count': 'COUNT',
    'length': 'LENGHT',
    'substring': 'SUBSTRING',
    'trim': 'TRIM',
    'get_byte': 'GET_BYTE',
    'md5': 'MD5',
    'set_byte': 'SET_BYTE',
    'sha256': 'SHA256',
    'substr': 'SUBSTR',
    'case': 'CASE',
    'when': 'WHEN',
    'else': 'ELSE',
    'end': 'END',
    'greatest': 'GREATEST',
    'least': 'LEAST',
    'limit': 'LIMIT',
    'asc': 'ASC',
    'desc': 'DESC',
    'first': 'FISRT',
    'last': 'LAST',
    'nulls': 'NULLS',
    'offset': 'OFFSET',
    'all': 'ALL',
    'union': 'UNION',
    'intersect': 'INTERSECT',
    'then': 'THEN',
    'decode': 'DECODE',
    'except': 'EXCEPT',
    'distinct': 'DISTINCT',
    'group': 'GROUP',
    'show': 'SHOW',
    'mode': 'MODE',
    'regex': 'REGEX',
    'add': 'ADD',
    'default': 'DEFAULT'
}

tokens = [
             'VIR',
             'DEC',
             'MAS',
             'MENOS',
             'ELEVADO',
             'MULTIPLICACION',
             'DIVISION',
             'MODULO',
             'MENOR',
             'MAYOR',
             'IGUAL',
             'MENOR_IGUAL',
             'MAYOR_IGUAL',
             'MENOR_MENOR',
             'MAYOR_MAYOR',
             'DIFERENTE',
             'SIMBOLOOR',
             'SIMBOLOAND',
             'PTCOMA',
             'LLAVEA',
             'LLAVEC',
             'PARA',
             'PARC',
             'DOSPUNTOS',
             'COMA',
             'PUNTO',
             'INT',
             'VARCHAR',
             'CHAR',
             'ID',
             'ASTERISCO',
             'PYC'
         ] + list(reservadas.values())

# Token

t_VIR = r'~'
t_MAS = r'\+'
t_MENOS = r'-'
t_ELEVADO = r'\^'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'
t_MENOR = r'<'
t_MAYOR = r'>'
t_IGUAL = r'='
t_MENOR_IGUAL = r'<='
t_MAYOR_IGUAL = r'>='
t_MENOR_MENOR = r'<<'
t_MAYOR_MAYOR = r'>>'
t_DIFERENTE = r'<>'
t_SIMBOLOOR = r'\|'
t_SIMBOLOAND = r'&'
t_LLAVEA = r'{'
t_LLAVEC = r'}'
t_PARA = r'\('
t_PARC = r'\)'
t_DOSPUNTOS = r':'
t_COMA = r','
t_PUNTO = r'.'
t_ASTERISCO = r'\*'
t_PYC = r'\;'


def t_DEC(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Error no se puede convertir %d", t.value)
        t.value = 0
    return t


def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor numerico incorrecto %d", t.value)
        t.value = 0
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t


def t_VARCHAR(t):
    r'\'.*?\''
    t.value = t.value[1:-1]  # remuevo las comillas
    return t


def t_COMENT_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1


def t_COMENT_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


t_ignore = " \t"


def t_nuevalinea(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Error lexico'%s'" % t.value[0])
    t.lexer.skip(1)


import ply.lex as lex

lexer = lex.lex()

precedence = (
    ('left', 'PUNTO'),
    # ('right','UMAS','UMENOS'),
    ('left', 'ELEVADO'),
    ('left', 'MULTIPLICACION', 'DIVISION', 'MODULO'),
    ('left', 'MAS', 'MENOS'),
    ('right', 'NOT'),
    ('left', 'AND'),
    ('left', 'OR')
)


# Importar lo que nos ayude a ejecutar
# from expresiones import *
# from instrucciones import *

def p_init(t):
    'init : inicio'


def p_inicio(t):
    '''inicio : CREATE sentencia_create
              | SHOW sentencia_show
              | ALTER sentencia_alter
              | DROP sentencia_drop
              |
    '''


def p_sentencia_create(t):
    '''sentencia_create : DATABASE sentencia_database
                        | OR REPLACE DATABASE sentencia_database
                        | TABLE sentencia_create_table
    '''


def p_sentencia_database(t):
    '''sentencia_database : IF NOT EXISTS ID owner_or_mode
                           | ID owner_or_mode
    '''


def p_owner_or_mode(t):
    '''owner_or_mode : OWNER IGUAL ID owner_or_mode
                     | MODE IGUAL INT owner_or_mode
                     | PYC inicio
    '''


def p_sentencia_show(t):
    '''sentencia_show : DATABASE LIKE REGEX PYC inicio
                       | DATABASE PYC inicio
    '''


def p_sentencia_alter(t):
    '''sentencia_alter : DATABASE ID rename_or_owner
                        | TABLE alter_table
    '''


def p_alter_table(t):
    '''alter_table : ID ADD COLUMN ID tipos
                   | ID ADD CONSTRAINT ID UNIQUE PARA ID PARC PYC inicio
                   | ID ADD FOREIGN KEY PARA ID PARC REFERENCES ID PYC inicio
                   | ID ALTER COLUMN ID SET NOT NULL PYC inicio
                   | ID DROP CONSTRAINT ID PYC inicio
                   | ID RENAME COLUMN ID TO ID PYC inicio
                   | ID DROP COLUMN ID PYC inicio
    '''


def p_tipos(t):
    '''tipos : INTEGER PYC inicio
             | BIGINT PYC inicio
             | DECIMAL PYC inicio
             | NUMERIC PYC inicio
             | REAL PYC inicio
             | DOUBLE PYC inicio
             | PRECISION PYC inicio
             | CHARACTER PYC inicio
             | VARYING PYC inicio
             | TEXT PYC inicio
    '''


def p_rename_or_owner(t):
    '''rename_or_owner : RENAME TO ID PYC inicio
                       | OWNER TO ID PYC inicio
                       | OWNER TO VARCHAR PYC inicio
    '''


def p_sentencia_drop(t):
    '''sentencia_drop : DATABASE IF EXISTS ID PYC inicio
                      | DATABASE ID PYC inicio
                      | TABLE ID PYC inicio
    '''


def p_sentencia_create_table(t):
    '''sentencia_create_table : ID PARA tabla_columna_inicial'''


def p_tabla_columna_inicial(t):
    '''tabla_columna_inicial : ID INTEGER tabla_identificador
                             | ID BIGINT tabla_identificador
                             | ID DECIMAL tabla_identificador
                             | ID NUMERIC tabla_identificador
                             | ID REAL tabla_identificador
                             | ID DOUBLE tabla_identificador
                             | ID PRECISION tabla_identificador
                             | ID CHARACTER tabla_identificador
                             | ID VARYING tabla_identificador
                             | ID TEXT tabla_identificador
    '''


def p_tabla_identificador(t):
    '''tabla_identificador : DEFAULT VARCHAR tabla_identificador
                           | NOT NULL tabla_identificador
                           | CONSTRAINT ID UNIQUE tabla_identificador
                           | PRIMARY KEY tabla_identificador
                           | REFERENCES tabla_identificador
                           | COMA tabla_columnas
                           | PRIMARY KEY sentencia_unique_or_key
                           | FOREIGN KEY sentencia_unique_or_key
                           | PARC PYC inicio
    '''


def p_tabla_columnas(t):
    '''tabla_columnas : ID INTEGER tabla_identificador
                      | ID BIGINT tabla_identificador
                      | ID DECIMAL tabla_identificador
                      | ID NUMERIC tabla_identificador
                      | ID REAL tabla_identificador
                      | ID DOUBLE tabla_identificador
                      | ID PRECISION tabla_identificador
                      | ID CHARACTER tabla_identificador
                      | ID VARYING tabla_identificador
                      | ID TEXT tabla_identificador
    '''


def p_sentencia_unique_or_key(t):
    '''sentencia_unique_or_key : ID COMA sentencia_unique_or_key
                                | ID PARC tabla_identificador_aux
    '''


def p_tabla_identficador_aux(t):
    '''tabla_identificador_aux : COMA tabla_columnas
                               | PARA PYC inicio
    '''


def p_error(t):
    print("Error sintáctico en '%s'" % t.value)


def Analizar(texto):
    global textoretorno
    textoretorno = ""
    start = time.time()
    parser.parse(texto)
    end = time.time()
    textoretorno += "Tiempo de ejecucion descendente: " + str(end - start)
    return textoretorno


import ply.yacc as yacc

parser = yacc.yacc()

f = open("./entrada2.txt", "r")
input = f.read()
print(input)
parser.parse(input)
