# LISTA DE PALABRAS RESERVADAS
reservadas = {
    # Numeric Types
    'smallint': 'tSmallint',
    'integer': 'tInteger',
    'bigint': 'tBigint',
    'decimal': 'tDecimal',
    'numeric': 'tNumeric',
    'real': 'tReal',
    'double': 'tDouble',
    'precision': 'tPrecision',
    'money': 'tMoney',

    # Character types
    'character': 'tCharacter',
    'varying': 'tVarying',
    'varchar': 'tVarchar',
    'char': 'tChar',
    'text': 'tText',

    # Date/Time Types
    'timestamp': 'tTimestamp',
    'date': 'tDate',
    'time': 'tTime',
    'interval': 'tInterval',

    # Interval Type
    'year': 'tYear',
    'month': 'tMonth',
    'day': 'tDay',
    'hour': 'tHour',
    'minute': 'tMinute',
    'second': 'tSecond',
    'to': 'tTo',

    # Boolean Type
    'boolean': 'tBoolean',
    'false': 'tFalse',
    'true': 'tTrue',

    'create': 'create',
    'database': 'database',
    'or': 'or',
    'replace': 'replace',
    'if': 'if',

    'not': 'not',
    'exists': 'exists',
    'databases': 'databases',
    'drop': 'drop',
    'owner': 'owner',

    'mode': 'mode',
    'alter': 'alter',
    'show': 'show',
    'like': 'like',
    'insert': 'insert',

    'values': 'values',
    'null': 'null',
    'into': 'into',
    'from': 'from',

    'where': 'where',
    'as': 'as',
    'select': 'select',
    'update': 'tUpdate',
    'set': 'tSet',

    'delete': 'tDelete',
    'truncate': 'tTruncate',
    'table': 'table',
    'tables': 'tables',
    'between': 'tBetween',

    'rename': 'rename',
    'isNull': 'isNull',
    'in': 'tIn',
    'ilike': 'tILike',
    'similar': 'tSimilar',

    'is': 'tIs',
    'notnull': 'notNull',
    'and': 'And',
    'current_user': 'currentuser',
    'session_user': 'sessionuser',
    'type': 'ttype',
    'enum': 'tenum',
    'yes': 'yes',
    'no': 'no',
    'on': 'on',
    'off': 'off',

    # >inicia fl
    'inherits': 'tInherits',
    'default': 'tDefault',
    'primary': 'tPrimary',
    'foreign': 'tForeign',
    'key': 'tKey',
    'references': 'tReferences',
    'check': 'tCheck',
    'constraint': 'tConstraint',
    'unique': 'tUnique',
    'column': 'tColumn',
    'add': 'add',

    # >termina fl
    'no': 'no',
    'yes': 'yes',
    'on': 'on',
    'off': 'off',

    # TOKENS QUERIES
    'distinct': 'distinct',
    'group': 'group',
    'by': 'by',
    'having': 'having',
    # agregacion
    'count': 'count',
    'avg': 'avg',
    'max': 'max',
    'min': 'min',
    'sum': 'sum',
    # matematicas
    'abs': 'abs',
    'cbrt': 'cbrt',
    'ceil': 'ceil',
    'ceiling': 'ceiling',
    'degrees': 'degrees',
    'div': 'div',
    'exp': 'exp',
    'factorial': 'factorial',
    'floor': 'floor',
    'gcd': 'gcd',
    'ln': 'ln',
    'log': 'log',
    'mod': 'mod',
    'pi': 'pi',
    'power': 'power',
    'radians': 'radians',
    'round': 'round',
    'sign': 'sign',
    'sqrt': 'sqrt',
    'trunc': 'trunc',
    'width_bucket': 'width_bucket',
    'random': 'random',
    # trigonometricas
    'acos': 'acos',
    'acosd': 'acosd',
    'asin': 'asin',
    'asind': 'asind',
    'atan': 'atan',
    'atand': 'atand',
    'atan2': 'atan2',
    'atan2d': 'atan2d',
    'cos': 'cos',
    'cosd': 'cosd',
    'cot': 'cot',
    'cotd': 'cotd',
    'sin': 'sin',
    'sind': 'sind',
    'tan': 'tan',
    'tand': 'tand',
    'sinh': 'sinh',
    'cosh': 'cosh',
    'tanh': 'tanh',
    'asinh': 'asinh',
    'acosh': 'acosh',
    'atanh': 'atanh',
    # binary
    'length': 'length',
    'substring': 'substring',
    'trim': 'trim',
    'get_byte': 'get_byte',
    'md5': 'md5',
    'set_byte': 'set_byte',
    'sha256': 'sha256',
    'substr': 'substr',
    'convert': 'convert',
    'encode': 'encode',
    'decode': 'decode',

    # otros
    'all': 'all',
    'any': 'any',
    'some': 'some',

    # EXPRESSIONS
    'case': 'case',
    'when': 'when',
    'then': 'then',
    'else': 'else',
    'end': 'end',
    'greatest': 'greatest',
    'least': 'least',
    'limit': 'limit',
    'offset': 'offset',
    'union': 'union',
    'except': 'except',
    'intersect': 'intersect',

    # otros
    'date_part': 'date_part',
    'now': 'now',
    'current_date': 'current_date',
    'current_time': 'current_time',
    'extract': 'tExtract',
    'in': 'in',

    # nuevos -10
    'asc': 'asc',
    'desc': 'desc',
    'nulls': 'nulls',
    'first': 'first',
    'last': 'last',
    'order': 'order',
    'use': 'tuse',

    # otros
    'unknown': 'unknown',
    'bytea': 'bytea',
    # nuevos
    'return':  'treturn',
    'returns': 'returns',
    'declare': 'declare',
    'begin': 'begin',
    'function': 'function',
    'language': 'language',
    'for': 'tfor',
    'alias': 'talias',
    'do': 'do',
    'elsif':'elsif',
    'continue':'tcontinue',
    'exit':'texit',
    'raise':'raise',
    'notice':'notice',
    'rowtype':'rowtype',
    'procedure':'procedure',
    'next':'next',
    'out': 'out',
    'constant': 'constant',
    'query': 'tquery',
    'inout': 'inout', 
    'state': 'state',
    'lower': 'lower',
    'using': 'using',
    'index':'index',
    'hash': 'hash',
    'include': 'include',
    'execute':'execute'
}

# LISTA DE TOKENS
tokens = [
             'punto',
             'dosPts',
             'mas',

             'menos',
             'elevado',
             'multi',
             'divi',
             'modulo',

             'igual',
             'menor',
             'mayor',
             'menorIgual',
             'mayorIgual',

             'diferente',
             'id',
             'decimal',
             'entero',
             'cadena',
             'cadenaLike',

             'parAbre',
             'parCierra',
             'coma',
             'ptComa',
             # tks
             'barra',
             'barraDoble',
             'amp',
             'numeral',
             'virgulilla',
             'mayormayor',
             'menormenor',

             # TOKENS PARA EL RECONOCIMIENTO DE FECHA Y HORA
             'fecha',
             'hora',
             'fecha_hora',
             'intervaloc',
             'dobledolar',
             'val',
             'asig'
              
         ] + list(reservadas.values())

# DEFINICIÓN DE TOKENS
t_punto = r'\.'
t_asig = r':='
t_dosPts = r':'

t_mas = r'\+'
t_menos = r'-'
t_elevado = r'\^'
t_multi = r'\*'
t_divi = r'/'

t_modulo = r'%'
t_igual = r'='
t_menor = r'<'
t_mayor = r'>'
t_menorIgual = r'<='

t_mayorIgual = r'>='
t_diferente = r'<>'

t_parAbre = r'\('
t_parCierra = r'\)'
t_coma = r','
t_ptComa = r';'

# tk_queries
t_barra = r'\|'
t_barraDoble = r'\|\|'
t_amp = r'&'
t_numeral = r'\?'
t_virgulilla = r'~'
t_mayormayor = r'>>'
t_menormenor = r'<<'
t_dobledolar = r'\$\$'



