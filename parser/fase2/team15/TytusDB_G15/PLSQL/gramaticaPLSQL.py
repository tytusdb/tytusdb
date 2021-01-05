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
    'select' : 'SELECT'
}

# Declaracion tokens
tokens = [
    'FLOTANTE',
    'ENTERO',
    'CADENA',
    'ID',
    'DOSPUNTOS',
    'PUNTOYCOMA',
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
    'NOT',
    'MAYOR',
    'MENOR',
    'IGUAL',
    'DOLAR'
         ] + list(reservadas.values())

# Tokens ER
t_DOSPUNTOS = r':'
t_COMA = r','
t_PUNTOYCOMA = r';'
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
t_NOT = r'!'
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
    ('right', 'NOT', 'NOTB', 'UMENOS'),
    ('left', 'PARA', 'PARC')
    )


# Importacion de clases para la creación del AST

# Definición de la gramática ---------------------------------------------------------------------------------------------------
listaGramatica = []

def p_inicio(t):
    'inicio    : codigo'

def p_lenguaje_augus(t):
    '''codigo    : instrucciones_globales_list'''

def p_instrucciones_globales_list(t):
    'instrucciones_globales_list    : instrucciones_globales_list instrucciones_global_sent'

def p_instrucciones_globales_list_sent(t):
    'instrucciones_globales_list    : instrucciones_global_sent'

def p_instrucciones_global_sent(t):
    '''instrucciones_global_sent    : funcion
                                    | llamada_funcion'''

def p_instrucciones_global_sent_error(t):
    'instrucciones_global_sent    : error'

def p_instrucciones_funct_list(t):
    'instrucciones_funct_list    : instrucciones_funct_list instrucciones_funct_sent'

def p_instrucciones_funct_list_sent(t):
    'instrucciones_funct_list    : instrucciones_funct_sent'

def p_instrucciones_funct_sent(t):
    '''instrucciones_funct_sent    : asignacion
                                    | declaracion
                                    | imprimir
                                    | sentencia_if
                                    | sentencia_switch
                                    | PUNTOYCOMA
                                    | llamada_funcion
                                    | empty'''

def p_instrucciones_funct_sent_error(t):
    'instrucciones_funct_sent    : error'

def p_funcion(t):
    'funcion    : CREATE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR BEGIN instrucciones_funct_list END PUNTOYCOMA DOLAR DOLAR LANGUAGE PLPGSQL PUNTOYCOMA'

def p_funcion2(t):
    'funcion    : CREATE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR DECLARE instrucciones_funct_list BEGIN instrucciones_funct_list END PUNTOYCOMA DOLAR DOLAR LANGUAGE PLPGSQL PUNTOYCOMA'
    
def p_funcion_r(t):
    'funcion    : CREATE OR REPLACE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR BEGIN instrucciones_funct_list END PUNTOYCOMA DOLAR DOLAR LANGUAGE PLPGSQL PUNTOYCOMA'

def p_funcion2_r(t):
    'funcion    : CREATE OR REPLACE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR DECLARE instrucciones_funct_list BEGIN instrucciones_funct_list END PUNTOYCOMA DOLAR DOLAR LANGUAGE PLPGSQL PUNTOYCOMA'
    
#PROCEDURE
def p_procedure(t):
    'funcion    : CREATE PROCEDURE ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR BEGIN instrucciones_funct_list END PUNTOYCOMA DOLAR DOLAR LANGUAGE PLPGSQL PUNTOYCOMA'

def p_procedure2(t):
    'funcion    : CREATE PROCEDURE ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR DECLARE instrucciones_funct_list BEGIN instrucciones_funct_list END PUNTOYCOMA DOLAR DOLAR LANGUAGE PLPGSQL PUNTOYCOMA'
    
def p_procedure_r(t):
    'funcion    : CREATE OR REPLACE PROCEDURE ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR BEGIN instrucciones_funct_list END PUNTOYCOMA DOLAR DOLAR LANGUAGE PLPGSQL PUNTOYCOMA'
  
def p_procedure2_r(t):
    'funcion    : CREATE OR REPLACE PROCEDURE ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR DECLARE instrucciones_funct_list BEGIN instrucciones_funct_list END PUNTOYCOMA DOLAR DOLAR LANGUAGE PLPGSQL PUNTOYCOMA'
   
def p_llamada_funcion(t):
    'llamada_funcion    : SELECT ID PARA params PARC PUNTOYCOMA'
  
