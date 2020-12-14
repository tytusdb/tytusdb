from Interprete.OperacionesConExpresiones.Opera_Relacionales import Opera_Relacionales
from Interprete.Condicionantes.Condicion import Condicion
from Interprete.SELECT.select import select
from Interprete.Arbol import Arbol

from Parser.Reportes.Nodo import Nodo

reservadas = {

	# Boolean Type
	'boolean': 'BOOLEAN',
	'true': 'TRUE',
	'false': 'FALSE',
	'order': 'ORDER',

	'into': 'INTO',

	# operator Precedence
	'isnull': 'ISNULL',
	'notnull': 'NOTNULL',

	# Definition
	'replace': 'REPLACE',
	'owner': 'OWNER',
	'show': 'SHOW',
	'databases': 'DATABASES',
	'MAP' : 'MAP',
	'LIST' : 'LIST',

	# Inheritance
	'inherits': 'INHERITS',

	# ESTRUCTURAS DE CONSULTA Y DEFINICIONES
	'select'  : 'SELECT',
	'insert'  : 'INSERT',
	'update'  : 'UPDATE',
	'drop'  : 'DROP',
	'delete'  : 'DELETE',
	'alter'  : 'ALTER',
	'constraint'  : 'CONSTRAINT',
	'from' : 'FROM',
	'group' : 'GROUP',
	'by'  : 'BY',
	'where'  : 'WHERE',
	'having'   : 'HAVING',
	'create' : 'CREATE',
	'type' : 'TYPE',
	'primary' : 'PRIMARY',
	'foreign' : 'FOREIGN',
	'add' : 'ADD',
	'rename' : 'RENAME',
	'set' : 'SET',
	'key' : 'KEY',
	'if' : 'IF',
	'unique' : 'UNIQUE',
	'references' : 'REFERENCES',
	'check' : 'CHECK',
	'column' : 'COLUMN',
	'database' : 'DATABASE',
	'table' : 'TABLE',
	'text' : 'TEXT',
	'float' : 'FLOAT',
	'values' : 'VALUES',
	'int' : 'INT',
	'default' : 'DEFAULT',
	'null' : 'NULL',

	# TIPOS NUMERICOS
	'smallint' : 'SMALLINT',
	'integer' : 'INTEGER',
	'bigint' : 'BIGINT',
	'decimal' : 'DECIMAL',
	'numeric' : 'NUMERIC',
	'real' : 'REAL',
	'double' : 'DOUBLE',
	'precision' : 'PRECISION',
	'money' : 'MONEY',
	'varying' : 'VARYING',
	'varchar' : 'VARCHAR',
	'character' : 'CHARACTER',
	'char' : 'CHAR',
	'clear' : 'CLEAR',

	# TIPOS EN FECHAS
	'timestamp' : 'TIMESTAMP',
	'date' : 'DATE',
	'time' : 'TIME',
	'interval' : 'INTERVAL',
	'year' : 'YEAR',
	'day' : 'DAY',
	'hour' : 'HOUR',
	'minute' : 'MINUTE',
	'second' : 'SECOND',
	'to' : 'TO',


	# ENUM
	'enum'  : 'ENUM',

	# OPERADORES LOGICOS
	'and' : 'AND',
	'or'  : 'OR',
	'not'   : 'NOT',

	# PREDICADOS DE COMPARACION
	'between'   : 'BETWEEN',
	'unknown' : 'UNKNOWN',
	'is'    : 'IS',
	'distinct'  : 'DISTINCT',

	# FUNCIONES MATEMATICAS
	'abs' : 'ABS',
	'cbrt' : 'CBRT',
	'ceil' : 'CEIL',
	'ceiling' : 'CEILING',
	'degrees' : 'DEGREES',
	'div' : 'DIV',
	'exp' : 'EXP',
	'factorial' : 'FACTORIAL',
	'floor' : 'FLOOR',
	'gcd' : 'GCD',
	'lcm' : 'LCM',
	'ln' : 'LN',
	'log' : 'LOG',
	'log10' : 'LOG10',
	'min_scale' : 'MIN_SCALE',
	'mod' : 'MOD',
	'pi' : 'PI',
	'power' : 'POWER',
	'radians' : 'RADIANS',
	'round' : 'ROUND',
	'scale' : 'SCALE',
	'sign' : 'SIGN',
	'sqrt' : 'SQRT',
	'trim_scale' : 'TRIM_SCALE',
	'truc' : 'TRUC',
	'width_bucker' : 'WIDTH_BUCKET',
	'random' : 'RANDOM',
	'setseed' : 'SETSEED',
	'contains' : 'CONTAINS',
	'remove': 'REMOVE',

	# FUNCIONES DE AGREGACION
	'count' : 'COUNT',
	'sum' : 'SUM',
	'avg' : 'AVG',
	'max' : 'MAX',
	'min' : 'MIN',

	# FUNCIONES TRIGONOMETRICAS
	'acos' : 'ACOS',
	'acosd' : 'ACOSD',
	'asin' : 'ASIN',
	'asind' : 'ASIND',
	'atan' : 'ATAN',
	'atand' : 'ATAND',
	'atan2' : 'ATAN2',
	'atan2d' : 'ATAN2D',
	'cos' : 'COS',
	'cosd' : 'COSD',
	'cot' : 'COT',
	'cotd' : 'COTD',
	'sin' : 'SIN',
	'sind' : 'SIND',
	'tan' : 'TAN',
	'tand' : 'TAND',
	'sinh' : 'SINH',
	'cosh' : 'COSH',
	'tanh' : 'TANH',
	'asinh' : 'ASINH',
	'acosh   ' : 'ACOSH',
	'atanh' : 'ATANH',
	'SIZE' : 'SIZE',

	# FUNCIONES DE CADENA BINARIAS
	'length' : 'LENGTH',
	'substring' : 'SUBSTRING',
	'trim' : 'TRIM',
	'get_byte' : 'GET_BYTE',
	'md5' : 'MD5',
	'set_byte' : 'SET_BYTE',
	'sha256' : 'SHA256',
	'substr' : 'SUBSTR',
	'convert' : 'CONVERT',
	'encode' : 'ENCODE',
	'decode' : 'DECODE',

	# COINCidenCIA POR PATRON
	'like' : 'LIKE',
	'ilike' : 'ILIKE',
	'similar' : 'SIMILAR',
	'as' : 'AS',
	'couter' : 'COUTER',

	# SUBQUERYS
	'in' : 'IN',
	'exists' : 'EXISTS',
	'any' : 'ANY',
	'all' : 'ALL',
	'some' : 'SOME',

	# JOINS
	'join' : 'JOIN',
	'inner' : 'INNER',
	'left' : 'LEFT',
	'right' : 'RIGHT',
	'full' : 'FULL',
	'outer' : 'OUTER',
	'on' : 'ON',

	# ORDENAMIENTO DE FILAS
	'asc' : 'ASC',
	'desc' : 'DESC',
	'nulls' : 'NULLS',
	'first' : 'FIRST',
	'last' : 'LAST',

	# EXPRESIONES
	'case' : 'CASE',
	'when' : 'WHEN',
	'then' : 'THEN',
	'end' : 'END',
	'greatest' : 'GREATEST',
	'least' : 'LEAST',

	# LIMITE Y OFFSET
	'limit' : 'LIMIT',
	'offset' : 'OFFSET',

	# CONSULTAS DE COMBINACION
	'union' : 'UNION',
	'intersect' : 'INTERSECT',
	'except' : 'EXCEPT'

}