# DEFINICIÓN DE UN NÚMERO DECIMAL
def t_decimal(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t


# DEFINICIÓN DE UN NÚMERO ENTERO
def t_entero(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


# DEFINICION PARA INTERVALO
def t_intervaloc(t):
    r'\'\d+[\s(Year|Years|Month|Months|day|days|hour|hours|minute|minutes|second|seconds)]+\''
    t.value = t.value[1:-1]
    return t

# DEFINICIÓN PARA LA HORA
def t_hora(t):
    r'\'[0-2]?[0-9]:[0-5]?[0-9]:[0-5]?[0-9]\''
    t.value = t.value[1:-1]
    return t


# DEFINICIÓN PARA LA FECHA
def t_fecha(t):
    r'\'[0-9]{4}-[0-1]?[0-9]-[0-3]?[0-9]\''
    t.value = t.value[1:-1]
    return t


# DEFINICIÓN PARA TIMESTAMP
def t_fecha_hora(t):
    r'\'([0-9]{4}-[0-1]?[0-9]-[0-3]?[0-9])(\s)([0-2]?[0-9]:[0-5]?[0-9]:[0-5]?[0-9])\''
    t.value = t.value[1:-1]
    return t


# DEFINICIÓN DE UNA CADENA PARA LIKE
def t_cadenaLike(t):
    r'\'%.*?%\'|\"%.*?%\"'
    t.value = t.value[2:-2]
    return t


# DEFINICIÓN DE UNA CADENA
def t_cadena(t):
    r'\'.*?\'|\".*?\"'
    t.value = t.value[1:-1]
    return t

# DEFINICIÓN DE UN ID
def t_val(t):
    r'\$\d+' 
    t.value = t.value[1:-1]
    return t


# DEFINICIÓN DE UN ID
def t_id(t):
    r'[a-zA-Z]([a-zA-Z]|[0-9]|_)*'
    t.type = reservadas.get(t.value.lower(), 'id')
    return t



# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


# DEFINICIÓN DE UN COMENTARIO SIMPLE
def t_COMENTARIO_SIMPLE(t):
    r'--.*'
    # t.lexer.lineno += 1  # Descartamos la linea desde aca


# IGNORAR COMENTARIOS SIMPLES
t_ignore_COMENTARIO_SIMPLE = r'\#.*'

# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# IMPORTACIÓN Y CREACIÓN DE LISTAS PARA GUARDAR LOS ERRORES
from Error import Error

errores_lexicos = []
errores_sintacticos = []


# HALLAR LA COLUMNA DEL TOKEN ESPECIFICADO
def find_column(token):  # Columna relativa a la fila
    global con
    line_start = con.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# FUNCIÓN DE ERROR PARA LOS ERRORES LÉXICOS
def t_error(t):
    col = find_column(t)
    # print("Caracter inválido '%s'" % t.value[0], " Línea: '%s'" % str(t.lineno))
    errores_lexicos.append(
        Error(t.value[0], 'Error Léxico', 'El caracter \'' + str(t.value[0]) + '\' no pertenece al lenguaje', col,
              t.lineno))
    t.lexer.skip(1)


# Construyendo el analizador léxico
import ply.lex as lex
import re

# DEFINIENDO LA PRECEDENCIA DE LOS OPERADORES
# ---------Modificado Edi------
precedence = (
    ('right', 'not'),
    ('left', 'And'),
    ('left', 'or','barraDoble'),
    ('left', 'diferente', 'igual', 'mayor', 'menor', 'menorIgual', 'mayorIgual'),
    ('left', 'punto'),
    ('right', 'umenos'),
    ('left', 'mas', 'menos'),
    ('left', 'elevado'),
    ('left', 'multi', 'divi', 'modulo'),
    ('nonassoc', 'parAbre', 'parCierra')
)
# ---------Modificado Edi---------
# <<<<<<<<<<<<<<<<<<<<<<<<<<< INICIO DE LAS PRODUCCIONES <<<<<<<<<<<<<<<<<<<<<<<<<<<<
from sentencias import *

from graphviz import Digraph


def p_init(t):
    'inicio :   sentencias'
    print("Lectura Finalizada")
    t[0] = t[1]


def p_sentencias_lista(t):
    'sentencias : sentencias sentencia'
    t[1].append(t[2])
    t[0] = t[1]


def p_sentencias_sentencia(t):
    'sentencias : sentencia'
    t[0] = [t[1]]


def p_sentencia(t):
    '''sentencia : CrearBase
                 | ShowBase
                 | AlterBase
                 | DropBase
                 | EnumType
                 | UpdateBase
                 | DeleteBase
                 | TruncateBase
                 | CREATE_TABLE
                 | SHOW_TABLES
                 | ALTER_TABLE
                 | DROP_TABLE
                 | INSERT
                 | QUERIES ptComa
                 | USEDB
                 | CREATE_FUNCION
                 | DROP_FUNCTION
                 | BLOCKDO 
                 | CREATE_INDEX
                 | DROP_INDEX
                 | ALTER_INDEX
                 | CALL ptComa
    '''
    t[0] = t[1]


def p_DropFuncion(t):
    ''' DROP_FUNCTION : drop function id ptComa '''
    t[0]=SDropFunction(t[3])

def p_ALTER_INDEX(t):
    ''' ALTER_INDEX : alter index id rename tTo id ptComa
                    | alter index if exists id rename tTo id ptComa


                    | alter index id id E ptComa 
                    | alter index if exists id id E ptComa 
    '''
    if len(t) == 7:
        t[0] = SAlterIndexColumna(t[3],t[4],t[5],False)
    elif len(t) == 8:
        t[0] = SAlterIndex(False,t[3],t[6])
    elif len(t) == 9:
        t[0] = SAlterIndexColumna(t[5],t[6],t[7],True)
    elif len(t) == 10:
        t[0] = SAlterIndex(True,t[5],t[8])


def p_DROP_INDEX(t):

    ''' DROP_INDEX  : drop index L_IDs ptComa
                    | drop index if exists L_IDs ptComa '''
    
    if len(t) == 5:
        t[0] = SDropIndex(False,t[3])
    elif len(t) == 7:
        t[0] = SDropIndex(True,t[5])


# <<<<<<<<<<<<<<<<<<<<<<<<<<< Edi Yovani Tomas  <<<<<<<<<<<<<<<<<<<<<<<<<<<<

def p_BLOCKDO(t):
    ''' BLOCKDO : do dobledolar BLOQUE dobledolar ptComa
    '''

def p_CrearFunciones(t):
    ''' CREATE_FUNCION :  TIPOFUNCION id parAbre L_PARAMETROS parCierra returns TIPO  as dobledolar BLOQUE dobledolar language id ptComa
                       |  TIPOFUNCION id parAbre  parCierra returns TIPO  as dobledolar BLOQUE dobledolar language id ptComa  
                       |  TIPOFUNCION id parAbre L_PARAMETROS parCierra returns TIPO  as dobledolar BLOQUE dobledolar  ptComa
                       |  TIPOFUNCION id parAbre  parCierra returns TIPO  as dobledolar BLOQUE dobledolar ptComa   
                       
    '''
    if len(t) == 15:
        t[0]= SCreateFunction(t[2], t[4], t[10], t[7], t[1]["rep"], t[1]["tipo"])
    elif len(t) == 14:
        t[0]= SCreateFunction(t[2], False, t[9], t[6], t[1]["rep"], t[1]["tipo"])
    elif len(t) == 13:
        t[0]= SCreateFunction(t[2], t[4], t[10], t[7], t[1]["rep"], t[1]["tipo"])
    elif len(t) == 12:
        t[0]= SCreateFunction(t[2], False, t[9], t[6], t[1]["rep"], t[1]["tipo"])

def p_CrearFunciones1(t):
    ''' CREATE_FUNCION : TIPOFUNCION id parAbre  parCierra as dobledolar BLOQUE dobledolar language id ptComa 
                        | TIPOFUNCION id parAbre L_PARAMETROS parCierra  as dobledolar BLOQUE dobledolar language id ptComa'''    
    if len(t)==12:
        t[0]=SCreateFunction(t[2],False,t[7],False,t[1]["rep"],t[1]["tipo"])
    else:
        t[0]=SCreateFunction(t[2],t[4],t[7],False,t[1]["rep"],t[1]["tipo"])

def p_TIPOFUNCION(t):
    ''' TIPOFUNCION :   create function
                      | create procedure
                      | create or replace function
                      | create or replace procedure  
    '''
    if len(t) == 3:
        t[0] = {"rep": False, "tipo":t[2]}
    elif len(t) == 5:
        t[0] = {"rep": True, "tipo":t[4]}


def p_BLOQUE(t):
    ''' BLOQUE  : DECLARE STATEMENT 
                | DECLARE
                | STATEMENT 
    '''
    if len(t) == 3:
        t[1].append(t[2])
        t[0]=t[1]
    else:
        t[0]= [t[1]]
       
def p_DECLARE(t):
    ''' DECLARE : declare BODYDECLARE
    '''
    t[0] = t[2]


def p_BODYDECLARE(t):

    ''' BODYDECLARE : BODYDECLARE DECLARATION
                    | DECLARATION
    '''
    if len(t) == 3:
        t[1].append(t[2])
        t[0]=t[1]
    else:
        t[0]= [t[1]]


def p_DECLARATIONP1(t):
    ''' DECLARATION :  NAME_CONSTANT TIPO ASIGNAR E ptComa
                    | NAME_CONSTANT ASIGNAR E ptComa
    '''
    if len(t)==5:
        t[0] = SDeclaracion(t[1]["id"],t[1]["constt"], None, False, t[2], t[3])
    else: 
        t[0] = SDeclaracion(t[1]["id"],t[1]["constt"], t[2], False, t[3], t[4])


def p_DECLARATION(t):
    ''' DECLARATION :  NAME_CONSTANT TIPO ptComa
                    |  NAME_CONSTANT TIPO not null ASIGNAR E ptComa 
                    |  NAME_CONSTANT talias tfor E ptComa 
                    |  NAME_CONSTANT TIPO not null ptComa 
       
            '''
    if len(t) == 4:
        t[0] = SDeclaracion(t[1]["id"],t[1]["constt"], t[2], False, False, False)
    elif len(t) == 8:
        t[0] = SDeclaracion(t[1]["id"],t[1]["constt"], t[2], True, t[5], t[6])
    elif len(t) == 6:
        if t[3].lower() == "for":
            t[0] = SDeclaracion(t[1]["id"],t[1]["constt"],t[2], False, False,t[4])
        if t[3].lower() == "not":
            t[0] = SDeclaracion(t[1]["id"],t[1]["constt"], t[2], True, False, False)

def p_DECLARATIONSTIPO(t):
    ''' DECLARATION :  NAME_CONSTANT ptComa
                    |  NAME_CONSTANT not null ASIGNAR E ptComa 
                    |  NAME_CONSTANT not null ptComa
    '''
    if len(t) == 3:
        t[0] = SDeclaracion(t[1]["id"],t[1]["constt"], None, False, False, False)
    elif len(t) == 7:
        t[0] = SDeclaracion(t[1]["id"],t[1]["constt"], None, True, t[4], t[5])
    elif len(t) == 5:
        t[0] = SDeclaracion(t[1]["id"],t[1]["constt"], None, True, False, False)



def p_DECLARATIONP0(t):
    ''' DECLARATION :  NAME_CONSTANT ACCESO modulo ttype ptComa
                    |  NAME_CONSTANT id modulo rowtype ptComa'''
    t[0] = SDeclaracionType(t[1]["id"],t[1]["constt"], t[2], t[4])



#  *******QQQQQQQQQ SE AGREGO MAS PRODUCCIONES EDI TOMAS 
def p_ASIGNACION1(t):
    '''   ASIGNACION : id asig  parAbre QUERY parCierra   ptComa
                     | id igual parAbre QUERY parCierra   ptComa
                     | id asig   QUERY  ptComa
                     | id igual  QUERY  ptComa
                             
    '''
    if len(t) == 5:
        t[0] = SAsignaQuery(t[1],t[3])
    elif len(t) == 7:
        t[0] = SAsignaQuery(t[1],t[4])


def p_DECLARATIONQUERY(t):
    ''' DECLARATION :  NAME_CONSTANT ASIGNAR QUERY ptComa
                    |  NAME_CONSTANT TIPO ASIGNAR QUERY ptComa
                    |  NAME_CONSTANT not null ASIGNAR QUERY ptComa
                    |  NAME_CONSTANT TIPO not null ASIGNAR QUERY ptComa 
                    |  NAME_CONSTANT not null ASIGNAR parAbre QUERY parCierra ptComa
                    |  NAME_CONSTANT TIPO not null ASIGNAR parAbre QUERY parCierra ptComa                     
    '''
    if len(t) == 5:
        t[0] = SDeclaracionQuery(t[1]["id"],t[1]["constt"], None, False, t[2], t[3])
    elif len(t) == 6:
        t[0] = SDeclaracionQuery(t[1]["id"],t[1]["constt"], t[2], False, t[3], t[4])
    elif len(t) == 7:
        t[0] = SDeclaracionQuery(t[1]["id"],t[1]["constt"], None, True, t[4], t[5])
    elif len(t) == 8:
        t[0] = SDeclaracionQuery(t[1]["id"],t[1]["constt"], t[2], True, t[5], t[6])
    elif len(t) == 9:
        t[0] = SDeclaracionQuery(t[1]["id"],t[1]["constt"], None, True, t[4], t[6])
    elif len(t) == 10:
        t[0] = SDeclaracionQuery(t[1]["id"],t[1]["constt"], t[2], True, t[5], t[7])

def p_DECLARATIONQUERY2(t):
    ''' DECLARATION :   NAME_CONSTANT ASIGNAR parAbre QUERY parCierra ptComa
                    |   NAME_CONSTANT TIPO ASIGNAR parAbre QUERY parCierra ptComa'''
    if len(t) == 7:
        t[0] = SDeclaracionQuery(t[1]["id"],t[1]["constt"], None, False, t[2], t[4])
    elif len(t) == 8:
        t[0] = SDeclaracionQuery(t[1]["id"],t[1]["constt"], t[2], False, t[3], t[5])


def p_DECLARATIONQUERY3(t):
    ''' DECLARATION :  NAME_CONSTANT talias tfor QUERY ptComa  
                    |  NAME_CONSTANT talias tfor parAbre QUERY parCierra ptComa 
    '''
    if len(t) == 6:
        t[0] = SDeclaracionQuery(t[1]["id"],t[1]["constt"], t[2], False, False, t[4])
    elif len(t) == 8:
        t[0] = SDeclaracionQuery(t[1]["id"],t[1]["constt"], t[2], False, False, t[5])
#*********************************************************************************************************************




def p_ACCESO(t):
    ''' ACCESO : ACCESO punto id
               |  id  '''
    if len(t) == 4:
        t[1].append(t[3])
        t[0] =t[1]
    else:
        t[0] = [t[1]]
 
def p_DECLARATION1(t):
    ''' ASIGNAR : asig
                 | igual
                 | tDefault              
    '''
    if t[1].lower()=="default":
        t[0] = True
    else:
        t[0] = False

def p_DECLARATION2(t):
    ''' NAME_CONSTANT : id
                      | id constant              
    '''
    if len(t) == 2:
        t[0] = {"constt": False, "id":t[1] }
    elif len(t) ==3:
        t[0] = {"constt": True, "id":t[1] }

def p_STATEMENT(t):
    ''' STATEMENT   : begin L_BLOCK end ptComa
                    | begin end ptComa
    '''
    t[0] = t[2]


def p_L_BLOCK(t):
    ''' L_BLOCK : L_BLOCK BLOCK 
                | BLOCK         
    '''
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]


def p_BLOCK(t):
    ''' BLOCK :   sentencias 
                | ASIGNACION
                | RETORNO
                | SENTENCIAS_CONTROL
                | DECLARACION_RAICENOTE
                | STATEMENT        
    '''
    t[0] = t[1]


def p_CALL(t):
    ''' CALL :  execute id parAbre LISTA_EXP parCierra 
              | execute id parAbre  parCierra     
    '''
    if len(t) == 6:
        t[0] = SCall(t[2],t[4])
    elif len(t) == 5:
        t[0] = SCall(t[2],False)

        
              
def p_CALL2(t):
    ''' CALL : id parAbre LISTA_EXP parCierra 
             | id parAbre parCierra     
    '''
    if len(t) == 5:
        t[0] = SCall(t[1],t[3])
    elif len(t) == 4:
        t[0] = SCall(t[1],False)


def p_ASIGNACION(t):
    '''   ASIGNACION : id asig E ptComa
                     | id igual E ptComa         
    '''
    t[0] = SAsignacion(t[1],t[3])



def p_LISTA_PARAMETROS(t):
    '''   L_PARAMETROS :   L_PARAMETROS coma PARAMETROS 
                       |   PARAMETROS      
    '''
    if len(t) == 4:
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_PARAMETROS(t):
    '''   PARAMETROS : id TIPO
                     | TIPO 
                     | out id TIPO 
                     | inout id TIPO  
    '''
    if len(t) == 4:
        t[0] = SParam(t[2],t[3],t[1])
    elif len(t) == 2:
        t[0] = SParam(False,t[1],False)
    elif len(t) == 3:
        t[0] = SParam(t[1],t[2],False)


def p_RETORNO(t):
    '''   RETORNO : treturn E ptComa
                  | treturn next E ptComa
                  | treturn tquery QUERY ptComa
                  | treturn ptComa
    '''
    if len(t) == 3:
        t[0] = SReturn(False,False,False)
    elif len(t) == 4:
        t[0] = SReturn(False,False,t[2])
    elif len(t) == 5:
        if t[2].lower=="next":
            t[0] = SReturn(True,False,t[3])
        elif t[2].lower=="query":
            t[0] = SReturn(False,t[3],False)

def p_RETORNO2(t):
    '''   RETORNO : treturn QUERY  ptComa
    '''
    t[0] = SReturn(False,t[2],False)


def p_CONTINUE(t):
    ''' CONTINUE : tcontinue EXPR_WHERE ptComa      
    '''

def p_EXIT(t):
    '''   EXIT : texit EXPR_WHERE ptComa    
               | texit ptComa     
               | texit id ptComa
               | texit id EXPR_WHERE ptComa
    '''


def p_OTROSTIPOS(t):
    '''   OTROSTIPOS :   tNumeric parAbre entero parCierra
                       | tVarchar 
                       | tChar    
    '''
    if len(t) == 2:
        t[0] = STipoDato(t[1], TipoDato.CHAR, None)
    elif len(t) == 5:
        t[0] = STipoDato(t[1], TipoDato.NUMERICO, t[3])

def p_SENTENCIAS_CONTROL(t):
    '''   SENTENCIAS_CONTROL : IF
                             | SEARCH_CASE
    '''
    t[0] = t[1]

#----------------IF--------------------------------------  
def p_IF(t):
    '''    IF : if  E then  L_BLOCK  end if ptComa
              | if  E then  L_BLOCK  ELSE
              | if  E then  L_BLOCK  ELSEIF  ELSE
              | if  E then  L_BLOCK  ELSEIF  end if ptComa
    '''
    if len(t) == 6:
        t[0]=SIf(t[2],t[4],False,t[5])
    elif len(t) == 7:
        t[0]=SIf(t[2],t[4],t[5],t[6])
    elif len(t) == 8:
        t[0]=SIf(t[2],t[4],False,False)
    elif len(t)==9:
        t[0]=SIf(t[2],t[4],t[5],False)

def p_ELSE(t):
    '''   ELSE : else L_BLOCK end if ptComa
    '''
    t[0] = t[2]

def p_ELSEIF(t):
    '''   ELSEIF : ELSEIF SINOSI
                 | SINOSI
    '''
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_SINOSI(t):
    '''   SINOSI :   elsif E then L_BLOCK
    '''
    t[0] = SSinosi(t[2],t[4])
    

def p_SEARCH_CASE(t):
    '''  SEARCH_CASE : case E L_CASE end case ptComa
                     | case E L_CASE SINO end case ptComa 
                     | case L_CASE end case ptComa
    '''
    if len(t)==7:
        t[0]=SSearchCase(t[2],t[3],False)
    elif len(t)==8:
        t[0]=SSearchCase(t[2],t[3],t[4])
    elif len(t)==6:
        t[0]=SSearchCase(False,t[2],False)
def p_SEARCH_CASE0(t):
    '''  SEARCH_CASE : case L_CASE SINO end case ptComa'''
    t[0]=SSearchCase(False,t[2],t[3])

def p_CUERPOCASE(t):
    '''   L_CASE :  L_CASE CASE   
                 | CASE
    '''
    if len(t)==3:
        t[1].append(t[2])
        t[0]=t[1]
    else:
        t[0]=[t[1]]

def p_CASE(t):
    '''   CASE :  when LISTA_EXP then L_BLOCK
                | when Condiciones then L_BLOCK  
    '''
    t[0]=SCasepl(t[2],t[4])
def p_SINO(t):
    '''   SINO : else L_BLOCK   
    '''
    t[0]=t[2]

def p_Raice_Note(t):
    ' DECLARACION_RAICENOTE : raise notice LISTA_EXP ptComa'
    t[0]=SRaise(t[3])

#------------------------INDEX

def p_index(t):
    ''' CREATE_INDEX :  create index id on id OPCION_INDEX ptComa
                    |   create tUnique index id on id OPCION_INDEX ptComa 
                    |   create index id on id OPCION_INDEX EXPR_WHERE ptComa
                    |	create tUnique index id on id OPCION_INDEX EXPR_WHERE ptComa
    '''

    if len(t) == 8:

        if str(t[2]).lower() == "index":
            if t[6]['parametro'] == "lista_id":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Ascendente',False,True,False,False,False)
            elif t[6]['parametro'] == "hash":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'Hash',t[6]['lista'],'Ascendente',False,True,False,False,False)
            elif t[6]['parametro'] == "asc":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Ascendente',False,True,False,False,False)
            elif t[6]['parametro'] == "first":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Ascendente',True,False,False,False,False)
            elif t[6]['parametro'] == "last":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Ascendente',False,True,False,False,False)
            elif t[6]['parametro'] == "desc":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Descendente',False,True,False,False,False)
            elif t[6]['parametro'] == "asc_first":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Ascendente',True,False,False,False,False)
            elif t[6]['parametro'] == "desc_first":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Descendente',True,False,False,False,False)
            elif t[6]['parametro'] == "asc_last":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Ascendente',False,True,False,False,False)
            elif t[6]['parametro'] == "desc_last":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Descendente',False,True,False,False,False)
            elif t[6]['parametro'] == "lower":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Ascendente',False,True,True,False,False)
    
    elif len(t) == 9:

        if str(t[2]).lower() == "index":
            if t[6]['parametro'] == "lista_id":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Ascendente',False,True,False,t[7],False)
            elif t[6]['parametro'] == "hash":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'Hash',t[6]['lista'],'Ascendente',False,True,False,t[7],False)
            elif t[6]['parametro'] == "asc":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Ascendente',False,True,False,t[7],False)
            elif t[6]['parametro'] == "first":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Ascendente',True,False,False,t[7],False)
            elif t[6]['parametro'] == "last":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Ascendente',False,True,False,t[7],False)
            elif t[6]['parametro'] == "desc":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Descendente',False,True,False,t[7],False)
            elif t[6]['parametro'] == "asc_first":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Ascendente',True,False,False,t[7],False)
            elif t[6]['parametro'] == "desc_first":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Descendente',True,False,False,t[7],False)
            elif t[6]['parametro'] == "asc_last":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Ascendente',False,True,False,t[7],False)
            elif t[6]['parametro'] == "desc_last":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Descendente',False,True,False,t[7],False)
            elif t[6]['parametro'] == "lower":
                t[0] = SCrearIndice(str(t[3]),str(t[5]),'B-tree',t[6]['lista'],'Ascendente',False,True,True,t[7],False)

        elif str(t[2]).lower() == "unique":
            if t[7]['parametro'] == "lista_id":
                t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Ascendente',False,True,False,False,True)
            elif t[7]['parametro'] == "hash":
                t[0] = SCrearIndice(str(t[4]),str(t[6]),'Hash',t[7]['lista'],'Ascendente',False,True,False,False,True)
            elif t[7]['parametro'] == "asc":
                t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Ascendente',False,True,False,False,True)
            elif t[7]['parametro'] == "first":
                t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Ascendente',True,False,False,False,True)
            elif t[7]['parametro'] == "last":
                t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Ascendente',False,True,False,False,True)
            elif t[7]['parametro'] == "desc":
                t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Descendente',False,True,False,False,True)
            elif t[7]['parametro'] == "asc_first":
                t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Ascendente',True,False,False,False,True)
            elif t[7]['parametro'] == "desc_first":
                t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Descendente',True,False,False,False,True)
            elif t[7]['parametro'] == "asc_last":
                t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Ascendente',False,True,False,False,True)
            elif t[7]['parametro'] == "desc_last":
                t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Descendente',False,True,False,False,True)
            elif t[7]['parametro'] == "lower":
                t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Ascendente',False,True,True,False,True)
    elif len(t) == 10:
        if t[7]['parametro'] == "lista_id":
            t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Ascendente',False,True,False,t[8],True)
        elif t[7]['parametro'] == "hash":
            t[0] = SCrearIndice(str(t[4]),str(t[6]),'Hash',t[7]['lista'],'Ascendente',False,True,False,t[8],True)
        elif t[7]['parametro'] == "asc":
            t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Ascendente',False,True,False,t[8],True)
        elif t[7]['parametro'] == "first":
            t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Ascendente',True,False,False,t[8],True)
        elif t[7]['parametro'] == "last":
            t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Ascendente',False,True,False,t[8],True)
        elif t[7]['parametro'] == "desc":
            t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Descendente',False,True,False,t[8],True)
        elif t[7]['parametro'] == "asc_first":
            t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Ascendente',True,False,False,t[8],True)
        elif t[7]['parametro'] == "desc_first":
            t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Descendente',True,False,False,t[8],True)
        elif t[7]['parametro'] == "asc_last":
            t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Ascendente',False,True,False,t[8],True)
        elif t[7]['parametro'] == "desc_last":
            t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Descendente',False,True,False,t[8],True)
        elif t[7]['parametro'] == "lower":
            t[0] = SCrearIndice(str(t[4]),str(t[6]),'B-tree',t[7]['lista'],'Ascendente',False,True,True,t[8],True)


