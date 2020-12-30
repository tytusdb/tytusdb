##REPORTE GRAMATICAL ASCENDENTE DESCENDENTE

----------

###Palabras Reservadas

- SMALLINT
- INTEGER
- BIGINIT
- DECIMAL
- NUMERIC
- REAL
- DOUBLE
- PRECISION
- MONEY
- VARCHAR
- CHARACTER
- TEXT
- TIMESTAMP
- WITHOUT
- TIME
- ZONE
- WITH
- DATE
- INTERVAL
- YEAR
- MONTH
- DAY
- HOUR
- MINUTE
- SECOND
- TO
- BOOLEAN
- CREATE
- TYPE
- AS
- ENUM
- BETWEEN
- IN
- LIKE
- ILIKE
- SIMILAR
- ISNULL
- NOTNULL
- NOT
- NULL
- AND
- OR
- REPLACE
- DATABASE
- IF
- EXISTS
- OWNER
- MODE
- SHOW
- DATABASES
- ALTER
- RENAME
- DROP
- TABLE
- CONSTRAINT
- UNIQUE
- CHECK
- PRIMARY
- KEY
- REFERENCES
- FOREIGN
- ADD
- SET
- DELETE
- FROM
- WHERE
- INHERITS
- INSERT
- INTO
- UPDATE
- VALUES
- SELECT
- DISTINCT
- GROUP
- BY
- HAVING
- SUM
- COUNT
- AVG
- MAX
- MIN
- ABS
- CBRT
- CEIL
- CEILING
- DEGREES
- DIV
- EXP
- FACTORIAL
- FLOOR
- GCD
- LCM
- LN
- LOG
- LOG10
- MIN_SCALE
- MOD
- PI
- POWER
- RADIANS
- ROUND
- SCALE
- SIGN
- SQRT
- TRIM_SCALE
- WIDTH_BUCKET
- RANDOM
- SETSEED
- ACOS
- ACOSD
- ASIN
- ASIND
- ATAN
- ATAND
- ATAN2
- ATAN2D
- COS
- COSD
- COT
- COTD
- SIN
- SIND
- TAN
- TAND
- SINH
- COSH
- TANH
- ASINH
- ACOSH
- ATANH
- LENGTH
- SUBSTRING
- TRIM
- GET_BYTE
- MD5
- SET_BYTE
- SHA256
- SUBSTR
- CONVERT
- ENCODE
- DECODE
- EXTRACT
- CENTURY
- DECADE
- DOW
- DOY
- EPOCH
- ISODOWN
- ISOYEAR
- MICROSECONDS
- MILENNIUM
- MILLISECONDS
- QUARTER
- TIMEZONE
- TIMEZONE_HOUR
- TIMEZONE_MINUTE
- WEEK
- AT
- CURRENT_DATE
- CURRENT_TIME
- CURRENT_TIMESTAMP
- LOCALTIME
- LOCALTIMESTAMP
- PG_SLEEP
- PG_SLEEP_FOR
- PG_SLEEP_UNTIL
- INNER
- LEFT
- RIGHT
- FULL
- OUTER
- JOIN
- ALL
- ANY
- SOME
- ORDER
- ASC
- DESC
- CASE
- WHEN
- THEN
- ELSE
- END
- GREATEST
- LEAST
- LIMIT
- UNION
- INTERSECT
- EXCEPT
- IS
- DEFAULT
- TRUE
- FALSE
- COLUMN
- CURRENT_USER
- SESSION_USER
- DATE_PART
- NOW
- TRUNC
- OFFSET
- NULLS
- FIRST
- LAST
- CHAR

----------

###Tokens

- PTCOMA
- COMA
- PUNTO
- TYPECAST
- MAS
- MENOS
- POTENCIA
- MULTIPLICACION
- DIVISION
- MODULO
- MENOR_QUE
- MENOR_IGUAL
- MAYOR_QUE
- MAYOR_IGUAL
- IGUAL
- DISTINTO
- LLAVEIZQ
- LLAVEDER
- PARIZQUIERDO
- PARDERECHO
- DECIMAL_
- ENTERO
- CADENA
- ID
- ESPACIO


----------

#GRAMÁTICA ASCENDENTE


----------

