# Construyendo el analizador léxico
import ply.lex as lex
from ts import *
from lex import *
from type_checker import *
from columna import *
from graphviz import Graph

dot = Graph()
dot.attr(splines = 'false')
dot.node_attr.update(fontname = 'Eras Medium ITC', style='filled', fillcolor="tan",
                     fontcolor = 'black', rankdir = 'RL')
dot.edge_attr.update(color = 'black')

lexer = lex.lex()
tabla_simbolos = TablaDeSimbolos()
consola = []
salida = []
nodo_alias = 0
nodo_distinct = 0
type_checker = TypeChecker(tabla_simbolos, tabla_errores, consola, salida)

i = 0
temp_tabla = -1
temp_base = -1
def inc():
    global i 
    i += 1
    return i


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
    id = inc()
    dot.node(str(id), 'INICIO')
    for element in t[1]:
        dot.edge(str(id), str(element['id']))
    for element in tabla_errores.errores:
        print('Error tipo: ', element.tipo, ' Descripción: ', element.descripcion, ' en la línea: ', element.linea)
    
def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    #                   [{'id': id}]  {'id': id}
    t[1].append(t[2])
    #[{'id': id}, {'id': id}, ...]
    t[0] = t[1]


def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]
    # [{'id': id}]

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
    id = inc()
    t[0] = {'id': id}

    if t[1].upper() == 'CREATE':
        t[0] = t[2]

    elif t[1].upper() == 'SHOW':
        t[0] = t[2]

    elif t[1].upper() == 'ALTER':
        t[0] = t[3]

        # if t[2].upper() == 'TABLE':
        #     dot.node(str(id), 'ALTER TABLE')
        # elif t[2].upper() == 'DATABASE':
        #     dot.node(str(id), 'ALTER DATABASE')
        #     dot.edge(str(id), str(t[3]['id']))

    elif t[1].upper() == 'USE':
        t[0] = t[2]
        # dot.node(str(id), 'USE')

        # for element in t[2]:
        #     dot.edge(str(id), str(element['id']))

    elif t[1].upper() == 'SELECT':
        t[0] = t[2]
        # dot.node(str(id), 'SELECT')

    elif t[1].upper() == 'DELETE':
        t[0] = t[2]
        # dot.node(str(id), 'DELETE')

    elif t[1].upper() == 'UPDATE':
        t[0] = t[2]
        # dot.node(str(id), 'UPDATE')

    elif t[1].upper() == 'INSERT':
        t[0] = t[2]
        # dot.node(str(id), 'INSERT E')

    elif t[1].upper() == 'DROP':
        t[0] = t[2]

    
#========================================================

#========================================================
# INSTRUCCION CON "CREATE"
def p_instruccion_creacion(t) :
    '''creacion     : DATABASE crear_bd
                    | OR REPLACE DATABASE crear_bd
                    | TABLE crear_tb
                    | TYPE crear_type'''
    print("Creacion")
    id = inc()
    t[0] = [{'id': id}]

    if t[1].upper() == 'DATABASE':
        t[0] = t[2]
    elif t[1].upper() == 'OR':
        dot.node(str(t[4]['id']), 'CREATE OR REPLACE\nDATABASE')
        t[0] = t[4]
    elif t[1].upper() == 'TABLE':
        t[0] = t[2]
    elif t[1].upper() == 'TYPE':
        dot.node(str(id), 'TYPE')
        
        for element in t[2]:
            dot.edge(str(id), str(element['id']))

def p_instruccion_crear_BD(t) :
    'crear_bd     : ID PTCOMA'
    type_checker.createDatabase(database = t[1].upper(), line = t.lexer.lineno)
    id = inc()
    t[0] = {'id': id}
    id_id = inc()
    dot.node(str(id), 'CREATE DATABASE')
    dot.node(str(id_id), t[1])
    dot.edge(str(id), str(id_id))

def p_instruccion_crear_BD_Parametros(t) :
    'crear_bd     : ID lista_parametros_bd PTCOMA'
    
    id = inc()
    t[0] = {'id': id}
    global temp_base
    id_id = temp_base
    dot.node(str(id), 'CREATE DATABASE')
    dot.node(str(id_id), t[1])
    dot.edge(str(id), str(id_id))

    for element in t[2]['id']:
        dot.edge(str(id), str(element))

    if 'mode' in t[2]:
        type_checker.createDatabase(database = t[1].upper(), mode = t[2]['params']['mode'], line = t.lexer.lineno)
    else:
        type_checker.createDatabase(database = t[1].upper(), line = t.lexer.lineno)

    temp_base = -1

def p_instruccion_crear_BD_Parametros_error(t) :
    'crear_bd   : ID error PTCOMA'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[2], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'ERROR')

def p_instruccion_crear_BD_if_exists(t) :
    'crear_bd       : IF NOT EXISTS ID PTCOMA'
    type_checker.createDatabase(database = t[4].upper(), line = t.lexer.lineno)
    id = inc()
    t[0] = {'id': id}
    id_if = inc()
    id_id = inc()
    dot.node(str(id), 'CREATE DATABASE')
    dot.node(str(id_if), 'IF NOT EXIST')
    dot.node(str(id_id), t[4])
    dot.edge(str(id), str(id_if))
    dot.edge(str(id_if), str(id_id))

def p_instruccion_crear_BD_if_exists_Parametros(t) :
    'crear_bd       : IF NOT EXISTS ID lista_parametros_bd PTCOMA'
    if 'mode' in t[5]:
        type_checker.createDatabase(database = t[4].upper(), mode = t[5]['params']['mode'], line = t.lexer.lineno)
    else:
        type_checker.createDatabase(database = t[4].upper(), line = t.lexer.lineno)

    id = inc()
    t[0] = {'id': id}
    global temp_base
    id_if = inc()
    id_id = temp_base
    dot.node(str(id), 'CREATE DATABASE')
    dot.node(str(id_if), 'IF NOT EXIST')
    dot.node(str(id_id), t[4])
    dot.edge(str(id), str(id_if))
    dot.edge(str(id_if), str(id_id))

    for element in t[5]['id']:
            dot.edge(str(id_if), str(element))
    
    temp_base = -1

def p_instruccion_crear_TB_herencia(t):
    '''crear_tb     : ID PARIZQ crear_tb_columnas PARDER tb_herencia PTCOMA'''
    print("Creación de Tabla con herencia")
    #t[0] = Crear_TB_Herencia(t[1], t[3], t[5])|||
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), t[1])
    for element in t[3]:
        dot.edge(str(id), str(element['id']))
    for element in t[5]:
        dot.edge(str(id), str(element['id']))


def p_instruccion_crear_TB(t):
    '''crear_tb     : ID PARIZQ crear_tb_columnas PARDER PTCOMA'''
    type_checker.createTable(table = t[1], columns = t[3], line = t.lexer.lineno)
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'CREATE TABLE')

    global temp_tabla
    id_id = temp_tabla
    dot.node(str(id_id), t[1])
    dot.edge(str(id), str(id_id))

    id_cols = inc()
    dot.node(str(id_cols), 'COLUMNAS')
    dot.edge(str(id), str(id_cols))
    for element in t[3]:
        if type(element) == list:
            for element2 in element:
                dot.edge(str(id_cols), str(element2['id']))
        else:
            dot.edge(str(id_cols), str(element['id']))
    temp_tabla = -1


def p_isntruccion_crear_TYPE(t) :
    '''crear_type   : ID AS ENUM PARIZQ lista_objetos PARDER PTCOMA
                    '''
    print("Creacion de un type enumerado")
    #t[0] = Crear_Type(t[1], t[5])
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ENUM')
    dot.edge(str(id), 'IDENTIFICADOR\n' + t[1])

    for element in t[5]:
        dot.edge(str(id), str(element['id']))


def p_instruccion_TB_herencia(t) :
    'tb_herencia    : INHERITS PARIZQ ID PARDER'
    #t[0] = Heredero(t[4])
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'INHERITS')
    dot.edge(str(id), t[3])

#========================================================

#========================================================
# INSTRUCCION SHOW DATABASE
def p_instruccion_show(t) :
    '''show_db      : DATABASES
                    | DATABASES LIKE CADENA'''
    id = inc()
    dot.node(str(id), 'SHOW DATABASES')
    t[0] = {'id': id}

    if len(t) == 2:
        type_checker.showDatabase()

    else:
        type_checker.showDatabase(t[3].upper())
        id_er = inc()
        dot.node(str(id_er), t[3] + ' [er]')
        dot.edge(str(id), str(id_er))
        


#========================================================

#========================================================
# INSTRUCCION ALTER DATABASE
def p_instruccion_alter_database(t) :
    '''alter_database   : ID RENAME TO ID
                        | ID OWNER TO def_alter_db'''
    id = inc()
    t[0] = {'id': id}
    if t[2].upper() == 'RENAME':
        type_checker.alterDatabase(databaseOld = t[1].upper(), databaseNew = t[4].upper(), line = t.lexer.lineno)
        dot.node(str(id), 'RENAME TO')
        id_old = inc()
        id_new = inc()
        dot.node(str(id_old), 'OLD ID\n' + t[1])
        dot.node(str(id_new), 'NEW ID\n' + t[4])
        dot.edge(str(id), str(id_old))
        dot.edge(str(id), str(id_new))
        
    elif t[2].upper() == 'OWNER':
        dot.node(str(id), 'OWNER TO')
        dot.edge(str(id), str(t[4]['id']))


def p_def_alter_db(t) :
    '''def_alter_db     : ID
                        | CURRENT_USER
                        | SESSION_USER'''

    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), t[1])

#========================================================

#========================================================

# INSTRUCCION CON "USE"
def p_instruccion_Use_BD(t) :
    'cambio_bd     : ID PTCOMA'
    type_checker.useDatabase(t[1].upper(), line = t.lexer.lineno)

    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), t[1])

#========================================================

#========================================================
# INSTRUCCIONES CON "SELECT"

def p_instruccion_selects(t) :
    '''selects      : lista_parametros FROM lista_parametros inicio_condicional state_fin_query 
                    '''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'SELECT')

    id_id = inc()
    dot.node(str(id_id), 'FIELDS')
    dot.edge(str(id), str(id_id))

    id_from = inc()
    dot.node(str(id_from), 'FROM')
    dot.edge(str(id), str(id_from))

    # id_where = inc()
    # dot.node(str(id_where), 'WHERE')
    # dot.edge(str(id), str(id_where))

    id_campos = inc()
    global nodo_alias
    global nodo_distinct

    for element in t[1]:
        dot.edge(str(id_id), str(element['id']))
        # dot.edge(str(id_id), str(id_campos))
        
    # print("------------->" + str(id_campos))
    # if nodo_alias != 0:
    #     dot.edge(str(id_campos), str(nodo_alias))
    # if nodo_distinct != 0:
    #     dot.edge(str(id_campos), str(nodo_distinct))

    nodo_alias = 0
    nodo_distinct = 0

    for element in t[3]:
        dot.edge(str(id_from), str(element['id']))
        
    if t[4] != []:
        dot.edge(str(id), str(t[4]['id'])) 

    if t[5] != []:
        id_sub = inc()
        dot.node(str(id_sub), 'SECOND QUERY')
        dot.edge(str(id), str(id_sub))
        dot.edge(str(id_sub), str(t[5]['id'])) 
    # for element in t[4]:
    #     # if type(element) !=  str:
    #     dot.edge(str(id), str(element['id']))


def p_instruccion_selects2(t) :
    '''selects      : lista_parametros COMA CASE case_state FROM lista_parametros inicio_condicional state_fin_query inicio_group_by
                    '''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'CASE')
    for element in t[1]:
        dot.edge(str(id), str(element['id']))
    for element in t[4]:
        dot.edge(str(id), str(element['id']))
    for element in t[6]:
        dot.edge(str(id), str(element['id']))
    if t[7] != []:
        dot.edge(str(id), str(t[7]['id'])) 
    # for element in t[7]:
    #     dot.edge(str(id), str(element['id']))


def p_instruccion_selects3(t) :
    '''selects      : fun_trigonometrica state_aliases_field 
                    '''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'SELECT')

    id_id = inc()
    dot.node(str(id_id), 'FUNCION TRIGONOMETRICA')
    dot.edge(str(id), str(id_id))

    dot.edge(str(id_id), str(t[1]['id'])) 

    if t[2] != []:
        dot.edge(str(id_id), str(t[2]['id'])) 

    # for element in t[1]:
    #     dot.edge(str(id), str(element))
    # for element in t[2]:
    #     dot.edge(str(id), str(element))


