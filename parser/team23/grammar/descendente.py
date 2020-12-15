#Palabras reservadas para la gramatica
reservadas = {
    'select' : 'SELECT',
    'update' : 'UPDATE',
    'where' : 'WHERE',
    'join' : 'JOIN',
    'create' : 'CREATE',
    'delete' : 'DELETE',
    'count' : 'COUNT',
    'sum' : 'SUM',
    'from' : 'FROM',
    'case' : 'CASE',
    'then' : 'THEN',
    'else' : 'ELSE',
    'smallint' : 'SMALLINT',
    'integer' : 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'money' : 'MONEY',
    'char' : 'CHAR',
    'character' : 'CHARACTER',
    'varying' : 'VARYING',
    'timestamp' : 'TIMESTAMP',
    'without' : 'WITHOUT',
    'with' : 'WITH',
    'time' : 'TIME',
    'zone' : 'ZONE',
    'date' : 'DATE',
    'interval' : 'INTERVAL',
    'fields' : 'FIELDS',
    'year' : 'YEAR',
    'month' : 'MONTH',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'to' : 'TO',
    'boolean' : 'BOOLEAN',
    'as' : 'AS',
    'enum' : 'ENUM',
    'type' : 'TYPE',
    'is' : 'IS',
    'isnull' : 'ISNULL',
    'notnull' : 'NOTNULL',
    'not' : 'NOT',
    'and' : 'AND',
    'or' : 'OR',
    'between' : 'BETWEEN',
    'like' : 'LIKE',
    'in' : 'IN',
    'ilike' : 'ILIKE',
    'similar' : 'SIMILAR',
    'replace' : 'REPLACE',
    'mode' : 'MODE',
    'owner' : 'OWNER',
    'if' : 'IF',
    'exists' : 'EXISTS',
    'alter' : 'ALTER',
    'database' : 'DATABASE',
    'rename' : 'RENAME',
    'drop' : 'DROP',
    'table' : 'TABLE',
    'primary' : 'PRIMARY',
    'foreign' : 'FOREIGN',
    'key' : 'KEY',
    'references' : 'REFERENCES',
    'constraint' : 'CONSTRAINT',
    'check' : 'CHECK',
    'set' : 'SET',
    'insert' : 'INSERT',
    'by' : 'BY',
    'group' : 'GROUP',
    'having' : 'HAVING',
    'order' : 'ORDER',
    'when' : 'WHEN',
    'union' : 'UNION',
    'end' : 'END',
    'values' : 'VALUES',
    'intersect' : 'INTERSECT',
    'limit' : 'LIMIT',
    'inner' : 'INNER',
    'left' : 'LEFT',
    'right' : 'RIGHT',
    'outer' : 'OUTER',
    'asc' : 'ASC',
    'desc' : 'DESC',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    'offset' : 'OFFSET',
    'first' : 'FIRST',
    'last' : 'LAST',
    'full' : 'FULL',
    'all' : 'ALL',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'inherits' : 'INHERITS',
    'null' : 'NULL'
}

#Lista de tokens
tokens = [
    'PUNTO',
    'ASTERISCO',
    'PUNTOCOMA',
    'IGUAL',
    'PAR_ABRE',
    'PAR_CIERRA',    
    'CADENA',
    'ENTERO',
    'MENOR_IGUAL',
    'MAS',
    'MAYOR_IGUAL',
    'NO_IGUAL',
    'DIFERENTE',
    'CORCHE_ABRE',
    'CORCHE_CIERRA',
    'CASTEO',
    'MENOR',
    'MAYOR',
    'MENOS',
    'COMA',
    'DIVISION',
    'MODULO',
    'POTENCIA',
    'ID'
] + list(reservadas.values())

#Expresiones regulares
t_PUNTO = r'\.'
t_ASTERISCO = r'\*'
t_MAS       = r'\+'
t_PUNTOCOMA = r';'
t_IGUAL = r'='
t_PAR_ABRE = r'\('
t_PAR_CIERRA = r'\)'
t_MENOR = r'<'
t_MAYOR = r'>'
t_COMA = r','
t_MENOR_IGUAL = r'<='
t_MAYOR_IGUAL = r'>='
t_NO_IGUAL = r'!='
t_DIFERENTE = r'<>'
t_MENOS = r'-'
t_DIVISION = r'/'
t_MODULO = r'%'
t_CORCHE_ABRE = r'\['
t_CORCHE_CIERRA = r'\]'
t_POTENCIA = r'\^'
t_CASTEO = r'::'

def t_DECIMAL(t):
    r'\d+(\.\d+)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor decimal es muy grande %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor entero es muy grande %d", t.value)
        t.value = 0
    return

