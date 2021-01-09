from Parser.Reportes.Nodo1 import Nodo
from Interprete.Manejo_errores.ErroresSintacticos import ErroresSintacticos
from Interprete.Manejo_errores.ErroresLexicos import ErroresLexicos
from Main.erroresglobales import erroresglobales

reservadas = {

    # LOWER

    'lower': 'LOWER',
    'owned': 'OWNED',
    'reset': 'RESET',
    'nowait': 'NOWAIT',
    'statistics': 'STATISTICS',
    'extension': 'EXTENSION',
    'depends': 'DEPENDS',
    'partition': 'PARTITION',
    'attach': 'ATTACH',
    'tablespace': 'TABLESPACE',
    'cascade': 'CASCADE',
    'restrict': 'RESTRICT',
    'concurrently': 'CONCURRENTLY',
    # INDEXES
    'index': 'INDEX',
    'hash': 'HASH',

    'raise': 'RAISE',
    'notice': 'NOTICE',
    'returning': 'RETURNING',
    'strict': 'STRICT',
    'perfom': 'PERFORM',

    # Boolean Type
    'boolean': 'BOOLEAN',
    'true': 'TRUE',
    'false': 'FALSE',
    'order': 'ORDER',

    'into': 'INTO',

    # operator Precedence
    'isnull': 'ISNULL',
    'notnull': 'NOTNULL',

    # Definition
    'replace': 'REPLACE',
    'owner': 'OWNER',
    'show': 'SHOW',
    'databases': 'DATABASES',
    'map': 'MAP',
    'list': 'LIST',
    'mode': 'MODE',
    'use': 'USE',

    # Inheritance
    'inherits': 'INHERITS',

    # ESTRUCTURAS DE CONSULTA Y DEFINICIONES
    'select': 'SELECT',
    'insert': 'INSERT',
    'update': 'UPDATE',
    'drop': 'DROP',
    'delete': 'DELETE',
    'alter': 'ALTER',
    'constraint': 'CONSTRAINT',
    'from': 'FROM',
    'group': 'GROUP',
    'by': 'BY',
    'where': 'WHERE',
    'having': 'HAVING',
    'create': 'CREATE',
    'type': 'TYPE',
    'primary': 'PRIMARY',
    'foreign': 'FOREIGN',
    'add': 'ADD',
    'rename': 'RENAME',
    'set': 'SET',
    'key': 'KEY',
    'if': 'IF',
    'elsif': 'ELSIF',
    'else': 'ELSE',
    'unique': 'UNIQUE',
    'references': 'REFERENCES',
    'check': 'CHECK',
    'column': 'COLUMN',
    'database': 'DATABASE',
    'table': 'TABLE',
    'text': 'TEXT',
    'float': 'FLOAT',
    'values': 'VALUES',
    'int': 'INT',
    'default': 'DEFAULT',
    'null': 'NULL',
    'now': 'NOW',
    'bytea': 'BYTEA',
    'begin': 'BEGIN',
    'exception': 'EXCEPTION',

    # TIPOS NUMERICOS
    'smallint': 'SMALLINT',
    'integer': 'INTEGER',
    'bigint': 'BIGINT',
    'decimal': 'DECIMAL',
    'numeric': 'NUMERIC',
    'real': 'REAL',
    'double': 'DOUBLE',
    'precision': 'PRECISION',
    'money': 'MONEY',
    'varying': 'VARYING',
    'varchar': 'VARCHAR',
    'character': 'CHARACTER',
    'char': 'CHAR',
    'clear': 'CLEAR',
    'string': 'STRING',

    # TIPOS EN FECHAS
    'timestamp': 'TIMESTAMP',
    'date': 'DATE',
    'time': 'TIME',
    'interval': 'INTERVAL',
    'year': 'YEAR',
    'day': 'DAY',
    'hour': 'HOUR',
    'minute': 'MINUTE',
    'second': 'SECOND',
    'to': 'TO',
    'current_date': 'CURRENT_DATE',
    'current_time': 'CURRENT_TIME',
    'current_user': 'CURRENT_USER',
    'session_user': 'SESSION_USER',
    'date_part': 'DATE_PART',
    'month': 'MONTH',
    'exit': 'EXIT',

    # ENUM
    'enum': 'ENUM',

    # OPERADORES LOGICOS
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'return': 'RETURN',

    # PREDICADOS DE STRICT
    'between': 'BETWEEN',
    'unknown': 'UNKNOWN',
    'is': 'IS',
    'distinct': 'DISTINCT',

    # FUNCIONES MATEMATICAS
    'abs': 'ABS',
    'cbrt': 'CBRT',
    'ceil': 'CEIL',
    'ceiling': 'CEILING',
    'degrees': 'DEGREES',
    'extract': 'EXTRACT',
    'div': 'DIV',
    'exp': 'EXP',
    'trunc': 'TRUNC',
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
    'width_bucker': 'WIDTH_BUCKET',
    'random': 'RANDOM',
    'setseed': 'SETSEED',
    'contains': 'CONTAINS',
    'remove': 'REMOVE',
    'function': 'FUNCTION',
    'procedure': 'PROCEDURE',

    # FUNCIONES DE AGREGACION
    'count': 'COUNT',
    'sum': 'SUM',
    'avg': 'AVG',
    'max': 'MAX',
    'min': 'MIN',

    # FUNCIONES TRIGONOMETRICAS
    'acos': 'ACOS',
    'acosd': 'ACOSD',
    'asin': 'ASIN',
    'asind': 'ASIND',
    'constant': 'CONSTANT',
    'atan': 'ATAN',
    'atand': 'ATAND',
    'atan2': 'ATAN2',
    'atan2d': 'ATAN2D',
    'cos': 'COS',
    'cosd': 'COSD',
    'cot': 'COT',
    'cotd': 'COTD',
    'sin': 'SIN',
    'sind': 'SIND',
    'tan': 'TAN',
    'tand': 'TAND',
    'sinh': 'SINH',
    'cosh': 'COSH',
    'tanh': 'TANH',
    'asinh': 'ASINH',
    'acosh   ': 'ACOSH',
    'atanh': 'ATANH',
    'SIZE': 'SIZE',
    'next': 'NEXT',
    'query': 'QUERY',
    'execute': 'EXECUTE',
    'using': 'USING',
    'call': 'CALL',

    # FUNCIONES DE CADENA BINARIAS
    'length': 'LENGTH',
    'substring': 'SUBSTRING',
    'trim': 'TRIM',
    'get_byte': 'GET_BYTE',
    'md5': 'MD5',
    'set_byte': 'SET_BYTE',
    'sha256': 'SHA256',
    'substr': 'SUBSTR',
    'convert': 'CONVERT',
    'encode': 'ENCODE',
    'decode': 'DECODE',

    # COINCidenCIA POR PATRON
    'like': 'LIKE',
    'ilike': 'ILIKE',
    'similar': 'SIMILAR',
    'as': 'AS',
    'couter': 'COUTER',
    'collate': 'COLLATE',

    # SUBQUERYS
    'in': 'IN',
    'exists': 'EXISTS',
    'any': 'ANY',
    'all': 'ALL',
    'some': 'SOME',

    # JOINS
    'join': 'JOIN',
    'inner': 'INNER',
    'left': 'LEFT',
    'right': 'RIGHT',
    'full': 'FULL',
    'outer': 'OUTER',
    'on': 'ON',
    'declare': 'DECLARE',

    # ORDENAMIENTO DE FILAS
    'asc': 'ASC',
    'desc': 'DESC',
    'nulls': 'NULLS',
    'first': 'FIRST',
    'last': 'LAST',

    # EXPRESIONES
    'case': 'CASE',
    'when': 'WHEN',
    'then': 'THEN',
    'end': 'END',
    'greatest': 'GREATEST',
    'least': 'LEAST',

    # LIMITE Y OFFSET
    'limit': 'LIMIT',
    'offset': 'OFFSET',

    # CONSULTAS DE COMBINACION
    'union': 'UNION',
    'intersect': 'INTERSECT',
    'except': 'EXCEPT',
    'language': 'LANGUAGE',
    'returns': 'RETURNS',

}

tokens = [
             'PT',
             'DOBPTS',
             'MAS',
             'MENOS',
             'MULTI',
             'DIVISION',
             'MODULO',
             'IGUAL',
             'PARIZQ',
             'PARDER',
             'PTCOMA',
             'COMA',
             'TKNOT',
             'NOTBB',
             'ANDBB',
             'ORBB',
             'ORBBDOBLE',
             'NUMERAL',
             'TKEXP',
             'SHIFTIZQ',
             'SHIFTDER',
             'IGUALQUE',
             'DISTINTO',
             'MAYORIG',
             'MENORIG',
             'MAYORQUE',
             'MENORQUE',
             'CORIZQ',
             'CORDER',
             'DOSPTS',
             'TKDECIMAL',
             'ENTERO',
             'CADENA',
             'CADENADOBLE',
             'ID',
             'DOLAR'
         ] + list(reservadas.values())

# Tokens
t_PT = r'\.'
t_DOBPTS = r'::'
t_CORIZQ = r'\['
t_CORDER = r']'
t_DOLAR = r'\$'
t_MAS = r'\+'
t_MENOS = r'-'
t_TKEXP = r'\^'
t_MULTI = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'
t_IGUAL = r'='
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_PTCOMA = r';'
t_COMA = r','
t_TKNOT = r'!'
t_NOTBB = r'~'
t_ANDBB = r'&'
t_ORBB = r'\|'
t_ORBBDOBLE = r'\|\|'
t_NUMERAL = r'\#'

t_SHIFTIZQ = r'<<'
t_SHIFTDER = r'>>'
t_IGUALQUE = r'=='
t_DISTINTO = r'!='
t_MAYORIG = r'>='
t_MENORIG = r'<='
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_DOSPTS = r':'


def t_TKDECIMAL(t):
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


def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
    return t


def t_CADENADOBLE(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t


t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)  # t.value.count("\n")


