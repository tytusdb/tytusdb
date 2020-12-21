import ply.yacc as yacc
import tempfile
from analizador_lexico import tokens
from analizador_lexico import analizador
from Nodo import *
from datetime import datetime
# import storageManager
from storageManager import jsonMode as manager
from expresiones import *
from instrucciones import *
from graphviz import *


# precedence = (
#     ('left', 'OPSUM', 'OPMENOS'),
#     ('left', 'MULT', 'OPDIV'),
# )


nombres = {}
resultado_gramatica = []

dot = Digraph(comment='The Round Table')

i = 0


def inc():
    global i
    i += 1
    return i

# *************************************************
# **********************         init  Modificado 11  de diciembre  Henry , acepta varias sentencias ***********
# *************************************************


def p_init(t):
    '''init : statement_list
    '''
    t[0] = Nodo("init", [t[1]], 'N', None)


def p_statement_list(t):
    '''statement_list : statement_list statement
    '''
    temp = list()
    temp.append(t[1])
    temp.append(t[2])
    t[0] = Nodo("statement_list", temp, 'N', None)


def p_statement_list_statement(t):
    'statement_list : statement'
    t[0] = Nodo("statement_list", [t[1]], 'N', None)


def p_statement(t):
    '''statement : insert_statement
                 | definitiondb_statement
                 | update_statement
                 | delete_statement
                 | select_statement
    '''
    t[0] = Nodo("statement", [t[1]], 'N', None)

    # *************************************************
    # **********************         createdb_statement Modificado 11  de diciembre  Henry      ***********
    # *************************************************


def p_definitiondb_statement(t):
    '''definitiondb_statement : create_db
                              | alter_db
                              | show_db
                              | drop_db
    '''
    t[0] = Nodo("definitiondb_statement", [t[1]], 'N', None)


def p_create2_db(t):
    'create_db : CREATE DATABASE ID PTCOMA'
    t[0] = Nodo("create_db", [t[3]], 'S', str(t[3]))


def p_show_db(t):
    'show_db : SHOW DATABASES PTCOMA'
    t[0] = Nodo("show_db", [t[2]], 'S', str(t[2]))


def p_alter0_db(t):
    'alter_db : ALTER DATABASE ID OWNER TO ID PTCOMA'
    temp = list()
    temp.append(t[3])
    temp.append(t[4])
    temp.append(t[6])
    t[0] = Nodo("alter_db", temp, 'S', None)


def p_alter1_db(t):
    'alter_db : ALTER DATABASE ID RENAME TO ID PTCOMA'
    temp = list()
    temp.append(t[3])
    temp.append(t[4])
    temp.append(t[6])
    t[0] = Nodo("alter_db", temp, 'S', None)


def p_drop0_db(t):
    'drop_db : DROP DATABASE IF EXISTS ID PTCOMA'
    t[0] = Nodo("drop_db", [t[5]], 'S', str(t[5]))


def p_drop1_db(t):
    'drop_db : DROP DATABASE ID PTCOMA'
    t[0] = Nodo("drop_db", [t[3]], 'S', str(t[3]))


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


def p_insert_value(t) :
    '''value_list    : insert_value
    '''
    t[0] = Nodo("value_list1", [t[1]],'N',None)        

def p_valorasign(t):
    '''insert_value : ENTERO
                    | DECIMALV
                    | CADENACOMSIMPLE
                    | DEFAULT
                    | NOW PARIZQ PARDER
                    | MD5 PARIZQ CADENACOMSIMPLE PARDER                    
    '''
    #t[0] = Nodo("insert_value", [t[1]],'S',str(t[1]))
    if (len(t) < 5):
        t[0] = Nodo("insert_value", [t[1]],'S',str(t[1]))
    elif (len(t)==5):
        temp = list()
        tempNode1 = Nodo("value_list", [t[1]],'S',str(t[1]))
        temp.append(tempNode1)
        tempNode3 = Nodo("value_list", [t[3]],'S',str(t[3]))
        temp.append(tempNode3)
        t[0] = Nodo("value_list", temp,'N',None)       