def t_CADENA(t):
    r'(\".*?\")|(\'.*?\')'
    t.value = t.value[1:-1]
    t.value = t.value.replace("\\\"", "\"").replace("\\\'", "\'").replace("\\n", "\n").replace("\\t", "\t")
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(),'ID') 
    return t

# Comentario de múltiples líneas /* .. */
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
    print("Caracter incorrecto '%s'" % t.value[0])
    t.lexer.skip(1)

import re
import ply.lex as lex
lexer = lex.lex(reflags=re.IGNORECASE)

precedence = (
    ('left', 'PAR_ABRE', 'PAR_CIERRA')
)
#Analizador Sintáctico 

def p_init(t):
    'init            : instrucciones'


def p_instrucciones(t):
    'instrucciones    :  instruccion produc_a'

def p_produc_a(t):
    '''produc_a : instruccion produc_a
            |  '''

def p_instruccion(t):
    '''instruccion : crear t_PUNTOCOMA
	        | SHOW DATABASE t_PUNTOCOMA
            | alter_db t_PUNTOCOMA
    	    | drop_db t_PUNTOCOMA
            | INSERT INTO ID VALUES t_PAR_ABRE list_val t_PAR_CIERRA t_PUNTOCOMA
            | UPDATE ID SET ID t_IGUAL op_val where t_PUNTOCOMA 
            | DELET FROM ID where t_PUNTOCOMA 
            | seleccionar t_PUNTOCOMA'''


def p_crear(t):
    '''crear : CREATE TABLE  ID t_PAR_ABRE  contenido_tabla  t_PAR_CIERRA inherits 	
            |CREATE or_replace DATABASE if_not_exists ID owner_ mode_'''

def p_or_replace(t):
    '''or_replace : OR REPLACE
            | '''

def p_if_not_exists(t):
    '''if_not_exists : IF NOT EXISTS 
               | '''

def p_ower_(t):
    '''owner_ : OWNER = ID
            | '''

def p_mode_(t):
    '''mode_ : MODE = ENTERO
                |'''

def p_alter_db(t):
    '''alter_db: ALTER DATABASE ID rename_owner
             |ALTER TABLE ID alter_op'''

def p_rename_owner(t):
    '''rename_owner: RENAME TO ID
	       |OWNER TO t_LLAVE_ABRE ow_op t_LLAVE_CIERRA'''

def p_ow_op(t):
    '''ow_op: ID
	 |CURRENT_USER
	 |SESSION_USER'''

def p_drop_db(t):
    '''drop_db : DROP DATABASE if_exists ID 
    	   |DROP TABLE ID'''

def p_if_exists(t):
    '''if_exists: IF EXISTS
         |  '''

def p_contenido_tabla(t):
    '''contenido_tabla: contenido_tabla t_COMA manejo_tabla
	         |manejo_tabla'''

def p_manejo_tabla(t):
    '''manejo_tabla: declaracion_columna
	      |condition_column'''

def p_declaracion_columna(t):
    '''declaracion_columna: ID type_column condition_column_row
		        |ID type_column'''

def p_type_column(t):
    '''type_column: SMALLINT
	      |INTEGER
	      |BIGINT
	      |DECIMAL
	      |NUMERIC
	      |REAL
	      |DOUBLE PRECISION
	      |MONEY
	      |VARCHAR t_PAR_ABRE ENTERO t_PAR_CIERRA
          |NVARCHAR t_PAR_ABRE ENRETO t_PAR_CIERRA
          |VARCHAR
          |NVARCHAR
	      |CHAR
 	      |TEXTE
	      |DATE'''

def p_condition_column_row(t):
    '''condition_column_row: condition_column_row condition_column
	               |condition_column'''

def p_condition_column(t):
    '''condition_column: DEFAULT op_val
                |NULL
		        |NOT NULL
	            |constraint UNIQUE op_unique
                |constraint CHECK t_PAR_ABRE  condition_columns t_PAR_CIERRA
                |constraint UNIQUE  constraint CHECK t_PAR_ABRE  condition_columns t_PAR_CIERRA
 		        |key_table                  
                |REFERENCE ID
		        |CONSTRAINT ID key_table
 		        |epsilon'''

def p_constraint(t):
    '''constraint: CONSTRAINT ID
           |epsilon'''

def p_op_unique(t):
'''op_unique: t_PAR_ABRE list_id t_PAR_CIERRA
          |epsilon'''

def p_list_id(t):
'list_id: ID alias produc_b '

def p_produc_b(t):
'''produc_b: , ID alias produc_b
            | epsilon'''

def p_alias(t):
'''alias: AS ID 
      |epsilon'''

def p_condition_columns(t):
'condition_columns: condition_columns produc_c'

def p_produc_c(t):
'''produc_c : , expression produc_c
            | epsilon'''

def p_key_table(t):
'''key_table: PRIMARY KEY list_key 
	    |FOREIGN KEY t_PAR_ABRE list_id t_PAR_CIERRA REFERENCES ID t_PAR_ABRE list_id t_PAR_CIERRA'''

