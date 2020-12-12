#PARSER
import ply.yacc as yacc
import lexico
import nodos as grammer

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
        node = grammer.nodoDireccion('inicio')
        node.agregar(t[1])
        t[0] = node

def p_instrucciones(p):
		'''instrucciones : instrucciones NEWLINE instruccion'''
        #se genera el nodo del arbol
        node = grammer.nodoDireccion('instrucciones')
        node.agregar(t[1])
        node.agregar(t[3])
    
        t[0] =node


def p_instrucciones2(p):
        '''instrucciones : instruccion'''
        node = grammer.nodoDireccion('instrucciones')
        node.agregar(t[1])
        t[0]= node

def p_instruccion(p):
		'''instruccion : ddl
		            | dml'''
        node = grammer.nodoDireccion('instruccion')
        node.agregar(t[1])
        t[0]= node


def p_ddl(p):
		'''ddl : sentencia_create
		    | sentencia_alter
		    | sentencia_drop
		    | sentencia_truncate'''

        node = grammer.nodoDireccion('ddl')
        node.agregar(t[1])
        t[0] = node

def p_dml(p):
		'''dml : sentencia_insert
		    | sentencia_update
		    | sentencia_delete
		    | sentencia_select
		    | sentencia_show'''
        node = grammer.nodoDireccion('dml')
        node.agregar(t[1])
        t[0]= node

#----------DDL----------
#CREAR
def p_crear(p):
		'''sentencia_create : create create_cont
							| replace create_cont'''

        node = grammer.nodoDireccion('sentencia_Create')
        node1 = grammer.nodoDireccion(''+t[1])
        node.agregar(node1)
        node.agregar(t[2])
        t[0]= node


def p_create_cont(p):
		'''create_cont : database if_not pyc'''
        node = grammer.nodoDireccion('create_cont')
        node1 = grammer.nodoDireccion(''+t[1])
        node.agregar(node1)
        node.agregar(t[2])
        t[0]= node

def p_create_cont2(p):
        '''create_cont : table if_not par1 col_tabla par2 fin_tabla '''
        node = grammer.nodoDireccion('create_cont')
        node1 = grammer.nodoDireccion(''+t[1])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(t[4])
        node.agregar(t[6])
        t[0] = node

def p_create_cont3(p):
        '''create_cont : type valor as enum par1 lista_insertar par2 pyc'''
        node = grammer.nodoDireccion('create_cont')
        node1 = grammer.nodoDireccion(''+t[1])
        node.agregar(node1)
        node.agregar(t[2])
        node2 = grammer.nodoDireccion(' '+t[3])
        node3 = grammer.nodoDireccion(' '+t[4])
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(t[6])
        t[0]=node

def p_inherits(p):
		'''fin_tabla : inherits par1 identificador par2 pyc'''
        node = grammer.nodoDireccion('fin_tabla')
        node1 = grammer.nodoDireccion(''+t[1])
        node.agregar(node1)
        node.agregar(t[3])
        t[0] = node

def p_inherits2(p):
        '''fin_tabla : pyc'''
        node = grammer.nodoDireccion('fin_tabla')
        node1 = grammer.nodoDireccion(''+t[1])
        node.agregar(node1)
        t[0] = node

def p_if_not(p):
		'''if_not : if not exists identificadorr'''
        node = grammer.nodoDireccion('if_not')
        node1 = grammer.nodoDireccion(''+t[1])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar
def p_if_not2(p):
        '''if_not : identificador'''
        node =grammer.nodoDireccion('if_not')
        node1 =grammer.nodoDireccion('(ID)'+ t[1])
        node.agregar(node1)
        t[0]= node

def p_if_not3(p):
        '''if_not : if not exists identificador owner igual valor'''
        node =grammer.nodoDireccion('if_not')
        node1= grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node3 = grammer.nodoDireccion(t[3])
        node4= grammer.nodoDireccion('(ID) '+t[4])
        node5 = grammer.nodoDireccion(t[5])
        node6 = grammer.nodoDireccion(t[6])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(node5)
        node.agregar(node6)
        node.agregar(t[7])
        t[0]= node

