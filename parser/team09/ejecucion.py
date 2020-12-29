import ply.yacc as yacc
import ply.lex as lex
import re
import Expresiones as expre

import instrucciones as ins 
import tabla_simbolos as TS
import Errores as E

ts_global = TS.tabla_simbolos()

i = 0
lst_instrucciones = []

def inc_index():
    global i
    i += 1
    return i

# Lista de palabras reservadas
reservadas = {
    'create'        : 'CREATE',
    'type'          : 'TYPE',
    'as'            : 'AS',
    'enum'          : 'ENUM',
    'replace'       : 'REPLACE',
    'database'      : 'DATABASE',
    'if'            : 'IF',
    'not'           : 'NOT',
    'exists'        : 'EXISTS',
    'or'            : 'OR',
    'owner'         : 'OWNER',
    'mode'          : 'MODE',
    'show'          : 'SHOW',
    'like'          : 'LIKE',
    'databases'     : 'DATABASES',
    'rename'        : 'RENAME',
    'currente_user' : 'CURRENT_USER',
    'session_user'  : 'SESSION_USER',
    'text'          : 'TEXT',
    'numeric'       : 'NUMERIC',
    'integer'       : 'INTEGER',
    'alter'         : 'ALTER',
    'to'            : 'TO',
    'drop'          : 'DROP',
    'table'         : 'TABLE',
    'default'       : 'DEFAULT',
    'primary'       : 'PRIMARY',
    'key'           : 'KEY',
    'foreign'       : 'FOREIGN',
    'null'          : 'NULL',
    'constraint'    : 'CONSTRAINT',
    'unique'        : 'UNIQUE',
    'check'         : 'CHECK',
    'references'    : 'REFERENCES',
    'smallint'      : 'SMALLINT',
    'bigint'        : 'BIGINT',
    'decimal'       : 'DECIMAL',
    'real'          : 'REAL',
    'double'        : 'DOUBLE',
    'precision'     : 'PRECISION',
    'money'         : 'MONEY',
    'character'     : 'CHARACTER',
    'varying'       : 'VARYING',
    'varchar'       : 'VARCHAR',
    'char'          : 'CHAR',
    'timestamp'     : 'TIMESTAMP',
    'data'          : 'DATA',
    'time'          : 'TIME',
    'interval'      : 'INTERVAL',
    'with'          : 'WITH',
    'without'       : 'WITHOUT',
    'zone'          : 'ZONE',
    'column'        : 'COLUMN',
    'add'           : 'ADD',
    'delete'        : 'DELETE',
    'from'          : 'FROM',
    'where'         : 'WHERE',
    'insert'        : 'INSERT',
    'into'          : 'INTO',
    'values'        : 'VALUES',
    'update'        : 'UPDATE',
    'set'           : 'SET',
    'and'           : 'AND',
    'sum'           : 'SUM',
    'avg'           : 'AVG',
    'max'           : 'MAX',
    'pi'            : 'PI',
    'power'         : 'POWER',
    'sqrt'          : 'SQRT',
    'select'        : 'SELECT',
    'inner'         : 'INNER',
    'left'          : 'LEFT',
    'right'         : 'RIGHT',
    'full'          : 'FULL',
    'outer'         : 'OUTER',
    'boolean'       : 'BOOLEAN', 
    'off'           : 'OFF', 
    'on'            : 'ON',
    'join'          : 'JOIN',
    'order'         : 'ORDER',
    'by'            : 'BY',
    'asc'           : 'ASC',
    'desc'          : 'DESC',
    'inherits'      : 'INHERITS',
    'distinct'      : 'DISTINCT',
    'use'           : 'USE',
    'true'          : 'TRUE',
    'false'         : 'FALSE',
    'date'          : 'DATE',
    'abs'	        : 'ABS',
    'cbrt'	        : 'CBRT',
    'ceil'	        : 'CEIL',
    'ceiling'       : 'CEILING',
    'degrees'	    : 'DEGREES',
    'div'	        : 'DIV',
    'exp'	        : 'EXP',
    'factorial'	    : 'FACTORIAL',
    'floor'	        : 'FLOOR',
    'gcd'	        : 'GCD',
    'ln'	        : 'LN',
    'log'	        : 'LOG',
    'mod'	        : 'MOD',
    'radians'	    : 'RADIANS',
    'round'	        : 'ROUND',
    'sign'	        : 'SIGN',
    'width_bucket'	: 'WIDTH_BUCKET',
    'trunc'	        : 'TRUNC',
    'random'	    : 'RANDOM',
    'extract'	    : 'EXTRACT',
    'year'	        : 'YEAR',
    'month'	        : 'MONTH',
    'day'	        : 'DAY',
    'hour'	        : 'HOUR',
    'minute'	    : 'MINUTE',
    'second'	    : 'SECOND',
    'date_part'	    : 'DATE_PART',
    'sha256'	    : 'SHA256',
    'substr'	    : 'SUBSTR',
    'get_byte'	    : 'GET_BYTE',
    'set_byte'	    : 'SET_BYTE',
    'convert'	    : 'CONVERT',
    'encode'	    : 'ENCODE',
    'decode'	    : 'DECODE',
    'length'	    : 'LENGTH',
    'md5'	        : 'MD5',
    'substring'	    : 'SUBSTRING',
    'trim'	        : 'TRIM',
    'leading'	    : 'LEADING',
    'trailing'	    : 'TRAILING',
    'both'	        : 'BOTH',
    'acos'	        : 'ACOS',
    'acosd'	        : 'ACOSD',
    'asin'	        : 'ASIN',
    'asind'	        : 'ASIND',
    'atan'	        : 'ATAN',
    'atand'	        : 'ATAND',
    'atan2'	        : 'ATAN2',
    'atan2d'	    : 'ATAN2D',
    'cos'	        : 'COS',
    'cosd'	        : 'COSD',
    'cot'	        : 'COT',
    'cotd'	        : 'COTD',
    'sin'	        : 'SIN',
    'sind'	        : 'SIND',
    'tan'	        : 'TAN',
    'tand'	        : 'TAND',
    'sinh'	        : 'SINH',
    'cosh'	        : 'COSH',
    'asinh'	        : 'ASINH',
    'acosh'	        : 'ACOSH',
    'atanh'	        : 'ATANH',
    'use'           : 'USE',
    'now'           : 'NOW',
    'in'            : 'IN',
    'count'         : 'COUNT',
    'true'          : 'TRUE',
    'false'         : 'FALSE',
    'group'         : 'GROUP',
    'by'            : 'BY',
    'current_time'  : 'CURRENT_TIME',
    'current_date'  : 'CURRENT_DATE',
    'between'       : 'BETWEEN',
    'having'        : 'HAVING'
}