def t_COMENTARIO_SIMPLE(t):
    r'\--.*\n'
    t.lexer.lineno += 1


def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


def t_error(t):
    print("Caracter NO Valido: '%s'" % t.value[0])
    t.lexer.skip(1)
    print(t.value[0])
    descripncion = "Caracter ilegal " + str(t.value[0])
    error_l: ErroresLexicos = ErroresLexicos(descripncion, int(t.lexer.lineno), int(t.lexer.lineno), 'Lexico')
    erroresglobales.errores_lexicos.append(error_l)


# -----------------------------------------------------------------------------------
# ---------------------- SINTACTICO -------------------------------------------------
# -----------------------------------------------------------------------------------


# -----------------------
import ply.lex as lex

lexerreporte = lex.lex()
# -----------------------
precedence = (
    # ('left','CONCAT'),
    # ('left','MENOR','MAYOR','IGUAL','MENORIGUAL','MAYORIGUAL','DIFERENTE'),
    ('left', 'IGUAL', 'DISTINTO'),
    ('left', 'MENORQUE', 'MAYORQUE', 'MENORIG', 'MAYORIG'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTI', 'DIVISION', 'MODULO'),
    ('left', 'TKEXP'),
    # ('right','UMENOS'),
)


def p_init(t):
    'init : inter'
    t[0] = Nodo("init")
    addSimple(t, 0, 1)

def p_inter(t):
    'inter : definitions'
    t[0] = Nodo("inter")
    addSimple(t, 0, 1)


def p_definitions(t):
    '''
        definitions   : definitions definition
                      | definition
    '''
    if len(t) == 3:
        t[1].add(t[2])
        t[0] = t[1]
    else:
        t[0] = Nodo("definitions")
        t[0].add(t[1])


def p_definition(t):
    '''
        definition   : instruction PTCOMA
    '''
    t[0] = Nodo("definition")
    addSimple(t, 0, 1)
    add(t, 0, node(t, 2, 2))


def p_instruction(t):
    '''
        instruction     : DataManipulationLenguage
                        |  plpgsql
                        |  statements
                        |  index
    '''
    t[0] = Nodo("instruccion")
    addSimple(t, 0, 1)


# --------------------------------------------------------------------------------------
# ------------------------------- PL/PGSQL ---------------------------------------------
# --------------------------------------------------------------------------------------

def p_cierreplpgsql(t):
    '''
        statements : DOLAR DOLAR LANGUAGE ID
    '''
    t[0] = Nodo("statements")
    add(t, 0, node(t,1, 4))

def p_plpgsql(t):
    '''
        plpgsql : function_or_procedure definitions BEGIN definitions plpgsql_ending
                | function_or_procedure label definitions BEGIN definitions plpgsql_ending
                | function_or_procedure BEGIN definitions plpgsql_ending
    '''
    t[0] = Nodo("plpgsql")
    if len(t) == 6:
        #function_or_procedure definitions BEGIN definitions plpgsql_ending
        addList(t, 0, 1,2)
        add(t, 0, node(t, 3))
        addList(t, 0, 4, 5)

    elif len(t) == 7:
        #function_or_procedure label definitions BEGIN definitions plpgsql_ending
        addList(t, 0, 1,3)
        add(t, 0, node(t, 4))
        addList(t, 0, 5,6)

    elif len(t) == 5:
        #function_or_procedure BEGIN definitions plpgsql_ending
        addList(t, 0, 1)
        add(t, 0, node(t, 2))
        addList(t, 0,3,4)


# -------------------------------Pablo PL/PGSQL ---------------------------------------------

def p_functions_or_procedures(t):
    '''
        functions_or_procedures : functions_or_procedures function_or_procedure
                                | function_or_procedure
    '''
    if len(t) == 3:
        t[1].add(t[2])
        t[0] = t[1]
    else:
        t[0] = Nodo("functions_or_procedures")
        t[0].add(t[1])


def p_function_or_procedure(t):
    '''
        function_or_procedure : function
                              | procedure
    '''
    t[0] = Nodo("function_or_procedure")
    addList(t, 0, 1)


def p_procedure(t):
    '''
        procedure : CREATE PROCEDURE ID PARIZQ arguments PARDER LANGUAGE ID AS DOLAR DOLAR
                  | CREATE OR REPLACE PROCEDURE ID PARIZQ arguments PARDER LANGUAGE ID AS DOLAR DOLAR
                  | CREATE PROCEDURE ID PARIZQ PARDER LANGUAGE ID AS DOLAR DOLAR
                  | CREATE OR REPLACE PROCEDURE ID PARIZQ PARDER LANGUAGE ID AS DOLAR DOLAR
    '''
    t[0] = Nodo("procedure")
    if len(t) == 12:
        #CREATE PROCEDURE ID PARIZQ arguments PARDER LANGUAGE ID AS DOLAR DOLAR
        add(t, 0, node(t, 1, 3))
        addList(t, 0, 5)
        add(t, 0, node(t, 7, 8))
    elif len(t) == 14:
        # CREATE OR REPLACE PROCEDURE ID PARIZQ arguments PARDER LANGUAGE ID AS DOLAR DOLAR
        add(t, 0, node(t, 1, 5))
        addList(t, 0, 7)
        add(t, 0, node(t, 9, 10))
    elif len(t) == 11:
        # CREATE PROCEDURE ID PARIZQ PARDER LANGUAGE ID AS DOLAR DOLAR
        add(t, 0, node(t, 1, 3))
        add(t, 0, node(t, 6, 7))
    elif len(t) == 13:
        # CREATE OR REPLACE PROCEDURE ID PARIZQ PARDER LANGUAGE ID AS DOLAR DOLAR
        add(t, 0, node(t, 1, 5))
        add(t, 0, node(t, 8, 9))


# ================= EXCEPTION =================


def p_plpgsql_ending(t):
    '''
        plpgsql_ending : exception END
                       | END
    '''
    t[0] = Nodo("plpgsql_ending")
    if len(t) == 3:
        addList(t, 0, 1)
        add(t, 0, node(t, 2))
    else:
        add(t, 0, node(t, 1))


def p_exception(t):
    '''
        exception : EXCEPTION exception_whens
    '''
    t[0] = Nodo("exception")
    add(t, 0, node(t, 1))
    addList(t, 0, 2)


def p_end(t):
    '''
        end : END ID
            | END
    '''
    t[0] = Nodo("end")

    if len(t) == 3:
        add(t, 0, node(t, 1, 2))
    else:
        add(t, 0, node(t, 1))


def p_exception_whens(t):
    '''
        exception_whens : exception_whens exception_when
                        | exception_when
    '''
    if len(t) == 3:
        t[1].add(t[2])
        t[0] = t[1]
    else:
        t[0] = Nodo("exception_whens")
        t[0].add(t[1])


def p_exception_when(t):
    '''
        exception_when : WHEN exp THEN stmts
    '''
    t[0] = Nodo("exception_when")
    add(t, 0, node(t, 1))
    addList(t, 0, 2)
    add(t, 0, node(t, 3))
    addList(t, 0, 4)


# ================= FUNCTION =================


def p_function(t):
    '''
        function : CREATE FUNCTION ID PARIZQ arguments function_ending
                 | CREATE OR REPLACE FUNCTION ID PARIZQ arguments function_ending
                 | CREATE FUNCTION ID PARIZQ function_ending
                 | CREATE OR REPLACE FUNCTION ID PARIZQ function_ending
    '''
    t[0] = Nodo("function")
    if len(t) == 7:
        # CREATE FUNCTION ID PARIZQ arguments function_ending
        add(t, 0, node(t, 1, 3))
        addList(t, 0, 5, 6)
    elif len(t) == 9:
        # CREATE OR REPLACE FUNCTION ID PARIZQ arguments function_ending
        add(t, 0, node(t, 1, 5))
        addList(t, 0, 7, 8)
    elif len(t) == 6:
        # CREATE FUNCTION ID PARIZQ function_ending
        add(t, 0, node(t, 1, 3))
        addList(t, 0, 7, 5)

    elif len(t) == 8:
        # CREATE OR REPLACE FUNCTION ID PARIZQ function_ending
        add(t, 0, node(t, 1, 5))
        addList(t, 0, 7)


def p_function_ending(t):
    '''
        function_ending : PARDER RETURNS types
                        | PARDER RETURNS types AS DOLAR DOLAR
                        | PARDER
    '''
    t[0] = Nodo("function_ending")
    if len(t) == 4:
        add(t, 0, node(t, 1, 2))
        addList(t, 0, 3)

    elif len(t) == 7:
        add(t, 0, node(t, 1, 2))
        addList(t, 0, 3)
        add(t, 0, node(t, 4, 6))

    elif len(t) == 2:
        add(t, 0, node(t, 1))


def p_arguments(t):
    '''
        arguments : arguments COMA argument
                  | argument
    '''
    if len(t) == 4:
        t[1].add(t[3])
        t[0] = t[1]
    else:
        t[0] = Nodo("arguments")
        t[0].add(t[1])


def p_argument(t):
    '''
      argument : ID types
    '''
    t[0] = Nodo("argument")
    add(t, 0, node(t, 1))
    addList(t, 0, 2)


def p_label(t):
    '''
        label : SHIFTIZQ ID SHIFTDER
    '''
    t[0] = Nodo("label")
    add(t, 0, node(t, 1, 3))


def p_stmts(t):
    '''
        stmts : stmts stmt
              | stmt
    '''
    if len(t) == 3:
        t[1].add(t[2])
        t[0] = t[1]
    else:
        t[0] = Nodo("stmts")
        t[0].add(t[1])


def p_stmt(t):
    '''
        stmt : DataManipulationLenguage PTCOMA
             | statements PTCOMA
    '''
    t[0] = Nodo("stmt")
    addList(t, 0, 1)
    add(t, 0, node(t, 2))


def p_statements_conditionals(t):
    '''
        statements : conditionals
                   | return
                   | execute_procedure
                   | PRAISE
                   | callfunction
                   | exit
                   | asignacionvar
                   | declarer
                   | drop_function
                   | drop_procedure
    '''
    t[0] = Nodo("statements")
    addList(t, 0, 1)


def p_exit(t):
    '''
        exit : EXIT
             | EXIT ID
             | EXIT WHEN exp
             | EXIT ID WHEN exp
    '''
    t[0] = Nodo("plpgsql")
    if len(t) == 2:  # EXIT
        add(t, 0, node(t, 1))

    elif len(t) == 3:  # EXIT ID
        add(t, 0, node(t, 1, 2))

    elif len(t) == 4:  # EXIT WHEN exp
        add(t, 0, node(t, 1, 2))
        addList(t, 0, 3)

    elif len(t) == 5:  # EXIT ID WHEN exp
        add(t, 0, node(t, 1, 3))
        addList(t, 0, 4)


def p_execute_procedure(t):
    '''
        execute_procedure : EXECUTE ID PARIZQ exp_list PARDER
                          | EXECUTE ID PARIZQ PARDER
    '''
    t[0] = Nodo("execute_procedure")
    if len(t) == 6:
        # EXECUTE ID PARIZQ exp_list PARDER
        add(t, 0, node(t, 1, 2))
        addList(t, 0,4)

    else:
        # EXECUTE ID PARIZQ PARDER
        add(t, 0, node(t, 1, 4))


# ================= RETURN =================

def p_statements_return(t):
    '''
        return : RETURN exp
               | RETURN NEXT exp
               | RETURN QUERY select
               | RETURN QUERY EXECUTE exp
               | RETURN QUERY EXECUTE exp USING exp_list
               | RETURN
    '''
    t[0] = Nodo("return")
    if len(t) == 3:
        # RETURN exp
        add(t, 0, node(t, 1))
        addList(t, 0, 2)

    elif len(t) == 4:
        # RETURN NEXT  exp | RETURN QUERY select
        add(t, 0, node(t, 1, 2))
        addList(t, 0, 3)

    elif len(t) == 5:
        # RETURN QUERY EXECUTE exp
        add(t, 0, node(t, 1, 3))
        addList(t, 0, 4)

    elif len(t) == 7:
        # RETURN QUERY EXECUTE exp USING exp_list
        add(t, 0, node(t, 1, 3))
        addList(t, 0, 4)
        add(t, 0, node(t, 5))
        addList(t, 0, 6)


def p_conditionals(t):
    '''
        conditionals : ifheader
                     | caseheader
    '''
    t[0] = Nodo("conditionals")
    addList(t, 0, 1)


# ================= IF =================

def p_ifheader(t):
    '''
        ifheader : IF if END IF
    '''
    t[0] = Nodo("ifheader")
    add(t, 0, node(t, 1))
    addList(t, 0, 2)
    add(t, 0, node(t, 3,4))


def p_if(t):
    '''
        if : exp THEN definitions
           | exp THEN definitions ELSE stmts
           | exp THEN definitions ELSIF if
    '''
    t[0] = Nodo("if")

    if len(t) == 4:
        addList(t, 0, 1)
        add(t, 0, node(t, 2))
        addList(t, 0, 3)
    elif len(t) == 6:
        addList(t, 0, 1)
        add(t, 0, node(t, 2))
        addList(t, 0, 3)
        add(t, 0, node(t, 4))
        addList(t, 0, 5)


# ================= CASE =================

def p_caseheader(t):
    '''
        caseheader : CASE exp case END CASE
                   | CASE case END CASE
    '''
    t[0] = Nodo("caseheader")
    if len(t) == 6:
        add(t, 0, node(t, 1))
        addList(t, 0, 2, 3)
        add(t, 0, node(t, 4, 5))
    else:
        add(t, 0, node(t, 1))
        addList(t, 0, 2)
        add(t, 0, node(t, 3, 4))


def p_case(t):
    '''
        case : WHEN exp THEN stmts ELSE stmts
             | WHEN exp THEN stmts case
             | WHEN exp THEN stmts
    '''
    t[0] = Nodo("plpgsql")
    add(t, 0, node(t, 1))
    addList(t, 0, 2)
    add(t, 0, node(t, 3))
    addList(t, 0, 4)

    if len(t) == 7:
        add(t, 0, node(t, 5))
        addList(t, 0, 6)

    elif len(t) == 6:
        add(t, 0, node(t, 5))


# ================= DROP FUNCTION Y PROCEDURE =================

def p_drop_function(t):
    '''
        drop_function : DROP FUNCTION ID
                      | DROP FUNCTION IF EXISTS ID
    '''
    t[0] = Nodo("drop_function")
    add(t, 0, node(t, 1, 3))


def p_drop_procedure(t):
    '''
        drop_procedure : DROP PROCEDURE IF EXISTS ID
                       | DROP PROCEDURE ID
    '''
    t[0] = Nodo("drop_procedure")
    add(t, 0, node(t, 1, 3))


# -------------------------------Pablo PL/PGSQL ---------------------------------------------

# ================= RAISE ================= its Nery bitch

def p_Raise_simple(t):
    '''
        PRAISE : RAISE NOTICE exp
    '''
    t[0] = Nodo("praise")
    add(t, 0, node(t, 1, 2))
    addList(t, 0, 3)


def p_Raise_complex(t):
    '''
        PRAISE : RAISE NOTICE exp COMA ID
    '''
    t[0] = Nodo("praise")
    add(t, 0, node(t, 1, 2))
    addList(t, 0, 3)
    add(t, 0, node(t, 5))


# ================= RAISE ================= its Nery bitch


# -------------------------------Cristopher PL/PGSQL ---------------------------------------------

def p_declarevarheader(t):
    '''
         declarer   : declarerdeep
                    | DECLARE declarerdeep
    '''
    if len(t) == 2:
        t[0] = Nodo("declarer")
        addList(t, 0, 1)

    else:
        t[0] = Nodo("declarer")
        add(t, 0, node(t, 1))
        addList(t, 0, 2)


def p_declarevar(t):
    '''
         declarerdeep : ID types NOTNULL DOSPTS IGUAL exp
                      | ID types NOTNULL IGUAL exp
                      | ID types DOSPTS  IGUAL exp
                      | ID types IGUAL exp
                      | ID types
    '''
    t[0] = Nodo("declarerdeep")
    if len(t) == 7:
        # ID types NOTNULL DOSPTS IGUAL exp
        add(t, 0, node(t, 1))
        addList(t, 0, 2)
        add(t, 0, node(t, 3, 5))
        addList(t, 0, 6)

    elif len(t) == 6:
        # ID types NOTNULL IGUAL exp
        # ID types DOSPTS IGUAL exp
        add(t, 0, node(t, 1))
        addList(t, 0, 2)
        add(t, 0, node(t, 3, 4))
        addList(t, 0, 5)

    elif len(t) == 5:
        # ID types IGUAL exp
        add(t, 0, node(t, 1))
        addList(t, 0, 2)
        add(t, 0, node(t, 3))
        addList(t, 0, 4)

    else:
        # ID types
        add(t, 0, node(t, 1))
        addList(t, 0, 2)


# -------------------------------Cristopher PL/PGSQL ---------------------------------------------


# -------------------------------Jonathan PL/PGSQL ---------------------------------------------

# ================= assign =================
def p_statements_assign(t):
    '''
        asignacionvar   : ID  DOSPTS IGUAL exp
                        | ID  IGUAL exp
    '''
    t[0] = Nodo("asignacionvar")
    if len(t) == 5:
        add(t, 0, node(t, 1, 3))
        addList(t, 0, 4)

    else:
        add(t, 0, node(t, 1, 2))
        addList(t, 0, 3)


# ================= perform =================
def p_statements_perfom(t):
    '''
        statements : PERFORM select
    '''
    t[0] = Nodo("statements")
    add(t, 0, node(t, 1))
    addList(t, 0, 2)



# -------------------------------Jonathan PL/PGSQL ---------------------------------------------
# callfunction

def p_callfunction(t):
    '''
        callfunction : SELECT ID PARIZQ exp_list PARDER
                     | SELECT ID PARIZQ PARDER
    '''
    if len(t)==6:
        t[0] = Nodo("callfunction")
        add(t, 0, node(t, 1, 2))
        addList(t, 0, 4)

    elif len(t)==5:
        add(t, 0, node(t, 1, 2))
        addList(t, 0, 4)


def p_callfunction_lappel(t):
    '''
        callfunction : ID PARIZQ exp_list PARDER
                     | ID PARIZQ PARDER
    '''
    t[0] = Nodo("callfunction")
    add(t, 0, node(t, 1))
    addList(t, 0, 3)


# =================  INDEX =================
def p_index(t):
    '''
        index : create_index
              | drop_index
              | alter_index
    '''
    t[0] = Nodo("index")
    addList(t, 0, 1)


# ================= CREATE INDEX =================

def p_create_index1(t):
    '''
       create_index : CREATE        index_id_on_id             PARIZQ index_params PARDER
    '''
    t[0] = Nodo("create_index")
    add(t, 0, node(t, 1))
    addList(t, 0, 2)
    addList(t, 0, 4)


def p_create_index2(t):
    '''
        create_index : CREATE        index_id_on_id             PARIZQ index_params PARDER conditions
    '''
    t[0] = Nodo("create_index")
    add(t, 0, node(t, 1))
    addList(t, 0, 2)
    addList(t, 0, 4)
    addList(t, 0, 6)


def p_create_index3(t):
    '''
        create_index : CREATE UNIQUE index_id_on_id             PARIZQ index_params PARDER conditions
    '''
    t[0] = Nodo("create_index")
    add(t, 0, node(t, 1, 2))
    addList(t, 0, 3)
    addList(t, 0, 5)
    addList(t, 0, 7)


def p_create_index4(t):
    '''
        create_index : CREATE UNIQUE index_id_on_id             PARIZQ index_params PARDER
    '''
    t[0] = Nodo("create_index")
    add(t, 0, node(t, 1, 2))
    addList(t, 0, 3)
    addList(t, 0, 5)


def p_create_index5(t):
    '''
        create_index : CREATE        index_id_on_id USING HASH  PARIZQ index_params PARDER
    '''
    t[0] = Nodo("create_index")
    add(t, 0, node(t, 1))
    addList(t, 0, 2)
    add(t, 0, node(t, 3, 4))
    addList(t, 0, 6)


def p_create_index(t):
    '''
        create_index : CREATE        index_id_on_id USING HASH  PARIZQ index_params PARDER conditions
    '''
    t[0] = Nodo("create_index")
    add(t, 0, node(t, 1))
    addList(t, 0, 2)
    add(t, 0, node(t, 3, 4))
    addList(t, 0, 6)
    addList(t, 0, 8)


# ================= INDEX_PARAMS =================

def p_index_id_on_id(t):
    '''
        index_id_on_id : INDEX ID ON ID
                       | INDEX    ON ID
    '''
    t[0] = Nodo("index_id_on_id")
    if len(t) == 5:
        add(t, 0, node(t, 1, 4))
    if len(t) == 4:
        add(t, 0, node(t, 1, 3))


def p_index_params(t):
    '''
        index_params    : index_params COMA index_param
                        | index_param
    '''
    if len(t) == 4:
        t[1].add(t[3])
        t[0] = t[1]
    else:
        t[0] = Nodo("index_params")
        t[0].add(t[1])


def p_index_param1(t):
    '''
        index_param     :  ID options
                        |  ID
    '''
    t[0] = Nodo("index_param")
    if len(t) == 3:
        add(t, 0, node(t, 1))
        addList(t, 0, 2)
    else:
        add(t, 0, node(t, 1))


def p_index_param(t):
    '''
        index_param     :  exp
                        |  exp options
    '''
    t[0] = Nodo("index_param")
    if len(t) == 3:
        addList(t, 0, 1, 2)
    else:
        addList(t, 0, 1)


def p_options(t):
    '''
        options    : options option
                   | option
    '''
    if len(t) == 3:
        t[1].add(t[2])
        t[0] = t[1]
    else:
        t[0] = Nodo("options")
        t[0].add(t[1])


def p_option(t):
    '''
        option    : COLLATE
                  | ASC
                  | DESC
                  | NULLS
                  | FIRST
                  | LAST
    '''
    t[0] = Nodo("option")
    add(t, 0, node(t, 1))


# ================= drop index =================

def p_drop_index1(t):
    '''
        drop_index    : DROP INDEX CONCURRENTLY IF EXISTS list_cascade
    '''
    t[0] = Nodo("drop_index")
    add(t, 0, node(t, 1, 5))
    addList(t, 0, 6)


def p_drop_index2(t):
    '''
        drop_index    : DROP INDEX CONCURRENTLY           list_cascade
    '''
    t[0] = Nodo("drop_index")
    add(t, 0, node(t, 1, 3))
    addList(t, 0, 4)


def p_drop_index3(t):
    '''
        drop_index    : DROP INDEX  IF EXISTS list_cascade
    '''
    t[0] = Nodo("drop_index")
    add(t, 0, node(t, 1, 4))
    addList(t, 0, 5)


def p_drop_index4(t):
    '''
        drop_index    : DROP INDEX            list_cascade
    '''
    t[0] = Nodo("drop_index")
    add(t, 0, node(t, 1, 2))
    addList(t, 0, 3)


def p_list_cascade(t):
    '''
        list_cascade    : idlist cascade_strict
                        | idlist
    '''
    t[0] = Nodo("list_cascade")
    if len(t) == 3:
        addList(t, 0, 1, 2)
    else:
        addList(t, 0, 1)


def p_drop_cascade_strict(t):
    '''
        cascade_strict  : CASCADE
                        | RESTRICT
    '''
    t[0] = Nodo("cascade_strict")
    add(t, 0, node(t, 1))


# ================= alter index =================

def p_alter_index1(t):
    '''
        alter_index  : sub_alter  ID RENAME TO ID
    '''
    t[0] = Nodo("alter_index")
    addList(t, 0, 1)
    add(t, 0, node(t, 2, 5))


def p_alter_index9(t):
    '''
        alter_index  : sub_alter ID SET TABLESPACE ID
    '''
    t[0] = Nodo("alter_index")
    addList(t, 0, 1)
    add(t, 0, node(t, 2, 5))


def p_alter_index2(t):
    '''
        alter_index  : sub_alter ID ATTACH PARTITION TO ID
    '''
    t[0] = Nodo("alter_index")
    addList(t, 0, 1)
    add(t, 0, node(t, 2, 6))


def p_alter_index3(t):
    '''
        alter_index  : sub_alter ID DEPENDS ON EXTENSION TO ID
    '''
    t[0] = Nodo("alter_index")
    addList(t, 0, 1)
    add(t, 0, node(t, 2, 7))


def p_alter_index4(t):
    '''
        alter_index  : sub_alter ID ALTER COLUMN ENTERO SET STATISTICS ENTERO
    '''
    t[0] = Nodo("alter_index")
    addList(t, 0, 1)
    add(t, 0, node(t, 2, 8))


def p_alter_index5(t):
    '''
        alter_index  : sub_alter ID ALTER        ENTERO SET STATISTICS ENTERO
    '''
    t[0] = Nodo("alter_index")
    addList(t, 0, 1)
    add(t, 0, node(t, 2, 7))


def p_alter_index6(t):
    '''
        alter_index  : sub_alter ID SET PARIZQ exp_list PARDER
    '''
    t[0] = Nodo("alter_index")
    addList(t, 0, 1)
    add(t, 0, node(t, 2, 3))
    addList(t, 0, 5)


def p_alter_index7(t):
    '''
        alter_index  : sub_alter ID RESET PARIZQ exp_list PARDER
    '''
    t[0] = Nodo("alter_index")
    addList(t, 0, 1)
    add(t, 0, node(t, 2, 3))
    addList(t, 0, 5)


def p_alter_index8(t):
    '''
        alter_index  : sub_alter ALL IN TABLESPACE ID OWNED BY idlist SET TABLESPACE ID NOWAIT
    '''
    t[0] = Nodo("alter_index")
    addList(t, 0, 1)
    add(t, 0, node(t, 2, 7))
    addList(t, 0, 8)
    add(t, 0, node(t, 9, 12))


def p_alter_index(t):
    '''
        alter_index  : sub_alter ID ALTER COLUMN ID ID
    '''
    t[0] = Nodo("alter_index")
    addList(t, 0, 1)
    add(t, 0, node(t, 2))
    add(t, 0, node(t, 3, 4))
    add(t, 0, node(t, 5))
    add(t, 0, node(t, 6))


def p_sub_alter(t):
    '''
        sub_alter : ALTER INDEX IF EXISTS
                  | ALTER INDEX
    '''
    t[0] = Nodo("sub_alter")
    if len(t) == 5:
        add(t, 0, node(t, 1, 4))
    else:
        add(t, 0, node(t, 1, 2))


# ------------------------------------------------------------------------------------------

# --------------------------------Fin PL/PGSQL ---------------------------------------------
# ------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------
# ------------------------------------ DataManipulationLenguage ---------------------------------------------
# -----------------------------------------------------------------------------------------------------------

def p_DataManipulationLenguage_select(t):
    '''
        DataManipulationLenguage  : select
    '''
    t[0] = Nodo("DataManipulationLenguage")
    addList(t, 0, 1)


def p_DataManipulationLenguage_use(t):
    '''
        DataManipulationLenguage  : use_database
    '''
    t[0] = Nodo("DataManipulationLenguage")
    addList(t, 0, 1)


def p_DataManipulationLenguage_show_databases(t):
    '''
        DataManipulationLenguage  : SHOW DATABASES
    '''
    t[0] = Nodo("DataManipulationLenguage")
    add(t, 0, node(t, 1, 2))


def p_use_database(t):
    '''
        use_database : USE ID
    '''
    t[0] = Nodo("use_database")
    add(t, 0, node(t, 1, 2))


def p_DataManipulationLenguage_createTB(t):
    '''
        DataManipulationLenguage  : createTB
    '''
    t[0] = Nodo("DataManipulationLenguage")
    addSimple(t, 0, 1)


def p_DataManipulationLenguage_insert(t):
    '''
        DataManipulationLenguage  : insert
    '''
    t[0] = Nodo("DataManipulationLenguage")
    addSimple(t, 0, 1)


def p_DataManipulationLenguage_update(t):
    '''
        DataManipulationLenguage  : update
    '''
    t[0] = Nodo("DataManipulationLenguage")
    addSimple(t, 0, 1)


def p_DataManipulationLenguage_deletetable(t):
    '''
        DataManipulationLenguage  : deletetable
    '''
    t[0] = Nodo("ddl")
    addSimple(t, 0, 1)


def p_DataManipulationLenguage_droptable(t):
    '''
        DataManipulationLenguage  : drop_table
    '''
    t[0] = Nodo("DataManipulationLenguage")
    addSimple(t, 0, 1)


def p_DataManipulationLenguage_create_db(t):
    '''
        DataManipulationLenguage  : create_db
    '''
    t[0] = Nodo("ddl")
    addSimple(t, 0, 1)


def p_DataManipulationLenguage_alter_table(t):
    '''
        DataManipulationLenguage  : alter_table
    '''
    t[0] = Nodo("DataManipulationLenguage")
    addSimple(t, 0, 1)


def p_DataManipulationLenguage_create_type(t):
    '''
        DataManipulationLenguage  : create_type
    '''
    t[0] = Nodo("DataManipulationLenguage")
    addSimple(t, 0, 1)


def p_DataManipulationLenguage_alter_database(t):
    '''
        DataManipulationLenguage  : alter_database
    '''
    t[0] = Nodo("DataManipulationLenguage")
    addSimple(t, 0, 1)


def p_DataManipulationLenguage_drop_database(t):
    '''
        DataManipulationLenguage  : drop_database
    '''
    t[0] = Nodo("DataManipulationLenguage")
    addSimple(t, 0, 1)


def p_DataManipulationLenguage_UNION(t):
    '''
        DataManipulationLenguage  : select UNION select
    '''
    t[0] = Nodo("DataManipulationLenguage")
    addSimple(t, 0, 1)
    add(t, 0, node(t, 2))
    addSimple(t, 0, 3)


def p_DataManipulationLenguage_INTERSECT(t):
    '''
        DataManipulationLenguage  : select INTERSECT select
    '''
    t[0] = Nodo("DataManipulationLenguage")
    addSimple(t, 0, 1)
    add(t, 0, node(t, 2))
    addSimple(t, 0, 3)


def p_DataManipulationLenguage_except(t):
    '''
        DataManipulationLenguage  : select EXCEPT select
    '''
    t[0] = Nodo("DataManipulationLenguage")
    addSimple(t, 0, 1)
    add(t, 0, node(t, 2))
    addSimple(t, 0, 3)


def p_select(t):
    '''
        select  : SELECT exp_list FROM exp_list conditions
    '''
    t[0] = Nodo("select")
    add(t, 0, node(t, 1))
    addList(t, 0, 2)
    add(t, 0, node(t, 3))
    addList(t, 0, 4, 5)


def p_select_simple(t):
    '''
        select : SELECT exp_list FROM exp_list
    '''
    t[0] = Nodo("select")
    add(t, 0, node(t, 1))
    addList(t, 0, 2)
    add(t, 0, node(t, 3))
    addList(t, 0, 4)


def p_select_simple_simple(t):
    '''
        select : SELECT exp_list
    '''
    t[0] = Nodo("select")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 2)