----------

	<init>   			::=	<instrucciones>

	<instrucciones>  	::=	<instrucciones> <instruccion>  
						|	<intruccion>


	<instruccion>  		::=	<insert_table>
                    	|   <delete_table>
                    	|   <update_table>
						| 	<crear_instr>
						| 	<alter_instr>
						| 	<drop_instr>
						| 	<inst_select> PTCOMA


	<crear_instr> 		::= CREATE TABLE ID PARIZQUIERDO <columnas> PARDERECHO <herencia> PTCOMA
						|	CREATE <opReplace> DATABASE <opExists> ID <opDatabase> PTCOMA
						|	CREATE TYPE ID AS ENUM PARIZQUIERDO ID PARDERECHO PTCOMA


    <insert_table>   	::=	INSERT INTO ID VALUES <lista_valores> PTCOMA
                      	|   INSERT INTO ID PARIZQUIERDO  <lista_columnas>  PARDERECHO VALUES <lista_valores> PTCOMA
                      	|   INSERT INTO ID DEFAULT VALUES PTCOMA
                      	|   INSERT INTO ID PARIZQUIERDO <lista_columnas> PARDERECHO DEFAULT VALUES PTCOMA

    
	<lista_columnas>   	::=	<lista_columnas> COMA ID
                       	|   ID


	<lista_valores>	  	::=	<lista_valores> COMA <tupla>
                      	|   <tupla>


	<tupla>  			::=	PARIZQUIERDO <lista_expresiones> PARDERECHO


	<lista_expresiones>	::=	<lista_expresiones> COMA <expresion>
    					|   <expresion>


    <expresion>  		::=	CADENA
						|	ENTERO
						|	DECIMAL_


	<delete_table>   	::=	DELETE FROM ID PTCOMA
                      	|   DELETE FROM ID WHERE <exp_operacion> PTCOMA


	<exp_operacion>  	::=	<exp_logica>


	<exp_logica>     	::=	<exp_logica> OR <exp_logica>
                      	|   <exp_logica> AND <exp_logica>
                      	|   NOT <exp_logica>
                      	|   <exp_relacional>


    <exp_relaciona>   	::=	<exp_relacional> MENOR_QUE <exp_relacional>
                        |   <exp_relacional> MENOR_IGUAL <exp_relacional>
                        |   <exp_relacional> MAYOR_QUE <exp_relacional>
                        |   <exp_relacional> MAYOR_IGUAL <exp_relacional>
                        |   <exp_relacional> DISTINTO <exp_relacional>
                        |   <exp_relacional> IGUAL <exp_relacional>
                        |   <exp_aritmetica>


	<exp_aritmetica>  	::=	<exp_aritmetica> MAS <exp_aritmetica>
                        |   <exp_aritmetica> MENOS <exp_aritmetica>
                        |   <exp_aritmetica> MULTIPLICACION <exp_aritmetica>
                        |   <exp_aritmetica> DIVISION <exp_aritmetica>
                        |   <exp_aritmetica> MODULO <exp_aritmetica>
                        |   <exp_aritmetica> POTENCIA <exp_aritmetica>
                        |   <exp_aritmetica> BETWEEN <exp_aritmetica> AND <exp_aritmetica>
                        |   <exp_aritmetica> NOT BETWEEN <exp_aritmetica> AND <exp_aritmetica>
                        |   <exp_aritmetica> IN PARIZQUIERDO <lista_expresiones> PARDERECHO
                        |   <exp_aritmetica> NOT IN PARIZQUIERDO <lista_expresiones> PARDERECHO
                        |   <exp_aritmetica> IN <subquery> 
                        |   <exp_aritmetica> NOT IN <subquery>
                        |   <exp_aritmetica> LIKE <exp_aritmetica>
                        |   <exp_aritmetica> NOT LIKE <exp_aritmetica>
                        |   <exp_aritmetica> ILIKE <exp_aritmetica>
                        |   <exp_aritmetica> NOT ILIKE <exp_aritmetica>
                        |   <exp_aritmetica> SIMILAR TO <exp_aritmetica>
                        |   <exp_aritmetica> IS NULL
                        |   <exp_aritmetica> IS NOT NULL
                        |   <primitivo>


	<primitivo>  		::=   ID
						|	ID PUNTO ID
						|   MAS <primitivo>
                    	|   MENOS <primitivo>
                    	|   PARIZQUIERDO <exp_operacion> PARDERECHO
						|	ENTERO
						|	DECIMAL_
						|	CADENA
						|	TRUE
						|	FALSE
						|	<funcion>


	<update_table>     	::=	UPDATE ID SET <lista_seteos> PTCOMA
                        |   UPDATE ID SET <lista_seteos> WHERE <exp_operacion> PTCOMA


	<lista_seteos>     	::=	<lista_seteos> COMA <set_columna>
                        |   <set_columna>


	<set_columna>    	::=	ID IGUAL <exp_operacion>


	<columnas> 			::=	<columnas> COMA <columna>
						|	<columna>


    <columna> 			::= ID <tipos> <opcional>
						|	PRIMARY KEY PARIZQUIERDO <identificadores> PARDERECHO
						|	FOREIGN KEY PARIZQUIERDO <identificadores> PARDERECHO REFERENCES ID PARIZQUIERDO <identificadores> PARDERECHO
						|	UNIQUE PARIZQUIERDO <identificadores> PARDERECHO


	<opcional> 			::=	DEFAULT <opcionNull>
						|	<opcionNull>


	<opcionNull> 		::=	NOT NULL <opConstraint>
						|	<opConstraint>


	<opConstraint> 		::= CONSTRAINT ID <opUniqueCheck>
						| 	<opUniqueCheck>


	<opUniqueCheck> 	::=	UNIQUE
						| 	CHECK PARIZQUIERDO <condicion_check> PARDERECHO
						| 	empty


	<condicion_check> 	::=	ID MENOR_QUE <expresion>
                        | 	ID MENOR_IGUAL <expresion>
                        | 	ID MAYOR_QUE <expresion>
                        | 	ID MAYOR_IGUAL <expresion>
                        | 	ID DISTINTO <expresion>
                        | 	ID IGUAL <expresion>


	<herencia> 			::= INHERITS PARIZQUIERDO ID PARDERECHO'
						|	empty


	<identificadores> 	::= <identificadores> COMA ID
						|	ID

	<opReplace> 		::= OR REPLACE'
						|	empty


	<opExists> 			::= IF NOT EXISTS
						|	empty


	<opDatabase> 		::= OWNER <opIgual> ID <mode>
						|	mode


	<opIgual> 			::= IGUAL
						|	empty


	<mode> 				::= MODE <opIgual> ENTERO
						| 	empty


	<alter_instr> 		::= ALTER DATABASE ID <opAlterDatabase> PTCOMA
						|	ALTER TABLE ID <alter_table_instr> PTCOMA
	

	<opAlterDatabase> 	::= RENAME TO ID
						| 	OWNER TO <ownerList>

	<ownerList> 		::= ID
						|	CURRENT_USER
						|	SESSION_USER


	<alter_table_instr>	::= ADD <add_instr>
						|	<alter_columnas>
						|	<drop_columnas>


	<alter_columnas> 	::= <alter_columnas> COMA <alter_columna>
						|	<alter_columna>


	<alter_columna> 	::= ALTER COLUMN ID <alter_column_instr>


	<drop_columnas> 	::= <drop_columnas> COMA <drop_columna>
						|	<drop_columna>


	<drop_columna> 		::= DROP COLUMN ID


	<alter_table_instr> ::= DROP CONSTRAINT ID
						| 	SET NOT NULL
						|	SET NULL
						|	TYPE ID


	<add_instr> 		::= CHECK PARIZQUIERDO <condicion_check> PARDERECHO
						|	CONSTRAINT ID UNIQUE PARIZQUIERDO ID PARDERECHO
						

	<drop_instr> 		::= DROP DATABASE <si_existe> ID PTCOMA
						|	DROP TABLE ID PTCOMA

	<si_existe> 		::= IF EXISTS
						|	empty

	<inst_select>  		::=	<select_query>
                    	|   <select_query> UNION <select_query>
	                    |   <select_query> UNION ALL <select_query>
	                    |   <select_query> INTERSECT <select_query>
	                    |   <select_query> INTERSECT ALL <select_query>
	                    |   <select_query> EXCEPT <select_query>
	                    |   <select_query> EXCEPT ALL <select_query>


	<select_query>     	::=	SELECT DISTINCT <select_list> FROM <from_query_list> <lista_condiciones_query>
                        |   SELECT <select_list> FROM <from_query_list> <lista_condiciones_query>
                        |   SELECT DISTINCT <select_list> FROM <from_query_list> 
                        |   SELECT <select_list> FROM <from_query_list>
                        |   SELECT <select_list>


	<select_list>  		::=	MULTIPLICACION
                    	|   <elementos_select_list>


	<elementos_select_list>	::=	<elementos_select_list> COMA <elemento_select>
                           	|   <elemento_select>


	<elemento_select>  	::=	<dec_select_columna>
	 					|	<subquery> AS ID
                        |   <subquery> ID
                        |   <subquery>
						|	<funcion> AS ID
                        |   <funcion> ID
                        |   <funcion>

	<dec_select_columna>::=	ID PUNTO ID AS ID
                       	|   ID PUNTO ID ID
                       	|   ID PUNTO ID
                        |   ID


	<funcion>  			::=	<funcion_time>
		                |   <funcion_mate>
		                |   <funcion_trig>
		                |   <funcion_binstr>
		                |   <funcion_exprecion>
		                |   <funcion_agregacion>
		                |   <dec_case>

	<funcion_time> 		::=	EXTRACT PARIZQUIERDO <var_time> FROM <var_timeextract> CADENA PARDERECHO
	                    |   DATE_PART PARIZQUIERDO CADENA COMA <var_timeextract> CADENA PARDERECHO
	                    |   NOW PARIZQUIERDO PARDERECHO
	                    |   CURRENT_DATE
	                    |   CURRENT_TIME


	<var_time> 			::=	YEAR
		                |   MONTH
		                |   DAY
		                |   HOUR
		                |   MINUTE
		                |   SECOND


	<var_timeextract>  	::=	TIMESTAMP
                        |   TIME
                        |   DATE
                        |   INTERVAL


	<funcion_mate> 		::=	ABS PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   CBRT PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   CEIL PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   CEILING PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   DEGREES PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   DIV PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO
	                    |   EXP PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   FACTORIAL PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   FLOOR PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   GCD PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO
	                    |   LN PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   LOG PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   MOD PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO
	                    |   PI PARIZQUIERDO PARDERECHO
	                    |   POWER PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO
	                    |   RADIANS PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ROUND PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO
	                    |   SIGN PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   SQRT PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   WIDTH_BUCKET PARIZQUIERDO <exp_operacion> COMA <exp_operacion> COMA <exp_operacion> COMA <exp_operacion> PARDERECHO
	                    |   TRUNC PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   RANDOM PARIZQUIERDO <exp_operacion> PARDERECHO


    <funcion_trig> 		::=	ACOS PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ACOSD PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ASIN PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ASIND PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ATAN PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ATAND PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ATAN2 PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO
	                    |   ATAN2D PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO
	                    |   COS PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   COSD PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   SIN PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   SIND PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   TAN PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   TAND PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   SINH PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   COSH PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   TANH PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ASINH PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ACOSH PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ATANH PARIZQUIERDO <exp_operacion> PARDERECHO


	<funcion_binstr>   	::=	LENGTH PARIZQUIERDO <exp_operacion> PARDERECHO
                        |   SUBSTRING PARIZQUIERDO <exp_operacion> COMA ENTERO COMA ENTERO PARDERECHO
                        |   TRIM PARIZQUIERDO <exp_operacion> PARDERECHO
                        |   MD5 PARIZQUIERDO <exp_operacion> PARDERECHO
                        |   SHA256 PARIZQUIERDO <exp_operacion> PARDERECHO
                        |   SUBSTR PARIZQUIERDO <exp_operacion> COMA ENTERO COMA ENTERO PARDERECHO
                        |   GET_BYTE PARIZQUIERDO <exp_operacion> COMA ENTERO PARDERECHO
                        |   SET_BYTE PARIZQUIERDO <exp_operacion> COMA ENTERO COMA ENTERO PARDERECHO
                        |   CONVERT PARIZQUIERDO <exp_operacion> AS <tipos> PARDERECHO
                        |   ENCODE PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO
                        |   DECODE PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO


    <funcion_agregacion>::=	SUM PARIZQUIERDO <exp_operacion PARDERECHO
                      	|   COUNT PARIZQUIERDO <exp_operacion> PARDERECHO
                        |   COUNT PARIZQUIERDO MULTIPLICACION PARDERECHO
                        |   AVG PARIZQUIERDO <exp_operacion> PARDERECHO
                        |   MAX PARIZQUIERDO <exp_operacion> PARDERECHO
                        |   MIN PARIZQUIERDO <exp_operacion> PARDERECHO


	<funcion_exprecion>	::=	GREATEST PARIZQUIERDO <lista_exp> PARDERECHO
                       	|   LEAST PARIZQUIERDO <lista_exp> PARDERECHO


    <dec_case> 			::=	CASE <lista_when_case> ELSE <exp_operacion> END
                		|   CASE <lista_when_case> END


	<lista_when_case>	::=	<lista_when_case> <clausula_case_when>
                        |   <clausula_case_when>


	<clausula_case_when>::=	WHEN <exp_operacion> THEN <exp_operacion>


	<from_query_list>	::=	<from_query_list> COMA <from_query_element>
                        |   <from_query_element>



	<from_query_element>::=	<dec_id_from>
                      	|   <subquery> AS ID
                       	|   <subquery> ID
                       	|   <subquery>


	<dec_id_from>  		::=	ID AS ID
	                    |   ID ID
	                    |   ID


    <lista_condiciones_query>	::=	<lista_condiciones_query> <condicion_query>
                               	|   <condicion_query>


	<condicion_query> 	::=	WHERE <exp_operacion>
                        |   GROUP BY <lista_ids>
                        |   HAVING <exp_operacion>
                        |   ORDER BY <lista_order_by>
                        |   LIMIT <condicion_limit> OFFSET <exp_operacion>
                        |   LIMIT <condicion_limit>


	<condicion_limit>  	::=	<exp_operacion>
						|	ALL

	<lista_ids>    		::=	<lista_ids> COMA <dec_select_columna>
                    	|   <dec_select_columna>


	<lista_order_by>   	::=	<lista_order_by> COMA <elemento_order_by>
                        |   <elemento_order_by>


	<elemento_order_by>	::=	<exp_operacion> <asc_desc> NULLS <condicion_null>
						|	<exp_operacion> <asc_desc>

	<asc_desc> 			::=	ASC
                		|   DESC


	<condicion_null>   	::=	FIRST
                        |   LAST


	<subquery> 			::=	PARIZQUIERDO <select_query> PARDERECHO


	<lista_exp>    		::=	<lista_exp> COMA <exp_operacion>
                    	|   <exp_operacion>


	<tipos> 			::=	SMALLINT
                        | INTEGER
                        | BIGINIT
                        | DECIMAL
                        | NUMERIC
                        | REAL
                        | DOUBLE
                        | MONEY
                        | VARCHAR
                        | CHARACTER
                        | TEXT
                        | TIMESTAMP
                        | TIME
                        | DATE
                        | INTERVAL
                        | BOOLEAN


