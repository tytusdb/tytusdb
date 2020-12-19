# Construyendo el analizador léxico
import ply.lex as lex
from lex import *
from columna import *

lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left','CONCAT'),
    ('left','MENOR','MAYOR','IGUAL','MENORIGUAL','MAYORIGUAL','DIFERENTE'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVISION','MODULO'),
    ('left','EXP'),
    #('right','UMENOS'),
    )

# Definición de la gramática

from expresiones import *
from instrucciones import *

def p_init(t) :
    'init            : instrucciones'
    print('init')

#====================================================
#INSTRUCCIONES INICIALES
def p_instrucciones_lista(t) :
    'instrucciones  : instruccion instrucciones2'
    print('instrucciones')

def p_instrucciones_lista2(t) :
    '''instrucciones2    : instruccion instrucciones2
                        |'''
    print('instrucciones2')

def p_instrucciones_instruccion(t) :
    '''instruccion  : CREATE creacion PTCOMA
                    | SHOW show_db PTCOMA
                    | ALTER DATABASE alter_database PTCOMA
                    | USE cambio_db PTCOMA
                    | SELECT selects PTCOMA
                    | DELETE deletes PTCOMA
                    | ALTER TABLE alter_table PTCOMA
                    | UPDATE update_table PTCOMA
                    | INSERT insercion PTCOMA
                    | DROP dropear PTCOMA'''
    print('instruccion')

#====================================================
#====================================================
#INSTRUCCIONES DE CREACION
def p_instrucciones_create(t) :
    '''creacion : DATABASE crear_db
                | OR REPLACE DATABASE crear_db
                | TABLE crear_tb
                | TYPE crear_type'''

#====================================================

#====================================================
# CREACION DE BASE DE DATOS
def p_instrucciones_create_db(t) :
    '''crear_db : ID lista_parametros_bd2
                | IF NOT EXISTS ID lista_parametros_bd2'''

def p_instrucciones_lista_parametros_bd2(t) :
    '''lista_parametros_bd2 : parametros_bd lista_parametros_bd2
                            |'''

def p_instrucciones_parametros_bd(t) :
    '''parametros_bd    : OWNER igual ID
                        | MODE igual ENTERO'''

def p_instrucciones_igual(t) :
    '''igual    : IGUAL
                |'''

#====================================================

#====================================================
#INSTRUCCIONES DE CREACION DE TABLAS
def p_instrucciones_create_tb(t) :
    'crear_tb   : ID PARIZQ crear_tb_columnas PARDER tb_herencia'

def p_instrucciones_tb_herencia(t) :
    '''tb_herencia    : INHERITS PARIZQ ID PARDER
                    |'''

def p_instrucciones_crear_tb_columnas(t) :
    'crear_tb_columnas  : crear_tb_columna crear_tb_columnas2'

def p_instrucciones_crear_tb_columnas2(t) :
    '''crear_tb_columnas2   : COMA crear_tb_columna crear_tb_columnas2
                            |'''

def p_instrucciones_crear_tb_columna(t) :
    '''crear_tb_columna : ID tipos parametros_columna
                        | PRIMARY KEY PARIZQ lista_id PARDER
                        | FOREIGN KEY PARIZQ lista_id PARDER
                        | chequeo
                        | UNIQUE PARIZQ lista_id PARDER'''
    
def p_instrucciones_chequeo(t) :
    '''chequeo  : CONSTRAINT ID CHECK PARIZQ relacional PARDER
                | CHECK PARIZQ relacional PARDER'''

def p_instrucciones_parametros_columna(t) :
    '''parametros_columna   : parametro_columna parametros_columna
                            |'''

def p_instrucciones_parametro_columna(t) :
    '''parametro_columna    : unul
                            | unic
                            | chequeo
                            | PRIMARY KEY
                            | DEFAULT valor
                            | REFERENCES ID'''

def p_instrucciones_unul(t) :
    '''unul : NULL
            | NOT NULL'''

def p_instrucciones_unic(t) :
    '''unic : CONSTRAINT ID UNIQUE
            | UNIQUE'''

#====================================================

#====================================================
#INSTRUCCIONES CREACIÓN TYPE
def p_instrucciones_create_type(t) :
    'crear_type : ID AS ENUM PARIZQ lista_objetos PARDER'

def p_instrucciones_lista_objetos(t) :
    'lista_objetos  : valor lista_objetos2'

