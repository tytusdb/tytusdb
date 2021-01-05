# Manual Técnico :blue_book:

### Integrantes
201800634	ANTHONY FERNANDO SON MUX

201801181	CÉSAR EMANUEL GARCIA PÉREZ

201801195	JOSE CARLOS JIMENEZ

201801237	JOSÉ RAFAEL MORENTE GONZÁLEZ

## Contenido
1. [Gramática Ascendente](#id1)
2. [PLY](#id2)
3. [Ejecución Programa](#id3)

### Gramática Ascendente<a name="id1"></a>
```sh
<INICIO> ::= <INSTRUCCIONES>

<INSTRUCCIONES> ::= <INSTRUCCIONES> <INSTRUCCION>
			| <INSTRUCCION>

<INSTRUCCION> ::= <USE>
			| <SHOW>
			| <CREATE>
			| <ALTER>
			| <DROP>
			| <INSERT>
			| <UPDATE>
			| <DELETE>
			| <SELECT>

<USE> ::= USE IDENTIFICADOR;

<SHOW> ::= SHOW DATABASES;

<CREATE> ::= create <TIPO_CREATE> 

<TIPO_CREATE> ::= <REPLACE> DATABASE <IF_EXIST> IDENTIFICADOR <CREATE_OPCIONES> ;
			| TABLE IDENTIFICADOR ( <DEFINICION_COLUMNA> );
			| TYPE IDENTIFICADOR AS ENUM ( <LIST_VLS> );

<REPLACE> ::= OR REPLACE 
			| épsilon

<CREATE_OPCIONES> ::= OWNER = IDENTIFICADOR <CREATE_OPCIONES>
			| MODE = numero <CREATE_OPCIONES>
			| épsilon

<DEFINICION_COLUMNA> ::= <DEFINICION_COLUMNA>, <COLUMNA>
			| <COLUMNA>

<COLUMNA> ::= IDENTIFICADOR <TIPO_DATO> <DEFINICION_VALOR_DEFECTO> <CONSTRAINT> 
            | <PRIMARY_KEY>
            | <FOREIGN_KEY>

<DEFINICION_VALOR_DEFECTO> ::= DEFAULT <TIPO_DEFAULT>
			| épsilon

<CONSTRAINT>::= CONSTRAINT IDENTIFICADOR <RESTRICCION_COLUMNA>
			| <RESTRICCION_COLUMNA>
			| épsilon

<RESTRICCION_COLUMNA> ::= NOT NULL
			| NULL
			| PRIMARY KEY
			| UNIQUE

<PRIMARY_KEY> ::= PRIMARY KEY ( <NOMBRE_COLUMNAS> )

<FOREIGN_KEY> ::= FOREING KEY ( <NOMBRE_COLUMNAS> ) REFERENCES IDENTIFICADOR ( <NOMBRE_COLUMNAS> )

<NOMBRE_COLUMNAS> ::= <NOMBRE_COLUMNAS> , IDENTIFICADOR
            | IDENTIFICADOR

<DROP> ::= DROP <TIPO_DROP>

<ALTER> ::= ALTER <TIPO_ALTER>

<TIPO_ALTER> ::= DATABASE IDENTIFICADOR <ALTER_DATABASE> ;
			| TABLE IDENTIFICADOR <ALTERACION_TABLA> ;

<ALTER_DATABASE> ::= RENAME TO IDENTIFICADOR
			| OWNER TO IDENTIFICADOR

<ALTERACION_TABLA> ::= <ALTERACION_TABLA>,<ALTERAR_TABLA>
			| <ALTERAR_TABLA>

<ALTERAR_TABLA> ::= add column <COLUMNA>
			| alter column <COLUMNA>
			| drop column IDENTIFICADOR 
			| drop constraint IDENTIFICADOR 

<TIPO_DROP> ::= DATABASE <IF_EXIST> IDENTIFICADOR;
			| TABLE IDENTIFICADOR;

<IF_EXIST> ::= IF EXIST
			| épsilon

<INSERT> ::= INSERT INTO IDENTIFICADOR VALUES ( <VALUES> );
			| INSERT INTO IDENTIFICADOR ( <LIST_ID> ) VALUES ( <LIST_VLS> ) PUNTO_COMA

<VALUES> ::= <VALUES> , <VALUE>
			| <VALUE>

<VALUE> ::= CADENA
			| CADENASIMPLE
			| NUMERO
			| NUM_DECIMAL
			| FECHA_HORA
			| TRUE
			| FALSE 
			| NULL
			| F_HORA

<LIST_ID> ::= <LIST_ID> , IDENTIFICADOR
			| IDENTIFICADOR

<LIST_VLS> ::= <LIST_VLS> , <VALUE>
			| <VALUE>

<SELECT> ::= <SELECT> UNION <OPTION_ALL> <SELECT>
			| <SELECT> INTERSECT <OPTION_ALL> <SELECT> 
			| <SELECT> EXCEPT <OPTION_ALL>  <SELECT>;              
			| SELECT <DIST> <T_LIST> FROM <T_EXPRESSION> <WHERE> <GROUPBY> <ORDERBY> <LIMIT> <OFFSET>       

<OPTION_ALL> ::= ALL
		    | EPSILON

<DIST> ::= DISTINCT
		    | EPSILON

<T_LIST> ::= <S_LIST>
			| *

<S_LIST> ::= <S_LIST> , <VAL> <AS>
			|<VAL>

<VAL> ::= IDENTIFICADOR <TABLE>
			| <AGGREGATES>
            | <FUNCTIONS>

<TABLE> ::= IDENTIFICADOR
			| EPSILON

<AS> ::= AS IDENTIFICADOR
			| AS CADENA
            | CADENA
            | EPSILON

<T_EXPRESSION> ::= <T_EXPRESSION> , IDENTIFICADOR
			| IDENTIFICADOR

<WHERE> ::= WHERE <EXP>
			| EPSILON

<LIMIT> ::= LIMIT <OPTION_LIMIT>
			| EPSILON

<OPTION_LIMIT> ::= NUMERO
			| ALL

<OFFSET> ::= OFFSET NUMERO
			| EPSILON

<EXP> ::= <EXP> + <EXP>
			| <EXP> - <EXP>
            | <EXP> * <EXP>
            | <EXP> / <EXP>
            | <EXP> % <EXP>
            | <EXP> ^ <EXP>
            | <EXP> or <EXP>
            | <EXP> AND <EXP>
            | <EXP> < <EXP>
            | <EXP> > <EXP>
            | <EXP> <= <EXP>
            | <EXP> >= <EXP>
			| <EXP> = <EXP>
            | <EXP> <> <EXP>
            | <EXP> != <EXP>
            | <PATTERN>
			| <SUB_CONSULTA>
            | NOT <EXP>
			| <DATA>
			| <PREDICATES>
			| <AGGREGATES>
			| <FUNCTIONS>
			| <PATTERNS>
            | <CASE>
            | <GREATEST>
            | <LEAST>
            | <VALUE>

<GREATEST> ::= GREATEST ( <EXP_LIST> )

<LEAST> ::= LEAST ( <EXP_LIST> )

<EXP_LIST> ::= <EXP_LIST> , <EXP>
			| <EXP>

<CASE> ::= CASE <WHEN> <ELSE> AND
                
<WHEN> ::= <WHEN> WHEN <EXP> THEN <EXP>
	        | WHEN <EXP> THEN <EXP> 

<ELSE> ::= ELSE <EXP>
			| EPSILON
	       
<SUB_CONSULTA> ::= ( <SELECT> )

<DATA> ::=  IDENTIFICADOR <TABLE_AT>

<TABLE_AT> ::= IDENTIFICADOR
			| EPSILON

<PREDICATES> ::= <DATA> BETWEEN <VALUE> AND <VALUE>
			| <DATA> NOT BETWEEN <VALUE> AND <VALUE>
			| <DATA> BETWEEN SYMMETRIC <VALUE> AND <VALUE>
			| <DATA> NOT BETWEEN SYMMETRIC <VALUE> AND <VALUE>
			| <DATA> IS distinct from <VALUE>
			| <DATA> IS NOT distinct from <VALUE>
			| <DATA> IS NULL
			| <DATA> IS NOT NULL
			| <DATA> ISNULL
			| <DATA> NOTNULL
			| <DATA> IS TRUE
			| <DATA> IS NOT TRUE
			| <DATA> IS FALSE
			| <DATA> IS NOT FALSE
			| <DATA> IS UNKNOW
			| <DATA> IS NOT UNKNOW

<AGGREGATES> ::= COUNT ( <APARAM> ) 
			| SUM ( <APARAM> )
			| AVG ( <APARAM> )
			| MAX ( <APARAM> )
			| MIN ( <APARAM> )

<APARAM> ::= IDENTIFICADOR
			| *

<FUNCTIONS>::= <MATH>
			| <TRIG>
			| <STRING_FUNC>
			| <TFUNC>

<MATH> ::= AVG ( NUMERO ) 
			| CBRT ( NUMERO ) 
			| CEIL ( NUMERO )  
			| CEILING ( NUMERO ) 
			| DEGREES ( NUMERO ) 
			| DIV ( NUMERO, NUMERO ) 
			| EXP ( NUMERO ) 
			| FACTORIAL ( NUMERO ) 
			| FLOOR ( NUMERO ) 
			| GCD ( NUMERO, NUMERO ) 
			| LN ( NUMERO ) 
			| LOG ( NUMERO ) 
			| MOD ( NUMERO, NUMERO ) 
			| PI ( ) 
			| POWER ( NUMERO, NUMERO ) 
			| ROUND ( NUMERO )

<TRIG> ::= ACOS ( NUMERO )
			| ACOSD (NUMERO )
			| ASIN ( NUMERO )
			| ASIND ( NUMERO )
			| ATAN ( NUMERO )
			| ATAND ( NUMERO )
			| ATAN2 ( NUMERO, NUMERO )
			| ATAN2D ( NUMERO, NUMERO )
			| COS ( NUMERO )
			| COSD ( NUMERO )
			| COT ( NUMERO )
			| COTD (NUMERO )
			| SIN ( NUMERO )
			| SIND ( NUMERO )
			| TAN ( NUMERO )
			| TAND ( NUMERO )
			| SINH ( NUMERO )
			| COSH ( NUMERO )
			| TANH ( NUMERO )
			| ASINH ( NUMERO )
			| ACOSH ( NUMERO )
			| ATANH ( NUMERO )

<STRING_FUNC> ::= LENGTH ( <SPARAM> )
			| SUBSTRING ( <SPARAM>, NUMERO, NUMERO )
			| SUBSTRING ( <SPARAM>, <SPARAM> , STRING )
			| TRIM ( <SPARAM> )
			| GET_BYTE ( <SPARAM>, NUMERO)
			| MD5 ( <SPARAM> )	
			| SET_BYTE ( <SPARAM>, NUMERO , NUMERO)
			| SHA256 ( <SPARAM> )
			| SUBSTR ( <SPARAM>, NUMERO, NUMERO )
			| CONVERT ( <TIPO_DATO> , <DATA> )
			| ENCODE ( <SPARAM>, <SPARAM> )
			| DECODE ( <SPARAM>, <SPARAM>)

<SPARAM> ::= <SPARAM> <STRINGOP> STRING
			| STRING

<STRINGOP> ::= ||
			| &
			| |
			| #
			| ~
			| >>
			| <<

<PATTERN> ::= <DATA> LIKE STRING
			| <DATA> NOT LIKE STRING

<TFUNC> ::= DATE_PART ( ' <H_M_S> ', INTERVAL F_TIEMPO)	
			| NOW ( )
			| EXTRACT ( <RESERV_TIME> FROM TIMESTAMP DATE )	
			| CURRENT_TIME
			| CURRENT_DATE
			| TIMESTAMP COMILLA NOW COMILLA

<RESERV_TIME> ::= <H_M_S>
			| YEAR
			| MONTH
			| DAY

 <H_M_S> ::= HOUR
			| MINUTE
			| SECOND

<GROUPBY> ::= GROUP BY <GLIST>
			| EPSILON

<GLIST> ::= <GLIST> , <GITEM>
			| <GITEM>

<GITEM> ::= IDENTIFICADOR <G_REFITEM>

<G_REFITEM> ::= IDENTIFICADOR
			| EPSILON

<ORDERBY> ::= ORDER BY <OLIST>
			| EPSILON

<OLIST> ::= <OLIST> , <OITEM>
			| <OITEM>

<OITEM> ::= ID <O_REFITEM> <AD> <NULLS>

<O_REFITEM>	::=  ID
			| EPSILON

<AD> ::= ASC
			| DESC
			| EPSILON

<NULLS> ::= NULLS <FL>
			| EPSILON

<FL> ::= FIRST
			| LAST

<UPDATE> ::= UPDATE ID SET <ASIGN_LIST> WHERE <EXP> ;

<ASIGN_LIST> ::= <ASIGN_LIST> , ID = <VALUE>                           
			| ID = <VALUE>
                         
<DELETE> ::= DELETE FROM ID WHERE <EXP> ;

```

### PLY<a name="id2"></a>
PLY es una implementación de las herramientas de análisis lex y yacc para Python.

#### Características
  - Está implementado completamente en Python.
  - Utiliza el análisis sintáctico LR que es razonablemente eficiente y muy adecuado para gramáticas más extensas.
  - PLY proporciona la mayoría de las características estándar de lex / yacc, incluido el soporte para producciones vacías, reglas de precedencia, recuperación de errores y soporte para gramáticas ambiguas.
  - PLY es fácil de usar y proporciona una comprobación de errores muy extensa.
  - PLY no intenta hacer nada más o menos que proporcionar la funcionalidad básica de lex / yacc. En otras palabras, no es un gran marco de análisis o un componente de algún sistema más grande.

### Ejecución Programa<a name="id3"></a>

Para ejecutar el programa de python, debes de seguir los siguientes pasos:

```sh
$ cd G-27
$ python inicio.py
```

### Librerías usadas<a name="id3"></a>

Si quieres ejecutar el programa en python, debes asegurarte que tengas instaladas las siguientes librerías, utilizando el comando.

```sh
$ pip install <NAME-PACKAGE>
```
#### PrettyTable

El objetivo principal de PrettyTable es permitirle imprimir tablas en un atractivo formato ASCII.

```sh
$ pip install prettytable
```

#### Pandas

Pandas es un paquete de Python que proporciona estructuras de datos rápidas, flexibles y expresivas diseñadas para que el trabajo con datos estructurados y de series de tiempo sea fácil e intuitivo.

```sh
$ pip install pandas
```