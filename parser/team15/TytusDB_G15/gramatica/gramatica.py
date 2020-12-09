# -----------------------------------------------------------------------------
# Gramatica del Proyecto Fase 1 - Compiladores 2
# -----------------------------------------------------------------------------


reservadas = {
    'select': 'SELECT',
    'insert': 'INSERT',
    'update': 'UPDATE',
    'delete': 'DELETE',
    'count': 'COUNT',
    'from': 'FROM',
    'into': 'INTO',
    'values': 'VALUES',
    'sum' : 'SUM',
    'set': 'SET',
    'inner': 'INNER',
    'join': 'JOIN',
    'on': 'ON',
    'case': 'CASE',
    'when': 'WHEN',
    'then': 'THEN',
    'end': 'END',
    'and': 'AND',
    'or': 'OR',
    'else': 'ELSE',
    'where': 'WHERE',
    'as': 'AS',
    'create': 'CREATE',
    'table': 'TABLE',
    'inherits': 'INHERITS',
    'alter': 'ALTER',
    'database': 'DATABASE',
    'to': 'TO',
    'rename': 'RENAME',
    'owner': 'OWNER',
    'drop': 'DROP',
    'currUser' : 'CURRENT_USER',
    'sessUser' : 'SESSION_USER',
    'foreign' : 'FOREIGN',
    'key': 'KEY',
    'add' : 'ADD',
    'check' : 'CHECK',
    'constraint': 'CONSTRAINT',
    'column' : 'COLUMN',
    'unique' : 'UNIQUE',
    'references' : 'REFERENCES',
    'type' : 'TYPE',
    'set' : 'SET',
    'not' : 'NOT',
    'null' : 'NULL',
    'text': 'TEXT',
    'float': 'FLOAT',
    'int': 'INT',
    'char': 'CHAR',
    'varchar' : 'VARCHAR',
    'smallint':'SMALLINT',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'double' : 'DOUBLE',
    'precision' : 'PRECISION',
    'money' : 'MONEY',
    'character' : 'CHARACTER',
    'varying' : 'VARYING',
    'timestamp' : 'TIMESTAMP',
    'date' : 'DATE',
    'time' : 'TIME',
    'interval' : 'INTERVAL',
    'year' : 'YEAR',
    'month' : 'MONTH',
    'day' : 'DAY',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'to' : 'TO',
    'hour': 'HOUR',
    'boolean' : 'BOOLEAN',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'enum' : 'ENUM'

}

tokens = [
    'PTCOMA',
    'ASTERISCO',
    'COMA',
    'PAR_A',
    'PAR_C',
    'ENTERO',
    'CADENA',
    'ID',
    'PUNTO',
    'MENIGQUE',
    'MAYIGQUE',
    'MENQUE',
    'MAYQUE',
    'DOBLEIG',
    'NOIG',
    'APOSTROFE',
    'IGUAL'
] + list(reservadas.values())

#tokens
t_PTCOMA        = r';'
t_ASTERISCO     = r'\*'
t_COMA          = r','
t_PAR_A         = r'\('
t_PAR_C         = r'\)'
t_PUNTO         = r'.'
t_MENIGQUE      = r'<='
t_MAYIGQUE      = r'>='
t_MENQUE        = r'\<'
t_MAYQUE        = r'\>'
t_DOBLEIG       = r'=='
t_NOIG          = r'!='
t_IGUAL         = r'\='
t_APOSTROFE     = r'\''

def t_FLOTANTE(t):
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

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


# Asociación de operadores y precedencia


# Definición de la gramática

def p_init(t) :
    'init            : instrucciones'


def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'


def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
                        

def p_instruccion(t):
    '''instruccion : create_Table_isnrt 
                  | select_insrt
                  | insert_insrt 
                  | delete_insrt
                  | update_insrt
                  | alterDB_insrt
                  | alterTable_insrt
                  | drop_insrt'''

'----------- GRAMATICA PARA LA INSTRUCCION DROP TABLE----------'
def p_dropTable(t):
    ' drop_insrt : DROP TABLE lista_tablas_lista PTCOMA'

def p_lista_tabla_lista(t):
    ' lista_tablas_lista : lista_tablas_lista COMA lista_tabla'

def p_lista_tabla(t):
    ' lista_tablas_lista : lista_tabla'

def p_tablas_lista(t):
    ' lista_tabla : ID'

'----------- GRAMATICA PARA LA INSTRUCCION ALTER DATABASE ---------'
def p_AlterDB(t):
    ' alterDB_insrt : ALTER DATABASE ID opcion_alterDB'