def p_time(t):
    '''
        time : YEAR
             | HOUR
             | SECOND
             | MINUTE
             | MONTH
             | DAY
    '''
    t[0] = Nodo("time")
    add(t, 0, node(t, 1, 1))


def p_conditions(t):
    '''
        conditions  : conditions condition
                    | condition
    '''
    if len(t) == 3:
        t[1].add(t[3])
        t[0] = t[1]
    else:
        t[0] = Nodo("conditions")
        t[0].add(t[1])


def p_condition(t):
    '''
        condition       : WHERE exp
                        | ORDER BY exp setOrder
                        | GROUP BY exp_list
                        | LIMIT exp
                        | HAVING exp
    '''
    t[0] = Nodo("condition")

    if t[1].lower() == "where":
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 2)
    elif t[1].lower() == "order":
        # ORDER BY listavalores ordenamiento
        add(t, 0, node(t, 1, 2))
        addSimple(t, 0, 3)
        addSimple(t, 0, 4)

    elif t[1].lower() == "group":
        # GROUP BY listavalores
        add(t, 0, node(t, 1, 2))
        addSimple(t, 0, 3)

    elif t[1].lower() == "limit":
        # LIMIT exp
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 2)
        pass
    elif t[1].lower() == "having":
        # HAVING exp
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 2)


