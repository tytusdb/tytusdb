import ply.yacc as yacc
import tempfile
from analizador_lexico import tokens
from analizador_lexico import analizador
from Nodo import *
from datetime import datetime
#import storageManager
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
                 | definitiontable_statement
                 | update_statement
                 | delete_statement
                 | select_statement
                 | enumtype
    '''
    t[0] = Nodo("statement", [t[1]], 'N', None)

    #*************************************************
    #**********************        type enum Modificado 14  de diciembre  Henry    Todas las posibles opcciones   ***********

    #*************************************************     

def p_enumtype(t):
    'enumtype : CREATE TYPE id_enum AS ENUM PARIZQ list_enum PARDER PTCOMA' 
    temp = list() 
    temp.append(t[3]) 
    temp.append(t[7])    
    t[0] = Nodo("enumtype", temp,'N',None)


def p_list_enum(t):
    'list_enum : list_enum  COMA  otro_id '
    temp = list()
    temp.append(t[1]) 
    temp.append(t[3])   
    t[0] = Nodo("list_enum", temp,'N',None) 

def p_otro_id(t) :
    'list_enum : otro_id'
    t[0] = Nodo("list_enum", [t[1]],'N',None)


def p_list1_enum(t):
    'otro_id :  CADENACOMSIMPLE ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))
    
def p_id_enum(t):
    'id_enum :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))    

    # *************************************************
    # **********************         createdb_statement Modificado 11  de diciembre  Henry      ***********
    # *************************************************


def p_definitiondb_statement(t):
    '''definitiondb_statement : create_db 
                              | alter_db  
                              | show_db   
                              | drop_db 
                              | use_db
                              
    '''       
    t[0] = Nodo("definitiondb_statement", [t[1]], 'N', None)

 #...............USE DEB........................................................................................................................
def p_use_db(t):
    'use_db : USE id_dbx PTCOMA'
    temp = list()
    temp.append(t[2])   
    t[0] = Nodo("use_db", temp,'N',None)
    
def p_id_dbx(t):
    'id_dbx :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))   
 
 
#................................CREATE DATABASE................................................................................................    
def p_create0_db(t):
    'create_db : CREATE ORH REPLACE DATABASE IF NOTH EXISTS id_create00 PTCOMA'
    temp = list()
    temp.append(t[8])   
    t[0] = Nodo("create_db", temp,'N',None)
    
def p_id_create00(t):
    'id_create00 :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))     

def p_create1_db(t):
    'create_db : CREATE ORH REPLACE DATABASE IF NOTH EXISTS id_create0 createdb_option PTCOMA'
    temp = list()
    temp.append(t[8])   
    temp.append(t[9])    
    t[0] = Nodo("create_db", temp,'N',None)    
    
def p_id_create0(t):
    'id_create0 :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))     
     
def p_create2_db(t):
    'create_db : CREATE ORH REPLACE DATABASE id_create22 PTCOMA'
    temp = list()
    temp.append(t[5])   
    t[0] = Nodo("create_db", temp,'N',None)    
   
def p_id_create22(t):
    'id_create22 :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))     
    

def p_create3_db(t):
    'create_db : CREATE ORH REPLACE DATABASE id_create1 createdb_option PTCOMA'
    temp = list()
    temp.append(t[5])  
    temp.append(t[6]) 
    t[0] = Nodo("create_db", temp,'N',None)  
    
    
def p_id_create1(t):
    'id_create1 :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))  
 
    
def p_create4_db(t):
    'create_db : CREATE DATABASE IF NOTH EXISTS id_create44 PTCOMA'
    temp = list()
    temp.append(t[6])   
    t[0] = Nodo("create_db", temp,'N',None) 

def p_id_create44(t):
    'id_create44 :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))     

def p_create5_db(t):
    'create_db : CREATE DATABASE IF NOTH EXISTS id_create2 createdb_option PTCOMA'
    temp = list()
    temp.append(t[6]) 
    temp.append(t[7])    
    t[0] = Nodo("create_db", temp,'N',None)     

def p_id_create2(t):
    'id_create2 :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1])) 
def p_create6_db(t):
    'create_db : CREATE DATABASE id_create66 PTCOMA'
    temp = list()
    temp.append(t[3])   
    t[0] = Nodo("create_db", temp,'N',None)   

def p_id_create66(t):
    'id_create66 :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))

def p_create7_db(t):
    'create_db : CREATE DATABASE id_create3 createdb_option PTCOMA'
    temp = list()
    temp.append(t[3])
    temp.append(t[4])
    t[0] = Nodo("create_db", temp,'N',None)
 
def p_id_create3(t):
    'id_create3 :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1])) 
    
def p_createdb_option(t): 
    """createdb_option : op_owner_mode
               | op_owner
               | op_mode
    """
    t[0] = Nodo("createdb_option", [t[1]],'N',None)  
   

def p_owner_mode(t): 
    'op_owner_mode : op_owner op_mode ' 
    temp = list()
    temp.append(t[1])
    temp.append(t[2])
    t[0] = Nodo("op_owner_mode", temp,'N',None)    
    
    
def p_p0_owner(t): 
    'op_owner : OWNER IGUAL CADENACOMSIMPLE ' 
    t[0] = Nodo("op_owner", [t[3]],'S',str(t[3]))       

def p_p1_owner(t): 
    'op_owner : OWNER CADENACOMSIMPLE ' 
    t[0] = Nodo("op_owner", [t[2]],'S',str(t[2]))   
    
def p_p0_mode(t): 
    'op_mode : MODE IGUAL ENTERO' 
    t[0] = Nodo("op_mode", [t[3]],'S',str(t[3]))   
    
def p_p1_mode(t): 
    'op_mode : MODE ENTERO ' 
    t[0] = Nodo("op_mode", [t[2]],'S',str(t[2]))  

def p_show_db(t):
    'show_db : SHOW DATABASES PTCOMA'
    t[0] = Nodo("show_db", [t[2]],'S',str(t[2]))

def p_alter0_db(t):
    'alter_db : ALTER DATABASE a_id OWNER TO a_cad PTCOMA'
    temp = list()
    temp.append(t[3])
    temp.append(t[6])
    t[0] = Nodo("alter_db", temp,'N',None)  
    
def p_a_id(t):
    'a_id :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1])) 
    
def p_a_cad(t):
    'a_cad :  CADENACOMSIMPLE' 
    t[0] = Nodo("owner", [t[1]],'S',str(t[1]))    
    
def p_alter1_db(t):
    'alter_db : ALTER DATABASE ID RENAME TO ID PTCOMA'
    temp = list()
    temp.append(t[3])
    temp.append(t[6])
    t[0] = Nodo("alter_db", temp, 'S', None)


def p_drop0_db(t):
    'drop_db : DROP DATABASE IF EXISTS ID PTCOMA'
    t[0] = Nodo("drop_db", [t[5]], 'S', str(t[5]))


def p_drop1_db(t):
    'drop_db : DROP DATABASE ID PTCOMA'
    t[0] = Nodo("drop_db", [t[3]], 'S', str(t[3]))


    # *************************************************
    # **********************        statement create_table Modificado 14  de diciembre  Henry      ***********
    # *************************************************    
 
def p_definitiontb_statement(t):
    '''definitiontable_statement : create_table 
                              | alter_table 
                              | drop_table 
    '''       
    t[0] = Nodo("definitiontb_statement", [t[1]],'N',None)   

#...........................................................DROP TABLE....................................................................       
def p_drop_table(t):
    'drop_table : DROP TABLE id_dt0 PTCOMA'
    temp = list() 
    temp.append(t[3]) 
    t[0] = Nodo("drop_table", temp,'N',None) 
    
def p_id_dt0(t):
    'id_dt0 :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))    
 
#................................ALTER TABLE-------------------------------------------------------------------------------------------------
def p_alter_table(t):
    'alter_table : ALTER TABLE id_at0 alter_option PTCOMA' 
    temp = list() 
    temp.append(t[3]) 
    temp.append(t[4]) 
    t[0] = Nodo("alter_table", temp,'N',None)     
    
def p_id_at0(t):
    'id_at0 :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))     
    
def p_alter_option(t): 
    'alter_option : ADD COLUMN id_at1 un_tipo'
    temp = list() 
    temp.append(t[3]) 
    temp.append(t[4]) 
    t[0] = Nodo("alter_option", temp,'N',None)  

def p_id_at1(t):
    'id_at1 :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))
    
def p_alter_option0(t): 
    'alter_option : DROP COLUMN id_at2'
    temp = list() 
    temp.append(t[3]) 
    t[0] = Nodo("alter_option", temp,'N',None) 


def p_id_at2(t):
    'id_at2 :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))

def p_alter_option1(t): 
    'alter_option : ADD CHECK PARIZQ condicion_check  PARDER'
    temp = list() 
    temp.append(t[4]) 
    t[0] = Nodo("alter_option", temp,'N',None)  
    
#...............check.......................................................................................................
def p_condition_check(t):  
    'condicion_check : id_check0 operador_check expresion_check'
    temp = list()
    temp.append(t[1]) 
    temp.append(t[2]) 
    temp.append(t[3])
    t[0] = Nodo("condicion_check", temp,'N',None)
    
def p_id_check(t):  
    'id_check0 :  ID' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))      
    
def p_operador_check(t):   
    """operador_check :  DIFERENTEH IGUAL   
                      | IGUAL 
                      | MENQUE
                      | MAYQUE
                      | MENORIGU 
                      | MAYORIGU
                      | DIFERENTEH
                     
    """
    if (len(t) == 3):
        temp = list()
        temp.append(t[1])
        temp.append(t[2])
        t[0] = Nodo("operador_check", temp,'S',None)
     
    else:
        t[0] = Nodo("operador_check", [t[1]],'S',str(t[1])) 


def p_expresion_check0(t):  
    """expresion_check :   un_entero
                          | una_cadena
                          | un_DECIMALV
                          | un_idd
                                        
    """
    t[0] = Nodo("expresion_check", [t[1]],'N',None)


def p_expresion_check1(t):  
    'un_entero :  ENTERO' 
    t[0] = Nodo("entero", [t[1]],'S',str(t[1]))
    
def p_expresion_check2(t):  
    'una_cadena :  CADENACOMSIMPLE' 
    t[0] = Nodo("cadena", [t[1]],'S',str(t[1]))  
    
def p_expresion_check3(t):  
    'un_DECIMALV :  DECIMALV' 
    t[0] = Nodo("DECIMALV", [t[1]],'S',str(t[1]))  
    
def p_expresion_check4(t):  
    'un_idd :  ID' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))  
    
def p_alter_option2(t): 
    'alter_option : ALTER COLUMN id_nulo SET NOTH NULL'
    temp = list() 
    temp.append(t[3]) 
    t[0] = Nodo("alter_option", temp,'N',None)    

def p_id_nulo(t):  
    'id_nulo :  ID' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1])) 
    
def p_alter_option3(t): 
    'alter_option : DROP CONSTRAINT id_ct'
    temp = list() 
    temp.append(t[3]) 
    t[0] = Nodo("alter_option", temp,'N',None)    

def p_id_ct(t):  
    'id_ct :  ID' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))       
    
#---------------------UNIQUE-------------------------------------------------------------------------------------------------
def p_alter_option4(t):
    'alter_option : ADD CONSTRAINT id2_at2 UNIQUE PARIZQ p_column PARDER'
    temp = list()
    temp.append(t[3]) 
    temp.append(t[6]) 
    t[0] = Nodo("alter_option", temp,'N',None)
    
def p_id2_at2(t):  
    'id2_at2 :  ID' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))    

def p_p_column(t):  
    'p_column :  ID' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))      



#.....................FOREIGN -----------------------------------------------------------------------------------------------
def p_alter_option5(t):
    'alter_option : ADD FOREIGN KEY PARIZQ column_group1 PARDER  REFERENCES PARIZQ column_group1 PARDER'
    temp = list()
    temp.append(t[5]) 
    temp.append(t[9]) 
    t[0] = Nodo("alter_option", temp,'N',None)

#---Para grupo de columna    
def p_column_group1(t):
    'column_group1 : column_group1  COMA  column_g'
    temp = list()
    temp.append(t[1]) 
    temp.append(t[3])   
    t[0] = Nodo("column_group", temp,'N',None) 
    
def p_columng(t) :
    'column_group1 : column_g'
    t[0] = Nodo("column_group", [t[1]],'N',None)

def p_columng1(t):
    'column_g :  ID' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))


#.........................................CAMBIO DE TIPOS PARA STRINGS...........................................................
def p_alter_option6(t):
    'alter_option : lista_columnas'
    temp = list()
    temp.append(t[1]) 
    t[0] = Nodo("alter_option", temp,'N',None)

def p_lista_columnas(t):
    'lista_columnas : lista_columnas COMA lista_col'
    temp = list()
    temp.append(t[1])  
    temp.append(t[3]) 
    t[0] = Nodo("lista_columnas", temp,'N',None)

def p_lista_col(t):
    'lista_columnas : lista_col'
    temp = list()
    temp.append(t[1])  
    t[0] = Nodo("lista_columnas", [t[1]],'N',None)
    
def p_lista_col0(t):
    'lista_col : ALTER COLUMN p1  TYPE p2 PARIZQ p3 PARDER '
    temp = list()
    temp.append(t[3])  
    temp.append(t[5])
    temp.append(t[7]) 
    t[0] = Nodo("lista_col", temp,'N',None)

def p_p1(t):
    'p1 :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))

def p_p2(t):
    '''p2 :  VARCHAR
            | CHAR
            | CHARACTER
            ''' 
    t[0] = Nodo("tipo", [t[1]],'S',str(t[1]))

def p_p3(t):
    'p3 : ENTERO ' 
    t[0] = Nodo("valor", [t[1]],'S',str(t[1]))
    

   
#...........................................CREATE TABLE.......................................................................  
def p_create_table(t):
    'create_table : CREATE TABLE id_ct1 PARIZQ list_rowsh PARDER PTCOMA' 
    temp = list() 
    temp.append(t[3]) 
    temp.append(t[5]) 
    t[0] = Nodo("create_table", temp,'N',None) 
    
    
def p_create_table0(t):
    'create_table : CREATE TABLE id_ct1  PARIZQ list_rowsh PARDER inherits_table' 
    temp = list() 
    temp.append(t[3]) 
    temp.append(t[5]) 
    temp.append(t[7]) 
    t[0] = Nodo("create_table", temp,'N',None)        
    
def p_id_ct1(t):
    'id_ct1 :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))
    

def p_end_create_table(t):
    'inherits_table : INHERITS PARIZQ  id_inh0 PARDER PTCOMA'  
    temp = list() 
    temp.append(t[3]) 
    t[0] = Nodo("inherits_table", temp,'N',None)  
    
def p_id_inh0(t):
    'id_inh0 :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))
    
def p_list_rowsh(t):
    'list_rowsh : list_rowsh COMA rowsh'
    temp = list()
    temp.append(t[1]) 
    temp.append(t[3])   
    t[0] = Nodo("list_rowsh", temp,'N',None)    
    
def p_list_rowsh0(t) :
    'list_rowsh : rowsh'
    t[0] = Nodo("list_rowsh", [t[1]],'N',None)

def p_list_rowsh1(t) :
    'rowsh : id_row un_tipo'
    temp = list()
    temp.append(t[1]) 
    temp.append(t[2])   
    t[0] = Nodo("columna", temp,'N',None) 
    
           
def p_id_row(t):
    'id_row  :  ID ' 
    t[0] = Nodo("id", [t[1]],'S',str(t[1]))     
    
#ver todos los tipoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooos    
def p_un_tipo(t):  
    """un_tipo :  FLOAT
                | TEXT
                | INT
                | MONEY
                | BIGINT
                | SMALLINT
                
                                               
    """
    t[0] = Nodo("tipo", [t[1]],'S',str(t[1])) 
    
    

#*************************************************
#**********************         insert_statement      ***********
#*************************************************   
#region INSERT
def p_insert_statement(t) :
    '''insert_statement : INSERT INTO table_name insert_columns_and_source PTCOMA
    '''
    temp = list()
    temp.append(t[3])
    temp.append(t[4])
    t[0] = Nodo("insert_statement", temp,'N',None)


def p_table_name(t) :
    'table_name : ID '
    t[0] = Nodo("table_name", [t[1]],'S',str(t[1]))


#*************************************************
#**********************         insert_columns_and_source      ***********
#*************************************************    

def p_insert_columns_and_source(t) :
    '''insert_columns_and_source : PARIZQ insert_column_list PARDER VALUES query_expression_insert
                                    | VALUES query_expression_insert
                                    | insert_default_values
    '''
    if (len(t) == 6):
        #t[0] =InsertColumnsValues(t[2],t[5])
        temp = list()
        temp.append(t[2])
        temp.append(t[5])
        t[0] = Nodo("insert_columns_and_source", temp,'N',None)
    elif (len(t)==3):
        #t[0] =InsertValues(t[1],t[2])
        t[0] = Nodo("insert_columns_and_source", [t[2]],'N',None)

    elif (len(t)==2):
        #t[0] =InsertValues(t[1],t[2])
        t[0] = Nodo("insert_columns_and_source", [t[1]],'N',None)


def p_insert_defaul_values(t) :
    'insert_default_values    : DEFAULT VALUES'
    t[0] = Nodo("column_name", [t[1]],'S',str(t[1]))

#*************************************************
#**********************         insert_column_list      ***********
#*************************************************   

def p_insert_column_list(t) :
    'insert_column_list    : insert_column_list  COMA column_name'
    temp = list()
    temp.append(t[1])
    temp.append(t[3])
    t[0] = Nodo("insert_column_list1", temp,'N', None)

def p_insert_column_name(t) :
    'insert_column_list    : column_name'
    #t[0] = [t[1]]
    t[0] = Nodo("insert_column_list2", [t[1]],'N',None)


def p_column_name(t) :
    'column_name    : ID '
    t[0] = Nodo("column_name", [t[1]],'S',str(t[1]))


#*************************************************
#**********************         query_expression_insert      ***********
#*************************************************

def p_query_expression_insert(t):
    '''query_expression_insert :    insert_list
                        '''
    t[0] = Nodo("query_expression_insert", [t[1]],'N',None)

def p_insert_list(t) :
    '''insert_list    :  insert_list COMA insert_value_list  '''
    temp = list()
    temp.append(t[1])
    temp.append(t[3])
    t[0] = Nodo("insert_list2", temp,'N',None)


def p_insert_item(t) :
    '''insert_list    :  insert_value_list  '''
    t[0] = Nodo("insert_list1", [t[1]],'N',None)

def p_insert_value_list(t) :
    '''insert_value_list    : PARIZQ value_list PARDER '''
    t[0] = Nodo("insert_value_list", [t[2]],'N',None)


def p_value_list(t) :
    '''value_list    : value_list  COMA insert_value'''
    temp = list()
    temp.append(t[1])
    temp.append(t[3])
    t[0] = Nodo("value_list1", temp,'N',None)


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

#*************************************************
#**********************         update_statement      ***********
#*************************************************   
#region UPDATE
def p_update_statement(t) :
    '''update_statement : UPDATE table_name SET set_clause_list WHERE search_condition PTCOMA
                        | UPDATE table_name SET set_clause_list PTCOMA
    '''
    if (len(t) == 8):
        temp = list()
        temp.append(t[2])
        temp.append(t[4])
        temp.append(t[6])
        t[0] = Nodo("update_statement", temp,'N',None)        
    elif (len(t)==6):
        temp = list()
        temp.append(t[2])
        temp.append(t[4])
        t[0] = Nodo("update_statement", temp,'N',None)



def p_set_clause_list(t) :
    '''set_clause_list    : set_clause_list  COMA set_clause'''
    temp = list()
    temp.append(t[1])
    temp.append(t[3])
    t[0] = Nodo("set_clause_list", temp,'N',None)


def p_p_set_clause_item(t) :
    '''set_clause_list    : set_clause'''
    t[0] = Nodo("set_clause_list", [t[1]],'N',None)


def p_set_clause(t) :
    'set_clause : column_name  IGUAL update_source'
    temp = list()
    temp.append(t[1])
    temp.append(t[3])
    t[0] = Nodo("set_clause", temp,'N',None)

def p_update_source(t) :
    '''update_source : value_expression  
                | NULL 
    '''
    t[0] = Nodo("update_source", [t[1]],'N',None)


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
                        | ABS
                        | CBRT
                        | CEIL
                        | CEILING
                        | DEGREES
                        | DIV
                        | EXP
                        | FACTORIAL
                        | FLOOR
                        | GCD
                        | LN
                        | LOG
                        | MOD
                        | PI
                        | POWER
                        | RADIANS
                        | ROUND
                        | SIGN
                        | SQRT
                        | TRUNC
                        | RANDOM
                        | ACOS
                        | ACOSD
                        | ASIN
                        | ASIND
                        | ATAN
                        | ATAND
                        | ATAN2
                        | ATAN2D
                        | COS
                        | COSD
                        | COT
                        | COTD
                        | SIN
                        | SIND
                        | TAN
                        | TAND
                        | SINH
                        | COSH
                        | TANH
                        | ASINH
                        | ACOSH
                        | ATANH
                        | LENGTH
                        | SUBSTRING
                        | MD5
                        | SHA256
                        | SUBSTR
                        | GET_BYTE
                        | SET_BYTE
                        | TRIM
                        | CONVERT
                        | ENCODE
                        | DECODE
                        | RAIZQ
                        | NOW
                        | CURRENT_DATE 
                        | CURRENT_TIME 
                        | TIMESTAMP                          
                        | EXTRACT                          
                        | DATE_PART 
                        | MULT 
                        | ENTERO
                        | DECIMALV
                        | CADENACOMSIMPLE
                        | DEFAULT
                        | ID
                        | select_function_element column_select_punto
                                             
    '''
    if (len(t) == 2):
        t[0] = Nodo("column_name", [t[1]],'S', str(t[1]) )
    if (len(t) == 3):
        temp = list()
        temp.append(t[1])
        temp.append(t[2])
        t[0] = Nodo("column_name", temp, 'N', None)


