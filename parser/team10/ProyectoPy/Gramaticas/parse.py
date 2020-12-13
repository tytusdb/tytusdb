#PARSER
import ply.yacc as yacc
import lexico
from Gramaticas import ReporteErrores


tokens = lexico.tokens

precedence = (
    ('left', 'mas', 'menos'),
    ('left', 'por', 'div'),
    ('nonassoc','between', 'like'),
    ('left', 'menor', 'mayor', 'igual', 'menorigual', 'mayorigual', 'diferente'),
    ('right', 'not'),
    ('left', 'and'),
    ('left', 'or')
)


def p_inicio(p):
		'''inicio : instrucciones'''
		print('Termina inicio')

def p_instrucciones(p):
		'''instrucciones : instrucciones NEWLINE instruccion
					     | instruccion'''
		#if str(p[1]) == "instrucciones" : print('******* dos instrucciones en el else')

def p_instruccion(p):
		'''instruccion : ddl
		            | dml'''
		print('El valor de la expresión es: ' + str(p[1]))

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
				    | type valor as enum par1 lista_insertar par2 pyc'''

def p_inherits(p):
		'''fin_tabla : inherits par1 identificador par2 pyc
				  | pyc'''
def p_if_not(p):

		'''if_not : if not exists identificador
			      | identificador
			      | if not exists identificador owner igual valor
			      | identificador owner valor
			      | if not exists identificador mode igual valor
			      | identificador mode igual valor'''

def p_col_tabla(p):
		'''col_tabla : col_tabla coma identificador tipo propiedades
				  | col_tabla coma identificador tipo
				  | identificador tipo propiedades
				  | identificador tipo
				  | foreing key lista_id references identificador
				  | col_tabla coma primary key lista_id'''

def p_propiedades(p):
		'''propiedades : null propiedades
		            | not null propiedades
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
			 | int
			 | identificador'''

#ALTER
def p_alter(p):
		'''sentencia_alter : alter alter_objeto'''

def p_alter_objeto(p):
		'''alter_objeto : table identificador alter_cont pyc
						| database identificador rename to identificador pyc
						| database identificador owner to identificador pyc'''

def p_alter_cont(p):
		'''alter_cont : add con_add
				   | drop con_drop
				   | rename con_rename
				   | alter con_alter'''

def p_con_add(p):
		'''con_add : column identificador tipo
					| check  par1 valor diferente vacio par2
					| foreing key par1 identificador par2 references identificador'''	

def p_con_drop(p):
		'''con_drop : column identificador
				 | constraint identificador '''

def p_con_rename(p):
		'''con_rename : column identificador to identificador'''

def p_con_alter(p):
		'''con_alter : column identificador set not null'''

#DROP
def p_drop(p):
		'''sentencia_drop : drop objeto if_exist pyc'''

def p_if_exist(p) : 
		'''if_exist : if exists identificador
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
		'''lista_campos : lista_campos coma identificador
		 	  	 	 | identificador'''

def p_valor(p):
		'''valor : num
		      | cadena
		      | pdecimal
		      | identificador
		      | cadenacaracter
		      | substring par1 valor coma valor coma valor par2'''

def p_lista_insertar(p):
		'''lista_insertar : lista_insertar coma operacion_aritmetica
					   | operacion_aritmetica'''

#UPDATE
def p_update(p):
		'''sentencia_update : update  identificador set identificador igual operacion_aritmetica condicion'''

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
		'''sentencia_select : select opciones_fecha
							| select select_cont from lista_from condicion_cont'''

def p_order(p):
		'''order_by : order by identificador opcion_order order_by
				 | condicion_cont
				 | limit operacion_aritmetica order_by
				 | offset operacion_aritmetica order_by'''

def p_opcion_order(p):
		'''opcion_order : asc
					 | desc'''

def p_condicion_cont(p):
		'''condicion_cont : where operacion_logica fin_select
					   | where operacion_relacional fin_select
					   | where operacion_logica group by identificador fin_select
				       | group by lista_id fin_select
				       | group by lista_id having operacion_logica fin_select
				       | where exists par1 sentencia_select par2 fin_select
				       | where operacion_aritmetica in par1 sentencia_select par2 fin_select
				       | where operacion_aritmetica not in par1 sentencia_select par2 fin_select
				       | fin_select'''

def p_fin_select(p):
		'''fin_select : order_by
				        | pyc
				        | union sentencia_select
				        | intersect sentencia_select
				        | except sentencia_select'''

