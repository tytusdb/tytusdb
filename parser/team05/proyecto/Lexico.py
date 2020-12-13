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
import re

# VARIABLES GLOBALES
counter_lexical_error = 1
counter_syntactic_error = 1

# LISTADO DE PALABRAS RESERVADAS
palabras_reservadas = {
    'select'        : 'SELECT',
    'from'          : 'FROM',
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
    'isnull'        : 'ISNULL',
    'notnull'       : 'NOTNULL',
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
    'exists'         : 'EXISTS',
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
    'if'            : 'IF',
    'exists'        : 'EXISTS',
    'owner'         : 'OWNER',
    'mode'          : 'MODE',
    'alter'         : 'ALTER',
    'drop'          : 'DROP',
    'show'          : 'SHOW',
    'rename'        : 'RENAME',
    'owner'         : 'OWNER',
    'to'            : 'TO',
    'insert'        : 'INSERT',
    'update'        : 'UPDATE',
    'set'           : 'SET',
    'into'          : 'INTO',
    'values'        : 'VALUES',
    'table'         : 'TABLE',
    'from'          : 'FROM',
    'delete'        : 'DELETE'
    

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
    'DECIMAL',
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
    'DesplazaD',
    'CADENASI'
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


def t_DECIMAL(t):
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
    r'\".*?\"'
    t.value = t.value[1:-1] 
    return t 

def t_CADENASI(t):
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
    ('left','OR'),
    ('left','AND'),
    ('right', 'NOT'),
    ('nonassoc', 'IS', 'ISNULL', 'NOTNULL'),
    ('left','MENORIGUAL','MAYORIGUAL','IGUAL', 'DIF', 'DIF1', 'MENOR', 'MAYOR'),
    ('nonassoc','BETWEEN'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO', 'MODULO'),
    ('left', 'EXP'),
    ('right','UMENOS', 'UMAS')

)


# GRAMMAR DEFINITION
def p_Inicio(t):
    'INSTRUCCIONES  :   INSTRUCCIONES INSTRUCCION   '
    t[0] = "terminado"

def p_Inicio1(t):
    'INSTRUCCIONES  :   INSTRUCCION '

def p_Instruccion(t):
    'INSTRUCCION  :   I_SELECT  '

def p_Instruccion1(t):
    'INSTRUCCION  :   I_CREATE  '

def p_Instruccion2(t):
    'INSTRUCCION  :   I_DROP '

def p_Instruccion3(t):
    'INSTRUCCION  :   I_INSERT '

def p_Instruccion4(t):
    'INSTRUCCION  :   I_ALTER '

def p_Instruccion5(t):
    'INSTRUCCION  :   I_UPDATE '

def p_Instruccion6(t):
    'INSTRUCCION  :   I_SHOW '

def p_Instruccion7(t):
    'INSTRUCCION  :   I_DELETE '

def p_Create(t):
    'I_CREATE      : CREATE I_REPLACE'
    t[0] = t[2]
    print('Se creo la base de datos ' + t[0])

def p_Replace(t):
    'I_REPLACE     : OR REPLACE DATABASE I_EXIST'
    t[0] = t[4]
def p_Replace1(t):
    'I_REPLACE     : DATABASE I_EXIST'
    t[0] = t[2]

def p_drop(t):
    'I_DROP      : DROP I_TDROP ' 

def p_alter(t):
    'I_ALTER     : ALTER I_TALTER'

def p_tAlter(t):
    'I_TALTER    : I_ALTERDB'

def p_tDrop(t):
    'I_TDROP     : I_DROPDB'

def p_tDrop2(t):
    'I_TDROP     : I_DROPTB'

def p_dropDB(t):
    'I_DROPDB    : DATABASE I_IFEXIST'

def p_ifExist(t):
    'I_IFEXIST     : IF EXISTS ID PCOMA'

def p_ifExist2(t):
    'I_IFEXIST     : ID PCOMA'

def p_Exist(t):
    'I_EXIST       : IF NOT EXISTS ID I_OWMOD '
    t[0] = t[4]
def p_Exist1(t):
    'I_EXIST       : ID PCOMA'
    t[0] = t[1]

def p_Owmod(t):
    'I_OWMOD       : OWNER IGUAL ID I_MODE'

def p_Owmod1(t):
    'I_OWMOD       : MODE IGUAL ID I_OWNER'

def p_Owmod2(t):
    'I_OWMOD       : PCOMA'

def p_Mode(t):
    'I_MODE        : MODE IGUAL ID PCOMA'

def p_Mode1(t):
    'I_MODE        : PCOMA'

def p_Owner(t):
    'I_OWNER       : OWNER IGUAL ID PCOMA'

def p_Owner1(t):
    'I_OWNER       : PCOMA'

def p_AlterDB(t):
    'I_ALTERDB     : ALTER DATABASE ID I_OPALTERDB I_VALALTDB'

def p_opAlterDB(t):
    'I_OPALTERDB   : RENAME TO'

def p_opAlterDB2(t):
    'I_OPALTERDB   : OWNER TO'

def p_valAlterDb(t):
    'I_VALALTDB    : ID'

def p_valAlterDb1(t):
    'I_VALALTDB    : CADENASI'

def p_dropTB(t):
    'I_DROPTB      : TABLE ID PCOMA'

def p_insertTB(t):
    'I_INSERT      : INSERT INTO ID VALUES PABRE I_LVALT PCIERRA PCOMA'

def p_lValt(t):
    'I_LVALT       : I_LVALT COMA I_VALTAB'

def p_update(t):
    'I_UPDATE      : UPDATE ID SET I_LUPDATE PWHERE '

def p_lUpdate(t):
    'I_LUPDATE     : I_LUPDATE COMA I_VALUPDATE'

def p_lUpdate1(t):
    'I_LUPDATE     : I_VALUPDATE'

def p_valUpdate(t):
    'I_VALUPDATE   : ID IGUAL I_VALOR'

def p_valor(t):
    'I_VALOR       : CADENASI'

def p_valor1(t):
    'I_VALOR      : NUMERO'

def p_show(t):
    'I_SHOW       : SHOW DATABASE PCOMA'

def p_delete(t):
    'I_DELETE     : DELETE FROM ID PWHERE'

def p_lValt1(t):
    'I_LVALT       : I_VALTAB'

def p_valTab(t):
    'I_VALTAB      : NUMERO'

def p_valTab1(t):
    'I_VALTAB      : CADENASI'

def p_ISelect(t):
    'I_SELECT  :   SELECT VALORES PFROM COMPLEMENTO   '
    
def p_ISelect1(t):
    'I_SELECT  :   SELECT VALORES PFROM PWHERE COMPLEMENTO    '

def p_ISelect2(t):
    'I_SELECT  :   SELECT DISTINCT VALORES PFROM COMPLEMENTO   '

def p_ISelect3(t):
    'I_SELECT  :   SELECT DISTINCT VALORES PFROM PWHERE COMPLEMENTO    '

def p_ISelect4(t):
    'I_SELECT   :   SELECT VALORES '

def p_ComplementoH(t):
    'COMPLEMENTO  :   PGROUPBY PHAVING  '

def p_ComplementoHL(t):
    'COMPLEMENTO  :   PGROUPBY PHAVING PLIMIT   '

def p_ComplementoG(t):
    'COMPLEMENTO  :   PGROUPBY  '

def p_ComplementoGL(t):
    'COMPLEMENTO  :   PGROUPBY PLIMIT   '

def p_ComplementoO(t):
    'COMPLEMENTO  :   PORDERBY  '

def p_ComplementoOL(t):
    'COMPLEMENTO  :   PORDERBY PLIMIT   '

def p_ComplementoL(t):
    'COMPLEMENTO  :   PLIMIT    '

def p_ComplementoE(t):
    'COMPLEMENTO  :   EMPTY '

def p_Limit(t):
    'PLIMIT  :   LIMIT CONDICION    '

def p_LimitOff(t):
    'PLIMIT  :   LIMIT CONDICION OFFSET CONDICION   '

def p_OrderBy(t):
    'PORDERBY  :   ORDER BY LCOMPLEMENTOORDERBY '

def p_ComplementoOrderL(t):
    'LCOMPLEMENTOORDERBY  :   LCOMPLEMENTOORDERBY COMA COMPLEMENTOORDERBY  '

def p_ComplementoOrderL1(t):
    'LCOMPLEMENTOORDERBY  :   COMPLEMENTOORDERBY    '

def p_ComplementoOrderCI(t):
    'COMPLEMENTOORDERBY  :   ID COMPLEMENTOORDERBY1    '

def p_ComplementoOrderCOBC(t):
    'COMPLEMENTOORDERBY1  :   COMPLEMENTOORDER   '

def p_ComplementoOrderCOBP(t):
    'COMPLEMENTOORDERBY1  :   PUNTO ID COMPLEMENTOORDER   '


def p_ComplementoOrder(t):
    'COMPLEMENTOORDER  :   ASC  '

def p_ComplementoOD(t):
    'COMPLEMENTOORDER  :   DESC '

def p_ComplementoOANF(t):
    'COMPLEMENTOORDER  :   ASC NULLS FIRST  '

def p_ComplementoOANL(t):
    'COMPLEMENTOORDER  :   ASC NULLS LAST   '

def p_ComplementoODNF(t):
    'COMPLEMENTOORDER  :   DESC NULLS FIRST '

def p_ComplementoODNL(t):
    'COMPLEMENTOORDER  :   DESC NULLS LAST  '

def p_ComplementoEm(t):
    'COMPLEMENTOORDER  :   EMPTY    '


def p_Having(t):
    'PHAVING  :   HAVING CONDICION '

def p_GroupBy(t):
    'PGROUPBY  :   GROUP BY LCOMPLEMENTOGROUP '

def p_ComplementoGroupL(t):
    'LCOMPLEMENTOGROUP  :   LCOMPLEMENTOGROUP COMA COMPLEMENTOGROUP '

def p_ComplementoGroupLS(t):
    'LCOMPLEMENTOGROUP  :   COMPLEMENTOGROUP '

def p_ComplementoGroupC(t):
    'COMPLEMENTOGROUP  :   ID '

def p_ComplementoGroupC1(t):
    'COMPLEMENTOGROUP  :   ID PUNTO ID '

def p_Valores(t):
    'VALORES  :   POR '

def p_ValoresLista(t):
    'VALORES  :   LISTAVALORES '

def p_ListaValores(t):
    'LISTAVALORES  :   LISTAVALORES COMA VALOR '

def p_ListaValoresS(t):
    'LISTAVALORES  :   VALOR '


def p_ValorSub(t):
    'VALOR  :   PABRE SUBCONSULTA PCIERRA ALIAS'

def p_ValorSub1(t):
    'VALOR  :   PABRE SUBCONSULTA PCIERRA '

def p_ValorCountAa(t):
    'VALOR  :   COUNT PABRE POR PCIERRA ALIAS'

def p_ValorCounta(t):
    'VALOR  :   COUNT PABRE ID PCIERRA ALIAS'

def p_ValorCountA(t):
    'VALOR  :   COUNT PABRE POR PCIERRA '

def p_ValorCount(t):
    'VALOR  :   COUNT PABRE ID PCIERRA '

def p_ValorCountAliasId(t):
    'VALOR  :   COUNT PABRE ID PUNTO ID PCIERRA ALIAS'

def p_ValorCountIdP(t):
    'VALOR  :   COUNT PABRE ID PUNTO ID PCIERRA'

def p_ValorFunciones(t):
    'VALOR  :   FUNCION PABRE ID PUNTO ID PCIERRA'

def p_ValorFunciones1(t):
    'VALOR  :   FUNCION PABRE ID  PCIERRA'

def p_ValorFuncionesA(t):
    'VALOR  :   FUNCION PABRE ID PUNTO ID PCIERRA ALIAS'

def p_ValorFunciones1A(t):
    'VALOR  :   FUNCION PABRE ID  PCIERRA ALIAS'

def p_funcionAvg(t):
    'FUNCION    :   AVG'

def p_funcionSum(t):
    'FUNCION    :   SUM'

def p_funcionMin(t):
    'FUNCION    :   MIN'

def p_funcionMax(t):
    'FUNCION    :   MAX'

def p_Alias(t):
    'ALIAS  :   AS ID '

def p_AliasS(t):
    'ALIAS  :   ID '

def p_AliasC(t):
    'ALIAS  :   AS IDALIAS'

def p_AliasCS(t):
    'ALIAS  :   IDALIAS'

def p_FromIdA(t):
    'PFROM  :   FROM ID ALIAS '

def p_FromId(t):
    'PFROM  :   FROM ID '

def p_FromSub(t):
    'PFROM  :   FROM PABRE SUBCONSULTA PCIERRA ALIAS    '

def p_SubconsultaFrom(t):
    'SUBCONSULTA    :   SELECT VALORES PFROM COMPLEMENTO '

def p_SubconsultaFromW(t):
    'SUBCONSULTA    :   SELECT VALORES PFROM PWHERE COMPLEMENTO '


def p_Where(t):
    'PWHERE  :   WHERE CONDICION '

def p_CondicionIgual(t):
    'CONDICION  :   CONDICION IGUAL CONDICION '

def p_CondicionDif(t):
    'CONDICION  :   CONDICION DIF CONDICION '

def p_CondicionDif1(t):
    'CONDICION  :   CONDICION DIF1 CONDICION '

def p_CondicionMenor(t):
    'CONDICION  :   CONDICION MENOR CONDICION '

def p_CondicionMenorI(t):
    'CONDICION  :   CONDICION MENORIGUAL CONDICION '

def p_CondicionMayor(t):
    'CONDICION  :   CONDICION MAYOR CONDICION '

def p_CondicionMayorI(t):
    'CONDICION  :   CONDICION MAYORIGUAL CONDICION '

def p_CondicionAnd(t):
    'CONDICION  :   CONDICION AND CONDICION '

def p_CondicionOr(t):
    'CONDICION  :   CONDICION OR CONDICION '

def p_CondicionNot(t):
    'CONDICION  :   NOT CONDICION '

def p_CondicionParentesis(t):
    'CONDICION  :   PABRE CONDICION PCIERRA '

def p_CondicionMas(t):
    'CONDICION  :   CONDICION MAS CONDICION '

def p_CondicionMenos(t):
    'CONDICION  :   CONDICION MENOS CONDICION '

def p_CondicionPor(t):
    'CONDICION  :   CONDICION POR CONDICION '

def p_CondicionDiv(t):
    'CONDICION  :   CONDICION DIVIDIDO CONDICION '

def p_CondicionMod(t):
    'CONDICION  :   CONDICION MODULO CONDICION '

def p_CondicionExp(t):
    'CONDICION  :   CONDICION EXP CONDICION '

def p_CondicionIs(t):
    'CONDICION  :   CONDICION IS CONDICION '

def p_CondicionIsN(t):
    'CONDICION  :   CONDICION ISNULL CONDICION '

def p_CondicionNotN(t):
    'CONDICION  :   CONDICION NOTNULL CONDICION '

def p_CondicionM(t):
    'CONDICION  :   MENOS CONDICION %prec UMENOS'

def p_CondicionP(t):
    'CONDICION  :   MAS CONDICION %prec UMAS'

def p_CondicionNum(t):
    'CONDICION  :   NUMERO '

def p_CondicionDec(t):
    'CONDICION  :   DECIMAL'

def p_CondicionCad(t):
    'CONDICION  :   CADENA '

def p_CondicionTrue(t):
    'CONDICION  :   TRUE '

def p_CondicionFalse(t):
    'CONDICION  :   FALSE '

def p_CondicionId(t):
    'CONDICION  :   ID '

def p_CondicionIdP(t):
    'CONDICION  :   ID PUNTO ID '

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
        if not entry or entry.type == 'RBRACE':
            break
    parser.restart()


# START PARSING THE INPUT TEXT
parser = yacc.yacc()


def parse(p_input):
    global counter_lexical_error, counter_syntactic_error
    counter_lexical_error = 1
    counter_syntactic_error = 1
    return parser.parse(p_input)
