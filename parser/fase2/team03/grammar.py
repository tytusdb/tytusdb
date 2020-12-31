from scanner import tokens
start = 'statements'
#start = 'expression'
precedence = (
    #Arthmetic
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIAGONAL'),
    ('left', 'EXPONENCIANCION'),    
    #logic
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
)
def p_statements(t):
    '''statements   : statements statement
                    | statement'''

def p_statement(t):
    '''statement    : stm_select PUNTOCOMA 
                    |    stm_insert PUNTOCOMA
                    |    stm_update PUNTOCOMA
                    |    stm_delete PUNTOCOMA
                    |    stm_create PUNTOCOMA
                    |    stm_alter  PUNTOCOMA
                    |    stm_drop   PUNTOCOMA
                    |    stm_show   PUNTOCOMA
                    |    stm_select UNION all_opt stm_select
                    |    stm_select INTERSECT all_opt stm_select
                    |    stm_select EXCEPT all_opt 
                    |    stm_use_db PUNTOCOMA
    '''

def p_all_opt(t):
    '''all_opt  : ALL
                | empty'''

def p_stm_select(t):
    '''stm_select : SELECT distinct_opt list_names FROM table_list where_clause_opt group_clause_opt having_clause_opt order_by_opt limit_opt offset_opt '''

def p_distinct_opt(t):
    '''distinct_opt : not_opt DISTINCT
                    | empty'''

def p_where_clause_opt(t):
    '''where_clause_opt : where_clause
                        | empty'''

def p_group_clause_opt(t):
    '''group_clause_opt : group_clause
                        | empty'''

def p_having_clause_opt(t):
    '''having_clause_opt    : having_clause
                    | empty'''

def p_order_by_opt(t):
    '''order_by_opt : ORDER BY col_name
                    | empty'''

def p_limit_opt(t):
    '''limit_opt    : LIMIT ENTERO
                    | empty'''

def p_offset_opt(t):
    '''offset_opt   : OFFSET ENTERO
                    | empty'''

def p_table(t):
    '''table    : ID AS TEXTO
                | ID
                | PARA stm_select PARC AS TEXTO
                | PARA stm_select PARC'''

def p_stm_insert(t):
    '''stm_insert   : INSERT INTO ID insert_ops'''

def p_insert_ops(t):
    '''insert_ops   : column_list_param_opt VALUES PARA exp_list PARC
                    |   column_list_param_opt stm_select'''

def p_table_list(t):
    '''table_list   : table_list COMA table_ref 
                    | table_ref'''

def p_table_ref(t):
    '''table_ref    : table NATURAL join_type JOIN table
                    | table join_type JOIN table
                    | table'''

def p_join_type(t):
    '''join_type    : INNER
                    |   outer_join_type OUTER
                    |   outer_join_type 
    '''
def p_outer_join_type(t):
    '''outer_join_type  : LEFT
                        | RIGHT
                        | FULL'''

def p_list_names(t):
    '''list_names   : list_names COMA names AS TEXTO
                    | list_names COMA names
                    | names AS TEXTO
                    | names'''

def p_names(t):
    '''names    : POR
                | expression
                | GREATEST PARA exp_list PARC
                | LEAST PARA exp_list PARC
                | case_clause
                | time_ops'''

def p_group_clause(t):
    '''group_clause : GROUP BY PARA group_list PARC
    '''

def p_group_list(t):
    '''group_list   : group_list COMA col_name
                    | col_name'''

def p_stm_show(t):
    '''stm_show : SHOW DATABASES LIKE TEXTO
                | SHOW DATABASES'''

def p_stm_use_db(t):
    '''stm_use_db   : USE DATBASE ID'''

def p_having_clause(t):
    '''having_clause    : HAVING logicExpression'''

def p_case_clause(t):
    '''case_clause  : CASE case_inner ELSE expression
                    | CASE case_inner'''

def p_case_inner(t):
    '''case_inner   : case_inner WHEN logicExpression THEN expression
                    | WHEN logicExpression THEN expression'''

def p_time_ops(t):
    '''time_ops : EXTRACT PARA ops_from_ts COMA TEXTO PARC
                |    DATE_PART PARA TEXTO COMA INTERVAL TEXTO PARC'''

