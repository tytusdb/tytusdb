# Gramática SQL :page_facing_up:

## __Integrantes__
**201800634**	ANTHONY FERNANDO SON MUX

**201801181**	CÉSAR EMANUEL GARCIA PÉREZ

**201801195**	JOSE CARLOS JIMENEZ

**201801237**	JOSÉ RAFAEL MORENTE GONZÁLEZ

## __GRAMÁTICA ASCENDENTE__

### INICIO  DE INSTRUCCION EN SQL POSTGRESQL


La elección de gramática ascendente se debe a que es más sencillo utilizar atributos sintetizados al momento de recorrer el AST. Analizando el comportamiento de la gramática descendente concluimos que es la peor opción al momento de ejecutar las instrucciones ya que tenemos dos opciones generar el árbol de análisis sintáctico y posteriormente recorrerlo para ir ejecutando las instrucciones o la otra opción es manipular la pila para ir heredando atributos para posteriormente sintetizarlos, el problema de utilizar la pila es que si hacemos una mala referencia a una parte de memoria inexistente entonces el programa va a tender a tener bugs, tambien el uso de una gramática descendente en el momento de ejecución lo vuelve lento ya que debe de realizar dos veces el recorrido, mientras que con una gramática ascendente se sintetizan los atributos por lo tanto no hay que realizar dos o mas veces el recorrido del árbol, con una pasada es suficiente para poder ejecutar las instrucciones.


### GRAMÁTICA DE INSTRUCCIONES
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

### GRAMÁTICA DE INSTRUCCION DE USE
~~~
<INS_USE> ::= USE ID ';'
~~~
### GRAMÁTICA DE INSTRUCCION SHOW DATABSE
~~~
<INS_SHOW> ::= SHOW DATABASES ';'
~~~

### GRAMÁTICA DE INSTRUCCIONES ALTER DATABASE Y ALTER TABLE
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

### GRAMÁTICA DE INSTRUCCIONES DROP  DATABASE Y DROP TABLE 
~~~
<INS_DROP> ::= DROP <TIPO_DROP>

<TIPO_DROP> ::= DATABASE <IF_EXISTS> ID ';'
                | TABLE ID ';'
~~~

### GRAMÁTICA DE INSTRUCCIONES CREATE  DATABASE Y CREATE TABLE
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

### GRAMÁTICA DE INSTRUCCIONES INSERT
~~~
<INS_INSERT> ::= INSERT INTO ID VALUES '(' <LIST_VLS> ')' ';'
~~~

### DEFINICIÓN DE INSTRUCCIONES SELECT
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

### DEFINICIÓN DE INSTRUCCIONES UPDATES
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

### DEFINICIÓN DE INSTRUCCIONES DELETE
~~~
<INS_DELETE>   ::= DELETE FROM ID WHERE <EXP> ';'
~~~

### DEFINICIÓN DE TIPO DE DATO
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

### DEFINICIÓN DE COLUMNAS EN TABLAS
~~~
<DEFINICION_COLUMNA> ::= <DEFINICION_COLUMNA> ',' <COLUMNA> 
                | <COLUMNA>
<COLUMNA> ::= ID <TIPO_DATO> <DEFINICION_VALOR_DEFECTO> 

<DEFINICION_VALOR_DEFECTO> ::= DEFAULT <TIPO_DEFAULT> 
                | EPSILON
~~~

### DEFINICIÓN DE EXPRESIONES
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

### DECLARACIÓN DE PREDICADOS
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

### DECLARACIÓN DE FUNCIONES DE AGREGACIÓN
~~~
<AGGREGATES>   ::=   COUNT '(' <PARAM> ')'
                |   SUM '(' <PARAM> ')'
                |   AVG '(' <PARAM> ')'
                |   MAX '(' <PARAM> ')'
                |   MIN '(' <PARAM> ')'

<PARAM> ::=   ID <DOT_TABLE>
                |   SIGNO_POR
~~~

### DECLARACION DE FUNCIONES  
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

### INSTRUCCIONES PL/PSQL
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

### INSTRUCCIONES INDICES
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

## __GRAMÁTICA DESCENDENTE__

### INICIO  DE INSTRUCCIONES EN SQL POSTGRESQL
~~~
<INICIO> ::= <LISTA_SENTENCIA>

<LISTA_SENTENCIA> ::=   <SENTENCIA> ';' <LISTA_SENTENCIA>
                |   EPSILON