def p_instrucciones_lista_objetos2(t) :
    '''lista_objetos2   : COMA valor lista_objetos2
                        |'''

#====================================================
#====================================================
#INSTRUCCIONES SHOW DATABASE
def p_instrucciones_show_db(t) :
    'show_db    : DATABASES like_cadena'

def p_instrucciones_like_cadena(t) :
    '''like_cadena  : LIKE CADENA
                    |'''

#====================================================

#====================================================
# INSTRUCCIONES DE ALTER DATABASE
def p_instrucciones_alter_database(t) :
    'alter_database : ID rename_owner'

def p_instrucciones_rename_owenr(t) :
    '''rename_owner : RENAME ID
                    | OWNER TO def_alter_db'''

def p_instrucciones_def_alter_db(t) :
    '''def_alter_db : ID
                    | CURRENT_USER
                    | SESSION_USER'''
#====================================================
#====================================================
# INSTRUCCIONES DE USE DATABASE
def p_instrucciones_cambio_db(t) :
    'cambio_db  : ID'

#====================================================
#====================================================
#INSTRUCCIONES DE SELECT
def p_instrucciones_selects(t) :
    '''selects  : POR FROM select_o_state
                | lista_parametros from_o_coma
                | GREATEST PARIZQ lista_parametros PARDER
                | LEAST PARIZQ lista_parametros PARDER
                | fun_trigonometrica state_aliases_field from_ep
                | DISTINCT por_lista_parametros'''

def p_instrucciones_select_o_state(t) :
    '''select_o_state   : select_all
                        | state_subquery inicio_condicional'''

def p_instrucciones_from_o_coma(t) :
    '''from_o_coma  : FROM lista_parametros inicio_condicional
                    | COMA CASE case_state FROM lista_parametros inicio_condicional
                    |'''

def p_instrucciones_from_ep(t) :
    '''from_ep  : FROM ID state_aliases_table
                |'''

def p_instrucciones_por_lista_parametros(t) :
    '''por_lista_parametros : POR FROM select_all
                            | lista_parametros from_ep_distinct'''

def p_instrucciones_from_ep_distinct(t) :
    '''from_ep_distinct : FROM lista_parametros inicio_condicional
                        | COMA CASE case_state FROM lista_parametros inicio_condicional
                        |'''

def p_instrucciones_select_all(t) :
    'select_all : ID state_aliases_table inicio_condicional'

def p_instrucciones_inicio_condicional(t) :
    '''inicio_condicional   : WHERE relacional inicio_group_by
                            | inicio_group_by
                            |'''

def p_instrucciones_inicio_group_by(t) :
    '''inicio_group_by  : GROUP BY lista_parametros inicio_having
                        | inicio_order_by'''

def p_instrucciones_inicio_having(t) :
    '''inicio_having    : HAVING relacional inicio_order_by
                        | inicio_order_by'''
    
def p_instrucciones_order_by(t) :
    '''inicio_order_by  : ORDER BY sorting_rows state_limit
                        | state_limit'''

def p_instrucciones_sorting_rows(t) :
    'sorting_rows   : sort sorting_rows2'

def p_instrucciones_sorting_rows2(t) :
    '''sorting_rows2    : COMA sort sorting_rows2
                        |'''

def p_instrucciones_sort(t) :
    'sort   : ID asc_desc'

def p_instrucciones_asc_desc(t) :
    '''asc_desc : ASC
                | DESC
                |'''

def p_instrucciones_state_limit(t) :
    '''state_limit  : LIMIT all_entero
                    | state_offset'''

def p_instrucciones_all_entero(t) :
    '''all_entero   : ENTERO state_offset
                    | ALL state_offset'''

def p_instrucciones_state_offset(t) :
    '''state_offset : OFFSET ENTERO state_offset_opciones
                    | state_offset_opciones
                    | state_subquery'''

def p_instrucciones_state_offset_opciones(t) :
    '''state_offset_opciones    : state_union
                                | state_intersect
                                | state_except'''

def p_instrucciones_state_union(t) :
    '''state_union  : UNION state_opciones
                    |'''

def p_instrucciones_state_intersect(t) :
    '''state_intersect  : INTERSECT state_opciones'''

def p_instrucciones_state_except(t) :
    '''state_except : EXCEPT state_opciones
                    |'''