def p_opcion_AlterDB(t):
    ''' opcion_alterDB : RENAME TO ID PTCOMA
                          | OWNER TO usuarioDB PTCOMA'''

def p_usuarioDB(t):
    '''usuarioDB : ID
                | CURRENT_USER
                | SESSION_USER'''

'----------- GRAMATICA PARA LA INSTRUCCION ALTER TABLE ---------'
def p_alterTable(t):
    'alterTable_insrt : ALTER TABLE ID alterTable_type PTCOMA'

def p_alterTable_type(t):
    '''alterTable_type : ADD alterTable_add
                       | alterTable_alter
                       | '''
# ---------necesita modificaciones-------------------------

def p_alterTable_add(t):
    '''alterTable_add : COLUMN ID TIPO_DATO
                      | CHECK PAR_A expresion_logica PAR_C 
                      | CONSTRAINT ID constraint_esp 
                      | FOREIGN KEY PAR_A campos_c PAR_C REFERENCES campos_c'''
def p_constraint_esp(t):
   '''constraint_esp : CHECK PAR_A expresion_logica PAR_C
                     | UNIQUE PAR_A campos_c PAR_C
                     | FOREIGN KEY PAR_A campos_c PAR_C REFERENCES campos_c'''

def p_alerTable_alter(t):
    '''alterTable_alter : alterTable_alter COMA Table_alter
                       | Table_alter'''

def p_Table_alter(t):
    'Table_alter : ALTER COLUMN ID alter_type'

def p_alter_type(t):
   '''alter_type : TYPE TIPO_DATO
                 | SET NOT NULL '''

#def p_alterTable_add_col(t):
 #   '''alterTable_add_col : TYPE TIPO_DATO '''     

def p_cons_campos(t):
    '''campos_c : campos_c COMA ID
                  | ID '''

' ---------- GRAMATICA PARA LA INSTRUCCION CREATE TABLE ---------'

def p_create_table(t):
    ''' create_Table_isnrt : CREATE TABLE ID PAR_A cuerpo_createTable_lista PAR_C PTCOMA
                           | CREATE TABLE ID PAR_A cuerpo_createTable_lista PAR_C herencia PTCOMA '''

def p_herencia(t):
    ' herencia :  INHERITS PAR_A ID PAR_C'

def p_cuerpo_createTable_lista(t):
    ' cuerpo_createTable_lista : cuerpo_createTable_lista COMA cuerpo_createTable'

def p_cuerpo_createTable(t):
    ' cuerpo_createTable_lista : cuerpo_createTable'

def p_createTable(t):
    ' cuerpo_createTable :  ID TIPO_DATO'

def p_tipo_dato(t):
    ''' TIPO_DATO : TEXT 
                  | FLOAT
                  | INT
                  | SMALLINT
                  | DECIMAL PAR_A ENTERO COMA ENTERO PAR_C
                  | NUMERIC PAR_A ENTERO COMA ENTERO PAR_C
                  | BIGINT
                  | REAL
                  | DOUBLE PRECISION 
                  | CHARACTER VARYING PAR_A ENTERO PAR_C
                  | TIMESTAMP
                  | TIME
                  | DATE
                  | INTERVAL APOSTROFE ID APOSTROFE
                  | VARCHAR PAR_A ENTERO PAR_C
                  | CHAR PAR_A ENTERO PAR_C'''

# Nota: Decimal y numeric requieren (p,s) presicion (numero de digitos en total) y scale (cantidad de digitos despues del punto decimal)
# Nota2: como se usa real?, completar date/time types
# interval (p) define la fraccion de digitos en segundos, valido de 0-6
#def p_tiempo_i(t):
 #   '''tiempo_i : tiempo_i tiempo
  #              | tiempo '''

' ----------- GRAMATICA PARA LA INSTRUCCION UPDATE ------'
def p_update_insrt(t):
    ' update_insrt : UPDATE ID SET lista_update WHERE ID IGUAL datos_insert PTCOMA'

def p_lista_update(t):
    ' lista_update :  lista_update COMA parametro_update'

def p_lista_update_lista(t):
    ' lista_update : parametro_update'

def p_parametro_update(t):
    ' parametro_update : ID IGUAL datos_insert'

' ---------- GRAMATICA PARA LA INSTRUCCION DELETE --------'
def p_delete_insrt(t):
    ' delete_insrt : DELETE FROM ID WHERE ID IGUAL CADENA PTCOMA'

' ------------- GRAMATICA PARA LA INSTRUCCION SELECT --------------'

def p_instruccion_select_insrt(t):
    ''' select_insrt : SELECT opcion_select_lista FROM ID AS ID PTCOMA
                     | SELECT opcion_select_lista FROM ID AS ID LISTA_SELECT_LISTA PTCOMA '''