def p_atributoselecit_subquery(t):
    '''
        condition : subquery
    '''
    t[0] = Nodo("atributoselect")
    addSimple(t, 0, 1)


def p_setOrder(t):
    '''
        setOrder   : ASC
                       | DESC
    '''
    t[0] = Nodo("ordenamiento")
    addSimple(t, 0, 1)


def p_exp_list(t):
    '''
        exp_list   : exp_list COMA exp
                       | exp
    '''
    if len(t) == 4:
        t[1].add(t[3])
        t[0] = t[1]
    else:
        t[0] = Nodo("exp_list")
        t[0].add(t[1])


# --------------------------------------------------------------------------------------
# ------------------------------------ EXPRESSION  --------------------------------------------
# --------------------------------------------------------------------------------------
def p_exp_call(t):
    '''
        exp   : LOWER PARIZQ exp PARDER
              |       PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    if len(t) == 4:
        addList(t, 0, 2)
    else:
        add(t, 0, node(t, 1))
        addList(t, 0, 3)


def p_exp_count(t):
    '''
        exp   : COUNT PARIZQ exp PARDER
              | COUNT PARIZQ MULTI PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 2))
    addSimple(t, 0, 3)
    add(t, 0, node(t, 4, 4))


def p_exp_sum(t):
    '''
        exp   : SUM PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_avg(t):
    '''
        exp   : AVG PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_greatest(t):
    '''
        exp   : GREATEST PARIZQ exp_list PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_least(t):
    '''
        exp   : LEAST PARIZQ exp_list PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_max(t):
    '''
        exp   : MAX PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_min(t):
    '''
        exp   : MIN PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_abs(t):
    '''
        exp   : ABS PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_cbrt(t):
    '''
        exp   : CBRT PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_ceil(t):
    '''
        exp   : CEIL PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_ceiling(t):
    '''
        exp   : CEILING PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_degrees(t):
    '''
        exp   : DEGREES PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_div(t):
    '''
        exp   : DIV PARIZQ exp_list PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_tkexp(t):
    '''
        exp   : TKEXP PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_factorial(t):
    '''
        exp   : FACTORIAL PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_floor(t):
    '''
        exp   : FLOOR PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_gcd(t):
    '''
        exp   : GCD PARIZQ exp_list PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_ln(t):
    '''
        exp   : LN PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_log(t):
    '''
        exp   : LOG PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_mod(t):
    '''
        exp   : MOD PARIZQ exp_list PARDER
   '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_pi(t):
    '''
        exp   : PI PARIZQ PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))


