# Gramática SQL :page_facing_up:

## __Integrantes__
**201800634**	ANTHONY FERNANDO SON MUX

**201801181**	CÉSAR EMANUEL GARCIA PÉREZ

**201801195**	JOSE CARLOS JIMENEZ

**201801237**	JOSÉ RAFAEL MORENTE GONZÁLEZ

## __GRAMÁTICA ASCENDENTE__

### INICIO  DE INSTRUCCIN EN SQL POSTGRESQL


La elección de gramática ascendente se debe a que es más sencillo utilizar atributos sintetizados al momento de recorrer el AST. Analizando el comportamiento de la gramática descendente concluimos que es la peor opción al momento de ejecutar las instrucciones ya que tenemos dos opciones generar el árbol de análisis sintáctico y posteriormente recorrerlo para ir ejecutando las instrucciones o la otra opción es manipular la pila para ir heredando atributos para posteriormente sintetizarlos, el problema de utilizar la pila es que si hacemos una mala referencia a una parte de memoria inexistente entonces el programa va a tender a tener bugs, tambien el uso de una gramática descendente en el momento de ejecución lo vuelve lento ya que debe de realizar dos veces el recorrido, mientras que con una gramática ascendente se sintetizan los atributos por lo tanto no hay que realizar dos o mas veces el recorrido del árbol, con una pasada es suficiente para poder ejecutar las instrucciones.



~~~
<inicio> ::= <instrucciones>

<instrucciones> ::= <instrucciones> <instruccion> 
                     | <instruccion>

<instruccion> ::= <ins_use>
                   | <ins_show>
                   | <ins_alter>
                   | <ins_drop>
                   | <ins_create>
                   | <ins_insert>
                   | <ins_select>
                   | <ins_update>
                   | <ins_delete>
~~~

### GRAMÁTICA DE INSTRUCCION DE USE
~~~
<ins_use> ::= USE ID PUNTO_COMA
~~~
### GRAMÁTICA DE INSTRUCCION SHOW DATABSE
~~~
<ins_show> ::= SHOW DATABASES PUNTO_COMA
~~~

### GRAMÁTICA DE INSTRUCCIONES ALTER DATABASE Y ALTER TABLE
~~~
<ins_alter> ::= ALTER <tipo_alter>

<tipo_alter> ::= DATABASE ID <alter_database> PUNTO_COMA
             | TABLE ID <alteracion_tabla> PUNTO_COMA

<alter_database> ::= RENAME TO ID
                 | OWNER TO ID

<alteracion_tabla> ::= <alteracion_tabla> COMA <alterar_tabla>
                        | <alterar_tabla>

<alterar_tabla> ::= ADD COLUMN <columna>
                     | ADD CONSTRAINT ID <columna>
                     | ALTER COLUMN <columna>
                     | DROP COLUMN ID
                     | DROP CONSTRAINT ID
~~~

### GRAMÁTICA DE INSTRUCCIONES DROP  DATABASE Y DROP TABLE 
~~~
<ins_drop> ::= DROP <tipo_drop>

<tipo_drop> ::= DATABASE <if_exists> ID PUNTO_COMA
                 | TABLE ID PUNTO_COMA
~~~

### GRAMÁTICA DE INSTRUCCIONES CREATE  DATABASE Y CREATE TABLE
~~~
<ins_create> ::= CREATE <tipo_create>

<tipo_create> ::= <ins_replace> DATABASE <if_exists> ID <create_opciones> PUNTO_COMA
              | TABLE ID PARABRE <definicion_columna> PARCIERRE <ins_inherits> PUNTO_COMA

<create_opciones> ::= OWNER SIGNO_IGUAL user_name <create_opciones>
                       | MODE SIGNO_IGUAL NUMERO <create_opciones>
                       | ε

<tipo_default> ::= NUMERIC
                | DECIMAL
                | NULL

<ins_constraint>
                | ID <definicion_valor_defecto> <ins_constraint>
                | ID TYPE <tipo_dato> <definicion_valor_defecto> <ins_constraint>
                | <primary_key> 
                | <foreign_key>