def p_if_not4(p):
        '''if_not : identificador owner valor'''
        node =grammer.nodoDireccion('if_not')
        node1= grammer.nodoDireccion('(ID)'+t[1])
        node2 = grammer.nodoDireccion(t[2])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        t[0]= node
def p_if_not5(p):
        '''if_not : if not exists identificador mode igual valor'''
        node =grammer.nodoDireccion('if_not')
        node1= grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node3 = grammer.nodoDireccion(t[3])
        node4= grammer.nodoDireccion('(ID) '+t[4])
        node5 = grammer.nodoDireccion(t[5])
        node6 = grammer.nodoDireccion(t[6])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(node5)
        node.agregar(node6)
        node.agregar(t[7])
        t[0]= node

def p_if_not6(p):
        '''if_not : identificador mode igual valor'''
        node =grammer.nodoDireccion('if_not')
        node1= grammer.nodoDireccion('(ID) 't[1])
        node2 = grammer.nodoDireccion(t[2])
        node3 = grammer.nodoDireccion(t[3])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(t[4])
        t[0]= node

def p_col_tabla(p):
		'''col_tabla : col_tabla coma identificador tipo propiedades'''
        node =grammer.nodoDireccion('col_tabla')
        node.agregar(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node4= grammer.nodoDireccion('(ID) '+t[3])
        node.agregar(node2)
        node.agregar(node4)
        node.agregar(t[4])
        node.agregar(t[5])
        t[0]= node

def p_col_tabla2(p):
        '''col_tabla : col_tabla coma identificador tipo'''
        node =grammer.nodoDireccion('col_tabla')
        node.agregar(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node4= grammer.nodoDireccion('(ID) '+t[3])
        node.agregar(node2)
        node.agregar(node4)
        node.agregar(t[4])
        t[0]= node

def p_col_tabla3(p):
        '''col_tabla : identificador tipo propiedades'''
        node =grammer.nodoDireccion('col_tabla')       
        node2 = grammer.nodoDireccion(t[1]) 
        node.agregar(node2)
        node.agregar(t[2])
        node5 = grammer.nodoDireccion(t[3])
        node.agregar(node5)        
        t[0]= node
def p_col_tabla4(p):
        '''col_tabla : identificador tipo'''
        node =grammer.nodoDireccion('col_tabla')
        
        node2 = grammer.nodoDireccion(t[1])
        node.agregar(node2)
        node.agregar(t[2])
        t[0]= node

def p_col_tabla5(p):
        '''col_tabla : foreing key lista_id references identificador'''
        node =grammer.nodoDireccion('col_tabla')
        node1= grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node4= grammer.nodoDireccion(t[4])
        node5 = grammer.nodoDireccion(t[5])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        node.agregar(node4)
        node.agregar(node5)
        t[0]= node
        

def p_col_tabla6(p):
        '''col_tabla : col_tabla coma primary key lista_id'''
        node =grammer.nodoDireccion('col_tabla')
        node2 = grammer.nodoDireccion(t[2])
        node3 = grammer.nodoDireccion(t[3])
        node4= grammer.nodoDireccion(t[4])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(t[5])
        t[0]= node

def p_propiedades(p):
		'''propiedades : null propiedades'''
        node = grammer.nodoDireccion('propiedades')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        node.agregar(t[2])
        t[0] = node

def p_propiedades2(p):
        '''propiedades : not null propiedades'''
        node = grammer.nodoDireccion('propiedades')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        t[0] = node
def p_propiedades3(p):
        '''propiedades : identity propiedades'''
        node = grammer.nodoDireccion('propiedades')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        node.agregar(t[2])
        t[0] = node
def p_propiedades4(p):
        '''propiedades : primary key propiedades '''
        node = grammer.nodoDireccion('propiedades')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        t[0] = node
def p_propiedades5(p):
        '''propiedades : null'''
        node = grammer.nodoDireccion('propiedades')
        node1 = grammer.nodoDireccion(t[1])
        
        node.agregar(node1)
        t[0] = node
def p_propiedades6(p):
        '''propiedades : not null'''
        node = grammer.nodoDireccion('propiedades')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node.agregar(node1)
        node.agregar(node2)
        t[0] = node
def p_propiedades7(p):
        '''propiedades : identity'''
        node = grammer.nodoDireccion('propiedades')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        t[0] = node
def p_propiedades8(p):
        '''propiedades : primary key'''
        node = grammer.nodoDireccion('propiedades')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node.agregar(node1)
        node.agregar(node2)
        t[0] = node
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
			 | text
			 | date
			 | boolean
			 | int
			 | identificador'''
        node = grammer.nodoDireccion('tipo')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        t[0] = node

def p_tipo2(p):
        '''tipo : varying par1 num par2'''
        node = grammer.nodoDireccion('tipo')
        node1= grammer.nodoDireccion(t[1])
        node2= grammer.nodoDireccion(t[2])
        node3= grammer.nodoDireccion(t[3])
        node4= grammer.nodoDireccion(t[4])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        t[0]= node
def p_tipo3(p):
        '''tipo : varchar par1 num par2'''
        node = grammer.nodoDireccion('tipo')
        node1= grammer.nodoDireccion(t[1])
        node2= grammer.nodoDireccion(t[2])
        node3= grammer.nodoDireccion(t[3])
        node4= grammer.nodoDireccion(t[4])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        t[0]= node
def p_tipo4(p):
        '''tipo : character par1 num par2'''
        node = grammer.nodoDireccion('tipo')
        node1= grammer.nodoDireccion(t[1])
        node2= grammer.nodoDireccion(t[2])
        node3= grammer.nodoDireccion(t[3])
        node4= grammer.nodoDireccion(t[4])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        t[0]= node
def p_tipo5(p):
        '''tipo :char par1 num par2'''
        node = grammer.nodoDireccion('tipo')
        node1= grammer.nodoDireccion(t[1])
        node2= grammer.nodoDireccion(t[2])
        node3= grammer.nodoDireccion(t[3])
        node4= grammer.nodoDireccion(t[4])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        t[0]= node

#ALTER
def p_alter(p):
		'''sentencia_alter : alter alter_objeto'''
        node = grammer.nodoDireccion('sentencia_alter')
        node1= grammer.nodoDireccion(t[1])
        node.agregar(node1)
        node.agregar(t[2])
        t[0]= t[1]

def p_alter_objeto(p):
		'''alter_objeto : table identificador alter_cont pyc'''
        node = grammer.nodoDireccion('alter_objeto')
        node1= grammer.nodoDireccion(t[1])
        node2= grammer.nodoDireccion(t[2])
        node4= grammer.nodoDireccion(t[4])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        node.agregar(node4)
        t[0]= node

def p_alter_objeto2(p):
        '''alter_objeto : database identificador rename to identificador pyc
						| database identificador owner to identificador pyc'''
        node = grammer.nodoDireccion('alter_objeto')
        node1= grammer.nodoDireccion(t[1])
        node2= grammer.nodoDireccion(t[2])
        node3= grammer.nodoDireccion(t[3])
        node4= grammer.nodoDireccion(t[4])
        node5= grammer.nodoDireccion(t[5])
        node6= grammer.nodoDireccion(t[6])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(node5)
        node.agregar(node6)
        t[0]= node

def p_alter_cont(p):
		'''alter_cont : add con_add
				   | drop con_drop
				   | rename con_rename
				   | alter con_alter'''
        node = grammer.nodoDireccion('alter_cont')
        node1= grammer.nodoDireccion(t[1])
        node.agregar(node1)
        node.agregar(t[2])
        t[0]= node

def p_con_add(p):
		'''con_add : column identificador tipo'''
        node = grammer.nodoDireccion('con_add')
        node1= grammer.nodoDireccion(t[1])
        node2= grammer.nodoDireccion(t[2])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        t[0]= node

def p_con_add2(p):
		'''con_add : check  par1 valor diferente vacio par2'''
        node = grammer.nodoDireccion('con_add')
        node1= grammer.nodoDireccion(t[1])
        node2= grammer.nodoDireccion(t[2])
        node4 = grammer.nodoDireccion(t[4])
        node5 = grammer.nodoDireccion(t[5])
        node6 = grammer.nodoDireccion(t[6])

        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        node.agregar(node4)
        node.agregar(node5)
        node.agregar(node6)
        t[0]= node
def p_con_add3(p):
		'''con_add : foreing key par1 identificador par2 references identificador'''

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
		'''if_exist : identificador'''

def p_if_exist2(p) : 
		'''if_exist :  identificador'''

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
		'''insert_cont : values par1 lista_insertar par2'''
                

def p_insert_cont2(p):
		'''insert_cont : par1 lista_campos par2 values par1 lista_insertar par2'''

def p_lista_campos(p):
		'''lista_campos : lista_campos coma identificador
		 	  	 	 | identificador'''

def p_lista_campos(p):
		'''lista_campos : identificador'''

def p_valor(p):
		'''valor : num'''

def p_valor2(p):
		'''valor : cadena'''

def p_valor3(p):
		'''valor : pdecimal'''

def p_valor4(p):
		'''valor : identificador'''

def p_valor5(p):
		'''valor : cadenacaracter'''

def p_valor6(p):
		'''valor : substring par1 valor coma valor coma valor par2'''

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
		'''delete_cont : only identificador'''

def p_delete_cont2(p):
		'''delete_cont : only identificador por'''

def p_delete_cont3(p):
		'''delete_cont : identificador por'''

def p_delete_cont4(p):
		'''delete_cont : identificador'''

#SELECT
def p_select(p):
		'''sentencia_select : select opciones_fecha'''

def p_select2(p):
		'''sentencia_select : select select_cont from lista_from order_by'''

def p_order(p):
		'''order_by : order by identificador opcion_order order_by'''

def p_order2(p):
		'''order_by : condicion_cont'''

def p_order3(p):
		'''order_by : limit operacion_aritmetica order_by'''

def p_order4(p):
		'''order_by : offset operacion_aritmetica order_by'''

def p_opcion_order(p):
		'''opcion_order : asc
					 | desc'''

def p_condicion_cont(p):
		'''condicion_cont : where operacion_logica fin_select'''

def p_condicion_cont2(p):
		'''condicion_cont : where operacion_logica group by identificador fin_select'''

def p_condicion_cont3(p):
		'''condicion_cont : group by lista_id fin_select'''

def p_condicion_cont4(p):
		'''condicion_cont : group by lista_id having operacion_logica fin_select'''

def p_condicion_cont5(p):
		'''condicion_cont : where exists par1 sentencia_select par2 fin_select'''

def p_condicion_cont6(p):
		'''condicion_cont : where operacion_aritmetica in par1 sentencia_select par2 fin_select'''

def p_condicion_cont7(p):
		'''condicion_cont : where operacion_aritmetica not in par1 sentencia_select par2 fin_select'''

def p_condicion_cont(p):
		'''condicion_cont8 : fin_select'''


def p_fin_select(p):
		'''fin_select : order_by identificador opcion_order pyc'''

def p_fin_select2(p):
		'''fin_select : pyc'''

def p_fin_select3(p):
		'''fin_select : union sentencia_select'''

def p_fin_select4(p):
		'''fin_select : intersect sentencia_select'''

def p_fin_select5(p):
		'''fin_select : except sentencia_select'''

def p_lista_from(p):
		'''lista_from : lista_from coma identificador as identificador'''

def p_lista_from2(p):
		'''lista_from : lista_from coma identificador'''

def p_lista_from3(p):
		'''lista_from :identificador as identificador'''

def p_lista_from4(p):
		'''lista_from : identificador'''

def p_lista_from5(p):
		'''lista_from : hacer_join'''

def p_lista_from6(p):
		'''lista_from : par1 sentencia_select par2 as identificador'''

def p_lista_from7(p):
		'''lista_from : par1 sentencia_select par2'''

def p_tipo_join(p):
		'''tipo_join : inner
					 | left
					 | right
					 | full
					 | outer'''

def p_hacer_join(p):
		'''hacer_join : identificador tipo_join join identificador on operacion_logica'''

def p_hacer_join2(p):
		'''hacer_join : identificador tipo_join join identificador'''

def p_select_cont(p):
		'''select_cont : por'''

def p_select_cont2(p):
		'''select_cont : distinct lista_id'''

def p_select_cont3(p):
		'''select_cont : lista_id'''

def p_select_cont4(p):
		'''select_cont : sen_case'''

def p_sen_case(p):
		'''sen_case : case case_when'''

def p_case_when(p):
		'''case_when : when operacion_logica then operacion_aritmetica case_when'''		

def p_case_when2(p):
		'''case_when : end valor'''

def p_lista_id(p):
		'''lista_id : lista_id coma operacion_aritmetica'''

def p_lista_id2(p):
		'''lista_id : lista_id coma identificador punto identificador'''

def p_lista_id3(p):
		'''lista_id : operacion_aritmetica'''

def p_lista_id4(p):
		'''lista_id : identificador punto identificador'''

def p_lista_id5(p):
		'''lista_id : substring par1 valor coma valor coma valor par2'''

def p_opciones_fecha(p):
		'''opciones_fecha : extract par1 tipo_date from timestamp valor par2 pyc'''

def p_opciones_fecha2(p):
		'''opciones_fecha : now par1 par2 pyc'''

def p_opciones_fecha3(p):
		'''opciones_fecha :date_part par1 valor coma interval valor par2 pyc'''

def p_opciones_fecha4(p):
		'''opciones_fecha : current_date pyc'''

def p_opciones_fecha5(p):
		'''opciones_fecha : current_time pyc'''

def p_opciones_fecha6(p):
		'''opciones_fecha : timestamp valor pyc'''

def p_tipo_date(p):
		'''tipo_date : year
					  | month
					  | day
					  | hour
					  | minute
					  | second'''

def p_condicion(p):
		'''condicion : pyc'''

def p_condicion2(p):
		'''condicion : where operacion_logica pyc'''

def p_condicion3(p):
		'''condicion : where identificador igual operacion_aritmetica pyc'''

def p_condicion4(p):
		'''condicion : where exists par1 sentencia_select par2 pyc'''
        node= grammer.nodoDireccion('condicion')
        node1 = grammer.nodoDireccion(t[1])
        node2= grammer.nodoDireccion(t[2])
        node3= grammer.nodoDireccion(t[3])
        node5= grammer.nodoDireccion(t[5])
        node6 = grammer.nodoDireccion(t[6])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(t[4])
        node.agregar(node5)
        node.agregar(node6)
        t[0]=node

def p_condicion5(p):
		'''condicion : where operacion_aritmetica in par1 sentencia_select par2 pyc'''
        node= grammer.nodoDireccion('condicion')
        node1 = grammer.nodoDireccion(t[1])
        node3= grammer.nodoDireccion(t[3])
        node4= grammer.nodoDireccion(t[4])
        node6= grammer.nodoDireccion(t[6])
        node7 = grammer.nodoDireccion(t[7])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(t[5])
        node.agregar(node6)
        node.agregar(node7)
        t[0]=node

def p_condicion6(p):
		'''condicion :where operacion_aritmetica not in par1 sentencia_select par2 pyc'''
        node= grammer.nodoDireccion('condicion')
        node1 = grammer.nodoDireccion(t[1])
        node3= grammer.nodoDireccion(t[3])
        node4= grammer.nodoDireccion(t[4])
        node5= grammer.nodoDireccion(t[5])
        node7 = grammer.nodoDireccion(t[7])
        node8= grammer.nodoDireccion(t[8])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(node5)
        node.agregar(t[6])
        node.agregar(node7)
        node.agregar(node8)
        t[0]=node

def p_op_aritmetica(p):
		'''operacion_aritmetica : operacion_aritmetica mas operacion_aritmetica'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        node2= grammer.nodoDireccion(t[2])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(t[3])
        t[0]=node

def p_op_aritmetica2(p):
		'''operacion_aritmetica : operacion_aritmetica menos operacion_aritmetica'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        node2= grammer.nodoDireccion(t[2])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(t[3])
        t[0]=node

def p_op_aritmetica3(p):
		'''operacion_aritmetica : operacion_aritmetica por operacion_aritmetica'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        node2= grammer.nodoDireccion(t[2])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(t[3])
        t[0]=node

def p_op_aritmetica4(p):
		'''operacion_aritmetica : operacion_aritmetica div operacion_aritmetica'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        node2= grammer.nodoDireccion(t[2])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(t[3])
        t[0]=node

def p_op_aritmetica5(p):
		'''operacion_aritmetica : par1 operacion_aritmetica par2'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        node1= grammer.nodoDireccion(t[1])
        node4= grammer.nodoDireccion(t[3])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(node4)
        t[0]=node

def p_op_aritmetica6(p):
		'''operacion_aritmetica : valor'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        node.agregar(t[0])
        t[0]=node

def p_op_aritmetica7(p):
		'''operacion_aritmetica : sum par1 operacion_aritmetica par2'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        node1= grammer.nodoDireccion(t[1])
        node2= grammer.nodoDireccion(t[2])
        node4= grammer.nodoDireccion(t[4])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        node.agregar(node4)
        t[0]=node

def p_op_aritmetica8(p):
		'''operacion_aritmetica : avg par1 operacion_aritmetica par2'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        node1= grammer.nodoDireccion(t[1])
        node2= grammer.nodoDireccion(t[2])
        node4= grammer.nodoDireccion(t[4])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        node.agregar(node4)
        t[0]=node

def p_op_aritmetica9(p):
		'''operacion_aritmetica : max par1 operacion_aritmetica par2'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        node1= grammer.nodoDireccion(t[1])
        node2= grammer.nodoDireccion(t[2])
        node4= grammer.nodoDireccion(t[4])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        node.agregar(node4)
        t[0]=node

def p_op_aritmetica10(p):
		'''operacion_aritmetica :  pi'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        node1= grammer.nodoDireccion(t[1])
        node.agregar(node1)
        t[0]=node

def p_op_aritmetica11(p):
		'''operacion_aritmetica : power par1 operacion_aritmetica par2'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        node1= grammer.nodoDireccion(t[1])
        node2= grammer.nodoDireccion(t[2])
        node4= grammer.nodoDireccion(t[4])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        node.agregar(node4)
        t[0]=node

def p_op_aritmetica12(p):
		'''operacion_aritmetica : sqrt par1 operacion_aritmetica par2'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        node1= grammer.nodoDireccion(t[1])
        node2= grammer.nodoDireccion(t[2])
        node4= grammer.nodoDireccion(t[4])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        node.agregar(node4)
        t[0]=node

def p_op_aritmetica13(p):
		'''operacion_aritmetica : valor between valor'''
        node= grammer.nodoDireccion('operacion_aritmetica')        
        node2= grammer.nodoDireccion(t[2])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(t[3])
        t[0]=node

def p_op_aritmetica14(p):
		'''operacion_aritmetica : valor is distinct from valor'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        
        node2= grammer.nodoDireccion(t[2])
        node3= grammer.nodoDireccion(t[3])
        node4= grammer.nodoDireccion(t[4])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(t[5])
        t[0]=node

def p_op_aritmetica15(p):
		'''operacion_aritmetica : valor is not distinct from valor'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        
        node2= grammer.nodoDireccion(t[2])
        node3= grammer.nodoDireccion(t[3])
        node4= grammer.nodoDireccion(t[4])
        node5 = grammer.nodoDireccion(t[5])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(node5)
        node.agregar(t[6])
        t[0]=node

def p_op_aritmetica16(p):
		'''operacion_aritmetica : valor is null'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        
        node2= grammer.nodoDireccion(t[2])
        node3= grammer.nodoDireccion(t[3])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(node3)
        t[0]=node

def p_op_aritmetica17(p):
		'''operacion_aritmetica : valor is not null'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        
        node2= grammer.nodoDireccion(t[2])
        node3= grammer.nodoDireccion(t[3])
        node4= grammer.nodoDireccion(t[4])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        t[0]=node

def p_op_aritmetica18(p):
		'''operacion_aritmetica :valor is true'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        
        node2= grammer.nodoDireccion(t[2])
        node3= grammer.nodoDireccion(t[3])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(node3)
        t[0]=node

def p_op_aritmetica19(p):
		'''operacion_aritmetica : valor is not true'''
        node= grammer.nodoDireccion('operacion_aritmetica')        
        node2= grammer.nodoDireccion(t[2])
        node3= grammer.nodoDireccion(t[3])
        node4= grammer.nodoDireccion(t[4])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        t[0]=node

def p_op_aritmetica20(p):
		'''operacion_aritmetica : valor is false'''
        node= grammer.nodoDireccion('operacion_aritmetica')        
        node2= grammer.nodoDireccion(t[2])
        node3= grammer.nodoDireccion(t[3])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(node3)
        t[0]=node

def p_op_aritmetica21(p):
		'''operacion_aritmetica : valor is not false'''
        node= grammer.nodoDireccion('operacion_aritmetica')
        
        node2= grammer.nodoDireccion(t[2])
        node3= grammer.nodoDireccion(t[3])
        node4= grammer.nodoDireccion(t[4])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        t[0]=node

def p_op_relacional(p):
		'''operacion_relacional : operacion_relacional mayor operacion_relacional'''
        node= grammer.nodoDireccion('operacion_relacional')
        node2= grammer.nodoDireccion(t[2])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(t[3])
        t[0]=node

def p_op_relacional2(p):
		'''operacion_relacional : operacion_relacional menor operacion_relacional'''
        node= grammer.nodoDireccion('operacion_relacional')
        node2= grammer.nodoDireccion(t[2])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(t[3])
        t[0]=node

def p_op_relacional3(p):
		'''operacion_relacional : operacion_relacional mayorigual operacion_relacional'''
        node= grammer.nodoDireccion('operacion_relacional')
        node2= grammer.nodoDireccion(t[2])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(t[3])
        t[0]=node

def p_op_relacional4(p):
		'''operacion_relacional : operacion_relacional menorigual operacion_relacional'''
        node= grammer.nodoDireccion('operacion_relacional')
        node2= grammer.nodoDireccion(t[2])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(t[3])
        t[0]=node
        

def p_op_relacional5(p):
		'''operacion_relacional : operacion_relacional diferente operacion_relacional'''
        node= grammer.nodoDireccion('operacion_relacional')
        node2= grammer.nodoDireccion(t[2])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(t[3])
        t[0]=node

def p_op_relacional6(p):
		'''operacion_relacional :operacion_relacional igual operacion_relacional'''
        node= grammer.nodoDireccion('operacion_relacional')
        node2= grammer.nodoDireccion(t[2])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(t[3])
        t[0]=node

def p_op_relacional7(p):
		'''operacion_relacional : operacion_aritmetica'''
        node= grammer.nodoDireccion('operacion_relacional')
        node.agregar(t[1])
        t[0]=node

def p_op_logica(p):
		'''operacion_logica : operacion_logica and operacion_logica'''
        node= grammer.nodoDireccion('operacion_logica')
        node2= grammer.nodoDireccion(t[2])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(t[3])
        t[0]=node

def p_op_logica2(p):
		'''operacion_logica : operacion_logica or operacion_logica'''
        node= grammer.nodoDireccion('operacion_logica')
        node2= grammer.nodoDireccion(t[2])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(t[3])
        t[0]=node

def p_op_logica3(p):
		'''operacion_logica : operacion_logica not operacion_logica'''
        node= grammer.nodoDireccion('operacion_logica')
        node2= grammer.nodoDireccion(t[2])
        node.agregar(t[1])
        node.agregar(node2)
        node.agregar(t[3])
        t[0]=node

def p_op_logica4(p):
		'''operacion_logica :operacion_relacional'''
        node= grammer.nodoDireccion('operacion_logica')
        node.agregar(t[1])
        t[0]=node
def p_show(p):
		'''sentencia_show : show databases show_cont'''
        node= grammer.nodoDireccion('sentencia_show')
        node1= grammer.nodoDireccion(t[1])
        node2= grammer.nodoDireccion(t[2])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        t[0]=node

def p_show_cont(p):
		'''show_cont : pyc'''
        node= grammer.nodoDireccion('show_cont')
        node1= grammer.nodoDireccion(t[1])
        node.agregar(node1)
        t[0]=node
def p_show_cont2(p):
		'''show_cont : ins_like pyc'''
        node= grammer.nodoDireccion('show_cont')
        node2= grammer.nodoDireccion(t[2])
        node.agregar(t[1])
        node.agregar(node2)
        t[0]=node

def p_ins_like(p):
		'''ins_like : like porcentaje identificador porcentaje'''
        node= grammer.nodoDireccion('ins_like')
        node1= grammer.nodoDireccion(t[1])
        node2= grammer.nodoDireccion(t[2])
        node3= grammer.nodoDireccion(t[3])
        node4= grammer.nodoDireccion(t[4])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        t[0]=node

def p_empty(p):
     'empty :'
     pass

#def p_error(p):
#    print("Error sintáctico en '%s'" % p.value)


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