import ply.yacc as yacc
from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))


# Construccion del analizador léxico
import ply.lex as lex
from analizer.tokensFP import *

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
from abstract.expression import TYPE
from abstract.expression import newTemp
from abstract.expression import incTemp
import modules.expressions as expression
from modules import code

isBlock = False

# region PL/SQL


def p_init(t):
    """
    init : istructionList
    """
    t[0] = t[1]


def p_instruction_list(t):
    """istructionList : istructionList instruction"""
    t[1].append(t[2])
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_instruction_u(t):
    """istructionList : instruction"""
    t[0] = [t[1]]
    repGrammar.append(t.slice)


def p_instruction(t):
    """
    instruction : stmt
    | block
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_block(t):
    """
    block : function_stmt R_AS S_DOLAR S_DOLAR declaration_stmt R_BEGIN block_stmts exception_stmts R_END label S_PUNTOCOMA S_DOLAR S_DOLAR language_function S_PUNTOCOMA
    """
    t[0] = code.Block(t[1], t[5], t[7], t[8], t[10], 0, 0)
    repGrammar.append(t.slice)


# region function

# TODO: isBlock = True
def p_function_stmt(t):
    """
    function_stmt : R_CREATE orReplace R_FUNCTION ID function_opt
    """
    repGrammar.append(t.slice)


def p_function_opt(t):
    """
    function_opt : S_PARIZQ params_function S_PARDER returns_function
    | S_PARIZQ S_PARDER returns_function
    """
    repGrammar.append(t.slice)


def p_params_function(t):
    """
    params_function : params_function S_COMA param_function
    | param_function
    """
    repGrammar.append(t.slice)


def p_param_function(t):
    """
    param_function : ID types_d
    | types_d
    """
    repGrammar.append(t.slice)


def p_returns_function(t):
    """
    returns_function : R_RETURNS types_d
    |
    """
    repGrammar.append(t.slice)


def p_language_function(t):
    """
    language_function : R_LANGUAGE R_PLPGSQL
    |
    """
    repGrammar.append(t.slice)


# endregion


# region declaration


def p_declaration_stmt(t):
    """
    declaration_stmt : R_DECLARE global_variable_declaration
    """
    t[0] = t[2]
    repGrammar.append(t.slice)


def p_declaration_stmt_n(t):
    """
    declaration_stmt :
    """
    t[0] = []
    repGrammar.append(t.slice)


def p_global_variable_declaration(t):
    """
    global_variable_declaration : global_variable_declaration declaration
    """
    t[1].append(t[2])
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_global_variable_declaration_1(t):
    """
    global_variable_declaration : declaration
    """
    t[0] = [t[1]]
    repGrammar.append(t.slice)

def p_global_vd(t):
    """
    declaration : ID R_ALIAS R_FOR S_DOLAR INTEGER S_PUNTOCOMA
        | ID R_RECORD S_PUNTOCOMA
        | ID R_ALIAS R_FOR ID S_PUNTOCOMA
    """
    repGrammar.append(t.slice)

def p_global_vd_assignment(t):
    """
    declaration : ID constant types_d assignment S_PUNTOCOMA
    """
    ass = None
    if t[4]:
        ass = code.Assignment(t[1], t[4], t.slice[1].lineno, t.slice[1].lexpos)
    t[0] = code.Declaration(
        t[1], t[3], ass, t.slice[1].lineno, t.slice[1].lexpos)
    repGrammar.append(t.slice)


def p_constant(t):
    """
    constant : R_CONSTANT
        |
    """
    repGrammar.append(t.slice)


def p_assignment(t):
    """
    assignment : assignment_operator_D expresion
    """
    global isBlock
    isBlock = True
    t[0] = t[2]
    repGrammar.append(t.slice)

def p_assignment_none(t):
    """
    assignment :
    """
    t[0] = None
    repGrammar.append(t.slice)


def p_assignment_operator_D(t):
    """
    assignment_operator_D : R_DEFAULT
        | O_ASIGNACION
        | OL_ESIGUAL
    """
    repGrammar.append(t.slice)


def p_label(t):
    """label : ID
    |
    """
    repGrammar.append(t.slice)


# endregion

# region typedeclaration


def p_types_d(t):
    """
    types_d :  ID
    """
    t[0] = TYPE.TYPE
    repGrammar.append(t.slice)


def p_types_d_simple_num(t):
    """
    types_d : T_SMALLINT
    | T_INTEGER
    | T_BIGINT
    | T_REAL
    | T_DOUBLE T_PRECISION
    | T_MONEY
    """
    t[0] = TYPE.NUMBER
    repGrammar.append(t.slice)


def p_types_d_simple_str(t):
    """
    types_d :  T_TEXT
    """
    t[0] = TYPE.STRING
    repGrammar.append(t.slice)

def p_types_d_params_num(t):
    """
    types_d : T_DECIMAL optParams
    | T_NUMERIC optParams
    """
    t[0] = TYPE.NUMBER
    global isBlock
    isBlock = True
    repGrammar.append(t.slice)


def p_types_d_params_str(t):
    """
    types_d : T_VARCHAR optParams
    | T_CHARACTER optParams
    | T_CHAR optParams
    """
    t[0] = TYPE.STRING
    global isBlock
    isBlock = True
    repGrammar.append(t.slice)

def p_typesvar(t):
    """
    types_d : T_CHARACTER T_VARYING optParams
    """
    t[0] = TYPE.STRING
    global isBlock
    isBlock = True
    repGrammar.append(t.slice)


def p_vartype(t):
    """types_d :  ID O_MODULAR R_TYPE"""
    repGrammar.append(t.slice)


def p_columntype(t):
    """types_d :  ID S_PUNTO ID O_MODULAR R_TYPE"""
    repGrammar.append(t.slice)


def p_rowtypes(t):
    """types_d :  ID O_MODULAR R_ROWTYPE """
    repGrammar.append(t.slice)


# endregion


# region block stmts


def p_block_stmts(t):
    """
    block_stmts : block_stmts block_stmt 
    """
    t[1].append(t[2])
    t[0]=t[1]


def p_block_stmts_u(t):
    """
    block_stmts : block_stmt
    """
    t[0]=[t[1]]


def p_block_stmt(t):
    """
    block_stmt : local_variable_declaration
                | statement
                | stmt
    """
    t[0]=t[1]
    repGrammar.append(t.slice)


# endregion

# region local variable declaration


def p_local_variable_declaration(t):
    """
    local_variable_declaration : ID assignment_operator expresion S_PUNTOCOMA
    """
    global isBlock
    isBlock = True
    t[0] = code.Assignment(t[1], t[3], t.slice[1].lineno, t.slice[1].lexpos)
    repGrammar.append(t.slice)


def p_assignment_operator(t):
    """
    assignment_operator : O_ASIGNACION
        | S_IGUAL
    """
    repGrammar.append(t.slice)


# endregion

# region Control Structures


def p_statement(t):
    """
    statement : if_stmt
            | case_stmt
            | stmt_without_substmt
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_stmt_without_substmt(t):
    """
    stmt_without_substmt : R_NULL S_PUNTOCOMA
    | query_single_row
    """

