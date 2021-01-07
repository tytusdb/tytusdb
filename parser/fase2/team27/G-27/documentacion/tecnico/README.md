# Manual Técnico Fase 2 :blue_book:

### Integrantes
201800634	ANTHONY FERNANDO SON MUX

201801181	CÉSAR EMANUEL GARCIA PÉREZ

201801195	JOSE CARLOS JIMENEZ

201801237	JOSÉ RAFAEL MORENTE GONZÁLEZ

## Contenido
1. [Gramática Ascendente](#id1)
2. [PLY](#id2)
2. [Optimizacion de Código Intermedio](#id3)
3. [Ejecución Programa](#id4)
4. [Librerías Utilizadas](#id5)

### Gramática Ascendente<a name="id1"></a>
#### GRAMÁTICA DE INSTRUCCIONES
~~~
<INICIO> ::= <INSTRUCCIONES>

<INSTRUCCIONES> ::= <INSTRUCCIONES> <INSTRUCCION> 
                | <INSTRUCCION>

<INSTRUCCION> ::=  <INS_USE>
                | <INS_SHOW>
                | <INS_ALTER>
                | <INS_DROP>
                | <INS_CREATE>
                | <INS_INSERT>
                | <INS_SELECT>
                | <INS_UPDATE>
                | <INS_DELETE>
                | <EXECUTE>
                | <INS_CREATE_PL>
                | <DROP_INDEX>
                | <ALTER_INDEX>
~~~

#### GRAMÁTICA DE INSTRUCCION DE USE
~~~
<INS_USE> ::= USE ID ';'
~~~
#### GRAMÁTICA DE INSTRUCCION SHOW DATABSE
~~~
<INS_SHOW> ::= SHOW DATABASES ';'
~~~

#### GRAMÁTICA DE INSTRUCCIONES ALTER DATABASE Y ALTER TABLE
~~~
<INS_ALTER> ::= ALTER <TIPO_ALTER>

<TIPO_ALTER> ::= DATABASE ID <ALTER_DATABASE> ';'
                | TABLE ID <ALTERACION_TABLA> ';'

<ALTER_DATABASE> ::= RENAME TO ID
                | OWNER TO ID

<ALTERACION_TABLA> ::= <ALTERACION_TABLA> ',' <ALTERAR_TABLA>
                | <ALTERAR_TABLA>

<ALTERAR_TABLA> ::= ADD COLUMN <COLUMNA>
                | ADD CONSTRAINT ID <COLUMNA>
                | ALTER COLUMN <COLUMNA>
                | DROP COLUMN ID
                | DROP CONSTRAINT ID
~~~

#### GRAMÁTICA DE INSTRUCCIONES DROP  DATABASE Y DROP TABLE 
~~~
<INS_DROP> ::= DROP <TIPO_DROP>

<TIPO_DROP> ::= DATABASE <IF_EXISTS> ID ';'
                | TABLE ID ';'
~~~

#### GRAMÁTICA DE INSTRUCCIONES CREATE  DATABASE Y CREATE TABLE
~~~
<INS_CREATE> ::= CREATE <TIPO_CREATE>

<TIPO_CREATE> ::= <INS_REPLACE> DATABASE <IF_EXISTS> ID <CREATE_OPCIONES> ';'
                | TABLE ID '(' <DEFINICION_COLUMNA> ')' <INS_INHERITS> ';'

<CREATE_OPCIONES> ::= OWNER SIGNO_IGUAL USER_NAME <CREATE_OPCIONES>
                | MODE SIGNO_IGUAL NUMERO <CREATE_OPCIONES>
                | EPSILON

<TIPO_DEFAULT> ::= NUMERIC
                | DECIMAL
                | NULL

<INS_CONSTRAINT>
                | ID <DEFINICION_VALOR_DEFECTO> <INS_CONSTRAINT>
                | ID TYPE <TIPO_DATO> <DEFINICION_VALOR_DEFECTO> <INS_CONSTRAINT>
                | <PRIMARY_KEY> 
                | <FOREIGN_KEY>

<PRIMARY_KEY> ::= PRIMARY KEY '(' <NOMBRE_COLUMNAS> ')' <INS_REFERENCES>

<FOREIGN_KEY> ::= FOREIGN KEY '(' <NOMBRE_COLUMNAS> ')' REFERENCES ID '(' <NOMBRE_COLUMNAS> ')' <INS_REFERENCES>

<NOMBRE_COLUMNAS> ::= <NOMBRE_COLUMNAS> ',' ID 
                | ID 

<INS_REFERENCES> ::= ON DELETE ACCION <INS_REFERENCES>
                | ON UPDATE ACCION <INS_REFERENCES>
                | EPSILON

<DEFINICION_COLUMNA> ::= <DEFINICION_COLUMNA> ',' <COLUMNA> 
                | <COLUMNA> 
                     
<INS_INHERITS> ::= INHERITS '(' ID ')'
                |  EPSILON

<INS_REPLACE> ::= OR REPLACE
                | EPSILON
               
<IF_EXISTS> ::=  IF NOT EXISTS
                |  IF EXISTS
                |   EPSILON
~~~

#### GRAMÁTICA DE INSTRUCCIONES INSERT
~~~
<INS_INSERT> ::= INSERT INTO ID VALUES '(' <LIST_VLS> ')' ';'
~~~

#### DEFINICIÓN DE INSTRUCCIONES SELECT
~~~
<INS_SELECT> ::= <INS_SELECT> UNION <OPTION_ALL> <INS_SELECT> ';'
                |    <INS_SELECT> INTERSECT <OPTION_ALL> <INS_SELECT> ';'
                |    <INS_SELECT> EXCEPT <OPTION_ALL> <INS_SELECT> ';'
                |    SELECT <ARG_DISTICT> <COLUM_LIST> FROM <TABLE_LIST> <ARG_WHERE> <ARG_GROUP_BY> <ARG_ORDER_BY> <ARG_LIMIT> <ARG_OFFSET> ';'

<OPTION_ALL>   ::= ALL
                | EPSILON

<ARG_DISTICT> ::= DISTINCT
                | EPSILON

<COLUM_LIST>   ::=   <S_LIST>
                |   SIGNO_POR

<S_LIST>   ::=   <S_LIST> ',' <COLUMNS> <AS_ID>
                |   <COLUMNS> <AS_ID>

<AS_ID> ::=   AS ID
                |   AS CADENA
                |   CADENA
                |   EPSILON

<COLUMNS>   ::= ID DOT_TABLE
                |   <AGGREGATES>
                |   <FUNCTIONS>

<TABLE_LIST>   ::=   <TABLE_LIST> ',' ID <AS_ID>
                |   ID <AS_ID>

<ARG_WHERE> ::=   WHERE <EXP>
                |  EPSILON

<ARG_GROUP_BY>  ::=   GROUP BY <G_LIST>
                |  EPSILON

<G_LIST> ::= <G_LIST> ',' <G_ITEM>
                | <G_ITEM> 

<G_ITEM> ::= ID <G_REFITEM>

<G_REFITEM>  ::= PUNTO ID
                | EPSILON

<ARG_ORDER_BY> ::=   ORDER BY <O_LIST>
                |  EPSILON

<O_LIST> ::= <O_LIST> ',' <O_ITEM>
                | <O_ITEM> 

<O_ITEM> ::= ID <O_REFITEM> <AD> <ARG_NULLS>

<O_REFITEM>  ::= PUNTO ID
                | EPSILON

<AD> ::= ASC
                | DESC
                | EPSILON

<ARG_NULLS> ::= NULLS <ARG_FL>
                | EPSILON

<ARG_FL> ::= FIRST
                | LAST

<ARG_LIMIT>   ::=  LIMIT <OPTION_LIMIT>
                |  EPSILON

<OPTION_LIMIT>   ::= NUMERO
                | ALL 

ARG_OFFSET   ::= OFFSET NUMERO 
                |  EPSILON
~~~

#### DEFINICIÓN DE INSTRUCCIONES UPDATES
~~~
<INS_UPDATE>   ::= UPDATE ID SET <ASIGN_LIST> WHERE <EXP> ';'

<ASIGN_LIST>  ::= <ASIGN_LIST> ',' ID SIGNO_IGUAL <VAL_VALUE> 
                | ID SIGNO_IGUAL <VAL_VALUE>

<VAL_VALUE> ::= CADENA
                |   CADENASIMPLE
                |   NUMERO
                |   NUM_DECIMAL
                |   FECHA_HORA
                |   TRUE
                |   FALSE 
                |   NULL
                |   F_HORA
~~~

#### DEFINICIÓN DE INSTRUCCIONES DELETE
~~~
<INS_DELETE>   ::= DELETE FROM ID WHERE <EXP> ';'
~~~

#### DEFINICIÓN DE TIPO DE DATO
~~~
<TIPO_DATO> ::= SMALLINT          
                | BIGINT
                | NUMERIC
                | DECIMAL
                | INTEGER
                | REAL
                | DOUBLE PRECISION
                | CHAR '(' NUMERO ')'
                | VARCHAR '(' NUMERO ')'
                | CHARACTER '(' NUMERO ')'
                | TEXT
                | TIMESTAMP <ARG_PRECISION>
                | TIME <ARG_PRECISION>
                | DATE
                | INTERVAL <ARG_TIPO> <ARG_PRECISION>
                | BOOLEAN
                | MONEY

<ARG_PRECISION> ::= '(' NUMERO ')' 
                | EPSILON

<ARG_TIPO> ::= MONTH
                | YEAR
                | HOUR
                | MINUTE
                | SECOND
                | EPSILON
~~~

#### DEFINICIÓN DE COLUMNAS EN TABLAS
~~~
<DEFINICION_COLUMNA> ::= <DEFINICION_COLUMNA> ',' <COLUMNA> 
                | <COLUMNA>
<COLUMNA> ::= ID <TIPO_DATO> <DEFINICION_VALOR_DEFECTO> 

<DEFINICION_VALOR_DEFECTO> ::= DEFAULT <TIPO_DEFAULT> 
                | EPSILON
~~~

#### DEFINICIÓN DE EXPRESIONES
~~~
<EXP_LIST>  ::= <EXP_LIST> ',' <EXP>
                | <EXP>

<EXP>  ::= <EXP> SIGNO_MAS <EXP>
                | <EXP> SIGNO_MENOS <EXP> 
                | <EXP> SIGNO_POR <EXP> 
                | <EXP> SIGNO_DIVISION <EXP> 
                | <EXP> SIGNO_MODULO <EXP> 
                | <EXP> SIGNO_POTENCIA <EXP> 
                | <EXP> OR <EXP> 
                | <EXP> AND <EXP> 
                | <EXP> MENORQUE <EXP> 
                | <EXP> MAYORQUE <EXP> 
                | <EXP> MAYORIGUALQUE <EXP> 
                | <EXP> MENORIGUALQUE <EXP> 
                | <EXP> SIGNO_IGUAL <EXP>
                | <EXP> SIGNO_MENORQUE_MAYORQUE <EXP>
                | <EXP> SIGNO_NOT <EXP> 
                | <ARG_PATTERN>
                | <SUB_CONSULTA>
                | NOT <EXP>
                | <DATA>
                | <PREDICATES>
                | <AGGREGATES>
                | <FUNCTIONS>
                | <ARG_CASE>
                | <ARG_GREATEST>
                | <ARG_LEAST> 
                | <VAL_VALUE>

<ARG_PATTERN>   ::= <DATA> LIKE CADENA   
                | <DATA> NOT LIKE CADENA

<DATA>  ::= ID <TABLE_AT>

<TABLE_AT>  ::= PUNTO ID
                | EPSILON

<SUB_CONSULTA>   ::= '(' <INS_SELECT>  ')'

<ARG_CASE>  ::= CASE <ARG_WHEN> <ARG_ELSE> END

<ARG_ELSE> ::=  ELSE <EXP>
                | EPSILON

<ARG_WHEN>  ::= <ARG_WHEN> WHEN <EXP> THEN <EXP>
                | WHEN <EXP> THEN <EXP>

<ARG_GREATEST>  ::= GREATEST '(' <EXP_LIST> ')'

<ARG_LEAST>  ::= LEAST '(' <EXP_LIST> PARCIERR
~~~

#### DECLARACIÓN DE PREDICADOS
~~~
<PREDICATES>  ::=  BETWEEN <LIST_VLS> AND <LIST_VLS>
                | <DATA> NOT BETWEEN <LIST_VLS> AND <LIST_VLS>
                | <DATA> BETWEEN SYMMETRIC <LIST_VLS> AND <LIST_VLS> 
                | <DATA> NOT BETWEEN SYMMETRIC <LIST_VLS> AND <LIST_VLS>
                | <DATA> IS DISTINCT FROM <LIST_VLS>
                | <DATA> IS NOT DISTINCT FROM <LIST_VLS>
                | <DATA> IS NULL 
                | <DATA> ISNULL
                | <DATA> NOTNULL
                | <DATA> IS TRUE
                | <DATA> IS NOT TRUE
                | <DATA> IS FALSE
                | <DATA> IS NOT FALSE
                | <DATA> IS UNKNOWN
                | <DATA> IS NOT UNKNOWN

<LIST_VLS> ::= <LIST_VLS> ',' <VAL_VALUE>
                | <VAL_VALUE> 

<VAL_VALUE> ::= CADENA
                |   CADENASIMPLE
                |   NUMERO
                |   NUM_DECIMAL
                |   FECHA_HORA
                |   TRUE
                |   FALSE 
                |   NULL
                |   F_HORA
~~~

#### DECLARACIÓN DE FUNCIONES DE AGREGACIÓN
~~~
<AGGREGATES>   ::=   COUNT '(' <PARAM> ')'
                |   SUM '(' <PARAM> ')'
                |   AVG '(' <PARAM> ')'
                |   MAX '(' <PARAM> ')'
                |   MIN '(' <PARAM> ')'

<PARAM> ::=   ID <DOT_TABLE>
                |   SIGNO_POR
~~~

#### DECLARACION DE FUNCIONES  
~~~
<FUNCTIONS>  ::=   <MATH>
                |   <TRIG>
                |   <STRING_FUNC>
                |   <TIME_FUNC>

<MATH> ::=   AVG '(' NUMERO ')'
                |   CBRT '(' NUMERO ')'
                |   CEIL '(' NUMERO ')'
                |   CEILING '(' NUMERO ')'
                |   DEGREES '(' NUMERO ')'
                |   DIV '(' NUMERO ',' NUMERO ')'
                |   EXP '(' NUMERO ')'
                |   FACTORIAL '(' NUMERO ')'
                |   FLOOR '(' NUMERO ')'
                |   GCD '(' NUMERO ',' NUMERO ')'
                |   IN '(' NUMERO ')'
                |   LOG '(' NUMERO ')'
                |   MOD '(' NUMERO ',' NUMERO ')'
                |   PI '('  ')'
                |   POWER '(' NUMERO ',' NUMERO ')' 
                |   ROUND '(' NUMERO ')'

<TRIG> ::=   ACOS '(' NUMERO ')'
                |   ACOSD '(' NUMERO ')'
                |   ASIN '(' NUMERO ')'
                |   ASIND '(' NUMERO ')'
                |   ATAN '(' NUMERO ')'
                |   ATAND '(' NUMERO ')'
                |   ATAN2 '(' NUMERO ',' NUMERO ')'
                |   ATAN2D '(' NUMERO ',' NUMERO ')'
                |   COS '(' NUMERO ')'
                |   COSD '(' NUMERO ')'
                |   COT '(' NUMERO ')'
                |   COTD '(' NUMERO ')'
                |   SIN '(' NUMERO ')'
                |   SIND '(' NUMERO ')'
                |   TAN '(' NUMERO ')'
                |   TAND '(' NUMERO ')'
                |   SINH '(' NUMERO ')'
                |   COSH '(' NUMERO ')'
                |   TANH '(' NUMERO ')'
                |   ASINH '(' NUMERO ')'
                |   ACOSH '(' NUMERO ')'
                |   ATANH '(' NUMERO ')'  

<STRING_FUNC>  ::=   LENGTH '(' <S_PARAM> ')'
                |   SUBSTRING '(' <S_PARAM> ',' NUMERO ',' NUMERO ')'
                |   SUBSTRING '(' <S_PARAM> ',' <S_PARAM> ',' CADENA ')'
                |   TRIM '(' <S_PARAM> ')'
                |   GET_BYTE '(' <S_PARAM> ',' NUMERO ')'
                |   MOD5 '(' <S_PARAM> ')'
                |   SET_BYTE '(' ',' NUMERO ',' NUMERO <S_PARAM> ')'
                |   SHA256 '(' <S_PARAM> ')'
                |   SUBSTR '(' <S_PARAM> ',' NUMERO ',' NUMERO ')'
                |   CONVERT '(' TIPO_DATO ',' ID DOT_TABLE ')'
                |   ENCODE '(' <S_PARAM> ',' <S_PARAM> ')'
                |   DECODE '(' <S_PARAM> ',' <S_PARAM> ')'

<S_PARAM>  ::=   <S_PARAM> <STRING_OP> CADENA
                |   CADENA 

<STRING_OP> ::=   SIGNO_PIPE
                |   SIGNO_DOBLE_PIPE
                |   SIGNO_AND
                |   SIGNO_VIRGULILLA
                |   SIGNO_NUMERAL
                |   SIGNO_DOBLE_MENORQUE
                |   SIGNO_DOBLE_MAYORQUE

<TIME_FUNC> ::=   DATE_PART '(' COMILLA <H_M_S> COMILLA ',' INTERVAL F_HORA ')' 
                |   NOW '(' ')'
                |   EXTRACT '(' <RESERV_TIME>  FROM TIMESTAMP  ')'
                |   CURRENT_TIME
                |   CURRENT_DATE

<RESERV_TIME>  ::=   <H_M_S> 
                |   YEAR
                |   MONTH
                |   DAY

<H_M_S> ::=   HOUR
                |   MINUTE
                |   SECOND
~~~

#### INSTRUCCIONES PL/PSQL
~~~
    <INS_CREATE_PL> ::= CREATE <OP_REPLACE> FUNCTION ID '('() <PARAMETERS> ')' <RETURNS> AS  <BLOCK> LANGUAGE ID ';'
                | CREATE <OP_REPLACE> PROCEDURE ID '('() <PARAMETERS> ')'() AS  <BLOCK> LANGUAGE ID ';'

    <OP_REPLACE> ::=  OR REPLACE
                |
    
    <PARAMETERS> ::= <PARAMETERS> ',' <PARAMETER>
                | <PARAMETER>
                |
                
    <PARAMETER> ::= ID <TIPO_DATO>
                | ID ANYELEMENT
                | ID ANYCOMPATIBLE
                | OUT ID TIPO_DATO
                | ID
                | <TIPO_DATO>
                
    <RETURNS> ::= RETURNS <EXP>
                | RETURNS ANYELEMENT
                | RETURNS TABLE '(' PARAMETERS ')' 
                | RETURNS ANYCOMPATIBLE
                | RETURNS <TIPO_DATO>
                | RETURNS VOID
            
    <BLOCK> ::= DOLAR_LABEL  <BODY> ';' DOLAR_LABEL
    
    <BODY> ::=  <DECLARE_STATEMENT> BEGIN <INTERNAL_BLOCK> END
    
    <DECLARE_STATEMENT> ::= <DECLARE_STATEMENT> DECLARE <STATEMENTS>
                | DECLARE <STATEMENTS>
                | 

    <DECLARACION>  ::= ID <CONSTANTE> <TIPO_DATO> <NOT_NULL> <DECLARACION_DEFAULT> ';'
    
    <INTERNAL_BLOCK> ::= <INTERNAL_BLOCK> <INTERNAL_BODY> 
                | <INTERNAL_BODY> 
                | 
    
    <INTERNAL_BODY> ::= <BODY> ';'
                | <INSTRUCCION_IF>
                | <INSTRUCCION_CASE>
                | <RETURN>
                | <STATEMENTS>
    
    <CONSTANTE>  ::= CONSTANT
                | EPSILON
    
    <NOT_NULL>  ::= NOT NULL 
                | EPSILON
    
    <DECLARACION_DEFAULT>  ::= DEFAULT <EXP>
                | SIGNO_IGUAL <EXP>
                | DOSPUNTOS SIGNO_IGUAL  <EXP>
                | EPSILON
    
    <DECLARACION_FUNCION> ::= ID ALIAS FOR DOLAR NUMERO ';'
                | ID ALIAS FOR ID ';'
    
    <DECLARACION_COPY> ::= ID ID PUNTO ID SIGNO_MODULO TYPE ';'
    
    <DECLARACION_ROW> ::= ID ID SIGNO_MODULO ROWTYPE ';'
    
    <DECLARACION_RECORD> ::= ID RECORD ';'
    
    <ASIGNACION> ::= ID <REFERENCIA_ID> SIGNO_IGUAL <EXP> ';'
                | ID <REFERENCIA_ID> SIGNO_IGUAL <INS_SELECT_PARENTESIS> ';'
                | ID <REFERENCIA_ID> SIGNO_IGUAL '(' <INS_SELECT_PARENTESIS> ')' ';'
                | ID <REFERENCIA_ID> DOSPUNTOS SIGNO_IGUAL <EXP> ';'
                | ID <REFERENCIA_ID> DOSPUNTOS SIGNO_IGUAL <INS_SELECT_PARENTESIS> ';'
                | ID <REFERENCIA_ID> DOSPUNTOS SIGNO_IGUAL '(' <INS_SELECT_PARENTESIS> ')' ';'
    
    <REFERENCIA_ID> ::= PUNTO ID
                | EPSILON
                
    <RETURN> ::= RETURN <EXP> ';'
                | RETURN NEXT <EXP> ';'
                | RETURN QUERY <QUERY>
    
    <QUERY> ::= <INS_INSERT>
                | <INS_SELECT>
                | <INS_UPDATE>
                | <INS_DELETE>
                
    <INSTRUCCION_IF> ::= IF <EXP> <THEN> <ELSE_IF> <ELSE> END IF ';'
    
    <THEN> ::= THEN <STATEMENTS>
    
    <ELSE_IF> ::= <ELSE_IF> <INSTRUCCION_ELSE>
                | <INSTRUCCION_ELSE>
                | EPSILON
    
    <INSTRUCCION_ELSE> ::= ELSIF <EXP> <THEN>
    
    <ELSE> ::= ELSE <SENTENCIA>
                | EPSILON
    
    <SENTENCIA> ::= <STATEMENTS>
    
    <INSTRUCCION_CASE> ::= CASE <EXP> <CASES> <ELSE> END CASE ';'
    
    <CASES> ::= <CASES> <INSTRUCCION_CASE_ONLY>
                | <INSTRUCCION_CASE_ONLY>
                | EPSILON
    
    <INSTRUCCION_CASE_ONLY> ::= WHEN <EXP> <THEN>
    
    <LISTA_EXP> ::= <LISTA_EXP> ',' <EXP>
                | <EXP>
    
    <STATEMENTS> ::= <STATEMENTS> <STATEMENT>
                | <STATEMENT>
    
    <STATEMENT> : <ASIGNACION>
                | <PERFORM>
                | <F_QUERY> 
                | <EXECUTE>
                | <NULL>
                | <DECLARACION>
                | <DECLARACION_FUNCION>
                | <DECLARACION_COPY>
                | <DECLARACION_ROW>
                | <DECLARACION_RECORD>
                | <INSTRUCCION_IF>
                | <INSTRUCCION_CASE>
                | <RETURN>
    
    <PERFORM> ::= PERFORM <INSTRUCCION>
    
    <F_QUERY> ::= SELECT <ARG_DISTICT> <COLUM_LIST> <INTO> FROM <TABLE_LIST> <ARG_WHERE> <ARG_GROUP_BY> <ARG_ORDER_BY> <ARG_LIMIT> <ARG_OFFSET> ';'
                | <INS_INSERT> <F_RETURN>
                | <INS_UPDATE> <F_RETURN>
                | <INS_DELETE> <F_RETURN>
    
    <F_RETURN> ::= RETURNING <EXP> <INTO> 
                |
    
    <INTO> ::= INTO ID
                | INTO STRICT ID
    
    <EXECUTE> ::= EXECUTE CADENA <INTO> USING <EXP_LIST> ';'
                | EXECUTE CADENASIMPLE <INTO> USING <EXP_LIST> ';'
                | EXECUTE <EXP> ';'
    
    <NULL> ::= NULL ';'
~~~

#### INSTRUCCIONES INDICES
~~~
    <CREATE_INDEX> ::= CREATE <ARG_UNIQUE> INDEX ID ON ID <ARG_HASH> '(' <PARAM_INDEX> ')' <ARG_INCLUDE> <ARG_WHERE_INDEX> <ARG_PUNTO_COMA>
    
    <ARG_INCLUDE> ::= INCLUDE '(' INDEX_STR ')'
                | EPSILON
                   
    <PARAM_INDEX> ::= <ID_LIST> <ARG_ORDER> <ARG_NULL>
                | '(' <CONCAT_LIST> ')'
                | ID ID 
                | ID COLLATE <TIPO_CADENA>
             
    <TIPO_CADENA> ::= CADENA
                | CADENASIMPLE

    <CONCAT_LIST> ::= <CONCAT_LIST> SIGNO_DOBLE_PIPE <INDEX_STR>
                | <INDEX_STR>
  
    <INDEX_STR> ::= ID
                | ID '(' ID ')'
                | CADENA
                | CADENASIMPLE
    
    <ARG_HASH> ::= USING HASH
                |
    
    <ID_LIST> ::= <ID_LIST> ',' <INDEX>
                | <INDEX>
    
    <INDEX> ::= ID '(' ID ')'
                | ID
    
    <ARG_PUNTO_COMA> ::= ';'
                |

    <ARG_UNIQUE> ::= UNIQUE
                |

    <ARG_ORDER> ::= ASC 
                | DESC
                |
    
    <ARG_NULL> ::=  NULLS FIRST
                | NULLS LAST
                |
    
    <ARG_WHERE_INDEX> ::= WHERE <ARG_WHERE_PARAM> 
                |

    <ARG_WHERE_PARAM> ::= '(' <EXP> ')'
                | <EXP>

    <DROP_INDEX> ::= DROP INDEX ID <ARG_PUNTO_COMA>

    <ALTER_INDEX> ::= ALTER INDEX ID ID <ARGCOL> <ARG_PUNTO_COMA>

    <ARGCOL> ::= ID
                | NUMERO
~~~

#### ELIMINACION PROCEDIMIENTOS, FUNCIONES E INDICES
~~~
<DROP_PF> : DROP <DROP_CASE> <OPT_EXIST> ID '(' <ARG_LIST_OPT> ')' ';'

<DROP_CASE> : FUNCTION
                | PROCEDURE

<OPT_EXIST> : IF EXIST
                |

<ARG_LIST_OPT> : <ARG_LIST>
                |

<ARG_LIST> : <ARG_LIST> COMA ID
                | ID

<DROP_INDEX> : DROP INDEX ID <ARG_PUNTO_COMA>
~~~

### PLY<a name="id2"></a>
PLY es una implementación de las herramientas de análisis lex y yacc para Python.

#### Características
  - Está implementado completamente en Python.
  - Utiliza el análisis sintáctico LR que es razonablemente eficiente y muy adecuado para gramáticas más extensas.
  - PLY proporciona la mayoría de las características estándar de lex / yacc, incluido el soporte para producciones vacías, reglas de precedencia, recuperación de errores y soporte para gramáticas ambiguas.
  - PLY es fácil de usar y proporciona una comprobación de errores muy extensa.
  - PLY no intenta hacer nada más o menos que proporcionar la funcionalidad básica de lex / yacc. En otras palabras, no es un gran marco de análisis o un componente de algún sistema más grande.

### Optimizacion de Código Intermedio<a name="id3"></a>

Para el proyecto Tytus, el proceso de optimización ha utilizar será el método conocido como mirilla.

Los tipos de transformación para realizar la optimización por mirilla serán los siguientes:
  - Eliminación de instrucciones redundantes de carga y almacenamiento.
  - Eliminación de código inalcanzable.
  - Optimizaciones de Flujo de control.
  - Simplificación algebraica y reducción por fuerza.

#### Regla No. 1
Si existe una asignación de valor de la forma a = b y posteriormente existe una asignación de
forma b = a, se eliminará la segunda asignación siempre que a no haya cambiado su valor. Se
deberá tener la seguridad de que no exista el cambio de valor y no existan etiquetas entre las 2
asignaciones:

```
ENTRADA: 
t2 = b;
b = t2;

SALIDA:
t2 = b
```

#### Regla No. 2
Si existe un salto condicional de la forma Lx y exista una etiqueta Lx:, todo código contenido
entre el goto Lx y la etiqueta Lx, podrá ser eliminado siempre y cuando no exista una etiqueta
en dicho código.

```
ENTRADA: 
goto L1;
<instrucciones>
L1:

SALIDA:
L1:
```

#### Regla No. 3
Si existe un alto condicional de la forma if <cond> goto Lv; goto Lf; inmediatamente después de
sus etiquetas Lv: <instrucciones> Lf: se podrá reducir el número de saltos negando la
condición, cambiando el salto condicional hacia la etiqueta falsa Lf: y eliminando el salto
condicional innecesario a goto Lf y quitando la etiqueta Lv:.

```
ENTRADA: 
if a == 10 goto L1;
goto L2;
L1:
<instrucciones>
L2:

SALIDA:
if a != 10 goto L2;
<instrucciones>
L2:
```

#### Regla No. 4
Si se utilizan valores constantes dentro de las condiciones de la forma if <cond> goto Lv; goto
Lf; y el resultado de la condición es una constante verdadera, se podrá transformar en un salto
incondicional y eliminarse el salto hacia la etiqueta falsa Lf.

```
ENTRADA: 
if 1 == 1 goto L1;
goto L2;

SALIDA:
goto L1;
```

#### Regla No. 5
Si se utilizan valores constantes dentro de las condiciones de la forma if <cond> goto Lv; goto
Lf; y el resultado de la condición es una constante falsa, se podrá transformar en un salto
incondicional y eliminarse el salto hacia la etiqueta verdadera Lv.

```
ENTRADA: 
if 1 == 0 goto L1;
goto L2;

SALIDA:
goto L2;
```

#### Regla No. 6
Si existe un salto incondicional de la forma goto Lx donde existe la etiqueta Lx: y la primera
instrucción, luego de la etiqueta, es otro salto, de la forma goto Ly; se podrá realizar la
modificación al primer salto para que sea dirigido hacia la etiqueta Ly: , para omitir el salto
condicional hacia Lx.

```
ENTRADA: 
goto L1;
<instrucciones>
L1:
goto L2;

SALIDA:
goto L2;
<instrucciones>
L1:
goto L2;
```

#### Regla No. 7
Si existe un salto incondicional de la forma if <cond> goto Lx; y existe la etiqueta Lx: y la
primera instrucciones luego de la etiqueta es otro salto, de la forma goto Ly; se podrá realizar la
modificación al primer salto para que sea dirigido hacia la etiqueta Ly: , para omitir el salto
condicional hacia Lx

```
ENTRADA: 
if t9 >= t10 goto L1;
<instrucciones>
L1:
goto L2;

SALIDA:
if t9 >= t10 goto L2;
<instrucciones>
L1:
goto L2;
```

#### Regla No. 8
Eliminación de las instrucciones que tenga la siguiente forma:

```
ENTRADA: 
x = x + 0;

SALIDA:
#Se elimina la instrucción
```

#### Regla No. 9
Eliminación de las instrucciones que tenga la siguiente forma:

```
ENTRADA: 
x = x - 0;

SALIDA:
#Se elimina la instrucción
```

#### Regla No. 10
Eliminación de las instrucciones que tenga la siguiente forma:

```
ENTRADA: 
x = x * 1;

SALIDA:
#Se elimina la instrucción
```

#### Regla No. 11
Eliminación de las instrucciones que tenga la siguiente forma:

```
ENTRADA: 
x = x / 1;

SALIDA:
#Se elimina la instrucción
```

#### Regla No. 12
Eliminación de las instrucciones que tenga la siguiente forma:

```
ENTRADA: 
x = y + 0; 

SALIDA:
x = y; 
```

#### Regla No. 13
Eliminación de las instrucciones que tenga la siguiente forma:

```
ENTRADA: 
x = y + 0; 

SALIDA:
x = y; 
```

#### Regla No. 14
Eliminación de las instrucciones que tenga la siguiente forma:

```
ENTRADA: 
x = y * 1; 

SALIDA:
x = y; 
```

#### Regla No. 15
Eliminación de las instrucciones que tenga la siguiente forma:

```
ENTRADA: 
x = y / 1;

SALIDA:
x = y;
```

#### Regla No. 16
Eliminación de las instrucciones que tenga la siguiente forma:

```
ENTRADA: 
x = y * 2; 

SALIDA:
x = y + y;
```

#### Regla No. 17
Eliminación de las instrucciones que tenga la siguiente forma:

```
ENTRADA: 
x = y * 0;

SALIDA:
x = 0;
```

#### Regla No. 18
Eliminación de las instrucciones que tenga la siguiente forma:

```
ENTRADA: 
x = 0 / y;

SALIDA:
x = 0;
```

### Ejecución Programa<a name="id4"></a>

Para ejecutar el programa de python, debes de seguir los siguientes pasos:

```sh
$ cd G-27
$ python inicio.py
```

### Librerías usadas<a name="id5"></a>

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