def p_column_select_punto(t) :
    '''column_select_punto  : PUNTO select_function_element                        
    '''
    #t[0] = Nodo("column_select_punto", [t[2]],'S', str(t[1]) )
    t[0] = Nodo("column_select_punto", [t[2]], 'N', None)
   


def p_select_function_element(t) :
    '''select_function_element  : ID
                                | MULT
                                | ENTERO
                                | ENTERO COMA ENTERO
                                | DECIMALV COMA ENTERO
                                | DECIMALV COMA DECIMALV
                                | ENTERO COMA DECIMALV                               
                                | DECIMALV
                                | CADENACOMSIMPLE
                                | NULL
                                
    '''
    if (len(t) == 2):
        t[0] = Nodo("select_function_element", [t[1]], 'S', str(t[1]))
    if (len(t) == 4):
        t[0] = Nodo("select_function_element", [t[1]], 'S', str(t[1])+","+str(t[3]))
    else :
        t[0] = Nodo("select_function_element", [t[1]], 'S', str(t[1]))


def p_column_functionext_select(t):
    '''column_funtionext_select : column_datefuntion_select 
                                | column_datepartfuntion_select 
    '''
    t[0] = Nodo("column_funtionext_select", [t[1]], 'N', None)

def p_column_datefunction_select(t) :
    '''column_datefuntion_select    : column_dateExtractfunc_select FROM TIMESTAMP  column_datefuntion_select_date column_datefuntion_select_hour COMSIM                 
    '''
    temp = list()
    temp.append(t[1])
    temp.append(t[4])
    temp.append(t[5])
    
    t[0] = Nodo("column_datefuntion_select", temp, 'N', None)