def p_stmt_without_substmt_rtn(t):
    """
    stmt_without_substmt : R_RETURN return_stmt
    """
    t[0] = t[2]


# endregion

# region CONDITIONALS IF, CASE
# IF


def p_if_stmt(t):
    """if_stmt : R_IF expBool R_THEN block_stmts elseif_stmts_opt else_stmt_opt R_END R_IF S_PUNTOCOMA"""
    global isBlock
    isBlock = True
    repGrammar.append(t.slice)
    t[0] = t[2]
    #expBool contiene el C3D de la expresion

def p_elseif_stmts_opt(t):
    """
    elseif_stmts_opt : elseif_stmts
                |
    """
    repGrammar.append(t.slice)


def p_elseif_stmts(t):
    """
    elseif_stmts : elseif_stmts elseif_stmt
                | elseif_stmt
    """
    repGrammar.append(t.slice)


def p_elseif_stmt(t):
    """elseif_stmt :  R_ELSEIF expBool R_THEN block_stmts"""
    global isBlock
    isBlock = True
    #expBool contiene el C3D de la expresion
    repGrammar.append(t.slice)


def p_else_stmt_opt(t):
    """
    else_stmt_opt : R_ELSE block_stmts
                |
    """
    repGrammar.append(t.slice)


# endregion

# region CASE


def p_case_stmt(t):
    """
    case_stmt : case_stmt_n
            | case_stmt_bool
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_case_stmt_n(t):
    """case_stmt_n : R_CASE ID R_WHEN list_expression R_THEN block_stmts else_case_stmt_n_opt else_stmt_opt R_END R_CASE S_PUNTOCOMA"""
    repGrammar.append(t.slice)


def p_else_case_stmt_n_opt(t):
    """
    else_case_stmt_n_opt : else_case_stmt_n
                        |
    """
    repGrammar.append(t.slice)


def p_else_case_stmt_n(t):
    """
    else_case_stmt_n : else_case_stmt_n R_WHEN list_expression R_THEN block_stmts
    | R_WHEN list_expression R_THEN block_stmts
    """
    repGrammar.append(t.slice)


def p_case_stmt_bool(t):
    """case_stmt_bool : R_CASE R_WHEN expBool R_THEN block_stmts else_case_stmt_bool_opt else_stmt_opt R_END R_CASE S_PUNTOCOMA"""
    global isBlock
    isBlock = True
    t[0] = t[3]
        #expBool contiene el C3D de la expresion
    # TODO: agregar el else case
    repGrammar.append(t.slice)


def p_else_case_stmt_bool_opt(t):
    """
    else_case_stmt_bool_opt : else_case_stmt_bool 
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_else_case_stmt_bool_opt_none(t):
    """
    else_case_stmt_bool_opt :
    """
    t[0] = None
    repGrammar.append(t.slice)


def p_else_case_stmt_bool(t):
    """
    else_case_stmt_bool : else_case_stmt_bool  R_WHEN expBool R_THEN block_stmts
    """
    global isBlock
    isBlock = True
    #expBool contiene el C3D de la expresion
    t[1].append(t[3])
    t[0]=t[1]
    repGrammar.append(t.slice)

    
def p_else_case_stmt_bool_u(t):
    """
    else_case_stmt_bool : R_WHEN expBool R_THEN block_stmts 
    """
    global isBlock
    isBlock = True
    #expBool contiene el C3D de la expresion
    t[0] = [t[2]]
    repGrammar.append(t.slice)


def p_list_expression(t):
    """
    list_expression : exp1
                    | list_expression S_COMA exp1
    """
    repGrammar.append(t.slice)


def p_exp1(t):
    """
    exp1 : INTEGER
    | STRING
    | DECIMAL
    | CHARACTER
    | R_TRUE
    | R_FALSE
    """
    repGrammar.append(t.slice)


# endregion

# region return

# TODO: isblock False
def p_return_stmt(t):
    """
    return_stmt : R_QUERY selectStmt S_PUNTOCOMA
                | S_PUNTOCOMA
                | R_QUERY execute_return S_PUNTOCOMA
    """
    repGrammar.append(t.slice)


def p_return_stmt_exp(t):
    """
    return_stmt : expresion S_PUNTOCOMA
    """
    global isBlock
    isBlock = True
    t[0]= t[1]
    repGrammar.append(t.slice)

def p_return_stmt_exp_next(t):
    """
    return_stmt : R_NEXT expresion S_PUNTOCOMA
    """
    global isBlock
    isBlock = True
    t[0]= t[2]
    repGrammar.append(t.slice)


# endregion

# region EXECUTE


def p_execute_return(t):
    """execute_return : R_EXECUTE exp_string  using  """
    repGrammar.append(t.slice)


