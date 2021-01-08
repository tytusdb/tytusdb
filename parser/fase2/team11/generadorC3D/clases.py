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

def p_datepart(t):
    'datepart_instr    :  DATE_PART PARIZQ CADENASIMPLE COMA INTERVAL CADENASIMPLE PARDER'

def p_current(t):
    '''current     :  CURRENT_DATE
                   | CURRENT_TIME'''

def p_timestamp(t):
    'timestampnow     :  TIMESTAMP CADENASIMPLE'

def p_nowinstr(t):
    'nowinstr     :  NOW PARIZQ PARDER'

# ####################################### PL/psSQL ################################################

# ----- llamadas a procedimientos y funciones 

def p_llamasProcedimientos(t):
    'llamadaprocedimiento  : EXECUTE ID PARIZQ PARDER PTCOMA'
    g = '<llamadaprocedimiento>  : EXECUTE ID PARIZQ PARDER PTCOMA'
    t[0] = Nodo('EXECUTE', t[2], [], t.lexer.lineno, 0, g)

def p_llamasProcedimientos1(t):
    'llamadaprocedimiento  : EXECUTE ID PARIZQ listaexpresiones PARDER PTCOMA'
    g = '<llamadaprocedimiento>  : EXECUTE ID PARIZQ <listaexpresiones> PARDER PTCOMA'
    t[0] = Nodo('EXECUTE', t[2], t[4], t.lexer.lineno, 0, g)

def p_llamasFuncion(t):
    'llamadafunciones   : SELECT ID PARIZQ PARDER PTCOMA'
    g = '<llamadafunciones> : SELECT ID PARIZQ PARDER PTCOMA'
    t[0] = Nodo('SELECT FUNC', t[2], [], t.lexer.lineno, 0, g)

def p_llamasFuncion1(t):
    'llamadafunciones   : SELECT ID PARIZQ listaexpresiones PARDER PTCOMA'
    g = '<llamadafunciones> : SELECT ID PARIZQ <listaexpresiones> PARDER PTCOMA'
    t[0] = Nodo('SELECT FUNC', t[2], t[4], t.lexer.lineno, 0, g)


# ------- creacion de procedimientos y funciones 

def p_funciones_procedimientos(t):
    'plsql_instr   : CREATE procedfunct ID PARIZQ parametrosfunc PARDER tiporetorno cuerpofuncion'
    t[0] = getfuncion_procedimiento(t)

def p_procedurefunction(t):
    '''procedfunct  : PROCEDURE 
                    | FUNCTION'''
    t[0] = t[1]

def p_retornafuncion(t):
    '''tiporetorno  : RETURNS type_column1 AS
                    | LANGUAGE PLPGSQL AS
                    | AS
                    | empty'''
    t[0] = getretornofuncion(t)

def p_parametrosfunc(t):
    '''parametrosfunc  : listaparametrosfunc
                       | empty'''
    t[0] = t[1]

def p_listaparametrosfunc(t):
    '''listaparametrosfunc : listaparametrosfunc COMA parfunc
                            | parfunc'''
    t[0] = getparametrosfunc(t)

def p_parfunc(t):
    '''parfunc    : OUT ID type_column1
                  | INOUT ID type_column1
                  | ID type_column1
                  | type_column1'''
    t[0] = getparfunc(t)

def p_cuerpofuncion(t):
    'cuerpofuncion  : CADDOLAR declaraciones cuerpo CADDOLAR LANGUAGE PLPGSQL PTCOMA'
    t[0] = getCuerpoFuncion(t)

def p_cuerpofuncion1(t):
    'cuerpofuncion  : CADDOLAR declaraciones cuerpo CADDOLAR PTCOMA'
    t[0] = getCuerpoFuncion(t)

def p_declaraciones(t):
    'declaraciones   : DECLARE listadeclaraciones'
    g = '<declaraciones>   : DECLARE <listadeclaraciones>'
    t[0] = Nodo('DECLARE', '', t[2], t.lexer.lineno, 0, g)

def p_declaraciones1(t):
    'declaraciones   :  empty'
    t[0] = None

def p_listadeclaraciones(t):
    '''listadeclaraciones : listadeclaraciones declaracion
                          | declaracion'''
    t[0] = getlistadeclaraciones(t)

