import ply.yacc as yacc
# Construccion del analizador léxico
import ply.lex as lex
from tokens import *
lexer = lex.lex()
# Asociación de operadores y precedencia
listInst = []
repGrammar = []
precedence = (
    ("left", "R_UNION", "R_INTERSECT", "R_EXCEPT"),
    ("right", "R_NOT"),
    ("left", "R_AND", "R_OR"),
    (
        "left",
        "R_BETWEEN",
        "R_IS",
    ),
    (
        "left",
        "S_IGUAL",
        "OL_DISTINTODE",
        "OL_MAYORQUE",
        "OL_MENORQUE",
        "OL_MAYORIGUALQUE",
        "OL_MENORIGUALQUE",
    ),
    ("left", "OC_CONCATENAR"),
    ("left", "O_SUMA", "O_RESTA"),
    ("left", "O_PRODUCTO", "O_DIVISION", "O_MODULAR"),
    ("right", "UO_SUMA", "UO_RESTA"),
    ("left", "O_EXPONENTE"),
)

# Definición de la gramática

#block

def p_init(t):
    """block :  declaration_stmt R_BEGIN block_stmts exception R_END label S_PUNTOCOMA"""

#declaration

def p_declaration_stmt(t):
    """declaration_stmt : label_stmt R_DECLARE global_variable_declaration
        |   """

def p_global_variable_declaration(t):
    """global_variable_declaration : declaration 
                                    | global_variable_declaration declaration"""

def p_global_vd(t):
    """declaration : ID constant types_d assignment S_PUNTOCOMA
        | ID R_ALIAS R_FOR S_DOLAR INTEGER S_PUNTOCOMA
        | ID R_RECORD S_PUNTOCOMA
        | ID R_ALIAS R_FOR ID S_PUNTOCOMA"""

def p_constant(t):
    """constant : R_CONSTANT
        |"""

def p_assignment(t):
    """assignment : assignment_operator_D datatype_d
        |"""
def p_assignment_operator_D(t):
    """assignment_operator_D : R_DEFAULT
        | O_ASIGNACION
        | OL_ESIGUAL"""

def p_label_stmt(t):
    """label_stmt : OC_SHIFTL ID OC_SHIFTR
                | """

def p_label(t):
    """label : ID
    |"""

#typedeclaration

def p_types_d(t):
    """
    types_d :  ID
    """

def p_types_d_simple(t):
    """
    types_d : T_SMALLINT
    | T_INTEGER
    | T_BIGINT
    | T_REAL
    | T_DOUBLE T_PRECISION
    | T_MONEY
    | T_TEXT
    | T_BOOLEAN
    | R_TIMESTAMP
    | T_DATE
    | T_TIME
    """

def p_types_d_params(t):
    """
    types_d : T_DECIMAL optParams
    | T_NUMERIC optParams
    | T_VARCHAR optParams
    | T_CHARACTER optParams
    | T_CHAR optParams
    """

def p_typesvar(t):
    """
    types_d : T_CHARACTER T_VARYING optParams
    """
    
def p_timeType_interval_d(t):
    """
    types_d : R_INTERVAL intervalFields
    """

def p_vartype(t):
    """types_d :  ID O_MODULAR R_TYPE"""

def p_columntype(t):
    """types_d :  ID S_PUNTO ID O_MODULAR R_TYPE"""

def p_rowtypes(t):
    """types_d :  ID O_MODULAR R_ROWTYPE """


#datatype
 
def p_datatype_operadores_binarios1_d(t):
    """
    datatype_d : datatype_d O_SUMA datatype_d
    | datatype_d O_RESTA datatype_d
    | datatype_d O_PRODUCTO datatype_d
    | datatype_d O_DIVISION datatype_d
    | datatype_d O_EXPONENTE datatype_d
    | datatype_d O_MODULAR datatype_d
    """

def p_datatype_operadores_binarios2_d(t):
    """
    datatype_d : datatype_d OC_CONCATENAR datatype
    """

def p_datatype_operadores_unarios_d(t):
    """
    datatype_d : O_RESTA datatype_d %prec UO_RESTA
    | O_SUMA datatype_d %prec UO_SUMA
    """

def p_datatype_operandos_d(t):
    """
    datatype_d : literal_d
    | funcCall
    | extract
    | datePart
    | current
    | parameter
    """

def p_datatype_agrupacion_d(t):
    """
    datatype_d : S_PARIZQ datatype_d S_PARDER
    """

def p_literal_d(t):
    """
    literal_d :  INTEGER
    | STRING
    | DECIMAL
    | CHARACTER
    | R_TRUE
    | R_FALSE
    | ID
    """

#block stmts

def p_block_stmts(t):
    """block_stmts : block_stmts block_stmt """

def p_empty(t):
    """block_stmts :
    exception :"""

def p_block_stmt(t):
    """block_stmt : local_variable_declaration
                | statement
                | stmt"""

#Control Structures

def p_statement(t):
    """statement : if_stmt
        | loop_stmt
        | while_stmt
        | for_stmt_int
        | for_stmt_query
        | case_stmt
        | stmt_without_substmt"""

def p_stmt_without_substmt(t):
    """stmt_without_substmt : R_NULL S_PUNTOCOMA
        | R_RETURN return_stmt
        | R_EXIT exit_stmt
        | R_CONTINUE continue_stmt
        | query_single_row
        """