# Lista de tokens
tokens = [
    'COMA',
    'PARIZQ',
    'PARDER',
    'PTCOMA',
    'MAYIG',
    'MENIG',
    'DIFEQ',
    'MAYOR',
    'MENOR',
    'IGUAL',
    'MULTI',
    'MENOS',
    'SUMAS',
    'DIVIS',
    'POTEN',
    'CADENA',
    'ID',
    'DECIMA',
    'ENTERO',
    'PUNTO', 
    'APOS',
    'SQRTROOT',
    'CUBEROOT',
    'BITAND',
    'BITOR',
    'BITXOR',
    'BITNOT',
    'BITSLEFT',
    'BITSRIGHT'
] + list(reservadas.values())

# Expresiones regulares par los tokens
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_PTCOMA = r';'
t_MAYIG = r'>='
t_MENIG = r'<='
t_DIFEQ = r'<>'
t_MAYOR = r'>'
t_MENOR = r'<'
t_IGUAL = r'='
t_MULTI = r'\*'
t_MENOS = r'-'
t_SUMAS = r'\+'
t_DIVIS = r'/'
t_POTEN = r'\^'
t_PUNTO = r'.'
t_APOS = r'\''
t_SQRTROOT = r'\|/'
t_CUBEROOT = r'\|\|/'
t_BITAND = r'&'
t_BITOR = r'\|'
t_BITXOR = r'#'
t_BITNOT = r'~'
t_BITSLEFT = r'<<'
t_BITSRIGHT = r'>>'

t_ignore = " \t"

def t_COMENTARIO_S(t):
    r'--.*\n'
    global linea, columna
    linea = linea + 1
    columna = 1
    t.lexer.lineno += 1

def t_COMENTARIO_M(t):
    r'/\*(.|\n)*?\*/'
    global linea, columna
    linea = linea + t.value.count('\n')
    columna = 1
    t.lexer.lineno += t.value.count('\n')

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Revisa las palabras reservadas 
     return t

def t_CADENA(t):
    r'([\"]|[\']).*?([\"]|[\'])'
    t.value = '\'' + t.value[1:-1] '\''
    return t 

def t_DECIMA(t):
    r'\d+[.]\d+'
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

def t_nuevalinea(t):
    r'\n+'

    linea = t.value.count('\n')
    columna = 1
    t.lexer.lineno += t.value.count("\n")

# Errores léxicos
def t_error(t):

    lex_error(t.value[0], linea, t.lexpos)
    t.lexer.skip(1)


lexer = lex.lex(reflags=re.IGNORECASE)

# Asociación de operadores y precedencia
precedence = (
    ('left','SUMAS','MENOS'),
    ('left','MULTI','DIVIS'),
    ('left','POTEN'),
    ('right','UMENOS', 'USUMAS'),
    ('left','MAYIG','MENIG','IGUAL','DIFEQ','MAYOR','MENOR'),
    ('right','NOT'),
    ('left','AND'),
    ('left','OR'),
    ) 

# Definir gramática

def p_entrada(p):
    '''entrada : entrada create_type
                | entrada create_db
                | entrada show_db
                | entrada alter_db
                | entrada drop_db
                | entrada create_table
                | entrada drop_table
                | entrada alter_table
                | entrada s_delete
                | entrada s_insert
                | entrada s_update
                | entrada s_select
                | entrada s_use
                | create_type
                | create_db
                | show_db
                | alter_db 
                | drop_db 
                | create_table
                | drop_table
                | alter_table
                | s_delete
                | s_insert
                | s_update
                | s_select
                | s_use'''

def p_s_use(p):
    '''s_use : USE ID PTCOMA'''
    global lst_instrucciones
    cons = ins.UseDB(p[2])
    lst_instrucciones.append(cons)

#region 'Select Analisis'

def p_s_select(p):
    '''s_select : SELECT dist list_cols FROM list_from PTCOMA'''
    cons = ins.Select(p[2], p[3], p[5], None, None, None)
    lst_instrucciones.append(cosn)
    

def p_s_select2(p):
    '''s_select : SELECT dist list_cols FROM list_from list_conditions PTCOMA'''
    cons = ins.Select(p[2], p[3], p[5], None, None, p[6])
    lst_instrucciones.append(cons)
    
def p_s_select3(p):
    '''s_select : SELECT dist list_cols FROM list_from list_order PTCOMA'''
    cons = ins.Select(p[2], p[3], p[5], None, p[6], None)
    lst_instrucciones.append(cons)