def p_column_datefunction_select_date(t) :
    '''column_datefuntion_select_date    : column_date_year column_date_month  column_date_day               
    '''
    temp = list()
    temp.append(t[1])
    temp.append(t[2])
    temp.append(t[3])
    t[0] = Nodo("column_datefuntion_select_date", temp, 'N', None)

def p_column_datefunction_select_hour(t) :
    '''column_datefuntion_select_hour    : column_date_hour column_date_min  column_date_seg               
    '''
    temp = list()
    temp.append(t[1])
    temp.append(t[2])
    temp.append(t[3])
    t[0] = Nodo("column_datefuntion_select_hour", temp, 'N', None)




def p_column_date_year(t) :
    '''column_date_year   : COMSIM  ENTERO                                  
    '''
    t[0] = Nodo("column_date_year", [t[2]],'S', str(t[2]) )
   
def p_column_date_month(t) :
    '''column_date_month   : OPMENOS ENTERO                                   
    '''
    t[0] = Nodo("column_date_month", [t[2]],'S', str(t[2]) )
   
def p_column_date_DAY(t) :
    '''column_date_day   : OPMENOS ENTERO                                   
    '''
    t[0] = Nodo("column_date_day", [t[2]],'S', str(t[2]) )
   

def p_column_date_hour(t) :
    '''column_date_hour   : ENTERO                                  
    '''
    t[0] = Nodo("column_date_hour", [t[1]],'S', str(t[1]) )
   
