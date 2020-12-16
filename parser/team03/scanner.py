import ply.lex as lex
import re

reserved = {
    'smallint' : 'SMALLINT',
    'integer' : 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'double' : 'DOUBLE',
    'precision' : 'PRECISION',
    'money' : 'MONEY',
    'caracter' : 'CARACTER',
    'varying' : 'VARYING',
    'varchar' : 'VARCHAR',
    'character' : 'CHARACTER',
    'char' : 'CHAR',
    'text' : 'TEXT',
    'timestamp' : 'TIMESTAMP',
    'date' : 'DATE',
    'time' : 'TIME',
    'interval' : 'INTERVAL',
    'year' : 'YEAR',
    'month' : 'MONTH',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'extract' : 'EXTRACT',
    'date_part' : 'DATE_PART',
    'now' : 'NOW',
    'current_date' : 'CURRENT_DATE',
    'current_time' : 'CURRENT_TIME',
    'boolean' : 'BOOLEAN',
    'between' : 'BETWEEN',
    'symmetric' : 'SYMMETRIC',
    'in' : 'IN',
    'like' : 'LIKE',
    'ilike' : 'ILIKE',
    'similar' : 'SIMILAR',
    'is' : 'IS',
    'null' : 'NULL',
    'not' : 'NOT',
    'and' : 'AND',
    'or' : 'OR',
    'select' : 'SELECT',
    'from' : 'FROM',
    'where' : 'WHERE',
    'create' : 'CREATE',
    'type' : 'TYPE',
    'as' : 'AS',
    'enum' : 'ENUM',
    'replace' : 'REPLACE',
    'database' : 'DATABASE',
    'if' : 'IF',
    'exists' : 'EXISTS',
    'owner' : 'OWNER',
    'mode' : 'MODE',
    'show' : 'SHOW',
    'databases' : 'DATABASES',
    'alter' : 'ALTER',
    'rename' : 'RENAME',
    'to' : 'TO',
    'drop' : 'DROP',
    'current_user' : 'CURRENT_USER',
    'session_user' : 'SESSION_USER',
    'table' : 'TABLE',
    'default' : 'DEFAULT',
    'constraint' : 'CONSTRAINT',
    'unique' : 'UNIQUE',
    'check' : 'CHECK',
    'primary' : 'PRIMARY',
    'key' : 'KEY',
    'references' : 'REFERENCES',
    'foreign' : 'FOREIGN',
    'add' : 'ADD',
    'column' : 'COLUMN',
    'set' : 'SET',
    'inherits' : 'INHERITS',
    'insert' : 'INSERT',
    'into' : 'INTO',
    'values' : 'VALUES',
    'update' : 'UPDATE',
    'delete' : 'DELETE',
    'distinct' : 'DISTINCT',
    'group' : 'GROUP',
    'by' : 'BY',
    'having' : 'HAVING',
    'unknown' : 'UNKNOWN',
    'count' : 'COUNT',
    'min' : 'MIN',
    'max' : 'MAX',
    'sum' : 'SUM',
    'avg' : 'AVG',
    'abs' : 'ABS',
    'cbrt' : 'CBRT',
    'ceil' : 'CEIL',
    'ceiling' : 'CEILING',
    'degrees' : 'DEGREES',
    'div' : 'DIV',
    'exp' : 'EXP',
    'factorial' : 'FACTORIAL',
    'floor' : 'FLOOR',
    'gcd' : 'GCD',
    'lcm' : 'LCM',
    'ln' : 'LN',
    'log' : 'LOG',
    'log10' : 'LOG10',
    'min_scale' : 'MIN_SCALE',
    'mod' : 'MOD',
    'pi' : 'PI',
    'power' : 'POWER',
    'radians' : 'RADIANS',
    'round' : 'ROUND',
    'scale' : 'SCALE',
    'sign' : 'SIGN',
    'sqrt' : 'SQRT',
    'trim_scale' : 'TRIM_SCALE',
    'truc' : 'TRUC',
    'width_bucket' : 'WIDTH_BUCKET',
    'random' : 'RANDOM',
    'setseed' : 'SETSEED',
    'acos' : 'ACOS',
    'acosd' : 'ACOSD',
    'asin' : 'ASIN',
    'asind' : 'ASIND',
    'atan' : 'ATAN',
    'atand' : 'ATAND',
    'atan2' : 'ATAN2',
    'atan2d' : 'ATAN2D',
    'cos' : 'COS',
    'cosd' : 'COSD',
    'cot' : 'COT',
    'cotd' : 'COTD',
    'sin' : 'SIN',
    'sind' : 'SIND',
    'tan' : 'TAN',
    'tand' : 'TAND',
    'sinh' : 'SINH',
    'cosh' : 'COSH',
    'tanh' : 'TANH',
    'asinh' : 'ASINH',
    'acosh' : 'ACOSH',
    'atanh' : 'ATANH',
    'length' : 'LENGTH',
    'substring' : 'SUBSTRING',
    'trim' : 'TRIM',
    'get_byte' : 'GET_BYTE',
    'md5' : 'MD5',
    'set_byte' : 'SET_BYTE',
    'sha256' : 'SHA256',
    'substr' : 'SUBSTR',
    'convert' : 'CONVERT',
    'encode' : 'ENCODE',
    'decode' : 'DECODE',
    'substring' : 'SUBSTRING',
    'any' : 'ANY',
    'all' : 'ALL',
    'some' : 'SOME',
    'asc' : 'ASC',
    'desc' : 'DESC',
    'case' : 'CASE',
    'when' : 'WHEN',
    'then' : 'THEN',
    'else' : 'ELSE',
    'end' : 'END',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    'order' : 'ORDER',
    'limit' : 'LIMIT',
    'offset' : 'OFFSET',
    'union' : 'UNION',
    'intersect' : 'INTERSECT',
    'except' : 'EXCEPT',
    'inner' : 'INNER',
    'left' : 'LEFT',
    'right' : 'RIGHT',
    'full' : 'FULL',
    'outer' : 'OUTER',
    'join' : 'JOIN',
    'on' : 'ON',
    'using' : 'USING',
    'natural' : 'NATURAL',
    'first' : 'FIRST',
    'last' : 'LAST',
    'nulls' : 'NULLS',

}