def p_createIndex1(t):
    ''' OPCION_INDEX :  using hash parAbre id parCierra 
                     |  parAbre OPT_INDEX_PAR parCierra
                      '''

    if len(t) == 4:
        t[0] = t[2]
    elif len(t) == 6:   
        t[0] = {"parametro" : "hash","lista": [t[4]]}


def p_createIndex2(t):
    ' OPT_INDEX_PAR : L_IDs'
    t[0] = {"parametro":"lista_id","lista": t[1]}

def p_createIndex2_1(t):
    ''' OPT_INDEX_PAR   : id nulls FIRST_LAST
                        | id DESC_ASC nulls FIRST_LAST '''

    if len(t) == 4:
        t[0] = {"parametro":str(t[3]),"lista": [t[1]]}
    elif len(t) == 5:
        t[0] = {"parametro":str(t[2]) + "_" + str(t[4]),"lista": [t[1]]}

def p_createIndex2_3(t):
    ' OPT_INDEX_PAR : lower parAbre id parCierra '
    t[0] = {"parametro":"lower","lista": [t[3]]}


def p_first_last(t):
    ''' FIRST_LAST : first
                   | last '''
    t[0] = str(t[1]).lower()


def p_desc_asc(t):
    ''' DESC_ASC    : desc
                    | asc '''

    t[0] = str(t[1] ).lower()