def p_instrucciones_state_opciones(t) :
    '''state_opciones   : SELECT selects
                        | ALL SELECT selects'''

def p_instrucciones_lista_parametros(t) :
    '''lista_parametros : parametro state_aliases_field lista_parametros2'''

def p_instrucciones_lista_parametros2(t) :
    '''lista_parametros2    : COMA parametro state_aliases_field lista_parametros2
                            |'''

def p_instrucciones_state_aliases_field(t) :
    '''state_aliases_field  : AS cadena_o_id
                            | cadena_o_id
                            |'''

def p_instrucciones_cadena_o_id(t) :
    '''cadena_o_id  : ID
                    | CADENA_DOBLE
                    | CADENA'''
    
def p_instrucciones_case_state(t) :
    'case_state : auxcase_state END case_state2'

def p_instrucciones_case_state2(t) :
    '''case_state2  : auxcase_state END case_state2
                    |'''

def p_instrucciones_auxcase_state(t) :
    '''auxcase_state    :   WHEN relacional THEN CADENA
                        | ELSE COMILLA_SIMPLE ID COMILLA_SIMPLE'''
#====================================================
#====================================================
#INSTRUCCIONES DE DELETE
def p_instrucciones_deletes(t) :
    'deletes    : ID FROM ID condicion_delete'

def p_instrucciones_condicion_delete(t) :
    '''condicion_delete : WHERE relacional
                        |'''
#====================================================
#====================================================
#INSTRUCCIONES DE ALTER TABLE
def p_instrucciones_alter_tables(t) :
    'alter_table    : ID def_alter'

def p_instrucciones_def_alter(t) :
    '''def_alter    : ADD def_alter_tb_add
                    | DROP def_alter_tb_drop
                    | ALTER COLUMN ID SET NOT NULL
                    | RENAME COLUMN ID TO ID'''

def p_instrucciones_def_alter_tb_add(t) :
    '''def_alter_tb_add : CHECK PARIZQ relacional PARDER
                        | CONSTRAINT constraint_params
                        | FOREIGN KEY PARIZQ lista_parametros
                        | COLUMN ID tipos'''

def p_instrucciones_def_alter_tb_add_constraint(t) :
    '''constraint_params    : ID UNIQUE PARIZQ ID PARDER
                            | ID FOREIGN KEY PARIZQ ID PARDER REFERENCES ID PARIZQ ID PARDER'''


def p_instrucciones_def_alter_tb_drop(t) :
    '''def_alter_tb_drop    : COLUMN ID
                            | CONSTRAINT ID PARDER REFERENCES PARIZQ lista_parametros PARDER'''

#====================================================
#====================================================
#INSTRUCCIONES DE UPDATE
def p_instrucciones_update_table(t) :
    'update_table   : ID SET def_update update_table_condicion'

def p_instrucciones_update_table_condicion(t) :
    '''update_table_condicion   : WHERE relacional
                                |'''

def p_instrucciones_def_update(t) :
    '''def_update   : ID IGUAL valor def_update2'''

def p_instrucciones_def_update2(t) :
    '''def_update2  : COMA ID IGUAL valor def_update2
                    |'''
#====================================================
#====================================================
#INSTRUCCIONES DE INSERT
def p_instrucciones_insercion(t) :
    'insercion  : INTO ID insercion_params'

def p_instrucciones_params(t) :
    '''insercion_params : PARIZQ lista_id PARDER VALUES PARIZQ lista_insercion PARDER
                        | VALUES PARIZQ lista_insercion PARDER'''

def p_instrucciones_lista_insercion(t) :
    '''lista_insercion  : valor lista_insercion2
                        | PARIZQ SELECT selects PARDER lista_insercion2'''

def p_instrucciones_lista_insercion2(t) :
    '''lista_insercion2 : COMA valor lista_insercion2
                        | COMA PARIZQ SELECT selects PARDER lista_insercion2
                        |'''
    try:
        print('se insertó: ', t[2])
    except:
        print('terminó lista insercion2')
#====================================================
#====================================================
#INSTRUCCIONES DE DROP
def p_instrucciones_dropear(t) :
    '''dropear  : DATABASE if_exist ID
                | TABLE ID'''

def p_instrucciones_if_exist(t) :
    '''if_exist : IF EXISTS
                |'''