def p_declaracion(t):
    '''declaracion : ID constantintr type_column1 notnullinst asignavalor PTCOMA'''
    t[0] = getdeclaraciones(t)

def p_declaracion1(t):
    '''declaracion : ID ALIAS1 FOR DOLAR ENTERO PTCOMA
                   | ID ALIAS1 FOR ID PTCOMA'''
    t[0] = getdeclaraciones1(t)

def p_declaracion2(t):
    '''declaracion : ID cualquieridentificador MODULO TYPE PTCOMA'''
    t[0] = getdeclaraciones2(t)

def p_declaracion3(t):
    '''declaracion : ID cualquieridentificador MODULO ROWTYPE PTCOMA'''
    t[0] = getdeclaraciones2(t)

def p_constantintr(t):
    '''constantintr : CONSTANT
                    | empty'''
    t[0] = getconstant(t)

def p_notnullinst(t):
    '''notnullinst  : NOT NULL
                    | empty'''
    t[0] = getnotnull(t)

def p_asignavalor(t):
    '''asignavalor      : DEFAULT expresion
                        | PTIGUAL expresion
                        | IGUAL expresion
                        | empty'''
    t[0] = getasignavalor(t)

def p_cuerpo(t):
    'cuerpo     : BEGIN instrlistabloque END PTCOMA'
    t[0] = getcuerpo(t)

def p_insrtlistabloque(t):
    '''instrlistabloque : listabloque
                        | empty'''
    t[0] = getinstlistabloque(t)

def p_listabloque(t):
    '''listabloque : listabloque bloque
                   | bloque'''
    t[0] = getlistabloque(t)

def p_bloque(t):
    '''bloque       : raisenotice
                    | asignacionbloque
                    | subbloque
                    | returnbloque
                    | instrexecute
                    | getdiagnostic
                    | instrnull
                    | instrif
                    | instrcase
                    | commitinstr
                    | rollbackinstr
                    | insert_instr
                    | update_instr
                    | alter_instr
                    | drop_table   
                    | delete_instr
                    | truncate_instr
                    | indexinstr'''
    t[0] = t[1]

def p_commit(t):
    'commitinstr : COMMIT PTCOMA'
    t[0] = Nodo('COMMIT', '', [], t.lexer.lineno)

def p_rollback(t):
    'rollbackinstr : ROLLBACK PTCOMA'
    t[0] = Nodo('ROLLBACK', '', [], t.lexer.lineno)

def p_raisenotice(t):
    '''raisenotice   : RAISE NOTICE CADENASIMPLE COMA ID PTCOMA
                     | RAISE NOTICE CADENASIMPLE PTCOMA'''
    t[0] = getraisenotice(t)

def p_asignacionbloque(t):
    'asignacionbloque : ID IGUAL expresion PTCOMA'
    t[0] = getasignacionbloque(t)

def p_asignacionbloque1(t):
    'asignacionbloque : ID PTIGUAL expresion PTCOMA'
    t[0] = getasignacionbloque(t)

def p_return(t):
    'returnbloque : RETURN condicion PTCOMA'
    g = '<returnbloque> : RETURN <condicion> PTCOMA'
    t[0] = Nodo('RETURN', '', [t[2]], t.lexer.lineno, 0, g)

def p_return2(t):
    'returnbloque : RETURN QUERY select_instr PTCOMA'
    g = '<returnbloque> : RETURN QUERY <select_instr> PTCOMA'
    t[0] = Nodo('RETURN QUERY', '', [t[3]], t.lexer.lineno, 0, g)

def p_return3(t):
    'returnbloque : RETURN QUERY instrexecute PTCOMA'
    t[0] = Nodo('RETURN QUERY', '', [t[3]], t.lexer.lineno)

def p_return4(t):
    'returnbloque : RETURN PTCOMA'
    g = '<returnbloque> : RETURN PTCOMA'
    t[0] = Nodo('RETURN', '', [], t.lexer.lineno, 0, g)

def p_subloque(t):
    'subbloque : declaraciones cuerposub'
    t[0] = getsubbloque(t)