def p_instruccion_selects4(t) :
    '''selects      : fun_trigonometrica state_aliases_field FROM ID state_aliases_table 
                    '''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'SELECT')

    id_id = inc()
    dot.node(str(id_id), 'FUNCION TRIGONOMETRICA')
    dot.edge(str(id), str(id_id))
    
    id_from = inc()
    dot.node(str(id_from), 'FROM\n' + t[4])
    dot.edge(str(id), str(id_from))

    dot.edge(str(id_id), str(t[1]['id'])) 

    if t[2] != []:
        dot.edge(str(id_id), str(t[2]['id'])) 

    if t[5] != []:
        dot.edge(str(id_from), str(t[5]['id'])) 

    


def p_instruccion_selects5(t) :
    '''selects      : POR FROM select_all 
                    | POR FROM state_subquery inicio_condicional 
                    | GREATEST PARIZQ lista_parametros_funciones PARDER 
                    | LEAST PARIZQ lista_parametros_funciones PARDER 
                    | lista_parametros 
                    '''

    print("selects")
    id = inc()
    t[0] = {'id': id}

    if len(t) >3: 
        if t[1].upper() == '*':
            dot.node(str(id), 'SELECT ALL')
            if len(t) == 4:
                dot.edge(str(id), str(t[3]['id'])) 
                # for element in t[3]:
                #     dot.edge(str(id), str(element['id']))
            else:
                dot.edge(str(id), str(t[3]['id'])) 
                # for element in t[3]:
                #     dot.edge(str(id), str(element['id']))
                if t[4] != []:
                    dot.edge(str(id), str(t[4]['id'])) 
                # for element in t[4]:
                #     dot.edge(str(id), str(element['id']))
        
        if t[1].upper() == 'GREATEST':
            dot.node(str(id), 'GREATEST')
            for element in t[3]:
                dot.edge(str(id), str(element['id']))

        if t[1].upper() == 'LEAST':
            dot.node(str(id), 'LEAST')
            for element in t[3]:
                dot.edge(str(id), str(element['id']))

    else:
        dot.node(str(id), 'SELECT')
        for element in t[1]:
            dot.edge(str(id), str(element['id']))



# def p_instruccion_selects_distinct(t) :
#     '''selects      : DISTINCT POR FROM select_all 
#                     | DISTINCT lista_parametros FROM lista_parametros inicio_condicional 
#                     | DISTINCT lista_parametros 
#                     | DISTINCT lista_parametros COMA CASE case_state FROM lista_parametros inicio_condicional'''
#     id = inc()
#     t[0] = {'id': id}
#     dot.node(str(id), 'SELECT')
#     id_dist = inc()
#     dot.node(str(id_dist), 'DISTINCT')
#     dot.edge(str(id), str(id_dist))

#     if len(t) == 5:
#         for element in t[4]:
#             dot.edge(str(id), str(element['id']))
        
#     elif len(t) == 6:
#         for element in t[2]:
#             dot.edge(str(id), str(element['id']))
#         for element in t[4]:
#             dot.edge(str(id), str(element['id']))
#         if t[5] != []:
#             dot.edge(str(id), str(t[5]['id'])) 
#         # for element in t[5]:
#         #     dot.edge(str(id), str(element['id']))

#     elif t[3].upper() == ',':
#         for element in t[2]:
#             dot.edge(str(id), str(element['id']))

#         dot.edge(str(id), 'CASE')
#         for element in t[5]:
#             dot.edge(str(id), str(element['id']))
#         for element in t[7]:
#             dot.edge(str(id), str(element['id']))
#         for element in t[8]:
#             dot.edge(str(id), str(element['id']))

#     else:
#         for element in t[2]:
#             dot.edge(str(id), str(element['id']))


def p_instruccion_selects_where(t) :
    'inicio_condicional      : WHERE relacional inicio_condicional'
    print("Condiciones (Where)")
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'WHERE')
    dot.edge(str(id), str(t[2]['id'])) 
    if t[3] != []:
        dot.edge(str(id), str(t[3]['id'])) 
    # for element in t[3]:
    #     # if element['id'] != '':
    #     dot.edge(str(id), str(element['id']))

def p_instruccion_selects_sin_where(t) :
    'inicio_condicional      : inicio_group_by'
    t[0] = t[1]
    # print("Condiciones (Where)")

# def p_instruccion_selects_where2(t) :
#     'inicio_condicional      : WHERE lista_condiciones inicio_group_by PTCOMA'
#     print("Condiciones (Where)")
    # id = inc()
    # t[0] = {'id': id}
    # dot.node(str(id), 'ORDER BY')
    # dot.node(str(id), str(t[1]['id'])) 

def p_instruccion_selects_group_by(t) :
    'inicio_group_by      : GROUP BY lista_parametros inicio_having'
    # print("GROUP BY")
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'GROUP BY')
    for element in t[3]:
        dot.edge(str(id), str(element['id']))
    # dot.edge(str(id), str(t[3]['id'])) 
    if t[4] != []:
        dot.edge(str(id), str(t[4]['id'])) 

def p_instruccion_selects_group_by2(t) :
    'inicio_group_by      : inicio_order_by '
    t[0] = t[1]
    # print("NO HAY GROUP BY")
    # id = inc()
    # t[0] = {'id': id}
    # dot.node(str(id), 'ORDER BY')
    # dot.node(str(id), str(t[1]['id'])) 

def p_instruccion_selects_having(t) :
    'inicio_having     : HAVING relacional inicio_order_by'
    # print("HAVING")
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'HAVING')
    dot.edge(str(id), str(t[2]['id'])) 
    # for element in t[2]:
    #     dot.edge(str(id), str(element['id']))
    dot.edge(str(id), str(t[3]['id'])) 
    # for element in t[3]:
    #     dot.edge(str(id), str(element['id']))
    # dot.edge(str(id), str(t[2]['id'])) 
    # dot.edge(str(id), str(t[3]['id'])) 

def p_instruccion_selects_having2(t) :
    'inicio_having      : inicio_order_by '
    t[0] = t[1]
    # print("NO HAY HAVING")
    # id = inc()
    # t[0] = {'id': id}
    # dot.node(str(id), 'ORDER BY')
    # dot.node(str(id), str(t[1]['id'])) 

def p_instruccion_selects_order_by(t) :
    'inicio_order_by      : ORDER BY sorting_rows state_limit'
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'ORDER BY')
    for element in t[3]:
        dot.edge(str(id), str(element['id']))
    
    if t[4] != []:
        dot.edge(str(id), str(t[4]['id'])) 

    # for element in t[4]:
    #     print(">> ***********" + str(element))
    #     dot.edge(str(id), str(element['id']))


def p_instruccion_selects_order_by2(t) :
    'inicio_order_by      : state_limit '
    t[0] = t[1]
    # id = inc()
    # t[0] = {'id': id}
    # dot.node(str(id), 'LIMIT')
    # dot.node(str(id), str(t[1]['id'])) 

def p_instruccion_selects_limit(t) :
    '''state_limit      : LIMIT ENTERO state_offset
                        | LIMIT ALL state_offset'''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'LIMIT\n' + str(t[2]))

    # if t[2].upper() == 'ALL':
    #     dot.edge(str(id), t[2])
    # else:
    #     dot.edge(str(id), t[2])
    if t[3] != []:
        dot.edge(str(id), str(t[3]['id'])) 


def p_instruccion_selects_limit2(t) :
    'state_limit      : state_offset'
    t[0] = t[1]
    # id = inc()
    # t[0] = {'id': id}
    # dot.node(str(id), 'OFFSET')

    # dot.node(str(id), str(t[1]['id'])) 

def p_instruccion_selects_offset(t) :
    '''state_offset         : OFFSET ENTERO state_union 
                            | OFFSET ENTERO state_intersect
                            | OFFSET ENTERO state_except'''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'OFFSET\n' + str(t[2]))
    # dot.edge(str(id), t[2])
    if t[3] != []:
        dot.edge(str(id), str(t[3]['id'])) 


def p_instruccion_selects_offset2(t) :
    '''state_offset      : '''
    t[0] = []


def p_instruccion_state_fin_query(t) :
    '''state_fin_query      : state_union 
                            | state_intersect
                            | state_except
                            | state_subquery
                            |'''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = []

    # id = inc()
    # t[0] = {'id': id}
    # dot.node(str(id), 'OFFSET')
    # dot.node(str(id), str(t[1]['id'])) 

    
def p_instruccion_selects_union(t) :
    '''state_union      : UNION SELECT selects
                        | UNION ALL SELECT selects'''
    id = inc()
    t[0] = {'id': id}

    if t[2].upper() == 'ALL':
        dot.node(str(id), 'ALL UNION')
        dot.edge(str(id), str(t[4]['id'])) 
    else:
        dot.node(str(id), 'UNION')
        dot.edge(str(id), str(t[3]['id']))

    
def p_instruccion_selects_union2(t) :
    'state_union      : '
    t[0] = []
    
def p_instruccion_selects_intersect(t) :
    '''state_intersect      : INTERSECT SELECT selects
                            | INTERSECT ALL SELECT selects'''
    id = inc()
    t[0] = {'id': id}

    if t[2].upper() == 'ALL':
        dot.node(str(id), 'ALL INTERSECT')
        dot.edge(str(id), str(t[4]['id'])) 
    else:
        dot.node(str(id), 'INTERSECT')
        dot.edge(str(id), str(t[3]['id'])) 

    
# def p_instruccion_selects_intersect2(t) :
#     'state_intersect      : PTCOMA'
#     id = inc()
#     t[0] = {'id': id}
#     dot.node(str(id), 'FIN')
    
def p_instruccion_selects_except(t) :
    '''state_except     : EXCEPT SELECT selects
                        | EXCEPT ALL SELECT selects'''
    id = inc()
    t[0] = {'id': id}

    if t[2].upper() == 'ALL':
        dot.node(str(id), 'ALL EXCEPT')
        dot.edge(str(id), str(t[4]['id'])) 
    else:
        dot.node(str(id), 'EXCEPT')
        dot.edge(str(id), str(t[3]['id'])) 

    
# def p_instruccion_selects_except2(t) :
#     'state_except      : PTCOMA'
#     # t[0] = []
#     t[0] = []


def p_instruccion_Select_All(t) :
    'select_all     : ID state_aliases_table inicio_condicional'
    t[0] = Select_All(t[1])
    # print("Consulta ALL para tabla: " + t[1])
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'IDENTIFICADOR\n' + t[1])

    for element in t[2]:
        dot.edge(str(id), str(element['id']))
    # dot.edge(str(id), str(t[2]['id'])) 
    
    if t[3] != []:
        dot.edge(str(id), str(t[3]['id'])) 

#Gramatica para fechas
#========================================================
def p_date_functions1(t):
    '''date_functions   : EXTRACT PARIZQ opcion_date_functions 
                        | NOW PARIZQ PARDER'''
    print("fecha")
    id = inc()
    t[0] = {'id': id}

    if t[1].upper() == 'EXTRACT':
        dot.node(str(id), 'EXTRACT')
        for element in t[3]:
            dot.edge(str(id), str(element['id']))

    elif t[1].upper() == 'NOW':
        dot.node(str(id), 'NOW')
        # dot.edge(str(id), str(t[3]['id'])) 
        # for element in t[3]:
        #     dot.edge(str(id), str(element['id']))

def p_date_functions(t):
    '''date_functions   : date_part PARIZQ opcion_date_functions
                        | opcion_date_functions'''
    print("fecha")

    
    if str(t[1]['valor']) != 'cadenas':
        id = inc()
        t[0] = {'id': id, 'valor': 'date'}
        dot.node(str(id), 'FUNCION FECHA')
        
        if len(t) == 2:
            dot.edge(str(id), str(t[1]['id'])) 
            # for element in t[1]:
            #     dot.edge(str(id), str(element['id']))
        else:
            for element in t[1]:
                dot.edge(str(id), str(element['id']))
            for element in t[3]:
                dot.edge(str(id), str(element['id']))
    else:
        t[0] = t[1]
        # t[0] = {'id': id, 'valor': 'cadenas'}
        # dot.node(str(id), 'CADENAS')
    
    

def p_validate_date(t):
    'lista_date_functions : def_fields FROM TIMESTAMP CADENA PARDER'
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'FROM TIMESTAMP')

    for element in t[1]:
        dot.edge(str(id), str(element['id']))
    dot.edge(str(id), t[4])

    try:
        fecha = re.split('[-: ]',t[4].replace("'",""))
        if (5 < len(fecha)):
            if (int(fecha[0]) and len(fecha[0]) <= 4) and (int(fecha[1]) and int(fecha[1]) <= 12) and (int(fecha[2]) and int(fecha[2]) <= 31) and (int(fecha[3]) and int(fecha[3]) <= 24) and (int(fecha[4]) and int(fecha[4]) <= 60) and (int(fecha[5]) and int(fecha[5]) <= 60):
                print("Formato fecha aceptado")
        elif (2 < len(fecha)):
            if (int(fecha[0]) and len(fecha[0]) <= 4) and (int(fecha[1]) and int(fecha[1]) <= 12) and (int(fecha[2]) and int(fecha[2])):
                print("Formato fecha aceptado")
    except Exception:
        pass


