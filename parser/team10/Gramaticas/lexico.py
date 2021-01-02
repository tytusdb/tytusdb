#LEX
from ply import *

elex = []

#lexer = lex.lex()

keywords = (
    'create', 'varchar', 'date', 'not', 'null', 'identity', 'primary', 'key', 'alter', 'database', 'owner',
    'table', 'add', 'drop', 'truncate', 'insert', 'into', 'values', 'update', 'set', 'from','delete', 'select', 
    'where', 'as', 'and', 'or','smallint', 'integer', 'bigint', 'decimal', 'numeric', 'real', 'double', 'money',
    'char', 'varying', 'character', 'text', 'boolean', 'type', 'enum', 'replace', 'if',  'exist',  'column',
    'exists', 'show', 'databases', 'int', 'foreing', 'references', 'inherits', 'only', 'group', 'by', 'having',
    'order', 'asc', 'desc', 'inner', 'left', 'right', 'full', 'on', 'outer', 'join', 'check', 'constraint',
    'to', 'rename' , 'sum', 'avg', 'max', 'min', 'pi', 'power', 'sqrt', 'like', 'union', 'in', 'limit', 'offset',
    'intersect', 'except', 'between', 'extract', 'year', 'month', 'day', 'hour', 'minute', 'second', 'interval',
    'timestamp', 'current_date', 'current_time', 'now', 'date_part', 'mode', 'substring', 'distinct', 'case',
    'when', 'then', 'end', 'is', 'true', 'false','use', 'abs', 'cbrt', 'ceil', 'celing', 'degrees', 'exp', 
    'factorial', 'floor', 'ln', 'log', 'radians',  'sign', 'sqrt', 'width_bucket', 'random', 'div', 
    'gcd', 'mod', 'round', 'acos', 'acosd', 'asin', 'asind', 'atan', 'atand', 'atan2', 'cos', 'cosd', 'cot', 
    'cotd', 'sin', 'sind', 'tan', 'tand', 'sinh', 'cosh', 'tanh', 'asinh', 'acosh', 'atanh', 'substr', 'set_byte', 
    'convert', 'decode', 'trim', 'md5', 'length', 'sha256', 'get_byte', 'encode', 'bytea'
)

tokens = keywords + (
	'igual', 'mas' ,'menos' ,'por' ,'division','par1','par2','menor', 'menorigual', 'mayor', 'mayorigual', 
	'diferente', 'coma', 'punto', 'pyc', 'num', 'pdecimal' ,'cadena', 'NEWLINE', 'dosp',
	'vacio', 'porcentaje', 'cor1', 'cor2', 'identificador', 'cadenacaracter'
)

t_igual = r'='
t_porcentaje = r'%'
t_mas = r'\+'
t_menos = r'-'
t_por = r'\*'
t_division = r'/'
t_par1 = r'\('
t_par2 = r'\)'
t_cor1 = r'\['
t_cor2 = r'\]'
t_menor = r'<'
t_menorigual = r'<='
t_mayor = r'>'
t_mayorigual = r'>='
t_diferente = r'<>'
t_coma = r'\,'
t_punto = r'\.'
t_pyc = r';'
t_dosp = r':'
t_num = r'\d+'
t_vacio = r'\'\''
t_pdecimal = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_cadena = r'\".*?\"'
t_cadenacaracter = r'\'.*?\''

t_ignore_COMMENT = r'\/\*.*\*\/'

t_ignore = ' \t'


def t_identificador(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    if t.value in keywords:
        t.type = t.value
    return t

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)
    

lex.lex(debug=0)