tokens  = [
	'PT',
	'DOBPTS',
	'MAS',
	'MENOS',
	'MULTI',
	'DIVISION',
	'MODULO',
	'IGUAL',
	'PARIZQ',
	'PARDER',
	'PTCOMA',
	'COMA',
	'TKNOT',
	'NOTBB',
	'ANDBB',
	'ORBB',
	'NUMERAL',
	'TKEXP',
	'SHIFTIZQ',
	'SHIFTDER',
	'IGUALQUE',
	'DISTINTO',
	'MAYORIG',
	'MENORIG',
	'MAYORQUE',
	'MENORQUE',
	'CORIZQ',
	'CORDER',
	'DOSPTS',
	'TKDECIMAL',
	'ENTERO',
	'CADENA',
	'CADENADOBLE',
	'ID'
] + list(reservadas.values())

# Tokens
t_PT        = r'\.'
t_DOBPTS    = r'::'
t_CORIZQ      = r'\['
t_CORDER      = r']'

t_MAS       = r'\+'
t_MENOS     = r'-'
t_TKEXP     = r'\^'
t_MULTI     = r'\*'
t_DIVISION  = r'/'
t_MODULO   = r'%'
t_IGUAL     = r'='
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_PTCOMA    = r';'
t_COMA      = r','
t_TKNOT       = r'!'
t_NOTBB     = r'~'
t_ANDBB     = r'&'
t_ORBB      = r'\|'