def p_opcion_lista_date_fuctions(t):
    '''opcion_date_functions    : opcion_date_functions lista_date_functions
                                | lista_date_functions
                                '''
    id = inc()

    if len(t) == 2:
        
        if str(t[1]['valor']) != 'cadenas':
            t[0] = {'id': id, 'valor' : 'date'}
            dot.node(str(id), 'FUNCION DATE')
            dot.edge(str(id), str(t[1]['id'])) 
        else:
            t[0] = {'id': id, 'valor' : 'cadenas'}
            dot.node(str(id), 'CADENAS')
            dot.edge(str(id), str(t[1]['id'])) 

    else:
        
        if str(t[2]['valor']) != 'cadenas':
            t[0] = {'id': id, 'valor' : 'date'}
            dot.node(str(id), 'FUNCIONES DATE')
            dot.edge(str(id), str(t[1]['id'])) 
            dot.edge(str(id), str(t[2]['id'])) 
        else:
            dot.node(str(id), 'CADENAS')
            t[0] = {'id': id, 'valor' : 'cadenas'}
            dot.edge(str(id), str(t[1]['id'])) 
            dot.edge(str(id), str(t[2]['id'])) 

        


def p_lista_date_functions(t):
    '''lista_date_functions : TIMESTAMP CADENA
                            | CURRENT_DATE
                            | CURRENT_TIME
                            | PARDER'''
    if len(t) == 2:
        if t[1].upper() != 'PARDER':
            id = inc()
            t[0] = {'id': id, 'valor': 'date'}
            dot.node(str(id), 'FUNCION DATE')
            dot.edge(str(id), t[1])
        else:
            t[0] = t[1]

    elif len(t) == 3:
        id = inc()
        t[0] = {'id': id, 'valor': 'date'}
        dot.node(str(id), 'TIMESTAMP')
        dot.edge(str(id), t[2])

    elif len(t) == 4:
        id = inc()
        t[0] = {'id': id, 'valor': 'cadenas'}
        dot.node(str(id), 'CADENAS')
        dot.edge(str(id), t[1])
        dot.edge(str(id), str(t[3]['id']))  

    else: 
        id = inc()
        t[0] = {'id': id, 'valor': 'date'}
        dot.node(str(id), 'INTERVAL')
        dot.edge(str(id), t[1])
        dot.edge(str(id), t[4])


# Subqueries
def p_state_subquery(t):
    '''state_subquery   : PARIZQ SELECT selects PARDER'''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'SUB-QUERY')
    dot.edge(str(id), str(t[3]['id'])) 
    # for element in t[3]:
    #         dot.edge(str(id), str(element['id']))

def p_state_subquery_error(t) :
    'state_subquery : PARIZQ SELECT error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'ERROR')
#========================================================

    
#========================================================
# INSERT INTO TABLAS
def p_instruccion_Insert_columnas(t) :
    '''insercion    : INTO ID PARIZQ lista_id PARDER VALUES PARIZQ lista_insercion PARDER PTCOMA
                    '''
    print('Insert con columnas')
    #t[0] = Insert(t[2], t[4], t[8])
    #if len(t[4]) != len(t[8]):
        #print('Error, no está insertando la misma cantidad de datos que de columnas')
    #else:
        #print('Insertó')
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'INSERT INTO')
    
    id_id = inc()
    dot.node(str(id_id), 'ID TABLA\n' + t[2])
    dot.edge(str(id), str(id_id))


    id_field = inc()
    dot.node(str(id_field), 'FIELDS')
    dot.edge(str(id), str(id_field))
    # dot.edge(str(id), str(t[4]['id'])) 
    for element in t[4]:
        dot.edge(str(id_field), str(element))
    # dot.edge(str(id_id), str(t[8]['id'])) 
    
    id_val = inc()
    dot.node(str(id_val), 'VALORES A INSERTAR')
    dot.edge(str(id), str(id_val))
    for element in t[8]:
        dot.edge(str(id_val), str(element['id']))

def p_instruccion_insert(t) :
    '''insercion    : INTO ID VALUES PARIZQ lista_insercion PARDER PTCOMA
                    '''
    print('Insert sin columnas')
    id = inc()
    t[0] = {'id': id}
    id_id = inc()
    dot.node(str(id), 'INSERT INTO')
    dot.node(str(id_id), 'ID TABLA\n' + t[2])
    dot.edge(str(id), str(id_id))

    id_val = inc()
    dot.node(str(id_val), 'VALORES A INSERTAR')
    dot.edge(str(id), str(id_val))
    
    for element in t[5]:
        dot.edge(str(id_val), str(element['id']))

#========================================================
# DROP BASES DE DATOS Y TABLAS
def p_instruccion_Drop_BD_exists(t) :
    '''dropear      : DATABASE IF EXISTS ID PTCOMA
                    '''
    type_checker.dropDatabase(database = t[4].upper(), line = t.lexer.lineno)
    id = inc()
    id_id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'DROP DATABASE\nIF EXISTS')
    dot.node(str(id_id), str(t[4]))
    dot.edge(str(id), str(id_id))

def p_instruccion_Drop_BD(t) :
    '''dropear      : DATABASE ID PTCOMA
                    '''
    type_checker.dropDatabase(database = t[2].upper(), line = t.lexer.lineno)
    id = inc()
    id_id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'DROP DATABASE')
    dot.node(str(id_id), str(t[2]))
    dot.edge(str(id), str(id_id))


def p_instruccion_Drop_TB(t) :
    '''dropear      : TABLE ID PTCOMA
                    '''
    #T[0] = DropTabla(t[2])
    id = inc()
    t[0] = [{'id': id}]

    dot.node(str(id), 'TABLE')
    dot.edge(str(id), t[2])

#========================================================

#========================================================
# PARAMETROS PARA CREATE BASE DE DATOS
def p_instrucciones_parametros_BD(t) :
    '''lista_parametros_bd  : parametros_bd
                            | parametros_bd parametros_bd'''
    t[0] = {'id': [t[1]['id']]}
    if len(t) == 3:
        t[1].update(t[2])
        t[0]['id'].append(t[2]['id'])

    t[0]['params'] = t[1]

def p_parametros_BD_owner(t) :
    '''parametros_bd    : OWNER IGUAL ID
                        | OWNER ID'''
    id = inc()

    global temp_base
    if temp_base == -1:
        temp_base = id
        dot.node(str(temp_base), '')
        id = inc()

    dot.node(str(id), 'OWNER')

    id_id = inc()
    if len(t) == 3:
        dot.node(str(id_id), t[2])
        dot.edge(str(id), str(id_id))
        t[0] = {'owner': t[2], 'id': id}
    else:
        dot.node(str(id_id), t[3])
        dot.edge(str(id), str(id_id))
        t[0] = {'owner': t[3], 'id': id}

def p_parametros_BD_Mode(t) :
    '''parametros_bd    : MODE IGUAL ENTERO
                        | MODE ENTERO'''
    id = inc()

    global temp_base
    if temp_base == -1:
        temp_base = id
        dot.node(str(temp_base), '')
        id = inc()

    dot.node(str(id), 'MODE')
    
    id_entero = inc()
    if len(t) == 3:
        dot.node(str(id_entero), str(t[2]))
        dot.edge(str(id), str(id_entero))
        t[0] = {'mode': t[2], 'id': id}
    else:
        dot.node(str(id_entero), str(t[3]))
        dot.edge(str(id), str(id_entero))
        t[0] = {'mode': t[3], 'id': id}


#========================================================

# LISTA DE SORTING ROWS
#========================================================
def p_instrucciones_lista_sorting_rows(t) :
    'sorting_rows    : sorting_rows COMA sort'
    t[1].append(t[3])
    t[0] = t[1]
    # id = inc()
    # t[0] = [{'id': id}]
    # dot.node(str(id), 'SORTING ROWS')

    # for element in t[1]:
    #     dot.edge(str(id), str(element['id']))
    # for element in t[2]:
    #     dot.edge(str(id), str(element['id']))


def p_instrucciones_sort_DESC(t) :   
    'sorting_rows         : sort'
    t[0] = [t[1]]
    # print("sort")
    # id = inc()
    # t[0] = [{'id': id}]
    # dot.node(str(id), 'SORT')

def p_temporalmente_nombres(t) :
    '''sort         : ID ASC
                    | ID DESC
                    | ID'''
    id = inc()
    t[0] = {'id': id}

    if len(t) == 2:
        dot.node(str(id), 'IDENTIFICADOR\n' + t[1])
    else:
        dot.node(str(id),'SORT TYPE\n' +  t[2])
        dot.edge(str(id), 'IDENTIFICADOR\n' +  t[1])

#========================================================

#========================================================
# LISTA DE PARAMETROS DE FUNCINOES
def p_instrucciones_lista_parametros_fun(t) :
    'lista_parametros_funciones    : lista_parametros_funciones COMA valor_dato'
    t[1].append(t[3])
    t[0] = t[1]

def p_instrucciones_parametro_fun(t) :
    'lista_parametros_funciones    : valor_dato '
    t[0] = [t[1]]

def p_valores_fun(t) :
    '''valor_dato        : ID '''   
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'IDENTIFICADOR\n' +  t[1])
    
def p_valores_fun2(t) :
    '''valor_dato        : ENTERO
                         | DECIMAL '''   
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'NUMERO\n' +  str(t[1]))
    
def p_valores_fun3(t) :
    '''valor_dato        : CADENA '''   
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'CADENA\n' +  t[1])
#========================================================

#========================================================
# LISTA DE PARAMETROS
def p_instrucciones_lista_parametros(t) :
    'lista_parametros    : lista_parametros COMA es_distinct parametro state_aliases_field'
    t[1].append(t[4])
    t[0] = t[1]
    # print("Varios parametros")
    # id = inc()
    # t[0] = [{'id': id}]
    # dot.node(str(id), 'LISTA PARAMETROS')

    # for element in t[1]:
    #     dot.edge(str(id), str(element['id']))
    # for element in t[3]:
    #     dot.edge(str(id), str(element['id'])) 
    # for element in t[3]:
    #     dot.edge(str(id), str(element['id']))

    # for element in t[5]:
    #     dot.edge(str(id), str(element['id']))

def p_instrucciones_lista_parametros_error2(t) :
    'lista_parametros   : lista_parametros COMA error state_aliases_field'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[1].append({'id':id})
    t[0] = t[1]
    dot.node(str(id), 'ERROR')

def p_instrucciones_parametro(t) :
    'lista_parametros    : es_distinct parametro state_aliases_field '
    t[0] = [t[2]]
    # print("Un parametro")
    # id = inc()
    # t[0] = {'id': id}
    # dot.node(str(id), 'LISTA PARAMETROS')


    # dot.edge(str(id), str(t[1]['id'])) 

    # for element in t[2]:
    #     dot.edge(str(id), str(element['id']))
    
def p_instrucciones_parametro_error(t) :
    'lista_parametros   : es_distinct error state_aliases_field'
    id = inc()
    t[0] = [{'id':id}]
    dot.node(str(id), 'ERROR')

def p_instrucciones_distinct(t) :
    '''es_distinct      : DISTINCT
                        | '''
    if len(t) == 2:
        id = inc()
        global nodo_distinct
        nodo_distinct = id
        t[0] = {'id': id}
        dot.node(str(id), 'DISTINCT')
    else:
        t[0] = []


def p_parametro_con_tabla(t) :
    '''parametro        : ID PUNTO ID
                        | ID PUNTO POR'''   # ESTO SE HA COLOCADO CUANDO SE SOLICITAN TODAS LAS 
                                            # COLUMNAS DE ALGUNA TABLA INDICADA.
    # t[0] = t[1]
    id = inc()
    t[0] = {'id': id}

    # dot.node(str(id), 'IDENTIFICADOR')
    dot.node(str(id), 'IDENTIFICADOR\n' +  t[1] + '.' + t[3])

def p_parametro_con_tabla_error(t) :
    'parametro  : ID PUNTO error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id),'INDENTIFICADOR\n'+ t[1] +'.ERROR')

def p_parametros_funciones(t) :
    '''parametro         : lista_funciones
                         | funciones_math_esenciales
                         | fun_binario_select
                         | date_functions
                         | state_subquery
                         '''
    t[0] = t[1]
    # id = inc()
    # t[0] = {'id': id}
    # dot.node(str(id), 'FUNCIONES 0')
    # for element in t[1]:
    #     dot.edge(str(id), str(element['id']))

def p_parametros_cadena(t) :
    'parametro         : CADENA'
    # t[0] = t[1]
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'CADENA\n' + str(t[1]))

