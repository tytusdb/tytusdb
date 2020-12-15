
from Tokens import *

# Construccion del analizador léxico
import ply.lex as lex
lexer = lex.lex()
# Asociación de operadores y precedencia
precedence = (
    ("left", "OC_CONCATENAR"),
    ("left", "O_SUMA", "O_RESTA"),
    ("left", "O_PRODUCTO", "O_DIVISION", "O_MODULAR"),
    ("left", "O_EXPONENTE"),
    ("right", "UO_SUMA", "UO_RESTA"),
    (
        "left",
        "S_IGUAL",
        "OL_DISTINTODE",
        "OL_MAYORQUE",
        "OL_MENORQUE",
        "OL_MAYORIGUALQUE",
        "OL_MENORIGUALQUE",
    ),
    (
        "left",
        "R_BETWEEN",
        # "R_IS",
    ),
    ("right", "R_NOT"),
    ("left", "R_AND", "R_OR"),
    ("left","R_UNION","R_INTERSECT","R_EXCEPT")
)

# Definición de la gramática

import Expresiones
import Instrucciones

def p_init(t):
    """init : stmtList"""
    t[0] = t[1]

def p_stmt_list(t):
    """stmtList : stmtList stmt"""
    t[1].append(t[2])
    t[0] = t[1]

def p_stmt_u(t):
    """stmtList : stmt"""
    t[0] = [t[1]]

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
    t[0] = t[1].execute()

# Statement para el CREATE
# region CREATE
def p_createStmt(t):
    """createStmt : R_CREATE createBody"""
    t[0] = t[2]

def p_createBody(t):
    """
    createBody : R_OR R_REPLACE createOpts
    | createOpts
    """

def p_createOpts(t):
    """
    createOpts : R_TABLE ifNotExists ID S_PARIZQ createTableList S_PARDER inheritsOpt
    | R_DATABASE ifNotExists ID createOwner createMode
    | R_TYPE ifNotExists ID R_AS R_ENUM S_PARIZQ paramsList S_PARDER
    """

def p_ifNotExists(t):
    """
    ifNotExists : R_IF R_NOT R_EXISTS
    |
    """

def p_inheritsOpt(t):
    """
    inheritsOpt : R_INHERITS S_PARIZQ ID S_PARDER
    |
    """

def p_createOwner(t):
    """
    createOwner : R_OWNER ID
    | R_OWNER S_IGUAL ID
    |
    """

def p_createMode(t):
    """
    createMode : R_MODE INTEGER
    | R_MODE S_IGUAL INTEGER
    |
    """

def p_createTable_list(t):
    """createTableList : createTableList S_COMA createTable"""

def p_createTable_u(t):
    """createTableList :  createTable"""

def p_createTable(t):
    """
    createTable :  ID types createColumns
    | createConstraint
    | createUnique
    | createPrimary
    | createForeign
    """

def p_createColumNs(t):
    """
    createColumns : colOptionsList
    |
    """

def p_createConstraint(t):
    """createConstraint : constrName R_CHECK S_PARIZQ expBoolCheck S_PARDER"""

def p_createUnique(t):
    """createUnique : R_UNIQUE S_PARIZQ idList S_PARDER"""

def p_createPrimary(t):
    """createPrimary : R_PRIMARY R_KEY S_PARIZQ idList S_PARDER"""

def p_createForeign(t):
    """
    createForeign : R_FOREIGN R_KEY S_PARIZQ idList S_PARDER R_REFERENCES ID S_PARIZQ idList S_PARDER
    | R_FOREIGN R_KEY S_PARIZQ idList S_PARDER R_REFERENCES ID
    """

def p_constrName(t):
    """
    constrName : R_CONSTRAINT ID
    |
    """

def p_id_list(t):
    """idList : idList S_COMA ID"""

def p_id_u(t):
    """idList : ID"""

def p_types(t):
    """
    types :  ID
    | T_SMALLINT
    | T_INTEGER
    | T_BIGINT
    | T_DECIMAL
    | T_NUMERIC
    | T_REAL
    | T_DOUBLE T_PRECISION
    | T_MONEY
    | T_CHARACTER T_VARYING optParams
    | T_VARCHAR optParams
    | T_CHARACTER optParams
    | T_CHAR optParams
    | T_TEXT
    | timeType
    """