#endregion

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

def p_update_source(t) :
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
# **********************         select_statement      ***********
# *************************************************

def p_select_statement(t):
    '''select_statement : select_col_statement PTCOMA
                        | select_col_statement select_where_statement PTCOMA
                        | select_col_statement  groupby_statement PTCOMA
                        | select_col_statement  select_where_statement groupby_statement PTCOMA
    '''
    if (len(t) == 3):
        # t[0] =InsertColumnsValues(t[2],t[5])
        t[0] = Nodo("select_statement", [t[1]], 'N', None)
    elif (len(t) == 4):
        # t[0] =InsertColumnsValues(t[2],t[5])
        temp = list()
        temp.append(t[1])
        temp.append(t[2])
        t[0] = Nodo("select_statement", temp, 'N', None)
    elif (len(t) == 5):
        # t[0] =InsertColumnsValues(t[2],t[5])
        temp = list()
        temp.append(t[1])
        temp.append(t[2])
        temp.append(t[3])       
        t[0] = Nodo("select_statement", temp, 'N', None)   

def p_select_col_statement(t):
    '''select_col_statement : SELECT select_column_list FROM table_name_s                     
    '''
    if (len(t) == 5):
        # t[0] =InsertColumnsValues(t[2],t[5])
        temp = list()
        temp.append(t[2])
        temp.append(t[4])       
        t[0] = Nodo("select_col_statement", temp, 'N', None)
    

def p_table_name_list(t):
    'table_name_list    : table_name_list COMA table_name_l'
    temp = list()
    temp.append(t[1])
    temp.append(t[3])
    t[0] = Nodo("table_name_list", temp, 'N', None)


def p_table_name_list_name(t):
    'table_name_list : table_name_l'     
    t[0] = Nodo("table_name_list1", [t[1]], 'N', None)


    
def p_table_name_l(t):
    '''table_name_l     : table_name_s
                        | table_name_s table_name_as
    '''
    temp = list()
    temp.append(t[1])
    temp.append(t[2])
    t[0] = Nodo("select_table_name_l", temp, 'N', None)


# def p_table_name_l_name(t):
#     'table_name_l : table_name_s'     
#     t[0] = Nodo("select_table_name", [t[1]], 'N', None)

def p_table_name_s(t):
    '''table_name_s : ID                 
    '''
    t[0] = Nodo("table_name_s", [t[1]], 'S', str(t[1]))
    

def p_table_name_as(t):
    '''table_name_as : ID                 
    '''
    t[0] = Nodo("table_name_as", [t[1]], 'S', str(t[1]))


def p_table_name_s_alias(t):
    '''table_name_s_alias : ID 
    '''
    if (len(t) == 2):
        t[0] = Nodo("table_name_alias_name", [t[1]], 'S', str(t[1]))


def p_select_where_list(t):
    'select_where_statement    :  WHERE search_condition  '
    t[0] = Nodo("select_where_statement", [t[2]], 'N', None)

# *************************************************
# **********************         select_column_list      ***********
# *************************************************

def p_select_column_list(t):
    'select_column_list    : select_column_list COMA column_select_statement'
    temp = list()
    temp.append(t[1])
    temp.append(t[3])
    t[0] = Nodo("select_column_list1", temp, 'N', None)


def p_select_column_name(t):
    'select_column_list : column_select_statement'     
    t[0] = Nodo("select_column_list2", [t[1]], 'N', None)