def p_exp_now(t):
    '''
        exp   : NOW PARIZQ PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 3))


def p_exp_power(t):
    '''
        exp   : POWER PARIZQ exp_list PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_radians(t):
    '''
        exp   : RADIANS PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_round(t):
    '''
        exp   : ROUND PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_sign(t):
    '''
        exp   : SIGN PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_sqrt(t):
    '''
        exp   : SQRT PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_width(t):
    '''
        exp   : WIDTH_BUCKET PARIZQ exp COMA exp COMA exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    addSimple(t, 0, 5)
    addSimple(t, 0, 7)
    addSimple(t, 0, 9)


def p_exp_trunc(t):
    '''
        exp   : TRUNC PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_random(t):
    '''
        exp   : RANDOM PARIZQ PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 3))


# ==================================================================================
# ================================Fin Funciones Trigonometricas  ===================
# ==================================================================================

def p_exp_acos(t):
    '''
        exp   : ACOS PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_acosd(t):
    '''
        exp   : ACOSD PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_asin(t):
    '''
        exp   : ASIN PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_asind(t):
    '''
        exp   : ASIND PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_atan(t):
    '''
        exp   : ATAN PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_atand(t):
    '''
        exp   : ATAND PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_atan2(t):
    '''
        exp   : ATAN2 PARIZQ exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    addSimple(t, 0, 5)


def p_exp_atan2d(t):
    '''
        exp   : ATAN2D PARIZQ exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    addSimple(t, 0, 5)


def p_exp_cos(t):
    '''
        exp   : COS PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_cosd(t):
    '''
        exp   : COSD PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_cot(t):
    '''
        exp   : COT PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_cotd(t):
    '''
        exp   : COTD PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_sin(t):
    '''
        exp   : SIN PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_sind(t):
    '''
        exp   : SIND PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_tan(t):
    '''
        exp   : TAN PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_tand(t):
    '''
        exp   : TAND PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_sinh(t):
    '''
        exp   : SINH PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_cosh(t):
    '''
        exp   : COSH PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_tanh(t):
    '''
        exp   : TANH PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_asinh(t):
    '''
        exp   : ASINH PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_acosh(t):
    '''
        exp   : ACOSH PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_atanh(t):
    '''
        exp   : ATANH PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


# ==================================================================================
# ================================Fin Funciones Trigonometricas  ===================
# ==================================================================================

def p_exp_length(t):
    '''
        exp   : LENGTH PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_substring(t):
    '''
        exp   : SUBSTRING PARIZQ exp COMA exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_trim(t):
    '''
        exp   : TRIM PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_md5(t):
    '''
        exp   : MD5 PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_sha256(t):
    '''
        exp   : SHA256 PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_substr(t):
    '''
        exp   : SUBSTR PARIZQ exp COMA exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    addSimple(t, 0, 5)
    addSimple(t, 0, 7)


def p_exp_getbyte(t):
    '''
        exp   : GET_BYTE PARIZQ exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    addSimple(t, 0, 5)


def p_exp_setbyte(t):
    '''
        exp   : SET_BYTE PARIZQ exp COMA exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    addSimple(t, 0, 5)
    addSimple(t, 0, 7)


def p_exp_convert(t):
    '''
        exp   : CONVERT PARIZQ exp AS types PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    add(t, 0, node(t, 4, 4))
    addSimple(t, 0, 5)


def p_exp_encode(t):
    '''
        exp   : ENCODE PARIZQ exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    addSimple(t, 0, 5)


def p_exp_decode(t):
    '''
        exp   : DECODE PARIZQ exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    addSimple(t, 0, 5)