def p_list_key(t):
'''list_key: t_PAR_ABRE list_id t_PAR_CIERRA
	   |epsilon'''

def p_alter_op(t):
'''alter_op: ADD op_add
	   |ALTER COLUMN ID alter_col_op
	   |DROP CONSTRAINT ID'''

def p_op_add(t):   
'''op_add: CHECK t_PAR_ABRE ID t_DIFERENTE t_CADENA t_PAR_CIERRA
       |CONSTRAINT ID UNIQUE t_PAR_ABRE ID t_PAR_CIERRA
       |key_table REFERENCES t_PAR_ABRE list_id t_PAR_CIERRA'''

def p_alter_col_op(t):
'''alter_col_op: SET NOT NULL
             |TYPE type_column'''

def p_inherits(t):
'''inherits: INHERITS t_PAR_ABRE ID t_PAR_CIERRA
         |epsilon'''

def p_list_val(t):
'list_val: op_val produc_d'

def p_produc_d(t):
'''produc_d: , op_val produc_d
            | epsilon'''

def p_op_val(t):
'''op_val: ID
       |t_CADENA
       |t_DECIMAL'''

def p_where(t):
'''where: WHERE ID t_IGUAL op_val
      |epsilon'''

def p_seleccionar(t):
'''seleccionar: SELECT distinto  select_list FROM table_expression list_fin_select
            | SELECT GREATEST expressiones
            | SELECT LEAST expressiones'''

def p_list_fin_select(t):
'list_fin_select: fin_select produc_e'

def p_produc_e(t):
'''produc_e : fin_select produc_e
            | epsilon'''

def p_fin_select(t):
'''fin_select: group_by  
	| donde
	| order_by
	| group_by
	| group_having
	| limite
	|epsilon'''

def p_expressiones(t):
'''expressiones: list_expression
            | ( list_expression )'''

def p_distinto(t):
'''distinto : DISTINCT
	|epsilon'''

def p_select_list(t):
'''select_list: ASTERISCO
	| expressiones'''

def p_table_expression(t):
'table_expression: expressiones'
	
def p_donde(t):
'donde: WHERE expressiones'

def p_group_by(t):
'group_by : GROUP BY expressiones'

def p_order_by(t):
'order_by : ORDER BY expressiones asc_desc nulls_f_l'

def p_group_having(t):
'group_having: HAVING expressiones'

def p_asc_desc(t):
'''asc_desc: ASC
	| DESC'''

def p_nulls_f_l(t):
'''nulls_f_l: NULLS LAST
	| NULLS FIRST
	| epsilon '''

def p_limite(t):
'''limite: LIMIT ENTERO
	| LIMIT ALL
	| OFFSET ENTERO'''

def p_list_expression(t):
'list_expression:  expression produc_f'

def p_produc_f(t):
'''produc_f : , expression produc_f
            | epsilon'''

def p_expression(t):
'''expression: expression > expression
            | expression < expression
            | expression >= expression
            | expression <= expression
            | expression AND expression
            | expression OR expression
            | NOT expression
            | expression = expression
            | expression != expression
            | expression <> expression
            | ( expression )
            | expression BETWEEN expression AND expression
            | expression NOT BETWEEN expression AND expression 
            | expression BETWEEN SYMMETRIC expression AND expression
            | expression NOT BETWEEN SYMMETRIC expression AND expression
            | expression IS DISTINCT FROM expression
            | expression IS NOT DISTINCT FROM expression
            | expression PUNTO expression
            | expression IS NULL
            | expression IS NOT NULL
            | expression ISNULL
            | expression NOTNULL
            | expression IS TRUE
            | expression IS NOT TRUE
            | expression IS FALSE
            | expression IS NOT FALSE
            | expression IS UNKNOWN
            | expression IS NOT UNKNOWN
            | SUBSTRING ( expression COMA expression COMA expression)
            | funciones_math
            | ID
            | CADENA
            | DECIMAL
            | ENTERO
            | *
            | seleccionar'''

def p_funciones_math(t):
'''funciones_math : SUM ( expression )
            | COUNT ( expression )
            | AVG ( expression )
            | MAX ( expression )
            | MIN ( expression )
            | ABS ( expression )
            | CBRT ( expression )
            | CEIL ( expression )
            | CEILING ( expression ) 
            | DEGREES ( expression )
            | DIV ( expression )
            | EXP ( expression )
            | FACTORIAL ( expression ) 
            | FLOOR ( expression )
            | GCD ( expression )
            | LN ( expression )
            | LOG ( expression )
            | MOD ( expression )
            | PI ( expression )
            | POWER ( expression )
            | RADIANS ( expression )
            | ROUND ( expression )'''