def p_cuerposub(t):
    'cuerposub : BEGIN listasubbloque END PTCOMA'
    t[0] = getcuerposubbloque(t)

def p_cuerposub1(t):
    'cuerposub : BEGIN empty END PTCOMA'
    t[0] = getcuerposubbloque(t)

def p_listasubbloque(t):
    '''listasubbloque : listasubbloque subbloque1
                      | subbloque1'''
    t[0] = getlistasubbloque(t)

def p_bloque1(t):
    '''subbloque1   : raisenotice1
                    | asignacionbloque'''
    t[0] = t[1]

def p_raisenotice1(t):
    '''raisenotice1  : RAISE NOTICE CADENASIMPLE COMA ID PTCOMA
                     | RAISE NOTICE CADENASIMPLE COMA OUTERBLOCK PUNTO ID PTCOMA
                     | RAISE NOTICE CADENASIMPLE PTCOMA'''
    t[0] = getraisenoticesubbloque(t)

def p_type_column1(t):
    '''type_column1   : SMALLINT
                      | INTEGER
                      | BIGINT
                      | RDECIMAL
                      | RDECIMAL PARIZQ ENTERO COMA ENTERO PARDER
                      | NUMERIC
                      | NUMERIC PARIZQ ENTERO PARDER
                      | REAL
                      | FLOAT
                      | INT
                      | DOUBLE
                      | MONEY
                      | VARCHAR
                      | VARCHAR PARIZQ ENTERO PARDER
                      | CHARACTER VARYING PARIZQ ENTERO PARDER
                      | CHARACTER PARIZQ ENTERO PARDER
                      | CHAR 
                      | CHAR PARIZQ ENTERO PARDER
                      | TEXT
                      | TIMESTAMP 
                      | TIMESTAMP PARIZQ ENTERO PARDER
                      | DATE
                      | TIME
                      | BOOLEAN
                      | ID
                      | TIME PARIZQ ENTERO PARDER
                      | RECORD
                      | TABLE PARIZQ parametrosfunc PARDER'''
    t[0] = gettypecolumn(t)

# INSTRUCCION
def p_instrexecute(t):
    'instrexecute    : EXECUTE CSIMPLE select_instr CSIMPLE intotarget usingexpresion'
    t[0] = getinstrexecute(t)

def p_instrexecute1(t):
    'instrexecute    : EXECUTE FORMAT PARIZQ CSIMPLE select_instr CSIMPLE PARDER intotarget usingexpresion'
    t[0] = getinstrexecute1(t)

def p_intotarget(t):
    '''intotarget    : INTO ID
                    | empty'''
    t[0] = getintotarget(t)

def p_usingexpresion(t):
    '''usingexpresion  : USING listaexpresiones
                       | empty'''
    t[0] = getusingexpresion(t)

def p_listaexpresiones(t):
    '''listaexpresiones : listaexpresiones COMA expresion
                        | expresion'''
    t[0] = getlistexpresiones(t)

# INSTRUCCION 
def p_getdiagnostic(t):
    'getdiagnostic : GET DIAGNOSTICS ID IGUAL ID'
    n1 = Nodo('ID', t[3], [], t.lexer.lineno)
    n2 = Nodo('ID', t[5], [], t.lexer.lineno)
    t[0] = Nodo('GET DIAGNOSTICS', t[4], [n1, n2], t.lexer.lineno)

def p_getdiagnostic1(t):
    'getdiagnostic : GET DIAGNOSTICS ID PTIGUAL ID'
    n1 = Nodo('ID', t[3], [], t.lexer.lineno)
    n2 = Nodo('ID', t[5], [], t.lexer.lineno)
    t[0] = Nodo('GET DIAGNOSTICS', t[4], [n1, n2], t.lexer.lineno)

# INSTRUCCION 
def p_instrnull(t):
    'instrnull    : NULL PTCOMA'
    t[0] = Nodo('NULL', '', [], t.lexer.lineno)

# INSTRUCCION 
def p_instrif(t):
    'instrif    : IF condiciones THEN instrlistabloque END IF PTCOMA'
    t[0] = getinstrif(t)

def p_instrif1(t):
    'instrif    : IF condiciones THEN instrlistabloque ELSE instrlistabloque END IF PTCOMA'
    t[0] = getinstrif1(t)

