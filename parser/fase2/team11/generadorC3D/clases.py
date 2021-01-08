import ply.yacc as yacc
import ply.lex as lex
import re

from generadorC3D.clases import Enum, Error, EType, Nodo, TraducirProcedimientos
from generadorC3D.creacionArbol import *
#from reporteEnEjecucion import *
from graphviz import render


contadorTemp = 0
C3Direcciones = []
Errores = []
procedimientos = []

reservadas = {
    'smallint': 'SMALLINT',          'integer': 'INTEGER',
    'bigint': 'BIGINT',            'numeric': 'NUMERIC',
    'real': 'REAL',                'double': 'DOUBLE',
    'money': 'MONEY',             'character': 'CHARACTER',
    'varying': 'VARYING',           'varchar': 'VARCHAR',
    'char': 'CHAR',              'text': 'TEXT',
    'date': 'DATE',              'time': 'TIME',
    'timestamp': 'TIMESTAMP',    'float': 'FLOAT',
    'int': 'INT',            
    'boolean': 'BOOLEAN',           'create': 'CREATE',
    'or': 'OR',                 'if': 'IF',
    'not': 'NOT',               'alter': 'ALTER',
    'drop': 'DROP',
    'table': 'TABLE',             'default': 'DEFAULT',
    'null': 'NULL',             'and': 'AND',                   
    'insert': 'INSERT',         'into': 'INTO',
    'update': 'UPDATE',         'delete': 'DELETE',
    'from': 'FROM',              'truncate': 'TRUNCATE',
    'year': 'YEAR',
    'month': 'MONTH',              'day': 'DAY',
    'minute': 'MINUTE',             'second': 'SECOND',
    'type': 'TYPE',             'interval': 'INTERVAL',
    'hour': 'HOUR',             'select': 'SELECT',
    'as': 'AS',         
    'abs': 'ABS',                'cbrt': 'CBRT',
    'ceil': 'CEIL',               'ceiling': 'CEILING',
    'degrees': 'DEGREES',            'div': 'DIV',
    'exp': 'EXP',                'factorial': 'FACTORIAL',
    'floor': 'FLOOR',              'gcd': 'GCD',
    'ln': 'LN',                 'log': 'LOG',
    'mod': 'MOD',                'pi': 'PI',
    'power': 'POWER',              'radians': 'RADIANS',
    'round': 'ROUND',
    'acos': 'ACOS',               'acosd': 'ACOSD',
    'asin': 'ASIN',               'asind': 'ASIND',
    'atan': 'ATAN',               'atand': 'ATAND',
    'atan2': 'ATAN2',              'atan2d': 'ATAN2D',
    'cos': 'COS',                'cosd': 'COSD',
    'cot': 'COT',                'cotd': 'COTD',
    'sin': 'SIN',                'sind': 'SIND',
    'tan': 'TAN',                'tand': 'TAND',
    'sinh': 'SINH',               'cosh': 'COSH',
    'tanh': 'TANH',               'asinh': 'ASINH',
    'acosh': 'ACOSH',              'atanh': 'ATANH',
    'length': 'LENGTH',             'substring': 'SUBSTRING',
    'trim': 'TRIM',               'get_byte': 'GET_BYTE',
    'md5': 'MD5',                'set_byte': 'SET_BYTE',
    'sha256': 'SHA256',             'substr': 'SUBSTR',
    'convert': 'CONVERT',            'encode': 'ENCODE',
    'decode': 'DECODE',             'for': 'FOR',
    'between': 'BETWEEN',           'case' : 'CASE',
    'end' : 'END',                  'when' : 'WHEN',
    'then' : 'THEN'   ,              'else' : 'ELSE',
    'sign': 'SIGN',                 'sqrt': 'SQRT',
    'width_bucket': 'WBUCKET',      'trunc': 'TRUNC',
    'random': 'RANDOM',             'true': 'TRUE',
    'false': 'FALSE',               'decimal': 'RDECIMAL', 
    'extract': 'EXTRACT',           'date_part': 'DATE_PART',
    'current_date': 'CURRENT_DATE', 'current_time': 'CURRENT_TIME',
    'now': 'NOW',                   'index': 'INDEX', 
    'on': 'ON',                     'using': 'USING',
    'function': 'FUNCTION',         'returns': 'RETURNS',
    'declare': 'DECLARE',           'begin': 'BEGIN',
    'raise': 'RAISE',               'notice': 'NOTICE',
    'return': 'RETURN',             'outerblock': 'OUTERBLOCK',
    'constant': 'CONSTANT',         'alias': 'ALIAS1',
    'out': 'OUT',                   'language': 'LANGUAGE',
    'plpgsql': 'PLPGSQL',           'record':'RECORD',
    'query': 'QUERY',               'rowtype':'ROWTYPE',
    'execute': 'EXECUTE',           'using':'USING',
    'format': 'FORMAT',             'diagnostics':'DIAGNOSTICS', 
    'get': 'GET',                   'procedure': 'PROCEDURE',
    'inout': 'INOUT',               'elsif': 'ELSIF',
    'rollback':'ROLLBACK',          'commit':'COMMIT',
    'exists': 'EXISTS'

}

