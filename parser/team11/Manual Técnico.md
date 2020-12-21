# Manual Técnico Proyecto 1 : *TytusDB*
<p align="center">
  <img src="img/tytus.png" width="100" alt="Presentación">
</p>

---

        Universidad de San Carlos de Guatemala
        Facultad de ingeniería
        Escuela de Ciencias y Sistemas 
        781 Organización de lenguajes y compiladores 2
        Manual de usuario proyecto 1

                                                   Perteneciente a: Grupo 11
                                                  

***
## Índice
- [Competencias del proyecto](#competencias-del-proyecto)
- [Descripcion de TytusDB](#descripcion-de-tytusdb)
- [Flujo del programa](#flujo-del-programa)
- [Plataforma de Desarrollo](#plataforma-de-desarrollo)
- [Gramatica utilizada](#gramatica-utilizada)
    - [Analisis Léxico](#Analisis-Léxico)
    - [Analisis Sintáctico](#Analisis-Sintáctico)
***
## Competencias del proyecto:
### *General:*
- Poner en práctica los conocimientos teóricos adquiridos durante cada curso y aplicarlo a un proyecto real de código abierto fortaleciendo las competencias de administración de equipos de desarrollo.
### *Específico:*
- El estudiante construye un intérprete para el subconjunto del lenguaje SQL mediante la traducción dirigida por la sintaxis.
- El estudiante utiliza la herramienta PLY o SLY de Python para la traducción.

 
***
## Descripcion de TytusDB:
Es un proyecto Open Source para desarrollar un administrador de bases de datos. Está compuesto por tres componentes interrelacionados: el administrador de almacenamiento de la base de datos, que estará a cargo del curso de Estructuras de Datos; el administrador de la base de datos, que estará a cargo del curso de Sistemas de Bases de Datos 1, este administrador se compone a su vez de un servidor y de un cliente; y el SQL Parser, que estará a cargo del curso de Organización de Lenguajes y Compiladores 2.

### Utilización de funciones CRUD de las bases de datos:
```
def createDatabase(database: str) -> int:
```
Crea una base de datos.  (CREATE)  
Parámetro database: es el nombre de la base de datos, debe cumplir con las reglas de identificadores de SQL.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 base de datos existente  

```
def showDatabases() -> list:
```
Devuelve una lista de los nombres de las bases de datos. (READ)  
Valor de retorno: lista de strings con los nombres de las bases de datos, si ocurrió un error o no hay bases de datos devuelve una lista vacía [].  

```
def alterDatabase(databaseOld, databaseNew) -> int:
```
Renombra la base de datos databaseOld por databaseNew.  (UPDATE)  
Parámetro databaseOld: es el nombre actual de la base de datos, debe cumplir con las reglas de identificadores de SQL.  
Parámetro databaseNew: es el nuevo nombre que tendrá de la base de datos databaseOld, debe cumplir con las reglas de identificadores de SQL.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 databaseOld no existente, 3 databaseNew existente.  

```
def dropDatabase(database: str) -> int: 
```
Elimina por completo la base de datos indicada en database.  (DELETE)  
Parámetro database: es el nombre de la base de datos que se desea eliminar, debe cumplir con las reglas de identificadores de SQL.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 base de datos no existente.  


### Utilización de funciones CRUD de las tablas:

```
def createTable(database: str, table: str, numberColumns: int) -> int:
```
Crea una tabla en una base de datos especificada recibiendo una lista de índices referentes a la llave primaria y llave foránea.  (CREATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla que se desea crear.  
Parámetro numberColumns: es el número de columnas que tendrá cada registro de la tabla.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 base de datos inexistente, 3 tabla existente.  

```
def showTables(database: str) -> list:
```
Devuelve una lista de los nombres de las tablas de una bases de datos.  (READ)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Valor de retorno: si existen la base de datos y las tablas devuelve una lista de nombres de tablas, si existe la base de datos pero no existen tablas devuelve una lista vacía, y si no existe la base de datos devuelve None.  

```
def extractTable(database: str, table: str) -> list:
```
Extrae y devuelve una lista con elementos que corresponden a cada registro de la tabla.  (READ)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Valor de retorno: si existen la base de datos, la tabla y los registros devuelve una lista con los registros, si existen las base de datos, la tablas pero no registros devuelve una lista vacía, y si no existe la base de datos o la tabla devuelve None.  

```
def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
```
Extrae y devuelve una lista con los elementos que corresponden a un rango de registros de la tabala.  (READ)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Parámetro columnNumber: es el número de índice de columna a restringir o verificar con los valores upper y lower.
Parámetro lower: es el limite inferior (inclusive) del rango a extraer de la columna indicada de la tabla.  
Parámetro upper: es el limite superior (inclusive) del rango a extraer de la columna indicada de la tabla.  
Valor de retorno: si existen la base de datos, la tabla y los registros devuelve una lista con los registros(lista), si existen las base de datos, la tablas pero no registros devuelve una lista vacía, y si no existe la base de datos o la tabla o cualquier error devuelve None.  
Consideraciones:
- Para la comparación de lower y upper se puede hacer cast a str cuando las llaves sean compuestas o en general para reducir complejidad.
- Ver el submódulo Any del paquete typing.  

```
def alterAddPK(database: str, table: str, columns: list) -> int:
```
Asocia a la tabla una llave primaria simple o compuesta mediante la lista de número de columnas, esto para anticipar el índice de la estructura de la tabla cuando se inserten registros. (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Parámetro columns: es el listado de números de columnas que formarán parte de la llave primaria. 
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave primaria existente, 5 columnas fuera de limites.  

Considerar:
- Si no se define al menos una llave primaria, cuando ocurre el primer insert se debe utilizar una llave primaria escondida (numérica).  
- Si ya existían datos sin llave primaria explícita se recalcula el índice de la estructura de índices con la actual llave primaria.  
- Si la llave primaria es compuesta, se sugiere concatener en cualqueir estilo las columnas, para manternas intactas (sería como llave primaria escondida).
- El error 42P16 de PostgreSQL invalid_table_definition, entre algunas causas no permite definir múltiples llaves primarias (nótese de la diferencia de una llave primaria compuesta). Si ya existe una llave primaria y se desea agregar otro campo, entonces se debe eliminar la llave actual recalculado el índice cuando sea modificado, si no hay modificación se queda con el llave anterior.
- El error 23505 de PostgreSQL unique_violation, cuando se ejecuta esta función se debe recalcular el índice, si hay un valor duplicado en una parte de la llave primaria debe dar error y dejar el índice como estaba.

```
def alterDropPK(database: str, table: str) -> int:
```
Elimina la llave primaria actual en la información de la tabla, manteniendo el índice actual de la estructura del árbol hasta que se invoque de nuevo el alterAddPK().  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 pk no existente.  

```
def alterAddFK(database: str, table: str, references: dict) -> int:
```
Asocia la integridad referencial entre llaves foráneas y llaves primarias, para efectos de la fase 1 se ignora esta petición. Debido a que será parte de la fase 2 en la construcción de índices secundarios.  (UPDATE PENDIENTE)  

```
def alterAddIndex(database: str, table: str, references: dict) -> int:
```
Asocia un índice, para efectos de la fase 1 se ignora esta petición. Debido a que será parte de la fase 2 en la construcción de índices secundarios.  (UPDATE PENDIENTE)  

```
def alterTable(database: str, tableOld: str, tableNew: str) -> int:
```
Renombra el nombre de la tabla de una base de datos especificada.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro tableOld: es el nombre de la tabla a renombrar.  
Parámetro tableNew: es el nuevo nombre con que renombrará la tableOld.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 tableOld no existente, 4 tableNew existente.  

```
def alterAddColumn(database: str, table: str, default: any) -> int:
```
Agrega una columna al final de cada registro de la tabla y base de datos especificada.  (UPDATE) 
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a modificar.  
Parámetro default: es el valor que se establecerá en al nueva columna para los registros existentes.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente.  

```
def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
```
Eliminar una n-ésima columna de cada registro de la tabla excepto si son llaves primarias.  (DELETE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a modificar.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave no puede elimnarse o tabla quedarse sin columnas, 5 columna fuera de limites.  

```
def dropTable(database: str, table: str) -> int: 
```
Elimina por completo una tabla de una base de datos especificada.  (DELETE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a eliminar.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente.  

### Utilización de las funciones CRUD de las tuplas:

```
def insert(database: str, table: str, register: list) -> int:
```
Inserta un registro en la estructura de datos asociada a la tabla y la base de datos.  (CREATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Parámetro register: es una lista de elementos que representan un registro.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave primari  a duplicada, 5 columnas fuera de limites.  

```
def loadCSV(file: str, database: str, table: str) -> list:
```
Carga un archivo CSV de una ruta especificada indicando la base de datos y tabla donde será almacenado. La base de datos y la tabla deben existir, y coincidir con el número de columnas. Si hay llaves primarias duplicadas se ignoran. No se utilizan títulos de columnas y la separación es por comas.  (CREATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Valor de retorno, una lista con el resultado de insertar cada línea del CSV: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave primari  a duplicada, 5 columnas fuera de limites.  

```
def extractRow(database: str, table: str, columns: list) -> list:
```
Extrae y devuelve un registro especificado por su llave primaria.  (READ)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Parámeto columns: es la llave primaria, si es simple [llave], si es compuesta [llaveatr1, llaveatr2...].  (si no hay pk se debe enviar la hiddenPK)  
Valor de retorno: lista con los valores del registro, si ocurrió un error o no hay registro que mostrar devuelve una lista vacía [].  

```
def update(database: str, table: str, register: dict, columns: list) -> int:
``` 
Inserta un registro en la estructura de datos asociada a la tabla y la base de datos.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Parámetro register: es una lista de elementos llave:valor que representa los elementos a actualizar del registro. La llave el número de coluna y el valor el contenido del campo.  
Parámeto columns: es la llave primaria, si es simple [llave], si es compuesta [llaveatr1, llaveatr2...].  (si no hay pk se debe enviar la hiddenPK)
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave primaria no existe.

```
def delete(database: str, table: str, columns: list) -> int:
```
Elimina un registro de una tabla y base de datos especificados por la llave primaria.  (DELETE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Parámeto columns: es la llave primaria, si es simple [llave], si es compuesta [llaveatr1, llaveatr2...].  (si no hay pk se debe enviar la hiddenPK)  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave primaria no existe.  

```
def truncate(database: str, table: str) -> int:
```
Elimina todos los registros de una tabla y base de datos.  (DELETE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente.  

---

## Flujo del programa:
<p align="center">
  <img src="img/flujo.png" width="700" alt="Presentación">
</p>
TytusDB ha sido creado para los desarroladores tanto como principiantes como avanzados en el lenguaje SQL (especificamente POSTGRES SQL) Dado que puede recibir toda las instrucciones SQL, este programa puede brindar al usuario una serie de reportes en los cuales se pueden analizar todas las instrucciones ingresadas asi como su salida de resultados con sus respectivos errores tanto léxicos, sintácticos y semánticos. Reporte AST mostrando las instrucciones ingresadas de una forma ascendente. 
Este programa ha sido desarrollado en Python, bajo licencia MIT.

---
## Plataforma de Desarrollo
El programa se ha desarrollado en el IDE Visual Studio Code:
* Versión: 1.52.1 (user setup)
* Confirmación: ea3859d4ba2f3e577a159bc91e3074c5d85c0523
* Fecha: 2020-12-16T16:34:46.910Z
* Electron: 9.3.5
* Chrome: 83.0.4103.122
* Node.js: 12.14.1
* V8: 8.3.110.13-electron.0
* Sistema Operativo: Windows_NT x64 10.0.19041
---
## Gramatica utilizada

### Analisis Léxico
#### *Palabras Reservadas*
    reservadas = {
    'smallint': 'SMALLINT',          'integer': 'INTEGER',
    'bigint': 'BIGINT',            'numeric': 'NUMERIC',
    'real': 'REAL',              'mode': 'MODE',
    'double': 'DOUBLE',            'precision': 'PRECISION',
    'money': 'MONEY',             'character': 'CHARACTER',
    'varying': 'VARYING',           'varchar': 'VARCHAR',
    'char': 'CHAR',              'text': 'TEXT',
    'date': 'DATE',              'time': 'TIME',
    'timestamp': 'TIMESTAMP',    'float': 'FLOAT',
    'int': 'INT',                'inherits': 'INHERITS',
    'boolean': 'BOOLEAN',           'create': 'CREATE',
    'or': 'OR',                'replace': 'REPLACE',
    'database': 'DATABASE',          'if': 'IF',
    'not': 'NOT',               'exists': 'EXISTS',
    'owner': 'OWNER',             'show': 'SHOW',
    'like': 'LIKE',              'regex': 'REGEX',
    'alter': 'ALTER',             'rename': 'RENAME',
    'to': 'TO',                'current_user': 'CURRENT_USER',
    'session_user': 'SESSION_USER',    'drop': 'DROP',
    'table': 'TABLE',             'default': 'DEFAULT',
    'null': 'NULL',               'unique': 'UNIQUE',
    'and': 'AND',                'constraint': 'CONSTRAINT',
    'check': 'CHECK',             'primary': 'PRIMARY',
    'key': 'KEY',               'references': 'REFERENCES',
    'foreign': 'FOREIGN',           'add': 'ADD',
    'column': 'COLUMN',            'insert': 'INSERT',
    'into': 'INTO',              'values': 'VALUES',
    'update': 'UPDATE',             'set': 'SET',
    'where': 'WHERE',             'delete': 'DELETE',
    'from': 'FROM',              'truncate': 'TRUNCATE',
    'cascade': 'CASCADE',           'year': 'YEAR',
    'month': 'MONTH',              'day': 'DAY',
    'minute': 'MINUTE',             'second': 'SECOND',
    'enum': 'ENUM',               'type': 'TYPE',
    'interval': 'INTERVAL',           'zone': 'ZONE',
    'databases': 'DATABASES',         'without': 'WITHOUT',
    'with': 'WITH',               'hour': 'HOUR',
    'select': 'SELECT',
    'as': 'AS',                'distinct': 'DISTINCT',
    'count': 'COUNT',             'sum': 'SUM',
    'avg': 'AVG',               'max': 'MAX',
    'min': 'MIN',               'in': 'IN',
    'group': 'GROUP',             'by': 'BY',
    'order': 'ORDER',             'having': 'HAVING',
    'asc': 'ASC',               'desc': 'DESC',
    'nulls': 'NULLS',             'first': 'FIRST',
    'last': 'LAST',              'limit': 'LIMIT',
    'all': 'ALL',               'offset': 'OFFSET',
    'abs': 'ABS',                'cbrt': 'CBRT',
    'ceil': 'CEIL',               'ceiling': 'CEILING',
    'degrees': 'DEGREES',            'div': 'DIV',
    'exp': 'EXP',                'factorial': 'FACTORIAL',
    'floor': 'FLOOR',              'gcd': 'GCD',
    'ln': 'LN',                 'log': 'LOG',
    'mod': 'MOD',                'pi': 'PI',
    'power': 'POWER',              'radians': 'RADIANS',
    'round': 'ROUND',
    'acos': 'ACOS',               'acosd': 'ACOSD',
    'asin': 'ASIN',               'asind': 'ASIND',
    'atan': 'ATAN',               'atand': 'ATAND',
    'atan2': 'ATAN2',              'atan2d': 'ATAN2D',
    'cos': 'COS',                'cosd': 'COSD',
    'cot': 'COT',                'cotd': 'COTD',
    'sin': 'SIN',                'sind': 'SIND',
    'tan': 'TAN',                'tand': 'TAND',
    'sinh': 'SINH',               'cosh': 'COSH',
    'tanh': 'TANH',               'asinh': 'ASINH',
    'acosh': 'ACOSH',              'atanh': 'ATANH',
    'length': 'LENGTH',             'substring': 'SUBSTRING',
    'trim': 'TRIM',               'get_byte': 'GET_BYTE',
    'md5': 'MD5',                'set_byte': 'SET_BYTE',
    'sha256': 'SHA256',             'substr': 'SUBSTR',
    'convert': 'CONVERT',            'encode': 'ENCODE',
    'decode': 'DECODE',             'for': 'FOR',
    'between': 'BETWEEN',           'isnull' : 'ISNULL',
    'notnull' : 'NOTNULL',          'case' : 'CASE',
    'end' : 'END',                  'when' : 'WHEN',
    'then' : 'THEN'   ,              'else' : 'ELSE',
    'is' : 'IS',
    'sign': 'SIGN',                 'sqrt': 'SQRT',
    'width_bucket': 'WBUCKET',      'trunc': 'TRUNC',
    'random': 'RANDOM',             'true': 'TRUE',
    'false': 'FALSE',               'use' : 'USE'


}


#### *Simbolos*
    tokens = [
        'DOSPUNTOS',   'COMA',      'PTCOMA',
        'LLAVIZQ',     'LLAVDER',   'PARIZQ',
        'PARDER',      'CORCHIZQ',  'CORCHDER',
        'IGUAL',       'MAS',       'MENOS',
        'ASTERISCO',   'DIVIDIDO',  'EXPONENTE',
        'MENQUE',      'MAYQUE',
        'NIGUALQUE',   'DIFERENTE', 'MODULO',
        'DECIMAL',     'ENTERO',    'CADENADOBLE',
        'CADENASIMPLE', 'ID',        'MENIGUAL',
        'MAYIGUAL',    'PUNTO',     'CADENALIKE',
        'CONCAT', 'BITWAND', 'BITWOR', 'BITWXOR',
        'BITWNOT', 'BITWSHIFTL', 'BITWSHIFTR', 'CSIMPLE'
    ] + list(reservadas.values())


#### *Expresiones regulares, Precedencia de operadores, terminación de analisis léxico*
    t_PUNTO = r'\.'
    t_DOSPUNTOS = r':'
    t_COMA = r','
    t_PTCOMA = r';'
    t_LLAVIZQ = r'{'
    t_LLAVDER = r'}'
    t_PARIZQ = r'\('
    t_PARDER = r'\)'
    t_CORCHIZQ = r'\['
    t_CORCHDER = r'\]'
    t_IGUAL = r'='
    t_MAS = r'\+'
    t_MENOS = r'-'
    t_ASTERISCO = r'\*'
    t_DIVIDIDO = r'/'
    t_EXPONENTE = r'\^'
    t_MENQUE = r'<'
    t_MAYQUE = r'>'
    t_MENIGUAL = r'<='
    t_MAYIGUAL = r'>='
    t_DIFERENTE = r'<>'
    t_MODULO = r'\%'
    t_BITWOR = r'\|'
    t_CONCAT = r'\|\|'
    t_BITWAND = r'&'
    t_BITWXOR = r'\#'
    t_BITWNOT = r'~'
    t_BITWSHIFTL = r'<<'
    t_BITWSHIFTR = r'>>'
    t_CSIMPLE = r'\''

---

    def t_DECIMAL(t):
        r'\d+\.\d+'
        try:
            t.value = float(t.value)
        except ValueError:
            print("Float value too large %d", t.value)
            t.value = 0
        return t

---
    def t_ENTERO(t):
      r'\d+'
      try:
          t.value = int(t.value)
      except ValueError:
          print("Integer value too large %d", t.value)
          t.value = 0
      return t
---
    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reservadas.get(t.value.lower(), 'ID')
        return t
---
#### Cadenas

    def t_CADENADOBLE(t):
        r'\".*?\"'
        t.value = t.value[1:-1]
        return t
---

    def t_CADENALIKE(t):
        r'\'%.*?%\''
        t.value = t.value[1:-1]
        return t
---

    def t_CADENASIMPLE(t):
        r'\'.*?\''
        t.value = t.value[1:-1]
        return t
---
#### Comentarios
    def t_COMENTARIO_MULTILINEA(t):
        r'/\*(.|\n)*?\*/'
        t.lexer.lineno += t.value.count('\n')

    def t_COMENTARIO_SIMPLE(t):
        r'--.*\n'
        t.lexer.lineno += 1
---
#### Caracteres ignorados
    t_ignore = " \t"

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")


    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
---
##### Asociación de operadores y precedencia
      precedence = (

        ('left', 'CONCAT'),
        ('left', 'BITWOR'),
        ('left', 'BITWXOR'),
        ('left', 'BITWAND'),
        ('left', 'BITWSHIFTL', 'BITWSHIFTR'),
        ('left', 'BITWNOT'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'MENQUE', 'MAYQUE', 'MENIGUAL', 'MAYIGUAL', 'IGUAL', 'DIFERENTE'),
        ('left', 'MAS', 'MENOS'),
        ('left', 'ASTERISCO', 'DIVIDIDO', 'MODULO'),
        ('left', 'EXPONENTE'),
        ('right', 'UMENOS')
      )