def p_execute(t):
    """execute : R_EXECUTE exp_string into_strict using """
    repGrammar.append(t.slice)


def p_into_strict(t):
    """
    into_strict : R_INTO strict ID
    |
    """
    repGrammar.append(t.slice)


def p_exp_string(t):
    """
    exp_string : id_or_string
                | exp_string OC_CONCATENAR id_or_string
    """
    repGrammar.append(t.slice)


def p_using(t):
    """
    using : R_USING list_expression_2
    |
    """
    repGrammar.append(t.slice)


def p_list_expression_2(t):
    """
    list_expression_2 : ID
                    | list_expression_2 S_COMA ID
    """
    repGrammar.append(t.slice)


def p_exp_string_id(t):
    """
    id_or_string : STRING
    | ID
    | funcCall
    """
    global isBlock
    isBlock = True
    repGrammar.append(t.slice)


# endregion

# region query single row


def p_query_single_row(t):
    """
    query_single_row : insertStmt_SR S_PUNTOCOMA
                    | updateStmt_SR S_PUNTOCOMA
                    | deleteStmt_SR S_PUNTOCOMA
                    | selectStmt_SR S_PUNTOCOMA
                    | perform S_PUNTOCOMA
                    | execute S_PUNTOCOMA
                    | get S_PUNTOCOMA
    """
    repGrammar.append(t.slice)


# insert
# TODO: isBlock
def p_insertStmt_single_row(t):
    """insertStmt_SR : R_INSERT R_INTO ID paramsColumn R_VALUES S_PARIZQ paramsList S_PARDER R_RETURNING returnParams  R_INTO strict ID """
    repGrammar.append(t.slice)


# update


def p_updateStmt_single_row(t):
    """
    updateStmt_SR : R_UPDATE fromBody R_SET updateCols whereCl R_RETURNING returnParams R_INTO strict ID
    """
    repGrammar.append(t.slice)


# delete
def p_deleteStmt_single_row(t):
    """
    deleteStmt_SR : R_DELETE fromCl whereCl R_RETURNING returnParams R_INTO strict ID
    """
    repGrammar.append(t.slice)


# region select


def p_selectStmt_single_row_1(t):
    """
    selectStmt_SR : R_SELECT R_DISTINCT selectParams R_INTO strict ID fromCl whereCl groupByCl limitCl
    """
    repGrammar.append(t.slice)


def p_selectStmt_single_row_2(t):
    """
    selectStmt_SR : R_SELECT selectParams R_INTO strict ID fromCl whereCl groupByCl limitCl
    """
    repGrammar.append(t.slice)


def p_selectStmt_union_single_row(t):
    """selectStmt_SR : selectStmt_SR R_UNION allOpt selectStmt_SR"""
    repGrammar.append(t.slice)


def p_selectStmt_intersect_single_row(t):
    """selectStmt_SR : selectStmt_SR R_INTERSECT allOpt selectStmt_SR"""
    repGrammar.append(t.slice)


def p_selectStmt_except_single_row(t):
    """selectStmt_SR : selectStmt_SR R_EXCEPT allOpt selectStmt_SR"""
    repGrammar.append(t.slice)


def p_selectStmt_agrupacion_single_row(t):
    """selectStmt_SR : S_PARIZQ selectStmt_SR S_PARDER"""
    repGrammar.append(t.slice)


def p_selectstmt_only_params_single_row(t):
    """selectStmt_SR : R_SELECT selectParams R_INTO strict ID"""
    repGrammar.append(t.slice)


# endregion

# perform


def p_perform(t):
    """perform : R_PERFORM STRING """


# region GET


def p_get(t):
    """get : R_GET current_ R_DIAGNOSTIC ID assignment_operator item """


def p_current_g(t):
    """
    current_ : R_CURRENT
    |
    """


def p_item(t):
    """item : R_ROW_COUNT"""


# endregion

# endregion

# region strict


def p_strict(t):
    """
    strict : R_STRICT
    |
    """


# endregion

# region returnParams


def p_returnparams_all(t):
    """returnParams : O_PRODUCTO"""


def p_returnparams_params(t):
    """returnParams : returnlist"""


# TODO: isBlock optAlias
# En caso de errores cambiar returnlistParams -> expresion
def p_returnlist_list(t):
    """returnlist : returnlist S_COMA returnlistParams optAlias"""


# En caso de errores cambiar returnlistParams -> expresion
def p_returnlist_u(t):
    """returnlist : returnlistParams optAlias"""


def p_returnlistParams_1(t):
    """returnlistParams : expresion"""
    global isBlock
    isBlock = True


def p_returnlistParams_2(t):
    """returnlistParams : ID S_PUNTO O_PRODUCTO"""


# endregion

# region EXCEPTION


def p_exception_stmts(t):
    """
    exception_stmts : R_EXCEPTION when_stmt
    |
    """


def p_while_stmt_exp(t):
    """
    when_stmt : R_WHEN expBoolOR R_THEN handler_statements_opt
            | when_stmt R_WHEN expBoolOR R_THEN handler_statements_opt
    """


def p_expBoolOR(t):
    """
    expBoolOR : expBoolOR OC_OR expBoolExcept
    """


def p_expBoolOR_u(t):
    """
    expBoolOR : expBoolExcept
    """


def p_expBoolExcept(t):
    """
    expBoolExcept : ID
                | R_SQLSTATE STRING
                | R_OTHERS
    """


def p_handler_statements_opt(t):
    """
    handler_statements_opt : handler_statements
    |
    """


def p_handler_statements(t):
    """
    handler_statements : handler_statements handler_statement
                        | handler_statement
    """


def p_handler_statement(t):
    """
    handler_statement : R_RAISE R_NOTICE STRING S_PUNTOCOMA
                    | R_RAISE R_EXCEPTION STRING S_PUNTOCOMA
                    | R_RETURN return_stmt
                    | R_NULL S_PUNTOCOMA
    """