def p_parametros_numeros(t) :
    '''parametro            : DECIMAL
                            | ENTERO'''
    # t[0] = t[1]
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'VALOR NUMERICO\n' + str(t[1]))

def p_parametro_sin_tabla(t) :
    'parametro        : ID'
    # t[0] = t[1]
    print("Parametro SIN indice de tabla")

    id = inc()
    t[0] = {'id': id}
    # dot.node(str(id), 'IDENTIFICADOR')
    dot.node(str(id), 'IDENTIFICADOR\n' + str(t[1]))

# def p_parametro_con_tabla_alias(t) :
#     '''parametro        : ID AS ID
#                         | ID ID'''
#     t[0] = t[1]
#     # print("Parametro SIN indice de tabla")

#========================================================

#========================================================
# CONTENIDO DE TABLAS EN CREATE TABLE
def p_instrucciones_lista_columnas(t) :
    'crear_tb_columnas      : crear_tb_columnas COMA crear_tb_columna'
    t[1].append(t[3])
    t[0] = t[1]

def p_instrucciones_lista_columnas_error(t) :
    'crear_tb_columnas      : crear_tb_columnas COMA error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[1].append({'id':id})
    t[0] = t[1]
    dot.node(str(id), 'ERROR')

def p_instrucciones_columnas(t) :
    'crear_tb_columnas      : crear_tb_columna'
    t[0] = [t[1]]

def p_instrucciones_columnas_error(t) :
    'crear_tb_columnas  : error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[1], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[0] = [{'id':id}]
    dot.node(str(id), 'ERROR')

def p_instrucciones_columna_parametros(t) :
    'crear_tb_columna       : ID tipos parametros_columna'
    id = inc()

    global temp_tabla
    if temp_tabla == -1:
        temp_tabla = id
        dot.node(str(temp_tabla), '')
        id = inc()

    dot.node(str(id), t[1])
    dot.edge(str(id), str(t[2]['id']))
    id_params = inc()
    dot.node(str(id_params), 'PARAMETROS')
    dot.edge(str(id), str(id_params))

    col = Columna(tipo = t[2], line = t.lexer.lineno)
    
    for parametro in t[3]['parametros']:
        dot.edge(str(id_params), str(parametro['id'])) 
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
    t[0] = {'nombre': t[1], 'col': col, 'id': id}


def p_instrucciones_columna_parametros_error(t) :
    'crear_tb_columna       : ID error parametros_columna'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[2], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[0] = [{'nombre':t[1], 'col':Columna(tipo='ERROR', line = t.lexer.lineno), 'id':id}]
    dot.node(str(id), 'ID')
    dot.edge(str(id),t[1])
    id2 = inc()
    dot.edge(str(id),str(id2))
    dot.node(str(id2),'ERROR')

def p_instrucciones_columna_noparam(t) :
    'crear_tb_columna       : ID tipos'
    id = inc()

    global temp_tabla
    if temp_tabla == -1:
        temp_tabla = id
        dot.node(str(temp_tabla), '')
        id = inc()

    dot.node(str(id), t[1])
    dot.edge(str(id), str(t[2]['id']))

    t[0] = {'nombre': t[1].lower(), 'col': Columna(tipo = t[2], line = t.lexer.lineno), 'id' : id}


def p_instrucciones_columna_pk(t) :
    'crear_tb_columna       : PRIMARY KEY PARIZQ lista_id PARDER'
    #t[0] = LlavesPrimarias(t[4])
    id = inc()
    t[0] = [{'id': id}]
    print('primary key t0 ',t[0])
    dot.node(str(id), ' PRIMARY KEY')
    
    dot.edge(str(id), str(t[4]['id'])) 
    # for element in t[4]:
    #     dot.edge(str(id), str(element['id']))



def p_instrucciones_columna_fk(t) :
    'crear_tb_columna       : FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER'
    if len(t[4]) != len(t[9]):
        print('Error el número de columnas referencias es distinto al número de columnas foraneas')
    else:
        print('Se creó referencia de llave foranea')

    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), ' FOREIGN KEY')
    
    for element in t[4]:
        dot.edge(str(id), str(element['id']))

    dot.node(str(id), t[6] + ' - ' + t[7])
    for element in t[9]:
        dot.edge(str(id), str(element['id']))


def p_instrucciones_columna_check(t) :
    'crear_tb_columna   : chequeo'
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'PARAMETRO')
    
    for element in t[1]:
        dot.edge(str(id), str(element['id']))

def p_instrucciones_columna_unique(t) :
    'crear_tb_columna   : UNIQUE PARIZQ lista_id PARDER'
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'UNIQUE')
    
    for element in t[3]:
        dot.edge(str(id), str(element['id']))

def p_instrucciones_lista_params_columnas(t) :
    'parametros_columna     : parametros_columna parametro_columna'
    t[1]['parametros'].append(t[2])
    #t[1] = {} -> t[0] = {}
    id = inc()
    t[0] = {'id': id, 'parametros': t[1]['parametros']}

def p_instrucciones_lista_params_columnas_error(t) :
    'parametros_columna : parametros_columna error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[2], t.lexer.lineno)
    tabla_errores.agregar(error)
    t[1].update(t[2])
    id2 = inc()
    id = inc()
    t[0] = {'id':id2}
    dot.node(str(id2), 'PARAMETRO')
    dot.edge(str(id2), str(t[1]['id']))
    dot.edge(str(id2), str(id))
    dot.node(str(id),'ERROR')

def p_instrucciones_params_columnas(t) :
    'parametros_columna     : parametro_columna'
    t[0] = {'id': id, 'parametros': [t[1]]}


def p_instrucciones_params_columnas_error(t) :
    'parametros_columna : error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[1], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'PARAMETRO')
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    dot.edge(str(id), str(id2))

def p_instrucciones_parametro_columna_default(t) :
    'parametro_columna      : DEFAULT valor'
    #t[1] = {} -> t[0] = {}
    id = inc()
    t[0] = {'id': id, 'default': t[2]['valor']}
    dot.node(str(id), 'DEFAULT')
    dot.edge(str(id), str(t[2]['id']))

def p_instrucciones_parametro_columna_nul(t) :
    'parametro_columna      : unul'
    t[0] = t[1]


def p_instrucciones_parametro_columna_unique(t) :
    'parametro_columna      : unic'
    t[0] = t[1]

def p_instrucciones_parametro_columna_checkeo(t) :
    'parametro_columna      : chequeo'
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'PARAMETRO')

    dot.edge(str(id), str(t[1]['id'])) 
    # for element in t[1]:
    #     dot.edge(str(id), str(element['id']))

def p_instrucciones_parametro_columna_pkey(t) :
    'parametro_columna      : PRIMARY KEY'
    id = inc()
    t[0] = {'id': id, 'is_primary': 1}
    dot.node(str(id), 'PRIMARY KEY')

def p_instrucciones_parametro_columna_fkey(t) :
    'parametro_columna      : REFERENCES ID'
    id = inc()
    t[0] = {'id': id, 'references': t[2]}
    dot.node(str(id), 'REFERENCES')
    dot.edge(str(id), t[2])

def p_instrucciones_nnul(t) :
    'unul   : NOT NULL'
    t[0] = {'is_null': TipoNull.NOT_NULL}
    id = inc()
    t[0]['id'] = id
    dot.node(str(id), 'NOT NULL')

def p_instrucciones_unul(t) :
    'unul   : NULL'
    t[0] = {'is_null': TipoNull.NULL}
    id = inc()
    t[0]['id'] = id
    dot.node(str(id), 'NULL')

def p_instrucciones_unic_constraint(t) :
    'unic   : CONSTRAINT ID UNIQUE'
    id = inc()
    t[0] = {'id': id, 'is_unique': 1, 'constraint': Constraint(tipo = TipoConstraint.UNIQUE, name = t[2])}
    dot.node(str(id), 'CONSTRAINT ' + t[2] + ' UNIQUE')

def p_instrucciones_unic(t) :
    'unic   : UNIQUE'
    id = inc()
    dot.node(str(id), 'UNIQUE')
    t[0] = {'id': id, 'is_unique': 1}

def p_instrucciones_chequeo_constraint(t) :
    'chequeo    : CONSTRAINT ID CHECK PARIZQ relacional PARDER'
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'CONSTRAINT ' + t[2] + ' CHECK')
    dot.edge(str(id), str(t[5]['id'])) 
    # for element in t[5]:
    #     dot.edge(str(id), str(element['id']))

def p_instrucciones_chequeo_constraint_error(t) :
    'chequeo    : CONSTRAINT ID CHECK PARIZQ error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[5], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'CONSTRAINT '+t[2]+' CHECK')
    id2 = inc()
    dot.edge(str(id), str(id2))
    dot.node(str(id2), 'ERROR')

def p_instrucciones_chequeo(t) :
    'chequeo    : CHECK PARIZQ relacional PARDER'
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'CHECK')
    for element in t[3]:
        dot.edge(str(id), str(element['id']))
    
def p_instrucciones_chequeo_error(t) :
    'chequeo    : CHECK PARIZQ error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[0] = {'id':id}
    id2 = inc()
    dot.node(str(id), 'CHECK')
    dot.node(str(id2),'ERROR')
    dot.edge(str(id), str(id2))
    
#========================================================

#========================================================
# LISTA DE ELEMENTOS REUTILIZABLES
def p_instrucciones_lista_ids(t) :
    'lista_id   : lista_id COMA ID'
    t[1].append(t[3])
    t[0] = t[1]
    # id = inc()
    # t[0] = {'id': id}
    # dot.node(str(id), 'Lista de ID')

    # dot.edge(str(id), str(t[1]['id'])) 
    # dot.edge(str(id), t[3])
def p_instrucciones_lista_ids_error(t) :
    'lista_id   : lista_id COMA error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[1].append({'id':id})
    t[0] = t[1]
    dot.node(str(id), 'ERROR')

def p_instrucciones_lista_id(t) :
    'lista_id   : ID'
    t[0] = [t[1]]
    # id = inc()
    # t[0] = {'id': id}
    # dot.node(str(id), 'ID')
    # dot.edge(str(id), t[1])

def p_isntrucciones_lista_id_error(t) :
    'lista_id   : error'
    #error sintáctico
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[1], t.lexer.lineno)
    tabla_errores.agregar(error)
    print(error.imprimir())
    id = inc()
    t[0] = [{'id':id}]
    dot.node(str(id), 'ERROR')
    

def p_instrucciones_lista_objetos(t) :
    '''lista_objetos  : lista_objetos COMA objeto
                      | CADENA COMA INTERVAL CADENA'''
    # t[1].append(t[3])
    # t[0] = t[1]
    id = inc()
    t[0] = {'id': id}

    if len(t) == 4:
        dot.node(str(id), 'Lista de Objetos')
        for element in t[1]:
            dot.edge(str(id), str(element['id']))
        dot.edge(str(id), t[3])

    else:
        dot.node(str(id), 'INTERVAL')
        dot.edge(str(id), t[1])
        dot.edge(str(id), t[4])

def p_instrucciones_lista_objetos_error2(t) :
    'lista_objetos  : lista_objetos COMA error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[0] = {'id':id}
    dot.edge(str(id), t[1])
    id2 = inc()
    dot.edge(str(id), id2)
    dot.node(str(id2), 'ERROR')

def p_instrucciones_lista_objeto(t) :
    'lista_objetos  : objeto'
    # t[0] = [t[1]]
    id = inc()
    t[0] = {'id': id}

    dot.edge(str(id), str(t[1]['id'])) 
    # for element in t[1]:
    #     dot.edge(str(id), str(element['id']))

# def p_instrucciones_objeto(t) :
#     'objeto       : CADENA'
#     id = inc()
#     t[0] = {'id': id}

#     dot.node(str(id), 'OBJETO')
#     dot.edge(str(id), 'CADENA\n' + t[1])

def p_instrucciones_lista_objeto_error(t) :
    'lista_objetos  : error'
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id',id}
    dot.edge(str(id), str(id2))

def p_instrucciones_objeto2(t) :
    '''objeto       : valor
                    | fun_binario_insert
                    '''
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'OBJETO')
    dot.edge(str(id), str(t[1]['id'])) 



def p_instrucciones_lista_insercion_objeto(t) :
    '''lista_insercion  : lista_insercion COMA objeto
                         '''
    t[1].append(t[3])
    t[0] = t[1]
    #para objetos simples
    # id = inc()
    # t[0] = {'id': id}
    # dot.node(str(id), 'Lista de Insercion')

    # dot.edge(str(id), str(t[1]['id'])) 
    # dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_lista_insercion_objeto_error(t) :
    'lista_insercion    : lista_insercion COMA error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[1].append({'id':id})
    t[0] = t[1]

