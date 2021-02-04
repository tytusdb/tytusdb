#LEX
from ply import *
from InstruccionesPL.ExceptionPL import ExceptionPL
elex = []
lista_errores_lexico=[]
global columna
columna=0
#lexer = lex.lex()

keywords = (
    'IF', 'THEN', 'END', 'ELSE', 'ELSIF', 'CASE', 'WHEN', 'LOOP', 'EXIT', 'CONTINUE', 'WHILE', 'FOR', 
    'IN', 'FOREACH', 'EXCEPTION', 'GET', 'STACKED', 'DIAGNOSTICS', 'RETURN', 'QUERY', 'EXECUTE', 'CALL', 'PERFORM', 'STRICT', 'RETURNING', 'USING', 'CURRENT',
    'RETURNS', 'BEGIN', 'CREATE', 'VARCHAR', 'DATE', 'NOT', 'NULL', 'IDENTITY', 'PRIMARY', 'KEY', 'ALTER', 'DATABASE', 'OWNER',
    'TABLE', 'ADD', 'DROP', 'INSERT', 'INTO', 'VALUES', 'UPDATE', 'SET', 'FROM','DELETE', 'SELECT', 
    'WHERE', 'AS', 'AND', 'OR','SMALLINT', 'INTEGER', 'BIGINT', 'DECIMAL', 'NUMERIC', 'REAL', 'DOUBLE', 'MONEY',
    'CHAR', 'VARYING', 'CHARACTER', 'TEXT', 'BOOLEAN', 'TYPE', 'ENUM', 'REPLACE',  'EXIST',  'COLUMN',
    'IS', 'TRUE', 'FALSE','USE', 'ARRAY', 'PG_CONTEXT',
    'ALIAS', 'CONSTANT', 'COLLATE', 'ROW_COUNT', 'DEFAULT', 'LANGUAGE', 'DECLARE', 'PROCEDURE', 'REFCURSOR', 'CURSOR',
    'SCROLL', 'NO', 'OPEN', 'FETCH', 'NEXT', 'OF', 'OUT', 'BACKWARD', 'FORWARD', 'LAST', 'RELATIVE', 'ABSOLUTE', 'FIRST',
    'PRIOR', 'CLOSE', 'MOVE', 'INT', 'FUNCTION', 'INOUT', 'CASCADE', 'RESTRICT', 'EXISTS', 'NULLS', 'OPCLASS',
    'RAISE', 'ON', 'INDEX', 'UNIQUE', 'ASC', 'DESC', 'TIMESTAMP', 'PRECISION', 'LOWER'
    )

tokens = keywords + (
	'IGUAL', 'MAS' ,'MENOS' ,'POR' ,'DIVISION','PAR1','PAR2','MENOR', 'MENORIGUAL', 'MAYOR', 'MAYORIGUAL', 
	'DIFERENTE', 'COMA', 'PUNTO', 'PYC', 'NUM', 'PDECIMAL' ,'CADENA', 'DOSP','VACIO', 'PORCENTAJE', 'COR1',
    'COR2', 'IDENTIFICADOR', 'CADENACARACTER', 'COMILLA', 'DOLLAR', 'NEWLINE', 'EXPONENCIACION'
)

t_EXPONENCIACION = r'\^'
t_IGUAL = r'='
t_PORCENTAJE = r'%'
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVISION = r'/'
t_PAR1 = r'\('
t_PAR2 = r'\)'
t_COR1 = r'\['
t_COR2 = r'\]'
t_MENOR = r'<'
t_MENORIGUAL = r'<='
t_MAYOR = r'>'
t_MAYORIGUAL = r'>='
t_DIFERENTE = r'<>'
t_COMA = r'\,'
t_PUNTO = r'\.'
t_PYC = r';'
t_DOSP = r':'
t_NUM = r'\d+'
t_VACIO = r'\'\''
t_PDECIMAL = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
#t_CADENA = r'\".*?\"'
t_CADENACARACTER = r'\'.*?\''
t_COMILLA = r'\''
t_DOLLAR = r'\$'

t_ignore_COMMENT = r'\/\*.*\*\/'

t_ignore = ' \t'


def t_IDENTIFICADOR(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    if t.value in keywords:
        t.type = t.value
    return t


def t_CADENA(t):
    r'\"(.|\n)*?\"'
    t.value = t.value[1:-1]  # remuevo las comillas dobles
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def columas(args):
    valor = lexer.lexpos-args
    return valor

def t_error(t):
    global columna
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)
    col = columas(columna)
    dato = ExceptionPL(0,"Error Lexico", f"El Simbolo << {t.value[0]} >> No Pertenece al Lenguaje", t.lexer.lineno, col)
    lista_errores_lexico.append(dato)
    t.lexer.skip(1)
    
import re

print("---------------------------------------")
lexer = lex.lex(reflags=re.IGNORECASE)
