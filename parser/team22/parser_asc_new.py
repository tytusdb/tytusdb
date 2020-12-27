# Construyendo el analizador léxico
import ply.lex as lex
from lex import *
from columna import *
from graphviz import Graph
from grammar.gramatical import *

dot = Graph()
dot.attr(splines = 'false')
dot.node_attr.update(fontname = 'Eras Medium ITC', style='filled', fillcolor="tan",
                     fontcolor = 'black', rankdir = 'RL')
dot.edge_attr.update(color = 'black')

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
    t[0] = t[1]
    
def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]
    

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]
    

def p_instruccion(t) :
    '''instruccion      : CREATE creacion
                        | SHOW show_db PTCOMA
                        | ALTER DATABASE alter_database PTCOMA
                        | USE cambio_bd
                        | SELECT selects PTCOMA
                        | DELETE deletes
                        | ALTER TABLE alter_table PTCOMA
                        | UPDATE update_table PTCOMA
                        | INSERT insercion
                        | DROP dropear
                        '''
    if t[1].upper() == 'CREATE' or t[1].upper() == 'SHOW' or t[1].upper() == 'DROP' or t[1].upper() == 'USE' or t[1].upper() == 'SELECT':
        t[0] = t[2]
    elif t[1].upper() == 'ALTER' and t[2].upper() == 'DATABASE':
        t[0] = t[3]


#========================================================

#========================================================
# INSTRUCCION CON "CREATE"
def p_instruccion_creacion(t) :
    '''creacion     : DATABASE crear_bd
                    | OR REPLACE DATABASE replace_bd
                    | TABLE crear_tb
                    | TYPE crear_type'''

    if t[1].upper() == 'DATABASE' or t[1].upper() == 'TABLE':
        t[0] = t[2]
    elif t[1].upper() == 'OR':
        t[0] = t[4]

def p_instruccion_crear_BD(t) :
    'crear_bd     : ID PTCOMA'
    t[0] = Crear_BD(t[1].upper(), t.lexer.lineno - 1)

def p_instruccion_crear_BD_Parametros(t) :
    'crear_bd     : ID lista_parametros_bd PTCOMA'
    t[0] = Crear_BD(t[1].upper(), t.lexer.lineno - 1)

def p_instruccion_crear_BD_if_exists(t) :
    'crear_bd       : IF NOT EXISTS ID PTCOMA'
    t[0] = Crear_BD(t[4].upper(), t.lexer.lineno - 1)

def p_instruccion_crear_BD_if_exists_Parametros(t) :
    'crear_bd       : IF NOT EXISTS ID lista_parametros_bd PTCOMA'
    t[0] = Crear_BD(t[4].upper(), t.lexer.lineno - 1)

def p_instruccion_replace_BD(t) :
    'replace_bd     : ID PTCOMA'
    t[0] = Crear_BD(t[1].upper(), t.lexer.lineno - 1, True)

def p_instruccion_replace_BD_Parametros(t) :
    'replace_bd     : ID lista_parametros_bd PTCOMA'
    t[0] = Crear_BD(t[1].upper(), t.lexer.lineno - 1, True)

def p_instruccion_replace_BD_if_exists(t) :
    'replace_bd       : IF NOT EXISTS ID PTCOMA'
    t[0] = Crear_BD(t[4].upper(), t.lexer.lineno - 1, True)

def p_instruccion_replace_BD_if_exists_Parametros(t) :
    'replace_bd       : IF NOT EXISTS ID lista_parametros_bd PTCOMA'
    t[0] = Crear_BD(t[4].upper(), t.lexer.lineno - 1, True)

def p_instruccion_crear_TB_herencia(t):
    '''crear_tb     : ID PARIZQ crear_tb_columnas PARDER tb_herencia PTCOMA'''


def p_instruccion_crear_TB(t):
    '''crear_tb     : ID PARIZQ crear_tb_columnas PARDER PTCOMA'''
    t[0] = Crear_TB(t[1].lower(), t[3], t.lexer.lineno - 1)


def p_isntruccion_crear_TYPE(t) :
    '''crear_type   : ID AS ENUM PARIZQ lista_objetos PARDER PTCOMA
                    '''


def p_instruccion_TB_herencia(t) :
    'tb_herencia    : INHERITS PARIZQ ID PARDER'


#========================================================

#========================================================
# INSTRUCCION SHOW DATABASE
def p_instruccion_show(t) :
    '''show_db      : DATABASES
                    | DATABASES LIKE CADENA''' 
    if len(t) == 2:
        t[0] = Show_BD(t.lexer.lineno - 1)
    else:
        t[0] = Show_BD(t.lexer.lineno - 1, t[3].upper())

#========================================================

#========================================================
# INSTRUCCION ALTER DATABASE
def p_instruccion_alter_database(t) :
    '''alter_database   : ID RENAME TO ID
                        | ID OWNER TO def_alter_db'''
    if t[2].upper() == 'RENAME':
        t[0] = Alter_BD(t[1].upper(), t[4].upper(), t.lexer.lineno - 1)

