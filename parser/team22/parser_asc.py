# Construyendo el analizador léxico
import ply.lex as lex
from ts import *
from lex import *
#from type_checker import *
from columna import *
from graphviz import Graph
from grammar.gramatical import *

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
#type_checker = TypeChecker(tabla_simbolos, tabla_errores, consola, salida)
gramatical = Gramatical()

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
        if element != None:
            dot.edge(str(id), str(element['id']))
            gramatica = "<init>	::= <instrucciones>"
            no_terminal = ["<init>","<instrucciones>"]
            terminal = []
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"init")
    for element in tabla_errores.errores:
        print('Error tipo: ', element.tipo, ' Descripción: ', element.descripcion, ' en la línea: ', element.linea)
    
def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    #                   [{'id': id}]  {'id': id}
    if t[2] != None:
        t[1].append(t[2])
    #[{'id': id}, {'id': id}, ...]
    if t[1] == None:
        t[1] = []
    t[0] = t[1]
    gramatica = "<instrucciones>	::= <instrucciones> <instruccion>"
    no_terminal = ["<instrucciones>", "<instruccion>"]
    terminal = []
    reg_gramatical = "\ninstrucciones.append(instruccion) \n instrucciones.syn = instrucciones.syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"instrucciones")

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    if t[1] != None:
        t[0] = [t[1]]
    # [{'id': id}]
    gramatica = "				| <instruccion>"
    no_terminal = ["<instrucciones>", "<instruccion>"]
    terminal = []
    reg_gramatical = "\ninstrucciones.syn = [instrucciones.syn]"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"instrucciones")

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
                        | TABLE
                        '''
    id = inc()
    t[0] = {'id': id}

    if len(t) == 2:
        type_checker.showTables(line = t.lexer.lineno)

    if t[1].upper() == 'CREATE':
        t[0] = t[2]
        gramatica = "<instruccion>	::= CREATE <creacion>"
        no_terminal = ["<instruccion>","<creacion>"]
        terminal = ["CREATE"]
        reg_gramatical = "\ninstruccion.syn = creacion.syn"
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"instruccion")

    elif t[1].upper() == 'SHOW':
        t[0] = t[2]
        gramatica = "				| SHOW <show_db> PTCOMA"
        no_terminal = ["<show_db>"]
        terminal = ["SHOW", "PTCOMA"]
        reg_gramatical = "\ninstruccion.syn = show_db.syn"
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"instruccion")

    elif t[1].upper() == 'ALTER':
        t[0] = t[3]
        gramatica = "				| ALTER DATABASE <alter_database> PTCOMA\n 				| ALTER TABLE <alter_table> PTCOMA"
        no_terminal = ["<alter_database>"]
        terminal = ["ALTER", "DATABASE", "TABLE", "PTCOMA"]
        reg_gramatical = "\ninstruccion.syn = alter_database.syn \n instruccion.syn = alter_table.syn"
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"instruccion")

        # if t[2].upper() == 'TABLE':
        #     dot.node(str(id), 'ALTER TABLE')
        # elif t[2].upper() == 'DATABASE':
        #     dot.node(str(id), 'ALTER DATABASE')
        #     dot.edge(str(id), str(t[3]['id']))

    elif t[1].upper() == 'USE':
        t[0] = t[2]
        gramatica = "				| USE <cambio_bd>"
        no_terminal = ["<cambio_bd>"]
        terminal = ["USE"]
        reg_gramatical = "\ninstruccion.syn = cambio_bd.syn"
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"instruccion")
        # dot.node(str(id), 'USE')

        # for element in t[2]:
        #     dot.edge(str(id), str(element['id']))

    elif t[1].upper() == 'SELECT':
        t[0] = t[2]
        gramatica = "				| SELECT <selects>"
        no_terminal = ["<selects>"]
        terminal = ["SELECT"]
        reg_gramatical = "\ninstruccion.syn = selects.syn"
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"instruccion")
        # dot.node(str(id), 'SELECT')

    elif t[1].upper() == 'DELETE':
        t[0] = t[2]
        gramatica = "				| DELETE <deletes>"
        no_terminal = ["<deletes>"]
        terminal = ["DELETE"]
        reg_gramatical = "\ninstruccion.syn = deletes.syn"
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"instruccion")
        # dot.node(str(id), 'DELETE')

    elif t[1].upper() == 'UPDATE':
        t[0] = t[2]
        gramatica = "				| UPDATE <update_table> PTCOMA"
        no_terminal = ["<update_table>"]
        terminal = ["UPDATE","PTCOMA"]
        reg_gramatical = "\ninstruccion.syn = update_table.syn"
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"instruccion")
        # dot.node(str(id), 'UPDATE')

    elif t[1].upper() == 'INSERT':
        t[0] = t[2]
        gramatica = "				| INSERT <insercion>"
        no_terminal = ["<insercion>"]
        terminal = ["INSERT"]
        reg_gramatical = "\ninstruccion.syn = insercion.syn"
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"instruccion")
        # dot.node(str(id), 'INSERT E')

    elif t[1].upper() == 'DROP':
        t[0] = t[2]
        gramatica = "				| DROP <dropear>"
        no_terminal = ["<dropear>"]
        terminal = ["DROP"]
        reg_gramatical = "\ninstruccion.syn = dropear.syn"
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"instruccion")

'''
def p_instruccion_error(t) :
    'instruccion    : error PTCOMA'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[2], t.lexer.lineno)
    tabla_errores.agregar(error)
    '''
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
    t[0] = {'id': id}

    if t[1].upper() == 'DATABASE':
        t[0] = t[2]
        gramatica = "<creacion>	::= DATABASE <crear_bd>"
        no_terminal = ["<creacion>","<crear_bd>"]
        terminal = ["DATABASE"]
        reg_gramatical = "\ncreacion.syn = crear_bd.syn"
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"creacion")
    elif t[1].upper() == 'OR':
        dot.node(str(t[4]['id']), 'CREATE OR REPLACE\nDATABASE')
        t[0] = t[4]
        gramatica = "			| OR REPLACE DATABASE <crear_bd>"
        no_terminal = ["<crear_bd>"]
        terminal = ["OR", "REPLACE" , "DATABASE"]
        reg_gramatical = "\ncreacion.syn = crear_bd.syn"
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"creacion")
    elif t[1].upper() == 'TABLE':
        t[0] = t[2]
        gramatica = "			| TABLE <crear_tb>"
        no_terminal = ["<crear_tb>"]
        terminal = ["TABLE"]
        reg_gramatical = "\ncreacion.syn = crear_tb.syn"
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"creacion")
    elif t[1].upper() == 'TYPE':
        dot.node(str(id), 'TYPE')
        dot.edge(str(id), str(t[2]['id']))

        gramatica = "			| TYPE <crear_type>"
        no_terminal = ["<crear_type>"]
        terminal = ["TYPE"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"creacion")

def p_instruccion_crear_BD(t) :
    'crear_bd     : ID PTCOMA'
    #type_checker.createDatabase(database = t[1].upper(), line = t.lexer.lineno)
    id = inc()
    t[0] = {'id': id}
    id_id = inc()
    dot.node(str(id), 'CREATE DATABASE')
    dot.node(str(id_id), t[1])
    dot.edge(str(id), str(id_id))
    
    gramatica = "<crear_bd>	::= ID PTCOMA"
    no_terminal = ["<crear_bd>"]
    terminal = ["ID","PTCOMA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"crear_bd")

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
    
    gramatica = "			| ID <lista_parametros_bd> PTCOMA"
    no_terminal = ["<lista_parametros_bd>"]
    terminal = ["ID","PTCOMA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"crear_bd")

    '''if 'mode' in t[2]:
        type_checker.createDatabase(database = t[1].upper(), mode = t[2]['params']['mode'], line = t.lexer.lineno)
    else:
        type_checker.createDatabase(database = t[1].upper(), line = t.lexer.lineno)
'''
    temp_base = -1

def p_instruccion_crear_BD_Parametros_error(t) :
    'crear_bd   : ID error PTCOMA'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[2], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instruccion_crear_BD_if_exists(t) :
    'crear_bd       : IF NOT EXISTS ID PTCOMA'
    #type_checker.createDatabase(database = t[4].upper(), line = t.lexer.lineno)
    id = inc()
    t[0] = {'id': id}
    id_if = inc()
    id_id = inc()
    dot.node(str(id), 'CREATE DATABASE')
    dot.node(str(id_if), 'IF NOT EXIST')
    dot.node(str(id_id), t[4])
    dot.edge(str(id), str(id_if))
    dot.edge(str(id_if), str(id_id))

    gramatica = "			| IF NOT EXISTS ID PTCOMA"
    no_terminal = []
    terminal = ["IF","NOT","EXISTS","ID","PTCOMA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"crear_bd")

def p_instruccion_crear_BD_if_exists_Parametros(t) :
    'crear_bd       : IF NOT EXISTS ID lista_parametros_bd PTCOMA'
    '''if 'mode' in t[5]:
        type_checker.createDatabase(database = t[4].upper(), mode = t[5]['params']['mode'], line = t.lexer.lineno)
    else:
        type_checker.createDatabase(database = t[4].upper(), line = t.lexer.lineno)