def p_ops_from_ts(t):
    '''ops_from_ts  : YEAR FROM TIMESTAMP
                |    HOUR FROM TIMESTAMP
                |    MINUTE FROM TIMESTAMP
                |    SECOND FROM TIMESTAMP
                |    MONTH FROM TIMESTAMP
                |    DAY FROM TIMESTAMP
    '''

def p_column_list_param_opt(t):
    '''column_list_param_opt  : PARA column_list PARC
                                | empty'''    

def p_column_list(t):
    '''column_list  : column_list COMA ID
                    | ID'''

def p_stm_update(t):
    '''stm_update : UPDATE ID SET update_list where_clause
                    | UPDATE ID SET update_list'''

def p_update_list(t):
    '''update_list  : update_list COMA ID IGUAL logicExpression
                    | ID IGUAL logicExpression'''

def p_stm_delete(t):
    '''stm_delete   : DELETE FROM ID where_clause
                    | DELETE FROM ID'''
def p_where_clause(t):
    '''where_clause : WHERE predicateExpression'''

def p_stm_create(t):
    '''stm_create   : CREATE TYPE ID AS ENUM PARA exp_list PARC
                    | CREATE or_replace_opt DATABASE ID owner_opt mode_opt
                    | CREATE TABLE ID PARA tab_create_list PARC inherits_opt'''
def p_tab_create_list(t):
    '''tab_create_list  : tab_create_list COMA ID type nullable_opt primary_key_opt
                        | ID type nullable_opt primary_key_opt'''

def p_primary_key_opt(t):
    '''primary_key_opt  : PRIMARY KEY
                        | empty'''

def p_nullable(t):
    '''nullable : NULL
                | NOT NULL'''

def p_nullable_opt(t):
    '''nullable_opt  : nullable
                    | empty'''


def p_inherits_opt(t):
    '''inherits_opt : INHERITS PARA ID PARC
                    | empty'''

def p_owner_opt(t):
    '''owner_opt    : OWNER IGUAL TEXTO
                    | empty'''

def p_mode_opt(t):
    '''mode_opt     : MODE IGUAL ENTERO
                    | empty'''

def p_or_replace_opt(t):
    '''or_replace_opt   : OR REPLACE
                        | empty'''

def p_stm_alter(t):
    '''stm_alter    : ALTER DATABASE ID RENAME TO ID
                    |    ALTER DATABASE ID OWNER TO db_owner
                    |    ALTER TABLE ID ADD COLUMN ID type param_int_opt
                    |    ALTER TABLE ID ADD CHECK PARA logicExpression PARC
                    |    ALTER TABLE ID DROP COLUMN ID
                    |    ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARA ID PARC
                    |    ALTER TABLE ID ADD FOREIGN KEY PARA ID PARC REFERENCES ID 
                    |    ALTER TABLE ID ALTER COLUMN ID SET NOT NULL
                    |    ALTER TABLE ID DROP CONSTRAINT ID
                    |    ALTER TABLE ID RENAME COLUMN ID TO ID
                    |    ALTER TABLE ID ALTER COLUMN TYPE type param_int_opt'''

def p_param_int_opt(t):
    '''param_int_opt  : PARA ENTERO PARC
                | empty''' 

def p_exp_list(t):
    '''exp_list : exp_list COMA expression
                |    expression'''

def p_db_owner(t):
    ''' db_owner    : TEXTO
                    | CURRENT_USER
                    | SESSION_USER'''

def p_stm_drop(t):
    '''stm_drop : DROP DATABASE if_exists_opt ID
                |    DROP TABLE ID''' 

def p_if_exist_opt(t):
    '''if_exists_opt    : IF EXISTS
                        | empty'''

