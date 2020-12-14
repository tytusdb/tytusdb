import ply.yacc as yacc
from lexicosql import tokens

# _______________________________________________________________________________________________________________________________
#                                                          PARSER
# _______________________________________________________________________________________________________________________________

# ---------------- MANEJO DE LA PRECEDENCIA
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'IGUAL', 'DIFERENTE', 'DIFERENTE2'),
    ('left', 'MENOR', 'MAYOR', 'MENORIGUAL', 'MAYORIGUAL'),
    ('left', 'OR'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'ASTERISCO', 'DIVISION', 'AND', 'OR'),
    ('left', 'XOR', 'MODULO'),
    ('right', 'UMENOS', 'NOT', 'UMAS')
)


def p_init(p):
    'init : instrucciones'
    p[0] = [p[1]]


def p_instrucciones_list(p):
    '''instrucciones    : instrucciones instruccion '''
    p[1].append(p[2])
    p[0] = p[1]


def p_instrucciones_instruccion(p):
    'instrucciones  :   instruccion'
    p[0] = [p[1]]


def p_instruccion(p):
    '''instruccion :  sentenciaUpdate PTCOMA 
                    | sentenciaDelete PTCOMA
                    | insert PTCOMA
                    | definicion PTCOMA'''
    p[0] = p[1]
# __________________________________________definicion

# <DEFINICION> ::= 'create' 'type' 'as' 'enum' '(' <LISTA_ENUM> ')'
#               | <CREATE_OR_REPLACE> 'database' <COMBINACIONES1>
#               | 'show' 'databases' 'like' regex
#               | 'show' 'databases'
#               | 'alter' 'database' id <ALTER>
#               | 'drop' 'database' 'if' 'exists' id
#               | 'drop' 'database' id
#               | 'drop' 'table' id
#               | 'create' 'table' id (<COLUMNAS>)<INHERITS>
#               | 'create' 'table' id (<COLUMNAS>)


def p_definicion_1(p):
    'definicion : CREATE TYPE AS ENUM PABRE lista_enum PCIERRA'


def p_definicion_2(p):
    'definicion : create_or_replace DATABASE combinaciones1'


def p_definicion_3(p):
    'definicion : SHOW DATABASES LIKE REGEX'


def p_definicion_4(p):
    'definicion : SHOW DATABASES'


def p_definicion_5(p):
    'definicion : ALTER DATABASE ID  alter'


def p_definicion_6(p):
    'definicion : DROP DATABASE IF EXISTS ID'


def p_definicion_7(p):
    'definicion : DROP DATABASE ID'


def p_definicion_8(p):
    'definicion : DROP TABLE ID'


def p_definicion_9(p):
    'definicion : CREATE TABLE ID PABRE columnas PCIERRA inherits'


def p_definicion_10(p):
    'definicion : CREATE TABLE ID PABRE columnas PCIERRA'

# __________________________________________ lista_enum
# <LISTA_ENUM> ::= <ITEM>
#               | <LISTA_ENUM> ',' <ITEM>


def p_lista_enum_1(p):
    'lista_enum : item'


def p_lista_enum_2(p):
    'lista_enum : lista_enum COMA item'
# __________________________________________ ITEM
# <ITEM> ::= cadena


def p_item(p):
    'item : CADENA'

# __________________________________________ create_or_replace
# <CREATE_OR_REPLACE> ::= 'create'
#                      | 'create or replace'


def p_create_or_replace_1(p):
    'create_or_replace : CREATE'


def p_create_or_replace_2(p):
    'create_or_replace : CREATE OR REPLACE'

# __________________________________________ combinaciones1
# <COMBINACIONES1> ::= 'if' 'not' 'exists' id <COMBINACIONES2>
#                   | id <COMBINACIONES2>
#                   | id


def p_combinaciones1_1(p):
    'combinaciones1 : IF NOT EXISTS ID combinaciones2'


def p_combinaciones1_2(p):
    'combinaciones1 : ID combinaciones2'


def p_combinaciones1_3(p):
    'combinaciones1 : ID'
# ________________________________________ combinaciones2
# <COMBINACIONES2> ::= <OWNER>
#                   |<MODE>
#                   |<OWNER><MODE>


