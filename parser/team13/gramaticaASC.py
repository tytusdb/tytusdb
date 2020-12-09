#LISTA DE PALABRAS RESERVADAS
reservadas = {
    #Numeric Types
    'smallint' : 'tSmallint',
    'integer':'tInteger',
    'bigint' : 'tBigint',
    'decimal' : 'tDecimal',
    'numeric' : 'tNumeric',
    'real' : 'tReal',
    'double' : 'tDouble',
    'precision' : 'tPrecision',
    'money' : 'tMoney',

    #Character types
    'character' : 'tCharacter',
    'varying' : 'tVarying',
    'varchar' : 'tVarchar',
    'char' : 'tChar',
    'text' : 'tText',

    #Date/Time Types
    'timestamp' : 'tTimestamp',
    'date' : 'tDate',
    'time' : 'tTime',
    'interval' : 'tInterval',

    #Interval Type
    'YEAR' : 'tYear',
    'MONTH' : 'tMonth',
    'DAY' : 'tDay',
    'HOUR' : 'tHour',
    'MINUTE' : 'tMinute',
    'SECOND' : 'tSecond',
    'to' : 'tTo',

    #Boolean Type
    'boolean' : 'tBoolean',
    'false' : 'tFalse',
    'true' : 'tTrue',

    'create' : 'create',
    'database' : 'database',
    'or' : 'or',
    'replace' : 'replace',
    'if' : 'if',

    'not' : 'not',
    'exists' : 'exists',
    'databases' : 'databases',
    'drop' : 'drop',
    'owner' : 'owner',

    'mode' : 'mode',
    'alter' : 'alter',
    'show' : 'show',
    'like' : 'like',
    'insert' : 'insert',

    'values' : 'values',
    'null' : 'null',
    'primarykey' : 'primarykey',
    'into' : 'into',
    'from' : 'from',

    'where' : 'where',
    'as' : 'as',
    'select' : 'select',
    'update' : 'tUpdate',
    'set' : 'tSet',

    'delete' : 'tDelete',
    'truncate' : 'tTruncate',
    'table' : 'table',
    'tables' : 'tables',
    'between' : 'tBetween',

    'rename' : 'rename',
    'isNull' : 'isNull',
    'in' : 'tIn',
    'iLike' : 'tILike',
    'similar' : 'tSimilar',

    'is' : 'tIs',
    'notNull' : 'notNull',
    'and' : 'tAnd',
    'current_user': 'currentuser', 
    'session_user': 'sessionuser',

    #>inicia fl
    'inherits':'tInherits',
    'default': 'tDefault',
    'primary':'tPrimary',
    'foreign':'tForeign',
    'key':'tKey',
    'references':'tReferences',
    'check':'tCheck',
    'constraint':'tConstraint',
    'unique':'tUnique',
    'column':'tColumn'
    #>termina fl
}


#LISTA DE TOKENS
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


#DEFINICIÓN DE TOKENS
t_punto     = r'\.'
t_dosPts    = r':'
t_corcheI   = r'\['
t_corcheD   = r'\]'

t_mas       = r'\+'
t_menos     = r'-'
t_elevado   = r'\^'
t_multi     = r'\*'
t_divi      = r'/'

t_modulo    = r'%'
t_igual     = r'='
t_menor     = r'<'
t_mayor     = r'>'
t_menorIgual    = r'<='

t_mayorIgual    = r'>='
t_diferente     = r'<>'

t_parAbre   = r'\('
t_parCierra = r'\)'
t_coma      = r','
t_ptComa    = r';'