#====================================================
#====================================================
#ELEMENTOS BÁSICOS
def p_instrucciones_lista_id(t) :
    'lista_id   : ID lista_id2'

def p_instrucciones_lista_id2(t) :
    '''lista_id2    : COMA ID lista_id2
                    |'''

def p_instrucciones_tipos(t) :
    '''tipos    : SMALLINT
                | INTEGER
                | BIGINT
                | R_DECIMAL
                | NUMERIC
                | REAL
                | DOUBLE PRECISION
                | MONEY
                | TEXT
                | TIMESTAMP
                | DATE
                | TIME
                | BOOLEAN
                | INTERVAL
                | CHARACTER varing_parizq
                | VARCHAR PARIZQ ENTERO PARDER
                | CHAR PARIZQ ENTERO PARDER
                | TIMESTAMP def_dt_types
                | TIME def_dt_types
                | INTERVAL def_interval'''

def p_instrucciones_varing_parizq(t) :
    '''varing_parizq    : VARYING PARIZQ ENTERO PARDER
                        | PARIZQ ENTERO PARDER'''

def p_instrucciones_def_dt_types(t) :
    '''def_dt_types : PARIZQ ENTERO PARDER with_time_zone
                    | WITHOUT TIME ZONE
                    | WITH TIME ZONE'''

def p_instrucciones_with_time_zone(t) :
    '''with_time_zone   : WITHOUT TIME ZONE
                        | WITH TIME ZONE
                        |'''

def p_instrucciones_def_interval(t) :
    '''def_interval : def_fld_to def_interval_param
                    | PARIZQ ENTERO PARDER'''

def p_instrucciones_def_interval_param(t) :
    '''def_interval_param   : PARIZQ ENTERO PARDER
                            |'''

def p_instrucciones_def_fld_to(t) :
    'def_fld_to   : def_fields to_def_fields'

def p_instrucciones_to_def_fields(t) :
    '''to_def_fields    : TO def_fields
                        |'''
    
def p_instrucciones_def_fields(t) :
    '''def_fields   : YEAR
                    | MONTH
                    | DAY
                    | HOUR
                    | MINUTE
                    | SECOND'''

def p_instrucciones_relacional(t) :
    '''relacional   : aritmetica continuacion_relacional_aritmetica relacional2
                    | NOT relacional relacional2
                    | EXISTS state_subquery relacional2
                    | IN state_subquery relacional2
                    | NOT IN state_subquery relacional2
                    | ANY state_subquery relacional2
                    | SOME state_subquery relacional2
                    | state_between relacional2
                    | state_predicate_nulls relacional2
                    | state_is_distinct relacional2
                    | state_pattern_match relacional2'''

def p_instrucciones_relacional2(t) :
    '''relacional2  : AND relacional
                    | OR relacional
                    |'''

def p_instrucciones_continuacion_relacional_aritmetica(t) :
    '''continuacion_relacional_aritmetica   : MENOR aritmetica
                                            | MAYOR aritmetica
                                            | IGUAL igual aritmetica
                                            | MENORIGUAL aritmetica
                                            | MAYORIGUAL aritmetica
                                            | DIFERENTE aritmetica
                                            | NO_IGUAL aritmetica
                                            |'''

def p_instrucciones_aritmetica(t) :
    '''aritmetica   : valor aritmetica2
                    | PARIZQ aritmetica PARDER aritmetica2
                    | funciones_math_esenciales aritmetica2
                    | fun_binario_select aritmetica2
                    | fun_trigonometrica aritmetica2'''

def p_instrucciones_aritmetica2(t) :
    '''aritmetica2   : MAS aritmetica aritmetica2
                    | MENOS aritmetica aritmetica2
                    | POR aritmetica aritmetica2
                    | DIVISION aritmetica aritmetica2
                    | MODULO aritmetica aritmetica2
                    | EXP aritmetica aritmetica2
                    |'''

def p_instrucciones_valor(t) :
    '''valor    : ID punto_id
                | ENTERO
                | DECIMAL
                | date_functions
                | CADENA
                | lista_funciones
                | fun_trigonometrica
                | fun_binario_where
                | state_subquery
                | TRUE
                | FALSE'''
    t[0] = t[1]

def p_instrucciones_state_between(t) :
    'state_between  : valor continuacion_state_between'

def p_instrucciones_continuacion_state_between(t) :
    '''continuacion_state_between   : BETWEEN valor AND valor
                                    | NOT between_in'''

