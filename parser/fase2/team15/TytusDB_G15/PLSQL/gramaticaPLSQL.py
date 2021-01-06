# Global Variables
listaErroresLexicos = []
listaErroresSintacticos = []

# Declaracion palabras reservadas
reservadas = {
    'true' : 'TRUE',
    'false' : 'FALSE',
    'smallint' : 'SMALLINT',
    'integer': 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'precision':'PRECISION',
    'money':'MONEY',
    'character' : 'CHARACTER',
    'varying' : 'VARYING',
    'char': 'CHAR',
    'text': 'TEXT',
    'varchar' : 'VARCHAR',
    'double': 'DOUBLE',
    'float': 'FLOAT',
    'timestamp' : 'TIMESTAMP',
    'date' : 'DATE',
    'time' : 'TIME',
    'interval' : 'INTERVAL',
    'boolean' : 'BOOLEAN',
    'if': 'IF',
    'else': 'ELSE',
    'default': 'DEFAULT',
    'case': 'CASE',
    'void': 'VOID',
    'end' : 'END',
    'then' : 'THEN',
    'elseif': 'ELSEIF',
    'when' : 'WHEN',
    'create' :'CREATE',
    'function' : 'FUNCTION',
    'procedure' : 'PROCEDURE',
    'call' : 'CALL',
    'returns' : 'RETURNS',
    'as' : 'AS',
    'declare' : 'DECLARE',
    'begin' : 'BEGIN',
    'language' : 'LANGUAGE',
    'plpgsql' : 'PLPGSQL',
    'or' : 'OR',
    'replace' : 'REPLACE',
    'raise' : 'RAISE',
    'select' : 'SELECT',
    'database': 'DATABASE',
    'not' : 'NOT',
    'exists' : 'EXISTS',
    'owner': 'OWNER',
    'mode' : 'MODE',
    'show': 'SHOW',
    'tables':'TABLES',
    'use' : 'USE',
    'drop': 'DROP',
    'databases': 'DATABASES',
}

# Declaracion tokens
tokens = [
    'FLOTANTE',
    'ENTERO',
    'CADENA',
    'ID',
    'DOSPUNTOS',
    'PTCOMA',
    'PARA',
    'PARC',
    'LLAVEA',
    'LLAVEC',
    'CORCHETEA',
    'CORCHETEC',
    'COMA',
    'ANDB',
    'MENOS',
    'MAS',
    'POR',
    'DIV',
    'MOD',
    'AND',
    'ORR',
    'NOTB',
    'ORB',
    'XORB',
    'SHIFTI',
    'SHIFTD',
    'IGUALIGUAL',
    'MAYORIGUAL',
    'MENORIGUAL',
    'NOTIGUAL',
    'NOTT',
    'MAYOR',
    'MENOR',
    'IGUAL',
    'DOLAR'
         ] + list(reservadas.values())

# Tokens ER
t_DOSPUNTOS = r':'
t_COMA = r','
t_PTCOMA = r';'
t_PARA = r'\('
t_PARC = r'\)'
t_LLAVEA = r'{'
t_LLAVEC = r'}'
t_CORCHETEA = r'\['
t_CORCHETEC = r'\]'
t_ANDB = r'&'
t_MENOS = r'-'
t_MAS = r'\+'
t_POR = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_AND = r'&&'
t_ORR = r'\|\|'
t_NOTB = r'~'
t_ORB = r'\|'
t_XORB = r'\^'
t_SHIFTI = r'<<'
t_SHIFTD = r'>>'
t_IGUALIGUAL = r'=='
t_IGUAL = r'='
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_NOTIGUAL = r'!='
t_NOTT = r'!'
t_MAYOR = r'>'
t_MENOR = r'<'
t_DOLAR = r'\$'


# Caracteres ignorados (espacio)
t_ignore = " \t"

# Cadena ER
def t_CADENA(t):
    r'\".*?\"|\'.*?\''
    t.value = t.value[1:-1]  # remuevo las comillas
    return t


