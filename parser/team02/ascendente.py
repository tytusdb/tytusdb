import ply.yacc as yacc


reservadas = {
    'select'	: 'SELECT',
    'from'      :  'FROM',
    'insert'	: 'INSERT',
    'values'    : 'VALUES',
    'delete'	: 'DELETE',
    'update'    : 'UPDATE',
    'inner'     : 'INNER',
    'join'      : 'JOIN',
    'is'        : 'IS',
    'create'    : 'CREATE',
    'table'	    : 'TABLE',
	'database'	: 'DATABASE',
    'databases'	: 'DATABASES',
    'inherits'	: 'INHERITS',
    'drop'      : 'DROP',
    'foreign'   : 'FOREIGN',
    'create'    : 'CREATE',
    'group'     : 'GROUP',
    'alter'	    : 'ALTER',
    'substring'	: 'SUBSTRING',
    'rename'	: 'RENAME',
    'sum'    	: 'SUM',
    'column'	: 'COLUMN',
    'to'    	: 'TO',
	'where'   	: 'WHERE',
    'having'    : 'HAVING',
    'order'     : 'ORDER',
    'by'	    : 'BY',
    'primary'	: 'PRIMARY',
    'key'    	: 'KEY',
    'distinct'	: 'DISTINCT',
    'smallint'	: 'SMALLINT',
    'integer'   : 'INTEGER',
    'int'       : 'INT',
    'bigint'    : 'BIGINT',
    'decimal'   : 'DECIMAL',
    'numeric'	: 'NUMERIC',
    'real'  	: 'REAL',
    'double'	: 'DOUBLE',
    'precision' : 'PRECISION',
    'money' 	: 'MONEY',
    'character'	: 'CHARACTER',
    'varying'	: 'VARYING',
    'varchar'	: 'VARCHAR',
    'char'  	: 'CHAR',
    'text'  	: 'TEXT',
    'type'  	: 'TYPE',
    'or'     	: 'OR2',
    'replace'   : 'REPLACE',
    'exists'    : 'EXISTS',
    'if'        : 'IF',
    'owner'     : 'OWNER',
    'mode'      : 'MODE',
    'default'   : 'DEFAULT',
    'show'      : 'SHOW',

    'timestamp' : 'TIMESTAMP',
    'without'  	: 'WITHOUT',
    'time'  	: 'TIME',
    'zone'  	: 'ZONE',
    'with'  	: 'WITH',
    'interval'  : 'INTERVAL',
    'datetime'	: 'DATETIME',
    'float' 	: 'FLOAT',
    'date'	    : 'DATE',
    'date_part'	: 'DATE_PART',
    'current_date'	: 'CURRENT_DATE',
    'current_time'	: 'CURRENT_TIME',
    'references'	: 'REFERENCES',

    'year'  	: 'YEAR',
    'month'     : 'MONTH',
    'day'   	: 'DAY',
    'hour'  	: 'HOUR',
    'minute'	: 'MINUTE',
    'second'	: 'SECOND',


    'extract'  	: 'EXTRACT',
    'month'     : 'MONTH',
    'day'   	: 'DAY',
    'hour'  	: 'HOUR',
    'minute'	: 'MINUTE',
    'second'	: 'SECOND',
    'between'   : 'BETWEEN',
    'in'    	: 'IN',
    'like'  	: 'LIKE',
    'ilike'	    : 'ILIKE',
    'similar'	: 'SIMILAR',
    'and'   	: 'AND2',
    'into'	    : 'INTO',
    'using'	    : 'USING',
    'not'   	: 'NOT2',
    'null'  	: 'NULL',
    'as'	    : 'AS',
    'constraint': 'CONSTRAINT',
    'set'	    : 'SET',
    'now'	    : 'NOW',

}