def p_s_select4(p):
    '''s_select : SELECT dist list_cols FROM list_from list_joins PTCOMA'''
    cons = ins.Select(p[2], p[3], p[5], p[6], None, None)
    lst_instrucciones.append(cons)

def p_s_select5(p):
    '''s_select : SELECT dist list_cols FROM list_from list_conditions list_order PTCOMA'''
    cons = ins.Select(p[2], p[3], p[5], None, p[7], p[6])
    lst_instrucciones(cons)

def p_s_select6(p):
    '''s_select : SELECT dist list_cols FROM list_from list_joins list_conditions PTCOMA'''
    cons = ins.Select(p[2], p[3], p[5], p[6], None, p[7])
    lst_instrucciones.append(cons)

def p_s_select7(p):
    '''s_select : SELECT dist list_cols FROM list_from list_joins list_order PTCOMA'''
    cons = ins.Select(p[2], p[3], p[5], p[6], p[7], None)
    lst_instrucciones.append(cons)

def p_s_select8(p):
    '''s_select : SELECT dist list_cols FROM list_from list_joins list_conditions list_order PTCOMA'''
    cons = ins.Select(p[2], p[3], p[5], p[6], p[8], p[7])
    lst_instrucciones.append(cons)

def p_dist(p):
    '''dist : DISTINCT
             | '''
    try:
        if p[1]:
            p[0] = p[1]
        else: 
            p[0] = ' '
    except IndexError:
        print('out of range')

def p_list_cols(p):
    '''list_cols :  DISTINCT list_alias
                  | MULTI
                  | list_alias'''
    
    


def p_list_alias(p):
    '''list_alias : list_alias COMA sel_id'''

    p[0] = p[3].append(p[1])

def p_list_alias_2(p):
    '''list_alias : sel_id'''
    
    p[0] = p[1]

def p_sel_id(p):
    ''' sel_id : ID PUNTO ID AS ID
                  | ID PUNTO ID
                  | ID AS ID
                  | ID'''
    p[0] = p[1]


def p_list_from(p):
    '''list_from :  list_from COMA from_id'''

    p[0] = p[3].append(p[1])

def p_list_from(p):
    '''list_from :  from_id'''
    
    p[0] = p[1]
    

def p_from_id(p):
    '''from_id : ID AS ID
                | ID'''

    p[0] = p[1]    

def p_list_joins(p):
    '''list_joins : list_joins join_type JOIN ID join_conditions'''

    p[0] = p[4].append(p[1])

def p_list_joins_2(p):
    '''list_joins : list_joins JOIN ID join_conditions'''

    p[0] = p[3].append(p[1])

def p_list_joins_3(p):
    '''list_joins : join_type JOIN ID join_conditions'''

    p[0] = p[3]

def p_list_joins_4(p):
    '''list_joins : JOIN ID join_conditions
                  | JOIN ID'''

    p[0] = p[2]
    
def p_join_type(p):
    '''join_type : LEFT OUTER
                 | RIGHT OUTER
                 | FULL OUTER
                 | LEFT
                 | RIGHT
                 | FULL
                 | INNER'''

    if p[2] != None:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_join_conditions(p):
    '''join_conditions : ON expresion'''


def p_list_conditions(p):
    '''list_conditions : WHERE expresion'''


def p_list_order(p):
    '''list_order : ORDER BY ID ASC
                  | ORDER BY ID DESC'''
    p[0] = p[3]


#end region 

def p_create_type(p):
    '''create_type : CREATE TYPE ID AS ENUM PARIZQ lista1 PARDER PTCOMA'''

    

def p_lista1(p):
    '''lista1 : lista1 COMA CADENA'''
    p[0] = p[3].append(p[1])

def p_lista1_2(p):
    '''lista1 : CADENA'''
    p[0] = p[1]
    

def p_data_type(p):
    '''data_type : NUMERIC
            | INTEGER
            | TEXT
            | SMALLINT 
            | BIGINT
            | DECIMAL
            | REAL
            | MONEY
            | TIMESTAMP
            | DATA
            | TIME
            | INTERVAL
            | BOOLEAN
            | DOUBLE PRECISION
            | ID'''

    p[0] = (str(p[1]))

def p_data_type_3(p):
    '''data_type    : VARCHAR PARIZQ ENTERO PARDER
                    | CHARACTER PARIZQ ENTERO PARDER
                    | CHAR PARIZQ ENTERO PARDER'''

    p[0] = (p[1]) + "," + str(p[3])
    #p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])

def p_create_db(p):
    '''create_db : CREATE DATABASE db_exist ID db_owner db_mode PTCOMA'''
    global lst_instrucciones
    cons = ins.CreateDB(False, p[3], p[4], p[5], p[6])
    lst_instrucciones.append(cons)


def p_create_db_2(p):
    '''create_db : CREATE OR REPLACE DATABASE db_exist ID db_owner db_mode PTCOMA'''
    global lst_instrucciones
    cons = ins.CreateDB(True, p[5], p[6], p[7], p[8])
    lst_instrucciones.append(cons)

def p_c_dc_exist(p):
    '''db_exist : IF NOT EXISTS
                | '''
    try:
        if p[2]:
            p[0] = True
    except:
        p[0] = False

def p_db_owner(p):
    '''db_owner : OWNER IGUAL ID 
                | OWNER ID 
                |'''
    try:
        if p[2] == '=':
            p[0] = p[3]
        else:
            p[0] = p[2]
    except:
        p[0] = None

def p_db_mode(p):
    '''db_mode :  MODE IGUAL ENTERO
                | MODE ENTERO
                |'''
    try:
        if p[2] == '=':
            p[0] = p[3]
        else:
            p[0] = p[2]
    except:
        p[0] = None

