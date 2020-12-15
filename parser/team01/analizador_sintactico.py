import ply.yacc as yacc
import tempfile
from analizador_lexico import tokens
from analizador_lexico import analizador
from Nodo import *



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


def p_statement(t):
    '''statement : insert_statement
                 | update_statement
                 | delete_statement
    '''
    t[0] = Nodo("statement", [t[1]], 'N', None)

# *************************************************
# **********************         insert_statement      ***********
# *************************************************
# region INSERT
def p_insert_statement(t):
    '''insert_statement : INSERT INTO table_name insert_columns_and_source PTCOMA
    '''
    temp = list()
    temp.append(t[3])
    temp.append(t[4])
    t[0] = Nodo("insert_statement", temp, 'N', None)


def p_table_name(t):
    'table_name : ID '
    t[0] = Nodo("table_name", [t[1]], 'S', str(t[1]))


# *************************************************
# **********************         insert_columns_and_source      ***********
# *************************************************

def p_insert_columns_and_source(t):
    '''insert_columns_and_source : PARIZQ insert_column_list PARDER VALUES query_expression_insert
                                    | VALUES query_expression_insert
                                    | insert_default_values
    '''
    if (len(t) == 6):
        # t[0] =InsertColumnsValues(t[2],t[5])
        temp = list()
        temp.append(t[2])
        temp.append(t[5])
        t[0] = Nodo("insert_columns_and_source", temp, 'N', None)
    elif (len(t) == 3):
        # t[0] =InsertValues(t[1],t[2])
        t[0] = Nodo("insert_columns_and_source", [t[2]], 'N', None)

    elif (len(t) == 2):
        # t[0] =InsertValues(t[1],t[2])
        t[0] = Nodo("insert_columns_and_source", [t[1]], 'N', None)


def p_insert_defaul_values(t):
    'insert_default_values    : DEFAULT VALUES'
    t[0] = Nodo("column_name", [t[1]], 'S', str(t[1]))

# *************************************************
# **********************         insert_column_list      ***********
# *************************************************


def p_insert_column_list(t):
    'insert_column_list    : insert_column_list  COMA column_name'
    temp = list()
    temp.append(t[1])
    temp.append(t[3])
    t[0] = Nodo("insert_column_list1", temp, 'N', None)


def p_insert_column_name(t):
    'insert_column_list    : column_name'
    # t[0] = [t[1]]
    t[0] = Nodo("insert_column_list2", [t[1]], 'N', None)


def p_column_name(t):
    'column_name    : ID '
    t[0] = Nodo("column_name", [t[1]], 'S', str(t[1]))


# *************************************************
# **********************         query_expression_insert      ***********
# *************************************************

def p_query_expression_insert(t):
    '''query_expression_insert :    insert_list
                        '''
    t[0] = Nodo("query_expression_insert", [t[1]], 'N', None)


def p_insert_list(t):
    '''insert_list    :  insert_list COMA insert_value_list  '''
    temp = list()
    temp.append(t[1])
    temp.append(t[3])
    t[0] = Nodo("insert_list2", temp, 'N', None)


def p_insert_item(t):
    '''insert_list    :  insert_value_list  '''
    t[0] = Nodo("insert_list1", [t[1]], 'N', None)


def p_insert_value_list(t):
    '''insert_value_list    : PARIZQ value_list PARDER '''
    t[0] = Nodo("insert_value_list", [t[2]], 'N', None)


def p_value_list(t):
    '''value_list    : value_list  COMA insert_value'''
    temp = list()
    temp.append(t[1])
    temp.append(t[3])
    t[0] = Nodo("value_list1", temp, 'N', None)


def p_insert_value(t):
    '''value_list    : insert_value'''
    t[0] = Nodo("value_list1", [t[1]], 'N', None)


def p_valorasign(t):
    '''insert_value : ENTERO
                    | DECIMAL
                    | CADENACOMSIMPLE
                    | DEFAULT
    '''
    t[0] = Nodo("insert_value", [t[1]], 'S', str(t[1]))

# endregion

# *************************************************
# **********************         update_statement      ***********
# *************************************************
# region UPDATE


def p_update_statement(t):
    '''update_statement : UPDATE table_name SET set_clause_list WHERE search_condition PTCOMA
                        | UPDATE table_name SET set_clause_list PTCOMA
    '''
    if (len(t) == 8):
        temp = list()
        temp.append(t[2])
        temp.append(t[4])
        temp.append(t[6])
        t[0] = Nodo("update_statement", temp, 'N', None)
    elif (len(t) == 6):
        temp = list()
        temp.append(t[2])
        temp.append(t[4])
        t[0] = Nodo("update_statement", temp, 'N', None)


def p_set_clause_list(t):
    '''set_clause_list    : set_clause_list  COMA set_clause'''
    temp = list()
    temp.append(t[1])
    temp.append(t[3])
    t[0] = Nodo("set_clause_list", temp, 'N', None)


def p_p_set_clause_item(t):
    '''set_clause_list    : set_clause'''
    t[0] = Nodo("set_clause_list", [t[1]], 'N', None)


def p_set_clause(t):
    'set_clause : column_name  IGUAL update_source'
    temp = list()
    temp.append(t[1])
    temp.append(t[3])
    t[0] = Nodo("set_clause", temp, 'N', None)


def p_update_source(t):
    '''update_source : value_expression
                | NULL
    '''
    t[0] = Nodo("update_source", [t[1]], 'N', None)


# *************************************************
# **********************         delete_statement      ***********
# *************************************************