def p_column_select_st(t):
    '''column_select_statement  : column_name_select
                                | column_name_select AS value_expression 
                                | DISTINCT column_name_select 
                                | DISTINCT column_name_select AS value_expression 
    '''
    if (len(t) == 4):
        # t[0] =InsertColumnsValues(t[2],t[5])
        temp = list()
        temp.append(t[1])
        temp.append(t[3])
        t[0] = Nodo("column_select_as_statement", temp, 'N', None)
    elif (len(t) == 2):
        # t[0] =InsertColumnsValues(t[2],t[5])        
        t[0] = Nodo("column_select_statement", [t[1]], 'N', None)
    elif (len(t) == 3):
        # t[0] =InsertColumnsValues(t[2],t[5])        
        t[0] = Nodo("column_select_statement", [t[2]], 'N', None)
    elif (len(t) == 5):
        # t[0] =InsertColumnsValues(t[2],t[5])        
        temp = list()
        temp.append(t[2])
        temp.append(t[4])
        t[0] = Nodo("column_select_as__statement", temp, 'N', None)




def p_column_select(t):
    '''column_name_select   : select_function 
                            | select_function PARIZQ select_function_element PARDER
                            | select_function value_expression
                            | select_function PARIZQ PARDER
                            | select_function PARIZQ column_funtionext_select PARDER
    '''
    # value_expression
    if (len(t) == 5):
        # t[0] =InsertColumnsValues(t[2],t[5])
        temp = list()
        temp.append(t[1])
        temp.append(t[3])
        t[0] = Nodo("column_func_name_select", temp, 'N', None)
    elif (len(t) == 2):
        # t[0] =InsertColumnsValues(t[2],t[5])        
        t[0] = Nodo("column_name_select", [t[1]], 'N', None)
    elif (len(t) == 4):
        # t[0] =InsertColumnsValues(t[2],t[5])        
        t[0] = Nodo("column_func_name_select", [t[1]], 'N', None)
    elif (len(t) == 3):
        # t[0] =InsertColumnsValues(t[2],t[5])
        temp = list()
        temp.append(t[1])
        temp.append(t[2])
        t[0] = Nodo("column_func_name_select", temp, 'N', None)


def p_select_function(t) :
    '''select_function  : SUM  
                        | COUNT 
                        | NOW
                        | CURRENT_DATE 
                        | CURRENT_TIME 
                        | TIMESTAMP                          
                        | EXTRACT                          
                        | DATE_PART 
                        | MULT 
                        | ID 
                                             
    '''
    t[0] = Nodo("column_name", [t[1]],'S', str(t[1]) )


def p_select_function_element(t) :
    '''select_function_element  : ID
                                | NULL
                                
    '''
    if (len(t) == 2):
        t[0] = Nodo("select_function_element", [t[1]], 'S', str(t[1]))
    else :
        t[0] = Nodo("select_function_element", [t[1]], 'S', 'vacio')


def p_column_functionext_select(t):
    '''column_funtionext_select : column_datefuntion_select 
                                | column_datepartfuntion_select 
    '''
    t[0] = Nodo("column_funtionext_select", [t[1]], 'N', None)

def p_column_datefunction_select(t) :
    '''column_datefuntion_select    : column_dateExtractfunc_select FROM TIMESTAMP  value_expression                  
    '''
    temp = list()
    temp.append(t[1])
    temp.append(t[4])
    t[0] = Nodo("column_datefuntion_select", temp, 'N', None)
    


def p_column_dateExtractfunc_select(t) :
    '''column_dateExtractfunc_select    : HOUR  
                                        | MINUTE 
                                        | SECOND
                                        | YEAR 
                                        | MONTH 
                                        | DAY                          
    '''
    t[0] = Nodo("column_dateExtractfunc_select", [t[1]],'S', str(t[1]) )
   


def p_column_datepartfunction_select(t) :
    '''column_datepartfuntion_select    : column_datepartfunc_select COMA INTERVAL column_datepartfuncDATE_select              
    '''
    temp = list()
    temp.append(t[1])
    temp.append(t[4])
    t[0] = Nodo("column_datefuntion_select", temp, 'N', None)
    


def p_column_datepartfunc_select(t) :
    '''column_datepartfunc_select   : HOURS  
                                    | MINUTES 
                                    | SECONDS                       
    '''
    t[0] = Nodo("column_dateExtractfunc_select", [t[1]],'S', str(t[1]) )
   

