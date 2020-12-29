# GRUPO 5
# 201213062 - Mónica Raquel Calderon Muñoz
# 201213223 - Astrid Edith Hernandez Gonzalez
# 201213255 - Leonel Eduardo Avila Calvillo
# 201220159 - Diego Ahtohil Noj Armira
# 201220165 - Oscar Rolando Bernard Peralta

# IMPORT SECTION
import ply.lex as lex
import ply.yacc as yacc
from Expresiones import *
from Instrucciones import *
from Retorno import Retorno
from NodoAST import NodoAST
import re

# VARIABLES GLOBALES
counter_lexical_error = 1
counter_syntactic_error = 1
reporte_gramatical = []

# LISTADO DE PALABRAS RESERVADAS
palabras_reservadas = {
    'select'        : 'SELECT',
    'where'         : 'WHERE',
    'limit'         : 'LIMIT',
    'group'         : 'GROUP',
    'by'            : 'BY',
    'having'        : 'HAVING',
    'order'         : 'ORDER',
    'asc'           : 'ASC',
    'desc'          : 'DESC',
    'offset'        : 'OFFSET',
    'nulls'         : 'NULLS',
    'last'          : 'LAST',
    'first'         : 'FIRST',
    'as'            : 'AS',
    'is'            : 'IS',
    'and'           : 'AND',
    'or'            : 'OR',
    'true'          : 'TRUE',
    'false'         : 'FALSE',
    'not'           : 'NOT',
    'distinct'      : 'DISTINCT',
    'count'         : 'COUNT',
    'avg'           : 'AVG',
    'sum'           : 'SUM',
    'max'           : 'MAX',
    'min'           : 'MIN',
    'greatest'      : 'GREATEST',
    'least'         : 'LEAST',
    'unknown'       : 'UNKNOWN',
    'between'       : 'BETWEEN',
    'simmetric'     : 'SIMMETRIC',
    'null'          : 'NULL',
    'union'         : 'UNION',
    'all'           : 'ALL',
    'intersect'     : 'INTERSECT',
    'except'        : 'EXCEPT',
    'case'          : 'CASE',
    'when'          : 'WHEN',
    'end'           : 'END',
    'then'          : 'THEN',
    'else'          : 'ELSE',
    'pi'            : 'PI',
    'in'            : 'IN',
    'any'           : 'ANY',
    'some'          : 'SOME',
    'like'          : 'LIKE',
    'substring'     : 'SUBSTRING',
    'substr'        : 'SUBSTR',
    'trim'          : 'TRIM',
    'leading'       : 'LEADING',
    'trailing'      : 'TRAILING',
    'both'          : 'BOTH',
    'encode'        : 'ENCODE',
    'decode'        : 'DECODE',
    'abs'           : 'ABS',
    'cbrt'          : 'CBRT',
    'ceil'          : 'CEIL',
    'ceiling'       : 'CEILING',
    'degrees'       : 'DEGREES',
    'div'           : 'DIV',
    'factorial'     : 'FACTORIAL',
    'floor'         : 'FLOOR',
    'gcd'           : 'GCD',
    'ln'            : 'LN',
    'log'           : 'LOG',
    'mod'           : 'MOD',
    'power'         : 'POWER',
    'radians'       : 'RADIANS',
    'round'         : 'ROUND',
    'sign'          : 'SIGN',
    'sqrt'          : 'SQRT',
    'width_bucket'  : 'WIDTH_BUCKET',
    'trunc'         : 'TRUNC',
    'random'        : 'RANDOM',
    'exp'           : 'FEXP',
    'extract'       : 'EXTRACT',
    'now'           : 'NOW',
    'hour'          : 'HOUR',
    'minute'        : 'MINUTE',
    'second'        : 'SECOND',
    'year'          : 'YEAR',
    'month'         : 'MONTH',
    'day'           : 'DAY',
    'timestamp'     : 'TIMESTAMP',
    'interval'      : 'INTERVAL',
    'date_part'     : 'DATE_PART',
    'current_date'  : 'CURRENT_DATE',
    'current_time'  : 'CURRENT_TIME',
    'length'        : 'LENGTH',
    'sha256'        : 'SHA256',
    'date'          : 'DATE',
    'integer'       : 'INTEGER',
    'convert'       : 'CONVERT',
    'create'        : 'CREATE',
    'replace'       : 'REPLACE',
    'database'      : 'DATABASE',
    'databases'      : 'DATABASES',
    'if'            : 'IF',
    'exists'        : 'EXISTS',
    'owner'         : 'OWNER',
    'mode'          : 'MODE',
    'alter'         : 'ALTER',
    'drop'          : 'DROP',
    'show'          : 'SHOW',
    'rename'        : 'RENAME',
    'to'            : 'TO',
    'insert'        : 'INSERT',
    'update'        : 'UPDATE',
    'set'           : 'SET',
    'into'          : 'INTO',
    'values'        : 'VALUES',
    'table'         : 'TABLE',
    'from'          : 'FROM',
    'delete'        : 'DELETE',
    'acos'          : 'ACOS',
    'acosd'         : 'ACOSD',
    'asin'          : 'ASIN',
    'asind'         : 'ASIND',
    'atan'          : 'ATAN',
    'atand'         : 'ATAND',
    'atan2'         : 'ATAN2',
    'atan2d'        : 'ATAN2D',
    'cos'           : 'COS',
    'cosd'          : 'COSD',
    'cot'           : 'COT',
    'cotd'          : 'COTD',
    'sin'           : 'SIN',
    'sind'          : 'SIND',
    'tan'           : 'TAN',
    'tand'          : 'TAND',
    'sinh'          : 'SINH',
    'cosh'          : 'COSH',
    'tanh'          : 'TANH',
    'asinh'         : 'ASINH',
    'acosh'         : 'ACOSH',
    'atanh'         : 'ATANH',
    'get_byte'      : 'GETBYTE',
    'set_byte'      : 'SETBYTE',
    'inherits'      : 'INHERITS',
    'primary'       : 'PRIMARY',
    'key'           : 'KEY',
    'foreign'       : 'FOREIGN',
    'references'    : 'REFERENCES',
    'constraint'    : 'CONSTRAINT',
    'check'         : 'CHECK',
    'unique'        : 'UNIQUE',
    'default'       : 'DEFAULT',
    'smallint'      : 'SMALLINT',
    'bigint'        : 'BIGINT',
    'numeric'       : 'NUMERIC',
    'real'          : 'REAL',
    'double'        : 'DOUBLE',
    'money'         : 'MONEY',
    'character'     : 'CHARACTER',
    'varchar'       : 'VARCHAR',
    'char'          : 'CHAR',
    'text'          : 'TEXT',
    'time'          : 'TIME',
    'boolean'       : 'BOOLEAN',
    'varying'       : 'VARYING',
    'type'          : 'TYPE',
    'enum'          : 'ENUM',
    'add'           : 'ADD',
    'column'        : 'COLUMN',
    'use'           : 'USE',
    'md5'           : 'MD5',
    'decimal'       : 'DECIMAL',
    'current_user'  : 'CURRENT_USER',
    'session_user'  : 'SESSION_USER'
}

# LISTADO DE SIMBOLOS Y TOKENS
tokens = [
    'COMA',
    'ID',
    'PABRE',
    'PCIERRA',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'MODULO',
    'EXP',
    'PUNTO',
    'IGUAL',     
    'DIF',       
    'DIF1',      
    'MENOR',     
    'MENORIGUAL',
    'MAYOR',     
    'MAYORIGUAL',
    'NUMERO',
    'DECIMALN',
    'CADENA',
    'PCOMA',
    'IDALIAS',
    'raizCuadrada',
    'raizCubica',
    'BAnd',
    'BOr',
    'BXor',
    'BNot',
    'DesplazaI',
    'DesplazaD'
] + list(palabras_reservadas.values())

# EXPRESIONES REGULARES PARA TOKENS
t_COMA            = r','
t_PABRE           = r'\('
t_PCIERRA         = r'\)'
t_MAS             = r'\+'
t_MENOS           = r'-'
t_POR             = r'\*'
t_DIVIDIDO        = r'/'
t_MODULO          = r'\%'
t_EXP             = r'\^'
t_PUNTO           = r'\.'
t_IGUAL           = r'\='
t_DIF             = r'<>'
t_DIF1            = r'!='
t_MENOR           = r'<'
t_MENORIGUAL      = r'<='
t_MAYOR           = r'>'
t_MAYORIGUAL      = r'>='
t_PCOMA           = r';'
t_raizCuadrada    = r'\|\/'
t_raizCubica      = r'\|\|\/'
t_BAnd            = r'&'
t_BOr             = r'\|'
t_BXor            = r'#'
t_BNot            = r'~'
t_DesplazaI       = r'<<'
t_DesplazaD       = r'>>'

# TOKENS IGNORADOS
t_ignore = " \t"