def p_combinaciones2_1(p):
    'combinaciones2 : owner'


def p_combinaciones2_2(p):
    'combinaciones2 : mode'


def p_combinaciones2_3(p):
    'combinaciones2 : owner mode'

# ________________________________________ <OWNER>
# <OWNER> ::= 'owner' id
#          | 'owner' '=' id


def p_owner_1(p):
    'owner : OWNER ID'


def p_owner_2(p):
    'owner : OWNER IGUAL ID'

# ________________________________________ <MODE>
# <MODE> ::= 'mode' entero
#         | 'mode' '=' entero


def p_mode_1(p):
    'mode : MODE NUMERO'


def p_mode_2(p):
    'mode : MODE IGUAL NUMERO'


# _________________________________________ <alter>
# <ALTER> ::= 'rename to' id
#          | 'owner to' <NEW_OWNER>

def p_alter_1(p):
    'alter : RENAME TO ID '


def p_alter_2(p):
    'alter : OWNER TO new_owner '

# _________________________________________ new_owner
#  <NEW_OWNER> ::= id
#              | 'current_user'
#              | 'session_user'


def p_new_owner_1(p):
    'new_owner : ID '


def p_new_owner_2(p):
    'new_owner : CURRENT_USER '


def p_new_owner_3(p):
    'new_owner : SESSION_USER'

# _________________________________________ inherits
# <INHERITS> ::= 'INHERITS' '('ID')'


def p_inherits(p):
    'inherits : INHERITS PABRE ID PCIERRA'

# _________________________________________ columnas
# <COLUMNAS> ::= <COLUMNA>
#             | <COLUMNAS>, <COLUMNA>


def p_columnas_1(p):
    'columnas : columna'


def p_columnas_2(p):
    'columnas : columnas COMA columna'


# _________________________________________ columna
#  <COLUMNA> ::=
#             | id' <TIPO>
#             | id' <TIPO> <listaOpciones>
#             | 'constraint' 'id' 'check' (<LISTA_CONDICIONES>)
#             | 'id' 'check' (<LISTA_CONDICIONES>)
#             | 'unique' (<LISTA_IDS>)
#             | 'primary' 'key' (<LISTA_IDS>)
#             | 'foreign' 'key' (<LISTA_IDS>) 'references' 'id' (<LISTA_IDS>)

# listaOpciones> ::= <listaOpciones> <opCol>
#                  | <opCol>

# <opCol>   ::=  <DEFAULT>
#             |  <CONSTRAINTS>
#             |  <CHECKS>
#             |  <nulleable>
#             |  'primary' 'key'
#             |  'references' 'id'

# ___________________________________________ declaracion de columna
def p_columna_1(p):
    'columna : ID tipo'


def p_columna_2(p):
    'columna : ID tipo listaOpciones'


def p_columna_3(p):
    'columna : CONSTRAINT  ID CHECK PABRE lista_condiciones PCIERRA '


def p_columna_4(p):
    'columna : UNIQUE PABRE lista_ids PCIERRA'


def p_columna_5(p):
    'columna :  PRIMARY KEY PABRE lista_ids PCIERRA'


def p_columna_6(p):
    'columna : FOREIGN KEY PABRE lista_ids PCIERRA REFERENCES ID PABRE lista_ids PCIERRA'


def p_columna_7(p):
    'columna : CHECK PABRE lista_condiciones PCIERRA'


def p_listaOpciones_List(p):
    'listaOpciones : listaOpciones opCol'


def p_listaOpciones_una(p):
    'listaOpciones : opCol'


def p_opCol_1(p):
    'opCol : default'


def p_opCol_2(p):
    'opCol : constraints'


def p_opCol_3(p):
    'opCol :  checks'


def p_opCol_4(p):
    'opCol :  PRIMARY KEY'


def p_opCol_5(p):
    'opCol : REFERENCES ID'


def p_opCol_6(p):
    'opCol : nullable'


# __________________________________________ <TIPO>