def p_column_datepartfuncDATE_select(t) :
    '''column_datepartfuncDATE_select   : ENTERO HOURS    
                                        | ENTERO HOURS ENTERO MINUTES  
                                        | ENTERO HOURS ENTERO MINUTES ENTERO SECONDS                        
    '''
    t[0] = Nodo("column_dateExtractfunc_select", [t[1]],'S', str(t[1]) )




# def p_value_expression_datetime(t):
#     '''value_expression_datetime : ENTERO
#                         | ID
#     '''
#     t[0] = t[1]    



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
    #  | <between predicate>
    #  | <in predicate>
    #  | <like predicate>
    #  | <null predicate>
    #  | <quantified comparison predicate>
    #  | <exists predicate>
    #  | <match predicate>
    #  | <overlaps predicate>
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


def p_trim_operands(t) :
    '''trim_operands : trim_specification trim_character FROM trim_source
                            | trim_specification FROM trim_source
                            |  trim_character FROM trim_source
                            |   FROM trim_source
                            |  trim_source
    '''
    if (len(t) == 5):
        temp = list()
        temp.append(t[1])
        temp.append(t[2])
        tempNode3 = Nodo("trim_operands", [t[3]],'S',str(t[3]))
        temp.append(tempNode3)
        temp.append(t[4])
        t[0] = Nodo("trim_operands", temp,'N',None)      
    elif (len(t) == 4):
        temp = list()
        temp.append(t[1])
        tempNode2 = Nodo("trim_operands", [t[2]],'S',str(t[2]))
        temp.append(tempNode2)
        temp.append(t[3])
        t[0] = Nodo("trim_operands", temp,'N',None)  
    elif (len(t) == 3):
        temp = list()
        tempNode1 = Nodo("trim_operands", [t[1]],'S',str(t[1]))
        temp.append(tempNode1)
        temp.append(t[2])
        t[0] = Nodo("trim_operands", temp,'N',None)  
    elif (len(t)==2):
        t[0] = Nodo("trim_operands", [t[1]],'N',None)

def p_trim_specification(t) :
    '''trim_specification : LEADING
            | TRAILING
            | BOTH
    '''
    t[0] = Nodo("trim_specification", [t[1]],'S',str(t[1]))  


def p_trim_character(t) :
    '''trim_character : character_value_expression 
    '''
    t[0] = Nodo("trim_character", [t[1]],'N',None)  

def p_trim_source(t) :
    '''trim_source : character_value_expression 
    '''
    t[0] = Nodo("trim_source", [t[1]],'N',None)  


def p_character_value_expression(t) :
    '''character_value_expression : concatenation 
                        | character_factor
    '''
    t[0] = Nodo("character_value_expression", [t[1]],'N',None) 


def p_concatenation(t) :
    '''concatenation : character_value_expression ORCOMP character_factor
    '''
    temp = list()
    temp.append(t[1])
    tempNode2 = Nodo("concatenation", [t[2]],'S',str(t[2]))
    temp.append(tempNode2)
    temp.append(t[3])
    t[0] = Nodo("concatenation", temp,'N',None)  


def p_character_factor(t) :
    '''character_factor : character_primary
    '''
    t[0] = Nodo("character_factor", [t[1]],'N',None)


def p_character_primary(t):
    '''character_primary : value_expression_primary 
                                | string_value_function 
    '''
    t[0] = Nodo("character_primary", [t[1]], 'N', None)

def p_string_value_function(t):
    '''string_value_function : trim_function 
    '''
    t[0] = Nodo("string_value_function", [t[1]], 'N', None)


def p_value_expression_primary(t):
    '''value_expression_primary : unsigned_value_specification 
                                | column_reference 
                                | function_specification
                                |  PARIZQ value_expression PARDER
    '''
    if (len(t)==2):
        t[0] = Nodo("value_expression_primary", [t[1]],'N',None)

    elif (len(t) == 4):
        t[0] = Nodo("value_expression_primary", [t[2]],'N',None)