def p_column_date_min(t) :
    '''column_date_min   : DOSPUNTOS ENTERO                                   
    '''
    t[0] = Nodo("column_date_min", [t[2]],'S', str(t[2]) )
   
def p_column_date_seg(t) :
    '''column_date_seg   : DOSPUNTOS ENTERO                                   
    '''
    t[0] = Nodo("column_date_seg", [t[2]],'S', str(t[2]) )


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


def p_groupby_statement(t) :
    '''groupby_statement   : GROUP BY groupby_column_list    
    '''
    t[0] = Nodo("groupby_statement", [t[3]], 'N', None)
   


def p_groupby_column_list(t):
    'groupby_column_list    : groupby_column_list  COMA column_name_groupby'
    temp = list()
    temp.append(t[1])
    temp.append(t[3])
    t[0] = Nodo("groupby_column_list1", temp, 'N', None)


def p_groupby_column_list_name(t):
    'groupby_column_list : column_name_groupby'     
    t[0] = Nodo("groupby_column_list2", [t[1]], 'N', None)


# def p_column_name_select(t):
#     'column_name_select   : column_funtion_select'
#     # t[0] = Nodo("column_name_select", [t[1]], 'S', str(t[1]))
#     t[0] = Nodo("column_name_select", [t[1]], 'N', None)


