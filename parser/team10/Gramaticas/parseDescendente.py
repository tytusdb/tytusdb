#PARSER
import ply.yacc as yacc
import lexico
import nodo as grammer
import graficas as generar

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


def p_inicio(t):
    '''inicio : instrucciones'''


def p_instrucciones(t):
    '''instrucciones : instruccion instrucciones_2'''


def p_instrucciones_2(t):
    '''instrucciones_2 : NEWLINE instruccion instrucciones_2
                        | empty'''


def p_instruccion(t):
    '''instruccion : ddl
                    | dml
                    | ins_use'''


def p_ddl(t):
    '''ddl : sentencia_create
            | sentencia_alter
            | sentencia_drop
            | sentencia_truncate'''


def p_dml(t):
    '''dml : sentencia_insert
            | sentencia_update
            | sentencia_delete
            | sentencia_select
            | sentencia_show'''


def p_ins_use(t):
    '''ins_use : use identificador'''

#----------DDL----------
#CREAR


def p_crear(t):
    '''sentencia_create : create create_cont
                        | replace create_cont'''


def p_create_cont(t):
    '''create_cont : database if_not pyc
                    | table if_not par1 col_tabla par2 fin_tabla
                    | type valor as enum par1 lista_insertar par2 pyc'''


def p_inherits(t):
    '''fin_tabla : inherits par1 identificador par2 pyc
                | pyc'''


def p_if_not(t):

    '''if_not : if not exists identificador
            | identificador
            | if not exists identificador owner igual valor
            | identificador owner valor
            | if not exists identificador mode igual valor
            | identificador mode igual valor'''


def p_col_tabla(t):
    '''col_tabla : identificador tipo propiedades col_tabla_2
                | identificador tipo col_tabla_2
                | foreing key lista_id references identificador col_tabla_2'''


def p_col_tabla_2(t):
    '''col_tabla_2 : coma identificador tipo propiedades col_tabla_2
                | coma identificador tipo col_tabla_2
                | coma primary key lista_id col_tabla_2
                | empty'''


def p_propiedades(t):
    '''propiedades : null propiedades
                    | not null propiedades
                    | identity propiedades
                    | primary key propiedades
                    | null
                    | not null
                    | identity
                    | primary key'''


def p_tipo(t):
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


def p_alter(t):
    '''sentencia_alter : alter alter_objeto'''


def p_alter_objeto(t):
    '''alter_objeto : table identificador alter_cont pyc
                    | database identificador rename to identificador pyc
                    | database identificador owner to identificador pyc'''


def p_alter_cont(t):
    '''alter_cont : add con_add
                | drop con_drop
                | rename con_rename
                | alter con_alter'''


def p_con_add(t):
    '''con_add : column identificador tipo
                | check  par1 valor diferente vacio par2
                | foreing key par1 identificador par2 references identificador'''


def p_con_drop(t):
    '''con_drop : column identificador
                | constraint identificador '''


def p_con_rename(t):
    '''con_rename : column identificador to identificador'''


def p_con_alter(t):
    '''con_alter : column identificador set not null'''

#DROP


def p_drop(t):
    '''sentencia_drop : drop objeto if_exist pyc'''


def p_if_exist(t):
    '''if_exist : if exists identificador
                | identificador'''


def p_objeto(t):
    '''objeto : table
            | database'''

#TRUNCATE


def p_truncate(t):
    '''sentencia_truncate : truncate table identificador pyc'''

#----------DML----------
#INSERT


def p_insert(t):
    '''sentencia_insert : insert into identificador insert_cont pyc'''


def p_insert_cont(t):
    '''insert_cont : values par1 lista_insertar par2
                    | par1 lista_campos par2 values par1 lista_insertar par2'''


def p_lista_campos(t):
    '''lista_campos :  identificador lista_campos_2'''


def p_lista_campos_2(t):
    '''lista_campos_2 : coma identificador lista_campos_2
                    | empty'''


def p_valor(t):
    '''valor : num
            | cadena
            | pdecimal
            | identificador
            | cadenacaracter
            | substring par1 valor coma valor coma valor par2'''


def p_lista_insertar(t):
    '''lista_insertar : operacion_aritmetica lista_insertar_2'''


def p_lista_insertar_2(t):
    '''lista_insertar_2 : coma operacion_aritmetica lista_insertar_2
                        | empty'''

#UPDATE


def p_update(t):
    '''sentencia_update : update  identificador set identificador igual operacion_aritmetica condicion'''

#DELETE


