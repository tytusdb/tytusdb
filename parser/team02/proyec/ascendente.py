import ply.yacc as yacc
from ast.Declarevar import Declarevar
from Reportes.Datos import Datos
import Reportes.Errores as Reporte
from Valor.Asignacion import Asignacion
from ast.Label import Label
from Valor.Operar import Operar
from Valor.Operar import TIPO
from Valor.Valor import Valor
from ast.Insercion import Insercion
from ast.Select import Select



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
    'add'       : 'ADD',
    'table'	    : 'TABLE',
	'database'	: 'DATABASE',
	'unique'	: 'UNIQUE',    
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
    'check'    	: 'CHECK',
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
    'decimal'   : 'DECIMAL2',
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
    'exist'     : 'EXIST2',
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
    'md5'	: 'MD5',
    'now'	: 'NOW',
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
    'CADENA2',
    'DECIMAL',
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
t_COMA      = r','
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

t_APOST     = r'\''



def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Entero demasiado largo %d", t.value)
        t.value = 0
    return t


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
    p = Datos("LEXICO","Error lexico, simbolo "+t.value[0]+" no  valido ",t.lexer.lineno,find_column(t))
    Reporte.agregar(p)
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
    '''instrucciones      : instruccion                       
                        '''
    t[0] = [t[1]]


def p_instruccion(t) :
    '''instruccion      : creartable PUNTOCOMA 
                       | createbase PUNTOCOMA
                       | expresion2
                       | ddm PUNTOCOMA
                       | selecttable PUNTOCOMA
                       | error                         
                        '''
    t[0] = t[1]

def p_instruccion2(t) :
    '''instruccion4      : creartable INHERITS PARENIN ID PARENOUT PUNTOCOMA
                        | createbase PUNTOCOMA
                        | createbase2 PUNTOCOMA
                        | DROP TABLE ID PUNTOCOMA
                        | altertable
                        | ddm PUNTOCOMA
                        | error '''
    t[0] = t[1]


def p_createbase(t) :
    '''createbase      :    CREATE DATABASE ID
    | CREATE error DATABASE ID
    | CREATE  DATABASE error ID
                            '''
    t[0] = Declarevar(t[3],"",t.slice[1].lineno,find_column(t.slice[1]),t[2])


def p_createbase2(t) :
    '''createbase2      :    CREATE DATABASE IF NOT2 EXIST2 ID
    |  CREATE error DATABASE IF NOT2 EXIST2 ID
    |  CREATE  DATABASE error IF NOT2 EXIST2 ID
    |  CREATE  DATABASE  IF error NOT2 EXIST2 ID                              '''
    t[0] = Declarevar(t[6],"",t.slice[1].lineno,find_column(t.slice[1]),t[2])


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
    '''ddm     :  insertstatement
                        | UPDATE ID SET ID IGUAL valor wherecondicion
                        | UPDATE ID SET ID IGUAL valor
                        | DELETE FROM ID wherecondicion
'''
    t[0] = t[1]

def p_insertstatement(t) :
        'insertstatement   : INSERT INTO ID VALUES PARENIN valores PARENOUT'
        t[0] = Insercion(t[3],t[6],t.slice[1].lineno,find_column(t.slice[1]),t[1])


def p_valores(t) :
    'valores    : valores COMA valor '
    t[1].append(t[3])
    t[0] = t[1]

def p_valores2(t) :
    '''valores      : valor                       
                        '''
    t[0] = [t[1]]


def p_whrecondicion(t) :
        '''wherecondicion   : WHERE  condition
                      |      WHERE  condition AND2 condition
                      
                      '''
        t[0] = t[1]

def p_whrecondicion2(t) :
    'wherecondicion   :  '
    t[0] = []

def p_creartable(t) :
    'creartable     : CREATE TABLE ID PARENIN params PARENOUT '   
    t[0] = Label(t[3],t[5],t.slice[1].lineno,find_column(t.slice[1]),t[2])
def p_creartable9(t) :
    'creartable     : CREATE TABLE ID PARENIN PARENOUT '   
    t[0] = Asignhacion(t[3],"",t.slice[1].lineno,find_column(t.slice[1]),t[2])


def p_selecttable(t) :
    '''selecttable     : SELECT selectclausules FROM  selectbody wherecondicion
                      | SELECT selectclausules FROM selectbody wherecondicion GROUP BY valores
                      | SELECT selectclausules FROM selectbody wherecondicion GROUP BY valores HAVING funciones
                     '''
    t[0] = Select(t[2],t[4],t.slice[1].lineno,find_column(t.slice[1]),t[5])


def p_selectbody(t) :
    '''selectbody     : ID                      
                     '''
    clase = Select("","","","","")  
    clase.type =  "ID"            
    clase.value =  t[1]     
    t[0] = clase
 
def p_selectbody2(t) :
    '''selectbody     :  PARENIN selecttable  PARENOUT
                        | ID ID
                     '''
    t[0] = t[1]
 

def p_selectclausules2(t) :
    'selectclausules     : POR'
    clase = Select("","","","","")             
    clase.type = '*'     
    t[0] = clase
   