'''
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

    gramatica = "			| IF NOT EXISTS ID <lista_parametros_bd> PTCOMA"
    no_terminal = ["<lista_parametros_bd>"]
    terminal = ["IF","NOT","EXISTS","ID","PTCOMA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"crear_bd")

def p_instruccion_crear_TB_herencia(t):
    '''crear_tb     : ID PARIZQ crear_tb_columnas PARDER tb_herencia PTCOMA'''
    print("Creación de Tabla con herencia")
    #t[0] = Crear_TB_Herencia(t[1], t[3], t[5])|||
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), t[1])
    for element in t[3]:
        if element != None:
            dot.edge(str(id), str(element['id']))
    dot.edge(str(id), str(t[5]['id']))

def p_instruccion_crear_TB_herencia_error(t) :
    'crear_tb   : ID PARIZQ error PARDER tb_herencia PTCOMA'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[2], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), t[1])
    for element in t[5]:
        dot.edge(str(id), str(element['id']))

    gramatica = "<crear_tb>	::= ID PARIZQ <crear_tb_columnas> PARDER <tb_herencia> PTCOMA"
    no_terminal = ["crear_tb","<crear_tb_columnas>","<tb_herencia>"]
    terminal = ["PARIZQ","PARDER","ID","PTCOMA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"crear_tb")


def p_instruccion_crear_TB(t):
    '''crear_tb     : ID PARIZQ crear_tb_columnas PARDER PTCOMA'''
    #type_checker.createTable(table = t[1], columns = t[3], line = t.lexer.lineno)
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
    gramatica = "			| ID PARIZQ <crear_tb_columnas> PARDER PTCOMA"
    no_terminal = ["<crear_tb_columnas>"]
    terminal = ["PARIZQ","PARDER","ID","PTCOMA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"crear_tb")
    
def p_instruccion_crear_TB_error(t) :
    'crear_tb   : ID PARIZQ error PARDER PTCOMA'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[2], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), t[1])

def p_isntruccion_crear_TYPE(t) :
    '''crear_type   : ID AS ENUM PARIZQ lista_objetos PARDER PTCOMA
                    '''
    print("Creacion de un type enumerado")
    #t[0] = Crear_Type(t[1], t[5])
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ENUM')
    dot.edge(str(id), 'IDENTIFICADOR\n' + t[1])
    if type(t[5]) == list:
        for element in t[5]:
            dot.edge(str(id), str(element['id']))
    else:
        dot.edge(str(id), str(t[5]['id']))

    gramatica = "<crear_type>	::= ID AS ENUM PARIZQ <lista_objetos> PARDER PTCOMA"
    no_terminal = ["<crear_type>","<lista_objetos>"]
    terminal = ["PARIZQ","PARDER","ID","PTCOMA","AS","ENUM"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"crear_type")

def p_instruccion_TB_herencia(t) :
    'tb_herencia    : INHERITS PARIZQ ID PARDER'
    #t[0] = Heredero(t[4])
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'INHERITS')
    dot.edge(str(id), t[3])

    gramatica = "<tb_herencia>	::= INHERITS PARIZQ ID PARDER"
    no_terminal = ["<tb_herencia>"]
    terminal = ["PARIZQ","PARDER","ID","INHERITS"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"tb_herencia")

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
        #type_checker.showDatabase()
        print()

    else:
        #type_checker.showDatabase(t[3].upper())
        id_er = inc()
        dot.node(str(id_er), t[3] + ' [er]')
        dot.edge(str(id), str(id_er))

    gramatica = "<show_db> 	::= DATABASES\n			| DATABASES LIKE CADENA"
    no_terminal = ["<show_db>"]
    terminal = ["DATABASES","LIKE","CADENA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"show_db")    


#========================================================

#========================================================
# INSTRUCCION ALTER DATABASE
def p_instruccion_alter_database(t) :
    '''alter_database   : ID RENAME TO ID
                        | ID OWNER TO def_alter_db'''
    id = inc()
    t[0] = {'id': id}
    if t[2].upper() == 'RENAME':
        #type_checker.alterDatabase(databaseOld = t[1].upper(), databaseNew = t[4].upper(), line = t.lexer.lineno)
        dot.node(str(id), 'RENAME TO')
        id_old = inc()
        id_new = inc()
        dot.node(str(id_old), 'OLD ID\n' + t[1])
        dot.node(str(id_new), 'NEW ID\n' + t[4])
        dot.edge(str(id), str(id_old))
        dot.edge(str(id), str(id_new))
        gramatica = "<alter_database>	::= ID RENAME ID"
        no_terminal = ["<alter_database>"]
        terminal = ["ID","RENAME"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"alter_database") 

    elif t[2].upper() == 'OWNER':
        dot.node(str(id), 'OWNER TO')
        dot.edge(str(id), str(t[4]['id']))
        gramatica = "					| ID OWNER TO <def_alter_db>"
        no_terminal = ["<def_alter_db>"]
        terminal = ["ID","OWNER","TO"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"alter_database") 


def p_def_alter_db(t) :
    '''def_alter_db     : ID
                        | CURRENT_USER
                        | SESSION_USER'''

    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), t[1])

    gramatica = "<def_alter_db>	::= ID\n				| CURRENT_USER\n				| SESSION_USER"
    no_terminal = ["<def_alter_db>"]
    terminal = ["ID","CURRENT_USER","SESSION_USER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_alter_db")

#========================================================

#========================================================

# INSTRUCCION CON "USE"
def p_instruccion_Use_BD(t) :
    'cambio_bd     : ID PTCOMA'
    #type_checker.useDatabase(t[1].upper(), line = t.lexer.lineno)

    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), t[1])

    gramatica = "<cambio_bd>	::= ID PTCOMA"
    no_terminal = ["<cambio_bd>"]
    terminal = ["ID","PTCOMA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"cambio_bd")

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
        if element != None:
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

    gramatica = "<selects>      ::= <lista_parametros> FROM <lista_parametros> <inicio_condicional> <state_fin_query>"
    no_terminal = ["<selects>","<lista_parametros>","<inicio_condicional>","<state_fin_query>"]
    terminal = ["FROM"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"selects")


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
    
    gramatica = "			| <lista_parametros> COMA CASE <case_state> FROM <lista_parametros> <inicio_condicional> <state_fin_query> <inicio_group_by>"
    no_terminal = ["<case_state>","<lista_parametros>","<inicio_condicional>","<state_fin_query>","<inicio_group_by>"]
    terminal = ["COMA","CASE","FROM"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"selects")


def p_instruccion_selects3(t) :
    '''selects      : fun_trigonometrica state_aliases_field 
                    | aritmetica state_aliases_field  '''
    # print(t[1]['funcion'].upper() )
    '''if t[1]['funcion'].upper() != 'ATAN2D' and t[1]['funcion'].upper() != 'ATAN2':
        resultado = type_checker.Funciones_Trigonometricas_1(t[1]['funcion'], t[1]['valor'], line = t.lexer.lineno)
    else:
        resultado = type_checker.Funciones_Trigonometricas_2(t[1]['funcion'], t[1]['valor1'], t[1]['valor1'], line = t.lexer.lineno)
  '''
    #print("================================>", resultado)
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

    gramatica = "			| <fun_trigonometrica> <state_aliases_field>"
    no_terminal = ["<fun_trigonometrica>","<state_aliases_field>"]
    terminal = []
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"selects")


def p_instruccion_selects4(t) :
    '''selects      : fun_trigonometrica state_aliases_field FROM ID state_aliases_table 
                    | aritmetica state_aliases_field FROM ID state_aliases_table  '''
    '''if t[1]['funcion'].upper() != 'ATAN2D' and t[1]['funcion'].upper() != 'ATAN2':
        resultado = type_checker.Funciones_Trigonometricas_1(t[1]['funcion'], t[1]['valor'], line = t.lexer.lineno)
    else:
        resultado = type_checker.Funciones_Trigonometricas_2(t[1]['funcion'], t[1]['valor1'], t[1]['valor1'], line = t.lexer.lineno)
  '''
    #print("================================>", resultado)

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

    gramatica = "			| <fun_trigonometrica> <state_aliases_field> FROM ID <state_aliases_table>"
    no_terminal = ["<fun_trigonometrica>","<state_aliases_field>","<state_aliases_table>"]
    terminal = ["PTCOMA","FROM","ID"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"selects")    


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
            
            gramatica = "			| POR FROM <select_all>\n			| POR FROM <state_subquery> <inicio_condicional>"
            no_terminal = ["<select_all>","<state_subquery>","<inicio_condicional>"]
            terminal = ["POR","FROM"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"selects")
        
        if t[1].upper() == 'GREATEST':
            dot.node(str(id), 'GREATEST')
            for element in t[3]:
                dot.edge(str(id), str(element['id']))
            
            gramatica = "			| GREATEST PARIZQ <lista_parametros> PARDER"
            no_terminal = ["<lista_parametros>"]
            terminal = ["GREATEST","PARIZQ","PARDER","PTCOMA"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"selects")

        if t[1].upper() == 'LEAST':
            dot.node(str(id), 'LEAST')
            for element in t[3]:
                dot.edge(str(id), str(element['id']))

            gramatica = "			| LEAST PARIZQ <lista_parametros> PARDER"
            no_terminal = ["<lista_parametros>"]
            terminal = ["LEAST","PARIZQ","PARDER","PTCOMA"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"selects")    

    else:
        dot.node(str(id), 'SELECT')
        if t[1] != None:
            for element in t[1]:
                if element != None:
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
    gramatica = "<inicio_condicional>	::= WHERE <relacional> <inicio_condicional>"
    no_terminal = ["<inicio_condicional>","<relacional>"]
    terminal = ["WHERE"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"inicio_condicional") 
    # for element in t[3]:
    #     # if element['id'] != '':
    #     dot.edge(str(id), str(element['id']))

def p_instruccion_selects_sin_where(t) :
    'inicio_condicional      : inicio_group_by'
    t[0] = t[1]
    gramatica = "						| <inicio_group_by>"
    no_terminal = ["<inicio_group_by>"]
    terminal = []
    reg_gramatical = "\ninicio_condicional.syn = inicio_group_by.syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"inicio_condicional") 
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
        
    gramatica = "<inicio_group_by>	::= GROUP BY <lista_parametros> <inicio_having>"
    no_terminal = ["<inicio_group_by>","<lista_parametros>","<inicio_having>"]
    terminal = ["GROUP","BY"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"inicio_group_by")  

def p_instruccion_selects_group_by2(t) :
    'inicio_group_by      : inicio_order_by '
    t[0] = t[1]
    gramatica = "					| <inicio_order_by>"
    no_terminal = ["<inicio_order_by>"]
    terminal = []
    reg_gramatical = "\ninicio_group_by.syn = inicio_order_by.syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"inicio_group_by")
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
    
    gramatica = "<inicio_having>	::= HAVING <relacional> <inicio_order_by>"
    no_terminal = ["<inicio_having>","<relacional>","<inicio_order_by>"]
    terminal = ["HAVING"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"inicio_having") 

def p_instruccion_selects_having2(t) :
    'inicio_having      : inicio_order_by '
    t[0] = t[1]
    gramatica = "				| <inicio_order_by>"
    no_terminal = ["<inicio_order_by>"]
    terminal = []
    reg_gramatical = "\ninicio_having.syn = inicio_order_by.syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"inicio_having")
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

    gramatica = "<inicio_order_by>	::= ORDER BY <sorting_rows>	<state_limit>"
    no_terminal = ["<inicio_order_by>","<sorting_rows>","<state_limit>"]
    terminal = ["ORDER","BY"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"inicio_order_by")

def p_instruccion_selects_order_by2(t) :
    'inicio_order_by      : state_limit '
    t[0] = t[1]
    gramatica = "					| <state_limit>"
    no_terminal = ["<state_limit>"]
    terminal = []
    reg_gramatical = "\ninicio_order_by.syn = state_limit.syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"inicio_order_by")
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

    gramatica = "<state_limit>	::= LIMIT ENTERO <state_offset>\n				| LIMIT ALL <state_offset>"
    no_terminal = ["<state_limit","<state_offset>"]
    terminal = ["LIMIT","ENTERO","ALL"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_limit")

def p_instruccion_selects_limit2(t) :
    'state_limit      : state_offset'
    t[0] = t[1]
    gramatica = "				| <state_offset>"
    no_terminal = ["<state_offset>"]
    terminal = []
    reg_gramatical = "\nstate_limit.syn = state_offset.syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_limit")
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

    gramatica = "<state_offset>	::= OFFSET ENTERO <state_union>\n				| OFFSET ENTERO <state_intersect>"
    gramatica += "\n				| OFFSET ENTERO <state_except>"
    no_terminal = ["<state_offset>","<state_union>","<state_intersect>","<state_except>"]
    terminal = ["OFFSET","ENTERO"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_offset")

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

    gramatica = "				| <state_union>\n				| <state_intersect>"
    gramatica += "\n				| <state_except>\n				| <state_subquery>\n				| epsilon"
    no_terminal = ["<state_subquery>","<state_union>","<state_intersect>","<state_except>"]
    terminal = ["epsilon"]
    reg_gramatical = "\nstate_offset.syn = (state_union or state_intersect or state_except or state_subquery).syn or []"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_offset")
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
        
        gramatica = "<state_union>	::= UNION ALL SELECT <selects>"
        no_terminal = ["<selects>","<state_union>"]
        terminal = ["UNION","ALL","SELECT"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_union") 
    else:
        dot.node(str(id), 'UNION')
        dot.edge(str(id), str(t[3]['id']))
        gramatica = "				| UNION SELECT <selects>"
        no_terminal = ["<selects>"]
        terminal = ["UNION","SELECT"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_union") 

    
def p_instruccion_selects_union2(t) :
    'state_union      : '
    t[0] = []
    gramatica = "				| epsilon"
    no_terminal = []
    terminal = ["epsilon"]
    reg_gramatical = "\nstate_union.syn = []"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_union")

def p_instruccion_selects_intersect(t) :
    '''state_intersect      : INTERSECT SELECT selects
                            | INTERSECT ALL SELECT selects'''
    id = inc()
    t[0] = {'id': id}

    if t[2].upper() == 'ALL':
        dot.node(str(id), 'ALL INTERSECT')
        dot.edge(str(id), str(t[4]['id']))
        
        gramatica = "<state_intersect>	::= INTERSECT ALL SELECT <selects>"
        no_terminal = ["<state_intersect>","<selects>"]
        terminal = ["INTERSECT","ALL","SELECT"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_intersect")  
    else:
        dot.node(str(id), 'INTERSECT')
        dot.edge(str(id), str(t[3]['id'])) 
        gramatica = "					| INTERSECT SELECT <selects>"
        no_terminal = ["<selects>"]
        terminal = ["INTERSECT","SELECT"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_intersect") 
    
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
        gramatica = "<state_except>	::= EXCEPT ALL SELECT <selects>"
        no_terminal = ["<state_except>","<selects>"]
        terminal = ["EXCEPT","ALL","SELECT"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_except") 
    else:
        dot.node(str(id), 'EXCEPT')
        dot.edge(str(id), str(t[3]['id'])) 
        gramatica = "				| EXCEPT SELECT <selects>"
        no_terminal = ["<selects>"]
        terminal = ["EXCEPT","SELECT"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_except") 

    
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
    if type(t[2]) != list:
        dot.edge(str(id), str(t[2]['id']))
    else:
        for element in t[2]:
            dot.edge(str(id), str(element['id']))
    # dot.edge(str(id), str(t[2]['id'])) 
    
    if t[3] != []:
        dot.edge(str(id), str(t[3]['id'])) 
        
    gramatica = "<select_all>	::= ID <state_aliases_table> <inicio_condicional>"
    no_terminal = ["<select_all>","<state_aliases_table>","<inicio_condicional>"]
    terminal = ["ID"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"select_all")  

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
        gramatica = "<date_functions>	::= EXTRACT PARIZQ <opcion_date_functions>"
        no_terminal = ["<date_functions>","<opcion_date_functions>"]
        terminal = ["EXTRACT","PARIZQ"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"date_functions")  

    elif t[1].upper() == 'NOW':
        dot.node(str(id), 'NOW')
        # dot.edge(str(id), str(t[3]['id'])) 
        # for element in t[3]:
        #     dot.edge(str(id), str(element['id']))
        
        gramatica = "					| NOW PARIZQ PARDER"
        no_terminal = []
        terminal = ["NOW","PARIZQ","PARDER"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"date_functions") 

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
    
    gramatica = "					| <date_part> PARIZQ <opcion_date_functions>\n					| <opcion_date_functions>"
    no_terminal = ["<date_part>","<opcion_date_functions>"]
    terminal = ["PARIZQ"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"date_functions") 

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

    gramatica = "<lista_date_functions>	::= <def_fields> FROM TIMESTAMP CADENA PARDER"
    no_terminal = ["<def_fields>","<lista_date_functions>"]
    terminal = ["FROM","TIMESTAMP","CADENA","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_date_functions")

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

    gramatica = "<opcion_date_functions>	::= <opcion_date_functions> <lista_date_functions>\n						| <lista_date_functions>"
    no_terminal = ["<opcion_date_functions>","<lista_date_functions>"]
    terminal = []
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"opcion_date_functions")
        


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
        gramatica = "						| CURRENT_DATE\n						| CURRENT_TIME\n						| PARDER"
        no_terminal = []
        terminal = ["CURRENT_DATE","CURRENT_TIME","PARDER"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_date_functions")
    elif len(t) == 3:
        id = inc()
        t[0] = {'id': id, 'valor': 'date'}
        dot.node(str(id), 'TIMESTAMP')
        dot.edge(str(id), t[2])
        gramatica = "						| TIMESTAMP CADENA"
        no_terminal = []
        terminal = ["TIMESTAMP","CADENA"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_date_functions")

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
        gramatica = "						| CADENA COMA INTERVAL CADENA PARDER"
        no_terminal = []
        terminal = ["COMA","CADENA","INTERVAL","PARDER"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_date_functions")


# Subqueries
def p_state_subquery(t):
    '''state_subquery   : PARIZQ SELECT selects PARDER'''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'SUB-QUERY')
    dot.edge(str(id), str(t[3]['id'])) 
    # for element in t[3]:
    #         dot.edge(str(id), str(element['id']))
    
    gramatica = "<state_subquery>	::= PARIZQ SELECT <selects> PARDER"
    no_terminal = ["<state_subquery>","<selects>"]
    terminal = ["PARIZQ","SELECT","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_subquery")        

def p_state_subquery_error(t) :
    'state_subquery : PARIZQ SELECT error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
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
    
    gramatica = "<insercion>	::= INTO ID PARIZQ <lista_id> PARDER VALUES PARIZQ <lista_insercion> PARDER PTCOMA"
    no_terminal = ["<insercion>","<lista_id>","<lista_insercion>"]
    terminal = ["INTO","ID","PARIZQ","VALUES","PARDER","PTCOMA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"insercion")

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
    
    gramatica = "			| INTO ID VALUES PARIZQ <lista_insercion> PARDER PTCOMA"
    no_terminal = ["<lista_insercion>"]
    terminal = ["INTO","ID","PARIZQ","VALUES","PARDER","PTCOMA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"insercion")

#========================================================
# DROP BASES DE DATOS Y TABLAS
def p_instruccion_Drop_BD_exists(t) :
    '''dropear      : DATABASE IF EXISTS ID PTCOMA
                    '''
    #type_checker.dropDatabase(database = t[4].upper(), line = t.lexer.lineno)
    id = inc()
    id_id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'DROP DATABASE\nIF EXISTS')
    dot.node(str(id_id), str(t[4]))
    dot.edge(str(id), str(id_id))

    gramatica = "<dropear>	::= DATABASE IF EXISTS ID PTCOMA"
    no_terminal = ["<dropear>"]
    terminal = ["DATABASE","IF","EXISTS","ID","PTCOMA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"dropear")

def p_instruccion_Drop_BD(t) :
    '''dropear      : DATABASE ID PTCOMA
                    '''
    #type_checker.dropDatabase(database = t[2].upper(), line = t.lexer.lineno)
    id = inc()
    id_id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'DROP DATABASE')
    dot.node(str(id_id), str(t[2]))
    dot.edge(str(id), str(id_id))

    gramatica = "			| DATABASE ID PTCOMA"
    no_terminal = []
    terminal = ["DATABASE","ID","PTCOMA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"dropear")


def p_instruccion_Drop_TB(t) :
    '''dropear      : TABLE ID PTCOMA
                    '''
    #type_checker.dropTable(table = t[2].lower(), line = t.lexer.lineno)
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'DROP TABLE')
    id_id = inc()
    dot.node(str(id_id), t[2])
    dot.edge(str(id), str(id_id))

    gramatica = "			| TABLE ID PTCOMA"
    no_terminal = []
    terminal = ["TABLE","ID","PTCOMA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"dropear")

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

    gramatica = "<lista_parametros_bd>	::= <parametros_bd>\n						| <parametros_bd> <parametros_bd>"
    no_terminal = ["<lista_parametros_bd>","<parametros_bd>"]
    terminal = []
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_parametros_bd")

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
        gramatica = "<parametros_bd>	::= OWNER ID"
        no_terminal = ["<parametros_bd>"]
        terminal = ["OWNER","ID"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametros_bd")
    else:
        dot.node(str(id_id), t[3])
        dot.edge(str(id), str(id_id))
        t[0] = {'owner': t[3], 'id': id}
        gramatica = "				| OWNER IGUAL ID"
        no_terminal = []
        terminal = ["OWNER","ID","IGUAL"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametros_bd")

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
        gramatica = "				| MODE ENTERO"
        no_terminal = []
        terminal = ["MODE","ENTERO"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametros_bd")
    else:
        dot.node(str(id_entero), str(t[3]))
        dot.edge(str(id), str(id_entero))
        t[0] = {'mode': t[3], 'id': id}
        gramatica = "				| MODE IGUAL ENTERO"
        no_terminal = []
        terminal = ["MODE","ENTERO","IGUAL"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametros_bd")


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
    gramatica = "<sorting_rows>	::= <sorting_rows> COMA <sort>"
    no_terminal = ["<sorting_rows>","<sort>"]
    terminal = ["COMA"]
    reg_gramatical = "\nsorting_rows.syn = sorting_rows.syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"sorting_rows")


def p_instrucciones_sort_DESC(t) :   
    'sorting_rows         : sort'
    t[0] = [t[1]]
    # print("sort")
    # id = inc()
    # t[0] = [{'id': id}]
    # dot.node(str(id), 'SORT')
    gramatica = "				| <sort>"
    no_terminal = ["<sort>"]
    terminal = []
    reg_gramatical = "\nsorting_rows.syn = [sort.syn]"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"sorting_rows")

def p_temporalmente_nombres(t) :
    '''sort         : ID ASC
                    | ID DESC
                    | ID'''
    id = inc()
    t[0] = {'id': id}

    if len(t) == 2:
        dot.node(str(id), 'IDENTIFICADOR\n' + t[1])
        gramatica = "<sort>	::= ID"
        no_terminal = []
        terminal = ["ID"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"sort")
    else:
        dot.node(str(id),'SORT TYPE\n' +  t[2])
        dot.edge(str(id), 'IDENTIFICADOR\n' +  t[1])
        gramatica = "		| ID DESC\n		| ID ASC"
        no_terminal = []
        terminal = ["ID","DESC","ASC"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"sort")

#========================================================

#========================================================
# LISTA DE PARAMETROS DE FUNCINOES
def p_instrucciones_lista_parametros_fun(t) :
    'lista_parametros_funciones    : lista_parametros_funciones COMA valor_dato'
    t[1].append(t[3])
    t[0] = t[1]
    gramatica = "<lista_parametros_funciones>    ::= <lista_parametros_funciones> COMA <valor_dato>"
    no_terminal = ["<lista_parametros_funciones>","<valor_dato>"]
    terminal = ["COMA"]
    reg_gramatical = "\nlista_parametros_funciones.append(valor_dato)\n lista_parametros_funciones = lista_parametros_funciones"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_parametros_funciones")

def p_instrucciones_parametro_fun(t) :
    'lista_parametros_funciones    : valor_dato '
    t[0] = [t[1]]
    gramatica = "								| <valor_dato>"
    no_terminal = ["<valor_dato>"]
    terminal = []
    reg_gramatical = "\nlista_parametros_funciones = [valor_dato]"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_parametros_funciones")

def p_valores_fun(t) :
    '''valor_dato        : ID '''   
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'IDENTIFICADOR\n' +  t[1])
    gramatica = "<valor_dato>	:= ID"
    no_terminal = ["<valor_dato>"]
    terminal = ["ID"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"valor_dato")
    
def p_valores_fun2(t) :
    '''valor_dato        : ENTERO
                         | DECIMAL '''   
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'NUMERO\n' +  str(t[1]))
    gramatica = "				| ENTERO\n				| DECIMAL"
    no_terminal = []
    terminal = ["ENTERO","DECIMAL"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"valor_dato")
    
def p_valores_fun3(t) :
    '''valor_dato        : CADENA '''   
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'CADENA\n' +  t[1])
    gramatica = "				| CADENA"
    no_terminal = []
    terminal = ["CADENA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"valor_dato")
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
    gramatica = "<lista_parametros>	::= <lista_parametros> COMA <es_distinct> <parametro> <state_aliases_field>"
    no_terminal = ["<lista_parametros>","<es_distinct>","<parametro>","<state_aliases_field>"]
    terminal = ["COMA"]
    reg_gramatical = "\nlista_parametros.append(parametro.syn) \nlista_parametros.syn = lista_parametros.syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_parametros")


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
    gramatica = "<					| <es_distinct> <parametro> <state_aliases_field>"
    no_terminal = ["<es_distinct>","<parametro>","<state_aliases_field>"]
    terminal = []
    reg_gramatical = "\nlista_parametros = [parametro.syn]"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_parametros")

#def p_instrucciones_parametro_error(t) :
#   'lista_parametros   : es_distinct error state_aliases_field'
#    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[2], t.lexer.lineno)
#    tabla_errores.agregar(error)
#    id = inc()
#    t[0] = [{'id':id}]
#    dot.node(str(id), 'ERROR')
#    print(t[2])
#    t.lexer.token()

    

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
    gramatica = "<es_distinct>	::= DISTINCT\n                | epsilon"
    no_terminal = ["<es_distinct>"]
    terminal = ["DISTINCT","epsilon"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"es_distinct")


def p_parametro_con_tabla(t) :
    '''parametro        : ID PUNTO ID
                        | ID PUNTO POR'''   # ESTO SE HA COLOCADO CUANDO SE SOLICITAN TODAS LAS 
                                            # COLUMNAS DE ALGUNA TABLA INDICADA.
    # t[0] = t[1]
    id = inc()
    t[0] = {'id': id}

    # dot.node(str(id), 'IDENTIFICADOR')
    dot.node(str(id), 'IDENTIFICADOR\n' +  t[1] + '.' + t[3])
    gramatica = "<parametro>	::= ID PUNTO ID\n				| ID PUNTO POR"
    no_terminal = ["<parametro>"]
    terminal = ["ID","PUNTO","POR"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametro")

def p_parametro_con_tabla_error(t) :
    'parametro  : ID PUNTO error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_parametros_funciones(t) :
    '''parametro         : funciones_math_esenciales
                         | fun_binario_select
                         | date_functions
                         | state_subquery
                         '''
    t[0] = t[1]
    gramatica = "				| <funciones_math_esenciales>\n				| <fun_binario_select>\n\
				| <date_functions>\n				| <state_subquery>"
    no_terminal = ["<funciones_math_esenciales>","<fun_binario_select>","<date_functions>","<state_subquery>"]
    terminal = []
    reg_gramatical = "\nparametro.syn = (funciones_math_esenciales or fun_binario_select or date_functions or state_subquery).syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametro")

def p_parametros_funciones2(t) :
    '''parametro         : lista_funciones
                         '''
    t[0] = t[1]
    resultado = 0
    '''if t[1]['funcion'] != 'MOD' and t[1]['funcion'] != 'POWER'and t[1]['funcion'] != 'WIDTH_BUCKET' and t[1]['funcion'] != 'DIV' and t[1]['funcion'] != 'GCD':
        resultado = type_checker.Funciones_Matematicas_1( t[1]['funcion'], t[1]['valor'], line = t.lexer.lineno)
    else:
        resultado = type_checker.Funciones_Matematicas_2( t[1]['funcion'], t[1]['valor'], t[1]['valor2'], line = t.lexer.lineno)
    '''
    #print("=========>>>", resultado)

    gramatica = "				| <lista_funciones>"
    no_terminal = ["<lista_funciones>"]
    terminal = []
    reg_gramatical = "\nparametro.syn = lista_funciones.syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametro")

def p_parametros_cadena(t) :
    'parametro         : CADENA'
    # t[0] = t[1]
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'CADENA\n' + str(t[1]))
    gramatica = "				| CADENA"
    no_terminal = []
    terminal = ["CADENA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametro")

def p_parametros_numeros(t) :
    '''parametro            : DECIMAL
                            | ENTERO'''
    # t[0] = t[1]
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'VALOR NUMERICO\n' + str(t[1]))
    gramatica = "				| DECIMAL\n				| ENTERO"
    no_terminal = []
    terminal = ["DECIMAL","ENTERO"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametro")

def p_parametro_sin_tabla(t) :
    'parametro        : ID'
    # t[0] = t[1]
    print("Parametro SIN indice de tabla")

    id = inc()
    t[0] = {'id': id}
    # dot.node(str(id), 'IDENTIFICADOR')
    dot.node(str(id), 'IDENTIFICADOR\n' + str(t[1]))
    gramatica = "				| ID"
    no_terminal = []
    terminal = ["ID"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametro")

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
    if t[1] == None:
        t[1] = []
    t[1].append(t[3])
    t[0] = t[1]
    gramatica = "<crear_tb_columnas>	::= <crear_tb_columnas> COMA <crear_tb_columna>"
    no_terminal = ["<crear_tb_columnas>"]
    terminal = ["COMA"]
    reg_gramatical = "\ncrear_tb_columnas.append(crear_tb_columnas.syn)\n crear_tb_columnas.syn = crear_tb_columnas.syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"crear_tb_columnas")

def p_instrucciones_lista_columnas_error(t) :
    'crear_tb_columnas      : crear_tb_columnas COMA error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)


def p_instrucciones_columnas(t) :
    'crear_tb_columnas      : crear_tb_columna'
    t[0] = [t[1]]
    gramatica = "					| <crear_tb_columna>"
    no_terminal = ["<crear_tb_columnas>"]
    terminal = []
    reg_gramatical = "\ncrear_tb_columnas.syn = [crear_tb_columnas.syn]"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"crear_tb_columnas")

def p_instrucciones_columnas_error(t) :
    'crear_tb_columnas  : error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[1], t.lexer.lineno)
    tabla_errores.agregar(error)

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
    t[0] = {'nombre': t[1].lower(), 'col': col, 'id': id}

    dot.edge(str(id), str(t[2]['id'])) 
    # for element in t[2]:
    #     dot.edge(str(id), str(element['id']))
    if t[3] != None:
        dot.edge(str(id), str(t[3]['id'])) 
    # for element in t[3]:
    #     dot.edge(str(id), str(element['id']))
    gramatica = "<crear_tb_columna>	::= ID <tipos> <parametros_columna>"
    no_terminal = ["<crear_tb_columna>","<tipos>","<parametros_columna>"]
    terminal = ["ID"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"crear_tb_columna")

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

    gramatica = "					| ID <tipos>"
    no_terminal = ["<tipos>"]
    terminal = ["ID"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"crear_tb_columna")

def p_instrucciones_columna_noparam_error(t) :
    'crear_tb_columna       : ID error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[2], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_columna_pk(t) :
    'crear_tb_columna       : PRIMARY KEY PARIZQ lista_id PARDER'
    id = inc()
    t[0] = {'id': id, 'primary': t[4]}
    print('primary key t0 ',t[0])
    dot.node(str(id), ' PRIMARY KEY')
    
    for element in t[4]:
         dot.edge(str(id), str(element['id']))

    gramatica = "					| PRIMARY KEY PARIZQ <lista_id> PARDER"
    no_terminal = ["<lista_id>"]
    terminal = ["PRIMARY","KEY","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"crear_tb_columna")


def p_instrucciones_columna_fk(t) :
    'crear_tb_columna       : FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER'
    if len(t[4]) != len(t[9]):
        error = Error('Semántico', "El número de columnas referencias es distinto al número de columnas foraneas", t.lexer.lineno)
        tabla_errores.agregar(error)
        
    id = inc()
    t[0] = {'id': id, 'foreign': t[4], 'table': t[7].lower(), 'references': t[9]}
    dot.node(str(id), ' FOREIGN KEY')
    
    if t[4] != None:
        for element in t[4]:
            id2 = inc()
            dot.node(str(id2), str(element))
            dot.edge(str(id), str(id2)) 

    dot.node(str(id), t[6] + ' - ' + t[7])
    if t[9] != None:
        for element in t[9]:
            id2 = inc()
            dot.node(str(id2), str(element))
            dot.edge(str(id), str(id2)) 

def p_instrucciones_columna_fk_error(t) :
    'crear_tb_columna   : FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[9], t.lexer.lineno)
    tabla_errores.agregar(error)

    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'FOREIGN KEY')

    for element in t[4] :
        dot.edge(str(id), str(element['id']))
    
    dot.node(str(id), t[6] + ' - ' + t[7])
    gramatica = "					| FOREIGN KEY PARIZQ <lista_id> PARDER REFERENCES ID PARIZQ <lista_id> PARDER"
    no_terminal = ["<lista_id>"]
    terminal = ["FOREIGN","KEY","PARIZQ","PARDER","REFERENCES","ID"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"crear_tb_columna")

def p_instrucciones_columna_check(t) :
    'crear_tb_columna   : chequeo'
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'PARAMETRO')
    
    for element in t[1]:
        dot.edge(str(id), str(element['id']))
    gramatica = "					| <chequeo>"
    no_terminal = ["<chequeo>"]
    terminal = []
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"crear_tb_columna")

def p_instrucciones_columna_unique(t) :
    'crear_tb_columna   : UNIQUE PARIZQ lista_id PARDER'
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'UNIQUE')
    
    for element in t[3]:
        dot.edge(str(id), str(element['id']))
    gramatica = "					| UNIQUE PARIZQ <lista_id> PARDER"
    no_terminal = ["<lista_id>"]
    terminal = ["UNIQUE","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"crear_tb_columna")

def p_instrucciones_lista_params_columnas(t) :
    'parametros_columna     : parametros_columna parametro_columna'
    t[1]['parametros'].append(t[2])
    #t[1] = {} -> t[0] = {}
    id = inc()
    t[0] = {'id': id, 'parametros': t[1]['parametros']}
    dot.node(str(id), 'PARAMETRO')
    
    dot.edge(str(id), str(t[1]['id'])) 
    # for element in t[1]:
    #     dot.edge(str(id), str(element['id']))
    dot.edge(str(id), str(t[2]['id'])) 
    # for element in t[2]:
    #     dot.edge(str(id), str(element['id']))
    gramatica = "<parametros_columna>	::= <parametros_columna> <parametro_columna>"
    no_terminal = ["<parametros_columna>","<parametro_columna>"]
    terminal = []
    reg_gramatical = "\n parametros_columna.update(parametro_columna.syn)\n parametros_columna.syn = parametros_columna.syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametros_columna")

def p_instrucciones_lista_params_columnas_error(t) :
    'parametros_columna : error parametro_columna'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[2], t.lexer.lineno)
    tabla_errores.agregar(error)
    

def p_instrucciones_params_columnas(t) :
    'parametros_columna     : parametro_columna'
    id = inc()
    t[0] = {'id': id, 'parametros': [t[1]]}

    
    dot.node(str(id), 'PARAMETRO')
    
    dot.edge(str(id), str(t[1]['id'])) 
    # for element in t[1]:
    #     dot.edge(str(id), str(element['id']))
    gramatica = "						| <parametro_columna>"
    no_terminal = ["<parametro_columna>"]
    terminal = []
    reg_gramatical = "parametros_columna.syn = parametro_columna.syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametros_columna")

def p_instrucciones_params_columnas_error(t) :
    'parametros_columna : error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[1], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_parametro_columna_default(t) :
    'parametro_columna      : DEFAULT valor'
    #t[1] = {} -> t[0] = {}
    id = inc()
    t[0] = {'id': id, 'default': t[2]['valor']}
    dot.node(str(id), 'DEFAULT')
    dot.edge(str(id), str(t[2]['id']))
    
    for element in t[2]:
        dot.edge(str(id), str(element['id']))
    gramatica = "<parametro_columna>	::= DEFAULT <valor>"
    no_terminal = ["<parametro_columna>","<valor>"]
    terminal = ["DEFAULT"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametro_columna")

def p_instrucciones_parametro_columna_nul(t) :
    'parametro_columna      : unul'
    t[0] = t[1]
    gramatica = "					| <unul>"
    no_terminal = ["<unul>"]
    terminal = []
    reg_gramatical = "\nparametro_columna.syn = unul.syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametro_columna")

def p_instrucciones_parametro_columna_unique(t) :
    'parametro_columna      : unic'
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'PARAMETRO')

    dot.edge(str(id), str(t[1]['id']))
    gramatica = "					| <unic>"
    no_terminal = ["<unic>"]
    terminal = []
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametro_columna")    

def p_instrucciones_parametro_columna_checkeo(t) :
    'parametro_columna      : chequeo'
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'PARAMETRO')

    dot.edge(str(id), str(t[1]['id'])) 
    # for element in t[1]:
    #     dot.edge(str(id), str(element['id']))
    gramatica = "					| <chequeo>"
    no_terminal = ["<chequeo>"]
    terminal = []
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametro_columna")  

def p_instrucciones_parametro_columna_pkey(t) :
    'parametro_columna      : PRIMARY KEY'
    id = inc()
    t[0] = {'id': id, 'is_primary': 1}
    dot.node(str(id), 'PRIMARY KEY')
    gramatica = "					| PRIMARY KEY"
    no_terminal = []
    terminal = ["PRIMARY", "KEY"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametro_columna")

def p_instrucciones_parametro_columna_fkey(t) :
    'parametro_columna      : REFERENCES ID PARIZQ ID PARDER'
    id = inc()
    t[0] = {'id': id, 'references': t[2] + '.' + t[4]}
    dot.node(str(id), 'REFERENCES')
    dot.edge(str(id), t[2] + '.' + t[4])
    gramatica = "					| REFERENCES ID"
    no_terminal = []
    terminal = ["REFERENCES","ID"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"parametro_columna")

def p_instrucciones_nnul(t) :
    'unul   : NOT NULL'
    t[0] = {'is_null': TipoNull.NOT_NULL}
    id = inc()
    t[0]['id'] = id
    dot.node(str(id), 'NOT NULL')
    gramatica = "<unul>	::= NOT NULL"
    no_terminal = ["<unul>"]
    terminal = ["NOT","NULL"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"unul")

def p_instrucciones_unul(t) :
    'unul   : NULL'
    t[0] = {'is_null': TipoNull.NULL}
    id = inc()
    t[0]['id'] = id
    dot.node(str(id), 'NULL')
    gramatica = "		| NULL"
    no_terminal = []
    terminal = ["NULL"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"unul")

def p_instrucciones_unic_constraint(t) :
    'unic   : CONSTRAINT ID UNIQUE'
    id = inc()
    t[0] = {'id': id, 'is_unique': 1, 'constraint': Constraint(tipo = TipoConstraint.UNIQUE, name = t[2], line = t.lexer.lineno)}
    dot.node(str(id), 'CONSTRAINT ' + t[2] + ' UNIQUE')
    gramatica = "<unic> ::= CONSTRAINT ID UNIQUE"
    no_terminal = ["<unic>"]
    terminal = ["CONSTRAINT","ID","UNIQUE"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"unic")

def p_instrucciones_unic(t) :
    'unic   : UNIQUE'
    id = inc()
    dot.node(str(id), 'UNIQUE')
    t[0] = {'id': id, 'is_unique': 1}
    gramatica = "		| UNIQUE"
    no_terminal = []
    terminal = ["UNIQUE"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"unic")

def p_instrucciones_chequeo_constraint(t) :
    'chequeo    : CONSTRAINT ID CHECK PARIZQ relacional PARDER'
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'CONSTRAINT ' + t[2] + ' CHECK')
    dot.edge(str(id), str(t[5]['id'])) 
    # for element in t[5]:
    #     dot.edge(str(id), str(element['id']))
    gramatica = "<chequeo>	::= CONSTRAINT ID CHECK PARIZQ <relacional> PARDERE"
    no_terminal = ["<chequeo>","<relacional>"]
    terminal = ["CONSTRAINT","ID","CHECK","PARIZQ","PARDERE"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"chequeo")

def p_instrucciones_chequeo_constraint_error(t) :
    'chequeo    : CONSTRAINT ID CHECK PARIZQ error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[5], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_chequeo(t) :
    'chequeo    : CHECK PARIZQ relacional PARDER'
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'CHECK')
    for element in t[3]:
        dot.edge(str(id), str(element['id']))
    gramatica = "			| CHECK PARIZQ <relacional> PARDER"
    no_terminal = ["<relacional>"]
    terminal = ["CHECK","PARIZQ","PARDERE"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"chequeo")
    
def p_instrucciones_chequeo_error(t) :
    'chequeo    : CHECK PARIZQ error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    
#========================================================

#========================================================
# LISTA DE ELEMENTOS REUTILIZABLES
def p_instrucciones_lista_ids(t) :
    'lista_id   : lista_id COMA ID'
    id = inc()
    t[1].append({'id': id, 'valor': t[3].lower()})
    t[0] = t[1]

    dot.node(str(id), t[3])
    
    
    gramatica = "<lista_id>	::= <lista_id> COMA ID"
    no_terminal = ["<lista_id>"]
    terminal = ["COMA","ID"]
    reg_gramatical = "\nlista_id.append(ID.valor)\n lista_id.syn = lista_id.syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_id")

def p_instrucciones_lista_ids_error(t) :
    'lista_id   : lista_id COMA error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_lista_id(t) :
    'lista_id   : ID'
    id = inc()
    t[0] = [{'id': id, 'valor': t[1].lower()}]
    dot.node(str(id), t[1])
    # id = inc()
    # t[0] = {'id': id}
    # dot.node(str(id), 'ID')
    # dot.edge(str(id), t[1])
    gramatica = "			| ID"
    no_terminal = []
    terminal = ["ID"]
    reg_gramatical = "\nlista_id.syn = [ID.valor]"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_id")

def p_isntrucciones_lista_id_error(t) :
    'lista_id   : error'
    #error sintáctico
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[1], t.lexer.lineno)
    tabla_errores.agregar(error)
    print(error.imprimir())
    

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
        gramatica = "<lista_objetos> ::= <lista_objetos> COMA <objeto>"
        no_terminal = ["<lista_objetos>","<objeto>"]
        terminal = ["CADENA"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_objetos")

    else:
        dot.node(str(id), 'INTERVAL')
        dot.edge(str(id), t[1])
        dot.edge(str(id), t[4])
        gramatica = "                | CADENA COMA INTERVAL CADENA"
        no_terminal = []
        terminal = ["CADENA","COMA","INTERVAL"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_objetos")

def p_instrucciones_lista_objetos_error2(t) :
    'lista_objetos  : lista_objetos COMA error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_lista_objeto(t) :
    'lista_objetos  : objeto'
    # t[0] = [t[1]]
    id = inc()
    t[0] = {'id': id}
    if t[1] != None:
        dot.edge(str(id), str(t[1]['id'])) 
    # for element in t[1]:
    #     dot.edge(str(id), str(element['id']))
    gramatica = "                | <objeto>"
    no_terminal = ["<objeto>"]
    terminal = []
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_objetos")

# def p_instrucciones_objeto(t) :
#     'objeto       : CADENA'
#     id = inc()
#     t[0] = {'id': id}

#     dot.node(str(id), 'OBJETO')
#     dot.edge(str(id), 'CADENA\n' + t[1])

def p_instrucciones_objeto2(t) :
    '''objeto       : valor
                    | fun_binario_insert
                    '''
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'OBJETO')
    dot.edge(str(id), str(t[1]['id']))
    gramatica = "<objeto>	::= <valor>\n			| <fun_binario_insert>"
    no_terminal = ["<objeto>","<valor>","<fun_binario_insert>"]
    terminal = []
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"objeto") 

def p_instrucciones_lista_objeto_error(t) :
    'objeto  : error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[1], t.lexer.lineno)
    tabla_errores.agregar(error)

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
    gramatica = "<lista_insercion>	::= <lista_insercion> COMA <objeto>"
    no_terminal = ["<objeto>","<lista_insercion>"]
    terminal = ["COMA"]
    reg_gramatical = "\nlista_insercion.append(objeto.syn)\n lista_insercion.syn = lista_insercion.syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_insercion")  

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
    gramatica = "					| <lista_insercion> COMA PARIZQ SELECT <state_subquery> PARDER"
    no_terminal = ["<state_subquery>","<lista_insercion>"]
    terminal = ["COMA","PARIZQ","SELECT","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_insercion")  

def p_instrucciones_insercion_objeto(t) :
    '''lista_insercion  : objeto
                        '''
    t[0] = [t[1]]
    #para un objeto simple
    # id = inc()
    # t[0] = {'id': id}
    # dot.node(str(id), 'Insercion de Objeto')
    # dot.edge(str(id), str(t[1]['id']))
    gramatica = "					| <objeto>"
    no_terminal = ["<objeto>"]
    terminal = []
    reg_gramatical = "lista_insercion.syn = [objeto.syn]"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_insercion")   

def p_instrucciones_insercion_select(t) :
    'lista_insercion  : PARIZQ SELECT state_subquery PARDER'
    t[0] = [t[3]]
    #Para un query select
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'SUB-QUERY')

    for element in t[3]:
        dot.edge(str(id), str(element['id']))
    gramatica = "					| PARIZQ SELECT <state_subquery> PARDER"
    no_terminal = ["<state_subquery>"]
    terminal = ["PARIZQ","SELECT","PARDER"]
    reg_gramatical = "lista_insercion.syn = [state_subquery.syn]"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_insercion")      

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
    gramatica = "<deletes>	::= <delete_condicional>\n			| <delete_incondicional>"
    no_terminal = ["<deletes>","<delete_condicional>","<delete_incondicional>"]
    terminal = []
    reg_gramatical = "\ndeletes.syn = (delete_condicional or delete_incondicional).syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"deletes")  

def p_instruccion_delete_incondicional(t) :
    'delete_incondicional     : ID PTCOMA'
    t[0] = Delete_incondicional(t[1])
    print("Eliminar tabla: " + t[1])
                    
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'DELETE INCONDICIONAL')
    dot.edge(str(id), 'TABLA\n' + t[1])
    gramatica = "<delete_incondicional>	::= ID PTCOMA"
    no_terminal = ["<delete_incondicional>"]
    terminal = ["ID","PTCOMA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"delete_incondicional")

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
    gramatica = "<delete_condicional>	::= ID WHERE <relacional> PTCOMA"
    no_terminal = ["<delete_condicional>","<relacional>"]
    terminal = ["ID","WHERE","PTCOMA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"delete_condicional")

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
    if t[2] != None:
        dot.edge(str(id_id), str(t[2]['id']))  
    gramatica = "<alter_table>	::= ID <def_alter>"
    no_terminal = ["<alter_table>","<def_alter>"]
    terminal = ["ID"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"alter_table")  

def p_def_alter_error_FOREIGNKEY(t) :
    'def_alter  : ADD FOREIGN KEY PARIZQ lista_parametros PARDER REFERENCES ID PARIZQ error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[10], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'FOREIGN KEY ERROR references')

def p_def_alter_error_FOREIGNKEY_columnas(t) :
    'def_alter  : ADD FOREIGN KEY PARIZQ error PARDER REFERENCES ID PARIZQ lista_parametros PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[10], t.lexer.lineno)
    tabla_errores.agregar(error)

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
            gramatica = "<def_alter>	::= ADD COLUMN ID <tipos>"
            no_terminal = ["<tipos>","<def_alter>"]
            terminal = ["ADD","COLUMN","ID"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_alter")   
            
        elif t[2].upper() == 'CHECK':
            dot.node(str(id), 'ADD CHECK')
            dot.edge(str(id), str(t[4]['id']))
            gramatica = "			| ADD CHECK PARIZQ <relacional> PARDER"
            no_terminal = ["<relacional>"]
            terminal = ["ADD","CHECK","PARIZQ","PARDER"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_alter")   

        elif t[2].upper() == 'CONSTRAINT':
            dot.node(str(id), 'ADD CONSTRAINT')
            id_id = inc()
            dot.node(str(id_id), 'IDENTIFICADOR\n' +  t[3])
            dot.edge(str(id), str(id_id))
            dot.edge(str(id_id), 'UNIQUE')
            dot.edge(str(id_id), 'COLUMN\n' +  str(t[6]))
            gramatica = "			| ADD CONSTRAINT ID UNIQUE PARIZQ ID PARDER"
            no_terminal = []
            terminal = ["ADD","CONSTRAINT","ID","UNIQUE","PARIZQ","PARDER"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_alter") 

        elif t[2].upper() == 'FOREIGN':
            dot.node(str(id), 'ADD FOREIGN KEY')
            gramatica = "			| ADD FOREIGN KEY PARIZQ <lista_parametros> "
            no_terminal = ["<lista_parametros>"]
            terminal = ["ADD","FOREIGN","KEY","PARIZQ"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_alter") 

    elif t[1].upper() == 'DROP':
        if t[2].upper() == 'COLUMN':
            dot.node(str(id), 'DROP COLUMN')
            dot.edge(str(id), 'IDENTIFICADOR\n' +  t[3])
            gramatica = "			| DROP COLUMN ID"
            no_terminal = []
            terminal = ["DROP","COLUMN","ID"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_alter") 

        elif t[2].upper() == 'CONSTRAINT':
            dot.node(str(id), 'DROP CONSTRAINT')
            dot.edge(str(id), 'IDENTIFICADOR\n' +  str(t[3]))
            gramatica = "			| DROP CONSTRAINT ID"
            no_terminal = []
            terminal = ["DROP","CONSTRAINT","ID"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_alter") 

    elif t[1].upper() == 'ALTER':
        dot.node(str(id), 'ALTER COLUMN')
        dot.edge(str(id), 'IDENTIFICADOR\n' +  t[3])
        gramatica = "			| ALTER COLUMN ID SET NOT NULL"
        no_terminal = []
        terminal = ["ALTER","COLUMN","ID","SET","NOT","NULL"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_alter") 

    elif t[1].upper() == 'RENAME':
        id_id1 = inc()
        id_id2 = inc()
        dot.node(str(id), 'RENAME COLUMN')
        dot.node(str(id_id1), 'OLD ID\n' + t[3])
        dot.node(str(id_id2), 'NEW ID\n' + t[5])
        dot.edge(str(id), str(id_id1))
        dot.edge(str(id), str(id_id2))
        gramatica = "			| RENAME COLUMN ID TO ID"
        no_terminal = []
        terminal = ["RENAME","COLUMN","ID","TO"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_alter") 


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
    gramatica = "<tipos>	::= SMALLINT\n		| INTEGER\n		| BIGINT\n		| R_DECIMAL\n		| NUMERIC\n		| REAL\n		| DOUBLE PRECISION\n\
		| MONEY\n		| TEXT\n		| TIMESTAMP\n		| DATE\n		| TIME\n		| BOOLEAN\n		| INTERVAL"
    no_terminal = ["<tipos>"]
    terminal = ["SMALLINT","INTEGER","BIGINT","R_DECIMAL","NUMERIC","REAL","DOUBLE","PRECISION","MONEY","TEXT","TIMESTAMP","DATE","TIME","BOOLEAN","INTERVAL"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"tipos") 

def p_tipos_2(t) :
    '''tipos        : CHARACTER VARYING PARIZQ ENTERO PARDER'''
    id = inc()

    t[0] = {'tipo': TipoColumna['CHARACTER_VARYING'], 'n': t[4], 'id': id}
    dot.node(str(id), 'TIPO DE DATO\nCHARACTER VARYING')
    id_entero = inc()
    dot.node(str(id_entero), str(t[4]))
    dot.edge(str(id), str(id_entero))
    gramatica = "		| CHARACTER VARING PARIZQ ENTERO PARDER"
    no_terminal = []
    terminal = ["CHARACTER","VARING","PARIZQ","ENTERO","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"tipos")

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
    gramatica = "		| VARCHAR PARIZQ ENTERO PARDER\n		| CHARACTER PARIZQ ENTERO PARDER\n		| CHAR PARIZQ ENTERO PARDER"
    no_terminal = []
    terminal = ["CHARACTER","VARCHAR","CHAR","PARIZQ","ENTERO","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"tipos")

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
    gramatica = "		| TIMESTAMP <def_dt_types>\n		| TIME <def_dt_types>"
    no_terminal = ["<def_dt_types>"]
    terminal = ["TIMESTAMP","TIME"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"tipos")

def p_tipos_5(t) :
    '''tipos        : INTERVAL def_interval'''
    id = inc()
    dot.node(str(id), t[1])

    for element in t[2]['id']:
        dot.edge(str(id), str(element))

    t[0] = t[2]
    t[0].update({'tipo': TipoColumna[t[1].upper()], 'id': id})
    gramatica = "		| INTERVAL <def_interval>"
    no_terminal = ["<def_interval>"]
    terminal = ["INTERVAL"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"tipos")
    
def p_def_dt_types_1_error(t) :
    '''def_dt_types : PARIZQ error PARDER WITHOUT TIME ZONE
                    | PARIZQ error PARDER WITH TIME ZONE
                    | PARIZQ error PARDER'''

    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[2], t.lexer.lineno)
    tabla_errores.agregar(error)
    print(error.imprimir())

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
    gramatica = "<def_dt_types>	::= PARIZQ ENTERO PARDER WITHOUT TIME ZONE\n				| PARIZQ ENTERO PARDER WITH TIME ZONE\n\
				| PARIZQ ENTERO PARDER"
    no_terminal = ["<def_dt_types>"]
    terminal = ["PARIZQ","ENTERO","PARDER","WITHOUT","TIME","ZONE","WITH"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_dt_types")

                    
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
    gramatica = "				| WITHOUT TIME ZONE\n				| WITH TIME ZONE"
    no_terminal = ["<def_dt_types>"]
    terminal = ["WITHOUT","TIME","ZONE","WITH"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_dt_types")

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
    gramatica = "<def_interval>	::= <def_fld_to> PARIZQ ENTERO PARDER\n				| <def_fld_to>"
    no_terminal = ["<def_interval>","<def_fld_to>"]
    terminal = ["PARIZQ","ENTERO","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_interval")   

def p_def_interval_2(t) :
    '''def_interval : PARIZQ ENTERO PARDER'''
    id = inc()
    t[0] = {'p': t[2], 'id': [id]}
    dot.node(str(id), str(t[2]))
    gramatica = "				| PARIZQ ENTERO PARDER"
    no_terminal = []
    terminal = ["PARIZQ","ENTERO","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_interval") 

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
    gramatica = "<def_fld_to>	::= <def_fields> TO <def_fields>\n				| <def_fields>"
    no_terminal = ["<def_fld_to>","<def_fields>"]
    terminal = ["TO"]
    reg_gramatical = "\ndef_fld_to.syn = def_fld_to.syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_fld_to")    


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
    gramatica = "<def_fields>	::= YEAR\n				| MONTH\n				| DAY\n				| HOUR\n				| MINUTE\n\
				| SECOND"
    no_terminal = ["<def_fields>"]
    terminal = ["YEAR","MONTH","DAY","HOUR","MINUTE"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_fields") 

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
            if t[1] != None:
                dot.edge(str(id_op_signo), str(t[1]['id'])) 
            if t[3] != None:
                dot.edge(str(id_op_signo), str(t[3]['id']))  
            gramatica = "<relacional>	::= <aritmetica> MENORIGUAL <aritmetica>"
            no_terminal = ["<relacional>","<aritmetica>"]
            terminal = ["MENORIGUAL"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"relacional")   

        elif t[2].upper() == '<':
            dot.node(str(id_op_signo), 'MENOR')
            dot.edge(str(id), str(id_op_signo))
            if t[1] != None:
                dot.edge(str(id_op_signo), str(t[1]['id'])) 
            if t[3] != None:
                dot.edge(str(id_op_signo), str(t[3]['id']))   
            gramatica = "				| <aritmetica> MENOR <aritmetica>"
            no_terminal = ["<aritmetica>"]
            terminal = ["MENOR"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"relacional")   
            
        elif t[2].upper() == '>=':
            dot.node(str(id_op_signo), 'MAYOR O IGUAL')
            dot.edge(str(id), str(id_op_signo))
            if t[1] != None:
                dot.edge(str(id_op_signo), str(t[1]['id'])) 
            if t[3] != None:
                dot.edge(str(id_op_signo), str(t[3]['id']))    
            gramatica = "				| <aritmetica> MAYORIGUAL <aritmetica>"
            no_terminal = ["<aritmetica>"]
            terminal = ["MAYORIGUAL"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"relacional")   
            
        elif t[2].upper() == '>':
            dot.node(str(id_op_signo), 'MAYOR')
            dot.edge(str(id), str(id_op_signo))
            if t[1] != None:
                dot.edge(str(id_op_signo), str(t[1]['id'])) 
            if t[3] != None:
                dot.edge(str(id_op_signo), str(t[3]['id']))   
            gramatica = "				| <aritmetica> MAYOR <aritmetica>"
            no_terminal = ["<aritmetica>"]
            terminal = ["MAYOR"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"relacional")  
            
        elif t[2].upper() == '=':
            dot.node(str(id_op_signo), 'IGUAL')
            dot.edge(str(id), str(id_op_signo))
            if t[1] != None:
                dot.edge(str(id_op_signo), str(t[1]['id'])) 
            if t[3] != None:
                dot.edge(str(id_op_signo), str(t[3]['id']))    
            gramatica = "				| <aritmetica> IGUAL <aritmetica>"
            no_terminal = ["<aritmetica>"]
            terminal = ["IGUAL"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"relacional")  
            
        # PARA LOS OPERADORES LOGICOS
        elif t[2].upper() == 'AND':
            dot.node(str(id_op_signo), 'AND')
            dot.edge(str(id), str(id_op_signo))
            if t[1] != None:
                dot.edge(str(id_op_signo), str(t[1]['id'])) 
            if t[3] != None:
                dot.edge(str(id_op_signo), str(t[3]['id']))   
            
            gramatica = "				| <relacional> AND <relacional>"
            no_terminal = ["<relacional>"]
            terminal = ["AND"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"relacional")  

        elif t[2].upper() == 'OR':
            dot.node(str(id_op_signo), 'OR')
            dot.edge(str(id), str(id_op_signo))
            if t[1] != None:
                dot.edge(str(id_op_signo), str(t[1]['id'])) 
            if t[3] != None:
                dot.edge(str(id_op_signo), str(t[3]['id']))    
            gramatica = "				| <relacional> OR <relacional>"
            no_terminal = ["<relacional>"]
            terminal = ["OR"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"relacional")  

    elif len(t) == 5:
        id_op_signo = inc()
        if t[2].upper() == '=':
            dot.node(str(id_op_signo), 'IGUAL IGUAL')
            dot.edge(str(id), str(id_op_signo))
            if t[1] != None:
                dot.edge(str(id_op_signo), str(t[1]['id'])) 
            if t[3] != None:
                dot.edge(str(id_op_signo), str(t[4]['id']))   

            gramatica = "				| <aritmetica> IGUAL IGUAL <aritmetica>"
            no_terminal = ["<aritmetica>"]
            terminal = ["IGUAL"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"relacional") 
    else:
        id_op_signo = inc()
        dot.node(str(id_op_signo), 'NOT')
        dot.edge(str(id), str(id_op_signo))
        if t[2] != None:
            dot.edge(str(id_op_signo), str(t[2]['id'])) 

        gramatica = "				| NOT <relacional>"
        no_terminal = ["<relacional>"]
        terminal = ["NOT"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"relacional") 

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
    id = inc()
    t[0] = {'id' : id}
    dot.node(str(id),  'OPERACION RELACIONAL')

    if len(t) == 4:
        idsigno = inc()
        dot.node(str(idsigno), str(t[2]))
        dot.edge(str(id), str(idsigno))
        if t[3] != None:
            dot.edge(str(idsigno), str(t[3]['id']))
    else:
        idsigno = inc()
        dot.node(str(idsigno), str(t[2] + t[3]))
        dot.edge(str(id), str(idsigno))
        if t[4] != None:
            dot.edge(str(idsigno), str(t[4]['id']))


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
    id = inc()
    t[0] = {'id' : id}
    dot.node(str(id),  'OPERACION RELACIONAL')

    if len(t) == 4:
        idsigno = inc()
        dot.node(str(idsigno), str(t[2]))
        dot.edge(str(id), str(idsigno))
        if t[1] != None:
            dot.edge(str(idsigno), str(t[1]['id']))
    else:
        idsigno = inc()
        dot.node(str(idsigno), str(t[2] + t[3]))
        dot.edge(str(id), str(idsigno))
        if t[1] != None:
            dot.edge(str(idsigno), str(t[1]['id']))

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
        gramatica = "				| EXISTS <state_subquery>"
        no_terminal = ["<state_subquery>"]
        terminal = ["EXISTS"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"relacional") 

    elif t[1].upper() == 'IN':
        dot.node(str(id_op), 'IN')
        dot.edge(str(id), str(id_op))
        dot.edge(str(id_op), str(t[2]['id']))
        gramatica = "				| IN <state_subquery>"
        no_terminal = ["<state_subquery>"]
        terminal = ["IN"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"relacional")  

    elif t[1].upper() == 'NOT':
        if t[2].upper() == 'IN':
            dot.node(str(id_op), 'NOT IN')
            dot.edge(str(id), str(id_op))
            dot.edge(str(id_op), str(t[3]['id']))
            gramatica = "				| NOT IN <state_subquery>"
            no_terminal = ["<state_subquery>"]
            terminal = ["NOT","IN"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"relacional") 
        else: 
            dot.node(str(id_op), 'NOT EXISTS')
            dot.edge(str(id), str(id_op))
            dot.edge(str(id_op), str(t[3]['id']))

    elif t[1].upper() == 'ANY':
        dot.node(str(id_op), 'ANY')
        dot.edge(str(id), str(id_op))
        dot.edge(str(id_op), str(t[2]['id']))
        gramatica = "				| ANY <state_subquery>"
        no_terminal = ["<state_subquery>"]
        terminal = ["ANY"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"relacional")  

    elif t[1].upper() == 'ALL':
        dot.node(str(id_op), 'ALL')
        dot.edge(str(id), str(id_op))
        dot.edge(str(id_op), str(t[2]['id']))
        gramatica = "				| ALL <state_subquery>"
        no_terminal = ["<state_subquery>"]
        terminal = ["ALL"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"relacional")  

    elif t[1].upper() == 'SOME':
        dot.node(str(id_op), 'SOME')
        dot.edge(str(id), str(id_op))
        dot.edge(str(id_op), str(t[2]['id']))
        gramatica = "				| SOME <state_subquery>"
        no_terminal = ["<state_subquery>"]
        terminal = ["SOME"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"relacional")  


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
    gramatica = "				| <state_between>\n				| <state_predicate_nulls>\n				| <state_is_distinct>\n\
				| <state_pattern_match>"
    no_terminal = ["<state_between>","<state_predicate_nulls>","<state_is_distinct>","<state_pattern_match>"]
    terminal = []
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"relacional")  
        
def p_aritmetica1(t) :
    '''aritmetica   : PARIZQ aritmetica PARDER
                    | PARIZQ relacional PARDER'''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'Valor aritmetico' )
    dot.edge(str(id), str(t[2]['id']))
    gramatica = "<aritmetica>	::= PARIZQ <aritmetica> PARDER\n				| PARIZQ <relacional> PARDER"
    no_terminal = ["<aritmetica>","<relacional>"]
    terminal = ["PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"aritmetica") 

def p_aritmetica(t) :
    '''aritmetica   : aritmetica MAS aritmetica
                    | aritmetica MENOS aritmetica
                    | aritmetica POR aritmetica
                    | aritmetica DIVISION aritmetica
                    | aritmetica MODULO aritmetica
                    | aritmetica EXP aritmetica
                    | MENOS aritmetica 
                    | valor'''
    id = inc()
    dot.node(str(id), 'Valor aritmetico' )

    if len(t) == 2:
        if t[1] != None:
            
            t[0] = {'id': id, 'valor': str(t[1]['valor'])}
            dot.edge(str(id), str(t[1]['id'])) 

    elif len(t) == 3:
        if t[2] != None:
            #valor = type_checker.Validando_Operaciones_Aritmeticas((t[2]['valor']), (t[2]['valor']), 'NEGATIVO')
            t[0] = {'id': id}
            dot.edge(str(id), 'NEGATIVO')
            dot.edge(str(id), str(t[2]['id'])) 
    else:
        if t[1] != None and t[3] != None:
            #valor = type_checker.Validando_Operaciones_Aritmeticas((t[1]['valor']), (t[3]['valor']), str(t[2]))
            t[0] = {'id': id}
            dot.edge(str(id), str(t[1]['id'])) 
            dot.edge(str(id), t[2])
            dot.edge(str(id), str(t[3]['id'])) 

    gramatica = "				| <aritmetica> MAS <aritmetica>\n				| <aritmetica> MENOS <aritmetica>\n\
				| <arimtetica> POR <aritmetica>\n				| <aritmetica> DIVISION <aritmetica>\n\
				| <aritmetica> MODULO <aritmetica>\n				| <aritmetica> EXP <aritmetica>"
    no_terminal = ["<aritmetica>"]
    terminal = ["MAS","MENOS","POR","DIVISION","MODULO","EXP"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"aritmetica") 

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
    id = inc()
    dot.node(str(id), 'Valor aritmetico' )
    if t[3] != None and t[3] != ')':
        idoperador = inc()
        dot.node(str(idoperador), t[2])
        dot.edge(str(id), str(idoperador))
        dot.edge(str(idoperador), str(t[3]['id']))
        t[0] = {'id':id, 'valor':t[3]['valor']}
    else:
        t[0] = {'id':id,'valor':0}

def p_aritmetica_error2(t) :
    '''aritmetica   : aritmetica MAS error
                    | aritmetica MENOS error
                    | aritmetica POR error
                    | aritmetica DIVISION error
                    | aritmetica MODULO error
                    | aritmetica EXP error'''
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    dot.node(str(id), 'Valor aritmetico' )
    if t[1] != None and t[1] != ')':
        idoperador = inc()
        dot.node(str(idoperador), t[2])
        dot.edge(str(id), str(idoperador))
        dot.edge(str(idoperador), str(t[1]['id']))
        t[0] = {'id':id,'valor':t[1]['valor']}
    else:
        t[0] = {'id':id, 'valor':0}

def p_aritmetica2(t) :
    '''aritmetica   : funciones_math_esenciales
                    | fun_binario_select
                    '''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'Funciones')

    dot.edge(str(id), str(t[1]['id'])) 

def p_aritmetica1_2(t) :
    '''aritmetica   : lista_funciones
                    '''
    '''if t[1]['funcion'] != 'MOD' and t[1]['funcion'] != 'POWER'and t[1]['funcion'] != 'WIDTH_BUCKET'and t[1]['funcion'] != 'DIV' and t[1]['funcion'] != 'GCD':
        resultado = type_checker.Funciones_Matematicas_1( t[1]['funcion'], t[1]['valor'], line = t.lexer.lineno)
    else:
        resultado = type_checker.Funciones_Matematicas_2( t[1]['funcion'], t[1]['valor'], t[1]['valor2'], line = t.lexer.lineno)
    print("=========>>>", resultado)'''

    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'Funciones')

    dot.edge(str(id), str(t[1]['id'])) 

def p_aritmetica3(t) :
    '''aritmetica   : fun_trigonometrica'''
    '''if t[1]['funcion'].upper() != 'ATAN2D' and t[1]['funcion'].upper() != 'ATAN2':
        resultado = type_checker.Funciones_Trigonometricas_1(t[1]['funcion'], t[1]['valor'], line = t.lexer.lineno)
    else:
        resultado = type_checker.Funciones_Trigonometricas_2(t[1]['funcion'], t[1]['valor1'], t[1]['valor1'], line = t.lexer.lineno)
  '''
    #print("================================>", resultado)
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'Funciones')
    if type(t[1]) == list:
        for element in t[1]:
            dot.edge(str(id), str(element['id']))
    else:
        dot.edge(str(id), str(t[1]['id'])) 
    # for element in t[1]:
    #     dot.edge(str(id), str(element['id']))
    gramatica = "				| <funciones_math_esenciales>\n				| <lista_funciones>\n				| <fun_binario_select>\n\
				| <fun_trigonometrica>"
    no_terminal = ["<funciones_math_esenciales>","<lista_funciones>","<fun_binario_select>","<fun_trigonometrica>"]
    terminal = []
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"aritmetica") 

def p_valor_id(t) :
    '''valor        : ID
                    | ID PUNTO ID'''
    id = inc()

    if len(t) == 2:
        t[0] = {'id': id, 'valor': str(t[1])}
        dot.node(str(id), 'IDENTIFICADOR\n' + str(t[1]))
        # dot.edge(str(id), ' '+ str(t[1]) )
        gramatica = "<valor>	::= ID"
        no_terminal = ["<valor>"]
        terminal = ["ID"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"valor")
    else:
        t[0] = {'id': id, 'valor': str(t[1] + t[2] + t[3])}
        dot.node(str(id), 'FIELD\n' + t[1] + t[2] + t[3])
        # dot.edge(str(id), t[1] + t[2] + t[3])
        gramatica = "		| ID PUNT ID"
        no_terminal = []
        terminal = ["ID","PUNTO"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"valor")

def p_valor_num(t) :
    '''valor        : ENTERO
                    | DECIMAL  '''
    id = inc()
    t[0] = {'id': id, 'valor': str(t[1])}
    dot.node(str(id), 'NUMERO\n'+ str(t[1]))
    # dot.edge(str(id), ' '+ str(t[1]) )
    gramatica = "		| ENTERO\n		| DECIMAL"
    no_terminal = []
    terminal = ["ENTERO","DECIMAL"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"valor")

def p_valor(t) :
    '''valor        : CADENA
                    '''
    id = inc()
    t[0] = {'id': id, 'valor': str(t[1])}
    dot.node(str(id), 'CADENA\n'+ str(t[1]))
    # dot.edge(str(id), ' '+ str(t[1]) )
    gramatica = "		| CADENA"
    no_terminal = []
    terminal = ["CADENA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"valor")

def p_valor2(t) :
    '''valor        : lista_funciones_where
                    | fun_binario_where
                    | state_subquery
                    | fun_binario_update
                    | fun_binario_select
                    '''
    id = inc()
    try:
        if t[1]['valor'] != None:
            t[0] = {'id':id, 'valor':t[1]['valor']}
    except KeyError:
        #REVISAR FALTA PONER ALGO AQUÍ PARA VALIDAR QUE CONTENGA VALOR, YA QUE ESO SE REQUIERE EN ARITMETICA
        t[0] = {'id': id, 'valor':0}
    dot.node(str(id), 'FUNCIONES')
    # for element in t[1]:
    #     dot.edge(str(id), str(element['id']))
    if t[1] != None:
        if type(t[1]) == list:
            for element in t[1]:
                dot.edge(str(id), str(element['id']))     
        else:
            dot.edge(str(id), str(t[1]['id'])) 
        

    gramatica = "		| <lista_funciones_where>\n		| <fun_binario_where>\n		| <state_subquery>\n        | <fun_binario_update>\n\
        | <fun_binario_select>"
    no_terminal = ["<lista_funciones_where>","<fun_binario_where>","<state_subquery>","<fun_binario_update>","<fun_binario_select>"]
    terminal = []
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"valor")

def p_valor3(t) :
    '''valor        : fun_trigonometrica
                    '''
    '''if t[1]['funcion'].upper() != 'ATAN2D' and t[1]['funcion'].upper() != 'ATAN2':
        resultado = type_checker.Funciones_Trigonometricas_1(t[1]['funcion'], t[1]['valor'], line = t.lexer.lineno)
    else:
        resultado = type_checker.Funciones_Trigonometricas_2(t[1]['funcion'], t[1]['valor1'], t[1]['valor1'], line = t.lexer.lineno)
  '''
    #print("================================>", resultado)
  
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'FUNCIONES')
    # for element in t[1]:
    #     dot.edge(str(id), str(element['id']))
        
    dot.edge(str(id), str(t[1]['id']))
    gramatica = "		| <fun_trigonometrica>"
    no_terminal = ["<fun_trigonometrica>"]
    terminal = []
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"valor") 

def p_valor4(t) :
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
    gramatica = "		| <date_functions>"
    no_terminal = ["<date_functions>"]
    terminal = []
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"valor") 

'''
def p_valor_error(t) :
    'valor  : error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[1], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[0] = {'id':id}
    dot.node(str(id), 'ERROR')
    '''

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
    gramatica = "<update_table>	::= ID SET <def_update> WHERE <relacional>"
    no_terminal = ["<update_table>","<def_update>","<relacional>"]
    terminal = ["ID","SET","WHERE"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"update_table") 

def p_instruccion_update_where_error(t) :
    'update_table   : ID SET error WHERE relacional'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[1], t.lexer.lineno)
    tabla_errores.agregar(error)
    id = inc()
    t[0] = {'id':id}

    dot.node(str(id), 'UPDATE')
    dot.edge(str(id), 'TABLA\n' + t[1])
    

def p_instruccion_update(t) :
    '''update_table : ID SET def_update'''
    print("UPDATE TABLE")
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'UPDATE')
    dot.edge(str(id), 'TABLA\n' + t[1])

    for element in t[3]:
        dot.edge(str(id), str(element['id']))
    gramatica = "				| ID SET <def_update>"
    no_terminal = ["<def_update>"]
    terminal = ["ID","SET"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"update_table")

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
    gramatica = "<def_update>	::= <def_update> COMA <def_update_asig>"
    no_terminal = ["<def_update>","<def_update_asig>"]
    terminal = ["COMA"]
    reg_gramatical = "\ndef_update.append(def_update_asig.syn)\n def_update.syn = def_update.syn"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_update") 

def p_def_update_rec_error2(t) :
    'def_update : def_update COMA error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_def_update(t) :
    '''def_update   : def_update_asig'''
    t[0] = [t[1]]
    # id = inc()
    # t[0] = {'id': id}
    # dot.node(str(id), 'ASIGNACION')
    # dot.edge(str(id), 'IDENTIFICADOR\n' + t[1])
    # dot.edge(str(id), str(t[3]['id'])) 
    gramatica = "				| <def_update_asig>"
    no_terminal = ["<def_update_asig>"]
    terminal = []
    reg_gramatical = "\ndef_update.syn = [def_update_asig.syn]"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_update") 

def p_def_update_error(t) :
    'def_update : error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[1], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_def_update_2(t) :
    '''def_update_asig   : ID IGUAL valor'''
    id = inc()
    t[0] = {'id': id}
    dot.node(str(id), 'ASIGNACION')
    dot.edge(str(id), 'IDENTIFICADOR\n' + t[1])
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "<def_update_asig>   : ID IGUAL <valor>"
    no_terminal = ["<def_update_asig>","<valor>"]
    terminal = ["ID","IGUAL"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"def_update_asig") 

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
            gramatica = "				| <valor> NOT IN <state_subquery>"
            no_terminal = ["<state_subquery>","<valor>"]
            terminal = ["NOT","IN"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_between")
        else:
            dot.node(str(id), 'NOT BETWEEN')
            dot.edge(str(id), str(t[1]['id'])) 
            id_and = inc()
            dot.node(str(id_and), 'AND')
            dot.edge(str(id), str(id_and))
            dot.edge(str(id_and), str(t[4]['id'])) 
            dot.edge(str(id_and), str(t[6]['id'])) 
            gramatica = "				| <valor> NOT BETWEEN <valor> AND <valor>"
            no_terminal = ["<valor>"]
            terminal = ["NOT","BETWEEN","AND"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_between")
    else:
        dot.node(str(id), 'BETWEEN')
        dot.edge(str(id), str(t[1]['id'])) 
        id_and = inc()
        dot.node(str(id_and), 'AND')
        dot.edge(str(id), str(id_and))
        dot.edge(str(id_and), str(t[3]['id'])) 
        dot.edge(str(id_and), str(t[5]['id']))
        gramatica = "<state_between>	::= <valor> BETWEEN <valor> AND <valor>"
        no_terminal = ["<valor>","<state_between>"]
        terminal = ["BETWEEN","AND"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_between") 

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
        gramatica = "						| <valor> IS NOT DISTINCT FROM <valor> <state_aliases_table>"
        no_terminal = ["<valor>","<state_aliases_table>"]
        terminal = ["IS","NOT","DISTINCT","FROM"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_is_distinct") 
    else:
        dot.node(str(id), 'IS DISTINCT')
        dot.edge(str(id), str(t[1]['id'])) 
        dot.edge(str(id), str(t[5]['id'])) 
        # dot.edge(str(id), t[5] + ' [table]')
        if type(t[6]) != list:
            dot.edge(str(id), str(t[6]['id'])) 
        
        gramatica = "<state_is_distinct>	::= <valor> IS DISTINCT FROM <valor> <state_aliases_table>"
        no_terminal = ["<valor>","<state_aliases_table>","<state_is_distinct>"]
        terminal = ["IS","DISTINCT","FROM"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_is_distinct") 
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
            gramatica = "						| <valor> IS NOT NULL"
            no_terminal = ["<valor>"]
            terminal = ["IS","NOT","NULL"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_predicate_nulls") 
        else:
            dot.edge(str(id), 'PREDICATES\nIS NULL')
            dot.edge(str(id), str(t[1]['id']))
            gramatica = "<state_predicate_nulls>	::= <valor> IS NULL"
            no_terminal = ["<valor>","<state_predicate_nulls>"]
            terminal = ["IS","NULL"]
            reg_gramatical = ""
            gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_predicate_nulls")  
    else:
        dot.node(str(id), 'PREDICATES\n' + t[2])
        dot.edge(str(id), str(t[1]['id']))
        gramatica = "						| <valor> ISNULL\n						| <valor> NOTNULL"
        no_terminal = ["<valor>"]
        terminal = ["ISNULL","NOTNULL"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_predicate_nulls")  
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
    gramatica = "<state_pattern_match>	::= <aritmetica> LIKE CADENA\n						| <aritmetica> LIKE CADENA_DOBLE"
    no_terminal = ["<state_pattern_match>","<aritmetica>"]
    terminal = ["LIKE","CADENA","CADENA_DOBLE"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_pattern_match")
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
        gramatica = "						| ID"
        no_terminal = ["<state_aliases_table>"]
        terminal = ["ID"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_aliases_table")
    else:
        dot.node(str(id), 'ALIAS\n' + t[2])
        gramatica = "<state_aliases_table>	::= AS ID"
        no_terminal = ["<state_aliases_table>"]
        terminal = ["AS","ID"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_aliases_table")


def p_aliases_table2(t):
    ' state_aliases_table     : '
    t[0] = []
    gramatica = "						| epsilon"
    no_terminal = []
    terminal = ["epsilon"]
    reg_gramatical = "\nstate_aliases_table.syn = []"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_aliases_table")
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
        gramatica = "<state_aliases_field>	::= AS CADENA\n						| AS CADNEA_DOBLE\n						| AS ID"
        no_terminal = ["<state_aliases_field>"]
        terminal = ["AS","CADENA","CADNEA_DOBLE","ID"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_aliases_field")
    else:
        dot.node(str(id), 'ALIAS\n' + t[1])
        gramatica = "						| ID"
        no_terminal = []
        terminal = ["ID"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_aliases_field")

def p_aliases_field2(t):
    ' state_aliases_field     : '
    t[0] = []
    gramatica = "						| epsilon"
    no_terminal = []
    terminal = ["epsilon"]
    reg_gramatical = "\nstate_aliases_field.syn = []"
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"state_aliases_field")
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
        gramatica = "				| <auxcase_state> END"
        no_terminal = ["<auxcase_state>"]
        terminal = ["END"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"case_state")
    else:
        dot.edge(str(id), str(t[1]['id']))
        gramatica = "<case_state>	::= <case_state> <auxcase_state> END"
        no_terminal = ["<case_state>","<auxcase_state>"]
        terminal = ["END"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"case_state") 
            
    dot.edge(str(id), str(t[2]['id'])) 
    dot.edge(str(id), 'END')
                      
def p_auxcase_state(t):
    'auxcase_state  : WHEN relacional THEN CADENA'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'WHEN')
    dot.edge(str(id), str(t[2]['id']))
        
    dot.edge(str(id), t[4])
    gramatica = "<auxcase_state>	::= WHEN <relacional> THEN CADENA"
    no_terminal = ["<auxcase_state>","<relacional>"]
    terminal = ["WHEN","THEN","CADENA"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"auxcase_state") 

def p_auxcase_state2(t):
    'auxcase_state  : ELSE COMILLA_SIMPLE ID COMILLA_SIMPLE'
    id = inc()
    t[0] = [{'id': id}]

    dot.node(str(id), 'ELSE')
    dot.edge(str(id), t[3])
    gramatica = "				| ELSE COMILLA_SIMPLE ID COMILLA_SIMPLE"
    no_terminal = []
    terminal = ["ELSE","COMILLA_SIMPLE","ID"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"auxcase_state")
#========================================================

# FUNCIONES MATEMÁTICAS
def p_instrucciones_funcion_count(t):
    '''funciones_math_esenciales    : COUNT PARIZQ lista_funciones_math_esenciales PARDER parametro
                                    | COUNT PARIZQ lista_funciones_math_esenciales PARDER'''
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'COUNT')
    if len == 5:
        for element in t[3]:
            dot.edge(str(id), str(element['id']))
        gramatica = "<funciones_math_esenciales>	::= COUNT PARIZQ <lista_funciones_math_esenciales> PARDER"
        no_terminal = ["<funciones_math_esenciales>","<lista_funciones_math_esenciales>"]
        terminal = ["COUNT","PARIZQ","PARDER"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"funciones_math_esenciales")
    else:
        for element in t[3]:
            dot.edge(str(id), str(element['id']))
        dot.edge(str(id), t[5])
        gramatica = "							| COUNT PARIZQ <lista_funciones_math_esenciales> PARDER <parametro>"
        no_terminal = ["<parametro>","<lista_funciones_math_esenciales>"]
        terminal = ["COUNT","PARIZQ","PARDER"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"funciones_math_esenciales")

def p_instrucciones_funcion_sum(t):
    '''funciones_math_esenciales    : SUM PARIZQ lista_funciones_math_esenciales PARDER parametro
                                    | SUM PARIZQ lista_funciones_math_esenciales PARDER'''
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SUM')
    if len(t) == 5:
        if type(t[3]) == list:
            for element in t[3]:
                dot.edge(str(id), str(element['id']))
        else:
            dot.edge(str(id), str(t[3]['id']))

        gramatica = "<funciones_math_esenciales>	::= SUM PARIZQ <lista_funciones_math_esenciales> PARDER"
        no_terminal = ["<funciones_math_esenciales>","<lista_funciones_math_esenciales>"]
        terminal = ["SUM","PARIZQ","PARDER"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"funciones_math_esenciales")
    else:
        if type(t[3]) == list:
            for element in t[3]:
                dot.edge(str(id), str(element['id']))
        else:
            dot.edge(str(id), str(t[3]['id']))
        dot.edge(str(id), t[5])
        gramatica = "							| SUM PARIZQ <lista_funciones_math_esenciales> PARDER <parametro>"
        no_terminal = ["<parametro>","<lista_funciones_math_esenciales>"]
        terminal = ["SUM","PARIZQ","PARDER"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"funciones_math_esenciales")

def p_instrucciones_funcion_avg(t):
    '''funciones_math_esenciales    : AVG PARIZQ lista_funciones_math_esenciales PARDER
                                    | AVG PARIZQ lista_funciones_math_esenciales PARDER parametro
                                    '''
    
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'AVG')
    
    if len == 5:
        # for element in t[3]:
        #     dot.edge(str(id), str(element['id']))
        gramatica = "<funciones_math_esenciales>	::= AVG PARIZQ <lista_funciones_math_esenciales> PARDER"
        no_terminal = ["<funciones_math_esenciales>","<lista_funciones_math_esenciales>"]
        terminal = ["AVG","PARIZQ","PARDER"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"funciones_math_esenciales")
    else:
        dot.edge(str(id), str(t[3]['id'])) 
        # for element in t[3]:
        #     dot.edge(str(id), str(element['id']))
        dot.edge(str(id), str(t[5]['id']))
        gramatica = "							| AVG PARIZQ <lista_funciones_math_esenciales> PARDER <parametro>"
        no_terminal = ["<parametro>","<lista_funciones_math_esenciales>"]
        terminal = ["AVG","PARIZQ","PARDER"]
        reg_gramatical = ""
        gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"funciones_math_esenciales") 

def p_lista_instrucciones_funcion_math(t):
    '''lista_funciones_math_esenciales  : aritmetica
                                        | lista_id
                                        '''
    id = inc()
    if type(t[1]) != list:
        t[0] = {'id': id, 'valor': t[1]['valor']}
    else:
        t[0] = {'id':id, 'valor':t[1]}
    dot.node(str(id), 'PARAMETROS')
    if type(t[1]) != list:
        dot.edge(str(id), str(t[1]['id']))
    else:
        for element in t[1]:
            id2 = inc()
            dot.node(str(id2),str(element))
            dot.edge(str(id), str(id2))
    
def p_lista_instrucciones_funcion_math2(t):
    '''lista_funciones_math_esenciales  : POR'''
    id = inc()
    t[0] = {'id': id, 'valor': '*'}

    dot.node(str(id), t[1])

    gramatica = "<lista_funciones_math_esenciales>	::= <aritmetica>\n									| <lista_id>\n\
									| POR"
    no_terminal = ["<aritmetica>","<lista_funciones_math_esenciales>","<lista_id>"]
    terminal = ["POR"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones_math_esenciales")

#SOLO ESTOS SE PUEDEN USAR EN EL WHERE
def p_instrucciones_funcion_abs_where(t) :
    'lista_funciones_where    : ABS PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ABS')
    dot.edge(str(id), str(t[3]['id'])) 
    # for element in t[3]:
    #     dot.edge(str(id), str(element['id']))
    gramatica = "<lista_funciones_where>	::= ABS PARIZQ <funcion_math_parametro> PARDER"
    no_terminal = ["<lista_funciones_where>","<funcion_math_parametro>"]
    terminal = ["ABS","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones_where")

def p_instrucciones_funcion_cbrt_where(t) :
    'lista_funciones_where    : CBRT PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'CBRT')
    dot.edge(str(id), str(t[3]['id'])) 
    # for element in t[3]:
    #     dot.edge(str(id), str(element['id']))
    gramatica = "						| CBRT PARIZQ <funcion_math_parametro> PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["CBRT","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones_where")

def p_instrucciones_funcion_ceil_where(t) :
    'lista_funciones_where    : CEIL PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'CEIL')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| CEIL PARIZQ <funcion_math_parametro> PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["CEIL","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones_where") 

def p_instrucciones_funcion_cieling_where(t) :
    'lista_funciones_where    : CEILING PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'CEILING')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| CEILING PARIZQ <funcion_math_parametro> PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["CEILING","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones_where")  

#ESTOS SE USAN EN EL SELECT
def p_instrucciones_funcion_abs_select(t) :
    'lista_funciones    : ABS PARIZQ funcion_math_parametro PARDER'

    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor']}
    dot.node(str(id), 'ABS')
    dot.edge(str(id), str(t[3]['id'])) 
    # for element in t[3]:
    #     dot.edge(str(id), str(element['id']))
    gramatica = "<lista_funciones>	::= ABS PARIZQ <funcion_math_parametro>	PARDER"
    no_terminal = ["<lista_funciones>","<funcion_math_parametro>"]
    terminal = ["ABS","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones")

def p_instrucciones_funcion_cbrt_select(t) :
    'lista_funciones    : CBRT PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor']}

    dot.node(str(id), 'CBRT')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "					| CBRT PARIZQ <funcion_math_parametro> PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["CBRT","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones") 

def p_instrucciones_funcion_ceil_select(t) :
    'lista_funciones    : CEIL PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor']}

    dot.node(str(id), 'CEIL')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "					| CEIL PARIZQ <funcion_math_parametro> PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["CEIL","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones") 

def p_instrucciones_funcion_cieling_select(t) :
    'lista_funciones    : CEILING PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor']}

    dot.node(str(id), 'CEILING')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "					| CEILING PARIZQ <funcion_math_parametro> PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["CEILING","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones") 

def p_instrucciones_funcion_degrees(t) :
    'lista_funciones    : DEGREES PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor']}

    dot.node(str(id), 'DEGREES')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "					| DEGREES PARIZQ <funcion_math_parametro> PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["DEGREES","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones")  

def p_instrucciones_funcion_div(t) :
    'lista_funciones    : DIV PARIZQ funcion_math_parametro COMA ENTERO PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor'], 'valor2': t[5]}

    dot.node(str(id), 'DIV')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "					| DIV PARIZQ <funcion_math_parametro> COMA ENTERO PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["DEGREES","PARIZQ","COMA","ENTERO","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones") 

def p_instrucciones_funcion_exp(t) :
    'lista_funciones    : EXP PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor']}

    dot.node(str(id), 'EXP')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "					| EXP PARIZQ <funcion_math_parametro> PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["EXP","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones")  

def p_instrucciones_funcion_factorial(t) :
    'lista_funciones    : FACTORIAL PARIZQ ENTERO PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': str(t[3]) }

    dot.node(str(id), 'FACTORIAL')
    dot.edge(str(id), str(t[3]))
    gramatica = "					| FACTORIAL PARIZQ ENTERO PARDER"
    no_terminal = []
    terminal = ["FACTORIAL","PARIZQ","ENTERO","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones")

def p_instrucciones_funcion_floor(t) :
    'lista_funciones    : FLOOR PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor']}

    dot.node(str(id), 'FLOOR')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "					| FLOOR PARIZQ <funcion_math_parametro> PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["FLOOR","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones") 

def p_instrucciones_funcion_gcd(t) :
    'lista_funciones    : GCD PARIZQ ENTERO COMA ENTERO PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3], 'valor2': t[5]}

    dot.node(str(id), 'GCD')
    dot.edge(str(id), t[3] + ', ' + t[5])
    gramatica = "					| GCD PARIZQ COMA ENTERO COMA PARDER"
    no_terminal = []
    terminal = ["GCD","PARIZQ","COMA","ENTERO","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones")

def p_instrucciones_funcion_ln(t) :
    'lista_funciones    : LN PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor']}

    dot.node(str(id), 'LN')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "					| LN PARIZQ <funcion_math_parametro> PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["LN","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones") 

def p_instrucciones_funcion_log(t) :
    'lista_funciones    : LOG PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor']}

    dot.node(str(id), 'LOG')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "					| LOG PARIZQ <funcion_math_parametro> PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["LOG","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones") 

def p_instrucciones_funcion_mod(t) :
    'lista_funciones    : MOD PARIZQ funcion_math_parametro COMA ENTERO PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor'], 'valor2': t[5]}

    dot.node(str(id), 'MOD')
    dot.edge(str(id), str(t[3]['id'])) 

    dot.edge(str(id), str(t[5]))
    gramatica = "					| MOD PARIZQ <funcion_math_parametro> COMA ENTERO PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["MOD","PARIZQ","PARDER","COMA","ENTERO"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones")

def p_instrucciones_funcion_pi(t) :
    'lista_funciones    : PI PARIZQ PARDER'
    id = inc()
    t[0] = {'id': id}
    t[0] = {'id': id, 'funcion': t[1], 'valor': 1}

    dot.node(str(id), 'PI')
    gramatica = "					| PI PARIZQ PARDER"
    no_terminal = []
    terminal = ["PI","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones")

def p_instrucciones_funcion_power(t) :
    'lista_funciones    : POWER PARIZQ funcion_math_parametro COMA ENTERO PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor'], 'valor2': t[5]}

    dot.node(str(id), 'POWER')
    dot.edge(str(id), str(t[3]['id'])) 

    dot.edge(str(id), t[5])
    gramatica = "					| POWER PARIZQ <funcion_math_parametro> COMA ENTERO PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["POWER","PARIZQ","PARDER","COMA","ENTERO"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones")

def p_instrucciones_funcion_radians(t) :
    'lista_funciones    : RADIANS PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor']}

    dot.node(str(id), 'RADIANS')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "					| RADIANS PARIZQ <funcion_math_parametro> PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["RADIANS","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones") 

def p_instrucciones_funcion_round(t) :
    'lista_funciones    : ROUND PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor']}

    dot.node(str(id), 'ROUND')
    dot.edge(str(id), str(t[3]['id'])) 
    gramatica = "					| ROUND PARIZQ <funcion_math_parametro> PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["ROUND","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones") 

def p_instrucciones_funcion_sign(t) :
    'lista_funciones    : SIGN PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor']}

    dot.node(str(id), 'SIGN')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "					| SIGN PARIZQ <funcion_math_parametro> PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["SIGN","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones") 

def p_instrucciones_funcion_sqrt(t) :
    'lista_funciones    : SQRT PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor']}

    dot.node(str(id), 'SQRT')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "					| SQRT PARIZQ <funcion_math_parametro> PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["SQRT","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones") 

def p_instrucciones_funcion_width_bucket(t) :
    'lista_funciones    : WIDTH_BUCKET PARIZQ funcion_math_parametro COMA funcion_math_parametro COMA funcion_math_parametro COMA funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor']}

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
    gramatica = "					| WIDTH_BUCKET PARIZQ <funcion_math_parametro> COMA <funcion_math_parametro> COMA <funcion_math_parametro> COMA <funcion_math_parametro> PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["WIDTH_BUCKET","PARIZQ","COMA","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones")

def p_instrucciones_funcion_trunc(t) :
    'lista_funciones    : TRUNC PARIZQ funcion_math_parametro PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': t[3]['valor']}

    dot.node(str(id), 'TRUNC')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "					| TRUNC PARIZQ <funcion_math_parametro> PARDER"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["TRUNC","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones")  

def p_instrucciones_funcion_random(t) :
    'lista_funciones    : RANDOM PARIZQ PARDER'
    id = inc()
    t[0] = {'id': id, 'funcion': t[1], 'valor': 1}

    dot.node(str(id), 'RANDOM')
    gramatica = "					| RANDOM PARIZQ PARDER"
    no_terminal = []
    terminal = ["RANDOM","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"lista_funciones")


def p_instrucciones_funcion_math_parametro(t) :
    '''funcion_math_parametro   : ENTERO
                                | ID
                                | DECIMAL
                                '''
    id = inc()
    t[0] = {'id': id, 'valor': t[1]}

    dot.node(str(id), 'PARAMETRO' + str(t[0]))
    # dot.edge(str(id), t[3])
    gramatica = "<funcion_math_parametro>	::= ENTERO\n							| ID\n							| DECIMAL"
    no_terminal = ["<funcion_math_parametro>"]
    terminal = ["ENTERO","ID","DECIMAL"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"funcion_math_parametro")

def p_instrucciones_funcion_math_parametro_error(t) :
    'funcion_math_parametro : error'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[1], t.lexer.lineno)
    tabla_errores.agregar(error)
    
def p_instrucciones_funcion_math_parametro2(t) :
    '''funcion_math_parametro   : funcion_math_parametro_negativo'''
    id = inc()
    t[0] = {'id': id, 'valor' : t[1]['valor']}
    dot.node(str(id), 'FUNCION MATEMATICA')
    dot.edge(str(id), str(t[1]['id']))
    gramatica = "							| <funcion_math_parametro_negativo>"
    no_terminal = ["<funcion_math_parametro_negativo>"]
    terminal = []
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"funcion_math_parametro") 

def p_instrucciones_funcion_math_parametro_negativo(t) :
    '''funcion_math_parametro_negativo  : MENOS DECIMAL
                                        | MENOS ENTERO'''
    id = inc()
    val = -1*t[2]
    t[0] = {'id': id, 'valor': val}

    dot.node(str(id), 'NUMERO NEGATIVO\n' + str(t[2]))
    gramatica = "<funcion_math_parametro_negativo>	::= MENOS DECIMAL\n									| MENOS ENTERO"
    no_terminal = ["<funcion_math_parametro_negativo>"]
    terminal = ["MENOS","DECIMAL","ENTERO"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"funcion_math_parametro_negativo")

#========================================================

#========================================================
# FUNCIONES TRIGONOMÉTRICAS

#El unico valor que aceptan es double y devuelven un double
def p_instrucciones_funcion_trigonometrica_acos(t) :
    'fun_trigonometrica : ACOS PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ACOS')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}
    # print(">>>" + str(t[3]['valor']))
    dot.node(str(id), 'ACOS')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "<fun_trigonometrica>	::= ACOS PARIZQ <aritmetica> PARDER"
    no_terminal = ["<fun_trigonometrica>","<aritmetica>"]
    terminal = ["ACOS","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_asin(t) :
    'fun_trigonometrica : ASIN PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ASIN')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'ASIN')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| ASIN PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["ASIN","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_atan(t) :
    'fun_trigonometrica : ATAN PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ATAN')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'ATAN')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| ATAN PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["ATAN","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica")  

def p_instrucciones_funcion_trigonometrica_atan2(t) :
    'fun_trigonometrica : ATAN2 PARIZQ aritmetica COMA aritmetica PARDER'
    print('Ejecuta Funcion ATAN2')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor1': str(t[3]['valor']), 'valor2': str(t[3]['valor'])}

    dot.node(str(id), 'ATAN2')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]['id']))
    gramatica = "						| ATAN2 PARIZQ <aritmetica> COMA <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["ATAN2","PARIZQ","COMA","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_cos(t) :
    'fun_trigonometrica : COS PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion COS')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'COS')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| COS PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["COS","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_cot(t) :
    'fun_trigonometrica : COT PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion COT')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'COT')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| COT PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["COT","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_sin(t) :
    'fun_trigonometrica : SIN PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion SIN')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'SIN')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| SIN PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["SIN","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_tan(t) :
    'fun_trigonometrica : TAN PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion TAN')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'TAN')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| TAN PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["TAN","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_acosd(t) :
    'fun_trigonometrica : ACOSD PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ACOSD')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'ACOSD')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| ACOSD PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["ACOSD","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_asind(t) :
    'fun_trigonometrica : ASIND PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ASIND')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'ASIND')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| ASIND PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["ASIND","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_atand(t) :
    'fun_trigonometrica : ATAND PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ATAND')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'ATAND')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| ATAND PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["ATAND","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_atan2d(t) :
    'fun_trigonometrica : ATAN2D PARIZQ aritmetica COMA aritmetica PARDER'
    print('Ejecuta Funcion ATAN2D')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor1': str(t[3]['valor']), 'valor2': str(t[3]['valor'])}

    dot.node(str(id), 'ACATAN2DOS')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]['id']))
    gramatica = "						| ATAN2D PARIZQ <aritmetica> COMA <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["ATAND","PARIZQ","COMA","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_cosd(t) :
    'fun_trigonometrica : COSD PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion COSD')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'COSD')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| COSD PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["COSD","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_cotd(t) :
    'fun_trigonometrica : COTD PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion COTD')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'COTD')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| COTD PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["COTD","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_sind(t) : 
    'fun_trigonometrica : SIND PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion SIND')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'SIND')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| SIND PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["SIND","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_tand(t) :
    'fun_trigonometrica : TAND PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion TAND')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'TAND')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| TAND PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["TAND","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_sinh(t) :
    'fun_trigonometrica : SINH PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion SINH')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'SINH')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| SINH PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["SINH","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_cosh(t) :
    'fun_trigonometrica : COSH PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion COSH')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'COSH')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| COSH PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["COSH","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica")  

def p_instrucciones_funcion_trigonometrica_tanh(t) :
    'fun_trigonometrica : TANH PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion TANH')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'TANH')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| TANH PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["TANH","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_asinh(t) :
    'fun_trigonometrica : ASINH PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ASINH')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'ASINH')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| ASINH PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["ASINH","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_acosh(t) :
    'fun_trigonometrica : ACOSH PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ACOSH')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'ACOSH')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| ACOSH PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["ACOSH","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 

def p_instrucciones_funcion_trigonometrica_atanh(t) :
    'fun_trigonometrica : ATANH PARIZQ aritmetica PARDER'
    print('Ejecuta Funcion ATANH')
    id = inc()
    t[0] = {'id': id, 'funcion': str(t[1].upper()), 'valor': str(t[3]['valor'])}

    dot.node(str(id), 'ATANH')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| ATANH PARIZQ <aritmetica> PARDER"
    no_terminal = ["<aritmetica>"]
    terminal = ["ATANH","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_trigonometrica") 
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
    gramatica = "<fun_binario_select>	::= LENGTH PARIZQ <valor> PARDER"
    no_terminal = ["<fun_binario_select>","<valor>"]
    terminal = ["LENGTH","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_select") 

def p_instruccciones_funcion_binary_string_length_select_error(t) :
    'fun_binario_select : LENGTH PARIZQ error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_length_where(t) :
    'fun_binario_where    : LENGTH PARIZQ valor PARDER'
    print('Ejecuta Funcion length')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'LENGTH')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "<fun_binario_where>	::= LENGTH PARIZQ <valor> PARDER"
    no_terminal = ["<fun_binario_where>","<valor>"]
    terminal = ["LENGTH","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_where") 

def p_instrucciones_funcion_binary_string_length_where_error(t) :
    'fun_binario_where  : LENGTH PARIZQ error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_substring_select(t) :
    'fun_binario_select    : SUBSTRING PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta Funcion substring')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))
    gramatica = "						| SUBSTRING PARIZQ <valor> COMA ENTERO COMA ENTERO PARDER"
    no_terminal = ["<valor>"]
    terminal = ["SUBSTRING","PARIZQ","PARDER","COMA","ENTERO"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_select")

def p_instrucciones_funcion_binary_string_substring_select_error(t) :
    'fun_binario_select : SUBSTRING PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_substring_insert(t) :
    'fun_binario_insert    : SUBSTRING PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta Funcion substring')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))
    gramatica = "						| SUBSTRING PARIZQ <valor> COMA ENTERO COMA ENTERO PARDER"
    no_terminal = ["<valor>"]
    terminal = ["SUBSTRING","PARIZQ","PARDER","COMA","ENTERO"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_insert")

def p_instrucciones_funcion_binary_string_substring_insert_error(t) :
    'fun_binario_insert : SUBSTRING PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_substring_update(t) :
    'fun_binario_update    : SUBSTRING PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta Funcion substring')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))
    gramatica = "						| SUBSTRING PARIZQ <valor> COMA ENTERO COMA ENTERO PARDER"
    no_terminal = ["<valor>"]
    terminal = ["SUBSTRING","PARIZQ","PARDER","COMA","ENTERO"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_update")

def p_instrucciones_funcion_binary_string_substring_update_error(t) :
    'fun_binario_update : SUBSTRING PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_substring_where(t) :
    'fun_binario_where    : SUBSTRING PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta Funcion substring')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SUBSTRING')
    # dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))
    gramatica = "						| SUBSTRING PARIZQ <valor> COMA ENTERO COMA ENTERO PARDER"
    no_terminal = ["<valor>"]
    terminal = ["SUBSTRING","PARIZQ","PARDER","COMA","ENTERO"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_where")

def p_instrucciones_funcion_binary_string_substring_where_error(t) :
    'fun_binario_where  : SUBSTRING PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_trim_select(t) :
    'fun_binario_select    : TRIM PARIZQ CADENA FROM valor PARDER'
    print('Ejecuta Funcion trim')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'TRIM')
    dot.edge(str(id), t[3])
    dot.edge(str(id), str(t[5]['id']))
    gramatica = "						| TRIM PARIZQ CADENA FROM <valor> PARDER"
    no_terminal = ["<valor>"]
    terminal = ["TRIM","PARIZQ","PARDER","CADENA","FROM"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_select") 

def p_instrucciones_funcion_binary_string_trim_select_error(t) :
    'fun_binario_select : TRIM PARIZQ CADENA FROM error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[5], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_trim_insert(t) :
    'fun_binario_insert    : TRIM PARIZQ CADENA FROM valor PARDER'
    print('Ejecuta Funcion trim')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'TRIM')
    dot.edge(str(id), t[3])
    dot.edge(str(id), str(t[5]['id']))
    gramatica = "						| TRIM PARIZQ CADENA FROM <valor> PARDER"
    no_terminal = ["<valor>"]
    terminal = ["TRIM","PARIZQ","PARDER","CADENA","FROM"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_insert")  

def p_instrucciones_funcion_binary_string_trim_insert_error(t) :
    'fun_binario_insert : TRIM PARIZQ CADENA FROM error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[5], t.lexer.lineno)
    tabla_errores.agregar(error)
    
def p_instrucciones_funcion_binary_string_trim_update(t) :
    'fun_binario_update    : TRIM PARIZQ CADENA FROM valor PARDER'
    print('Ejecuta Funcion trim')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'TRIM')
    dot.edge(str(id), t[3])
    dot.edge(str(id), str(t[5]['id']))
    gramatica = "						| TRIM PARIZQ CADENA FROM <valor> PARDER"
    no_terminal = ["<valor>"]
    terminal = ["TRIM","PARIZQ","PARDER","CADENA","FROM"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_update")  

def p_instrucciones_funcion_binary_string_trim_update_error(t) :
    'fun_binario_update : TRIM PARIZQ CADENA FROM error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[5], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_trim_where(t) :
    'fun_binario_where    : TRIM PARIZQ CADENA FROM valor PARDER'
    print('Ejecuta Funcion trim')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'TRIM')
    dot.edge(str(id), t[3])
    dot.edge(str(id), str(t[5]['id']))
    gramatica = "						| TRIM PARIZQ CADENA FROM <valor> PARDER"
    no_terminal = ["<valor>"]
    terminal = ["TRIM","PARIZQ","PARDER","CADENA","FROM"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_where")  

def p_instrucciones_funcion_binary_string_trim_where_error(t) :
    'fun_binario_where  : TRIM PARIZQ CADENA FROM error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[5], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_md5_insert(t) :
    'fun_binario_insert : MD5 PARIZQ valor PARDER'
    print('Ejecuta Funcion md5')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'MD5')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| MD5 PARIZQ <valor> PARDER"
    no_terminal = ["<valor>"]
    terminal = ["MD5","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_insert") 

def p_instrucciones_funcion_binary_string_md5_insert_error(t) :
    'fun_binario_insert : MD5 PARIZQ error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_md5_update(t) :
    'fun_binario_update : MD5 PARIZQ valor PARDER'
    print('Ejecuta Funcion md5')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'MD5')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| MD5 PARIZQ <valor> PARDER"
    no_terminal = ["<valor>"]
    terminal = ["MD5","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_update")  

def p_instrucciones_funcion_binary_string_md5_update_error(t) :
    'fun_binario_update : MD5 PARIZQ error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_sha256_select(t) :
    'fun_binario_select : SHA256 PARIZQ valor PARDER'
    print('Ejecuta Funcion sha256')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SHA256')
    dot.edge(str(id), str(t[3]['id']))
    gramatica = "						| SHA256 PARIZQ <valor> PARDER"
    no_terminal = ["<valor>"]
    terminal = ["SHA256","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_select")  

def p_instrucciones_funcion_binary_string_sha256_select_error(t) :
    'fun_binario_select : SHA256 PARIZQ error PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_substr_select(t) :
    'fun_binario_select : SUBSTR PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta Funcion substr')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))
    gramatica = "						| SUBSTR PARIZQ <valor> COMA ENTERO COMA ENTERO PARDER"
    no_terminal = ["<valor>"]
    terminal = ["SUBSTR","PARIZQ","COMA","ENTERO","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_select")

def p_instrucciones_funcion_binary_string_substr_select_error(t) :
    'fun_binario_select : SUBSTR PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_substr_insert(t) :
    'fun_binario_insert : SUBSTR PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta Funcion substr')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))
    gramatica = "						| SUBSTR PARIZQ <valor> COMA ENTERO COMA ENTERO PARDER"
    no_terminal = ["<valor>"]
    terminal = ["SUBSTR","PARIZQ","COMA","ENTERO","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_insert")

def p_instrucciones_funcion_binary_string_substr_insert_error(t) :
    'fun_binario_insert : SUBSTR PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_substr_update(t) :
    'fun_binario_update : SUBSTR PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta Funcion substr')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))
    gramatica = "						| SUBSTR PARIZQ <valor> COMA ENTERO COMA ENTERO PARDER"
    no_terminal = ["<valor>"]
    terminal = ["SUBSTR","PARIZQ","COMA","ENTERO","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_update")

def p_instrucciones_funcion_binary_string_substr_update_error(t) :
    'fun_binario_update : SUBSTR PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_substr_where(t) :
    'fun_binario_where : SUBSTR PARIZQ valor COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta Funcion substr')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SUBSTRING')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    dot.edge(str(id), str(t[7]))
    gramatica = "						| SUBSTR PARIZQ <valor> COMA ENTERO COMA ENTERO PARDER"
    no_terminal = ["<valor>"]
    terminal = ["SUBSTR","PARIZQ","COMA","ENTERO","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_where")

def p_instrucciones_funcion_binary_string_substr_where_error(t) :
    'fun_binario_where  : SUBSTR PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_get_byte(t) :
    'fun_binario_select : GET_BYTE PARIZQ valor DOS_PUNTOS DOS_PUNTOS BYTEA COMA ENTERO PARDER'
    print('Ejecuta funcion getbyte')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'GET_BYTE')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[8]))
    gramatica = "						| GET_BYTE PARIZQ <valor> DOS_PUNTOS DOS_PUNTOS BYTEA COMA ENTERO PARDER"
    no_terminal = ["<valor>"]
    terminal = ["GET_BYTE","PARIZQ","DOS_PUNTOS","BYTEA","COMA","ENTERO","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_select")

def p_instrucciones_funcion_binary_string_get_byte_error(t) :
    'fun_binario_select : GET_BYTE PARIZQ error DOS_PUNTOS DOS_PUNTOS BYTEA COMA ENTERO PARDER'
    
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_get_byte2(t) :
    'fun_binario_select : GET_BYTE PARIZQ valor COMA ENTERO PARDER'
    print('Ejecuta funcion getbyte')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'GET_BYTE')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]))
    gramatica = "						| GET_BYTE PARIZQ <valor> COMA ENTERO PARDER"
    no_terminal = ["<valor>"]
    terminal = ["GET_BYTE","PARIZQ","COMA","ENTERO","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_select")

def p_instrucciones_funcion_binary_string_get_byte2_error(t) :
    'fun_binario_select : GET_BYTE PARIZQ error COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_set_byte(t) :
    'fun_binario_select : SET_BYTE PARIZQ valor DOS_PUNTOS DOS_PUNTOS BYTEA COMA ENTERO COMA ENTERO PARDER'
    print('Ejecuta funcion setbyte')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'SET_BYTE')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[8]))
    dot.edge(str(id), str(t[10]))
    gramatica = "						| SET_BYTE PARIZQ <valor> DOS_PUNTOS DOS_PUNTOS BYTEA COMA ENTERO COMA ENTERO PARDER"
    no_terminal = ["<valor>"]
    terminal = ["SET_BYTE","PARIZQ","DOS_PUNTOS","BYTEA","COMA","ENTERO","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_select")

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
    gramatica = "						| SET_BYTE PARIZQ <valor> COMA ENTERO COMA ENTERO PARDER"
    no_terminal = ["<valor>"]
    terminal = ["SET_BYTE","PARIZQ","COMA","ENTERO","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_select")

def p_instrucciones_funcion_binary_string_set_byte2_error(t) :
    'fun_binario_select : SET_BYTE PARIZQ error COMA ENTERO COMA ENTERO PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_Convert(t) :
    'fun_binario_select : CONVERT PARIZQ valor AS tipos PARDER'
    print('Ejecuta funcion convert')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'CONVERT')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), str(t[5]['id']))
    gramatica = "						| CONVERT PARIZQ <valor> AS <tipos> PARDER"
    no_terminal = ["<valor>","<tipos>"]
    terminal = ["CONVERT","AS","PARIZQ","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_select") 

def p_instrucciones_funcion_binary_string_convert_error(t) :
    'fun_binario_select : CONVERT PARIZQ error AS tipos PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_encode(t) :
    'fun_binario_select : ENCODE PARIZQ valor DOS_PUNTOS DOS_PUNTOS BYTEA COMA CADENA PARDER'
    print('Ejectua funcion encode')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ENCODE')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), t[8])
    gramatica = "						| ENCODE PARIZQ <valor> DOS_PUNTOS DOS_PUNTOS BYTEA COMA CADENA PARDER"
    no_terminal = ["<valor>"]
    terminal = ["ENCODE","PARIZQ","DOS_PUNTOS","BYTEA","COMA","CADENA","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_select")

def p_instrucciones_funcion_binary_string_encode_error(t) :
    'fun_binario_select : ENCODE PARIZQ error DOS_PUNTOS DOS_PUNTOS BYTEA COMA CADENA PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_encode2(t) :
    'fun_binario_select : ENCODE PARIZQ valor COMA CADENA PARDER'
    print('Ejecuta funcion encode')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'ENCODE')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), t[5])
    gramatica = "						| ENCODE PARIZQ <valor> COMA CADENA PARDER"
    no_terminal = ["<valor>"]
    terminal = ["ENCODE","PARIZQ","COMA","CADENA","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_select")

def p_instrucciones_funcion_binary_string_encode2_error(t) :
    'fun_binario_select : ENCODE PARIZQ error COMA CADENA PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

def p_instrucciones_funcion_binary_string_decode(t) :
    'fun_binario_select : DECODE PARIZQ valor COMA CADENA PARDER'
    print('Ejecuta funcion decode')
    id = inc()
    t[0] = {'id': id}

    dot.node(str(id), 'DECODE')
    dot.edge(str(id), str(t[3]['id'])) 
    dot.edge(str(id), t[5])
    gramatica = "						| DECODE PARIZQ <valor> COMA CADENA PARDER"
    no_terminal = ["<valor>"]
    terminal = ["DECODE","PARIZQ","COMA","CADENA","PARDER"]
    reg_gramatical = ""
    gramatical.agregarGramatical(gramatica,reg_gramatical,terminal,no_terminal,"fun_binario_select")

def p_instrucciones_funcion_binary_string_decode_error(t) :
    'fun_binario_select : DECODE PARIZQ error COMA CADENA PARDER'
    error = Error('Sintactico', "No se esperaba la entrada '%s'" %t[3], t.lexer.lineno)
    tabla_errores.agregar(error)

#========================================================

def p_error(t):
    if t == None:
        error = Error('Sintáctcio', "Problema con el final del texto a analizar", 404)
        tabla_errores.agregar(error)
        print(error.imprimir())
    else:
        error = Error('Sintáctico', "No se esperaba el caracter '%s'" %t.value, t.lexer.lineno)
        tabla_errores.agregar(error)
        print(error.imprimir())

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    retorno = parser.parse(input)
    # dot.view()
    return retorno