tokens = [
    'PARA',
    'PARC',
    'CORCHA',
    'CORCHC',
    'PUNTO',
    'COMA',
    'PUNTOCOMA',
    'MAS',
    'MENOS',
    'POR',
    'DIAGONAL',
    'EXPONENCIANCION',
    'PORCENTAJE',
    'MAYOR',
    'MENOR',
    'IGUAL',
    'MAYORQ',
    'MENORQ',
    'DIFERENTE',
    'ENTERO',
    'FLOAT',
    'TEXTO',
    'FECHA_HORA',
    'PATTERN_LIKE',
    'BOOLEAN_VALUE',
    'ID',
    'SQUARE_ROOT',
    'CUBE_ROOT',
    'AMPERSON',
    'NUMERAL',
    'PRIME',
    'SHIFT_L',
    'SHIFT_R',
] +list(reserved.values()) 

t_PARA = r'\('
t_PARC = r'\)'
t_CORCHA = r'\['
t_CORCHC = r'\]'
t_PUNTO = r'\.'
t_COMA = r'\,'
t_PUNTOCOMA = r'\;'
t_MAS = r'\+'
t_MENOS = r'\-'
t_POR = r'\*'
t_DIAGONAL = r'\/'
t_EXPONENCIANCION = r'\^'
t_PORCENTAJE = r'%'
t_MAYOR = r'>'
t_MENOR = r'<'
t_IGUAL = r'='
t_MAYORQ = r'>='
t_MENORQ = r'<='
t_SQUARE_ROOT = r'\|'
t_CUBE_ROOT = r'\|\|'
t_AMPERSON = r'\&'
t_NUMERAL = r'\#'
t_PRIME = r'\~'
t_SHIFT_L = r'<<'
t_SHIFT_R = r'>>'



# ignored regular expressions
t_ignore = " \t"
t_ignore_COMMENT =r'\-\-.*'
t_ignore_COMMENTMULTI = r'(/\*(.|\n)*?\*/)|(//.*)'

def t_DIFERENTE(t):
    r'((<>)|(!=))'
    t.type = reserved.get(t.value,'DIFERENTE')    
    return t


def t_FLOAT(t):
    r'((\d+\.\d*)((e[\+-]?\d+)?)|(\d*e[\+-]?\d+))'
    t.value = float(t.value)    
    return t


def t_ENTERO(t):
    r'\d+'
    t.value = int(float(t.value))  
    return t

def t_FECHA_HORA(t):
    r'\'\d{4}-[0-1]?\d-[0-3]?\d [0-2]\d:[0-5]\d:[0-5]\d\''
    t.value = t.value[1:-1]
    t.type = reserved.get(t.value,'FECHA_HORA')
    return t

def t_PATTERN_LIKE(t):
    r'\'\%.*\%\''
    t.value = t.value[2:-2]
    t.type = reserved.get(t.value,'PATTERN_LIKE')
    return t

def t_TEXTO(t):
    r'\'([^\\\n]|(\\.))*?\''
    t.value = t.value[1:-1]
    t.type = reserved.get(t.value,'TEXTO')    
    return t
    
def t_BOOLEAN_VALUE(t):
    r'((false)|(true))'
    t.value = t.value.lower()
    t.type = reserved.get(t.value,'BOOLEAN_VALUE')    
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(),'ID')    
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
    
def t_error(t):
    print("--> Error Lexico: Illegal character \'"+ t.value[0] + "\' Line: "+ str(t.lineno) )
    t.lexer.skip(1)


lexer = lex.lex(debug = False, reflags=re.IGNORECASE) 