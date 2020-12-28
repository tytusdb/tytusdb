import Errores.Nodo_Error as err
from ply import lex
from AST.Sentencias import Raiz, Sentencia
import AST.SentenciasDDL as DDL
import ply.yacc as yacc

reservadas = {
    'select': 't_select',
    'distinct': 't_distinct',
    'as': 't_as',
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
    'decimal': 't_decimal',
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
    'inherits': 't_inherits',
    'primary': 't_primary',
    'key': 't_key',
    'references': 't_references',
    'foreign': 't_foreign',
    'null': 't_null',
    'constraint': 't_constraint',
    'unique': 't_unique',
    'check': 't_check',
    'add': 't_add',
    'set': 't_set',
    'rename': 't_rename',
    'column': 't_column',
    'inner': 't_inner',
    'left': 't_left',
    'right': 't_right',
    'full': 't_full',
    'outer': 't_outer',
    'join': 't_join',
    'natural': 't_natural',
    'on': 't_on',
    'abs': 't_abs',
    'cbrt': 't_cbrt',
    'ceil': 't_ceil',
    'ceiling': 't_ceiling',
    'degrees': 't_degrees',
    'div': 't_div',
    'exp': 't_exp',
    'factorial': 't_factorial',
    'floor': 't_floor',
    'gcd': 't_gcd',
    'ln': 't_ln',
    'log': 't_log',
    'mod': 't_mod',
    'pi': 't_pi',
    'power': 't_power',
    'radians': 't_radians',
    'round': 't_round',
    'use': 't_use',
    'default' : 't_default',
    'acos' : 't_acos',
    'acosd' : 't_acosd',
    'asin' : 't_asin',
    'asind' : 't_asind',
    'atan' : 't_atan',
    'atand' : 't_atand',
    'atan2' : 't_atan2',
    'atan2d' : 't_atan2d',
    'cos' : 't_cos',
    'cosd' : 't_cosd',
    'cot' : 't_cot',
    'cotd' : 't_cotd',
    'sin' : 't_sin',
    'sind' : 't_sind',
    'tan' : 't_tan',
    'tand' : 't_tand',
    'sinh' : 't_sinh',
    'cosh' : 't_cosh',
    'tanh' : 't_tanh',
    'asinh' : 't_asinh',
    'acosh' : 't_acosh',
    'atanh' : 't_atanh',
    'min_scale' : 't_min_scale',
    'scale' : 't_scale',
    'sign' : 't_sign',
    'sqrt' : 't_sqrt',
    'trim_scale' : 't_trim_scale',
    'trunc' : 't_trunc',
    'width_bucket' : 't_width_bucket',
    'random' : 't_random',
    'setseed' : 't_setseed',
    'length' : 't_length',
    'substring' : 't_substring',
    'trim' : 't_trim',
    'md5' : 't_md5',
    'sha256' : 't_sha256',
    'substr' : 't_substr',
    'get_byte' : 't_get_byte',
    'set_byte' : 't_set_byte',
    'convert' : 't_convert',
    'encode' : 't_encode',
    'decode' : 't_decode',
    'group':'t_group',
    'by' :'t_by',
    'having': 't_having',
    'order': 't_order',
    'asc':'t_asc',
    'desc':'t_desc',
    'first':'t_first',
    'last':'t_last',
    'nulls':'t_nulls',
    'all':'t_all',
    'offset':'t_offset',
    'limit':'t_limit',
    'date':'t_date'
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
t_punto = r'\.'
t_coma = r'\,'
t_igual = r'\='
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
        ListaErrores.insertar(err.Nodo_Error("Lexico", "El valor es muy grande '%s'" % str(t.value),
                                      t.lineno, find_column(input, t)))
        t.value = 0
    return t


def t_entero(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("El valor de integer es muy grande %d", t.value)
        ListaErrores.insertar(err.Nodo_Error("Lexico", "El valor de integer es muy grande '%s'" % str(t.value),
                                      t.lineno, find_column(input, t)))
        t.value = 0
    return t


def t_char(t):
    r'\'.*?\''
    t.value = t.value[1:-1]  # se remueven comillas
    return t


def t_string(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # se remueven comillas
    return t


def t_id(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'id')  # Check for reserved words
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
    ListaErrores.insertar(err.Nodo_Error("Lexico", "Caracter no valido '%s'" % t.value[0],
                                      t.lineno, find_column(input, t)))
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

precedence = (
    ('left', 'punto', 'bipunto'),
    ('left', 'coma'),
    ('right', 'igual'),
    ('left', 'cor1', 'cor2'),
    ('left', 'mas', 'menos'),
    ('left', 'asterisco', 'div', 'porcentaje'),
    ('left', 'pot'),
    ('right', 'umenos', 'umas'),
    ('left', 'par1', 'par2'),
    # Between , in , like, ilike, simiar, is isnull notnull
    ('left', 't_or'),
    ('left', 't_and'),
    ('left', 'diferente'),
    ('left', 'mayor', 'menor', 'mayori', 'menori'),
    ('right', 't_not')
)

from AST.Expresiones import *
from AST.SentenciasDML import *
reporteg = ''

def p_sql(p):
    'SQL : Sentencias_SQL'
    p[0] = Raiz(ListaErrores, p[1])

def p_sql2(p):
    'SQL : empty'
    p[0] = Raiz(ListaErrores)

def p_Sentencias_SQL_Sentencia_SQL(p):
    'Sentencias_SQL : Sentencias_SQL Sentencia_SQL'
    p[0] = p[1] + [p[2]]
    concatenar_gramatica('\n <TR><TD> SENTENCIAS_SQL ::= SENTENCIAS_SQL SENTENCIA_SQL </TD> <TD> { sentencias_sql.lista = sentencias_sql.lista.add(sentencia_sql.lista) } </TD></TR> ')


def p_Sentencias_SQL(p):
    'Sentencias_SQL : Sentencia_SQL'
    p[0] = [p[1]]
    concatenar_gramatica('\n <TR><TD> SENTENCIAS_SQL ::= SENTENCIA_SQL </TD> <TD> { sentencias_sql.lista = [sentencia_sql] } </TD></TR>')

def p_Sentencia_SQL_DML(p):
    'Sentencia_SQL : Sentencias_DML'
    p[0] = Sentencia("SentenciaDML", [p[1]])
    concatenar_gramatica('\n <TR><TD> SENTENCIA_SQL ::= SENTENCIAS_DML </TD> <TD> { sentencia_sql.inst = sentencias_dml.inst } </TD></TR>')

#def p_Sentencia_SQL_DML(p):
 #   'Sentencia_SQL : EXP pyc'
  #  p[0] = Sentencia("EXP", [p[1]])
   
def p_Sentencia_SQL_DDL(p):
    'Sentencia_SQL : Sentencias_DDL'
    p[0] = Sentencia("SentenciaDDL", [p[1]])
    concatenar_gramatica('\n <TR><TD> SENTENCIA_SQL ::= SENTENCIAS_DDL </TD> <TD> { sentencia_sql.inst = sentencias_dll.inst } </TD></TR>')

# -------------------------------------------------------------SENTENCIAS DML
def p_Sentencias_DML(p):
    '''Sentencias_DML : t_select Lista_EXP Select_SQL Condiciones GRP ORD pyc
                    | t_select asterisco Select_SQL Condiciones GRP ORD pyc
                    | t_insert t_into id Insert_SQL pyc
                    | t_update id t_set Lista_EXP Condiciones1 pyc
                    | t_delete t_from id Condiciones1 pyc
                    | t_use id pyc'''
    vaciar_lista()
    if p[1] == 'select':
        p[0] = Select(p[2], p[3], p[4], p[5], p[6], p.slice[2].lineno, find_column(input, p.slice[2]))
        concatenar_gramatica('\n <TR><TD> SENTENCIAS_DML ::= select' + str(p[2]) + 'SELECT_SQL ; </TD><TD> { sentencias_dml.inst = select(lista_exp.lista, Select_SQL.val,Condiciones.val)}  </TD></TR>')
    elif p[1] == 'insert':
        p[0] = Insert(p[3], p[4]['col'],p[4]['valores'], p.slice[1].lineno, find_column(input, p.slice[1]))
        concatenar_gramatica('\n <TR><TD> SENTENCIAS_DML ::= insert into id INSERT_SQL ; </TD> <TD> {sentencias_dml.inst = insert(id,Insert_SQL.inst)}  </TD></TR>')
    elif p[1] == 'update':
        p[0] = Update(p[2],p[4],p[5],p.slice[1].lineno, find_column(input, p.slice[1]))
        concatenar_gramatica('\n <TR><TD> SENTENCIAS_DML ::= update id set LISTA_EXP where EXP ; </TD> <TD> {sentencias_dml.inst = update(id, lista_exp.list, exp.val)} </TD></TR>')
    elif p[1] == 'delete':
        p[0] = Delete(p[3],p[4],p.slice[1].lineno, find_column(input, p.slice[1]))
        concatenar_gramatica('\n <TR><TD> SENTENCIAS_DML ::= delete from id CONDICIONES ; </TD> <TD> { sentencias_dml.inst = delete(id, Condiciones.val) } </TD></TR>')
    else: 
        p[0] = UseDB(p[2], p.slice[2].lineno, find_column(input, p.slice[2]))
        concatenar_gramatica('\n <TR><TD> SENTENCIAS_DML ::= use database id ; </TD>  <TD> {sentencias_dml.inst = use(id)} </TD></TR>')

def p_Select_SQL(p):
    'Select_SQL : t_from Table_Expression'
    p[0] = p[2]
    concatenar_gramatica('\n <TR><TD> SELECT_SQL ::= from TABLE_EXPRESSION CONDICIONES </TD> <TD> { select_sql.val = Table_Expression.val } </TD></TR>')


def p_Select2_SQL(p):
    'Select_SQL : empty'
    p[0] = []
    concatenar_gramatica('\n <TR><TD> SELECT_SQL ::= EMPTY </TD>  <TD> { select_sql.val = empty.val }</TD></TR>')


def p_Table_Expression(p):
    '''Table_Expression : Alias_Tabla
                        | Subqueries'''
    p[0] = p[1]
    concatenar_gramatica('\n <TR><TD> TABLE_EXPRESSION ::= ' + str(p[1]) + '</TD> <TD> { table_expression.val = ' + str(p[1]) + '.val } </TD></TR>')


def p_Alias_Tabla(p):
    '''Alias_Tabla :  Lista_ID
                | Lista_Alias'''
    p[0] = p[1]
    concatenar_gramatica('\n <TR><TD> ALIAS_TABLA ::= ' + str(p[1]) + '</TD> <TD> { alias_tabla.val = ' + str(p[1]) + '.list } </TD></TR>')

def p_Subqueries(p):
    '''Subqueries : par1 t_select  par2'''
    concatenar_gramatica('\n <TR><TD> SUBQUERIES ::= ( select )</TD> <TD> { subqueries.inst = select() } </TD></TR>')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INSERT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def p_Insert_SQL(p):
    'Insert_SQL : par1 Lista_ID par2 t_values par1 Lista_EXP par2'
    p[0] = {'col':p[2],'valores':p[6]}
    concatenar_gramatica('\n <TR><TD> INSERT_SQL ::= ( LISTA_ID ) values ( LISTA_EXP ) </TD> <TD> { insert_sql.inst = insert.lista.add(lista_id.lista,lista_exp.lista)} </TD></TR>')

def p_Insert_SQL2(p):
    'Insert_SQL : t_values par1 Lista_EXP par2'
    p[0] = {'col':None,'valores':p[3]}
    concatenar_gramatica('\n <TR><TD> INSERT_SQL ::= values ( LISTA_EXP ) </TD>  <TD> { insert_sql.inst = insert1(lista_exp.lista)} </TD></TR>')

def p_Condiciones(p):
    '''Condiciones : t_where EXP
            | empty'''
    if len(p) == 3:
        p[0] = Where(p[2], p.slice[1].lineno, find_column(input, p.slice[1]))
        concatenar_gramatica('\n <TR><TD> CONDICIONES ::= where EXP  </TD>  <TD> condiciones.val = exp.val </TD></TR>')
    else:
        p[0] = []
        concatenar_gramatica('\n <TR><TD> INSERT_SQL ::= EMPTY </TD> <TD> { insert_sql.val = empty.val }</TD></TR>')

def p_Condiciones1(p):
    '''Condiciones1 : t_where EXP
            | empty'''
    if len(p) == 3:
        p[0] = p[2]
        concatenar_gramatica('\n <TR><TD> CONDICIONES ::= where EXP  </TD>  <TD> condiciones.val = exp.val </TD></TR>')
    else:
        p[0] = p[1]
        concatenar_gramatica('\n <TR><TD> INSERT_SQL ::= EMPTY </TD> <TD> { insert_sql.val = empty.val }</TD></TR>')


# ---------------------------- Group, having and order by --------------
def p_GRP(p):
    '''GRP : t_group t_by Lista_ID
           | t_group t_by Lista_ID HV
           | empty'''
    if len(p) == 5:
        p[0] = p[3] + p[4]
    elif len(p) == 4:
        p[0] = p[3]

def p_HV(p):
    '''HV : t_having EXP'''
    p[0] = p[2]

def p_ORD(p):
    '''ORD : t_order t_by LSORT
           | t_order t_by LSORT LMT
           | empty'''
    if len(p) == 4:
        p[0] = p[3]
    elif len(p) == 5:
        p[0] = p[3] + [p[4]]


def p_L_SORT(p):
    '''LSORT : LSORT coma SORT
                | SORT'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_SORT(p):
    '''SORT : EXP AD NFL
            | EXP AD
            | EXP'''
    if len(p) == 4:
        p[0] = Order(p[1], p[2], p[3], p.slice[1].lineno, find_column(input, p.slice[1]))
    elif len(p) == 3:
        p[0] = Order(p[1], p[2], p.slice[1].lineno, find_column(input, p.slice[1]))
    else:
        p[0] = Order(p[1], p.slice[1].lineno, find_column(input, p.slice[1]))

def p_AD(p):
    '''AD : t_asc
          | t_desc'''
    p[0] = p[1]


def p_NFL(p):
    '''NFL : t_nulls t_first
           | t_nulls t_last'''
    p[0] = p[2]

def p_LMT(p):
    '''LMT : t_limit NAL t_offset entero
           | t_limit NAL
           | t_offset entero '''
    if len(p) == 5:
        p[0] = p[1] + ':' + p[2] + ':' + p[3] + ':' + p[4]
    else:
        p[0] = p[1] + ':' + p[2]

def p_NAL(p):
    '''NAL : entero
           | t_all '''
    p[0] = p[1]

# ---------------------------- Sentencias DDL y Enum Type --------------
def p_Sentencias_DDL(p):
    '''Sentencias_DDL : t_show t_databases Show_DB_Like_Char pyc
                    | Enum_Type
                    | t_drop Drop pyc
                    | t_alter Alter pyc
                    | t_create Create pyc'''
    if p[1].__class__.__name__ == 'CreateType':
        p[0] = p[1]
        concatenar_gramatica('\n <TR><TD> SENTENCIAS_DDL ::= ENUM_TYPE </TD>  <TD> { sentencias_ddl.inst = enum_type.inst } </TD></TR>')
    elif p[1].upper() == 'SHOW':
        p[0] = DDL.ShowDatabases(p.slice[1].lineno, find_column(input, p.slice[1]), p[3])
        concatenar_gramatica('\n <TR><TD> SENTENCIAS_DDL ::= show databases SHOW_DB_LIKE_CHAR ; </TD>  <TD> { sentencias_ddl.inst = show() } </TD></TR>')
    elif p[1].upper() == 'CREATE':
        p[0] = p[2]
        concatenar_gramatica('\n <TR><TD> SENTENCIAS_DDL ::= create CREATE ; </TD>  <TD> { sentencias_ddl.inst = create.inst} </TD></TR>')
    elif p[1].upper() == 'DROP':
        p[0] = p[2]
        concatenar_gramatica('\n <TR><TD> SENTENCIAS_DDL ::= drop Drop ; </TD> <TD> { sentencias_ddl.inst = drop.inst } </TD></TR>')
    elif p[1].upper() == 'ALTER':
        p[0] = p[2]
        concatenar_gramatica('\n <TR><TD> SENTENCIAS_DDL ::= alter ALTER ; </TD>  <TD> { sentencias_ddl.inst = alter.inst }</TD></TR>')
    else:
        p[0] = None

def p_show_db_like_regex(p):
    '''Show_DB_Like_Char : t_like char 
                        | empty '''
    if len(p) == 3:
        p[0] = p[2]
        concatenar_gramatica('\n <TR><TD> SHOW_DB_LIKE_CHAR ::= like char </TD>  <TD> { show_db_like_char.inst = char }</TD></TR>')
    else:
        p[0] = None
        concatenar_gramatica('\n <TR><TD> SHOW_DB_LIKE_CHAR ::= EMPTY </TD>  <TD> { show_db_like_char.inst = None }</TD></TR>')

def p_Enum_Type(p):#Agregado
    'Enum_Type : t_create t_type id t_as t_enum par1 Lista_Enum par2 pyc'
    p[0] = DDL.CreateType(p.slice[1].lineno, find_column(input, p.slice[1]), p[3].lower(), p[7])
    concatenar_gramatica('\n <TR><TD> ENUM_TYPE ::= create type id as enum ( LISTA_ENUM ) ; </TD>  <TD> { enum_type.inst = createType(id,lista_Enum.val) } </TD></TR>')

def p_Drop(p): #Agregado
    '''Drop : t_database DropDB id
            | t_table  id '''
    if p[1].lower() == 'database':
        p[0] = DDL.DropDatabase(p.slice[1].lineno, find_column(input, p.slice[1]), p[3], p[2])
        concatenar_gramatica('\n <TR><TD> DROP ::= database DROPDB id  </TD> <TD> { drop.inst = dropBD( id) } </TD></TR>')
    else:
        p[0] = DDL.DropTable(p.slice[1].lineno, find_column(input, p.slice[1]), p[2]) 
        concatenar_gramatica('\n <TR><TD> DROP ::= table  id  </TD>  <TD> {drop.inst = dropTb( id )} </TD></TR>')
   
def p_DropDB(p): #Agregado
    '''DropDB : t_if t_exists
            | empty'''
    if p[1].lower() == 'if':
        p[0] = True
        concatenar_gramatica('\n <TR><TD> DROPDB ::= if exists </TD>  <TD> { dropdb.val = True} </TD></TR>')
    else:
        p[0] = False
        concatenar_gramatica('\n <TR><TD> DROPDB ::= EMPTY </TD> <TD> { dropdb.val = False } </TD></TR>')

def p_Alter(p): #Agregado
    '''Alter : t_database id AlterDB
            | t_table id AlterTB '''
    if p[1] == 'database':
        p[0] = DDL.AlterDatabase(p.slice[1].lineno, find_column(input, p.slice[1]), p[2], p[3]['nuevo_nombre_DB'], p[3]['owner'])
        concatenar_gramatica('\n <TR><TD> ALTER ::= database id ALTERDB </TD> <TD> alter.inst = alterDB( id,alterdb.inst ) </TD></TR>')
    else:
        p[0] = DDL.AlterTable(p.slice[1].lineno, find_column(input, p.slice[1]), p[2], p[3]) 
        concatenar_gramatica('\n <TR><TD> ALTER ::= table id ALTERTB </TD> <TD>  alter.inst = altertb(id, altertb.inst)  </TD></TR>')

def p_AlterDB(p): #Agregado
    ''' AlterDB : t_rename t_to id
                | t_owner t_to SesionDB '''
    if p[1] == 'rename':
        p[0] = {'nuevo_nombre_DB':p[3], 'owner': None}
        concatenar_gramatica('\n <TR><TD> ALTERDB ::= rename to id </TD> <TD> { alterdb.val = rename id } </TD></TR>')
    else:
        p[0] = {'nuevo_nombre_DB': None, 'owner':p[3]} 
        concatenar_gramatica('\n <TR><TD> ALTERDB ::= owner to SESIONDB </TD> <TD> { alterdb.val = owner sessiondb.val} </TD> </TR>')

def p_SesionDB(p): #Agregado
    ''' SesionDB : id
                | t_current_user
                | t_session_user '''
    if p[1].lower() == 'current_user':
        concatenar_gramatica('\n <TR><TD> SESSIONDB ::= current_user </TD>  <TD> { sessiondb.val = current_user } </TD></TR>')
    elif p[1].lower() == 'session_user': 
        concatenar_gramatica('\n <TR><TD> SESSIONDB ::= session_user </TD> <TD> { sessiondb.val = session_user } </TD></TR>')
    else: 
        concatenar_gramatica('\n <TR><TD> SESSIONDB ::= id </TD> <TD> { sessiondb.val = id } </TD></TR>')
    p[0]=p[1]

def p_AlterTB(p): #Agregado
    ''' AlterTB : t_add Add_Opc
                | t_drop Drop_Opc
                | t_alter t_column Alter_Column
                | t_rename t_column id t_to id '''
    if p[1] == 'add':
        p[0] = p[2]
        concatenar_gramatica('\n <TR><TD> ALTERTB ::= add ADD_OPC </TD>  <TD> { altertb.inst = add(add_Opc.val) } </TD></TR>')
    elif p[1] == 'drop':
        p[0] = p[2]
        concatenar_gramatica('\n <TR><TD> ALTERTB ::= drop DROP_OPC </TD> <TD> { altertb.inst =  drop(drop_opc.val) } </TD></TR>')
    elif p[1] == 'alter': 
        p[0] = p[3]
        concatenar_gramatica('\n <TR><TD> ALTERTB ::= alter column ALTER_COLUMN </TD> <TD> { altertb.inst = alter(alter_column.val) } </TD></TR>')
    elif p[1] == 'rename':
        p[0] = DDL.AlterTBRename(p.slice[1].lineno, find_column(input, p.slice[1]), p[3], p[5])
        concatenar_gramatica('\n <TR><TD> ALTERTB ::= rename column id to id </TD> <TD> { altertb.inst = rename(id1,id2) } </TD></TR>')

def p_Add_Opc(p): #Agregado
    '''Add_Opc : t_column id Tipo
               | Constraint_AlterTB t_foreign t_key par1 Lista_ID par2 t_references id par1 Lista_ID par2
               | Constraint_AlterTB t_unique par1 id par2
               | Constraint_AlterTB t_check EXP '''
    if p[2].lower() == 'foreign':
        p[0] = DDL.AlterTBAdd(p.slice[2].lineno, find_column(input, p.slice[2]), 2, {'id_constraint': p[1], 'Lista_ID': p[5], 'id_ref': p[8], 'Lista_ID_ref': p[10]})
        concatenar_gramatica('\n <TR><TD> ADD_OPC ::= CONSTRAINT_ALTERTB foreign key ( id ) references id par1 Lista_ID par2 </TD> <TD> { add_opc.isnt = foreign(id1,id2)} </TD></TR>')
    elif p[2].lower() == 'unique':
        p[0] = DDL.AlterTBAdd(p.slice[2].lineno, find_column(input, p.slice[2]), 3, {'id_constraint': p[1], 'id': p[4]})
        concatenar_gramatica('\n <TR><TD> ADD_OPC ::= CONSTRAINT_ALTERTB unique ( id ) </TD> <TD> { add_opc.inst = constraint(id1,id2)} </TD></TR>')
    elif p[2].lower() == 'check': 
        p[0] = DDL.AlterTBAdd(p.slice[2].lineno, find_column(input, p.slice[2]), 4, {'id_constraint': p[1], 'EXP': p[3]})
        concatenar_gramatica('\n <TR><TD> ADD_OPC ::= CONSTRAINT_ALTERTB check EXP </TD> <TD> {add_opc.inst = check( exp.val )} </TD></TR>')
    else: #p[1].lower() == 'column':
        p[0] = DDL.AlterTBAdd(p.slice[1].lineno, find_column(input, p.slice[1]), 1, {'id': p[2], 'tipo': p[3]})
        concatenar_gramatica('\n <TR><TD> ADD_OPC ::= column id TIPO </TD> <TD> { add_opc.inst = column(id, tipo.type) } </TD></TR>')

def p_Constraint_AlterTB(p): #Agregado
    '''Constraint_AlterTB : t_constraint id
                            | empty'''
    if p[1].lower() == 'constraint':
        p[0] = p[2]
        concatenar_gramatica('\n <TR><TD> CONSTRAINT_ALTERTB ::= constraint id </TD> <TD> { constraint_altertb.inst = id } </TD></TR>')
    else:
        p[0] = None
        concatenar_gramatica('\n <TR><TD> CONSTRAINT_ALTERTB ::= EMPTY </TD> <TD> { constraint_altertb.inst = None } </TD></TR>')

def p_Drop_Opc(p): #Agregado
    ''' Drop_Opc :  t_column id
                 |  t_constraint id '''
    if p[1] == 'column':
        p[0] = DDL.AlterTBDrop(p.slice[1].lineno, find_column(input, p.slice[1]), 1, p[2])
        concatenar_gramatica('\n <TR><TD> DROP_OPC ::= column id TIPO </TD> <TD> {drop_opc.val = column,id }</TD></TR>')
    elif p[1] == 'constraint':
        p[0] = DDL.AlterTBDrop(p.slice[1].lineno, find_column(input, p.slice[1]), 2, p[2])
        concatenar_gramatica('\n <TR><TD> DROP_OPC ::= foreign key ( id ) references id </TD> <TD> { drop_opc.val = constraint,id}  </TD></TR>')

def p_Alter_Column(p): #Agregado
    ''' Alter_Column :   id t_set t_not t_null
                     |   Alter_Columns'''
    if len(p) == 5:
        p[0] = DDL.AlterTBAlter(p.slice[1].lineno, find_column(input, p.slice[1]), p[1].lower(), None)
        concatenar_gramatica('\n <TR><TD> ALTER_COLUMN ::= id set not null </TD> <TD> { alter_column.val = id} </TD></TR>')
    else:
        p[0] = DDL.AlterTBAlter(p.slice[1].lineno, find_column(input, p.slice[1]), None, p[1])
        concatenar_gramatica('\n <TR><TD> ALTER_COLUMN ::= ALTER_COLUMNS </TD> <TD> { alter_column.val = alter_columns.val } </TD></TR>')

def p_Alter_Columns(p): #Agregado
    ''' Alter_Columns : Alter_Columns coma Alter_Column1
                    | Alter_Column1'''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
        concatenar_gramatica('\n <TR><TD> ALTER_COLUMNS ::= ALTER_COLUMNS , ALTER_COLUMN1 </TD> <TD> { alter_columns.lista.add(alter_column1.val) } </TD></TR>')
    else:
        p[0] = [p[1]] 
        concatenar_gramatica('\n <TR><TD> ALTER_COLUMNS ::= ALTER_COLUMN1 </TD> <TD> { alter_columns.lista = [alter_column.val]} </TD></TR>')

def p_Alter_Colum1(p): #Agregado
    '''Alter_Column1 :  id t_type t_varchar par1 entero par2
                    | t_alter t_column id t_type t_varchar par1 entero par2'''
    if p[1].lower() != 'alter':
        p[0] = {
            'nombre_columna': p[1].lower(),
            'entero': p[5]
        }
        concatenar_gramatica('\n <TR><TD> ALTER_COLUMN1 ::= alter column id type varchar ( entero ) </TD> <TD> { alter_Column.inst = alter_column(id,varchar,entero) }</TD></TR>')
    else:
        p[0] = {
            'nombre_columna': p[3].lower(),
            'entero': p[7]
        } 
        concatenar_gramatica('\n <TR><TD> ALTER_COLUMN1 ::= id type varchar ( entero ) </TD> <TD> { alter_Column.inst = alter_Column(id,varchar,entero)} </TD></TR>')

def p_Create(p):#Agregado
    'Create : CreateDB'
    p[0] = p[1]
    concatenar_gramatica('\n <TR><TD> CREATE ::= CREATEDB </TD> <TD> { create.val = createDB.val } </TD></TR>')

def p_Create1(p):
    'Create : CreateTB '
    p[0] = p[1]
    concatenar_gramatica('\n <TR><TD> CREATE ::= CREATETB </TD>  <TD> { create.val = createtb.val }</TD></TR>')

def p_CreateDB(p):#Agregado
    'CreateDB : OrReplace_CreateDB t_database IfNotExist_CreateDB id Sesion '
    p[0] = DDL.CreateDatabase(p.slice[1].lineno, find_column(input, p.slice[1]), p[4], p[1], p[3], p[5]['owner'], p[5]['mode'])
    concatenar_gramatica('\n <TR><TD> CREATEDB ::= ORREPLACECREATEDB database IFNOTEXISTCREATEDB id SESION </TD> <TD> { createdb.inst = createDB() } </TD></TR>')

def p_CreateDB_or_replace(p):#Agregado
    '''OrReplace_CreateDB : t_or t_replace
                            | empty '''
    if len(p) == 3:
        p[0] = True
        concatenar_gramatica('\n <TR><TD> ORREPLACECREATEDB ::= or replace </TD>  <TD> { orreplacecreatedb.inst = True } </TD></TR>')
    else:
        p[0] = False
        concatenar_gramatica('\n <TR><TD> ORREPLACECREATEDB ::= EMPTY </TD> <TD> { orreplacecreatedb.inst = False } </TD></TR>')

def p_IfNotExist_CreateDB(p):#Agregado
    ''' IfNotExist_CreateDB : t_if t_not t_exists
               | empty '''
    if len(p) == 4:
        p[0] = True
        concatenar_gramatica('\n <TR><TD> IFNOTEXIST_CREATEDB ::= if not exists </TD>  <TD> { ifnotexist.inst = True } </TD></TR>')
    else:
        p[0] = False
        concatenar_gramatica('\n <TR><TD> IFNOTEXIST_CREATEDB ::= EMPTY </TD>  <TD> { ifnotexist.inst = False } </TD></TR>')

def p_Sesion(p):#Agregado
    ''' Sesion : t_owner Op_Sesion Sesion_mode
                | t_mode Op_Mode
                | empty '''
    if len(p) == 4:
        p[0] = {'mode': p[3]['mode'], 'owner': p[2]}
        concatenar_gramatica('\n <TR><TD> SESION ::= owner OP_SESION SESION_MODE </TD> <TD> { session.val = session_mode.val.add(Op_Sesion.val)} </TD></TR>')
    elif len(p) == 3:
        p[0] = {'mode': p[2], 'owner': None}
        concatenar_gramatica('\n <TR><TD> SESION ::= mode OP_MODE </TD> <TD> { session.val = op_mode.val} </TD></TR>')
    else:
        p[0] = {'mode': 1, 'owner': None}
        concatenar_gramatica('\n <TR><TD> SESION ::= EMPTY </TD>  <TD> { session.val = empty.val } </TD></TR>')

def p_Op_Sesion(p):#Agregado
    ''' Op_Sesion : igual char
            | char  '''
    if len(p) == 3:
        p[0] = p[2]
        concatenar_gramatica('\n <TR><TD> OP_SESION ::= = char </TD> <TD> { Op_sesion.val = char } </TD></TR>')
    else:
        p[0] = p[1]
        concatenar_gramatica('\n <TR><TD> OP_SESION ::= char </TD> <TD> { Op_sesion.val = char } </TD></TR>')

def p_Sesion_mode(p):#Agregado
    ''' Sesion_mode : t_mode Op_Mode
                    | empty '''
    if len(p) == 3:
        p[0] = {'mode': p[2], 'owner': None}
        concatenar_gramatica('\n <TR><TD> SESION_MODE ::= mode OP_MODE </TD> <TD> {sesion_mode.val = mode op_mode.val} </TD></TR>')
    else:
        p[0] = {'mode': 1, 'owner': None}
        concatenar_gramatica('\n <TR><TD> SESION_MODE ::= EMPTY </TD> <TD> { sesion_mode.val = empty.val } </TD></TR>')

def p_Op_Mode(p):#Agregado
    ''' Op_Mode : igual entero
                | entero  '''
    if len(p) == 3:
        p[0] = p[2]
        concatenar_gramatica('\n <TR><TD> OP_MODE ::= = entero </TD> <TD> { op_mode.val = entero } </TD></TR>')
    else:
        p[0] = p[1]
        concatenar_gramatica('\n <TR><TD> OP_MODE ::= entero </TD> <TD> { op_mode.val = entero } </TD></TR>')

def p_CreateTB(p): #Agregado
    'CreateTB : t_table id par1 Columnas par2 Inherits '
    p[0] = DDL.CreateTable(p.slice[1].lineno, find_column(input, p.slice[1]), p[2], p[4], p[6])
    concatenar_gramatica('\n <TR><TD> CREATETB ::= table id ( COLUMNAS ) INHERITS </TD> <TD> {createtb.inst = createtb(id,columnas.val,inherits.val)} </TD></TR>')

def p_Inherits(p):#Agregado
    ''' Inherits : t_inherits par1 id par2
               | empty '''
    if len(p) == 5:
        p[0] = p[3]
        concatenar_gramatica('\n <TR><TD> INHERITS ::= inherits ( id ) </TD> <TD> { inherits.inst = inherits(id) } </TD></TR>')
    else:
        p[0] = None
        concatenar_gramatica('\n <TR><TD> INHERITS ::= EMPTY </TD>  <TD> { inherits.inst = None } </TD></TR>')
    
def p_Columnas(p): #Agregado
    ''' Columnas : Columnas coma Columna
                | Columna '''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
        concatenar_gramatica('\n <TR><TD> COLUMNAS ::= COLUMNAS , COLUMNA </TD>  <TD> {columnas.val = concatenar(columna.aux , columna.val)}</TD></TR>')
    else:
        p[0] = [p[1]]
        concatenar_gramatica('\n <TR><TD> COLUMNAS ::= COLUMNA </TD> <TD> columnas.aux = columna.val </TD></TR>')

def p_Columna(p): #Agregado
    ''' Columna : id Tipo Cond_CreateTB
                | Constraint'''
    if len(p) == 4:
        p[0] = DDL.CreateTableColumn(p.slice[1].lineno, find_column(input, p.slice[1]), p[1], p[2], p[3])
        concatenar_gramatica('\n <TR><TD> COLUMNA ::= id TIPO COND_CREATETB </TD> <TD> {columna.val = cond_createtb.val} </TD></TR>')
    else:
        p[0] = p[1]
        concatenar_gramatica('\n <TR><TD> COLUMNA ::= CONSTRAINT </TD> <TD> { columna.val = constraint.val} </TD></TR>')

def p_Cond_CreateTB(p): #Agregado
    ''' Cond_CreateTB : Constraint_CreateTB t_default id Cond_CreateTB
                        | Constraint_CreateTB t_not t_null Cond_CreateTB
                        | Constraint_CreateTB t_null Cond_CreateTB
                        | Constraint_CreateTB t_unique Cond_CreateTB
                        | Constraint_CreateTB t_check par1 EXP par2 Cond_CreateTB
                        | Constraint_CreateTB t_primary t_key Cond_CreateTB
                        | Constraint_CreateTB t_references id Cond_CreateTB
                        | empty'''
    if len(p) == 2:
        p[0] = [] 
        concatenar_gramatica('\n <TR><TD> COND_CREATETB ::=  EMPTY  </TD>  <TD> { cond_createtb.val = empty.val } </TD></TR>')
    elif p[2].lower() == 'default':
        p[4].append(DDL.CreateTableConstraint(p.slice[2].lineno, find_column(input, p.slice[2]), p[1], 1, p[3]))
        p[0] = p[4]
        concatenar_gramatica('\n <TR><TD> COND_CREATETB ::=  CONSTRAINT_CREATETB default id COND_CREATETB </TD>  <TD> { cond_createtb.val = id cond_createtb.val } </TD></TR>')
    elif p[2].lower() == 'not':
        p[4].append(DDL.CreateTableConstraint(p.slice[2].lineno, find_column(input, p.slice[2]), p[1], 2, False))
        p[0] = p[4]
        concatenar_gramatica('\n <TR><TD> COND_CREATETB ::=  CONSTRAINT_CREATETB not null COND_CREATETB </TD>  <TD> { cond_createtb.val = cond_createtb.val }  </TD></TR>')
    elif p[2].lower() == 'null':
        p[3].append(DDL.CreateTableConstraint(p.slice[2].lineno, find_column(input, p.slice[2]), p[1], 2, True))
        p[0] = p[3]
        concatenar_gramatica('\n <TR><TD> COND_CREATETB ::=  CONSTRAINT_CREATETB null COND_CREATETB </TD> { cond_createtb.val = cond_createtb.val } </TD></TR>')
    elif p[2].lower() == 'unique':
        p[3].append(DDL.CreateTableConstraint(p.slice[2].lineno, find_column(input, p.slice[2]), p[1], 3, None))
        p[0] = p[3]
        concatenar_gramatica('\n <TR><TD> COND_CREATETB ::=  CONSTRAINT_CREATETB t_unique COND_CREATETB </TD> { cond_createtb.val = id opc_constraint.val cond_createtb.val }   <TD> </TD></TR>')
    elif p[2].lower() == 'check':
        p[6].append(DDL.CreateTableConstraint(p.slice[2].lineno, find_column(input, p.slice[2]), p[1], 4, p[4]))
        p[0] = p[6]
        concatenar_gramatica('\n <TR><TD> COND_CREATETB ::=  CONSTRAINT_CREATETB t_check par1 EXP par2 COND_CREATETB </TD> { cond_createtb.val = id opc_constraint.val cond_createtb.val }   <TD> </TD></TR>')
    elif p[2].lower() == 'primary':
        p[4].append(DDL.CreateTableConstraint(p.slice[2].lineno, find_column(input, p.slice[2]), p[1], 6, None))
        p[0] = p[4]
        concatenar_gramatica('\n <TR><TD> COND_CREATETB ::=  CONSTRAINT_CREATETB primary key COND_CREATETB </TD>  <TD> { cond_createtb.val = cond_createtb.val } </TD></TR>')
    else: #if p[2].lower() == 'references':
        p[4].append(DDL.CreateTableConstraint(p.slice[2].lineno, find_column(input, p.slice[2]), p[1], 5, {'nombre_ref': p[3], 'lista_columnas': None, 'lista_columnas_ref': None}))
        p[0] = p[4]
        concatenar_gramatica('\n <TR><TD> COND_CREATETB ::=  CONSTRAINT_CREATETB references id COND_CREATETB </TD> <TD> { cond_createtb.val = id cond_createtb.val } </TD></TR>')

def p_Constraint_CreateTB(p): #Agregado
    '''Constraint_CreateTB : t_constraint id
                            | empty'''
    if p[1].lower() == 'constraint':
        p[0] = p[2]
        concatenar_gramatica('\n <TR><TD> CONSTRAINT_CREATETB ::= constraint id </TD> <TD> { constraint_createtb.inst = id } </TD></TR>')
    else:
        p[0] = None
        concatenar_gramatica('\n <TR><TD> CONSTRAINT_CREATETB ::= EMPTY </TD> <TD> { constraint_createtb.inst = None } </TD></TR>')

def p_Constraint(p): #Agregado
    ''' Constraint : Constraint_CreateTB t_unique par1 Lista_ID par2
                    | Constraint_CreateTB t_check par1 EXP par2
                    | Constraint_CreateTB t_primary t_key par1 Lista_ID par2
                    | Constraint_CreateTB t_foreign t_key par1 Lista_ID par2 t_references id par1 Lista_ID par2
                    | empty '''
    if p[2].lower() == 'unique':
        p[0] = DDL.CreateTableConstraint(p.slice[2].lineno, find_column(input, p.slice[2]), p[1], 3, p[4])
        concatenar_gramatica('\n <TR><TD> CONSTRAINT ::= CONSTRAINT_CREATETB unique ( LISTA_ID )  </TD>  <TD> {constraint.inst = unique(lista_id.list)}</TD></TR>')
    elif p[2].lower() == 'check':
        p[0] = DDL.CreateTableConstraint(p.slice[2].lineno, find_column(input, p.slice[2]), p[1], 4, p[4])
        concatenar_gramatica('\n <TR><TD> CONSTRAINT ::= CONSTRAINT_CREATETB check ( EXP )  </TD>  <TD> { constraint.inst = check(exp.val)} </TD></TR>')
    elif p[2].lower() == 'primary':
        p[0] = DDL.CreateTableConstraint(p.slice[2].lineno, find_column(input, p.slice[2]), p[1], 6, p[5])
        concatenar_gramatica('\n <TR><TD> CONSTRAINT ::= CONSTRAINT_CREATETB primary key ( LISTA_ID ) </TD>  <TD> {constraint.inst = primary(lista_id.list)} </TD> </TR>')
    elif p[2].lower() == 'foreign':
        p[0] = DDL.CreateTableConstraint(p.slice[2].lineno, find_column(input, p.slice[2]), p[1], 5, {'lista_columnas': p[5], 'lista_columnas_ref': p[10], 'nombre_ref': p[8]}) 
        concatenar_gramatica('\n <TR><TD> CONSTRAINT ::= CONSTRAINT_CREATETB foreign key ( LISTA_ID ) references id ( LISTA_ID )  </TD>  <TD> { constraint.inst = foreign(lista_id.lista,id,lista_id.lista)} </TD></TR>')
    else:
        p[0] = None 
        concatenar_gramatica('\n <TR><TD> CONSTRAINT ::=  EMPTY </TD> <TD> { constraint.inst = empty.val } </TD></TR>')

def p_Tipo(p):
    ''' Tipo : t_smallint
              | t_integer
              | t_bigint
              | t_decimal
              | t_numeric par1 entero par2
              | t_real
              | t_double t_precision
              | t_money
              | t_character t_varying par1 entero par2
              | t_varchar par1 entero par2
              | t_character par1 entero par2
              | t_charn par1 entero par2
              | t_text
              | t_boolean
              | t_date
              | id'''
    if p[1].lower() == 'smallint':
        p[0] = {
            'tipo': 'smallint',
            'size': 2
        }
    elif p[1].lower() == 'integer':
        p[0] = {
            'tipo': 'integer',
            'size': 4
        }
    elif p[1].lower() == 'bigint':
        p[0] = {
            'tipo': 'bigint',
            'size': 8
        }
    elif p[1].lower() == 'decimal':
        p[0] = {
            'tipo': 'decimal',
            'size': 8
        }
    elif p[1].lower() == 'numeric':
        p[0] = {
            'tipo': 'numeric',
            'size': p[3]
        }
    elif p[1].lower() == 'real':
        p[0] = {
            'tipo': 'real',
            'size': 4
        }
    elif p[1].lower() == 'double':
        p[0] = {
            'tipo': 'double',
            'size': 8
        }
    elif p[1].lower() == 'money':
        p[0] = {
            'tipo': 'money',
            'size': 8
        }
    elif p[1].lower() == 'character':
        if len(p) == 6:
            p[0] = {
                'tipo': 'character varying',
                'size': p[4]
            }
        else:
            p[0] = {
                'tipo': 'character',
                'size': p[3]
            }
    elif p[1].lower() == 'varchar':
        p[0] = {
            'tipo': 'varchar',
            'size': p[3]
        }
    elif p[1].lower() == 'char':
        p[0] = {
            'tipo': 'char',
            'size': p[3]
        }
    elif p[1].lower() == 'text':
        p[0] = {
            'tipo': 'text',
            'size': 1998
        }
    elif p[1].lower() == 'boolean':
        p[0] = {
            'tipo': 'boolean',
            'size': 1
        }
    elif p[1].lower() == 'date':
        p[0] = {
            'tipo': 'date',
            'size': 4
        }
    else:
        p[0] = {
            'tipo': p[1],
            'size': 1998
        }
    concatenar_gramatica('\n <TR><TD> TIPO ::= ' + str(p[1]) + '</TD>  <TD> { tipo.type = ' + str(p[1]) + '  } </TD></TR>')

def p_Valor(p):
    ''' Valor : decimal
            | entero
            | string
            | char
            | t_true
            | t_false'''
    p[0] = Expression(p[1], p.slice[1].lineno, find_column(input, p.slice[1]), p.slice[1].type)
    concatenar_gramatica('\n <TR><TD> VALOR ::= ' + str(p[1]) + '</TD> <TD> { Valor.val = '  + str(p[1]) +  '} </TD></TR>')


def p_Valor2(p):
    'Valor : id'
    p[0] = Expression(p[1], p.slice[1].lineno, find_column(input, p.slice[1]))
    concatenar_gramatica('\n <TR><TD> VALOR ::= id </TD>  <TD> { valor.val = '  + str(p[1]) +  ' } </TD></TR>')

def p_empty(p):
    'empty :'
    p[0] = ''
    concatenar_gramatica('\n <TR><TD> EMPTY ::= epsilon </TD>  <TD> { }  </TD></TR>')

# ----------------------------EXPRESIONES Y OPERACIONES---------------------------------------------------------------

def p_aritmeticas(p):
    '''EXP : EXP mas EXP
           | EXP menos EXP
           | EXP asterisco EXP
           | EXP div EXP
           | EXP pot EXP
           | EXP porcentaje EXP'''
    p[0] = Expression(p[1], p[3], p.slice[2].value, p.slice[2].lineno, find_column(input, p.slice[2]),'Aritmetica')
    concatenar_gramatica('\n <TR><TD> EXP ::= EXP' + str(p[2]) + ' EXP </TD>  <TD> { Exp = Exp1.val ' + str(p[2]) + ' Exp2.val } </TD></TR>')

def p_parentesis(p):
    'EXP : par1 EXP par2'
    p[0] = p[2]
    concatenar_gramatica('\n <TR><TD> EXP ::= ( EXP ) </TD>  <TD> { exp.val = exp1.val }  </TD></TR>')


def p_funciones(p):
    'EXP : id par1 Lista_EXP par2'
    p[0] = p[1]
    Expression(p[1], p[2], p.slice[2].lineno, find_column(input, p.slice[2]))
    concatenar_gramatica('\n <TR><TD> EXP ::= ( EXP ) </TD>  <TD> { exp.val = exp1.val }  </TD></TR>')


def p_relacionales(p):
    '''EXP : EXP mayor EXP
           | EXP mayori EXP
           | EXP menor EXP
           | EXP menori EXP
           | EXP igual EXP
           | EXP diferente EXP
           | EXP diferentede EXP'''
    p[0] = Expression(p[1], p[3], p.slice[2].value, p.slice[2].lineno, find_column(input, p.slice[2]), 'Relacional')
    concatenar_gramatica('\n <TR><TD> EXP ::= EXP' + str(p[2]) + ' EXP </TD> <TD> { Exp = Exp1.val ' + str(p[2]) + ' Exp2.val } </TD></TR>')

def p_logicos(p):
    '''EXP : EXP t_and EXP
       | EXP t_or EXP
       '''
    p[0] = Expression(p[1], p[3], p.slice[2].value, p.slice[2].lineno, find_column(input, p.slice[2]), 'Logica')
    concatenar_gramatica('\n <TR><TD> EXP ::= EXP' + str(p[2]) + ' EXP </TD>  <TD> { Exp = Exp1.val ' + str(p[2]) + ' Exp2.val } </TD></TR>')

def p_unario(p):
    '''EXP : mas EXP  %prec umas
           | menos EXP  %prec umenos
           | t_not EXP'''
    if p[1] == 'not': 
        p[0] = Expression(p.slice[1].value, p[2], p.slice[1].lineno, find_column(input, p.slice[1]), 'unario')
        concatenar_gramatica('\n <TR><TD> EXP ::= not EXP </TD>  <TD> { Exp =  Exp1.val  } </TD></TR>')
    else: 
        p[0] = Expression(p.slice[1].value, p[2], p.slice[1].lineno, find_column(input, p.slice[1]), 'unario')
        concatenar_gramatica('\n <TR><TD> EXP ::= ' + str(p[1]) + 'EXP %prec' +  str(p[2]) +'</TD> <TD> { exp = exp1.val  } </TD></TR>')

def p_EXP_Valor(p):
    'EXP : Valor'
    p[0] = p[1]
    concatenar_gramatica('\n <TR><TD> EXP ::= VALOR </TD>  <TD> { exp.val = valor.val } </TD></TR>')

def p_EXP_Indices(p):
    '''EXP : id punto id'''
    p[0] = Expression(p[1], p[3], p.slice[2].lineno, find_column(input, p.slice[2]), 'indice')
    concatenar_gramatica('\n <TR><TD> EXP ::= id . id </TD>  <TD> { exp.val = id1.val . id2.val } </TD></TR>')


def p_EXP_IndicesAS(p):
    '''EXP : EXP t_as EXP'''
    p[0] = Expression(p[1], p[3], p.slice[2].lineno, find_column(input, p.slice[2]), 'as')
    concatenar_gramatica('\n <TR><TD> EXP ::= EXP as EXP </TD>  <TD> { exp.val = exp1.val as exp'
                         '2.val } </TD></TR>')


def p_exp_agregacion(p):
    '''EXP :  t_avg par1 EXP par2
            | t_sum par1 EXP par2
            | t_count par1 EXP par2
            | t_count par1 asterisco par2
            | t_max par1 EXP par2
            | t_min par1 EXP par2'''
    p[0] = Expression(p[1], p[3], p.slice[2].lineno, find_column(input, p.slice[2]), 'aggregate')
    concatenar_gramatica('\n <TR><TD> EXP ::= ' + str(p[1]) + '( EXP ) </TD> <TD> { exp.val = ' + str(p[1]) + ' ( exp1.val ) } </TD></TR>')

def p_funciones_matematicas(p):
    '''EXP : t_abs par1 EXP par2
            | t_cbrt par1 EXP par2
            | t_ceil par1 EXP par2
            | t_ceiling par1 EXP par2
            | t_degrees par1 EXP par2
            | t_exp par1 EXP par2
            | t_factorial par1 EXP par2
            | t_floor par1 EXP par2
            | t_gcd par1 Lista_EXP par2
            | t_ln par1 EXP par2
            | t_log par1 EXP par2
            | t_pi par1  par2
            | t_radians par1 EXP par2
            | t_round par1 EXP par2
            | t_min_scale par1 EXP par2
            | t_scale par1 EXP par2
            | t_sign par1 EXP par2
            | t_sqrt par1 EXP par2
            | t_trim_scale par1 EXP par2
            | t_trunc par1 EXP par2
            | t_width_bucket par1 Lista_EXP par2
            | t_random par1 par2
            | t_setseed par1 EXP par2'''
    p[0] = Expression(p[1], p[3], p.slice[1].lineno, find_column(input, p.slice[1]), 'math')
    concatenar_gramatica('\n <TR><TD> EXP ::= ' + str(p[1]) + '( EXP ) </TD> <TD> { exp.val = ' + str(p[1]) + ' ( exp1.val )  } </TD></TR>')

def p_funciones_matematicas2(p):
    ''' EXP : t_div par1 EXP coma EXP par2
            | t_mod par1 EXP coma EXP par2
            | t_power par1 EXP coma EXP par2'''
    p[0] = Expression(p[1], p[3], p[5],  p.slice[1].lineno, find_column(input, p.slice[1]), 'math2')
    concatenar_gramatica('\n <TR><TD> EXP ::= ' + str(p[1]) + '( EXP , EXP) </TD> <TD> { exp.val = ' + str(p[1]) + ' ( exp1.val , exp2.val) } </TD></TR>')

def p_funciones_Trigonometricas(p):
    ''' EXP : t_acos par1 EXP par2
            | t_acosd par1 EXP par2
            | t_asin par1 EXP par2
            | t_asind par1 EXP par2
            | t_atan par1 EXP par2
            | t_atand par1 EXP par2
            | t_cos par1 EXP par2
            | t_cosd par1 EXP par2
            | t_cot par1 EXP par2
            | t_cotd par1 EXP par2
            | t_sin par1 EXP par2
            | t_sind par1 EXP par2
            | t_tan par1 EXP par2
            | t_tand par1 EXP par2 '''
    p[0] = Expression(p[1], p[3],  p.slice[1].lineno, find_column(input, p.slice[1]), 'trigo')
    concatenar_gramatica('\n <TR><TD> EXP ::= ' + str(p[1]) + '( EXP ) </TD> <TD> { exp.val = ' + str(p[1]) + ' ( exp1.val )}  </TD></TR>')

def p_funciones_Trigonometricas1(p):
    ''' EXP : t_atan2 par1 EXP coma EXP par2
            | t_atan2d par1 EXP coma EXP par2 '''
    concatenar_gramatica('\n <TR><TD> EXP ::= ' + str(p[1]) + '( EXP , EXP ) </TD> <TD> { exp.val = ' + str(p[1]) + ' ( exp1.val , exp2.val ) } </TD></TR>')

def p_funciones_String_Binarias(p):
    ''' EXP : t_length par1 id par2
            | t_substring par1 char coma entero coma entero par2
            | t_trim par1 char par2
            | t_md5 par1 char par2
            | t_sha256 par1 par2
            | t_substr par1 par2
            | t_get_byte par1 par2
            | t_set_byte par1 par2
            | t_convert par1 EXP t_as Tipo par2
            | t_encode par1 par2
            | t_decode par1 par2 '''
    if p[1] == 'substring': 
        concatenar_gramatica('\n <TR><TD> EXP ::= substring ( char , integer , integer ) </TD> <TD> { exp.val = substring ( char, integer,integer } </TD></TR>')
    elif p[1] == 'convert':
        concatenar_gramatica('\n <TR><TD> EXP ::= convert ( EXP as TIPO ) </TD> <TD> { exp.val = conver( exp.val , Tipo.type )} </TD></TR>')
    else: 
        concatenar_gramatica('\n <TR><TD> EXP ::= ' + str(p[1]) + '( EXP ) </TD> <TD> { exp.val = ' + str(p[1]) + ' ( exp1.val ) }</TD></TR>')

# --------------------------------------Listas Fundamentales--------------------------------------------
def p_Lista_ID(p):
    '''Lista_ID : Lista_ID coma id
               | id '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
        concatenar_gramatica('\n <TR><TD> LISTA_ID ::= LISTA_ID , id </TD>  <TD> { lista_id.val = concatenar (lista_id.aux, lista_id.val) } </TD></TR>')
    else:
        p[0] = [p[1]]
        concatenar_gramatica('\n <TR><TD> LISTA_ID ::= id </TD> <TD> { lista_id.aux = id } </TD></TR>')

def p_Lista_Enum(p):#Agregado
    '''Lista_Enum : Lista_Enum coma char
               | char '''
    if len(p) == 4:
        p[0] = p[1]+[p[3]]
        concatenar_gramatica('\n <TR><TD> LISTA_ENUM ::= LISTA_ENUM , char </TD>  <TD> { lista_enum.lista = lista_enum.lista.add(lista_enum.aux) } </TD></TR>')
    else:
        p[0] = [p[1]]
        concatenar_gramatica('\n <TR><TD> LISTA_ENUM ::= char </TD>  <TD> { lista_enum.lista = [char] } </TD></TR>')

def p_Lista_EXP(p):
    '''Lista_EXP : Lista_EXP coma EXP
               | EXP '''
    if len(p) == 4:
        if isinstance(p[1], list):
            insert_nodo_exp(p[3])
        else:
            insert_nodo_exp(p[1])
            insert_nodo_exp(p[3])
        p[0] = list_exp
        concatenar_gramatica('\n <TR><TD> LISTA_EXP ::= LISTA_EXP , EXP </TD>  <TD> { lista_exp.val = concatenar (lista_exp.aux , lista_exp.val) }</TD></TR>')
    else:
        insert_nodo_exp(p[1])
        p[0] = list_exp
        concatenar_gramatica('\n <TR><TD> LISTA_EXP ::=  EXP </TD>  <TD> { lista_exp.aux = char } </TD></TR>')

def p_Lista_Alias(p):
    '''Lista_Alias : Lista_Alias coma Nombre_Alias
               | Nombre_Alias '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
        concatenar_gramatica('\n <TR><TD> LISTA_ALIAS ::= LISTA_ALIAS , Nombre_Alias </TD> <TD> { lista_alias.val = concatenar ( lista_alias.aux , lista_alias.val) }</TD></TR>')
    else:
        p[0] = [p[1]]
        concatenar_gramatica('\n <TR><TD> LISTA_ALIAS ::= Nombre_Alias </TD> <TD> { lista_alias.aux = nombre_alias.val } </TD></TR>')

def p_Nombre_Alias(p):
    '''Nombre_Alias : id id'''
    p[0] = p[1] + ';' + p[2]
    concatenar_gramatica('\n <TR><TD> NOMBRE_ALIAS ::= id id </TD> <TD> { nombre_alias.val = id1 id2}</TD></TR>')

def p_error(p):
    if not p:
        print('end of file')
        ListaErrores.insertar(err.Nodo_Error("Sintactico", "Se esperaba mas pero llega fin de texto", input.count('\n'), len(input)))
        return

    ListaErrores.insertar(err.Nodo_Error("Sintactico", str(p.value),
                                      p.lineno, find_column(input, p)))
    while True:
        tok = parser.token()
        if not tok or tok.type == 'pyc':
            break

def concatenar_gramatica(cadena):
    global reporteg
    reporteg = cadena + reporteg


def insert_nodo_exp(nodo):
    global list_exp
    list_exp.append(nodo)

def insert_nodo_alias(nodo):
    global list_alias
    list_alias.append(nodo)


def vaciar_lista():
    global list_exp
    list_exp = []

def parse(input1, errores1):
    global input
    global ListaErrores
    global reporteg
    global list_exp
    global list_alias
    list_alias = []
    list_exp = []
    ListaErrores = errores1
    reporteg = ''
    input = input1
    global parser
    parser = yacc.yacc()
    parser.errok()
    par = parser.parse(input, tracking=True, lexer=lexer)
    return par