t_NUMERAL   = r'\#'

t_SHIFTIZQ  = r'<<'
t_SHIFTDER  = r'>>'
t_IGUALQUE  = r'=='
t_DISTINTO  = r'!='
t_MAYORIG   = r'>='
t_MENORIG   = r'<='
t_MAYORQUE  = r'>'
t_MENORQUE  = r'<'
t_DOSPTS    = r':'

def t_ENTERO(t):
	r'\d+'
	try:
		t.value = int(t.value)
	except ValueError:
		print("Integer value too large %d", t.value)
		t.value = 0
	return t

def t_TKDECIMAL(t):
	r'\d+\.\d+'
	try:
		t.value = float(t.value)
	except ValueError:
		print("Float value too large %d", t.value)
		t.value = 0
	return t


def t_CADENA(t):
	r'\'.*?\''
	t.value = t.value[1:-1]
	return t

def t_CADENADOBLE(t):
	r'\".*?\"'
	t.value = t.value[1:-1]
	return t

def t_ID(t):
	 r'[a-zA-Z_][a-zA-Z_0-9]*'
	 t.type = reservadas.get(t.value.lower(),'ID')
	 return t

t_ignore = " \t"

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value) # t.value.count("\n")

def t_COMENTARIO_SIMPLE(t):
	r'\--.*\n'
	t.lexer.lineno += 1

def t_COMENTARIO_MULTILINEA(t):
	r'/\*(.|\n)*?\*/'
	t.lexer.lineno += t.value.count('\n')

def t_error(t):
	print("Caracter NO Valido: '%s'" % t.value[0])
	t.lexer.skip(1)
	print(t.value[0])


# -----------------------------------------------------------------------------------
# ---------------------- SINTACTICO -------------------------------------------------
# -----------------------------------------------------------------------------------


#-----------------------
import ply.lex as lex
lexer2 = lex.lex()
#-----------------------
precedence = (
	#('left','CONCAT'),
	#('left','MENOR','MAYOR','IGUAL','MENORIGUAL','MAYORIGUAL','DIFERENTE'),
	('left','MENORQUE','MAYORQUE','IGUAL','MENORIG','MAYORIG','DISTINTO'),
	('left','MAS','MENOS'),
	('left','MULTI','DIVISION','MODULO'),
	('left','TKEXP'),
	#('right','UMENOS'),
)


def p_init(t):
	'init : sentences'
	t[0] = Nodo("init", "")
	t[0].add(t[1])

def p_sentences(t):
	'''
		sentences   : sentences setInstruccions
					| setInstruccions
	'''
	if len(t) == 3:  # listawhere atributoselect
		t[1].add(t[2])
		t[0] = t[1]
	else:  # atributoselect
		t[0] = Nodo("sentences", "")
		t[0].add(t[1])

def p_setInstruccions(t):
	'''
		setInstruccions   : sentence PTCOMA
	'''
	t[0] = Nodo("setInstruccions", "")
	t[0].add(t[1])

def p_sentence(t):
	'''
		sentence     : ddl
	'''
	t[0] = Nodo("sentence", "")
	t[0].add(t[1])