<SENTENCIA> ::= <SENTENCIA_USE>
                |     <SENTENCIA_CREATE>
                |     <SENTENCIA_INSERT>
                |     <SENTENCIA_UPDATE>
                |     <SENTENCIA_DROP
                |     <SENTENCIA_ALTER>
                |     <DECLARACION_SHOW_DB>
~~~

### GRAMÁTICA DE INSTRUCCION DE USE
~~~
<SENTENCIA_USE> ::= USE ID ';'
~~~
### GRAMÁTICA DE INSTRUCCION SHOW DATABSE
~~~
<DECLARACION_SHOW_DB> ::= SHOW DATABASES <REGEX> 

<REGEX> ::= LIKE '%' IDENTIFICADOR '%'
                | EPSILON
~~~

### GRAMÁTICA DE INSTRUCCIONES ALTER DATABASE Y ALTER TABLE
~~~
<SENTENCIA_ALTER>   ::= ALTER <OPCION_ALTER> 

<OPCION_ALTER>   ::= <DECLARACION_ALTER_DB>
                | <DECLARACION_ALTER_TABLE>

<DECLARACION_ALTER_DB> ::= ALTER DATABASE IDENTIFICADOR <CUERPO_ALERT_DB>

<CUERPO_ALTER_DB> ::=   RENAME TO IDENTIFICADOR
                | OWNER TO { IDENTIFICADOR | CURRENT_USER | SESSION_USER }

<DECLARACION_ALTER_TABLE> ::= ALTER TABLE IDENTIFICADOR <CUERPO_ALTER_TABLE>
<CUERPO_ALTER_TABLE> ::=     ADD <CUERPO_ALTER_TABLE_ADD> 
                |   DROP 
                |   ALTER  COLUMN IDENTIFICADOR SET NOT NULL;
                |   RENAME COLUMN IDENTIFICADOR TO IDENTIFICADOR
<CUERPO_ALTER_TABLE_ADD> ::= CHECK '(' IDENTIFICADOR '<>' '' ')'
                | CONSTRAINT IDENTIFICADOR UNIQUE '(' IDENTIFICADOR ')'
                | FOREIGN KEY '(' IDENTIFICADOR ')' REFERENCES IDENTIFICADOR

~~~

### GRAMÁTICA DE INSTRUCCIONES CREATE  DATABASE Y CREATE TABLE
~~~
<SENTENCIA_CREATE>   ::= CREATE <OPCION_CREATE> 

<OPCION_CREATE>   ::= <DECLARACION_CREATE_DB>
                | <DECLARACION_CREATE_TABLE>

<DECLARACION_CREATE_DB> ::= <ARGUMENTO_OR_REPLACE> IDENTIFICADOR <ARGUMENTO_IF_NOT_EXITS> IDENTIFICADOR
    [ OWNER [=] IDENTIFICADOR ]         //[ OWNER [=] USER_NAME ]
    [ MODE [=] IDENTIFICADOR ]        //[ MODE [=] MODE_NUMBER ]

<DECLARACION_CREATE_TABLE> ::= TABLE IDENTIFICADOR '(' <CUERPO_CREATE> ')' [INHERITS '(' IDENTIFICADOR ')' ] 

<SENTENCIA_INHERIT> ::= INHERITS IDENTIFICADOR
                | EPSILON

<CUERPO_CREATE> ::= IDENTIFICADOR <TYPE> <ARGUMENTO_DEFAULT_VALUE> <ARGUMENTO_NNULL> <ARGUMENTO_CONSTRAINT_UNIQUE> [[CONSTRAINT NAME] CHECK (CONDITION_COLUMN1)]

<CUERPO_CREATE'> ::= ',' IDENTIFICADOR <TYPE> <ARGUMENTO_DEFAULT_VALUE> <ARGUMENTO_NNULL> <ARGUMENTO_CONSTRAINT_UNIQUE> [[CONSTRAINT NAME] CHECK (CONDITION_COLUMN1)]
                |   ',' UNIQUE '(' <LISTA_COLUMNA> ) <CUERPO_CREATE'>
                |   ',' <ARGUMENTO_CONSTRAINT> CHECK '(' CONDITION_MANY_COLUMNS ')' <CUERPO_CREATE'>
                |   ',' PRIMARY KEY  '(' <LISTA_COLUMNA> ')' <CUERPO_CREATE'>
                |   ',' FOREIGN KEY  '(' <LISTA_COLUMNA> ')' REFERENCES TABLE '(' <LISTA_COLUMNA> ')' <CUERPO_CREATE'>
                |   EPSILON