def p_def_alter_db(t) :
    '''def_alter_db     : ID
                        | CURRENT_USER
                        | SESSION_USER'''


#========================================================

#========================================================

# INSTRUCCION CON "USE"
def p_instruccion_Use_BD(t) :
    'cambio_bd     : ID PTCOMA'
    t[0] = Cambio_BD(t[1].upper(), t.lexer.lineno - 1)

#========================================================

#========================================================
# INSTRUCCIONES CON "SELECT"

def p_instruccion_selects(t) :
    '''selects      : lista_parametros FROM lista_parametros inicio_condicional state_fin_query 
                    '''


def p_instruccion_selects2(t) :
    '''selects      : lista_parametros COMA CASE case_state FROM lista_parametros inicio_condicional state_fin_query inicio_group_by
                    '''


def p_instruccion_selects3(t) :
    '''selects      : fun_trigonometrica state_aliases_field 
                    | aritmetica state_aliases_field '''
    t[0] = Select({'objeto': t[1], 'alias': t[2]}, t.lexer.lineno - 1)

def p_instruccion_selects4(t) :
    '''selects      : fun_trigonometrica state_aliases_field FROM ID state_aliases_table 
                    | aritmetica state_aliases_field FROM ID state_aliases_table  '''
    


def p_instruccion_selects5(t) :
    '''selects      : POR FROM select_all 
                    | POR FROM state_subquery inicio_condicional 
                    | GREATEST PARIZQ lista_parametros_funciones PARDER 
                    | LEAST PARIZQ lista_parametros_funciones PARDER 
                    | lista_parametros 
                    '''


def p_instruccion_selects_where(t) :
    'inicio_condicional      : WHERE relacional inicio_condicional'


def p_instruccion_selects_sin_where(t) :
    'inicio_condicional      : inicio_group_by'


def p_instruccion_selects_group_by(t) :
    'inicio_group_by      : GROUP BY lista_parametros inicio_having'


def p_instruccion_selects_group_by2(t) :
    'inicio_group_by      : inicio_order_by '


def p_instruccion_selects_having(t) :
    'inicio_having     : HAVING relacional inicio_order_by'


def p_instruccion_selects_having2(t) :
    'inicio_having      : inicio_order_by '


def p_instruccion_selects_order_by(t) :
    'inicio_order_by      : ORDER BY sorting_rows state_limit'


def p_instruccion_selects_order_by2(t) :
    'inicio_order_by      : state_limit '


def p_instruccion_selects_limit(t) :
    '''state_limit      : LIMIT ENTERO state_offset
                        | LIMIT ALL state_offset'''


def p_instruccion_selects_limit2(t) :
    'state_limit      : state_offset'


def p_instruccion_selects_offset(t) :
    '''state_offset         : OFFSET ENTERO state_union 
                            | OFFSET ENTERO state_intersect
                            | OFFSET ENTERO state_except'''


def p_instruccion_selects_offset2(t) :
    '''state_offset      : '''


def p_instruccion_state_fin_query(t) :
    '''state_fin_query      : state_union 
                            | state_intersect
                            | state_except
                            | state_subquery
                            |'''

    
def p_instruccion_selects_union(t) :
    '''state_union      : UNION SELECT selects
                        | UNION ALL SELECT selects'''

    
def p_instruccion_selects_union2(t) :
    'state_union      : '


def p_instruccion_selects_intersect(t) :
    '''state_intersect      : INTERSECT SELECT selects
                            | INTERSECT ALL SELECT selects'''
    
    
def p_instruccion_selects_except(t) :
    '''state_except     : EXCEPT SELECT selects
                        | EXCEPT ALL SELECT selects'''


def p_instruccion_Select_All(t) :
    'select_all     : ID state_aliases_table inicio_condicional'


#Gramatica para fechas
#========================================================
def p_date_functions1(t):
    '''date_functions   : EXTRACT PARIZQ opcion_date_functions 
                        | NOW PARIZQ PARDER'''


def p_date_functions(t):
    '''date_functions   : date_part PARIZQ opcion_date_functions
                        | opcion_date_functions'''


def p_validate_date(t):
    'lista_date_functions : def_fields FROM TIMESTAMP CADENA PARDER'


def p_opcion_lista_date_fuctions(t):
    '''opcion_date_functions    : opcion_date_functions lista_date_functions
                                | lista_date_functions
                                '''      


def p_lista_date_functions(t):
    '''lista_date_functions : TIMESTAMP CADENA
                            | CURRENT_DATE
                            | CURRENT_TIME
                            | PARDER'''



# Subqueries
def p_state_subquery(t):
    '''state_subquery   : PARIZQ SELECT selects PARDER'''
      
#========================================================

    
#========================================================
# INSERT INTO TABLAS
def p_instruccion_Insert_columnas(t) :
    '''insercion    : INTO ID PARIZQ lista_id PARDER VALUES PARIZQ lista_insercion PARDER PTCOMA
                    '''


def p_instruccion_insert(t) :
    '''insercion    : INTO ID VALUES PARIZQ lista_insercion PARDER PTCOMA
                    '''