def p_column_name_groupby(t):
    '''column_name_groupby    : groupby_column_item 
    '''

    t[0] = Nodo("column_name_select", [t[1]], 'N', None)    


def p_groupby_column_item(t) :
    '''groupby_column_item  : ID 
                                             
    '''
    t[0] = Nodo("column_name", [t[1]],'S', str(t[1]) )



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
    tempNode2 = Nodo("opOR", [t[2]],'S',str(t[2]))
    temp.append(tempNode2)        
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
    tempNode2 = Nodo("opAnd", [t[2]],'S',str(t[2]))
    temp.append(tempNode2)    
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
                | between_predicate
                | in_predicate
                | like_percent_predicate
                | null_predicate
                | distinct_predicate
                | substring_predicate
                | extract_predicate
    '''
    t[0] = Nodo("predicate", [t[1]],'N',None)  


#*************************************************
#**********************         comparasion           ***********
#*************************************************  

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

# def p_value_expression(t):
#     '''value_expression : ENTERO
#                         | DECIMALV
#                         | CADENACOMSIMPLE
#                         | DEFAULT
#                         | ID
#                         | NOW PARIZQ PARDER
#     '''
#     t[0] = Nodo("value_expression", [t[1]],'S',str(t[1])) 

#endregion

#*************************************************
#**********************         BETWEEN PREDICATE           ***********
#*************************************************  

def p_between_predicate(t) :
    '''between_predicate : row_value_constructor NOTH BETWEEN row_value_constructor AND row_value_constructor
                            | row_value_constructor BETWEEN row_value_constructor AND row_value_constructor
    '''
    if (len(t) == 7):
        temp = list()
        temp.append(t[1])
        tempNode1 = Nodo("between_predicate", [t[2]],'S',str(t[2]))
        temp.append(tempNode1)
        tempNode3 = Nodo("between_predicate", [t[3]],'S',str(t[3]))
        temp.append(tempNode3)
        temp.append(t[4])
        tempNode5 = Nodo("between_predicate", [t[5]],'S',str(t[5]))
        temp.append(tempNode5)
        temp.append(t[6])
        t[0] = Nodo("between_predicate", temp,'N',None)        

    elif (len(t)==6):
        temp = list()
        temp.append(t[1])
        tempNode2 = Nodo("between_predicate", [t[2]],'S',str(t[2]))
        temp.append(tempNode2)
        temp.append(t[3])
        tempNode4 = Nodo("between_predicate", [t[4]],'S',str(t[4]))
        temp.append(tempNode4)
        temp.append(t[5])
        t[0] = Nodo("between_predicate", temp,'N',None) 

#*************************************************
#**********************         IN PREDICATE           ***********
#*************************************************  

def p_in_predicate(t) :
    '''in_predicate : row_value_constructor NOT IN in_predicate_value
                            | row_value_constructor IN in_predicate_value
    '''
    if (len(t) == 5):
        temp = list()
        temp.append(t[1])
        tempNode1 = Nodo("in_predicate", [t[2]],'S',str(t[2]))
        temp.append(tempNode1)
        tempNode3 = Nodo("in_predicate", [t[3]],'S',str(t[3]))
        temp.append(tempNode3)
        temp.append(t[4])
        t[0] = Nodo("in_predicate", temp,'N',None)        

    elif (len(t)==4):
        temp = list()
        temp.append(t[1])
        tempNode2 = Nodo("in_predicate", [t[2]],'S',str(t[2]))
        temp.append(tempNode2)
        temp.append(t[3])
        t[0] = Nodo("in_predicate", temp,'N',None) 


def p_in_predicate_value(t) :
    '''in_predicate_value : PARIZQ in_value_list PARDER
    '''
    t[0] = Nodo("in_predicate_value", [t[2]],'N',None)


def p_in_value_list(t) :
    '''in_value_list    : in_value_list  COMA value_expression'''
    temp = list()
    temp.append(t[1])
    temp.append(t[3])
    t[0] = Nodo("in_value_list", temp,'N',None)


def p_in_value_item(t) :
    '''in_value_list    : value_expression'''
    t[0] = Nodo("in_value_list", [t[1]],'N',None)


