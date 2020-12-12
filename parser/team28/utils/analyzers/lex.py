import libs.ply.lex as lex
from libs.ply.lex import TOKEN
from models.error import Error
from controllers.linked_list import SingleLinkedList
from models.find_type_error import FindTypeError

# Hacen falta palabras reservadas hay que anadirlas
list_errors = SingleLinkedList()
id_error = 1

# Definitions of tokens reserved
k_reserved = {
    'ADD' : 'ADD',
    'ALL': 'ALL',
    'ALTER': 'ALTER',
    'ABS': 'ABS',
    'AND': 'AND',
    'AS': 'AS',
    'ASC': 'ASC',
    'AVG': 'AVG',
    'BETWEEN': 'BETWEEN',
    'BIGINT': 'BIGINT',
    'BOOLEAN': 'BOOLEAN',
    'BY': 'BY',
    'CBRT': 'CBRT',
    'CONVERT': 'CONVERT',
    'CEIL': 'CEIL',
    'CEILING': 'CEILING',
    'CHAR': 'CHAR',
    'CHARACTER': 'CHARACTER',
    'CHECK' : 'CHECK',
    'CREATE': 'CREATE',
    'COLUMN' : 'COLUMN',
    'CONSTRAINT' : 'CONSTRAINT',
    'COUNT': 'COUNT',
    'CURRENT_USER' : 'CURRENT_USER',
    'DAY': 'DAY',
    'DATABASE' : 'DATABASE',
    'DATABASES' : 'DATABASES',
    'DATE': 'DATE',
    'DECIMAL': 'DECIMAL',
    'DEGREES': 'DEGREES',
    'DECODE': 'DECODE',
    'DECLARE': 'DECLARE',
    'DEFAULT' : 'DEFAULT',
    'DELETE': 'DELETE',
    'DESC': 'DESC',
    'DISTINCT': 'DISTINCT',
    'DIV': 'DIV',
    'DOUBLE': 'DOUBLE',
    'DROP' : 'DROP',
    'ENUM' : 'ENUM',  
    'EXISTS': 'EXISTS',
    'EXCEPT': 'EXCEPT',
    'EXP': 'EXP',
    'EXTRACT': 'EXTRACT',
    'FACTORIAL': 'FACTORIAL',
    'FALSE': 'FALSE',
    'FOREIGN' : 'FOREIGN',
    'FROM': 'FROM',
    'FLOOR': 'FLOOR',
    'FULL': 'FULL',
    'GROUP': 'GROUP',
    'GCD': 'GCD',
    'HAVING': 'HAVING',
    'HOUR': 'HOUR',
    'IF' : 'IF',
    'ILIKE': 'ILIKE',
    'IN': 'IN',
    'INHERITS' : 'INHERITS', 
    'INSERT': 'INSERT',
    'INTEGER': 'INTEGER',
    'INTERVAL': 'INTERVAL',
    'INTO': 'INTO',
    'INNER': 'INNER',
    'INTERSECT': 'INTERSECT',
    'IS': 'IS',
    'ISNULL': 'ISNULL',
    'JOIN': 'JOIN',
    'KEY' : 'KEY', 
    'LEFT': 'LEFT',
    'LENGTH': 'LENGTH',
    'LIKE': 'LIKE',
    'LIMIT': 'LIMIT',
    'LN': 'LN',
    'LOG': 'LOG',
    'MAX': 'MAX',
    'MIN': "MIN",
    'MOD': 'MOD',
    'MINUTE': 'MINUTE',
    'MODE' : 'MODE', 
    'MONEY': 'MONEY',
    'MONTH': 'MONTH',
    'MD5': 'MD5',
    'NOT': 'NOT',
    'NOTNULL': 'NOTNULL',
    'NULL': 'NULL',
    'NUMERIC': 'NUMERIC',
    'ON': 'ON',
    'OUTER': 'OUTER',
    'OR': 'OR',
    'ORDER': 'ORDER',
    'OWNER' : 'OWNER',  
    'OFFSET': 'OFFSET',
    'PRECISION': 'PRECISION',
    'PRIMARY' : 'PRIMARY',
    'PI': 'PI',
    'POWER': 'POWER',
    'RANDOM': 'RANDOM',
    'RADIANS': 'RADIANS',
    'REAL': 'REAL',
    'REFERENCES' : 'REFERENCES', 
    'RENAME' : 'RENAME',
    'REPLACE' : 'REPLACE',
    'RETURNING': 'RETURNING',
    'RIGHT': 'RIGHT',
    'ROUND': 'ROUND',
    'SELECT': 'SELECT',
    'SECOND': 'SECOND',
    'SESSION_USER' : 'SESSION_USER',
    'SHOW' : 'SHOW',   
    'SHA256': 'SHA256',
    'SMALLINT': 'SMALLINT',
    'SET': 'SET',
    'SIMILAR': 'SIMILAR',
    'SIGN': 'SIGN',
    'SUM': 'SUM',
    'SUBSTRING': 'SUBSTRING',
    'SUBSTR': 'SUBSTR',
    'SQRT': 'SQRT',
    'SYMMETRIC' : 'SYMMETRIC',
    'TABLE' : 'TABLE',
    'TEXT': 'TEXT',
    'TIME': 'TIME',
    'TIMESTAMP': 'TIMESTAMP',
    'TO' : 'TO', 
    'TYPE': 'TYPE',
    'TRIM': 'TRIM',
    'TRUNC': 'TRUNC',
    'TRUE': 'TRUE',
    'UPDATE': 'UPDATE',
    'USING': 'USING',
    'UNION': 'UNION',
    'UNKNOWN': 'UNKNOWN',
    'UNIQUE': 'UNIQUE',
    'VALUES': 'VALUES',
    'VARCHAR': 'VARCHAR',
    'VARYING': 'VARYING',
    'WHERE': 'WHERE',
    'WIDTH_BUCKET': 'WIDTH_BUCKET',
    'YEAR': 'YEAR',
    
    #Trigonometricas
    'ACOS': 'ACOS',
    'ACOSD': 'ACOSD',
    'ASIN': 'ASIN',
    'ASIND': 'ASIND',
    'ATAN': 'ATAN',
    'ATAND': 'ATAND',
    'ATAN2': 'ATAN2',
    'ATAN2D': 'ATAN2D',
    'COS': 'COS',
    'COSD': 'COSD',
    'COT': 'COT',
    'COTD': 'COTD',
    'SIN': 'SIN',
    'SIND': 'SIND',
    'TAN': 'TAN',
    'TAND': 'TAND',
    'COSH': 'COSH',
    'SINH': 'SINH',
    'TANH': 'TANH',
    'ACOSH': 'ACOSH',
    'ASINH': 'ASINH',
    'ATANH': 'ATANH'
}