#========================================================
# DROP BASES DE DATOS Y TABLAS
def p_instruccion_Drop_BD_exists(t) :
    '''dropear      : DATABASE IF EXISTS ID PTCOMA
                    '''
    t[0] = Drop_BD(t[4].upper(), t.lexer.lineno - 1)

def p_instruccion_Drop_BD(t) :
    '''dropear      : DATABASE ID PTCOMA
                    '''
    t[0] = Drop_BD(t[2].upper(), t.lexer.lineno - 1)


def p_instruccion_Drop_TB(t) :
    '''dropear      : TABLE ID PTCOMA
                    '''
    t[0] = Drop_TB(t[2].lower(), t.lexer.lineno - 1)

#========================================================

#========================================================
# PARAMETROS PARA CREATE BASE DE DATOS
def p_instrucciones_parametros_BD(t) :
    '''lista_parametros_bd  : parametros_bd
                            | parametros_bd parametros_bd'''


def p_parametros_BD_owner(t) :
    '''parametros_bd    : OWNER IGUAL ID
                        | OWNER ID'''


def p_parametros_BD_Mode(t) :
    '''parametros_bd    : MODE IGUAL ENTERO
                        | MODE ENTERO'''


#========================================================

# LISTA DE SORTING ROWS
#========================================================
def p_instrucciones_lista_sorting_rows(t) :
    'sorting_rows    : sorting_rows COMA sort'



def p_instrucciones_sort_DESC(t) :   
    'sorting_rows         : sort'


def p_temporalmente_nombres(t) :
    '''sort         : ID ASC
                    | ID DESC
                    | ID'''

#========================================================

#========================================================
# LISTA DE PARAMETROS DE FUNCINOES
def p_instrucciones_lista_parametros_fun(t) :
    'lista_parametros_funciones    : lista_parametros_funciones COMA valor_dato'


def p_instrucciones_parametro_fun(t) :
    'lista_parametros_funciones    : valor_dato '


def p_valores_fun(t) :
    '''valor_dato        : ID '''   

    
def p_valores_fun2(t) :
    '''valor_dato        : ENTERO
                         | DECIMAL '''   

    
def p_valores_fun3(t) :
    '''valor_dato        : CADENA '''   

#========================================================

#========================================================
# LISTA DE PARAMETROS
def p_instrucciones_lista_parametros(t) :
    'lista_parametros    : lista_parametros COMA es_distinct parametro state_aliases_field'



def p_instrucciones_parametro(t) :
    'lista_parametros    : es_distinct parametro state_aliases_field '
    

def p_instrucciones_distinct(t) :
    '''es_distinct      : DISTINCT
                        | '''



def p_parametro_con_tabla(t) :
    '''parametro        : ID PUNTO ID
                        | ID PUNTO POR'''   # ESTO SE HA COLOCADO CUANDO SE SOLICITAN TODAS LAS 
                                            # COLUMNAS DE ALGUNA TABLA INDICADA.



def p_parametros_funciones(t) :
    '''parametro         : funciones_math_esenciales
                         | fun_binario_select
                         | date_functions
                         | state_subquery
                         '''


def p_parametros_funciones2(t) :
    '''parametro         : lista_funciones
                         '''


def p_parametros_cadena(t) :
    'parametro         : CADENA'


def p_parametros_numeros(t) :
    '''parametro            : DECIMAL
                            | ENTERO'''


def p_parametro_sin_tabla(t) :
    'parametro        : ID'

#========================================================

#========================================================
# CONTENIDO DE TABLAS EN CREATE TABLE
def p_instrucciones_lista_columnas(t) :
    'crear_tb_columnas      : crear_tb_columnas COMA crear_tb_columna'
    t[1].append(t[3])
    t[0] = t[1]

def p_instrucciones_columnas(t) :
    'crear_tb_columnas      : crear_tb_columna'
    t[0] = [t[1]]


def p_instrucciones_columna_parametros(t) :
    'crear_tb_columna       : ID tipos parametros_columna'
    col = Columna(tipo = t[2], line = t.lexer.lineno)
    
    for parametro in t[3]:
        if 'default' in parametro:
            col.addDefault(parametro['default'])
        elif 'is_null' in parametro:
            col.addNull(parametro['is_null'])
        elif 'is_unique' in parametro:
            if 'constraint' in parametro:
                col.addUnique(valor = parametro['is_unique'], constraint = parametro['constraint'])
            else:
                col.addUnique(parametro['is_unique'])
        elif 'is_primary' in parametro:
            col.addPrimaryKey(parametro['is_primary'])
        elif 'references' in parametro:
            col.addReference(parametro['references'])

    col.printCol()
    t[0] = {'nombre': t[1].lower(), 'col': col}



def p_instrucciones_columna_noparam(t) :
    'crear_tb_columna       : ID tipos'
    t[0] = {'nombre': t[1].lower(), 'col': Columna(tipo = t[2], line = t.lexer.lineno - 1)}


def p_instrucciones_columna_pk(t) :
    'crear_tb_columna       : PRIMARY KEY PARIZQ lista_id PARDER'
    t[0] = {'primary': t[4]}