# Decimal ER
def t_FLOTANTE(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


# Entero ER
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


# Id de la forma aceptara ER
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')  # Check for reserved words
    return t


# Comentario multi linea
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1


# Salto de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# Error Lexico
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    listaErroresLexicos.append(ErrorLexico(t.value[0], t.lexer.lineno, t.lexpos))
    t.lexer.skip(1)

# Construyendo el analizador léxico


# Asociación de operadores y precedencia
precedence = (
    ('left', 'ORR'),
    ('left', 'AND'),
    ('left', 'XORB'),
    ('left', 'ORB'),
    ('left', 'ANDB'),
    ('left', 'IGUALIGUAL', 'NOTIGUAL'),
    ('left', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL'),
    ('left', 'SHIFTD', 'SHIFTI'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIV', 'MOD'),
    ('right', 'NOTT', 'NOTB', 'UMENOS'),
    ('left', 'PARA', 'PARC')
    )


# Importacion de clases para la creación del AST
from PLSQL.expresionesPLSQL import *
from PLSQL.instruccionesPLSQL import *

# Definición de la gramática ---------------------------------------------------------------------------------------------------
listaGramatica = []

def p_inicio(t):
    'inicio    : codigo'
    t[0] = t[1]

def p_lenguaje_augus(t):
    '''codigo    : instrucciones_globales_list'''
    t[0] = t[1]

def p_instrucciones_globales_list(t):
    'instrucciones_globales_list    : instrucciones_globales_list instrucciones_global_sent'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_globales_list_sent(t):
    'instrucciones_globales_list    : instrucciones_global_sent'
    t[0] = [t[1]]

def p_instrucciones_global_sent(t):
    '''instrucciones_global_sent    : funcion
                                    | llamada_funcion
                                    | createDB_insrt
                                    | show_databases_instr
                                    | show_tables_instr
                                    | use_database_instr
                                    | drop_database_instr'''
    t[0] = t[1]

def p_instrucciones_global_sent_error(t):
    'instrucciones_global_sent    : error'

def p_instrucciones_funct_list(t):
    'instrucciones_funct_list    : instrucciones_funct_list instrucciones_funct_sent'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_funct_list_sent(t):
    'instrucciones_funct_list    : instrucciones_funct_sent'
    t[0] = [t[1]]

def p_instrucciones_funct_sent(t):
    '''instrucciones_funct_sent    : asignacion
                                    | declaracion
                                    | imprimir
                                    | sentencia_if
                                    | sentencia_switch
                                    | PTCOMA
                                    | llamada_funcion
                                    | empty'''
    t[0] = t[1]

def p_instrucciones_funct_sent_error(t):
    'instrucciones_funct_sent    : error'

#CREATE TABLE 
def p_createDB(t):
    'createDB_insrt : CREATE DATABASE ID PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ';')

def p_createDB_wRP(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ';')

def p_createDB_wIfNot(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ';')

def p_createDB_wRP_wIN(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ';')

#?######################################################
# ANCHOR        UN PARAMETRO
#?######################################################

def p_createDB_up(t):
    'createDB_insrt : CREATE DATABASE ID createDB_unParam PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ';')

def p_createDB_wRP_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_unParam PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ';')

def p_createDB_wIfNot_up(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ';')

def p_createDB_wRP_wIN_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ';')

#?######################################################
# ANCHOR          DOS PARAMETROS
#?######################################################

def p_createDB_dp(t):
    'createDB_insrt : CREATE DATABASE ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ';')


def p_createDB_wRP_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ';')

def p_createDB_wIfNot_dp(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ';')

def p_createDB_wRP_wIN_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ';')



def p_createDB_dosParam_Owner(t):
    '''createDB_dosParam : OWNER string_type MODE ENTERO
                         | MODE ENTERO OWNER string_type'''
    cadena = str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' '+ str(t[4]) + ' '
    t[0] = cadena

def p_createDB_dosParam_Owner2(t):
    '''createDB_dosParam : OWNER string_type MODE IGUAL ENTERO
                         | OWNER IGUAL string_type MODE ENTERO
                         | MODE ENTERO OWNER IGUAL string_type
                         | MODE IGUAL ENTERO OWNER ID'''
    cadena = str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '
    t[0] = cadena

def p_createDB_dosParam_Owner3(t):
    '''createDB_dosParam : OWNER IGUAL string_type MODE IGUAL ENTERO
                         | MODE IGUAL ENTERO OWNER IGUAL ID'''
    cadena = str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '
    t[0] = cadena

def p_createDB_unParam_Owner(t):
    '''createDB_unParam : OWNER IGUAL string_type
                        | MODE IGUAL ENTERO'''
    cadena = t[1] + ' ' + t[2] + ' ' + str(t[3]) + ' '
    t[0] = cadena