def p_exp_opunary(t):
    '''
        exp   : ORBB        exp
              | ORBBDOBLE   exp
              | NOTBB       exp
              | MAS         exp
              | MENOS       exp
              | NOT         exp
              | IS          exp
              | EXISTS      exp
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 2)


def p_exp_case(t):
    '''
        exp : case
    '''
    t[0] = Nodo("exp")
    addSimple(t, 0, 1)


def p_exp_between(t):
    '''
        exp : exp BETWEEN exp
    '''
    t[0] = Nodo("exp")
    addSimple(t, 0, 1)
    add(t, 0, node(t, 2, 2))
    addSimple(t, 0, 3)


def p_exp_distinct(t):
    '''
         exp  : exp IS DISTINCT FROM exp
    '''
    t[0] = Nodo("exp")
    addSimple(t, 0, 1)
    add(t, 0, node(t, 2, 4))
    addSimple(t, 0, 5)


def p_exp_notdistinct(t):
    '''
         exp  : exp IS NOT DISTINCT FROM exp
    '''
    t[0] = Nodo("exp")
    addSimple(t, 0, 1)
    add(t, 0, node(t, 2, 5))
    addSimple(t, 0, 6)


def p_exp(t):
    '''
        exp   : exp ANDBB       exp
              | exp ORBB        exp
              | exp NUMERAL     exp
              | exp SHIFTIZQ    exp
              | exp SHIFTDER    exp
              | exp TKEXP       exp
              | exp MULTI       exp
              | exp DIVISION    exp
              | exp MODULO      exp
              | exp MAS         exp
              | exp MENOS       exp
              | exp LIKE        exp
              | exp ILIKE       exp
              | exp SIMILAR     exp
              | exp NOT         exp
              | exp IN          exp
              | exp IGUALQUE    exp
              | exp IGUAL       exp
              | exp MAYORQUE    exp
              | exp MENORQUE    exp
              | exp MAYORIG     exp
              | exp MENORIG     exp
              | exp IS          exp
              | exp ISNULL      exp
              | exp NOTNULL     exp
              | exp AND         exp
              | exp OR          exp
              | expSimple
              | dateFunction
              | callfunction
              | exp NOT IN exp
    '''
    t[0] = Nodo("exp")
    if len(t) == 4:
        addSimple(t, 0, 1)
        add(t, 0, node(t, 2, 2))
        addSimple(t, 0, 3)


    elif len(t) == 2:
        # expSimple
        addSimple(t, 0, 1)


# --------------------------------------------------------------------------------------
# ------------------------------------ EXP SIMPLE --------------------------------------
# --------------------------------------------------------------------------------------
def p_expSimples_distinct(t):
    '''
        expSimple   : DISTINCT exp
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 2)


def p_expSimples_subquery(t):
    '''
        expSimple   : subquery
    '''
    t[0] = Nodo("expSimple")
    addSimple(t, 0, 1)


def p_expSimples(t):
    '''
        expSimple   : NULL
    '''
    t[0] = t[1]


def p_dateFunction(t):
    '''
        dateFunction : EXTRACT PARIZQ time FROM TIMESTAMP exp PARDER
                     | DATE_PART PARIZQ CADENA COMA INTERVAL exp PARDER
                     | NOW PARIZQ PARDER
                     | CURRENT_DATE
                     | CURRENT_TIME
                     | TIMESTAMP CADENA
    '''
    t[0] = Nodo("dateFunction")
    if t[1].lower() == "extract":
        # SELECT EXTRACT PARIZQ time FROM TIMESTAMP CADENA PARDER
        add(t, 0, node(t, 1, 2))
        addList(t, 0, 4)
        add(t, 0, node(t, 5, 8))

    elif t[1].lower() == "date_part":
        # SELECT DATE_PART PARIZQ CADENA COMA INTERVAL exp PARDER
        add(t, 0, node(t, 1, 2))
        add(t, 0, node(t, 1, 4))
        add(t, 0, node(t, 1, 6))
        addList(t, 0, 7)

    elif t[1].lower() == "now":
        # SELECT NOW PARIZQ PARDER
        add(t, 0, node(t, 1, 4))

    elif t[1].lower() == "current_date":
        # SELECT CURRENT_DATE
        add(t, 0, node(t, 1, 3))

    elif t[1].lower() == "current_time":
        # SELECT CURRENT_TIME
        add(t, 0, node(t, 1, 2))

    elif t[1].lower() == "timestamp":
        # SELECT TIMESTAMP CADENA
        add(t, 0, node(t, 1, 3))


def p_expSimples_ACCESO_TYPE(t):
    '''
        expSimple : ID CORIZQ exp CORDER
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_expSimples_ALIAS_MULTI(t):
    '''
        expSimple : ID PT MULTI
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 3))


def p_expSimples_MULTI(t):
    '''
        expSimple : MULTI
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))


def p_expSimples_ID(t):
    '''
        expSimple : ID
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))


def p_expSimples_ID_PT_ID(t):
    '''
        expSimple : ID PT ID
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 3))


def p_expSimples_ID_ID(t):
    '''
        expSimple : ID ID
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 2))


def p_expSimples_ID_AS_ID(t):
    '''
        expSimple : ID AS ID
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 3))


def p_expSimples_exp_AS_ID(t):
    '''
        expSimple : exp AS CADENA
                  | exp AS ID
                  | exp AS CADENADOBLE
    '''
    t[0] = Nodo("expSimple")
    addSimple(t, 0, 1)
    add(t, 0, node(t, 2, 3))


# --------------------------------------------------------------------------------------
# ----------------------------------------- SUBQUERY --------------------------------------
# --------------------------------------------------------------------------------------
def p_subquery(t):
    '''
        subquery : PARIZQ select PARDER
                 | PARIZQ select PARDER ID
                 | PARIZQ select PARDER AS ID
    '''
    t[0] = Nodo("subquery")
    if len(t) == 4:
        # PARIZQ select PARDER
        addSimple(t, 0, 2)

    elif len(t) == 5:
        # PARIZQ select PARDER ID
        addSimple(t, 0, 2)
        addSimple(t, 0, 4)

    elif len(t) == 6:
        # PARIZQ select PARDER AS ID
        pass


def p_expSimples_entero(t):
    '''
        expSimple   :   ENTERO
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))


def p_expSimples_decimal(t):
    '''
        expSimple   :  TKDECIMAL
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))


def p_expSimples_cadenas(t):
    '''
        expSimple   :   CADENA
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))


def p_expSimples_cadenadoble(t):
    '''
        expSimple   :   CADENADOBLE
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))


def p_expSimples_true(t):
    '''
        expSimple   :   TRUE
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))


