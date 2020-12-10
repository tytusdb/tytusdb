# Construyendo el analizador léxico
import ply.lex as lex
from lex import *
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
                        | USE cambio_bd
                        | SELECT selects
                        | DELETE deletes
                        | ALTER alter_table PTCOMA
                        | UPDATE update_table PTCOMA
                        | INSERT insercion
                        | DROP dropear'''
    t[0] = t[2]

# INSTRUCCION CON "CREATE"
def p_instruccion_creacion(t) :
    '''creacion     : DATABASE crear_bd
                    | TABLE crear_tb
                    | TYPE crear_type'''
    print("Creacion")

def p_instruccion_crear_BD(t) :
    'crear_bd     : ID PTCOMA'
    t[0] = Crear_BD(t[1])
    print("Creacion de BD")

def p_instruccion_crear_BD_Parametros(t) :
    'crear_bd     : ID lista_parametros_bd PTCOMA'
    #t[0] = Crear_BD_Parametros(t[1])
    print('Creacion de BD parametros')

def p_instruccion_crear_BD_if_exists(t) :
    'crear_bd       : IF NOT EXISTS ID PTCOMA'
    print('Creacion de BD if not exists')

def p_instruccion_crear_BD_if_exists_Parametros(t) :
    'crear_bd       : IF NOT EXISTS ID lista_parametros_bd PTCOMA'
    print('Creacion de BD parametros if not exist')

def p_instruccion_crear_TB_herencia(t):
    '''crear_tb     : ID PARIZQ crear_tb_columnas PARDER tb_herencia PTCOMA
                    | ID PARIZQ crear_tb_columnas PARDER tb_herencia'''
    print("Creación de Tabla con herencia")
    #t[0] = Crear_TB_Herencia(t[1], t[3], t[5])|||

def p_instruccion_crear_TB(t):
    '''crear_tb     : ID PARIZQ crear_tb_columnas PARDER PTCOMA
                    | ID PARIZQ crear_tb_columnas PARDER'''
    print("Creación de tabla sin herencia")
    #t[0] = Crear_TB(t[1], t[3])

def p_isntruccion_crear_TYPE(t) :
    '''crear_type   : ID AS ENUM PARIZQ lista_objetos PARDER PTCOMA
                    | ID AS ENUM PARIZQ lista_objetos PARDER'''
    print("Creacion de un type enumerado")
    #t[0] = Crear_Type(t[1], t[5])

def p_instruccion_TB_herencia(t) :
    'tb_herencia    : INHERITS PARIZQ ID PARDER'
    #t[0] = Heredero(t[4])

# INSTRUCCION CON "USE"
def p_instruccion_Use_BD(t) :
    'cambio_bd     : ID PTCOMA'
    t[0] = Cambio_BD(t[1])
    print("CAMBIO de BD")


# INSTRUCCIONES CON "SELECT"
def p_instruccion_selects(t) :
    '''selects      : POR FROM select_all 
                    | lista_parametros FROM lista_parametros inicio_condicional '''
    # print("selects")

def p_instruccion_selects_distinct(t) :
    '''selects      : DISTINCT POR FROM select_all 
                    | DISTINCT lista_parametros FROM lista_parametros inicio_condicional '''
    # print("selects")

def p_instruccion_selects_where(t) :
    'inicio_condicional      : WHERE lista_condiciones inicio_group_by'
    # print("Condiciones (Where)")

def p_instruccion_selects_sin_where(t) :
    'inicio_condicional      : inicio_group_by'
    # print("Condiciones (Where)")

# def p_instruccion_selects_where2(t) :
#     'inicio_condicional      : WHERE lista_condiciones inicio_group_by PTCOMA'
#     print("Condiciones (Where)")

def p_instruccion_selects_group_by(t) :
    'inicio_group_by      : GROUP BY lista_parametros inicio_having'
    # print("GROUP BY")

def p_instruccion_selects_group_by2(t) :
    'inicio_group_by      : inicio_having '
    # print("NO HAY GROUP BY")

def p_instruccion_selects_having(t) :
    'inicio_having     : HAVING lista_condiciones inicio_order_by'
    # print("HAVING")

def p_instruccion_selects_having2(t) :
    'inicio_having      : inicio_order_by '
    # print("NO HAY HAVING")

def p_instruccion_selects_order_by(t) :
    '''inicio_order_by      : ORDER BY lista_parametros state_union
                            | ORDER BY lista_parametros state_intersect
                            | ORDER BY lista_parametros state_except'''
    # print("ORDER BY")

def p_instruccion_selects_order_by2(t) :
    '''inicio_order_by      : state_union 
                            | state_intersect
                            | state_except'''
    # print("NO HAY ORDER BY")
    
def p_instruccion_selects_union(t) :
    '''state_union      : UNION SELECT selects
                        | UNION ALL SELECT selects'''
    
def p_instruccion_selects_union2(t) :
    'state_union      : PTCOMA'
    
def p_instruccion_selects_intersect(t) :
    '''state_intersect      : INTERSECT SELECT selects
                            | INTERSECT ALL SELECT selects'''
    
def p_instruccion_selects_intersect2(t) :
    'state_intersect      : PTCOMA'
    
def p_instruccion_selects_except(t) :
    '''state_except     : EXCEPT SELECT selects
                        | EXCEPT ALL SELECT selects'''
    
def p_instruccion_selects_except2(t) :
    'state_except      : PTCOMA'


def p_instruccion_Select_All(t) :
    'select_all     : ID inicio_condicional'
    t[0] = Select_All(t[1])
    # print("Consulta ALL para tabla: " + t[1])
    
#========================================================
# INSERT INTO TABLAS
def p_instruccion_Insert_columnas(t) :
    '''insercion    : INTO ID PARIZQ lista_id PARDER VALUES PARIZQ lista_insercion PARDER PTCOMA
                    | INTO ID PARIZQ lista_id PARDER VALUES PARIZQ lista_insercion PARDER'''
    print('Insert con columnas')
    #t[0] = Insert(t[2], t[4], t[8])
    #if len(t[4]) != len(t[8]):
        #print('Error, no está insertando la misma cantidad de datos que de columnas')
    #else:
        #print('Insertó')

def p_instruccion_insert(t) :
    '''insercion    : INTO ID VALUES PARIZQ lista_insercion PARDER PTCOMA
                    | INTO ID VALUES PARIZQ lista_insercion PARDER'''
    print('Insert sin columnas')

#========================================================

#========================================================
# DROP BASES DE DATOS Y TABLAS
def p_instruccion_Drop_BD_exists(t) :
    '''dropear      : DATABASE IF EXISTS ID PTCOMA
                    | DATABASE IF EXISTS ID'''
    #t[0] = DropBaseExiste(t[4])

def p_instruccion_Drop_BD(t) :
    '''dropear      : DATABASE ID PTCOMA
                    | DATABASE ID'''
    #t[0] = DropBase(t[2])

def p_instruccion_Drop_TB(t) :
    '''dropear      : TABLE ID PTCOMA
                    | TABLE ID'''
    #T[0] = DropTabla(t[2])

#========================================================

#========================================================
# PARAMETROS PARA CREATE BASE DE DATOS
def p_instrucciones_parametros_BD_owner(t) :
    'lista_parametros_bd    : OWNER IGUAL ID'

def p_instrucciones_parametros_BD_Mode(t) :
    'lista_parametros_bd    : MODE IGUAL ENTERO'

def p_instrucciones_parametros_BD_Mode_owner(t) :
    'lista_parametros_bd    : OWNER IGUAL ID MODE IGUAL ENTERO'

def p_instrucciones_parametros_BD_owner_Mode(t) :
    'lista_parametros_bd    : MODE IGUAL ENTERO OWNER IGUAL ID'

#========================================================

#========================================================
# LISTA DE PARAMETROS
def p_instrucciones_lista_parametros(t) :
    'lista_parametros    : lista_parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]
    # print("Varios parametros")

def p_instrucciones_parametro(t) :
    'lista_parametros    : parametro '
    t[0] = [t[1]]
    # print("Un parametro")

def p_parametro_con_tabla(t) :
    'parametro        : ID PUNTO name_column'
    t[0] = t[1]
    # print("Parametro con indice de tabla")

def p_parametro_con_tabla_columna(t) :
    'name_column        : ID'
    t[0] = t[1]
    # print("Nombre de la columna")

def p_parametro_sin_tabla(t) :
    'parametro        : ID'
    t[0] = t[1]
    # print("Parametro SIN indice de tabla")
#========================================================

#========================================================
# CONTENIDO DE TABLAS EN CREATE TABLE
def p_instrucciones_lista_columnas(t) :
    'crear_tb_columnas      : crear_tb_columnas COMA crear_tb_columna'
    #t[1].append(t[3])
    #t[0] = t[1]

def p_instrucciones_columnas(t) :
    'crear_tb_columnas      : crear_tb_columna'
    #t[0] = [t[1]]

def p_instrucciones_columna_parametros(t) :
    'crear_tb_columna       : ID tipos parametros_columna'
    #t[0] = Nueva_Columna_Param(t[1], t[2], t[3])

def p_instrucciones_columna_noparam(t) :
    'crear_tb_columna       : ID tipos'
    #t[0] = Nueva_Columna(t[1], t[2])

def p_instrucciones_columna_pk(t) :
    'crear_tb_columna       : PRIMARY KEY PARIZQ lista_id PARDER'
    #t[0] = LlavesPrimarias(t[4])

def p_instrucciones_columna_fk(t) :
    'crear_tb_columna       : FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER'
    #t[0] = Llaves Foraneas(t[4], t[7], t[9])
    if len(t[4]) != len(t[9]):
        print('Error el número de columnas referencias es distinto al número de columnas foraneas')
    else:
        print('Se creó referencia de llave foranea')

def p_instrucciones_lista_params_columnas(t) :
    'parametros_columna     : parametros_columna parametro_columna'
    #t[1].append(t[2])
    #t[0] = t[1]

def p_instrucciones_params_columnas(t) :
    'parametros_columna     : parametro_columna'
    #t[0] = [t[1]]

def p_instrucciones_parametro_columna_nul(t) :
    'parametro_columna      : unul'
    #t[0] = t[1]

def p_instrucciones_parametro_columna_pkey(t) :
    'parametro_columna      : PRIMARY KEY'
    #t[0] = Parametro('PRIMARY KEY')

def p_instrucciones_parametro_columna_auto_increment(t) :
    'parametro_columna      : AUTO_INCREMENT'
    #t[0] = Parametro('AUTO_INCREMENT')

def p_instrucciones_nnul(t) :
    'unul   : NOT NULL'
    #t[0] = Parametro('NOT NULL')

def p_instrucciones_unul(t) :
    'unul   : NULL'
    #t[0] = Parametros('NULL')

#========================================================

#========================================================
# LISTA DE ELEMENTOS REUTILIZABLES
def p_instrucciones_lista_ids(t) :
    'lista_id   : lista_id COMA ID'
    t[1].append(t[3])
    t[0] = t[1]

def p_instrucciones_lista_id(t) :
    'lista_id   : ID'
    t[0] = [t[1]]

def p_instrucciones_lista_objetos(t) :
    'lista_objetos  : lista_objetos COMA objeto'
    #t[1].append(t[3])
    #t[0] = t[1]

def p_instrucciones_lista_objeto(t) :
    'lista_objetos  : objeto'
    #t[0] = [t[1]]

def p_instrucciones_objeto(t) :
    '''objeto       : DECIMAL
                    | ENTERO
                    | CADENA'''
    #t[0] = t[1]

def p_instrucciones_lista_insercion_objeto(t) :
    '''lista_insercion  : lista_insercion COMA objeto'''
    #para objetos simples

def p_instrucciones_lista_insercion_select(t) :
    'lista_insercion  : lista_insercion COMA PARIZQ SELECT selects PARDER'
    #para cuando haya querys select

def p_instrucciones_insercion_objeto(t) :
    '''lista_insercion  : objeto'''
    #para un objeto simple

def p_instrucciones_insercion_select(t) :
    'lista_insercion  : PARIZQ SELECT selects PARDER'
    #Para un query select

#========================================================

#========================================================
# LISTA DE CONDICIONES
def p_instrucciones_lista_condiciones_AND(t) :
    'lista_condiciones    : lista_condiciones AND condicion'
    t[1].append(t[3])
    t[0] = t[1]
    # print("condicion con  AND")
    
def p_instrucciones_lista_condiciones_OR(t) :
    'lista_condiciones    : lista_condiciones OR condicion'
    t[1].append(t[3])
    t[0] = t[1]
    # print("condicion con OR")
    
def p_instrucciones_lista_condiciones_NOT(t) :
    'lista_condiciones    : NOT lista_condiciones'
    t[1].append(t[3])
    t[0] = t[1]
    # print("condicion con NOT")

def p_instrucciones_condiciones(t) :
    'lista_condiciones    : condicion '
    t[0] = [t[1]]
    # print("Una condicion")

def p_parametro_con_tabl_2(t) :
    'condicion        : def_condicion signo_relacional ID PUNTO name_column '
    t[0] = t[1]
    # print("Condicion con indice de tabla")

def p_def_condicion(t) :
    '''def_condicion    : ID PUNTO ID
                        | ID'''

def p_parametro_signo_relacional(t) :
    '''signo_relacional         : IGUAL IGUAL
                                | MAYOR
                                | MENOR
                                | MENORIGUAL
                                | MAYORIGUAL
                                | DIFERENTE'''
    t[0] = t[1]

    if t[1] == '>':
        print("Condicion de tipo MAYOR")
    elif t[1] == '<':
        print("Condicion de tipo MENOR")
    elif t[1] == '<=':
        print("Condicion de tipo MENOR IGUAL")
    elif t[1] == '>=':
        print("Condicion de tipo MAYOR IGUAL")
    elif t[1] == '<>':
        print("Condicion de tipo DIFERENTE")
    else:
        print("Condicion de tipo IGUALACION")

def p_parametro_sin_tabla_2(t) :
    'condicion        : ID signo_relacional ID'
    t[0] = t[1]
    # print("Condicion SIN indice de tabla")

#========================================================

# INSTRUCCION CON "DELETE"
def p_instruccion_delete(t) :
    '''deletes      : delete_condicional
                    | delete_incondicional'''
    print("ELIMINACION")

def p_instruccion_delete_incondicional(t) :
    'delete_incondicional     : ID PTCOMA'
    t[0] = Delete_incondicional(t[1])
    print("Eliminar tabla: " + t[1])

def p_instruccion_delete_condicional(t) :
    'delete_condicional     : ID WHERE lista_condiciones PTCOMA'
    # t[0] = Delete_incondicional(t[1])
    print("Eliminar tabla: " + t[1])

# INSTRUCCION ALTER TABLE
def p_instruccion_alter(t) :
    '''alter_table  : TABLE ID def_alter'''
    print("ALTER TABLE")

def p_def_alter(t) :
    '''def_alter    : ADD COLUMN ID tipos
                    | DROP COLUMN ID
                    | ADD CHECK PARIZQ relacional PARDER
                    | ADD CONSTRAINT ID UNIQUE PARIZQ ID PARDER
                    | ADD FOREIGN KEY PARIZQ lista_parametros PARDER REFERENCES PARIZQ lista_parametros PARDER
                    | ALTER COLUMN ID SET NOT NULL
                    | DROP CONSTRAINT ID
                    | RENAME COLUMN ID TO ID'''

def p_tipos(t) :
    '''tipos        : SMALLINT
                    | INTEGER
                    | BIGINT
                    | R_DECIMAL
                    | NUMERIC
                    | REAL
                    | DOUBLE PRECISION
                    | MONEY
                    | CHARACTER VARYING PARIZQ ENTERO PARDER
                    | VARCHAR PARIZQ ENTERO PARDER
                    | CHARACTER PARIZQ ENTERO PARDER
                    | CHAR PARIZQ ENTERO PARDER
                    | TEXT
                    | TIMESTAMP def_dt_types
                    | DATE
                    | TIME def_dt_types
                    | INTERVAL def_interval
                    | BOOLEAN'''

def p_def_dt_types(t) :
    '''def_dt_types : def_dt_types WITHOUT TIME ZONE
                    | def_dt_types WITH TIME ZONE
                    | WITHOUT TIME ZONE
                    | WITH TIME ZONE
                    | PARIZQ ENTERO PARDER'''

def p_def_interval(t) :
    '''def_interval : def_interval PARIZQ ENTERO PARDER
                    | def_fld_to
                    | PARIZQ ENTERO PARDER'''

def p_def_fld_to(t) :
    '''def_fld_to   : def_fields TO def_fields
                    | def_fields'''

def p_def_fields(t) :
    '''def_fields   : YEAR
                    | MONTH
                    | DAY
                    | HOUR
                    | MINUTE
                    | SECOND'''

def p_relacional(t) :
    '''relacional   : aritmetica MENOR aritmetica
                    | aritmetica MAYOR aritmetica
                    | aritmetica IGUAL aritmetica
                    | aritmetica MENORIGUAL aritmetica
                    | aritmetica MAYORIGUAL aritmetica
                    | aritmetica DIFERENTE aritmetica
                    | aritmetica'''

def p_aritmetica(t) :
    '''aritmetica   : valor MAS valor
                    | valor MENOS valor
                    | valor POR valor
                    | valor DIVISION valor
                    | valor MODULO valor
                    | valor EXP valor
                    | valor'''

def p_valor(t) :
    '''valor        : ID
                    | ENTERO
                    | DECIMAL
                    | CADENA'''

def p_instruccion_update_where(t) :
    '''update_table : ID SET def_update WHERE lista_condiciones'''
    print("UPDATE TABLE")

def p_instruccion_update(t) :
    '''update_table : ID SET def_update'''
    print("UPDATE TABLE")

def p_def_update_rec(t) :
    '''def_update   : def_update COMA ID IGUAL valor'''

def p_def_update(t) :
    '''def_update   : ID IGUAL valor'''

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t)

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    return parser.parse(input)