def p_createDB_unParam_MODE(t):
    '''createDB_unParam : OWNER string_type
                        | MODE ENTERO'''
    cadena = t[1] + ' ' + str(t[2]) + ' '
    t[0] = cadena


#?######################################################
# TODO        GRAMATICA DROP DATABASE
#?######################################################


def p_instruccion_drop_database(t):
    '''drop_database_instr : DROP DATABASE IF EXISTS ID PTCOMA'''
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ';')

def p_instruccion_drop_database1(t):
    '''drop_database_instr : DROP DATABASE ID PTCOMA'''
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3]+ ';')



#?######################################################
# TODO        GRAMATICA SHOW DATABASE
#?######################################################

def p_instruccion_show_databases(t):
    'show_databases_instr : SHOW DATABASES PTCOMA'
    t[0] = ShowDatabases(t[1] + ' ' + t[2] +';')

#?######################################################
# ANCHOR        GRAMATICA SHOW TABLES
#?######################################################


def p_instruccion_showTables(t):
    'show_tables_instr : SHOW TABLES PTCOMA'
    t[0] = ShowTables(t[1] + ' ' + t[2] +';')

#?######################################################
# TODO        GRAMATICA USE DATABASE
#?######################################################


def p_instruccion_use_database(t):
    'use_database_instr : USE ID PTCOMA'
    t[0] = UseDatabase(t[1] + ' ' + t[2] +';')

def p_string_type(t):
    ''' string_type : CADENA '''
    cadena = '\\\''+t[1]+'\\\''
    t[0] = cadena

def p_string_type2(t):
    ' string_type : ID'
    t[0] = t[1]




def p_funcion(t):
    'funcion    : CREATE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'
    t[0] = Funcion(TIPO_DATO.INT, t[3], t[5], Principal(t[13]))

def p_funcion2(t):
    'funcion    : CREATE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR DECLARE instrucciones_funct_list BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'
    instrucs = []
    for instru1 in t[13]:
        instrucs.append(instru1)
    for instru2 in t[15]:
        instrucs.append(instru2)
    t[0] = Funcion(TIPO_DATO.INT, t[3], t[5], Principal(instrucs))

def p_funcion_r(t):
    'funcion    : CREATE OR REPLACE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'
    t[0] = Funcion(TIPO_DATO.INT, t[5], t[7], Principal(t[15]))

def p_funcion2_r(t):
    'funcion    : CREATE OR REPLACE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR DECLARE instrucciones_funct_list BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'
    instrucs = []
    for instru1 in t[15]:
        instrucs.append(instru1)
    for instru2 in t[17]:
        instrucs.append(instru2)
    t[0] = Funcion(TIPO_DATO.INT, t[5], t[7], Principal(instrucs))

#PROCEDURE
def p_procedure(t):
    'funcion    : CREATE PROCEDURE ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'
    t[0] = Funcion(TIPO_DATO.INT, t[3], t[5], Principal(t[13]))

def p_procedure2(t):
    'funcion    : CREATE PROCEDURE ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR DECLARE instrucciones_funct_list BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'
    instrucs = []
    for instru1 in t[13]:
        instrucs.append(instru1)
    for instru2 in t[15]:
        instrucs.append(instru2)
    t[0] = Funcion(TIPO_DATO.INT, t[3], t[5], Principal(instrucs))

def p_procedure_r(t):
    'funcion    : CREATE OR REPLACE PROCEDURE ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'
    t[0] = Funcion(TIPO_DATO.INT, t[5], t[7], Principal(t[15]))

def p_procedure2_r(t):
    'funcion    : CREATE OR REPLACE PROCEDURE ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR DECLARE instrucciones_funct_list BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'
    instrucs = []
    for instru1 in t[15]:
        instrucs.append(instru1)
    for instru2 in t[17]:
        instrucs.append(instru2)
    t[0] = Funcion(TIPO_DATO.INT, t[5], t[7], Principal(instrucs))
    

def p_llamada_funcion(t):
    'llamada_funcion    : SELECT ID PARA params PARC PTCOMA'
    t[0] = LlamadaFuncion(t[2], t[4])

def p_llamada_funcion1(t):
    'llamada_funcion    : CALL ID PARA params PARC PTCOMA'
    t[0] = LlamadaFuncion(t[2], t[4])

