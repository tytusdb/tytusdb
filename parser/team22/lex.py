from tabla_errores import *
tabla_errores = TablaDeErrores()

##-------------------------GRAMATICA ASCENDENTE-------------------------------
reservadas = {
    'create' : 'CREATE',
    'databases' : 'DATABASES',  
    'database' : 'DATABASE', 
    'current_user': 'CURRENT_USER',
    'session_user': 'SESSION_USER',   
    'table' : 'TABLE',
    'insert': 'INSERT',
    'inherits' : 'INHERITS',
    'smallint': 'SMALLINT',
    'integer': 'INTEGER',
    'bigint': 'BIGINT',
    'decimal': 'R_DECIMAL',
    'numeric': 'NUMERIC',
    'real': 'REAL',
    'double': 'DOUBLE',
    'precision': 'PRECISION',
    'money': 'MONEY',
    'character': 'CHARACTER',
    'varying': 'VARYING',
    'varchar' : 'VARCHAR',
    'bytea' : 'BYTEA',
    'char' : 'CHAR',
    'text' : 'TEXT',
    'now' : 'NOW',
    'date_part' : 'date_part',
    'current_date' : 'CURRENT_DATE',
    'current_time' : 'CURRENT_TIME',
    'extract' : 'EXTRACT',
    'timestamp' : 'TIMESTAMP',
    'without' : 'WITHOUT',
    'time' : 'TIME',
    'zone' : 'ZONE',
    'date' : 'DATE',
    'interval' : 'INTERVAL',
    'month' : 'MONTH',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'boolean' : 'BOOLEAN',
    'year' : 'YEAR',
    'datetime' : 'DATETIME',
    'drop' : 'DROP',
    'alter' : 'ALTER',
    'delete' : 'DELETE',
    'not' : 'NOT',
    'null' : 'NULL',
    'foreign' : 'FOREIGN',
    'key' : 'KEY',
    'primary' : 'PRIMARY',
    'references' : 'REFERENCES',
    'use' : 'USE',
    'select' : 'SELECT',
    'distinct' : 'DISTINCT',
    'as' : 'AS',
    'enum' : 'ENUM',
    'type' : 'TYPE',
    'from' : 'FROM',
    'left' : 'LEFT',
    'join' : 'JOIN',
    'right' : 'RIGHT',
    'on' : 'ON',
    'any' : 'ANY',
    'count' : 'COUNT',
    'sum' : 'SUM',
    'like' : 'LIKE',
    'avg' : 'AVG',
    'abs' : 'ABS',
    'cbrt' : 'CBRT',
    'ceil' : 'CEIL',
    'ceiling' : 'CEILING',
    'degrees' : 'DEGREES',
    'div' : 'DIV',
    'exp' : 'REXP',
    'factorial' : 'FACTORIAL',
    'floor' : 'FLOOR',
    'gcd' : 'GCD',
    'ln' : 'LN',
    'log' : 'LOG',
    'mod' : 'MOD',
    'pi' : 'PI',
    'power' : 'POWER',
    'radians' : 'RADIANS',
    'round' : 'ROUND',
    'acos' : 'ACOS',
    'asin' : 'ASIN',
    'atan' : 'ATAN',
    'atan2' : 'ATAN2',
    'cos' : 'COS',
    'cot' : 'COT',
    'sin' : 'SIN',
    'tan' : 'TAN',
    'acosd' : 'ACOSD',
    'asind' : 'ASIND',
    'atand' : 'ATAND',
    'atan2d' : 'ATAN2D',
    'cosd' : 'COSD',
    'cotd' : 'COTD',
    'sind' : 'SIND',
    'tand' : 'TAND',
    'sinh' : 'SINH',
    'cosh' : 'COSH',
    'tanh' : 'TANH',
    'asinh' : 'ASINH',
    'acosh' : 'ACOSH',
    'atanh' : 'ATANH',
    'max' : 'MAX',
    'min' : 'MIN',
    'order' : 'ORDER',
    'where' : 'WHERE',
    'if' : 'IF',
    'owner' : 'OWNER',
    'mode' : 'MODE',
    'and' : 'AND',
    'or' : 'OR',
    'between' : 'BETWEEN',
    'in' : 'IN',
    'inner' : 'INNER',
    'full' : 'FULL',
    'self' : 'SELF',
    'case' : 'CASE',
    'union' : 'UNION',
    'group' : 'GROUP',
    'having' : 'HAVING',
    'exists' : 'EXISTS',
    'intersect' : 'INTERSECT',
    'except' : 'EXCEPT',
    'offset' : 'OFFSET',
    'limit' : 'LIMIT',
    'all' : 'ALL',
    'into' : 'INTO',
    'some' : 'SOME',
    'backup' : 'backup',
    'to' : 'TO',
    'disk' : 'DISK',
    'constraint' : 'CONSTRAINT',
    'rename' : 'RENAME',
    'add' : 'ADD',
    'check' : 'CHECK',
    'default' : 'DEFAULT',
    'modify' : 'MODIFY',
    'column' : 'COLUMN',
    'set' : 'SET',
    'unique' : 'UNIQUE',
    'index' : 'INDEX',
    'auto_increment' : 'AUTO_INCREMENT',
    'values' : 'VALUES',
    'identity' : 'IDENTITY',
    'by' : 'BY',
    'with' : 'WITH',
    'replace' : 'REPLACE',    
    'desc' : 'DESC',
    'outer' : 'OUTER',
    'is' : 'IS',
    'top' : 'TOP',
    'truncate' : 'TRUNCATE',
    'update' : 'UPDATE',
    'asc' : 'ASC',
    'show': 'SHOW',
    'when' : 'WHEN',
    'then' : 'THEN',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    'end' : 'END',
    'else' : 'ELSE',
    'least': 'LEAST',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'unknown' : 'UNKNOWN',
    'isnull' : 'ISNULL',
    'notnull' : 'NOTNULL',
    'length' : 'LENGTH',
    'substring' : 'SUBSTRING',
    'trim' : 'TRIM',
    'md5' : 'MD5',
    'sha256' : 'SHA256',
    'substr' : 'SUBSTR',
    'get_byte' : 'GET_BYTE',
    'set_byte' : 'SET_BYTE',
    'convert' : 'CONVERT',
    'encode' : 'ENCODE',
    'decode' : 'DECODE',
    'sign' : 'SIGN',
    'sqrt' : 'SQRT',
    'width_bucket' : 'WIDTH_BUCKET',
    'trunc' : 'TRUNC',
    'random' : 'RANDOM',
    'exp' : 'EXP'
}