def p_ddl(t):
	'''
		ddl  : select
			 | table_create
			 | insert
			 | update
			 | deletetable
	'''
	t[0] = Nodo("ddl", "")
	t[0].add(t[1])

def p_select(t):
	'''
		select  : SELECT listavalores FROM exp listawhere
	'''
	t[0] = Nodo("select", "")
	t[1].add(Nodo(t[1], ''))
	t[0].add(t[2])
	t[1].add(Nodo(t[3], ''))
	t[0].add(t[4])
	t[0].add(t[5])

def p_listawhere(t):
	'''
		listawhere  : listawhere atributoselect
					| atributoselect
	'''
	if len(t) == 3:  # listawhere atributoselect
		t[1].add(t[2])
		t[0] = t[1]
	else:  # atributoselect
		t[0] = Nodo("listawhere", "")
		t[0].add(t[1])


def p_atributoselect(t):
	'''
		atributoselect  : WHERE exp
						| ORDER BY exp ordenamiento
						| GROUP BY exp
						| LIMIT exp
	'''
	t[0] = Nodo("atributoselect", "")
	if t[1].lower() == "where":
		t[1].add(Nodo(t[1], ''))
		t[1].add(t[2])
	elif t[1].lower() == "order":
		t[1].add(Nodo(t[1]+' '+t[2], ''))
		t[1].add(t[3])
		t[1].add(t[4])
	elif t[1].lower() == "group":
		t[1].add(Nodo(t[1] + ' ' + t[2], ''))
		t[1].add(t[3])
	elif t[1].lower() == "limit":
		t[1].add(Nodo(t[1], ''))
		t[1].add(t[2])


def p_ordenamiento(t):
	'''
		ordenamiento   : ASC
					   | DESC
	'''
	t[0] = Nodo("ordenamiento", "")
	t[1].add(Nodo(t[1], ''))

def p_listavalores(t):
	'''
		listavalores   : listavalores COMA exp
					   | exp
	'''
	if len(t) == 4: #listavalores COMA exp
		t[1].add(t[3])
		t[0] = t[1]
	else: # exp
		t[0] = Nodo("listavalores", "")
		t[0].add(t[1])

def p_exp(t):
	'''
		exp   : MAS exp
			  | MENOS exp
			  | exp TKEXP 	exp
			  | exp MULTI 	exp
			  | exp DIVISION exp
			  | exp MODULO exp
			  | exp MAS exp
			  | exp MENOS exp
			  | exp BETWEEN exp
			  | exp IN exp
			  | exp LIKE exp
			  | exp ILIKE exp
			  | exp SIMILAR exp
			  | exp IGUAL exp
			  | exp MAYORQUE exp
			  | exp MENORQUE exp
			  | exp MAYORIG exp
			  | exp MENORIG exp
			  | exp IS exp
			  | exp ISNULL exp
			  | exp NOTNULL exp
			  | NOT exp
			  | exp AND exp
			  | exp OR exp
	'''
	t[0] = Nodo("exp", "")
	if len(t) == 3:#LITERAL exp
		t[0].add(Nodo(t[1], ''))
		t[0].add(t[2])
	elif len(t) == 4:#exp LITERAL exp
		t[0].add(t[1])
		t[0].add(Nodo(t[2], ''))
		t[0].add(t[3])

def p_expSimples(t):
	'''
		exp         :   ID
					| ENTERO
					| TKDECIMAL
					| TRUE
					| FALSE
					| CADENADOBLE
					| CADENA
	'''
	t[0] = Nodo("exp", "")
	t[0].add(Nodo(t[1], ''))


