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


# DEFINIENDO LA PRECEDENCIA DE LOS OPERADORES
# ---------Modificado Edi---------
# <<<<<<<<<<<<<<<<<<<<<<<<<<< INICIO DE LAS PRODUCCIONES <<<<<<<<<<<<<<<<<<<<<<<<<<<<
from sentencias import *


def p_init(t):
    'inicio :   sentencias'
        
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
    ''' UpdateBase   : tUpdate id tSet L_ASIGN where CondicionBase ptComa '''
    

# PRODUCCIÓN PARA HACER UN DELETE
def p_produccion0_1(t):
    ''' DeleteBase  : tDelete from id where CondicionBase ptComa '''


def p_produccion0_2(t):
    ''' DeleteBase : tDelete from id ptComa'''




#PRODUCCIÓN PARA LAS CONDICIONES DEL DELETE Y EL UPDATE
def p_produccion0_3(p):
    ''' CondicionBase   : Condi CondicionBase
                        | Condi

                        '''
def p_produccionCondi(p):
    ''' Condi        :  ORAND Condiciones 
                     | Condiciones '''



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
    '''CREATE_TABLE : create table id parAbre COLUMNS parCierra ptComa
                    | create table id parAbre COLUMNS parCierra tInherits parAbre id parCierra ptComa '''


def p_EXPR_COLUMNS(t):
    '''COLUMNS : ASSIGNS coma COLUMNS 
               | ASSIGNS
    '''


def p_EXPR_ASSIGNS(t):
    '''ASSIGNS : id TIPO
               | id TIPO OPCIONALES
               | tCheck E
               | tConstraint id tCheck E
               | tUnique parAbre COLS parCierra
               | tPrimary tKey parAbre COLS parCierra
               | tConstraint id tForeign tKey parAbre COLS parCierra tReferences id parAbre COLS parCierra
               | tForeign tKey parAbre COLS parCierra tReferences id parAbre COLS parCierra'''



# MODIFICADO ----edi
def p_EXPR_OPCIONALES(t):
    '''OPCIONALES : OPCION OPCIONALES 
                  | OPCION '''



def p_EXPR_OPCION(t):
    '''OPCION : tDefault E'''
    

def p_EXPR_OPCION1(t):
    '''OPCION : tPrimary tKey'''
    

def p_EXPR_OPCION2(t):
    '''OPCION : not null'''
    

def p_EXPR_OPCION3(t):
    '''OPCION : null'''
    

def p_EXPR_OPCION4(t):
    '''OPCION : tUnique'''
    

def p_EXPR_OPCION5(t):
    '''OPCION : tCheck E'''
    

def p_EXPR_OPCION6(t):
    ''' OPCION : tConstraint id tUnique '''
    

def p_EXPR_OPCION7(t):
    '''OPCION : tConstraint id tCheck E'''
    

# MODIFICADO ----edi
def p_EXPR_COLS(t):
    '''COLS : E  coma COLS
            | E '''

    
def p_EXPR_TIPO(t):
    '''TIPO : NUMERIC_TYPES
            | CHAR_TYPES
            | DATE_TYPES
            | BOOL_TYPES
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


def p_EXPR_BOOL_TYPES(t):
    '''BOOL_TYPES : tBoolean'''


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

def p_EXPR_ALTER_TABLE1(t):
    '''ALTER_TABLE : alter table id LDColumn ptComa '''

def p_LDropColumn(t):
    ''' LDColumn : LDCol coma  LDColumn
                 | LDCol'''


def p_LDCol(t):
    ''' LDCol : drop tColumn id '''
    t[0] = SNAlterDrop(t[3])


def p_LAddColumn(t):
    ''' LColumn : LCol  coma  LColumn
                | LCol '''

def p_LCol(t):
    '''LCol : add tColumn id TIPO'''


def p_EXPR_ALTER(t):
    '''EXPR_ALTER :  alter tColumn id tSet not null ptComa   coma EXPR_ALTER 
                  |  alter tColumn id ttype CHAR_TYPES ptComa coma EXPR_ALTER 
                  |  alter tColumn id ttype CHAR_TYPES ptComa
                  |  alter tColumn id tSet not null ptComa
                   '''


# <<<<<<<<<<<<<<<<<<<<<<<<<<< FRANCISCO <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< EDI <<<<<<<<<<<<<<<<<<<<<<<<<<<<
def p_INSERT(p):
    ''' INSERT :  insert into id values parAbre LISTA_EXP parCierra ptComa
               |  insert into id parAbre LISTA_EXP parCierra values parAbre LISTA_EXP parCierra ptComa'''


def p_LISTA_EXP(p):
    ''' LISTA_EXP :    E_FUNC coma LISTA_EXP     
                    |  E_FUNC
                     
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
    '''  B_PRIMA : And C B_PRIMA
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

def p_fecha(p):
    ''' I : fecha    
    '''


def p_hora(p):
    ''' I : hora    
    '''


def p_fecha_hora(p):
    ''' I : fecha_hora    
    '''


def p_booleano(p):
    '''I : yes
          | no
          | on
          | off
          | tTrue
          | tFalse
    '''

def p_interval(p):
    '''I : intervaloc '''


# <<<<<<<<<<<<<<<<<<<<<<<<<<< EDI <<<<<<<<<<<<<<<<<<<<<<<<<<<<

def p_QUERIES(p):
    '''QUERIES : QUERY union QUERY
               | QUERY intersect QUERY
               | QUERY except QUERY
               | QUERY'''

def p_QUERY(p):
    '''QUERY : EXPR_SELECT 
             | EXPR_SELECT EXPR_FROM 
             | EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_HAVING EXPR_ORDERBY EXPR_LIMIT 
    '''

def p_QUERY_p4_1(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_ORDERBY'''