def p_selectclausules(t) :
    '''selectclausules     : valores                     
                     '''        
    clase = Select("","","","","")             
    clase.type = 'valores' 
    clase.value =   t[1]
    t[0] = clase
   

def p_selectclausules4(t) :
    '''selectclausules     :  DISTINCT  valores
                      | SUBSTRING PARENIN valor COMA valor COMA  valor PARENOUT

                     '''
        
    t[0] = t[1]


def p_funciones(t) :
    '''funciones     : SUM PARENIN ID PARENOUT  signos valor
                    '''

def p_params_lista(t) :
    '''params    :  params COMA valores_inside 
                 | params error valores_inside  '''
    t[1].append(t[3])
    t[0] = t[1]

def p_params(t) :
    'params     : valores_inside '
    t[0] =  [t[1]]


def p_valores_inside(t) :
    '''valores_inside     : expresion
                | expresion2 '''
    t[0] = t[1]



def p_expresion(t):
    'expresion     : ID TIPODATO compl'    
    t[0] = Declarevar(t[1],"",t.slice[1].lineno,find_column(t.slice[1]),t[2])
def p_expresion2(t):
    'expresion2     : ID TIPODATO DEFAULT expresion_num compl'    
    t[0] = Asignacion(t[1],t[4],t.slice[1].lineno,find_column(t.slice[1]),t[2])
def p_compl(t):
     '''compl : NOT2 NULL
             | UNIQUE NOT2 NULL
             | UNIQUE 
             | NOT2 NULL PRIMARY KEY 
             | PRIMARY KEY 
               
             '''               
     t[0] = t[1]

def p_compl2(t) :
    'compl   :  '
    t[0] = []
  
def p_expresion_num(t):
        '''expresion_num : valor
                     | operacion_binar
                    '''
        t[0] = t[1]        


def p_expresionp(t):
    'expresion     : PRIMARY KEY PARENIN ID PARENOUT'
    t[0] = t[1]
def p_expresionf(t):
    'expresion     : FOREIGN KEY PARENIN ID PARENOUT REFERENCES ID PARENIN ID PARENOUT'
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

def p_operacion_binar(t):
    '''operacion_binar   :      valor MAS valor
                            |   valor MENOS valor
                            |   valor POR valor
                            |   valor DIV valor
                            |   valor PORC valor'''

    clase = Operar()
    if(t.slice[2].type == 'MAS'):
        clase.Node(t[1],t[3],TIPO.SUM,t.slice[2].lineno,1)       
    elif(t.slice[2].type == 'MENOS'):
        clase.Node(t[1],t[3],TIPO.REST,t.slice[2].lineno,1)       
    elif(t.slice[2].type == 'POR'):
        clase.Node(t[1],t[3],TIPO.MULT,t.slice[2].lineno,1)
        
    elif(t.slice[2].type == 'DIV'):
        clase.Node(t[1],t[3],TIPO.DIV,t.slice[2].lineno,1)
       
    elif(t.slice[2].type == 'PORC'):
        clase.Node(t[1],t[3],TIPO.PORC,t.slice[2].lineno,1)
       
    t[0] = clase

def p_valorz(t):
    '''valor :     ENTERO
                 | DECIMAL
                 | APOST FECHA APOST
                 | CADENA
                 | CADENA2
                 | MD5 PARENIN CADENA  PARENOUT
                 | NOW PARENIN PARENOUT
                 | ID
                 | ID PUNTO ID                 
                 | PARENIN selecttable  PARENOUT
            '''
    l= Operar() 

    if(t.slice[1].type == 'CADENA' or t.slice[1].type == 'CADENA2'):
        l.Value_normal(Valor(str(t[1]),t.slice[1].lineno,find_column(t.slice[1])))
    elif(t.slice[1].type == 'DECIMAL'):
        l.Value_normal(Valor(float(t[1]),t.slice[1].lineno,find_column(t.slice[1])))
    elif(t.slice[1].type == 'ENTERO'):
        l.Value_normal(Valor(int(t[1]),t.slice[1].lineno,find_column(t.slice[1])))
    t[0] = l
  
    
def p_TIPODATO(t):
    ''' TIPODATO : TEXT
                  | SMALLINT
                  | VARCHAR PARENIN ENTERO  PARENOUT                  
                  | INTEGER
                  | INT
                  | BIGINT
                  | DECIMAL2
                  | NUMERIC
                  | REAL
                  | DOUBLE
                  | CHARACTER
                  | CHAR  PARENIN ENTERO PARENOUT
                  | TIMESTAMP
                  | DATETIME
                  | FLOAT
                  | DATE
                  | MONEY
                  '''
    t[0] = t[1]

def p_error(t):
    try:
         print("Error sintactico, no se espera el valor "+t.value,t.lineno,find_column(t))
         p = Datos("SINTACTICO","Error sintactico, no se espera el valor "+t.value,t.lineno,find_column(t))
         Reporte.agregar(p)
    except:
        print("Error sintactico irrecuperable",1,1)
        p = Datos("SINTACTICO","Error sintactico irrecuperable",1,1)
        Reporte.agregar(p)

parser = yacc.yacc()

def parse(input) :
    global lexer
    input = input.replace("\r","")
    print("el input es ",input)

    lexer = lex.lex()
    return parser.parse(input)