tokens  = [
    'PUNTOCOMA',
    'DOSPUNTOS',
    'ENTERO',
    'CADENA',
    'ID',
    'FECHA',
    'HORA',
    'PARENIN',
    'PARENOUT',
    'CORCHIN',
    'CORCHOUT',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'PORC',
    'PUNTO',
    'IGUAL',
    'NOIGUAL',
    'MAYOROIGUAL',
    'MENOROIGUAL',
    'MENOR',
    'MAYOR',
    'IGUALIGUAL',
    'OR',
    'BAR',
    'AND',
    'AMPER',
    'NOT',
    'EXP',
    'COMA',
    'APOST'
] + list(reservadas.values())

# Tokens
t_PUNTOCOMA   = r';'
t_DOSPUNTOS	  = r':'
t_PARENIN     = r'\('
t_PARENOUT    = r'\)'
t_CORCHIN     = r'\['
t_CORCHOUT    = r'\]'
t_MAS         = r'\+'
t_MENOS        = r'-'
t_POR        = r'\*'
t_DIV         = r'/'
t_PORC        = r'%'
t_PUNTO       = r'.'
t_IGUAL     = r'='
t_NOIGUAL = r'!='
t_MAYOROIGUAL    = r'>='
t_MENOROIGUAL    = r'<='
t_MENOR    = r'<'
t_MAYOR    = r'>'
t_IGUALIGUAL = r'=='
t_OR        = r'\|\|'
t_BAR       = r'\|'
t_AND       = r'&&'
t_AMPER       = r'&'
t_NOT       = r'!'
t_EXP       = r'\^'
t_COMA      = r','
t_APOST     = r'\''



def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float DEMASIADO LARGO %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # CHECK FOR RESERVED WORDS
     return t

def t_FECHA(t):
     r'[0-9][-0-9]*'
     t.type = reservadas.get(t.value.lower(),'FECHA')    # CHECK FOR RESERVED WORDS
     return t

def t_HORA(t):
     r'[0-9][:0-9]*'
     t.type = reservadas.get(t.value.lower(),'HORA')    # CHECK FOR RESERVED WORDS
     return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Entero demasiado largo %d", t.value)
        t.value = 0
    return t






def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1] #quitar las comillas
    return t

def t_CADENA2(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t
# ignorar Caracteres
t_ignore = " \t\r"

# Comentario simple
def t_COMENTARIO(t):
    r'//.*\n'
    t.lexer.lineno += 1

def t_COMENTARIOS(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


def t_error(t):
    print("Error lexico, simbolo "+t.value[0]+" no  valido. en la linea: "+t.lexer.lineno+" y columna: "+find_column(t))
    t.lexer.skip(1)


def t_newline(t):
     r'\n+'
     t.lexer.lineno += t.value.count("\n")



# obtener la columna
def find_column(token):
    line_start = texto.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


precedence = (
    ('left','OR','EXP'),
    ('left','AND'),
    ('nonassoc','MENOR','MAYOR','MENOROIGUAL','MAYOROIGUAL','IGUALIGUAL','NOIGUAL'),
    ('left','MAS','MENOS'),
    ('left','POR','DIV','PORC'),
    ('right','NOT'),
    )


texto = ""

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]
    print("arbol terminado")

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion '
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]


def p_instruccion(t) :
    '''instruccion      : creartable PUNTOCOMA
                        | creartable INHERITS PARENIN ID PARENOUT PUNTOCOMA
                        | CREATE DATABASE ID PUNTOCOMA
                        | selecttable PUNTOCOMA
                        | DROP TABLE ID PUNTOCOMA
                        | altertable
                        | ddm PUNTOCOMA
                        | error '''
    t[0] = t[1]
def p_altertable(t) :
    '''altertable     :  ALTER TABLE ID
                        | ALTER COLUMN ID TYPE TIPODATO
                        | ALTER TABLE ID ADD COLUMN ID TIPODATO
                        | ALTER TABLE ID ADD CHECK  PARENIN condition PARENOUT
                        | ALTER TABLE ID DROP COLUMN ID
                        | ALTER TABLE ID DROP CONSTRAINT ID
                        | ALTER TABLE ID ALTER COLUMN ID SET NOT2 NULL '''
    t[0] = t[1]