def p_instrucciones_columna_fk(t) :
    'crear_tb_columna       : FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER'
    if len(t[4]) != len(t[9]):
        error = Error('Semántico', "El número de columnas referencias es distinto al número de columnas foráneas", t.lexer.lineno - 1)
        tabla_errores.agregar(error)
    else:
        t[0] = {'foreign': t[4], 'table': t[7].lower(), 'references': t[9]}
    
def p_instrucciones_columna_check(t) :
    'crear_tb_columna   : chequeo'


def p_instrucciones_columna_unique(t) :
    'crear_tb_columna   : UNIQUE PARIZQ lista_id PARDER'
    t[0] = {'unique': t[3]}

def p_instrucciones_lista_params_columnas(t) :
    'parametros_columna     : parametros_columna parametro_columna'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_params_columnas(t) :
    'parametros_columna     : parametro_columna'
    t[0] = [t[1]]

def p_instrucciones_parametro_columna_default(t) :
    'parametro_columna      : DEFAULT valor'
    t[0] = {'default': t[2]}

def p_instrucciones_parametro_columna_nul(t) :
    'parametro_columna      : unul'
    t[0] = t[1]

def p_instrucciones_parametro_columna_unique(t) :
    'parametro_columna      : unic'
    t[0] = t[1]

def p_instrucciones_parametro_columna_checkeo(t) :
    'parametro_columna      : chequeo'
 

def p_instrucciones_parametro_columna_pkey(t) :
    'parametro_columna      : PRIMARY KEY'
    t[0] = {'is_primary': 1}

def p_instrucciones_parametro_columna_fkey(t) :
    'parametro_columna      : REFERENCES ID PARIZQ ID PARDER'
    t[0] = {'references': t[2] + '.' + t[4]}

def p_instrucciones_nnul(t) :
    'unul   : NOT NULL'
    t[0] = {'is_null': TipoNull.NOT_NULL}

def p_instrucciones_unul(t) :
    'unul   : NULL'
    t[0] = {'is_null': TipoNull.NULL}

def p_instrucciones_unic_constraint(t) :
    'unic   : CONSTRAINT ID UNIQUE'
    t[0] = {'is_unique': 1, 'constraint': Constraint(tipo = TipoConstraint.UNIQUE, name = t[2], line = t.lexer.lineno)}


def p_instrucciones_unic(t) :
    'unic   : UNIQUE'
    t[0] = {'is_unique': 1}

def p_instrucciones_chequeo_constraint(t) :
    'chequeo    : CONSTRAINT ID CHECK PARIZQ relacional PARDER'


def p_instrucciones_chequeo(t) :
    'chequeo    : CHECK PARIZQ relacional PARDER'

    
#========================================================

#========================================================
# LISTA DE ELEMENTOS REUTILIZABLES
def p_instrucciones_lista_ids(t) :
    'lista_id   : lista_id COMA ID'
    t[1].append(t[3].lower())
    t[0] = t[1]

def p_instrucciones_lista_id(t) :
    'lista_id   : ID'
    t[0] = [t[1].lower()]
    

def p_instrucciones_lista_objetos(t) :
    '''lista_objetos  : lista_objetos COMA objeto
                      | CADENA COMA INTERVAL CADENA'''


def p_instrucciones_lista_objeto(t) :
    'lista_objetos  : objeto'


def p_instrucciones_objeto2(t) :
    '''objeto       : valor
                    | fun_binario_insert
                    '''


def p_instrucciones_lista_insercion_objeto(t) :
    '''lista_insercion  : lista_insercion COMA objeto
                         '''



def p_instrucciones_lista_insercion_select(t) :
    'lista_insercion  : lista_insercion COMA PARIZQ SELECT state_subquery PARDER'


def p_instrucciones_insercion_objeto(t) :
    '''lista_insercion  : objeto
                        '''


def p_instrucciones_insercion_select(t) :
    'lista_insercion  : PARIZQ SELECT state_subquery PARDER'
    

#========================================================

#========================================================

# INSTRUCCION CON "DELETE"
def p_instruccion_delete(t) :
    '''deletes      : delete_condicional
                    | delete_incondicional'''
 

def p_instruccion_delete_incondicional(t) :
    'delete_incondicional     : ID PTCOMA'


def p_instruccion_delete_condicional(t) :
    'delete_condicional     : ID WHERE relacional PTCOMA'


# INSTRUCCION ALTER TABLE
def p_instruccion_alter(t) :
    '''alter_table  : ID def_alter'''



def p_def_alter(t) :
    '''def_alter    : ADD COLUMN ID tipos
                    | DROP COLUMN ID
                    | ADD CHECK PARIZQ relacional PARDER
                    | ADD CONSTRAINT ID UNIQUE PARIZQ ID PARDER
                    | ADD FOREIGN KEY PARIZQ lista_parametros PARDER REFERENCES ID PARIZQ lista_parametros PARDER
                    | ALTER COLUMN ID SET NOT NULL
                    | DROP CONSTRAINT ID
                    | RENAME COLUMN ID TO ID
                    |'''
                    