def p_show_db(p):
    '''show_db : SHOW DATABASES PTCOMA'''
    global lst_instrucciones
    cons = ins.ShowDB()
    lst_instrucciones.append(cons)

def p_alter_db(p):
    '''alter_db : ALTER DATABASE ID al_db PTCOMA'''
    cons = ins.AlterDB(p[3],p[4])
    lst_instrucciones.append(cons) 

def p_al_db(p):
    '''al_db : RENAME TO ID
            | OWNER TO owner_db'''
    
    if str(p[1]).upper() == 'RENAME':
        p[0] = p[3]

def p_owner_db(p):
    '''owner_db : ID
                | CURRENT_USER
                | SESSION_USER'''
    
    p[0] = p[1]

def p_drop_db(p):
    '''drop_db  : DROP DATABASE ID PTCOMA'''
    cons = ins.DropDB(str(p[3]), False)
    lst_instrucciones.append(cons)

def p_drop_db_2(p):
    '''drop_db  : DROP DATABASE IF EXISTS ID PTCOMA'''
    cons = ins.DropDB(str(p[5]), True)
    lst_instrucciones.append(cons)

def p_create_table(p): 
    '''create_table   : CREATE TABLE ID PARIZQ columnas PARDER PTCOMA'''
    arr = p[5]
    cons = ins.CreateTable(str(p[3]), None, arr[0], None,arr[1]) #Hay que cambiar el 2do parametro porque es el nombre de la base de datos
    lst_instrucciones.append(cons)

def p_create_table_2(p):
    '''create_table   : CREATE TABLE ID PARIZQ columnas PARDER INHERITS PARIZQ ID PARDER PTCOMA'''
    arr = p[5]
    cons = ins.CreateTable(str(p[3]), None, arr[0], p[9],arr[1]) #Hay que cambiar el 2do parametro porque es el nombre de la base de datos
    lst_instrucciones.append(cons)

def p_columnas(p):
    '''columnas  : colum_list'''

    lis = []
    arr = []
    arr.append(p[1])
    arr.append(lis)
    p[0] = arr

def p_columnas_2(p):
    '''columnas  : colum_list const_keys'''
    arr = []
    arr.append(p[1])
    arr.append(p[2])
    p[0] = arr

def p_id_data(p):
    '''id_data   : ID data_type const'''

    #Verificar si el data type viene con longitud o no
    x = p[2].split(',')
    tipo = tipo_data(x[0])
    if len(x) == 2: 
        nueva_columna = TS.Simbolo(p[1], tipo,p[3], None, x[1], False, False, None) 
        nueva_columna.valor = p[3]
    else:
        nueva_columna = TS.Simbolo(p[1],tipo, p[3], None, None, False, False, None)
        nueva_columna.valor = p[3]
        
    p[0] = nueva_columna

def p_id_data_2(p):
    '''id_data   : ID data_type '''
    
    #Verificar si el data type viene con longitud o no
    x = p[2].split(',')
    tipo = tipo_data(x[0])
    if len(x) == 2:
        nueva_columna = TS.Simbolo(p[1], tipo,None , None, x[1], False,False, None) 
    else:
        nueva_columna = TS.Simbolo(p[1], tipo, None, None, None, False, False, None)

    p[0] = nueva_columna

def p_colum_list(p):
    '''colum_list   : colum_list COMA id_data'''

    p[1].append(p[3])
    p[0] = p[1]

def p_colum_list_2(p):
    '''colum_list   : id_data'''

    #id_data treae una columna con sus constraints si es que tenia 
    arr = []
    arr.append(p[1])

    p[0] = arr

def p_const_keys(p):
    '''const_keys   : const_keys COMA CONSTRAINT ID PRIMARY KEY PARIZQ lista_id PARDER
                    | const_keys COMA CONSTRAINT ID FOREIGN KEY PARIZQ ID PARDER REFERENCES ID PARIZQ ID PARDER
                    | const_keys COMA PRIMARY KEY PARIZQ lista_id PARDER
                    | const_keys COMA FOREIGN KEY PARIZQ ID PARDER REFERENCES ID PARIZQ ID PARDER'''

    if str(p[3]).upper() == 'CONSTRAINT':
        if str(p[5]).upper() == 'PRIMARY':
            for x in p[8]:
                const = TS.const(p[4], None, None, TS.t_constraint.PRIMARY,x)
                p[1].append(const)
        elif str(p[5]).upper() == 'FOREIGN':
            o = str(p[11]) + ',' + str(p[13])
            const = TS.const(p[4], o, None, TS.t_constraint.FOREIGN, p[8])
            p[1].append(const)
    elif str(p[3]).upper() == 'PRIMARY':
        for x in p[6]:
            const = TS.const(None, None, None, TS.t_constraint.PRIMARY,x)
            p[1].append(const)
    elif str(p[3]).upper() == 'FOREIGN':
        oo = str(p[9]) + ',' + str(p[11])
        const = TS.const(None, oo, None, TS.t_constraint.FOREIGN, p[6])
        p[1].append(const)
    
    p[0] = p[1]

