import parserT28.libs.ply.lex as lex
from parserT28.libs.ply.lex import TOKEN

from parserT28.controllers.error_controller import ErrorController

# Hacen falta palabras reservadas hay que anadirlas
# Definitions of tokens reserved
k_reserved = {
    'ADD': 'ADD',
    'ALIAS': 'ALIAS',
    'ALL': 'ALL',
    'ALTER': 'ALTER',
    'ABS': 'ABS',
    'AND': 'AND',
    'AS': 'AS',
    'ASC': 'ASC',
    'AVG': 'AVG',
    'BEGIN': 'BEGIN',
    'BETWEEN': 'BETWEEN',
    'BTREE': 'BTREE',
    'BIGINT': 'BIGINT',
    'BOOLEAN': 'BOOLEAN',
    'BY': 'BY',
    'CASE': 'CASE',
    'CBRT': 'CBRT',
    'CONVERT': 'CONVERT',
    'CONCURRENTLY': 'CONCURRENTLY',
    'CASCADE': 'CASCADE',
    'CEIL': 'CEIL',
    'CEILING': 'CEILING',
    'CHAR': 'CHAR',
    'CHARACTER': 'CHARACTER',
    'CHECK': 'CHECK',
    'CREATE': 'CREATE',
    'COLUMN': 'COLUMN',
    'COLLATE': 'COLLATE',
    'CONCAT': 'CONCAT',
    'CONSTANT': 'CONSTANT',
    'CONSTRAINT': 'CONSTRAINT',
    'COUNT': 'COUNT',
    'CURRENT_DATE': 'CURRENT_DATE',
    'CURRENT_TIME': 'CURRENT_TIME',
    'CURRENT_USER': 'CURRENT_USER',
    'DAY': 'DAY',
    'DATABASE': 'DATABASE',
    'DATABASES': 'DATABASES',
    'DATE': 'DATE',
    'DATE_PART': 'DATE_PART',
    'DECIMAL': 'DECIMAL',
    'DEGREES': 'DEGREES',
    'DECODE': 'DECODE',
    'DECLARE': 'DECLARE',
    'DEFAULT': 'DEFAULT',
    'DELETE': 'DELETE',
    'DESC': 'DESC',
    'DISTINCT': 'DISTINCT',
    'DIV': 'DIV',
    'DOUBLE': 'DOUBLE',
    'DROP': 'DROP',
    'ENUM': 'ENUM',
    'EXISTS': 'EXISTS',
    'EXCEPT': 'EXCEPT',
    'EXECUTE': 'EXECUTE',
    'EXP': 'EXP',
    'ELSE': 'ELSE',
    'ELSEIF': 'ELSEIF',
    'ELSIF': 'ELSIF',
    'END': 'END',
    'EXCEPTION': 'EXCEPTION',
    'EXTRACT': 'EXTRACT',
    'FACTORIAL': 'FACTORIAL',
    'FALSE': 'FALSE',
    'FIRST': 'FIRST',
    'FOR': 'FOR',
    'FOREIGN': 'FOREIGN',
    'FROM': 'FROM',
    'FLOOR': 'FLOOR',
    'FULL': 'FULL',
    'FUNCTION': 'FUNCTION',
    'GROUP': 'GROUP',
    'GREATEST': 'GREATEST',
    'GCD': 'GCD',
    'HAVING': 'HAVING',
    'HASH': 'HASH',
    'HOUR': 'HOUR',
    'IF': 'IF',
    'ILIKE': 'ILIKE',
    'IN': 'IN',
    'INDEX': 'INDEX',
    'INHERITS': 'INHERITS',
    'INSERT': 'INSERT',
    'INTEGER': 'INTEGER',
    'INTERVAL': 'INTERVAL',
    'INTO': 'INTO',
    'INNER': 'INNER',
    'INTERSECT': 'INTERSECT',
    'IS': 'IS',
    'ISNULL': 'ISNULL',
    'JOIN': 'JOIN',
    'KEY': 'KEY',
    'LANGUAGE': 'LANGUAGE',
    'LEFT': 'LEFT',
    'LEAST': 'LEAST',
    'LENGTH': 'LENGTH',
    'LIKE': 'LIKE',
    'LAST': 'LAST',
    'LIMIT': 'LIMIT',
    'LOWER': 'LOWER',
    'LN': 'LN',
    'LOG': 'LOG',
    'MAX': 'MAX',
    'MIN': "MIN",
    'MOD': 'MOD',
    'MINUTE': 'MINUTE',
    'MODE': 'MODE',
    'MONEY': 'MONEY',
    'MONTH': 'MONTH',
    'MD5': 'MD5',
    'NOT': 'NOT',
    'NOTICE': 'NOTICE',
    'NOTNULL': 'NOTNULL',
    'NOW': 'NOW',
    'NULL': 'NULL',
    'NUMERIC': 'NUMERIC',
    'NULLS': 'NULLS',
    'ON': 'ON',
    'OUT': 'OUT',
    'OUTER': 'OUTER',
    'OR': 'OR',
    'ORDER': 'ORDER',
    'OWNER': 'OWNER',
    'OFFSET': 'OFFSET',
    'PRECISION': 'PRECISION',
    'PRIMARY': 'PRIMARY',
    'PI': 'PI',
    'PLPGSQL': 'PLPGSQL',
    'POWER': 'POWER',
    'PROCEDURE': 'PROCEDURE',
    'RAISE': 'RAISE',
    'RANDOM': 'RANDOM',
    'RADIANS': 'RADIANS',
    'REAL': 'REAL',
    'RECORD': 'RECORD',
    'REFERENCES': 'REFERENCES',
    'RENAME': 'RENAME',
    'REPLACE': 'REPLACE',
    'RETURN': 'RETURN',
    'RETURNS': 'RETURNS',
    'RETURNING': 'RETURNING',
    'RIGHT': 'RIGHT',
    'ROUND': 'ROUND',
    'RESTRICT': 'RESTRICT',
    'ROWTYPE': 'ROWTYPE',
    'SELECT': 'SELECT',
    'SECOND': 'SECOND',
    'SESSION_USER': 'SESSION_USER',
    'SHOW': 'SHOW',
    'SHA256': 'SHA256',
    'SMALLINT': 'SMALLINT',
    'SET': 'SET',
    'SIMILAR': 'SIMILAR',
    'SIGN': 'SIGN',
    'SUM': 'SUM',
    'SUBSTRING': 'SUBSTRING',
    'SUBSTR': 'SUBSTR',
    'SQRT': 'SQRT',
    'SYMMETRIC': 'SYMMETRIC',
    'TABLE': 'TABLE',
    'TEXT': 'TEXT',
    'TIME': 'TIME',
    'TIMESTAMP': 'TIMESTAMP',
    'THEN': 'THEN',
    'TO': 'TO',
    'TYPE': 'TYPE',
    'TRIM': 'TRIM',
    'TRUNC': 'TRUNC',
    'TRUE': 'TRUE',
    'UPDATE': 'UPDATE',
    'USE': 'USE',
    'USING': 'USING',
    'UNION': 'UNION',
    'UNKNOWN': 'UNKNOWN',
    'UNIQUE': 'UNIQUE',
    'VALUES': 'VALUES',
    'VARCHAR': 'VARCHAR',
    'VARIADIC': 'VARIADIC',
    'VARYING': 'VARYING',
    'VOID': 'VOID',
    'WHERE': 'WHERE',
    'WHEN': 'WHEN',
    'WIDTH_BUCKET': 'WIDTH_BUCKET',
    'YEAR': 'YEAR',


    # Trigonometricas
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
    'SEMICOLON',
    'COLON',
    'DOUBLE_DOLLAR',
    'DOLLAR',

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
    'DIVISION',
    'EXPONENT',
    'MODULAR',
    # Assignment Operators
    'EQUALS',
    'COLONEQUALS',

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
t_DOUBLE_DOLLAR = r'\$\$'
t_DOLLAR = r'\$'
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
t_COLONEQUALS = r'\:\='
t_EQUALS = r'\='
t_COLON = r'\:'
t_PLUS = r'\+'
t_REST = r'\-'
t_DIVISION = r'\/'
t_EXPONENT = r'\^'
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


@TOKEN(multi_line)
def t_MULTI_LINE_COMMENT(t):
    t.lexer.lineno += t.value.count('\n')


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
    global input

    description = ' or near ' + str(t.value[0])
    column = find_column(t)
    ErrorController().add(33, 'Lexical', description, t.lexer.lineno, column)

    print(
        f"The character {t.value[0]} ilegal, {t.lexer.lineno} {find_column(t)}")

    t.lexer.skip(1)

# Find column


def find_column(token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


def get_text(entra):
    global input
    input = entra
    return input