#local variable declaration

def p_local_variable_declaration(t):
    """local_variable_declaration : ID assignment_operator datatype S_PUNTOCOMA"""

def p_assignment_operator(t):
    """assignment_operator : O_ASIGNACION
        | S_IGUAL"""

#return

def p_return_stmt(t):
    """return_stmt : expresion S_PUNTOCOMA
                | R_NEXT expresion S_PUNTOCOMA
                | R_QUERY  selectStmt S_PUNTOCOMA
                | S_PUNTOCOMA
                | R_QUERY execute_return S_PUNTOCOMA"""



#CONDITIONALS IF, CASE
#IF
def p_if_stmt(t):
    """if_stmt : R_IF expBool R_THEN block_stmts elseif_stmts else_stmt_opt R_END R_IF S_PUNTOCOMA"""

def p_else_stmt(t):
    """elseif_stmts : elseif_stmts elseif_stmt"""

def p_elseif_stmt(t):
    """elseif_stmt :  R_ELSEIF expBool R_THEN block_stmts"""

def p_else_stmt_opt(t):
    """else_stmt_opt : R_ELSE block_stmts"""

def p_else_empty_stmt(t):
    """elseif_stmts :
        else_stmt_opt :"""

#CASE
def p_case_stmt(t):
    """case_stmt : case_stmt_n
        | case_stmt_bool"""

def p_case_stmt_n(t):
    """case_stmt_n : R_CASE ID R_WHEN list_expression R_THEN block_stmts else_case_stmt_n else_stmt_opt R_END R_CASE S_PUNTOCOMA"""

def p_else_case_stmt_n(t):
    """else_case_stmt_n : else_case_stmt_n R_WHEN list_expression R_THEN block_stmts 
    | R_WHEN list_expression R_THEN block_stmts  
    |"""

def p_case_stmt_bool(t):
    """case_stmt_bool : R_CASE R_WHEN expBool R_THEN block_stmts else_case_stmt_bool else_stmt_opt R_END R_CASE S_PUNTOCOMA"""

def p_else_case_stmt_bool(t):
    """else_case_stmt_bool : else_case_stmt_bool  R_WHEN expBool R_THEN block_stmts  
                        |  R_WHEN expBool R_THEN block_stmts 
                        |"""

def p_list_expression(t):
    """list_expression : exp1
        | list_expression S_COMA exp1"""

def p_exp1(t):
    """exp1 : INTEGER
    | STRING
    | DECIMAL
    | CHARACTER
    | R_TRUE
    | R_FALSE"""

#LOOPS 

#loop

def p_loop_stmt(t):
    """loop_stmt : label_stmt R_LOOP block_stmts R_END R_LOOP label S_PUNTOCOMA"""


#exit
def p_exit_stmt(t):
    """exit_stmt : S_PUNTOCOMA
        | label R_WHEN expBool S_PUNTOCOMA"""

#continue

def p_continue_stmt(t):
    """continue_stmt : S_PUNTOCOMA
        | label R_WHEN expBool S_PUNTOCOMA"""

#while

def p_while_stmt(t):
    """while_stmt : label_stmt R_WHILE expBool R_LOOP block_stmts R_END R_LOOP label S_PUNTOCOMA"""

#for integer variant
def p_for_stmt_int(t):
    """for_stmt_int : label_stmt R_FOR ID R_IN reverse INTEGER S_DOSPUNTOS INTEGER by_stmt R_LOOP block_stmts R_END R_LOOP label S_PUNTOCOMA"""

def p_reverse(t):
    """reverse : R_REVERSE
        |"""

def p_by_stmt(t):
    """by_stmt : R_BY INTEGER
        |"""

#for query result
def p_for_stmt_query(t):
    """for_stmt_query : label_stmt R_FOR ID R_IN selectStmt R_LOOP block_stmts R_END R_LOOP label S_PUNTOCOMA"""





#EXECUTE QUERY SINGLE ROW

def p_query_single_row(t):
    """query_single_row : insertStmt_SR S_PUNTOCOMA
    | updateStmt_SR S_PUNTOCOMA
    | deleteStmt_SR S_PUNTOCOMA
    | selectStmt_SR S_PUNTOCOMA
    | perform S_PUNTOCOMA
    | execute S_PUNTOCOMA
    | get S_PUNTOCOMA"""

#insert

def p_insertStmt_single_row(t):
    """insertStmt_SR : R_INSERT R_INTO ID paramsColumn R_VALUES S_PARIZQ paramsList S_PARDER R_RETURNING returnParams  R_INTO strict ID """


#update

def p_updateStmt_single_row(t):
    """updateStmt_SR : R_UPDATE fromBody R_SET updateCols whereCl R_RETURNING returnParams R_INTO strict ID """

   

#delete

def p_deleteStmt_single_row(t):
    """deleteStmt_SR : R_DELETE fromCl whereCl R_RETURNING returnParams R_INTO strict ID """

#select
def p_selectStmt_single_row_1(t):
    """selectStmt_SR : R_SELECT R_DISTINCT selectParams R_INTO strict ID fromCl whereCl groupByCl limitCl """



def p_selectStmt_single_row_2(t):
    """selectStmt_SR : R_SELECT selectParams R_INTO strict ID fromCl whereCl groupByCl limitCl"""