# ---------------CREATE TABLE---------------
def p_table_create(t):
	'''
		table_create : CREATE TABLE ID PARIZQ lista_table COMA listadolprimary PARDER
					 | CREATE TABLE ID PARIZQ lista_table PARDER
					 | CREATE TABLE IF NOT EXISTS ID PARIZQ lista_table COMA listadolprimary PARDER
					 | CREATE TABLE IF NOT EXISTS ID PARDER lista_table PARDER
	'''
	t[0] = Nodo("table_create", "")
	if len(t) == 9:
		#CREATE TABLE ID PARIZQ lista_table COMA listadolprimary PARDER
		t[1].add(Nodo(t[1]+' '+t[2]+' '+t[3],''))
		t[1].add(t[5])
		t[1].add(t[7])
	elif len(t) == 7:
		#CREATE TABLE ID PARIZQ lista_table PARDER
		t[1].add(Nodo(t[1]+' '+t[2]+' '+t[3],''))
		t[1].add(t[5])
	elif len(t) == 12:
		#CREATE TABLE IF NOT EXISTS ID PARIZQ lista_table COMA listadolprimary PARDER
		t[1].add(Nodo(t[1]+' '+t[2]+' '+t[3]+' '+t[4]+' '+t[5]+' '+t[6],''))
		t[1].add(t[8])
		t[1].add(t[10])
	elif len(t) == 10:
		#CREATE TABLE IF NOT EXISTS ID PARDER lista_table PARDER
		t[1].add(Nodo(t[1]+' '+t[2]+' '+t[3]+' '+t[4]+' '+t[5]+' '+t[6],''))
		t[1].add(t[8])

def p_lista_table(t):
	'''
		lista_table  : lista_table COMA atributo_table
					 | atributo_table
	'''
	if len(t) == 3: #lista_table COMA atributo_table
		t[1].add(t[3])
		t[0] = t[1]
	else: # atributo_table
		t[0] = Nodo("lista_table", "")
		t[0].add(t[1])

def p_listadolprimary(t):
	'''
		listadolprimary  : listadolprimary COMA lista_primary
						 | lista_primary
	'''
	if len(t) == 3: #listadolprimary COMA lista_primary
		t[1].add(t[3])
		t[0] = t[1]
	else: # lista_primary
		t[0] = Nodo("listadolprimary", "")
		t[0].add(t[1])

def p_lista_primary(t):
	'''
		lista_primary : PRIMARY KEY PARIZQ listaids PARDER
					  | FOREIGN KEY PARIZQ listaids PARDER REFERENCES ID PARIZQ listaids PARDER
					  | CONSTRAINT ID CHECK PARIZQ exp PARDER
					  | UNIQUE PARIZQ listaids PARDER
	'''
	t[0] = Nodo("lista_primary", "")
	if t[1].tolower() == 'primary':#PRIMARY KEY PARIZQ listaids PARDER
		t[0].add(Nodo(t[1]+''+t[2], ''))
		t[1].add(t[4])
	elif t[1].tolower() == 'foreign':#FOREIGN KEY PARIZQ listaids PARDER REFERENCES ID PARIZQ listaids PARDER
		t[0].add(Nodo(t[1]+''+t[2], ''))
		t[1].add(t[4])
		t[0].add(Nodo(t[6]+''+t[7], ''))
		t[1].add(t[9])
	elif t[1].tolower() == 'contraint': #CONSTRAINT ID CHECK PARIZQ exp PARDER
		t[0].add(Nodo(t[1], ''))
		t[0].add(Nodo(t[2], ''))
		t[0].add(Nodo(t[3], ''))
		t[1].add(t[5])
	elif t[1].tolower() == 'unique':#UNIQUE PARIZQ listaids PARDER
		t[0].add(Nodo(t[1], ''))
		t[1].add(t[3])

def p_atributo_table(t):
	'''
		atributo_table : ID  tipocql listaespecificaciones
					   | ID  tipocql
	'''
	t[0] = Nodo("atributo_table", "")
	if len(t)==3:#ID  tipocql
		t[0].add(Nodo(t[1], ''))
		t[1].add(t[2])
	else:#ID  tipocql listaespecificaciones
		t[0].add(Nodo(t[1], ''))
		t[1].add(t[2])
		t[1].add(t[3])

def p_listaespecificaciones(t):
	'''
		listaespecificaciones  : listaespecificaciones especificaciones
							   | especificaciones
	'''
	if len(t) == 3: #listaespecificaciones especificaciones
		t[1].add(t[2])
		t[0] = t[1]
	else: # especificaciones
		t[0] = Nodo("listaespecificaciones", "")
		t[0].add(t[1])