# <TIPO> ::= 'smallint'
#         |  'integer'
#         |  'bigint'
#         |  'decimal'
#         |  'numeric'
#         |  'real'
#         |  'double' 'precision'
#         |  'money'
#         |  'character' 'varying' ('numero')
#         |  'varchar' ('numero')
#         |  'character' ('numero')
#         |  'char' ('numero')
#         |  'text'
#         |  <TIMESTAMP>
#         |  'date'
#         |  <TIME>
#         |  <INTERVAL>
#         |  'boolean'

def p_tipo_1(p):
    'tipo : SMALLINT'


def p_tipo_2(p):
    'tipo : INTEGER'


def p_tipo_3(p):
    'tipo : BIGINT'


def p_tipo_4(p):
    'tipo : DECIMAL'


def p_tipo_5(p):
    'tipo : NUMERIC'


def p_tipo_6(p):
    'tipo : REAL'


def p_tipo_7(p):
    'tipo : DOUBLE PRECISION'


def p_tipo_8(p):
    'tipo : MONEY'


def p_tipo_9(p):
    'tipo : CHARACTER VARYING PABRE NUMERO PCIERRA'


def p_tipo_10(p):
    'tipo : VARCHAR PABRE NUMERO PCIERRA'


def p_tipo_11(p):
    'tipo : CHARACTER PABRE NUMERO PCIERRA'


def p_tipo_12(p):
    'tipo : CHAR PABRE NUMERO PCIERRA'


def p_tipo_13(p):
    'tipo : TEXT '


def p_tipo_14(p):
    'tipo : timestamp'


def p_tipo_15(p):
    'tipo : DATE'


def p_tipo_16(p):
    'tipo : time'


def p_tipo_17(p):
    'tipo : interval'


def p_tipo_18(p):
    'tipo : BOOLEAN'
# __________________________________________ <INTERVAL>
# <INTERVAL> ::= 'interval' <FIELDS> ('numero')
#             |  'interval' <FIELDS>
#             |  'interval' ('numero')
#             |  'interval'


def p_interval_1(p):
    'interval : INTERVAL fields PABRE NUMERO PCIERRA'


def p_interval_2(p):
    'interval : INTERVAL fields'


def p_interval_3(p):
    'interval : INTERVAL PABRE NUMERO PCIERRA'


def p_interval_4(p):
    'interval : INTERVAL '

# _________________________________________ <fields>
# <FIELDS> ::= 'year'
#           |  'month'
#           |  'day'
#           |  'hour'
#           |  'minute'
#           |  'second'


def p_fields(p):
    '''fields : YEAR 
              | MONTH
              | DAY
              | HOUR
              | MINUTE
              | SECOND '''
    p[0] = p[1]  # fijo es un sintetizado

# __________________________________________ <time>
# <TIME> ::= 'time' ('numero') 'tmstamp'
#         |  'time' 'tmstamp'
#         |  'time' ('numero')
#         |  'time'


def p_time_1(p):
    'time : TIME PABRE NUMERO PCIERRA CADENA'


def p_time_2(p):
    'time : TIME CADENA'


def p_time_3(p):
    'time : TIME PABRE NUMERO PCIERRA'


def p_time_4(p):
    'time : TIME'

# __________________________________________ <timestamp>
# <TIMESTAMP> ::= 'timestamp' ('numero') 'tmstamp'
#             |   'timestamp' 'tmstamp'
#             |   'timestamp' ('numero')
#             |   'timestamp'
#             |    'now' '(' ')'


def p_timestamp_1(p):
    'timestamp : TIMESTAMP PABRE NUMERO PCIERRA CADENA '


def p_timestamp_2(p):
    'timestamp : TIMESTAMP  CADENA '


def p_timestamp_3(p):
    'timestamp : TIMESTAMP PABRE NUMERO PCIERRA '


def p_timestamp_4(p):
    'timestamp : TIMESTAMP'


def p_timestamp_5(p):
    'timestamp : NOW PABRE PCIERRA'

# __________________________________________ <DEFAULT>
# <DEFAULT> ::= 'default' <VALOR>


def p_default(p):
    'default : DEFAULT expresion'

# _________________________________________ <VALOR>
# falta la produccion valor , le deje expresion :v

# __________________________________________ <NULLABLE>
# <NULLABLE> ::= 'not' 'null'
#             | 'null'