# Definitios of tokens not reserved
tokens = [
    'ID',

    # Symbols
    'COMMA',
    'DOT',
    'ASTERISK',
    'LEFT_PARENTHESIS',
    'RIGHT_PARENTHESIS',
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'SEMICOLON',
    'COLON',
    'TYPE_CAST',
    
    'SQUARE_ROOT',
    'CUBE_ROOT',
    'BITWISE_AND',
    'BITWISE_OR',
    'BITWISE_XOR',
    'BITWISE_NOT',
    'BITWISE_SHIFT_LEFT',
    'BITWISE_SHIFT_RIGHT',

    # Logical Operators
    'LESS_THAN',
    'LESS_EQUAL',
    'GREATE_THAN',
    'GREATE_EQUAL',
    'NOT_EQUAL',
    'NOT_EQUAL_LR',

    # Basic Operators
    'PLUS',
    'REST',
    'PRODUCT',
    'DIVISION',
    'EXPONENT',
    'MODULAR',
    # Assignment Operators
    'EQUALS',

    # Types of Contents
    'INT_NUMBER',
    'FLOAT_NUMBER',
    'STRINGCONT',
    'CHARCONT',

    # COMMENTS
    'SINGLE_LINE_COMMENT',
    'MULTI_LINE_COMMENT'
]