def p_USEDB(t):
    ''' USEDB : tuse id ptComa'''
    t[0] = SUse(t[2])


# <<<<<<<<<<<<<<<<<<<<<<<<<<< HEIDY <<<<<<<<<<<<<<<<<<<<<<<<<<<<

def p_crearBase(t):
    '''CrearBase : create database E ptComa
                 | create database E owner igual E ptComa
                 | create database E mode igual entero ptComa
                 | create database E owner igual E mode igual entero ptComa
                 | create or replace database E ptComa
                 | create or replace database E owner igual E ptComa
                 | create or replace database E mode igual entero ptComa
                 | create or replace database E owner igual E mode igual entero ptComa
                 | create database if not exists E ptComa
                 | create database if not exists E owner igual E ptComa
                 | create database if not exists E mode igual entero ptComa
                 | create database if not exists E owner igual E mode igual entero ptComa'''
    # def __init__(self, owner, mode, replace, exists, id)
    if len(t) == 5:
        # primera produccion
        t[0] = SCrearBase(False, False, False, False, t[3])
        # agregar codigo de grafica
    elif len(t) == 8:
        if t[4].lower() == "mode":
            # tercera produccion
            t[0] = SCrearBase(False, t[6], False, False, t[3])
        elif t[4].lower() == "owner":
            print("entre aqui")
            # segunda produccion
            t[0] = SCrearBase(t[6], False, False, False, t[3])
        if t[4].lower() == "not":
            # novena produccion
            t[0] = SCrearBase(False, False, False, True, t[6])
    elif len(t) == 11:
        if t[4].lower() == "not":
            if t[7].lower() == "owner":
                # decima produccion
                t[0] = SCrearBase(t[9], False, False, True, t[6])
            elif t[7].lower() == "mode":
                # onceava produccion
                t[0] = SCrearBase(False, t[9], False, True, t[6])
        else:
            # cuarta produccion
            t[0] = SCrearBase(t[6], t[9], False, False, t[3])
    elif len(t) == 7:
        # quinta produccion
        t[0] = SCrearBase(False, False, True, False, t[5])
    elif len(t) == 10:
        if t[6].lower() == "mode":
            # septima produccion
            t[0] = SCrearBase(False, t[8], True, False, t[5])
        else:
            # sexta produccion
            t[0] = SCrearBase(t[8], False, True, False, t[5])
    elif len(t) == 13:
        # octava produccion
        t[0] = SCrearBase(t[8], t[11], True, False, t[5])
    elif len(t) == 14:
        # doceava produccion
        t[0] = SCrearBase(t[9], t[12], False, True, t[6])


def p_showBase(t):
    '''ShowBase : show databases ptComa
                | show databases like cadenaLike ptComa'''
    # def __init__(self,like,cadena):
    if len(t) == 4:
        t[0] = SShowBase(False, None)

    else:
        t[0] = SShowBase(True, t[4])


def p_AlterBase(t):
    '''AlterBase : alter database E rename tTo id ptComa
                 | alter database E owner tTo id ptComa
                 | alter database E owner tTo currentuser ptComa
                 | alter database E owner tTo sessionuser ptComa
    '''
    # def __init__(self, id, rename, owner, id):
    if t[4].lower() == "rename":
        t[0] = SAlterBase(t[3], True, False, t[6])
    else:
        t[0] = SAlterBase(t[3], False, True, t[6])


def p_DropBase(t):
    '''DropBase : drop database E ptComa
                | drop database if exists E ptComa'''
    if len(t) == 5:
        t[0] = SDropBase(False, t[3])
    else:
        t[0] = SDropBase(True, t[5])


def p_EnumType(t):
    'EnumType   : create ttype id as tenum parAbre LISTA_EXP parCierra ptComa'
    t[0] = STypeEnum(t[3], t[7])


# <<<<<<<<<<<<<<<<<<<<<<<<<<< HEIDY <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< ARIEL <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# PRODUCCIÓN PARA HACER UN UPDATE
def p_produccion0(t):
    ''' UpdateBase   : tUpdate id tSet L_ASIGN where CondicionBase ptComa'''
    if len(t)==5:
        t[0] = SUpdateBase(t[2], t[4], False)
    else:
        t[0] = SUpdateBase(t[2], t[4], t[6])


def p_produccion0_0(t):
    ''' UpdateBase   : tUpdate id tSet L_ASIGN ptComa '''
    t[0] = SUpdateBase(t[2], t[4], False)


# PRODUCCIÓN PARA HACER UN DELETE
def p_produccion0_1(t):
    ''' DeleteBase  : tDelete from id where CondicionBase ptComa '''
    t[0] = SDeleteBase(t[3], t[5])


def p_produccion0_2(t):
    ''' DeleteBase : tDelete from id ptComa'''
    t[0] = SDeleteBase(t[3], False)


#PRODUCCIÓN PARA LAS CONDICIONES DEL DELETE Y EL UPDATE
def p_produccion0_3(p):
    ''' CondicionBase   : CondicionBase Condiciones
                        | CondicionBase ORAND Condiciones
                        | ORAND Condiciones 
                        | Condiciones '''

    if len(p) == 2 :
        p[0] = p[1]
    elif len(p) == 3:
        print(str(p[1]))
        p[1].append(p[2])
        p[0] = [p[1]]
    elif len(p)==4:

        if p[2][0].lower() == 'and':
            p[0] = SOperacion(p[1],p[3],Logicas.AND)
        else:
            p[0] = SOperacion(p[1],p[3],Logicas.OR)

def p_produccion0_4(p):
    ''' Condiciones : E_FUNC 
                    | E_FUNC tIs distinct from E_FUNC
                    | E_FUNC tIs not distinct from E_FUNC
                    | substring parAbre E_FUNC coma E_FUNC coma E_FUNC parCierra igual E
                    | E_FUNC tIs tTrue
                    | E_FUNC tIs not tTrue 
                    | E_FUNC tIs tFalse
                    | E_FUNC tIs not tFalse
                    | E_FUNC tIs unknown
                    | E_FUNC tIs not unknown
                    | E_FUNC tIs null 
                    | E_FUNC tIs not null
                    | E_FUNC isNull
                    | E_FUNC notNull
                    | E_FUNC tILike cadenaLike
                    | E_FUNC like cadenaLike
                    | E_FUNC tSimilar tTo E_FUNC
                    | substr parAbre E_FUNC coma E_FUNC coma E_FUNC parCierra igual E '''


    if len(p) == 2:
        p[0] = p[1]

    elif len(p) == 3:

        if p[2].lower() == 'isnull':
            p[0] = SOperacion(p[1],SExpresion(None,Expresion.NULL),Relacionales.IGUAL)
        elif p[2].lower() == 'notnull':
            p[0] = SOperacion(p[1],SExpresion(None,Expresion.NULL),Relacionales.DIFERENTE)

    elif len(p) == 4:

        if p[2].lower() == 'like':
            p[0] = SLike(p[1],p[3])
        elif p[2].lower() == 'ilike':
            p[0] = SILike(p[1],p[3])
        elif p[3].lower() == 'true':
            p[0] = SOperacion(p[1],SExpresion(True,Expresion.BOOLEAN),Relacionales.IGUAL)
        elif p[3].lower() == 'false':
            p[0] = SOperacion(p[1],SExpresion(False,Expresion.BOOLEAN),Relacionales.IGUAL)
        elif p[3].lower() == 'unknown' or p[3].lower() == 'null':
            p[0] = SOperacion(p[1],SExpresion(None,Expresion.NULL),Relacionales.IGUAL)

    elif len(p) == 5:

        if p[2].lower() == 'similar':
            p[0] = SSimilar(p[1],p[4])
        elif p[4].lower() == 'true':
            p[0] = SOperacion(p[1],SExpresion(True,Expresion.BOOLEAN),Relacionales.DIFERENTE)
        elif p[4].lower() == 'false':
            p[0] = SOperacion(p[1],SExpresion(False,Expresion.BOOLEAN),Relacionales.DIFERENTE)
        elif p[4].lower() == 'unknown' or p[4].lower() == 'null':
            p[0] = SOperacion(p[1],SExpresion(None,Expresion.NULL),Relacionales.DIFERENTE)

    elif len(p) == 6:
        
        if p[3].lower() == 'distinct':
            p[0] = SOperacion(p[1],p[5],Relacionales.DIFERENTE)
    elif len(p) == 7:
        if p[4].lower() == 'distinct':
            p[0] = SOperacion(p[1],p[6],Relacionales.IGUAL)
    elif len(p) == 11:
        if p[1].lower() == 'substring' or p[1].lower() == 'substr':
            p[0] = SSubstring(p[3],p[5],p[7],p[10])



def p_produccion0_5(p):
    ''' Condiciones : exists parAbre QUERY parCierra
                | not exists parAbre QUERY parCierra
                | E_FUNC in parAbre QUERY parCierra 
                | E_FUNC not in parAbre QUERY parCierra
                | E_FUNC OPERATOR any parAbre QUERY parCierra
                | E_FUNC OPERATOR some parAbre QUERY parCierra
                | E_FUNC OPERATOR all parAbre QUERY parCierra '''


