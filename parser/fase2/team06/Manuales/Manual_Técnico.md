![Help Builder Web Site](./Logo.png)

# Manual Técnico - Parser (TytusDB-Fase2)
### Grupo 6
<b>Juan Pablo García Monzon - 2012-22615<br>
Jossie Bismarck Castrillo Fajardo 2013-13692<br>
Byron David Cermeno Juarez 2013-13734<br>
Hayrton Omar Ixpata Coloch 2013-13875<br></b>


## Este proyecto necesita estos requerimientos para funcionar

* Navegador (Chrome, Edge, etc)

* Windows 10, Linux, Mac

* 1GB de RAM

* Python

## Estas librerias de Python son necesarias para correr el proyecto:<br>
```python
1. os
2. sys
3. webbrowser
4. tkinter
5. Enum
6. platform
7. re
8. numpy
9. datetime
10. time
11. pandas
12. goto
```

## Flujo del proyecto
* Primero tener el conocimiento que este parser es para analizar un lenguaje de tipo SQL.

* Para esta primera fase no se ha implementado lo que es un ejecutable del proyecto por lo que todavía se ejecuta el archivo "ventana.py" para empezar.

* Se pone una cadena de texto para analizar en el área de texto de fondo blanco, se puede copiar y pegar una cadena o utilizar el botón de "Abrir" que se ubica en el menú "Archivo".

* Al analizar la cadena de texto saldrá una respuesta en la consola, área de texto con fondo negro.

* Se pueden ver todos los reportes generados como "Reporte Gramatical, Reporte de Errores, Reporte de Tabla de Simbolos, Reporte de AST".  

* Si necesita un flujo mas visual se puede ver el manual de usuario en el menú "Manuales" donde se puede visualizar "Manual de Usuario y Manual Técnico".

## Clases principales
### ventana.py
Clase donde se encuentra todo lo relacionado con la interfaz gráfica, las librerias principales utilizadas son "os,webbrowser y tkinter" y las clases referenciadas son "ascendente.py", "CustomText.py" y "TextLine.py".
### TextLine.py
Aquí se encuentran los métodos para obtener el numero de línea actual y agregarlo a la interfaz de usuario.
### CustomText.py
Esta clase y sus métodos son utilizados para el enumerado de línea del área de texto,agrega los eventos necesarios, para que el numero aparezca cada vez que el texto cambia.
### expresiones.py
Clase donde se crean clases abstractas para expresiones aritmeticas, relacionales, lógicas y binaria que nos ayudaran para crear clases que se convertiran en objetos para ir subiendo valores de producciones para luego utilizar esa instancia para usarlo en el análisis semántico.
### queries.py
Clase donde se crean clases abstractas para queries que nos ayudaran para crear clases que se convertiran en objetos para ir subiendo valores de producciones para luego utilizar esa instancia para usarlo en el análisis semántico.
### gramaticaAscendente.py
Esta clase se utiliza para el analisis ascendente. En esta clase se encuentra todos los
métodos del analizador léxico (ply.lex) y todos los métodos del analizador sintáctico
(ply.yaccc) con sus respectivos métodos de error, se crean los primeros valores de
la tabla de simbolos, se genera el reporte gramatical, y si existieran
errores se genera su respectiva lista de errores (léxicos y sintácticos).
### ascendente.py
Clase donde se realiza toda la ejecución (análisis semántico) de la sintaxis de la cadena de entrada, y la generación de los reportes (gramatical, tabla de simbolos, errores y AST).