def p_instrucciones_lista_insercion_select(t) :
    'lista_insercion  : lista_insercion COMA PARIZQ SELECT state_subquery PARDER'
    # t[1].append(t[4])
    # t[0] = t[1]
    #para cuando haya querys select
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'Lista de Insercion')

    for element in t[1]:
        dot.edge(str(id), str(element['id']))

    for element in t[3]:
        dot.edge(str(id), str(element['id']))

def p_instrucciones_insercion_objeto(t) :
    '''lista_insercion  : objeto
                        '''
    t[0] = [t[1]]
    #para un objeto simple
    # id = inc()
    # t[0] = {'id': id}
    # dot.node(str(id), 'Insercion de Objeto')
    # dot.edge(str(id), str(t[1]['id'])) 

def p_instrucciones_insercion_select(t) :
    'lista_insercion  : PARIZQ SELECT state_subquery PARDER'
    t[0] = [t[3]]
    #Para un query select
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'SUB-QUERY')

    for element in t[3]:
        dot.edge(str(id), str(element['id']))

#========================================================

#========================================================

# INSTRUCCION CON "DELETE"
def p_instruccion_delete(t) :
    '''deletes      : delete_condicional
                    | delete_incondicional'''
    print("ELIMINACION")
    t[0] = t[1]
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'DELETE')
    dot.edge(str(id), str(t[1]['id'])) 

def p_instruccion_delete_incondicional(t) :
    'delete_incondicional     : ID PTCOMA'
    t[0] = Delete_incondicional(t[1])
    print("Eliminar tabla: " + t[1])
                    
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'DELETE INCONDICIONAL')
    dot.edge(str(id), 'TABLA\n' + t[1])

def p_instruccion_delete_condicional(t) :
    'delete_condicional     : ID WHERE relacional PTCOMA'
    # t[0] = Delete_incondicional(t[1])
    print("Eliminar tabla: " + t[1])
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'DELETE CONDICIONAL')
    dot.edge(str(id), 'TABLA\n' + t[1])
    
    id_where = inc()
    dot.node(str(id_where), 'COONDICION WHERE')
    dot.edge(str(id), str(id_where))

    dot.edge(str(id_where), str(t[3]['id'])) 


# INSTRUCCION ALTER TABLE
def p_instruccion_alter(t) :
    '''alter_table  : ID def_alter'''
    print("ALTER TABLE")

    id = inc()
    t[0] = {'id': id}
    id_id = inc()
    dot.node(str(id), 'ALTER TABLE')
    dot.node(str(id_id), 'IDENTIFICADOR\n' + t[1])
    dot.edge(str(id), str(id_id))
    dot.edge(str(id_id), str(t[2]['id']))  


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
                    
    id = inc()
    t[0] = {'id': id}

    if t[1].upper() == 'ADD':
        if t[2].upper() == 'COLUMN':
            id_id = inc()
            dot.node(str(id), 'ADD COLUMN')
            dot.node(str(id_id), 'IDENTIFICADOR\n' +  t[3])
            dot.edge(str(id), str(id_id))
            dot.edge(str(id_id), str(t[4]['id']))  
            
        elif t[2].upper() == 'CHECK':
            dot.node(str(id), 'ADD CHECK')
            dot.edge(str(id), str(t[4]['id']))  

        elif t[2].upper() == 'CONSTRAINT':
            dot.node(str(id), 'ADD CONSTRAINT')
            id_id = inc()
            dot.node(str(id_id), 'IDENTIFICADOR\n' +  t[3])
            dot.edge(str(id), str(id_id))
            dot.edge(str(id_id), 'UNIQUE')
            dot.edge(str(id_id), 'COLUMN\n' +  str(t[6]))

        elif t[2].upper() == 'FOREIGN':
            dot.node(str(id), 'ADD FOREIGN KEY')

    elif t[1].upper() == 'DROP':
        if t[2].upper() == 'COLUMN':
            dot.node(str(id), 'DROP COLUMN')
            dot.edge(str(id), 'IDENTIFICADOR\n' +  t[3])

        elif t[2].upper() == 'CONSTRAINT':
            dot.node(str(id), 'DROP CONSTRAINT')
            dot.edge(str(id), 'IDENTIFICADOR\n' +  str(t[3]))

    elif t[1].upper() == 'ALTER':
        dot.node(str(id), 'ALTER COLUMN')
        dot.edge(str(id), 'IDENTIFICADOR\n' +  t[3])

    elif t[1].upper() == 'RENAME':
        id_id1 = inc()
        id_id2 = inc()
        dot.node(str(id), 'RENAME COLUMN')
        dot.node(str(id_id1), 'OLD ID\n' + t[3])
        dot.node(str(id_id2), 'NEW ID\n' + t[5])
        dot.edge(str(id), str(id_id1))
        dot.edge(str(id), str(id_id2))


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
    id = inc()

    if len(t) == 2:
        t[0] = {'tipo': TipoColumna[t[1].upper()], 'id': id}
        dot.node(str(id), 'TIPO DE DATO\n' + t[1])
    else:
        t[0] = {'tipo': TipoColumna['DOUBLE_PRECISION'], 'id': id}
        dot.node(str(id), 'TIPO DE DATO\nDOUBLE_PRECISION')


def p_tipos_2(t) :
    '''tipos        : CHARACTER VARYING PARIZQ ENTERO PARDER'''
    id = inc()

    t[0] = {'tipo': TipoColumna['CHARACTER_VARYING'], 'n': t[4], 'id': id}
    dot.node(str(id), 'TIPO DE DATO\nCHARACTER VARYING')
    id_entero = inc()
    dot.node(str(id_entero), str(t[4]))
    dot.edge(str(id), str(id_entero))


def p_tipos_3(t) :
    '''tipos        : VARCHAR PARIZQ ENTERO PARDER
                    | CHARACTER PARIZQ ENTERO PARDER
                    | CHAR PARIZQ ENTERO PARDER'''   
    id = inc()

    t[0] = {'tipo': TipoColumna[t[1].upper()], 'n': t[3], 'id': id}
    dot.node(str(id), 'TIPO DE DATO\n' + t[1])
    id_entero = inc()
    dot.node(str(id_entero), str(t[3]))
    dot.edge(str(id), str(id_entero))

def p_tipos_4(t) :
    '''tipos        : TIMESTAMP def_dt_types
                    | TIME def_dt_types'''
    id = inc()
    sufix = t[2]['w'] if 'w' in t[2] else ''
    t[0] = {'tipo': TipoColumna[t[1].upper() + sufix], 'id': id}
    if 'p' in t[2]:
        t[0]['p'] = t[2]['p'] 
        
    dot.node(str(id), 'TIPO DE DATO\n' + t[1])
    
    for element in t[2]['id']:
        dot.edge(str(id), str(element))


def p_tipos_5(t) :
    '''tipos        : INTERVAL def_interval'''
    id = inc()
    dot.node(str(id), t[1])

    for element in t[2]['id']:
        dot.edge(str(id), str(element))

    t[0] = t[2]
    t[0].update({'tipo': TipoColumna[t[1].upper()], 'id': id})

    
def p_def_dt_types_1_error(t) :
    '''def_dt_types : PARIZQ error PARDER WITHOUT TIME ZONE
                    | PARIZQ error PARDER WITH TIME ZONE
                    | PARIZQ error PARDER'''

    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[2], t.lexer.lineno)
    tabla_errores.agregar(error)
    print(error.imprimir())
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'ERROR')

def p_def_dt_types_1(t) :
    '''def_dt_types : PARIZQ ENTERO PARDER WITHOUT TIME ZONE
                    | PARIZQ ENTERO PARDER WITH TIME ZONE
                    | PARIZQ ENTERO PARDER'''
    id = inc()
    dot.node(str(id), str(t[2]))
    t[0] = {'p': t[2], 'id': [id]}

    if len(t) > 4:
        id_tz = inc()
        if t[4].lower() == 'without':
            t[0]['w'] = '_WO' 
            dot.node(str(id_tz), 'SIN TIPO DE DATO\nWITHOUT TIME ZONE')
            
        else:
            dot.node(str(id_tz), 'CON TIPO DE DATO\nWITH TIME ZONE')
            t[0]['w'] = '_W' 
        t[0]['id'].append(id_tz)


                    
def p_def_dt_types_2(t) :
    '''def_dt_types : WITHOUT TIME ZONE
                    | WITH TIME ZONE'''
    id = inc()
    
    if t[1].lower() == 'without':
        t[0] = {'id': [id], 'w': '_WO'}
        dot.node(str(id), 'SIN ZONA HORARIA\nWITHOUT TIME ZONE')
    else:
        t[0] = {'id': [id], 'w': '_W'}
        dot.node(str(id), 'CON ZONA HORARIA\nWITH TIME ZONE')

def p_def_interval_1(t) :
    '''def_interval : def_fld_to PARIZQ ENTERO PARDER
                    | def_fld_to'''
    id = inc()
    dot.node(str(id), 'FIELDS')
    t[0] = {'field': t[1], 'id': [id]}

    for element in t[1]['id']:
        dot.edge(str(id), str(element))

    if len(t) == 5:
        id_entero = inc()
        dot.node(str(id_entero), str(t[3]))
        t[0]['p'] = t[3]
        t[0]['id'].append(id_entero)

def p_def_interval_2(t) :
    '''def_interval : PARIZQ ENTERO PARDER'''
    id = inc()
    t[0] = {'p': t[2], 'id': [id]}
    dot.node(str(id), str(t[2]))

def p_def_fld_to(t) :
    '''def_fld_to   : def_fields TO def_fields
                    | def_fields'''
    
    t[0] = t[1]

    if len(t) > 2:
        id = inc()
        dot.node(str(id), 'TO')
        t[0]['destino'] = t[3]['origen']
        dot.edge(str(id), str(t[1]['id'][0]))
        dot.edge(str(id), str(t[3]['id'][0]))
        t[0]['id'][0] = id


def p_def_fields(t) :
    '''def_fields   : YEAR
                    | MONTH
                    | DAY
                    | HOUR
                    | MINUTE
                    | SECOND'''
    id = inc()
    t[0] = {'origen': TipoFields[t[1].upper()], 'id': [id]}
    dot.node(str(id), t[1])


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
    id = inc()
    t[0] = {'id' : id}
    dot.node(str(id),  'OPERACION RELACIONAL')
    
    if len(t) == 4:
        id_op_signo = inc()

        if t[2].upper() == '<=':
            dot.node(str(id_op_signo), 'MENOR O IGUAL')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(t[1]['id'])) 
            dot.edge(str(id_op_signo), str(t[3]['id']))  

        elif t[2].upper() == '<':
            dot.node(str(id_op_signo), 'MENOR')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(t[1]['id'])) 
            dot.edge(str(id_op_signo), str(t[3]['id']))  
            
        elif t[2].upper() == '>=':
            dot.node(str(id_op_signo), 'MAYOR O IGUAL')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(t[1]['id'])) 
            dot.edge(str(id_op_signo), str(t[3]['id']))  
            
        elif t[2].upper() == '>':
            dot.node(str(id_op_signo), 'MAYOR')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(t[1]['id'])) 
            dot.edge(str(id_op_signo), str(t[3]['id']))  
            
        elif t[2].upper() == '=':
            dot.node(str(id_op_signo), 'IGUAL')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(t[1]['id'])) 
            dot.edge(str(id_op_signo), str(t[3]['id']))  
            
        # PARA LOS OPERADORES LOGICOS
        elif t[2].upper() == 'AND':
            dot.node(str(id_op_signo), 'AND')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(t[1]['id'])) 
            dot.edge(str(id_op_signo), str(t[3]['id']))  

        elif t[2].upper() == 'OR':
            dot.node(str(id_op_signo), 'OR')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(t[1]['id'])) 
            dot.edge(str(id_op_signo), str(t[3]['id']))  

    elif len(t) == 5:
        id_op_signo = inc()
        if t[2].upper() == '=':
            dot.node(str(id_op_signo), 'IGUAL IGUAL')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(t[1]['id'])) 
            dot.edge(str(id_op_signo), str(t[4]['id'])) 
    else:
        id_op_signo = inc()
        dot.node(str(id_op_signo), 'NOT')
        dot.edge(str(id), str(id_op_signo))
        dot.edge(str(id_op_signo), str(t[2]['id'])) 

