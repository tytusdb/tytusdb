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
                node = grammer.nodoDireccion('inicio')
                node.agregar(t[1])
                t[0] = node


def p_instrucciones(t):
    '''instrucciones : instruccion instrucciones_2'''

    node = grammer.nodoDireccion('instrucciones')
    node.agregar(t[1])
    node.agregar(t[2])
    t[0] = node


def p_instrucciones_2(t):
    '''instrucciones_2 : NEWLINE instruccion instrucciones_2'''

    node = grammer.nodoDireccion('instrucciones')
    node.agregar(t[3])
    node.agregar(t[2])
    t[0] = node


def p_instrucciones_3(t):
    '''instrucciones_2 : empty'''
    node = grammer.nodoDireccion('vacio')
    node.agregar(t[1])
    t[0] = node


def p_instruccion(t):
    '''instruccion : ddl
                    | dml
                    | ins_use'''

    node = grammer.nodoDireccion('instruccion')
    node.agregar(t[1])
    t[0] = node


def p_ddl(t):
    '''ddl : sentencia_create
            | sentencia_alter
            | sentencia_drop
            | sentencia_truncate'''
    node = grammer.nodoDireccion('ddl')
    node.agregar(t[1])
    t[0] = node


def p_dml(t):
    '''dml : sentencia_insert
            | sentencia_update
            | sentencia_delete
            | sentencia_select
            | sentencia_show'''
    node = grammer.nodoDireccion('dml')
    node.agregar(t[1])
    t[0] = node


def p_ins_use(t):
    '''ins_use : use identificador'''
    node = grammer.nodoDireccion('ins_use')
    node2 = grammer.nodoDireccion(t[1])
    node3 = grammer.nodoDireccion(t[2])
    node.agregar(node2)
    node.agregar(node3)
    t[0] = node

#----------DDL----------
#CREAR


def p_crear(t):
        '''sentencia_create : create create_cont
                            | replace create_cont'''

        node = grammer.nodoDireccion('sentencia_Create')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        node.agregar(t[2])
        t[0] = node


def p_create_cont(t):
    '''create_cont : database if_not pyc'''

    node = grammer.nodoDireccion('create_cont')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    node.agregar(t[2])
    t[0] = node


def p_create_cont2(t):
    '''create_cont : table if_not par1 col_tabla par2 fin_tabla '''

    node = grammer.nodoDireccion('create_cont')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    node.agregar(t[2])
    node.agregar(t[4])
    node.agregar(t[6])
    t[0] = node


def p_create_cont3(t):
    '''create_cont : type valor as enum par1 lista_insertar par2 pyc'''

    node = grammer.nodoDireccion('create_cont')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    node.agregar(t[2])
    node2 = grammer.nodoDireccion(t[3])
    node3 = grammer.nodoDireccion(t[4])
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(t[6])
    t[0] = node