def p_LISTA_SELECT_LISTA(t):
    ''' LISTA_SELECT_LISTA : LISTA_SELECT_LISTA  LISTA_SELECT  '''

def p_OPCIONES_SELECT_LISTA(t):
    ' LISTA_SELECT_LISTA : LISTA_SELECT'

def p_LISTA_SELECT(t):
    ''' LISTA_SELECT : INNER_JOIN
                     | WHERE_INSRT '''
            
def p_WHERE_INSRT(t):
    ' WHERE_INSRT : WHERE expresion_logica'

def p_select_lista(t):
    ' opcion_select_lista : opcion_select_lista COMA opcion_select'

def p_opcion_select_lista(t):
    ' opcion_select_lista : opcion_select '

def p_opcion_select(t):
    ''' opcion_select : ASTERISCO
                      | sum_insrt 
                      | count_insrt
                      | ID 
                      | ID PUNTO ID
                      | case_insrt'''

' ---------- GRAMATICA PARA LA INSTRUCCION DE CASE --------------'
def p_case_insrt(t):
    ''' case_insrt : CASE ID estructura_when_lista ELSE datos_insert END
                    | CASE estructura_when_lista ELSE datos_insert END'''

def p_estructura_when_lista(t):
    ' estructura_when_lista : estructura_when_lista estructura_when '

def p_opcion_estructura_when(t):
    ' estructura_when_lista : estructura_when'

def p_estructura_when(t):
    ' estructura_when : WHEN expresion_logica THEN datos_insert'

' ---------- GRAMATICA PARA LA INSTRUCCION DE INNER JOIN ----------'
def p_INNER_JOIN(t):
    'INNER_JOIN : INNER JOIN ID AS ID ON CONDICION_INNER_JOIN'

def p_CONDICION_INNER_JOIN(t):
    'CONDICION_INNER_JOIN : expresion_logica'


' ---------- GRAMATICA PARA LA INSTRUCCION DE SUM ----------'
def p_sum_insert(t):
    ' sum_insrt : SUM PAR_A ID PAR_C'

' ---------- GRAMATICA PAR LA INSTRUCCIONN DE COUNT ---------'
def p_count_insrt(t):
    ''' count_insrt : COUNT PAR_A ID PAR_C 
                    | COUNT PAR_A ASTERISCO PAR_C'''

' --------- GRAMATICA PARA LA INSTRUCCION INSERT  -------'

def p_insert_insrt(t):
    ' insert_insrt : INSERT INTO ID PAR_A lista_parametros_lista PAR_C  VALUES PAR_A lista_datos PAR_C PTCOMA'


' -------- GRAMATICA PARA LA LISTA DE PARAMETROS DEL INSERT ----------'

def p_lista_parametros_lista(t):
    ' lista_parametros_lista : lista_parametros_lista COMA lista_parametros'

def p_lista_parametros(t):
    ' lista_parametros_lista : lista_parametros'

def p_parametros(t):
    ' lista_parametros : ID'

'------- GRAMATICA PARA LA LISTA DE DATOS DEL INSERT -------' 

def p_parametros_lista_datos(t):
    ' lista_datos : lista_datos COMA datos_insert'

def p_datos_insert_lista(t):
    ' lista_datos : datos_insert'

def p_datos_insert(t):
    ''' datos_insert : CADENA
                     | ENTERO 
                     | PAR_A expresion_logica PAR_C
                     | ID 
                     | ID PUNTO ID'''

' --------------- EXPRESIONES -----------------------'
def p_expresion_relacional(t):
    ''' expresion_relacional : datos_insert MAYQUE datos_insert
                             | datos_insert MENQUE datos_insert
                             | datos_insert MAYIGQUE datos_insert
                             | datos_insert MENIGQUE datos_insert
                             | datos_insert DOBLEIG datos_insert
                             | datos_insert IGUAL datos_insert
                             | datos_insert NOIG datos_insert
                             | datos_insert '''

def p_expresion_logica(t):
    ''' expresion_logica : expresion_relacional AND expresion_logica
                        | expresion_relacional OR expresion_logica
                        | expresion_relacional''' 

def p_error(t):
    print("Error sintáctico en '%s'" % t.value, str(t.lineno),find_column(str(input), t))
    

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    print((token.lexpos - line_start) + 1)
    return (token.lexpos - line_start) + 1

import ply.yacc as yacc
parser = yacc.yacc()

f = open("./entrada.txt", "r")
input = f.read()
print(input)
parser.parse(input)


