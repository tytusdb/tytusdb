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
    'primarykey': 'primarykey',
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
    'iLike': 'tILike',
    'similar': 'tSimilar',

    'is': 'tIs',
    'notNull': 'notNull',
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
    'lcm': 'lcm',
    'ln': 'ln',
    'log': 'log',
    'log10': 'log10',
    'min_scale': 'min_scale',
    'mod': 'mod',
    'pi': 'pi',
    'power': 'power',
    'radians': 'radians',
    'round': 'round',
    'scale': 'scale',
    'sign': 'sign',
    'sqrt': 'sqrt',
    'trim_scale': 'trim_scale',
    'trunc': 'trunc',
    'width_bucket': 'width_bucket',
    'random': 'random',
    'setseed': 'setseed',
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
    'tand':'tand',
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
    'in': 'in'

    #nuevos -10
    ,'asc':'asc',
    'desc':'desc',
    'nulls':'nulls',
    'first':'first',
    'last':'last',
    'order':'order',
    'use': 'tuse',
    'unknown':'unknown',
    'bytea':'bytea'
 
}

# LISTA DE TOKENS
tokens = [
             'punto',
             'dosPts',
             'corcheI',
             'corcheD',
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

             #TOKENS PARA EL RECONOCIMIENTO DE FECHA Y HORA
             'fecha',
             'hora',
             'fecha_hora',
             'intervaloc',
             'notEqual'

         ] + list(reservadas.values())

# DEFINICIÓN DE TOKENS
t_punto = r'\.'
t_dosPts = r':'
t_corcheI = r'\['
t_corcheD = r'\]'

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
t_numeral = r'\#'
t_virgulilla = r'~'
t_mayormayor = r'>>'
t_menormenor = r'<<'
t_notEqual = r'!='


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
    r'\'[\d+\s(Year|Years|Month|Months|day|days|hour|hours|minute|minutes|second|seconds)]+\''
    return t


#DEFINICIÓN PARA LA HORA
def t_hora(t):
    r'\'[0-2]?[0-9]:[0-5]?[0-9]:[0-5]?[0-9]\''
    return t


#DEFINICIÓN PARA LA FECHA
def t_fecha(t):
    r'\'[0-9]{4}-[0-1]?[0-9]-[0-3]?[0-9]\''
    return t


#DEFINICIÓN PARA TIMESTAMP
def t_fecha_hora(t):
    r'\'([0-9]{4}-[0-1]?[0-9]-[0-3]?[0-9])(\s)([0-2]?[0-9]:[0-5]?[0-9]:[0-5]?[0-9])\''
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
    #t.lexer.lineno += 1  # Descartamos la linea desde aca


# IGNORAR COMENTARIOS SIMPLES
t_ignore_COMENTARIO_SIMPLE = r'\#.*'

# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    t.lexer.skip(1)

    print("Caracter inválido '%s'" % t.value[0], " Línea: '%s'" % str(t.lineno))




# Construyendo el analizador léxico
import ply.lex as lex
import re

lexer = lex.lex()
lex.lex(reflags=re.IGNORECASE)

# DEFINIENDO LA PRECEDENCIA DE LOS OPERADORES
# ---------Modificado Edi---------
# <<<<<<<<<<<<<<<<<<<<<<<<<<< INICIO DE LAS PRODUCCIONES <<<<<<<<<<<<<<<<<<<<<<<<<<<<
from sentencias import *


def p_init(t):
    'inicio :   sentencias'
    print(" LECTURA FINALIZADA*")
    
def p_sentencias_lista(t):
    '''sentencias :  sentencia sentencias 
                                         
    '''