def p_expression(t):
    ''' expression  : expression MAS expression
                    | expression MENOS expression
                    | expression POR expression
                    | expression DIAGONAL expression
                    | expression PORCENTAJE expression
                    | expression EXPONENCIANCION expression
                    | ABS PARA expression PARC
                    | CBRT PARA expression PARC
                    | CEIL PARA expression PARC
                    | CEILING PARA expression PARC
                    | DEGREES PARA expression PARC
                    | DIV PARA expression COMA expression PARC
                    | EXP PARA expression  PARC    
                    | FACTORIAL PARA expression  PARC
                    | FLOOR PARA expression  PARC
                    | GCD PARA expression COMA expression PARC
                    | LCM PARA expression COMA expression PARC
                    | LN PARA expression PARC
                    | LOG PARA expression PARC
                    | LOG10 PARA expression PARC
                    | MIN_SCALE PARA expression PARC
                    | MOD PARA expression COMA expression PARC
                    | PI PARA PARC
                    | POWER PARA expression COMA expression PARC
                    | RADIANS PARA expression PARC
                    | RUND PARA expression PARC
                    | SCALE PARA expression PARC
                    | SIGN PARA expression PARC
                    | SQRT PARA expression PARC
                    | TRIM_SCALE PARA expression PARC
                    | TRUC PARA expression PARC
                    | WIDTH_BUCKET PARA expression COMA expression PARC
                    | RANDOM PARA PARC
                    | SETSEED PARA expression PARC
                    | ACOS PARA expression PARC
                    | ACOSD PARA expression PARC
                    | ASIN PARA expression PARC
                    | ASIND PARA expression PARC
                    | ATAN PARA expression PARC
                    | ATAND PARA expression PARC
                    | ATAN2 PARA expression COMA expression PARC
                    | ATAN2D PARA expression COMA expression PARC
                    | COS PARA expression PARC
                    | COSD PARA expression PARC
                    | COT PARA expression PARC
                    | COTD PARA expression PARC
                    | SIN PARA expression PARC
                    | SIND PARA expression PARC
                    | TAN PARA expression PARC
                    | TAND PARA expression PARC
                    | SINH PARA expression PARC
                    | COSH PARA expression PARC
                    | TANH PARA expression PARC
                    | ASINH PARA expression PARC
                    | ACOSH PARA expression PARC
                    | ATANH PARA expression PARC
                    | NOT expression 
                    | MAS expression 
                    | MENOS expression
                    | TEXTO
                    | col_name
                    | TRUE
                    | FALSE
                    | numero
                    | NOW PARA PARC
                    | PARA logicExpression PARC'''

def p_predicateExpression(t):
    '''predicateExpression  : BETWEEN expression AND expression
                            | expression IS NULL
                            | expression IS NOT NULL
                            | expression IS not_opt DISTINCT FROM expression
                            | expression IS not_opt TRUE expression
                            | expression IS not_opt FALSE expression
                            | expression IS not_opt UNKNOWN expression
                            | logicExpression'''

def p_logicExpression(t):
    '''logicExpression  : relExpression AND relExpression
                        | relExpression OR  relExpression
                        | NOT relExpression
                        | relExpression '''

def p_relExpression(t):
    '''relExpression    : expression MENOR expression 
                        | expression MAYOR  expression
                        | expression IGUAL  expression
                        | expression MENORQ expression
                        | expression MAYORQ expression
                        | expression DIFERENTE expression
                        | expression NOT LIKE TEXTO
                        | expression LIKE TEXTO
                        | expression'''
def p_not_opt(t):
    '''not_opt       : NOT
                    | empty'''

def p_percentopt(t):
    '''percentopt   : PORCENTAJE
                    | empty'''

def p_type(t):
    ''' type    : SMALLINT
                | INTEGER                
                | BIGINT
                | DECIMAL
                | NUMERIC
                | REAL
                | DOUBLE PRECISION
                | MONEY
                | CARACTER VARYING
                | VARCHAR
                | CHARACTER
                | CHAR
                | TEXT
                | TIMESTAMP
                | DATE
                | TIME
                | INTERVAL
                | BOOLEAN'''

def p_time(t):
    ''' time    : YEAR
                | MONTH
                | DAY
                | HOUR
                | MINUTE
                | SECOND'''

def p_numero(t):
    ''' numero  : ENTERO
                | FLOAT'''

def p_col_name(t):
    ''' col_name : ID PUNTO ID
                | ID '''

def p_empty(t):
    '''empty :'''
    pass

def p_error(p):
    pass

import ply.yacc as yacc
parse = yacc.yacc()

def toParse(input):
    return parse.parse(input)