def p_tipos_1(t) :
    '''tipos        : SMALLINT
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
                    | INTERVAL'''      
    if len(t) == 2:
        t[0] = {'tipo': TipoColumna[t[1].upper()]}
    else:
        t[0] = {'tipo': TipoColumna['DOUBLE_PRECISION']}

def p_tipos_2(t) :
    '''tipos        : CHARACTER VARYING PARIZQ ENTERO PARDER'''
    t[0] = {'tipo': TipoColumna['CHARACTER_VARYING'], 'n': t[4]}

def p_tipos_3(t) :
    '''tipos        : VARCHAR PARIZQ ENTERO PARDER
                    | CHARACTER PARIZQ ENTERO PARDER
                    | CHAR PARIZQ ENTERO PARDER'''   
    t[0] = {'tipo': TipoColumna[t[1].upper()], 'n': t[3]}

def p_tipos_4(t) :
    '''tipos        : TIMESTAMP def_dt_types
                    | TIME def_dt_types'''
    sufix = t[2]['w'] if 'w' in t[2] else ''
    t[0] = {'tipo': TipoColumna[t[1].upper() + sufix]}
    if 'p' in t[2]:
        t[0]['p'] = t[2]['p'] 

def p_tipos_5(t) :
    '''tipos        : INTERVAL def_interval'''
    t[0] = t[2]
    t[0].update({'tipo': TipoColumna[t[1].upper()]})


def p_def_dt_types_1(t) :
    '''def_dt_types : PARIZQ ENTERO PARDER WITHOUT TIME ZONE
                    | PARIZQ ENTERO PARDER WITH TIME ZONE
                    | PARIZQ ENTERO PARDER'''
    t[0] = {'p': t[2]}

    if len(t) > 4:
        if t[4].lower() == 'without':
            t[0]['w'] = '_WO' 
        else:
            t[0]['w'] = '_W' 

                    
def p_def_dt_types_2(t) :
    '''def_dt_types : WITHOUT TIME ZONE
                    | WITH TIME ZONE'''
    if t[1].lower() == 'without':
        t[0] = {'w': '_WO'}
    else:
        t[0] = {'w': '_W'}

def p_def_interval_1(t) :
    '''def_interval : def_fld_to PARIZQ ENTERO PARDER
                    | def_fld_to'''
    t[0] = {'field': t[1]}
    if len(t) == 5:
        t[0]['p'] = t[3]

def p_def_interval_2(t) :
    '''def_interval : PARIZQ ENTERO PARDER'''
    t[0] = {'p': t[2]}

def p_def_fld_to(t) :
    '''def_fld_to   : def_fields TO def_fields
                    | def_fields'''
    t[0] = t[1]
    if len(t) > 2:
        t[0]['destino'] = t[3]['origen']


def p_def_fields(t) :
    '''def_fields   : YEAR
                    | MONTH
                    | DAY
                    | HOUR
                    | MINUTE
                    | SECOND'''
    t[0] = {'origen': TipoFields[t[1].upper()]}

def p_relacional_op(t) :
    '''relacional   : aritmetica MENOR aritmetica
                    | aritmetica MAYOR aritmetica
                    | aritmetica IGUAL IGUAL aritmetica
                    | aritmetica MENORIGUAL aritmetica
                    | aritmetica MAYORIGUAL aritmetica
                    | aritmetica DIFERENTE aritmetica
                    | aritmetica NO_IGUAL aritmetica
                    | aritmetica IGUAL aritmetica
                    | relacional AND relacional
                    | relacional OR relacional
                    | NOT relacional
                    '''


def p_relacional_val(t) :
    'relacional   : aritmetica'
    t[0] = t[1]


def p_relacional(t) :
    '''relacional   : EXISTS state_subquery
                    | NOT EXISTS state_subquery
                    | IN state_subquery
                    | NOT IN state_subquery
                    | ANY state_subquery
                    | ALL state_subquery
                    | SOME state_subquery
                    '''


def p_relacional2(t) :
    '''relacional   : state_between
                    | state_predicate_nulls
                    | state_is_distinct
                    | state_pattern_match
                    '''
    t[0] = t[1]
        
def p_aritmetica1(t) :
    '''aritmetica   : PARIZQ aritmetica PARDER
                    | PARIZQ relacional PARDER'''
    t[0] = t[2]

def p_aritmetica(t) :
    '''aritmetica   : aritmetica MAS aritmetica
                    | aritmetica MENOS aritmetica
                    | aritmetica POR aritmetica
                    | aritmetica DIVISION aritmetica
                    | aritmetica MODULO aritmetica
                    | aritmetica EXP aritmetica
                    | MENOS aritmetica 
                    | valor'''
    if len(t) == 2:
        t[0] = t[1]
    elif len(t) == 3:
        t[0] = FuncionAritmetica( 'NEGATIVO', str(t[1]), str(t[3]), t.lexer.lineno - 1 )
    else:
        t[0] = FuncionAritmetica( str(t[2]), str(t[1]), str(t[3]), t.lexer.lineno - 1 )

def p_aritmetica2(t) :
    '''aritmetica   : funciones_math_esenciales
                    | fun_binario_select
                    '''
    t[0] = t[1]

