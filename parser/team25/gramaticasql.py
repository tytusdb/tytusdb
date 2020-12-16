import ply.yacc as yacc
from lexicosql import tokens
from astExpresion import ExpresionNegativa, ExpresionNumero, ExpresionPositiva, TIPO_DE_DATO, ExpresionAritmetica, OPERACION_ARITMETICA

#_______________________________________________________________________________________________________________________________
#                                                          PARSER
#_______________________________________________________________________________________________________________________________

#---------------- MANEJO DE LA PRECEDENCIA
precedence = (
    ('left','IGUAL','DIFERENTE','DIFERENTE2'),
    ('left','MENOR','MAYOR','MENORIGUAL','MAYORIGUAL'),
    ('left','MAS','MENOS'),
    ('left','EXPONENT'),
    ('left','ASTERISCO','DIVISION','MODULO'),
    ('left','AND'),
    ('left','OR'),
    ('nonassoc','BETWEEN','IN','LIKE','ILIKE','SIMILAR'),
    ('nonassoc','IS','ISNULL','NOTNULL','FROM' , 'SYMMETRIC','NOTBETWEEN'),
    ('right','UMENOS','UMAS','NOT'),  
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
    '''instruccion :  sentenciaUpdate   PTCOMA 
                    | sentenciaDelete   PTCOMA
                    | insert            PTCOMA
                    | definicion        PTCOMA
                    | alter_table       PTCOMA
                    | combine_querys    PTCOMA
                    | USE ID            PTCOMA
                    '''     
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

def p_alter_table(p):
    '''alter_table : ALTER TABLE ID alter_options
                   | ALTER TABLE ID alter_varchar_lista'''

def p_alter_options(p):
    '''alter_options : ADD COLUMN ID tipo
                    | DROP COLUMN ID
                    | ADD CHECK PABRE ID DIFERENTE CADENA PCIERRA
                    | ADD CONSTRAINT ID UNIQUE PABRE ID PCIERRA
                    | ADD FOREIGN KEY PABRE lista_ids PCIERRA REFERENCES lista_ids
                    | ALTER COLUMN ID SET NOT NULL
                    | DROP CONSTRAINT ID'''

def p_alter_varchar_lista(p):
    '''alter_varchar_lista :  alter_varchar
                           |  alter_varchar_lista COMA alter_varchar'''

def p_alter_varchar(p):
    '''alter_varchar : ALTER COLUMN ID TYPE VARCHAR PABRE NUMERO PCIERRA '''

# <TABLA> ::=  'id' 
#          |   'id' 'as' 'id'
#          |   <SUBQUERY>
#          |   <SUBQUERY> 'as' 'id'
def p_tablas(p):
    '''tabla : ID
            |  ID AS ID
            |  subquery
            |  subquery AS ID '''

def p_filtro(p):
    '''filtro : where group_by having
              | where group_by
              | where '''

def p_join(p):
    '''join :  join_type JOIN ID ON expresion
            |  join_type JOIN ID USING PABRE JOIN lista_ids PCIERRA
            |  NATURAL join_type JOIN ID'''

def p_join_type(p):
    '''join_type : INNER
                |  outer'''

def p_outer(p):
    '''outer : LEFT OUTER
            |  RIGHT OUTER
            |  FULL OUTER
            |  LEFT
            |  RIGHT
            |  FULL'''

def p_combine_querys1(p):
    'combine_querys : combine_querys UNION ALL select'

def p_combine_querys2(p):
    'combine_querys : combine_querys UNION select'

def p_combine_querys3(p):
    'combine_querys : combine_querys INTERSECT ALL select'

def p_combine_querys4(p):
    'combine_querys : combine_querys INTERSECT select'

def p_combine_querys5(p):
    'combine_querys : combine_querys EXCEPT ALL select'

def p_combine_querys6(p):
    'combine_querys : combine_querys EXCEPT select'

def p_combine_querys7(p):
    'combine_querys : select'
#_____________________________________________________________ SELECT
def p_select0(p):
    'select : SELECT expresion'
    p[0] = p[2].ejecutar(0)
    print(p[0].val)

def p_select1(p):
    'select : SELECT select_list FROM lista_tablas filtro join'

def p_select2(p):
    'select : SELECT select_list FROM lista_tablas filtro'

def p_select3(p):
    'select : SELECT select_list FROM lista_tablas orders limits offset join'

def p_select4(p):
    'select : SELECT select_list FROM lista_tablas orders limits offset'

def p_select5(p):
    'select : SELECT select_list FROM lista_tablas orders limits join'

def p_select6(p):
    'select : SELECT select_list FROM lista_tablas orders limits'

def p_select7(p):
    'select : SELECT select_list FROM lista_tablas orders offset join'

def p_select8(p):
    'select : SELECT select_list FROM lista_tablas orders offset'

def p_select9(p):
    'select : SELECT select_list FROM lista_tablas orders join'

def p_select10(p):
    'select : SELECT select_list FROM lista_tablas orders'

def p_select11(p):
    'select : SELECT select_list FROM lista_tablas limits offset join'

def p_select12(p):
    'select : SELECT select_list FROM lista_tablas limits offset'

def p_select13(p):
    'select : SELECT select_list FROM lista_tablas limits join'

def p_select14(p):
    'select : SELECT select_list FROM lista_tablas limits'

def p_select15(p):
    'select : SELECT select_list FROM lista_tablas offset join'

def p_select16(p):
    'select : SELECT select_list FROM lista_tablas offset'

def p_select17(p):
    'select : SELECT ASTERISCO FROM lista_tablas filtro join'

def p_select18(p):
    'select : SELECT ASTERISCO FROM lista_tablas filtro'

def p_select19(p):
    'select : SELECT DISTINCT opcionDistinct FROM lista_tablas filtro join'

def p_select20(p):
    'select : SELECT DISTINCT opcionDistinct FROM lista_tablas filtro'

def p_select21(p):
    'select : SELECT SUBSTRING PABRE ID COMA NUMERO COMA NUMERO PCIERRA FROM  lista_tablas filtro join'

def p_select22(p):
    'select : SELECT SUBSTRING PABRE ID COMA NUMERO COMA NUMERO PCIERRA FROM  lista_tablas filtro'

def p_select23(p):
    'select : SELECT select_list FROM lista_tablas join'

def p_select24(p):
    'select : SELECT select_list FROM lista_tablas'

def p_select25(p):
    'select : SELECT ASTERISCO FROM lista_tablas join'

def p_select26(p):
    'select : SELECT ASTERISCO FROM lista_tablas'
    print('select ok')

def p_select27(p):
    'select : SELECT DISTINCT opcionDistinct FROM lista_tablas join'

def p_select28(p):
    'select : SELECT DISTINCT opcionDistinct FROM lista_tablas'
    print('select con un DISTINC ok')

def p_select29(p):
    'select : SELECT SUBSTRING PABRE ID COMA NUMERO COMA NUMERO PCIERRA FROM lista_tablas join'

def p_select30(p):
    'select : SELECT SUBSTRING PABRE ID COMA NUMERO COMA NUMERO PCIERRA FROM  lista_tablas'

def p_select31(p):
    'select : SELECT funciones AS ID join'
    print('ok')

def p_select32(p):
    'select : SELECT funciones AS ID'
    print('ok')

def p_select33(p):
    'select : SELECT funciones join'
    print('ok')

def p_select34(p):
    'select : SELECT funciones'
    print('ok')

#________________________________________ opcionDistinct
def p_opcionDistinct(p):
    ''' opcionDistinct : ID
                       | ASTERISCO '''

#________________________________________ LIMIT 

def p_limits(p):
    'limits : LIMIT limitc'

def p_limitc1(p):
    'limitc : NUMERO'

def p_limitc2(p):
    'limitc : ALL'

def p_offset(p):
    'offset : OFFSET NUMERO'

def p_funciones1(p):
    'funciones : LENGTH PABRE ID PCIERRA'

def p_funciones2(p):
    'funciones : SUBSTRING PABRE ID COMA NUMERO COMA NUMERO PCIERRA'

def p_funciones3(p):
    'funciones : TRIM PABRE ID PCIERRA'

def p_funciones4(p):
    'funciones : MD5 PABRE CADENA PCIERRA'

def p_funciones5(p):
    'funciones : SHA256 PABRE CADENA PCIERRA'

def p_funciones6(p):
    'funciones : SUBSTR PABRE ID COMA NUMERO COMA NUMERO PCIERRA'

def p_funciones7(p):
    'funciones : GET_BYTE PABRE CADENA TYPECAST BYTEA COMA NUMERO PCIERRA'

def p_funciones8(p):
    'funciones : SET_BYTE PABRE CADENA TYPECAST BYTEA COMA NUMERO COMA NUMERO PCIERRA'

def p_funciones9(p):
    'funciones : CONVERT PABRE CADENA AS DATE PCIERRA'

def p_funciones10(p):
    'funciones : CONVERT PABRE CADENA AS INTEGER PCIERRA'

def p_funciones11(p):
    'funciones : ENCODE PABRE CADENA BYTEA COMA CADENA PCIERRA'

def p_funciones12(p):
    'funciones : DECODE PABRE CADENA COMA CADENA PCIERRA'

def p_funciones13(p):
    'funciones : AS PABRE expresion PCIERRA'
 
def p_funciones14(p):
    'funciones : ACOS PABRE expresion PCIERRA'

def p_funciones15(p):
    'funciones : ACOSD PABRE expresion PCIERRA'

def p_funciones16(p):
    'funciones : ASIN PABRE expresion PCIERRA'
 
def p_funciones17(p):
    'funciones : ASIND PABRE expresion PCIERRA'

def p_funciones18(p):
    'funciones : ATAN PABRE expresion PCIERRA'

def p_funciones19(p):
    'funciones : ATAND PABRE expresion PCIERRA'

def p_funciones20(p):
    'funciones : ATAN2 PABRE expresion COMA expresion PCIERRA'

def p_funciones21(p):
    'funciones : ATAN2D PABRE expresion COMA expresion PCIERRA'

def p_funciones22(p):
    'funciones : COS PABRE expresion PCIERRA'
 
def p_funciones23(p):
    'funciones : COSD PABRE expresion PCIERRA'

def p_funciones24(p):
    'funciones : COT PABRE expresion PCIERRA'

def p_funciones25(p):
    'funciones : COTD PABRE expresion PCIERRA'
 
def p_funciones26(p):
    'funciones : SIN PABRE expresion PCIERRA'

def p_funciones27(p):
    'funciones : SIND PABRE expresion PCIERRA'

def p_funciones28(p):
    'funciones : TAN PABRE expresion PCIERRA'

def p_funciones29(p):
    'funciones : TAND PABRE expresion PCIERRA'
 
def p_funciones30(p):
    'funciones : COSH PABRE expresion PCIERRA'

def p_funciones31(p):
    'funciones : SINH PABRE expresion PCIERRA'

def p_funciones32(p):
    'funciones : TANH PABRE expresion PCIERRA'
 
def p_funciones33(p):
    'funciones : ACOSH PABRE expresion PCIERRA'

def p_funciones34(p):
    'funciones : ASINH PABRE expresion PCIERRA'

def p_funciones35(p):
    'funciones : ATANH PABRE expresion PCIERRA'

def p_funciones36(p):
    'funciones : ABS PABRE expresion PCIERRA'
 
def p_funciones37(p):
    'funciones : CBRT PABRE expresion PCIERRA'

def p_funciones38(p):
    'funciones : CEIL PABRE expresion PCIERRA'

def p_funciones39(p):
    'funciones : CEILING PABRE expresion PCIERRA'
 
def p_funciones40(p):
    'funciones : DEGREES PABRE expresion PCIERRA'

def p_funciones41(p):
    'funciones : DIV PABRE expresion COMA expresion PCIERRA'

def p_funciones42(p):
    'funciones : FACTORIAL PABRE expresion PCIERRA'
 
def p_funciones43(p):
    'funciones : FLOOR PABRE expresion PCIERRA'

def p_funciones44(p):
    'funciones : GCD PABRE expresion PCIERRA'

def p_funciones45(p):
    'funciones : LN PABRE expresion PCIERRA'

def p_funciones46(p):
    'funciones : LOG PABRE expresion PCIERRA'
 
def p_funciones47(p):
    'funciones : EXP PABRE expresion PCIERRA'

def p_funciones48(p):
    'funciones : MOD PABRE expresion COMA expresion PCIERRA'

def p_funciones49(p):
    'funciones : PI PABRE PCIERRA'

def p_funciones50(p):
    'funciones : POWER PABRE expresion COMA expresion PCIERRA'

def p_funciones51(p):
    'funciones : RADIANS PABRE expresion PCIERRA'

def p_funciones52(p):
    'funciones : ROUND PABRE expresion PCIERRA'

def p_funciones53(p):
    'funciones : SIGN PABRE tipo_numero PCIERRA'

def p_funciones54(p):
    'funciones : SQRT PABRE tipo_numero PCIERRA'
 
def p_funciones55(p):
    'funciones : WIDTH_BUCKET PABRE lista_numeros PCIERRA'

def p_funciones56(p):
    'funciones : TRUNC PABRE tipo_numero COMA NUMERO PCIERRA'

def p_funciones57(p):
    'funciones : TRUNC PABRE tipo_numero PCIERRA'

def p_funciones58(p):
    'funciones : RANDOM PABRE PCIERRA'

def p_funciones59(p):
    'funciones : SUM PABRE ID PCIERRA'

def p_funciones60(p):
    'funciones : PIPE tipo_numero'

def p_funciones61(p):
    'funciones : DOBLE_PIPE tipo_numero'

def p_funciones62(p):
    'funciones : tipo_numero AMPERSAND tipo_numero'

def p_funciones63(p):
    'funciones : tipo_numero PIPE tipo_numero'

def p_funciones64(p):
    'funciones : tipo_numero NUMERAL tipo_numero'

def p_funciones65(p):
    'funciones : BITWISE_NOT tipo_numero'

def p_funciones66(p):
    'funciones : tipo_numero CORRIMIENTO_IZQ tipo_numero'

def p_funciones67(p):
    'funciones : tipo_numero CORRIMIENTO_DER tipo_numero'

def p_lista_numeros(p):
    '''lista_numeros : tipo_numero
                     | lista_numeros COMA tipo_numero'''
#___________________________________ <TIPO_NUMERO>                    
#    <TIPO_NUMERO> ::= 'numero'
#                  |   'decimal'
def p_tipo_numero1(p):
    'tipo_numero : NUMERO'

def p_tipo_numero2(p):
    'tipo_numero : DECIMAL_LITERAL'
    

def p_lista_tablas(p):
    '''
    lista_tablas : lista_tablas COMA tabla
                 | tabla
    '''


    

def p_select_list(p):
    '''select_list : select_item
                   | select_list COMA select_item'''

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
def p_combinaciones1_0(p):
    'combinaciones1 : IF NOT EXISTS ID'

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
#             | 'constraint' 'id' 'check' (<lista_exp>)
#             | 'id' 'check' (<lista_exp>)
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
    'columna : CONSTRAINT  ID CHECK PABRE lista_exp PCIERRA '


def p_columna_4(p):
    'columna : UNIQUE PABRE lista_ids PCIERRA'


def p_columna_5(p):
    'columna :  PRIMARY KEY PABRE lista_ids PCIERRA'


def p_columna_6(p):
    'columna : FOREIGN KEY PABRE lista_ids PCIERRA REFERENCES ID PABRE lista_ids PCIERRA'


def p_columna_7(p):
    'columna : CHECK PABRE lista_exp PCIERRA'


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


#_________________________________________ <CHECKS>
# <CHECKS> ::= 'constraint' 'id' 'check' '('<EXPRESION>')'
#             |'check' '('<EXPRESION>')' 

def p_checks_1(p):
    'checks : CONSTRAINT ID CHECK PABRE expresion PCIERRA '

def p_checks_2(p):
    'checks : CHECK PABRE expresion PCIERRA'  







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
    ''' insert : INSERT INTO ID VALUES PABRE lista_exp PCIERRA'''
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

def p_expresiones_unarias(p):
    ''' expresion : MENOS expresion %prec UMENOS 
                  | MAS expresion %prec UMAS'''
    if p[1] == '+':
        p[0] = ExpresionPositiva(p[2], 0)
    elif p[1] == '-':
        p[0] = ExpresionNegativa(p[2], 0)
    
def p_expresiones_is_complemento(p):
    '''
    expresion    : expresion IS NULL    
                 | expresion IS NOT NULL
                 | expresion ISNULL 
                 | expresion NOTNULL
                 | expresion IS TRUE
                 | expresion IS NOT TRUE
                 | expresion IS FALSE 
                 | expresion IS NOT FALSE
                 | expresion IS UNKNOWN
                 | expresion IS NOT UNKNOWN 
                 | expresion IS DISTINCT FROM expresion 
                 | expresion IS NOT DISTINCT FROM expresion '''
  

def p_expresion_ternaria(p): 
    '''expresion : expresion BETWEEN  exp_aux AND exp_aux
                 | expresion BETWEEN SYMMETRIC exp_aux AND exp_aux
                 | expresion NOTBETWEEN exp_aux AND exp_aux
                 | expresion NOTBETWEEN SYMMETRIC exp_aux AND exp_aux''' 
                 
def p_expreion_funciones(p):
    'expresion : funciones'
    
def p_expreion_entre_parentesis(p):
    'expresion : PABRE expresion  PCIERRA'
    p[0] = p[2]

def p_expresion_primitivo(p):
    'expresion : CADENA'

def p_expresion_primitivo1(p):
    'expresion : NUMERO'
    p[0] = ExpresionNumero(p[1], TIPO_DE_DATO.ENTERO, 0)

def p_expresion_primitivo2(p):
    'expresion : DECIMAL_LITERAL'
    p[0] = ExpresionNumero(p[1], TIPO_DE_DATO.DECIMAL, 0)

def p_expresion_id(p):
    'expresion : ID'
    p[0] = p[1]
    
def p_expresion_tabla_campo(p):
    'expresion : ID PUNTO ID'
    
def p_expresion_timestamp(p):
    'expresion : timestamp'

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
                 | expresion EXPONENT expresion
                 | expresion MODULO expresion
                 | expresion OR expresion
                 | expresion AND expresion
    '''
    if p[2] == '+':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.MAS)
    elif p[2] == '-':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.MENOS)
    elif p[2] == '*':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.POR)
    elif p[2] == '/':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.DIVIDO)
    elif p[2] == '%':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.MODULO)
    elif p[2] == '^':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.EXPONENTE)




#----------------------------------------------------------------------------------------------------- FIN EXPRESION
#<EXP_AUX>::= '-'  <EXP_AUX>
#          |    '+'  <EXP_AUX>
#          | <EXP_AUX>  '+'  <EXP_AUX>
#          | <EXP_AUX>  '-'  <EXP_AUX>
#          | <EXP_AUX>  '*'  <EXP_AUX>
#          | <EXP_AUX>  '/'  <EXP_AUX>
#          | <EXP_AUX>  '%'  <EXP_AUX>
#          | <EXP_AUX>  '^'  <EXP_AUX>
def p_exp_aux(p):
        '''exp_aux : exp_aux MAS exp_aux 
                 | exp_aux MENOS exp_aux
                 | exp_aux ASTERISCO exp_aux
                 | exp_aux DIVISION exp_aux 
                 | exp_aux EXPONENT exp_aux
                 | exp_aux MODULO exp_aux
    '''
#          | '(' <EXP_AUX> ')'
def p_exp_aux_entre_parentesis(p):
    'exp_aux : PABRE exp_aux  PCIERRA'
#          | 'cadena'
def p_exp_aux_cadena(p):
    'exp_aux :  CADENA'
#          | 'numero'          
def p_exp_aux_numero(p):
    'exp_aux :  NUMERO'
#          | 'decimal'
def p_exp_aux_decimal(p):
    'exp_aux :  DECIMAL_LITERAL'
#          | 'id' '.' 'id'
def p_exp_aux_tabla(p):
    'exp_aux :  ID PUNTO ID'
#          | 'id'
def p_exp_aux_id(p):
    'exp_aux :  ID'
#          | <FUNCIONES>
def p_exp_aux_funciones(p):
    'exp_aux :  funciones'
#          | <TIMESTAMP>
def p_exp_aux_timestamp(p):
    'exp_aux :  timestamp'

#<SUBQUERY> ::= '('<SELECT>')'
def p_subquery(p):
        'subquery :  PABRE select PCIERRA'

#<WHERE> ::= 'where' <EXPRESION>
def p_where(p):
        'where : WHERE expresion'
        print('realizando un sentencia con un WHERE')

#<GROUP_BY> ::= <LISTA_IDS>
def p_groupby(p):
        'group_by : lista_ids'

#<HAVING> ::= 'having' <EXPRESION>
def p_having(p):
        'having : HAVING expresion'

#    <ORDERS> ::= <ORDERBY>
def p_orders(p):
        'orders : orderby'
#                |<ORDERS> ',' <ORDERBY>
def p_orders1(p):
        'orders : orders COMA orderby'

#    <ORDERBY> ::= 'order' 'by' <EXPRESION> <ASC_DEC> <NULLS>
def p_orderby(p):
        'orderby : ORDER BY expresion asc_dec nulls'
#               | 'order' 'by' <EXPRESION> <ASC_DEC>
def p_orderby1(p):
        'orderby : ORDER BY expresion asc_dec'
#                | 'order' 'by' <EXPRESION> <NULLS>
def p_orderby2(p):
        'orderby : ORDER BY expresion nulls'
#                | 'order' 'by' <EXPRESION>        
def p_orderby3(p):
        'orderby : ORDER BY expresion'

#    <ASC_DEC> ::= 'asc'
def p_asc_dec(p):
        'asc_dec : ASC'
#               | 'desc'
def p_asc_dec1(p):
        'asc_dec : DESC'

#<NULLS> ::= 'nulls' <FIRST_LAST>
def p_nulls(p):
        'nulls : NULLS first_last'

#   <FIRST_LAST> ::= 'first'
def p_first_last(p):
        'first_last : FIRST'
#                |    'last'
def p_first_last1(p):
        'first_last : LAST'

#    <SELECT_ITEM>::=  'id'
def p_select_item(p):
        'select_item : ID'
#                  | 'id' '.' 'id'
def p_select_item1(p):
        'select_item : ID PUNTO ID'
#                  | <COUNT>
def p_select_item2(p):
        'select_item : count'
#                  | <AGGREGATE_F>
def p_select_item3(p):
        'select_item : aggregate_f'
#                  | <SUBQUERY>
def p_select_item4(p):
        'select_item : subquery'
#                  | <CASE>
def p_select_item5(p):
        'select_item : case'
#                  | <GREATEST>
def p_select_item6(p):
        'select_item : greatest'
#                  | <LEAST>
def p_select_item7(p):
        'select_item : least'

#    <COUNT> ::= 'count' '(' '*' ')'  
def p_count(p):
        'count : COUNT PABRE ASTERISCO PCIERRA'
#             |  'count' '(' 'id' ')'
def p_count1(p):
        'count : COUNT PABRE ID PCIERRA'
#             |  'count' '(' 'distinct' 'id' ')' 
def p_count2(p):
        'count : COUNT PABRE DISTINCT ID PCIERRA'

#    <AGGREGATE_F> ::= 'sum' '(' 'id' ')'
def p_aggregate_f(p):
        'aggregate_f : SUM PABRE ID PCIERRA'
#                |     'avg' '(' 'id' ')'
def p_aggregate_f1(p):
        'aggregate_f : AVG PABRE ID PCIERRA'
#                |     'max' '(' 'id' ')'
def p_aggregate_f2(p):
        'aggregate_f : MAX PABRE ID PCIERRA'
#                |     'min' '(' 'id' ')'
def p_aggregate_f3(p):
        'aggregate_f : MIN PABRE ID PCIERRA'

#    <CASE> ::= 'case' <SUBCASE> <ELSE_CASE> 'end'
def p_case(p):
        'case : CASE subcase else_case END'
#             | 'case' <SUBCASE> 'end'   
def p_case1(p):
        'case : CASE subcase END'    
#    <SUBCASE> ::= <WHEN_CASE>
def p_subcase(p):
        'subcase : when_case'
#                | <SUBCASE> <WHEN_CASE>
def p_subcase1(p):
        'subcase : subcase when_case'

#<ELSE_CASE> ::= 'else' <EXPRESION>
def p_else_case(p):
        'else_case : ELSE expresion'

#<GREATEST> ::= 'greatest' '(' <LISTA_EXP>')'
def p_greatiest(p):
        'greatest : GREATEST PABRE lista_exp PCIERRA'

#<LEAST> ::= 'least' '(' <LISTA_EXP> ')'
def p_least(p):
        'least : LEAST PABRE lista_exp PCIERRA'

# <LISTA_EXP> ::= <EXPRESION>
#            | <LISTA_EXP> ',' <EXPRESION>

def p_lista_exp_1(p):
    'lista_exp : expresion'

def p_lista_exp_2(p):
    'lista_exp : lista_exp COMA expresion'    

#<WHEN_CASE> ::= 'when' <EXPRESION> 'then' <EXPRESION>
def p_when_case(p):
    'when_case : WHEN expresion THEN expresion'
        




def p_error(p):
    print(p)
    print("Error sintáctico en '%s'" % p.value)


parser = yacc.yacc()


def analizarEntrada(entrada):
    return parser.parse(entrada)


print(analizarEntrada('''
select -(((5+5-(8*8)+90)/2)%5)^2;
                      '''))