<primary_key> ::= PRIMARY KEY PARABRE <nombre_columnas> PARCIERRE <ins_references>

<foreign_key> ::= FOREIGN KEY PARABRE <nombre_columnas> PARCIERRE REFERENCES ID PARABRE <nombre_columnas> PARCIERRE <ins_references>

<nombre_columnas> ::= <nombre_columnas> COMA ID 
                  | ID 

<ins_references> ::= ON DELETE accion <ins_references>
                      | ON UPDATE accion <ins_references>
                      | ε

<definicion_columna> ::= <definicion_columna> COMA <columna> 
                	 | <columna> 
					 
<ins_inherits> ::= INHERITS PARABRE ID PARCIERRE
               |  ε

<ins_replace> ::= OR REPLACE
               | ε
			   
<if_exists> ::=  IF NOT EXISTS
            |  IF EXISTS
            |	ε
~~~


### GRAMÁTICA DE INSTRUCCIONES INSERT
~~~
<ins_insert> ::= INSERT INTO ID VALUES PARABRE <list_vls> PARCIERRE PUNTO_COMA
~~~

### DEFINICIÓN DE INSTRUCCIONES SELECT
~~~
<ins_select> ::= <ins_select> UNION <option_all> <ins_select> PUNTO_COMA
                    |    <ins_select> INTERSECT <option_all> <ins_select> PUNTO_COMA
                    |    <ins_select> EXCEPT <option_all> <ins_select> PUNTO_COMA
                    |    SELECT <arg_distict> <colum_list> FROM <table_list> <arg_where> <arg_group_by> <arg_order_by> <arg_limit> <arg_offset> PUNTO_COMA

<option_all>   ::= ALL
               | ε

<arg_distict> ::= DISTINCT
              | ε

<colum_list>   ::=   <s_list>
               |   SIGNO_POR

<s_list>   ::=   <s_list> COMA <columns> <as_id>
           |   <columns> <as_id>

<as_id>    ::=   AS ID
            |   AS CADENA
            |   CADENA
            |   ε

<columns>   ::= ID dot_table
            |   <aggregates>
            |   <functions>

<table_list>   ::=   <table_list> COMA ID <as_id>
                    |   ID <as_id>

<arg_where>    ::=   WHERE <exp>
                |  ε

<arg_group_by>  ::=   GROUP BY <g_list>
                |  ε

<g_list>    ::= <g_list> COMA <g_item>
            | <g_item> 

<g_item>    ::= ID <g_refitem>

<g_refitem>  ::= PUNTO ID
             | ε

<arg_order_by>    ::=   ORDER BY <o_list>
                |  ε

<o_list>    ::= <o_list> COMA <o_item>
                 | <o_item> 

<o_item>    ::= ID <o_refitem> <ad> <arg_nulls>

<o_refitem>  ::= PUNTO ID
             | ε

<ad> ::= ASC
    | DESC
    | ε

<arg_nulls> ::= NULLS <arg_fl>
            | ε

<arg_fl> ::= FIRST
         | LAST

<arg_limit>   ::=  LIMIT <option_limit>
              |  ε

<option_limit>   ::= NUMERO
                | ALL 

arg_offset   ::= OFFSET NUMERO 
             |  ε
~~~

### DEFINICIÓN DE INSTRUCCIONES UPDATES
~~~
<ins_update>   ::= UPDATE ID SET <asign_list> WHERE <exp> PUNTO_COMA

<asign_list>  ::= <asign_list> COMA ID SIGNO_IGUAL <val_value> 
                   | ID SIGNO_IGUAL <val_value>

<val_value> ::= CADENA
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
<ins_delete>   ::= DELETE FROM ID WHERE <exp> PUNTO_COMA
~~~