def p_selectStmt__single_row_1(t):
    """selectStmt_SR : R_SELECT selectParams R_INTO strict ID fromCl joinList whereCl groupByCl orderByCl limitCl"""
   


def p_selectStmt__single_row_2(t):
    """selectStmt_SR : R_SELECT selectParams R_INTO strict ID fromCl whereCl groupByCl orderByCl limitCl"""
   


def p_selectStmt__single_row_3(t):
    """selectStmt_SR : R_SELECT selectParams R_INTO strict ID fromCl joinList whereCl groupByCl limitCl"""
    


def p_selectStmt_union_single_row(t):
    """selectStmt_SR : selectStmt_SR R_UNION allOpt selectStmt_SR"""
    


def p_selectStmt_intersect_single_row(t):
    """selectStmt_SR : selectStmt_SR R_INTERSECT allOpt selectStmt_SR"""
    


def p_selectStmt_except_single_row(t):
    """selectStmt_SR : selectStmt_SR R_EXCEPT allOpt selectStmt_SR"""
    


def p_selectStmt_agrupacion_single_row(t):
    """selectStmt_SR : S_PARIZQ selectStmt_SR S_PARDER"""
    

def p_selectstmt_only_params_single_row(t):
    """selectStmt_SR : R_SELECT selectParams R_INTO strict ID"""
   

#strict

def p_strict(t):
    """strict : R_STRICT
    |"""

#returnParams
def p_returnparams_all(t):
    """returnParams : O_PRODUCTO"""


def p_returnparams_params(t):
    """returnParams : returnlist"""


# En caso de errores cambiar returnlistParams -> expresion
def p_returnlist_list(t):
    """returnlist : returnlist S_COMA returnlistParams optAlias"""


# En caso de errores cambiar returnlistParams -> expresion
def p_returnlist_u(t):
    """returnlist : returnlistParams optAlias"""


def p_returnlistParams_1(t):
    """returnlistParams : expresion"""
   

def p_returnlistParams_2(t):
    """returnlistParams : ID S_PUNTO O_PRODUCTO"""
    



#PERFORM

def p_perform(t):
    """perform : R_PERFORM STRING """

#EXECUTE

def p_execute_return(t):
    """execute_return : R_EXECUTE exp_string  using  """

def p_execute(t):
    """execute : R_EXECUTE exp_string into_strict using """

def p_into_strict(t):
    """into_strict : R_INTO strict ID
    |"""

def p_using(t):
    """using : R_USING list_expression_2
    |"""

def p_list_expression_2(t):
    """list_expression_2 : ID
                        | list_expression_2 S_COMA ID"""

def p_exp_string(t):
    """exp_string : id_or_string 
                | exp_string OC_CONCATENAR id_or_string"""

def p_exp_string_id(t):
    """id_or_string : STRING
    | ID 
    | funcCall"""

#GET 

def p_get(t):
    """get : R_GET current R_DIAGNOSTIC ID assignment_operator item """

def p_current_g(t):
    """current : R_CURRENT
    |"""

def p_item(t):
    """item : R_ROW_COUNT"""

#EXCEPTION

def p_exception(t):
    """exception : R_EXCEPTION when_stmt R_END S_PUNTOCOMA """

def p_while_stmt_exp(t):
    """when_stmt : R_WHEN expBoolOR R_THEN handler_statements
    | when_stmt R_WHEN expBoolOR R_THEN handler_statements  """

def p_expBoolOR(t):
    """expBoolOR : ID
                | expBoolOR OC_OR ID  """

def p_handler_statements(t):
    """handler_statements : handler_statements handler_statement """

def p_empty_handler_stmt(t):
    """handler_statements :"""

def p_handler_statement(t):
    """handler_statement : R_RAISE R_NOTICE STRING S_PUNTOCOMA
    | R_RETURN return_stmt  
    | R_NULL S_PUNTOCOMA"""

#gramatica actual

   


def p_stmt_list(t):
    """stmtList : stmtList stmt"""

    


def p_stmt_u(t):
    """stmtList : stmt"""

    


def p_stmt(t):
    """
    stmt : createStmt  S_PUNTOCOMA
        | showStmt S_PUNTOCOMA
        | alterStmt S_PUNTOCOMA
        | dropStmt S_PUNTOCOMA
        | insertStmt S_PUNTOCOMA
        | updateStmt S_PUNTOCOMA
        | deleteStmt S_PUNTOCOMA
        | truncateStmt S_PUNTOCOMA
        | useStmt S_PUNTOCOMA
        | selectStmt S_PUNTOCOMA
    """

    


# Statement para el CREATE
# region CREATE
def p_id_string(t):
    """
    idOrString : ID
    | STRING
    | CHARACTER
    """

    


def p_createstmt(t):
    """createStmt : R_CREATE createBody"""

    


def p_createbody(t):
    """
    createBody : createOpts
    """

    


def p_createopts_table(t):
    """createOpts : R_TABLE ifNotExists idOrString S_PARIZQ createTableList S_PARDER inheritsOpt """
 
    


def p_createopts_db(t):
    """
    createOpts : orReplace R_DATABASE ifNotExists idOrString createOwner createMode
    """
   
def p_createopts_index(t):
    """
    createOpts : indexUnique R_INDEX ID R_ON ID usingHash S_PARIZQ indexList S_PARDER whereCl
    """
  