#DEFINICIÓN DE UN NÚMERO DECIMAL
def t_decimal(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t


#DEFINICIÓN DE UN NÚMERO ENTERO
def t_entero(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


#DEFINICIÓN DE UNA CADENA PARA LIKE
def t_cadenaLike(t):
    r'\'%.*?%\'|\"%.*?%\"'
    t.value = t.value[2:-2]
    return t

#DEFINICIÓN DE UNA CADENA
def t_cadena(t):
    r'\'.*?\'|\".*?\"'
    t.value = t.value[1:-1]
    return t


#DEFINICIÓN DE UN ID
def t_id(t):
     r'[a-zA-Z]([a-zA-Z]|[0-9]|_)*'
     t.type = reservadas.get(t.value.lower(),'id')
     return t


#DEFINICIÓN DE UN COMENTARIO SIMPLE
def t_COMENTARIO_SIMPLE(t):
    r'--.*'
    t.lexer.lineno += 1 #Descartamos la linea desde aca


#IGNORAR COMENTARIOS SIMPLES
t_ignore_COMENTARIO_SIMPLE = r'\#.*'


# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")   

def t_error(t):
    t.lexer.skip(1)

    print("Caracter inválido '%s'" % t.value[0], " Línea: '%s'" % str(t.lineno))


def find_column(input, token):#Columna relativa a la fila
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# Construyendo el analizador léxico
import ply.lex as lex
import re
lexer = lex.lex()
lex.lex(reflags=re.IGNORECASE) 


#DEFINIENDO LA PRECEDENCIA DE LOS OPERADORES
#---------Modificado Edi------ 
precedence = (
    ( 'right', 'not' ),
    ( 'left',   'tAnd' ),
    ( 'left',   'or' ),
    ( 'left', 'punto' ),
    ( 'right', 'umenos' ),
    ( 'left', 'mas', 'menos' ),
    ( 'left', 'elevado' ),
    ( 'left', 'multi', 'divi','modulo' ),
    ( 'nonassoc', 'parAbre','parCierra','diferente','igual','mayor','menor','menorIgual','mayorIgual' )
)
#---------Modificado Edi---------
# <<<<<<<<<<<<<<<<<<<<<<<<<<< INICIO DE LAS PRODUCCIONES <<<<<<<<<<<<<<<<<<<<<<<<<<<<
def p_init(t):
    'inicio :   sentencias'
    print("Lectura Finalizada")
    #t[0] = t[1]

def p_sentencias_lista(t):
    'sentencias : sentencias sentencia'
    #t[1].append(t[2])
    #t[0] = t[1]

def p_sentencias_sentencia(t):
    'sentencias : sentencia'
    #t[0] = [t[1]]

def p_sentencia(t):
    '''sentencia : CrearBase
                 | ShowBase
                 | AlterBase
                 | DropBase
                 | UpdateBase
                 | DeleteBase
                 | TruncateBase
                 | CREATE_TABLE
                 | SHOW_TABLES
                 | ALTER_TABLE
                 | DROP_TABLE
    '''
    #t[0] = t[1]
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<< HEIDY <<<<<<<<<<<<<<<<<<<<<<<<<<<<
def p_crearBase(t):
    '''CrearBase : create database id ptComa
                 | create database id owner igual id ptComa
                 | create database id owner igual id mode igual entero ptComa
                 | create or replace database id ptComa
                 | create or replace database id owner igual id ptComa
                 | create or replace database id owner igual id mode igual entero ptComa
                 | create database if not exists id ptComa
                 | create database if not exists id owner igual id ptComa
                 | create database if not exists id owner igual id mode igual entero ptComa'''

def p_showBase(t):
    '''ShowBase : show databases ptComa
                | show databases like cadenaLike ptComa'''

def p_AlterBase(t):
    '''AlterBase : alter database rename tTo id ptComa
                 | alter database owner tTo id ptComa
                 | alter database owner tTo currentuser ptComa
                 | alter database owner tTo sessionuser ptComa
    '''

def p_DropBase(t):
    '''DropBase : drop database id ptComa
                | drop database if exists id ptComa'''

# <<<<<<<<<<<<<<<<<<<<<<<<<<< HEIDY <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< ARIEL <<<<<<<<<<<<<<<<<<<<<<<<<<<<

#PRODUCCIÓN PARA HACER UN UPDATE
def p_produccion0(t):
    ''' UpdateBase   : tUpdate id tSet L_ASIGN where OR_EXP ptComa '''


#PRODUCCIÓN PARA HACER UN DELETE
def p_produccion0_1(t):
    ''' DeleteBase  : tDelete from id CONDICION ptComa '''


#CONDICIÓN QUE PUEDE O NO VENIR DENTRO DE UN DELETE
def p_produccion0_2(t):
    ''' CONDICION   : where OR_EXP
                    |  '''


#PRODUCCIÓN PARA HACER UN TRUNCATE
def p_produccion1_0(t):
    ''' TruncateBase    : tTruncate L_IDs ptComa'''


#PRODUCCIÓN PARA UNA LISTA DE IDENTIFICADORES
def p_produccion1_1(t):
    ''' L_IDs   : L_IDs coma id 
                | id '''


#PRODUCCIÓN PARA UNA LISTA DE ASIGNACIONES: id1 = 2, id2 = 3, id3, = 'Hola', etc...
def p_produccion1(t):
    ''' L_ASIGN : L_ASIGN coma id igual OR_EXP
                | id igual OR_EXP '''


#PRODUCCIÓN PARA UNA CONDICIONAL "Or"
def p_produccion2(t):
    ''' OR_EXP  : OR_EXP or AND_EXP
                | AND_EXP '''


#PRODUCCIÓN PARA UNA CONDICIONAL "And"
def p_produccion3(t):
    ''' AND_EXP : AND_EXP tAnd REL_EXP
                | REL_EXP '''


#PRODUCCIÓN PARA LAS OPERACIONES RELACIONALES
def p_produccion5(t):
    ''' REL_EXP : REL_EXP menor ADD_EXP
                | REL_EXP mayor ADD_EXP
                | REL_EXP menorIgual ADD_EXP
                | REL_EXP mayorIgual ADD_EXP
                | REL_EXP diferente ADD_EXP
                | REL_EXP igual ADD_EXP
                | ADD_EXP '''


#PRODUCCIÓN PARA UNA OPERACIÓN DE SUMA O RESTA
def p_produccion6(t):
    ''' ADD_EXP : ADD_EXP mas MULT_EXP
                | ADD_EXP menos MULT_EXP
                | MULT_EXP '''
 

 #PRODUCCIÓN PARA UNA OPERACIÓN DE MULTIPLICACIÓN, DIVISIÓN O MÓDULO
def p_produccion7(t):
    ''' MULT_EXP    : MULT_EXP multi POT_EXP
                    | MULT_EXP divi POT_EXP
                    | MULT_EXP modulo POT_EXP
                    | POT_EXP  '''


#PRODUCCIÓN PARA UNA OPERACIÓN DE POTENCIA
def p_produccion8(t):
    ''' POT_EXP : POT_EXP elevado NEG_VAL
	            | NEG_VAL '''


#PRODUCCIÓN PARA LA NEGACIÓN DE VALORES
def p_produccion9(t):
    ''' NEG_VAL : menos EXPRESION
                | not EXPRESION
                | EXPRESION '''


#PRODUCCIÓN PARA LAS EXPRESIONES
def p_produccion10(t):
    ''' EXPRESION   : id
                    | decimal
                    | entero
                    | cadena
                    | cadenaLike
                    | tTrue
                    | tFalse
                    | parAbre OR_EXP parCierra '''

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
               | tConstraint id tCheck parAbre COLS parCierra
               | tCheck parAbre EXPRE parCierra
               | tPrimary tKey parAbre COLS parCierra
               | tForeign tKey parAbre COLS parCierra tReferences id parAbre COLS parCierra'''

def p_EXPR_OPCIONALES(t):
    '''OPCIONALES : OPCIONALES OPCION
                | OPCION '''

def p_EXPR_OPCION(t):
    '''OPCION : tDefault EXPRE
              | tPrimary tKey
              | not null
              | null
              | ASSIGNS'''


def p_EXPR_COLS(t):
    '''COLS : COLS coma EXPRE
            | EXPRE '''             

def p_EXPR_EXPRE(t):
    '''EXPRE : id 
             | entero
             | cadena
             | decimal
             | tFalse
             | tTrue'''

def p_EXPR_TIPO(t):
    '''TIPO : NUMERIC_TYPES
            | CHAR_TYPES
            | DATE_TYPES
            | tBoolean
            | EXPRE''' 

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
                  | tInterval''' 
                                   
def p_EXPR_SHOW_TABLE(t):
    '''SHOW_TABLES : show tables ptComa'''

def p_EXPR_DROP_TABLE(t):
    '''DROP_TABLE : drop table id ptComa
    '''

def p_EXPR_ALTER_TABLE(t):
    '''ALTER_TABLE : alter table id rename tColumn id tTo id ptComa
                   | alter table id alter tColumn id tSet not null ptComa
                   | alter table id add tColumn id CHAR_TYPES ptComa
                   | alter table id add tCheck E ptComa
                   | alter table id add tConstraint id tUnique parAbre id parCierra ptComa      
                   | alter table id add tForeign tKey parAbre id parCierra tReferences id ptComa    
                   | alter table id drop tColumn id ptComa
                   | alter table id drop tConstraint id ptComa 
                   '''

# <<<<<<<<<<<<<<<<<<<<<<<<<<< FRANCISCO <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< EDI <<<<<<<<<<<<<<<<<<<<<<<<<<<<
     def p_INSERT( p ):
    ''' INSERT :  insert into id values parAbre LISTA_EXP parCierra ptComa  
    '''

def p_LISTA_EXP( p ): 
    ''' LISTA_EXP :    LISTA_EXP coma E    
                    |  E 
    '''
def p_E( p ):
    ''' E :  E or         E  
          |  E tAnd       E
          |  not E
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
          |  menos E %prec umenos
          |  parAbre E parCierra       
    '''

def p_entero( p ):
    ''' E : entero    
    '''
   
def p_decimal( p ):
    ''' E : decimal    
    '''

def p_cadena( p ):
    ''' E : cadena    
    '''

def p_id( p ):
    ''' E : id    
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