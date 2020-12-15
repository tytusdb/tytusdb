def p_empty(p):
     'empty :'
     pass

def p_error(t):
    print(t)
    print("Error sintáctico, símbolo: %s",t.value)

def p_queriesLista(t):
    'queries : queries query'
    t[1].append(t[2])
    t[0] = t[1]

def p_queriesSingle(t):
    'queries : query'
    t[0] = [t[1]]

def p_query(t):
    'query : queryp com PUNTOCOMA'
    #por el momento
    t[0] = t[1] 

def p_com(t):
    ''' 
    com : union query 
        | intersect query
        | except query
        | empty
    '''

def p_queryP(t):
    'queryp : SELECT distinct select_list FROM table_expression condition group having order lim off  '
    t[0] =  select(t[2],t[3],t[5],t[6],t[7],t[8],t[9],t[10],t[11])

def p_distinct(t):
    'distinct : DISTINCT'
    t[0] = True

def p_distinctEmpty(t):
    'distinct : empty'
    t[0] = False

def p_select_listAll(t):
    'select_list : MULTIPLICACION'
    t[0] = ['All']

def p_select_listList(t):
    'select_list : list'
    t[0] = t[1]

def p_list(t):
    'list : list COMA column aliascol'



def p_listSingle(t):
    'list: column aliascol'

def p_column(t):
    'column : ID columnp '

def p_columnFunc(t):
    '''
    column : trig
            | math
            | function

    '''

def p_TRIG(t):
    '''
        trig : ACOS PARA exp PARC
		| ACOSD PARA exp PARC
		| ASIN PARA exp PARC
		| ASIND PARA exp PARC
		| ATAN PARA exp PARC
		| ATAND PARA exp PARC
		| ATAN2 PARA exp COMA exp PARC
		| ATAN2D PARA exp COMA exp PARC
		| COS PARA exp PARC
		| COSD PARA exp PARC
		| COT PARA exp PARC
		| COTD PARA exp PARC
		| SIN PARA exp PARC
		| SIND PARA exp PARC
		| TAN PARA exp PARC
		| TAND PARA exp PARC
		| SINH PARA exp PARC
		| COSH PARA exp PARC 
		| TANH PARA exp PARC
		| ASINH PARA exp PARC
		| ACOSH PARA exp PARC
		| ATANH PARA exp PARC
    '''

def p_math(t):
    '''
    math : abs PARA  exp PARC
		| cbrt PARA  exp PARC
		| ceil PARA  exp PARC
		| ceiling PARA  exp PARC
		| degrees PARA  exp PARC
		| div PARA  exp COMA exp PARC	
		| exp PARA  exp PARC	
		| factorial PARA  exp PARC
		| floor PARA  exp PARC
		| gcd PARA  exp COMA exp PARC
		| lcm PARA  exp COMA exp PARC
		| ln PARA  exp PARC
		| log PARA  exp COMA exp PARC
		| log10 PARA  exp PARC
		| min_scale PARA exp PARC
		| mod PARA exp COMA exp PARC
		| pi PARA PARC
		| power PARA  exp COMA exp PARC
		| radians PARA  exp PARC
		| round PARA  exp PARC
		| scale PARA  exp PARC
		| sign PARA  exp PARC
		| sqrt PARA  exp PARC
		| trim_scale PARA exp PARC
		| trunc PARA  exp PARC 
		| width_bucket PARA  exp COMA exp COMA exp COMA exp PARC
		| random PARA PARC
		| setseed PARA  exp PARC    

    '''
def p_function(t):
    '''
        function : SUM PARA exp PARC
                | AVG PARA exp PARC
                | MAX PARA exp PARC
                | MIN PARA exp PARC
                | COUNT PARA exp PARC
                | LENGTH PARA exp PARC
                | SUBSTRING PARA exp COMA INT COMA INT PARC
                | TRIM PARA exp PARC
                | MD5 PARA exp PARC
                | SHA256 PARA exp PARC
                | SUBSTR PARA exp COMA INT COMA INT PARC
                | CONVERT PARA exp AS type PARC
                | GREATEST PARA LEXPS PARC
                | LEAST PARA LEXPS PARC

    '''

def p_lexps(t):
    'lexps : lexps , exp'

def p_lexpsSingle(t):
    'lexps : exp '

def p_columnp(t):
    'columnp : PUNTO ID'

def p_columnpEmpty(t):
    'columnp : empty'
    t[0] = None

def p_aliascol(t):
    'aliascol : AS ID'

def p_aliascolEmpty(t):
    'aliascol : empty'
    t[0] = None

def p_table_expression(t):
    'table_expression : ID aliastable tep'

def p_table_expressionQuery(t):
    'table_expression : PARA query PARC tep'


