##-------------------------GRAMATICA ASCENDENTE-------------------------------
reservadas = {
    'create' : 'CREATE',
    'database' : 'DATABASE',    
    'table' : 'TABLE',
    'char' : 'CHAR',
    'varchar' : 'VARCHAR',
    'boolean' : 'BOOLEAN',
    'int' : 'INT',
    'integer' : 'INTEGER',
    'float' : 'FLOAT',
    'double' : 'DOUBLE',
    'date' : 'DATE',
    'year' : 'YEAR',
    'datetime' : 'DATETIME',
    'time' : 'TIME',
    'drop' : 'DROP',
    'alter' : 'ALTER',
    'delete' : 'DELETE',
    'not' : 'NOT',
    'null' : 'NULL',
    'foreign' : 'FOREIGN',
    'key' : 'KEY',
    'primary' : 'PRIMARY',
    'references' : 'REFERENCES',
    'use' : 'USE',
    'select' : 'SELECT',
    'distinct' : 'DISTINCT',
    'as' : 'AS',
    'from' : 'FROM',
    'left' : 'LEFT',
    'join' : 'JOIN',
    'right' : 'RIGHT',
    'on' : 'ON',
    'any' : 'ANY',
    'sum' : 'SUM',
    'like' : 'LIKE',
    'avg' : 'AVG',
    'max' : 'MAX',
    'min' : 'MIN',
    'order' : 'ORDER',
    'where' : 'WHERE',
    'and' : 'AND',
    'or' : 'OR',
    'between' : 'BETWEEN',
    'in' : 'IN',
    'inner' : 'INNER',
    'full' : 'FULL',
    'self' : 'SELF',
    'case' : 'CASE',
    'union' : 'UNION',
    'group' : 'GROUP',
    'having' : 'HAVING',
    'exists' : 'EXISTS',
    'all' : 'ALL',
    'into' : 'INTO',
    'some' : 'SOME',
    'backup' : 'backup',
    'to' : 'TO',
    'disk' : 'DISK',
    'constraint' : 'CONSTRAINT',
    'add' : 'ADD',
    'check' : 'CHECK',
    'default' : 'DEFAULT',
    'modify' : 'MODIFY',
    'column' : 'COLUMN',
    'set' : 'SET',
    'unique' : 'UNIQUE',
    'index' : 'INDEX',
    'auto_increment' : 'AUTO_INCREMENT',
    'values' : 'VALUES',
    'identity' : 'IDENTITY',
    'by' : 'BY',
    'with' : 'WITH',
    'replace' : 'REPLACE',    
    'desc' : 'DESC',
    'outer' : 'OUTER',
    'is' : 'IS',
    'top' : 'TOP',
    'truncate' : 'TRUNCATE',
    'update' : 'UPDATE',
    'asc' : 'ASC',
}

tokens  = [
    'PTCOMA',
    'PARIZQ',
    'PARDER',
    'COMA',
    'PUNTO',
    'MAS',
    'MENOS',
    'POR',
    'DIVISION',
    'MODULO',
    'CONCAT',
    'PIPE',
    'EXP',
    'IGUAL',
    'MAYOR',
    'MENOR',
    'MENORIGUAL',
    'MAYORIGUAL',
    'DIFERENTE',
    'ASIGNACION_SUMA',
    'ASIGNACION_RESTA',
    'ASIGNACION_MULT',
    'ASIGNACION_DIVID',
    'ASIGNACION_MODULO',
    'DOS_PUNTOS',
    'DIAG_INVERSA',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'ID'
] + list(reservadas.values())

# Tokens
t_PTCOMA            = r';'
t_PARIZQ            = r'\('
t_PARDER            = r'\)'
t_COMA              = r'\,'
t_PUNTO             = r'\.'
t_MAS               = r'\+'
t_MENOS             = r'-'
t_POR               = r'\*'
t_DIVISION          = r'/'
t_MODULO            = r'\%'
t_PIPE              = r'\|'
t_EXP               = r'\^'
t_IGUAL             = r'\='
t_MAYOR             = r'>'
t_MENOR             = r'<'
t_MENORIGUAL        = r'<='
t_MAYORIGUAL        = r'>='
t_DIFERENTE         = r'<>'
t_ASIGNACION_SUMA   = r'\+='
t_ASIGNACION_RESTA  = r'\-='
t_ASIGNACION_MULT   = r'\*='
t_ASIGNACION_DIVID  = r'\/='
t_ASIGNACION_MODULO = r'\%='
t_DOS_PUNTOS        = r'\:'
t_DIAG_INVERSA      = r'\\'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