def p_delete_statement(t):
    '''delete_statement : DELETE FROM table_name_d PTCOMA
                        | DELETE FROM table_name_d WHERE search_condition PTCOMA
    '''
    if (len(t) == 5):
        # t[0] =InsertColumnsValues(t[2],t[5])
        
        t[0] = Nodo("delete_statement", [t[3]], 'N', None)
    elif (len(t) == 7):
        # t[0] =InsertColumnsValues(t[2],t[5])
        temp = list()
        temp.append(t[3])
        temp.append(t[5])
        
        t[0] = Nodo("delete_statement", temp, 'N', None)
    


def p_table_name_d(t):
    'table_name_d : ID '
    t[0] = Nodo("table_name_d", [t[1]], 'S', str(t[1]))

# *************************************************
# **********************         search_condition      ***********
# *************************************************  

def p_search_condition_boolean(t) :
    '''search_condition : boolean_term 
    '''
    t[0] = Nodo("search_condition", [t[1]],'N',None)

def p_search_condition(t) :
    '''search_condition : search_condition OR boolean_term 
    '''
    temp = list()
    temp.append(t[1])
    temp.append(t[3])
    t[0] = Nodo("search_condition", temp,'N',None)

def p_p_boolean_term_item(t) :
    '''boolean_term : boolean_factor 
    '''
    t[0] = Nodo("boolean_term", [t[1]],'N',None)



def p_boolean_term(t) :
    '''boolean_term : boolean_term AND boolean_factor 
    '''
    temp = list()
    temp.append(t[1])
    temp.append(t[3])
    t[0] = Nodo("boolean_term", temp,'N',None)

    
def p_boolean_factor(t) :
    '''boolean_factor : NOT boolean_test 
                        | boolean_test
    '''
    if (len(t) == 3):
        temp = list()
        temp.append(t[1])
        temp.append(t[2])
        t[0] = Nodo("boolean_factor", temp,'N',None)        
    elif (len(t)==2):
        temp = list()
        temp.append(t[1])
        t[0] = Nodo("boolean_factor", temp,'N',None)


def p_boolean_test(t) :
    '''boolean_test : boolean_primary
    '''
    t[0] = Nodo("boolean_test", [t[1]],'N',None)    

def p_boolean_primary(t) :
    '''boolean_primary : predicate
                        |  PARIZQ search_condition PARDER
    '''
    if (len(t) == 2):
        t[0] = Nodo("boolean_primary", [t[1]],'N',None)         
    elif (len(t)==4):
        t[0] = Nodo("boolean_primary", [t[2]],'N',None) 

def p_predicate(t) :
    '''predicate : comparison_predicate
    '''

    t[0] = Nodo("predicate", [t[1]],'N',None)  


def p_comparison_predicate(t) :
    '''comparison_predicate : row_value_constructor comp_op row_value_constructor
    '''
    temp = list()
    temp.append(t[1])
    temp.append(t[2])
    temp.append(t[3])
    t[0] = Nodo("comparison_predicate", temp,'N',None) 

def p_comp_op(t) :
    '''comp_op : IGUAL
                | MENQUE MAYQUE
                | MENQUE 
                | MAYQUE
                | MENORIGU
                | MAYORIGU
    '''
    if (len(t) == 2):
        t[0] = Nodo("comp_op", [t[1]],'S',str(t[1]))         
    elif (len(t)==3):
        temp = list()
        temp.append(t[1])
        temp.append(t[2])
        t[0] = Nodo("comp_op", temp,'N',None)

def p_row_value_constructor(t) :
    '''row_value_constructor : row_value_constructor_element
                                    | PARIZQ row_value_constructor_list PARDER
    '''
    if (len(t) == 2):
        t[0] = Nodo("row_value_constructor", [t[1]],'N',None)       
    elif (len(t)==4):
        t[0] = Nodo("row_value_constructor", [t[2]],'N',None) 

def p_row_value_constructor_list(t) :
    '''row_value_constructor_list : row_value_constructor_list COMA row_value_constructor_element
    '''
    temp = list()
    temp.append(t[1])
    temp.append(t[3])
    t[0] = Nodo("row_value_constructor_list", temp,'N',None)      

def p_row_value_constructor_item(t) :
    '''row_value_constructor_list : row_value_constructor_element
    '''
    t[0] = Nodo("row_value_constructor_list", [t[1]],'N',None)

def p_row_value_constructor_element(t) :
    '''row_value_constructor_element : value_expression
                                    | NULL
    '''
    t[0] = Nodo("row_value_constructor_element", [t[1]],'N',None) 

def p_value_expression(t):
    '''value_expression : ENTERO
                        | DECIMAL
                        | CADENACOMSIMPLE
                        | DEFAULT
                        | ID
    '''
    t[0] = Nodo("value_expression", [t[1]],'S',str(t[1])) 

# endregion

# *************************************************
# **********************         Error           ***********
# *************************************************  

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {} ".format( str(t.type),str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)
 

# *************************************************
# **********************               ***********
# *************************************************   

# Build the parser
parser = yacc.yacc()

def ejecucion_sintactico(data):
    global resultado_gramatica
    resultado_gramatica.clear()
    gram = parser.parse(data)
    if gram:
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d_%m_%Y %H_%M_%S")
        print(dot.source)
        dot.attr(splines='false')
        dot.node_attr.update(shape='circle',fontname='arial',color='blue4',fontcolor='blue4')
        dot.edge_attr.update(color='blue4')
        dot.render('.\\tempPDF\\'+dt_string+'.gv', view=False)  # doctest: +SKIP
        '.\\tempPDF\\'+dt_string+'.gv.pdf'


        resultado_gramatica.append(gram)
    else: print("vacio")

    return(resultado_gramatica)