def p_sentencias_sentencia(t):
    '''sentencias :  sentencia 
    '''

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
    '''

def p_USEDB(t):
    ''' USEDB : tuse id ptComa'''

    

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
    

def p_showBase(t):
    '''ShowBase : show databases ptComa
                | show databases like cadenaLike ptComa'''
    

def p_AlterBase(t):
    '''AlterBase : alter database E rename tTo id ptComa
                 | alter database E owner tTo id ptComa
                 | alter database E owner tTo currentuser ptComa
                 | alter database E owner tTo sessionuser ptComa
    '''

def p_DropBase(t):
    '''DropBase : drop database E ptComa
                | drop database if exists E ptComa'''
    

def p_EnumType(t):
    'EnumType   : create ttype id as tenum parAbre LISTA_EXP parCierra ptComa'
    

# <<<<<<<<<<<<<<<<<<<<<<<<<<< HEIDY <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< ARIEL <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# PRODUCCIÓN PARA HACER UN UPDATE
def p_produccion0(t):
    ''' UpdateBase   : tUpdate id tSet L_ASIGN where E ptComa '''
    

# PRODUCCIÓN PARA HACER UN DELETE
def p_produccion0_1(t):
    ''' DeleteBase  : tDelete from id CONDICION ptComa '''


# CONDICIÓN QUE PUEDE O NO VENIR DENTRO DE UN DELETE
def p_produccion0_2(t):
    ''' CONDICION   : where E
                    |  '''


# PRODUCCIÓN PARA HACER UN TRUNCATE
def p_produccion1_0(t):
    ''' TruncateBase    : tTruncate L_IDs ptComa'''


# PRODUCCIÓN PARA UNA LISTA DE IDENTIFICADORES
# MODIFICADO ----edi
def p_produccion1_1(t):
    ''' L_IDs   : id coma L_IDs 
                | id '''
                  

# PRODUCCIÓN PARA UNA LISTA DE ASIGNACIONES: id1 = 2, id2 = 3, id3, = 'Hola', etc...
# MODIFICADO ----edi
def p_produccion1(t):
    ''' L_ASIGN : id igual E coma L_ASIGN  
                | id igual E '''
    

# <<<<<<<<<<<<<<<<<<<<<<<<<<< ARIEL <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< FRANCISCO <<<<<<<<<<<<<<<<<<<<<<<<<<<<

def p_EXPR_CREATE_TABLE(t):
    '''CREATE_TABLE : create table id parAbre COLUMN_CREATE parCierra ptComa
                    | create table id parAbre COLUMN_CREATE parCierra tInherits parAbre id parCierra ptComa '''

# MODIFICADO ----edi
def p_EXPR_COLUMN_CREATE(t):
    '''COLUMN_CREATE : COLUMNS COLUMN_CREATE
                     | COLUMNS'''

# MODIFICADO ----edi
def p_EXPR_COLUMNS(t):
    '''COLUMNS : LIST_COLUMNS coma COLUMNS 
               | LIST_COLUMNS 
               '''
   
def p_EXPR_COLUMNS1(t):
    ''' LIST_COLUMNS : ASSIGNS OPCIONALES 
                     | ASSIGNS
    '''

def p_EXPR_ASSIGNS(t):
    '''ASSIGNS : id TIPO
               | tUnique
               | tUnique parAbre COLS parCierra
               | tConstraint id tUnique 
               | tConstraint id tCheck E
               | tCheck E
               | tPrimary tKey parAbre COLS parCierra
               | tForeign tKey parAbre COLS parCierra tReferences id parAbre COLS parCierra'''

# MODIFICADO ----edi
def p_EXPR_OPCIONALES(t):
    '''OPCIONALES : OPCIONALES OPCION 
                  | OPCION '''


def p_EXPR_OPCION(t):
    '''OPCION : tDefault E
              | tPrimary tKey
              | not null
              | null
              | ASSIGNS'''

# MODIFICADO ----edi
def p_EXPR_COLS(t):
    '''COLS : E  coma COLS
            | E '''

    

def p_EXPR_TIPO(t):
    '''TIPO : NUMERIC_TYPES
            | CHAR_TYPES
            | DATE_TYPES
            | tBoolean
            | E'''


def p_EXPR_NUMERIC_TYPES(t):
    '''NUMERIC_TYPES : tSmallint
                     | tInteger
                     | tBigint
                     | tDecimal
                     | tNumeric
                     | tReal
                     | tDouble tPrecision
                     | tMoney'''


def p_EXPR_CHAR_TYPES(t):
    '''CHAR_TYPES : tVarchar parAbre entero parCierra
                  | tCharacter tVarying parAbre entero parCierra
                  | tCharacter parAbre entero parCierra
                  | tChar parAbre entero parCierra
                  | tText'''


def p_EXPR_DATE_TYPES(t):
    '''DATE_TYPES : tDate
                  | tTimestamp 
                  | tTime 
                  | tInterval
                  | tInterval FIELDS'''


def p_EXPR_FIELDS(t):
    '''FIELDS : tYear
              | tMonth
              | tDay
              | tHour
              | tMinute
              | tSecond'''


def p_EXPR_SHOW_TABLE(t):
    '''SHOW_TABLES : show tables ptComa'''


def p_EXPR_DROP_TABLE(t):
    '''DROP_TABLE : drop table id ptComa
    '''


def p_EXPR_ALTER_TABLE(t):
    '''ALTER_TABLE : alter table id rename tColumn id tTo id ptComa
                   | alter table id EXPR_ALTER
                   | alter table id add tColumn id CHAR_TYPES ptComa
                   | alter table id add tCheck E ptComa
                   | alter table id add tConstraint id tUnique parAbre id parCierra ptComa      
                   | alter table id add tForeign tKey parAbre id parCierra tReferences id ptComa    
                   | alter table id drop tColumn id ptComa
                   | alter table id drop tConstraint id ptComa 
                   '''


def p_EXPR_ALTER(t):
    '''EXPR_ALTER : EXPR_ALTER coma alter tColumn id tSet not null ptComa
                  | EXPR_ALTER coma alter tColumn id ttype CHAR_TYPES ptComa
                  | alter tColumn id ttype CHAR_TYPES ptComa
                  | alter tColumn id tSet not null ptComa
                   '''


# <<<<<<<<<<<<<<<<<<<<<<<<<<< FRANCISCO <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< EDI <<<<<<<<<<<<<<<<<<<<<<<<<<<<
def p_INSERT(p):
    ''' INSERT :  insert into id values parAbre LISTA_EXP parCierra ptComa   '''


def p_LISTA_EXP(p):
    ''' LISTA_EXP :    E coma LISTA_EXP     
                    |  E
                     
    '''
    
#------ Pendiente

def p_E(p):
    '''  E : A '''

def p_A(p):
    '''  A : B A_PRIMA
            |          
    '''

def p_A_PRIMA(p):
    '''  A_PRIMA : or B A_PRIMA
                  |
    '''

def p_B(p):
    ''' B :  C B_PRIMA
          |
    '''

def p_B_PRIMA(p):
    '''  B_PRIMA : tAnd C B_PRIMA
                 |
    '''

def p_C(p):
    ''' C : D C_PRIMA
          |
    '''

def p_C_PRIMA(p):
    ''' C_PRIMA : igual     D C_PRIMA
                | diferente D C_PRIMA
                |
    '''
 
def p_D(p):
    ''' D : F D_PRIMA
          |
    '''

def p_D_PRIMA(p):
    ''' D_PRIMA : mayor F D_PRIMA
                | menor F D_PRIMA
                | mayorIgual F D_PRIMA
                | menorIgual F D_PRIMA
                |
    '''

def p_F(p):
    ''' F :  G F_PRIMA
             |
    '''

def p_F_PRIMA(p):
    ''' F_PRIMA : mas   G F_PRIMA
                | menos G F_PRIMA
    '''
    print( p[1])

def p_F_PRIMA1(p):
    ''' F_PRIMA :
    '''
    
    

def p_G(p):
    ''' G :  H G_PRIMA
           |
    '''

def p_G_PRIMA(p):
    ''' G_PRIMA : multi H G_PRIMA
                | divi H G_PRIMA
                | modulo H G_PRIMA
                |
    '''

def p_H(p):
    ''' H : I H_PRIMA
           | 
    '''
def p_H_PRIMA(p):
    ''' H_PRIMA : elevado I H_PRIMA
                | 
    '''
def p_OpNot(p):
    ''' I : not E '''

def p_punto(p):
    ''' I : punto E '''

def p_OpNegativo(p):
    ''' I : menos E '''
    

def p_OpParentesis(p):
    ''' I : parAbre E parCierra  '''
    

def p_entero(p):
    ''' I : entero    
    '''
    print(p[1])

def p_decimal(p):
    ''' I : decimal    
    '''
    

def p_cadena(p):
    ''' I : cadena    
    '''
    

def p_id(p):
    ''' I : id    
    '''
    

def p_booleano(p):
    '''I  : yes
          | no
          | on
          | off
          | tTrue
          | tFalse
    '''
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<< EDI <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN DE LAS PRODUCCIONES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def p_error(t):
    print("Error sintáctico en '%s'" % t.value, " Línea: '%s'" % str(t.lineno))


import ply.yacc as yacc
parser = yacc.yacc()


f = open("./entrada.sql", "r")
input = f.read()
parser.parse(input)