def p_nullable_1(p):
    'nullable : NOT NULL'


def p_nullable_2(p):
    'nullable : NULL'
# __________________________________________ <CONSTRAINTS>
# <CONSTRAINTS> ::= 'constraint' id 'unique'
#                 | 'unique'


def p_constraints_1(p):
    'constraints : CONSTRAINT ID UNIQUE'


def p_constraints_2(p):
    'constraints : UNIQUE'


# _________________________________________ <CHECKS>
# <CHECKS> ::= 'constraint' id 'check' (<CONDICION>)
#             |'check' (<CONDICION>)

def p_checks_1(p):
    'checks : CONSTRAINT ID CHECK PABRE condicion PCIERRA '


def p_checks_2(p):
    'checks : CHECK PABRE condicion PCIERRA '

# _________________________________________ condicion
# <CONDICION> ::= <PREDICADO>
#              |  <CONDICION> ',' <PREDICADO>


def p_condicion_1(p):
    'condicion : predicado'


def p_condicion_2(p):
    'condicion : condicion COMA predicado'


# _________________________________________ <LISTA_CONDICIONES>
# <LISTA_CONDICIONES> ::= <CONDICION>
#                     |   <LISTA_CONDICIONES>, <CONDICION>

def p_lista_condiciones_1(p):
    'lista_condiciones : condicion'


def p_lista_condiciones_2(p):
    'lista_condiciones : lista_condiciones condicion'


# __________________________________________update
def p_update(p):
    '''sentenciaUpdate : UPDATE ID SET lista_asignaciones WHERE expresion 
                       | UPDATE ID SET lista_asignaciones '''
    if (len(p) == 6):
        print('update LARGO')
        p[0] = p[1]
    else:
        print('update CORTO')
        p[0] = p[1]
 # __________________________________________INSERT


def p_sentenciaInsert(p):
    ''' insert : INSERT INTO ID parametros VALUES parametros'''
    p[0] = p[1]
# ___________________________________________PARAMETROS


def p_parametros(p):
    ''' parametros : PABRE lista_ids  PCIERRA'''
    p[0] = p[1]
# __________________________________________lista ids
# <LISTA_IDS> ::= <LISTA_IDS> ',' 'ID'
#          | 'ID'


def p_lista_ids(p):
    ''' lista_ids : lista_ids COMA  ID
                  | ID '''

    if (len(p) == 3):
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


# __________________________________________DELETE
def p_sentenciaDelete(p):
    ''' sentenciaDelete : DELETE FROM ID WHERE expresion
                        | DELETE FROM ID '''
    p[0] = p[1]


# ___________________________________________ASIGNACION____________________________________

def p_lista_asignaciones(p):
    '''lista_asignaciones : lista_asignaciones COMA asignacion
                          | asignacion'''
    if (len(p) == 3):
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_asignacion(p):
    ''' asignacion : ID IGUAL expresion'''
    print('asignacion de campo')
    p[0] = p[1]


# ______________________________________________EXPRESION_______________________________
# <EXPRESION> ::= 'not' <EXPRESION>
#             | '-'   <EXPRESION>
#             | <EXPRESION> 'and'  <EXPRESION>
#             | <EXPRESION> 'or'   <EXPRESION>
#             | <EXPRESION> '='  <EXPRESION>
#             | <EXPRESION> '<>'  <EXPRESION>
#             | <EXPRESION> '>='  <EXPRESION>
#             | <EXPRESION> '<='  <EXPRESION>
#             | <EXPRESION>  '>'  <EXPRESION>
#             | <EXPRESION>  '<'  <EXPRESION>
#             | <EXPRESION>  '+'  <EXPRESION>
#             | <EXPRESION>  '-'  <EXPRESION>
#             | <EXPRESION>  '*'  <EXPRESION>
#             | <EXPRESION>  '/'  <EXPRESION>
#             | 'cadena'
#             | 'numero'
#             | 'decimal'
#             | 'id' '.' 'id'
#             | 'id'
#             | '(' <EXPRESION> ')'
# ------------------- falta esta parte -------------------------
#             | 'sum' '(' 'id' ')'
#             | <TIMESTAMP>
#             | 'substring' '(' 'id' ',' 'entero' ',' 'entero' ')'