### DEFINICIÓN DE TIPO DE DATO
~~~
<tipo_dato> ::= SMALLINT          
                 | BIGINT
                 | NUMERIC
                 | DECIMAL
                 | INTEGER
                 | REAL
                 | DOUBLE PRECISION
                 | CHAR PARABRE NUMERO PARCIERRE
                 | VARCHAR PARABRE NUMERO PARCIERRE
                 | CHARACTER PARABRE NUMERO PARCIERRE
                 | TEXT
                 | TIMESTAMP <arg_precision>
                 | TIME <arg_precision>
                 | DATE
                 | INTERVAL <arg_tipo> <arg_precision>
                 | BOOLEAN
                 | MONEY

<arg_precision> ::= PARABRE NUMERO PARCIERRE 
                | ε

<arg_tipo> ::= MONTH
            | YEAR
            | HOUR
            | MINUTE
            | SECOND            
            | ε
~~~

### DEFINICIÓN DE COLUMNAS EN TABLAS
~~~
<definicion_columna> ::= <definicion_columna> COMA <columna> 
                          | <columna>
<columna> ::= ID <tipo_dato> <definicion_valor_defecto> 

<definicion_valor_defecto> ::= DEFAULT <tipo_default> 
                         | ε
~~~

### DEFINICIÓN DE EXPRESIONES
~~~
<exp_list>  ::= <exp_list> COMA <exp>
            | <exp>

<exp>  ::= <exp> SIGNO_MAS <exp>
            | <exp> SIGNO_MENOS <exp> 
            | <exp> SIGNO_POR <exp> 
            | <exp> SIGNO_DIVISION <exp> 
            | <exp> SIGNO_MODULO <exp> 
            | <exp> SIGNO_POTENCIA <exp> 
            | <exp> OR <exp> 
            | <exp> AND <exp> 
            | <exp> MENORQUE <exp> 
            | <exp> MAYORQUE <exp> 
            | <exp> MAYORIGUALQUE <exp> 
            | <exp> MENORIGUALQUE <exp> 
            | <exp> SIGNO_IGUAL <exp>
            | <exp> SIGNO_MENORQUE_MAYORQUE <exp>
            | <exp> SIGNO_NOT <exp> 
            | <arg_pattern>
            | <sub_consulta>
            | NOT <exp>
            | <data>
            | <predicates>
            | <aggregates>
            | <functions>
            | <arg_case>
            | <arg_greatest>
            | <arg_least> 
            | <val_value>

<arg_pattern>   ::= <data> LIKE CADENA   
                | <data> NOT LIKE CADENA

<data>  ::= ID <table_at>

<table_at>  ::= PUNTO ID
            | ε

<sub_consulta>   ::= PARABRE <ins_select>  PARCIERRE

<arg_case>  ::= CASE <arg_when> <arg_else> END

<arg_else> ::=  ELSE <exp>
         | ε

<arg_when>  ::= <arg_when> WHEN <exp> THEN <exp>
                 | WHEN <exp> THEN <exp>

<arg_greatest>  ::= GREATEST PARABRE <exp_list> PARCIERRE

<arg_least>  ::= LEAST PARABRE <exp_list> PARCIERR
~~~

##### DECLARACIÓN DE PREDICADOS
~~~
<predicates>  ::=  BETWEEN <list_vls> AND <list_vls>
                   | <data> NOT BETWEEN <list_vls> AND <list_vls>
                   | <data> BETWEEN SYMMETRIC <list_vls> AND <list_vls> 
                   | <data> NOT BETWEEN SYMMETRIC <list_vls> AND <list_vls>
                   | <data> IS DISTINCT FROM <list_vls>
                   | <data> IS NOT DISTINCT FROM <list_vls>
                   | <data> IS NULL 
                   | <data> ISNULL
                   | <data> NOTNULL
                   | <data> IS TRUE
                   | <data> IS NOT TRUE
                   | <data> IS FALSE
                   | <data> IS NOT FALSE
                   | <data> IS UNKNOWN
                   | <data> IS NOT UNKNOWN


<list_vls> ::= <list_vls> COMA <val_value>
                | <val_value> 