def p_aritmetica1_2(t) :
    '''aritmetica   : lista_funciones
                    '''
    t[0] = t[1]

def p_aritmetica3(t) :
    '''aritmetica   : fun_trigonometrica'''
    t[0] = t[1]

def p_valor_id(t) :
    '''valor        : ID
                    | ID PUNTO ID'''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = t[1] + t[2] + t[3]

def p_valor_num(t) :
    '''valor        : ENTERO
                    | DECIMAL  '''
    t[0] = t[1]

def p_valor(t) :
    '''valor        : CADENA
                    '''
    t[0] = t[1]

def p_valor2(t) :
    '''valor        : lista_funciones_where
                    | fun_binario_where
                    | state_subquery
                    | fun_binario_update
                    | fun_binario_select
                    '''
    t[0] = t[1]

def p_valor3(t) :
    '''valor        : fun_trigonometrica
                    '''
    t[0] = t[1]

def p_valor4(t) :
    '''valor        : date_functions
                    '''
    t[0] = t[1]


def p_instruccion_update_where(t) :
    '''update_table : ID SET def_update WHERE relacional'''


    

def p_instruccion_update(t) :
    '''update_table : ID SET def_update'''


def p_def_update_rec(t) :
    '''def_update   : def_update COMA def_update_asig'''


def p_def_update(t) :
    '''def_update   : def_update_asig'''



def p_def_update_2(t) :
    '''def_update_asig   : ID IGUAL valor'''


# BETWEEN
#=======================================================
def p_between(t) :
    '''state_between    : valor BETWEEN valor AND valor
                        | valor NOT BETWEEN valor AND valor
                        | valor NOT IN state_subquery'''


#=======================================================

# IS [NOT] DISTINCT
#=======================================================
def p_is_distinct(t) :
    '''state_is_distinct    : valor IS DISTINCT FROM valor state_aliases_table
                            | valor IS NOT DISTINCT FROM valor state_aliases_table'''

#=======================================================


# ESTADO PREDICATES
#=======================================================
def p_predicate_nulls(t) :
    '''state_predicate_nulls        : valor IS NULL
                                    | valor IS NOT NULL
                                    | valor ISNULL
                                    | valor NOTNULL'''

#=======================================================


# # Pattern Matching
# #=======================================================
def p_matchs(t) :
    '''state_pattern_match      : aritmetica LIKE CADENA'''

# #=======================================================


# ESTADOS PARA LOS ALIAS
# #=======================================================
# PARA LAS TABLAS
# -------------------------------------------------------
def p_aliases_table(t):
    ''' state_aliases_table     : AS ID
                                | ID'''


def p_aliases_table2(t):
    ' state_aliases_table     : '

# -------------------------------------------------------

# PARA LOS CAMPOS
# -------------------------------------------------------
def p_aliases_field(t):
    ''' state_aliases_field     : AS CADENA
                                | AS ID
                                | ID
                                '''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = t[2]

def p_aliases_field2(t):
    ' state_aliases_field     : '
    t[0] = ''
# -------------------------------------------------------
# #=======================================================


# CASE
#========================================================
def p_case_state(t):
    ''' case_state    : case_state auxcase_state END
                      | auxcase_state END'''

                      
def p_auxcase_state(t):
    'auxcase_state  : WHEN relacional THEN CADENA'


def p_auxcase_state2(t):
    'auxcase_state  : ELSE COMILLA_SIMPLE ID COMILLA_SIMPLE'

#========================================================

# FUNCIONES MATEMÁTICAS
def p_instrucciones_funcion_count(t):
    '''funciones_math_esenciales    : COUNT PARIZQ lista_funciones_math_esenciales PARDER parametro
                                    | COUNT PARIZQ lista_funciones_math_esenciales PARDER'''


def p_instrucciones_funcion_sum(t):
    '''funciones_math_esenciales    : SUM PARIZQ lista_funciones_math_esenciales PARDER parametro
                                    | SUM PARIZQ lista_funciones_math_esenciales PARDER'''


def p_instrucciones_funcion_avg(t):
    '''funciones_math_esenciales    : AVG PARIZQ lista_funciones_math_esenciales PARDER
                                    | AVG PARIZQ lista_funciones_math_esenciales PARDER parametro
                                    '''
    


def p_lista_instrucciones_funcion_math(t):
    '''lista_funciones_math_esenciales  : aritmetica
                                        | lista_id
                                        '''

    
def p_lista_instrucciones_funcion_math2(t):
    '''lista_funciones_math_esenciales  : POR'''
    

#SOLO ESTOS SE PUEDEN USAR EN EL WHERE
def p_instrucciones_funcion_abs_where(t) :
    'lista_funciones_where    : ABS PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_cbrt_where(t) :
    'lista_funciones_where    : CBRT PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)
    

def p_instrucciones_funcion_ceil_where(t) :
    'lista_funciones_where    : CEIL PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)
    

def p_instrucciones_funcion_cieling_where(t) :
    'lista_funciones_where    : CEILING PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)
    