def p_llamada_funcion1(t):
    'llamada_funcion    : CALL ID PARA params PARC PUNTOYCOMA'
   
def p_params_list(t):
    'params     : params COMA expresion'
  

def p_params_sent(t):
    '''params   : expresion
                | empty'''

def p_parametros_list(t):
    'parametros     : parametros COMA parametro'


def p_parametros_sent(t):
    'parametros     : parametro'

def p_parametro1(t):
    'parametro       : ID tipo'

def p_parametro2(t):
    '''parametro       : empty'''

def p_sentencia_switch(t):
    'sentencia_switch   : CASE expresion case_list END CASE PUNTOYCOMA'

def p_case_list_list(t):
    '''case_list    : case_list case'''

def p_case_list_sent(t):
    '''case_list    : case'''

def  p_case(t):
    '''case     : WHEN expresion THEN instrucciones_funct_list'''

def  p_case_default(t):
    '''case     : ELSE instrucciones_funct_list'''

def p_sentencia_if(t):
    'sentencia_if   : IF expresion THEN instrucciones_funct_list else END IF PUNTOYCOMA'

def p_sentencia_if_else1(t):
    'else     : ELSE instrucciones_funct_list '
def p_sentencia_if_else2(t):
    'else     : ELSEIF expresion THEN instrucciones_funct_list else '

def p_sentencia_if_else3(t):
    'else     : '

def p_imprimir(t):
    'imprimir   : RAISE lista_imprimir PUNTOYCOMA'

def p_imprimir_lista(t):
    'lista_imprimir     : lista_imprimir COMA sent_imprimir'

def p_imprimir_lista_sent(t):
    'lista_imprimir     : sent_imprimir'

def p_imprimir_sent(t):
    'sent_imprimir  : expresion'
def p_asignacion(t):
    'asignacion    : ID DOSPUNTOS IGUAL expresion PUNTOYCOMA'

def p_definicion(t):
    'declaracion    :  ID tipo DOSPUNTOS IGUAL expresion PUNTOYCOMA'

def p_definicion_2(t):
    'declaracion    :  ID tipo PUNTOYCOMA'

def p_definicion_3(t):
    'declaracion    :  ID tipo DEFAULT expresion PUNTOYCOMA'

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

def p_tipo_dato_cadena(t):
    'tipo     : CHAR PARA ENTERO PARC'

def p_tipo_dato_cadena2(t):
    'tipo     : CHARACTER VARYING PARA ENTERO PARC'

def p_tipo_dato_cadena3(t):
    'tipo     : VARCHAR PARA ENTERO PARC'

def p_tipo_dato_cadena4(t):
    'tipo     : CHARACTER PARA ENTERO PARC'

def p_tipo_dato_cadena5(t):
    'tipo     : TEXT'

def p_tipo_dato_time(t):
    ' tipo :  TIME'

def p_tipo_dato_time2(t):
    ' tipo :  TIMESTAMP'

def p_tipo_dato_tim3(t):
    'tipo : DATE'

def p_expresion(t):
    '''expresion    : log'''

def p_log(t):
    '''log      : expresion AND expresion
                | expresion ORR expresion'''

def p_log_uni(t):
    '''log      : rel'''


def p_rel(t):
    '''rel      : arit MAYOR arit
                | arit MENOR arit
                | arit MAYORIGUAL arit
                | arit MENORIGUAL arit
                | arit IGUALIGUAL arit
                | arit NOTIGUAL arit'''

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

def p_arit_parentecis(t):
    ''' arit    : PARA expresion PARC'''

def p_arit_ID(t):
    ''' arit    : ID'''

def p_arit_cadena(t):
    ''' arit    : CADENA'''

def p_arit_numero(t):
    ''' arit    : ENTERO
                | FLOTANTE
                | MENOS expresion %prec UMENOS
                | NOTB expresion
                | NOT expresion'''
def p_arit_numero1(t):
    ''' arit    : TRUE'''

def p_arit_numero2(t):
    ''' arit    : FALSE'''

# Epsilon
def p_empty(t):
    'empty :'
    pass

# Errores Sintacticos
def p_error(t):
    print("Error sintáctico en '%s'" % t.value)


# Función para realizar analisis
def parse(input):
    import ply.yacc as yacc
    parser = yacc.yacc()
    import ply.lex as lex
    lexer = lex.lex()
    return parser.parse(input)

parse('SELECT hola();')