def p_QUERY_p4_2(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_LIMIT'''


def p_QUERY_p4_3(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE'''


def p_QUERY_p4_4(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_HAVING'''


def p_QUERY_p4_5(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY'''

    # LEN 5     #select, ffrom, where, groupby, having, orderby, limit


def p_QUERY_p5_1(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_ORDERBY EXPR_LIMIT'''


def p_QUERY_p5_2(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_ORDERBY '''


def p_QUERY_p5_3(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_LIMIT'''


def p_QUERY_p5_4(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY'''


def p_QUERY_p5_5(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_LIMIT'''


def p_QUERY_p5_6(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_ORDERBY '''


def p_QUERY_p5_7(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_HAVING'''


def p_QUERY_p5_8(p):
    '''QUERY :  EXPR_SELECT EXPR_FROM EXPR_HAVING EXPR_LIMIT'''


def p_QUERY_p5_9(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_HAVING EXPR_ORDERBY'''


def p_QUERY_p5_10(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_HAVING'''


# LEN 6     #select, ffrom, where, groupby, having, orderby, limit
def p_QUERY_p6_1(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_ORDERBY EXPR_LIMIT '''


def p_QUERY_p6_2(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_ORDERBY '''


def p_QUERY_p6_3(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_LIMIT '''


def p_QUERY_p6_4(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_HAVING '''


def p_QUERY_p6_5(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_ORDERBY EXPR_LIMIT '''


def p_QUERY_p6_6(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_HAVING EXPR_LIMIT '''


def p_QUERY_p6_7(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_HAVING EXPR_ORDERBY '''


def p_QUERY_p6_8(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_HAVING EXPR_ORDERBY EXPR_LIMIT'''


def p_QUERY_p6_9(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_HAVING EXPR_LIMIT'''


def p_QUERY_p6_10(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_HAVING EXPR_ORDERBY'''


# LEN 7     #select, ffrom, where, groupby, having, orderby, limit
def p_QUERY_p7_1(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_ORDERBY EXPR_LIMIT'''


def p_QUERY_p7_2(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_HAVING EXPR_LIMIT'''


def p_QUERY_p7_3(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_HAVING EXPR_ORDERBY'''


def p_QUERY_p7_4(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_HAVING EXPR_ORDERBY EXPR_LIMIT'''


def p_QUERY_p7_5(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_HAVING EXPR_ORDERBY EXPR_LIMIT'''

def p_EXPR_SELECT(p):
    '''EXPR_SELECT : select distinct EXPR_COLUMNAS
                   | select multi
                   '''
def p_EXPR_SELECT_C(p):
    '''EXPR_SELECT : select EXPR_COLUMNAS'''

def p_EXPR_COLUMNAS(p):
    '''EXPR_COLUMNAS : EXPR_COLUMNAS1 coma EXPR_COLUMNAS
                     | EXPR_COLUMNAS1
                     '''
                                      

def p_EXPR_COLUMNAS1(p):
    '''EXPR_COLUMNAS1 : E
                     | EXPR_AGREGACION
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

def p_EXPR_COLUMNAS2(p):
    '''EXPR_COLUMNAS1 : parAbre QUERY parCierra
                     | parAbre QUERY parCierra E
                     | parAbre QUERY parCierra as E'''


def p_EXPR_COLUMNAS1_p1(p):  # error
    '''EXPR_COLUMNAS1 : substring parAbre E coma E coma E parCierra
                     | greatest parAbre E_LIST parCierra
                     | least parAbre E_LIST parCierra
                     | substring parAbre E coma E coma E parCierra as E
                     | substr parAbre E coma E coma E parCierra as E
                     | substr parAbre E coma E coma E parCierra 
                     | greatest parAbre E_LIST parCierra as E
                     | least parAbre E_LIST parCierra as E '''

def p_EXPR_EXTRA(p):
    '''EXPR_EXTRA : tExtract parAbre FIELDS from tTimestamp fecha_hora parCierra
                  | tExtract parAbre FIELDS from E parCierra'''


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
                     | virgulilla E
                     | PP
                     '''


                     
def p_EXPR_BINARIAS1(p):
    '''  PP  : RR PPRIMA'''


def p_EXPR_BINARIAS2(p):
    '''  PPRIMA   :  amp RR PPRIMA 
                  |  barra RR PPRIMA
                  |  numeral RR PPRIMA
                  |  menormenor RR PPRIMA
                  |  mayormayor RR PPRIMA
                  |
    '''

def p_EXPR_BINARIAS3(p):
    '''   RR : E '''

def p_EXPR_FECHA(p):
    '''EXPR_FECHA : date_part parAbre E coma DATE_TYPES E parCierra
                  | current_date
                  | current_time
                  | now parAbre parCierra
                  | DATE_TYPES E'''

def p_EXPR_CASE(p):
    '''EXPR_CASE : case CASE_LIST end
                 | case CASE_LIST else E end'''

def p_CASE_LIST(p):
    '''CASE_LIST : when E then E CASE_LIST
                 | when E then E'''


def p_E_LIST(p):
    '''E_LIST : E_LIST1 coma E_LIST
              | E_LIST1
              '''

def p_E_LIST1(p):
    '''E_LIST1 : E
               | now parAbre parCierra'''


def p_EXPR_FROM(p):
    '''EXPR_FROM : from L_IDsAlias 
                 | from parAbre QUERY parCierra 
                 | from parAbre QUERY parCierra id
                 | from parAbre QUERY parCierra as id'''


def p_L_IDsAlias(p):
    '''L_IDsAlias : L_IDsAlias1 coma L_IDsAlias
                  | L_IDsAlias1 '''


def p_L_IDsAlias_p1(p):  # fix
    '''L_IDsAlias1 : id id 
                    | id as id 
                    | id'''



def p_EXPR_WHERE(p):
    '''EXPR_WHERE : where LIST_CONDS '''


def p_LIST_CONDS(p):
    '''LIST_CONDS : COND1 LIST_CONDS
                  | ORAND COND1 LIST_CONDS
                  | ORAND COND1
                  | COND1  '''

def p_LIST_ORAND(p):
    '''ORAND : or
             | And'''


def p_COND1(p):
    '''COND1 :  E_FUNC 
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
                | substr parAbre E_FUNC coma E_FUNC coma E_FUNC parCierra igual E '''


def p_COND2(p):
    '''COND1 :    exists parAbre QUERY parCierra
                | not exists parAbre QUERY parCierra
                | E_FUNC in parAbre QUERY parCierra 
                | E_FUNC not in parAbre QUERY parCierra
                | E_FUNC OPERATOR any parAbre QUERY parCierra
                | E_FUNC OPERATOR some parAbre QUERY parCierra
                | E_FUNC OPERATOR all parAbre QUERY parCierra'''


def p_COND3(p):
    '''COND1 :    E_FUNC tBetween E_FUNC 
                | E_FUNC not tBetween E_FUNC'''


def p_OPERATOR(p):
    '''OPERATOR : igual
                | menor
                | mayor
                | menorIgual
                | mayorIgual
                | diferente'''


def p_EXPR_GROUPBY(p):
    '''EXPR_GROUPBY : group by LISTA_EXP'''

def p_EXPR_HAVING(p):
    '''EXPR_HAVING : having E_FUNC '''

def p_EXPR_E_FUNC(p):
    '''E_FUNC : EXPR_AGREGACION
              | EXPR_MATHS
              | EXPR_TRIG
              | EXPR_BINARIAS
              | EXPR_FECHA
              | E '''

def p_EXPR_ORDERBY(p):
    '''EXPR_ORDERBY : order by LIST_ORDERBY'''


def p_LIST_ORDERBY(p):
    '''LIST_ORDERBY : LIST_ORDERBY_1 coma LIST_ORDERBY
                    | LIST_ORDERBY_1'''


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

def p_EXPR_LIMIT(p):
    '''EXPR_LIMIT : limit all
                  | limit all offset E'''

def p_EXPR_LIMIT2(p):
    '''EXPR_LIMIT : limit E
                  | limit E offset E'''



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN DE LAS PRODUCCIONES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<


def p_error(t):
    print("Error sintáctico en '%s'" % t.value, " Línea: '%s'" % str(t.lineno))





import ply.yacc as yacc


def analizadordesc(input):
    lexer = lex.lex()
    lex.lex(reflags=re.IGNORECASE)
    parser = yacc.yacc()
    analizador=parser.parse(input)
    return analizador 