### reportes.py
Clase donde se crea el formato de los reportes HTML (Errores, Tabla de Simbolos y Gramatical).
### TablaDeSimbolos.py
Clase donde se encuentran los métodos de la estructura de la tabla de símbolos, como obtener, actualizar, mostrar y agregar.
### nodeAst.py
Clase que forma el nodo de el árbol AST.
### astMethod.py
Clase que tiene los métodos para generar el archivo .dot y .png con la herramienta "Graphviz".
### gramaticaAscendenteTree.py
Clase donde se van creando los nodos de tipo nodeAst en cada una de las producciones de la gramática y así subir todos esos datos para subir el AST.
### gramaticaAscendente3D.py
Clase donde se van creando las traducciones a codigo tres direcciones de las diferentes queries.
### optimizacionCodigo3D.py
Clase donde se optimiza con las reglas de Mirilla las prodccciones traducidas.

### Analizador Lexico
#### Palabras reservadas
```python
'show' : 'SHOW',
    'databases' : 'DATABASES',
    'database' : 'DATABASE',
    'tables' : 'TABLES',
    'columns' : 'COLUMNS',
    'from' : 'FROM',
    'select' : 'SELECT',
    'distinct' : 'DISTINCT',
    'limit' : 'LIMIT',
    'offset' : 'OFFSET',
    'of':'OF',
    'order' : 'ORDER',
    'by' : 'BY',
    'where' : 'WHERE',
    'and' : 'AND',
    'or' : 'OR',
    'not' : 'NOT',
    'in' : 'IN',
    'concat' : 'CONCAT',
    'only':'ONLY',

    'as' : 'AS',
    'upper' : 'UPPER',
    'sqrt' : 'SQRT',
    'avg' : 'AVG',
    'sum' : 'SUM',
    'cont' :'CONT',
    'desc' : 'DESC',
    'asc' : 'ASC',
    'like' : 'LIKE',
    'min' : 'MIN',
    'max' : 'MAX',
    'abs' : 'ABS',
    'on' : 'ON',
    'union' : 'UNION',
    'all' : 'ALL',
    'insert' : 'INSERT',
    'unknown':'UNKNOWN',
    'into' : 'INTO',
    'values' : 'VALUES',
    'update' : 'UPDATE',
    'set' : 'SET',
    'delete' : 'DELETE',
    'create' : 'CREATE',
    'primary' : 'PRIMARY',
    'key' : 'KEY',
    'null' : 'NULL',
    'nulls':'NULLS',

    'unique' : 'UNIQUE',
    'check' : 'CHECK',
    'cbrt' : 'CBRT',
    'ceil' : 'CEIL',
    'ceiling' : 'CEILING',
    'degrees' : 'DEGREES',
    'div':'DIV',
    'exp':'EXP',
    'factorial':'FACTORIAL',
    'floor':'FLOOR',
    'gcd':'GCD',
    'lcm':'LCM',
    'ln':'LN',
    'log':'LOG',
    'log10':'LOG10',
    #'current':'CURRENT',
    'default' : 'DEFAULT',
    'auto_increment' : 'AUTO_INCREMENT',
    'alter' : 'ALTER',
    'table' : 'TABLE',
    'add' : 'ADD',
    'drop' : 'DROP',
    'column' : 'COLUMN',
    'rename' : 'RENAME',
    'to' : 'TO',
    'view' : 'VIEW',
    'replace' : 'REPLACE',
    'type' : 'TYPE',
    'enum' : 'ENUM',
    'if' : 'IF',
    'exists' : 'EXISTS',
    'min_scale':'MIN_SCALE',
    'mod':'MOD',
    'pi':'PI',
    'power':'POWER',
    'radians':'RADIANS',
    'round':'ROUND',
    'scale':'SCALE',
    'sign':'SIGN',
    'mode' : 'MODE',
    'owner' : 'OWNER',
    'constraint' : 'CONSTRAINT',
    'foreign' : 'FOREIGN',
    'references' : 'REFERENCES',
    'inherits' : 'INHERITS',
    'group' : 'GROUP',
    'having' : 'HAVING',
    'inner' : 'INNER',
    'outer' : 'OUTER',
    'trim_scale':'TRIM_SCALE',
    'truc':'TRUC',
    'width_bucket':'WIDTH_BUCKET',
    'random':'RANDOM',
    'setseed':'SETSEED',
    'acos':'ACOS',
    'acosd':'ACOSD',
    'asin':'ASIN',
    'asind':'ASIND',
    'atan':'ATAN',
    'atan2':'ATAN2',
    'cos':'COS',
    'cosd':'COSD',
    'cot':'COT',
    'cotd':'COTD',
    'sin':'SIN',
    'sind':'SIND',
    'tan':'TAN',
    'tand':'TAND',
    'sinh':'SINH',
    'cosh':'COSH',
    'tanh':'TANH',
    'asinh':'ASINH',
    'acosh':'ACOSH',
    'atanh':'ATANH',
    'length':'LENGTH',
    'substring':'SUBSTRING',
    'trim':'TRIM',
    'get_byte':'GET_BYTE',
    'md5':'MD5',
    'set_byte':'SET_BYTE',
    'sha256':'SHA256',
    'substr':'SUBSTR',
    'convert':'CONVERT',
    'encode':'ENCODE',
    'decode':'DECODE',
    'escape':'ESCAPE',
    'any':'ANY',
    'some':'SOME',
    'using':'USING',
    'first':'FIRST',
    'last':'LAST',
    'current_user':'CURRENT_USER',
    'session_user':'SESSION_USER',
    'symmetric':'SYMMETRIC',
    'izquierda' : 'LEFT',
    'derecha' : 'RIGHT',
    'full' : 'FULL',
    'join' : 'JOIN',
    'natural' : 'NATURAL',
    'case' : 'CASE',
    'when' : 'WHEN',
    'then' : 'THEN',
    'begin' : 'BEGIN',
    'end' : 'END',
    'else' : 'ELSE',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    'intersect' : 'INTERSECT',
    'except' : 'EXCEPT',
    #  tipos de datos permitidos
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
    'text' : 'TEXT',
    'boolean' : 'BOOLEAN',
    'timestamp':'TIMESTAMP',
    'time':'TIME',
    'date':'DATE',
    'interval':'INTERVAL',
    'year':'YEAR',
    'month':'MONTH',
    'day':'DAY',
    'hour':'HOUR',
    'minute':'MINUTE',
    'second':'SECOND',
    'to':'TO',
    'true':'TRUE',
    'false':'FALSE',
    'declare' : 'DECLARE',
    'function' : 'FUNCTION',
    'returns' : 'RETURNS',
    'returning':'RETURNING',

    'between' : 'BETWEEN',
    'ilike' : 'ILIKE',
    'is':'IS',
    'isnull':'ISNULL',
    'notnull':'NOTNULL',
    #enums
    'type':'TYPE',
    'ENUM':'ENUM',

    #para trim
    'leading':'LEADING',
    'trailing':'TRAILING',
    'both':'BOTH',
    'for':'FOR',
    'symmetric':'SYMMETRIC'
```
### Listado de Tokens
```python
t_PUNTOYCOMA                            = r';'
t_MAS                                   = r'\+'
t_MENOS                                 = r'-'
t_POR                                   = r'\*'
t_DIV                                   = r'/'
t_DOSPUNTOS                             = r':'
t_PUNTO                                 = r'\.'
t_TYPECAST                              = r'::'
t_CORCHETEDER                           = r']'
t_CORCHETEIZQ                           = r'\['
t_POTENCIA                              = r'\^'
t_RESIDUO                               = r'%'
t_MAYOR                                 = r'<'
t_MENOR                                 = r'>'
t_IGUAL                                 = r'='
t_MAYORIGUAL                            = r'>='
t_MENORIGUAL                            = r'<='
t_DIFERENTE                             = r'<>'
t_IGUALIGUAL                            = r'=='
t_PARENTESISIZQUIERDA                   = r'\('
t_PARENTESISDERECHA                     = r'\)'
t_COMA                                  = r','
t_NOTEQUAL                              = r'!='
t_SIMBOLOOR                             = r'\|\|' 
t_SIMBOLOAND                            = r'&&'
t_SIMBOLOAND2                           = r'\&'
t_SIMBOLOOR2                            = r'\|'
t_DESPLAZAMIENTODERECHA                 = r'>>'
t_DESPLAZAMIENTOIZQUIERDA               = r'<<'
```
### Expresiones Regulares
```python
Entero: r'\d+'
Decimal: r'\d+\.\d+'
Cadena: r'[\'|\"].*?[\'|\"]'
Identificador: r'[a-zA-Z]+[a-zA-_Z0-9]*'
Comentario Unilinea: r'--.*\n'
Comentario Multilinea: r'/\*(.|\n|)*?\*/'
Salto de Linea: r'\n+'
```
## Analizador Sintáctico
### Precendencia
```python
('left','TYPECAST'),
('right','UMINUS'),
('right','UNOT'),
('left','MAS','MENOS'),
('left','POTENCIA'),
('left','POR','DIV','RESIDUO'),
('left','AND','OR','SIMBOLOOR2','SIMBOLOOR','SIMBOLOAND2'),
('left','DESPLAZAMIENTOIZQUIERDA','DESPLAZAMIENTODERECHA'),
```
### Gramática
```sql
inicio               ::= queries 

 queries               ::= queries query

 queries               ::= query    

 query        ::= mostrarBD
                 | crearBD
                 | alterBD
                 | dropBD
                 | operacion
                 | insertinBD
                 | updateinBD
                 | deleteinBD
                 | createTable
                 | inheritsBD
                 | dropTable
                 | alterTable
                 | variantesAt
                 | contAdd
                 | contDrop
                 | contAlter
                 | listaid
                 | tipoAlter                    
                 | selectData

 crearBD    ::= CREATE DATABASE ID PUNTOYCOMA

 crearBD    ::= CREATE OR REPLACE DATABASE ID PUNTOYCOMA

 crearBD    ::= CREATE OR REPLACE DATABASE ID parametrosCrearBD PUNTOYCOMA

 crearBD    ::= CREATE  DATABASE ID parametrosCrearBD PUNTOYCOMA


createIndex    ::= CREATE INDEX ID ON ID PARENTESISIZQUIERDA listaid PARENTESISDERECHA PUNTOYCOMA

createIndex    ::= CREATE INDEX ID ON ID PARENTESISIZQUIERDA lower PARENTESISDERECHA PUNTOYCOMA

createIndex    ::= CREATE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA PUNTOYCOMA

createIndex    ::= CREATE INDEX ID ON ID PARENTESISIZQUIERDA listaid PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA

createIndex    ::= CREATE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA WHERE whereOptions  PUNTOYCOMA

createIndex    ::= CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA listaid PARENTESISDERECHA PUNTOYCOMA

createIndex    ::= CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA PUNTOYCOMA

createIndex    ::= CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA listaid PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA

createIndex    ::= CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA

createIndex    ::= CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA listaid PARENTESISDERECHA PUNTOYCOMA

createIndex    ::= CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA PUNTOYCOMA

createIndex    ::= CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA listaid PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA

createIndex    ::= CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA

dropIndex    ::= DROP INDEX ID PUNTOYCOMA

dropIndex    ::= DROP INDEX IF EXISTS ID PUNTOYCOMA

alterIndex    ::= ALTER INDEX ID RENAME TO ID PUNTOYCOMA

alterIndex    ::= ALTER INDEX IF EXISTS ID RENAME TO ID PUNTOYCOMA

alterIndex    ::= ALTER INDEX ID ALTER final PUNTOYCOMA

alterIndex    ::= ALTER INDEX ID ALTER COLUMN final PUNTOYCOMA

alterIndex    ::= ALTER INDEX IF EXISTS ID ALTER final PUNTOYCOMA

alterIndex    ::= ALTER INDEX IF EXISTS ID ALTER COLUMN final PUNTOYCOMA
  
indexParams    ::= sort

whereOptions    ::= asignaciones

whereOptions    ::= operacion

whereOptions    ::= search_condition

sort    ::= NULLS FIRST

sort    ::= DESC NULLS FIRST

sort    ::= ASC NULLS FIRST

sort    ::= NULLS LAST

sort    ::= DESC NULLS LAST

sort    ::= ASC NULLS LAST

lower    ::= ID PARENTESISIZQUIERDA ID PARENTESISDERECHA


 parametrosCrearBD ::= parametrosCrearBD parametroCrearBD

 parametrosCrearBD ::=  parametroCrearBD

parametroCrearBD ::=  OWNER IGUAL final
                     |  MODE IGUAL final


 mostrarBD  ::= SHOW DATABASES PUNTOYCOMA

 alterBD    ::= ALTER DATABASE ID RENAME TO ID PUNTOYCOMA

 alterBD    ::= ALTER DATABASE ID OWNER TO parametroAlterUser PUNTOYCOMA

parametroAlterUser ::= CURRENT_USER
                     |   SESSION_USER
                     |   final

 dropTable  ::= DROP TABLE ID PUNTOYCOMA

 alterTable  ::= ALTER TABLE ID variantesAt PUNTOYCOMA

 variantesAt ::=   ADD contAdd
             |   ALTER contAlter
             |   DROP contDrop

 listaContAlter  ::= listaContAlter COMA contAlter 

 listaContAlter  ::= contAlter

 contAlter   ::= COLUMN ID SET NOT NULL 
             | COLUMN ID TYPE tipo

 contAdd     ::=   COLUMN ID tipo 
             |   CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA
             |   FOREIGN KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA REFERENCES ID
             |   CONSTRAINT ID UNIQUE PARENTESISIZQUIERDA listaid PARENTESISDERECHA

 contDrop    ::= COLUMN ID 
             | CONSTRAINT ID

 listaid     ::=   listaid COMA ID

 listaid     ::=   ID

 tipoAlter   ::=   ADD 
             |   DROP

 dropBD    ::= DROP DATABASE ID PUNTOYCOMA

 dropBD    ::= DROP DATABASE IF EXISTS ID PUNTOYCOMA

 operacion          ::= operacion MAS operacion
                       | operacion MENOS operacion
                       | operacion POR operacion
                       | operacion DIV operacion
                       | operacion RESIDUO operacion
                       | operacion POTENCIA operacion
                       | operacion AND operacion
                       | operacion OR operacion
                       | operacion SIMBOLOOR2 operacion
                       | operacion SIMBOLOOR operacion
                       | operacion SIMBOLOAND2 operacion
                       | operacion DESPLAZAMIENTOIZQUIERDA operacion
                       | operacion DESPLAZAMIENTODERECHA operacion
                       | operacion IGUAL operacion
                       | operacion IGUALIGUAL operacion
                       | operacion NOTEQUAL operacion
                       | operacion MAYORIGUAL operacion
                       | operacion MENORIGUAL operacion
                       | operacion MAYOR operacion
                       | operacion MENOR operacion
                       | operacion DIFERENTE operacion
                       | PARENTESISIZQUIERDA operacion PARENTESISDERECHA                          

 operacion ::= MENOS ENTERO  %prec UMINUS

 operacion ::= NOT operacion %prec UNOT

 operacion  ::= funcionBasica

 operacion ::=     final

 funcionBasica    ::= ABS PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | CBRT PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | CEIL PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | CEILING PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | DEGREES PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | DIV PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | EXP PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | FACTORIAL PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | FLOOR PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | GCD PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                     | LCM PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                     | LN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | LOG PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | LOG10 PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                 


                     | MIN_SCALE PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | MOD PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                     | POWER PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                     | RADIANS PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | SCALE ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | SIGN ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | SQRT ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | TRIM_SCALE ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | TRUC ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | WIDTH_BUCKET PARENTESISIZQUIERDA operacion COMA operacion COMA operacion COMA operacion PARENTESISDERECHA
                     | RANDOM PARENTESISIZQUIERDA PARENTESISDERECHA
                     | SETSEED PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | ACOS  PARENTESISIZQUIERDA operacion PARENTESISDERECHA



                     | ACOSD PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | ASIN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | ASIND PARENTESISIZQUIERDA operacion PARENTESISDERECHA                
                     | ATAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | ATAN2 PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | COS PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                  | COSD  PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | COT PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | COTD PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | SIN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | SIND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | TAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | TAND  PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | SINH PARENTESISIZQUIERDA operacion PARENTESISDERECHA



                     | COSH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | TANH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | ASINH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | ACOSH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | ATANH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | LENGTH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | TRIM PARENTESISIZQUIERDA opcionTrim operacion FROM operacion PARENTESISDERECHA
                     | GET_BYTE PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                     | MD5 PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | SET_BYTE PARENTESISIZQUIERDA operacion COMA operacion COMA operacion PARENTESISDERECHA
                     | SHA256 PARENTESISIZQUIERDA operacion PARENTESISDERECHA                       
                     | SUBSTR PARENTESISIZQUIERDA operacion  COMA operacion COMA operacion PARENTESISDERECHA
                     | CONVERT PARENTESISIZQUIERDA operacion  COMA operacion COMA operacion PARENTESISDERECHA
                     | ENCODE PARENTESISIZQUIERDA operacion  COMA operacion  PARENTESISDERECHA
                     | DECODE PARENTESISIZQUIERDA operacion  COMA operacion  PARENTESISDERECHA
                     | AVG PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                     | SUM PARENTESISIZQUIERDA operacion PARENTESISDERECHA

 funcionBasica   ::= SUBSTRING PARENTESISIZQUIERDA operacion FROM operacion FOR operacion PARENTESISDERECHA

 funcionBasica   ::= SUBSTRING PARENTESISIZQUIERDA operacion FROM operacion PARENTESISDERECHA

 funcionBasica   ::= SUBSTRING PARENTESISIZQUIERDA operacion FOR operacion PARENTESISDERECHA

  opcionTrim  ::= LEADING
                 | TRAILING
                 | BOTH

 final        ::= DECIMAL
                 | ENTERO

 final          ::= ID

 final          ::= ID PUNTO ID

 final          ::= CADENA

 insertinBD           ::= INSERT INTO ID VALUES PARENTESISIZQUIERDA listaParam PARENTESISDERECHA PUNTOYCOMA

 insertinBD           ::= INSERT INTO ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA VALUES PARENTESISIZQUIERDA listaParam PARENTESISDERECHA PUNTOYCOMA

 listaParam         ::= listaParam COMA final

 listaParam         ::= final

 updateinBD           ::= UPDATE ID SET asignaciones WHERE asignaciones PUNTOYCOMA

 asignaciones       ::= asignaciones COMA asigna

 asignaciones       ::= asigna

 asigna             ::= ID IGUAL operacion

 deleteinBD         ::= DELETE FROM ID PUNTOYCOMA

 deleteinBD         ::= DELETE FROM ID WHERE operacion PUNTOYCOMA

 createTable        ::= CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA PUNTOYCOMA

 inheritsBD         ::= CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA  INHERITS PARENTESISIZQUIERDA ID PARENTESISDERECHA PUNTOYCOMA

 creaColumnas        ::= creaColumnas COMA Columna 

 creaColumnas        ::= Columna 

 Columna            ::= ID tipo

 Columna            ::= ID tipo paramOpcional

 Columna            ::= uniqueinColumn

 Columna          ::= constraintinColumn 
                     | checkinColumn
                     | primaryKey
                     | foreignKey

 paramOpcional    ::= paramOpcional paramopc
 
 paramOpcional    ::= paramopc


 paramopc         ::= DEFAULT final
                     | NULL
                     | NOT NULL
                     | UNIQUE
                     | PRIMARY KEY

 paramopc           ::= constraintinColumn

 paramopc           ::= checkinColumn

 paramopc           ::= CONSTRAINT ID UNIQUE

 constraintinColumn   ::= CONSTRAINT ID checkinColumn

 ConstraintinColumn     ::= CONSTRAINT ID uniqueinColumn

 checkinColumn      ::= CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA

 uniqueinColumn     ::= UNIQUE PARENTESISIZQUIERDA listaParam PARENTESISDERECHA

 primaryKey         ::= PRIMARY KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA

 foreignKey         ::= FOREIGN KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA REFERENCES ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA 

 tipo            ::=  SMALLINT
                     | INTEGER
                     | BIGINT
                     | DECIMAL
                     | NUMERIC
                     | REAL
                     | DOUBLE PRECISION
                     | MONEY
                     | VARCHAR PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA
                     | CHARACTER VARYING PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA
                     | CHARACTER PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA
                     | CHAR PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA
                     | TEXT
                     | BOOLEAN
                     | TIMESTAMP
                     | TIME
                     | INTERVAL
                     | DATE
                     | YEAR
                     | MONTH 
                     | DAY
                     | HOUR 
                     | MINUTE
                     | SECOND

 selectData       ::= SELECT select_list FROM select_list WHERE search_condition opcionesSelect PUNTOYCOMA
                     | SELECT POR FROM select_list WHERE search_condition opcionesSelect PUNTOYCOMA



 selectData       ::= SELECT select_list FROM select_list WHERE search_condition  PUNTOYCOMA
                     | SELECT POR FROM select_list WHERE search_condition  PUNTOYCOMA


 selectData       ::= SELECT select_list FROM select_list  PUNTOYCOMA
                     | SELECT POR FROM select_list  PUNTOYCOMA


 selectData       ::= SELECT select_list   PUNTOYCOMA

 opcionesSelect   ::= opcionesSelect opcionSelect

 opcionesSelect   ::= opcionSelect


 opcionSelect     ::= LIMIT operacion
                     | GROUP BY select_list
                     | HAVING select_list
                     | ORDER BY select_list 
 opcionSelect     ::= LIMIT operacion OFFSET operacion
                     | ORDER BY select_list ordenamiento                     

 ordenamiento     ::= ASC
                     | DESC 

 search_condition   ::= search_condition AND search_condition
                       | search_condition OR search_condition                         

 search_condition   ::= NOT search_condition

 search_condition   ::= operacion

 search_condition   ::= PARENTESISIZQUIERDA search_condition PARENTESISDERECHA

  select_list   ::= select_list COMA operacion
 
 select_list    ::= operacion

  select_list   ::= select_list condicion_select operacion COMA operacion 

  select_list   ::= condicion_select   operacion 

  select_list   ::= select_list AS  operacion 

 condicion_select ::= DISTINCT FROM                 

 condicion_select ::= IS DISTINCT FROM                             

 condicion_select ::= IS NOT DISTINCT  FROM

 condicion_select ::= DISTINCT 

 condicion_select ::=  IS DISTINCT                 

 condicion_select ::= IS NOT DISTINCT                 

 funcionBasica   ::= operacion BETWEEN operacion AND operacion

 funcionBasica   ::=  operacion LIKE CADENA

 funcionBasica   ::= operacion  IN PARENTESISIZQUIERDA select_list PARENTESISDERECHA 

 funcionBasica   ::= operacion NOT BETWEEN operacion AND operacion 

 funcionBasica   ::= operacion  BETWEEN SYMMETRIC operacion AND operacion

 funcionBasica   ::= operacion NOT BETWEEN SYMMETRIC operacion AND operacion

 funcionBasica   ::= operacion condicion_select operacion
```