tokens = [
    'COMA',        'PTCOMA',  'PARIZQ',
    'PARDER',    'IGUAL',       'MAS', 
    'ASTERISCO',   'DIVIDIDO',  'EXPONENTE',
    'MENQUE',      'MAYQUE',    'MENOS',
    'DIFERENTE', 'MODULO',
    'DECIMAL',     'ENTERO',    'CADENADOBLE',
    'CADENASIMPLE', 'ID',        'MENIGUAL',
    'MAYIGUAL',    'PUNTO', 
    'CONCAT', 'BITWAND', 'BITWOR', 'BITWXOR',
    'BITWNOT', 'BITWSHIFTL', 'BITWSHIFTR', 'CSIMPLE',
    'CADDOLAR', 'PTIGUAL', 'DOLAR'
] + list(reservadas.values())

# Tokens
t_PUNTO = r'\.'
t_COMA = r','
t_PTCOMA = r';'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_IGUAL = r'='
t_MAS = r'\+'
t_MENOS = r'-'
t_ASTERISCO = r'\*'
t_DIVIDIDO = r'/'
t_EXPONENTE = r'\^'
t_MENQUE = r'<'
t_MAYQUE = r'>'
t_MENIGUAL = r'<='
t_MAYIGUAL = r'>='
t_DIFERENTE = r'<>'
t_MODULO = r'\%'
t_BITWOR = r'\|'
t_CONCAT = r'\|\|'
t_BITWAND = r'&'
t_BITWXOR = r'\#'
t_BITWNOT = r'~'
t_BITWSHIFTL = r'<<'
t_BITWSHIFTR = r'>>'
t_CSIMPLE = r'\''
t_CADDOLAR = r'\$\$'
t_PTIGUAL = r':=' 
t_DOLAR = r'\$'

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
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t