#*************************************************
#**********************         LIKE PREDICATE         ***********
#*************************************************  

def p_like_percent_predicate(t) :
    '''like_percent_predicate : ID NOT LIKE CADENACOMSIMPLE
                        | ID LIKE CADENACOMSIMPLE
    '''
    if (len(t) == 5):
        temp = list()
        temp.append(t[1])
        temp.append(t[2])
        temp.append(t[3])
        temp.append(t[4])
        t[0] = Nodo("like_percent_predicate", temp,'S',None)        
    elif (len(t)==4):
        temp = list()
        temp.append(t[1])
        temp.append(t[2])
        temp.append(t[3])
        t[0] = Nodo("like_percent_predicate", temp,'S',None)



#*************************************************
#**********************         NULL PREDICATE           ***********
#*************************************************  

def p_null_predicate(t) :
    '''null_predicate : row_value_constructor IS NOTH NULL
                        | row_value_constructor IS NULL
                        | row_value_constructor ISNULL
    '''
                        #| row_value_constructor NOTNULL
    if (len(t) == 5):
        temp = list()
        temp.append(t[1])
        tempNode2 = Nodo("null_predicate", [t[2]],'S',str(t[2]))
        temp.append(tempNode2)
        tempNode3 = Nodo("null_predicate", [t[3]],'S',str(t[3]))
        temp.append(tempNode3)
        tempNode4 = Nodo("null_predicate", [t[4]],'S',str(t[4]))
        temp.append(tempNode4)
        t[0] = Nodo("null_predicate", temp,'N',None)        
    elif (len(t)==4):
        temp = list()
        temp.append(t[1])
        tempNode2 = Nodo("null_predicate", [t[2]],'S',str(t[2]))
        temp.append(tempNode2)
        tempNode3 = Nodo("null_predicate", [t[3]],'S',str(t[3]))
        temp.append(tempNode3)
        t[0] = Nodo("null_predicate", temp,'N',None)   
    elif (len(t)==3):
        temp = list()
        temp.append(t[1])
        tempNode2 = Nodo("null_predicate", [t[2]],'S',str(t[2]))
        temp.append(tempNode2)
        t[0] = Nodo("null_predicate", temp,'N',None)   


#*************************************************
#**********************         DISTINCT PREDICATE         ***********
#*************************************************  

def p_distinct_predicate(t) :
    '''distinct_predicate : row_value_constructor IS DISTINCT FROM row_value_constructor
                            | row_value_constructor IS NOT DISTINCT FROM row_value_constructor
    '''
    if (len(t)==6):
        temp = list()
        temp.append(t[1])
        tempNode1 = Nodo("distinct_predicate", [t[2]],'S',str(t[2]))
        temp.append(tempNode1)
        tempNode3 = Nodo("distinct_predicate", [t[3]],'S',str(t[3]))
        temp.append(tempNode3)
        tempNode4 = Nodo("distinct_predicate", [t[4]],'S',str(t[4]))
        temp.append(tempNode4)
        temp.append(t[5])
        t[0] = Nodo("distinct_predicate", temp,'N',None) 
    elif (len(t) == 7):
        temp = list()
        temp.append(t[1])
        tempNode1 = Nodo("distinct_predicate", [t[2]],'S',str(t[2]))
        temp.append(tempNode1)
        tempNode3 = Nodo("distinct_predicate", [t[3]],'S',str(t[3]))
        temp.append(tempNode3)
        tempNode4 = Nodo("distinct_predicate", [t[4]],'S',str(t[4]))
        temp.append(tempNode4)
        tempNode5 = Nodo("distinct_predicate", [t[5]],'S',str(t[5]))
        temp.append(tempNode5)        
        temp.append(t[6])
        t[0] = Nodo("distinct_predicate", temp,'N',None)        


#*************************************************
#**********************         SUBSTRING PREDICATE         ***********
#*************************************************  

def p_substring_predicate(t) :
    '''substring_predicate : SUBSTRING PARIZQ  column_reference COMA select_function_element PARDER IGUAL CADENACOMSIMPLE
    '''
    temp = list()
    temp.append(t[3])
    temp.append(t[5])    
    tempNode7 = Nodo("substring_predicate", [t[7]],'S',str(t[7]))
    temp.append(tempNode7)
    tempNode8 = Nodo("substring_predicate", [t[8]],'S',str(t[8]))
    temp.append(tempNode8)
    t[0] = Nodo("substring_predicate", temp,'N',None) 



def p_extract_predicate(t) :
    '''extract_predicate :  ID EXTRACT  PARIZQ extract_field FROM extract_source PARDER IGUAL ENTERO IS TRUE
                            | ID EXTRACT  PARIZQ extract_field FROM extract_source PARDER IGUAL ENTERO IS FALSE
                            | EXTRACT  PARIZQ extract_field FROM extract_source PARDER IGUAL ENTERO IS TRUE
                            | EXTRACT  PARIZQ extract_field FROM extract_source PARDER IGUAL ENTERO IS FALSE
    '''
    if (len(t)==12):
        temp = list()
        tempNode1 = Nodo("extract_predicate", [t[1]],'S',str(t[1]))
        temp.append(tempNode1)
        temp.append(t[4])    
        temp.append(t[6])
        tempNode8 = Nodo("extract_predicate", [t[8]],'S',str(t[8]))
        temp.append(tempNode8)    
        tempNode9 = Nodo("extract_predicate", [t[9]],'S',str(t[9]))
        temp.append(tempNode9)    
        tempNode10 = Nodo("extract_predicate", [t[10]],'S',str(t[10]))
        temp.append(tempNode10)    
        tempNode11 = Nodo("extract_predicate", [t[11]],'S',str(t[11]))
        temp.append(tempNode11)        
        t[0] = Nodo("extract_predicate", temp,'N',None) 
    elif (len(t) == 11):
        temp = list()
        temp.append(t[3])    
        temp.append(t[5])
        tempNode8 = Nodo("extract_predicate", [t[7]],'S',str(t[7]))
        temp.append(tempNode8)    
        tempNode9 = Nodo("extract_predicate", [t[8]],'S',str(t[8]))
        temp.append(tempNode9)    
        tempNode10 = Nodo("extract_predicate", [t[9]],'S',str(t[9]))
        temp.append(tempNode10)    
        tempNode11 = Nodo("extract_predicate", [t[10]],'S',str(t[10]))
        temp.append(tempNode11)        
        t[0] = Nodo("extract_predicate", temp,'N',None) 