~~~

### DEFINICIÓN DE INSTRUCCIONES UPDATE
~~~
<SENTENCIA_UPDATE>   ::=  UPDATE IDENTIFICADOR SET IDENTIFICADOR = <__EXPRESION__>> WHERE <__SENTENCIA__>>;
~~~

### DEFINICIÓN DE TIPO DE DATO
~~~
<TYPE>  ::= SMALLINT
                | INTEGER
                | BIGINT
                | DECIMAL
                | NUMERIC
                | REAL
                | DOUBLE PRECISION
                | MONEY
                | CHARACTER [VARYING]
                | VARCHAR
                | CHAR
                | TEXT
                | TIME
                | TIMESTAMP
                | DATE
                | INTERVAL

<TIME> ::=  YEAR
            | MONTH
            | DAY
            | HOUR
            | MINUTE
            | SECOND 

<VALUE>   ::= CADENA
            | NUMERO
            | DEMCIMAL
            | TRUE
            | FALSE
            | CADENA_DATE
~~~

### DEFINICIÓN DE COLUMNAS EN TABLAS
~~~
<ARGUMENTO_IF_EXITS> ::= IF EXIST
                | EPSILON

<ARGUMENTO_IF_NOT_EXITS> ::= IF NOT EXIST
                | EPSILON

<ARGUMENTO_OR_REPLACE> ::= OR REPLACE
                | EPSILON

<ARGUMENTO_ONLY> ::= ONLY
                | EPSILON

<ARGUMENTO_ONLY> ::= AS
                | EPSILON

<ARGUMENTO_NNULL> ::= NULL
                | NOT NULL
                | EPSILON

<ARGUMENTO_CONSTRAINT_UNIQUE>   ::= <ARGUMENTO_CONSTRAINT> UNIQUE
                | EPSILON

<ARGUMENTO_CONSTRAINT>  ::= CONSTRAINT IDENTIFICADOR
                |   EPSILON

<ARGUMENTO_DEFAULT_VALUE>   ::= DEFAULT <VALUE>
                | EPSILON

<LISTA_COLUMNA> ::= IDENTIFICADOR <COLMNA_TABLA> <LISTA_COLUMNA'>

<COLMNA_TABLA>  ::= '.' IDENTIFICADOR
                | EPSILON

<LISTA_COLUMNA> ::= ',' IDENTIFICADOR <COLMNA_TABLA> <LISTA_COLUMNA'>
                | EPSILON
~~~

### DEFINICIÓN DE EXPRESIONES
~~~

<EXPRESION_BOLEANA> ::= <TERMINO_BOLEANO> <EXPRESION_BOLEANA'>

<EXPRESION_BOLEANA'> ::=  '||' <TERMINO_BOLEANO> <EXPRESION_BOLEANA'>
                | EPSILON
                
<TERMINO_BOLEANO>   ::= <FACTOR_BOLEANO> <TERMINO_BOLEANO'>

<TERMINO_BOLEANO'>  ::= '&&' <FACTOR_BOLEANO> <TERMINO_BOLEANO'>
                | EPSILON

<FACTOR_BOLEANO> ::= NOT <PRUEBA_BOLEANO>
                | <PRUEBA_BOLEANO>

<PRUEBA_BOLEANO> ::= <PREDICADO>
                | '(' EXPRESION_BOLEANA ')'

<PREDICADO> ::= <PREDICADO_BETWEN>
                | <PREDICADO_BETWEN>

<OPERATOR_LOGICO>  ::=  '&&'
                | '||'

<OPERATOR_COMPA> ::=     ‘<’  
                |  ‘>’  
                |  ‘<=’  
                |  ‘>=’  
                |  ‘=’  
                |  ‘<>’  
                |  ‘!=’
~~~

#### DECLARACION DE FUNCIONES  
~~~
<FUNCIONES_AGREGACION>  ::= COUNT '(' IDENTIFICADOR ')'
                | SUM '(' IDENTIFICADOR ')'
                | AVG '(' IDENTIFICADOR ')'
                | MAX '(' IDENTIFICADOR ')'
                | MIN '(' IDENTIFICADOR ')'
~~~

License
----

MIT