def p_inherits(t):
    '''fin_tabla : inherits par1 identificador par2 pyc'''

    node = grammer.nodoDireccion('fin_tabla')
    node1 = grammer.nodoDireccion(''+t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    t[0] = node


def p_inherits2(t):
    '''fin_tabla : pyc'''

    node = grammer.nodoDireccion('fin_tabla')
    node1 = grammer.nodoDireccion(''+t[1])
    node.agregar(node1)
    t[0] = node


def p_if_not(t):
    '''if_not : if not exists identificador'''

    node = grammer.nodoDireccion('if_not')
    node1 = grammer.nodoDireccion(''+t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    t[0] = node


def p_if_not2(t):
    '''if_not : identificador'''

    node = grammer.nodoDireccion('if_not')
    node1 = grammer.nodoDireccion('(ID)'+ t[1])
    node.agregar(node1)
    t[0] = node


def p_if_not3(t):
    '''if_not : if not exists identificador owner igual valor'''

    node = grammer.nodoDireccion('if_not')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion('(ID) '+t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(t[7])
    t[0] = node


def p_if_not4(t):
    '''if_not : identificador owner valor'''

    node = grammer.nodoDireccion('if_not')
    node1 = grammer.nodoDireccion('(ID)'+t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    t[0] = node


def p_if_not5(t):
    '''if_not : if not exists identificador mode igual valor'''

    node = grammer.nodoDireccion('if_not')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion('(ID) '+t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(t[7])
    t[0] = node


def p_if_not6(t):
    '''if_not : identificador mode igual valor'''

    node = grammer.nodoDireccion('if_not')
    node1 = grammer.nodoDireccion('(ID) '+t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(t[4])
    t[0] = node


def p_col_tabla(t):
    '''col_tabla : identificador tipo propiedades col_tabla_2'''

    node = grammer.nodoDireccion('col_tabla')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(node2)
    node.agregar(t[2])
    node.agregar(t[3])
    node.agregar(t[4])
    t[0] = node


def p_col_tabla2(t):
    '''col_tabla : identificador tipo col_tabla_2'''

    node = grammer.nodoDireccion('col_tabla')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(node2)
    node.agregar(t[2])
    node.agregar(t[3])
    t[0] = node


def p_col_tabla3(t):
    '''col_tabla : foreing key lista_id references identificador col_tabla_2'''

    node = grammer.nodoDireccion('col_tabla')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(t[6])
    t[0] = node


def p_col_tabla4(t):
    '''col_tabla_2 : coma identificador tipo propiedades col_tabla_2'''

    node = grammer.nodoDireccion('col_tabla')
    node.agregar(t[5])
    node2 = grammer.nodoDireccion(t[1])
    node4 = grammer.nodoDireccion('(ID) ' + t[2])
    node.agregar(node2)
    node.agregar(node4)
    node.agregar(t[3])
    node.agregar(t[4])
    t[0] = node


def p_col_tabla5(t):
    '''col_tabla_2 : coma identificador tipo col_tabla_2'''

    node = grammer.nodoDireccion('col_tabla')
    node.agregar(t[4])
    node2 = grammer.nodoDireccion(t[1])
    node4 = grammer.nodoDireccion('(ID) ' + t[2])
    node.agregar(node2)
    node.agregar(node4)
    node.agregar(t[3])
    t[0] = node


def p_col_tabla6(t):
    '''col_tabla_2 : coma primary key lista_id col_tabla_2'''

    node = grammer.nodoDireccion('col_tabla')
    node2 = grammer.nodoDireccion(t[1])
    node3 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[3])
    node.agregar(t[5])
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(t[4])
    t[0] = node


def p_col_tabla7(t):
    '''col_tabla_2 : empty'''
    node = grammer.nodoDireccion('vacio')
    node.agregar(t[1])
    t[0] = node


def p_propiedades(t):
    '''propiedades : null propiedades'''
    node = grammer.nodoDireccion('propiedades')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    node.agregar(t[2])
    t[0] = node


def p_propiedades2(t):
    '''propiedades : not null propiedades'''
    node = grammer.nodoDireccion('propiedades')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    t[0] = node


def p_propiedades3(t):
    '''propiedades : identity propiedades'''
    node = grammer.nodoDireccion('propiedades')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    node.agregar(t[2])
    t[0] = node


def p_propiedades4(t):
    '''propiedades : primary key propiedades '''
    node = grammer.nodoDireccion('propiedades')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    t[0] = node


def p_propiedades5(t):
    '''propiedades : null'''
    node = grammer.nodoDireccion('propiedades')
    node1 = grammer.nodoDireccion(t[1])

    node.agregar(node1)
    t[0] = node


def p_propiedades6(t):
    '''propiedades : not null'''
    node = grammer.nodoDireccion('propiedades')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(node2)
    t[0] = node


def p_propiedades7(t):
    '''propiedades : identity'''
    node = grammer.nodoDireccion('propiedades')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_propiedades8(t):
    '''propiedades : primary key'''
    node = grammer.nodoDireccion('propiedades')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(node2)
    t[0] = node


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
    | text
    | date
    | boolean
    | int
    | identificador'''

    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_tipo2(t):
    '''tipo : varying par1 num par2'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    t[0] = node


def p_tipo3(t):
    '''tipo : varchar par1 num par2'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    t[0] = node


def p_tipo4(t):
    '''tipo : character par1 num par2'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    t[0] = node


def p_tipo5(t):
    '''tipo : char par1 num par2'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    t[0] = node

# ALTER


def p_alter(t):
        '''sentencia_alter : alter alter_objeto'''
        node = grammer.nodoDireccion('sentencia_alter')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        node.agregar(t[2])
        t[0] = node


def p_alter_objeto(t):
        '''alter_objeto : table identificador alter_cont pyc'''
        node = grammer.nodoDireccion('alter_objeto')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node4 = grammer.nodoDireccion(t[4])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        node.agregar(node4)
        t[0] = node


def p_alter_objeto2(t):
        '''alter_objeto : database identificador rename to identificador pyc
        | database identificador owner to identificador pyc'''
        node = grammer.nodoDireccion('alter_objeto')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node3 = grammer.nodoDireccion(t[3])
        node4 = grammer.nodoDireccion(t[4])
        node5 = grammer.nodoDireccion(t[5])
        node6 = grammer.nodoDireccion(t[6])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(node5)
        node.agregar(node6)
        t[0] = node


def p_alter_cont(t):
        '''alter_cont : add con_add
        | drop con_drop
        | rename con_rename
        | alter con_alter'''
        node = grammer.nodoDireccion('alter_cont')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        node.agregar(t[2])
        t[0] = node


def p_con_add(t):
        '''con_add : column identificador tipo'''
        node = grammer.nodoDireccion('con_add')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        t[0] = node


def p_con_add2(t):
        '''con_add : check  par1 valor diferente vacio par2'''
        node = grammer.nodoDireccion('con_add')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node4 = grammer.nodoDireccion(t[4])
        node5 = grammer.nodoDireccion(t[5])
        node6 = grammer.nodoDireccion(t[6])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        node.agregar(node4)
        node.agregar(node5)
        node.agregar(node6)
        t[0] = node


def p_con_add3(t):
        '''con_add : foreing key par1 identificador par2 references identificador'''
        node= grammer.nodoDireccion('con_add')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node3 = grammer.nodoDireccion(t[3])
        node4 = grammer.nodoDireccion(t[4])
        node5 = grammer.nodoDireccion(t[5])
        node6 = grammer.nodoDireccion(t[6])
        node7 = grammer.nodoDireccion(t[7])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(node5)
        node.agregar(node6)
        node.agregar(node7)
        t[0] = node


def p_con_drop(t):
        '''con_drop : column identificador
        | constraint identificador '''
        node = grammer.nodoDireccion('con_drop')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node.agregar(node1)
        node.agregar(node2)
        t[0] = node


def p_con_rename(t):
        '''con_rename : column identificador to identificador'''
        node = grammer.nodoDireccion('con_raname')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node3 = grammer.nodoDireccion(t[3])
        node4 = grammer.nodoDireccion(t[4])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        t[0] = node


def p_con_alter(t):
        '''con_alter : column identificador set not null'''
        node = grammer.nodoDireccion('con_alter')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node3 = grammer.nodoDireccion(t[3])
        node4 = grammer.nodoDireccion(t[4])
        node5 = grammer.nodoDireccion(t[5])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(node5)
        t[0] = node

#DROP


def p_drop(t):
        '''sentencia_drop : drop objeto if_exist pyc'''
        node = grammer.nodoDireccion('sentencia_drop')
        node1 = grammer.nodoDireccion(t[1])
        node4 = grammer.nodoDireccion(t[4])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(t[3])
        node.agregar(node4)
        t[0] = node


def p_if_exist(t):
        'if_exist :  if exists identificador'
        node = grammer.nodoDireccion('if_exist')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node3 = grammer.nodoDireccion(t[3])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        t[0] = node


def p_if_exist2(t):
        'if_exist :  identificador'
        node = grammer.nodoDireccion('if_exist')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        t[0] = node


def p_objeto(t):
        '''objeto : table
        | database'''
        node = grammer.nodoDireccion('objeto')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        t[0] = node

#TRUNCATE


def p_truncate(t):
    'sentencia_truncate : truncate table identificador pyc'
    node = grammer.nodoDireccion('sentencia_truncate')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    t[0] = node


# ----------DML----------
# INSERT


def p_insert(t):
    'sentencia_insert : insert into identificador insert_cont pyc'
    node = grammer.nodoDireccion('sentencia_insert')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node5 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(t[4])
    node.agregar(node5)
    t[0] = node


def p_insert_cont(t):
    'insert_cont : values par1 lista_insertar par2'
    node = grammer.nodoDireccion('insert_cont')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    node.agregar(node4)
    t[0] = node


def p_insert_cont2(t):
    'insert_cont : par1 lista_campos par2 values par1 lista_insertar par2'
    node = grammer.nodoDireccion('insert_cont')
    node1 = grammer.nodoDireccion(t[1])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node7 = grammer.nodoDireccion(t[7])
    node.agregar(node1)
    node.agregar(t[2])
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(t[6])
    node.agregar(node7)
    t[0] = node


def p_lista_campos(t):
    '''lista_campos :  identificador lista_campos_2'''
    node = grammer.nodoDireccion('lista_campos')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    node.agregar(t[2])
    t[0] = node


def p_lista_campos_2(t):
    '''lista_campos_2 : coma identificador lista_campos_2'''
    node = grammer.nodoDireccion('lista_campos')
    node2 = grammer.nodoDireccion(t[1])
    node3 = grammer.nodoDireccion(t[2])
    node.agregar(t[3])
    node.agregar(node2)
    node.agregar(node3)
    t[0] = node


def p_lista_campos_3(t):
    '''lista_campos_2 : empty'''
    node = grammer.nodoDireccion('vacio')
    node.agregar(t[1])
    t[0] = node


def p_valor(t):
        'valor : num'
        node = grammer.nodoDireccion('valor')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        t[0] = node


def p_valor2(t):
        'valor : cadena'
        node = grammer.nodoDireccion('valor')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        t[0] = node


def p_valor3(t):
        'valor : pdecimal'
        node = grammer.nodoDireccion('valor')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        t[0] = node


def p_valor4(t):
        'valor : identificador'
        node = grammer.nodoDireccion('valor')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        t[0] = node


def p_valor5(t):
        'valor : cadenacaracter'
        node = grammer.nodoDireccion('valor')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        t[0] = node


def p_valor6(t):
        'valor : substring par1 valor coma valor coma valor par2'
        node = grammer.nodoDireccion('valor')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node4 = grammer.nodoDireccion(t[4])
        node6 = grammer.nodoDireccion(t[6])
        node8 = grammer.nodoDireccion(t[8])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        node.agregar(node4)
        node.agregar(t[5])
        node.agregar(node6)
        node.agregar(t[7])
        node.agregar(node8)
        t[0] = node


def p_lista_insertar(t):
    '''lista_insertar : operacion_aritmetica lista_insertar_2'''
    node = grammer.nodoDireccion('lista_insertar')
    node.agregar(t[1])
    node.agregar(t[2])
    t[0] = node

def p_lista_insertar_2(t):
    '''lista_insertar_2 : coma operacion_aritmetica lista_insertar_2'''
    node = grammer.nodoDireccion('lista_insertar')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(t[3])
    node.agregar(node2)
    node.agregar(t[2])
    t[0] = node


def p_lista_insertar_3(t):
    '''lista_insertar_2 : empty'''
    node = grammer.nodoDireccion('vacio')
    node.agregar(t[1])
    t[0] = node


#UPDATE


def p_update(t):
        'sentencia_update : update  identificador set identificador igual operacion_aritmetica condicion'
        node = grammer.nodoDireccion('sentencia_update')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node3 = grammer.nodoDireccion(t[3])
        node4 = grammer.nodoDireccion(t[4])
        node5 = grammer.nodoDireccion(t[5])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(node5)
        node.agregar(t[6])
        node.agregar(t[7])
        t[0] = node

#DELETE


def p_delete(t):
        'sentencia_delete : delete from delete_cont condicion'
        node = grammer.nodoDireccion('sentencia_delete')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        node.agregar(t[4])
        t[0] = node


def p_delete_cont(t):
        'delete_cont : only identificador'
        node = grammer.nodoDireccion('delete_cont')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node.agregar(node1)
        node.agregar(node2)
        t[0] = node


def p_delete_cont2(t):
        'delete_cont : only identificador por'
        node = grammer.nodoDireccion('delete_cont')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node3 = grammer.nodoDireccion(t[3])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        t[0] = node


def p_delete_cont3(t):
        'delete_cont : identificador por'
        node = grammer.nodoDireccion('delete_cont')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node.agregar(node1)
        node.agregar(node2)
        t[0] = node


def p_delete_cont4(t):
        'delete_cont : identificador'
        node = grammer.nodoDireccion('delete_cont')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        t[0] = node

#SELECT


def p_select(t):
        'sentencia_select : select opciones_fecha'
        node = grammer.nodoDireccion('sentencia_select')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        node.agregar(t[2])
        t[0] = node


def p_select2(t):
        'sentencia_select : select select_cont from lista_from condicion_cont'
        node = grammer.nodoDireccion('sentencia_select')
        node1 = grammer.nodoDireccion(t[1])
        node3 = grammer.nodoDireccion(t[3])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(node3)
        node.agregar(t[4])
        node.agregar(t[5])
        t[0] = node


def p_order(t):
        'order_by : order by identificador opcion_order order_by'
        node = grammer.nodoDireccion('order_by')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node3 = grammer.nodoDireccion(t[3])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(t[4])
        node.agregar(t[5])
        t[0] = node


def p_order2(t):
        'order_by : condicion_cont'
        node = grammer.nodoDireccion('order_by')
        node.agregar(t[1])
        t[0] = node


def p_order3(t):
        'order_by : limit operacion_aritmetica order_by'
        node = grammer.nodoDireccion('order_by')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(t[3])
        t[0] = node


def p_order4(t):
        '''order_by : offset operacion_aritmetica order_by'''
        node = grammer.nodoDireccion('order_by')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(t[3])
        t[0] = node


def p_opcion_order(t):
        '''opcion_order : asc
        | desc'''
        node = grammer.nodoDireccion('opcion_order')
        node1 = grammer.nodoDireccion(t[1])

        node.agregar(node1)
        t[0] = node


def p_condicion_cont(t):
        '''condicion_cont : where operacion_logica fin_select'''
        node = grammer.nodoDireccion('condicion_cont')
        node1 = grammer.nodoDireccion(t[1])

        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(t[3])
        t[0] = node


def p_condicion_cont1(t):
        'condicion_cont : where operacion_relacional fin_select'
        node = grammer.nodoDireccion('condicion_cont')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(t[3])
        t[0] = node


def p_condicion_cont2(t):
        'condicion_cont : where operacion_logica group by identificador fin_select'
        node = grammer.nodoDireccion('condicion_cont')
        node1 = grammer.nodoDireccion(t[1])
        node3 = grammer.nodoDireccion(t[3])
        node4 = grammer.nodoDireccion(t[4])
        node5 = grammer.nodoDireccion(t[5])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(node5)
        node.agregar(t[6])
        t[0] = node


def p_condicion_cont3(t):
        'condicion_cont : group by lista_id fin_select'
        node = grammer.nodoDireccion('condicion_cont')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        node.agregar(t[4])
        t[0] = node


def p_condicion_cont4(t):
        'condicion_cont : group by lista_id having operacion_logica fin_select'
        node = grammer.nodoDireccion('condicion_cont')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node4 = grammer.nodoDireccion(t[4])

        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        node.agregar(node4)
        node.agregar(t[5])
        node.agregar(t[6])
        t[0] = node


def p_condicion_cont5(t):
        'condicion_cont : where exists par1 sentencia_select par2 fin_select'
        node = grammer.nodoDireccion('condicion_cont')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node3 = grammer.nodoDireccion(t[3])
        node5 = grammer.nodoDireccion(t[5])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(t[4])
        node.agregar(node5)
        node.agregar(t[6])
        t[0] = node


def p_condicion_cont6(t):
        'condicion_cont : where operacion_aritmetica in par1 sentencia_select par2 fin_select'
        node = grammer.nodoDireccion('condicion_cont')
        node1 = grammer.nodoDireccion(t[1])
        node3 = grammer.nodoDireccion(t[3])
        node4 = grammer.nodoDireccion(t[4])
        node6 = grammer.nodoDireccion(t[6])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(t[5])
        node.agregar(node6)
        node.agregar(t[7])
        t[0] = node


def p_condicion_cont7(t):
        'condicion_cont : where operacion_aritmetica not in par1 sentencia_select par2 fin_select'
        node = grammer.nodoDireccion('condicion_cont')
        node1 = grammer.nodoDireccion(t[1])
        node3 = grammer.nodoDireccion(t[3])
        node4 = grammer.nodoDireccion(t[4])
        node5 = grammer.nodoDireccion(t[5])
        node7 = grammer.nodoDireccion(t[7])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(node5)
        node.agregar(t[6])
        node.agregar(node7)
        node.agregar(t[8])
        t[0] = node


def p_condicion_cont8(t):
        'condicion_cont : fin_select'
        node = grammer.nodoDireccion('condicion_cont')
        node.agregar(t[1])
        t[0] = node


def p_fin_select(t):
        'fin_select : order_by '
        node = grammer.nodoDireccion('fin_select')
        node.agregar(t[1])
        t[0] = node


def p_fin_select2(t):
        'fin_select : pyc'
        node = grammer.nodoDireccion('fin_select')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        t[0] = node


def p_fin_select3(t):
        'fin_select : union sentencia_select'
        node = grammer.nodoDireccion('fin_select')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        node.agregar(t[2])
        t[0] = node


def p_fin_select4(t):
        'fin_select : intersect sentencia_select'
        node = grammer.nodoDireccion('fin_select')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        node.agregar(t[2])
        t[0] = node


def p_fin_select5(t):
        'fin_select : except sentencia_select'
        node = grammer.nodoDireccion('fin_select')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        node.agregar(t[2])
        t[0] = node


def p_lista_from(t):
    '''lista_from : identificador as identificador lista_from_2'''
    node = grammer.nodoDireccion('lista_from')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(t[4])
    t[0] = node


def p_lista_from2(t):
    '''lista_from : identificador lista_from_2'''
    node = grammer.nodoDireccion('lista_from')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    node.agregar(t[2])
    t[0] = node


def p_lista_from3(t):
    '''lista_from : hacer_join lista_from_2'''
    node = grammer.nodoDireccion('lista_from')
    node.agregar(t[1])
    node.agregar(t[2])
    t[0] = node


def p_lista_from4(t):
    '''lista_from : par1 sentencia_select par2 as identificador lista_from_2'''
    node = grammer.nodoDireccion('lista_from')
    node1 = grammer.nodoDireccion(t[1])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(t[2])
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(t[6])
    t[0] = node


def p_lista_from5(t):
    '''lista_from : par1 sentencia_select par2 lista_from_2'''
    node = grammer.nodoDireccion('lista_from')
    node1 = grammer.nodoDireccion(t[1])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(t[2])
    node.agregar(node3)
    node.agregar(t[4])
    t[0] = node


def p_lista_from6(t):
    '''lista_from_2 : coma identificador as identificador lista_from_2'''
    node = grammer.nodoDireccion('lista_from')
    node1 = grammer.nodoDireccion(t[1])
    node3 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[3])
    node5 = grammer.nodoDireccion(t[4])
    node.agregar(t[5])
    node.agregar(node1)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    t[0] = node


def p_lista_from7(t):
    '''lista_from_2 : coma identificador lista_from_2'''
    node = grammer.nodoDireccion('lista_from')
    node1 = grammer.nodoDireccion(t[1])
    node3 = grammer.nodoDireccion(t[2])
    node.agregar(t[3])
    node.agregar(node1)
    node.agregar(node3)
    t[0] = node


def p_lista_from8(t):
    '''lista_from_2 : empty'''
    node = grammer.nodoDireccion("vacio")
    node.agregar(t[1])
    t[0] = node


def p_tipo_join(t):
        '''tipo_join : inner join
        | left join
        | right join
        | full join
        | outer join'''
        node = grammer.nodoDireccion('tipo_join')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        node2 = grammer.nodoDireccion(t[2])
        node.agregar(node2)
        t[0] = node


def p_tipo_join2(t):
        '''tipo_join : join'''
        node = grammer.nodoDireccion('tipo_join')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        t[0] = node


def p_hacer_join(t):
        '''hacer_join : identificador tipo_join identificador on operacion_logica'''
        node = grammer.nodoDireccion('hacer_join')
        node1 = grammer.nodoDireccion(t[1])
        node3 = grammer.nodoDireccion(t[3])
        node4 = grammer.nodoDireccion(t[4])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(t[5])
        t[0] = node


def p_hacer_join2(t):
        '''hacer_join : identificador tipo_join  identificador'''
        node = grammer.nodoDireccion('hacer_join')
        node1 = grammer.nodoDireccion(t[1])
        node3 = grammer.nodoDireccion(t[3])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(node3)
        t[0] = node


def p_select_cont(t):
        '''select_cont : por'''
        node = grammer.nodoDireccion('select_cont')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        t[0] = node


def p_select_cont2(t):
        '''select_cont : distinct lista_id'''
        node = grammer.nodoDireccion('select_cont')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        node.agregar(t[2])
        t[0] = node


def p_select_cont3(t):
        '''select_cont : lista_id'''
        node = grammer.nodoDireccion('select_cont')
        node.agregar(t[1])
        t[0] = node


def p_select_cont4(t):
        '''select_cont : sen_case'''
        node = grammer.nodoDireccion('select_cont')
        node.agregar(t[1])
        t[0] = node


def p_sen_case(t):
        '''sen_case : case case_when'''
        node = grammer.nodoDireccion('sen_case')
        node2 = grammer.nodoDireccion(t[1])
        node.agregar(node2)
        node.agregar(t[2])
        t[0] = node


def p_case_when(t):
        '''case_when : when operacion_logica then operacion_aritmetica case_when'''
        node = grammer.nodoDireccion('case_when')
        node1 = grammer.nodoDireccion(t[1])
        node3 = grammer.nodoDireccion(t[3])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(node3)
        node.agregar(t[4])
        node.agregar(t[5])
        t[0] = node


def p_case_when2(t):
        '''case_when : end valor'''
        node = grammer.nodoDireccion('case_when')
        node2 = grammer.nodoDireccion(t[1])
        node.agregar(node2)
        node.agregar(t[2])
        t[0] = node


def p_lista_id(t):
    '''lista_id : operacion_aritmetica lista_id_2'''
    node= grammer.nodoDireccion('lista_id')
    node.agregar(t[1])
    node.agregar(t[2])
    t[0]=node


def p_lista_id2(t):
    '''lista_id : identificador punto identificador lista_id_2'''
    node= grammer.nodoDireccion('lista_id')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(t[4])
    t[0]=node


def p_lista_id3(t):
    '''lista_id : substring par1 valor coma valor coma valor par2 lista_id_2'''
    node= grammer.nodoDireccion('lista_id')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[4])
    node6 = grammer.nodoDireccion(t[6])
    node8 = grammer.nodoDireccion(t[8])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    node.agregar(node4)
    node.agregar(t[5])
    node.agregar(node6)
    node.agregar(t[7])
    node.agregar(node8)
    node.agregar(t[9])
    t[0]=node


def p_lista_id4(t):
    '''lista_id_2 : coma operacion_aritmetica lista_id_2'''
    node= grammer.nodoDireccion('lista_id')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(node2)
    node.agregar(t[2])
    node.agregar(t[3])
    t[0]=node


def p_lista_id5(t):
    '''lista_id_2 : coma identificador punto identificador lista_id_2'''
    node= grammer.nodoDireccion('lista_id')
    node2 = grammer.nodoDireccion(t[1])
    node3 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[3])
    node5 = grammer.nodoDireccion(t[4])
    node.agregar(t[5])
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    t[0]=node


def p_lista_id6(t):
    '''lista_id_2 : empty'''
    node = grammer.nodoDireccion('vacio')
    node.agregar(t[1])
    t[0] = node



def p_opciones_fecha(t):
        'opciones_fecha : extract par1 tipo_date from timestamp valor par2 pyc'
        node = grammer.nodoDireccion('opciones_fecha')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node4 = grammer.nodoDireccion(t[4])
        node5 = grammer.nodoDireccion(t[5])
        node7 = grammer.nodoDireccion(t[7])
        node8 = grammer.nodoDireccion(t[8])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        node.agregar(node4)
        node.agregar(node5)
        node.agregar(t[6])
        node.agregar(node7)
        node.agregar(node8)
        t[0] = node


def p_opciones_fecha2(t):
        'opciones_fecha : now par1 par2 pyc'
        node = grammer.nodoDireccion('opciones_fecha')
        node2 = grammer.nodoDireccion(t[1])
        node4 = grammer.nodoDireccion(t[2])
        node5 = grammer.nodoDireccion(t[3])
        node7 = grammer.nodoDireccion(t[4])
        node.agregar(node2)
        node.agregar(node4)
        node.agregar(node5)
        node.agregar(node7)
        t[0] = node


def p_opciones_fecha3(t):
        'opciones_fecha : date_part par1 valor coma interval valor par2 pyc'
        node = grammer.nodoDireccion('opciones_fecha')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node4 = grammer.nodoDireccion(t[4])
        node5 = grammer.nodoDireccion(t[5])
        node7 = grammer.nodoDireccion(t[7])
        node8 = grammer.nodoDireccion(t[8])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(t[3])
        node.agregar(node4)
        node.agregar(node5)
        node.agregar(t[6])
        node.agregar(node7)
        node.agregar(node8)
        t[0] = node


def p_opciones_fecha4(t):
        'opciones_fecha : current_date pyc'
        node = grammer.nodoDireccion('opciones_fecha')
        node1 = grammer.nodoDireccion(t[2])
        node2 = grammer.nodoDireccion(t[1])
        node.agregar(node2)
        node.agregar(node1)
        t[0] = node


def p_opciones_fecha5(t):
        'opciones_fecha : current_time pyc'
        node = grammer.nodoDireccion('opciones_fecha')
        node1 = grammer.nodoDireccion(t[2])
        node2 = grammer.nodoDireccion(t[1])
        node.agregar(node2)
        node.agregar(node1)
        t[0] = node


def p_opciones_fecha6(t):
        'opciones_fecha : timestamp valor pyc'
        node = grammer.nodoDireccion('opciones_fecha')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[3])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(node2)
        t[0] = node


def p_tipo_date(t):
        '''tipo_date : year
        | month
        | day
        | hour
        | minute
        | second'''
        node = grammer.nodoDireccion('tipo_date')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        t[0] = node


def p_condicion(t):
        '''condicion : pyc'''
        node = grammer.nodoDireccion('condicion')
        node1 = grammer.nodoDireccion(t[1])
        node.agregar(node1)
        t[0] = node


def p_condicion2(t):
        '''condicion : where operacion_logica pyc'''
        node = grammer.nodoDireccion('condicion')
        node1 = grammer.nodoDireccion(t[1])
        node3 = grammer.nodoDireccion(t[3])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(node3)
        t[0] = node


def p_condicion3(t):
        '''condicion : where identificador igual operacion_aritmetica pyc'''
        node = grammer.nodoDireccion('condicion')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node3 = grammer.nodoDireccion(t[3])
        node5 = grammer.nodoDireccion(t[5])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(t[4])
        node.agregar(node5)
        t[0] = node


def p_condicion4(t):
        '''condicion : where exists par1 sentencia_select par2 pyc'''
        node = grammer.nodoDireccion('condicion')
        node1 = grammer.nodoDireccion(t[1])
        node2 = grammer.nodoDireccion(t[2])
        node3 = grammer.nodoDireccion(t[3])
        node5 = grammer.nodoDireccion(t[5])
        node6 = grammer.nodoDireccion(t[6])
        node.agregar(node1)
        node.agregar(node2)
        node.agregar(node3)
        node.agregar(t[4])
        node.agregar(node5)
        node.agregar(node6)
        t[0] = node


def p_condicion5(t):
        'condicion : where operacion_aritmetica in par1 sentencia_select par2 pyc'
        node = grammer.nodoDireccion('condicion')
        node1 = grammer.nodoDireccion(t[1])
        node3 = grammer.nodoDireccion(t[3])
        node4 = grammer.nodoDireccion(t[4])
        node6 = grammer.nodoDireccion(t[6])
        node7 = grammer.nodoDireccion(t[7])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(t[5])
        node.agregar(node6)
        node.agregar(node7)
        t[0] = node


def p_condicion6(t):
        'condicion : where operacion_aritmetica not in par1 sentencia_select par2 pyc'
        node = grammer.nodoDireccion('condicion')
        node1 = grammer.nodoDireccion(t[1])
        node3 = grammer.nodoDireccion(t[3])
        node4 = grammer.nodoDireccion(t[4])
        node5 = grammer.nodoDireccion(t[5])
        node7 = grammer.nodoDireccion(t[7])
        node8 = grammer.nodoDireccion(t[8])
        node.agregar(node1)
        node.agregar(t[2])
        node.agregar(node3)
        node.agregar(node4)
        node.agregar(node5)
        node.agregar(t[6])
        node.agregar(node7)
        node.agregar(node8)
        t[0] = node


def p_op_aritmetica(t):
    '''operacion_aritmetica : par1 operacion_aritmetica par2 operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node1 = grammer.nodoDireccion(t[1])
    node4 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(t[2])
    node.agregar(node4)
    node.agregar(t[4])
    t[0] = node


def p_op_aritmetica2(t):
    '''operacion_aritmetica : valor operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node.agregar(t[1])
    node.agregar(t[2])
    t[0] = node


def p_op_aritmetica3(t):
    '''operacion_aritmetica : sum par1 operacion_aritmetica par2 operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    node.agregar(node4)
    node.agregar(t[5])
    t[0] = node


def p_op_aritmetica4(t):
    '''operacion_aritmetica : avg par1 operacion_aritmetica par2 operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    node.agregar(node4)
    node.agregar(t[5])
    t[0] = node


def p_op_aritmetica5(t):
    '''operacion_aritmetica : max par1 operacion_aritmetica par2 operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    node.agregar(node4)
    node.agregar(t[5])
    t[0] = node


def p_op_aritmetica6(t):
    '''operacion_aritmetica : pi operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    node.agregar(t[2])
    t[0] = node


def p_op_aritmetica7(t):
    '''operacion_aritmetica : power par1 operacion_aritmetica par2 operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    node.agregar(node4)
    node.agregar(t[5])
    t[0] = node


def p_op_aritmetica8(t):
    '''operacion_aritmetica : sqrt par1 operacion_aritmetica par2 operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    node.agregar(node4)
    node.agregar(t[5])
    t[0] = node


def p_op_aritmetica9(t):
    '''operacion_aritmetica : valor between valor operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(t[1])
    node.agregar(node2)
    node.agregar(t[3])
    node.agregar(t[4])
    t[0] = node


def p_op_aritmetica10(t):
    '''operacion_aritmetica : valor is distinct from valor operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(t[1])
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(t[5])
    node.agregar(t[6])
    t[0] = node


def p_op_aritmetica11(t):
    '''operacion_aritmetica : valor is not distinct from valor operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node.agregar(t[1])
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(t[6])
    node.agregar(t[7])
    t[0] = node


def p_op_aritmetica12(t):
    '''operacion_aritmetica : valor is null operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(t[1])
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(t[4])
    t[0] = node


def p_op_aritmetica13(t):
    '''operacion_aritmetica : valor is not null operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(t[1])
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(t[5])
    t[0] = node


def p_op_aritmetica14(t):
    '''operacion_aritmetica : valor is true operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(t[1])
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(t[4])
    t[0] = node


def p_op_aritmetica15(t):
    '''operacion_aritmetica : valor is not true operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(t[1])
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(t[5])
    t[0] = node


def p_op_aritmetica16(t):
    '''operacion_aritmetica : valor is false operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(t[1])
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(t[4])
    t[0] = node


def p_op_aritmetica17(t):
    '''operacion_aritmetica : valor is not false operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(t[1])
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(t[5])
    t[0] = node


def p_operacion_aritmetica_18(t):
    '''operacion_aritmetica : funciones_extras operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(node2)
    t[0] = node


def p_operacion_aritmetica_19(t):
    '''operacion_aritmetica_2 : mas operacion_aritmetica operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(t[3])
    node.agregar(node2)
    node.agregar(t[2])
    t[0] = node


def p_operacion_aritmetica_20(t):
    '''operacion_aritmetica_2 : menos operacion_aritmetica operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(t[3])
    node.agregar(node2)
    node.agregar(t[2])
    t[0] = node


def p_operacion_aritmetica_21(t):
    '''operacion_aritmetica_2 : por operacion_aritmetica operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(t[3])
    node.agregar(node2)
    node.agregar(t[2])
    t[0] = node


def p_operacion_aritmetica_22(t):
    '''operacion_aritmetica_2 : div operacion_aritmetica operacion_aritmetica_2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(t[2])
    node.agregar(node2)
    node.agregar(t[3])
    t[0] = node


def p_operacion_aritmetica_23(t):
    '''operacion_aritmetica_2 : empty'''
    node = grammer.nodoDireccion('vacio')
    node.agregar(t[1])
    t[0] = node


def p_funciones_extras(t):
    '''funciones_extras : math_functions
	| trigonometricas
	| binary_string'''
    node = grammer.nodoDireccion('funciones_extras')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(node2)
    t[0] = node


def p_math_funciones(t):
    '''math_functions : funciones_math1 par1 operacion_aritmetica par2'''
    node = grammer.nodoDireccion('math_funciones')
    node.agregar(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[4])
    node.agregar(t[3])
    node.agregar(node2)
    node.agregar(node3)
    t[0] = node


def p_math_funciones2(t):
    '''math_functions : funciones_math2 par1 operacion_aritmetica coma operacion_aritmetica par2'''
    node = grammer.nodoDireccion('math_funciones')
    node.agregar(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[4])
    node4 = grammer.nodoDireccion(t[6])
    node.agregar(t[3])
    node.agregar(t[5])
    node.agregar(node2)
    node.agregar(node3)
    t[0] = node


def p_math_funciones3(t):
    '''math_functions : width_bucket par1 operacion_aritmetica coma operacion_aritmetica coma operacion_aritmetica coma operacion_aritmetica par2'''
    node = grammer.nodoDireccion('math_funciones')
    node.agregar(t[3])
    node2 = grammer.nodoDireccion(t[1])
    node3 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[8])
    node7 = grammer.nodoDireccion(t[10])
    node.agregar(t[5])
    node.agregar(t[7])
    node.agregar(t[9])
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    t[0] = node


def p_math_funciones4(t):
    '''math_functions : random par1 par2'''
    node = grammer.nodoDireccion('math_funciones')
    node2 = grammer.nodoDireccion(t[1])
    node3 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[3])
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    t[0] = node


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
    | round
    | sign
    | sqrt'''
    node = grammer.nodoDireccion('funciones_math')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(node2)
    t[0] = node


def p_funciones_math2(t):
    '''funciones_math2 : div
    | gcd
    | mod
    | round'''
    node = grammer.nodoDireccion('funciones_math')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(node2)
    t[0] = node


def p_trigonometricas(t):
    '''trigonometricas : funciones_tri par1 operacion_aritmetica par2'''
    node = grammer.nodoDireccion('trigonometricas')
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[4])
    node.agregar(t[1])
    node.agregar(t[3])
    node.agregar(node2)
    node.agregar(node3)
    t[0] = node


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
    node = grammer.nodoDireccion('funciones_tri')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(node2)
    t[0] = node


def p_binary_string(t):
    '''binary_string : funciones_string1 par1 par2'''
    node = grammer.nodoDireccion('binary_string')
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(t[1])
    node.agregar(node2)
    node.agregar(node3)
    t[0] = node


def p_binary_string2(t):
    '''binary_string : funciones_string2 par1 operacion_aritmetica par2'''
    node = grammer.nodoDireccion('binary_string')
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[4])
    node.agregar(t[1])
    node.agregar(t[3])
    node.agregar(node2)
    node.agregar(node3)
    t[0] = node


def p_binary_string3(t):
    '''binary_string : substr par1 operacion_aritmetica coma operacion_aritmetica coma operacion_aritmetica par2'''
    node = grammer.nodoDireccion('binary_string')
    node2 = grammer.nodoDireccion(t[1])
    node3 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[8])
    node.agregar(t[3])
    node.agregar(t[5])
    node.agregar(t[7])
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    t[0] = node


def p_binary_string4(t):
    '''binary_string : funciones_string3 par1 operacion_aritmetica dosp dosp bytea coma operacion_aritmetica par2'''
    node = grammer.nodoDireccion('binary_string')
    node3 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node7 = grammer.nodoDireccion(t[6])
    node8 = grammer.nodoDireccion(t[7])
    node9 = grammer.nodoDireccion(t[9])
    node.agregar(t[1])
    node.agregar(t[3])
    node.agregar(t[8])
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    t[0] = node


def p_binary_string5(t):
    '''binary_string : set_byte par1 operacion_aritmetica dosp dosp bytea coma operacion_aritmetica coma operacion_aritmetica par2'''
    node = grammer.nodoDireccion('binary_string')
    node2 = grammer.nodoDireccion(t[1])
    node3 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[7])
    node8 = grammer.nodoDireccion(t[9])
    node9 = grammer.nodoDireccion(t[11])
    node.agregar(t[3])
    node.agregar(t[10])
    node.agregar(t[8])
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    t[0] = node


def p_binary_string6(t):
    '''binary_string : convert par1 operacion_aritmetica as operacion_aritmetica par2'''
    node = grammer.nodoDireccion('binary_string')
    node2 = grammer.nodoDireccion(t[1])
    node3 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[6])
    node.agregar(t[3])
    node.agregar(t[5])
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    t[0] = node