#*************************************************
#**********************         expresion factor         ***********
#*************************************************  
def p_value_expression(t):
    '''value_expression : ENTERO
                        | DECIMALV
                        | CADENACOMSIMPLE
                        | DEFAULT
                        | ID
                        | NOW PARIZQ PARDER
                        | EXTRACT  PARIZQ extract_field FROM extract_source PARDER
    '''
                        # | numeric_value_expression
                        # | string_value_expression
                        # | datetime_value_expression
                        # | interval_value_expression
    if (len(t)==7):
        temp = list()
        temp.append(t[3])
        temp.append(t[5])
        t[0] = Nodo("value_expression", temp,'N',None) 
    elif (len(t)==4):
        t[0] = Nodo("value_expression", [t[1]],'S',str(t[1]))       
    elif (len(t) == 2):
         t[0] = Nodo("value_expression", [t[1]],'S',str(t[1]))       

# def p_value_expression(t):
#     '''value_expression_expand : numeric_value_expression
#                         | string_value_expression
#                         | datetime_value_expression
#                         | interval_value_expression





def p_datetime_value_expression(t) :
    '''datetime_value_expression : value_expression_primary
                                | interval_value_expression OPSUM value_expression_primary
                                | datetime_value_expression OPSUM interval_term
                                | datetime_value_expression OPMENOS interval_term
    '''
    if (len(t)==2):
        temp = list()
        temp.append(t[1])
        t[0] = Nodo("datetime_value_expression", temp,'N',None)         
    elif (len(t) == 4):
        temp = list()
        temp.append(t[1])        
        tempNode2 = Nodo("datetime_value_expression", [t[2]],'S',str(t[2]))
        temp.append(tempNode2)
        temp.append(t[3]) 
        t[0] = Nodo("datetime_value_expression", temp,'N',None)        


def p_interval_value_expression(t) :
    '''interval_value_expression : interval_term
                                | interval_value_expression_1 OPSUM interval_term_1
                                | interval_value_expression_1 OPMENOS interval_term_1
                                | PARIZQ datetime_value_expression OPMENOS value_expression_primary PARDER interval_qualifier
    '''
    if (len(t)==2):
        temp = list()
        temp.append(t[1])
        t[0] = Nodo("interval_value_expression", temp,'N',None)         
    elif (len(t) == 4):
        temp = list()
        temp.append(t[1])        
        tempNode2 = Nodo("interval_value_expression", [t[2]],'S',str(t[2]))
        temp.append(tempNode2)
        temp.append(t[3]) 
        t[0] = Nodo("interval_value_expression", temp,'N',None)        
    elif (len(t) == 7):
        temp = list()
        tempNode1 = Nodo("interval_value_expression", [t[1]],'S',str(t[1]))
        temp.append(tempNode1)
        temp.append(t[2])     
        tempNode3 = Nodo("interval_value_expression", [t[3]],'S',str(t[3]))
        temp.append(tempNode3)
        temp.append(t[4])     
        tempNode5 = Nodo("interval_value_expression", [t[5]],'S',str(t[5]))
        temp.append(tempNode5)
        temp.append(t[6])     
        t[0] = Nodo("interval_value_expression", temp,'N',None)


def p_interval_value_expression_1(t) :
    '''interval_value_expression_1 : interval_value_expression
    '''
    t[0] = Nodo("interval_value_expression_1", [t[1]],'N',None)        



def p_interval_term(t) :
    '''interval_term : interval_factor
                    | interval_term_2 MULT factor
                    | interval_term_2 OPDIV factor
                    | term MULT interval_factor
    '''
    if (len(t)==2):
        temp = list()
        temp.append(t[1])
        t[0] = Nodo("interval_term", temp,'N',None)         
    elif (len(t) == 4):
        temp = list()
        temp.append(t[1])        
        tempNode2 = Nodo("interval_term", [t[2]],'S',str(t[2]))
        temp.append(tempNode2)
        temp.append(t[3]) 
        t[0] = Nodo("interval_term", temp,'N',None)        


def p_interval_term_1(t) :
    '''interval_term_1 : interval_term
    '''
    t[0] = Nodo("interval_term_1", [t[1]],'N',None)   



def p_interval_term_2(t) :
    '''interval_term_2 : interval_term
    '''
    t[0] = Nodo("interval_term_2", [t[1]],'N',None)      

def p_interval_factor(t) :
    '''interval_factor : OPSUM interval_primary
                        | OPMENOS interval_primary
                        | interval_primary
    '''
    if (len(t)==2):
        temp = list()
        temp.append(t[1])
        t[0] = Nodo("interval_factor", temp,'N',None)         
    elif (len(t) == 3):
        temp = list()     
        tempNode1 = Nodo("interval_factor", [t[1]],'S',str(t[1]))
        temp.append(tempNode1)
        temp.append(t[2]) 
        t[0] = Nodo("interval_factor", temp,'N',None)  


def p_interval_primary(t) :
    '''interval_primary : value_expression_primary
                        | value_expression_primary interval_qualifier
    '''
    if (len(t)==2):
        t[0] = Nodo("interval_primary", [t[1]], 'N', None)
    elif (len(t) == 3):
        temp = list()     
        temp.append(t[1]) 
        temp.append(t[2]) 
        t[0] = Nodo("interval_primary", temp,'N',None)  



def p_interval_qualifier(t) :
    '''interval_qualifier : start_field TO end_field
                    | single_datetime_field
    '''
    if (len(t)==2):
        temp = list()
        temp.append(t[1])
        t[0] = Nodo("interval_qualifier", temp,'N',None)         
    elif (len(t) == 4):
        temp = list()
        temp.append(t[1])        
        tempNode2 = Nodo("interval_qualifier", [t[2]],'S',str(t[2]))
        temp.append(tempNode2)
        temp.append(t[3]) 
        t[0] = Nodo("interval_qualifier", temp,'N',None)  