<val_value> ::= CADENA
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
<aggregates>   ::=   COUNT PARABRE <param> PARCIERRE
                    |   SUM PARABRE <param> PARCIERRE
                    |   AVG PARABRE <param> PARCIERRE
                    |   MAX PARABRE <param> PARCIERRE
                    |   MIN PARABRE <param> PARCIERRE

<param>    ::=   ID <dot_table>
         	|   SIGNO_POR
~~~

##### DECLARACION DE FUNCINES  
~~~
<functions>  ::=   <math>
             |   <trig>
             |   <string_func>
             |   <time_func>

<math> ::=   AVG PARABRE NUMERO PARCIERRE
                |   CBRT PARABRE NUMERO PARCIERRE
                |   CEIL PARABRE NUMERO PARCIERRE
                |   CEILING PARABRE NUMERO PARCIERRE
                |   DEGREES PARABRE NUMERO PARCIERRE
                |   DIV PARABRE NUMERO COMA NUMERO PARCIERRE
                |   EXP PARABRE NUMERO PARCIERRE
                |   FACTORIAL PARABRE NUMERO PARCIERRE
                |   FLOOR PARABRE NUMERO PARCIERRE
                |   GCD PARABRE NUMERO COMA NUMERO PARCIERRE
                |   IN PARABRE NUMERO PARCIERRE
                |   LOG PARABRE NUMERO PARCIERRE
                |   MOD PARABRE NUMERO COMA NUMERO PARCIERRE
                |   PI PARABRE  PARCIERRE
                |   POWER PARABRE NUMERO COMA NUMERO PARCIERRE 
                |   ROUND PARABRE NUMERO PARCIERRE

<trig> ::=   ACOS PARABRE NUMERO PARCIERRE
                |   ACOSD PARABRE NUMERO PARCIERRE
                |   ASIN PARABRE NUMERO PARCIERRE
                |   ASIND PARABRE NUMERO PARCIERRE
                |   ATAN PARABRE NUMERO PARCIERRE
                |   ATAND PARABRE NUMERO PARCIERRE
                |   ATAN2 PARABRE NUMERO COMA NUMERO PARCIERRE
                |   ATAN2D PARABRE NUMERO COMA NUMERO PARCIERRE
                |   COS PARABRE NUMERO PARCIERRE
                |   COSD PARABRE NUMERO PARCIERRE
                |   COT PARABRE NUMERO PARCIERRE
                |   COTD PARABRE NUMERO PARCIERRE
                |   SIN PARABRE NUMERO PARCIERRE
                |   SIND PARABRE NUMERO PARCIERRE
                |   TAN PARABRE NUMERO PARCIERRE
                |   TAND PARABRE NUMERO PARCIERRE
                |   SINH PARABRE NUMERO PARCIERRE
                |   COSH PARABRE NUMERO PARCIERRE
                |   TANH PARABRE NUMERO PARCIERRE
                |   ASINH PARABRE NUMERO PARCIERRE
                |   ACOSH PARABRE NUMERO PARCIERRE
                |   ATANH PARABRE NUMERO PARCIERRE  

<string_func>  ::=   LENGTH PARABRE <s_param> PARCIERRE
                    |   SUBSTRING PARABRE <s_param> COMA NUMERO COMA NUMERO PARCIERRE
                    |   SUBSTRING PARABRE <s_param> COMA <s_param> COMA CADENA PARCIERRE
                    |   TRIM PARABRE <s_param> PARCIERRE
                    |   GET_BYTE PARABRE <s_param> COMA NUMERO PARCIERRE
                    |   MOD5 PARABRE <s_param> PARCIERRE
                    |   SET_BYTE PARABRE COMA NUMERO COMA NUMERO <s_param> PARCIERRE
                    |   SHA256 PARABRE <s_param> PARCIERRE
                    |   SUBSTR PARABRE <s_param> COMA NUMERO COMA NUMERO PARCIERRE
                    |   CONVERT PARABRE tipo_dato COMA ID dot_table PARCIERRE
                    |   ENCODE PARABRE <s_param> COMA <s_param> PARCIERRE
                    |   DECODE PARABRE <s_param> COMA <s_param> PARCIERRE