def p_const_keys_2(p):
    '''const_keys   : CONSTRAINT ID PRIMARY KEY PARIZQ lista_id PARDER
                    | CONSTRAINT ID FOREIGN KEY PARIZQ ID PARDER REFERENCES ID PARIZQ ID PARDER
                    | PRIMARY KEY PARIZQ lista_id PARDER
                    | FOREIGN KEY PARIZQ ID PARDER REFERENCES ID PARIZQ ID PARDER'''
    arr = []
    
    if str(p[1]).upper() == 'CONSTRAINT':
        if str(p[3]).upper() == 'PRIMARY':
            for x in p[6]:
                const = TS.const(p[2], None, None, TS.t_constraint.PRIMARY,x)
                arr.append(const)
        elif str(p[3]).upper() == 'FOREIGN':
            t_c = str(p[9]) + ',' + str(p[11])
            const = TS.const(p[2], t_c, None, TS.t_constraint.FOREIGN, p[6])
            arr.append(const)
    elif str(p[1]).upper() == 'PRIMARY':
        for x in p[4]:
            const = TS.const(None, None, None, TS.t_constraint.PRIMARY,x)
            arr.append(const)
    elif str(p[1]).upper() == 'FOREIGN':
        t_t = str(p[7]) + ',' + str(p[9])
        const = TS.const(None, t_t, None, TS.t_constraint.FOREIGN, p[4])
        arr.append(const)

    p[0] = arr

def p_const(p):
    '''const    : const DEFAULT valores
                | const NOT NULL
                | const NULL
                | const CONSTRAINT ID  UNIQUE
                | const CONSTRAINT ID  UNIQUE PARIZQ lista_id PARDER
                | const UNIQUE
                | const CONSTRAINT ID CHECK PARIZQ exp_check PARDER
                | const CHECK PARIZQ exp_check PARDER
                | const PRIMARY KEY
                | const REFERENCES ID PARIZQ lista_id PARDER'''

    creado = False
    const = ''

    if str(p[2]).upper() == 'DEFAULT':
        const = TS.const(None, p[2], None, TS.t_constraint.DEFOULT,None)
    elif str(p[2]).upper() == 'NOT':
        const = TS.const(None, None, None, TS.t_constraint.NOT_NULL,None)
    elif str(p[2]).upper() == 'NULL':
        const = TS.const(None, None, None, TS.t_constraint.NULL,None)
    elif str(p[2]).upper() == 'UNIQUE':
        const = TS.const(None, None, None, TS.t_constraint.UNIQUE,None)
    elif str(p[2]).upper() == 'PRIMARY':
        const = TS.const(None, None, None, TS.t_constraint.PRIMARY,None)
    elif str(p[2]).upper() == 'REFERENCES':
        const = TS.const(p[2], p[4], None, TS.t_constraint.FOREIGN,None) #ID va a ser igual al ID de la tabla y valor = columna de referencia
    elif str(p[2]).upper() == 'CHECK':
        const = TS.const(None, None, p[4], TS.t_constraint.CHECK,None)
    elif str(p[2]).upper() == 'CONSTRAINT':
        if str(p[4]).upper() == 'UNIQUE':
            
            try: 
                if (str(p[6]) == '('):
                    lista_id = p[6]
                    creado = True
                    for t_id in lista_id: #esto es para el alter, si viene varios id, el constraint se aplica a varias columnas
                        const = TS.const(str(p[2]),None,None,TS.t_constraint.UNIQUE,str(t_id))
                        p[1].append(const) #al agregarlos a las columnas verificar que no este dos o mas veces la misma
            except:
                #constraint id unique
                const = TS.const(str(p[2]),None,None,TS.t_constraint.UNIQUE,None)

        elif str(p[3]).upper() == 'CHECK':
            const = TS.const(p[2], None, p[6], TS.t_constraint.CHECK,None)

    if(creado == False):
        p[1].append(const)

    p[0] = p[1] 

    

def p_const_2(p):
    '''const    : DEFAULT valores
                | NOT NULL
                | NULL
                | CONSTRAINT ID UNIQUE
                | CONSTRAINT ID  UNIQUE PARIZQ lista_id PARDER
                | UNIQUE
                | CONSTRAINT ID CHECK PARIZQ exp_check PARDER
                | CHECK PARIZQ exp_check PARDER
                | PRIMARY KEY
                | REFERENCES ID PARIZQ lista_id PARDER
                 '''

    arr = []
    const = ''
    creado = False
    if str(p[1]).upper() == 'DEFAULT':
        const = TS.const(None, p[2], None, TS.t_constraint.DEFOULT,None)
    elif str(p[1]).upper() == 'NOT':
        const = TS.const(None, None, None, TS.t_constraint.NOT_NULL,None)
    elif str(p[1]).upper() == 'NULL':
        const = TS.const(None, None, None, TS.t_constraint.NULL,None)
    elif str(p[1]).upper() == 'UNIQUE':
        const = TS.const(None, None, None, TS.t_constraint.UNIQUE,None)
    elif str(p[1]).upper() == 'PRIMARY':
        const = TS.const(None, None, None, TS.t_constraint.PRIMARY,None)
    elif str(p[1]).upper() == 'REFERENCES':
        const = TS.const(p[2], p[4], None, TS.t_constraint.FOREIGN,None) #ID va a ser igual al ID de la tabla y valor = columna de referencia
    elif str(p[1]).upper() == 'CHECK':
        const = p[3]
    elif str(p[1]).upper() == 'CONSTRAINT':
        if str(p[3]).upper() == 'UNIQUE':
            
            try: 
                if (str(p[4]) == '('):
                    lista_id = p[5]
                    for t_id in lista_id: #esto es para el alter, si viene varios id, el constraint se aplica a varias columnas
                        const = TS.const(str(p[2]),None,None,TS.t_constraint.UNIQUE,str(t_id))
                        arr.append(const) #al agregarlos a las columnas verificar que no este dos o mas veces la misma
                    creado = True
            except:
                #constraint id unique
                const = TS.const(str(p[2]),None,None,TS.t_constraint.UNIQUE,None)

        elif str(p[3]).upper() == 'CHECK':
            p[5].id = p[2]
            const = p[5]

    if(creado == False):
        arr.append(const)
     
    p[0] = arr
        
