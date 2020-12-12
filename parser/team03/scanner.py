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
    'now' : 'NOW',
    'current_date' : 'CURRENT_DATE',
    'current_time' : 'CURRENT_TIME',
    'boolean' : 'BOOLEAN',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'between' : 'BETWEEN',
    'in' : 'IN',
    'like' : 'LIKE',
    'ilike' : 'ILIKE',
    'similar' : 'SIMILAR',
    'is' : 'IS',
    'isnull' : 'ISNULL',
    'null' : 'NULL',
    'notnull' : 'NOTNULL',
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
    'rund' : 'RUND',
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
    'gratest' : 'GRATEST',
    'least' : 'LEAST',
    'order' : 'ORDER',
    'limit' : 'LIMIT',
    'offset' : 'OFFSET',
    'union' : 'UNION',
    'intersect' : 'INTERSECT',
    'except' : 'EXCEPT',
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
    'ID',
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
t_DIFERENTE = r'<>'


# ignored regular expressions
t_ignore = " \t"
t_ignore_COMMENT =r'\-\-.*'
t_ignore_COMMENTMULTI = r'(/\*(.|\n)*?\*/)|(//.*)'


def t_FLOAT(t):
    r'((\d*\.\d*)((e[\+-]?\d+)?)|(\d*e[\+-]?\d+))'
    print(t.value)
    t.value = float(t.value)    
    return t


def t_ENTERO(t):
    r'\d+'
    t.value = int(float(t.value))  
    return t

def t_TEXTO(t):
    r'\'([^\\\n]|(\\.))*?\''
    t.type = reserved.get(t.value,'TEXTO')    # Check for reserved words
    return t
    
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(),'ID')    # Check for reserved words
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Construyendo el analizador léxico
lexer = lex.lex(debug = False, reflags=re.IGNORECASE) 