def p_instrif2(t):
    'instrif    : IF condiciones THEN instrlistabloque instrelseif END IF PTCOMA'
    t[0] = getinstrif2(t)

def p_instrif3(t):
    'instrif    : IF condiciones THEN instrlistabloque instrelseif ELSE instrlistabloque END IF PTCOMA'
    t[0] = getinstrif3(t)

def p_elseif(t):
    '''instrelseif : instrelseif in_elseif
                    | in_elseif'''
    t[0] = getinstrelseif(t)

def p_inelseif(t):
    'in_elseif : ELSIF condiciones THEN instrlistabloque'
    g = '<in_elseif> : ELSIF <condiciones> THEN <instrlistabloque>'
    childs = [Nodo('CONDICIONES', '', [t[2]], t.lexer.lineno)]
    if t[4] != None:
       childs.append(Nodo('THEN', '', t[4], t.lexer.lineno))
    t[0] =  Nodo('ELSIF', '', childs, t.lexer.lineno, 0, g)


# INSTRUCCION 
def p_instrcase(t):
    'instrcase : CASE expresion listawhen1 elsecase END CASE PTCOMA'
    t[0] = getinstrcase(t)

def p_elsecase(t):
    'elsecase : ELSE instrlistabloque'
    t[0] = Nodo('ELSE', '', t[2], t.lexer.lineno)

def p_elsecase1(t):
    'elsecase : empty'

def p_listawhen1(t):
    '''listawhen1  : listawhen1 when1
                   | when1'''
    t[0] = getlistawhen1(t)

def p_when1(t):
    'when1  : WHEN listaexpresiones THEN instrlistabloque'
    t[0] = getwhen1(t)

# INSTRUCCION 
def p_instrcase2(t):
    'instrcase : CASE listawhen2 elsecase END CASE PTCOMA'
    t[0] = getinstrcase2(t)

def p_listawhen2(t):
    '''listawhen2  : listawhen2 when2
                   | when2'''
    t[0] = getlistawhen1(t)

def p_when2(t):
    'when2  : WHEN ID BETWEEN ENTERO AND ENTERO THEN instrlistabloque'
    t[0] = getwhen21(t)

def p_when3(t):
    'when2  : WHEN condiciones THEN instrlistabloque'
    t[0] = getwhen22(t)

# Epsilon -------------------------------------------------------------------------------------
def p_empty(t):
    'empty            : '
    pass

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)
    Errores.append(Error('42601', EType.SINTACTICO, 'syntax_error', t.lexer.lineno))



## ################## Se genera AST de procedimiento y se traduce a 3d #########################
parser = yacc.yacc()
def parse(input) :

    entradaPL = obtenerSentenciasPL_SQL(input)
    if entradaPL != '':
        raiz = parser.parse(entradaPL)
        graficarAST(raiz)
        global C3Direcciones, contadorTemp
        gen3d = TraducirProcedimientos(raiz, C3Direcciones, contadorTemp)
        gen3d.traducir()
        gen3d.generateProYFunc()
        gen3d.crearReporte()


## #######################    Se separan sentencia SQL y PL/SQL    ############################
def obtenerSentenciasPL_SQL(input):
    global C3Direcciones
    input = input.strip()
    input = input.replace('\n', ' ')
    input = input.replace('\t', ' ')
    input = input[:-1]

    instrucciones = input.split(";")
    bandera = 0
    codigoPL = ''

    for instr in instrucciones:
        if bandera == 0:
            if 'create function' in instr.lower() or 'create procedure' in instr.lower():
                bandera = 1
                obtenerNombreFuncion(instr)
                instr = reestructurarPL(instr)
                codigoPL += instr + ';'
            elif 'drop function' in instr.lower() or 'drop procedure' in instr.lower():
                codigoPL += instr + ';'
                valores = instr.split()
                i = len(valores) -1
                cd3 ='\tglobals()[\''+ valores[i] + '\'] = 0'
                C3Direcciones.append(cd3)
            else:
                if 'execute' in instr.lower() or 'select1' in instr.lower():
                    guardarEn3dLlamada(instr)
                else: 
                    guardarEn3dSQL(instr)
        else:
            if instr.endswith("plpgsql") or instr.endswith("$$"):
                bandera = 0
            instr = reestructurarPL(instr)
            codigoPL += instr + ';'
    return codigoPL

