import Errores.Nodo_Error as err
from ply import lex
import ply.yacc as yacc

reservadas = {
    'select': 't_select',
    'from': 't_from',
    'where': 't_where',
    'having': 't_having',
    'avg': 't_avg',
    'min': 't_min',
    'max': 't_max',
    'sum': 't_sum',
    'count': 't_count',
    'insert': 't_insert',
    'into': 't_into',
    'values': 't_values',
    'delete': 't_delete',
    'update': 't_update',
    'true': 't_true',
    'false': 't_false',
    'not': 't_not',
    'and': 't_and',
    'or': 't_or',
    'smallint': 't_smallint',
    'integer': 't_integer',
    'bigint': 't_bigint',
    'decimal':'t_decimal',
    'numeric': 't_numeric',
    'real': 't_real',
    'double': 't_double',
    'precision': 't_precision',
    'money': 't_money',
    'character': 't_character',
    'varying': 't_varying',
    'varchar': 't_varchar',
    'char': 't_charn',
    'text': 't_text',
    'boolean': 't_boolean',
    'bool': 't_bool',
    'type': 't_type',
    'enum': 't_enum',
    'create': 't_create',
    'replace': 't_replace',
    'database': 't_database',
    'if': 't_if',
    'exists': 't_exists',
    'owner': 't_owner',
    'mode': 't_mode',
    'show': 't_show',
    'databases': 't_databases',
    'like': 't_like',
    'alter': 't_alter',
    'rename': 't_rename',
    'to': 't_to',
    'current_user': 't_current_user',
    'session_user': 't_session_user',
    'drop': 't_drop',
    'table': 't_table',
    'delete': 't_delete',
    'only': 't_only',
    'using': 't_using',
    'current': 't_current',
    'of': 't_of',
    'returning': 't_returning',
    'as' : 't_as',
    'inherits' : 't_inherits',
    'primary' : 't_primary',
    'key' : 't_key',
    'references' : 't_references',
    'foreign' : 't_foreign',
    'null' : 't_null',
    'constraint' : 't_constraint',
    'unique' : 't_unique',
    'check' : 't_check',
    'add' : 't_add',
    'set' : 't_set',
    'rename' : 't_rename',
    'column' : 't_column',
    'inner' : 't_inner',
    'left' : 't_left',
    'right' : 't_right',
    'full' : 't_full',
    'outer' : 't_outer',
    'join' : 't_join',
    'natural' : 't_natural',
    'on' : 't_on'
}

tokens = [
             'par1',
             'par2',
             'cor1',
             'cor2',
             'asterisco',
             'mas',
             'menos',
             'pyc',
             'coma',
             'div',
             'punto',
             'igual',
             'menor',
             'mayor',
             'menori',
             'mayori',
             'diferente',
             'porcentaje',
             'diferentede',
             'pot',
             'bipunto',
             'id',
             'decimal',
             'entero',
             'char',
             'string'
         ] + list(reservadas.values())

# Tokens
t_par1 = r'\('
t_par2 = r'\)'
t_cor1 = r'\['
t_cor2 = r'\]'
t_pyc = r';'
t_punto = r'.'
t_coma = r','
t_igual = r'='
t_mas = r'\+'
t_menos = r'-'
t_asterisco = r'\*'
t_div = r'/'
t_mayor = r'>'
t_menor = r'<'
t_mayori = r'>='
t_menori = r'<='
t_diferente = r'!='
t_porcentaje = r'\%'
t_pot = r'\^'
t_bipunto = r'::'
t_diferentede = r'<>'