def p_params_list(t):
    'params     : params COMA expresion'
    t[1].append(t[3])
    t[0] = t[1]

def p_params_sent(t):
    '''params   : expresion
                | empty'''
    t[0] = [t[1]]

def p_parametros_list(t):
    'parametros     : parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]

def p_parametros_sent(t):
    'parametros     : parametro'
    t[0] = [t[1]]


def p_parametro1(t):
    'parametro       : ID tipo'
    t[0] = Parametro(t[2], t[1])

def p_parametro2(t):
    '''parametro       : empty'''
    t[0] = None

def p_sentencia_switch(t):
    'sentencia_switch   : CASE expresion case_list END CASE PTCOMA'
    t[0] = SentenciaCase(t[2], t[3])

def p_case_list_list(t):
    '''case_list    : case_list case'''
    t[1].append(t[2])
    t[0] = t[1]

def p_case_list_sent(t):
    '''case_list    : case'''
    t[0] = [t[1]]

def  p_case(t):
    '''case     : WHEN expresion THEN instrucciones_funct_list'''
    t[0] = Caso(t[2], Principal(t[4]))

def  p_case_default(t):
    '''case     : ELSE instrucciones_funct_list'''
    t[0] = Caso(None, Principal(t[2]))

def p_sentencia_if(t):
    'sentencia_if   : IF expresion THEN instrucciones_funct_list else END IF PTCOMA'
    t[0] = SentenciaIf(t[2], Principal(t[4]), t[5])

def p_sentencia_if_else1(t):
    'else     : ELSE instrucciones_funct_list '
    t[0] = Principal(t[2])

def p_sentencia_if_else2(t):
    'else     : ELSEIF expresion THEN instrucciones_funct_list else '
    t[0] = SentenciaIf(t[2], Principal(t[4]), t[5])

def p_sentencia_if_else3(t):
    'else     : '
    t[0] = None

def p_imprimir(t):
    'imprimir   : RAISE lista_imprimir PTCOMA'
    t[0] = Impresion(t[2])

def p_imprimir_lista(t):
    'lista_imprimir     : lista_imprimir COMA sent_imprimir'
    t[1].append(t[3])
    t[0] = t[1]

def p_imprimir_lista_sent(t):
    'lista_imprimir     : sent_imprimir'
    t[0] = [t[1]]

def p_imprimir_sent(t):
    'sent_imprimir  : expresion'
    t[0] = t[1]

def p_asignacion(t):
    'asignacion    : ID DOSPUNTOS IGUAL expresion PTCOMA'
    t[0] = Asignacion(t[1], t[4])

def p_definicion(t):
    'declaracion    :  ID tipo DOSPUNTOS IGUAL expresion PTCOMA'
    t[0] = ListaDeclaraciones(t[2], [Declaracion(t[1], t[5])])

def p_definicion_2(t):
    'declaracion    :  ID tipo PTCOMA'
    t[0] = ListaDeclaraciones(t[2], [Declaracion(t[1], None)])

def p_definicion_3(t):
    'declaracion    :  ID tipo DEFAULT expresion PTCOMA'
    t[0] = ListaDeclaraciones(t[2], [Declaracion(t[1], t[4])])

def p_tipo_dato(t):
    '''tipo     : INTEGER
                | SMALLINT
                | BIGINT
                | DECIMAL
                | NUMERIC
                | REAL
                | CHAR
                | DOUBLE
                | PRECISION
                | MONEY
                | FLOAT
                | BOOLEAN
                | VOID'''
    if t[1] == 'integer': t[0] = TIPO_DATO.INT
    elif t[1] == 'smallint': t[0] = TIPO_DATO.INT
    elif t[1] == 'bigint': t[0] = TIPO_DATO.INT
    elif t[1] == 'decimal': t[0] = TIPO_DATO.FLOAT
    elif t[1] == 'numeric': t[0] = TIPO_DATO.FLOAT
    elif t[1] == 'real': t[0] = TIPO_DATO.FLOAT
    elif t[1] == 'void': t[0] = TIPO_DATO.INT
    elif t[1] == 'char': t[0] = TIPO_DATO.CHAR
    elif t[1] == 'double': t[0] = TIPO_DATO.DOUBLE
    elif t[1] == 'precision': t[0] = TIPO_DATO.DOUBLE
    elif t[1] == 'money': t[0] = TIPO_DATO.DOUBLE
    elif t[1] == 'float': t[0] = TIPO_DATO.FLOAT
    elif t[1] == 'boolean': t[0] = TIPO_DATO.BOOLEAN