def p_indexList(t):
    """
    indexList : indexList S_COMA ID indexOrder indexNull firstLast 
    """

def p_indexList2(t):
    """
    indexList : ID indexOrder indexNull firstLast 
    """
    

def p_usingHash(t):
    """
    usingHash : R_USING R_HASH
    |
    """


def p_indexOrder(t):
    """
    indexOrder : R_DESC
    | R_ASC
    |
    """


def p_indexNull(t):
    """
    indexNull : R_NULL
    |
    """


def p_indexFirstLast(t):
    """
    firstLast : R_FIRST
    | R_LAST
    |
    """

def p_createindex_unique(t):
    """
    indexUnique : R_UNIQUE
    |
    """




def p_replace_true(t):
    """
    orReplace : R_OR R_REPLACE
    """
   
    


def p_replace_false(t):
    """
    orReplace :
    """
  
    


def p_createopts_type(t):
    """
    createOpts : R_TYPE ifNotExists ID R_AS R_ENUM S_PARIZQ paramsList S_PARDER
    """
    
    


def p_ifnotexists_true(t):
    """
    ifNotExists : R_IF R_NOT R_EXISTS
    """
 
    


def p_ifnotexists_false(t):
    """
    ifNotExists :
    """
 
    


def p_inheritsOpt(t):
    """
    inheritsOpt : R_INHERITS S_PARIZQ ID S_PARDER
    """

    


def p_inheritsOpt_none(t):
    """
    inheritsOpt :
    """
 
    


def p_createowner(t):
    """
    createOwner : R_OWNER ID
    | R_OWNER STRING
    """

    


def p_createowner_asg(t):
    """
    createOwner :  R_OWNER S_IGUAL ID
    | R_OWNER S_IGUAL STRING
    """
 
    


def p_createowner_none(t):
    """
    createOwner :
    """
 
    


def p_createmode(t):
    """
    createMode : R_MODE INTEGER
    """

    


def p_createMode_asg(t):
    """
    createMode : R_MODE S_IGUAL INTEGER
    """

    


def p_createmode_none(t):
    """
    createMode :
    """

    


def p_createtable_list(t):
    """createTableList : createTableList S_COMA createTable"""

    


def p_createtable_u(t):
    """createTableList :  createTable"""

    


def p_createTable_id(t):
    """
    createTable :  ID types createColumns
    """

    


def p_createTable(t):
    """
    createTable : createConstraint
    | createUnique
    | createPrimary
    | createForeign
    """

    


def p_createColumNs(t):
    """
    createColumns : colOptionsList
    """

    


def p_createColumNs_none(t):
    """
    createColumns :
    """

    


def p_createConstraint(t):
    """createConstraint : constrName R_CHECK S_PARIZQ booleanCheck S_PARDER"""

    


def p_createUnique(t):
    """createUnique : R_UNIQUE S_PARIZQ idList S_PARDER"""

    


def p_createPrimary(t):
    """createPrimary : R_PRIMARY R_KEY S_PARIZQ idList S_PARDER"""

    


def p_createForeign(t):
    """
    createForeign : constrName R_FOREIGN R_KEY S_PARIZQ idList S_PARDER R_REFERENCES ID S_PARIZQ idList S_PARDER
    """

    


def p_constrName(t):
    """
    constrName : R_CONSTRAINT ID
    """

    


def p_constrName_none(t):
    """
    constrName :
    """

    


def p_id_list(t):
    """idList : idList S_COMA ID"""

    


def p_id_u(t):
    """idList : ID"""

    


def p_types(t):
    """
    types :  ID
    """

    


def p_types_simple(t):
    """
    types : T_SMALLINT
    | T_INTEGER
    | T_BIGINT
    | T_REAL
    | T_DOUBLE T_PRECISION
    | T_MONEY
    | T_TEXT
    | T_BOOLEAN
    | R_TIMESTAMP
    | T_DATE
    | T_TIME
    """

def p_types_params(t):
    """
    types : T_DECIMAL optParams
    | T_NUMERIC optParams
    | T_VARCHAR optParams
    | T_CHARACTER optParams
    | T_CHAR optParams
    """

    


def p_types_var(t):
    """
    types : T_CHARACTER T_VARYING optParams
    """

    


def p_timeType_interval(t):
    """
    types : R_INTERVAL intervalFields
    """
 
    


def p_intervalFields(t):
    """
    intervalFields :  R_YEAR
    | R_MONTH
    | R_DAY
    | R_HOUR
    | R_MINUTE
    | R_SECOND
    """



def p_intervalFields_none(t):
    """
    intervalFields :
    """

    


def p_optParams(t):
    """optParams : S_PARIZQ literalList S_PARDER"""

    


def p_optParams_none(t):
    """optParams : """

    


def p_colOptions_list(t):
    """colOptionsList : colOptionsList colOptions"""

    


def p_colOptions_u(t):
    """colOptionsList : colOptions"""

    


def p_colOptions(t):
    """
    colOptions : defaultVal
    | nullOpt
    | constraintOpt
    | primaryOpt
    | referencesOpt
    """

    


# cambiar literal
def p_defaultVal(t):
    """defaultVal : R_DEFAULT literal"""
    