# endregion

# region Fase 1


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
    global isBlock
    isBlock = False
    repGrammar.append(t.slice)


# Statement para el CREATE
# region CREATE
def p_id_string(t):
    """
    idOrString : ID
    | STRING
    | CHARACTER
    """
    repGrammar.append(t.slice)


def p_createstmt(t):
    """createStmt : R_CREATE createBody"""
    repGrammar.append(t.slice)


def p_createbody(t):
    """
    createBody : createOpts
    """
    repGrammar.append(t.slice)


def p_createopts_table(t):
    """createOpts : R_TABLE ifNotExists idOrString S_PARIZQ createTableList S_PARDER inheritsOpt """
    repGrammar.append(t.slice)


def p_createopts_db(t):
    """
    createOpts : orReplace R_DATABASE ifNotExists idOrString createOwner createMode
    """
    repGrammar.append(t.slice)


def p_createopts_index(t):
    """
    createOpts : indexUnique R_INDEX ID R_ON ID usingHash S_PARIZQ indexList S_PARDER whereCl
    """
    repGrammar.append(t.slice)


def p_indexList(t):
    """
    indexList : indexList S_COMA ID indexOrder indexNull firstLast
    """
    repGrammar.append(t.slice)


def p_indexList2(t):
    """
    indexList : ID indexOrder indexNull firstLast
    """
    repGrammar.append(t.slice)


def p_usingHash(t):
    """
    usingHash : R_USING R_HASH
    |
    """
    repGrammar.append(t.slice)


def p_indexOrder(t):
    """
    indexOrder : R_DESC
    | R_ASC
    |
    """
    repGrammar.append(t.slice)


def p_indexNull(t):
    """
    indexNull : R_NULL
    |
    """
    repGrammar.append(t.slice)


def p_indexFirstLast(t):
    """
    firstLast : R_FIRST
    | R_LAST
    |
    """
    repGrammar.append(t.slice)


def p_createindex_unique(t):
    """
    indexUnique : R_UNIQUE
    |
    """
    repGrammar.append(t.slice)


def p_replace_true(t):
    """
    orReplace : R_OR R_REPLACE
    """
    repGrammar.append(t.slice)


def p_replace_false(t):
    """
    orReplace :
    """
    repGrammar.append(t.slice)


def p_createopts_type(t):
    """
    createOpts : R_TYPE ifNotExists ID R_AS R_ENUM S_PARIZQ paramsList S_PARDER
    """
    repGrammar.append(t.slice)


def p_ifnotexists_true(t):
    """
    ifNotExists : R_IF R_NOT R_EXISTS
    """
    repGrammar.append(t.slice)


def p_ifnotexists_false(t):
    """
    ifNotExists :
    """
    repGrammar.append(t.slice)


def p_inheritsOpt(t):
    """
    inheritsOpt : R_INHERITS S_PARIZQ ID S_PARDER
    """
    repGrammar.append(t.slice)


def p_inheritsOpt_none(t):
    """
    inheritsOpt :
    """
    repGrammar.append(t.slice)


def p_createowner(t):
    """
    createOwner : R_OWNER ID
    | R_OWNER STRING
    """
    repGrammar.append(t.slice)


def p_createowner_asg(t):
    """
    createOwner :  R_OWNER S_IGUAL ID
    | R_OWNER S_IGUAL STRING
    """
    repGrammar.append(t.slice)


def p_createowner_none(t):
    """
    createOwner :
    """
    repGrammar.append(t.slice)


def p_createmode(t):
    """
    createMode : R_MODE INTEGER
    """
    repGrammar.append(t.slice)


def p_createMode_asg(t):
    """
    createMode : R_MODE S_IGUAL INTEGER
    """
    repGrammar.append(t.slice)


def p_createmode_none(t):
    """
    createMode :
    """
    repGrammar.append(t.slice)


def p_createtable_list(t):
    """createTableList : createTableList S_COMA createTable"""
    repGrammar.append(t.slice)


def p_createtable_u(t):
    """createTableList :  createTable"""
    repGrammar.append(t.slice)


def p_createTable_id(t):
    """
    createTable :  ID types createColumns
    """
    repGrammar.append(t.slice)


def p_createTable(t):
    """
    createTable : createConstraint
    | createUnique
    | createPrimary
    | createForeign
    """
    repGrammar.append(t.slice)


def p_createColumNs(t):
    """
    createColumns : colOptionsList
    """
    repGrammar.append(t.slice)


def p_createColumNs_none(t):
    """
    createColumns :
    """
    repGrammar.append(t.slice)


def p_createConstraint(t):
    """createConstraint : constrName R_CHECK S_PARIZQ booleanCheck S_PARDER"""
    repGrammar.append(t.slice)


def p_createUnique(t):
    """createUnique : R_UNIQUE S_PARIZQ idList S_PARDER"""
    repGrammar.append(t.slice)


def p_createPrimary(t):
    """createPrimary : R_PRIMARY R_KEY S_PARIZQ idList S_PARDER"""
    repGrammar.append(t.slice)


def p_createForeign(t):
    """
    createForeign : constrName R_FOREIGN R_KEY S_PARIZQ idList S_PARDER R_REFERENCES ID S_PARIZQ idList S_PARDER
    """
    repGrammar.append(t.slice)


def p_constrName(t):
    """
    constrName : R_CONSTRAINT ID
    """
    repGrammar.append(t.slice)


def p_constrName_none(t):
    """
    constrName :
    """
    repGrammar.append(t.slice)


def p_id_list(t):
    """idList : idList S_COMA ID"""
    repGrammar.append(t.slice)


def p_id_u(t):
    """idList : ID"""
    repGrammar.append(t.slice)


def p_types(t):
    """
    types :  ID
    """
    repGrammar.append(t.slice)


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
    repGrammar.append(t.slice)