def p_tipo_dato_cadena(t):
    'tipo     : CHAR PARA ENTERO PARC'
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_cadena2(t):
    'tipo     : CHARACTER VARYING PARA ENTERO PARC'
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_cadena3(t):
    'tipo     : VARCHAR PARA ENTERO PARC'
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_cadena4(t):
    'tipo     : CHARACTER PARA ENTERO PARC'
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_cadena5(t):
    'tipo     : TEXT'
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_time(t):
    ' tipo :  TIME'
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_time2(t):
    ' tipo :  TIMESTAMP'
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_tim3(t):
    'tipo : DATE'
    t[0] = TIPO_DATO.STRING

def p_expresion(t):
    '''expresion    : log'''
    t[0] = t[1]

def p_log(t):
    '''log      : expresion AND expresion
                | expresion ORR expresion'''
    if t[2] == '&&':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.AND)
    elif t[2] == '||':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.OR)

def p_log_uni(t):
    '''log      : rel'''
    t[0] = t[1]


def p_rel(t):
    '''rel      : arit MAYOR arit
                | arit MENOR arit
                | arit MAYORIGUAL arit
                | arit MENORIGUAL arit
                | arit IGUALIGUAL arit
                | arit NOTIGUAL arit'''
    if t[2] == '>':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MAYOR)
    elif t[2] == '<':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MENOR)
    elif t[2] == '>=':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MAYORIGUAL)
    elif t[2] == '<=':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MENORIGUAL)
    elif t[2] == '==':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.IGUAL)
    elif t[2] == '!=':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.DIFERENTE)

def p_rel_arit(t):
    '''rel      : arit'''
    t[0] = t[1]

def p_arit(t):
    ''' arit    : arit POR arit
                | arit DIV arit
                | arit MAS arit
                | arit MENOS arit
                | arit MOD arit
                | arit ANDB arit
                | arit SHIFTI arit
                | arit SHIFTD arit
                | arit XORB arit
                | arit ORB arit'''
    if t[2] == '*':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.POR)
    elif t[2] == '/':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.DIVIDIDO)
    elif t[2] == '+':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MAS)
    elif t[2] == '-':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MENOS)
    elif t[2] == '%':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MOD)
    elif t[2] == '&':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.ANDB)
    elif t[2] == '<<':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.SHIFTI)
    elif t[2] == '>>':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.SHIFTD)
    elif t[2] == '|':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.ORB)
    elif t[2] == '^':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.XORB)

def p_arit_parentecis(t):
    ''' arit    : PARA expresion PARC'''
    t[0] = t[2]

def p_arit_ID(t):
    ''' arit    : ID'''
    t[0] = ExpresionIdentificador(t[1])

def p_arit_cadena(t):
    ''' arit    : CADENA'''
    t[0] = ExpresionCadena(t[1])

def p_arit_numero(t):
    ''' arit    : ENTERO
                | FLOTANTE
                | MENOS expresion %prec UMENOS
                | NOTB expresion
                | NOTT expresion'''
    if t[1] == '-' :
        t[0] = ExpresionNegativo(t[2])
    elif t[1] == '~' :
        t[0] = ExpresionNOTBIN(t[2])
    elif t[1] == '!':
        t[0] = ExpresionNOT(t[2])
    else:
        t[0] = ExpresionNumero(t[1])

def p_arit_numero1(t):
    ''' arit    : TRUE'''
    t[0] = ExpresionBooleana(t[1])

def p_arit_numero2(t):
    ''' arit    : FALSE'''
    t[0] = ExpresionBooleana(t[1])

# Epsilon
def p_empty(t):
    'empty :'
    pass

# Errores Sintacticos
def p_error(t):
    print("Error sintáctico en '%s'" % t.value)
    listaErroresSintacticos.append(ErrorLexico(t.value, t.lineno, t.lexpos))


# Función para realizar analisis
def parse(input):
    import ply.yacc as yacc
    parser = yacc.yacc()
    import ply.lex as lex
    lexer = lex.lex()
    return parser.parse(input)