def p_timeType(t):
    """
    timeType :  R_TIMESTAMP optParams
    | T_DATE
    | T_TIME optParams
    | R_INTERVAL intervalFields optParams
    """

def p_intervalFields(t):
    """
    intervalFields :  R_YEAR
    | R_MONTH
    | R_DAY
    | R_HOUR
    | R_MINUTE
    | R_SECOND
    |
    """

def p_optParams(t):
    """optParams : S_PARIZQ literalList S_PARDER"""

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

def p_nullOpt(t):
    """
    nullOpt : R_NOT R_NULL
    | R_NULL
    """

# cambiar literal
def p_constraintOpt(t):
    """
    constraintOpt : constrName R_UNIQUE
    | constrName R_CHECK S_PARIZQ expBoolCheck S_PARDER
    """

def p_primaryOpt(t):
    """primaryOpt : R_PRIMARY R_KEY"""

def p_referencesOpt(t):
    """referencesOpt : R_REFERENCES ID"""

# endregion CREATE
# Gramatica para expresiones
# region Expresiones
def p_expresion(t) :
    '''
    expresion : datatype
            | expBool
    '''
    t[0] = t[1]

def p_expresion_(t) :
    '''
    expresion : S_PARIZQ selectStmt S_PARDER
    '''
    t[0] = t[2]

def p_funcCall_1(t) :
    '''
    funcCall : ID S_PARIZQ paramsList S_PARDER
    '''
    t[0] = Expresiones.FunctionCall(t[1],t[3])
    

def p_funcCall_2(t) :
    '''
    funcCall : ID S_PARIZQ S_PARDER
    '''
    t[0] = Expresiones.FunctionCall(t[1],[])

def p_funcCall_3(t) :
    '''
    funcCall : R_NOW S_PARIZQ S_PARDER
            | R_COUNT S_PARIZQ paramsList S_PARDER
            | R_COUNT S_PARIZQ O_PRODUCTO S_PARDER
            | R_SUM S_PARIZQ paramsList S_PARDER
            | R_SUM S_PARIZQ O_PRODUCTO S_PARDER
            | R_PROM S_PARIZQ paramsList S_PARDER
            | R_PROM S_PARIZQ O_PRODUCTO S_PARDER
    '''

def p_extract(t) :
  '''
  extract : R_EXTRACT S_PARIZQ optsExtract R_FROM timeStamp S_PARDER
  '''

def p_timeStamp(t) :
  '''
  timeStamp : R_TIMESTAMP STRING
        | R_INTERVAL STRING
  '''

def p_optsExtract(t) :
  '''
  optsExtract : R_YEAR
                | R_MONTH
                | R_DAY
                | R_HOUR 
                | R_MINUTE
                | R_SECOND
  '''

def p_datePart(t) :
  '''
  datePart : R_DATE_PART S_PARIZQ STRING S_COMA dateSource S_PARDER
  '''

def p_dateSource(t) :
  '''
  dateSource : R_TIMESTAMP STRING
        | T_DATE STRING
        | T_TIME STRING
        | R_INTERVAL intervalFields STRING
        | R_NOW S_PARIZQ S_PARDER
  '''

