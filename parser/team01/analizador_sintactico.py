import ply.yacc as yacc
import tempfile
from analizador_lexico import tokens
from analizador_lexico import analizador

from expresiones import *
from instrucciones import *
from graphviz import *



# Asociación de operadores y precedencia
# precedence = (
#     ('left','MAS'),
#     ('left','DIVIDIDO'),
#     ('right'),
#     )

nombres = {}
resultado_gramatica = []

dot = Digraph(comment='The Round Table')

i = 0

def inc():
    global i
    i += 1
    return i

#*************************************************
#**********************         init      ***********
#*************************************************   

def p_init(t) :
    '''init : insert_statement
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str('init'))
    dot.edge(str(id),str(t[1]))    
    # t[0] = t[1]
    

#*************************************************
#**********************         insert_statement      ***********
#*************************************************   

def p_insert_statement(t) :
    '''insert_statement : INSERT INTO table_name insert_columns_and_source
                        | INSERT INTO database_name PUNTO table_name insert_columns_and_source
                        | INSERT INTO PUNTO
    '''
    if (len(t) == 4):
        id = inc()
        t[0] = id
        dot.node(str(id),str('insert_statement'))
        dot.edge(str(id),str(t[1]))
        dot.edge(str(id),str(t[2]))
        dot.edge(str(id),str(t[3]))
        dot.edge(str(id),str(t[4]))
    else:
        t[0] = t[1]


def p_table_name(t) :
    'table_name : ID '
    id = inc()
    t[0] = id
    dot.node(str(id),str('table_name'))
    dot.edge(str(id),str(t[1]))


def p_database_name(t) :
    'database_name : ID '
    id = inc()
    t[0] = id
    dot.node(str(id),str('database_name'))
    dot.edge(str(id),str(t[1]))

#*************************************************
#**********************         insert_columns_and_source      ***********
#*************************************************    

def p_insert_columns_and_source(t) :
    '''insert_columns_and_source : PARIZQ insert_column_list PARDER VALUES query_expression_insert
     | VALUES query_expression_insert
     | DEFAULT VALUES
    '''
    if (len(t) == 5):
        id = inc()
        t[0] = id
        dot.node(str(id),str('insert_columns_and_source'))
        dot.edge(str(id),str(t[1]))
        dot.edge(str(id),str(t[2]))
        dot.edge(str(id),str(t[3]))
        dot.edge(str(id),str(t[4]))
        dot.edge(str(id),str(t[5]))
    elif (len(t)==2):
        id = inc()
        t[0] = id
        dot.node(str(id),str('insert_columns_and_source'))
        dot.edge(str(id),str(t[1]))
        dot.edge(str(id),str(t[2]))


#*************************************************
#**********************         insert_column_list      ***********
#*************************************************   

def p_insert_column_list(t) :
    'insert_column_list    : insert_column_list  COMA column_name'
    id = inc()
    t[0] = id
    dot.node(str(id),str('insert_column_list'))
    dot.edge(str(id),str(t[1]))
    #dot.edge(str(id),str(t[2]))
    dot.edge(str(id),str(t[3]))

def p_insert_column_name(t) :
    'insert_column_list    : column_name'
    id = inc()
    t[0] = id
    dot.node(str(id),str('insert_column_list'))
    dot.edge(str(id),str(t[1]))
    #t[0] = t[1]


def p_column_name(t) :
    'column_name    : ID '
    id = inc()
    t[0] = id
    dot.node(str(id),str('column_name'))
    dot.edge(str(id),str(t[1]))


#*************************************************
#**********************         query_expression_insert      ***********
#*************************************************

def p_query_expression_insert(t):
    '''query_expression_insert :    insert_list   PTCOMA
                        '''
    id = inc()
    t[0] = id
    dot.node(str(id),str('query_expression_insert'))
    dot.edge(str(id),str(t[1]))
    dot.edge(str(id),str(t[2]))

def p_insert_list(t) :
    '''insert_list    :  insert_list COMA insert_value_list  '''
    id = inc()
    t[0] = id
    dot.node(str(id),str('insert_list'))
    dot.edge(str(id),str(t[1]))
    #dot.edge(str(id),str(t[2]))
    dot.edge(str(id),str(t[3]))

def p_insert_item(t) :
    '''insert_list    :  insert_value_list  '''
    id = inc()
    t[0] = id
    dot.node(str(id),str('insert_list'))
    dot.edge(str(id),str(t[1]))

def p_insert_value_list(t) :
    '''insert_value_list    : PARIZQ value_list PARDER '''
    id = inc()
    t[0] = id
    dot.node(str(id),str('insert_value_list'))
    dot.edge(str(id),str(t[1]))
    dot.edge(str(id),str(t[2]))
    dot.edge(str(id),str(t[3]))


def p_value_list(t) :
    '''value_list    : value_list  COMA insert_value'''
    id = inc()
    t[0] = id
    dot.node(str(id),str('value_list'))
    dot.edge(str(id),str(t[1]))
    dot.edge(str(id),str(t[3]))


def p_insert_value(t) :
    '''value_list    : insert_value'''
    id = inc()
    t[0] = id
    dot.node(str(id),str('value_list'))
    dot.edge(str(id),str(t[1]))



def p_valorasign(t):
    '''insert_value : ENTERO
                    | DECIMAL
                    | CADENACOMSIMPLE
                    | DEFAULT
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str('insert_value'))
    dot.edge(str(id),str(t[1]))