<s_param>  ::=   <s_param> <string_op> CADENA
                |   CADENA 

<string_op>    ::=   SIGNO_PIPE
                    |   SIGNO_DOBLE_PIPE
                    |   SIGNO_AND
                    |   SIGNO_VIRGULILLA
                    |   SIGNO_NUMERAL
                    |   SIGNO_DOBLE_MENORQUE
                    |   SIGNO_DOBLE_MAYORQUE

<time_func>    ::=   DATE_PART PARABRE COMILLA <h_m_s> COMILLA COMA INTERVAL F_HORA PARCIERRE 
                    |   NOW PARABRE PARCIERRE
                    |   EXTRACT PARABRE <reserv_time>  FROM TIMESTAMP  PARCIERRE
                    |   CURRENT_TIME
                    |   CURRENT_DATE

<reserv_time>  ::=   <h_m_s> 
                    |   YEAR
                    |   MONTH
                    |   DAY

<h_m_s>    ::=   HOUR
            |   MINUTE
            |   SECOND
~~~


## __GRAMÁTICA DESCENDENTE__

### INICIO  DE INSTRUCCIN EN SQL POSTRGRES
~~~
<inicio>    ::= <lista_sentencia>

<lista_sentencia>    ::=   <sentencia> ';' <lista_sentencia>
                        |   epsilon

<sentencia>    ::=	<sentencia_use>
    			|     <sentencia_create>
     			|     <sentencia_insert>
     			|     <sentencia_update>
     			|     <sentencia_drop
     			|     <sentencia_alter>
     			|     <declaracion_show_db>
~~~


### GRAMÁTICA DE INSTRUCCION DE USE
~~~
<sentencia_use> ::= USE ID ';'
~~~
### GRAMÁTICA DE INSTRUCCION SHOW DATABSE
~~~
<declaracion_show_db> ::= SHOW DATABASES <regex> 

<regex> ::= LIKE '%' IDENTIFICADOR '%'
            | epsilon
~~~

### GRAMÁTICA DE INSTRUCCIONES ALTER DATABASE Y ALTER TABLE
~~~
<sentencia_alter>   ::= ALTER <opcion_alter> 

<opcion_alter>      ::= <declaracion_alter_db>
                        | <declaracion_alter_table>

<declaracion_alter_db> ::= ALTER DATABASE IDENTIFICADOR <cuerpo_alert_db>

<cuerpo_alter_db> ::=   RENAME TO IDENTIFICADOR
                        | OWNER TO { IDENTIFICADOR | CURRENT_USER | SESSION_USER }

<declaracion_alter_table> ::= ALTER TABLE IDENTIFICADOR <cuerpo_alter_table>
<cuerpo_alter_table>    ::=     ADD <cuerpo_alter_table_add> 
                            |   DROP 
                            |   ALTER  COLUMN IDENTIFICADOR SET NOT NULL;
                            |   RENAME COLUMN IDENTIFICADOR TO IDENTIFICADOR
<cuerpo_alter_table_add>    ::= CHECK '(' IDENTIFICADOR '<>' '' ')'
                                | CONSTRAINT IDENTIFICADOR UNIQUE '(' IDENTIFICADOR ')'
                                | FOREIGN KEY '(' IDENTIFICADOR ')' REFERENCES IDENTIFICADOR


~~~


### GRAMÁTICA DE INSTRUCCIONES CREATE  DATABASE Y CREATE TABLE
~~~
<sentencia_create>   ::= CREATE <opcion_create> 

<opcion_create>      ::= <declaracion_create_db>
                        | <declaracion_create_table>

<declaracion_create_db> ::= <argumento_or_replace> IDENTIFICADOR <argumento_if_NOT_exits> IDENTIFICADOR
    [ OWNER [=] IDENTIFICADOR ]         //[ OWNER [=] user_name ]
    [ MODE [=] IDENTIFICADOR ]        //[ MODE [=] mode_number ]