# Asociación de operadores y precedencia
precedence = (
    ('left','CONCAT'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVISION'),
    ('left','MODULO','EXP'),
    #('right','UMENOS'),
    )

# Definición de la gramática

from expresiones import *
from instrucciones import *


def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion      : CREATE creacion
                        | USE cambio_bd
                        | SELECT selects
                        | DELETE deletes'''
    t[0] = t[2]
    

# INSTRUCCION CON "CREATE"
def p_instruccion_creacion(t) :
    '''creacion     : DATABASE crear_bd
                    | TABLE crear_tb'''
    print("Creacion")

def p_instruccion_crear_BD(t) :
    'crear_bd     : ID PTCOMA'
    t[0] = Crear_BD(t[1])
    print("Creacion de BD")

def p_instruccion_crear_TB(t) :
    '''crear_tb     : ID PARIZQ crear_tb_columnas PARDER crear_tb_herencia PTCOMA
                    | ID PARIZQ crear_tb_columnas PARDER crear_tb_herencia
                    | ID PARIZQ crear_tb_columnas PARDER PTCOMA
                    | ID PARIZQ crear_tb_columnas PARDER'''
    
    if t[5] != None and t[5] != ';':
        #Si t[5] existe y no es punto y coma, entonces la tabla tiene herencia
        t[0] = Crear_TB_Herencia(t[1], t[3], t[5])
    else:
        #Si t[5] no existe o es Punto y coma, entonces la tabla no tiene herencia
        t[0] = Crear_TB(t[1], t[3])

# INSTRUCCION CON "USE"
def p_instruccion_Use_BD(t) :
    'cambio_bd     : ID PTCOMA'
    t[0] = Cambio_BD(t[1])
    print("CAMBIO de BD")


# INSTRUCCIONES CON "SELECT"
def p_instruccion_selects(t) :
    '''selects      : POR FROM select_all
                    | lista_parametros FROM ID PTCOMA'''
    print("selects")

def p_instruccion_Select_All(t) :
    'select_all     : ID PTCOMA'
    t[0] = Select_All(t[1])
    print("Consulta ALL para tabla: " + t[1])

#========================================================
# LISTA DE PARAMETROS
def p_instrucciones_lista_parametros(t) :
    'lista_parametros    : lista_parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]
    print("Varios parametros")

def p_instrucciones_parametro(t) :
    'lista_parametros    : parametro '
    t[0] = [t[1]]
    print("Un parametro")

def p_parametro_con_tabla(t) :
    'parametro        : ID PUNTO name_column'
    t[0] = t[1]
    print("Parametro con indice de tabla")

def p_parametro_con_tabla_columna(t) :
    'name_column        : ID'
    t[0] = t[1]
    print("Nombre de la columna")

def p_parametro_sin_tabla(t) :
    'parametro        : ID'
    t[0] = t[1]
    print("Parametro SIN indice de tabla")
#========================================================

#========================================================
# LISTA DE CONDICIONES

#========================================================

#========================================================
# LISTA DE PARAMETROS PARA CREAR TABLA
def p_instruccion_crear_TB_columnas(t) :
    '''crear_tb_columnas    : crear_tb_columnas COMA ID tipo_valor parametro_columna
                            | crear_tb_columnas COMA ID tipo_valor
                            | crear_tb_columnas COMA PRIMARY KEY PARIZQ pkey_id PARDER
                            | crear_tb_columnas COMA FOREIGN KEY PARIZQ pkey_id PARDER REFERNECES ID PARIZQ pkey_id PARDER
                            | ID tipo_valor parametro_columna
                            | ID tipo_valor
                            | PRIMARY KEY PARIZQ pkey_id PARDER
                            | FOREIGN KEY PARIZQ pkey_id PARDER REFERNECES ID PARIZQ pkey_id PARDER
    '''
    print('Cosas')    
    

#========================================================

# INSTRUCCION CON "DELETE"
def p_instruccion_delete(t) :
    '''deletes      : ID PTCOMA WHERE delete_condicional
                    | delete_incondicional'''
    print("ELIMINACION")

def p_instruccion_delete_incondicional(t) :
    'delete_incondicional     : ID PTCOMA'
    t[0] = Delete_incondicional(t[1])

def p_instruccion_delete_condicional(t) :
    'delete_condicional     : ID WHERE PTCOMA'
    # t[0] = Delete_incondicional(t[1])
    print("Eliminar tabla: " + t[1])

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    return parser.parse(input)