def p_nullOpt_true(t):
    """
    nullOpt : R_NOT R_NULL
    """
   
    


def p_nullOpt_false(t):
    """
    nullOpt : R_NULL
    """
   
    


# cambiar literal


def p_constraintOpt_unique(t):
    """
    constraintOpt : constrName R_UNIQUE
    """
    
    


def p_constraintOpt_check(t):
    """
    constraintOpt : constrName R_CHECK S_PARIZQ booleanCheck S_PARDER
    """
    
    


def p_primaryOpt(t):
    """primaryOpt : R_PRIMARY R_KEY"""
   
    


def p_referencesOpt(t):
    """referencesOpt : R_REFERENCES ID"""
    
    


# endregion CREATE

# Gramatica para expresiones

# region Expresiones
def p_expresion(t):
    """
    expresion : datatype
            | expBool
    """
    t[0] = t[1]
    


def p_expresion_(t):
    """
    expresion : S_PARIZQ selectStmt S_PARDER
    """
    t[0] = t[2]
    


def p_funcCall_1(t):
    """
    funcCall : ID S_PARIZQ paramsList S_PARDER
    """
    


def p_funcCall_2(t):
    """
    funcCall : ID S_PARIZQ S_PARDER
            | R_NOW S_PARIZQ S_PARDER
    """
    
    


def p_funcCall_3(t):
    """
    funcCall : R_COUNT S_PARIZQ datatype S_PARDER
            | R_COUNT S_PARIZQ O_PRODUCTO S_PARDER
            | R_SUM S_PARIZQ datatype S_PARDER
            | R_PROM S_PARIZQ datatype S_PARDER
    """
    
    


def p_extract_1(t):
    """
    extract : R_EXTRACT S_PARIZQ optsExtract R_FROM timeStamp S_PARDER
    """
    

    


def p_extract_2(t):
    """
    extract : R_EXTRACT S_PARIZQ optsExtract R_FROM columnName S_PARDER
    """
   
    


def p_timeStamp(t):
    """
    timeStamp : R_TIMESTAMP STRING
          | R_INTERVAL STRING
    """
    


def p_optsExtract(t):
    """
    optsExtract : R_YEAR
                  | R_MONTH
                  | R_DAY
                  | R_HOUR
                  | R_MINUTE
                  | R_SECOND
    """
  
    


def p_datePart(t):
    """
    datePart : R_DATE_PART S_PARIZQ STRING S_COMA dateSource S_PARDER
    """
    
    


def p_dateSource(t):
    """
    dateSource : R_TIMESTAMP STRING
          | T_DATE STRING
          | T_TIME STRING
          | R_INTERVAL STRING
          | R_NOW S_PARIZQ S_PARDER
    """
    t[0] = [t[1], t[2]]
    


def p_current(t):
    """
    current : R_CURRENT_DATE
          | R_CURRENT_TIME
    """
   

    


def p_current_1(t):
    """
    current : timeStamp
    """
    
    


def p_literal_list(t):
    """literalList : literalList S_COMA literal"""
   
    


def p_literal_u(t):
    """literalList : literal"""

    


def p_literal(t):
    """
    literal :  INTEGER
    | STRING
    | DECIMAL
    | CHARACTER
    | R_TRUE
    | R_FALSE
    | R_NULL
    """


    


def p_params_list(t):
    """paramsList : paramsList S_COMA datatype"""
   
    


def p_params_u(t):
    """paramsList : datatype"""
   
    


def p_datatype_operadores_binarios1(t):
    """
    datatype : datatype O_SUMA datatype
    | datatype O_RESTA datatype
    | datatype O_PRODUCTO datatype
    | datatype O_DIVISION datatype
    | datatype O_EXPONENTE datatype
    | datatype O_MODULAR datatype
    """
    

    


def p_datatype_operadores_binarios2(t):
    """
    datatype : datatype OC_CONCATENAR datatype
    """
    


def p_datatype_case_when(t):
    """
    datatype : R_CASE caseList optElse R_END
    """


def p_case_list(t):
    """
    caseList : caseList caseWhen
            | caseWhen
    """


def p_caseWhen(t):
    """caseWhen : R_WHEN expBool R_THEN literal"""


def p_caseWhen_2(t):
    """optElse : R_ELSE literal
    |
    """


def p_datatype_operadores_unarios(t):
    """
    datatype : O_RESTA datatype %prec UO_RESTA
    | O_SUMA datatype %prec UO_SUMA
    """
   
    


def p_datatype_operandos(t):
    """
    datatype : columnName
    | literal
    | funcCall
    | extract
    | datePart
    | current
    | parameter
    """
 
def p_datatype_parameter(t):
     """parameter :  S_DOLAR INTEGER"""
    


def p_datatype_agrupacion(t):
    """
    datatype : S_PARIZQ datatype S_PARDER
    """

    


def p_expCompBinario_1(t):
    """
    expComp : datatype OL_MENORQUE datatype
    | datatype OL_MAYORQUE datatype
    | datatype OL_MAYORIGUALQUE datatype
    | datatype OL_MENORIGUALQUE datatype
    | datatype S_IGUAL datatype
    | datatype OL_DISTINTODE datatype
    """
  
    


def p_expCompBinario_2(t):
    """
    expComp : datatype R_IS R_DISTINCT R_FROM datatype
    """
    
    