def p_start_field(t) :
    '''start_field : non_second_datetime_field PARIZQ ENTERO PARDER
                    | non_second_datetime_field
    '''
    if (len(t)==2):
        temp = list()
        temp.append(t[1])
        t[0] = Nodo("start_field", temp,'N',None)         
    elif (len(t) == 4):
        temp = list()
        temp.append(t[1])        
        temp.append(t[3]) 
        t[0] = Nodo("start_field", temp,'N',None)  



def p_end_field(t) :
    '''end_field : SECOND PARIZQ ENTERO PARDER
                    | non_second_datetime_field
                    | SECOND
    '''
    if (len(t)==2):
        temp = list()
        temp.append(t[1])
        t[0] = Nodo("end_field", temp,'N',None)         
    elif (len(t) == 5):
        temp = list()
        tempNode1 = Nodo("end_field", [t[1]],'S',str(t[1]))
        temp.append(tempNode1)        
        temp.append(t[3])
        t[0] = Nodo("end_field", temp,'N',None)  


def p_single_datetime_field(t) :
    '''single_datetime_field :    non_second_datetime_field PARIZQ ENTERO PARDER
                                | non_second_datetime_field
                                | second_comp
    '''
    if (len(t)==2):
        t[0] = Nodo("single_datetime_field", [t[1]],'N',str(t[1])) 
    elif (len(t) == 5):
        temp = list()
        temp.append(t[1])
        temp.append(t[3])
        t[0] = Nodo("single_datetime_field", temp,'N',None)  



def p_second_comp(t) :
    '''second_comp :    SECOND PARIZQ ENTERO COMA PARIZQ ENTERO PARDER
                        | SECOND PARIZQ ENTERO PARDER
                        | SECOND
    '''
    if (len(t)==2):
        t[0] = Nodo("second_comp", [t[1]],'S',str(t[1])) 
    elif (len(t) == 5):
        temp = list()
        tempNode1 = Nodo("second_comp", [t[1]],'S',str(t[1]))
        temp.append(tempNode1)        
        temp.append(t[3])
        t[0] = Nodo("second_comp", temp,'N',None)  
    elif (len(t) == 8):
        temp = list()
        tempNode1 = Nodo("second_comp", [t[1]],'S',str(t[1]))
        temp.append(tempNode1)        
        temp.append(t[3])
        temp.append(t[6])        
        t[0] = Nodo("second_comp", temp,'N',None)  


def p_non_second_datetime_field(t) :
    '''non_second_datetime_field    : HOUR  
                                        | MINUTE 
                                        | YEAR 
                                        | MONTH 
                                        | DAY                          
    '''
    t[0] = Nodo("non_second_datetime_field", [t[1]],'S', str(t[1]))


def p_string_value_expression(t) :
    '''string_value_expression : character_value_expression
    '''
    t[0] = Nodo("string_value_expression", [t[1]],'N',None)

def p_numeric_value_expression(t) :
    '''numeric_value_expression : term 
                            | numeric_value_expression OPSUM term
                            | numeric_value_expression OPMENOS term
    '''
    if (len(t)==2):
        t[0] = Nodo("numeric_value_expression", [t[1]],'N',None)

    elif (len(t) == 4):
        temp = list()
        temp.append(t[1])
        tempNode2 = Nodo("numeric_value_expression", [t[2]],'S',str(t[2]))
        temp.append(tempNode2)
        temp.append(t[3])
        t[0] = Nodo("numeric_value_expression", temp,'N',None)  


def p_term(t) :
    '''term : factor 
            | term MULT factor
            | term  OPDIV factor
    '''
    if (len(t)==2):
        t[0] = Nodo("term", [t[1]],'N',None)

    elif (len(t) == 4):
        temp = list()
        temp.append(t[1])
        tempNode2 = Nodo("term", [t[2]],'S',str(t[2]))
        temp.append(tempNode2)
        temp.append(t[3])
        t[0] = Nodo("term", temp,'N',None)  


def p_factor(t) :
    '''factor : numeric_primary 
            | OPSUM numeric_primary
            | OPMENOS numeric_primary
    '''
    if (len(t)==2):
        t[0] = Nodo("factor", [t[1]],'N',None)

    elif (len(t) == 3):
        temp = list()
        tempNode1 = Nodo("factor", [t[1]],'S',str(t[1]))
        temp.append(tempNode1)
        temp.append(t[2])
        t[0] = Nodo("factor", temp,'N',None)  

def p_numeric_primary(t) :
    '''numeric_primary : numeric_value_function
    '''
    t[0] = Nodo("numeric_primary", [t[1]],'N',None)  

def p_numeric_value_function(t) :
    '''numeric_value_function : extract_expression 
    '''
    t[0] = Nodo("numeric_value_function", [t[1]],'N',None)  

def p_extract_expression(t) :
    '''extract_expression : EXTRACT  PARIZQ extract_field FROM extract_source PARDER
    '''
    temp = list()
    temp.append(t[3])
    temp.append(t[5])
    t[0] = Nodo("extract_expression", temp,'N',None) 

def p_extract_field(t) :
    '''extract_field : datetime_field
    '''
    t[0] = Nodo("extract_field", [t[1]],'N',None) 


def p_datetime_field(t) :
    '''datetime_field : SECOND
            | YEAR
            | MONTH
            | DAY
            | HOUR
            | MINUTE
    '''
    t[0] = Nodo("datetime_field", [t[1]],'S',str(t[1]))         

def p_extract_source(t) :
    '''extract_source : datetime_value_expression 
                        | interval_value_expression
    '''
    t[0] = Nodo("extract_source", [t[1]],'N',None) 

def p_trim_function(t) :
    '''trim_function : TRIM  PARIZQ trim_operands PARDER
    '''
    t[3] = Nodo("trim_function", [t[3]],'N',None) 


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

#*************************************************
#**********************         Error           ***********
#*************************************************  

def p_error(t):
    global resultado_gramatica
    if t:
        #line_start = input.rfind('\n', 0, token.lexpos) + 1
        #return (token.lexpos - line_start) + 1        
        resultado = "Error sintactico de tipo {}, linea {}, posicion {}, en el valor {} ".format( str(t.type),str(t.lineno),str(t.lexpos),str(t.value[0]))
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