#ESTOS SE USAN EN EL SELECT
def p_instrucciones_funcion_abs_select(t) :
    'lista_funciones    : ABS PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_cbrt_select(t) :
    'lista_funciones    : CBRT PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)
    

def p_instrucciones_funcion_ceil_select(t) :
    'lista_funciones    : CEIL PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)
    

def p_instrucciones_funcion_cieling_select(t) :
    'lista_funciones    : CEILING PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)
    

def p_instrucciones_funcion_degrees(t) :
    'lista_funciones    : DEGREES PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)
    

def p_instrucciones_funcion_div(t) :
    'lista_funciones    : DIV PARIZQ funcion_math_parametro COMA ENTERO PARDER'
    

def p_instrucciones_funcion_exp(t) :
    'lista_funciones    : EXP PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)
    

def p_instrucciones_funcion_factorial(t) :
    'lista_funciones    : FACTORIAL PARIZQ ENTERO PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)
    

def p_instrucciones_funcion_floor(t) :
    'lista_funciones    : FLOOR PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)
    

def p_instrucciones_funcion_gcd(t) :
    'lista_funciones    : GCD PARIZQ ENTERO COMA ENTERO PARDER'
    

def p_instrucciones_funcion_ln(t) :
    'lista_funciones    : LN PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)
    

def p_instrucciones_funcion_log(t) :
    'lista_funciones    : LOG PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)
    

def p_instrucciones_funcion_mod(t) :
    'lista_funciones    : MOD PARIZQ funcion_math_parametro COMA ENTERO PARDER'
    

def p_instrucciones_funcion_pi(t) :
    'lista_funciones    : PI PARIZQ PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), 1, t.lexer.lineno - 1)
    

def p_instrucciones_funcion_power(t) :
    'lista_funciones    : POWER PARIZQ funcion_math_parametro COMA ENTERO PARDER'
    

def p_instrucciones_funcion_radians(t) :
    'lista_funciones    : RADIANS PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)
    

def p_instrucciones_funcion_round(t) :
    'lista_funciones    : ROUND PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)
    

def p_instrucciones_funcion_sign(t) :
    'lista_funciones    : SIGN PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)
    

def p_instrucciones_funcion_sqrt(t) :
    'lista_funciones    : SQRT PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)
    

def p_instrucciones_funcion_width_bucket(t) :
    'lista_funciones    : WIDTH_BUCKET PARIZQ funcion_math_parametro COMA funcion_math_parametro COMA funcion_math_parametro COMA funcion_math_parametro PARDER'
    

def p_instrucciones_funcion_trunc(t) :
    'lista_funciones    : TRUNC PARIZQ funcion_math_parametro PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), t[3], t.lexer.lineno - 1)
    

def p_instrucciones_funcion_random(t) :
    'lista_funciones    : RANDOM PARIZQ PARDER'
    t[0] = FuncionMatematica1(t[1].upper(), 1, t.lexer.lineno - 1)


def p_instrucciones_funcion_math_parametro(t) :
    '''funcion_math_parametro   : ENTERO
                                | DECIMAL
                                '''
    t[0] = t[1]

def p_instrucciones_funcion_math_parametro_3(t) :
    '''funcion_math_parametro   : ID
                                '''
    t[0] = t[1].lower()

def p_instrucciones_funcion_math_parametro2(t) :
    '''funcion_math_parametro   : funcion_math_parametro_negativo'''
    t[0] = t[1]

def p_instrucciones_funcion_math_parametro_negativo(t) :
    '''funcion_math_parametro_negativo  : MENOS DECIMAL
                                        | MENOS ENTERO'''
    t[0] = 1 - float(t[2])
    

#========================================================

#========================================================
# FUNCIONES TRIGONOMÉTRICAS