def t_CADENADOBLE(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_CADENASIMPLE(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
    return t


# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // --
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    Errores.append(Error('-----', EType.LEXICO, "   Caracter desconocido '%s'" % t.value[0],t.lexer.lineno))
    t.lexer.skip(1)


# Analizador léxico
lexer = lex.lex()
# Asociación de operadores y precedencia
precedence = (

    ('left', 'CONCAT'),
    ('left', 'BITWOR'),
    ('left', 'BITWXOR'),
    ('left', 'BITWAND'),
    ('left', 'BITWSHIFTL', 'BITWSHIFTR'),
    ('left', 'BITWNOT'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'MENQUE', 'MAYQUE', 'MENIGUAL', 'MAYIGUAL', 'IGUAL', 'DIFERENTE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'ASTERISCO', 'DIVIDIDO', 'MODULO'),
    ('left', 'EXPONENTE'),
    ('right', 'UMENOS')
)

###################################### Definición de la gramática #######################################
def p_init(t):
    'init             : instrucciones'
    t[0] = Nodo('RAIZ','',t[1],t.lexer.lineno)

def p_lista_instrucciones(t):
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_salida_instrucciones(t):
    'instrucciones    : instruccion'
    t[0] = [t[1]]

def p_instruccion(t):
    '''instruccion    : plsql_instr
                      | llamadafunciones
                      | llamadaprocedimiento
                      | dropfunction
                      | dropprocedure'''
    t[0] = t[1]

def p_dropFunction1(t):
    'dropfunction    :   DROP FUNCTION ID'
    g = '<dropfunction>    :   DROP FUNCTION ID'
    t[0] = Nodo('DROP', t[3], [], 0,0, g)

def p_dropFunction2(t):
    'dropfunction    :   DROP FUNCTION IF EXISTS ID PTCOMA'
    g = '<dropfunction>    :   DROP FUNCTION IF EXISTS ID PTCOMA'
    t[0] = Nodo('DROP', t[5], [], 0,0,g)

def p_dropProcedure1(t):
    'dropprocedure    :   DROP PROCEDURE ID PTCOMA'
    g = '<dropprocedure>    :   DROP PROCEDURE ID PTCOMA'
    t[0] = Nodo('DROP', t[3], [], 0,0,g)

def p_dropProcedure2(t):
    'dropprocedure    :   DROP PROCEDURE IF EXISTS ID PTCOMA'
    g = '<dropprocedure>    :   DROP PROCEDURE IF EXISTS ID PTCOMA'
    t[0] = Nodo('DROP', t[5], [], 0, 0, g)

def p_insert_sinorden(t):
    'insert_instr     : INSERT CADENADOBLE PTCOMA'
    g = '<insert_instr>     : INSERT CADENADOBLE PTCOMA'
    t[0] = Nodo('INSERT INTO',t[2],[], 0,0, g)

def p_update_sinwhere(t):
    'update_instr     : UPDATE CADENADOBLE PTCOMA'
    g = '<update_instr>     : UPDATE CADENADOBLE PTCOMA'
    t[0] = Nodo('UPDATE',t[2], [],0,0,g)

def p_delete_sinwhere(t):
    'delete_instr     : DELETE CADENADOBLE PTCOMA'
    g = '<delete_instr>     : DELETE CADENADOBLE PTCOMA'
    t[0] = Nodo('DELETE',t[2], [],0, 0, g)

def p_truncate_simple(t):
    'truncate_instr   : TRUNCATE CADENADOBLE PTCOMA'
    g = '<truncate_instr>   : TRUNCATE CADENADOBLE PTCOMA'
    t[0] = Nodo('TRUNCATE',t[2], [], 0, 0, g)

def p_drop_table(t):
    'drop_table : DROP CADENADOBLE PTCOMA'
    g = '<drop_table> : DROP CADENADOBLE PTCOMA'
    t[0] = Nodo('DROP',t[2], [],0,0,g)

def p_select_simple(t):
    'select_instr     : SELECT CADENADOBLE'
    g = '<select_instr>     : SELECT CADENADOBLE'
    t[0] = Nodo('SELECT',t[2],[], 0,0,g)

def p_inst_alter(t):
    'alter_instr      : ALTER CADENADOBLE PTCOMA'
    g = '<alter_instr>      : ALTER CADENADOBLE PTCOMA'
    t[0] = Nodo('ALTER',t[2],[],0,0,g)

def p_index0(t):
    'indexinstr   : CREATE INDEX CADENADOBLE PTCOMA'
    g = '<indexinstr>   : CREATE INDEX CADENADOBLE PTCOMA'
    t[0] = Nodo('CREATE INDEX',t[3],[], 0,0,g)


# ###################################### EXPRESIONES #########################################
# se utiliza misma gramatica del otro archivo
def p_lista_condicion(t):
    '''condiciones    : condiciones AND condicion
                      | condiciones OR condicion'''
    gramatica = '<condiciones> ::= <condiciones> \"'+ t[2]+'\" <condicion>'
    t[0] = Nodo('OPLOG', t[2], [t[1], t[3]], t.lexer.lineno, 0, gramatica)

def p_lista_condicion_salida1(t):
    'condiciones      : NOT PARIZQ condiciones PARDER'
    gramatica = '<condiciones> ::= NOT <condiciones>\n'
    t[0] = Nodo('OPLOG', 'NOT', [t[3]], t.lexer.lineno, 0, gramatica)

def p_lista_condicion_salida2(t):
    'condiciones      : NOT condiciones'
    gramatica = '<condiciones> ::= NOT <condiciones>\n'
    t[0] = Nodo('OPLOG', 'NOT', [t[2]], t.lexer.lineno, 0, gramatica)

def p_lista_condicion_salida(t):
    'condiciones      : condicion'
    t[1].gramatica = '<condiciones> ::= <condicion>\n' + t[1].gramatica
    t[0] = t[1]

# expresiones relacionales

def p_condicion(t):
    '''condicion      : expresion MENQUE expresion
                      | expresion MAYQUE expresion
                      | expresion MENIGUAL expresion
                      | expresion MAYIGUAL expresion
                      | expresion IGUAL expresion 
                      | expresion DIFERENTE expresion'''
    t[0] = getOpRelacional(t)

def p_condicion1(t):
    'condicion      : expresion'
    t[0] = t[1]

def p_expresion(t):
    '''expresion      : expresionaritmetica
                      | vallogico'''
    t[0] = t[1]

def p_expresion_2(t):
    'expresion        : select_instr'
    t[0] = t[1]

# expresiones aritmeticas

def p_expresion_aritmetica(t):
    '''expresionaritmetica  : expresionaritmetica MAS expresionaritmetica 
                            | expresionaritmetica MENOS expresionaritmetica 
                            | expresionaritmetica ASTERISCO expresionaritmetica 
                            | expresionaritmetica DIVIDIDO expresionaritmetica 
                            | expresionaritmetica MODULO expresionaritmetica 
                            | expresionaritmetica EXPONENTE expresionaritmetica'''
    gramatica = '<expresionaritmetica> ::= <expresionaritmetica> \"'+t[2]+'\" <expresionaritmetica>'
    t[0] = Nodo('OPARIT', t[2], [t[1], t[3]], t.lexer.lineno, 0, gramatica)

def p_expresion_aritmetica_2(t):
    'expresionaritmetica    : MENOS expresionaritmetica %prec UMENOS'
    gramatica = '<expresionaritmetica> ::= \"MENOS\" <expresionaritmetica> %prec \"UMENOS\"'
    t[0] = Nodo('NEGATIVO', '-', [t[2]], t.lexer.lineno, 0, gramatica)


def p_expresion_aritmetica_3(t):
    '''expresionaritmetica  : cualquiernumero
                            | cualquieridentificador
                            | cualquiercadena'''
    t[1].gramatica = '<expresionaritmetica> ::= <cualquiernumero>\n' + t[1].gramatica
    t[0] = t[1]

def p_expresion_aritmetica_4(t):
    'expresionaritmetica    : PARIZQ expresionaritmetica PARDER'
    t[2].gramatica = '<expresionaritmetica> ::= \"PARIZQ\" <expresionaritmetica> \"PARDER\"\n' + t[2].gramatica
    t[0] = t[2]

def p_expresion_aritmetica_5(t):
    '''expresionaritmetica    : funcion_matematica_ws
                              | funcion_matematica_s
                              | funcion_trigonometrica'''
    t[0] = t[1]
    

def p_cualquiernumero(t):
    '''cualquiernumero      : ENTERO
                            | DECIMAL'''
    t[0] = getValorNumerico(t)


def p_culquiercadena(t):
    '''cualquiercadena      : CADENASIMPLE
                            | CADENADOBLE'''
    t[0] = Nodo('CADENA', str(t[1]), [], t.lexer.lineno, 0)

def p_cualquiercadena1(t):
    '''cualquiercadena     : func_bin_strings_1
                           | func_bin_strings_2'''
    t[0] = t[1]

def p_culquieridentificador(t):
    '''cualquieridentificador    : ID
                                 | ID PUNTO ID'''
    t[0] = getIdentificador(t)

def p_valorlogico(t):
    '''vallogico    : FALSE
                    | TRUE'''
    gramatica = '<vallogico> ::= \"'+t[1]+'\"'
    t[0] = Nodo('LOGICO', t[1], [], t.lexer.lineno, 0, gramatica)

# --------------------------------- FUNCIONES MÁTEMÁTICAS ------------------------------------

# Select | Where
def p_funciones_matematicas1(t):
    '''funcion_matematica_ws    : ABS PARIZQ expresionaritmetica PARDER
                                | CBRT PARIZQ expresionaritmetica PARDER
                                | CEIL PARIZQ expresionaritmetica PARDER
                                | CEILING PARIZQ expresionaritmetica PARDER'''
    t[0] = Nodo('Matematica', t[1], [t[3]], t.lexer.lineno, 0)

# Select
def p_funciones_matematicas2(t):
    '''funcion_matematica_s     : DEGREES PARIZQ expresionaritmetica PARDER
                                | DIV PARIZQ expresionaritmetica COMA expresionaritmetica PARDER
                                | EXP PARIZQ expresionaritmetica PARDER
                                | FACTORIAL PARIZQ expresionaritmetica PARDER
                                | FLOOR PARIZQ expresionaritmetica PARDER
                                | GCD PARIZQ expresionaritmetica COMA expresionaritmetica PARDER
                                | LN PARIZQ expresionaritmetica PARDER
                                | LOG PARIZQ expresionaritmetica PARDER
                                | MOD PARIZQ expresionaritmetica COMA expresionaritmetica PARDER
                                | PI PARIZQ PARDER
                                | POWER PARIZQ expresionaritmetica COMA expresionaritmetica PARDER
                                | RADIANS PARIZQ expresionaritmetica PARDER
                                | ROUND PARIZQ expresionaritmetica PARDER
                                | SIGN PARIZQ expresionaritmetica PARDER
                                | SQRT PARIZQ expresionaritmetica PARDER
                                | WBUCKET PARIZQ explist PARDER
                                | TRUNC PARIZQ expresionaritmetica PARDER
                                | RANDOM PARIZQ PARDER'''
    t[0] = getFuncionMatematica(t)

def p_wbucket_exp(t):
    'explist  : expresionaritmetica COMA expresionaritmetica COMA expresionaritmetica COMA expresionaritmetica'
    t[0] = Nodo('VALORES','',[t[1],t[3],t[5],t[7]],t.lexer.lineno)
# ------------------------------- FUNCIONES TRIGONOMETRICAS ----------------------------------

def p_funciones_trigonometricas(t):
    '''funcion_trigonometrica  : ACOS PARIZQ expresionaritmetica PARDER
                               | ACOSD PARIZQ expresionaritmetica PARDER
                               | ASIN PARIZQ expresionaritmetica PARDER
                               | ASIND PARIZQ expresionaritmetica PARDER
                               | ATAN PARIZQ expresionaritmetica PARDER
                               | ATAND PARIZQ expresionaritmetica PARDER
                               | ATAN2 PARIZQ expresionaritmetica PARDER
                               | ATAN2D PARIZQ expresionaritmetica PARDER
                               | COS PARIZQ expresionaritmetica PARDER
                               | COSD PARIZQ expresionaritmetica PARDER
                               | COT PARIZQ expresionaritmetica PARDER
                               | COTD PARIZQ expresionaritmetica PARDER
                               | SIN PARIZQ expresionaritmetica PARDER
                               | SIND PARIZQ expresionaritmetica PARDER
                               | TAN PARIZQ expresionaritmetica PARDER
                               | TAND PARIZQ expresionaritmetica PARDER
                               | SINH PARIZQ expresionaritmetica PARDER
                               | COSH PARIZQ expresionaritmetica PARDER
                               | TANH PARIZQ expresionaritmetica PARDER
                               | ASINH PARIZQ expresionaritmetica PARDER
                               | ACOSH PARIZQ expresionaritmetica PARDER
                               | ATANH PARIZQ expresionaritmetica PARDER'''
    t[0] = Nodo('Trigonometrica', t[1], [t[3]], t.lexer.lineno)

# ---------------------------- FUNCIONES BINARIAS SOBRE CADENAS ------------------------------

def p_fbinarias_cadenas_1(t):
    'func_bin_strings_1    : LENGTH PARIZQ cualquiercadena PARDER '
    t[0] = Nodo('Binaria', 'length', [t[3]])

def p_fbinarias_cadenas_2(t):
    '''func_bin_strings_2   : SUBSTRING PARIZQ cualquiercadena COMA cualquiernumero COMA cualquiernumero PARDER 
                            | SUBSTR PARIZQ cualquiercadena COMA cualquiernumero COMA cualquiernumero PARDER
                            | TRIM PARIZQ cualquiercadena PARDER'''
    t[0] = getStringFunctionNode2(t)
                               


# ----------------------------------- EXTRACT, DATEPART, NOW-------------------------------------------
def p_extract(t):
    'extract_instr      :  EXTRACT PARIZQ valdate FROM TIMESTAMP CADENASIMPLE PARDER'

def p_valdate1(t):
    '''valdate   : YEAR
                 | HOUR
                 | MINUTE
                 | SECOND
                 | MONTH
                 | DAY'''