tokens += list(k_reserved.values())

# Definition of patrons for tokens
digit = r'[0-9]+'
letter = r'([_A-Za-z])'
identifier = r'(' + letter + r'(' + digit + r'|' + letter + r')*)'
decimal = r'\d+\.\d+'
char = r'\'[^"\'"]*\''
string = r'\"[^"\""]*\"'
single_line = r'\-\-.*\n'
multi_line = r'/\*(.|\n)*?\*/'

# Definition of Symbols
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_DOT = r'\.'
t_ASTERISK = r'\*'
t_LEFT_PARENTHESIS = r'\('
t_RIGHT_PARENTHESIS = r'\)'
t_LESS_THAN = r'\<'
t_LESS_EQUAL = r'\<\='
t_GREATE_THAN = r'\>'
t_GREATE_EQUAL = r'\>\='
t_NOT_EQUAL = r'\!\='
t_NOT_EQUAL_LR = r'\<\>'
t_EQUALS = r'\='
t_COLON = r'\:'
t_PLUS = r'\+'
t_REST = r'\-'
t_DIVISION = r'\/'
t_EXPONENT = r'\^'
t_TYPE_CAST = r'\:\:'
t_LEFT_BRACE = r'\['
t_RIGHT_BRACE = r'\]'
t_MODULAR = r'\%'
t_SQUARE_ROOT = r'\|\/'
t_CUBE_ROOT = r'\|\|\/'
t_BITWISE_AND = r'\&'
t_BITWISE_OR = r'\|'
t_BITWISE_XOR = r'\#'
t_BITWISE_NOT = r'\~'
t_BITWISE_SHIFT_LEFT = r'\<\<'
t_BITWISE_SHIFT_RIGHT = r'\>\>'

# Token recognition using patterns


input = ""
@TOKEN(decimal)
def t_FLOAT_NUMBER(t):
    # r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print(f'Error: %d {t.value}')
        t.value = 0
    return t


@TOKEN(digit)
def t_INT_NUMBER(t):
    try:
        t.value = int(t.value)
    except ValueError:
        print(f'Error: {t.value}')
        t.value = 0
    return t


@TOKEN(identifier)
def t_ID(t):
    t.type = k_reserved.get(t.value.upper(), 'ID')
    return t


@TOKEN(string)
def t_STRINGCONT(t):
    t.value = t.value[1:-1]
    t.lexer.lineno += t.value.count("\n")
    return t


@TOKEN(char)
def t_CHARCONT(t):
    t.value = t.value[1:-1]
    t.lexer.lineno += t.value.count("\n")
    return t


@TOKEN(single_line)
def t_SINGLE_LINE_COMMENT(t):
    t.lexer.lineno += t.value.count('\n')
    return t


@TOKEN(multi_line)
def t_MULTI_LINE_COMMENT(t):
    t.lexer.lineno += t.value.count('\n')
    return t


# New line recognition
def t_new_line(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Skip white spaces


def t_white_space(t):
    r'\s+'
    t.lexer.lineno += t.value.count('\n')

# Recognition of errors


def t_error(t):
    global list_errors
    global input
    global id_error
    
    id_error = list_errors.count + 1  if list_errors.count > 0 else 1
    SQLERROR = FindTypeError('Lexical')
    number_error, description = SQLERROR.find_type_error()
    
    description += ' or near ' + str(t.value[0])
    column = find_column(t)
    
    print(f"The character {t.value[0]} ilegal, {t.lexer.lineno}  {find_column(t)}")
    
    list_errors.insert_end(Error(id_error, 'Lexical',number_error, description, t.lexer.lineno, column))
    id_error += 1
    
    t.lexer.skip(1)

# Find column


def find_column(token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def get_text(entra):
    global input
    global id_error
    id_error = 1
    input = entra
    return input