def p_lista_id(p):
    '''lista_id : lista_id COMA ID'''
    
    p[1].append(p[3])
    p[0] = p[1]

def p_lista_id_2(p):
    '''lista_id : ID'''
    arr = []
    arr.append(p[1])

    p[0] = arr

def p_drop_table(p):
    '''drop_table : DROP TABLE ID PTCOMA'''
    cons = ins.DropTable(p[3], None)
    lst_instrucciones.append(cons)


def p_alter_table(p):
    '''alter_table : ALTER TABLE ID acciones PTCOMA'''

    cons = ins.AlterTable(p[3], p[4], None)
    lst_instrucciones.append(cons)
        
def p_acciones(p):
    '''acciones : ADD acc
                | ADD COLUMN ID data_type
                | ALTER COLUMN ID TYPE data_type
                | ALTER COLUMN ID SET const
                | DROP CONSTRAINT ID
                | DROP COLUMN ID
                | RENAME COLUMN ID TO ID'''

    arr = []
    
    if str(p[1]).upper() == 'ADD':
        if str(p[2]).upper() == 'COLUMN':
            arr.append('ADDCOL')
            #Verificar si el data type viene con longitud o no
            x = p[4].split(',')
            tipo = tipo_data(x[0])
            if len(x) == 2: 
                nueva_columna = TS.Simbolo(str(p[3]), tipo, None, None, x[1], False, False, None) 
            else:
                nueva_columna = TS.Simbolo(str(p[3]),tipo, None, None, None, False, False, None)
            arr.append(nueva_columna)
        else:
            arr.append('CONST')
            arr.append(p[2])
    elif str(p[1]).upper() == 'DROP':
        if str(p[2]).upper() == 'CONSTRAINT':
            arr.append('DCONS')
            arr.append(p[3])
        elif str(p[2]).upper() == 'COLUMN':
            arr.append('DCOL')
            arr.append(p[3])
    elif str(p[1]).upper() == 'ALTER':
        if str(p[4]).upper() == 'TYPE':
            arr.append('TYPE')
            arr.append(p[3])
            x = p[5].split(',')
            if len(x) == 2:
                tipo = tipo_data(x[0])
                arr.append(tipo)
                arr.append(x[1])
        elif str(p[4]).upper() == 'SET':
            arr.append('SET')
            arr.append(p[3])
            arr.append(p[5])

    p[0] = arr

def p_acc(p):
    '''acc  : const
            | const_keys'''

    p[0] = p[1]

def p_delete(p):
    '''s_delete : DELETE FROM ID PTCOMA'''
    cons = ins.Delete(str(p[3], None))
    lst_instrucciones.append(cons)

def p_delete_2(p):
    '''s_delete : DELETE FROM ID WHERE expresion PTCOMA '''
    cons = ins.Delete(str(p[3], p[5]))
    lst_instrucciones.append(cons)

def p_insert(p):
    '''s_insert : INSERT INTO ID PARIZQ lista_id PARDER VALUES lista_values PTCOMA '''
    global lst_instrucciones
    cons = None
    for valores in p[8]:
        cons = ins.InsertT(p[3], p[5], valores)
        lst_instrucciones.append(cons)

def p_insert_2(p):
    '''s_insert : INSERT INTO ID VALUES lista_values PTCOMA '''
    global lst_instrucciones
    cons = None
    for valores in p[5]:
        cons = ins.InsertT(p[3], None, valores)
        lst_instrucciones.append(cons)

def p_lista_values(p):
    '''lista_values : lista_values COMA PARIZQ lista_valores PARDER
                     | PARIZQ lista_valores PARDER'''
    p[0] = []
    if p[1] == '(':
        p[0].append(p[2]) # [[lista_valores1]]
    else:
        p[1].append(p[4]) # [[lista_valores1][lista_valores2]...[lista_valoresn]]
        p[0] = p[1]

def p_lista_valores(p):
    '''lista_valores : lista_valores COMA valores'''
    p[1].append(p[3])
    p[0] = p[1]

def p_lista_valores_2(p):
    '''lista_valores : valores'''
    p[0] = []
    p[0].append(p[1])

def p_valores(p):
    '''valores : CADENA
               | ENTERO
               | DECIMA
               | TRUE
               | FALSE
               | ON
               | OFF'''
    if str(p[1]).upper() == 'ON' or str(p[1]).upper() == 'TRUE':
        p[0] = True
    elif str(p[1]).upper() == 'OFF' or str(p[1]).upper() == 'FALSE':
        p[0] = False
    else:
        p[0] = p[1]

def p_s_update(p):
    '''s_update : UPDATE ID SET lista_asig PTCOMA'''
    cons = ins.Update(p[2], p[4])
    lst_instrucciones.append(cons)

def p_s_update_2(p):
    '''s_update : UPDATE ID SET lista_asig WHERE expresion PTCOMA'''
    cons = ins.Update(p[2], p[4])
    lst_instrucciones.append(cons)

def p_lista_asig(p):
    '''lista_asig : lista_asig COMA ID IGUAL valores'''
    exp = str(p[3]) + str(p[4]) + str(p[5])
    arr = []
    arr.append(p[1])
    arr.append(exp)
    p[0] = arr

def p_lista_asig(p):
    '''lista_asig :  ID IGUAL valores'''
    exp = str(p[1]) + str(p[2]) + str(p[3])
    p[0] = exp