def p_lista_from(p):
		'''lista_from : lista_from coma identificador as identificador
				   | lista_from coma identificador
				   | identificador as identificador
				   | identificador
				   | hacer_join
				   | par1 sentencia_select par2 as identificador
				   | par1 sentencia_select par2'''

def p_tipo_join(p):
		'''tipo_join : join
					 | inner join
					 | left join
					 | right join
					 | full join
					 | outer join'''

def p_hacer_join(p):
		'''hacer_join : identificador tipo_join identificador on operacion_logica
		 		   | identificador tipo_join join identificador'''

def p_select_cont(p):
		'''select_cont : por
					| distinct lista_id
					| lista_id
					| sen_case'''

def p_sen_case(p):
		'''sen_case : case case_when'''

def p_case_when(p):
		'''case_when : when operacion_logica then operacion_aritmetica case_when
					  | end valor'''		

def p_lista_id(p):
		'''lista_id : lista_id coma operacion_aritmetica
			     | lista_id coma identificador punto identificador
			     | operacion_aritmetica
			     | identificador punto identificador
			     | substring par1 valor coma valor coma valor par2'''

def p_opciones_fecha(p):
		'''opciones_fecha : extract par1 tipo_date from timestamp valor par2 pyc
     					   | now par1 par2 pyc
     					   | date_part par1 valor coma interval valor par2 pyc
     					   | current_date pyc
     					   | current_time pyc
     					   | timestamp valor pyc'''

def p_tipo_date(p):
		'''tipo_date : year
					  | month
					  | day
					  | hour
					  | minute
					  | second'''

def p_condicion(p):
		'''condicion : pyc
				  | where operacion_logica pyc
				  | where identificador igual operacion_aritmetica pyc
				  | where exists par1 sentencia_select par2 pyc
				  | where operacion_aritmetica in par1 sentencia_select par2 pyc
				  | where operacion_aritmetica not in par1 sentencia_select par2 pyc'''

def p_op_aritmetica(p):
		'''operacion_aritmetica : operacion_aritmetica mas operacion_aritmetica
							 | operacion_aritmetica menos operacion_aritmetica
							 | operacion_aritmetica por operacion_aritmetica
							 | operacion_aritmetica div operacion_aritmetica
							 | par1 operacion_aritmetica par2
							 | valor
							 | sum par1 operacion_aritmetica par2
							 | avg par1 operacion_aritmetica par2
							 | max par1 operacion_aritmetica par2
							 | pi
							 | power par1 operacion_aritmetica par2
							 | sqrt par1 operacion_aritmetica par2
							 | valor between valor
							 | valor is distinct from valor
							 | valor is not distinct from valor
							 | valor is null
							 | valor is not null
							 | valor is true
							 | valor is not true
							 | valor is false
							 | valor is not false'''

def p_op_relacional(p):
		'''operacion_relacional : operacion_relacional mayor operacion_relacional
							 | operacion_relacional menor operacion_relacional
							 | operacion_relacional mayorigual operacion_relacional
		 					 | operacion_relacional menorigual operacion_relacional
							 | operacion_relacional diferente operacion_relacional
							 | operacion_relacional igual operacion_relacional
							 | operacion_aritmetica'''

def p_op_logica(p):
		'''operacion_logica : operacion_logica and operacion_logica
						 | operacion_logica or operacion_logica
						 | operacion_logica not operacion_logica
						 | operacion_relacional'''

def p_show(p):
		'''sentencia_show : show databases show_cont'''

def p_show_cont(p):
		'''show_cont : pyc
				     | ins_like pyc'''

def p_ins_like(p):
		'''ins_like : like porcentaje identificador porcentaje'''

def p_empty(p):
     'empty :'
     pass

def p_error(p):
    if p:
        ReporteErrores.esin.append("Syntax error. Msg 42601, line: " + str(p.lexer.lineno) + ", col: " + str(p.lexer.lexpos) + ", keyword: " + str(p.value))
        parser.errok()
    else:
        ReporteErrores.esin.append("SQL statement not yet complete")

#def parse(data, debug=0):
#    parser.error = 0
#    p = parser.parse(data, debug=debug)
#    if parser.error:
#        return None
#    return p

parser = yacc.yacc()


f = open("./entrada.txt", "r")
input = f.read()
print(input)
parser.parse(input)