tokens  = [
    'PTCOMA',
    'PARIZQ',
    'PARDER',
    'COMA',
    'PUNTO',
    'MAS',
    'MENOS',
    'POR',
    'DIVISION',
    'MODULO',
    'CONCAT',
    'PIPE',
    'IGUAL',
    'MAYORIGUAL',
    'MAYOR',
    'DIFERENTE',
    'NO_IGUAL',
    'MENORIGUAL',
    'MENOR',
    'ASIGNACION_SUMA',
    'ASIGNACION_RESTA',
    'ASIGNACION_MULT',
    'ASIGNACION_DIVID',
    'ASIGNACION_MODULO',
    'DOS_PUNTOS',
    'DIAG_INVERSA',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'ID',
    'COMILLA_SIMPLE'
] + list(reservadas.values())

# Tokens
t_PTCOMA            = r';'
t_PARIZQ            = r'\('
t_PARDER            = r'\)'
t_COMA              = r'\,'
t_PUNTO             = r'\.'
t_MAS               = r'\+'
t_MENOS             = r'-'
t_POR               = r'\*'
t_DIVISION          = r'/'
t_MODULO            = r'\%'
t_PIPE              = r'\|'
t_EXP               = r'\^'
t_IGUAL             = r'\='
t_MAYOR             = r'>'
t_MENOR             = r'<'
t_MENORIGUAL        = r'<='
t_MAYORIGUAL        = r'>='
t_DIFERENTE         = r'<>'
t_NO_IGUAL          = r'!='
t_ASIGNACION_SUMA   = r'\+='
t_ASIGNACION_RESTA  = r'\-='
t_ASIGNACION_MULT   = r'\*='
t_ASIGNACION_DIVID  = r'\/='
t_ASIGNACION_MODULO = r'\%='
t_DOS_PUNTOS        = r'\:'
t_DIAG_INVERSA      = r'\\'
t_COMILLA_SIMPLE    = r'\''

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_@#][a-zA-Z_0-9@$#]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_CADENA(t):
    r'(\'.*?\')|(\".*?\")'
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_error(t):
    error = Error('Léxico', "Caracter desconocido '%s'" % t.value[0], t.lexer.lineno)
    tabla_errores.agregar(error)
    print(error.imprimir())
    t.lexer.skip(1)