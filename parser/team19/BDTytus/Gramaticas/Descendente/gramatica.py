#ANALIZADOR LEXICO
#----------------------------------------------------------------------------------------
reservadas = {
    'add' : 'ADD',
    'all' : 'ALL',
    'alter' :'ALTER',
    'and' : 'AND',
    'as' : 'AS',
    'asc':'ASC',
    'between' : 'BETWEEN',
    'by' : 'BY',
    'case' : 'CASE',
    'check' : 'CHECK',
    'column' : 'COLUMN',
    'constraint' : 'CONSTRAINT',
    'create' : 'CREATE',
    'current' : 'CURRENT',
    'current_user' : 'CURRENT_USER',
    'database' : 'DATABASE',
    'databases' : 'DATABASES',
    'default' : 'DEFAULT',
    'delete' : 'DELETE',
    'desc' : 'DESC',
    'distinct' : 'DISTINCT',
    'drop' : 'DROP',
    'else' : 'ELSE',
    'end' : 'END',
    'enum' : 'ENUM',
    'except' : 'EXCEPT',
    'exists' : 'EXISTS',
    'false' : 'FALSE',
    'first' : 'FIRST',
    'foreign' : 'FOREIGN',
    'from' : 'FROM',
    'full' : 'FULL',
    'greatest' : 'GREATEST',
    'group' : 'GROUP',
    'having' : 'HAVING',
    'if' : 'IF',
    'in' : 'IN',
    'inherits' : 'INHERITS',
    'inner' : 'INNER',
    'intersect' : 'INTERSECT',
    'insert' : 'INSERT',
    'into' : 'INTO',
    'is' : 'IS',
    'isnull' : 'ISNULL',
    'join': 'JOIN',
    'key': 'KEY',
    'last': 'LAST',
    'least': 'LEAST',
    'left': 'LEFT',
    'like': 'LIKE',
    'limit': 'LIMIT',
    'mode': 'MODE',
    'natural': 'NATURAL',
    'not': 'NOT',
    'notnull': 'NOTNULL',
    'null': 'NULL',
    'nulls': 'NULLS',
    'offset': 'OFFSET',
    'on': 'ON',
    'or': 'OR',
    'order': 'ORDER',
    'outer': 'OUTER',
    'owner': 'OWNER',
    'primary': 'PRIMARY',
    'references': 'REFERENCES',
    'rename': 'RENAME',
    'replace': 'REPLACE',
    'returning': 'RETURNING',
    'right': 'RIGHT',
    'select': 'SELECT',
    'session_user': 'SESSION_USER',
    'set': 'SET',
    'show': 'SHOW',
    'symmetric': 'SYMMETRIC',
    'table': 'TABLE',
    'then': 'THEN',
    'true': 'TRUE',
    'type': 'TYPE',
    'to' : 'TO',
    'union': 'UNION',
    'unique': 'UNIQUE',
    'unknow': 'UNKNOW',
    'update': 'UPDATE',
    'using' : 'USING',
    'values': 'VALUES',
    'when': 'WHEN',
    'where': 'WHERE',
    'yes': 'YES', #EXTRAS
    'no': 'NO',
    'of' : 'OF',
    'off': 'OFF',
    'only' : 'ONLY'
}

tokens  = [
    'PARENT_D',
    'PARENT_I',
    'LLAVE_ABRE',
    'LLAVE_CIERRE',
    'COMA',
    'P_COMA',
    'PUNTO',
    'MAS',
    'MENOS',
    'AND_SIGNO',
    'CONCATENACION',
    'XOR',
    'NOT_SIMBOLO',
    'POTENCIA',
    'POR',
    'DIVISION',
    'DECIMAL',
    'ENTERO',
    'CARACTER',
    'CADENA',
    'TYPECAST',
    'MODULO',
    'ORSIGNO',
    'SHIFTLEFT',
    'SHIFTRIGHT',
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IGUAL',
    'DISTINTO',
    'DIFERENTE',
    'CORABRE',
    'CORCIERRE',
    'ID',
    'BINARIO'
] + list(reservadas.values())