def p_produccion0_6(p):
    ''' Condiciones : E_FUNC tBetween E_FUNC 
                    | E_FUNC not tBetween E_FUNC '''

    print(len(p))
    if len(p) == 4:

        if hasattr(p[3].opIzq,'valor') and hasattr(p[3].opDer,'valor') :
            p[0] = SBetween(p[3].opIzq,p[1],p[3].opDer)
        elif hasattr(p[3].opIzq,'valor'):

            p[0] = SOperacion(SBetween(p[3].opIzq,p[1],p[3].opDer.opIzq),p[3].opDer.opDer,Logicas.OR)
        
        else:

            p[0] = SOperacion(SBetween(p[3].opIzq.opIzq,p[1],p[3].opIzq.opDer),p[3].opDer,Logicas.AND)

    elif len(p) == 5:

        if hasattr(p[4].opIzq,'valor') and hasattr(p[4].opDer,'valor') :

            p[0] = SNotBetween(p[4].opIzq,p[1],p[4].opDer)

        elif hasattr(p[4].opIzq,'valor'):

            p[0] = SOperacion(SNotBetween(p[4].opIzq,p[1],p[4].opDer.opIzq),p[4].opDer.opDer,Logicas.OR)
        
        else:

            p[0] = SOperacion(SNotBetween(p[4].opIzq.opIzq,p[1],p[4].opIzq.opDer),p[4].opDer,Logicas.AND)



# PRODUCCIÓN PARA HACER UN TRUNCATE
def p_produccion1_0(t):
    ''' TruncateBase    : tTruncate L_IDs ptComa'''
    t[0] = STruncateBase(t[2])


# PRODUCCIÓN PARA UNA LISTA DE IDENTIFICADORES
def p_produccion1_1(t):
    ''' L_IDs   : L_IDs coma id 
                | id '''
    if len(t) == 4:
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]


# PRODUCCIÓN PARA UNA LISTA DE ASIGNACIONES: id1 = 2, id2 = 3, id3, = 'Hola', etc...
def p_produccion1(t):
    ''' L_ASIGN : L_ASIGN coma id igual E
                | id igual E '''
    if len(t) == 6:
        val = SValSet(t[3], t[5])
        t[1].append(val)
        t[0] = t[1]
    else:
        val = SValSet(t[1], t[3])
        t[0] = [val]


# <<<<<<<<<<<<<<<<<<<<<<<<<<< ARIEL <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< FRANCISCO <<<<<<<<<<<<<<<<<<<<<<<<<<<<

def p_EXPR_CREATE_TABLE(t):
    '''CREATE_TABLE : create table id parAbre COLUMNS parCierra ptComa
                    | create table id parAbre COLUMNS parCierra tInherits parAbre id parCierra ptComa '''
    if len(t) == 8:
        t[0] = SCrearTabla(t[3], False, None, t[5])
    else:
        t[0] = SCrearTabla(t[3], True, t[9], t[5])


def p_EXPR_COLUMNS(t):
    '''COLUMNS : COLUMNS coma ASSIGNS
               | ASSIGNS
    '''
    if len(t) == 4:
        t[1].append(t[3])
        t[0] = t[1]
    elif len(t) == 2:
        t[0] = [t[1]]


def p_EXPR_ASSIGNS(t):
    '''ASSIGNS : id TIPO
               | id TIPO OPCIONALES
               | tCheck E
               | tConstraint id tCheck E
               | tUnique parAbre COLS parCierra
               | tPrimary tKey parAbre COLS parCierra
               | tConstraint id tForeign tKey parAbre COLS parCierra tReferences id parAbre COLS parCierra
               | tForeign tKey parAbre COLS parCierra tReferences id parAbre COLS parCierra'''
    if len(t) == 3:
        if t[1].lower == "check":
            t[0] = SColumnaCheck(None, t[2])
        else:
            t[0] = SColumna(t[1], t[2], None)
    elif len(t) == 4:
        t[0] = SColumna(t[1], t[2], t[3])
    elif len(t) == 5:
        if t[1].lower() == "constraint":
            t[0] = SColumnaCheck(t[2], t[4])
        else:
            t[0] = SColumnaUnique(t[3])
    elif len(t) == 6:
        t[0] = SColumnaPk(t[4])
    elif len(t) == 11:
        t[0] = SColumnaFk(t[7], None, t[4], t[9])
    else:
        t[0] = SColumnaFk(t[9], t[2], t[6], t[11])


def p_EXPR_OPCIONALES(t):
    '''OPCIONALES : OPCIONALES OPCION
                | OPCION '''
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]


def p_EXPR_OPCION(t):
    '''OPCION : tDefault E'''
    t[0] = SOpcionales(TipoOpcionales.DEFAULT, t[2], None)


def p_EXPR_OPCION1(t):
    '''OPCION : tPrimary tKey'''
    t[0] = SOpcionales(TipoOpcionales.PRIMARYKEY, None, None)


def p_EXPR_OPCION2(t):
    '''OPCION : not null'''
    t[0] = SOpcionales(TipoOpcionales.NOTNULL, None, None)


def p_EXPR_OPCION3(t):
    '''OPCION : null'''
    t[0] = SOpcionales(TipoOpcionales.NULL, None, None)


def p_EXPR_OPCION4(t):
    '''OPCION : tUnique'''
    t[0] = SOpcionales(TipoOpcionales.UNIQUE, None, None)


def p_EXPR_OPCION5(t):
    '''OPCION : tCheck E'''
    t[0] = SOpcionales(TipoOpcionales.CHECK, t[2], None)


def p_EXPR_OPCION6(t):
    ''' OPCION : tConstraint id tUnique '''
    t[0] = SOpcionales(TipoOpcionales.UNIQUE, None, t[2])


def p_EXPR_OPCION7(t):
    '''OPCION : tConstraint id tCheck E'''
    t[0] = SOpcionales(TipoOpcionales.CHECK, t[4], t[2])


def p_EXPR_COLS(t):
    '''COLS : COLS coma E
            | E '''

    if len(t) == 4:
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]


def p_EXPR_TIPO(t):
    '''TIPO : NUMERIC_TYPES
            | CHAR_TYPES
            | DATE_TYPES
            | BOOL_TYPES
            | id
            | OTROSTIPOS '''
            
    t[0] = t[1]

                    
def p_EXPR_NUMERIC_TYPES(t):
    '''NUMERIC_TYPES : tSmallint
                     | tInteger
                     | tBigint
                     | tDecimal
                     | tDecimal parAbre E coma E parCierra
                     | tNumeric
                     | tReal
                     | tDouble tPrecision
                     | tMoney'''
    t[0] = STipoDato(t[1], TipoDato.NUMERICO, None)


def p_EXPR_CHAR_TYPES(t):
    '''CHAR_TYPES : tVarchar parAbre entero parCierra
                  | tCharacter tVarying parAbre entero parCierra
                  | tCharacter parAbre entero parCierra
                  | tChar parAbre entero parCierra
                  | tText'''
    if len(t) == 2:
        t[0] = STipoDato(t[1], TipoDato.CHAR, None)
    elif len(t) == 5:
        t[0] = STipoDato(t[1], TipoDato.CHAR, t[3])
    else:
        t[0] = STipoDato(t[2], TipoDato.CHAR, t[4])


def p_EXPR_DATE_TYPES(t):
    '''DATE_TYPES : tDate
                  | tTimestamp 
                  | tTime 
                  | tInterval
                  | tInterval FIELDS'''
    t[0] = STipoDato(t[1], TipoDato.FECHA, None)


def p_EXPR_BOOL_TYPES(t):
    '''BOOL_TYPES : tBoolean'''
    t[0] = STipoDato(t[1], TipoDato.BOOLEAN, None)


def p_EXPR_FIELDS(t):
    '''FIELDS : tYear
              | tMonth
              | tDay
              | tHour
              | tMinute
              | tSecond'''
    t[0] = STipoDato(t[1], TipoDato.FIELDS, None)


def p_EXPR_SHOW_TABLE(t):
    '''SHOW_TABLES : show tables ptComa'''
    t[0] = SShowTable()


def p_EXPR_DROP_TABLE(t):
    '''DROP_TABLE : drop table id ptComa
    '''
    t[0] = SDropTable(t[3])


####@@@@@@@@@@@@@@@@@@@@@@@@@@ AQUI QUITE LA PENULTIMA PRODUCCION Y LA PUSE APARTE
def p_EXPR_ALTER_TABLE(t):
    '''ALTER_TABLE : alter table id rename tColumn id tTo id ptComa
                   | alter table id EXPR_ALTER
                   | alter table id LColumn ptComa
                   | alter table id add tConstraint id tCheck E ptComa
                   | alter table id add tCheck E ptComa
                   | alter table id add tConstraint id tUnique parAbre id parCierra ptComa
                   | alter table id add tConstraint id tForeign tKey parAbre COLS parCierra tReferences id parAbre COLS parCierra ptComa
                   | alter table id add tForeign tKey parAbre COLS parCierra tReferences id parAbre COLS parCierra ptComa
                   | alter table id drop tConstraint id ptComa
                   | alter table id rename tTo id ptComa
                   '''
    if len(t) == 10:
        if t[4].lower() == "rename":
            # primera produccion
            t[0] = SAlterTableRenameColumn(t[3], t[6], t[8])
        elif t[4].lower() == "add":
            t[0] = SAlterTableCheck(t[3], t[8], t[6])
    elif len(t) == 8:
        if t[4].lower() == "add":
            # cuarta produccion
            t[0] = SAlterTableCheck(t[3], t[6], None)
        elif t[4].lower() == "drop":
            t[0] = SAlterTableDrop(t[3], TipoAlterDrop.CONSTRAINT, t[6])
        elif t[4].lower() == "rename":
            t[0] = SAlterRenameTable(t[3], t[6])
    elif len(t) == 5:
        # segunda produccion
        t[0] = SAlterTable_AlterColumn(t[3], t[4])
    elif len(t) == 6:
        # tercera produccion
        t[0] = SAlterTableAddColumn(t[3], t[4])
    elif len(t) == 12:
        # quinta produccion
        t[0] = SAlterTableAddUnique(t[3], t[6], t[9])
    elif len(t) == 16:
        # sexta produccion
        t[0] = SAlterTableAddFK(t[3], t[11], None, t[8], t[13])
    else:
        t[0] = SAlterTableAddFK(t[3], t[13], t[6], t[10], t[15])


def p_EXPR_ALTER_TABLE1(t):
    '''ALTER_TABLE : alter table id LDColumn ptComa '''
    t[0] = SAlterTableDrop(t[3], TipoAlterDrop.COLUMN, t[4])


# @@@@@@@@@@ AQUI EMPIEZAN NUEVAS PRODUCCIONES
def p_LDropColumn(t):
    ''' LDColumn : LDColumn coma LDCol
                 | LDCol'''
    if len(t) == 4:
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]


def p_LDCol(t):
    ''' LDCol : drop tColumn id '''
    t[0] = SNAlterDrop(t[3])


def p_LAddColumn(t):
    ''' LColumn : LColumn coma LCol
                | LCol '''
    if len(t) == 4:
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]


def p_LCol(t):
    '''LCol : add tColumn id TIPO'''
    t[0] = SNAlterAdd(t[3], t[4])