def p_expresion(p):
    '''expresion : IN expresion
                 | EXISTS expresion
                 | MENOS expresion %prec UMENOS
                 | SUMAS expresion %prec USUMAS
                 | PARIZQ expresion PARDER
                 | SUM PARIZQ expresion PARDER
                 | AVG PARIZQ expresion PARDER
                 | MAX PARIZQ expresion PARDER
                 | COUNT PARIZQ MULTI PARDER
                 | COUNT PARIZQ expresion PARDER
                 | expresion BETWEEN expresion
                 | temp_exp expresion
                 | SQRTROOT expresion
                 | CUBEROOT expresion
                 | BITAND expresion
                 | BITOR expresion
                 | BITXOR expresion
                 | BITNOT expresion
                 | BITSLEFT expresion
                 | BITSRIGHT expresion
                 | math_sw
                 | math_select
                 | trigonometric
                 | ext
                 | d_part
                 | binary_string
                 | s_select'''

def p_expresion1(p):
    '''expresion    : ID
                    | ID PUNTO ID '''
    p[0] = p[1]

def p_expresion_p(p):
    '''expresion    : CADENA
					| ENTERO
					| DECIMA
					| TRUE
					| FALSE'''
    primitivo = expre.primitivo(p[1])    
    p[0] = primitivo

def p_expresiones_2(p):
    '''expresion    : NOW PARIZQ PARDER
					| CURRENT_DATE
					| CURRENT_TIME '''


def p_expresion_3(p):
    '''expresion 	: expresion MAYOR expresion
					| expresion MENOR expresion
					| expresion MAYIG expresion
					| expresion MENIG expresion
					| expresion IGUAL expresion
					| expresion DIFEQ expresion'''
    if(p[2] == '>'):
        expresion_relacional = expre.expresion_relacional(p[1],p[2],'>')
    elif(p[2] == '<'):
        expresion_relacional = expre.expresion_relacional(p[1],p[2],'<')
    elif(p[2] == '>='):
        expresion_relacional = expre.expresion_relacional(p[1],p[2],'>=')
    elif(p[2] == '<='):
        expresion_relacional = expre.expresion_relacional(p[1],p[2],'<=')
    elif(p[2] == '='):
        expresion_relacional = expre.expresion_relacional(p[1],p[2],'=')
    elif(p[2] == '<>'):
        expresion_relacional = expre.expresion_relacional(p[1],p[2],'<>')

def p_expresion_4(p):
    '''expresion 	: expresion POTEN expresion
					| expresion MULTI expresion
					| expresion DIVIS expresion
					| expresion SUMAS expresion
					| expresion MENOS expresion'''

    if p[2] == '+' :
        expresion_arit = expre.expresion_aritmetica(p[1],p[2],'+')
        p[0] = expresion_arit
    elif p[2] == '-':
        expresion_arit = expre.expresion_aritmetica(p[1],p[2],'-')
        p[0] = expresion_arit
    elif p[2] == '*':
        expresion_arit = expre.expresion_aritmetica(p[1],p[2],'*')
        p[0] = expresion_arit
    elif p[2] == '/':
        expresion_arit = expre.expresion_aritmetica(p[1],p[2],'/')
        p[0] = expresion_arit
    elif p[2] == '\^':
        expresion_arit = expre.expresion_aritmetica(p[1],p[2],'\^')
        p[0] = expresion_arit


def p_expresion_5(p):
    '''expresion 	: expresion OR expresion
					| expresion AND expresion
					| NOT expresion'''
    if p[2].upper == 'OR':
        exp_ñpgica = expre.expresion_logica(p[1],p[3],'OR')
    elif p[2].upper == 'AND':
        exp_ñpgica = expre.expresion_logica(p[1],p[3],'AND')
    elif p[2].upper == 'NOT':
        exp_ñpgica = expre.expresion_logica(p[1],None,'NOT')


def p_math_sw(p):
    '''math_sw : ABS PARIZQ expresion PARDER
               | CBRT PARIZQ expresion PARDER
               | CEIL PARIZQ expresion PARDER
               | CEILING PARIZQ expresion PARDER'''

def p_math_select(p):
    '''math_select : DEGREES PARIZQ expresion PARDER
                   | DIV PARIZQ expresion COMA expresion PARDER
                   | EXP PARIZQ expresion PARDER
                   | FACTORIAL PARIZQ expresion PARDER
                   | FLOOR PARIZQ expresion PARDER
                   | GCD PARIZQ expresion PARDER
                   | LN PARIZQ expresion PARDER
                   | LOG PARIZQ expresion PARDER
                   | MOD PARIZQ expresion COMA expresion PARDER
                   | PI PARIZQ PARDER
                   | POWER PARIZQ expresion COMA expresion PARDER
                   | RADIANS PARIZQ expresion PARDER
                   | ROUND PARIZQ expresion PARDER
                   | SIGN PARIZQ expresion PARDER
                   | SQRT PARIZQ expresion PARDER
                   | WIDTH_BUCKET PARIZQ expresion lista_exp PARDER
                   | TRUNC PARIZQ expresion trunc1
                   | RANDOM PARIZQ PARDER'''

def p_lista_exp(p):
    '''lista_exp : lista_exp COMA expresion
                |  COMA expresion'''

def p_trunc1(p):
    '''trunc1 : COMA ENTERO PARDER
             | PARDER'''