def p_current(t) :
  '''
  current : R_CURRENT_DATE
        | R_CURRENT_TIME
        | timeStamp
  '''

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
    """

    if t.slice[1].type == 'CHARACTER' or t.slice[1].type == 'STRING':
        tipo = Expresiones.TYPE.STRING
    elif t.slice[1].type == 'R_TRUE' or t.slice[1].type == 'R_FALSE':
        t.slice[1].value = t.slice[1].value == 'TRUE'
        tipo = Expresiones.TYPE.BOOLEAN
    else:
        tipo = Expresiones.TYPE.NUMBER
    t[0] = Expresiones.Primitivos(tipo, t.slice[1].value)


def p_params_list(t):
    """paramsList : paramsList S_COMA datatype"""
    t[1].append(t[3])
    t[0] = t[1] 

def p_params_u(t):
    """paramsList : datatype"""
    t[0] = [t[1]]

def p_datatype_operadores_binarios(t):
    """
    datatype : datatype O_SUMA datatype
    | datatype O_RESTA datatype
    | datatype O_PRODUCTO datatype
    | datatype O_DIVISION datatype
    | datatype O_EXPONENTE datatype
    | datatype O_MODULAR datatype
    | datatype OC_CONCATENAR datatype
    """
    t[0] = Expresiones.ExpresionBinaria(t[1], t[3], t[2])

def p_datatype_operadores_unarios(t):
    """
    datatype : O_RESTA datatype %prec UO_RESTA
    | O_SUMA datatype %prec UO_SUMA
    """
    t[0] = Expresiones.ExpresionUnaria(t[2], t[1])

def p_datatype_operandos(t):
    """
    datatype : columnName
    | literal
    | funcCall
    | extract
    | datePart
    | current
    """
    t[0] = t[1]

def p_datatype_agrupacion(t):
    """
    datatype : S_PARIZQ datatype S_PARDER
    """
    t[0] = t[2]

def p_expCompBinario_1(t):
    """
    expComp : datatype OL_MENORQUE datatype
    | datatype OL_MAYORQUE datatype
    | datatype OL_MAYORIGUALQUE datatype
    | datatype OL_MENORIGUALQUE datatype
    | datatype S_IGUAL datatype
    | datatype OL_DISTINTODE datatype
    """
    t[0] = Expresiones.ExpresionCompBinaria(t[1],t[3],t[2])

def p_expCompBinario_2(t):
    """
    expComp : datatype R_IS R_DISTINCT R_FROM datatype
    """
    t[0] = Expresiones.ExpresionCompBinaria(t[1],t[5],t[2]+t[3]+t[4])

def p_expCompBinario_3(t):
    """
    expComp : datatype R_IS R_NOT R_DISTINCT R_FROM datatype
    """
    t[0] = Expresiones.ExpresionCompBinaria(t[1],t[6],t[2]+t[3]+t[4]+t[5])

def p_expComp_ternario_1(t):
    """
    expComp :  datatype R_BETWEEN datatype R_AND datatype
    """
    t[0] = Expresiones.ExpresionCompTernaria(t[1],t[3],t[5],t[2])

def p_expComp_ternario_2(t):
    """
    expComp : datatype R_NOT R_BETWEEN datatype R_AND datatype
    | datatype R_BETWEEN R_SYMMETRIC datatype R_AND datatype
    """
    t[0] = Expresiones.ExpresionCompTernaria(t[1],t[4],t[6],t[2]+t[3])

def p_expComp_unario_1(t):
    """
    expComp : datatype R_ISNULL
    | datatype R_NOTNULL
    """
    t[0] = Expresiones.ExpresionCompUnaria(t[1],t[2])

def p_expComp_unario_2(t):
    """
    expComp : datatype R_IS R_NULL
    | datatype R_IS R_TRUE
    | datatype R_IS R_FALSE
    | datatype R_IS R_UNKNOWN
    """
    t[0] = Expresiones.ExpresionCompUnaria(t[1],t[2]+t[3])

def p_expComp_unario_3(t):
    """
    expComp : datatype R_IS R_NOT R_NULL
    | datatype R_IS R_NOT R_TRUE
    | datatype R_IS R_NOT R_FALSE
    | datatype R_IS R_NOT R_UNKNOWN
    """
    t[0] = Expresiones.ExpresionCompUnaria(t[1],t[2]+t[3]+t[4])

def p_expSubq(t) :
  '''
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
  '''

def p_stringExp(t) :
  '''
  stringExp : STRING
        | columnName
  '''


def p_subqValues(t):
  '''
  subqValues : R_ALL
                | R_ANY
                | R_SOME
  '''


def p_boolean_1(t):
    '''
    boolean : R_EXISTS S_PARIZQ selectStmt S_PARDER
            | datatype R_IN S_PARIZQ selectStmt S_PARDER
            | datatype R_NOT R_IN S_PARIZQ selectStmt S_PARDER
    '''

def p_boolean_2(t) :
    '''
    boolean : expComp
            | expSubq
    '''
    t[0] = t[1]

def p_expBool_1(t) :
    '''
    expBool : expBool R_AND expBool
            | expBool R_OR expBool
    '''
    t[0] = Expresiones.ExpresionBooleanaBinaria(t[1],t[3],t[2])

def p_expBool_2(t) :
    '''
    expBool : R_NOT expBool
    '''
    t[0] = Expresiones.ExpresionBooleanaUnaria(t[2],t[1])

def p_expBool_3(t) :
    '''
    expBool : S_PARIZQ expBool S_PARDER
    '''
    t[0] = t[2]

def p_expBool_4(t) :
    '''
    expBool : boolean
    '''
    t[0] = t[1]

def p_columnName_id(t):
    """
    columnName : ID
    """
    t[0] = Expresiones.NombreColumna(None, t[3])

def p_columnName_table_id(t):
    """
    columnName : ID S_PUNTO ID
    """
    t[0] = Expresiones.NombreColumna(t[1], t[3])

def p_expBoolCheck(t):
    """
    expBoolCheck :  expBoolCheck R_AND expBoolCheck
    | expBoolCheck R_OR expBoolCheck
    | R_NOT expBoolCheck
    | booleanCheck
    | S_PARIZQ booleanCheck S_PARDER
    """

def p_boolCheck(t):
    """
    booleanCheck :  expComp
    """

#endregion

# Statement para el ALTER
#region ALTER
def p_alterStmt(t):
    """alterStmt : R_ALTER R_DATABASE ID alterDb
    | R_ALTER R_TABLE ID alterTableList
    """

def p_alterDb(t):
    """alterDb : R_RENAME R_TO ID
    | R_OWNER R_TO ownerOPts
    """

def p_ownerOpts(t):
    """ownerOPts : ID
    | R_CURRENT_USER
    | R_SESSION_USER
    """

def p_alterTableList(t):
    """alterTableList : alterTableList S_COMA alterTable
    | alterTable
    """

def p_alterTable(t):
    """alterTable : R_ADD alterConstraint
    | alterCol
    | R_DROP R_CONSTRAINT ID
    | R_DROP R_COLUMN ID
    | R_RENAME R_COLUMN ID R_TO ID
    """

def p_alterConstraint(t):
    """alterConstraint : R_CHECK S_PARIZQ expBoolCheck S_PARDER
    | R_CONSTRAINT ID R_UNIQUE S_PARIZQ ID S_PARDER
    | createForeign
    | R_COLUMN ID types
    """

def p_alterCol(t):
    """alterCol : R_ALTER R_COLUMN ID R_SET R_NOT R_NULL
    | R_ALTER R_COLUMN ID R_SET R_NULL
    | R_ALTER R_COLUMN ID R_TYPE types
    """

#endregion

'''
Statement para el DROP
'''

#region DROP
def p_dropStmt(t):
    """dropStmt : R_DROP R_TABLE ID
    | R_DROP R_DATABASE ifExists ID
    """

def p_ifExists(t):
    """ifExists : R_IF R_EXISTS 
    |
    """

#endregion

# Statement para el SELECT
# region SELECT
def p_selectStmt(t):
    """selectStmt : R_SELECT selectParams R_FROM tableExp joinList whereCl groupByCl orderByCl limitCl
    | R_SELECT R_DISTINCT selectParams R_FROM tableExp whereCl groupByCl
    | selectStmt R_UNION allOpt selectStmt
    | selectStmt R_INTERSECT allOpt selectStmt
    | selectStmt R_EXCEPT allOpt selectStmt
    | S_PARIZQ selectStmt S_PARDER
    """

def p_selectstmt_only_params(t):
    """selectStmt : R_SELECT selectParams
    """
    t[0] = Instrucciones.SelectOnlyParams(t[2].params)

def p_allOpt(t):
    """allOpt : R_ALL
        |
    """

def p_selectparams_all(t):
    """selectParams : O_PRODUCTO"""
    t[0] = Instrucciones.SelectParams(Instrucciones.SELECT_MODE.ALL)

def p_selectparams_params(t):
    """selectParams : selectList"""
    t[0] = Instrucciones.SelectParams(Instrucciones.SELECT_MODE.PARAMS, t[1])

#cambiar datatype - expresion optAlias
def p_selectList_list(t):
    """selectList : selectList S_COMA expresion optAlias"""
    if t[4] != None: t[3].temp = t[4]
    t[1].append(t[3])
    t[0] = t[1]

#cambiar datatype - expresion optAlias
def p_selectList_u(t):
    """selectList : expresion optAlias"""
    if t[2] != None: t[1].temp = t[2]
    t[0] = [t[1]]


def p_optalias_as(t):
    """
    optAlias : R_AS ID
    | R_AS STRING
    """
    t[0] = t[2]

def p_optalias_id(t):
    """
    optAlias : ID
    | STRING
    """
    t[0] = t[1]

def p_optalias_none(t):
    """optAlias : """
    t[0] = None

def p_tableExp(t):
    """tableExp : tableExp S_COMA fromBody optAlias
    | fromBody optAlias
    """

def p_fromBody(t):
    """fromBody : columnName
    | S_PARIZQ selectStmt S_PARDER
    """

def p_joinList(t):
    """joinList : joinList2
    | 
    """

def p_joinList2(t):
    """joinList2 : joinList2 joinCl
    | joinCl"""

def p_joinCl(t):
    """joinCl : joinOpt R_JOIN columnName R_ON expBool
    | joinOpt R_JOIN columnName R_USING S_PARIZQ nameList S_PARDER
    | R_NATURAL joinOpt R_JOIN columnName
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
    """whereCl : R_WHERE expBool
    | 
    """