def p_relacional_error(t) :
    '''relacional   : error MENOR aritmetica
                    | error MAYOR aritmetica
                    | error IGUAL IGUAL aritmetica
                    | error MENORIGUAL aritmetica
                    | error MAYORIGUAL aritmetica
                    | error DIFERENTE aritmetica
                    | error NO_IGUAL aritmetica
                    | error IGUAL aritmetica '''
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[1], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id' : id}
    dot.node(str(id),  'OPERACION RELACIONAL')
    
    if len(t) == 4:
        id_op_signo = inc()

        if t[2].upper() == '<=':
            dot.node(str(id_op_signo), 'MENOR O IGUAL')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(id2))
            dot.edge(str(id_op_signo), str(t[3]['id']))  

        elif t[2].upper() == '<':
            dot.node(str(id_op_signo), 'MENOR')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(id2))
            dot.edge(str(id_op_signo), str(t[3]['id']))  
            
        elif t[2].upper() == '>=':
            dot.node(str(id_op_signo), 'MAYOR O IGUAL')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(id2))
            dot.edge(str(id_op_signo), str(t[3]['id']))  
            
        elif t[2].upper() == '>':
            dot.node(str(id_op_signo), 'MAYOR')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(id2))
            dot.edge(str(id_op_signo), str(t[3]['id']))  
            
        elif t[2].upper() == '=':
            dot.node(str(id_op_signo), 'IGUAL')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(id2)) 
            dot.edge(str(id_op_signo), str(t[3]['id']))  
            
        # PARA LOS OPERADORES LOGICOS
        elif t[2].upper() == 'AND':
            dot.node(str(id_op_signo), 'AND')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(id2)) 
            dot.edge(str(id_op_signo), str(t[3]['id']))  

        elif t[2].upper() == 'OR':
            dot.node(str(id_op_signo), 'OR')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(id2)) 
            dot.edge(str(id_op_signo), str(t[3]['id']))  

    elif len(t) == 5:
        id_op_signo = inc()
        if t[2].upper() == '=':
            dot.node(str(id_op_signo), 'IGUAL IGUAL')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(id2)) 
            dot.edge(str(id_op_signo), str(t[4]['id'])) 
    else:
        id_op_signo = inc()
        dot.node(str(id_op_signo), 'NOT')
        dot.edge(str(id), str(id_op_signo))
        dot.edge(str(id_op_signo), str(t[2]['id'])) 

def p_relacional_error2(t) :
    '''relacional   : aritmetica MENOR error
                    | aritmetica MAYOR error
                    | aritmetica IGUAL IGUAL error
                    | aritmetica MENORIGUAL error
                    | aritmetica MAYORIGUAL error
                    | aritmetica DIFERENTE error
                    | aritmetica NO_IGUAL error
                    | aritmetica IGUAL error'''
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id' : id}
    dot.node(str(id),  'OPERACION RELACIONAL')
    
    if len(t) == 4:
        id_op_signo = inc()

        if t[2].upper() == '<=':
            dot.node(str(id_op_signo), 'MENOR O IGUAL')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(t[1]['id'])) 
            dot.edge(str(id_op_signo), str(id2))  

        elif t[2].upper() == '<':
            dot.node(str(id_op_signo), 'MENOR')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(t[1]['id'])) 
            dot.edge(str(id_op_signo), str(id2))  
            
        elif t[2].upper() == '>=':
            dot.node(str(id_op_signo), 'MAYOR O IGUAL')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(t[1]['id'])) 
            dot.edge(str(id_op_signo), str(id2))  
            
        elif t[2].upper() == '>':
            dot.node(str(id_op_signo), 'MAYOR')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(t[1]['id'])) 
            dot.edge(str(id_op_signo), str(id2))  
            
        elif t[2].upper() == '=':
            dot.node(str(id_op_signo), 'IGUAL')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(t[1]['id'])) 
            dot.edge(str(id_op_signo), str(id2))  
            
        # PARA LOS OPERADORES LOGICOS
        elif t[2].upper() == 'AND':
            dot.node(str(id_op_signo), 'AND')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(t[1]['id'])) 
            dot.edge(str(id_op_signo), str(id2))  

        elif t[2].upper() == 'OR':
            dot.node(str(id_op_signo), 'OR')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(t[1]['id'])) 
            dot.edge(str(id_op_signo), str(id2))  

    elif len(t) == 5:
        id_op_signo = inc()
        if t[2].upper() == '=':
            dot.node(str(id_op_signo), 'IGUAL IGUAL')
            dot.edge(str(id), str(id_op_signo))
            dot.edge(str(id_op_signo), str(t[1]['id'])) 
            dot.edge(str(id_op_signo), str(id2)) 
    else:
        id_op_signo = inc()
        dot.node(str(id_op_signo), 'NOT')
        dot.edge(str(id), str(id_op_signo))
        dot.edge(str(id_op_signo), str(id2)) 

def p_relacional_val(t) :
    'relacional   : aritmetica'

    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'Valor Relacional')
    dot.edge(str(id), str(t[1]['id'])) 


def p_relacional(t) :
    '''relacional   : EXISTS state_subquery
                    | NOT EXISTS state_subquery
                    | IN state_subquery
                    | NOT IN state_subquery
                    | ANY state_subquery
                    | ALL state_subquery
                    | SOME state_subquery
                    '''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id),  'SUB - QUERY')
    id_op = inc()

    if t[1].upper() == 'EXISTS':
        dot.node(str(id_op), 'EXISTS')
        dot.edge(str(id), str(id_op))
        dot.edge(str(id_op), str(t[2]['id'])) 

    elif t[1].upper() == 'IN':
        dot.node(str(id_op), 'IN')
        dot.edge(str(id), str(id_op))
        dot.edge(str(id_op), str(t[2]['id'])) 

    elif t[1].upper() == 'NOT':
        if t[2].upper() == 'IN':
            dot.node(str(id_op), 'NOT IN')
            dot.edge(str(id), str(id_op))
            dot.edge(str(id_op), str(t[3]['id']))
        else: 
            dot.node(str(id_op), 'NOT EXISTS')
            dot.edge(str(id), str(id_op))
            dot.edge(str(id_op), str(t[3]['id']))

    elif t[1].upper() == 'ANY':
        dot.node(str(id_op), 'ANY')
        dot.edge(str(id), str(id_op))
        dot.edge(str(id_op), str(t[2]['id'])) 

    elif t[1].upper() == 'ALL':
        dot.node(str(id_op), 'ALL')
        dot.edge(str(id), str(id_op))
        dot.edge(str(id_op), str(t[2]['id'])) 

    elif t[1].upper() == 'SOME':
        dot.node(str(id_op), 'SOME')
        dot.edge(str(id), str(id_op))
        dot.edge(str(id_op), str(t[2]['id'])) 


def p_relacional2(t) :
    '''relacional   : state_between
                    | state_predicate_nulls
                    | state_is_distinct
                    | state_pattern_match
                    '''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'Valor Relacional')
    print("***" + str(t[1]))
    dot.edge(str(id), str(t[1]['id'])) 
        
def p_aritmetica1(t) :
    '''aritmetica   : PARIZQ aritmetica PARDER
                    | PARIZQ relacional PARDER'''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'Valor aritmetico' )
    dot.edge(str(id), str(t[2]['id'])) 

def p_aritmetica(t) :
    '''aritmetica   : aritmetica MAS aritmetica
                    | aritmetica MENOS aritmetica
                    | aritmetica POR aritmetica
                    | aritmetica DIVISION aritmetica
                    | aritmetica MODULO aritmetica
                    | aritmetica EXP aritmetica
                    | valor'''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'Valor aritmetico' )

    if len(t) == 2:
        dot.edge(str(id), str(t[1]['id'])) 
    else:
        dot.edge(str(id), str(t[1]['id'])) 
        dot.edge(str(id), t[2])
        dot.edge(str(id), str(t[3]['id'])) 

def p_aritmetica_error(t) :
    '''aritmetica   : error MAS aritmetica
                    | error MENOS aritmetica
                    | error POR aritmetica
                    | error DIVISION aritmetica
                    | error MODULO aritmetica
                    | error EXP aritmetica
                    | PARIZQ error PARDER'''
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[1], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'Valor aritmetico' )

    if len(t) == 2:
        dot.edge(str(id), str(id2)) 
    else:
        dot.edge(str(id), str(id2)) 
        dot.edge(str(id), t[2])
        dot.edge(str(id), str(t[3]['id'])) 

def p_aritmetica_error2(t) :
    '''aritmetica   : aritmetica MAS error
                    | aritmetica MENOS error
                    | aritmetica POR error
                    | aritmetica DIVISION error
                    | aritmetica MODULO error
                    | aritmetica EXP error'''
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'Valor aritmetico' )

    if len(t) == 2:
        dot.edge(str(id), str(t[1]['id'])) 
    else:
        dot.edge(str(id), str(t[1]['id'])) 
        dot.edge(str(id), t[2])
        dot.edge(str(id), str(id2)) 

def p_aritmetica2(t) :
    '''aritmetica   : funciones_math_esenciales
                    | lista_funciones
                    | fun_binario_select
                    | fun_trigonometrica'''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'Funciones')

    dot.edge(str(id), str(t[1]['id'])) 
    # for element in t[1]:
    #     dot.edge(str(id), str(element['id']))

def p_valor_id(t) :
    '''valor        : ID
                    | ID PUNTO ID'''
    id = inc()
    t[0] = {'id': id}

    if len(t) == 2:
        dot.node(str(id), 'IDENTIFICADOR\n' + str(t[1]))
        # dot.edge(str(id), ' '+ str(t[1]) )
    else:
        dot.node(str(id), 'FIELD\n' + t[1] + t[2] + t[3])
        # dot.edge(str(id), t[1] + t[2] + t[3])

def p_valor_num(t) :
    '''valor        : ENTERO
                    | DECIMAL  '''
    id = inc()
    t[0] = {'id': id, 'valor': t[1]}
    dot.node(str(id), 'NUMERO\n'+ str(t[1]))
    # dot.edge(str(id), ' '+ str(t[1]) )

def p_valor(t) :
    '''valor        : CADENA
                    '''
    id = inc()
    t[0] = {'id': id, 'valor': t[1]}
    dot.node(str(id), 'CADENA\n'+ str(t[1]))
    # dot.edge(str(id), ' '+ str(t[1]) )

def p_valor2(t) :
    '''valor        : lista_funciones_where
                    | fun_binario_where
                    | state_subquery
                    | fun_trigonometrica
                    | fun_binario_update
                    | fun_binario_select
                    '''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'FUNCIONES')
    # for element in t[1]:
    #     dot.edge(str(id), str(element['id']))
        
    dot.edge(str(id), str(t[1]['id'])) 


def p_valor3(t) :
    '''valor        : date_functions
                    '''
    id = inc()

    # if str(t[1]['valor']) != 'cadenas':
    #     t[0] = {'id': id, 'valor': 'date'}
    #     dot.node(str(id), 'Funciones')
    # else:
    t[0] = {'id': id, 'valor': 'cadenas'}
    dot.node(str(id), 'FUNCIONES DE FECHA')

    dot.edge(str(id), str(t[1]['id'])) 

def p_valor_error(t) :
    'valor  : error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[1], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'ERROR')

def p_instruccion_update_where(t) :
    '''update_table : ID SET def_update WHERE relacional'''
    print("UPDATE TABLE")
    id = inc()
    t[0] = {'id': id}
    
    dot.node(str(id), 'UPDATE')
    dot.edge(str(id), 'TABLA\n' + t[1])

    id_id = inc()
    dot.node(str(id_id), 'WHERE')
    dot.edge(str(id), str(id_id))
    # dot.edge(str(id_id), t[1])

    for element in t[3]:
        dot.edge(str(id), str(element['id']))
    dot.edge(str(id_id), str(t[5]['id'])) 

def p_instruccion_update(t) :
    '''update_table : ID SET def_update'''
    print("UPDATE TABLE")
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'UPDATE')
    dot.edge(str(id), 'TABLA\n' + t[1])

    for element in t[3]:
        dot.edge(str(id), str(element['id']))

def p_def_update_rec(t) :
    '''def_update   : def_update COMA def_update_asig'''
    t[1].append(t[3])
    t[0] = t[1]
    # id = inc()
    # t[0] = {'id': id}

    # # dot.edge(str(id), str(t[1]['id'])) 

    # dot.node(str(id), 'ASIGNACION 0')
    
    # dot.edge(str(id), str(t[1]['id'])) 
    # dot.edge(str(id), 'IDENTIFICADOR\n' + t[3])
    # dot.edge(str(id), str(t[5]['id'])) 

def p_def_update_rec_error2(t) :
    'def_update : def_update COMA error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    dot.node(str(id), 'ERROR')
    t[1].append({'id':id})
    t[0] = t[1]

def p_def_update(t) :
    '''def_update   : def_update_asig'''
    t[0] = [t[1]]
    # id = inc()
    # t[0] = {'id': id}
    # dot.node(str(id), 'ASIGNACION')
    # dot.edge(str(id), 'IDENTIFICADOR\n' + t[1])
    # dot.edge(str(id), str(t[3]['id'])) 

def p_def_update_error(t) :
    'def_update : error'
    id = inc()
    dot.node(str(id), 'ERROR')
    t[0] = [{'id':id}]