#*************************************************
#**********************         update_statement      ***********
#*************************************************   

def p_update_statement(t) :
    '''update_statement : UPDATE table_name SET set_clause_list
                        | UPDATE table_name SET set_clause_list WHERE search_condition
    '''
    t[0] = t[3]


def p_set_clause_list(t) :
    '''set_clause_list    : set_clause_list  COMA set_clause'''
    t[0] = t[1]


def p_p_set_clause_item(t) :
    '''set_clause_list    : set_clause'''
    t[0] = t[1]


def p_set_clause(t) :
    'set_clause : column_name  IGUAL update_source'
    t[0] = t[1]

def p_update_source(t) :
    '''update_source : value_expression  
                | NULL 
    '''
    t[0] = t[1]


#*************************************************
#**********************         search_condition      ***********
#*************************************************  


def p_search_condition(t) :
    '''search_condition : search_condition OR boolean_term 
    '''
    t[0] = t[1]

def p_search_condition_boolean(t) :
    '''search_condition : boolean_term 
    '''
    t[0] = t[1]

def p_boolean_term(t) :
    '''boolean_term : boolean_term AND boolean_factor 
    '''
    t[0] = t[1]

def p_p_boolean_term_item(t) :
    '''boolean_term : boolean_factor 
    '''
    t[0] = t[1]    

    
def p_boolean_factor(t) :
    '''boolean_factor : NOT boolean_test 
                        | boolean_test
    '''
    t[0] = t[1]    

def p_boolean_test(t) :
    '''boolean_test : boolean_primary
    '''
    t[0] = t[1]        

def p_boolean_primary(t) :
    '''boolean_primary : predicate
                        |  PARIZQ search_condition PARDER
    '''
    t[0] = t[1]   

def p_predicate(t) :
    '''predicate : comparison_predicate
    '''
    t[0] = t[1]

def p_comparison_predicate(t) :
    '''comparison_predicate : row_value_constructor comp_op row_value_constructor
    '''
    t[0] = t[1]


def p_comp_op(t) :
    '''comp_op : IGUAL
                | MENQUE MAYQUE
                | MENQUE 
                | MAYQUE
                | MENORIGU
                | MAYORIGU
    '''
    t[0] = t[1]

def p_row_value_constructor(t) :
    '''row_value_constructor : row_value_constructor_element
                                    | PARIZQ row_value_constructor_list PARDER
    '''
    t[0] = t[1]

def p_row_value_constructor_list(t) :
    '''row_value_constructor_list : row_value_constructor_list COMA row_value_constructor_element

    '''
    t[0] = t[1]

def p_row_value_constructor_item(t) :
    '''row_value_constructor_list : row_value_constructor_element
    '''
    t[0] = t[1]

def p_row_value_constructor_element(t) :
    '''row_value_constructor_element : value_expression
                                    | NULL
    '''
    t[0] = t[1]

def p_value_expression(t):
    '''value_expression : ENTERO
                        | DECIMAL
                        | CADENACOMSIMPLE
                        | DEFAULT
    '''
    t[0] = t[1]    

#*************************************************
#**********************                ***********
#*************************************************  


def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {} ".format( str(t.type),str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)
 

#*************************************************
#**********************               ***********
#*************************************************   

# Build the parser
parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()
    gram = parser.parse(data)
    if gram:
        dot.render('C:\\tmpgramaticagrupo1.gv', view=False)  # doctest: +SKIP
        'C:\\tmpgramaticagrupo1.gv.pdf'


        resultado_gramatica.append(str(gram))
    else: print("vacio")

    return(resultado_gramatica)