def p_delete(t):
    '''sentencia_delete : delete from delete_cont condicion'''


def p_delete_cont(t):
    '''delete_cont : only identificador
                    | only identificador por
                    | identificador por
                    | identificador'''

#SELECT


def p_select(t):
    '''sentencia_select : select opciones_fecha
                        | select select_cont from lista_from condicion_cont'''


def p_order(t):
    '''order_by : order by identificador opcion_order order_by
                | condicion_cont
                | limit operacion_aritmetica order_by
                | offset operacion_aritmetica order_by'''


def p_opcion_order(t):
    '''opcion_order : asc
                    | desc'''


def p_condicion_cont(t):
    '''condicion_cont : where operacion_logica fin_select
                    | where operacion_relacional fin_select
                    | where operacion_logica group by identificador fin_select
                    | group by lista_id fin_select
                    | group by lista_id having operacion_logica fin_select
                    | where exists par1 sentencia_select par2 fin_select
                    | where operacion_aritmetica in par1 sentencia_select par2 fin_select
                    | where operacion_aritmetica not in par1 sentencia_select par2 fin_select
                    | fin_select'''


def p_fin_select(t):
    '''fin_select : order_by
                | pyc
                | union sentencia_select
                | intersect sentencia_select
                | except sentencia_select'''


def p_lista_from(t):
    '''lista_from : identificador as identificador lista_from_2
                | identificador lista_from_2
                | hacer_join lista_from_2
                | par1 sentencia_select par2 as identificador lista_from_2
                | par1 sentencia_select par2 lista_from_2'''


def p_lista_from_2(t):
    '''lista_from_2 : coma identificador as identificador lista_from_2
                | coma identificador lista_from_2
                | empty'''


def p_tipo_join(t):
    '''tipo_join : inner
                | left
                | right
                | full
                | outer'''


def p_hacer_join(t):
    '''hacer_join : identificador tipo_join join identificador on operacion_logica
                | identificador tipo_join join identificador'''


def p_select_cont(t):
    '''select_cont : por
                    | distinct lista_id
                    | lista_id
                    | sen_case'''


def p_sen_case(t):
    '''sen_case : case case_when'''


def p_case_when(t):
    '''case_when : when operacion_logica then operacion_aritmetica case_when
                | end valor'''


def p_lista_id(t):
    '''lista_id : operacion_aritmetica lista_id_2
                | identificador punto identificador lista_id_2
                | substring par1 valor coma valor coma valor par2 lista_id_2'''


def p_lista_id_2(t):
    '''lista_id_2 : coma operacion_aritmetica lista_id_2
                | coma identificador punto identificador lista_id_2
                | empty'''


def p_opciones_fecha(t):
    '''opciones_fecha : extract par1 tipo_date from timestamp valor par2 pyc
                        | now par1 par2 pyc
                        | date_part par1 valor coma interval valor par2 pyc
                        | current_date pyc
                        | current_time pyc
                        | timestamp valor pyc'''


def p_tipo_date(t):
    '''tipo_date : year
                | month
                | day
                | hour
                | minute
                | second'''


def p_condicion(t):
    '''condicion : pyc
                | where operacion_logica pyc
                | where identificador igual operacion_aritmetica pyc
                | where exists par1 sentencia_select par2 pyc
                | where operacion_aritmetica in par1 sentencia_select par2 pyc
                | where operacion_aritmetica not in par1 sentencia_select par2 pyc'''


def p_op_aritmetica(t):
    '''operacion_aritmetica : par1 operacion_aritmetica par2 operacion_aritmetica_2
                            | valor operacion_aritmetica_2
                            | sum par1 operacion_aritmetica par2 operacion_aritmetica_2
                            | avg par1 operacion_aritmetica par2 operacion_aritmetica_2
                            | max par1 operacion_aritmetica par2 operacion_aritmetica_2
                            | pi operacion_aritmetica_2
                            | power par1 operacion_aritmetica par2 operacion_aritmetica_2
                            | sqrt par1 operacion_aritmetica par2 operacion_aritmetica_2
                            | valor between valor operacion_aritmetica_2
                            | valor is distinct from valor operacion_aritmetica_2
                            | valor is not distinct from valor operacion_aritmetica_2
                            | valor is null operacion_aritmetica_2
                            | valor is not null operacion_aritmetica_2
                            | valor is true operacion_aritmetica_2
                            | valor is not true operacion_aritmetica_2
                            | valor is false operacion_aritmetica_2
                            | valor is not false operacion_aritmetica_2
                            | funciones_extras operacion_aritmetica_2'''