def t_DECIMALN(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_NUMERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palabras_reservadas.get(t.value.lower(),'ID')    
    return t

def t_IDALIAS(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1] 
    return t 


def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1


# Function to count lines in input
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# Function to get column of a token
def get_column(p_input, p_token):
    line = p_input.rfind('\n', 0, p_token.lexpos) + 1
    column = (p_token.lexpos - line) + 1
    return column


# Function to print LEXICAL ERRORS
def t_error(t):
    global counter_lexical_error
    print("CARACTER ILEGAL '%s'" % t.value[0])
    err = open("reports/error_lexical.txt", "a+")
    txt = '<tr><td>' + str(counter_lexical_error) + '</td>'
    txt += '<td>' + str(t.value[0]) + '</td>'
    txt += '<td>' + 'Caracter ingresado no admitido.' + '</td>'
    txt += '<td>' + str(t.lexer.lineno) + '</td>'
    txt += '<td>' + str(get_column(t.lexer.lexdata, t)) + '</td><tr>\n'
    err.write(txt)
    err.close()
    counter_lexical_error += 1
    t.lexer.skip(1)


# BUILDING LEXICAL FILES
lexer = lex.lex(reflags=re.IGNORECASE)


# OPERATORS PRECEDENCE
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('nonassoc', 'IS', 'NULL'),
    ('left', 'MENORIGUAL', 'MAYORIGUAL', 'IGUAL', 'DIF', 'DIF1', 'MENOR', 'MAYOR'),
    ('nonassoc', 'BETWEEN', 'NOTB'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO', 'MODULO'),
    ('left', 'EXP'),
    ('right', 'UMENOS', 'UMAS')
)


# GRAMMAR DEFINITION
def p_init(t):
    """
        init            :   INSTRUCCIONES
    """
    t[0] = t[1]

    
def p_instrucciones1(t):
    """
        INSTRUCCIONES   :   INSTRUCCIONES INSTRUCCION
    """
    global reporte_gramatical
    reporte_gramatical.append("<INSTRUCCIONES> ::= <INSTRUCCIONES> <INSTRUCCION>")
    val = t[1].getInstruccion()
    val.append(t[2].getInstruccion())
    ret = Retorno(val, NodoAST("INST"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret


def p_instrucciones2(t):
    """
        INSTRUCCIONES   :   INSTRUCCION
    """
    global reporte_gramatical
    reporte_gramatical.append("<INSTRUCCIONES> ::= <INSTRUCCION>")
    val = [t[1].getInstruccion()]
    ret = Retorno(val, NodoAST("INST"))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret


def p_instruccion1(t):
    """
        INSTRUCCION     :   I_SELECT COMPLEMENTOSELECT
    """
    global reporte_gramatical
    reporte_gramatical.append("<INSTRUCCION> ::= <I_SELECT> <COMPLEMENTOSELECT>")
    if t[2] is None:
        t[0] = t[1]
    else:
        if isinstance(t[2].getInstruccion(), ComplementoSelectUnion):
            ret = Retorno(Union(t[1].getInstruccion(), t[2].getInstruccion().select), NodoAST("UNION"))
            ret.getNodo().setHijo(t[1].getNodo())
            ret.getNodo().setHijo(t[2].getNodo())
            t[0] = ret
        elif isinstance(t[2].getInstruccion(), ComplementoSelectUnionAll):
            ret = Retorno(UnionAll(t[1].getInstruccion(), t[2].getInstruccion().select), NodoAST("UNION ALL"))
            ret.getNodo().setHijo(t[1].getNodo())
            ret.getNodo().setHijo(t[2].getNodo())
            t[0] = ret
        elif isinstance(t[2].getInstruccion(), ComplementoSelectIntersect):
            ret = Retorno(Intersect(t[1].getInstruccion(), t[2].getInstruccion().select), NodoAST("INTERSECT"))
            ret.getNodo().setHijo(t[1].getNodo())
            ret.getNodo().setHijo(t[2].getNodo())
            t[0] = ret
        elif isinstance(t[2].getInstruccion(), ComplementoSelectIntersectALL):
            ret = Retorno(IntersectAll(t[1].getInstruccion(), t[2].getInstruccion().select), NodoAST("INTERSECT ALL"))
            ret.getNodo().setHijo(t[1].getNodo())
            ret.getNodo().setHijo(t[2].getNodo())
            t[0] = ret
        elif isinstance(t[2].getInstruccion(), ComplementoSelectExcept):
            ret = Retorno(Except(t[1].getInstruccion(), t[2].getInstruccion().select), NodoAST("EXCEPT"))
            ret.getNodo().setHijo(t[1].getNodo())
            ret.getNodo().setHijo(t[2].getNodo())
            t[0] = ret
        elif isinstance(t[2].getInstruccion(), ComplementoSelectExceptAll):
            ret = Retorno(ExceptAll(t[1].getInstruccion(), t[2].getInstruccion().select), NodoAST("EXCEPT ALL"))
            ret.getNodo().setHijo(t[1].getNodo())
            ret.getNodo().setHijo(t[2].getNodo())
            t[0] = ret

def p_instruccion2(t):
    """
        INSTRUCCION     :   I_REPLACE
                        |   I_CTABLE
                        |   I_CTYPE
                        |   I_DROP
                        |   I_INSERT
                        |   I_ALTERDB
                        |   I_UPDATE
                        |   I_SHOW
                        |   I_DELETE
                        |   I_USE
                        |   I_ALTERTB
    """
    t[0] = t[1]


def p_use(t):
    'I_USE           :   USE ID PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_USE> ::= "USE" "ID" ";"')
    ret = Retorno(UseDatabase(t[2]),NodoAST("USE"))
    ret.getNodo().setHijo(NodoAST(t[2]))
    t[0] = ret

    
# CREATE TYPE

def p_ctype(t):
    'I_CTYPE       : CREATE TYPE ID AS ENUM PABRE I_LVALUES PCIERRA PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_CTYPE> ::= "CREATE" "TYPE" "ID" "AS" "ENUM" "(" <I_LVALUES> ")" ";"')
    ret = Retorno(CreateType(t[3],t[7].getInstruccion()),NodoAST("CREATE TYPE"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(t[7].getNodo())
    t[0] = ret

def p_lcad1(t):
    'I_LVALUES          :   I_LVALUES COMA CONDI'
    global reporte_gramatical
    reporte_gramatical.append('<I_LVALUES> ::= <I_LVALUES> "," <CONDI>')
    val = t[1].getInstruccion()
    val.append(t[3].getInstruccion())
    ret = Retorno(val,NodoAST("VALOR"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())  
    t[0] = ret


def p_lcad2(t):
    'I_LVALUES          :   CONDI'
    global reporte_gramatical
    reporte_gramatical.append('<I_LVALUES> ::= <CONDI>')
    val = [t[1].getInstruccion()]
    ret = Retorno(val,NodoAST("VALOR"))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret
    

def p_Ilcad2(t):
    'CONDI          :   CONDICION'
    global reporte_gramatical
    reporte_gramatical.append('<CONDI> ::= <CONDICION>')
    t[0] = t[1]

# TERMINO CREATE TYPE


# CREATE TABLE

def p_ctable(t):
   'I_CTABLE        :   CREATE TABLE ID PABRE I_LTATRIBUTOS PCIERRA INHERITS PABRE ID PCIERRA PCOMA'
   global reporte_gramatical
   reporte_gramatical.append('<I_CTABLE> ::= "CREATE" "TABLE" "ID" "(" <I_LTATRIBUTOS> ")" <INHERITS> "(" "ID" ")" ";"')
   ret = Retorno(CreateTable(t[3],t[5].getInstruccion(),t[9]),NodoAST("CREATE TABLE"))
   ret.getNodo().setHijo(NodoAST(t[3]))
   ret.getNodo().setHijo(t[5].getNodo())
   ret.getNodo().setHijo(NodoAST("INHERITS"))
   ret.getNodo().setHijo(NodoAST(t[9]))
   t[0] = ret

def p_ctable1(t):
   'I_CTABLE        :   CREATE TABLE ID PABRE I_LTATRIBUTOS PCIERRA PCOMA'
   global reporte_gramatical
   reporte_gramatical.append('<I_CTABLE> ::= "CREATE" "TABLE" "ID" "(" <I_LTATRIBUTOS> ")" ";"')
   ret = Retorno(CreateTable(t[3],t[5].getInstruccion(),None),NodoAST("CREATE TABLE"))
   ret.getNodo().setHijo(NodoAST(t[3]))
   ret.getNodo().setHijo(t[5].getNodo())
   t[0] = ret

def p_tAtributos(t):
    'I_LTATRIBUTOS    : I_LTATRIBUTOS COMA I_TATRIBUTOS'
    global reporte_gramatical
    reporte_gramatical.append('<I_LTATRIBUTOS> ::= <I_LTATRIBUTOS> "," <I_TATRIBUTOS>')
    val = t[1].getInstruccion()
    val.append(t[3].getInstruccion())
    ret = Retorno(val,NodoAST("ATRIBUTOS"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())  
    t[0] = ret

def p_tAtributos1(t):
    'I_LTATRIBUTOS    : I_TATRIBUTOS'
    global reporte_gramatical
    reporte_gramatical.append('<I_LTATRIBUTOS> ::= <I_TATRIBUTOS>')
    val = [t[1].getInstruccion()]
    ret = Retorno(val,NodoAST("ATRIBUTOS"))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret

def p_atributosT(t):
    'I_TATRIBUTOS     : ID I_TIPO LI_LLAVES'
    global reporte_gramatical
    reporte_gramatical.append('<I_TATRIBUTOS> ::= "ID" <I_TIPO> <LI_LLAVES>')
    ret = Retorno(Campo(t[1],t[2].getInstruccion(),t[3].getInstruccion()),NodoAST(t[1]))
    ret.getNodo().setHijo(t[2].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_atributosTipo(t):
    'I_TATRIBUTOS     : ID I_TIPO'
    global reporte_gramatical
    reporte_gramatical.append('<I_TATRIBUTOS> ::= "ID" <I_TIPO>')
    ret = Retorno(Campo(t[1],t[2].getInstruccion(),None),NodoAST(t[1]))
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_atributosT1(t):
    'I_TATRIBUTOS     : PCONSTRAINT'
    global reporte_gramatical
    reporte_gramatical.append('<I_TATRIBUTOS> ::= <PCONSTRAINT>')
    t[0] = t[1]
    

def p_PConstraint(t):
    'PCONSTRAINT     : CONSTRAINT ID TIPO_CONSTRAINT'
    global reporte_gramatical
    reporte_gramatical.append('<PCONSTRAINT> ::= <CONSTRAINT> "," <TIPO_CONSTRAINT>')
    ret = Retorno(Constraint(t[2],t[3].getInstruccion()),NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(t[2]))
    t[0] = ret

def p_PConstrainTipo(t):
    'PCONSTRAINT     :  TIPO_CONSTRAINT'
    global reporte_gramatical
    reporte_gramatical.append('<PCONSTRAINT> ::= <TIPO_CONSTRAINT>')
    ret = Retorno(Constraint(None,t[1].getInstruccion()),NodoAST("CONSTRAINT"))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret


def p_TipoConstraintUnique(t):
    'TIPO_CONSTRAINT     :  UNIQUE PABRE I_LIDS PCIERRA' 
    global reporte_gramatical
    reporte_gramatical.append('<TIPO_CONSTRAINT> ::= "UNIQUE" "(" <I_LIDS> ")"')
    ret = Retorno(CreateUnique(None,t[3].getInstruccion()),NodoAST(t[1]))
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_TipoConstraintPrimaryKey(t):
    'TIPO_CONSTRAINT     :  PRIMARY KEY PABRE I_LIDS PCIERRA' 
    global reporte_gramatical
    reporte_gramatical.append('<TIPO_CONSTRAINT> ::= "PRIMARY" "KEY" "(" <I_LIDS> ")"')
    ret = Retorno(PK(t[4].getInstruccion()),NodoAST("PRIMARY KEY"))
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

def p_ipoConstraintCheck(t):
    'TIPO_CONSTRAINT        : CHECK CONDICION'
    global reporte_gramatical
    reporte_gramatical.append('<TIPO_CONSTRAINT> ::= "CHECK" <CONDICION>')
    ret = Retorno(CreateCheck(None,t[2].getInstruccion()),NodoAST(t[1]))
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_ipoConstraintForeignKey(t):
    'TIPO_CONSTRAINT        : FOREIGN KEY PABRE I_LIDS PCIERRA REFERENCES ID PABRE I_LIDS PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<TIPO_CONSTRAINT> ::= "FOREIGN" "KEY" "(" <I_LIDS> ")" "REFERENCES" "ID" "(" <I_LIDS> ")"')
    ret = Retorno(CreateFK(None,t[4].getInstruccion(),t[7],t[9].getInstruccion()),NodoAST("FOREIGN KEY"))
    ret.getNodo().setHijo(t[4].getNodo())
    ret.getNodo().setHijo(NodoAST(t[7]))
    ret.getNodo().setHijo(t[9].getNodo())
    t[0] = ret

def p_lIds(t):
    'I_LIDS           : I_LIDS COMA CONDICION'
    global reporte_gramatical
    reporte_gramatical.append('<I_LIDS> ::= <I_LIDS> "," <CONDICION>')
    val = t[1].getInstruccion()
    val.append(t[3].getInstruccion())
    ret = Retorno(val,NodoAST("VALOR"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())  
    t[0] = ret

def p_lIds1(t):
    'I_LIDS           : CONDICION'
    global reporte_gramatical
    reporte_gramatical.append('<I_LIDS> ::= <CONDICION>')
    val = [t[1].getInstruccion()]
    ret = Retorno(val,NodoAST("VALOR"))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret

def p_Lllave(t):
    'LI_LLAVES         : LI_LLAVES I_LLAVES'
    global reporte_gramatical
    reporte_gramatical.append('<LI_LLAVES> ::= <LI_LLAVES> <I_LLAVES>')
    val = t[1].getInstruccion()
    val.append(t[2].getInstruccion())
    ret = Retorno(val,NodoAST("CONDICION"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[2].getNodo())  
    t[0] = ret

def p_Lllave1(t):
    'LI_LLAVES         : I_LLAVES'
    global reporte_gramatical
    reporte_gramatical.append('<LI_LLAVES> ::= <I_LLAVES>')
    val = [t[1].getInstruccion()]
    ret = Retorno(val,NodoAST("CONDICION"))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret


def p_llave(t):
    'I_LLAVES         : PRIMARY KEY'
    global reporte_gramatical
    reporte_gramatical.append('<I_LLAVES> ::= "PRIMARY" "KEY" ')
    ret = Retorno(PK(None),NodoAST("PRIMARY KEY"))
    t[0] = ret

def p_llave2(t):
    'I_LLAVES         : REFERENCES ID PABRE I_CREFERENCE PCIERRA' 
    global reporte_gramatical
    reporte_gramatical.append('<I_LLAVES> ::= "REFERENCES" "ID" "(" <I_CREFERENCE> ")"')
    ret = Retorno(References(t[2],t[4].getInstruccion()),NodoAST(t[1]))
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

def p_llave3(t):
    'I_LLAVES         : DEFAULT CONDICION'
    global reporte_gramatical
    reporte_gramatical.append('<I_LLAVES> ::= "DEFAULT" <CONDICION>')
    ret = Retorno(Default(t[2].getInstruccion()),NodoAST(t[1]))
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_llave4(t):
    'I_LLAVES         : NULL'
    global reporte_gramatical
    reporte_gramatical.append('<LI_LLAVES> ::= "NULL"')
    ret = Retorno(NotNull(False),NodoAST("NULL"))
    t[0] = ret

def p_llave5(t):
    'I_LLAVES         : NOT NULL'
    global reporte_gramatical
    reporte_gramatical.append('<I_LLAVES> ::= "NOT" "NULL"')
    ret = Retorno(NotNull(True),NodoAST("NOT NULL"))
    t[0] = ret

def p_llave6(t):
    'I_LLAVES         : CONSTRAINT ID UNIQUE'
    global reporte_gramatical
    reporte_gramatical.append('<I_LLAVES> ::= "CONSTRAINT" "ID" "UNIQUE"')
    ret = Retorno(CreateUnique(None,t[2]),NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(t[2]))
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret


def p_llave9(t):
    'I_LLAVES         : UNIQUE'
    global reporte_gramatical
    reporte_gramatical.append('<I_LLAVES> ::= "UNIQUE"')
    ret = Retorno(CreateUnique(None,None),NodoAST(t[1]))
    t[0] = ret
    

def p_llave10(t):
    'I_LLAVES         : CHECK CONDICION'
    global reporte_gramatical
    reporte_gramatical.append('<I_LLAVES> ::= "CHECK" <CONDICION>')
    ret = Retorno(CreateCheck(None,t[2].getInstruccion()),NodoAST(t[1]))
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_llave11(t): 
    'I_LLAVES         : FOREIGN KEY PABRE I_LIDS PCIERRA REFERENCES ID PABRE I_LIDS PCIERRA '
    global reporte_gramatical
    reporte_gramatical.append('<I_LLAVES> ::= "FOREIGN" "KEY" "(" <I_LIDS> ")" "REFERENCES" "ID" "(" <I_LIDS> ")"')
    ret = Retorno(CreateFK(None,t[4].getInstruccion(),t[7],t[9].getInstruccion()),NodoAST("FOREIGN KEY"))
    ret.getNodo().setHijo(t[4].getNodo())
    ret.getNodo().setHijo(NodoAST(t[7]))
    ret.getNodo().setHijo(t[9].getNodo())
    t[0] = ret

def p_llave12(t):
    'I_LLAVES         : CONSTRAINT ID CHECK CONDICION'
    global reporte_gramatical
    reporte_gramatical.append('<I_LLAVES> ::= "CONSTRAINT" "ID" "CHECK" <CONDICION>')
    ret = Retorno(CreateCheck(t[2],t[4].getInstruccion()),NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(t[2]))
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

def p_cRef(t):
    'I_CREFERENCE     : I_CREFERENCE COMA ID'
    global reporte_gramatical
    reporte_gramatical.append('<I_CREFERENCE> ::= <I_CREFERENCE> "," "ID"')
    val = t[1].getInstruccion()
    val.append(t[3])
    ret = Retorno(val,NodoAST("VALOR"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret

def p_cRef2(t):
    'I_CREFERENCE     : ID'
    global reporte_gramatical
    reporte_gramatical.append('<I_CREFERENCE> ::= "ID"')
    val = [t[1]]
    ret = Retorno(val,NodoAST("VALOR"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    t[0] = ret
# TERMINA CREATE TABLE

# TIPOS DE DATOS

def p_tipo(t):
    'I_TIPO           : SMALLINT'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "SMALLINT" ') 
    ret = Retorno(TipoDato(None,None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    t[0] = ret

def p_tipo2(t):
    'I_TIPO           : INTEGER'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "INTEGER" ')
    ret = Retorno(TipoDato(None,None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    t[0] = ret

def p_tipo3(t):
    'I_TIPO           : BIGINT'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "BIGINT" ')
    ret = Retorno(TipoDato(None,None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    t[0] = ret
    

def p_tipo4(t):
    'I_TIPO           : DECIMAL PABRE NUMERO COMA NUMERO PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "DECIMAL" "(" "NUMERO" "," "NUMERO" ")" ')
    ret = Retorno(TipoDato(t[3],t[5],t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(str(t[1])))
    t[0] = ret

def p_tipo4_1(t):
    'I_TIPO           : DECIMAL'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "DECIMAL" ')
    ret = Retorno(TipoDato(None,None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    t[0] = ret

def p_tipo5(t):
    'I_TIPO           : NUMERIC'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "NUMERIC" ')
    ret = Retorno(TipoDato(None,None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    t[0] = ret

def p_tipo5_1(t):
    'I_TIPO           : NUMERIC PABRE NUMERO COMA NUMERO PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "NUMERIC" "(" "NUMERO" "," "NUMERO" ")" ')
    ret = Retorno(TipoDato(t[3],t[5],t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(str(t[3])))
    t[0] = ret

def p_tipo5_2(t):
    'I_TIPO           : NUMERIC PABRE NUMERO PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "NUMERIC" "(" "NUMERO" ")" ')
    ret = Retorno(TipoDato(t[3],None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(str(t[3])))
    t[0] = ret

def p_tipo6(t):
    'I_TIPO           : REAL'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "REAL" ')
    ret = Retorno(TipoDato(None,None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    t[0] = ret

def p_tipo7(t):
    'I_TIPO           : DOUBLE PABRE NUMERO PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "DOUBLE" "(" "NUMERO" ")" ')
    ret = Retorno(TipoDato(t[3],None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(str(t[3])))
    t[0] = ret

def p_tipo8(t):
    'I_TIPO           : MONEY'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "MONEY" ')
    ret = Retorno(TipoDato(None,None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    t[0] = ret

def p_tipo9(t):
    'I_TIPO           : CHARACTER VARYING PABRE NUMERO PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "CHARACTER" "VARYING" "(" "NUMERO" ")" ')
    ret = Retorno(TipoDato(t[4],None,"CHARACTER VARYING"),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST("CHARACTER VARYING"))
    ret.getNodo().setHijo(NodoAST(str(t[4])))
    t[0] = ret

def p_tipo9_1(t):
    'I_TIPO           : CHARACTER PABRE NUMERO PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "CHARACTER" "(" "NUMERO" ")" ')
    ret = Retorno(TipoDato(t[3],None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(str(t[3])))
    t[0] = ret

def p_tipo11(t):
    'I_TIPO           : VARCHAR PABRE NUMERO PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "VARCHAR" "(" "NUMERO" ")" ')
    ret = Retorno(TipoDato(t[3],None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(str(t[3])))
    t[0] = ret

def p_tipo22(t):
    'I_TIPO           : CHAR PABRE NUMERO PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "CHAR" "(" "NUMERO" ")" ')
    ret = Retorno(TipoDato(t[3],None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(str(t[3])))
    t[0] = ret

def p_tipo33(t):
    'I_TIPO           : TEXT'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "TEXT"')
    ret = Retorno(TipoDato(None,None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    t[0] = ret

def p_tipo44(t):
    'I_TIPO           : TIMESTAMP'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "TIMESTAMP"')
    ret = Retorno(TipoDato(None,None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    t[0] = ret

def p_tipo44_1(t):
    'I_TIPO           : TIMESTAMP PABRE NUMERO PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "TIMESTAMP" "(" "NUMERO" ")" ')
    ret = Retorno(TipoDato(t[3],None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(str(t[3])))
    t[0] = ret

def p_tipo55(t):
    'I_TIPO           : TIME'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "TIME"')
    ret = Retorno(TipoDato(None,None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    t[0] = ret

def p_tipo55_1(t):
    'I_TIPO           : TIME PABRE NUMERO PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "TIME" "(" "NUMERO" ")" ')
    ret = Retorno(TipoDato(t[3],None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(str(t[3])))
    t[0] = ret

def p_tipo66(t):
    'I_TIPO           : DATE'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "DATE"')
    ret = Retorno(TipoDato(None,None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    t[0] = ret

def p_tipo77(t):
    'I_TIPO           : INTERVAL I_FIELDS'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "INTERVAL" <I_FIELDS> ')
    ret = Retorno(TipoDato(None,None,t[2]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(t[2]))
    t[0] = ret

def p_tipo77_1(t):
    'I_TIPO           : INTERVAL I_FIELDS PABRE NUMERO PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "INTERVAL" <I_FIELDS> "(" "NUMERO" ")" ')
    ret = Retorno(TipoDato(t[4],None,t[2]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(t[2]))
    ret.getNodo().setHijo(NodoAST(str(t[4])))
    t[0] = ret

def p_tipo88(t):
    'I_TIPO           : BOOLEAN'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "BOOLEAN" ')
    ret = Retorno(TipoDato(None,None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    t[0] = ret

def p_tipoId(t):
    'I_TIPO           : ID'
    global reporte_gramatical
    reporte_gramatical.append('<I_TIPO> ::= "ID" ')
    ret = Retorno(TipoDato(None,None,t[1]),NodoAST("TIPO DATO"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    t[0] = ret

# TERMINA TIPO DE DATOS



def p_fields(t):
    'I_FIELDS         : MONTH'
    global reporte_gramatical
    reporte_gramatical.append('<I_FIELDS> ::= "MONTH" ')
    t[0] = t[1]

def p_fields1(t):
    'I_FIELDS         : HOUR'
    global reporte_gramatical
    reporte_gramatical.append('<I_FIELDS> ::= "HOUR" ')
    t[0] = t[1]

def p_fields2(t):
    'I_FIELDS         : MINUTE'
    global reporte_gramatical
    reporte_gramatical.append('<I_FIELDS> ::= "MINUTE" ')
    t[0] = t[1]

def p_fields3(t):
    'I_FIELDS         : SECOND'
    global reporte_gramatical
    reporte_gramatical.append('<I_FIELDS> ::= "SECOND" ')
    t[0] = t[1]

def p_fields4(t):
    'I_FIELDS         : YEAR'
    global reporte_gramatical
    reporte_gramatical.append('<I_FIELDS> ::= "YEAR" ')
    t[0] = t[1]


# CREATE DATABASE

def p_Replace(t):
    'I_REPLACE     : CREATE OR REPLACE DATABASE IF NOT EXISTS ID COMPLEMENTO_CREATE_DATABASE PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_REPLACE> ::= "CREATE" "OR" "REPLACE" "DATABASE" "IF" "NOT" "EXISTS" "ID" <COMPLEMENTO_CREATE_DATABASE> ";"')
    ret = Retorno(CreateDatabase(t[8],t[9].getInstruccion(),True,True),NodoAST("CREATE DATABASE"))
    ret.getNodo().setHijo(NodoAST(t[8]))
    ret.getNodo().setHijo(t[9].getNodo())
    t[0] = ret

def p_ReplaceV(t):
    'I_REPLACE     : CREATE OR REPLACE DATABASE IF NOT EXISTS ID PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_REPLACE> ::= "CREATE" "OR" "REPLACE" "DATABASE" "IF" "NOT" "EXISTS" "ID" ";"')
    ret = Retorno(CreateDatabase(t[8],None,True,True),NodoAST("CREATE DATABASE"))
    ret.getNodo().setHijo(NodoAST(t[8]))
    t[0] = ret



def p_Replace_1(t):
    'I_REPLACE     : CREATE OR REPLACE DATABASE ID COMPLEMENTO_CREATE_DATABASE PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_REPLACE> ::= "CREATE" "OR" "REPLACE" "DATABASE" "ID" <COMPLEMENTO_CREATE_DATABASE> ";"')
    ret = Retorno(CreateDatabase(t[5],t[6].getInstruccion(),False,True),NodoAST("CREATE DATABASE"))
    ret.getNodo().setHijo(NodoAST(t[5]))
    ret.getNodo().setHijo(t[6].getNodo())
    t[0] = ret

def p_Replace_1V(t):
    'I_REPLACE     : CREATE OR REPLACE DATABASE ID PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_REPLACE> ::= "CREATE" "OR" "REPLACE" "DATABASE" "ID"";"')
    ret = Retorno(CreateDatabase(t[5],None,False,True),NodoAST("CREATE DATABASE"))
    ret.getNodo().setHijo(NodoAST(t[5]))
    t[0] = ret
    

def p_Replace1(t):
    'I_REPLACE     : CREATE DATABASE IF NOT EXISTS ID COMPLEMENTO_CREATE_DATABASE PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_REPLACE> ::= "CREATE" "DATABASE" "IF" "NOT" "EXISTS" "ID" <COMPLEMENTO_CREATE_DATABASE> ";"')
    ret = Retorno(CreateDatabase(t[6],t[7].getInstruccion(),True,False),NodoAST("CREATE DATABASE"))
    ret.getNodo().setHijo(NodoAST(t[6]))
    ret.getNodo().setHijo(t[7].getNodo())
    t[0] = ret

def p_Replace1V(t):
    'I_REPLACE     : CREATE DATABASE IF NOT EXISTS ID PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_REPLACE> ::= "CREATE" "DATABASE" "IF" "NOT" "EXISTS" "ID" <COMPLEMENTO_CREATE_DATABASE> ";"')
    ret = Retorno(CreateDatabase(t[6],None,True,False),NodoAST("CREATE DATABASE"))
    ret.getNodo().setHijo(NodoAST(t[6]))
    t[0] = ret

def p_Replace2(t):
    'I_REPLACE     : CREATE DATABASE ID COMPLEMENTO_CREATE_DATABASE PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_REPLACE> ::= "CREATE" "DATABASE" "ID" <COMPLEMENTO_CREATE_DATABASE> ";"')
    ret = Retorno(CreateDatabase(t[3],t[4].getInstruccion(),False,False),NodoAST("CREATE DATABASE"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

def p_Replace2V(t):
    'I_REPLACE     : CREATE DATABASE ID PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_REPLACE> ::= "CREATE" "DATABASE" "ID" ";"')
    ret = Retorno(CreateDatabase(t[3],None,False,False),NodoAST("CREATE DATABASE"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret
 

def p_Owmod(t):
    'COMPLEMENTO_CREATE_DATABASE        : OWNER IGUAL CADENA MODE IGUAL NUMERO'
    global reporte_gramatical
    reporte_gramatical.append('<COMPLEMENTO_CREATE_DATABASE> ::= "OWNER" "=" "CADENA" "MODE" "=" "NUMERO"')
    ret = Retorno(OwnerMode(t[3],t[6]),NodoAST("VALORES"))
    ret.getNodo().setHijo(NodoAST("OWNER"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST("MODE"))
    ret.getNodo().setHijo(NodoAST(str(t[6])))
    t[0] = ret

def p_ModOwn(t):
    'COMPLEMENTO_CREATE_DATABASE        : MODE IGUAL NUMERO OWNER IGUAL CADENA '
    global reporte_gramatical
    reporte_gramatical.append('<COMPLEMENTO_CREATE_DATABASE> ::= "MODE" "=" "NUMERO" "OWNER" "=" "CADENA" ')
    ret = Retorno(OwnerMode(t[6],t[3]),NodoAST("VALORES"))
    ret.getNodo().setHijo(NodoAST("MODE"))
    ret.getNodo().setHijo(NodoAST(str(t[3])))
    ret.getNodo().setHijo(NodoAST("OWNER"))
    ret.getNodo().setHijo(NodoAST(t[6]))
    t[0] = ret

def p_Owmod1(t):
    'COMPLEMENTO_CREATE_DATABASE       : OWNER IGUAL CADENA'
    global reporte_gramatical
    reporte_gramatical.append('<COMPLEMENTO_CREATE_DATABASE> ::= "OWNER" "=" "CADENA" ')
    ret = Retorno(OwnerMode(t[3],None),NodoAST("VALORES"))
    ret.getNodo().setHijo(NodoAST("OWNER"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret


def p_OwmodN2(t):
    'COMPLEMENTO_CREATE_DATABASE       : MODE IGUAL NUMERO'
    global reporte_gramatical
    reporte_gramatical.append('<COMPLEMENTO_CREATE_DATABASE> ::= "MODE" "=" "NUMERO" ')
    ret = Retorno(OwnerMode(None,t[3]),NodoAST("VALORES"))
    ret.getNodo().setHijo(NodoAST("MODE"))
    ret.getNodo().setHijo(NodoAST(str(t[3])))
    t[0] = ret


# TERMINA CREATE DATABASE


# ALTER DATABASE

def p_tAlter(t):
    'I_ALTERDB    : ALTER DATABASE ID P_OPERACION_ALTERDB PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_ALTERDB> ::= "ALTER" "DATABASE" "ID" <P_OPERACION_ALTERDB> ";" ')
    ret = Retorno(AlterDB(t[3],t[4].getInstruccion()),NodoAST("ALTER DATABASE"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

def p_tAlterOpDB(t):
    'P_OPERACION_ALTERDB    : OWNER TO P_TIPOS_OWNER'
    global reporte_gramatical
    reporte_gramatical.append('<P_OPERACION_ALTERDB> ::= "OWNER" "TO" "ID" <P_TIPOS_OWNER>')
    ret = Retorno(AlterDBOwner(t[3]),NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret
    
def p_tAlterOpDB1(t):
    'P_OPERACION_ALTERDB    : MODE TO NUMERO'
    global reporte_gramatical
    reporte_gramatical.append('<P_OPERACION_ALTERDB> ::= "MODE" "TO" "NUMERO"')
    ret = Retorno(AlterDBMode(t[3]),NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(str(t[3])))
    t[0] = ret

def p_tAlterOpDB2(t):
    'P_OPERACION_ALTERDB    : RENAME TO CADENA'
    global reporte_gramatical
    reporte_gramatical.append('<P_OPERACION_ALTERDB> ::= "RENAME" "TO" "CADENA"')
    ret = Retorno(AlterDBRename(t[3]),NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret

def p_TipoOwner(t):
    'P_TIPOS_OWNER    : CADENA'
    global reporte_gramatical
    reporte_gramatical.append('<P_TIPOS_OWNER> ::= "CADENA"')
    t[0] = t[1]

def p_TipoOwner1(t):
    'P_TIPOS_OWNER    : CURRENT_USER'
    global reporte_gramatical
    reporte_gramatical.append('<P_TIPOS_OWNER> ::= "CURRENT_USER"')
    t[0] = t[1]

def p_TipoOwner2(t):
    'P_TIPOS_OWNER    : SESSION_USER'
    global reporte_gramatical
    reporte_gramatical.append('<P_TIPOS_OWNER> ::= "SESSION_USER"')
    t[0] = t[1]

def p_TipoOwner3(t):
    'P_TIPOS_OWNER    : ID'
    global reporte_gramatical
    reporte_gramatical.append('<P_TIPOS_OWNER> ::= "ID"')
    t[0] = t[1]


# TERMINA ALTER DATABASE

# ALTER TABLE 

def p_AlterTB(t):
    'I_ALTERTB    : ALTER TABLE ID L_ADD_COLUMNS PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_ALTERTB> ::= "ALTER" "TABLE" "ID" <L_ADD_COLUMNS> ";"')
    ret = Retorno(AlterAddC(t[3],t[4].getInstruccion()),NodoAST("ALTER TABLE"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(t[4].getNodo())  
    t[0] = ret

def p_AlterTB2(t):
    'I_ALTERTB    : ALTER TABLE ID L_DROP_COLUMNS PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_ALTERTB> ::= "ALTER" "TABLE" "ID" <L_DROP_COLUMNS> ";"')
    ret = Retorno(AlterD(t[3],t[4].getInstruccion()),NodoAST("ALTER TABLE"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(t[4].getNodo())  
    t[0] = ret

def p_AlterTB3(t):
    'I_ALTERTB    : ALTER TABLE ID ADD TIPOS_ALTER PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_ALTERTB> ::= "ALTER" "TABLE" "ID" "ADD" <TIPO_ALTER> ";"')
    ret = Retorno(AlterTBAdd(t[3],t[5].getInstruccion()),NodoAST("ALTER TABLE"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

def p_AlterTB4(t):
    'I_ALTERTB    : ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_ALTERTB> ::= "ALTER" "TABLE" "ID" "ALTER" "COLUMN" "ID" "SET" "NOT" "NULL" ";"')
    ret = Retorno(AlterNotNull(t[3],t[6]),NodoAST("ALTER TABLE"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[6]))
    ret.getNodo().setHijo(NodoAST("NOT NULL"))
    t[0] = ret

def p_AlterTB5(t):
    'I_ALTERTB    : ALTER TABLE ID DROP CONSTRAINT ID PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_ALTERTB> ::= "ALTER" "TABLE" "ID" "DROP" "CONTRAINT" "ID" ";"')
    ret = Retorno(AlterDConstraint(t[3],t[6]),NodoAST("ALTER TABLE"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST("DROP CONSTRAINT"))
    ret.getNodo().setHijo(NodoAST(t[6]))
    t[0] = ret

def p_AlterTB6(t):
    'I_ALTERTB    : ALTER TABLE ID L_COLUMN PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_ALTERTB> ::= "ALTER" "TABLE" "ID" <L_COLUMN> ";"')
    ret = Retorno(Alter(t[3],t[4].getInstruccion()),NodoAST("ALTER TABLE"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(t[4].getNodo())  
    t[0] = ret

def p_LColumn(t):
    'L_COLUMN    : L_COLUMN COMA P_COLUMN'
    global reporte_gramatical
    reporte_gramatical.append('<I_COLUMN> ::= <L_COLUMN> "," <P_COLUMN>')
    val = t[1].getInstruccion()
    val.append(t[3].getInstruccion())
    ret = Retorno(val,NodoAST("COLUMNA"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())  
    t[0] = ret

def p_LColumn1(t):
    'L_COLUMN    : P_COLUMN'
    global reporte_gramatical
    reporte_gramatical.append('<I_COLUMN> ::= <P_COLUMN>')
    val = [t[1].getInstruccion()]
    ret = Retorno(val,NodoAST("COLUMNA"))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret

def p_PColumn(t):
    'P_COLUMN    : ALTER COLUMN ID TYPE VARCHAR PABRE NUMERO PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<P_COLUMN> ::= "ALTER" "COLUMN" "ID" "TYPE" "VARCHAR" "(" "NUMERO" ")"')
    ret = Retorno(AlterType(t[3],t[7]),NodoAST("ALTER"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(str(t[7])))
    t[0] = ret

def p_TiposAlter(t):
    'TIPOS_ALTER    : CHECK CONDICION'
    global reporte_gramatical
    reporte_gramatical.append('<TIPOS_ALTER> ::= "CHECK" <CONDICION>')
    ret = Retorno(AlterCheck(None,t[2].getInstruccion()),NodoAST(t[1]))
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_TiposAlter1(t):
    'TIPOS_ALTER    : UNIQUE PABRE L_ID PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<TIPOS_ALTER> ::= "UNIQUE" "(" <L_ID> ")" ')
    ret = Retorno(AlterUnique(None,t[3].getInstruccion()),NodoAST(t[1]))
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret


def p_TiposAlter2(t):
    'TIPOS_ALTER    : FOREIGN KEY PABRE L_ID PCIERRA REFERENCES ID PABRE L_ID PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<TIPOS_ALTER> ::= "FOREIGN" "KEY" "("<L_ID>")" "REFERENCES" "ID" "(" <L_ID> ")"')
    ret = Retorno(AlterFK(None,t[4].getInstruccion(),t[7],t[9].getInstruccion()),NodoAST("FOREIGN KEY"))
    ret.getNodo().setHijo(t[4].getNodo())
    ret.getNodo().setHijo(NodoAST(t[7]))
    ret.getNodo().setHijo(t[9].getNodo())
    t[0] = ret



def p_TiposAlter3(t):
    'TIPOS_ALTER    : CONSTRAINT ID CHECK CONDICION'
    global reporte_gramatical
    reporte_gramatical.append('<TIPOS_ALTER> ::= "CONSTRAINT" "ID" "CHECK" <CONDICION>')
    ret = Retorno(AlterCheck(t[2],t[4].getInstruccion()),NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[2]))
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

def p_TiposAlter4(t):
    'TIPOS_ALTER    : CONSTRAINT ID UNIQUE PABRE L_ID PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<TIPOS_ALTER> ::= "CONSTRAINT" "ID" "UNIQUE" "(" <L_ID> ")"')
    ret = Retorno(AlterUnique(t[2],t[5].getInstruccion()),NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[2]))
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

def p_TiposAlter5(t):
    'TIPOS_ALTER    : CONSTRAINT ID FOREIGN KEY PABRE L_ID PCIERRA REFERENCES ID PABRE L_ID PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<TIPOS_ALTER> ::= "CONSTRAINT" "ID" "FOREIGN" "KEY" "(" <L_ID> ")" "REFERENCES" "ID" "(" <L_ID> ")"') 
    ret = Retorno(AlterFK(t[2],t[6].getInstruccion(),t[9],t[11].getInstruccion()),NodoAST("FOREIGN KEY"))
    ret.getNodo().setHijo(NodoAST(t[2]))
    ret.getNodo().setHijo(t[6].getNodo())
    ret.getNodo().setHijo(NodoAST(t[9]))
    ret.getNodo().setHijo(t[11].getNodo())
    t[0] = ret

def p_LID(t):
    'L_ID    : L_ID COMA ID'
    global reporte_gramatical
    reporte_gramatical.append('<L_ID> ::= <L_ID> "," "ID" ')
    val = t[1].getInstruccion()
    val.append(t[3])
    ret = Retorno(val,NodoAST("VALOR"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret

def p_LID1(t):
    'L_ID    : ID'
    global reporte_gramatical
    reporte_gramatical.append('<L_ID> ::= "ID" ')
    val = [t[1]]
    ret = Retorno(val,NodoAST("VALOR"))
    ret.getNodo().setHijo(NodoAST(t[1]))
    t[0] = ret



def p_L_DropColumns(t):
    'L_DROP_COLUMNS    : L_DROP_COLUMNS COMA DROP_COLUMN'
    global reporte_gramatical
    reporte_gramatical.append('<L_DROP_COLUMNS> ::= <L_DROP_COLUMNS> "," <DROP_COLUMN> ')
    val = t[1].getInstruccion()
    val.append(t[3].getInstruccion())
    ret = Retorno(val,NodoAST("DROP"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())  
    t[0] = ret

def p_L_DropColumns1(t):
    'L_DROP_COLUMNS    : DROP_COLUMN'
    global reporte_gramatical
    reporte_gramatical.append('<L_DROP_COLUMNS> ::= <DROP_COLUMN>')
    val = [t[1].getInstruccion()]
    ret = Retorno(val,NodoAST("DROP"))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret

def p_L_DropColumn(t):
    'DROP_COLUMN    : DROP COLUMN ID'
    global reporte_gramatical
    reporte_gramatical.append('<DROP_COLUMN> ::= "DROP" "COLUMN" "ID" ')
    ret = Retorno(AlterDrop(t[3]),NodoAST("COLUMNA"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret

def p_L_AddColumns(t):
    'L_ADD_COLUMNS    : L_ADD_COLUMNS COMA ADD_COLUMN'
    global reporte_gramatical
    reporte_gramatical.append('<L_ADD_COLUMNS> ::= <L_ADD_COLUMNS> "," <ADD_COLUMN> ')
    val = t[1].getInstruccion()
    val.append(t[3].getInstruccion())
    ret = Retorno(val,NodoAST("ADD"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())  
    t[0] = ret

def p_L_AddColumns1(t):
    'L_ADD_COLUMNS    : ADD_COLUMN'
    global reporte_gramatical
    reporte_gramatical.append('<L_ADD_COLUMNS> ::= <ADD_COLUMN> ')
    val = [t[1].getInstruccion()]
    ret = Retorno(val,NodoAST("ADD"))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret

def p_AddColumn(t):
    'ADD_COLUMN    : ADD COLUMN ID I_TIPO'
    global reporte_gramatical
    reporte_gramatical.append('<ADD_COLUMN> ::= "ADD" "COLUMN" "ID" <I_TIPO> ')
    ret = Retorno(AlterADD(t[3],t[4].getInstruccion()),NodoAST("COLUMNA"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

# TERMINA ALTER TABLE

# DROP TABLE

def p_dropTB(t):
    'I_DROP      : DROP TABLE ID PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_DROP> ::= "DROP" "TABLE" "ID" ";" ')
    ret = Retorno(DropT(t[3]),NodoAST("DROP"))
    ret.getNodo().setHijo(NodoAST("TABLE"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret

# TERMINA DROP TABLE

# DROP DATABASE
def p_dropDB(t):
    'I_DROP    : DROP DATABASE IF EXISTS ID PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_DROP> ::= "DROP" "DATABASE" "IF" "EXISTS" "ID" ";" ')
    ret = Retorno(IfExist1(t[5],True),NodoAST("DROP"))
    ret.getNodo().setHijo(NodoAST("DATABASE"))
    ret.getNodo().setHijo(NodoAST(t[5]))
    t[0] = ret


def p_DropDBid(t):
    'I_DROP     : DROP DATABASE ID PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_DROP> ::= "DROP" "DATABASE" "ID" ";" ')
    ret = Retorno(IfExist1(t[3],False),NodoAST("DROP"))
    ret.getNodo().setHijo(NodoAST("DATABASE"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret

# TERMINA DROP DATABASE




# INSERT
def p_insertTB(t):
    'I_INSERT      : INSERT INTO ID VALUES PABRE I_LVALT PCIERRA PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_INSERT> ::= "INSERT" "INTO" "ID" "VALUES" "(" <I_LVALT> ")" ";" ')
    ret = Retorno(Insert(t[3],None,t[6].getInstruccion()),NodoAST("INSERT"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(t[6].getNodo())
    t[0] = ret

def p_insertTB1(t):
    'I_INSERT      : INSERT INTO ID PABRE I_LVALT PCIERRA VALUES PABRE I_LVALT PCIERRA PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_INSERT> ::= "INSERT" "INTO" "ID" "(" <I_LVALT> ")" "VALUES "(" <I_LVARLT> ")" ";" ')
    ret = Retorno(Insert(t[3],t[5].getInstruccion(),t[9].getInstruccion()),NodoAST("INSERT"))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(t[5].getNodo())
    ret.getNodo().setHijo(t[9].getNodo())
    t[0] = ret

def p_lValt(t):
    'I_LVALT       : I_LVALT COMA I_VALTAB'
    global reporte_gramatical
    reporte_gramatical.append('<L_LVALT> ::= <I_LVALT> "," <I_VALTAB>')
    val = t[1].getInstruccion()
    val.append(t[3].getInstruccion())
    ret = Retorno(val,NodoAST("VALOR"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())  
    t[0] = ret

def p_lValt1(t):
    'I_LVALT       : I_VALTAB'
    global reporte_gramatical
    reporte_gramatical.append('<L_LVALT> ::= <I_VALTAB>')
    val = [t[1].getInstruccion()]
    ret = Retorno(val,NodoAST("VALOR"))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret

def p_valTab(t):
    'I_VALTAB      : CONDICION'
    global reporte_gramatical
    reporte_gramatical.append('<I_VALTAB> ::= <CONDICION>')
    t[0] = t[1]

def p_valTabMd51(t):
    'I_VALTAB      : MD5 PABRE CADENA PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<I_VALTAB> ::= "MD5" "(" "CADENA" ")"')
    ret = Retorno(Md5(t[3]),NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret

# TERMINA INSERT


# UPDATE  

def p_update(t):
    'I_UPDATE      : UPDATE ID SET I_LUPDATE PWHERE PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_UPDATE> ::= "UPDATE" "ID" "SET" <I_LUPDATE> <PWHERE> ";"')
    ret = Retorno(Update(t[2],t[4].getInstruccion(),t[5].getInstruccion()),NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(t[2]))
    ret.getNodo().setHijo(t[4].getNodo())
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

def p_lUpdate(t):
    'I_LUPDATE     : I_LUPDATE COMA I_VALUPDATE'
    global reporte_gramatical
    reporte_gramatical.append('<I_LUPDATE> ::= <I_LUPDATE> "," <I_VALUPDATE>')
    val = t[1].getInstruccion()
    val.append(t[3].getInstruccion())
    ret = Retorno(val,NodoAST("VALOR"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())  
    t[0] = ret

def p_lUpdate1(t):
    'I_LUPDATE     : I_VALUPDATE'
    global reporte_gramatical
    reporte_gramatical.append('<I_LUPDATE> ::= <I_VALUPDATE>')
    val = [t[1].getInstruccion()]
    ret = Retorno(val,NodoAST("VALOR"))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret

def p_valUpdate(t):
    'I_VALUPDATE   : CONDICION'
    global reporte_gramatical
    reporte_gramatical.append('<I_VALUPDATE> ::= <CONDICION>')
    t[0] = t[1]


def p_valUpdateT(t):
    'I_VALUPDATE   : CONDICION IGUAL FTRIGONOMETRICASUP PABRE LNUM PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<I_VALUPDATE> ::= <CONDICION> "=" <FTRIGONOMETRICASUP> "(" <LNUM> ")"')
    ret = Retorno(UpdateTrigo(t[1].getInstruccion(),t[3],t[5].getInstruccion()),NodoAST("UPDATE"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

    
def p_valTabMd5(t):
    'I_VALUPDATE      : MD5 PABRE CADENA PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append('<I_VALUPDATE> ::= "MD5" "(" "CADENA" ")"')
    ret = Retorno(Md5(t[3]),NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret

def p_FTUP(t):
    'FTRIGONOMETRICASUP   : ACOSD'
    global reporte_gramatical
    reporte_gramatical.append('<FTRIGONOMETRICASUP> ::= "ACOSD" ')
    t[0] = 'ACOSD'

def p_FTUP1(t):
    'FTRIGONOMETRICASUP   : ASIN'
    global reporte_gramatical
    reporte_gramatical.append('<FTRIGONOMETRICASUP> ::= "ASIN" ')
    t[0] = 'ASIN'

# TERMINA UPDATE




# SHOW

def p_show(t):
    'I_SHOW       : SHOW DATABASES PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_SHOW> ::= "SHOW" "DATABASE" ";" ')
    ret = Retorno(Show(t[2]),NodoAST("SHOW"))
    #ret.getNodo().setHijo(NodoAST(t[2]))
    t[0] = ret

# TERMINA SHOW

# DELETE

def p_delete(t):
    'I_DELETE     : DELETE FROM ID PWHERE PCOMA'
    global reporte_gramatical
    reporte_gramatical.append('<I_DELETE> ::= "DELETE" "FROM" "ID" <PWHERE> ";" ')
    ret = Retorno(DeleteFrom(t[3],t[4].getInstruccion()),NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

# TERMINA DELETE

#--------------------------------------------------------------------------------

def p_ISelect(t):
    'I_SELECT  :   SELECT VALORES PFROM LCOMPLEMENTOS'
    global reporte_gramatical
    reporte_gramatical.append("<I_SELECT> ::= \"SELECT\" <VALORES> <PFROM> <LCOMPLEMENTOS>")
    if isinstance(t[2], str):
        ret = Retorno(Select3(t[2], t[3].getInstruccion(), t[4].getInstruccion(), None, False), NodoAST("SELECT"))
        ret.getNodo().setHijo(NodoAST(t[2]))
        ret.getNodo().setHijo(t[3].getNodo())
        ret.getNodo().setHijo(t[4].getNodo())
        t[0] = ret
    else:
        ret = Retorno(Select3(t[2].getInstruccion(), t[3].getInstruccion(), t[4].getInstruccion(), None, False), NodoAST("SELECT"))
        ret.getNodo().setHijo(t[2].getNodo())
        ret.getNodo().setHijo(t[3].getNodo())
        ret.getNodo().setHijo(t[4].getNodo())
        t[0] = ret
    
    
def p_ISelect4(t):
    'I_SELECT  :   SELECT DISTINCT VALORES PFROM LCOMPLEMENTOS'
    global reporte_gramatical
    reporte_gramatical.append("<I_SELECT> ::= \"SELECT\" \"DISTINCT\" <VALORES> <PFROM> <LCOMPLEMENTOS>")
    if isinstance(t[3], str):
        ret = Retorno(Select3(t[3], t[4].getInstruccion(), None, t[5].getInstruccion(), True), NodoAST("SELECT"))
        ret.getNodo().setHijo(NodoAST(t[3]))
        ret.getNodo().setHijo(t[4].getNodo())
        ret.getNodo().setHijo(t[5].getNodo())
        t[0] = ret
    else:
        ret = Retorno(Select3(t[3].getInstruccion(), t[4].getInstruccion(), None, t[5].getInstruccion(), True), NodoAST("SELECT"))
        ret.getNodo().setHijo(t[3].getNodo())
        ret.getNodo().setHijo(t[4].getNodo())
        ret.getNodo().setHijo(t[5].getNodo())
        t[0] = ret

def p_ISelect2(t):
    'I_SELECT  :   SELECT VALORES PFROM PWHERE LCOMPLEMENTOS'
    global reporte_gramatical
    reporte_gramatical.append("<I_SELECT> ::= \"SELECT\" <VALORES> <PFROM> <PWHERE> <LCOMPLEMENTOS>")
    if isinstance(t[2], str):
        ret = Retorno(Select3(t[2], t[3].getInstruccion(), t[4].getInstruccion(), t[5].getInstruccion(), False), NodoAST("SELECT"))
        ret.getNodo().setHijo(NodoAST(t[2]))
        ret.getNodo().setHijo(t[3].getNodo())
        ret.getNodo().setHijo(t[4].getNodo())
        ret.getNodo().setHijo(t[5].getNodo())
        t[0] = ret
    else:
        ret = Retorno(Select3(t[2].getInstruccion(), t[3].getInstruccion(), t[4].getInstruccion(), t[5].getInstruccion(), False), NodoAST("SELECT"))
        ret.getNodo().setHijo(t[2].getNodo())
        ret.getNodo().setHijo(t[3].getNodo())
        ret.getNodo().setHijo(t[4].getNodo())
        ret.getNodo().setHijo(t[5].getNodo())
        t[0] = ret

def p_ISelect6(t):
    'I_SELECT  :   SELECT DISTINCT VALORES PFROM PWHERE LCOMPLEMENTOS'
    global reporte_gramatical
    reporte_gramatical.append("<I_SELECT> ::= \"SELECT\" \"DISTINCT\" <VALORES> <PFROM> <PWHERE> <LCOMPLEMENTOS>")
    if isinstance(t[3], str):
        ret = Retorno(Select3(t[3], t[4].getInstruccion(), t[5].getInstruccion(), t[6].getInstruccion(), True), NodoAST("SELECT"))
        ret.getNodo().setHijo(NodoAST(t[3]))
        ret.getNodo().setHijo(t[4].getNodo())
        ret.getNodo().setHijo(t[5].getNodo())
        ret.getNodo().setHijo(t[6].getNodo())
        t[0] = ret
    else:
        ret = Retorno(Select3(t[3].getInstruccion(), t[4].getInstruccion(), t[5].getInstruccion(), t[6].getInstruccion(), True), NodoAST("SELECT"))
        ret.getNodo().setHijo(t[3].getNodo())
        ret.getNodo().setHijo(t[4].getNodo())
        ret.getNodo().setHijo(t[5].getNodo())
        ret.getNodo().setHijo(t[6].getNodo())
        t[0] = ret

def p_ISelect3(t):
    'I_SELECT  :   SELECT VALORES PFROM PWHERE'
    global reporte_gramatical
    reporte_gramatical.append("<I_sELECT> ::= \"SELECT\" \DISTINCT\" <VALORES> <PFROM> <PWHERE>")
    if isinstance(t[2], str):
        ret = Retorno(Select3(t[2], t[3].getInstruccion(), t[4].getInstruccion(), None, False), NodoAST("SELECT"))
        ret.getNodo().setHijo(NodoAST(t[2]))
        ret.getNodo().setHijo(t[3].getNodo())
        ret.getNodo().setHijo(t[4].getNodo())
        t[0] = ret
    else:
        ret = Retorno(Select3(t[2].getInstruccion(), t[3].getInstruccion(), t[4].getInstruccion(), None, False), NodoAST("SELECT"))
        ret.getNodo().setHijo(t[2].getNodo())
        ret.getNodo().setHijo(t[3].getNodo())
        ret.getNodo().setHijo(t[4].getNodo())
        t[0] = ret


def p_ISelect7(t):
    'I_SELECT  :   SELECT DISTINCT VALORES PFROM PWHERE'
    global reporte_gramatical
    reporte_gramatical.append("<I_sELECT> ::= \"SELECT\" \DISTINCT\" <VALORES> <PFROM> <PWHERE>")
    if isinstance(t[3], str):
        ret = Retorno(Select3(t[3], t[4].getInstruccion(), t[5].getInstruccion(), None, True), NodoAST("SELECT"))
        ret.getNodo().setHijo(NodoAST(t[3]))
        ret.getNodo().setHijo(t[4].getNodo())
        ret.getNodo().setHijo(t[5].getNodo())
        t[0] = ret
    else:
        ret = Retorno(Select3(t[3].getInstruccion(), t[4].getInstruccion(), t[5].getInstruccion(), None, True), NodoAST("SELECT"))
        ret.getNodo().setHijo(t[3].getNodo())
        ret.getNodo().setHijo(t[4].getNodo())
        ret.getNodo().setHijo(t[5].getNodo())
        t[0] = ret

def p_ISelect5(t):
    'I_SELECT  :   SELECT DISTINCT VALORES PFROM'
    global reporte_gramatical
    reporte_gramatical.append("<I_SELECT> ::= \"SELECT\" \"DISTINCT\" <VALORES> <PFROM>")
    if isinstance(t[3], str):
        ret = Retorno(Select3(t[3],t[4].getInstruccion(),None,None,True),NodoAST("SELECT"))
        ret.getNodo().setHijo(NodoAST(t[3]))
        ret.getNodo().setHijo(t[4].getNodo())
        t[0] = ret
    else:
        ret = Retorno(Select3(t[3].getInstruccion(), t[4].getInstruccion(), None, None, None), NodoAST("SELECT"))
        ret.getNodo().setHijo(t[3].getNodo())
        ret.getNodo().setHijo(t[4].getNodo())
        t[0] = ret

def p_ISelect1(t):
    'I_SELECT  :   SELECT VALORES PFROM'
    global reporte_gramatical
    reporte_gramatical.append("<I_SELECT> ::= \"SELECT\" <VALORES> <PFROM>")
    if isinstance(t[2], str):
        ret = Retorno(Select3(t[2],t[3].getInstruccion(),None,None,False),NodoAST("SELECT"))
        ret.getNodo().setHijo(NodoAST(t[2]))
        ret.getNodo().setHijo(t[3].getNodo())
        t[0] = ret
    else:
        ret = Retorno(Select3(t[2].getInstruccion(), t[3].getInstruccion(), None, None, False), NodoAST("SELECT"))
        ret.getNodo().setHijo(t[2].getNodo())
        ret.getNodo().setHijo(t[3].getNodo())
        t[0] = ret    

def p_ISelect8(t):
    'I_SELECT   :   SELECT VALORES'
    global reporte_gramatical
    reporte_gramatical.append("<I_SELECT> ::= \"SELECT\" <VALORES>")
    if isinstance(t[2], str):
        ret = Retorno(Select3(t[2],None,None,None,False),NodoAST("SELECT"))
        ret.getNodo().setHijo(NodoAST(t[2]))
        t[0] = ret
    else:
        ret = Retorno(Select3(t[2].getInstruccion(), None, None, None, False), NodoAST("SELECT"))
        ret.getNodo().setHijo(t[2].getNodo())
        t[0] = ret


def p_ISelect9(t):
    'I_SELECT   :   SELECT DISTINCT VALORES '
    global reporte_gramatical
    reporte_gramatical.append("<I_SELECT> ::= \"SELECT\" \"DISTINCT\" <VALORES>")
    if isinstance(t[2], str):
        ret = Retorno(Select3(t[2], None, None, None, True), NodoAST("SELECT"))
        ret.getNodo().setHijo(NodoAST(t[2]))
        t[0] = ret
    else:
        ret = Retorno(Select3(t[2].getInstruccion(), None, None, None, True), NodoAST("SELECT"))
        ret.getNodo().setHijo(t[2].getNodo())
        t[0] = ret

def p_LComplementoS(t):
    'LCOMPLEMENTOS  :   LCOMPLEMENTOS COMPLEMENTO  '
    global reporte_gramatical
    reporte_gramatical.append("<LCOMPLEMENTOS> ::= <LCOMPLEMENTOS> <COMPLEMENTO>")
    val = t[1].getInstruccion()
    val.append(t[2].getInstruccion())
    ret = Retorno(val, NodoAST('COMPLEMENTO'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_LComplementoS1(t):
    'LCOMPLEMENTOS  :   COMPLEMENTO  '
    global reporte_gramatical
    reporte_gramatical.append("<LCOMPLEMENTOS> ::= <COMPLEMENTO>")
    val = [t[1].getInstruccion()]
    ret = Retorno(val, NodoAST('COMPLEMENTO'))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret

def p_ComplementoH(t):
    'COMPLEMENTO  :   PGROUPBY'
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTO> ::= <PGROUPBY>")
    t[0] = t[1]

def p_ComplementoHa(t):
    'COMPLEMENTO  :   PHAVING'
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTO> ::= <PHAVING>")
    t[0] = t[1]

def p_ComplementoO(t):
    'COMPLEMENTO  :   PORDERBY  '
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTO> ::= <PORDERBY>")
    t[0] = t[1]

def p_ComplementoL(t):
    'COMPLEMENTO  :   PLIMIT    '
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTO> ::= <PLIMIT>")
    t[0] = t[1]

def p_ComplementoSelectUnion(t):
    'COMPLEMENTOSELECT  : UNION I_SELECT PCOMA  '
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTOSELECT> ::= \"UNION\" <I_SELECT> \";\"")
    ret = Retorno(ComplementoSelectUnion(t[2].getInstruccion()), t[2].getNodo())
    t[0] = ret

def p_ComplementoSelectUnionAll(t):
    'COMPLEMENTOSELECT  : UNION ALL I_SELECT PCOMA '
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTOSELECT> ::= \"UNION\" \"ALL\" <I_SELECT> \";\"")
    ret = Retorno(ComplementoSelectUnionAll(t[3].getInstruccion()), t[3].getNodo())
    t[0] = ret

def p_ComplementoSelectIntersect(t):
    'COMPLEMENTOSELECT  : INTERSECT I_SELECT PCOMA '
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTOSELECT> ::= \"INTERSECT\" <I_SELECT> \";\"")
    ret = Retorno(ComplementoSelectIntersect(t[2].getInstruccion()), t[2].getNodo())
    t[0] = ret

def p_ComplementoSelectIntersectALL(t):
    'COMPLEMENTOSELECT  : INTERSECT ALL I_SELECT PCOMA '
    reporte_gramatical.append("<COMPLEMENTOSELECT> ::= \"INTERSECT\" \"ALL\" <I_SELECT> \";\"")
    ret = Retorno(ComplementoSelectIntersectALL(t[3].getInstruccion()), t[3].getNodo())
    t[0] = ret

def p_ComplementoSelectExcept(t):
    'COMPLEMENTOSELECT  : EXCEPT I_SELECT PCOMA '
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTOSELECT> ::= \"EXCEPT\" <I_SELECT> \";\"")
    ret = Retorno(ComplementoSelectExcept(t[2].getInstruccion()), t[2].getNodo())
    t[0] = ret

def p_ComplementoSelectExceptAll(t):
    'COMPLEMENTOSELECT  : EXCEPT ALL I_SELECT PCOMA '
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTOSELECT> ::= \"EXCEPT\" \"ALL\" <I_SELECT> \";\"")
    ret = Retorno(ComplementoSelectExceptAll(t[3].getInstruccion()), t[3].getNodo())
    t[0] = ret

def p_ComplementoSelectExceptPcoma(t):
    'COMPLEMENTOSELECT  : PCOMA '
    # INSTRUCCION COMPLEMENTOSELECTEXCEPTPCOMA
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTOSELECT> ::= \";\"")
    t[0] = None

def p_Limit(t):
    'PLIMIT  :   LIMIT CONDICION    '
    global reporte_gramatical
    reporte_gramatical.append("<PLIMIT> ::= \"LIMIT\" <CONDICION>")
    ret = Retorno(Limit(t[2].getInstruccion(), None), NodoAST('LIMIT'))
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_LimitOff(t):
    'PLIMIT  :   LIMIT CONDICION OFFSET CONDICION   '
    global reporte_gramatical
    reporte_gramatical.append("<PLIMIT> ::= \"LIMIT\" <CONDICION> \"OFFSET\" <CONDICION>")
    ret = Retorno(Limit(t[2].getInstruccion(), t[4].getInstruccion()), NodoAST('LIMIT'))
    ret.getNodo().setHijo(t[2].getNodo())
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

def p_OrderBy(t):
    'PORDERBY  :   ORDER BY LCOMPLEMENTOORDERBY '
    global reporte_gramatical
    reporte_gramatical.append("<PORDERBY> ::= \"ORDER\" \"BY\" <LCOMPLEMENTOORDERBY>")
    ret = Retorno(OrderBy(t[3].getInstruccion(), None), NodoAST('ORDER BY'))
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_ComplementoOrderL(t):
    'LCOMPLEMENTOORDERBY  :   LCOMPLEMENTOORDERBY COMA COMPLEMENTOORDERBY  '
    global reporte_gramatical
    reporte_gramatical.append("<LCOMPLEMENTOORDERBY> ::= <LCOMPLEMENTOORDERBY> \",\" <COMPLEMENTOORDERBY>")
    val = t[1].getInstruccion()
    val.append(t[3].getInstruccion())
    ret = Retorno(val, NodoAST('COMP ORDER'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_ComplementoOrderL1(t):
    'LCOMPLEMENTOORDERBY  :   COMPLEMENTOORDERBY    '
    global reporte_gramatical
    reporte_gramatical.append("<LCOMPLEMENTOORDERBY> ::= <COMPLEMENTOORDERBY>")
    val = [t[1].getInstruccion()]
    ret = Retorno(val, NodoAST('COMP ORDER'))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret

def p_ComplementoOrderCI(t):
    'COMPLEMENTOORDERBY  :   CONDICION COMPLEMENTOORDERBY1    '
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTOORDERBY> ::= <CONDICION> <COMPLEMENTOORDERBY1>")
    ret = Retorno(AuxiliarOrderBy(t[1].getInstruccion(), t[1]), NodoAST('COMP'))
    ret.getNodo().setHijo(t[1].getNodo())
    if t[2] == 'A':
        ret.getNodo().setHijo(NodoAST('ASC'))
    elif t[2] == 'D':
        ret.getNodo().setHijo(NodoAST('DESC'))
    elif t[2] == 'ANF':
        ret.getNodo().setHijo(NodoAST('ASC NULLS FIRST'))
    elif t[2] == 'ANL':
        ret.getNodo().setHijo(NodoAST('ASC NULLS LAST'))
    elif t[2] == 'DNF':
        ret.getNodo().setHijo(NodoAST('DESC NULLS FIRST'))
    elif t[2] == 'DNL': 
        ret.getNodo().setHijo(NodoAST('DESC NULLS LAST'))
    t[0] = ret

def p_ComplementoOrderCOBC(t):
    'COMPLEMENTOORDERBY1  :   COMPLEMENTOORDER   '
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTOORDERBY1> ::= <COMPLEMENTOORDER>")
    t[0] = t[1]

def p_ComplementoOrder(t):
    'COMPLEMENTOORDER  :   ASC  '
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTOORDER> ::= \"ASC\"")
    t[0] = 'A'

def p_ComplementoOD(t):
    'COMPLEMENTOORDER  :   DESC '
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTOORDER> ::= \"DESC\"")
    t[0] = 'D'

def p_ComplementoOANF(t):
    'COMPLEMENTOORDER  :   ASC NULLS FIRST  '
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTOORDER> ::= \"ASC\" \"NULLS\" \"FIRST\"")
    t[0] = 'ANF'

def p_ComplementoOANL(t):
    'COMPLEMENTOORDER  :   ASC NULLS LAST   '
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTOORDER> ::= \"ASC\" \"NULLS\" \"LAST\"")
    t[0] = 'ANL'

def p_ComplementoODNF(t):
    'COMPLEMENTOORDER  :   DESC NULLS FIRST '
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTOORDER> ::= \"DESC\" \"NULLS\" \"FIRST\"")
    t[0] = 'DNF'

def p_ComplementoODNL(t):
    'COMPLEMENTOORDER  :   DESC NULLS LAST  '
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTOORDER> ::= \"DESC\" \"NULLS\" \"LAST\"")
    t[0] = 'DNL'

def p_ComplementoEm(t):
    'COMPLEMENTOORDER  :   EMPTY    '
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTOORDER> ::= \"EPSILON\"")
    t[0] = None

def p_Having(t):
    'PHAVING  :   HAVING CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<PHAVING> ::= \"HAVING\" <CONDICION>")
    ret = Retorno(Having(t[2].getInstruccion()), NodoAST('HAVING'))
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_GroupBy(t):
    'PGROUPBY  :   GROUP BY LCOMPLEMENTOGROUP '
    global reporte_gramatical
    reporte_gramatical.append("<PGROUPBY> ::= \"GROUP\" \"BY\" <LCOMPLEMENTOGROUP>")
    ret = Retorno(GroupBy(t[3].getInstruccion()), NodoAST('GROUP BY'))
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_ComplementoGroupL(t):
    'LCOMPLEMENTOGROUP  :   LCOMPLEMENTOGROUP COMA COMPLEMENTOGROUP '
    global reporte_gramatical
    reporte_gramatical.append("<LCOMPLEMENTOGROUP> ::= <LCOMPLEMENTOGROUP> \",\" <COMPLEMENTOGROUP>")
    val = t[1].getInstruccion()
    val.append(t[3].getInstruccion())
    ret = Retorno(val, NodoAST('VALOR'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_ComplementoGroupLS(t):
    'LCOMPLEMENTOGROUP  :   COMPLEMENTOGROUP '
    global reporte_gramatical
    reporte_gramatical.append("<LCOMPLEMENTOGROUP> ::= <COMPLEMENTOGROUP>")
    val = [t[1].getInstruccion()]
    ret = Retorno(val, NodoAST('VALOR'))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret

def p_ComplementoGroupC(t):
    'COMPLEMENTOGROUP  :   CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<COMPLEMENTOGROUP> ::= <CONDICION>")
    t[0] = t[1]

def p_Valores(t):
    'VALORES  :   POR '
    global reporte_gramatical
    reporte_gramatical.append("<VALORES> ::= *")
    t[0] = t[1]

def p_ValoresLista(t):
    'VALORES  :   LISTAVALORES '
    global reporte_gramatical
    reporte_gramatical.append("<VALORES> ::= <LISTAVALORES>")
    t[0] = t[1]

def p_ListaValores(t):
    'LISTAVALORES  :   LISTAVALORES COMA VALOR '
    global reporte_gramatical
    reporte_gramatical.append("<LISTAVALORES> ::= <LISTAVALORES> \",\" <VALOR>")
    val = t[1].getInstruccion()
    val.append(t[3].getInstruccion())
    ret = Retorno(val, NodoAST('VALOR'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_ListaValoresS(t):
    'LISTAVALORES  :   VALOR '
    global reporte_gramatical
    reporte_gramatical.append("<LISTAVALORES> ::= <VALOR>")
    val = [t[1].getInstruccion()]
    ret = Retorno(val, NodoAST('VALOR'))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret


def p_ValorSub(t):
    'VALOR  :   PABRE SUBCONSULTA PCIERRA ALIAS'
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"(\" <SUBCONSULTA> \")\" <ALIAS>")
    ret = Retorno(Subconsulta(t[2].getInstruccion(), t[4].getInstruccion()), NodoAST("AS"))
    ret.getNodo().setHijo(t[2].getNodo())
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

def p_ValorCountAa(t):
    'VALOR  :   COUNT PABRE POR PCIERRA ALIAS'
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"COUNT\" \"(\" \"*\" \")\" <ALIAS>")
    ret = Retorno(FuncionAgregacion('COUNT', None, t[5].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('COUNT'))
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

def p_ValorCounta(t):
    'VALOR  :   COUNT PABRE ID PCIERRA ALIAS'
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"COUNT\" \"(\" \"ID\" \")\" <ALIAS>")
    val_id = Id(t[3], None)
    ret = Retorno(FuncionAgregacion('COUNT', val_id, t[5].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('COUNT'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

def p_ValorCountA(t):
    'VALOR  :   COUNT PABRE POR PCIERRA '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"COUNT\" \"(\" \"*\" \")\"")
    ret = Retorno(FuncionAgregacion('COUNT', None, t[1]), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('COUNT'))
    t[0] = ret

def p_ValorCount(t):
    'VALOR  :   COUNT PABRE ID PCIERRA '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"COUNT\" \"(\" \"ID\" \")\"")
    val_id = Id(t[3], None)
    ret = Retorno(FuncionAgregacion('COUNT', val_id, t[1]), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('COUNT'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret

def p_ValorCountAliasId(t):
    'VALOR  :   COUNT PABRE ID PUNTO ID PCIERRA ALIAS'
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"COUNT\" \"(\" \"ID\" \".\" \"ID\" \")\" <ALIAS>")
    val_id = Id(t[5], t[3])
    ret = Retorno(FuncionAgregacion('COUNT', val_id, t[7].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('COUNT'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[5]))
    ret.getNodo().setHijo(NodoAST(t[7].getNodo()))
    t[0] = ret

def p_ValorCountIdP(t):
    'VALOR  :   COUNT PABRE ID PUNTO ID PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"COUNT\" \"(\" \"ID\" \".\" \"ID\" \")\"")
    val_id = Id(t[3], None)
    ret = Retorno(FuncionAgregacion('COUNT', val_id, t[1]), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('COUNT'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[5]))
    t[0] = ret
   
def p_ValorCondicionAlias(t):
    'VALOR  :   CONDICION ALIAS '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= <CONDICION> <ALIAS>")
    ret = Retorno(Valores(t[1].getInstruccion(), t[2].getInstruccion()), NodoAST('AS'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_ValorCondicion(t):
    'VALOR  :   CONDICION'
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= <CONDICION>")
    ret = Retorno(Valores(t[1].getInstruccion(), None), t[1].getNodo())
    t[0] = ret

def p_ValorFTrigonometricas(t):
    'VALOR  :   FTRIGONOMETRICAS PABRE LNUM PCIERRA '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= <FTRIGONOMETRICAS> \"(\" <LNUM> \")\"")
    ret = Retorno(FuncionesTrigonometricas(t[1], t[3].getInstruccion(), t[1]), NodoAST('TRIGONOMETRICA'))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_ValorFTrigonometricasAlias(t):
    'VALOR  :   FTRIGONOMETRICAS PABRE LNUM PCIERRA ALIAS '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= <FTRIGONOMETRICAS> \"(\" <LNUM> \")\" <ALIAS>")
    ret = Retorno(FuncionesTrigonometricas(t[1], t[3].getInstruccion(), t[5].getInstruccion()), NodoAST('TRIGONOMETRICA'))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(t[3].getNodo())
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

def p_ValorGreatest(t):
    'VALOR  :   GREATEST PABRE LNUM PCIERRA '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"GREATEST\" \"(\" <LNUM> \")\"")
    ret = Retorno(FuncionGreatest(t[3].getInstruccion(), t[1]), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('GREATEST'))
    ret.getNodo().setHijo(t[3].getNodo())   
    t[0] = ret

def p_ValorLeast(t):
    'VALOR  :   LEAST PABRE LNUM PCIERRA '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"LEAST\" \"(\" <LNUM> \")\"")
    ret = Retorno(FuncionLeast(t[3].getInstruccion(), t[1]), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('LEAST'))
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_ValorGreatestAlias(t):
    'VALOR  :   GREATEST PABRE LNUM PCIERRA ALIAS'
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"GREATEST\" \"(\" <LNUM> \")\" <ALIAS>")
    ret = Retorno(FuncionGreatest(t[3].getInstruccion(), t[5].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('GREATEST'))
    ret.getNodo().setHijo(t[3].getNodo())
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

def p_ValorLeastAlias(t):
    'VALOR  :   LEAST PABRE LNUM PCIERRA ALIAS'
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"LEAST\" \"(\" <LNUM> \")\" <ALIAS>")
    ret = Retorno(FuncionLeast(t[3].getInstruccion(), t[5].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('LEAST'))
    ret.getNodo().setHijo(t[3].getNodo())
    ret.getNodo().setHijo(t[5].getNodo())
    t[0]= ret

def p_ValorRandomA(t):
    'VALOR  :   RANDOM PABRE PCIERRA ALIAS'
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"RANDOM\" \"(\" \")\" <ALIAS>")
    ret = Retorno(FuncionRandom(t[4].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('RANDOM'))
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

def p_ValorRandom(t):
    'VALOR  :   RANDOM PABRE PCIERRA '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"RANDOM\" \"(\" \")\"")
    ret = Retorno(FuncionRandom(t[1]), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('RANDOM'))
    t[0] = ret

def p_ValorPiAlias(t):
    'VALOR  :   PI PABRE PCIERRA   ALIAS '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"PI\" \"(\" \")\" <ALIAS>")
    ret = Retorno(FuncionPi(t[4].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('PI'))
    t[0] = ret
    
def p_ValorPi(t):
    'VALOR  :   PI PABRE PCIERRA '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"PI\" \"(\" \")\"")
    ret = Retorno(FuncionPi(t[1]), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('PI'))
    t[0] = ret

def p_ValorFuncionesDecodeA(t):
    'VALOR  :   DECODE PABRE CADENA COMA CADENA PCIERRA ALIAS   '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"DECODE\" \"(\" \"CADENA\" \",\" \"CADENA\" \")\" <ALIAS>")
    ret = Retorno(Decode(t[3], t[5], t[7].getInstruccion), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('DECODE'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[5]))
    ret.getNodo().setHijo(t[7].getNodo())
    t[0] = ret

def p_ValorFuncionesDecode(t):
    'VALOR  :   DECODE PABRE CADENA COMA CADENA PCIERRA   '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"DECODE\" \"(\" \"CADENA\" \",\" \"CADENA\" \")\"")
    ret = Retorno(Decode(t[3], t[5], t[1]), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('DECODE'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[5]))
    t[0] = ret

def p_ValorFuncionesEncodeA(t):
    'VALOR  :   ENCODE PABRE CADENA COMA CADENA PCIERRA ALIAS   '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"ENCODE\" \"(\" \"CADENA\" \",\" \"CADENA\" \")\" <ALIAS>")
    ret = Retorno(Encode(t[3], t[5], t[7].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('ENCODE'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[5]))
    ret.getNodo().setHijo(t[7].getNodo())
    t[0] = ret

def p_ValorFuncionesEncode(t):
    'VALOR  :   ENCODE PABRE CADENA COMA CADENA PCIERRA   '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"ENCODE\" \"(\" \"CADENA\" \",\" \"CADENA\" \")\"")
    ret = Retorno(Encode(t[3], t[5], t[1]), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('ENCODE'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[5]))
    t[0] = ret

def p_ValorFuncionesConvertDate(t):
    'VALOR  :   CONVERT PABRE CADENA AS DATE PCIERRA   '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"CONVERT\" \"(\" \"CADENA\" \"AS\" \"DATE\" \")\"")
    ret = Retorno(Convert(t[3], t[5], t[1]), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('CONVERT'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[5]))
    t[0] = ret

def p_ValorFuncionesConvertInt(t):
    'VALOR  :   CONVERT PABRE CADENA AS INTEGER PCIERRA   '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"CONVERT\" \"(\" \"CADENA\" \"AS\" \"INTEGER\" \")\"")
    ret = Retorno(Convert(t[3], t[5], t[1]), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('CONVERT'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[5]))
    t[0] = ret

def p_ValorFuncionesConvertDateA(t):
    'VALOR  :   CONVERT PABRE CADENA AS DATE PCIERRA ALIAS   '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"CONVERT\" \"(\" \"CADENA\" \"AS\" \"DATE\" \")\" <ALIAS>")
    ret = Retorno(Convert(t[3], t[5], t[7].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('CONVERT'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[5]))
    t[0] = ret

def p_ValorFuncionesConvertIntA(t):
    'VALOR  :   CONVERT PABRE CADENA AS INTEGER PCIERRA ALIAS   '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"CONVERT\" \"(\" \"CADENA\" \"AS\" \"INTEGER\" \")\" <ALIAS>")
    ret = Retorno(Convert(t[3], t[5], t[7].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('CONVERT'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[5]))
    ret.getNodo().setHijo(t[7].getNodo())
    t[0] = ret

def p_ValorFuncionesSha(t):
    'VALOR  :   SHA256 PABRE CADENA PCIERRA   '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"SHA256\" \"(\" \"CADENA\" \")\"")
    ret = Retorno(Sha256(t[3], None), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('SHA256'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret

def p_ValorFuncionesShaA(t):
    'VALOR  :   SHA256 PABRE CADENA PCIERRA ALIAS   '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"SHA256\" \"(\" \"CADENA\" \")\" <ALIAS>")
    ret = Retorno(Sha256(t[3], t[5].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('SHA256'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

def p_ValorOperadorMatAlias(t):
    'VALOR  :   NUM OPERADOR NUM ALIAS '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= <NUM> <OPERADOR> <NUM> <ALIAS>")
    val = OperacionBinariaS(t[1], t[3], t[2], t[4].getInstruccion())
    nodo = None
    if t[2] == OPERACION_STRING.BAND:
        nodo = NodoAST('&')
    elif t[2] == OPERACION_STRING.BOR:
        nodo = NodoAST('\\|')
    elif t[2] == OPERACION_STRING.BXOR:
        nodo = NodoAST('#')
    elif t[2] == OPERACION_STRING.DESPLAZAI:
        nodo = NodoAST('\\<\\<')
    elif t[2] == OPERACION_STRING.DESPLAZAD:
        nodo = NodoAST('\\>\\>')
    ret = Retorno(val, nodo)
    ret.getNodo().setHijo(NodoAST(str(t[1].valor)))
    ret.getNodo().setHijo(NodoAST(str(t[3].valor)))
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

def p_ValorOperadorMat(t):
    'VALOR  :   NUM OPERADOR NUM '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= <NUM> <OPERADOR> <NUM>")
    val = OperacionBinariaS(t[1], t[3], t[2], None)
    nodo = None
    if t[2] == OPERACION_STRING.BAND:
        nodo = NodoAST('&')
    elif t[2] == OPERACION_STRING.BOR:
        nodo = NodoAST('\\|')
    elif t[2] == OPERACION_STRING.BOR:
        nodo = NodoAST('#')
    elif t[2] == OPERACION_STRING.DESPLAZAI:
        nodo = NodoAST('\\<\\<')
    elif t[2] == OPERACION_STRING.DESPLAZAD:
        nodo = NodoAST('\\>\\>')
    ret = Retorno(val, nodo)
    ret.getNodo().setHijo(NodoAST(str(t[1].valor)))
    ret.getNodo().setHijo(NodoAST(str(t[3].valor)))
    t[0] = ret

def p_ValorOperadorNotA(t):
    'VALOR  :   BNot NUM ALIAS '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"" + str(t[1]) + "\" <NUM> <ALIAS>")
    ret = Retorno(OperacionUnariaS(t[2], OPERACION_STRING.BNOT, t[3].getInstruccion()), NodoAST('~'))
    ret.getNodo().setHijo(NodoAST(str(t[2].valor)))
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_ValorOperadorNot(t):
    'VALOR  :   BNot NUM '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"" + str(t[1]) + "\" <NUM>")
    ret = Retorno(OperacionUnariaS(t[2], OPERACION_STRING.BNOT, None), NodoAST('~'))
    ret.getNodo().setHijo(NodoAST(str(t[2].valor)))
    t[0] = ret

def p_ValorRaizCuadradaA(t):
    'VALOR  :   raizCuadrada NUM ALIAS '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"" + str(t[1]) + "\" <NUM> <ALIAS>")
    ret = Retorno(OperacionUnariaS(t[2], OPERACION_STRING.RAIZCUADRADA, t[3].getInstruccion()), NodoAST('\\|/'))
    ret.getNodo().setHijo(NodoAST(str(t[2].valor)))
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_ValorRaizCuadrada(t):
    'VALOR  :   raizCuadrada NUM '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"" + str(t[1]) + "\" <NUM>")
    ret = Retorno(OperacionUnariaS(t[2], OPERACION_STRING.RAIZCUADRADA, None), NodoAST('\\|/'))
    ret.getNodo().setHijo(NodoAST(str(t[2].valor)))
    t[0] = ret

def p_ValorRaizCubicaA(t):
    'VALOR  :   raizCubica NUM ALIAS '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"" + str(t[1]) + "\" <NUM> <ALIAS>")
    ret = Retorno(OperacionUnariaS(t[2], OPERACION_STRING.RAIZCUBICA, t[3].getInstruccion()), NodoAST('\\|\\|/'))
    ret.getNodo().setHijo(NodoAST(str(t[2].valor)))
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_ValorRaizCubica(t):
    'VALOR  :   raizCubica NUM '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"" + str(t[1]) + "\" <NUM>")
    ret = Retorno(OperacionUnariaS(t[2], OPERACION_STRING.RAIZCUBICA, None), NodoAST('\\|\\|/'))
    ret.getNodo().setHijo(NodoAST(str(t[2].valor)))
    t[0] = ret

def p_ValorFuncionesGetByte(t):
    'VALOR  :   GETBYTE PABRE CADENA COMA NUMERO PCIERRA '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"GET_BYTE\" \"(\" \"CADENA\" \",\" \"NUMERO\" \")\"")
    ret = Retorno(GetByte(t[3], t[5], None), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('GET_BYTE'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[5]))
    t[0] = ret

def p_ValorFuncionesGetByteA(t):
    'VALOR  :   GETBYTE PABRE CADENA COMA NUMERO PCIERRA ALIAS '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"GET_BYTE\" \"(\" \"CADENA\" \",\" \"NUMERO\" \")\" <ALIAS>")
    ret = Retorno(GetByte(t[3], t[5], t[7].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('GET_BYTE'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[5]))
    ret.getNodo().setHijo(t[7].getNodo())
    t[0] = ret

def p_ValorFuncionesSetByte(t):
    'VALOR  :   SETBYTE PABRE CADENA COMA NUMERO COMA NUMERO PCIERRA '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"SET_BYTE\" \"(\" \"CADENA\" \",\" \"NUMERO\" \",\" \"NUMERO\" \")\"")
    ret = Retorno(SetByte(t[3], t[5], t[7], None), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('SET_BYTE'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[5]))
    ret.getNodo().setHijo(NodoAST(t[7]))
    t[0] = ret

def p_ValorFuncionesSetByteA(t):
    'VALOR  :   SETBYTE PABRE CADENA COMA NUMERO COMA NUMERO PCIERRA ALIAS '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"SET_BYTE\" \"(\" \"CADENA\" \",\" \"NUMERO\" \",\" \"NUMERO\" \")\" <ALIAS>")
    ret = Retorno(SetByte(t[3], t[5], t[7], t[9].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('SET_BYTE'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[5]))
    ret.getNodo().setHijo(NodoAST(t[7]))
    ret.getNodo().setHijo(t[9].getNodo())
    t[0] = ret

def p_ValorCase(t):
    'VALOR  :   CASE LWHEN END '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"CASE\" <LWHEN> \"END\"")
    ret = Retorno(InstruccionCase(t[2].getInstruccion(), None), NodoAST('CASE'))
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_ValorCaseAlias(t):
    'VALOR  :   CASE LWHEN END ALIAS'
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= \"CASE\" <LWHEN> \"END\" <ALIAS>")
    ret = Retorno(InstruccionCase(t[2].getInstruccion(), t[4].getInstruccion()), NodoAST('CASE'))
    ret.getNodo().setHijo(t[2].getNodo())
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

def p_ValorFunAlias(t):
    'VALOR  :   ID_VALOR PABRE LCONDICION_FUNCION PCIERRA ALIAS   '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= <ID_VALOR> \"(\" <LCONDICION_FUNCION> \")\" <ALIAS>")
    ret = Retorno(FuncionesMatematicas(t[1], t[3].getInstruccion(), t[5].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(t[3].getNodo())
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

def p_ValorFun(t):
    'VALOR  :   ID_VALOR PABRE LCONDICION_FUNCION PCIERRA   '
    global reporte_gramatical
    reporte_gramatical.append("<VALOR> ::= <ID_VALOR> \"(\" <LCONDICION_FUNCION> \")\"")
    ret = Retorno(FuncionesMatematicas(t[1], t[3].getInstruccion(), t[1]), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_LWHEN(t):
    'LWHEN  :   LWHEN PWHEN '
    global reporte_gramatical
    reporte_gramatical.append("<LWHEN> ::= <LWHEN> <PWHEN>")
    val = t[1].getInstruccion()
    val.append(t[2].getInstruccion())
    ret = Retorno(val, NodoAST('WHEN'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_WHENWHEN(t):
    'LWHEN  :   PWHEN'
    global reporte_gramatical
    reporte_gramatical.append("<LWHEN> ::= <PWHEN>")
    val = [t[1].getInstruccion()]
    ret = Retorno(val, NodoAST('WHEN'))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret

def p_LWHENSimple(t):
    'PWHEN  :   WHEN CONDICION THEN CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<PWHEN> ::= \"WHEN\" <CONDICION> \"THEN\" <CONDICION>")
    val = InstruccionWhen(t[2].getInstruccion(), t[4].getInstruccion())
    auxval = [val]
    ret = Retorno(auxval, NodoAST('VALOR'))
    ret.getNodo().setHijo(t[2].getNodo())
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

def p_LWHENElse(t):
    'PWHEN  :   ELSE CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<PWHEN> ::= \"ELSE\" <CONDICION>")
    val = InstruccionElse(t[2].getInstruccion())
    auxval = [val]
    ret = Retorno(auxval, NodoAST('ELSE'))
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_IdFuncionDegrees(t):
    'ID_VALOR  :   DEGREES  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_VALOR> ::= \"DEGREES\"")
    t[0] = 'DEGREES'

def p_IdFuncionDiv(t):
    'ID_VALOR  :   DIV  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_VALOR> ::= \"DIV\"")
    t[0] = 'DIV'

def p_IdFuncionExp(t):
    'ID_VALOR  :   FEXP  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_VALOR> ::= \"EXP\"")
    t[0] = 'EXP'

def p_IdFuncionFactorial(t):
    'ID_VALOR  :   FACTORIAL  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_VALOR> ::= \"FACTORIAL\"")
    t[0] = 'FACTORIAL'

def p_IdFuncionFloor(t):
    'ID_VALOR  :   FLOOR  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_VALOR> ::= \"FLOOR\"")
    t[0] = 'FLOOR'

def p_IdFuncionGcd(t):
    'ID_VALOR  :   GCD  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_VALOR> ::= \"GCD\"")
    t[0] = 'GCD'

def p_IdFuncionLn(t):
    'ID_VALOR  :   LN  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_VALOR> ::= \"LN\"")
    t[0] = 'LN'

def p_IdFuncionLog(t):
    'ID_VALOR  :   LOG  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_VALOR> ::= \"LOG\"")
    t[0] = 'LOG'

def p_IdFuncionMod(t):
    'ID_VALOR  :   MOD  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_VALOR> ::= \"MOD\"")
    t[0] = 'MOD'

def p_IdFuncionPower(t):
    'ID_VALOR  :   POWER  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_VALOR> ::= \"POWER\"")
    t[0] = 'POWER'

def p_IdFuncionRadians(t):
    'ID_VALOR  :   RADIANS  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_VALOR> ::= \"RADIANS\"")
    t[0] = 'RADIANS'

def p_IdFuncionRound(t):
    'ID_VALOR  :   ROUND  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_VALOR> ::= \"ROUND\"")
    t[0] = 'ROUND'

def p_IdFuncionSign(t):
    'ID_VALOR  :   SIGN  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_VALOR> ::= \"SIGN\"")
    t[0] = 'SIGN'

def p_IdFuncionSqrt(t):
    'ID_VALOR  :   SQRT  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_VALOR> ::= \"SQRT\"")
    t[0] = 'SQRT'

def p_IdFuncionWidth_bucket(t):
    'ID_VALOR  :   WIDTH_BUCKET  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_VALOR> ::= \"WIDTH_BUCKET\"")
    t[0] = 'WIDTH_BUCKET'

def p_IdFuncionTrunc(t):
    'ID_VALOR  :   TRUNC  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_VALOR> ::= \"TRUNC\"")
    t[0] = 'TRUNC'

def p_OPERADORAnd(t):
    'OPERADOR  :   BAnd '
    global reporte_gramatical
    reporte_gramatical.append("<OPERADOR> ::= \"" + str(t[1]) + "\"")
    t[0] = OPERACION_STRING.BAND

def p_OPERADOROr(t):
    'OPERADOR  :   BOr '
    global reporte_gramatical
    reporte_gramatical.append("<OPERADOR> ::= \"" + str(t[1]) + "\"")
    t[0] = OPERACION_STRING.BOR

def p_OPERADORXor(t):
    'OPERADOR  :   BXor '
    global reporte_gramatical
    reporte_gramatical.append("<OPERADOR> ::= \"" + str(t[1]) + "\"")
    t[0] = OPERACION_STRING.BXOR

def p_OPERADORDIz(t):
    'OPERADOR  :   DesplazaI '
    global reporte_gramatical
    reporte_gramatical.append("<OPERADOR> ::= \"" + str(t[1]) + "\"")
    t[0] = OPERACION_STRING.DESPLAZAI

def p_OPERADORDDe(t):
    'OPERADOR  :   DesplazaD '
    global reporte_gramatical
    reporte_gramatical.append("<OPERADOR> ::= \"" + str(t[1]) + "\"")
    t[0] = OPERACION_STRING.DESPLAZAD

def p_LNumNumLNum(t):
    'LNUM  : LNUM COMA NUM'
    global reporte_gramatical
    reporte_gramatical.append("<LNUM> ::= <LNUM> \",\" <NUM>")
    val = t[1].getInstruccion()
    val.append(t[3])
    ret = Retorno(val, NodoAST('VALOR'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(NodoAST(str(t[3].valor)))
    t[0] = ret

def p_LNumNum(t):
    'LNUM   : NUM'
    global reporte_gramatical
    reporte_gramatical.append("<LNUM> ::= <NUM>")
    val = [t[1]]
    ret = Retorno(val, NodoAST('VALOR'))
    ret.getNodo().setHijo(NodoAST(str(t[1].valor)))
    t[0] = ret

def p_NumNumero(t):  
    'NUM    : NUMERO '
    global reporte_gramatical
    reporte_gramatical.append("<NUM> ::= \"NUMERO\"")
    t[0] = Numero(t[1])

def p_NumDecimal(t):
    'NUM  :   DECIMALN '
    global reporte_gramatical
    reporte_gramatical.append("<NUM> ::= \"DECIMALN\"")
    t[0] = Decimal(t[1])

def p_NumCadena(t):
    'NUM  :   CADENA '
    global reporte_gramatical
    reporte_gramatical.append("<NUM> ::= \"CADENA\"")
    t[0] = Cadena(t[1])

def p_FTrigonometricasAcos(t):
    'FTRIGONOMETRICAS  :   ACOS '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"ACOS\"")
    t[0] = 'ACOS'

def p_FTrigonometricasAcosd(t):
    'FTRIGONOMETRICAS  :   ACOSD '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"ACOSD\"")
    t[0] = 'ACOSD'

def p_FTrigonometricasAsin(t):
    'FTRIGONOMETRICAS  :   ASIN '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"ASIN\"")
    t[0] = 'ASIN'

def p_FTrigonometricasAsind(t):
    'FTRIGONOMETRICAS  :   ASIND '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"ASIND\"")
    t[0] = 'ASIND'

def p_FTrigonometricasAtan(t):
    'FTRIGONOMETRICAS  :   ATAN '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"ATAN\"")
    t[0] = 'ATAN'

def p_FTrigonometricasAtand(t):
    'FTRIGONOMETRICAS  :   ATAND '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"ATAND\"")
    t[0] = 'ATAND'

def p_FTrigonometricasAtan2(t):
    'FTRIGONOMETRICAS  :   ATAN2 '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"ATAN2\"")
    t[0] = 'ATAN2'

def p_FTrigonometricasAtan2d(t):
    'FTRIGONOMETRICAS  :   ATAN2D '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"ATAN2D\"")
    t[0] = 'ATAN2D'

def p_FTrigonometricasCos(t):
    'FTRIGONOMETRICAS  :   COS '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"COS\"")
    t[0] = 'COS'

def p_FTrigonometricasCosd(t):
    'FTRIGONOMETRICAS  :   COSD '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"COSD\"")
    t[0] = 'COSD'

def p_FTrigonometricasCot(t):
    'FTRIGONOMETRICAS  :   COT '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"COT\"")
    t[0] = 'COT'

def p_FTrigonometricasCotd(t):
    'FTRIGONOMETRICAS  :   COTD '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"COTD\"")
    t[0] = 'COTD'

def p_FTrigonometricasSin(t):
    'FTRIGONOMETRICAS  :   SIN '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"SIN\"")
    t[0] = 'SIN'

def p_FTrigonometricasSind(t):
    'FTRIGONOMETRICAS  :   SIND '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"SIND\"")
    t[0] = 'SIND'

def p_FTrigonometricasTan(t):
    'FTRIGONOMETRICAS  :   TAN '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"TAN\"")
    t[0] = 'TAN'

def p_FTrigonometricasTand(t):
    'FTRIGONOMETRICAS  :   TAND '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"TAND\"")
    t[0] = 'TAND'

def p_FTrigonometricasSinh(t):
    'FTRIGONOMETRICAS  :   SINH '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"SINH\"")
    t[0] = 'SINH'

def p_FTrigonometricasCosh(t):
    'FTRIGONOMETRICAS  :   COSH '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"COSH\"")
    t[0] = 'COSH'

def p_FTrigonometricasTanh(t):
    'FTRIGONOMETRICAS  :   TANH '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"TANH\"")
    t[0] = 'TANH'

def p_FTrigonometricasAsinh(t):
    'FTRIGONOMETRICAS  :   ASINH '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"ASINH\"")
    t[0] = 'ASINH'

def p_FTrigonometricasAcosh(t):
    'FTRIGONOMETRICAS  :   ACOSH '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"ACOSH\"")
    t[0] = 'ACOSH'

def p_FTrigonometricasAtanh(t):
    'FTRIGONOMETRICAS  :   ATANH '
    global reporte_gramatical
    reporte_gramatical.append("<FTRIGONOMETRICAS> ::= \"ATANH\"")
    t[0] = 'ATANH'

def p_funcionAvg(t):
    'FUNCION    :   AVG'
    global reporte_gramatical
    reporte_gramatical.append("<FUNCION> ::= \"AVG\"")
    t[0] = 'AVG'

def p_funcionSum(t):
    'FUNCION    :   SUM'
    global reporte_gramatical
    reporte_gramatical.append("<FUNCION> ::= \"SUM\"")
    t[0] = 'SUM'

def p_funcionMin(t):
    'FUNCION    :   MIN'
    global reporte_gramatical
    reporte_gramatical.append("<FUNCION> ::= \"MIN\"")
    t[0] = "MIN"

def p_funcionMax(t):
    'FUNCION    :   MAX'
    global reporte_gramatical
    reporte_gramatical.append("<FUNCION> ::= \"MAX\"")

def p_Alias(t):
    'ALIAS  :   AS ID '
    global reporte_gramatical
    reporte_gramatical.append("<ALIAS> ::= \"AS\" \"ID\"")
    val_id = Id(t[2], None)
    ret = Retorno(val_id, NodoAST('Alias'))
    ret.getNodo().setHijo(NodoAST(t[2]))
    t[0] = ret

def p_AliasS(t):
    'ALIAS  :   ID '
    global reporte_gramatical
    reporte_gramatical.append("<ALIAS> ::= \"ID\"")
    val_id = Id(t[1], None)
    ret = Retorno(val_id, NodoAST('Alias'))
    ret.getNodo().setHijo(NodoAST(t[1]))
    t[0] = ret

def p_AliasC(t):
    'ALIAS  :   AS IDALIAS'
    global reporte_gramatical
    reporte_gramatical.append("<ALIAS> ::= \"AS\" \"IDALIAS\"")
    val_id = Id(t[2], None)
    ret = Retorno(val_id, NodoAST('Alias'))
    ret.getNodo().setHijo(NodoAST(t[2]))
    t[0] = ret

def p_AliasCS(t):
    'ALIAS  :   IDALIAS'
    global reporte_gramatical
    reporte_gramatical.append("<ALIAS> ::= \"IDALIAS\"")
    val_id = Id(t[1], None)
    ret = Retorno(val_id, NodoAST('Alias'))
    ret.getNodo().setHijo(NodoAST(t[1]))
    t[0] = ret

def p_PFROM(t):
    'PFROM  :   FROM LVALORESFROM '
    global reporte_gramatical
    reporte_gramatical.append("<PFROM> ::= \"FROM\" <LVALORESFROM>")
    ret = Retorno(t[2].getInstruccion(), NodoAST('FROM'))
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_LValoresFrom(t):
    'LVALORESFROM   :   LVALORESFROM  COMA VALORFROM '
    global reporte_gramatical
    reporte_gramatical.append("<LVALORESFROM> ::= <LVALORESFROM> \",\" <VALORFROM>")
    val = t[1].getInstruccion()
    val.append(t[3].getInstruccion())
    ret = Retorno(val, NodoAST('Valor'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_LValoresFrom1(t):
    'LVALORESFROM   :   VALORFROM '
    global reporte_gramatical
    reporte_gramatical.append("<LVALORESFROM> ::= <VALORFROM>")
    val = [t[1].getInstruccion()]
    ret = Retorno(val, NodoAST('Valor'))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret

def p_ValoresFromIdAlias(t):
    'VALORFROM  :   ID ALIAS '
    global reporte_gramatical
    reporte_gramatical.append("<VALORFROM> ::= \"ID\" <ALIAS>")
    val_id = Id(t[1], t[2].getInstruccion())
    ret = Retorno(val_id, NodoAST(t[1]))
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_ValoresFromId(t):
    'VALORFROM  :   ID '
    global reporte_gramatical
    reporte_gramatical.append("<VALORFROM> ::= \"ID\"")
    val_id = Id(t[1], None)
    ret = Retorno(val_id, NodoAST(t[1]))
    t[0] = ret

def p_ValoresFromSub(t):
    'VALORFROM  :   PABRE SUBCONSULTA PCIERRA ALIAS    '
    global reporte_gramatical
    reporte_gramatical.append("<VALORFROM> ::= \"(\" <SUBCONSULTA> \")\" <ALIAS>")
    ret = Retorno(Subconsulta(t[2].getInstruccion(), t[4].getInstruccion()), NodoAST('AS'))
    ret.getNodo().setHijo(t[2].getNodo())
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

def p_SubconsultaFrom(t):
    'SUBCONSULTA    :   SELECT VALORES PFROM LCOMPLEMENTOS '
    global reporte_gramatical
    reporte_gramatical.append("<SUBCONSULTA> ::= \"SELECT\" <VALORES> <PFROM> <LCOMPLEMENTOS>")
    if isinstance(t[2], str):
        ret = Retorno(Select3(t[2], t[3].getInstruccion(), None, t[4].getInstruccion(), False), NodoAST("SELECT"))
        ret.getNodo().setHijo(NodoAST(t[2]))
        ret.getNodo().setHijo(t[3].getNodo())
        ret.getNodo().setHijo(t[4].getNodo())
        t[0] = ret
    else:
        ret = Retorno(Select3(t[2].getInstruccion(), t[3].getInstruccion(), None, t[4].getInstruccion(), False), NodoAST("SELECT"))
        ret.getNodo().setHijo(t[2].getNodo())
        ret.getNodo().setHijo(t[3].getNodo())
        ret.getNodo().setHijo(t[4].getNodo())
        t[0] = ret


def p_SubconsultaFromW(t):
    'SUBCONSULTA    :   SELECT VALORES PFROM PWHERE LCOMPLEMENTOS '
    global reporte_gramatical
    reporte_gramatical.append("<SUBCONSULTA> ::= \"SELECT\" <VALORES> <PFROM> <PWHERE> <LCOMPLEMENTOS>")
    if isinstance(t[2], str):
        ret = Retorno(Select3(t[2], t[3].getInstruccion(), t[4].getInstruccion(), t[5].getInstruccion(), False), NodoAST("SELECT"))
        ret.getNodo().setHijo(NodoAST(t[2]))
        ret.getNodo().setHijo(t[3].getNodo())
        ret.getNodo().setHijo(t[4].getNodo())
        ret.getNodo().setHijo(t[5].getNodo())
        t[0] = ret
    else:
        ret = Retorno(Select3(t[2].getInstruccion(), t[3].getInstruccion(), t[4].getInstruccion(), t[5].getInstruccion(), False), NodoAST("SELECT"))
        ret.getNodo().setHijo(t[2].getNodo())
        ret.getNodo().setHijo(t[3].getNodo())
        ret.getNodo().setHijo(t[4].getNodo())
        ret.getNodo().setHijo(t[5].getNodo())
        t[0] = ret

def p_SubconsultaFrom1(t):
    'SUBCONSULTA    :   SELECT VALORES PFROM'
    global reporte_gramatical
    reporte_gramatical.append("<SUBCONSULTA> ::= \"SELECT\" <VALORES> <PFROM>")
    if isinstance(t[2], str):
        ret = Retorno(Select3(t[2], t[3].getInstruccion(), None, None, False), NodoAST("SELECT"))
        ret.getNodo().setHijo(NodoAST(t[2]))
        ret.getNodo().setHijo(t[3].getNodo())
        t[0] = ret
    else:
        ret = Retorno(Select3(t[2].getInstruccion(), t[3].getInstruccion(), None, None, False), NodoAST("SELECT"))
        ret.getNodo().setHijo(t[2].getNodo())
        ret.getNodo().setHijo(t[3].getNodo())
        t[0] = ret

def p_SubconsultaFromW1(t):
    'SUBCONSULTA    :   SELECT VALORES PFROM PWHERE'
    global reporte_gramatical
    reporte_gramatical.append("<SUBCONSULTA> ::= \"SELECT\" <VALORES> <PFROM> <PWHERE>")
    if isinstance(t[2], str):
        ret = Retorno(Select3(t[2], t[3].getInstruccion(), t[4].getInstruccion(), None, False), NodoAST("SELECT"))
        ret.getNodo().setHijo(NodoAST(t[2]))
        ret.getNodo().setHijo(t[3].getNodo())
        ret.getNodo().setHijo(t[4].getNodo())
        t[0] = ret
    else:
        ret = Retorno(Select3(t[2].getInstruccion(), t[3].getInstruccion(), t[4].getInstruccion(), None, False), NodoAST("SELECT"))
        ret.getNodo().setHijo(t[2].getNodo())
        ret.getNodo().setHijo(t[3].getNodo())
        ret.getNodo().setHijo(t[4].getNodo())
        t[0] = ret


def p_Where(t):
    'PWHERE  :   WHERE CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<PWHERE> ::= \"WHERE\" <CONDICION>")
    ret = Retorno(t[2].getInstruccion(), NodoAST('WHERE'))
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_CondicionIgual(t):
    'CONDICION  :   CONDICION IGUAL CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"=\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACION_LOGICA.IGUAL),NodoAST("="))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionDif(t):
    'CONDICION  :   CONDICION DIF CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"<>\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACION_LOGICA.DIF),NodoAST("\\<\\>"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionDif1(t):
    'CONDICION  :   CONDICION DIF1 CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"!=\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACION_LOGICA.DIF),NodoAST("!="))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionMenor(t):
    'CONDICION  :   CONDICION MENOR CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"<\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACION_LOGICA.MENOR),NodoAST("\\<"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionMenorI(t):
    'CONDICION  :   CONDICION MENORIGUAL CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"<=\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACION_LOGICA.MENORIGUAL),NodoAST("\\<="))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionMayor(t):
    'CONDICION  :   CONDICION MAYOR CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \">\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACION_LOGICA.MAYOR),NodoAST("\\>"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionMayorI(t):
    'CONDICION  :   CONDICION MAYORIGUAL CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \">=\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACION_LOGICA.MAYORIGUAL),NodoAST("\\>="))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionAnd(t):
    'CONDICION  :   CONDICION AND CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"AND\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACION_LOGICA.AND),NodoAST("AND"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionOr(t):
    'CONDICION  :   CONDICION OR CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"OR\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACION_LOGICA.OR),NodoAST("OR"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionNot(t):
    'CONDICION  :   NOT CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"NOT\" <CONDICION>")
    ret = Retorno(ExpresionUnaria(t[2].getInstruccion(), OPERACION_LOGICA.NOT), NodoAST("NOT"))
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_CondicionParentesis(t):
    'CONDICION  :   PABRE CONDICION PCIERRA '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"(\" <CONDICION> \")\"")
    t[0] = t[2]

def p_CondicionMas(t):
    'CONDICION  :   CONDICION MAS CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"+\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACIONES.MAS),NodoAST("+"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionMenos(t):
    'CONDICION  :   CONDICION MENOS CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"-\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACIONES.MENOS),NodoAST("-"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionPor(t):
    'CONDICION  :   CONDICION POR CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"*\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACIONES.POR),NodoAST("*"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionDiv(t):
    'CONDICION  :   CONDICION DIVIDIDO CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"/\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACIONES.DIVIDIDO),NodoAST("/"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionMod(t):
    'CONDICION  :   CONDICION MODULO CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"%\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACIONES.MODULO),NodoAST("%"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionExp(t):
    'CONDICION  :   CONDICION EXP CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"^\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACIONES.EXP),NodoAST("^"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionIs(t):
    'CONDICION  :   CONDICION IS CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"IS\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACIONES.IS),NodoAST("IS"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionIsN(t):
    'CONDICION  :   CONDICION IS NULL CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"IS\" \"NULL\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACIONES.ISNULL),NodoAST("IS NULL"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionNotN(t):
    'CONDICION  :   CONDICION NOT NULL CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"NOT\" \"NULL\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(),t[3].getInstruccion(),OPERACIONES.NOTNULL),NodoAST("NOT NULL"))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionM(t):
    'CONDICION  :   MENOS CONDICION %prec UMENOS'
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"-\" <CONDICION>")
    ret = Retorno(ExpresionUnaria(t[2].getInstruccion(), OPERACIONES.MENOS), NodoAST('-'))
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_CondicionP(t):
    'CONDICION  :   MAS CONDICION %prec UMAS'
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"+\" <CONDICION>")
    ret = Retorno(ExpresionUnaria(t[2].getInstruccion(), OPERACIONES.MAS), NodoAST('+'))
    ret.getNodo().setHijo(t[2].getNodo())
    t[0] = ret

def p_CondicionExtract(t):
    'CONDICION  :   EXTRACT PABRE DATETIME FROM PTIMESTAMP PCIERRA '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"EXTRACT\" \"(\" <DATETIME> \"FROM\" <PTIMESTAMP> \")\"")
    ret = Retorno(Extract(t[5].getInstruccion(), t[3]), NodoAST('EXTRACT'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

def p_CondicionFuncionWhere(t):
    'CONDICION  :   FUNCIONES_WHERE '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <FUNCIONES_WHERE>")
    t[0] = t[1]

def p_CondicionNum(t):
    'CONDICION  :   NUMERO '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"NUMERO\"")
    ret = Retorno(Numero(t[1]),NodoAST(str(t[1])))
    t[0] = ret 

def p_CondicionDec(t):
    'CONDICION  :   DECIMALN'
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"DECIMALN\"")
    ret = Retorno(Decimal(t[1]),NodoAST(str(t[1])))
    t[0] = ret

def p_CondicionCad(t):
    'CONDICION  :   CADENA '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"CADENA\"")
    ret = Retorno(Cadena(t[1]),NodoAST(t[1]))
    t[0] = ret 

def p_CondicionTrue(t):
    'CONDICION  :   TRUE '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"TRUE\"")
    ret = Retorno(Booleano(t[1]),NodoAST(t[1]))
    t[0] = ret

def p_CondicionFalse(t):
    'CONDICION  :   FALSE '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"FALSE\"")
    ret = Retorno(Booleano(t[1]),NodoAST(t[1]))
    t[0] = ret

def p_CondicionId(t):
    'CONDICION  :   ID '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"ID\"")
    ret = Retorno(Id(t[1],None),NodoAST(t[1]))
    t[0] = ret

def p_CondicionIdP(t):
    'CONDICION  :   ID PUNTO ID '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"ID\" \".\" \"ID\"")
    val = Id(t[3], t[1])
    ret = Retorno(val, NodoAST('.'))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret

def p_CondicionIdPor(t):
    'CONDICION  :   ID PUNTO POR '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"ID\" \".\" \"*\"")
    val = Id('*', t[1])
    ret = Retorno(val, NodoAST('.'))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret

def p_CondicionFuncionSistema(t):
    'CONDICION  :   FUNCIONES_SISTEMA '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <FUNCIONES_SISTEMA>")
    t[0] = t[1]

def p_CondicionDatePart(t):
    'CONDICION  :   DATE_PART PABRE CADENA COMA INTERVAL CADENA PCIERRA '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"DATE_PART\" \"(\" \"CADENA\" \",\" \"INTERVAL\" \"CADENA\" \")\"")
    ret = Retorno(DatePart(t[3], t[6]), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('DATE_PART'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[6]))
    t[0] = ret

def p_CondicionCurrentDate(t):
    'CONDICION  :   CURRENT_DATE '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"CURRENT_DATE\"")
    ret = Retorno(CurrentDate(), NodoAST('CURRENT_DATE'))
    t[0] = ret

def p_CondicionCurrentTime(t):
    'CONDICION  :   CURRENT_TIME '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"CURRENT_TIME\"")
    ret = Retorno(CurrentTime(), NodoAST('CURRENT_TIME'))
    t[0] = ret

def p_CondicionTimeStamp(t):
    'CONDICION  :   TIMESTAMP CADENA '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"TIMESTAMP\" \"CADENA\"")
    ret = Retorno(Timestamp(t[2]), NodoAST('TIMESTAMP'))
    ret.getNodo().setHijo(NodoAST(t[2]))
    t[0] = ret

def p_CondicionBetween(t):
    'CONDICION  :   CONDICION BETWEEN CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"BETWEEN\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(), t[3].getInstruccion(), OPERACION_LOGICA.BETWEEN), NodoAST('BETWEEN'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_CondicionNotBetween(t):
    'CONDICION  :   CONDICION NOT BETWEEN CONDICION %prec NOTB'
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"NOT\" \"BETWEEN\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(), t[4].getInstruccion(), OPERACION_LOGICA.NOTBETWEEN), NodoAST('NOT BETWEEN'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

def p_CondicionBetweenSimetric(t):
    'CONDICION  :   CONDICION BETWEEN SIMMETRIC CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"BETWEEN\" \"SIMMETRIC\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(), t[4].getInstruccion(), OPERACION_LOGICA.BETWEENSIMMETRIC), NodoAST('BETWEEN SIMMETRIC'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

def p_CondicionBetweenNotSimetric(t):
    'CONDICION  :   CONDICION NOT BETWEEN SIMMETRIC CONDICION  %prec NOTB'
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"NOT\" \"BETWEEN\" \"SIMMETRIC\" <CONDICION>")
    ret = Retono(ExpresionBinaria(t[1].getInstruccion(), t[5].getInstruccion(), OPERACION_LOGICA.NOTBETWEENSIMMETRIC), NodoAST('NOT BETWEEN SIMMETRIC'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

def p_CondicionIsDistinct(t):
    'CONDICION  :   CONDICION IS DISTINCT FROM CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"IS\" \"DISTINCT\" \"FROM\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(), t[5].getInstruccion(), OPERACION_LOGICA.ISDISTINCT), NodoAST('IS DISTINCT'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

def p_CondicionIsNotDistinct(t):
    'CONDICION  :   CONDICION IS NOT DISTINCT FROM CONDICION '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <CONDICION> \"IS\" \"NOT\" \"DISTINCT\" \"FROM\" <CONDICION>")
    ret = Retorno(ExpresionBinaria(t[1].getInstruccion(), t[6].getInstruccion(), OPERACION_LOGICA.ISNOTDISTINCT), NodoAST('IS NOT DISTINCT'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[6].getNodo())
    t[0] = ret

def p_CondicionNull(t):
    'CONDICION  :   NULL '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"NULL\"")
    ret = Retorno(Null(), NodoAST('NULL'))
    t[0] = ret

def p_CondicionUnknown(t):
    'CONDICION  :   UNKNOWN '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"UNKNOWN\"")
    ret = Retorno(Unknow(), NodoAST('UNKNOW'))
    t[0] = ret

def p_CondicionSubConsulta(t):
    'CONDICION  :   PABRE SUBCONSULTA PCIERRA '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"(\" <SUBCONSULTA> \")\"")
    t[0] = t[2]