# Tokens
t_PARENT_I       = r'\('
t_PARENT_D       = r'\)'
t_LLAVE_ABRE     = r'\{'
t_LLAVE_CIERRE   = r'\}'
t_COMA          = r','
t_P_COMA         = r';'
t_PUNTO         = r'\.'
t_MAS           = r'\+'
t_MENOS         = r'-'
t_AND_SIGNO     = r'&'
t_CONCATENACION = r'\|\|'
t_XOR           = r'\#'
t_NOT_SIMBOLO    = r'~'
t_POTENCIA      = r'\^'
t_POR           = r'\*'
t_DIVISION      = r'/'
t_TYPECAST = r'[:]{2}'
t_MODULO = r'%'
t_ORSIGNO = r'[|]'
t_SHIFTLEFT = r'<<'
t_SHIFTRIGHT = r'>>'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_DISTINTO = r'<>'
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_IGUAL = r'='
t_DIFERENTE = r'!='
t_CORABRE = r'\['
t_CORCIERRE = r']'


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

def t_CARACTER(t):
    r'\'.?\''
    t.value = t.value[1:-1] # remuevo las comillas simples
    return t 

def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1] # remuevo las comillas dobles
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type =  reservadas.get(t.value.lower(), 'ID')
    return t

def t_COMMENTLINE(t):
    r'-{2}[^\n]*(\n|\Z)'
    t.lexer.lineno += 1
    print(t.value[2:-1])

def t_COMMENTMULTI(t):
    r'[/][*][^*]*[*]+([^/*][^*]*[*]+)*[/]'
    t.lexer.lineno += t.value.count('\n')
    print(t.value[2:-2])

def t_BINARIO(t):
    r'B\'[0-1]+\''
    t.value = t.value[2:-1] #Remuevo las comillas y la B al inicio
    return t

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


#ANALIZADOR SINTACTICO
#----------------------------------------------------------------------------------------
def p_init(t):
    's  : instrucciones'

def p_instrucciones_evaluar(t):
    '''instrucciones  : instruccion instrucciones_prima '''

def p_instrucciones_prima(t):
    '''instrucciones_prima    : P_COMA instrucciones_prima2 
                            | '''

def p_instrucciones_prima2(t):
    '''instrucciones_prima2 : instruccion P_COMA instrucciones_prima2
                            | '''
def p_instruccion_evaluar(t):
    '''instruccion  : CREATE c
                    | SHOW DATABASE lk
                    | ALTER dt
                    | DROP do
                    | DELETE FROM ol
                    | INSERT INTO ID VALUES PARENT_I l_val PARENT_D
                    | UPDATE ID SET act'''

def p_create(t):
    '''c : TYPE ID AS ENUM PARENT_I l_val PARENT_D 
         | re DATABASE ifex ID ow mo
         | TABLE ID PARENT_I ct PARENT_D inh'''

def p_l_val(t):
    'l_val : val l_valp'

def p_l_valp(t):
    '''l_valp : COMA val l_valp
              | '''
def p_val(t):
    ''' val : DECIMAL
            | ENTERO
            | CARACTER
            | CADENA
            | TRUE
            | FALSE'''

def p_re(t):
    '''re : OR REPLACE
          | '''

def p_ifex(t):
    ''' ifex : IF NOT EXISTS
             | '''
def p_ow(t):
    ''' ow : OWNER hi ID
           | '''

def p_hi(t):
    ''' hi : IGUAL
           | '''

def p_mo(t):
    '''mo : MODE hi ENTERO 
          | '''


def p_inh(t):
    '''inh : INHERITS PARENT_I ID PARENT_D
           | '''

def p_ct(t):
    'ct : col ctp'

def p_ctp(t):
    '''ctp : COMA col ctp
           |  '''

def p_col(t):
    ''' col : ID ID at
            | ck
            | UNIQUE PARENT_I l_id PARENT_D
            | PRIMARY KEY PARENT_I l_id PARENT_D
            | FOREIGN KEY PARENT_I l_id PARENT_D REFERENCES ID PARENT_I l_id PARENT_D '''

def p_l_id(t):
    'l_id : ID l_idp'

def p_l_idp(t):
    '''l_idp : COMA ID l_idp
             | '''

def p_at(t): 
    '''at : PRIMARY KEY
          | REFERENCES ID 
          | defu'''
        
def p_defu(t):
    '''defu : DEFAULT val nn
            | nn '''