def p_groupByCl(t):
    """groupByCl : R_GROUP R_BY groupList havingCl
    | 
    """

def p_groupList(t):
    """groupList :  groupList S_COMA columnName
    | columnName
    """

def p_havingCl(t):
    """havingCl : R_HAVING expBool
    |
    """

def p_orderByCl(t):
    """orderByCl : R_ORDER R_BY orderList
                |
    """

def p_orderList(t):
    """orderList : orderList S_COMA orderByElem
    | orderByElem
    """

def p_orderByElem(t):
    """orderByElem : columnName orderOpts orderNull"""

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
    |
    """

def p_offsetLimit(t):
    """offsetLimit : R_OFFSET INTEGER
        |
    """

#endregion

# Statement para el INSERT 

#region INSERT
def p_insertStmt(t):
    """insertStmt : R_INSERT R_INTO ID R_VALUES S_PARIZQ paramsList S_PARDER
    """
#endregion

# Statement para el UPDATE 

#region UPDATE
def p_updateStmt(t):
    """updateStmt : R_UPDATE ID optAlias R_SET updateCols S_IGUAL updateVals whereCl
    """

def p_updateCols(t):
    """updateCols : ID
                  | S_PARIZQ idList S_PARDER
    """

def p_updateVals(t):
    """updateVals : updateExp
                  | S_PARIZQ updateExp S_COMA updateList S_PARDER
    """

def p_updateList(t):
    """updateList : updateList S_COMA updateExp
    | updateExp
    """

def p_updateExp(t):
    """updateExp : datatype
    | R_DEFAULT
    """

#endregion

# Statement para el DELETE y OTROS

#region DELETE, ETC
def p_deleteStmt(t):
    """deleteStmt : R_DELETE R_FROM ID optAlias whereCl
    """

def p_truncateStmt(t):
    """truncateStmt : R_TRUNCATE tableOpt ID
    """

def p_tableOpt(t):
    """tableOpt : R_TABLE
        | 
    """

def p_showStmt(t):
    """showStmt : R_SHOW R_DATABASES likeOpt
    """

def p_likeOpt(t):
    """likeOpt : R_LIKE STRING
        |
    """

def p_useStmt(t):
    """useStmt : R_USE R_DATABASE ID
    """

#endregion

def p_error(t):
    try:
        print(t)
        print("Error sintáctico en '%s'" % t.value)
    except AttributeError:
        print("end of file")

import ply.yacc as yacc
parser = yacc.yacc()

s = """
    SELECT abs(-pi()+1),3+3,cos();
"""
result = parser.parse(s)
print(result)