<declaracion_create_table> ::= TABLE IDENTIFICADOR '(' <cuerpo_create> ')' [INHERITS '(' IDENTIFICADOR ')' ] 

<sentencia_inherIt> ::= INHERITS IDENTIFICADOR
                        | epsilon

<cuerpo_create> ::= IDENTIFICADOR <type> <argumento_default_value> <argumento_nnull> <argumento_constraint_unique> [[CONSTRAINT name] CHECK (condition_column1)]

<cuerpo_create'> ::= ',' IDENTIFICADOR <type> <argumento_default_value> <argumento_nnull> <argumento_constraint_unique> [[CONSTRAINT name] CHECK (condition_column1)]
                        |   ',' UNIQUE '(' <lista_columna> ) <cuerpo_create'>
                        |   ',' <argumento_constraint> CHECK '(' condition_many_columns ')' <cuerpo_create'>
                        |   ',' PRIMARY KEY  '(' <lista_columna> ')' <cuerpo_create'>
                        |   ',' FOREIGN KEY  '(' <lista_columna> ')' REFERENCES table '(' <lista_columna> ')' <cuerpo_create'>
                        |   epsilon
~~~

### DEFINICIÓN DE INSTRUCCIONES UPDATE
~~~
<sentencia_update>   ::=  UPDATE IDENTIFICADOR SET IDENTIFICADOR = <__expresion__>> WHERE <__sentencia__>>;
~~~


### DEFINICIÓN DE TIPO DE DATO
~~~
<type>  ::= SMALLINT
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


<time> ::=  YEAR
            | MONTH
            | DAY
            | HOUR
            | MINUTE
            | SECOND 


<value>   ::= CADENA
            | NUMERO
            | DEMCIMAL
            | TRUE
            | FALSE
            | CADENA_DATE
~~~

### DEFINICIÓN DE COLUMNAS EN TABLAS
~~~
<argumento_if_exits>    ::= IF EXIST
                            | epsilon
<argumento_if_NOT_exits>    ::= IF NOT EXIST
                            | epsilon
<argumento_or_replace>    ::= OR REPLACE
                            | epsilon
<argumento_only>    ::= ONLY
                        | epsilon
<argumento_only>    ::= AS
                        | epsilon
<argumento_nnull>    ::= NULL
                        | NOT NULL
                        | epsilon
<argumento_constraint_unique>   ::= <argumento_constraint> UNIQUE
                                    | epsilon
<argumento_constraint>  ::= CONSTRAINT IDENTIFICADOR
                            |   epsilon
<argumento_default_value>   ::= DEFAULT <value>
                                    | epsilon

<lista_columna> ::= IDENTIFICADOR <colmna_tabla> <lista_columna'>
<colmna_tabla>  ::= '.' IDENTIFICADOR
                    | epsilon
<lista_columna> ::= ',' IDENTIFICADOR <colmna_tabla> <lista_columna'>
                    | epsilon
~~~

### DEFINICIÓN DE EXPRESIONES
~~~

<expresion_boleana> ::= <termino_boleano> <expresion_boleana'>
<expresion_boleana'>    ::=  '||' <termino_boleano> <expresion_boleana'>
                            | epsilon
<termino_boleano>   ::= <factor_boleano> <termino_boleano'>
<termino_boleano'>  ::= '&&' <factor_boleano> <termino_boleano'>
                        | epsilon
<factor_boleano>    ::= NOT <prueba_boleano>
                        | <prueba_boleano>
<prueba_boleano>    ::= <predicado>
                        | '(' expresion_boleana ')'

<predicado> ::= <predicado_betwen>
                | <predicado_betwen>

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


##### DECLARACION DE FUNCINES  
~~~
<funciones_agregacion>  ::= COUNT '(' IDENTIFICADOR ')'
                            | SUM '(' IDENTIFICADOR ')'
                            | AVG '(' IDENTIFICADOR ')'
                            | MAX '(' IDENTIFICADOR ')'
                            | MIN '(' IDENTIFICADOR ')'

~~~