def p_unsigned_value_specification(t):
    '''unsigned_value_specification : unsigned_literal
    '''
    t[0] = Nodo("unsigned_value_specification", [t[1]], 'N', None)

def p_unsigned_literal(t):
    '''unsigned_literal : unsigned_numeric_literal 
    '''
    t[0] = Nodo("unsigned_literal", [t[1]], 'N', None)


# <general_literal>    ::=
#          <character_string_literal>
#      |     <national_character_string_literal>
#      |     <bit_string_literal>
#      |     <hex_string_literal>
#      |     <datetime_literal>
#      |     <interval_literal>


def p_unsigned_numeric_literal(t):
    '''unsigned_numeric_literal : exact_numeric_literal 
    '''
    t[0] = Nodo("unsigned_numeric_literal", [t[1]], 'N', None)



def p_exact_numeric_literal(t) :
    '''exact_numeric_literal : ENTERO PUNTO ENTERO
                        | ENTERO PUNTO 
                        |  PUNTO ENTERO
    '''
    if (len(t) == 4):
        temp = list()
        temp.append(t[1])
        temp.append(t[2])
        temp.append(t[3])
        t[0] = Nodo("exact_numeric_literal", temp,'S',None)        
    elif (len(t)==3):
        temp = list()
        temp.append(t[1])
        temp.append(t[2])
        t[0] = Nodo("exact_numeric_literal", temp,'S',None)




def p_column_reference(t) :
    '''column_reference : column_name 
                            | table_name PUNTO column_name
    '''
    if (len(t)==2):
        t[0] = Nodo("column_reference", [t[1]],'N',None)

    elif (len(t) == 4):
        temp = list()
        temp.append(t[1])
        tempNode2 = Nodo("column_reference", [t[2]],'S',str(t[2]))
        temp.append(tempNode2)
        temp.append(t[3])
        t[0] = Nodo("column_reference", temp,'N',None)  


def p_function_specification(t) :
    '''function_specification :  general_set_function
                                | COUNT PARIZQ MULT PARDER
    '''
    if (len(t)==2):
        t[0] = Nodo("function_specification", [t[1]],'N',None)

    elif (len(t) == 5):
        temp = list()
        tempNode1 = Nodo("function_specification", [t[1]],'S',str(t[1]))
        temp.append(tempNode1)        
        tempNode2 = Nodo("function_specification", [t[2]],'S',str(t[2]))
        temp.append(tempNode2)        
        tempNode3 = Nodo("function_specification", [t[3]],'S',str(t[3]))
        temp.append(tempNode3)        
        tempNode4 = Nodo("function_specification", [t[4]],'S',str(t[4]))
        temp.append(tempNode4)
        t[0] = Nodo("function_specification", temp,'N',None)  

def p_general_set_function(t) :
    '''general_set_function : set_function_type PARIZQ value_expression PARDER
                            | set_function_type PARIZQ set_quantifier value_expression PARDER
    '''
    if (len(t)==5):
        temp = list()
        temp.append(t[1])
        temp.append(t[3])
        t[0] = Nodo("general_set_function", temp,'N',None) 

    elif (len(t) == 4):
        temp = list()
        temp.append(t[1])
        temp.append(t[3])
        temp.append(t[4])        
        t[0] = Nodo("general_set_function", temp,'N',None) 


def p_set_function_type(t) :
    '''set_function_type : AVG
            | MAX
            | MIN
            | SUM
            | COUNT
    '''
    t[0] = Nodo("datetime_field", [t[1]],'S',str(t[1]))   

def p_set_quantifier(t) :
    '''set_quantifier : DISTINCT
            | ALL
    '''
    t[0] = Nodo("set_quantifier", [t[1]],'S',str(t[1]))   

#<general_set_function>    ::=
#         <set_function_type> <left_paren> [ <set_quantifier> ] <value_expression> <right_paren>

#<qualifier>    ::=   <table_name> 

#<correlation_name>    ::=   <identifier>

#<table_name>    ::=   <qualified_name> | <qualified_local_table_name>
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