def p_expCompBinario_3(t):
    """
    expComp : datatype R_IS R_NOT R_DISTINCT R_FROM datatype
    """
   
    


def p_expComp_ternario_1(t):
    """
    expComp :  datatype R_BETWEEN datatype R_AND datatype
    """
    
    


def p_expComp_ternario_2(t):
    """
    expComp : datatype R_NOT R_BETWEEN datatype R_AND datatype
    | datatype R_BETWEEN R_SYMMETRIC datatype R_AND datatype
    """
   

    


def p_expComp_unario_1(t):
    """
    expComp : datatype R_ISNULL
    | datatype R_NOTNULL
    """
 

    


def p_expComp_unario_2(t):
    """
    expComp : datatype R_IS R_NULL
    | datatype R_IS R_TRUE
    | datatype R_IS R_FALSE
    | datatype R_IS R_UNKNOWN
    """
    
    


def p_expComp_unario_3(t):
    """
    expComp : datatype R_IS R_NOT R_NULL
    | datatype R_IS R_NOT R_TRUE
    | datatype R_IS R_NOT R_FALSE
    | datatype R_IS R_NOT R_UNKNOWN
    """
   
    


def p_expSubq(t):
    """
    expSubq : datatype OL_MENORQUE  subqValues S_PARIZQ selectStmt S_PARDER
              | datatype OL_MAYORQUE  subqValues S_PARIZQ selectStmt S_PARDER
              | datatype OL_MAYORIGUALQUE subqValues S_PARIZQ selectStmt S_PARDER
              | datatype OL_MENORIGUALQUE subqValues S_PARIZQ selectStmt S_PARDER
              | datatype OL_ESIGUAL  subqValues S_PARIZQ selectStmt S_PARDER
              | datatype OL_DISTINTODE subqValues S_PARIZQ selectStmt S_PARDER
              | datatype R_BETWEEN datatype R_AND datatype subqValues S_PARIZQ selectStmt S_PARDER
              | datatype R_NOT R_BETWEEN datatype R_AND datatype subqValues S_PARIZQ selectStmt S_PARDER
              | datatype R_BETWEEN R_SYMMETRIC datatype R_AND datatype subqValues S_PARIZQ selectStmt S_PARDER
              | datatype R_IS R_DISTINCT R_FROM datatype subqValues S_PARIZQ selectStmt S_PARDER
              | datatype R_IS R_NOT R_DISTINCT R_FROM datatype subqValues S_PARIZQ selectStmt S_PARDER
              | datatype R_IS R_NULL subqValues S_PARIZQ selectStmt S_PARDER
              | datatype R_IS R_NOT R_NULL subqValues S_PARIZQ selectStmt S_PARDER
              | datatype R_ISNULL subqValues S_PARIZQ selectStmt S_PARDER
              | datatype R_NOTNULL subqValues S_PARIZQ selectStmt S_PARDER
              | datatype R_IS R_TRUE subqValues S_PARIZQ selectStmt S_PARDER
              | datatype R_IS R_NOT R_TRUE subqValues S_PARIZQ selectStmt S_PARDER
              | datatype R_IS R_FALSE subqValues S_PARIZQ selectStmt S_PARDER
              | datatype R_IS R_NOT R_FALSE subqValues S_PARIZQ selectStmt S_PARDER
              | datatype R_IS R_UNKNOWN subqValues S_PARIZQ selectStmt S_PARDER
              | datatype R_IS R_NOT R_UNKNOWN subqValues S_PARIZQ selectStmt S_PARDER
              | stringExp R_LIKE STRING
    """
    


def p_stringExp(t):
    """
    stringExp : STRING
          | columnName
    """
    


def p_subqValues(t):
    """
    subqValues : R_ALL
                  | R_ANY
                  | R_SOME
    """
    


def p_boolean_1(t):
    """
    boolean : R_EXISTS S_PARIZQ selectStmt S_PARDER
    """

    


def p_boolean_2(t):
    """
    boolean : datatype R_IN S_PARIZQ selectStmt S_PARDER
    """
   

def p_boolean_3(t):
    """
    boolean : datatype R_NOT R_IN S_PARIZQ selectStmt S_PARDER
    """
    


def p_boolean_4(t):
    """
    boolean : expComp
            | expSubq
    """

    


def p_expBool_1(t):
    """
    expBool : expBool R_AND expBool
            | expBool R_OR expBool
    """
  
    


def p_expBool_2(t):
    """
    expBool : R_NOT expBool
    """
   


def p_expBool_3(t):
    """
    expBool : S_PARIZQ expBool S_PARDER
    """
    
    


def p_expBool_5(t):
    """
    expBool : expBool optBoolPredicate
    """
   
    


def p_expBool_4(t):
    """
    expBool : boolean
    """
 
    


def p_optBoolPredicate_1(t):
    """
    optBoolPredicate : R_IS R_TRUE
    | R_IS R_FALSE
    | R_IS R_UNKNOWN
    """
   
    


def p_optBoolPredicate_2(t):
    """
    optBoolPredicate : R_IS R_NOT R_TRUE
    | R_IS R_NOT R_FALSE
    | R_IS R_NOT R_UNKNOWN
    """
  
    


def p_columnName_id(t):
    """
    columnName : ID
    """
    

    


def p_columnName_table_id(t):
    """
    columnName : ID S_PUNTO ID
    """
    
    