def p_binary_string7(t):
    '''binary_string : decode par1 operacion_aritmetica coma operacion_aritmetica par2'''
    node = grammer.nodoDireccion('binary_string')
    node2 = grammer.nodoDireccion(t[1])
    node3 = grammer.nodoDireccion(t[2])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[6])
    node.agregar(t[3])
    node.agregar(t[5])
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    t[0] = node

def p_funciones_string(t):
    '''funciones_string1 : trim
    | md5'''
    node = grammer.nodoDireccion('funciones_string')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(node2)
    t[0] = node


def p_funciones_string2(t):
    '''funciones_string2 : length
    | sha256'''
    node = grammer.nodoDireccion('funciones_string')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(node2)
    t[0] = node

def p_funciones_string3(t):
    '''funciones_string3 : get_byte
    | encode'''
    node = grammer.nodoDireccion('funciones_string')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(node2)
    t[0] = node


def p_op_relacional(t):
    '''operacion_relacional : operacion_aritmetica operacion_relacional_2'''
    node = grammer.nodoDireccion('operacion_relacional')
    node.agregar(t[1])
    node.agregar(t[2])
    t[0] = node


def p_op_relacional2(t):
    '''operacion_relacional_2 : mayor operacion_relacional operacion_relacional_2'''
    node = grammer.nodoDireccion('operacion_relacional')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(t[3])
    node.agregar(node2)
    node.agregar(t[2])
    t[0] = node


