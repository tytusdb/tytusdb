#PARSER
from ply import *
import lexico

tokens = lexico.tokens

precedence = (
    ('left', 'mas', 'menos'),
    ('left', 'por', 'div')
    #erlacionales y logicos
)


def p_inicio(p):
'''inicio : instrucciones'''

def p_instrucciones(p):
'''instrucciones : instruccion instrucciones_cont'''

def p_instrucciones_cont(p):
'''instrucciones_cont: instruccion instrucciones_cont
                    |empty'''

def p_empty(p):
    'empty :'
    pass

def p_instruccion(p):
'''instruccion : ddl
            | dml'''

def p_ddl(p):
'''ddl : sentencia_create
    | sentencia_alter
    | sentencia_drop
    | sentencia_truncate'''

def p_dml(p):
'''dml : sentencia_insert
    | sentencia_update
    | sentencia_delete
    | sentencia_select
    | sentencia_show'''

#----------DDL----------
#CREAR
def p_crear(p):
'''sentencia_create : create create_cont
                    | replace create_cont'''

def p_create_cont(p):
'''create_cont : database if_not pyc
		    | table if_not par1 col_tabla par2 fin_tabla
		    | type valor as enum par1 p_lista_insertar par2 pyc'''

def p_inherits
'''fin_tabla : inherits par1 identificador par2 pyc
		  | pyc'''

def p_if_not(p):
'''if_not: if not exist cadena
	      | cadena'''

def p_col_tabla(p):
'''col_tabla : cadena tipo propiedades coma col_tabla_cont
            | foreing key lista_id references identificador coma col_tabla_cont'''

def p_col_tabla_cont(p):
'''col_tabla_cont: cadena tipo propiedades col_tabla_cont
            | primary key lista_id col_tabla_cont
            |empty '''

def p_propiedades(p):
'''propiedades : null propiedades
            | not null proiedades
            | identity propiedades
            | primary key propiedades 
            | null
            | not null
            | identity
            | primary key'''

def p_tipo(p):
'''tipo : smallint
	 | integer
	 | bigint
	 | decimal
	 | numeric
	 | real
	 | double
	 | money
	 | character
	 | varying par1 num par2
	 | varchar par1 num par2
	 | character par1 num par2
	 | char par1 num par2
	 | text
	 | date
	 | boolean
	 | int'''

#ALTER
def p_alter(p):
'''sentencia_alter : alter table identificador alter_cont pyc'''

def p_alter_cont(p):
'''alter_cont : add identificador tipo
		   | drop identificador'''

#DROP
def p_drop(p):
'''sentencia_drop : drop objeto if_exist pyc'''

def p_if_exist(p):
'''if_exist : if exist identificador
			 | identificador'''

def p_objeto(p):
'''objeto : table
	   | database'''

#TRUNCATE
def p_truncate(p):
'''sentencia_truncate : truncate table identificador pyc'''

#----------DML----------
#INSERT
def p_insert(p):
'''sentencia_insert : insert into identificador insert_cont pyc'''

def p_insert_cont(p):
'''insert_cont : values par1 lista_insertar par2
			| par1 lista_campos par2 values par1 lista_insertar par2'''

def p_lista_campos(p):
'''lista_campos	: identificador lista_camposP'''

def p_lista_camposP(p):
'''lista_camposP : coma identificador lista_camposP
                |empty'''

def p_valor(p):
'''valor : num
      | cadena
      | decimal
      | identificador'''

def p_lista_insertar(p):
'''lista_insertar	: valor lista_insertarP'''


def p_lista_insertarP(p):
	'''lista_insertarP : coma valor lista_insertarP
	                    |empty'''

#UPDATE
def p_update(p):
'''sentencia_update : update  identificador set identificador igual valor condicion'''

#DELETE
def p_delete(p):
'''sentencia_delete : delete from delete_cont condicion'''

def p_delete_cont(p):
'''delete_cont : only identificador
			| only identificador por
			| identificador por
			| identificador'''

#SELECT
def p_select(p):
'''sentencia_select : select select_cont from lista_from condicion'''


def p_order(p):
'''order_by : order by identificador opcion_order condicion_cont
		 | condicion_cont'''

def p_opcion_order(p):
'''opcion_order : asc
			 | desc'''

def p_condicion_cont(p):
'''condicion_cont : where operacion_logica
			   | where operacion_logica group by identificador
		       | group by identificador
		       | group by identificador having operacion_logica'''

def p_fin_select(p):
'''fin select : order_by identificador opcion_order pyc
		        | pyc'''


def p_lista_from(p):
'''lista_from : identificador coma lista_fromP
				| identificador as identificador coma lista_fromP
                | hacer_join lista_fromP'''

def p_lista_fromP(p):
	'''lista_fromP : identificador lista_fromP
					| identificador as identificador lista_fromP
					|empty'''
def p_tipo_join(p):
'''tipo_join : inner
			 | left
			 | right
			 | full
			 | outer'''

def p_hacer_join(p):
'''hacer_join : identificador tipo_join join identificador on operacion_logica
 		   | identificador tipo_join join identificador'''

def p_select_cont(p):
'''select_cont : por
			| lista_id'''

def p_lista_id(p):
'''lista_id : identificador lista_idP
			| identificador punto identificador lista_idP'''

def p_lista_idP(p):
	'''lista_idP : coma identificador lista_idP
				| coma identificador as identificador lista_idP
				|empty'''

def p_condicion(p):
'''condicion : pyc
		  | where operacion_logica'''

def p_op_logica(p):
    '''operacion_logica : operacion_relacional operacion_logicaP'''

def p_op_logicaP(p):
    '''operacion_logicaP: and operacion_relacional operacion_logicaP
                        | or operacion_relacional operacion_logicaP
                        | not operacion_relacional operacion_logicaP'''

def p_op_logicaP2(p):
    '''operacion_logicaP : '''

def p_operacion_relacional(p):
    '''operacion_relacional : operacion_aritmetica operacion_relacionalP'''

def p_operacion_relacionalP(p):
    '''operacion_relacionalP : mayor operacion_aritmetica operacion_relacionalP
                                | menor operacion_aritmetica operacion_relacionalP
                                | mayorigual operacion_aritmetica operacion_relacionalP
                                | menorigual operacion_aritmetica operacion_relacionalP
                                | diferente operacion_aritmetica operacion_relacionalP
                                | igual operacion_aritmetica operacion_relacionalP'''

def p_operacion_relacionalP2(p):
    '''p_operacion_relacionalP : '''

def p_operacion_aritmetica(p):
    '''operacion_aritmetica : valor operacion_aritmeticaP'''

def p_operacion_aritmetica2(p):
    '''operacion_aritmetica : par1 operacion_logica par2 '''

def p_operacion_aritmeticaP(p):
    '''operacion_aritmeticaP : mas valor
                                | menos valor
                                | por valor
                                | div valor '''

def p_operacion_aritmeticaP2(p):
    '''operacion_aritmeticaP : '''

def p_error(p):
    if not p:
        print("SYNTAX ERROR AT EOF")

bparser = yacc.yacc()

def parse(data, debug=0):
    bparser.error = 0
    p = bparser.parse(data, debug=debug)
    if bparser.error:
        return None
    return p
