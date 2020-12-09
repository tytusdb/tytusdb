#import ply
import re

reservadas = {
    'smallint' : 'SMALLINT',
    'integer' : 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'real' : 'NUMERIC',
    'double' : 'DOUBLE',
    'precision' : 'PRECISION',
    'money' : 'MONEY',
    'text' : 'TEXT',
    'varying' : 'VARYING',
    'varchar' : 'VARCHAR',
    'character' : 'CHARACTER',
    'char' : 'CHAR',
    'timestamp' : 'TIMESTAMP',
    'date' : 'DATE',
    'time' : 'TIME',
    'interval' : 'INTERVAL',
    'year' : 'YEAR',
    'month' : 'MONTH',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'to' : 'TO',
    'boolean' : 'BOOLEAN',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'create' : 'CREATE',
    'type' : 'TYPE',
    'as' : 'AS',
    'enum' : 'ENUM',
    'not' : 'NOT',
    'and' : 'AND',
    'or' : 'OR',
    'is' : 'IS',
    'null':'NULL',
    'between':'BETWEEN',
    'in': 'IN',
    'like':'LIKE',
    'ilike':'ILIKE',
    'similar':'SIMILAR',
    'table': 'TABLE',
    'replace':'REPLACE',
    'database':'DATABASE',
    'show':'SHOW',
    'if':'IF',
    'alter':'ALTER',
    'rename':'RENAME',
    'owner':'OWNER',
    'drop':'DROP',
    'constraint':'CONSTRAINT',
    'unique':'UNIQUE',
    'check':'CHECK',
    'references':'REFERENCES',
    'primary':'PRIMARY',
    'key':'KEY',
    'foreign':'FOREIGN',
    'add':'ADD',
    'set':'SET',
    'select':'SELECT',
    'from':'FROM',
    'where': 'WHERE'
}

tokens  = [
    'PTCOMA',
    'LLAVIZQ',
    'LLAVDER',
    'PARIZQ',
    'PARDER',
    'IGUAL',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'CONCAT',
    'MENQUE',
    'MAYQUE',
    'IGUALQUE',
    'NIGUALQUE',
    'NUMDECIMAL',
    'ENTERO',
    'CADENA',



    'ID',
    'PORCENTAJE',
    'PUNTO',
    'DOSPUNTOS',
    'EXPONENCIAL',
    'MAYORIGUAL',
    'MENORIGUAL',
    'CORCHETEA',
    'CORCHETECER',
    'COMA'


] + list(reservadas.values())



# Tokens
t_PTCOMA    = r';'
t_LLAVIZQ   = r'{'
t_LLAVDER   = r'}'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_IGUAL     = r'='
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_CONCAT    = r'&'
t_MENQUE    = r'<'
t_MAYQUE    = r'>'
t_IGUALQUE  = r'=='
t_MAYORIGUAL = r'\>\='
t_MENORIGUAL = r'\<\='
#t_NIGUALQUE = r'!='
t_NIGUALQUE = r'NOT'
t_PORCENTAJE  = r'\%'
t_PUNTO  = r'\.'
t_DOSPUNTOS = r'\::'
t_EXPONENCIAL = r'\^'
t_CORCHETEA = r'\['
t_CORCHETECER = r'\]'
t_COMA = r'\,'

def t_NUMDECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor no es parseable a decimal %d",t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor no es parseable a integer %d",t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')
     return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t

def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Caracter irreconocible! '%s'"% t.value[0])
    #meter a tabla de errores!

    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()
lex.lex(reflags=re.IGNORECASE)

#import ply.yacc as yacc
#parser = yacc.yacc()

# Asociación de operadores y precedencia
precedence = (
    ('left','PUNTO'),
    ('left','DOSPUNTOS'),
    ('left','CORCHETECER','CORCHETEA'),
    ('left','POR'),
    ('left','DIVIDIDO'),
    ('left','PORCENTAJE'),
    ('left','MAS','MENOS'),
    ('right','UMENOS','UMAS')
    )

# Definición de la gramática
def p_init(t) :
    '''init            : instrucciones
                        '''
    t[0] = t[1]


def p_instrucciones(t):
    '''instrucciones : instrucciones instruccion

    '''
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones2(t):
    '''instrucciones : instruccion'''
    t[0] = [t[1]]


def p_instruccionSELECT(t):
    '''instruccion : inst_select
                    '''
    t[0]=t[1]

def p_instrucciondb(t):
    '''instruccion : createdb
                    '''
    t[0]=t[1]

def p_instselect(t):
    '''inst_select : SELECT POR FROM ID PTCOMA'''

    t[0] = t[1]+' '+t[2]+' '+t[3]+' '+t[4]+ ' '+t[5]


def p_instselect2(t):
    '''inst_select : SELECT listaid FROM listaid PTCOMA'''
    #t[4].extend(t[5])
    #t[3]= t[3]+ t[4]
    #t[2].extend(t[3])
    #t[1] = t[1] + t[2]
    #t[0] = t[1] #+' '+t[2]+' '+t[3]+' '+t[4]+' '+t[5]

    t[0]= t[1] +' '+t[2][0] +', '+t[2][1]+', '+t[2][2]+' '+t[3]+ ' '+t[4][0]+t[5]


def p_selectAlias(t):
    '''inst_select : SELECT listaidA FROM listaidA PTCOMA'''
    t[0] = t[1] + ' ' + t[2][0] + ', ' + t[2][1] + ', ' + t[2][2] + ' ' + t[3] + ' ' + t[4][0] + t[5]

def p_selectAlias(t):
    '''inst_select : SELECT listaid FROM listaidA PTCOMA'''
    t[0] = t[1] + ' ' + t[2][0] + ', ' + t[2][1] + ', ' + t[2][2] + ' ' + t[3] + ' ' + t[4][0] + t[5]

def p_listaId2(t):
    '''listaid : listaid COMA ID'''
    #t[2].extend(t[3])
    t[1].append(t[3])
    t[0] = t[1]


def p_listaId3(t):
    '''listaid : ID '''
    t[0] = [t[1]]


def p_listaId2A(t):
    '''listaidA : listaidA COMA ID ID'''
    #t[2].extend(t[3])
    t[3]=t[3]+' '+t[4]
    t[1].append(t[3])
    t[0] = t[1]


def p_listaId3A(t):
    '''listaidA : ID ID'''
    t[0] = [t[1]+' '+t[2]]



def p_createdb2(t):
    '''createdb : CREATE DATABASE ID PTCOMA'''
    t[0] = t[1]+' '+t[2]+' '+t[3]+' '+t[4]



def p_expruminus(t) :
    'expr : MENOS ENTERO %prec UMENOS'
    t[0] = - t[2]


def p_expreumas(t):
    'expr : MAS ENTERO %prec UMAS'
    t[0] = + t[2]



def p_error(t):
    print("Error sintáctico en " + t.value)



import ply.yacc as yacc
parser = yacc.yacc()


while True:
    res = parser.parse("SELECT id,nombre,pais FROM continente c;")
    print(res)
    break