def p_expresiones_unarias(p):
    ''' expresion : MENOS expresion %prec UMENOS 
                  | MAS expresion %prec UMAS
                  | NOT expresion 
                  | expresion IS NULL
                  | expresion IS NOT NULL
                  | expresion ISNULL
                  | expresion NOTNULL
                  | expresion IS TRUE
                  | expresion IS NOT TRUE
                  | expresion IS FALSE
                  | expresion IS NOT FALSE
                  | expresion IS UNKNOWN
                  | expresion IS NOT UNKNOWN
                  '''
    print('expresion: '+str(p[1]) + '.'+str(p[3]))  # solo para ver que viene
    p[0] = p[2]

def p_expreion_funciones(p):
    'expresion : funciones'
    
def p_expreion_entre_parentesis(p):
    'expresion : PABRE expresion  PCIERRA'
    p[0] = p[2]


def p_expresion_cadena(p):
    'expresion : CADENA '
    p[0] = p[1]


def p_expresion_id(p):
    'expresion : ID'
    p[0] = p[1]


def p_expresion_numero(p):
    'expresion : NUMERO'
    p[0] = p[1]


def p_expresion_decimal(p):
    'expresion : DECIMAL_LITERAL'
    p[0] = p[1]


def p_expresion_tabla_campo(p):
    'expresion : ID PUNTO ID'
    print('expresion: '+str(p[1]) + '.'+str(p[3]))  # solo para ver que viene
    p[0] = p[1]


def p_expresion_sum(p):
    'expresion: SUM PABRE ID PCIERRA'


def p_expresion_timestamp(p):
    'expresion: timestamp'


def p_expresion_substring(p):
    'expresion: SUBSTRING PABRE ID COMA NUMERO COMA NUMERO PCIERRA'


def p_expresion_con_dos_nodos(p):
    '''expresion : expresion MAS expresion 
                 | expresion MENOS expresion
                 | expresion ASTERISCO expresion
                 | expresion DIVISION expresion 
                 | expresion MAYOR expresion 
                 | expresion MENOR expresion
                 | expresion MAYORIGUAL expresion
                 | expresion MENORIGUAL expresion
                 | expresion DIFERENTE expresion
                 | expresion DIFERENTE2 expresion
                 | expresion IGUAL expresion
                 | expresion XOR expresion
                 | expresion MODULO expresion
                 | expresion OR expresion
                 | expresion AND expresion
                 | expresion IS DISTINCT FROM expresion
                 | expresion IS NOT DISTINCT FROM expresion
    '''
   # print('expresion:'+str(p[1])+str(p[2])+str(p[3])) # solo para ver que viene
   # if p[2] == '+':  p[0] = p[1]+p[2]
   # elif p[2] == '-': p[0] = p[1]-p[2]
   # elif p[2] == '*': p[0] = p[1]*p[2]
   # elif p[2] == '/': p[0] = p[1]/p[2]
   # elif p[2] == '>': print('mayor')
   # elif p[2] == '<': print('menor')
   # elif p[2] == '>=': print('MAYOR_igual')
   # elif p[2] == '<=': print('menor_igual')
   # elif p[2] == '^': print('POTENCIA o CIRCUNFLEJO')
   # elif p[2] == '%': print('modulo')
   # elif p[2] == '=': print('igual')
   # elif p[2] == '<>': print('distino')
   # elif p[2] == '!=': print('distino2')


def p_expresion_ternaria(p):
    '''expresion : expresion BETWEEN expresion AND expresion 
                 | expresion NOT BETWEEN expresion AND expresion
                 | expresion BETWEEN SYMMETRIC expresion AND expresion
                 | expresion NOT BETWEEN SYMMETRIC expresion AND expresion
    '''
def p_error(p):
    print(p)
    print("Error sintáctico en '%s'" % p.value)


parser = yacc.yacc()


def analizarEntrada(entrada):
    return parser.parse(entrada)


print(analizarEntrada('''
                      
CREATE TABLE employees (
   id varchar(10) PRIMARY KEY NOT NULL,
   first_name VARCHAR (50),
   last_name VARCHAR (50)
);

                      '''))