def p_operacion_aritmetica_2(t):
    '''operacion_aritmetica_2 : mas operacion_aritmetica operacion_aritmetica_2
                            | menos operacion_aritmetica operacion_aritmetica_2
                            | por operacion_aritmetica operacion_aritmetica_2
                            | div operacion_aritmetica operacion_aritmetica_2
                            | empty'''


def p_funciones_extras(t):
	'''funciones_extras : math_functions
					 | trigonometricas
					 | binary_string'''


def p_math_funciones(t):
	'''math_functions : funciones_math1 par1 operacion_aritmetica par2
				   | funciones_math2 par1 operacion_aritmetica coma operacion_aritmetica par2
				   | width_bucket par1 operacion_aritmetica coma operacion_aritmetica coma operacion_aritmetica coma operacion_aritmetica par2
				   | random par1 par2'''


def p_funciones_math1(t):
	'''funciones_math1 : abs
	                | cbrt
	                | ceil
	                | celing
	                | degrees
	                | exp
	                | factorial
	                | floor
	                | ln
	                | log
	                | radians
	                | rount
	                | sign
	                | sqrt'''


def p_funciones_math2(t):
	'''funciones_math2 : div
	                | gcd
	                | mod
	                | rount'''


def p_trigonometricas(t):
	'''trigonometricas : funciones_tri par1 operacion_aritmetica par2'''


def p_funciones_tri(t):
	'''funciones_tri : acos
				  | acosd
	              | asin
				  | asind
				  | atan
				  | atand
				  | atan2
				  | cos
				  | cosd
				  | cot
			  	  | cotd
				  | sin
				  | sind
				  | tan
				  | tand
				  | sinh
				  | cosh
				  | tanh
				  | asinh
				  | acosh
				  | atanh'''


def p_binary_string(t):
	'''binary_string : funciones_string1 par1 par2
				  | funciones_string2 par1 operacion_aritmetica par2
				  | substr par1 operacion_aritmetica coma operacion_aritmetica coma operacion_aritmetica par2
				  | funciones_string3 par1 operacion_aritmetica dosp dosp bytea coma operacion_aritmetica par2
				  | set_byte par1 operacion_aritmetica dosp dosp bytea coma operacion_aritmetica coma operacion_aritmetica par2
				  | convert par1 operacion_aritmetica as operacion_aritmetica par2
				  | decode par1 operacion_aritmetica coma operacion_aritmetica par2'''


def p_funciones_string1(t):
	'''funciones_string1 : trim
				 | md5'''


def p_funciones_string2(t):
	'''funciones_string2 : length
                 | sha256'''


def p_funciones_string3(t):
	'''funciones_string3 : get_byte
				  | encode'''


def p_op_relacional(t):
    '''operacion_relacional : operacion_aritmetica operacion_relacional_2'''


def p_operacion_relacional_2(t):
    '''operacion_relacional_2 : mayor operacion_relacional operacion_relacional_2
                            | menor operacion_relacional operacion_relacional_2
                            | mayorigual operacion_relacional operacion_relacional_2
                            | menorigual operacion_relacional operacion_relacional_2
                            | diferente operacion_relacional operacion_relacional_2
                            | igual operacion_relacional operacion_relacional_2
                            | empty'''


def p_op_logica(t):
    '''operacion_logica : operacion_relacional operacion_logica_2'''


def p_operacion_logica_2(t):
    '''operacion_logica_2 : and operacion_logica operacion_logica_2
                        | or operacion_logica operacion_logica_2
                        | not operacion_logica operacion_logica_2
                        | empty'''


def p_show(t):
    '''sentencia_show : show databases show_cont'''


def p_show_cont(t):
    '''show_cont : pyc
                | ins_like pyc'''


def p_ins_like(t):
    '''ins_like : like porcentaje identificador porcentaje'''


def p_empty(t):
     'empty :'
     pass

# def p_error(t):
#    if t:
#        ReporteErrores.esin.append("Syntax error. Msg 42601, line: " + str(t.lexer.lineno) + ", col: " + str(t.lexer.lexpos) + ", keyword: " + str(t.value))
#        parser.errok()
#    else:
#        ReporteErrores.esin.append("SQL statement not yet complete")

#def parse(data, debug=0):
#    parser.error = 0
#    p = parser.parse(data, debug=debug)
#    if parser.error:
#        return None
#    return p

parser = yacc.yacc()


def ejecutar():
    f = open("entrada.txt", "r")
    input = f.read()
    print(input)
    parser.parse(input)