def p_def_update_2(t) :
    '''def_update_asig   : ID IGUAL valor'''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'ASIGNACION')
    dot.edge(str(id), 'IDENTIFICADOR\n' + t[1])
    dot.edge(str(id), str(t[3]['id'])) 

# BETWEEN
#=======================================================
def p_between(t) :
    '''state_between    : valor BETWEEN valor AND valor
                        | valor NOT BETWEEN valor AND valor
                        | valor NOT IN state_subquery'''
    id = inc()
    t[0] = {'id': id}

    if t[2].upper() == 'NOT':
        if t[3].upper() == 'IN':
            dot.node(str(id), 'NOT IN')
            dot.edge(str(id), str(t[1]['id'])) 

            dot.edge(str(id), str(t[4]['id'])) 
            # for element in t[4]:
            #     dot.edge(str(id), str(element['id']))
        else:
            dot.node(str(id), 'NOT BETWEEN')
            dot.edge(str(id), str(t[1]['id'])) 
            id_and = inc()
            dot.node(str(id_and), 'AND')
            dot.edge(str(id), str(id_and))
            dot.edge(str(id_and), str(t[4]['id'])) 
            dot.edge(str(id_and), str(t[6]['id'])) 
    else:
        dot.node(str(id), 'BETWEEN')
        dot.edge(str(id), str(t[1]['id'])) 
        id_and = inc()
        dot.node(str(id_and), 'AND')
        dot.edge(str(id), str(id_and))
        dot.edge(str(id_and), str(t[3]['id'])) 
        dot.edge(str(id_and), str(t[5]['id'])) 

#=======================================================

# IS [NOT] DISTINCT
#=======================================================
def p_is_distinct(t) :
    '''state_is_distinct    : valor IS DISTINCT FROM valor state_aliases_table
                            | valor IS NOT DISTINCT FROM valor state_aliases_table'''
    id = inc()
    t[0] = {'id': id}

    if t[3].upper() == 'NOT':
        dot.node(str(id), 'IS NOT DISTINCT')
        dot.edge(str(id), str(t[1]['id'])) 
        dot.edge(str(id), str(t[6]['id'])) 
        # dot.edge(str(id), t[6] + ' [table]')

        for element in t[7]:
            dot.edge(str(id), str(element['id']))
    else:
        dot.node(str(id), 'IS DISTINCT')
        dot.edge(str(id), str(t[1]['id'])) 
        dot.edge(str(id), str(t[5]['id'])) 
        # dot.edge(str(id), t[5] + ' [table]')

        # dot.edge(str(id), str(t[6]['id'])) 
        # for element in t[6]:
        #     dot.edge(str(id), str(element['id']))
#=======================================================


# ESTADO PREDICATES
#=======================================================
def p_predicate_nulls(t) :
    '''state_predicate_nulls        : valor IS NULL
                                    | valor IS NOT NULL
                                    | valor ISNULL
                                    | valor NOTNULL'''
    id = inc()
    t[0] = {'id': id}


    if t[2].upper() == 'IS':
        if t[3].upper() == 'NOT':
            dot.node(str(id), 'PREDICATES\nIS NOT NULL')
            dot.edge(str(id), str(t[1]['id'])) 
        else:
            dot.edge(str(id), 'PREDICATES\nIS NULL')
            dot.edge(str(id), str(t[1]['id'])) 
    else:
        dot.node(str(id), 'PREDICATES\n' + t[2])
        dot.edge(str(id), str(t[1]['id'])) 
#=======================================================


# # Pattern Matching
# #=======================================================
def p_matchs(t) :
    '''state_pattern_match      : aritmetica LIKE CADENA'''
    print("LIKE")
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'Pattern Match')

    # dot.edge(str(id), t[1])
    dot.edge(str(id), str(t[1]['id'])) 
    dot.edge(str(id), t[3])
# #=======================================================


# ESTADOS PARA LOS ALIAS
# #=======================================================
# PARA LAS TABLAS
# -------------------------------------------------------
def p_aliases_table(t):
    ''' state_aliases_table     : AS ID
                                | ID'''
    id = inc()
    t[0] = {'id': id}

    if len(t) == 2:
        dot.node(str(id), 'ALIAS\n' + t[1])

    else:
        dot.node(str(id), 'ALIAS\n' + t[2])


def p_aliases_table2(t):
    ' state_aliases_table     : '
    t[0] = []
# -------------------------------------------------------

# PARA LOS CAMPOS
# -------------------------------------------------------
def p_aliases_field(t):
    ''' state_aliases_field     : AS CADENA
                                | AS ID
                                | ID
                                '''
    print("alias de campos")
    id = inc()
    global nodo_alias
    nodo_alias = id
    t[0] = {'id': id}
    
    if len(t) == 3:
        dot.node(str(id), 'ALIAS AS\n' + t[2])
    else:
        dot.node(str(id), 'ALIAS\n' + t[1])

def p_aliases_field2(t):
    ' state_aliases_field     : '
    t[0] = []
# -------------------------------------------------------
# #=======================================================


# CASE
#========================================================
def p_case_state(t):
    ''' case_state    : case_state auxcase_state END
                      | auxcase_state END'''
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'CASE')
    if len == 3:
        for element in t[1]:
            dot.edge(str(id), str(element['id']))
        dot.edge(str(id), 'END')
    else:
        dot.edge(str(id), str(t[1]['id'])) 
            
    dot.edge(str(id), str(t[2]['id'])) 
    dot.edge(str(id), 'END')
                      
def p_auxcase_state(t):
    'auxcase_state  : WHEN relacional THEN CADENA'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'WHEN')
    dot.edge(str(id), str(t[2]['id']))
        
    dot.edge(str(id), t[4])

def p_auxcase_state2(t):
    'auxcase_state  : ELSE COMILLA_SIMPLE ID COMILLA_SIMPLE'
    id = inc()
    t[0] = [{'id': id}]

    dot.node(str(id), 'ELSE')
    dot.edge(str(id), t[3])
#========================================================

# FUNCIONES MATEMÁTICAS
def p_instrucciones_funcion_count(t):
    '''funciones_math_esenciales    : COUNT PARIZQ lista_funciones_math_esenciales PARDER parametro
                                    | COUNT PARIZQ lista_funciones_math_esenciales PARDER'''
    id = inc()
    t[0] = [{'id': id}]

    dot.node(str(id), 'COUNT')
    if len == 5:
        for element in t[3]:
            dot.edge(str(id), str(element['id']))
    else:
        for element in t[3]:
            dot.edge(str(id), str(element['id']))
        dot.edge(str(id), t[5])

def p_instrucciones_funcion_sum(t):
    '''funciones_math_esenciales    : SUM PARIZQ lista_funciones_math_esenciales PARDER parametro
                                    | SUM PARIZQ lista_funciones_math_esenciales PARDER'''
    id = inc()
    t[0] = [{'id': id}]

    dot.node(str(id), 'SUM')
    if len == 5:
        for element in t[3]:
            dot.edge(str(id), str(element['id']))
    else:
        for element in t[3]:
            dot.edge(str(id), str(element['id']))
        dot.edge(str(id), t[5])

def p_instrucciones_funcion_avg(t):
    '''funciones_math_esenciales    : AVG PARIZQ lista_funciones_math_esenciales PARDER parametro
                                    | AVG PARIZQ lista_funciones_math_esenciales PARDER'''
    id = inc()
    t[0] = [{'id': id}]

    dot.node(str(id), 'AVG')
    if len == 5:
        for element in t[3]:
            dot.edge(str(id), str(element['id']))
    else:
        for element in t[3]:
            dot.edge(str(id), str(element['id']))
        dot.edge(str(id), t[5])

def p_lista_instrucciones_funcion_math(t):
    '''lista_funciones_math_esenciales  : aritmetica
                                        | lista_id
                                        | POR'''
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), t[0])

#SOLO ESTOS SE PUEDEN USAR EN EL WHERE
def p_instrucciones_funcion_abs_where(t) :
    'lista_funciones_where    : ABS PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = [{'id': id}]

    dot.node(str(id), 'ABS')
    dot.edge(str(id), str(t[3]['id'])) 
    # for element in t[3]:
    #     dot.edge(str(id), str(element['id']))


def p_instrucciones_funcion_cbrt_where(t) :
    'lista_funciones_where    : CBRT PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = [{'id': id}]

    dot.node(str(id), 'CBRT')
    dot.edge(str(id), str(t[3]['id'])) 
    # for element in t[3]:
    #     dot.edge(str(id), str(element['id']))

def p_instrucciones_funcion_ceil_where(t) :
    'lista_funciones_where    : CEIL PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = [{'id': id}]

    dot.node(str(id), 'CEIL')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_cieling_where(t) :
    'lista_funciones_where    : CEILING PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'CEILING')
    dot.edge(str(id), str(t[3]['id'])) 

#ESTOS SE USAN EN EL SELECT
def p_instrucciones_funcion_abs_select(t) :
    'lista_funciones    : ABS PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ABS')
    dot.edge(str(id), str(t[3]['id'])) 
    # for element in t[3]:
    #     dot.edge(str(id), str(element['id']))

def p_instrucciones_funcion_cbrt_select(t) :
    'lista_funciones    : CBRT PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'CBRT')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_ceil_select(t) :
    'lista_funciones    : CEIL PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'CEIL')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_cieling_select(t) :
    'lista_funciones    : CEILING PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'CEILING')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_degrees(t) :
    'lista_funciones    : DEGREES PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'DEGREES')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_div(t) :
    'lista_funciones    : DIV PARIZQ funcion_math_parametro COMA ENTERO PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'DIV')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_exp(t) :
    'lista_funciones    : EXP PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'EXP')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_factorial(t) :
    'lista_funciones    : FACTORIAL PARIZQ ENTERO PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'FACTORIAL')
    dot.edge(str(id), t[3])

def p_instrucciones_funcion_floor(t) :
    'lista_funciones    : FLOOR PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'FLOOR')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_gcd(t) :
    'lista_funciones    : GCD PARIZQ ENTERO COMA ENTERO PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'GCD')
    dot.edge(str(id), t[3] + ', ' + t[5])

def p_instrucciones_funcion_ln(t) :
    'lista_funciones    : LN PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'LN')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_log(t) :
    'lista_funciones    : LOG PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'LOG')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_mod(t) :
    'lista_funciones    : MOD PARIZQ funcion_math_parametro COMA ENTERO PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'MOD')
    dot.edge(str(id), str(t[3]['id'])) 

    dot.edge(str(id), t[5])

def p_instrucciones_funcion_pi(t) :
    'lista_funciones    : PI PARIZQ PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'PI')

def p_instrucciones_funcion_power(t) :
    'lista_funciones    : POWER PARIZQ funcion_math_parametro COMA ENTERO PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'POWER')
    dot.edge(str(id), str(t[3]['id'])) 

    dot.edge(str(id), t[5])

def p_instrucciones_funcion_radians(t) :
    'lista_funciones    : RADIANS PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'RADIANS')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_round(t) :
    'lista_funciones    : ROUND PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ROUND')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_sign(t) :
    'lista_funciones    : SIGN PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SIGN')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_sqrt(t) :
    'lista_funciones    : SQRT PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SQRT')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_width_bucket(t) :
    'lista_funciones    : WIDTH_BUCKET PARIZQ funcion_math_parametro COMA funcion_math_parametro COMA funcion_math_parametro COMA funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'WIDTH_BUCKET')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]['id'])) 
    dot.edge(str(id), str(t[7]['id'])) 
    dot.edge(str(id), str(t[9]['id'])) 
    # for element in t[5]:
    #     dot.edge(str(id), str(element['id']))
    # for element in t[7]:
    #     dot.edge(str(id), str(element['id']))
    # for element in t[9]:
    #     dot.edge(str(id), str(element['id']))

def p_instrucciones_funcion_trunc(t) :
    'lista_funciones    : TRUNC PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'TRUNC')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_random(t) :
    'lista_funciones    : RANDOM PARIZQ PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'RANDOM')

def p_instrucciones_funcion_math_parametro(t) :
    '''funcion_math_parametro   : ENTERO
                                | ID
                                | DECIMAL
                                '''
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'PARAMETRO' + str(t[0]))
    # dot.edge(str(id), t[3])

def p_instrucciones_funcion_math_parametro_error(t) :
    'funcion_math_parametro : error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[1], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'ERROR')
    
def p_instrucciones_funcion_math_parametro2(t) :
    '''funcion_math_parametro   : funcion_math_parametro_negativo'''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'FUNCION MATEMATICA')
    dot.edge(str(id), str(t[1]['id'])) 

def p_instrucciones_funcion_math_parametro_negativo(t) :
    '''funcion_math_parametro_negativo  : MENOS DECIMAL
                                        | MENOS ENTERO'''
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'NUMERO NEGATIVO\n' + str(t[2]))

