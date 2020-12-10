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
    'YEAR': 'tYear',
    'MONTH': 'tMonth',
    'DAY': 'tDay',
    'HOUR': 'tHour',
    'MINUTE': 'tMinute',
    'SECOND': 'tSecond',
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
    'and': 'tAnd',
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
    'add': 'add'
    # >termina fl
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
             'ptComa'

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
    t.lexer.lineno += 1  # Descartamos la linea desde aca


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


def find_column(input, token):  # Columna relativa a la fila
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# Construyendo el analizador léxico
import ply.lex as lex
import re

lexer = lex.lex()
lex.lex(reflags=re.IGNORECASE)

# DEFINIENDO LA PRECEDENCIA DE LOS OPERADORES
# ---------Modificado Edi------
precedence = (
    ('right', 'not'),
    ('left', 'tAnd'),
    ('left', 'or'),
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
    '''
    t[0] = t[1]


# <<<<<<<<<<<<<<<<<<<<<<<<<<< HEIDY <<<<<<<<<<<<<<<<<<<<<<<<<<<<
def p_crearBase(t):
    '''CrearBase : create database id ptComa
                 | create database id owner igual id ptComa
                 | create database id mode igual entero ptComa
                 | create database id owner igual id mode igual entero ptComa
                 | create or replace database id ptComa
                 | create or replace database id owner igual id ptComa
                 | create or replace database id mode igual entero ptComa
                 | create or replace database id owner igual id mode igual entero ptComa
                 | create database if not exists id ptComa
                 | create database if not exists id owner igual id ptComa
                 | create database if not exists id mode igual entero ptComa
                 | create database if not exists id owner igual id mode igual entero ptComa'''
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
        if t[3].lower() == "if":
            # novena produccion
            t[0] = SCrearBase(False, False, False, True, t[6])
    elif len(t) == 11:
        if t[3].lower() == "if":
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
    '''AlterBase : alter database id rename tTo id ptComa
                 | alter database id owner tTo id ptComa
                 | alter database id owner tTo currentuser ptComa
                 | alter database id owner tTo sessionuser ptComa
    '''
    # def __init__(self, id, rename, owner, id):
    if t[4].lower() == "rename":
        t[0] = SAlterBase(t[3], True, False, t[6])
    else:
        t[0] = SAlterBase(t[3], False, True, t[6])


def p_DropBase(t):
    '''DropBase : drop database id ptComa
                | drop database if exists id ptComa'''
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
    ''' UpdateBase   : tUpdate id tSet L_ASIGN where E ptComa '''
    t[0] = SUpdateBase(t[2], t[4], t[6])


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
def p_produccion1_1(t):
    ''' L_IDs   : L_IDs coma id 
                | id '''


# PRODUCCIÓN PARA UNA LISTA DE ASIGNACIONES: id1 = 2, id2 = 3, id3, = 'Hola', etc...
def p_produccion1(t):
    ''' L_ASIGN : L_ASIGN coma id igual E
                | id igual E '''
    if len(t) == 6:
        val = SValSet(t[3], t[5])
        t[1].append(val)
        t[0]=t[1]
    else:
        val=SValSet(t[1],t[3])
        t[0]=[val]


# <<<<<<<<<<<<<<<<<<<<<<<<<<< ARIEL <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< FRANCISCO <<<<<<<<<<<<<<<<<<<<<<<<<<<<

def p_EXPR_CREATE_TABLE(t):
    '''CREATE_TABLE : create table id parAbre COLUMN_CREATE parCierra ptComa
                    | create table id parAbre COLUMN_CREATE parCierra tInherits parAbre id parCierra ptComa '''


def p_EXPR_COLUMN_CREATE(t):
    '''COLUMN_CREATE : COLUMN_CREATE COLUMNS
                     | COLUMNS'''


def p_EXPR_COLUMNS(t):
    '''COLUMNS : COLUMNS coma ASSIGNS
               | COLUMNS coma ASSIGNS OPCIONALES
               | ASSIGNS
               | ASSIGNS OPCIONALES'''


def p_EXPR_ASSIGNS(t):
    '''ASSIGNS : id TIPO
               | tUnique
               | tUnique parAbre COLS parCierra
               | tConstraint id tUnique 
               | tConstraint id tCheck E
               | tCheck E
               | tPrimary tKey parAbre COLS parCierra
               | tForeign tKey parAbre COLS parCierra tReferences id parAbre COLS parCierra'''


def p_EXPR_OPCIONALES(t):
    '''OPCIONALES : OPCIONALES OPCION
                | OPCION '''


def p_EXPR_OPCION(t):
    '''OPCION : tDefault E
              | tPrimary tKey
              | not null
              | null
              | ASSIGNS'''


def p_EXPR_COLS(t):
    '''COLS : COLS coma E
            | E '''

    t[0] = t[1]


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
    ''' LISTA_EXP :    LISTA_EXP coma E    
                    |  E 
    '''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_E(p):
    ''' E : E or E
          |  E tAnd       E
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
        p[0] = SOperacion(p[1], p[3], Expresion.TABATT)


def p_OpNot(p):
    ''' E : not E '''
    p[0] = SExpresion(p[2], Logicas.NOT)


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


def p_booleano(p):
    '''E  : yes
          | no
          | on
          | off
          | tTrue
          | tFalse
    '''
    p[0] = SExpresion(p[1], Expresion.BOOLEAN)


# <<<<<<<<<<<<<<<<<<<<<<<<<<< EDI <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN DE LAS PRODUCCIONES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def p_error(t):
    print("Error sintáctico en '%s'" % t.value, " Línea: '%s'" % str(t.lineno))


import ply.yacc as yacc

parser = yacc.yacc()


def parse(input):
    return parser.parse(input)