# En caso de errores descomentar este metodo
'''
def p_columnName_table_idAll(t):
    """
    columnName : ID S_PUNTO O_PRODUCTO
    """
    t[0] = expression.TableAll(t[1], t.slice[1].lineno, t.slice[1].lexpos)
'''


def p_booleanCheck_1(t):
    """
    booleanCheck : idOrLiteral OL_MENORQUE idOrLiteral
    | idOrLiteral OL_MAYORQUE idOrLiteral
    | idOrLiteral OL_MAYORIGUALQUE idOrLiteral
    | idOrLiteral OL_MENORIGUALQUE idOrLiteral
    | idOrLiteral S_IGUAL idOrLiteral
    | idOrLiteral OL_DISTINTODE idOrLiteral
    """

   


def p_booleanCheck_2(t):
    """
    booleanCheck : idOrLiteral R_IS R_DISTINCT R_FROM idOrLiteral
    """

    
    


def p_booleanCheck_3(t):
    """
    booleanCheck : idOrLiteral R_IS R_NOT R_DISTINCT R_FROM idOrLiteral
    """

    
    


def p_idOrLiteral(t):
    """
    idOrLiteral : ID
    | INTEGER
    | STRING
    | DECIMAL
    | CHARACTER
    | R_TRUE
    | R_FALSE
    """

    


# endregion

# Statement para el ALTER
# region ALTER


def p_alterStmt(t):
    """alterStmt : R_ALTER R_DATABASE idOrString alterDb
    | R_ALTER R_TABLE idOrString alterTableList
    """
    
    


def p_alterDb(t):
    """alterDb : R_RENAME R_TO idOrString
    | R_OWNER R_TO ownerOPts
    """
   

    


def p_ownerOpts(t):
    """
    ownerOPts : idOrString
    | R_CURRENT_USER
    | R_SESSION_USER
    """
  
    


def p_alterTableList(t):
    """
    alterTableList : alterTableList S_COMA alterTable
    """
  
    


def p_alterTableList_u(t):
    """
    alterTableList : alterTable
    """
 
    


def p_alterTable(t):
    """
    alterTable : R_ADD alterAdd
    | R_ALTER alterAlter
    | R_DROP alterDrop
    | R_RENAME alterRename
    """

    


def p_alterAdd_column(t):
    """
    alterAdd : R_COLUMN ID types
    """

    


def p_alterAdd_constraint(t):
    """
    alterAdd : createConstraint
    | createPrimary
    | createForeign
    """

    


def p_alterAdd_unique(t):
    """
    alterAdd : constrName R_UNIQUE S_PARIZQ ID S_PARDER
    """
   
    


def p_alterAlter(t):
    """
    alterAlter : R_COLUMN ID R_SET nullOpt
    | R_COLUMN ID R_SET defaultVal
    | R_COLUMN ID R_TYPE types
    """

    


def p_alterDrop(t):
    """
    alterDrop : R_CONSTRAINT ID
    | R_COLUMN ID
    """

    


def p_alterRename(t):
    """
    alterRename : R_COLUMN ID R_TO ID
    """

    


# endregion


"""
Statement para el DROP
"""

# region DROP


def p_dropStmt(t):
    """
    dropStmt : R_DROP R_TABLE ifExists idOrString
    | R_DROP R_DATABASE ifExists idOrString
    """
    
    


def p_ifExists(t):
    """ifExists : R_IF R_EXISTS
    |
    """

    


# endregion

# Statement para el SELECT
# region SELECT


def p_selectStmt_1(t):
    """selectStmt : R_SELECT R_DISTINCT selectParams fromCl whereCl groupByCl limitCl"""

    


# TODO: Cambiar gramatica | R_SELECT selectParams R_FROM tableExp joinList whereCl groupByCl orderByCl limitCl
def p_selectStmt_2(t):
    """selectStmt : R_SELECT selectParams fromCl whereCl groupByCl limitCl"""

    


def p_selectStmt__1(t):
    """selectStmt : R_SELECT selectParams fromCl joinList whereCl groupByCl orderByCl limitCl"""
    


def p_selectStmt__2(t):
    """selectStmt : R_SELECT selectParams fromCl whereCl groupByCl orderByCl limitCl"""
    


def p_selectStmt__3(t):
    """selectStmt : R_SELECT selectParams fromCl joinList whereCl groupByCl limitCl"""
    


def p_selectStmt_union(t):
    """selectStmt : selectStmt R_UNION allOpt selectStmt"""
     


def p_selectStmt_intersect(t):
    """selectStmt : selectStmt R_INTERSECT allOpt selectStmt"""
    
    


def p_selectStmt_except(t):
    """selectStmt : selectStmt R_EXCEPT allOpt selectStmt"""
       


def p_selectStmt_agrupacion(t):
    """selectStmt : S_PARIZQ selectStmt S_PARDER"""

    


def p_fromClause(t):
    """
    fromCl : R_FROM tableExp
    """
    


def p_selectstmt_only_params(t):
    """selectStmt : R_SELECT selectParams"""
    

    


def p_allOpt(t):
    """allOpt : R_ALL
    |
    """

    


def p_selectparams_all(t):
    """selectParams : O_PRODUCTO"""


    


def p_selectparams_params(t):
    """selectParams : selectList"""
   