# @@@@@@@@@@ AQUI TERMINAN NUEVAS PRODUCCIONES


def p_EXPR_ALTER(t):
    '''EXPR_ALTER : EXPR_ALTER coma alter tColumn id tSet not null ptComa
                  | EXPR_ALTER coma alter tColumn id ttype CHAR_TYPES ptComa
                  | alter tColumn id ttype CHAR_TYPES ptComa
                  | alter tColumn id tSet not null ptComa
                   '''
    if len(t) == 8:
        t[0] = [SAlterColumn(t[3], TipoAlterColumn.NOTNULL, None)]
    elif len(t) == 7:
        t[0] = [SAlterColumn(t[3], TipoAlterColumn.CAMBIOTIPO, t[5])]
    elif len(t) == 10:
        val = SAlterColumn(t[5], TipoAlterColumn.NOTNULL, None)
        t[1].append(val)
        t[0] = t[1]
    elif len(t) == 9:
        val = SAlterColumn(t[5], TipoAlterColumn.CAMBIOTIPO, t[7])
        t[1].append(val)
        t[0] = t[1]


# <<<<<<<<<<<<<<<<<<<<<<<<<<< FRANCISCO <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< EDI <<<<<<<<<<<<<<<<<<<<<<<<<<<<
def p_INSERT(p):
    ''' INSERT :  insert into id values parAbre LISTA_EXP parCierra ptComa
               |  insert into id parAbre LISTA_EXP parCierra values parAbre LISTA_EXP parCierra ptComa'''
    if len(p) == 9:
        p[0] = SInsertBase(p[3], None, p[6])
    else:
        p[0] = SInsertBase(p[3], p[5], p[9])


def p_LISTA_EXP(p):
    ''' LISTA_EXP :    LISTA_EXP coma E_FUNC
                    |  E_FUNC
    '''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_E(p):
    ''' E :  E or E
          |  E And       E
          |  E diferente  E
          |  E igual      E
          |  E mayor      E
          |  E menor      E
          |  E mayorIgual E
          |  E menorIgual E
          |  E mas        E
          |  E menos      E
          |  E multi      E
          |  E divi       E
          |  E modulo     E
          |  E elevado    E
          |  E punto      E
          |  E  barraDoble E
    '''
    if p[2].lower() == "or":
        p[0] = SOperacion(p[1], p[3], Logicas.OR)
    elif p[2].lower() == "and":
        p[0] = SOperacion(p[1], p[3], Logicas.AND)
    elif p[2] == "<>":
        p[0] = SOperacion(p[1], p[3], Relacionales.DIFERENTE)
    elif p[2] == "=":
        p[0] = SOperacion(p[1], p[3], Relacionales.IGUAL)
    elif p[2] == ">":
        p[0] = SOperacion(p[1], p[3], Relacionales.MAYOR_QUE)
    elif p[2] == "<":
        p[0] = SOperacion(p[1], p[3], Relacionales.MENOR_QUE)
    elif p[2] == ">=":
        p[0] = SOperacion(p[1], p[3], Relacionales.MAYORIGUAL_QUE)
    elif p[2] == "<=":
        p[0] = SOperacion(p[1], p[3], Relacionales.MENORIGUAL_QUE)
    elif p[2] == "+":
        p[0] = SOperacion(p[1], p[3], Aritmetica.MAS)
    elif p[2] == "-":
        p[0] = SOperacion(p[1], p[3], Aritmetica.MENOS)
    elif p[2] == "*":
        p[0] = SOperacion(p[1], p[3], Aritmetica.POR)
    elif p[2] == "/":
        p[0] = SOperacion(p[1], p[3], Aritmetica.DIVIDIDO)
    elif p[2] == "%":
        p[0] = SOperacion(p[1], p[3], Aritmetica.MODULO)
    elif p[2] == "**":
        p[0] = SOperacion(p[1], p[3], Aritmetica.POTENCIA)
    elif p[2] == ".":
        p[0] = SExpresion(str(p[1].valor) + "_" + str(p[3].valor),Expresion.ID )


def p_OpNot(p):
    ''' E : not E '''
    p[0] = SOperacion(p[2],None, Logicas.NOT)


def p_OpNegativo(p):
    ''' E : menos E %prec umenos '''
    p[0] = SExpresion(p[2], Expresion.NEGATIVO)


def p_OpParentesis(p):
    ''' E : parAbre E parCierra  '''
    p[0] = p[2]


def p_entero(p):
    ''' E : entero    
    '''
    p[0] = SExpresion(p[1], Expresion.ENTERO)


def p_decimal(p):
    ''' E : decimal    
    '''
    p[0] = SExpresion(p[1], Expresion.DECIMAL)


def p_cadena(p):
    ''' E : cadena    
    '''
    p[0] = SExpresion(p[1], Expresion.CADENA)


def p_id(p):
    ''' E : id    
    '''
    p[0] = SExpresion(p[1], Expresion.ID)


def p_fecha(p):
    ''' E : fecha    
    '''
    p[0] = SExpresion(p[1], Expresion.FECHA)


def p_hora(p):
    ''' E : hora    
    '''
    p[0] = SExpresion(p[1], Expresion.HORA)


def p_fecha_hora(p):
    ''' E : fecha_hora    
    '''
    p[0] = SExpresion(p[1], Expresion.FECHA_HORA)


def p_booleano(p):
    '''E  : yes
          | no
          | on
          | off
          | tTrue
          | tFalse
    '''
    p[0] = SExpresion(p[1], Expresion.BOOLEAN)

def p_interval(p):
    '''E : intervaloc '''
    p[0]=SExpresion(p[1],Expresion.INTERVALO)


def p_nulo(p):
    '''E : null '''
    p[0]=SExpresion(None,Expresion.NULL)

def p_val(p):
    '''E : val '''

def p_LLAMADAFUNCION(p):
    '''E : CALL '''
    p[0] = SExpresion(p[1],Expresion.LLAMADA)

# <<<<<<<<<<<<<<<<<<<<<<<<<<< EDI <<<<<<<<<<<<<<<<<<<<<<<<<<<<

######################################### QUERIES 

def p_QUERIES(p):
    '''QUERIES : QUERY union QUERY
               | QUERY intersect QUERY
               | QUERY except QUERY
               | QUERY'''
    if len(p) == 2:
        p[0] = Squeries(p[1], False, False)
    elif len(p) == 4:
        p[0] = Squeries(p[1], p[2], p[3])


def p_QUERY(p):
    '''QUERY : EXPR_SELECT 
             | EXPR_SELECT EXPR_FROM 
             | EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_HAVING EXPR_ORDERBY EXPR_LIMIT 
    '''
    # LEN 2 Y 3 y 7    #select, ffrom, where, groupby, having, orderby, limit
    if len(p) == 2:
        p[0] = SQuery(p[1], False, False, False, False, False, False)
    elif len(p) == 3:
        p[0] = SQuery(p[1], p[2], False, False, False, False, False)
    else:
        p[0] = SQuery(p[1], p[2], p[3], p[4], p[5], p[6], p[7])

    # LEN 4     #select, ffrom, where, groupby, having, orderby, limit