def p_nn(t):
    '''nn : NOT NULL cc
          | NULL cc
          | cc '''

def p_cc(t):
    '''cc : CONSTRAINT ID uc
          | uc '''

def p_uc(t):
    '''uc : UNIQUE ck
          | CHECK PARENT_I log PARENT_D
          | '''

def p_ck(t):
    '''ck : CONSTRAINT ID CHECK PARENT_I log PARENT_D
          | '''

def p_log(t):
    'log : w logp'

def p_logp(t):
    '''logp : w logp
            | '''

def p_w(t):
    'w : y wp'

def p_wp(t):
    '''wp : MAS y wp
          | MENOS y wp 
          | '''

def p_y(t):
    'y : z yp'

def p_yp(t):
    '''yp : POR z yp
          | DIVISION z yp
          | MODULO z yp
          | '''
        
def p_z(t):
    'z : x zp'

def p_zp(t):
    '''zp : POTENCIA x zp
          | '''
        
def p_x(t):
    'x : u xp'

def p_xp(t):
    '''xp : MAYORQUE u
          | MENORQUE u
          | MAYORIGUAL u
          | MENORIGUAL u
          | IGUAL u
          | DISTINTO u
          | '''

def p_u(t):
    'u : v up'

def p_up(t):
    '''up : OR v up
          | '''

def p_v(t):
    'v : r vp'

def p_vp(t):
    '''vp : AND r vp
          | '''

def p_r(t):
    '''r : PARENT_I w PARENT_D
         | ID pu
         | val '''

def p_lk(t):
    '''lk : LIKE val
          | '''

def p_dt(t):
    '''dt : DATABASE ID al
          | TABLE ID fm'''

def p_al(t):
    '''al : RENAME TO ID
          | OWNER TO LLAVE_ABRE ID ORSIGNO CURRENT_USER ORSIGNO SESSION_USER LLAVE_CIERRE'''

def p_fm(t):
    '''fm : ADD cl
          | DROP dp
          | ALTER COLUMN ID SET ar
          | RENAME COLUMN ID TO ID'''

def p_cl(t):
    '''cl : COLUMN ID ID
          | CHECK PARENT_I log PARENT_D
          | CONSTRAINT ID UNIQUE PARENT_I ID PARENT_D
          | FOREIGN KEY PARENT_I ID PARENT_D REFERENCES ID '''

def p_dp(t):
    '''dp : COLUMN ID
          | CONSTRAINT ID'''

def p_ar(t):
    ''' ar : NOT NULL
           | NULL '''

def p_do(t):
    '''do : DATABASE ife ID
          | TABLE ID '''

def p_ife(t):
    '''ife : IF EXISTS
           |  '''

def p_ol(t):
    ''' ol : ONLY ID ico ali us wh ret
           | ID ico ali us wh ret '''

def p_ico(t):
    '''ico : POR
           | '''

def p_ali(t):
    '''ali : AS ID 
           | '''

def p_us(t):
    '''us : USING l_id
          | '''

def p_wh(t):
    '''wh : WHERE cd
          | '''

def p_cd(t):
    '''cd : log
          | CURRENT OF ID '''

def p_ret(t):
    '''ret : RETURNING rs
           | '''

def p_rs(t):
    '''rs : POR
          | log ali '''

def p_act(t):
    'act : l_asig WHERE log'

def p_l_asig(t):
    'l_asig : asig l_asigp'

def p_l_asigp(t):
    '''l_asigp : COMA asig l_asigp
               | '''

def p_asig(t):
    'asig : ID IGUAL val'

def p_pu(t):
    '''pu : PARENT_I se PARENT_D
          | '''

def p_se(t):
    '''se : l_arg
          | '''

def p_l_arg(t):
    'l_arg : arg l_argp'

def p_l_argp(t):
    '''l_argp : COMA arg l_argp
              | '''

def p_arg(t):
    'arg : log'

def p_error(t):
    print("Error sintáctico en " + str(t.value) + ", Fila: " + str(t.lexer.lineno))

# Construyendo el analizador sintactico
import ply.yacc as yacc
parser = yacc.yacc()

input = '''select * from hola
            --Comentario de una linea
            /*Estos son comentarios multilinea*/'''
parser.parse(input)