def guardarEn3dSQL(instr):
    instr = instr.strip()
    #instr = instr.replace('\'', '\\\'')
    instr = buscarFuncionENSQL(instr)
    cd3 ='\tt'+str(contadorTemp) +' = \"' + instr +';\"'
    C3Direcciones.append(cd3) 
    cd3 = '\tpila = [t'+str(contadorTemp)+']'
    C3Direcciones.append(cd3) 
    cd3 = '\tfuncionIntermedia()'
    C3Direcciones.append(cd3) 
    incremetarTemp()

def guardarEn3dLlamada(instr):
    tipo = instr
    instr = instr.strip()
    instr = instr[8:]
    cd3 = '\t'+instr
    if 'select1' in tipo.lower():
        cd3 = '\tprint('+instr+')'
    C3Direcciones.append(cd3)

def reestructurarPL(instr):
    if 'insert ' in instr.lower():
        c = re.split('insert into|INSERT INTO', instr)
        c[0] += 'insert \"insert into '+ c[1] + ';\"'
        instr = c[0]
    elif 'update ' in instr.lower(): 
        c = re.split('update|UPDATE', instr)
        c[0] += 'update \"update '+ c[1] + ';\"'
        instr = c[0]
    elif 'delete ' in instr.lower():
        c = re.split('delete|DELETE', instr)
        c[0] += 'delete \"delete '+ c[1] + ';\"'
        instr = c[0]
    elif 'select ' in instr.lower():
        c = re.split('select|SELECT', instr)
        c[0] = c[0][:-1]
        c[0] += 'select \"select '+ c[1] 
        instr = c[0]
        instr = instr[:-1]
        instr = instr + ';\"'
    elif 'alter ' in instr.lower():
        c = re.split('alter|ALTER', instr)
        c[0] += 'alter \"alter '+ c[1] + ';\"'
        instr = c[0]
    elif 'create index ' in instr.lower():
        c = re.split('create index|CREATE INDEX', instr)
        c[0] += 'create index \"create index '+ c[1] + ';\"'
        instr = c[0]
    elif 'create unique index ' in instr.lower():
        c = re.split('create unique index|CREATE UNIQUE INDEX', instr)
        c[0] += 'create index \"create unique index '+ c[1] + ';\"'
        instr = c[0]
    return instr

def obtenerNombreFuncion(instr):
    cadena = instr
    cadena = cadena.split('(')
    cadena = cadena[0].split()
    procedimientos.append(cadena[2])

def buscarFuncionENSQL(instr):
    for name in procedimientos:
        if name in instr:
            inicio = instr.index(name)
            n = ''
            for i in range(inicio, len(instr)):
                n += instr[i]
                if instr[i] == ')':
                    break
            instr = instr.replace(n, '\"+str('+n+')+\"')
            break
    return instr

## ######################## metodo para incremtar indice de temporales #######################
def incremetarTemp():
    global contadorTemp
    contadorTemp += 1
    return contadorTemp



# ######################## GRAFICA UNICAMENTE EL AST DE FUNCIONES Y PROCEDIMIENTOS ############
c = 0
def recorrerNodos(nodo):
    global c
    c += 1
    codigo = ""
    padre = 'nodo'+str(c)
    codigo = padre + '[label = \"' + nodo.etiqueta + '\\n' + nodo.valor + '\"];\n'
    for hijo in nodo.hijos: 
        codigo += padre + '->' + 'nodo' + str(c+1) + '\n'
        codigo += recorrerNodos(hijo)
    return codigo

def graficarAST(raiz):

    file = open("astPL.dot", "w")
    file.write(
            'digraph G {\n'
            + 'rankdir=TB; '
            + 'node[fillcolor=\"darkturquoise:darkslategray2\", shape=record ,fontname = \"Berlin Sans FB\" ,style = filled]  \n'
            + 'edge[arrowhead=none]; \n'
        )
    file.write(recorrerNodos(raiz))
    file.write('}\n')
    file.close()
    render('dot','svg','astPL.dot')