def p_op_relacional3(t):
    '''operacion_relacional_2 : menor operacion_relacional operacion_relacional_2'''
    node = grammer.nodoDireccion('operacion_relacional')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(t[3])
    node.agregar(node2)
    node.agregar(t[2])
    t[0] = node


def p_op_relacional4(t):
    '''operacion_relacional_2 : mayorigual operacion_relacional operacion_relacional_2'''
    node = grammer.nodoDireccion('operacion_relacional')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(t[3])
    node.agregar(node2)
    node.agregar(t[2])
    t[0] = node


def p_op_relacional5(t):
    '''operacion_relacional_2 : menorigual operacion_relacional operacion_relacional_2'''
    node = grammer.nodoDireccion('operacion_relacional')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(t[3])
    node.agregar(node2)
    node.agregar(t[2])
    t[0] = node


def p_op_relacional6(t):
    '''operacion_relacional_2 : diferente operacion_relacional operacion_relacional_2'''
    node = grammer.nodoDireccion('operacion_relacional')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(t[3])
    node.agregar(node2)
    node.agregar(t[2])
    t[0] = node


def p_op_relacional7(t):
    '''operacion_relacional_2 : igual operacion_relacional operacion_relacional_2'''
    node = grammer.nodoDireccion('operacion_relacional')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(t[3])
    node.agregar(node2)
    node.agregar(t[2])
    t[0] = node