def p_QUERY_p4_1(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_ORDERBY'''
    p[0] = SQuery(p[1], p[2], False, False, False, p[3], False)


def p_QUERY_p4_2(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_LIMIT'''
    p[0] = SQuery(p[1], p[2], False, False, False, False, p[3])


def p_QUERY_p4_3(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE'''
    p[0] = SQuery(p[1], p[2], p[3], False, False, False, False)


def p_QUERY_p4_4(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_HAVING'''
    p[0] = SQuery(p[1], p[2], False, False, p[3], False, False)


def p_QUERY_p4_5(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY'''
    p[0] = SQuery(p[1], p[2], False, p[3], False, False, False)

    # LEN 5     #select, ffrom, where, groupby, having, orderby, limit


def p_QUERY_p5_1(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_ORDERBY EXPR_LIMIT'''
    p[0] = SQuery(p[1], p[2], False, False, False, p[3], p[4])


def p_QUERY_p5_2(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_ORDERBY '''
    p[0] = SQuery(p[1], p[2], p[3], False, False, p[4], False)


def p_QUERY_p5_3(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_LIMIT'''
    p[0] = SQuery(p[1], p[2], p[3], False, False, False, p[4])


def p_QUERY_p5_4(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY'''
    p[0] = SQuery(p[1], p[2], p[3], p[4], False, False, False)


def p_QUERY_p5_5(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_LIMIT'''
    p[0] = SQuery(p[1], p[2], False, p[3], False, False, p[4])


def p_QUERY_p5_6(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_ORDERBY '''
    p[0] = SQuery(p[1], p[2], False, p[3], False, p[4], False)


def p_QUERY_p5_7(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_HAVING'''
    p[0] = SQuery(p[1], p[2], False, p[3], p[4], False, False)


def p_QUERY_p5_8(p):
    '''QUERY :  EXPR_SELECT EXPR_FROM EXPR_HAVING EXPR_LIMIT'''
    p[0] = SQuery(p[1], p[2], False, False, p[3], False, p[4])


def p_QUERY_p5_9(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_HAVING EXPR_ORDERBY'''
    p[0] = SQuery(p[1], p[2], False, False, p[3], p[4], False)


def p_QUERY_p5_10(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_HAVING'''
    p[0] = SQuery(p[1], p[2], p[3], False, p[4], False, False)


# LEN 6     #select, ffrom, where, groupby, having, orderby, limit
def p_QUERY_p6_1(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_ORDERBY EXPR_LIMIT '''
    p[0] = SQuery(p[1], p[2], p[3], False, False, p[4], p[5])


def p_QUERY_p6_2(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_ORDERBY '''
    p[0] = SQuery(p[1], p[2], p[3], p[4], False, p[5], False)


def p_QUERY_p6_3(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_LIMIT '''
    p[0] = SQuery(p[1], p[2], p[3], p[4], False, False, p[5])


def p_QUERY_p6_4(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_HAVING '''
    p[0] = SQuery(p[1], p[2], p[3], p[4], p[5], False, False)


def p_QUERY_p6_5(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_ORDERBY EXPR_LIMIT '''
    p[0] = SQuery(p[1], p[2], False, p[3], False, p[4], p[5])


def p_QUERY_p6_6(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_HAVING EXPR_LIMIT '''
    p[0] = SQuery(p[1], p[2], False, p[3], p[4], False, p[5])


def p_QUERY_p6_7(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_HAVING EXPR_ORDERBY '''
    p[0] = SQuery(p[1], p[2], False, p[3], p[4], p[5], False)


def p_QUERY_p6_8(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_HAVING EXPR_ORDERBY EXPR_LIMIT'''
    p[0] = SQuery(p[1], p[2], False, False, p[5], p[4], p[5])


def p_QUERY_p6_9(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_HAVING EXPR_LIMIT'''
    p[0] = SQuery(p[1], p[2], p[3], False, p[4], False, p[5])


def p_QUERY_p6_10(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_HAVING EXPR_ORDERBY'''
    p[0] = SQuery(p[1], p[2], p[3], False, p[4], p[5], False)


# LEN 7     #select, ffrom, where, groupby, having, orderby, limit
def p_QUERY_p7_1(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_ORDERBY EXPR_LIMIT'''
    p[0] = SQuery(p[1], p[2], p[3], p[4], False, p[5], p[6])


def p_QUERY_p7_2(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_HAVING EXPR_LIMIT'''
    p[0] = SQuery(p[1], p[2], p[3], p[4], p[5], False, p[6])


def p_QUERY_p7_3(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_HAVING EXPR_ORDERBY'''
    p[0] = SQuery(p[1], p[2], p[3], p[4], p[5], p[6], False)


def p_QUERY_p7_4(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_HAVING EXPR_ORDERBY EXPR_LIMIT'''
    p[0] = SQuery(p[1], p[2], False, p[3], p[4], p[5], p[6])


def p_QUERY_p7_5(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_HAVING EXPR_ORDERBY EXPR_LIMIT'''
    p[0] = SQuery(p[1], p[2], p[3], False, p[4], p[5], p[6])


def p_EXPR_SELECT(p):
    '''EXPR_SELECT : select distinct EXPR_COLUMNAS
                   | select multi
                   '''
    if len(p) == 3:
        p[0] = SSelectCols(False, p[2])
    else:
        p[0] = SSelectCols(True, p[3])


def p_EXPR_SELECT_C(p):
    '''EXPR_SELECT : select EXPR_COLUMNAS'''
    p[0] = SSelectCols(False, p[2])


# todos los parametros de select - columnas
def p_EXPR_COLUMNAS(p):
    '''EXPR_COLUMNAS : EXPR_COLUMNAS coma EXPR_COLUMNAS1
                     | EXPR_COLUMNAS1'''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


# LEN 1 y 3
def p_EXPR_COLUMNAS1(p):
    '''EXPR_COLUMNAS1 : EXPR_AGREGACION
                     | EXPR_MATHS
                     | EXPR_TRIG
                     | EXPR_BINARIAS
                     | EXPR_EXTRA
                     | EXPR_FECHA
                     | EXPR_CASE
                     | E as E
                     | EXPR_AGREGACION as E
                     | EXPR_MATHS as E
                     | EXPR_TRIG as E 
                     | EXPR_BINARIAS as E
                     | EXPR_EXTRA as E
                     | EXPR_FECHA as E
                     | EXPR_CASE as E 
                     | E E
                     | EXPR_AGREGACION  E
                     | EXPR_MATHS E
                     | EXPR_TRIG E 
                     | EXPR_BINARIAS E
                     | EXPR_EXTRA E
                     | EXPR_FECHA E
                     | EXPR_CASE E 
                     | E punto multi'''
    if len(p) == 4:
        if p[3] == "*":
            p[0] = SColumnasMulti(p[1], p[3])
        else: 
            p[0] = SColumnasAsSelect(p[3], p[1])
    elif len(p) == 3:
        p[0] = SColumnasAsSelect(p[2], p[1])
    else:
        p[0] = SColumnasAsSelect(False, p[1])

def p_EXPR_COLUMNASLlamada(p):
    '''EXPR_COLUMNAS1 : E '''
    p[0] = SSelectLlamadaQuery(p[1])


def p_EXPR_COLUMNAS2(p):
    '''EXPR_COLUMNAS1 : parAbre QUERY parCierra
                     | parAbre QUERY parCierra E
                     | parAbre QUERY parCierra as E'''
    if len(p) == 4: 
        p[0] = SColQuery(False, p[2])
    if len(p) == 5:
        p[0] = SColQuery(p[4], p[2])
    if len(p) == 6:
        p[0] = SColQuery(p[5], p[2])

# LEN
def p_EXPR_COLUMNAS1_p1(p):  # error
    '''EXPR_COLUMNAS1 : substring parAbre E coma E coma E parCierra
                     | greatest parAbre E_LIST parCierra
                     | least parAbre E_LIST parCierra
                     | substring parAbre E coma E coma E parCierra as E
                     | substr parAbre E coma E coma E parCierra as E
                     | substr parAbre E coma E coma E parCierra 
                     | greatest parAbre E_LIST parCierra as E
                     | least parAbre E_LIST parCierra as E '''
    if p[1].lower() == "substring":
        if len(p) == 11:
            p[0] = SColumnasSubstr(p[10], p[5], p[7], p[3])
        else:
            p[0] = SColumnasSubstr(False, p[3], p[5], p[7])
    elif p[1].lower() == "substr":
        if len(p) == 11:
            p[0] = SColumnasSubstr(p[10],p[3], p[5], p[7])
        else:
            p[0] = SColumnasSubstr(False,p[3], p[5], p[7])
    elif p[1].lower() == "greatest":
        if len(p) == 7:
            p[0] = SColumnasGreatest(p[6], p[3])
        else:
            p[0] = SColumnasGreatest(False, p[3])
    elif p[1].lower() == "least":
        if len(p) == 7:
            p[0] = SColumnasLeast(p[6], p[3])
        else:
            p[0] = SColumnasLeast(False, p[3])


def p_EXPR_EXTRA(p):
    '''EXPR_EXTRA : tExtract parAbre FIELDS from tTimestamp E parCierra
                  | tExtract parAbre FIELDS from E parCierra'''
    if len(p) == 7:
        p[0] = SExtract(p[3], p[5])
    else:
        p[0] = SExtract2(p[3], p[5], p[6])


def p_EXPR_AGREGACION(p):
    '''EXPR_AGREGACION : count E
                       | avg E
                       | max E
                       | min E
                       | sum E
                       | count parAbre multi parCierra  
                       | avg parAbre multi parCierra
                       | max parAbre multi parCierra
                       | min parAbre multi parCierra
                       | sum parAbre multi parCierra'''

    if len(p) == 3:
        print("aca")
        p[0] = SFuncAgregacion(p[1], p[2])
    else:
        p[0] = SFuncAgregacion(p[1], p[3])


def p_EXPR_MATHS(p):
    '''EXPR_MATHS : abs E
                     | cbrt E
                     | ceil E
                     | ceiling E
                     | degrees E
                     | div parAbre E coma E parCierra
                     | exp E
                     | factorial E
                     | floor E
                     | gcd parAbre E coma E parCierra
                     | ln E
                     | log E
                     | mod parAbre E coma E parCierra
                     | pi parAbre parCierra
                     | power parAbre E coma E parCierra
                     | radians E
                     | round E
                     | round parAbre E coma E parCierra
                     | sign E
                     | sqrt E
                     | trunc E
                     | width_bucket parAbre LISTA_EXP parCierra
                     | random parAbre parCierra '''
    if len(p) == 3:
        p[0] = SFuncMath(p[1], p[2])
    elif len(p) == 4:
        p[0] = SFuncMathSimple(p[1])
    elif len(p) == 7:
        p[0] = SFuncMath2(p[1], p[3], p[5])
    elif len(p) == 5:
        p[0] = SFuncMathLista(p[1], p[3])


def p_EXPR_TRIG(p):
    '''EXPR_TRIG :  acos E 
                | acosd E 
                | asin E 
                | asind E 
                | atan E 
                | atand E 
                | atan2 parAbre E coma E parCierra
                | atan2d parAbre E coma E parCierra
                | cos E 
                | cosd E 
                | cot E 
                | cotd E 
                | sin E 
                | sind E 
                | tan E 
                | sinh E 
                | cosh E 
                | tanh E 
                | tand E 
                | asinh E 
                | acosh E 
                | atanh E'''
    if len(p) == 3:
        p[0] = SFuncTrig(p[1], p[2])
    elif len(p) == 7:
        p[0] = SFuncTrig2(p[1], p[3], p[5])


def p_EXPR_BINARIAS(p):
    '''EXPR_BINARIAS : length E
                     | trim E
                     | get_byte parAbre E dosPts dosPts bytea coma E parCierra 
                     | md5 E
                     | set_byte parAbre E dosPts dosPts bytea coma E coma E parCierra 
                     | sha256 E
                     | convert parAbre E as TIPO parCierra
                     | encode parAbre E dosPts dosPts bytea coma E parCierra 
                     | decode parAbre E coma E parCierra 
                     | barra E
                     | barraDoble E
                     | E amp E
                     | E barra E
                     | E numeral E
                     | virgulilla E
                     | E menormenor E
                     | E mayormayor E'''
    if len(p) == 3:
        p[0] = SFuncBinary(p[1], p[2])
    if len(p) == 4:
        p[0] = SFuncBinary2(p[2], p[1], p[3])
    elif len(p) == 7:
        p[0] = SFuncBinary3(p[1], p[3], p[4], p[5])
    elif len(p) == 10:
        p[0] = SFuncBinary2(p[1], p[3], p[8])
    elif len(p) == 12:
        p[0] = SFuncBinary4(p[1], p[3], p[8], p[10])


def p_EXPR_FECHA(p):
    '''EXPR_FECHA : date_part parAbre E coma DATE_TYPES E parCierra
                  | current_date
                  | current_time
                  | now parAbre parCierra
                  | DATE_TYPES E'''
    if len(p) == 2:
        p[0] = SSelectFunc(p[1])
    elif len(p) == 4:
        p[0] = SSelectFunc(p[1])
    elif len(p) == 3:
        p[0] = SFechaFunc(p[1], p[2])
    else:
        p[0] = SDatePart(p[1], p[3], p[5], p[6])


def p_EXPR_CASE(p):
    '''EXPR_CASE : case CASE_LIST end
                 | case CASE_LIST else E end'''
    if len(p) == 4:
        p[0] = SCase(p[2])
    else:
        p[0] = SCaseElse(p[2], p[4])


def p_CASE_LIST(p):
    '''CASE_LIST : CASE_LIST when E then E
                | when E then E'''
    if len(p) == 6:
        p[0] = SCaseList(p[3], p[5], p[1])
    else:
        p[0] = SCaseList(p[2], p[4], False)


def p_E_LIST(p):
    '''E_LIST : E_LIST coma E_LIST1
              | E_LIST1
              '''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_E_LIST1(p):
    '''E_LIST1 : E
               | now parAbre parCierra'''
    if len(p) == 4:
        p[0] = SSelectFunc(p[1])
    else:
        p[0] = [p[1]]


def p_EXPR_FROM(p):
    '''EXPR_FROM : from L_IDsAlias 
                 | from parAbre QUERY parCierra 
                 | from parAbre QUERY parCierra id
                 | from parAbre QUERY parCierra as id'''
    if len(p) == 3:
        p[0] = SFrom(p[2])

    elif len(p) == 5:
        p[0] = SFrom2(False, p[3])
    elif len(p) == 6:
        print("uno")
        p[0] = SFrom2(p[5], p[3])
    elif len(p) == 7:
        print("dos")
        p[0] = SFrom2(p[6], p[3])


def p_L_IDsAlias(p):
    '''L_IDsAlias : L_IDsAlias coma L_IDsAlias1
                  | L_IDsAlias1 '''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_L_IDsAlias_p1(p):  # fix
    '''L_IDsAlias1 : id id 
                    | id as id 
                    | id'''
    if len(p) == 4:
        p[0] = SAlias(p[1], p[3])
    elif len(p) == 3:
        p[0] = SAlias(p[1], p[2])
    else:
        p[0] = SAlias(p[1], False)


def p_EXPR_WHERE(p):
    '''EXPR_WHERE : where LIST_CONDS '''
    p[0] = SWhere(p[2])


def p_LIST_CONDS(p):
    '''LIST_CONDS : LIST_CONDS COND1
                  | LIST_CONDS ORAND COND1
                  | ORAND COND1
                  | COND1  '''
    if len(p) == 2 :
        p[0] = p[1]
    elif len(p) == 3:
        print(str(p[1]))
        p[1].append(p[2])
        p[0] = [p[1]]
    elif len(p)==4:

        if p[2][0].lower() == 'and':
            p[0] = SOperacion(p[1],p[3],Logicas.AND)
        else:
            p[0] = SOperacion(p[1],p[3],Logicas.OR)

def p_LIST_ORAND(p):
    '''ORAND : or
             | And
             | barraDoble
             '''
    p[0]= [p[1]]


def p_COND1(p):
    '''COND1    : E_FUNC 
                | E_FUNC tIs distinct from E_FUNC
                | E_FUNC tIs not distinct from E_FUNC
                | substring parAbre E_FUNC coma E_FUNC coma E_FUNC parCierra igual E
                | E_FUNC tIs tTrue
                | E_FUNC tIs not tTrue 
                | E_FUNC tIs tFalse
                | E_FUNC tIs not tFalse
                | E_FUNC tIs unknown
                | E_FUNC tIs not unknown
                | E_FUNC tIs null 
                | E_FUNC tIs not null
                | E_FUNC isNull
                | E_FUNC notNull
                | E_FUNC tILike cadenaLike
                | E_FUNC like cadenaLike
                | E_FUNC tSimilar tTo E_FUNC
                | substr parAbre E_FUNC coma E_FUNC coma E_FUNC parCierra igual E '''

    if len(p) == 2:
        p[0] = p[1]

    elif len(p) == 3:

        if p[2].lower() == 'isnull':
            p[0] = SOperacion(p[1],SExpresion(None,Expresion.NULL),Relacionales.IGUAL)
        elif p[2].lower() == 'notnull':
            p[0] = SOperacion(p[1],SExpresion(None,Expresion.NULL),Relacionales.DIFERENTE)

    elif len(p) == 4:

        if p[2].lower() == 'like':
            p[0] = SLike(p[1],p[3])
        elif p[2].lower() == 'ilike':
            p[0] = SILike(p[1],p[3])
        elif p[3].lower() == 'true':
            p[0] = SOperacion(p[1],SExpresion(True,Expresion.BOOLEAN),Relacionales.IGUAL)
        elif p[3].lower() == 'false':
            p[0] = SOperacion(p[1],SExpresion(False,Expresion.BOOLEAN),Relacionales.IGUAL)
        elif p[3].lower() == 'unknown' or p[3].lower() == 'null':
            p[0] = SOperacion(p[1],SExpresion(None,Expresion.NULL),Relacionales.IGUAL)

    elif len(p) == 5:

        if p[2].lower() == 'similar':
            p[0] = SSimilar(p[1],p[4])
        elif p[4].lower() == 'true':
            p[0] = SOperacion(p[1],SExpresion(True,Expresion.BOOLEAN),Relacionales.DIFERENTE)
        elif p[4].lower() == 'false':
            p[0] = SOperacion(p[1],SExpresion(False,Expresion.BOOLEAN),Relacionales.DIFERENTE)
        elif p[4].lower() == 'unknown' or p[4].lower() == 'null':
            p[0] = SOperacion(p[1],SExpresion(None,Expresion.NULL),Relacionales.DIFERENTE)

    elif len(p) == 6:
        
        if p[3].lower() == 'distinct':
            p[0] = SOperacion(p[1],p[5],Relacionales.DIFERENTE)
    elif len(p) == 7:
        if p[4].lower() == 'distinct':
            p[0] = SOperacion(p[1],p[6],Relacionales.IGUAL)
    elif len(p) == 11:
        if p[1].lower() == 'substring' or p[1].lower() == 'substr':
            p[0] = SSubstring(p[3],p[5],p[7],p[10])


def p_COND2(p):
    '''COND1 :  exists parAbre QUERY parCierra
                | not exists parAbre QUERY parCierra
                | E_FUNC in parAbre QUERY parCierra 
                | E_FUNC not in parAbre QUERY parCierra
                | E_FUNC OPERATOR any parAbre QUERY parCierra
                | E_FUNC OPERATOR some parAbre QUERY parCierra
                | E_FUNC OPERATOR all parAbre QUERY parCierra'''
    if len(p) == 5:
        p[0] = SExist(p[3])
    elif len(p) == 6:
        if p[2].lower() == "exists":
            p[0] = SNotExist(p[4])
        else:
            p[0] = SIn(p[1],p[4])
    elif len(p) == 7:
        if p[3].lower() == "in":
            p[0] = SNotIn(p[1],p[5])
        elif p[3].lower() == "all":
            p[0] = SAny(p[1], p[2], p[5])
        else:
            p[0] = SAll(p[1], p[2], p[5])


def p_COND3(p):
    '''COND1 :  E_FUNC tBetween E_FUNC 
                | E_FUNC not tBetween E_FUNC'''
    print(len(p))
    if len(p) == 4:

        if hasattr(p[3].opIzq,'valor') and hasattr(p[3].opDer,'valor') :
            p[0] = SBetween(p[3].opIzq,p[1],p[3].opDer)
        elif hasattr(p[3].opIzq,'valor'):

            p[0] = SOperacion(SBetween(p[3].opIzq,p[1],p[3].opDer.opIzq),p[3].opDer.opDer,Logicas.OR)
        
        else:

            p[0] = SOperacion(SBetween(p[3].opIzq.opIzq,p[1],p[3].opIzq.opDer),p[3].opDer,Logicas.AND)

    elif len(p) == 5:

        if hasattr(p[4].opIzq,'valor') and hasattr(p[4].opDer,'valor') :

            p[0] = SNotBetween(p[4].opIzq,p[1],p[4].opDer)

        elif hasattr(p[4].opIzq,'valor'):

            p[0] = SOperacion(SNotBetween(p[4].opIzq,p[1],p[4].opDer.opIzq),p[4].opDer.opDer,Logicas.OR)
        
        else:

            p[0] = SOperacion(SNotBetween(p[4].opIzq.opIzq,p[1],p[4].opIzq.opDer),p[4].opDer,Logicas.AND)



def p_OPERATOR(p):
    '''OPERATOR : igual
                | menor
                | mayor
                | menorIgual
                | mayorIgual
                | diferente'''
    p[0] = p[1]


def p_EXPR_GROUPBY(p):
    '''EXPR_GROUPBY : group by LISTA_EXP'''
    p[0] = SGroupBy(p[3])


def p_EXPR_HAVING(p):
    '''EXPR_HAVING : having E_FUNC '''
    p[0] = SHaving(p[2])


def p_EXPR_E_FUNC(p):
    '''E_FUNC : EXPR_AGREGACION
              | EXPR_MATHS
              | EXPR_TRIG
              | EXPR_BINARIAS
              | EXPR_FECHA
              | E '''
    p[0] = p[1]


def p_EXPR_ORDERBY(p):
    '''EXPR_ORDERBY : order by LIST_ORDERBY'''
    p[0] = sOrderBy(p[3])


def p_LIST_ORDERBY(p):
    '''LIST_ORDERBY : LIST_ORDERBY coma LIST_ORDERBY_1
                    | LIST_ORDERBY_1'''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_LIST_ORDERBY_p1(p):
    '''LIST_ORDERBY_1 : E asc
                    | E asc nulls first
                    | E asc nulls last
                    | E desc 
                    | E desc nulls first
                    | E desc nulls last
                    | E 
                    | E nulls first
                    | E nulls last'''

    if len(p) == 2:
        p[0] = SListOrderBy(False, False, p[1])
    elif len(p) == 3:
        p[0] = SListOrderBy(p[2], False, p[1])
    elif len(p) == 4:
        p[0] = SListOrderBy(False, p[3], p[1])
    elif len(p) == 5:
        p[0] = SListOrderBy(p[2], p[4], p[1])


def p_EXPR_LIMIT(p):
    '''EXPR_LIMIT : limit all
                  | limit all offset E'''
    if len(p) == 3:
        p[0] = SLimit(p[2], 0)
    else:
        p[0] = SLimit(p[2], p[4])


def p_EXPR_LIMIT2(p):
    '''EXPR_LIMIT : limit E
                  | limit E offset E'''
    if len(p) == 3:
        p[0] = SLimit(p[2], 0)
    else:
        p[0] = SLimit(p[2], p[4])


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN DE LAS PRODUCCIONES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# FUNCIÓN PARA EL MANEJO DE LOS ERRORES SINTÁCTICOS
def p_error(t):
    if not t: return#Fin del archivo
    col = find_column(t)
    # print("Error sintáctico en '%s'" % t.value, " Línea: '%s'" % str(t.lineno), " Columna: '%s'" % str(col) )
    errores_sintacticos.append(Error(t.value, 'Error Sintáctico', 'Símbolo no esperado', col, t.lineno))


# MÉTODO PARA GENERAR EL REPORTE DE ERRORES LÉXICOS
def erroresLexicos():
    print('Generando reporte de errores léxicos')
    __generar_reporte('Lexicos', errores_lexicos)


# MÉTODO PARA GENERAR EL REPORTE DE ERRORES SINTÁCTICOS
def erroresSintacticos():
    print('Generando reporte de errores sintácticos')
    __generar_reporte('Sintacticos', errores_sintacticos)


from datetime import datetime


# FUNCIÓN PARA GENERAR EL REPORTE DE ERRORES
def __generar_reporte(titulo, lista):
    if len(lista) > 0:
        ''' '''
        nodos = '''<
        <TABLE>        
        <TR>
            <TD colspan="5">REPORTE DE ERRORES %s <BR/> %s </TD>
        </TR>
        <TR>
            <TD>LEXEMA</TD>
            <TD>TIPO</TD>
            <TD>DESCRIPCION</TD>
            <TD>COLUMNA</TD>
            <TD>FILA</TD>
        </TR>                               \n''' % (titulo, str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        s = Digraph(titulo,
                    node_attr={'color': 'black', 'fillcolor': 'lightblue2', 'style': 'filled', 'shape': 'record'})
        for e in lista:
            nodos += '<TR> '
            nodos += (' \n\t<TD> ' + str(e.lexema).replace('{', '\{').replace('}', '\}').replace('<', '\<').replace('>',
                                                                                                                    '\>') + ' </TD> ')
            nodos += (' \n\t<TD> ' + str(e.tipo) + ' </TD> ')
            nodos += (' \n\t<TD> ' + str(e.descripcion).replace('{', '\{').replace('}', '\}').replace('<',
                                                                                                      '\<').replace('>',
                                                                                                                    '\>') + ' </TD> ')
            nodos += (' \n\t<TD> ' + str(e.columna) + ' </TD> ')
            nodos += (' \n\t<TD> ' + str(e.fila) + ' </TD> ')
            nodos += ' \n</TR> \n'
        nodos += '</TABLE>>'
        s.node('lbl', nodos)
        s.render('Reportes/' + titulo, format='png', view=True)


import ply.yacc as yacc


def parse(input):
    global con
    con = input

    lexer = lex.lex()
    lex.lex(reflags=re.IGNORECASE)
    parser = yacc.yacc()

    return parser.parse(input)