def t_decimal(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("El valor es muy grande %d", t.value)
        t.value = 0
    return t


def t_entero(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("El valor de integer es muy grande %d", t.value)
        t.value = 0
    return t


def t_char(t):
    r'\'.\''
    t.value = t.value[1:-1]  # se remueven comillas
    return t


def t_string(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # se remueven comillas
    return t


def t_id(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'iden')  # Check for reserved words
    return t


def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


def t_error(t):
    # errores.insertar(err.Error("Lexico", "Caracter Invalido '%s'" % t.value[0],
    # t.lineno, find_column(input, t)))
    print("Caracter Invalido '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

precedence = (
    ('left', 'coma'),
    ('left', 'punto', 'bipunto'),
    ('left', 't_or'),
    ('left', 't_and'),
    ('left', 'igual', 'diferente'),
    ('left', 'mayor', 'menor', 'mayori', 'menori'),
    ('left', 'mas', 'menos'),
    ('left', 'asterisco', 'div', 'porcentaje', 'pot'),
    ('right', 't_not'),
    ('left', 'par1', 'par2', 'cor1', 'cor2',),
    ('right', 'umenos', 'umas')
)

from AST.Expresiones import *

reporteg = []


def p_sql(p):
    'SQL : Sentencias_SQL'
    p[0] = p[1]


def p_sql2(p):
    'SQL : '
    p[0] = []


def p_Sentencias_SQL_Sentencia_SQL(p):
    'Sentencias_SQL : Sentencias_SQL Sentencia_SQL'
    p[1].extend(p[2])
    p[0] = p[1]


def p_Sentencias_SQL(p):
    'Sentencias_SQL : Sentencia_SQL'
    p[0] = p[1]


def p_Sentencia_SQL(p):
    '''Sentencia_SQL : Sentencias_DML
                   | Sentencias_DDL'''
    p[0] = p[1]


#-------------------------------------------------------------SENTENCIAS DML
def p_Sentencias_DML(p):
    '''Sentencias_DML : Select_SQL pyc
                   | t_insert t_into id Insert_SQL pyc
                   | t_update Update_SQL pyc
                   | t_delete t_from DeleteTB Condiciones_Del Condiciones_Del2 pyc'''
    p[0] = p[1]


def p_Select_SQL(p):
    'Select_SQL : t_select Lista_ID t_from Lista_ID Condiciones_Sel'
    p[1] += ' ' + p[2] + ' ' + p[3] + ' ' + p[4] + ' ' + p[5]
    p[0] = p[1]


def p_Selec_SQL_Condiciones(p):
    '''Condiciones_Sel : t_where
                | t_having'''
    p[0] = p[1]


def p_Insert_SQL(p):
    'Insert_SQL : par1 Lista_ID par2 t_values par1 EXP par2'
    p[0] = p[1]


def p_Insert_SQL2(p):
    'Insert_SQL : t_values par1 EXP par2'
    p[0] = p[1]


def p_Update_SQL(p):
    'Update_SQL : t_update Lista_ID '
    p[0] = p[1]


def p_DeleteTB(p):
    '''DeleteTB : id 
            | t_only id'''
    if len(p) == 3:
         p[0] = p[1]
    else: 
         p[0] = p[1]


def p_Condiciones_Del(p):
    ''' Condiciones_Del : asterisco 
                | t_as id 
                | empty'''


def p_Condiciones_Del2(p):
    ''' Condiciones_Del2 : t_using Lista_ID
                           | t_where Opc_Where
                           | t_returning asterisco
                           | EXP 
                           | empty'''


def p_Opc_Where(p):
    '''Opc_Where : EXP 
                | t_current t_of id '''


# ---------------------------- Sentencias DDL y Enum Type --------------

def p_Sentencias_DDL(p):
    '''Sentencias_DDL : t_show t_databases pyc
                    | t_drop Drop pyc
                    | t_alter Alter pyc
                    | t_create Create pyc
                    | Enum_Type '''

def p_Enum_Type(p):
    'Enum_Type : t_create t_type id t_as t_enum par1 Lista_ID par2 pyc'
    p[0] = p[3]

def p_Drop(p):
    '''Drop : t_database DropDB id
            | t_table  id '''

def p_DropDB(p):
    '''DropDB : t_if t_exists
            | empty'''

def p_Alter(p):
    '''Alter : t_database id AlterDB
            | t_table id AlterTB '''

def p_AlterDB(p):
    ''' AlterDB : t_rename t_to id 
                | t_owner t_to SesionDB '''

def p_SesionDB(p):
    ''' SesionDB : id 
                | t_current_user
                | t_session_user '''
    
def p_AlterTB(p): 
    ''' AlterTB : t_add Add_Opc
                | t_drop Drop_Opc
                | t_alter t_column Alter_Column
                | t_rename t_column id t_to id '''
    
def p_Add_Opc(p):
    '''Add_Opc : t_column id Tipo
               | t_foreign t_key par1 id par2 t_references id
               | t_constraint id t_unique par1 id par2 
               | t_check EXP'''

def p_Drop_Opc(p):
    ''' Drop_Opc :  t_column id 
                 |  t_constraint id ''' 

def p_Alter_Column(p):
    ''' Alter_Column :   id t_set t_not t_null
                     |   Alter_Columns'''

def p_Alter_Columns(p):
    ''' Alter_Columns : Alter_Columns coma Alter_Column1 
                    | Alter_Column1'''

def p_Alter_Colum1(p):
    'Alter_Column1 :  id t_type t_varchar par1 entero par2 '

def p_Create(p): 
    ''' Create : CreateDB   
               | CreateTB '''

def p_CreateDB(p):
    '''CreateDB : t_database Op1_DB
                | t_or t_replace t_database Op1_DB'''
    if len(p) == 3:
         p[0] = p[1]
    else: 
         p[0] = p[1]

def p_Op1_DB(p):
    ''' Op1_DB : t_if t_not t_exists id Sesion
               | id Sesion'''
    if len(p) == 6:
         p[0] = p[1]
    else: 
         p[0] = p[1]

def p_Sesion(p):
    ''' Sesion : t_owner Op_Sesion Sesion_mode
                | t_mode Op_Sesion
                | empty '''

def p_Op_Sesion(p):
    ''' Op_Sesion : igual id 
            | id  '''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_Sesion_mode(p):
    ''' Sesion_mode : t_mode Op_Sesion
                  | empty '''

def p_CreateTB(p):
    'CreateTB : t_table id par1 Columnas par2 Inherits '

def p_Inherits(p):
    ''' Inherits : t_inherits par1 id par2
               | empty '''

def p_Columnas(p):
    '''Columnas : Columnas coma Columna
                | Columna'''
    if len(p) == 3:
        p[1].extend(p[2])
        p[0] = p[1]   
    else:
        p[0] = p[1] 

def p_Columna(p):
    ''' Columna : id Tipo Constraints
                | t_primary t_key par1 Lista_ID par2
                | t_unique par1 Lista_ID par2
                | t_constraint id t_check par1 EXP par2
                | t_check par1 EXP par2
                | t_foreign t_key par1 Lista_ID par2 t_references id par1 Lista_ID par2 '''
    
def p_Constraints(p):
    ''' Constraints :  t_primary t_key
                        | t_references id 
                        | t_not t_null
                        | t_null
                        | t_constraint id 
                        | t_unique Opc_Unique
                        | t_check par1 EXP par2 
                        | empty'''

def p_Opc_Unique(p):
  ''' Opc_Unique : t_not t_null 
                | empty '''

def p_Tipo(p):
    ''' Tipo : t_smallint
              | t_integer 
              | t_bigint
              | t_decimal 
              | t_numeric 
              | t_real
              | t_double t_precision
              | t_money
              | t_character t_varying par1 Valor par2 
              | t_varchar par1 Valor par2
              | t_character par1 Valor par2
              | t_charn par1 Valor par2
              | t_text 
              | t_boolean ''' 

def p_Valor(p):
    ''' Valor : decimal
            | entero
            | string
            | char 
            | t_true
            | t_false
            | id'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    p[0] = []


# ----------------------------EXPRESIONES Y OPERACIONES---------------------------------------------------------------
def p_aritmeticas(p):
    '''EXP : EXP mas EXP
           | EXP menos EXP
           | EXP asterisco EXP
           | EXP div EXP
           | EXP pot EXP
           | EXP porcentaje EXP'''
    p[0] = Aritmetica(p[1], p[3], p.slice[2].value, p.slice[2].lineno, find_column(input, p.slice[2]))


def p_relacionales(p):
    '''EXP : EXP mayor EXP
           | EXP mayori EXP
           | EXP menor EXP
           | EXP menori EXP
           | EXP igual EXP
           | EXP diferente EXP
           | EXP diferentede EXP'''
    p[0] = Relacional(p[1], p[3], p.slice[2].value, p.slice[2].lineno, find_column(input, p.slice[2]))


def p_logicos(p):
    '''EXP : EXP t_and EXP
       | EXP t_or EXP
       '''
    p[0] = logica(p[1], p[3], p.slice[2].value, p.slice[2].lineno, find_column(input, p.slice[2]))


def p_unario(p):
    '''EXP : mas EXP  %prec umas
           | menos EXP  %prec umenos
           | t_not EXP'''
    p[0]= unario(p[2], p[1], p.slice[1].lineno, find_column(input, p.slice[1]))


def p_EXP_Valor(p):
    'EXP : Valor'
    p[0] = p[1] #primitivo(p[1], p.slice[1].lineno, find_column(input, p.slice[1]), p.slice[1].type)


def p_exp_agregacion(p):
    '''EXP :  t_avg par1 EXP par2
            | t_sum par1 EXP par2
            | t_count par1 EXP par2
            | t_max par1 EXP par2
            | t_min par1 EXP par2'''


def p_Lista_ID(p):
    '''Lista_ID : Lista_ID coma id
               | id '''
    if len(p) == 3:
        p[1].extend(p[2])
        p[0] = p[1]
    else:
        p[0] = p[1]


def p_error(p):
    print("Error Sintactico en " + p.value)
    return False


parser = yacc.yacc()

res = parser.parse("")
while True :
    print(res)
    break