def p_trigonometric(p):
    '''trigonometric : ACOS PARIZQ expresion PARDER
                     | ACOSD PARIZQ expresion PARDER
                     | ASIN PARIZQ expresion PARDER
                     | ASIND PARIZQ expresion PARDER
                     | ATAN PARIZQ expresion PARDER
                     | ATAND PARIZQ expresion PARDER
                     | ATAN2 PARIZQ expresion COMA expresion PARDER
                     | ATAN2D PARIZQ expresion COMA expresion PARDER
                     | COS PARIZQ expresion PARDER
                     | COSD PARIZQ expresion PARDER
                     | COT PARIZQ expresion PARDER
                     | COTD PARIZQ expresion PARDER
                     | SIN PARIZQ expresion PARDER
                     | SIND PARIZQ expresion PARDER
                     | TAN PARIZQ expresion PARDER
                     | TAND PARIZQ expresion PARDER
                     | SINH PARIZQ expresion PARDER
                     | COSH PARIZQ expresion PARDER
                     | ASINH PARIZQ expresion PARDER
                     | ACOSH PARIZQ expresion PARDER
                     | ATANH PARIZQ expresion PARDER'''

def p_ext(p):
    '''ext : EXTRACT PARIZQ time_type FROM temp_exp expresion PARDER
           | EXTRACT PARIZQ time_type FROM expresion PARDER'''

def p_time_type(p):
    '''time_type : YEAR
                 | MONTH
                 | DAY
                 | HOUR
                 | MINUTE
                 | SECOND'''

def p_d_part(p):
    'd_part : DATE_PART PARIZQ CADENA COMA temp_exp CADENA PARDER'

def p_temp_exp(p):
    '''temp_exp : TIMESTAMP
                | TIME
                | INTERVAL'''

def p_binary_string(p):
    '''binary_string : SHA256 PARIZQ expresion PARDER
                     | SUBSTR PARIZQ expresion COMA ENTERO COMA ENTERO PARDER
                     | GET_BYTE PARIZQ expresion COMA ENTERO PARDER
                     | SET_BYTE PARIZQ expresion COMA ENTERO COMA ENTERO PARDER
                     | CONVERT PARIZQ expresion AS data_type PARDER
                     | ENCODE PARIZQ expresion COMA expresion PARDER
                     | DECODE PARIZQ expresion COMA expresion PARDER
                     | bs_sw
                     | bs_iu
                     | bs_siuw'''

def p_bs_sw(p):
    'bs_sw : LENGTH PARIZQ expresion PARDER'

def p_bs_iu(p):
    'bs_iu : MD5 PARIZQ expresion PARDER'

def p_bs_siuw(p):
    '''bs_siuw : SUBSTRING PARIZQ expresion COMA ENTERO COMA ENTERO PARDER
               | TRIM PARIZQ trim1 PARDER'''

def p_trim(p):
    '''trim1 : trim2 FROM expresion
            | expresion'''

def p_trim1(p):
    '''trim2 : LEADING
             | TRAILING
             | BOTH'''


def p_exp_check(p):
    '''exp_check    : ID MAYOR valores
                    | ID MENOR valores
                    | ID MAYIG valores
                    | ID MENIG valores
                    | ID IGUAL valores
                    | ID DIFEQ valores'''
    p[0] = TS.const(None, p[3], p[2], TS.t_constraint.CHECK, p[1])

def p_error(p):
    print('error')
    if p == None:
        token = "end of file"
    else:
        token = f"{p.type}({p.value}) on line {p.lineno}"
    print(token)



# Construyendo el analizador sintáctico
parser = yacc.yacc()

#Funcion para concatenar los errores léxicos en una variable
def lex_error(lex, linea, columna):
    print('error')


def ejecutar(entrada):
    global parser, ts_global, lst_instrucciones
    consola = ''
    parse_result = parser.parse(entrada)
    for cons in lst_instrucciones :
        consola = consola + str(cons.execute(ts_global)) + '\n'
    ts_global.graficar()
    
    result = [parse_result, consola]
    return result

def tipo_data(tipo):
    data_type = ''
    if tipo.upper() == 'INTEGER':
        data_type = TS.tipo_simbolo.INTEGER
    elif tipo.upper() == 'MONEY':
        data_type = TS.tipo_simbolo.MONEY
    elif tipo.upper() == 'BIGINT':
        data_type = TS.tipo_simbolo.BIGINT
    elif tipo.upper() == 'SMALLINT':
        data_type = TS.tipo_simbolo.SMALLINT
    elif tipo.upper() == 'DECIMAL':
        data_type = TS.tipo_simbolo.DECIMAL
    elif tipo.upper() == 'D_PRECISION':
        data_type = TS.tipo_simbolo.D_PRECISION
    elif tipo.upper() == 'TEXT':
        data_type = TS.tipo_simbolo.TEXT
    elif tipo.upper() == 'CHAR':
        data_type = TS.tipo_simbolo.CHAR
    elif tipo.upper() == 'CHARACTER':
        data_type = TS.tipo_simbolo.CHARACTER
    elif tipo.upper() == 'CHARACTER_V':
        data_type = TS.tipo_simbolo.CHARACTER_V
    elif tipo.upper() == 'INTERVAL':
        data_type = TS.tipo_simbolo.INTERVAL
    elif tipo.upper() == 'VARCHAR':
        data_type = TS.tipo_simbolo.VARCHR
    elif tipo.upper() == 'TIMESTAMP':
        data_type = TS.tipo_simbolo.TIMESTAMP
    elif tipo.upper() == 'INTEGER':
        data_type = TS.tipo_simbolo.TIME
    elif tipo.upper() == 'DATA':
        data_type = TS.tipo_simbolo.DATA
    elif tipo.upper() == 'DOUBLE':
        data_type = TS.tipo_simbolo.D_PRECISION
    elif tipo.upper() == 'BOOLEAN':
        data_type = TS.tipo_simbolo.BOOLEAN
    elif tipo.upper() == 'DATE':
        data_type = TS.tipo_simbolo.DATE
    return data_type

    