def p_especificaciones(t):
	'''
		especificaciones : UNIQUE
						 | NULL
						 | PRIMARY KEY
						 | NOT NULL
						 | REFERENCES ID
						 | CONSTRAINT ID
						 | DEFAULT exp
						 | CHECK PARIZQ exp PARDER
	'''
	t[0] = Nodo("especificaciones", "")

	if len(t)==3:
		if t[1].tolower()=='default':# DEFAULT exp
			t[0].add(Nodo(t[1], ''))
			t[0].add(t[2])
		else:  #| PRIMARY KEY | NOT NULL | REFERENCES ID | CONSTRAINT ID
			t[0].add(Nodo(t[1], ''))
			t[0].add(Nodo(t[2], ''))

	elif len(t) == 5:  #CHECK PARIZQ exp PARDER
		t[0].add(Nodo(t[1], ''))
		t[0].add(Nodo(t[2], ''))
		t[0].add(t[3])
		t[0].add(Nodo(t[4], ''))

	else: #UNIQUE | NULL | PRIMARY KEY | NOT NULL
		t[0].add(Nodo(t[1], ''))

def p_tipocql(t):
	'''
		tipocql : ID
				| tipo
	'''
	t[0] = Nodo("tipo", "")
	t[0].add(Nodo(t[1], ''))

def p_tipo(t):
	'''
		 tipo : SMALLINT
			  | INTEGER
			  | BIGINT
			  | DECIMAL
			  | NUMERIC
			  | REAL
			  | TIME
			  | MONEY
			  | TEXT
			  | DATE
			  | TIMESTAMP
			  | INTERVAL
			  | BOOLEAN
			  | DOUBLE 	  PRECISION
			  | VARCHAR   PARIZQ 		 exp PARDER
			  | CHARACTER PARIZQ 		 exp PARDER
			  | CHAR 	  PARIZQ 	     exp PARDER
			  | CHARACTER VARYING PARIZQ exp PARDER
	'''
	t[0] = Nodo("tipo", "")

	if len(t) ==2:
	#SMALLINT | INTEGER | BIGINT | DECIMAL |
	# NUMERIC | REAL | TIME | MONEY | TEXT | DATE | TIMESTAMP |
	# INTERVAL | BOOLEAN
		t[0].add(Nodo(t[1], ''))
	elif len(t) == 3:#DOUBLE 	  PRECISION
		t[0].add(Nodo(t[1], ''))
		t[0].add(Nodo(t[2], ''))
	elif len(t) ==5:# VARCHAR   PARIZQ exp PARDER | CHARACTER PARIZQ
		# exp PARDER | CHAR PARIZQ exp PARDER
		t[0].add(Nodo(t[1], ''))
		t[0].add(Nodo(t[2], ''))
		t[0].add(t[3])
		t[0].add(Nodo(t[4], ''))
	elif len(t) ==6:
		t[0].add(Nodo(t[1], ''))
		t[0].add(Nodo(t[2], ''))
		t[0].add(Nodo(t[3], ''))
		t[0].add(t[4])
		t[0].add(Nodo(t[5], ''))

# ---------------INSERT---------------
def p_insert(t):
	'''
		insert : INSERT INTO ID VALUES PARIZQ listavalores PARDER
			   | INSERT INTO ID PARIZQ listaids PARDER VALUES PARIZQ listavalores PARDER
	'''
	t[0] = Nodo("insert", "")
	if len(t) ==7: #INSERT INTO ID VALUES PARIZQ listavalores PARDER
		t[0].add(Nodo(t[1]+' '+t[2]+' '+t[3]+' '+t[4], ''))
		t[0].add(t[6])

	elif len(t) == 11: #INSERT INTO ID PARIZQ listaids PARDER VALUES PARIZQ listavalores PARDER
		t[0].add(Nodo(t[1]+' '+t[2]+' '+t[3], ''))
		t[0].add(t[5])
		t[0].add(Nodo(t[7], ''))
		t[0].add(t[9])