def p_op_relacional8(t):
    '''operacion_relacional_2 : empty'''
    node = grammer.nodoDireccion('vacio')
    node.agregar(t[1])
    t[0] = node


def p_op_logica(t):
    '''operacion_logica : operacion_relacional operacion_logica_2'''
    node = grammer.nodoDireccion('operacion_logica')
    node.agregar(t[1])
    node.agregar(t[2])
    t[0] = node


def p_op_logica2(t):
    '''operacion_logica_2 : and operacion_logica operacion_logica_2'''
    node = grammer.nodoDireccion('operacion_logica')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(t[3])
    node.agregar(node2)
    node.agregar(t[2])
    t[0] = node


def p_op_logica3(t):
    '''operacion_logica_2 : or operacion_logica operacion_logica_2'''
    node = grammer.nodoDireccion('operacion_logica')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(t[3])
    node.agregar(node2)
    node.agregar(t[2])
    t[0] = node


def p_op_logica4(t):
    '''operacion_logica_2 : not operacion_logica operacion_logica_2'''
    node = grammer.nodoDireccion('operacion_logica')
    node2 = grammer.nodoDireccion(t[1])
    node.agregar(t[3])
    node.agregar(node2)
    node.agregar(t[2])
    t[0] = node


def p_op_logica5(t):
    '''operacion_logica_2 : empty'''
    node = grammer.nodoDireccion('vacio')
    node.agregar(t[1])
    t[0] = node


def p_show(t):
    'sentencia_show : show databases show_cont'
    node = grammer.nodoDireccion('sentencia_show')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    t[0] = node


def p_show_cont(t):
    'show_cont : pyc'
    node = grammer.nodoDireccion('show_cont')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_show_cont2(t):
    'show_cont : ins_like pyc'
    node = grammer.nodoDireccion('show_cont')
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(t[1])
    node.agregar(node2)
    t[0] = node


def p_ins_like(t):
    'ins_like : like porcentaje identificador porcentaje'
    node = grammer.nodoDireccion('ins_like')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    t[0] = node


def p_empty(t):
    'empty :'
    node = grammer.nodoDireccion('empty')
    t[0] = node


parser = yacc.yacc()


generar.graficaArbol(parser)


def parse(input):
    print('estoy en el parse');
    resultado = parser.parse(input)
    arbolimas = generar.graficaArbol(resultado)
    arbolimas.ejecutarGrafica()


# f = open("Gramaticas/entrada.txt", "r")
# input = f.read()
# print(input)
# resultado = parser.parse(input)
# arbolimas = generar.graficaArbol(resultado)
# arbolimas.ejecutarGrafica()