def p_instrucciones_between_in(t) :
    '''between_in   : BETWEEN valor AND valor
                    | IN state_subquery'''

def p_instrucciones_predicate_nulls(t) :
    'state_predicate_nulls  : valor nules'

def p_instrucciones_nules(t) :
    '''nules    : ISNULL
                | NOTNULL
                | IS unul'''

def p_instrucciones_state_is_distinct(t) :
    'state_is_distinct  : valor IS state_is_distinct_notis'

def p_instrucciones_state_is_distinct_notis(t) :
    '''state_is_distinct_notis      : DISTINCT FROM valor state_aliases_table
                                    | NOT DISTINCT FROM valor state_aliases_table'''

def p_instrucciones_state_aliases_table(t) :
    '''state_aliases_table  : AS ID
                            | ID
                            |'''

def p_instrucciones_state_pattern_match(t) :
    'state_pattern_match : aritmetica LIKE cadenas'

def p_instrucciones_cadenas(t) :
    '''cadenas  : CADENA
                | CADENA_DOBLE'''

def p_instruciones_funciones_math_esenciales(t) :
    '''lista_funciones_math_esenciales  : COUNT PARIZQ lista_funciones_math_esenciales PARDER o_parametro
                                        | SUM PARIZQ lista_funciones_math_esenciales PARDER o_parametro
                                        | AVG PARIZQ lista_funciones_math_esenciales PARDER o_parametro'''

def p_instrucciones_o_parametro(t) :
    '''o_parametro  : parametro
                    |'''

def p_instrucciones_lista_funciones_math_esenciales(t) :
    '''lista_funciones_math_esenciales  : aritmetica
                                        | lista_id
                                        | POR'''

def p_instrucciones_parametro(t) :
    '''parametro    : ID punto_id
                    | lista_funciones
                    | funciones_math_esenciales
                    | fun_binario_select
                    | date_functions
                    | state_subquery
                    | CADENA
                    | DECIMAL
                    | ENTERO'''

def p_instrucciones_punto_id(t) :
    '''punto_id : PUNTO ID
                |'''

def p_instrucciones_funciones_math_esenciales(t) :
    '''funciones_math_esenciales    : COUNT PARIZQ lista_funciones_math_esenciales PARDER o_parametro
                                    | SUM PARIZQ lista_funciones_math_esenciales PARDER o_parametro
                                    | AVG PARIZQ lista_funciones_math_esenciales PARDER o_parametro'''

def p_instrucciones_lista_funciones(t) :
    '''lista_funciones  : ABS PARIZQ funcion_math_parametro PARDER
                        | CBRT PARIZQ funcion_math_parametro PARDER
                        | CEIL PARIZQ funcion_math_parametro PARDER
                        | CEILING PARIZQ funcion_math_parametro PARDER
                        | DEGREES PARIZQ funcion_math_parametro PARDER
                        | DIV PARIZQ funcion_math_parametro COMA funcion_math_parametro PARDER
                        | REXP PARIZQ funcion_math_parametro PARDER
                        | FACTORIAL PARIZQ funcion_math_parametro PARDER
                        | FLOOR PARIZQ funcion_math_parametro PARDER
                        | GCD PARIZQ funcion_math_parametro PARDER
                        | LN PARIZQ funcion_math_parametro PARDER
                        | LOG PARIZQ funcion_math_parametro PARDER
                        | MOD PARIZQ funcion_math_parametro PARDER
                        | PI PARIZQ PARDER
                        | POWER PARIZQ funcion_math_parametro COMA ENTERO PARDER
                        | RADIANS PARIZQ funcion_math_parametro PARDER
                        | ROUND PARIZQ funcion_math_parametro PARDER
                        | SIGN PARIZQ funcion_math_parametro PARDER
                        | SQRT PARIZQ funcion_math_parametro PARDER
                        | WIDTH_BUCKET PARIZQ funcion_math_parametro COMA funcion_math_parametro COMA funcion_math_parametro COMA funcion_math_parametro PARDER
                        | TRUNC PARIZQ funcion_math_parametro PARDER
                        | RANDOM PARIZQ PARDER'''