# TODO: Cambiar el optParams
def p_types_params(t):
    """
    types : T_DECIMAL optParams
    | T_NUMERIC optParams
    | T_VARCHAR optParams
    | T_CHARACTER optParams
    | T_CHAR optParams
    """
    repGrammar.append(t.slice)


def p_types_var(t):
    """
    types : T_CHARACTER T_VARYING optParams
    """
    repGrammar.append(t.slice)


def p_timeType_interval(t):
    """
    types : R_INTERVAL intervalFields
    """
    repGrammar.append(t.slice)


def p_intervalFields(t):
    """
    intervalFields :  R_YEAR
    | R_MONTH
    | R_DAY
    | R_HOUR
    | R_MINUTE
    | R_SECOND
    """
    repGrammar.append(t.slice)


def p_intervalFields_none(t):
    """
    intervalFields :
    """
    repGrammar.append(t.slice)


def p_optParams(t):
    """optParams : S_PARIZQ literalList S_PARDER"""
    repGrammar.append(t.slice)


def p_optParams_none(t):
    """optParams : """
    repGrammar.append(t.slice)


def p_colOptions_list(t):
    """colOptionsList : colOptionsList colOptions"""
    repGrammar.append(t.slice)


def p_colOptions_u(t):
    """colOptionsList : colOptions"""
    repGrammar.append(t.slice)


def p_colOptions(t):
    """
    colOptions : defaultVal
    | nullOpt
    | constraintOpt
    | primaryOpt
    | referencesOpt
    """
    repGrammar.append(t.slice)


# cambiar literal
def p_defaultVal(t):
    """defaultVal : R_DEFAULT literal"""
    repGrammar.append(t.slice)


def p_nullOpt_true(t):
    """
    nullOpt : R_NOT R_NULL
    """
    repGrammar.append(t.slice)


def p_nullOpt_false(t):
    """
    nullOpt : R_NULL
    """
    repGrammar.append(t.slice)


# cambiar literal


def p_constraintOpt_unique(t):
    """
    constraintOpt : constrName R_UNIQUE
    """
    repGrammar.append(t.slice)


def p_constraintOpt_check(t):
    """
    constraintOpt : constrName R_CHECK S_PARIZQ booleanCheck S_PARDER
    """
    repGrammar.append(t.slice)


def p_primaryOpt(t):
    """primaryOpt : R_PRIMARY R_KEY"""
    repGrammar.append(t.slice)


def p_referencesOpt(t):
    """referencesOpt : R_REFERENCES ID"""
    repGrammar.append(t.slice)


# endregion CREATE

# Gramatica para expresiones