----------

#GRAMÁTICA DESCENDENTE


----------

----------

	<init>   			::=	<instrucciones>

	<instrucciones>  	::=	<intruccion> <instruccion_p>  
						|	

	<instruccion_p>		::=	<instruccion> <instruccion_p>
						|	EMPTY


	<instruccion>  		::=	<insert_table>
                    	|   <delete_table>
                    	|   <update_table>
						| 	<crear_instr>
						| 	<alter_instr>
						| 	<drop_instr>
						| 	<inst_select> PTCOMA


	<crear_instr> 		::= CREATE TABLE ID PARIZQUIERDO <columnas> PARDERECHO <herencia> PTCOMA
						|	CREATE <opReplace> DATABASE <opExists> ID <opDatabase> PTCOMA
						|	CREATE TYPE ID AS ENUM PARIZQUIERDO ID PARDERECHO PTCOMA


    <insert_table>   	::=	INSERT INTO ID VALUES <lista_valores> PTCOMA
                      	|   INSERT INTO ID PARIZQUIERDO  <lista_columnas>  PARDERECHO VALUES <lista_valores> PTCOMA
                      	|   INSERT INTO ID DEFAULT VALUES PTCOMA
                      	|   INSERT INTO ID PARIZQUIERDO <lista_columnas> PARDERECHO DEFAULT VALUES PTCOMA

    
	<lista_columnas>   	::=	ID <lista_columnas_p>

	<lista_columnas_p> 	::=	COMA ID <lista_columnas_p>
						| 	EMPTY


	<lista_valores>	  	::=	<tupla> <lista_valores_p>

	<lista_valores_p>	::= COMA <tupla> <lista_valores_p>
						| 	EMPTY

	<tupla>  			::=	PARIZQUIERDO <lista_expresiones> PARDERECHO


	<lista_expresiones>	::=	<expresion> <lista_expresiones_p>

	<lista_expresiones_p>::= COMA <expresion> <lista_expresiones_p>
						| 	EMPTY


    <expresion>  		::=	CADENA
						|	ENTERO
						|	DECIMAL_


	<delete_table>   	::=	DELETE FROM ID PTCOMA
                      	|   DELETE FROM ID WHERE <exp_operacion> PTCOMA


	<exp_operacion>  	::=	<exp_logica>


	<exp_logica>     	::=	NOT <exp_logica> <exp_logica_p>
                      	|   <exp_relacional> <exp_logica_p>

	<exp_logica_p>		::= OR <exp_logica> <exp_logica_p>
                      	|   AND <exp_logica> <exp_logica_p>
						| 	EMPTY


    <exp_relaciona>   	::=	<exp_aritmetica> <exp_relaciona_p>

	<exp_relaciona_p>	::=	MENOR_QUE <exp_relacional> <exp_relaciona_p>
						|	MENOR_IGUAL <exp_relacional> <exp_relaciona_p>
						|	MAYOR_QUE <exp_relacional> <exp_relaciona_p>
						|	MAYOR_IGUAL <exp_relacional> <exp_relaciona_p>
						|	DISTINTO <exp_relacional> <exp_relaciona_p>
						|	IGUAL <exp_relacional> <exp_relaciona_p>
						| 	EMPTY


	<exp_aritmetica>  	::=	<primitivo> <exp_aritmetica_p>

	<exp_aritmetica_p>  ::=	MAS <exp_aritmetica> <exp_aritmetica_p>
                        |   MENOS <exp_aritmetica> <exp_aritmetica_p>
                        |   MULTIPLICACION <exp_aritmetica> <exp_aritmetica_p>
                        |   DIVISION <exp_aritmetica> <exp_aritmetica_p>
                        |   MODULO <exp_aritmetica> <exp_aritmetica_p>
                        |   POTENCIA <exp_aritmetica> <exp_aritmetica_p>
                        |   BETWEEN <exp_aritmetica> AND <exp_aritmetica> <exp_aritmetica_p>
                        |   NOT BETWEEN <exp_aritmetica> AND <exp_aritmetica> <exp_aritmetica_p>
                        |   IN PARIZQUIERDO <lista_expresiones> PARDERECHO <exp_aritmetica_p>
                        |   NOT IN PARIZQUIERDO <lista_expresiones> PARDERECHO <exp_aritmetica_p>
                        |   IN <subquery>  <exp_aritmetica_p>
                        |   NOT IN <subquery> <exp_aritmetica_p>
                        |   LIKE <exp_aritmetica> <exp_aritmetica_p>
                        |   NOT LIKE <exp_aritmetica> <exp_aritmetica_p>
                        |   ILIKE <exp_aritmetica> <exp_aritmetica_p>
                        |   NOT ILIKE <exp_aritmetica> <exp_aritmetica_p>
                        |   SIMILAR TO <exp_aritmetica> <exp_aritmetica_p>
                        |   IS NULL <exp_aritmetica_p>
                        |   IS NOT NULL <exp_aritmetica_p>
                        |   <primitivo> <exp_aritmetica_p>
						| 	EMPTY


	<primitivo>  		::=   ID
						|	ID PUNTO ID
						|   MAS <primitivo>
                    	|   MENOS <primitivo>
                    	|   PARIZQUIERDO <exp_operacion> PARDERECHO
						|	ENTERO
						|	DECIMAL_
						|	CADENA
						|	TRUE
						|	FALSE
						|	<funcion>


	<update_table>     	::=	UPDATE ID SET <lista_seteos> PTCOMA
                        |   UPDATE ID SET <lista_seteos> WHERE <exp_operacion> PTCOMA


	<lista_seteos>     	::=	<set_columna> <lista_seteos_p>

	<lista_seteos_p>	::=	COMA <set_columna> <lista_seteos_p>
						| EMPTY


	<set_columna>    	::=	ID IGUAL <exp_operacion>


	<columnas> 			::=	<columna> <columnas_p>

	<columnas_p>		::= COMA <columna> <columnas_p>


    <columna> 			::= ID <tipos> <opcional>
						|	PRIMARY KEY PARIZQUIERDO <identificadores> PARDERECHO
						|	FOREIGN KEY PARIZQUIERDO <identificadores> PARDERECHO REFERENCES ID PARIZQUIERDO <identificadores> PARDERECHO
						|	UNIQUE PARIZQUIERDO <identificadores> PARDERECHO


	<opcional> 			::=	DEFAULT <opcionNull>
						|	<opcionNull>


	<opcionNull> 		::=	NOT NULL <opConstraint>
						|	<opConstraint>


	<opConstraint> 		::= CONSTRAINT ID <opUniqueCheck>
						| 	<opUniqueCheck>


	<opUniqueCheck> 	::=	UNIQUE
						| 	CHECK PARIZQUIERDO <condicion_check> PARDERECHO
						| 	empty


	<condicion_check> 	::=	ID MENOR_QUE <expresion>
                        | 	ID MENOR_IGUAL <expresion>
                        | 	ID MAYOR_QUE <expresion>
                        | 	ID MAYOR_IGUAL <expresion>
                        | 	ID DISTINTO <expresion>
                        | 	ID IGUAL <expresion>


	<herencia> 			::= INHERITS PARIZQUIERDO ID PARDERECHO'
						|	empty


	<identificadores> 	::= ID <identificadores_p>

	<identificadores_p>	::=	COMA ID <identificadores_p>
						| EMPTY

	<opReplace> 		::= OR REPLACE'
						|	empty


	<opExists> 			::= IF NOT EXISTS
						|	empty


	<opDatabase> 		::= OWNER <opIgual> ID <mode>
						|	mode


	<opIgual> 			::= IGUAL
						|	empty


	<mode> 				::= MODE <opIgual> ENTERO
						| 	empty


	<alter_instr> 		::= ALTER DATABASE ID <opAlterDatabase> PTCOMA
						|	ALTER TABLE ID <alter_table_instr> PTCOMA
	

	<opAlterDatabase> 	::= RENAME TO ID
						| 	OWNER TO <ownerList>

	<ownerList> 		::= ID
						|	CURRENT_USER
						|	SESSION_USER


	<alter_table_instr>	::= ADD <add_instr>
						|	<alter_columnas>
						|	<drop_columnas>


	<alter_columnas> 	::= <alter_columna> <alter_columnas_p>

	<alter_columnas_p>	::=	COMA <alter_columna> <alter_columnas_p>
						| EMPTY


	<alter_columna> 	::= ALTER COLUMN ID <alter_column_instr>


	<drop_columnas> 	::= <drop_columna> <drop_columnas_p>

	<drop_columnas_p>	::= COMA <drop_columna> <drop_columnas_p>
						| EMPTY


	<drop_columna> 		::= DROP COLUMN ID


	<alter_table_instr> ::= DROP CONSTRAINT ID
						| 	SET NOT NULL
						|	SET NULL
						|	TYPE ID


	<add_instr> 		::= CHECK PARIZQUIERDO <condicion_check> PARDERECHO
						|	CONSTRAINT ID UNIQUE PARIZQUIERDO ID PARDERECHO
						

	<drop_instr> 		::= DROP DATABASE <si_existe> ID PTCOMA
						|	DROP TABLE ID PTCOMA

	<si_existe> 		::= IF EXISTS
						|	empty

	<inst_select>  		::=	<select_query>
                    	|   <select_query> UNION <select_query>
	                    |   <select_query> UNION ALL <select_query>
	                    |   <select_query> INTERSECT <select_query>
	                    |   <select_query> INTERSECT ALL <select_query>
	                    |   <select_query> EXCEPT <select_query>
	                    |   <select_query> EXCEPT ALL <select_query>


	<select_query>     	::=	SELECT DISTINCT <select_list> FROM <from_query_list> <lista_condiciones_query>
                        |   SELECT <select_list> FROM <from_query_list> <lista_condiciones_query>
                        |   SELECT DISTINCT <select_list> FROM <from_query_list> 
                        |   SELECT <select_list> FROM <from_query_list>
                        |   SELECT <select_list>


	<select_list>  		::=	MULTIPLICACION
                    	|   <elementos_select_list>


	<elementos_select_list>	::=	<elemento_select> <elementos_select_list_p>

	<elementos_select_list_p>	::=	COMA <elemento_select> <elementos_select_list_p>
								|	EMPTY


	<elemento_select>  	::=	<dec_select_columna>
	 					|	<subquery> AS ID
                        |   <subquery> ID
                        |   <subquery>
						|	<funcion> AS ID
                        |   <funcion> ID
                        |   <funcion>

	<dec_select_columna>::=	ID PUNTO ID AS ID
                       	|   ID PUNTO ID ID
                       	|   ID PUNTO ID
                        |   ID


	<funcion>  			::=	<funcion_time>
		                |   <funcion_mate>
		                |   <funcion_trig>
		                |   <funcion_binstr>
		                |   <funcion_exprecion>
		                |   <funcion_agregacion>
		                |   <dec_case>

	<funcion_time> 		::=	EXTRACT PARIZQUIERDO <var_time> FROM <var_timeextract> CADENA PARDERECHO
	                    |   DATE_PART PARIZQUIERDO CADENA COMA <var_timeextract> CADENA PARDERECHO
	                    |   NOW PARIZQUIERDO PARDERECHO
	                    |   CURRENT_DATE
	                    |   CURRENT_TIME


	<var_time> 			::=	YEAR
		                |   MONTH
		                |   DAY
		                |   HOUR
		                |   MINUTE
		                |   SECOND


	<var_timeextract>  	::=	TIMESTAMP
                        |   TIME
                        |   DATE
                        |   INTERVAL


	<funcion_mate> 		::=	ABS PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   CBRT PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   CEIL PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   CEILING PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   DEGREES PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   DIV PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO
	                    |   EXP PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   FACTORIAL PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   FLOOR PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   GCD PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO
	                    |   LN PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   LOG PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   MOD PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO
	                    |   PI PARIZQUIERDO PARDERECHO
	                    |   POWER PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO
	                    |   RADIANS PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ROUND PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO
	                    |   SIGN PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   SQRT PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   WIDTH_BUCKET PARIZQUIERDO <exp_operacion> COMA <exp_operacion> COMA <exp_operacion> COMA <exp_operacion> PARDERECHO
	                    |   TRUNC PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   RANDOM PARIZQUIERDO <exp_operacion> PARDERECHO


    <funcion_trig> 		::=	ACOS PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ACOSD PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ASIN PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ASIND PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ATAN PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ATAND PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ATAN2 PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO
	                    |   ATAN2D PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO
	                    |   COS PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   COSD PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   SIN PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   SIND PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   TAN PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   TAND PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   SINH PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   COSH PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   TANH PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ASINH PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ACOSH PARIZQUIERDO <exp_operacion> PARDERECHO
	                    |   ATANH PARIZQUIERDO <exp_operacion> PARDERECHO


	<funcion_binstr>   	::=	LENGTH PARIZQUIERDO <exp_operacion> PARDERECHO
                        |   SUBSTRING PARIZQUIERDO <exp_operacion> COMA ENTERO COMA ENTERO PARDERECHO
                        |   TRIM PARIZQUIERDO <exp_operacion> PARDERECHO
                        |   MD5 PARIZQUIERDO <exp_operacion> PARDERECHO
                        |   SHA256 PARIZQUIERDO <exp_operacion> PARDERECHO
                        |   SUBSTR PARIZQUIERDO <exp_operacion> COMA ENTERO COMA ENTERO PARDERECHO
                        |   GET_BYTE PARIZQUIERDO <exp_operacion> COMA ENTERO PARDERECHO
                        |   SET_BYTE PARIZQUIERDO <exp_operacion> COMA ENTERO COMA ENTERO PARDERECHO
                        |   CONVERT PARIZQUIERDO <exp_operacion> AS <tipos> PARDERECHO
                        |   ENCODE PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO
                        |   DECODE PARIZQUIERDO <exp_operacion> COMA <exp_operacion> PARDERECHO


    <funcion_agregacion>::=	SUM PARIZQUIERDO <exp_operacion PARDERECHO
                      	|   COUNT PARIZQUIERDO <exp_operacion> PARDERECHO
                        |   COUNT PARIZQUIERDO MULTIPLICACION PARDERECHO
                        |   AVG PARIZQUIERDO <exp_operacion> PARDERECHO
                        |   MAX PARIZQUIERDO <exp_operacion> PARDERECHO
                        |   MIN PARIZQUIERDO <exp_operacion> PARDERECHO


	<funcion_exprecion>	::=	GREATEST PARIZQUIERDO <lista_exp> PARDERECHO
                       	|   LEAST PARIZQUIERDO <lista_exp> PARDERECHO


    <dec_case> 			::=	CASE <lista_when_case> ELSE <exp_operacion> END
                		|   CASE <lista_when_case> END


	<lista_when_case>	::=	<clausula_case_when> <lista_when_case_p>

	<lista_when_case_p>	::=	<clausula_case_when> <lista_when_case_p>
						| 	EMPTY


	<clausula_case_when>::=	WHEN <exp_operacion> THEN <exp_operacion>


	<from_query_list>	::=	<from_query_element> <from_query_list_p>

	<from_query_list_p>	::=	COMA <from_query_element> <from_query_list_p>
						|	EMPTY


	<from_query_element>::=	<dec_id_from>
                      	|   <subquery> AS ID
                       	|   <subquery> ID
                       	|   <subquery>


	<dec_id_from>  		::=	ID AS ID
	                    |   ID ID
	                    |   ID


    <lista_condiciones_query>	::=	<condicion_query> <lista_condiciones_query_p>


	<lista_condiciones_query_p>	::=	<condicion_query> <lista_condiciones_query_p>
								| 	EMPTY


	<condicion_query> 	::=	WHERE <exp_operacion>
                        |   GROUP BY <lista_ids>
                        |   HAVING <exp_operacion>
                        |   ORDER BY <lista_order_by>
                        |   LIMIT <condicion_limit> OFFSET <exp_operacion>
                        |   LIMIT <condicion_limit>


	<condicion_limit>  	::=	<exp_operacion>
						|	ALL

	<lista_ids>    		::=	<dec_select_columna> <lista_ids_p>

	<lista_ids_p>		::=	COMA <dec_select_columna> <lista_ids_p>
						|	EMPTY 

	<lista_order_by>   	::=	<elemento_order_by> <lista_order_by_p>

	<lista_order_by_p>	::=	COMA <elemento_order_by> <lista_order_by_p>
						|	EMPTY


	<elemento_order_by>	::=	<exp_operacion> <asc_desc> NULLS <condicion_null>
						|	<exp_operacion> <asc_desc>

	<asc_desc> 			::=	ASC
                		|   DESC


	<condicion_null>   	::=	FIRST
                        |   LAST


	<subquery> 			::=	PARIZQUIERDO <select_query> PARDERECHO


	<lista_exp>    		::=	<exp_operacion> <lista_exp_p>

	<lista_exp_p>		::=	COMA <exp_operacion> <lista_exp_p>
						|	EMPTY


	<tipos> 			::=	SMALLINT
                        | INTEGER
                        | BIGINIT
                        | DECIMAL
                        | NUMERIC
                        | REAL
                        | DOUBLE
                        | MONEY
                        | VARCHAR
                        | CHARACTER
                        | TEXT
                        | TIMESTAMP
                        | TIME
                        | DATE
                        | INTERVAL
                        | BOOLEAN