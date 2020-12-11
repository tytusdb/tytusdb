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
    'min'           : 'MIN'

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
    'PCOMA'
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

# TOKENS IGNORADOS
t_ignore = " \t"

def t_NUMERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palabras_reservadas.get(t.value.lower(),'ID')    
    return t

def t_CADENA(t):
    r'\".*?\"'
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

def p_ISelect(t):
    'I_SELECT  :   SELECT VALORES PFROM COMPLEMENTO PCOMA   '

def p_ISelect1(t):
    'I_SELECT  :   SELECT VALORES PFROM PWHERE COMPLEMENTO PCOMA    '

def p_ISelect2(t):
    'I_SELECT  :   SELECT DISTINCT VALORES PFROM COMPLEMENTO PCOMA   '

def p_ISelect3(t):
    'I_SELECT  :   SELECT DISTINCT VALORES PFROM PWHERE COMPLEMENTO PCOMA    '


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

def p_Valor(t):
    'VALOR  :   ID ALIAS '

def p_Valor2(t):
    'VALOR  :   ID PUNTO ID ALIAS '

def p_Valor3(t):
    'VALOR  :   ID '

def p_Valor4(t):
    'VALOR  :   ID PUNTO ID'

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
