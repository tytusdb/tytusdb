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
    # ("right", "UO_SUMA", "UO_RESTA"),
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
    ("left", "R_AND"),
    ("left", "R_OR"),
)

# Definición de la gramática

from Instrucciones import *


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
    """stmt : createStmt S_PUNTOCOMA"""
    t[0] = t[1]


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
    | R_TYPE ifNotExists R_AS R_ENUM S_PARIZQ paramsList S_PARDER
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


# cambiar literal
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
            | expComp
            | expBool
  '''

#TODO: cambiar ID por nombres de funciones
def p_funcCall(t) :
  '''
  funcCall : ID S_PARIZQ paramsList S_PARDER
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
    | literalBoolean
    """


def p_literal_boolean(t):
    """
    literalBoolean :  R_TRUE
    | R_FALSE
    """


def p_params_list(t):
    """paramsList : paramsList S_COMA datatype"""


def p_params_u(t):
    """paramsList : datatype"""


def p_datatype(t):
    """
    datatype :  columnName
    | literal
    | funcCall
    | extract
    | datePart
    | current
    | datatype O_SUMA datatype
    | datatype O_RESTA datatype
    | datatype O_PRODUCTO datatype
    | datatype O_DIVISION datatype
    | datatype O_EXPONENTE datatype
    | datatype O_MODULAR datatype
    | datatype OC_CONCATENAR datatype
    | S_PARIZQ datatype S_PARDER
    """


def p_expComp(t):
    """
    expComp : datatype OL_MENORQUE datatype
    | datatype OL_MAYORQUE datatype
    | datatype OL_MAYORIGUALQUE datatype
    | datatype OL_MENORIGUALQUE datatype
    | datatype S_IGUAL datatype
    | datatype OL_DISTINTODE datatype
    | datatype R_BETWEEN datatype R_AND datatype
    | datatype R_NOT R_BETWEEN datatype R_AND datatype
    | datatype R_BETWEEN R_SYMMETRIC datatype R_AND datatype
    | datatype R_IS R_DISTINCT R_FROM datatype
    | datatype R_IS R_NOT R_DISTINCT R_FROM datatype
    | datatype R_IS R_NULL
    | datatype R_IS R_NOT R_NULL
    | datatype R_ISNULL
    | datatype R_NOTNULL
    | datatype R_IS R_TRUE
    | datatype R_IS R_NOT R_TRUE
    | datatype R_IS R_FALSE
    | datatype R_IS R_NOT R_FALSE
    | datatype R_IS R_UNKNOWN
    | datatype R_IS R_NOT R_UNKNOWN
    """


def p_stringExp(t) :
  '''
  stringExp : STRING
        | columnName
  '''


def p_subqValues(t) :
  '''
  subqValues : R_ALL
                | R_ANY
                | R_SOME
  '''

# TODO: agregar subqueries (selectStmt)
def p_boolean(t) :
  '''
  boolean : expComp
  '''


def p_expBool(t) :
  '''
  expBool : expBool R_AND expBool
            | expBool R_OR expBool
            | R_NOT expBool
            | boolean
  '''


def p_columnName(t):
    """
    columnName :  ID
    | ID S_PUNTO ID
    """


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

def p_error(t):
    try:
        print(t)
        print("Error sintáctico en '%s'" % t.value)
    except AttributeError:
        print("end of file")


import ply.yacc as yacc

parser = yacc.yacc()


s = """
CREATE TABLE IF NOT EXISTS User (
  id INTEGER NOT NULL DEFAULT 0 PRIMARY KEY,
  username VARCHAR(50) NULL CONSTRAINT k_username UNIQUE,
  email CHAR(100) CONSTRAINT k_email CHECK (username != false) REFERENCES Company,
  phone CHARACTER(15) NOT NULL,
  location_ CHARACTER VARYING(100),
  createdAt DATE,
  CONSTRAINT k_phone CHECK (username != "curioso"),
  CHECK (id BETWEEN 3-3 AND 4*5+(3%5) AND (EXTRACT(YEAR FROM TIMESTAMP '2020-08-12') <= 2000 ) OR 3 = sen(3)),
  UNIQUE (username, email),
  FOREIGN KEY (phone, location_) REFERENCES User
);
"""
result = parser.parse(s)
# print(result)