def p_ddm(t) :
    '''ddm     :  INSERT INTO ID VALUES PARENIN valores PARENOUT
                        | UPDATE ID SET ID IGUAL valor wherecondicion
                        | UPDATE ID SET ID IGUAL valor
                        | DELETE FROM ID wherecondicion
'''
    t[0] = t[1]



def p_whrecondicion(t) :
        '''wherecondicion   :WHERE  condition
                      |      WHERE  condition AND2 condition
                      '''



    t[0] = t[1]


def p_creartable(t) :
    'creartable     : CREATE TABLE ID PARENIN params PARENOUT '
    t[0] = t[1]

def p_selecttable(t) :
    '''selecttable     :SELECT selectclausules FROM  selectbody
                      | SELECT selectclausules FROM selectbody wherecondicion
                      | SELECT selectclausules FROM selectbody wherecondicion GROUP BY valores
                      | SELECT selectclausules FROM selectbody wherecondicion GROUP BY valores HAVING funciones
                     '''
    t[0] = t[1]

def p_selectbody(t) :
    '''selectbody     :ID
                      | PARENIN selecttable  PARENOUT
                      | ID ID
                     '''
    t[0] = t[1]

def p_selectclausules(t) :
    '''selectclausules     :POR
                      | valores
                      | DISTINCT  valores
                      | SUBSTRING PARENIN valor COMA valor COMA  valor PARENOUT

                     '''
    t[0] = t[1]


def p_funciones(t) :
    '''funciones     :SUM PARENIN ID PARENOUT  signos valor
                    '''
    t[0] = t[1]

def p_params(t) :
    '''params     : params COMA expresion
                | expresion '''
    t[0] = t[1]

def p_valores(t) :
    '''valores     : valores COMA valor
                | valor '''
    t[0] = t[1]

def p_expresion(t):
    '''expresion     : ID TIPODATO
                |      PRIMARY KEY PARENIN ID PARENOUT
                |      FOREIGN KEY PARENIN ID PARENOUT REFERENCES ID PARENIN ID PARENOUT'''

    t[0] = t[1]


def p_condition(t) :
    '''condition :      valor signos valor
                    |   valor BETWEEN valor AND2 valor
                    |  SUBSTRING PARENIN valor COMA valor COMA  valor PARENOUT signos  valor

                            '''
    t[0] = t[1]


def p_signos(t) :
    '''signos :                  MENOR
                            |    MAYOR
                            |    MENOROIGUAL
                            |    MAYOROIGUAL
                            |    IGUALIGUAL
                            |    IGUAL
                            |    NOT2 IN
                            |    IN
                            |    NOIGUAL
                            |    IS NOT2 DISTINCT FROM
                            |    IS  DISTINCT FROM
                             '''
    t[0] = t[1]


def p_valor(t):
    '''valor :     ENTERO
                 | DECIMAL
                 | APOST FECHA APOST
                 | CADENA
                 | CADENA2
                 | ID
                 | ID PUNTO ID
                 | PARENIN selecttable  PARENOUT
            '''
    t[0] = t[1]

def p_TIPODATO(t):
    ''' TIPODATO : TEXT
                  | SMALLINT
                  | INTEGER
                  | INT
                  | BIGINT
                  | DECIMAL
                  | NUMERIC
                  | REAL
                  | DOUBLE
                  | MONEY
                  | CHARACTER
                  | CHAR  PARENIN ENTERO PARENOUT
                  | TEXT
                  | TIMESTAMP
                  | DATETIME
                  | FLOAT
                  | DATE
                  | MONEY
                  | VARCHAR PARENIN ENTERO PARENOUT'''
    t[0] = t[1]

def p_error(t):
    try:
         print("Error sintactico, no se espera el valor "+t.value,t.lineno,find_column(t))

    except:
        print("Error sintactico irrecuperable",1,1)


parser = yacc.yacc()

def parse(input) :
    global lexer
    input = input.replace("\r","")
    print("el input es ",input)

    lexer = lex.lex()
    return parser.parse(input)