def p_instrucciones_lista_funciones_where(t) :
    '''lista_funciones_where    : ABS PARIZQ funcion_math_parametro PARDER
                                | CBRT PARIZQ funcion_math_parametro PARDER
                                | CEIL PARIZQ funcion_math_parametro PARDER
                                | CEILING PARIZQ funcion_math_parametro PARDER'''

def p_instrucciones_funcion_math_parametro(t) :
    '''funcion_math_parametro   : ENTERO
                                | ID
                                | DECIMAL
                                | funcion_math_parametro_negativo'''

def p_instrucciones_funcion_math_parametro_negativo(t) :
    'funcion_math_parametro_negativo    : MENOS dec_o_ent'

def p_instrucciones_dec_o_ent(t) :
    '''dec_o_ent  : DECIMAL
                | ENTERO'''

def p_instrucciones_fun_binario_select(t) :
    '''fun_binario_select   : LENGTH PARIZQ valor PARDER
                            | SUBSTRING PARIZQ valor COMA ENTERO COMA ENTERO PARDER
                            | TRIM PARIZQ CADENA FROM valor PARDER
                            | SHA256 PARIZQ valor PARDER
                            | SUBSTR PARIZQ valor COMA ENTERO COMA ENTERO PARDER
                            | GET_BYTE PARIZQ valor bytea COMA ENTERO PARDER
                            | SET_BYTE PARIZQ valor bytea COMA ENTERO PARDER
                            | CONVERT PARIZQ valor AS tipos PARDER
                            | ENCODE PARIZQ valor bytea COMA CADENA PARDER
                            | DECODE PARIZQ valor COMA CADENA PARDER'''

def p_instrucciones_fun_binario_where(t) :
    '''fun_binario_where    : LENGTH PARIZQ valor PARDER
                            | SUBSTRING PARIZQ valor COMA ENTERO COMA ENTERO PARDER
                            | TRIM PARIZQ CADENA FROM valor PARDER
                            | SUBSTR PARIZQ valor COMA ENTERO COMA ENTERO PARDER'''

def p_instrucciones_bytea(t) :
    '''bytea    : DOS_PUNTOS DOS_PUNTOS BYTEA
                |'''

def p_instrucciones_fun_trigonometrica(t) :
    '''fun_trigonometrica   : ACOS PARIZQ aritmetica PARDER
                            | ASIN PARIZQ aritmetica PARDER
                            | ATAN PARIZQ aritmetica PARDER
                            | ATAN2 PARIZQ aritmetica COMA aritmetica PARDER
                            | COS PARIZQ aritmetica PARDER
                            | COT PARIZQ aritmetica PARDER
                            | SIN PARIZQ aritmetica PARDER
                            | TAN PARIZQ aritmetica PARDER
                            | ACOSD PARIZQ aritmetica PARDER
                            | ASIND PARIZQ aritmetica PARDER
                            | ATAND PARIZQ aritmetica PARDER
                            | ATAN2D PARIZQ aritmetica COMA aritmetica PARDER
                            | COSD PARIZQ aritmetica PARDER
                            | COTD PARIZQ aritmetica PARDER
                            | SIND PARIZQ aritmetica PARDER
                            | TAND PARIZQ aritmetica PARDER
                            | SINH PARIZQ aritmetica PARDER
                            | COSH PARIZQ aritmetica PARDER
                            | TANH PARIZQ aritmetica PARDER
                            | ASINH PARIZQ aritmetica PARDER
                            | ACOSH PARIZQ aritmetica PARDER
                            | ATANH PARIZQ aritmetica PARDER'''

def p_instrucciones_date_functions(t) :
    '''date_functions   : EXTRACT PARIZQ lista_date_functions
                        | date_part PARIZQ lista_date_functions
                        | NOW PARIZQ lista_date_functions
                        | CURRENT_TIME
                        | CURRENT_DATE
                        | TIMESTAMP CADENA
                        '''
    #| lista_date_functions
        
def p_instrucciones_lista_date_functions(t) :
    
    '''lista_date_functions : def_fields FROM TIMESTAMP CADENA PARDER
                            | CADENA COMA INTERVAL CADENA PARDER                        
                            | TIMESTAMP CADENA
                            | CURRENT_TIME
                            | CURRENT_DATE
                            | PARDER'''

def p_instrucciones_state_subquery(t) :
    'state_subquery : PARIZQ SELECT selects PARDER'

#====================================================
#CONTROL DE ERRORES
def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t)

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    retorno = parser.parse(input)
    return retorno