def p_listaids(t):
	'''
		listaids : listaids COMA ID
				 | ID
	'''
	if len(t) == 4: #listaids COMA ID
		t[1].add(Nodo(t[3],''))
		t[0] = t[1]
	else: # ID
		t[0] = Nodo("listaids", "")
		t[0].add(Nodo(t[1],''))

# ---------------UPDATE---------------
def p_update(t):
	'''
		update : UPDATE ID SET listaupdate WHERE exp
			   | UPDATE ID SET listaupdate
	'''
	t[0] = Nodo("update", "")

	if len(t)==7:#UPDATE ID SET listaupdate WHERE exp
		t[0].add(Nodo(t[1], ''))
		t[0].add(Nodo(t[2], ''))
		t[0].add(Nodo(t[3], ''))
		t[0].add(t[4])
		t[0].add(Nodo(t[5], ''))
		t[0].add(t[6])
	elif len(t)==5:#UPDATE ID SET listaupdate
		t[0].add(Nodo(t[1], ''))
		t[0].add(Nodo(t[2], ''))
		t[0].add(Nodo(t[3], ''))
		t[0].add(t[4])

def p_listaupdate(t):
	'''
		listaupdate : listaupdate COMA asignacionupdate
					| asignacionupdate
	'''
	if len(t) == 4: # listaupdate COMA asignacionupdate
		t[1].add(t[3])
		t[0] = t[1]
	else:           # asignacionupdate
		t[0] = Nodo("listaupdate", "")
		t[0].add(t[1])

def p_asignacionupdate(t):
	'''
		asignacionupdate : acceso IGUAL exp
	'''
	t[0] = Nodo("asignacionupdate", "")
	t[0].add(t[1])
	t[0].add(Nodo(t[2], ''))
	t[0].add(t[3])

# TODO: Segun la gramatica, hace falta la produccion 'Variable' cuya exp. reg. es: "@[A-Za-z][_A-Za-z0-9]*"
def p_acceso(t):
	'''
		acceso : acceso PT ID
			   | acceso  CORIZQ exp CORDER
			   | ID
	'''
	t[0] = Nodo("acceso", "")

	if len(t) == 4:#acceso PT ID
		t[0].add(t[1])
		t[0].add(Nodo(t[2], ''))
		t[0].add(Nodo(t[3], ''))
		pass
	elif len(t) == 5: #acceso  CORIZQ exp CORDER
		t[0].add(t[1])
		t[0].add(Nodo(t[2], ''))
		t[0].add(t[3])
		t[0].add(Nodo(t[4], ''))
	elif len(t) == 2: # ID
		t[0].add(Nodo(t[1], ''))

def p_acceso1(t):
	'''
		acceso : acceso PT funcioncollection
	'''
	t[0] = Nodo("acceso", "")
	t[0].add(t[1])
	t[0].add(Nodo(t[2], ''))
	t[0].add(t[3])