# region Expresiones
def p_expresion(t):
    """
    expresion : datatype
            | expBool
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_expresion_(t):
    """
    expresion : S_PARIZQ selectStmt S_PARDER
    """
    repGrammar.append(t.slice)


def p_funcCall_1(t):
    """
    funcCall : ID S_PARIZQ paramsList S_PARDER
    """
    repGrammar.append(t.slice)


def p_funcCall_2(t):
    """
    funcCall : ID S_PARIZQ S_PARDER
            | R_NOW S_PARIZQ S_PARDER
    """
    repGrammar.append(t.slice)


def p_funcCall_3(t):
    """
    funcCall : R_COUNT S_PARIZQ datatype S_PARDER
            | R_COUNT S_PARIZQ O_PRODUCTO S_PARDER
            | R_SUM S_PARIZQ datatype S_PARDER
            | R_PROM S_PARIZQ datatype S_PARDER
    """
    repGrammar.append(t.slice)


def p_extract_1(t):
    """
    extract : R_EXTRACT S_PARIZQ optsExtract R_FROM timeStamp S_PARDER
    """
    repGrammar.append(t.slice)


def p_extract_2(t):
    """
    extract : R_EXTRACT S_PARIZQ optsExtract R_FROM columnName S_PARDER
    """
    repGrammar.append(t.slice)


def p_timeStamp(t):
    """
    timeStamp : R_TIMESTAMP STRING
          | R_INTERVAL STRING
    """
    repGrammar.append(t.slice)


def p_optsExtract(t):
    """
    optsExtract : R_YEAR
                  | R_MONTH
                  | R_DAY
                  | R_HOUR
                  | R_MINUTE
                  | R_SECOND
    """
    repGrammar.append(t.slice)


def p_datePart(t):
    """
    datePart : R_DATE_PART S_PARIZQ STRING S_COMA dateSource S_PARDER
    """
    repGrammar.append(t.slice)


def p_dateSource(t):
    """
    dateSource : R_TIMESTAMP STRING
          | T_DATE STRING
          | T_TIME STRING
          | R_INTERVAL STRING
          | R_NOW S_PARIZQ S_PARDER
    """
    repGrammar.append(t.slice)


def p_current(t):
    """
    current : R_CURRENT_DATE
          | R_CURRENT_TIME
    """
    repGrammar.append(t.slice)


def p_current_1(t):
    """
    current : timeStamp
    """
    repGrammar.append(t.slice)


def p_literal_list(t):
    """literalList : literalList S_COMA literal"""
    repGrammar.append(t.slice)


def p_literal_u(t):
    """literalList : literal"""
    repGrammar.append(t.slice)


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
    t[0] = expression.C3D("",t.slice[1].value, t.slice[1].lineno, t.slice[1].lexpos)
    repGrammar.append(t.slice)


def p_params_list(t):
    """paramsList : paramsList S_COMA datatype"""
    repGrammar.append(t.slice)


def p_params_u(t):
    """paramsList : datatype"""
    repGrammar.append(t.slice)


def p_datatype_operadores_binarios1(t):
    """
    datatype : datatype O_SUMA datatype
    | datatype O_RESTA datatype
    | datatype O_PRODUCTO datatype
    | datatype O_DIVISION datatype
    | datatype O_EXPONENTE datatype
    | datatype O_MODULAR datatype
    """
    t[0] = code.BinaryOperation(newTemp(),t[1],t[3],t[2], t[1].row, t[1].column)
    repGrammar.append(t.slice)


def p_datatype_operadores_binarios2(t):
    """
    datatype : datatype OC_CONCATENAR datatype
    """
    t[0] = code.BinaryOperation(newTemp(),t[1],t[3],t[2], t[1].row, t[1].column)
    repGrammar.append(t.slice)


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
    t[0] = code.UnaryOperation(newTemp(),t[2],t[1],t[2].row, t[2].column)
    repGrammar.append(t.slice)


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
    t[0]=t[1]
    repGrammar.append(t.slice)


def p_datatype_parameter(t):
    """
    parameter : S_DOLAR INTEGER
    """
    repGrammar.append(t.slice)


def p_datatype_agrupacion(t):
    """
    datatype : S_PARIZQ datatype S_PARDER
    """
    t[0]= t[2]
    repGrammar.append(t.slice)


def p_expCompBinario_1(t):
    """
    expComp : datatype OL_MENORQUE datatype
    | datatype OL_MAYORQUE datatype
    | datatype OL_MAYORIGUALQUE datatype
    | datatype OL_MENORIGUALQUE datatype
    | datatype S_IGUAL datatype
    | datatype OL_DISTINTODE datatype
    """
    t[0] = code.BinaryOperation(newTemp(),t[1],t[3],t[2], t[1].row, t[1].column)
    repGrammar.append(t.slice)


def p_expCompBinario_2(t):
    """
    expComp : datatype R_IS R_DISTINCT R_FROM datatype
    """
    t[0] = code.BinaryOperation(newTemp(), t[1], t[5],"!=", t[1].row, t[1].column)
    repGrammar.append(t.slice)


def p_expCompBinario_3(t):
    """
    expComp : datatype R_IS R_NOT R_DISTINCT R_FROM datatype
    """
    t[0] = code.BinaryOperation(newTemp(), t[1], t[6], "==", t[1].row, t[1].column)
    repGrammar.append(t.slice)


def p_expComp_ternario_1(t):
    """
    expComp :  datatype R_BETWEEN datatype R_AND datatype
    """
    t[0] = code.TernaryOperation(newTemp(), t[1],t[3],t[5],t[2],t[1].row,t[3].column)
    incTemp(2)
    repGrammar.append(t.slice)


def p_expComp_ternario_2(t):
    """
    expComp : datatype R_NOT R_BETWEEN datatype R_AND datatype
    """
    t[0] = code.TernaryOperation(newTemp(), t[1],t[4],t[6],t[2]+t[3],t[1].row,t[1].column)
    incTemp(3)
    repGrammar.append(t.slice)


def p_expComp_ternario_3(t):
    """
    expComp : datatype R_BETWEEN R_SYMMETRIC datatype R_AND datatype
    """
    t[0] = code.TernaryOperation(newTemp(), t[1],t[4],t[6],t[2]+t[3],t[1].row,t[1].column)
    incTemp(6)
    repGrammar.append(t.slice)


def p_expComp_unario_1(t):
    """
    expComp : datatype R_ISNULL
    | datatype R_NOTNULL
    """
    t[0] = code.UnaryOperation(newTemp(),t[1],t[2],t[1].row,t[1].column)
    repGrammar.append(t.slice)


def p_expComp_unario_2(t):
    """
    expComp : datatype R_IS R_NULL
    | datatype R_IS R_TRUE
    | datatype R_IS R_FALSE
    | datatype R_IS R_UNKNOWN
    """
    t[0] = code.UnaryOperation(newTemp(),t[1],t[2]+t[3],t[1].row,t[1].column)
    repGrammar.append(t.slice)


def p_expComp_unario_3(t):
    """
    expComp : datatype R_IS R_NOT R_NULL
    | datatype R_IS R_NOT R_TRUE
    | datatype R_IS R_NOT R_FALSE
    | datatype R_IS R_NOT R_UNKNOWN
    """
    t[0] = code.UnaryOperation(newTemp(),t[1],t[2]+t[3]+t[4],t[1].row,t[1].column)
    repGrammar.append(t.slice)


def p_boolean_1(t):
    """
    boolean : R_EXISTS S_PARIZQ selectStmt S_PARDER
    """
    repGrammar.append(t.slice)


def p_boolean_2(t):
    """
    boolean : datatype R_IN S_PARIZQ selectStmt S_PARDER
    """
    repGrammar.append(t.slice)


def p_boolean_3(t):
    """
    boolean : datatype R_NOT R_IN S_PARIZQ selectStmt S_PARDER
    """
    repGrammar.append(t.slice)


def p_boolean_4(t):
    """
    boolean : expComp
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_expBool_1(t):
    """
    expBool : expBool R_AND expBool
            | expBool R_OR expBool
    """
    t[0] = code.BinaryOperation(newTemp(), t[1], t[3], t[2], t[1].row, t[1].column)
    repGrammar.append(t.slice)


def p_expBool_2(t):
    """
    expBool : R_NOT expBool
    """
    t[0] = code.UnaryOperation(newTemp(),t[2],t[1],t[2].row, t[2].column)
    repGrammar.append(t.slice)


def p_expBool_3(t):
    """
    expBool : S_PARIZQ expBool S_PARDER
    """
    t[0] = t[2]
    repGrammar.append(t.slice)


def p_expBool_5(t):
    """
    expBool : expBool optBoolPredicate
    """
    t[0] = code.UnaryOperation(newTemp(), t[1], t[2], t[1].row, t[1].column )
    repGrammar.append(t.slice)