def p_expSimples_false(t):
    '''
        expSimple  :   FALSE
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))


# --------------------------------------------------------------------------------------
# ----------------------------------------- TABLE CREATE --------------------------------------
# --------------------------------------------------------------------------------------
def p_createTB(t):
    '''
        createTB     : CREATE TABLE ID PARIZQ atributesTable COMA especs inherits
                     | CREATE TABLE ID PARIZQ atributesTable inherits
                     | CREATE TABLE IF NOT EXISTS ID PARIZQ atributesTable COMA especs inherits
                     | CREATE TABLE IF NOT EXISTS ID PARIZQ atributesTable inherits
    '''
    t[0] = Nodo("plpgsql")
    if len(t) == 9:
        # CREATE TABLE ID PARIZQ atributesTable COMA especs inherits
        add(t, 0, node(t, 1, 3))
        addList(t, 0, 5)
        addList(t, 0, 7, 8)

    if len(t) == 7:
        # CREATE TABLE ID PARIZQ atributesTable inherits
        add(t, 0, node(t, 1, 3))
        addList(t, 0, 5,6)

    if len(t) == 12:
        # CREATE TABLE IF NOT EXISTS ID PARIZQ atributesTable COMA especs inherits
        add(t, 0, node(t, 1, 6))
        addList(t, 0, 8)
        addList(t, 0, 10, 11)

    if len(t) == 10:
        # CREATE TABLE IF NOT EXISTS ID PARIZQ atributesTable inherits
        add(t, 0, node(t, 1, 6))
        addList(t, 0, 8,9)


# todo:no se que hacer con PARDER FALTA ? O SOLO ASI ES ?
def p_inherits(t):
    '''
        inherits : PARDER INHERITS PARIZQ ID PARDER
    '''
    t[0] = Nodo("inherits")
    add(t, 0, node(t, 1, 2))
    add(t, 0, node(t, 4, 4))


def p_inherits_parder(t):
    '''
        inherits : PARDER
    '''
    t[0] = Nodo("inherits")
    add(t, 0, node(t, 1, 1))


def p_atributesTable(t):
    '''
        atributesTable  : atributesTable COMA atributeTable
                     | atributeTable
    '''
    if len(t) == 4:
        t[1].add(t[3])
        t[0] = t[1]
    else:
        t[0] = Nodo("atributesTable")
        t[0].add(t[1])


def p_especs(t):
    '''
        especs  : especs COMA nextespec
                         | nextespec
    '''
    if len(t) == 4:
        t[1].add(t[3])
        t[0] = t[1]
    else:
        t[0] = Nodo("especs")
        t[0].add(t[1])


def p_nextespec(t):
    '''
        nextespec     : PRIMARY KEY PARIZQ idlist PARDER
                      | FOREIGN KEY PARIZQ idlist PARDER REFERENCES ID PARIZQ idlist PARDER
                      | CONSTRAINT ID CHECK PARIZQ exp PARDER
                      | CHECK PARIZQ exp PARDER
                      | UNIQUE PARIZQ idlist PARDER
    '''
    if len(t) == 6:  # PRIMARY KEY PARIZQ idlist PARDER
        add(t, 0, node(t, 1, 2))
        addSimple(t, 0, 4)
    elif len(t) == 11:  # FOREIGN KEY PARIZQ idlist PARDER REFERENCES ID PARIZQ idlist PARDER
        add(t, 0, node(t, 1, 2))
        addSimple(t, 0, 4)
        add(t, 0, node(t, 6, 7))
        addSimple(t, 0, 9)

    elif len(t) == 7:  # CONSTRAINT ID CHECK PARIZQ exp PARDER
        add(t, 0, node(t, 1, 3))
        addSimple(t, 0, 5)

    else:
        # CHECK PARIZQ exp PARDER
        # UNIQUE PARIZQ listaids PARDER
        add(t, 0, node(t, 1, 2))
        addSimple(t, 0, 3)


def p_atributeTable(t):
    '''
        atributeTable : ID  definitionTypes listaespecificaciones
                       | ID definitionTypes
    '''
    t[0] = Nodo("atributeTable")
    if len(t) == 4:
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 2)
        addSimple(t, 0, 3)
    elif len(t) == 3:
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 2)


# --------------------------------------------------------------------------------------
# ----------------------------------------- ESPECIFICACIONES--------------------------------------
# --------------------------------------------------------------------------------------
def p_listaespecificaciones(t):
    '''
        listaespecificaciones  : listaespecificaciones especificaciones
                               | especificaciones
    '''
    if len(t) == 3:
        t[1].add(t[2])
        t[0] = t[1]
    else:
        t[0] = Nodo("listaespecificaciones")
        t[0].add(t[1])


def p_especificaciones_default(t):
    '''
        especificaciones : DEFAULT exp
    '''
    t[0] = Nodo("especificaciones")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 2)


def p_especificaciones_primary_key(t):
    '''
        especificaciones : PRIMARY KEY
    '''
    t[0] = Nodo("especificaciones")
    add(t, 0, node(t, 1, 2))


def p_especificaciones_references_id(t):
    '''
        especificaciones : REFERENCES ID
    '''
    t[0] = Nodo("especificaciones")
    add(t, 0, node(t, 1, 2))


def p_especificaciones_contraint_id_unique(t):
    '''
        especificaciones : CONSTRAINT ID UNIQUE
    '''
    t[0] = Nodo("especificaciones")
    add(t, 0, node(t, 1, 3))


def p_especificaciones_constraint(t):
    '''
        especificaciones : CONSTRAINT ID CHECK PARIZQ exp PARDER
    '''
    t[0] = Nodo("especificaciones")
    add(t, 0, node(t, 1, 3))
    addSimple(t, 0, 5)


def p_especificaciones_check(t):
    '''
        especificaciones : CHECK PARIZQ exp PARDER
    '''
    t[0] = Nodo("especificaciones")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_especificaciones_not_null(t):
    '''
        especificaciones : NOT NULL
    '''
    t[0] = Nodo("especificaciones")
    add(t, 0, node(t, 1, 2))


def p_especificaciones(t):
    '''
        especificaciones : UNIQUE
                         | NULL
    '''
    t[0] = Nodo("especificaciones")
    add(t, 0, node(t, 1, 1))


# --------------------------------------------------------------------------------------
# -----------------------------------------types--------------------------------------
# --------------------------------------------------------------------------------------
def p_definitionTypes(t):
    '''
        definitionTypes : f2types
    '''
    t[0] = Nodo("tipocql")
    addSimple(t, 0, 1)


def p_definitionTypes_id(t):
    '''
        definitionTypes : ID
    '''
    t[0] = t[1]


def p_f2types(t):
    '''
        f2types : SMALLINT
                | INTEGER
                | BIGINT
                | NUMERIC
                | REAL
                | MONEY
                | TEXT
                | FLOAT
                | TIME
                | DATE
                | TIMESTAMP
                | INTERVAL
                | BOOLEAN
                | DOUBLE    PRECISION
                | DECIMAL   PARIZQ      ENTERO COMA   ENTERO PARDER
                | CHARACTER VARYING     PARIZQ ENTERO PARDER
                | VARCHAR   PARIZQ      ENTERO PARDER
                | CHAR      PARIZQ      ENTERO PARDER
                | STRING
    '''
    t[0] = Nodo("f2types")
    if len(t) == 2:
        add(t, 0, node(t, 1))

    elif len(t) == 3:
        add(t, 0, node(t, 1,2))

    elif len(t) == 7:
        add(t, 0, node(t, 1,6))

    elif len(t) == 6:
        add(t, 0, node(t, 1,5))

    elif len(t) == 5:
        add(t, 0, node(t, 1,4))


def p_types(t):
    '''
         types : SMALLINT
              | INTEGER
              | BIGINT
              | DECIMAL PARIZQ exp COMA exp PARDER
              | NUMERIC
              | REAL
              | MONEY
              | TEXT
              | FLOAT
              | TIME
              | DATE
              | TIMESTAMP
              | INTERVAL
              | BOOLEAN
              | DOUBLE PRECISION
              | CHARACTER VARYING PARIZQ exp PARDER
              | VARCHAR PARIZQ exp PARDER
              | CHAR PARIZQ exp PARDER
              | STRING
    '''
    t[0] = Nodo("types")
    if len(t) == 2:
        add(t, 0, node(t, 1))
    elif len(t) == 3:
        add(t, 0, node(t, 1, 2))
    elif len(t) == 5:
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 3)
    elif len(t) == 6:
        add(t, 0, node(t, 1, 2))
        addSimple(t, 0, 4)
    elif len(t) == 7:
        add(t, 0, node(t, 1))
        addSimple(t, 0, 3)
        addSimple(t, 0, 5)


def p_types_character_varying(t):
    '''
        types : CHARACTER PARIZQ exp PARDER
    '''
    t[0] = Nodo("types")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


# --------------------------------------------------------------------------------------
# ----------------------------------------- INSERT--------------------------------------
# --------------------------------------------------------------------------------------
def p_insert(t):
    '''
        insert : INSERT INTO ID                        VALUES PARIZQ exp_list PARDER
               | INSERT INTO ID PARIZQ idlist PARDER VALUES PARIZQ exp_list PARDER
    '''
    t[0] = Nodo("insert")
    if len(t) == 8:
        # INSERT INTO ID VALUES PARIZQ listavalores PARDER
        add(t, 0, node(t, 1, 3))
        addSimple(t, 0, 6)
    elif len(t) == 11:
        # INSERT INTO ID PARIZQ listaids PARDER VALUES PARIZQ listavalores PARDER
        add(t, 0, node(t, 1, 3))
        addSimple(t, 0, 5)
        add(t, 0, node(t, 7, 7))
        addSimple(t, 0, 9)


def p_idlist(t):
    '''
        idlist   : idlist COMA ID
                 | ID
    '''
    if len(t) == 4:
        t[1].add(node(t,3))
        t[0] = t[1]
    else:
        t[0] = Nodo("idlist")
        t[0].add(node(t,1))


# --------------------------------------------------------------------------------------
# ----------------------------------------- UPDATE--------------------------------------
# --------------------------------------------------------------------------------------
def p_update(t):
    '''
        update : UPDATE ID SET exp_list WHERE exp
               | UPDATE ID SET exp_list
    '''
    t[0] = Nodo("update")
    if len(t) == 7:
        # UPDATE ID SET listaupdate WHERE exp
        add(t, 0, node(t, 1, 3))
        addSimple(t, 0, 4)
        add(t, 0, node(t, 5, 5))
        addSimple(t, 0, 6)
    elif len(t) == 5:
        # UPDATE ID SET listaupdate
        add(t, 0, node(t, 1, 3))
        addSimple(t, 0, 4)


def p_setcolumns(t):
    '''
        setcolumns : setcolumns COMA updateAsign
                   | updateAsign
    '''
    if len(t) == 4:  # listaupdate COMA asignacionupdate
        t[1].add(t[3])
        t[0] = t[1]
    else:  # asignacionupdate
        t[0] = Nodo("setcolumns")
        t[0].add(t[1])


def p_updateAsign(t):
    '''
        updateAsign : ID IGUAL exp
    '''
    t[0] = Nodo("updateAsign")
    add(t, 0, node(t, 1, 2))
    addSimple(t, 0, 3)


# --------------------------------------------------------------------------------------
# ------------------------------ defAcces--------------------------------------
# --------------------------------------------------------------------------------------
# TODO: Segun la gramatica, hace falta la produccion 'Variable' cuya exp. reg. es: "@[A-Za-z][_A-Za-z0-9]*"
def p_acceso(t):
    '''
        defAcces : defAcces PT newInstructions
               | defAcces  CORIZQ exp CORDER
               | ID
    '''
    t[0] = Nodo("defAcces")
    if len(t) == 4:
        # acceso PT funcioncollection
        addSimple(t, 0, 1)
        add(t, 0, node(t, 2, 2))
        addSimple(t, 0, 3)

    elif len(t) == 5:
        # acceso  CORIZQ exp CORDER
        addSimple(t, 0, 1)
        addSimple(t, 0, 3)

    elif len(t) == 2:
        # ID
        add(t, 0, node(t, 1, 1))


def p_acceso_ID(t):
    '''
        defAcces : defAcces PT ID
    '''
    t[0] = Nodo("defAcces")
    addSimple(t, 0, 1)
    add(t, 0, node(t, 2, 3))


# --------------------------------------------------------------------------------------
# ------------------------------NEW INSTRUCTIONS--------------------------------------
# --------------------------------------------------------------------------------------
def p_newInstructions(t):
    '''
        newInstructions   : INSERT PARIZQ exp COMA exp PARDER
                            | INSERT PARIZQ exp PARDER
                            | SET PARIZQ exp COMA exp PARDER
                            | REMOVE PARIZQ exp PARDER
                            | SIZE PARIZQ PARDER
                            | CLEAR PARIZQ PARDER
                            | CONTAINS PARIZQ exp PARDER
                            | LENGTH PARIZQ PARDER
                            | SUBSTRING PARIZQ exp COMA exp PARDER
    '''
    t[0] = Nodo("funcioncollection")

    if t[1].lower() == 'insert':
        if len(t) == 7:
            # INSERT PARIZQ exp COMA exp PARDER
            add(t, 0, node(t, 1, 1))
            addSimple(t, 0, 3)
            addSimple(t, 0, 4)
        elif len(t) == 5:
            # INSERT PARIZQ exp PARDER
            add(t, 0, node(t, 1, 1))
            addSimple(t, 0, 3)
    elif t[1].lower() == 'set':
        # SET PARIZQ exp COMA exp PARDER
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 3)
        addSimple(t, 0, 5)
    elif t[1].lower() == 'remove':
        # REMOVE PARIZQ exp PARDER
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 3)
    elif t[1].lower() == 'size':
        # SIZE PARIZQ PARDER
        add(t, 0, node(t, 1, 3))
    elif t[1].lower() == 'clear':
        # CLEAR PARIZQ PARDER
        add(t, 0, node(t, 1, 3))
    elif t[1].lower() == 'contains':
        # CONTAINS PARIZQ exp PARDER
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 3)
    elif t[1].lower() == 'length':
        # LENGTH PARIZQ PARDER
        add(t, 0, node(t, 1, 3))
    elif t[1].lower() == 'substring':
        # SUBSTRING PARIZQ exp COMA exp PARDER
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 3)
        addSimple(t, 0, 5)


# --------------------------------------------------------------------------------------
# --------------------------------- DELETE TABLE--------------------------------------
# --------------------------------------------------------------------------------------
def p_deletetable(t):
    '''
        deletetable : DELETE FROM ID WHERE exp
                    | DELETE FROM ID
                    | DELETE groupatributes FROM ID WHERE exp
                    | DELETE groupatributes FROM ID
    '''
    t[0] = Nodo("deletetable")
    if len(t) == 6:
        # DELETE FROM ID WHERE exp
        add(t, 0, node(t, 1, 4))
        addSimple(t, 0, 5)
    elif len(t) == 4:
        # DELETE FROM ID
        add(t, 0, node(t, 1, 3))
    elif len(t) == 7:
        # DELETE listaatributos FROM ID WHERE exp
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 2)
        add(t, 0, node(t, 3, 5))
        addSimple(t, 0, 6)
        pass
    elif len(t) == 5:
        # DELETE listaatributos FROM ID
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 2)
        add(t, 0, node(t, 3, 4))


# --------------------------------------------------------------------------------------
# --------------------------------- groupatributes--------------------------------------
# --------------------------------------------------------------------------------------
def p_groupatributes(t):
    '''
        groupatributes : groupatributes COMA defAcces
                       | defAcces
    '''
    if len(t) == 4:  # listaatributos COMA acceso
        t[1].add(t[3])
        t[0] = t[1]
    else:  # acceso
        t[0] = Nodo("groupatributes")
        t[0].add(t[1])


# -------------------------------------------------------------------------------------
# ---------------------------------CREATE DB--------------------------------------
# -------------------------------------------------------------------------------------
def p_create_db(t):
    '''
        create_db : CREATE OR REPLACE DATABASE IF NOT EXISTS createdb_extra
                  | CREATE OR REPLACE DATABASE createdb_extra
                  | CREATE DATABASE IF NOT EXISTS createdb_extra
                  | CREATE DATABASE createdb_extra
    '''
    t[0] = Nodo("create_db")

    if len(t) == 9:
        # CREATE OR REPLACE DATABASE IF NOT EXISTS createdb_extra
        add(t, 0, node(t, 1, 7))
        addSimple(t, 0, 8)
    elif len(t) == 6:
        # CREATE OR REPLACE DATABASE createdb_extra
        add(t, 0, node(t, 1, 4))
        addSimple(t, 0, 5)
    elif len(t) == 7:
        # CREATE DATABASE IF NOT EXISTS createdb_extra
        add(t, 0, node(t, 1, 5))
        addSimple(t, 0, 6)
    elif len(t) == 4:
        # CREATE DATABASE createdb_extra
        add(t, 0, node(t, 1, 2))
        addSimple(t, 0, 3)


# -------------------------------------------------------------------------------------
# ---------------------------------CREATEDB EXTRA--------------------------------------
# ------------------ESTA PARTE SOLO SE DEBE RECONOCER EN LA GRAMATICA------------------
# -------------------------------------------------------------------------------------
def p_createdb_extra(t):
    '''
        createdb_extra : ID OWNER  IGUAL exp MODE IGUAL exp
                       | ID OWNER  IGUAL exp MODE exp
                       | ID OWNER  exp   MODE IGUAL exp
                       | ID OWNER  exp   MODE exp
                       | ID OWNER  IGUAL exp
                       | ID MODE   IGUAL exp
                       | ID OWNER  exp
                       | ID MODE   exp
                       | ID
    '''
    t[0] = Nodo("createdb_extra")
    if len(t) == 2:  # ID
        add(t, 0, node(t, 1, 1))
    elif len(t) == 4:  # ID MODE   exp
        add(t, 0, node(t, 1, 3))
    elif len(t) == 5:  # ID MODE IGUAL exp
        add(t, 0, node(t, 1, 4))
    elif len(t) == 6:  # ID OWNER exp MODE exp
        add(t, 0, node(t, 1, 5))
    elif len(t) == 7:  # ID OWNER exp  MODE IGUAL exp
        add(t, 0, node(t, 1, 6))
    elif len(t) == 8:  # ID OWNER IGUAL exp MODE IGUAL exp
        add(t, 0, node(t, 1, 7))


# -------------------------------------------------------------------------------------
# --------------------------------- DROP TABLE--------------------------------------
# -------------------------------------------------------------------------------------
def p_drop_table(t):
    '''
        drop_table : DROP TABLE IF EXISTS ID
                   | DROP TABLE ID
    '''
    t[0] = Nodo("drop_table")
    if len(t) == 6:
        # DROP TABLE IF EXISTS ID
        add(t, 0, node(t, 1, 5))
    elif len(t) == 4:
        # DROP TABLE ID
        add(t, 0, node(t, 1, 3))


# -------------------------------------------------------------------------------------
# ---------------------------------ALTER TABLE--------------------------------------
# -------------------------------------------------------------------------------------
def p_alter_table(t):
    '''
        alter_table : ALTER TABLE ID ADD listaespecificaciones
                    | ALTER TABLE ID DROP listaespecificaciones
                    | ALTER TABLE ID groupcolumns
    '''
    t[0] = Nodo("alter_table")
    if len(t) == 6:
        # ALTER TABLE ID ADD listaespecificaciones
        # ALTER TABLE ID DROP listaespecificaciones
        add(t, 0, node(t, 1, 4))
        addSimple(t, 0, 5)

    elif len(t) == 5:
        # ALTER TABLE ID listacolumn
        add(t, 0, node(t, 1, 3))
        addSimple(t, 0, 4)


# -------------------------------------------------------------------------------------
# ---------------------------------LISTA COLUMN--------------------------------------
# -------------------------------------------------------------------------------------
def p_groupcolumns(t):
    '''
        groupcolumns : groupcolumns COMA column
                    | column
    '''
    if len(t) == 4:
        # listacolumn COMA column
        t[1].add(t[3])
        t[0] = t[1]
    else:
        # column
        t[0] = Nodo("listacolumn")
        t[0].add(t[1])


# ------------------------------------------------------------------------------------
# ---------------------------------COLUMN--------------------------------------
# ------------------------------------------------------------------------------------
def p_column(t):
    '''
        column : ALTER COLUMN ID listaespecificaciones
               | ADD COLUMN ID types
               | DROP COLUMN ID
    '''
    t[0] = Nodo("column")
    if t[1].lower() == 'alter':
        # ALTER COLUMN ID listaespecificaciones
        add(t, 0, node(t, 1, 3))
        addSimple(t, 0, 4)

    elif t[1].lower() == 'add':
        # ADD COLUMN ID tipo
        add(t, 0, node(t, 1, 3))
        addSimple(t, 0, 4)


    elif t[1].lower() == 'drop':
        # DROP COLUMN ID
        add(t, 0, node(t, 1, 3))


# -------------------------------------------------------------------------------------
# ---------------------------------CREATE TYPE--------------------------------------
# -------------------------------------------------------------------------------------
def p_create_type(t):
    '''
        create_type : CREATE TYPE ID AS ENUM PARIZQ exp_list PARDER
    '''
    t[0] = Nodo("create_type")
    add(t, 0, node(t, 1, 5))
    addSimple(t, 0, 7)


# -------------------------------------------------------------------------------------
# ---------------------------------ALTER DATABASE--------------------------------------
# -------------------------------------------------------------------------------------
# EN EL CASO DE LA PRODUCCION QUE TIENE EL TERMINAL OWNER UNICAMENTE SE VA A RECONOCER EN LA GRAMATICA
def p_alter_database(t):
    '''
        alter_database : ALTER DATABASE ID RENAME TO ID
                       | ALTER DATABASE ID OWNER  TO CURRENT_USER
                       | ALTER DATABASE ID OWNER  TO SESSION_USER
    '''
    t[0] = Nodo("alter_database")
    add(t, 0, node(t, 1, 6))


# ------------------------------------------------------------------------------------
# ---------------------------------DROP DATABASE--------------------------------------
# ------------------------------------------------------------------------------------
def p_drop_database(t):
    '''
        drop_database : DROP DATABASE IF EXISTS ID
                      | DROP DATABASE ID
    '''
    t[0] = Nodo("drop_database")

    if len(t) == 6:
        # DROP DATABASE IF EXISTS ID
        add(t, 0, node(t, 1, 4))
        add(t, 0, node(t, 5, 5))

    elif len(t) == 4:
        # DROP DATABASE ID
        add(t, 0, node(t, 1, 3))


# --------------- concat Nodo ---------------

def node(t, inicio: int, fin: int = -1) -> Nodo:
    if fin == -1:
        fin = inicio

    value = ''
    for i in range(inicio, fin + 1):
        value += str(t[i]).replace('"',"'") + ' '
    result = Nodo(value)
    return result


# --------------- add Nodo ---------------
def add(t, destino: int, Nodoorigen: Nodo):
    t[destino].add(Nodoorigen)


def addSimple(t, destino: int, origen: int):
    t[destino].add(t[origen])


def addList(t, destino: int, inicio: int, fin: int = -1):
    if fin == -1:
        fin = inicio

    for i in range(inicio, fin + 1):
        t[destino].add(t[i])


# ---------------ERROR SINTACTICO---------------
def p_error(t):
    print('error',t)
    #print("Error sintáctico en '%s'" % t.value)


import ply.yacc as yacc

parser = yacc.yacc()


def parseo(input):
    global cadena, lisErr, dot
    # parser = yacc.yacc()
    lexerreporte.lineno = 1
    # par= parser.parse("ADD")
    # print(par)
    return parser.parse(input)