#========================================================

#========================================================
# FUNCIONES TRIGONOMÉTRICAS

#El unico valor que aceptan es double y devuelven un double
def p_instrucciones_funcion_trigonometrica_acos(t) :
    'fun_trigonometrica : ACOS PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ACOS')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ACOS')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_asin(t) :
    'fun_trigonometrica : ASIN PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ASIN')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ASIN')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_atan(t) :
    'fun_trigonometrica : ATAN PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ATAN')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ATAN')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_atan2(t) :
    'fun_trigonometrica : ATAN2 PARIZQ aritmetica COMA aritmetica PARDER'
    print('Ejecuta Funcion ATAN2')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ATAN2')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]['id'])) 

def p_instrucciones_funcion_trigonometrica_cos(t) :
    'fun_trigonometrica : COS PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion COS')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'COS')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_cot(t) :
    'fun_trigonometrica : COT PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion COT')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'COT')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_sin(t) :
    'fun_trigonometrica : SIN PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion SIN')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SIN')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_tan(t) :
    'fun_trigonometrica : TAN PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion TAN')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'TAN')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_acosd(t) :
    'fun_trigonometrica : ACOSD PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ACOSD')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ACOSD')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_asind(t) :
    'fun_trigonometrica : ASIND PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ASIND')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ASIND')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_atand(t) :
    'fun_trigonometrica : ATAND PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ATAND')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ATAND')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_atan2d(t) :
    'fun_trigonometrica : ATAN2D PARIZQ aritmetica COMA aritmetica PARDER'
    print('Ejecuta Funcion ATAN2D')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ACATAN2DOS')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]['id'])) 

def p_instrucciones_funcion_trigonometrica_cosd(t) :
    'fun_trigonometrica : COSD PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion COSD')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'COSD')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_cotd(t) :
    'fun_trigonometrica : COTD PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion COTD')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'COTD')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_sind(t) : 
    'fun_trigonometrica : SIND PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion SIND')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SIND')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_tand(t) :
    'fun_trigonometrica : TAND PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion TAND')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'TAND')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_sinh(t) :
    'fun_trigonometrica : SINH PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion SINH')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SINH')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_cosh(t) :
    'fun_trigonometrica : COSH PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion COSH')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'COSH')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_tanh(t) :
    'fun_trigonometrica : TANH PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion TANH')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'TANH')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_asinh(t) :
    'fun_trigonometrica : ASINH PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ASINH')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ASINH')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_acosh(t) :
    'fun_trigonometrica : ACOSH PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ACOSH')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ACOSH')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_trigonometrica_atanh(t) :
    'fun_trigonometrica : ATANH PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ATANH')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ATANH')
    dot.edge(str(id), str(t[3]['id'])) 
#========================================================

#========================================================
# BINARY STRING FUNCTIONS
def p_instrucciones_funcion_binary_string_length_select(t) :
    'fun_binario_select    : LENGTH PARIZQ valor PARDER'
    print('Ejecuta Funcion length')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'LENGTH')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instruccciones_funcion_binary_string_length_select_error(t) :
    'fun_binario_select : LENGTH PARIZQ error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'LENGTH')
    dot.edge(str(id), str(id2))

def p_instrucciones_funcion_binary_string_length_where(t) :
    'fun_binario_where    : LENGTH PARIZQ valor PARDER'
    print('Ejecuta Funcion length')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'LENGTH')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_binary_string_length_where_error(t) :
    'fun_binario_where  : LENGTH PARIZQ error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'LENGTH')
    dot.edge(str(id), str(id2))

def p_instrucciones_funcion_binary_string_substring_select(t) :
    'fun_binario_select    : SUBSTRING PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta Funcion substring')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_substring_select_error(t) :
    'fun_binario_select : SUBSTRING PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(id2))
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_substring_insert(t) :
    'fun_binario_insert    : SUBSTRING PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta Funcion substring')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_substring_insert_error(t) :
    'fun_binario_insert : SUBSTRING PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(id2))
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_substring_update(t) :
    'fun_binario_update    : SUBSTRING PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta Funcion substring')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_substring_update_error(t) :
    'fun_binario_update : SUBSTRING PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(id2))
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_substring_where(t) :
    'fun_binario_where    : SUBSTRING PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta Funcion substring')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SUBSTRING')
    # dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_substring_where_error(t) :
    'fun_binario_where  : SUBSTRING PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(id2))
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_trim_select(t) :
    'fun_binario_select    : TRIM PARIZQ CADENA FROM valor PARDER'
    print('Ejecuta Funcion trim')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'TRIM')
    dot.edge(str(id), t[3])
    dot.edge(str(id), str(t[5]['id'])) 

def p_instrucciones_funcion_binary_string_trim_select_error(t) :
    'fun_binario_select : TRIM PARIZQ CADENA FROM error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[5], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'TRIM')
    dot.edge(str(id), str(t[3]))
    dot.edge(str(id), str(id2))

def p_instrucciones_funcion_binary_string_trim_insert(t) :
    'fun_binario_insert    : TRIM PARIZQ CADENA FROM valor PARDER'
    print('Ejecuta Funcion trim')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'TRIM')
    dot.edge(str(id), t[3])
    dot.edge(str(id), str(t[5]['id'])) 

def p_instrucciones_funcion_binary_string_trim_insert_error(t) :
    'fun_binario_insert : TRIM PARIZQ CADENA FROM error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[5], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'TRIM')
    dot.edge(str(id), str(t[3]))
    dot.edge(str(id), str(id2))
    
def p_instrucciones_funcion_binary_string_trim_update(t) :
    'fun_binario_update    : TRIM PARIZQ CADENA FROM valor PARDER'
    print('Ejecuta Funcion trim')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'TRIM')
    dot.edge(str(id), t[3])
    dot.edge(str(id), str(t[5]['id'])) 

def p_instrucciones_funcion_binary_string_trim_update_error(t) :
    'fun_binario_update : TRIM PARIZQ CADENA FROM error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[5], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'TRIM')
    dot.edge(str(id), str(t[3]))
    dot.edge(str(id), str(id2))

def p_instrucciones_funcion_binary_string_trim_where(t) :
    'fun_binario_where    : TRIM PARIZQ CADENA FROM valor PARDER'
    print('Ejecuta Funcion trim')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'TRIM')
    dot.edge(str(id), t[3])
    dot.edge(str(id), str(t[5]['id'])) 

def p_instrucciones_funcion_binary_string_trim_where_error(t) :
    'fun_binario_where  : TRIM PARIZQ CADENA FROM error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[5], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'TRIM')
    dot.edge(str(id), str(t[3]))
    dot.edge(str(id), str(id2))

def p_instrucciones_funcion_binary_string_md5_insert(t) :
    'fun_binario_insert : MD5 PARIZQ valor PARDER'
    print('Ejecuta Funcion md5')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'MD5')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_binary_string_md5_insert_error(t) :
    'fun_binario_insert : MD5 PARIZQ error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'MD5')
    dot.edge(str(id), str(id2))

def p_instrucciones_funcion_binary_string_md5_update(t) :
    'fun_binario_update : MD5 PARIZQ valor PARDER'
    print('Ejecuta Funcion md5')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'MD5')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_binary_string_md5_update_error(t) :
    'fun_binario_update : MD5 PARIZQ error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'MD5')
    dot.edge(str(id), str(id2))

def p_instrucciones_funcion_binary_string_sha256_select(t) :
    'fun_binario_select : SHA256 PARIZQ valor PARDER'
    print('Ejecuta Funcion sha256')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SHA256')
    dot.edge(str(id), str(t[3]['id'])) 

def p_instrucciones_funcion_binary_string_sha256_select_error(t) :
    'fun_binario_select : SHA256 PARIZQ error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'SHA256')
    dot.edge(str(id), str(id2))

def p_instrucciones_funcion_binary_string_substr_select(t) :
    'fun_binario_select : SUBSTR PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta Funcion substr')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_substr_select_error(t) :
    'fun_binario_select : SUBSTR PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(id2))
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_substr_insert(t) :
    'fun_binario_insert : SUBSTR PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta Funcion substr')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_substr_insert_error(t) :
    'fun_binario_insert : SUBSTR PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(id2))
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_substr_update(t) :
    'fun_binario_update : SUBSTR PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta Funcion substr')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_substr_update_error(t) :
    'fun_binario_update : SUBSTR PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(id2))
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_substr_where(t) :
    'fun_binario_where : SUBSTR PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta Funcion substr')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_substr_where_error(t) :
    'fun_binario_where  : SUBSTR PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(id2))
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_get_byte(t) :
    'fun_binario_select : GET_BYTE PARIZQ valor DOS_PUNTOS DOS_PUNTOS BYTEA COMA ENTERO PARDER'
    print('Ejecuta funcion getbyte')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'GET_BYTE')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[8]))

def p_instrucciones_funcion_binary_string_get_byte_error(t) :
    'fun_binario_select : GET_BYTE PARIZQ error DOS_PUNTOS DOS_PUNTOS BYTEA COMA ENTERO PARDER'
    
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'GET_BYTE')
    dot.edge(str(id), str(id2))
    dot.edge(str(id), str(t[8]))

def p_instrucciones_funcion_binary_string_get_byte2(t) :
    'fun_binario_select : GET_BYTE PARIZQ valor COMA ENTERO PARDER'
    print('Ejecuta funcion getbyte')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'GET_BYTE')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))

def p_instrucciones_funcion_binary_string_get_byte2_error(t) :
    'fun_binario_select : GET_BYTE PARIZQ error COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'GET_BYTE')
    dot.edge(str(id), str(id2))
    dot.edge(str(id), str(t[5]))

def p_instrucciones_funcion_binary_string_set_byte(t) :
    'fun_binario_select : SET_BYTE PARIZQ valor DOS_PUNTOS DOS_PUNTOS BYTEA COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta funcion setbyte')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SET_BYTE')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[8]))
    dot.edge(str(id), str(t[10]))

def p_instrucciones_funcion_binary_string_set_byte_error(t) :
    'fun_binario_select : SET_BYTE PARIZQ error DOS_PUNTOS DOS_PUNTOS BYTEA COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_set_byte2(t) :
    'fun_binario_select : SET_BYTE PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta funcion setbyte')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SET_BYTE')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_set_byte2_error(t) :
    'fun_binario_select : SET_BYTE PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'SET_BYTE')
    dot.edge(str(id), str(id2))
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))

def p_instrucciones_funcion_binary_string_Convert(t) :
    'fun_binario_select : CONVERT PARIZQ valor AS tipos PARDER'
    print('Ejecuta funcion convert')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'CONVERT')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]['id'])) 

def p_instrucciones_funcion_binary_string_convert_error(t) :
    'fun_binario_select : CONVERT PARIZQ error AS tipos PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'SET_BYTE')
    dot.edge(str(id), str(id2))
    dot.edge(str(id), str(t[5]['id']))

def p_instrucciones_funcion_binary_string_encode(t) :
    'fun_binario_select : ENCODE PARIZQ valor DOS_PUNTOS DOS_PUNTOS BYTEA COMA CADENA PARDER'
    print('Ejectua funcion encode')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ENCODE')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), t[8])

def p_instrucciones_funcion_binary_string_encode_error(t) :
    'fun_binario_select : ENCODE PARIZQ error DOS_PUNTOS DOS_PUNTOS BYTEA COMA CADENA PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'ENCODE')
    dot.edge(str(id), str(id2))
    dot.edge(str(id), str(t[8]))

def p_instrucciones_funcion_binary_string_encode2(t) :
    'fun_binario_select : ENCODE PARIZQ valor COMA CADENA PARDER'
    print('Ejecuta funcion encode')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ENCODE')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), t[5])

def p_instrucciones_funcion_binary_string_encode2_error(t) :
    'fun_binario_select : ENCODE PARIZQ error COMA CADENA PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'ENCODE')
    dot.edge(str(id), str(id2))
    dot.edge(str(id), str(t[5]))

def p_instrucciones_funcion_binary_string_decode(t) :
    'fun_binario_select : DECODE PARIZQ valor COMA CADENA PARDER'
    print('Ejecuta funcion decode')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'DECODE')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), t[5])

def p_instrucciones_funcion_binary_string_decode_error(t) :
    'fun_binario_select : DECODE PARIZQ error COMA CADENA PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id2 = inc()
    dot.node(str(id2), 'ERROR')
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'DECODE')
    dot.edge(str(id), str(id2))
    dot.edge(str(id), str(t[5]))

#========================================================

def p_error(t):
    error = Error('Sintáctico', "No se esperaba el caracter '%s'" % t.value[0], t.lexer.lineno)
    tabla_errores.agregar(error)
    print(error.imprimir())

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    retorno = parser.parse(input)
    dot.view()
    return retorno