def p_expBool_4(t):
    """
    expBool : boolean
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_optBoolPredicate_1(t):
    """
    optBoolPredicate : R_IS R_TRUE
    | R_IS R_FALSE
    | R_IS R_UNKNOWN
    """
    t[0] = t[1]+t[2]
    repGrammar.append(t.slice)


def p_optBoolPredicate_2(t):
    """
    optBoolPredicate : R_IS R_NOT R_TRUE
    | R_IS R_NOT R_FALSE
    | R_IS R_NOT R_UNKNOWN
    """
    t[0] = t[1]+t[2]+t[3]
    repGrammar.append(t.slice)


def p_columnName_id(t):
    """
    columnName : ID
    """
    t[0] = expression.C3D("",t[1], t.slice[1].lineno, t.slice[1].lexpos)
    
    repGrammar.append(t.slice)


def p_columnName_table_id(t):
    """
    columnName : ID S_PUNTO ID
    """
    repGrammar.append(t.slice)


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
    repGrammar.append(t.slice)


def p_booleanCheck_2(t):
    """
    booleanCheck : idOrLiteral R_IS R_DISTINCT R_FROM idOrLiteral
    """
    repGrammar.append(t.slice)


def p_booleanCheck_3(t):
    """
    booleanCheck : idOrLiteral R_IS R_NOT R_DISTINCT R_FROM idOrLiteral
    """
    repGrammar.append(t.slice)


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
    repGrammar.append(t.slice)


# endregion

# Statement para el ALTER
# region ALTER


def p_alterStmt(t):
    """alterStmt : R_ALTER R_DATABASE idOrString alterDb
    | R_ALTER R_TABLE idOrString alterTableList
    """
    repGrammar.append(t.slice)


def p_alterDb(t):
    """alterDb : R_RENAME R_TO idOrString
    | R_OWNER R_TO ownerOPts
    """
    repGrammar.append(t.slice)


def p_ownerOpts(t):
    """
    ownerOPts : idOrString
    | R_CURRENT_USER
    | R_SESSION_USER
    """
    repGrammar.append(t.slice)


def p_alterTableList(t):
    """
    alterTableList : alterTableList S_COMA alterTable
    """
    repGrammar.append(t.slice)


def p_alterTableList_u(t):
    """
    alterTableList : alterTable
    """
    repGrammar.append(t.slice)


def p_alterTable(t):
    """
    alterTable : R_ADD alterAdd
    | R_ALTER alterAlter
    | R_DROP alterDrop
    | R_RENAME alterRename
    """
    repGrammar.append(t.slice)


def p_alterAdd_column(t):
    """
    alterAdd : R_COLUMN ID types
    """
    repGrammar.append(t.slice)


def p_alterAdd_constraint(t):
    """
    alterAdd : createConstraint
    | createPrimary
    | createForeign
    """
    repGrammar.append(t.slice)


def p_alterAdd_unique(t):
    """
    alterAdd : constrName R_UNIQUE S_PARIZQ ID S_PARDER
    """
    repGrammar.append(t.slice)


def p_alterAlter(t):
    """
    alterAlter : R_COLUMN ID R_SET nullOpt
    | R_COLUMN ID R_SET defaultVal
    | R_COLUMN ID R_TYPE types
    """
    repGrammar.append(t.slice)


def p_alterDrop(t):
    """
    alterDrop : R_CONSTRAINT ID
    | R_COLUMN ID
    """
    repGrammar.append(t.slice)


def p_alterRename(t):
    """
    alterRename : R_COLUMN ID R_TO ID
    """
    repGrammar.append(t.slice)


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
    repGrammar.append(t.slice)


def p_ifExists(t):
    """ifExists : R_IF R_EXISTS
    |
    """
    repGrammar.append(t.slice)


# endregion

# Statement para el SELECT
# region SELECT


def p_selectStmt_1(t):
    """selectStmt : R_SELECT R_DISTINCT selectParams fromCl whereCl groupByCl limitCl orderByCl"""
    global isBlock
    isBlock = False
    repGrammar.append(t.slice)


def p_selectStmt_2(t):
    """selectStmt : R_SELECT selectParams fromCl whereCl groupByCl limitCl orderByCl"""
    global isBlock
    isBlock = False
    repGrammar.append(t.slice)


def p_selectStmt_union(t):
    """selectStmt : selectStmt R_UNION allOpt selectStmt"""
    global isBlock
    isBlock = False
    repGrammar.append(t.slice)


def p_selectStmt_intersect(t):
    """selectStmt : selectStmt R_INTERSECT allOpt selectStmt"""
    global isBlock
    isBlock = False
    repGrammar.append(t.slice)


def p_selectStmt_except(t):
    """selectStmt : selectStmt R_EXCEPT allOpt selectStmt"""
    global isBlock
    isBlock = False
    repGrammar.append(t.slice)


def p_selectStmt_agrupacion(t):
    """selectStmt : S_PARIZQ selectStmt S_PARDER"""
    global isBlock
    isBlock = False
    repGrammar.append(t.slice)


def p_fromClause(t):
    """
    fromCl : R_FROM tableExp
    """
    repGrammar.append(t.slice)


def p_selectstmt_only_params(t):
    """selectStmt : R_SELECT selectParams"""
    global isBlock
    isBlock = False
    t[0] = t[2]
    repGrammar.append(t.slice)


def p_allOpt(t):
    """allOpt : R_ALL
    |
    """
    repGrammar.append(t.slice)


def p_selectparams_all(t):
    """selectParams : O_PRODUCTO"""
    repGrammar.append(t.slice)


def p_selectparams_params(t):
    """selectParams : selectList"""
    t[0] = t[1]
    repGrammar.append(t.slice)


# En caso de errores cambiar selectListParams -> expresion
def p_selectList_list(t):
    """selectList : selectList S_COMA selectListParams optAlias"""
    t[1].append(t[3])
    t[0] = t[1]
    repGrammar.append(t.slice)


# En caso de errores cambiar selectListParams -> expresion
def p_selectList_u(t):
    """selectList : selectListParams optAlias"""
    t[0] = [t[1]]
    repGrammar.append(t.slice)


def p_selectListParams_1(t):
    """selectListParams : expresion"""
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_selectListParams_2(t):
    """selectListParams : ID S_PUNTO O_PRODUCTO"""
    repGrammar.append(t.slice)


def p_optalias_as(t):
    """
    optAlias : R_AS idOrString
    """
    repGrammar.append(t.slice)


def p_optalias_id(t):
    """
    optAlias : idOrString
    """
    repGrammar.append(t.slice)


def p_optalias_none(t):
    """optAlias : """
    repGrammar.append(t.slice)


def p_tableexp_list(t):
    """tableExp : tableExp S_COMA fromBody """
    repGrammar.append(t.slice)


def p_tableexp_u(t):
    """tableExp : fromBody """
    repGrammar.append(t.slice)


def p_fromBody(t):
    """fromBody : ID optAlias"""
    repGrammar.append(t.slice)


def p_tableexp_subq(t):
    """fromBody : S_PARIZQ selectStmt S_PARDER R_AS idOrString"""
    repGrammar.append(t.slice)


def p_whereCl(t):
    """whereCl : R_WHERE expBool"""
    repGrammar.append(t.slice)


def p_whereCl_none(t):
    """whereCl : """
    repGrammar.append(t.slice)


def p_groupByCl_1(t):
    """
    groupByCl : R_GROUP R_BY groupList havingCl
    """
    repGrammar.append(t.slice)


def p_groupByCl_2(t):
    """
    groupByCl :
    """
    repGrammar.append(t.slice)


def p_groupList_1(t):
    """
    groupList :  groupList S_COMA columnName
            | groupList S_COMA INTEGER
    """
    repGrammar.append(t.slice)


def p_groupList_2(t):
    """
    groupList :  columnName
            | INTEGER
    """
    repGrammar.append(t.slice)


def p_havingCl_1(t):
    """havingCl : R_HAVING expBool"""
    repGrammar.append(t.slice)


def p_havingCl_2(t):
    """havingCl :"""
    repGrammar.append(t.slice)


def p_orderByCl(t):
    """orderByCl : R_ORDER R_BY orderList"""
    repGrammar.append(t.slice)


def p_orderByCl_n(t):
    """orderByCl : """
    repGrammar.append(t.slice)


def p_orderList(t):
    """orderList : orderList S_COMA orderByElem"""
    repGrammar.append(t.slice)


def p_orderList_1(t):
    """orderList : orderByElem"""
    repGrammar.append(t.slice)


def p_orderByElem(t):
    """
    orderByElem : columnName orderOpts orderNull
                | INTEGER orderOpts orderNull
    """
    repGrammar.append(t.slice)


def p_orderOpts(t):
    """orderOpts : R_ASC
    | R_DESC
    """
    repGrammar.append(t.slice)


def p_orderOpts_n(t):
    """orderOpts :"""
    repGrammar.append(t.slice)


def p_orderNull(t):
    """orderNull : R_NULLS R_FIRST
    | R_NULLS R_LAST
    """
    repGrammar.append(t.slice)


def p_orderNull_n(t):
    """orderNull :"""
    repGrammar.append(t.slice)


def p_limitCl(t):
    """limitCl : R_LIMIT INTEGER offsetLimit
    | R_LIMIT R_ALL offsetLimit
    """
    repGrammar.append(t.slice)


def p_limitCl_n(t):
    """limitCl :"""
    repGrammar.append(t.slice)


def p_offsetLimit(t):
    """offsetLimit : R_OFFSET INTEGER"""
    repGrammar.append(t.slice)


def p_offsetLimit_n(t):
    """offsetLimit :"""
    repGrammar.append(t.slice)


# endregion

# Statement para el INSERT

# region INSERT


def p_insertStmt(t):
    """insertStmt : R_INSERT R_INTO ID paramsColumn R_VALUES S_PARIZQ paramsList S_PARDER"""
    repGrammar.append(t.slice)


def p_paramsColumn(t):
    """paramsColumn : S_PARIZQ idList S_PARDER"""
    repGrammar.append(t.slice)


def p_paramsColumn_none(t):
    """paramsColumn :"""
    repGrammar.append(t.slice)


# endregion

# Statement para el UPDATE

# region UPDATE


def p_updateStmt(t):
    """updateStmt : R_UPDATE fromBody R_SET updateCols whereCl"""
    repGrammar.append(t.slice)


def p_updateCols_list(t):
    """updateCols : updateCols S_COMA updateVals"""
    repGrammar.append(t.slice)


def p_updateCols_u(t):
    """updateCols : updateVals """
    repGrammar.append(t.slice)


def p_updateVals(t):
    """updateVals : ID S_IGUAL updateExp"""
    repGrammar.append(t.slice)


def p_updateExp(t):
    """updateExp : datatype
    | R_DEFAULT
    """
    repGrammar.append(t.slice)


# endregion

# Statement para el DELETE y OTROS

# region DELETE, ETC


def p_deleteStmt(t):
    """deleteStmt : R_DELETE fromCl whereCl"""
    repGrammar.append(t.slice)


def p_truncateStmt(t):
    """truncateStmt : R_TRUNCATE tableOpt ID"""
    repGrammar.append(t.slice)


def p_tableOpt(t):
    """tableOpt : R_TABLE
    |
    """
    repGrammar.append(t.slice)


def p_showStmt(t):
    """showStmt : R_SHOW R_DATABASES likeOpt"""
    repGrammar.append(t.slice)


def p_likeOpt(t):
    """likeOpt : R_LIKE STRING
    |
    """
    repGrammar.append(t.slice)


def p_useStmt(t):
    """useStmt : R_USE ID"""
    repGrammar.append(t.slice)


# endregion

# endregion

syntax_errors = list()
PostgreSQL = list()


def p_error(t):
    try:
        print(t)
        print("Error sintáctico en '%s'" % t.value)
    except AttributeError:
        print("end of file")


parser = yacc.yacc()


def parse(input):
    try:
        global repGrammar
        repGrammar = []
        lexer.lineno = 1
        result = parser.parse(input)
        return result
    except Exception as e:
        print(e)
        return None