def p_table_expressionCase(t):
    'table_expression : CASEHWEN tep'

def p_tep(t):
    'tep : COMA table_expression '

def p_aliastable(t):
    'aliastable : ID'

def p_aliastableEmpty(t):
    'alistable : empty'

def p_tepEmpty(t):
    'tep : empty'
    t[0] = None

def p_casewhen(t):
    'casewhen : CASE WHEN exp_case THEN exp casos else END alias'
    t[0] = casewhen( t[3], t[5], t[6], t[7], t[8])

def p_exp_case(t):
    'exp_case : exp oper exp'
    if t[2] == '='  : t[0] = exp_igual(t[1],t[3])
    elif t[2] == '>': t[0] = exp_mayor(t[1], t[3])
    elif t[2] == '<': t[0] = exp_menor(t[1], t[3])
    elif t[2] == '<>': t[0] = exp_diferente(t[1], t[3])
    elif t[2] == '>=': t[0] = exp_mayor_igual(t[1], t[3])
    elif t[2] == '<=': t[0] = exp_menor_igual(t[1], t[3])
    


def p_expcaseIn(t):
    'exp_case : exp IN PARA query PARC'
    t[0] = exp_in(t[1],t[4])

def p_expcaseNotIn(t):
    'exp_case : exp NOT IN PARA query PARC'
    t[0] = exp_not_in(t[1],t[5])

def p_expcaseBetween(t):
    'exp_case: exp between exp AND exp'
    t[0] = exp_between(t[1],t[3],t[5])


def p_expSingle(t):
    '''exp : INT
            | DEC
            | VARCHAR
            | FALSE
            | TRUE
            | ID columnp
    
    ''' 
    if t[1] == 'ID' : 
        if t[2] == None : t[0] = t[1] 
        else: t[0] = exp_id(t[2],t[1])
    else: 
        t[0] = t[1]



def p_expCombined(t):
    ''' exp : exp MAS exp
            | exp MENOS exp
            | exp MULTIPLICACION exp
            | exp DIVISION exp 
            | PARA exp PARC

    '''
    if t[1] == '(' : 
        t[0] = t[2]
    else:
        if t[2] == '+'  : t[0] = exp_suma(t[1],t[3])
        elif t[2] == '-': t[0] = exp_resta(t[1], t[3])
        elif t[2] == '*': t[0] = exp_multiplicacion(t[1], t[3])
        elif t[2] == '/': t[0] = exp_division(t[1], t[3])




def p_oper(t):
    ''' oper : IGUAL
            | MAYOR
            | MENOR
            | MAYOR_IGUAL   
            | MENOR_IGUAL
            | DIFERENTE
    '''
    t[0]=t[1]

def p_lcases(t):
    '''casos : lcases
    '''
    t[0] = t[1]
    
def p_lcases(t):
    '''casos :  empty             
    '''
    t[0] = None

def p_lista_cases(t):
    'lcases : lcases WHEN exp_case THEN exp '
    t[2] = case(t[3],t[5])
    t[1].append(t[2])
    t[0] = t[1]


def p_lcases_empty(t):
    'lcases :  WHEN exp_case THEN exp '
    t[0] =  [case(t[2],t[4])]

def p_else(t):
    'else : ELSE  exp '

def p_elseEmpty(t):
    'else : empty'
    t[0] = None

def p_alias(t):
    'alias : id '

def p_aliasEmpty(t):
    'alias : empty'
    t[0] = None

def p_condition(t):
    'condition : WHERE lconditions  '
    t[0]=t[2]

def p_lconditions(t):
    'lconditions : lconditions ANDOR exp_case'
    t[3] = condition(t[3],t[2])
    t[1].append(t[3])
    t[0] = t[1]


def p_lconditionsSingle(t):
    'lconditions : exp_case'
    t[0]= [condition(t[1],None)]

def p_andor(t):
    '''
    andor: AND
        | OR
    '''
    t[0] = t[1]

def p_conditionEmpty(t):
    'condition : empty'

def p_groupby(t):
    'group : GROUP BY LIDS'

def p_groupbyEmpty(t):
    'group : empty'

def p_lids(t):
    'lids : lids ID columnp'

def p_lids(t):
    'lids: ID aliascol'

def p_having(t):
    'having : HAVING exp_case '

def p_havingEmpty(t):
    'having : empty'

def p_orderby(t):
    'order : ORDER BY ID columnp ascdsc'

def p_orderby(t):
    'order : empty'

def p_ascdsc(t):
    '''ascdsc : ASC
                | DESC
    
    '''

def p_lim(t):
    'lim : LIMIT INT'

def p_limit(t):
    'lim : empty'

def p_offset(t):
    'off : OFFSET INT'

def p_offsetEmpty(t):
    'off : empty'