def p_funcioncollection(t):
	'''
		funcioncollection   : INSERT    PARIZQ exp COMA exp PARDER
							| INSERT    PARIZQ exp PARDER
							| SET       PARIZQ exp COMA exp PARDER
							| REMOVE    PARIZQ exp PARDER
							| SIZE      PARIZQ PARDER
							| CLEAR     PARIZQ PARDER
							| CONTAINS 	PARIZQ exp PARDER
							| LENGTH    PARIZQ PARDER
							| SUBSTRING PARIZQ exp COMA exp PARDER
	'''
	t[0] = Nodo("funcioncollection", "")

	if t[1].lower() == 'insert':

		if len(t) ==7: #INSERT PARIZQ exp COMA exp PARDER
			t[0].add(Nodo(t[1],''))
			t[0].add(Nodo(t[2],''))
			t[0].add(t[3])
			t[0].add(Nodo(t[4],''))
			t[0].add(t[5])
			t[0].add(Nodo(t[6],''))

		elif len(t) == 5: #INSERT PARIZQ exp PARDER
			t[0].add(Nodo(t[1],''))
			t[0].add(Nodo(t[2],''))
			t[0].add(t[3])
			t[0].add(Nodo(t[4],''))

	elif t[1].lower() == 'set': #SET PARIZQ exp COMA exp PARDER
		t[0].add(Nodo(t[1], ''))
		t[0].add(Nodo(t[2], ''))
		t[0].add(t[3])
		t[0].add(Nodo(t[4], ''))
		t[0].add(t[5])
		t[0].add(Nodo(t[6], ''))

	elif t[1].lower() == 'remove': #REMOVE PARIZQ exp PARDER
		t[0].add(Nodo(t[1], ''))
		t[0].add(Nodo(t[2], ''))
		t[0].add(t[3])
		t[0].add(Nodo(t[4], ''))

	elif t[1].lower() == 'size': #SIZE PARIZQ PARDER
		t[0].add(Nodo(t[1], ''))
		t[0].add(Nodo(t[2], ''))
		t[0].add(Nodo(t[3], ''))

	elif t[1].lower() == 'clear': #CLEAR PARIZQ PARDER
		t[0].add(Nodo(t[1], ''))
		t[0].add(Nodo(t[2], ''))
		t[0].add(Nodo(t[3], ''))

	elif t[1].lower() == 'contains': #CONTAINS PARIZQ exp PARDER
		t[0].add(Nodo(t[1], ''))
		t[0].add(Nodo(t[2], ''))
		t[0].add(t[3])
		t[0].add(Nodo(t[4], ''))

	elif t[1].lower() == 'length': #LENGTH PARIZQ PARDER
		t[0].add(Nodo(t[1], ''))
		t[0].add(Nodo(t[2], ''))
		t[0].add(Nodo(t[3], ''))

	elif t[1].lower() == 'substring': #SUBSTRING PARIZQ exp COMA exp PARDER
		t[0].add(Nodo(t[1], ''))
		t[0].add(Nodo(t[2], ''))
		t[0].add(t[3])
		t[0].add(Nodo(t[4], ''))
		t[0].add(t[5])
		t[0].add(Nodo(t[6], ''))

# ---------------DELETE---------------
def p_deletetable(t):
	'''
		deletetable : DELETE FROM ID WHERE exp
					| DELETE FROM ID
					| DELETE listaatributos FROM ID WHERE exp
					| DELETE listaatributos FROM ID
	'''
	t[0] = Nodo("deletetable", "")

	if len(t)==6: # DELETE FROM ID WHERE exp
		t[0].add(Nodo(t[1],''))
		t[0].add(Nodo(t[2],''))
		t[0].add(Nodo(t[3],''))
		t[0].add(Nodo(t[4],''))
		t[0].add(t[5])

	elif len(t) == 4:  # DELETE FROM ID
		t[0].add(Nodo(t[1],''))
		t[0].add(Nodo(t[2],''))
		t[0].add(Nodo(t[3],''))

	elif len(t) == 7:  # DELETE listaatributos FROM ID WHERE exp
		t[0].add(Nodo(t[1],''))
		t[0].add(t[2])
		t[0].add(Nodo(t[3],''))
		t[0].add(Nodo(t[4],''))
		t[0].add(Nodo(t[6],''))
		t[0].add(t[7])

	elif len(t) == 5:  # DELETE listaatributos FROM ID
		t[0].add(Nodo(t[1],''))
		t[0].add(t[2])
		t[0].add(Nodo(t[3],''))
		t[0].add(Nodo(t[4],''))

def p_listaatributos(t):
	'''
		listaatributos : listaatributos COMA acceso
					   | acceso
	'''
	if len(t) == 4:
		t[1].add(t[3])
		t[0] = t[1]
	else:
		t[0] = Nodo("listaatributos","")
		t[0].add(t[1])

# ---------------ERROR SINTACTICO---------------
def p_error(t):
	print(t)
	print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
	global cadena,lisErr, dot
	#parser = yacc.yacc()
	lexer2.lineno=1
	#par= parser.parse("ADD")
	#print(par)
	return parser.parse(input)