#El unico valor que aceptan es double y devuelven un double
def p_instrucciones_funcion_trigonometrica_acos(t) :
    'fun_trigonometrica : ACOS PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_asin(t) :
    'fun_trigonometrica : ASIN PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_atan(t) :
    'fun_trigonometrica : ATAN PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_atan2(t) :
    'fun_trigonometrica : ATAN2 PARIZQ aritmetica COMA aritmetica PARDER'
    t[0] = FuncionTrigonometrica2(t[1].upper(), t[3], t[5], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_cos(t) :
    'fun_trigonometrica : COS PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_cot(t) :
    'fun_trigonometrica : COT PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_sin(t) :
    'fun_trigonometrica : SIN PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_tan(t) :
    'fun_trigonometrica : TAN PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_acosd(t) :
    'fun_trigonometrica : ACOSD PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_asind(t) :
    'fun_trigonometrica : ASIND PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_atand(t) :
    'fun_trigonometrica : ATAND PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_atan2d(t) :
    'fun_trigonometrica : ATAN2D PARIZQ aritmetica COMA aritmetica PARDER'
    t[0] = FuncionTrigonometrica2(t[1].upper(), t[3], t[5], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_cosd(t) :
    'fun_trigonometrica : COSD PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_cotd(t) :
    'fun_trigonometrica : COTD PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_sind(t) : 
    'fun_trigonometrica : SIND PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_tand(t) :
    'fun_trigonometrica : TAND PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_sinh(t) :
    'fun_trigonometrica : SINH PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_cosh(t) :
    'fun_trigonometrica : COSH PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_tanh(t) :
    'fun_trigonometrica : TANH PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_asinh(t) :
    'fun_trigonometrica : ASINH PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_acosh(t) :
    'fun_trigonometrica : ACOSH PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)

def p_instrucciones_funcion_trigonometrica_atanh(t) :
    'fun_trigonometrica : ATANH PARIZQ aritmetica PARDER'
    t[0] = FuncionTrigonometrica1(t[1].upper(), t[3], t.lexer.lineno - 1)
#========================================================

#========================================================
# BINARY STRING FUNCTIONS
def p_instrucciones_funcion_binary_string_length_select(t) :
    'fun_binario_select    : LENGTH PARIZQ valor PARDER'
    

def p_instrucciones_funcion_binary_string_length_where(t) :
    'fun_binario_where    : LENGTH PARIZQ valor PARDER'
    

def p_instrucciones_funcion_binary_string_substring_select(t) :
    'fun_binario_select    : SUBSTRING PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    


def p_instrucciones_funcion_binary_string_substring_insert(t) :
    'fun_binario_insert    : SUBSTRING PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    

def p_instrucciones_funcion_binary_string_substring_update(t) :
    'fun_binario_update    : SUBSTRING PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    


def p_instrucciones_funcion_binary_string_substring_where(t) :
    'fun_binario_where    : SUBSTRING PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    


def p_instrucciones_funcion_binary_string_trim_select(t) :
    'fun_binario_select    : TRIM PARIZQ CADENA FROM valor PARDER'
    


def p_instrucciones_funcion_binary_string_trim_insert(t) :
    'fun_binario_insert    : TRIM PARIZQ CADENA FROM valor PARDER'
    

    
def p_instrucciones_funcion_binary_string_trim_update(t) :
    'fun_binario_update    : TRIM PARIZQ CADENA FROM valor PARDER'
    


def p_instrucciones_funcion_binary_string_trim_where(t) :
    'fun_binario_where    : TRIM PARIZQ CADENA FROM valor PARDER'
    

def p_instrucciones_funcion_binary_string_md5_insert(t) :
    'fun_binario_insert : MD5 PARIZQ valor PARDER'
    


def p_instrucciones_funcion_binary_string_md5_update(t) :
    'fun_binario_update : MD5 PARIZQ valor PARDER'
    


def p_instrucciones_funcion_binary_string_sha256_select(t) :
    'fun_binario_select : SHA256 PARIZQ valor PARDER'
     


def p_instrucciones_funcion_binary_string_substr_select(t) :
    'fun_binario_select : SUBSTR PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    


def p_instrucciones_funcion_binary_string_substr_insert(t) :
    'fun_binario_insert : SUBSTR PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    


def p_instrucciones_funcion_binary_string_substr_update(t) :
    'fun_binario_update : SUBSTR PARIZQ valor COMA ENTERO COMA ENTERO PARDER'



def p_instrucciones_funcion_binary_string_substr_where(t) :
    'fun_binario_where : SUBSTR PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    


def p_instrucciones_funcion_binary_string_get_byte(t) :
    'fun_binario_select : GET_BYTE PARIZQ valor DOS_PUNTOS DOS_PUNTOS BYTEA COMA ENTERO PARDER'
    


def p_instrucciones_funcion_binary_string_get_byte2(t) :
    'fun_binario_select : GET_BYTE PARIZQ valor COMA ENTERO PARDER'
    


def p_instrucciones_funcion_binary_string_set_byte(t) :
    'fun_binario_select : SET_BYTE PARIZQ valor DOS_PUNTOS DOS_PUNTOS BYTEA COMA ENTERO COMA ENTERO PARDER'
    


def p_instrucciones_funcion_binary_string_set_byte2(t) :
    'fun_binario_select : SET_BYTE PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    


def p_instrucciones_funcion_binary_string_Convert(t) :
    'fun_binario_select : CONVERT PARIZQ valor AS tipos PARDER'
    


def p_instrucciones_funcion_binary_string_encode(t) :
    'fun_binario_select : ENCODE PARIZQ valor DOS_PUNTOS DOS_PUNTOS BYTEA COMA CADENA PARDER'
    


def p_instrucciones_funcion_binary_string_encode2(t) :
    'fun_binario_select : ENCODE PARIZQ valor COMA CADENA PARDER'



def p_instrucciones_funcion_binary_string_decode(t) :
    'fun_binario_select : DECODE PARIZQ valor COMA CADENA PARDER'
    


#========================================================

def p_error(t):
    if t == None:
        error = Error('Sintáctcio', "Problema con el final del texto a analizar", 404)
        tabla_errores.agregar(error)
        print(error.imprimir())
    else:
        error = Error('Sintáctico', "No se esperaba el caracter '%s'" %t.value, t.lexer.lineno - 1)
        tabla_errores.agregar(error)
        print(error.imprimir())

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    retorno = parser.parse(input)
    #dot.view()
    return retorno