# En caso de errores cambiar selectListParams -> expresion
def p_selectList_list(t):
    """selectList : selectList S_COMA selectListParams optAlias"""

    


# En caso de errores cambiar selectListParams -> expresion
def p_selectList_u(t):
    """selectList : selectListParams optAlias"""


    


def p_selectListParams_1(t):
    """selectListParams : expresion"""

    


def p_selectListParams_2(t):
    """selectListParams : ID S_PUNTO O_PRODUCTO"""
 
    


def p_optalias_as(t):
    """
    optAlias : R_AS idOrString
    """

    


def p_optalias_id(t):
    """
    optAlias : idOrString
    """

    


def p_optalias_none(t):
    """optAlias : """
  
    


def p_tableexp_list(t):
    """tableExp : tableExp S_COMA fromBody """
 
    


def p_tableexp_u(t):
    """tableExp : fromBody """
   
    


def p_fromBody(t):
    """fromBody : ID optAlias"""
   
    


def p_tableexp_subq(t):
    """fromBody : S_PARIZQ selectStmt S_PARDER R_AS idOrString"""
    

    


def p_joinList(t):
    """joinList : joinList2"""
    


def p_joinList_2(t):
    """joinList2 : joinList2 joinCl
    | joinCl"""
    


def p_joinCl(t):
    """joinCl : joinOpt R_JOIN columnName optAlias R_ON expBool
    | joinOpt R_JOIN columnName optAlias R_USING S_PARIZQ nameList S_PARDER
    | R_NATURAL joinOpt R_JOIN columnName optAlias
    """

    


def p_nameList(t):
    """nameList : nameList S_COMA columnName
    | columnName
    """
    


def p_joinOpt(t):
    """joinOpt : R_INNER
    | R_LEFT
    | R_LEFT R_OUTER
    | R_RIGHT
    | R_RIGHT R_OUTER
    | R_FULL
    | R_FULL R_OUTER
    """
    


def p_whereCl(t):
    """whereCl : R_WHERE expBool"""



def p_whereCl_none(t):
    """whereCl : """



def p_groupByCl_1(t):
    """
    groupByCl : R_GROUP R_BY groupList havingCl
    """



def p_groupByCl_2(t):
    """
    groupByCl :
    """



def p_groupList_1(t):
    """
    groupList :  groupList S_COMA columnName
            | groupList S_COMA INTEGER
    """



def p_groupList_2(t):
    """
    groupList :  columnName
            | INTEGER
    """



def p_havingCl_1(t):
    """havingCl : R_HAVING expBool"""



def p_havingCl_2(t):
    """havingCl :"""



def p_orderByCl(t):
    """orderByCl : R_ORDER R_BY orderList"""



def p_orderList(t):
    """orderList : orderList S_COMA orderByElem
    | orderByElem
    """



def p_orderByElem(t):
    """
    orderByElem : columnName orderOpts orderNull
                | INTEGER orderOpts orderNull
    """
 


def p_orderOpts(t):
    """orderOpts : R_ASC
    | R_DESC
    |
    """



def p_orderNull(t):
    """orderNull : R_NULL R_FIRST
    | R_NULL R_LAST
    |
    """



def p_limitCl(t):
    """limitCl : R_LIMIT INTEGER offsetLimit
    | R_LIMIT R_ALL offsetLimit
    """



def p_limitCl_n(t):
    """limitCl :"""



def p_offsetLimit(t):
    """offsetLimit : R_OFFSET INTEGER"""


def p_offsetLimit_n(t):
    """offsetLimit :"""



# endregion

# Statement para el INSERT

# region INSERT


def p_insertStmt(t):
    """insertStmt : R_INSERT R_INTO ID paramsColumn R_VALUES S_PARIZQ paramsList S_PARDER"""


def p_paramsColumn(t):
    """paramsColumn : S_PARIZQ idList S_PARDER"""





# endregion

# Statement para el UPDATE

# region UPDATE


def p_updateStmt(t):
    """updateStmt : R_UPDATE fromBody R_SET updateCols whereCl"""



def p_updateCols_list(t):
    """updateCols : updateCols S_COMA updateVals"""



def p_updateCols_u(t):
    """updateCols : updateVals """



def p_updateVals(t):
    """updateVals : ID S_IGUAL updateExp"""



def p_updateExp(t):
    """updateExp : datatype
    | R_DEFAULT
    """



# endregion

# Statement para el DELETE y OTROS

# region DELETE, ETC


def p_deleteStmt(t):
    """deleteStmt : R_DELETE fromCl whereCl"""


def p_truncateStmt(t):
    """truncateStmt : R_TRUNCATE tableOpt ID"""


def p_tableOpt(t):
    """tableOpt : R_TABLE
    |
    """


def p_showStmt(t):
    """showStmt : R_SHOW R_DATABASES likeOpt"""

def p_likeOpt(t):
    """likeOpt : R_LIKE STRING
    |
    """



def p_useStmt(t):
    """useStmt : R_USE ID"""


def p_error(t):
    try:
        print("Error sintáctico en '%s'" % t.value)
        print(t.lineno)
    except AttributeError:
        print("end of file")

parser = yacc.yacc()

def parse(input):
    try:
        result = parser.parse(input)
        return result
    except Exception as e:
        print(e)
        return None