def p_CondicionFunciones(t):
    'CONDICION  :   FUNCION PABRE ID PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <FUNCION> \"(\" \"ID\" \")\"")
    val_id = Id(t[3], None)
    ret = Retorno(FuncionAgregacion(t[1], val_id, None), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret

def p_CondicionFunciones1(t):
    'CONDICION  :   FUNCION PABRE ID PUNTO ID PCIERRA'
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= <FUNCION> \"(\" \"ID\" \".\" \"ID\" \")\"")
    val_id = Id(t[5], t[3])
    ret = Retorno(FuncionAgregacion(t[1], val_id, None), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret

def p_CondicionNow(t):
    'CONDICION  :   NOW PABRE PCIERRA '
    global reporte_gramatical
    reporte_gramatical.append("<CONDICION> ::= \"NOW\" \"(\" \")\"")
    ret = Retorno(Now(), NodoAST('NOW'))
    t[0] = ret

def p_FuncionesSistemaAlias(t):
    'FUNCIONES_SISTEMA  :   ID_FUNCION PABRE LCONDICION_FUNCION PCIERRA ALIAS   '
    global reporte_gramatical
    reporte_gramatical.append("<FUNCIONES_SISTEMA> ::= <ID_FUNCION> \"(\" <LCONDICION_FUNCION> \")\" <ALIAS>")
    ret = Retorno(FuncionesMatematicas(t[1], t[3].getInstruccion(), t[5].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(t[3].getNodo())
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

def p_FuncionesSistema(t):
    'FUNCIONES_SISTEMA  :   ID_FUNCION PABRE LCONDICION_FUNCION PCIERRA   '
    global reporte_gramatical
    reporte_gramatical.append("<FUNCIONES_SISTEMA> ::= <ID_FUNCION> \"(\" <LCONDICION_FUNCION> \")\" \";\"")
    ret = Retorno(FuncionesMatematicas(t[1], t[3].getInstruccion(), t[1]), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_FuncionesSistemaString(t):
    'FUNCIONES_SISTEMA  :   ID_FUNCION_S PABRE LCONDICION_FUNCION_S PCIERRA ALIAS   '
    global reporte_gramatical
    reporte_gramatical.append("<FUNCIONES_SISTEMA> ::= <ID_FUNCION_S> \"(\" <LCONDICION_FUNCION_S> \")\" <ALIAS>")
    ret = Retorno(FuncionesSistema(t[1], t[3].getInstruccion(), t[5].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(t[3].getHijo())
    ret.getNodo().setHijo(t[5].getHijo())
    t[0] = ret

def p_FuncionesSistemaString1(t):
    'FUNCIONES_SISTEMA  :   ID_FUNCION_S PABRE LCONDICION_FUNCION_S PCIERRA   '
    global reporte_gramatical
    reporte_gramatical.append("<FUNCIONES_SISTEMA> ::= <ID_FUNCION> \"(\" <LCONDICION_FUNCION_S> \")\"")
    ret = Retorno(FuncionesSistema(t[1], t[3].getInstruccion(), None), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_FuncionesSistemaTrimA(t):
    'FUNCIONES_SISTEMA  :   TRIM PABRE LBOTH CADENA FROM CADENA PCIERRA ALIAS   '
    global reporte_gramatical
    reporte_gramatical.append("<FUNCIONES_SISTEMA> ::= \"TRIM\" \"(\" <LBOTH> \"CADENA\" \"FROM\" \"CADENA\" \")\" <ALIAS>")
    ret = Retorno(FuncionTrim(t[3], t[4], t[6], t[8].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('TRIM'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[4]))
    ret.getNodo().setHijo(NodoAST(t[6]))
    ret.getNodo().setHijo(t[8].getNodo())
    t[0] = ret

def p_FuncionesSistemaTrim(t):
    'FUNCIONES_SISTEMA  :   TRIM PABRE LBOTH CADENA FROM CADENA PCIERRA   '
    global reporte_gramatical
    reporte_gramatical.append("<FUNCIONES_SISTEMA> ::= \"TRIM\" \"(\" <LBOTH> \"CADENA\" \"FROM\" \"CADENA\" \")\"")
    ret = Retorno(FuncionTrim(t[3], t[4], t[6], None), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('TRIM'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[4]))
    ret.getNodo().setHijo(NodoAST(t[6]))
    t[0] = ret

def p_FuncionesSistemaTrimA1(t):
    'FUNCIONES_SISTEMA  :   TRIM PABRE LBOTH FROM CADENA COMA CADENA PCIERRA ALIAS   '
    global reporte_gramatical
    reporte_gramatical.append("\"TRIM\" \"(\" <LBOTH> \"FROM\" \"CADENA\" \",\" \"CADENA\" \")\" <ALIAS>")
    ret = Retorno(FuncionTrim(t[3], t[5], t[7], t[9].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('TRIM'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[5]))
    ret.getNodo().setHijo(NodoAST(t[7]))
    ret.getNodo().setHijo(t[9].getNodo())
    t[0] = ret

def p_FuncionesSistemaTrim1(t):
    'FUNCIONES_SISTEMA  :   TRIM PABRE LBOTH FROM CADENA COMA CADENA PCIERRA   '
    global reporte_gramatical
    reporte_gramatical.append("\"TRIM\" \"(\" <LBOTH> \"FROM\" \"CADENA\" \",\" \"CADENA\" \")\"")
    ret = Retorno(FuncionTrim(t[3], t[5], t[7], None), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('TRIM'))
    ret.getNodo().setHijo(NodoAST(t[3]))
    ret.getNodo().setHijo(NodoAST(t[5]))
    ret.getNodo().setHijo(NodoAST(t[7]))
    t[0] = ret

def p_Id_FuncionSubstring(t):
    'ID_FUNCION_S  :   SUBSTRING   '
    global reporte_gramatical
    reporte_gramatical.append("<ID_FUNCION_S> ::= \"SUBSTRING\"")
    t[0] = 'SUBSTRING'

def p_Id_FuncionLength(t):
    'ID_FUNCION_S  :   LENGTH   '
    global reporte_gramatical
    reporte_gramatical.append("<ID_FUNCION_S> ::= \"LENGTH\"")
    t[0] = 'LENGTH'

def p_Id_FuncionSubstr(t):
    'ID_FUNCION_S  :   SUBSTR   '
    global reporte_gramatical
    reporte_gramatical.append("<ID_FUNCION_S> ::= \"SUBSTR\"")
    t[0] = 'SUBSTR'

def p_LBOTHLeading(t):
    'LBOTH  :   LEADING   '
    global reporte_gramatical
    reporte_gramatical.append("<LBOTH> ::= \"LEADING\"")
    t[0] = 'LEADING'

def p_LBOTHTrailing(t):
    'LBOTH  :   TRAILING   '
    global reporte_gramatical
    reporte_gramatical.append("<LBOTH> ::= \"TRAILING\"")
    t[0] = 'TRAILING'

def p_LBOTHBoth(t):
    'LBOTH  :   BOTH   '
    global reporte_gramatical
    reporte_gramatical.append("<LBOTH> ::= \"BOTH\"")
    t[0] = 'BOTH'

def p_LCondicionFuncion_Condicion(t):
    'LCONDICION_FUNCION_S  :   CONDICION   '
    global reporte_gramatical
    reporte_gramatical.append("<LCONDICION_FUNCION_S> ::= <CONDICION>")
    t[0] = t[1]

def p_LCondicionFuncion_S(t):
    'LCONDICION_FUNCION_S  :   CONDICION COMA NUMERO COMA NUMERO   '
    global reporte_gramatical
    reporte_gramatical.append("<LCONDICION_FUNCION_S> ::= <CONDICION> \",\" \"NUMERO\" \",\" \"NUMERO\"")
    val = [t[1].getInstruccion(), Numero(t[3]), Numero(t[5])]
    ret = Retorno(val, NodoAST('PARAMETROS'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(NodoAST(str(t[3])))
    ret.getNodo().setHijo(NodoAST(str(t[5])))
    t[0] = ret

def p_IdFuncionAbs(t):
    'ID_FUNCION  :   ABS  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_FUNCION> ::= \"ABS\"")
    t[0] = 'ABS'

def p_IdFuncionCBRT(t):
    'ID_FUNCION  :   CBRT  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_FUNCION> ::= \"CBRT\"")
    t[0] = 'CBRT'

def p_IdFuncionCeil(t):
    'ID_FUNCION  :   CEIL  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_FUNCION> ::= \"CEIL\"")
    t[0] = 'CEIL'

def p_IdFuncionCeiling(t):
    'ID_FUNCION  :   CEILING  '
    global reporte_gramatical
    reporte_gramatical.append("<ID_FUNCION> ::= \"CEILING\"")
    t[0] = 'CEILING'

def p_LCondicionFuncion1(t):
    'LCONDICION_FUNCION  :   CONDICION  '
    global reporte_gramatical
    reporte_gramatical.append("<LCONDICION_FUNCION> ::= <CONDICION>")
    val = [t[1].getInstruccion()]
    ret = Retorno(val, NodoAST('VALOR'))
    ret.getNodo().setHijo(t[1].getNodo())
    t[0] = ret

def p_LCondicionFuncion(t):
    'LCONDICION_FUNCION  :   LCONDICION_FUNCION COMA CONDICION  '
    global reporte_gramatical
    reporte_gramatical.append("<LCONDICION_FUNCION> ::= <LCONDICION_FUNCION> \",\" <CONDICION>")
    val = t[1].getInstruccion()
    val.append(t[3].getInstruccion())
    ret = Retorno(val, NodoAST('VALOR'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_DateTimeYear(t):
    'DATETIME  :   YEAR '
    global reporte_gramatical
    reporte_gramatical.append("<DATETIME> ::= \"YEAR\"")
    t[0] = 'YEAR'

def p_DateTimeHour(t):
    'DATETIME  :   HOUR '
    global reporte_gramatical
    reporte_gramatical.append("<DATETIME> ::= \"HOUR\"")
    t[0] = 'HOUR'

def p_DateTimeMinute(t):
    'DATETIME  :   MINUTE '
    global reporte_gramatical
    reporte_gramatical.append("<DATETIME> ::= \"MINUTE\"")
    t[0] = 'MINUTE'

def p_DateTimeSecond(t):
    'DATETIME  :   SECOND '
    global reporte_gramatical
    reporte_gramatical.append("<DATETIME> ::= \"SECOND\"")
    t[0] = 'SECOND'

def p_DateTimeMonth(t):
    'DATETIME  :   MONTH '
    global reporte_gramatical
    reporte_gramatical.append("<DATETIME> ::= \"MONTH\"")
    t[0] = 'MONTH'
    
def p_DateTimeDay(t):
    'DATETIME  :   DAY '
    global reporte_gramatical
    reporte_gramatical.append("<DATETIME> ::= \"DAY\"")
    t[0] = 'DAY'

def p_FuncionesWhereExist(t):
    'FUNCIONES_WHERE  :   EXISTS PABRE SUBCONSULTA PCIERRA   '
    global reporte_gramatical
    reporte_gramatical.append("<FUNCIONES_WHERE> ::= \"EXISTS\" \"(\" <SUBCONSULTA> \")\"")
    ret = Retorno(Exists(t[3].getInstruccion()), NodoAST('FUNCION'))
    ret.getNodo().setHijo(NodoAST('EXISTS'))
    ret.getNodo().setHijo(t[3].getNodo())
    t[0] = ret

def p_FuncionesWhereIn(t):
    'FUNCIONES_WHERE  :   CONDICION IN PABRE SUBCONSULTA PCIERRA   '
    global reporte_gramatical
    reporte_gramatical.append("<FUNCIONES_WHERE> ::= <CONDICION> \"IN\" \"(\" <SUBCONSULTA> \")\"")
    ret = Retorno(In(t[1].getInstruccion(), t[4].getInstruccion(), True), NodoAST('IN'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[4].getNodo())
    t[0] = ret

def p_FuncionesWhereNotIn(t):
    'FUNCIONES_WHERE  :   CONDICION NOT IN PABRE SUBCONSULTA PCIERRA   '
    global reporte_gramatical
    reporte_gramatical.append("<FUNCIONES_WHERE> ::= <CONDICION> \"NOT\" \"IN\" \"(\" <SUBCONSULTA> \")\"")
    ret = Retorno(In(t[1].getInstruccion(), t[5].getInstruccion(), False), NodoAST('NOT IN'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

def p_FuncionesWhereAny(t):
    'FUNCIONES_WHERE  :   CONDICION OPERATOR_FW ANY PABRE SUBCONSULTA PCIERRA   '
    global reporte_gramatical
    reporte_gramatical.append("<FUNCIONES_WHERE> ::= <CONDICION> <OPERATOR_FW> \"ANY\" \"(\" <SUBCONSULTA> \")\"")
    ret = Retorno(Any_op(t[1].getInstruccion(), t[2], 'ANY', t[5].getInstruccion()), NodoAST(t[2]))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(NodoAST('ANY'))
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

def p_FuncionesWhereAll(t):
    'FUNCIONES_WHERE  :   CONDICION OPERATOR_FW ALL PABRE SUBCONSULTA PCIERRA   '
    global reporte_gramatical
    reporte_gramatical.append("<FUNCIONES_WHERE> ::= <CONDICION> <OPERATOR_FW> \"ALL\" \"(\" <SUBCONSULTA> \")\"")
    ret = Retorno(Any_op(t[1].getInstruccion(), t[2], 'ALL', t[5].getInstruccion()), NodoAST(t[2]))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(NodoAST('ALL'))
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

def p_FuncionesWhereSome(t):
    'FUNCIONES_WHERE  :   CONDICION OPERATOR_FW SOME PABRE SUBCONSULTA PCIERRA   '
    global reporte_gramatical
    reporte_gramatical.append("<FUNCIONES_WHERE> ::= <CONDICION> <OPERATOR_FW> \"SOME\" \"(\" <SUBCONSULTA> \")\"")
    ret = Retorno(Any_op(t[1].getInstruccion(), t[2], 'SOME', t[5].getInstruccion()), NodoAST(t[2]))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(NodoAST('SOME'))
    ret.getNodo().setHijo(t[5].getNodo())
    t[0] = ret

def p_FuncionesWhereLike(t):
    'FUNCIONES_WHERE  :   CONDICION LIKE CADENA   '
    global reporte_gramatical
    reporte_gramatical.append("<FUNCIONES_WHERE> ::= <CONDICION> \"LIKE\" \"CADENA\"")
    ret = Retorno(Like(t[1].getInstruccion(), t[3], True), NodoAST('LIKE'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(NodoAST(t[3]))
    t[0] = ret

def p_FuncionesWhereNotLike(t):
    'FUNCIONES_WHERE  :   CONDICION NOT LIKE CADENA   '
    global reporte_gramatical
    reporte_gramatical.append("<FUNCIONES_WHERE> ::= <CONDICION> \"NOT\" \"LIKE\" \"CADENA\"")
    ret = Retorno(Like(t[1].getInstruccion(), t[3], False), NodoAST('NOT LIKE'))
    ret.getNodo().setHijo(t[1].getNodo())
    ret.getNodo().setHijo(NodoAST(t[4]))
    t[0] = ret

def p_OperatorFwMenor(t):
    'OPERATOR_FW  :   MENOR   '
    global reporte_gramatical
    reporte_gramatical.append("<OPERATOR_FW> ::= \"" + str(t[1]) + "\"")
    t[0] = t[1]

def p_OperatorFwMayor(t):
    'OPERATOR_FW  :   MAYOR   '
    global reporte_gramatical
    reporte_gramatical.append("<OPERATOR_FW> ::= \"" + str(t[1]) + "\"")
    t[0] = t[1]

def p_OperatorFwMenorIgual(t):
    'OPERATOR_FW  :   MENORIGUAL   '
    global reporte_gramatical
    reporte_gramatical.append("<OPERATOR_FW> ::= \"" + str(t[1]) + "\"")
    t[0] = t[1]

def p_OperatorFwMayorIgual(t):
    'OPERATOR_FW  :   MAYORIGUAL   '
    global reporte_gramatical
    reporte_gramatical.append("<OPERATOR_FW> ::= \"" + str(t[1]) + "\"")
    t[0] = t[1]

def p_OperatorFwIgual(t):
    'OPERATOR_FW  :   IGUAL   '
    global reporte_gramatical
    reporte_gramatical.append("<OPERATOR_FW> ::= \"" + str(t[1]) + "\"")
    t[0] = t[1]

def p_OperatorFwDif(t):
    'OPERATOR_FW  :   DIF   '
    global reporte_gramatical
    reporte_gramatical.append("<OPERATOR_FW> ::= \"" + str(t[1]) + "\"")
    t[0] = t[1]

def p_OperatorFwDif1(t):
    'OPERATOR_FW  :   DIF1   '
    global reporte_gramatical
    reporte_gramatical.append("<OPERATOR_FW> ::= \"" + str(t[1]) + "\"")
    t[0] = t[1]

def p_PTimestamC(t):
    'PTIMESTAMP  :   TIMESTAMP CADENA '
    global reporte_gramatical
    reporte_gramatical.append("<PTIMESTAMP> ::= \"TIMESTAMP\" \"CADENA\"")
    ret = Retorno(Cadena(t[2]), NodoAST(t[2]))
    t[0] = ret

def p_PTimestamId(t):
    'PTIMESTAMP  :   TIMESTAMP ID '
    global reporte_gramatical
    reporte_gramatical.append("<PTIMESTAMP> ::= \"TIMESTAMP\" \"ID\"")
    ret = Retorno(Id(t[2], None), NodoAST(t[2]))
    t[0] = ret

def p_PTimestamIdPId(t):
    'PTIMESTAMP  :   TIMESTAMP ID PUNTO ID '
    global reporte_gramatical
    reporte_gramatical.append("<PTIMESTAMP> ::= \"TIMESTAMP\" \"ID\" \".\" \"ID\"")
    ret = Retorno(Id(t[4], t[2]), NodoAST('.'))
    ret.getNodo().setHijo(NodoAST(t[2]))
    ret.getNodo().setHijo(NodoAST(t[4]))

def p_PTimestamCadena(t):
    'PTIMESTAMP  :   CADENA '
    global reporte_gramatical
    reporte_gramatical.append("<PTIMESTAMP> ::= \"CADENA\"")
    ret = Retorno(Cadena(t[1]), NodoAST(t[1]))
    t[0] = ret

def p_PTimestamId1(t):
    'PTIMESTAMP  :   ID '
    global reporte_gramatical
    reporte_gramatical.append("<PTIMESTAMP> ::= \"ID\"")
    ret = Retorno(Id(t[1], None), NodoAST(t[1]))
    t[0] = ret

def p_PTimestamIdP(t):
    'PTIMESTAMP  :   ID PUNTO ID '
    global reporte_gramatical
    reporte_gramatical.append("<PTIMESTAMP> ::= \"ID\" \".\" \"ID\"")
    ret = Retorno(Id(t[3], t[1]), NodoAST('.'))
    ret.getNodo().setHijo(NodoAST(t[1]))
    ret.getNodo().setHijo(NodoAST(t[3]))

def p_empty(t):
    'EMPTY :'

def p_error(t):
    global counter_syntactic_error
    err = open("reports/error_syntactic.txt", "a+")
    txt = '<tr><td>' + str(counter_syntactic_error) + '</td>'
    txt += '<td>' + str(t.value) + '</td>'
    txt += '<td>' + 'Texto ingresado no reconocido.' + '</td>'
    txt += '<td>' + str(t.lexer.lineno) + '</td>'
    txt += '<td>' + str(get_column(t.lexer.lexdata, t)) + '</td><tr>\n'
    err.write(txt)
    err.close()
    counter_syntactic_error += 1
    if not t:
        return
    while True:
        entry = parser.token()
        if not entry or entry.type == 'PCOMA':
            break
    parser.restart()


# START PARSING THE INPUT TEXT
parser = yacc.yacc()


def parse(p_input):
    global counter_lexical_error, counter_syntactic_error
    counter_lexical_error = 1
    counter_syntactic_error = 1
    return parser.parse(p_input)

def analizar(input):
    global reporte_gramatical
    instrucciones_bnf = []  
    file = open ("proyecto/gramatica.md","w")
    for instruccion_bnf in reversed(reporte_gramatical) :
        file.write(instruccion_bnf)
        file.write("\n")
    file.close()
