# Reporte de la gramática elegida para el análisis sintáctico en el proyecto.

##### A continuación se presentarán dos gramáticas una ascendente y otra descendente y una conclusión de cual se eligió y las razones de dicha elección.

#### Gramática BNF Descendente
```sh
<init>	::= <instrucciones>

<instrucciones>	::= <instrucciones> <instruccion>
				| <instruccion>

<instruccion>	::= CREATE <creacion>
				| SHOW <show_db> PTCOMA
				| ALTER DATABASE <alter_database> PTCOMA
				| USE <cambio_bd>
				| SELECT <selects>
				| DELETE <deletes>
				| ALTER TABLE <alter_table> PTCOMA
				| UPDATE <update_table> PTCOMA
				| INSERT <insercion>
				| DROP <dropear>
#=================================================
#ELEMENTOS BÁSICOS
<lista_id>	::= <lista_id> COMA ID
			| ID

<tipos>	::= SMALLINT
		| INTEGER
		| BIGINT
		| R_DECIMAL
		| NUMERIC
		| REAL
		| DOUBLE PRECISION
		| MONEY
		| TEXT
		| TIMESTAMP
		| DATE
		| TIME
		| BOOLEAN
		| INTERVAL
		| CHARACTER VARING PARIZQ ENTERO PARDER
		| VARCHAR PARIZQ ENTERO PARDER
		| CHARACTER PARIZQ ENTERO PARDER
		| CHAR PARIZQ ENTERO PARDER
		| TIMESTAMP <def_dt_types>
		| TIME <def_dt_types>
		| INTERVAL <def_interval>

<def_dt_types>	::= PARIZQ ENTERO PARDER WITHOUT TIME ZONE
				| PARIZQ ENTERO PARDER WITH TIME ZONE
				| PARIZQ ENTERO PARDER
				| WITHOUT TIME ZONE
				| WITH TIME ZONE

<def_interval>	::= <def_fld_to> PARIZQ ENTERO PARDER
				| <def_fld_to>
				| PARIZQ ENTERO PARDER

<def_fld_to>	::= <def_fields> TO <def_fields>
				| <def_fields>

<def_fields>	::= YEAR
				| MONTH
				| DAY
				| HOUR
				| MINUTE
				| SECOND

<relacional>	::= <aritmetica> MENOR <aritmetica>
				| <aritmetica> MAYOR <aritmetica>
				| <aritmetica> IGUAL IGUAL <aritmetica>
				| <aritmetica> MENORIGUAL <aritmetica>
				| <aritmetica> MAYORIGUAL <aritmetica>
				| <aritmetica> DIFERENTE <aritmetica>
				| <aritmetica> NO_IGUAL <aritmetica>
				| <aritmetica> IGUAL <aritmetica>
				| <aritmetica>
				| <relacional> AND <relacional>
				| <relacional> OR <relacional>
				| NOT <relacional>
				| EXISTS <state_subquery>
				| IN <state_subquery>
				| NOT IN <state_subquery>
				| ANY <state_subquery>
				| ALL <state_subquery>
				| SOME <state_subquery>
				| <state_between>
				| <state_predicate_nulls>
				| <state_is_distinct>
				| <state_pattern_match>

<aritmetica>	::= <aritmetica> MAS <aritmetica>
				| <aritmetica> MENOS <aritmetica>
				| <arimtetica> POR <aritmetica>
				| <aritmetica> DIVISION <aritmetica>
				| <aritmetica> MODULO <aritmetica>
				| <aritmetica> EXP <aritmetica>
				| <valor>
				| PARIZQ <aritmetica> PARDER
				| <funciones_math_esenciales>
				| <lista_funciones>
				| <fun_binario_select>
				| <fun_trigonometrica>

<valor>	::= ID
		| ENTERO
		| DECIMAL
		| <date_functions>
		| CADENA
		| ID PUNT ID
		| <lista_funciones_where>
		| <fun_binario_where>
		| <state_subquery>	

<state_between>	::= <valor> BETWEEN <valor> AND <valor>
				| <valor> NOT BETWEEN <valor> AND <valor>
				| <valor> NOT IN <state_subquery>

<state_predicate_nulls>	::= <valor> IS NULL
						| <valor> IS NOT NULL
						| <valor> ISNULL
						| <valor> NOTNULL

<state_is_distinct>	::= <valor> IS DISTINCT FROM <valor> <state_aliases_table>
						| <valor> IS NOT DISTINCT FROM <valor> <state_aliases_table>

<state_aliases_table>	::= AS ID
						| ID
						|

<state_pattern_match>	::= <aritmetica> LIKE CADENA
						| <aritmetica> LIKE CADENA_DOBLE

<funciones_math_esenciales>	::= COUNT PARIZQ <lista_funciones_math_esenciales> PARDER <parametro>
							| COUNT PARIZQ <lista_funciones_math_esenciales> PARDER
							| SUM PARIZQ <lista_funciones_math_esenciales> PARDER <parametro>
							| SUM PARIZQ <lista_funciones_math_esenciales> PARDER
							| AVG PARIZQ <lista_funciones_math_esenciales> PARDER <parametro>
							| AVG PARIZQ <lista_funciones_math_esenciales> PARDER

<lista_funciones_math_esenciales>	::= <aritmetica>
									| <lista_id>
									| POR

<parametro>	::= ID PUNTO ID
				| <lista_funciones>
				| <funciones_math_esenciales>
				| <fun_binario_select>
				| <date_functions>
				| <state_subquery>
				| CADENA
				| DECIMAL
				| ENTERO
				| ID

<lista_funciones>	::= ABS PARIZQ <funcion_math_parametro>	PARDER
					| CBRT PARIZQ <funcion_math_parametro> PARDER
					| CEIL PARIZQ <funcion_math_parametro> PARDER
					| CEILING PARIZQ <funcion_math_parametro> PARDER
					| DEGREES PARIZQ <funcion_math_parametro> PARDER
					| DIV PARIZQ <funcion_math_parametro> PARDER
					| EXP PARIZQ <funcion_math_parametro> PARDER
					| FACTORIAL PARIZQ <funcion_math_parametro> PARDER
					| FLOOR PARIZQ <funcion_math_parametro> PARDER
					| GCD PARIZQ <funcion_math_parametro> PARDER
					| LN PARIZQ <funcion_math_parametro> PARDER
					| LOG PARIZQ <funcion_math_parametro> PARDER
					| MOD PARIZQ <funcion_math_parametro> PARDER
					| PI PARIZQ PARDER
					| POWER PARIZQ <funcion_math_parametro> COMA ENTERO PARDER
					| RADIANS PARIZQ <funcion_math_parametro> PARDER
					| ROUND PARIZQ <funcion_math_parametro> PARDER
					| SIGN PARIZQ <funcion_math_parametro> PARDER
					| SQRT PARIZQ <funcion_math_parametro> PARDER
					| WIDTH_BUCKET PARIZQ <funcion_math_parametro> COMA <funcion_math_parametro> COMA <funcion_math_parametro> COMA <funcion_math_parametro> PARDER
					| TRUNC PARIZQ <funcion_math_parametro> PARDER
					| RANDOM PARIZQ PARDER

<lista_funciones_where>	::= ABS PARIZQ <funcion_math_parametro> PARDER
						| CBRT PARIZQ <funcion_math_parametro> PARDER
						| CEIL PARIZQ <funcion_math_parametro> PARDER
						| CEILING PARIZQ <funcion_math_parametro PARDER

<funcion_math_parametro>	::= ENTERO
							| ID
							| DECIMAL
							| <funcion_math_parametro_negativo>

<funcion_math_parametro_negativo>	::= MENOS DECIMAL
									| MENOS ENTERO

<fun_binario_select>	::= LENGTH PARIZQ <valor> PARDER
						| SUBSTRING PARIZQ <valor> COMA ENTERO COMA ENTERO PARDER
						| TRIM PARIZQ CADENA FROM <valor> PARDER
						| SHA256 PARIZQ <valor> PARDER
						| SUBSTR PARIZQ <valor> COMA ENTERO COMA ENTERO PARDER
						| GET_BYTE PARIZQ <valor> DOS_PUNTOS DOS_PUNTOS BYTEA COMA ENTERO PARDER
						| GET_BYTE PARIZQ <valor> COMA ENTERO PARDER
						| SET_BYTE PARIZQ <valor> DOS_PUNTOS DOS_PUNTOS BYTEA COMA ENTERO COMA ENTERO PARDER
						| SET_BYTE PARIZQ <valor> COMA ENTERO COMA ENTERO PARDER
						| CONVERT PARIZQ <valor> AS <tipos> PARDER
						| ENCODE PARIZQ <valor> DOS_PUNTOS DOS_PUNTOS BYTEA COMA CADENA PARDER
						| ENCODE PARIZQ <valor> COMA CADENA PARDER
						| DECODE PARIZQ <valor> COMA CADENA PARDER

<fun_trigonometrica>	::= ACOS PARIZQ <aritmetica> PARDER
						| ASIN PARIZQ <aritmetica> PARDER
						| ATAN PARIZQ <aritmetica> PARDER
						| ATAN2 PARIZQ <aritmetica> COMA <aritmetica> PARDER
						| COS PARIZQ <aritmetica> PARDER
						| COT PARIZQ <aritmetica> PARDER
						| SIN PARIZQ <aritmetica> PARDER
						| TAN PARIZQ <aritmetica> PARDER
						| ACOSD PARIZQ <aritmetica> PARDER
						| ASIND PARIZQ <aritmetica> PARDER
						| ATAND PARIZQ <aritmetica> PARDER
						| ATAN2D PARIZQ <aritmetica> COMA <aritmetica> PARDER
						| COSD PARIZQ <aritmetica> PARDER
						| COTD PARIZQ <aritmetica> PARDER
						| SIND PARIZQ <aritmetica> PARDER
						| TAND PARIZQ <aritmetica> PARDER
						| SINH PARIZQ <aritmetica> PARDER
						| COSH PARIZQ <aritmetica> PARDER
						| TANH PARIZQ <aritmetica> PARDER
						| ASINH PARIZQ <aritmetica> PARDER
						| ACOSH PARIZQ <aritmetica> PARDER
						| ATANH PARIZQ <aritmetica> PARDER

<date_functions>	::= EXTRACT PARIZQ <lista_date_functions>
^					| <date_part> PARIZQ <lista_date_functions>
					| NOW PARIZQ <lista_date_functions>
					| <lista_date_functions>

<lista_date_functions>	::= <def_fields> FROM TIMESTAMP CADENA PARDER PTCOMA
						| CADENA COMA INTERVAL CADENA PARDER
						| TIMESTAMP CADENA
						| CURRENT_DATE
						| CURRENT_TIME
						| PARDER

<state_subquery>	::= PARIZQ SELECT selects PARDER
#=================================================

#=================================================
#INSTRUCCIONES DE CREACIÓN

<creacion>	::= DATABASE <crear_bd>
			| OR REPLACE DATABASE <crear_bd>
			| TABLE <crear_tb>
			| TYPE <crear_type>

<crear_bd>	::= ID PTCOMA
			| ID <lista_parametros_bd> PTCOMA
			| IF NOT EXISTS ID PTCOMA
			| IF NOT EXISTS ID <lista_parametros_bd> PTCOMA

<lista_parametros_bd>	::= <parametros_bd>
						| <parametros_bd> <parametros_bd>

<parametros_bd>	::= OWNER IGUAL ID
				| OWNER ID
				| MODE IGUAL ENTERO
				| MODE ENTERO

<crear_tb>	::= ID PARIZQ <crear_tb_columnas> PARDER <tb_herencia> PTCOMA
			| ID PARIZQ <crear_tb_columnas> PARDER PTCOMA

<tb_herencia>	::= INHERITS PARIZQ ID PARDER

<crear_tb_columnas>	::= <crear_tb_columnas> COMA <crear_tb_columna>
					| <crear_tb_columna>

<crear_tb_columna>	::= ID <tipos> <parametros_columna>
					| ID <tipos>
					| PRIMARY KEY PARIZQ <lista_id> PARDER
					| FOREIGN KEY PARIZQ <lista_id> PARDER REFERENCES ID PARIZQ <lista_id> PARDER
					| <chequeo>
					| UNIQUE PARIZQ <lista_id> PARDER

<chequeo>	::= CONSTRAINT ID CHECK PARIZQ <relacional> PARDER
			| CHECK PARIZQ <relacional> PARDER

<parametros_columna>	::= <parametros_columna> <parametro_columna>
						| <parametro_columna>

<parametro_columna>	::= <unul>
					| <unic>
					| <chequeo>
					| PRIMARY KEY 
					| DEFAULT <valor>
					| REFERENCES ID

<unul>	::= NULL
		| NOT NULL

<unic> ::= CONSTRAINT ID UNIQUE
		| UNIQUE


<crear_type>	::= ID AS ENUM PARIZQ <lista_objetos> PARDER PTCOMA

#=================================================

#=================================================
#INSTRUCCIONES DE SHOW DATABASE

<show_db> 	::= DATABASES
			| DATABASES LIKE CADENA

#=================================================

#=================================================
#INSTRUCCIONES DE ALTER DATABASE

<alter_database>	::= ID RENAME ID
					| ID OWNER TO <def_alter_db>

<def_alter_db>	::= ID
				| CURRENT_USER
				| SESSION_USER
#=================================================

#=================================================
#INSTRUCCIONES DE USE DATABASE

<cambio_db>	::= ID PTCOMA

#=================================================

#=================================================
# INSTRUCCIONES DE SELECT

<selects>	::= POR FROM <select_all>
			| POR FROM <state_subquery> <inicio_condicional>
			| <lista_parametros> FROM <lista_parametros> <inicio_condicional>
			| <lista_parametros> COMA CASE <case_state> FROM <lista_parametros> <inicio_condicional>
			| <lista_parametros> PTCOMA
			| GREATEST PARIZQ <lista_parametros> PARDER PTCOMA
			| LEAST PARIZQ <lista_parametros> PARDER PTCOMA
			| <fun_trigonometrica> <state_aliases_field> PTCOMA
			| <fun_trigonometrica> <state_aliases_field> FROM ID <state_aliases_table> PTCOMA
			| DISTINCT POR FROM <select_all>
			| DISTINCT <lista_parametros> FROM <lista_parametros> <inicio_condicional>
			| DISTINCT <lista_parametros> PTCOMA
			| DISTINCT <lista_parametros> COMA CASE <case_state> FROM <lista_parametros> <inicio_condicional>

<select_all>	::= ID <state_aliases_table> <inicio_condicional>

<inicio_condicional>	::= WHERE <relacional> <inicio_group_by>
						| <inicio_group_by>

<inicio_group_by>	::= GROUP BY <lista_parametros> <inicio_having>
					| <inicio_order_by>

<inicio_having>	::= HAVING <relacional> <inicio_order_by>
				| <inicio_order_by>

<inicio_order_by>	::= ORDER BY <sorting_rows>	<state_limit>
					| <state_limit>

<sorting_rows>	::= <sorting_rows> COMA <sort>
				| <sort>

<sort>	::= ID ASC
		| ID DESC
		| ID

<state_limit>	::= LIMIT ENTERO <state_offset>
				| LIMIT ALL <state_offset>
				| <state_offset>

<state_offset>	::= OFFSET ENTERO <state_union>
				| OFFSET ENTERO <state_intersect>
				| OFFSET ENTERO <state_except>
				| <state_union>
				| <state_intersect>
				| <state_except>
				| <state_subquery>

<state_union>	::= UNION SELECT <selects>
				| UNION ALL SELECT <selects>
				| PTCOMA

<state_intersect>	::= INTERSECT SELECT <selects>
					| INTERSECT ALL SELECT <selects>
					| PTCOMA

<state_except>	::= EXCEPT SELECT <selects>
				| EXCEPT ALL SELECT <selects>
				| PTCOMA

<lista_parametros>	::= <lista_parametros> COMA <parametro> <state_aliases_field>
					| <parametro> <state_aliases_field>

<state_aliases_field>	::= AS CADENA
						| AS CADNEA_DOBLE
						| AS ID
						|

<case_state>	::= <case_state> <auxcase_state> END
				| <auxcase_state> END

<auxcase_state>	::= WHEN <relacional> THEN CADENA
				| ELSE COMILLA_SIMPLE ID COMILLA_SIMPLE
#=================================================

#=================================================
#INSTRUCCIONES DE DELETE
<deletes>	::= <delete_condicional>
			| <delete_incondicional>

<delete_condicional> ::= ID WHERE <relacional> PTCOMA

<delete_incondicional> ::= ID PTCOMA

#=================================================

#=================================================
#INSTRUCCIONES DE ALTER TABLE
<alter_table>	::= ID <def_alter>

<def_alter>	::= ADD COLUMN ID <tipos>
			| ADD CHECK PARIZQ <relacional> PARDER
			| ADD CONSTRAINT ID UNIQUE PARIZQ ID PARDER
			| ADD FOREIGN KEY PARIZQ <lista_parametros> 
			| DROP COLUMN ID
			| DROP CONSTRAINT ID
			PARDER REFERENCES PARIZQ <lista_parametros> PARDER
			| ALTER COLUMN ID SET NOT NULL
			| RENAME COLUMN ID TO ID

#=================================================

#=================================================
#INSTRUCCIONES DE UPDATE

<update_table>	::= ID SET <def_update> WHERE <relacional>
				| ID SET <def_update>

<def_update>	::= <def_update> COMA ID IGUAL <valor>
				| ID IGUAL <valor>

#=================================================

#=================================================
#INSTRUCCIONES DE INSERT

<insercion>	::= INTO ID PARIZQ <lista_id> PARDER VALUES PARIZQ <lista_insercion> PARDER PTCOMA
			| INTO ID VALUES PARIZQ <lista_insercion> PARDER PTCOMA

<lista_insercion>	::= <lista_insercion> COMA <objeto>
					| <lista_insercion> COMA PARIZQ SELECT <selects> PARDER
					| <objeto>
					| PARIZQ SELECT <selects> PARDER

<objeto>	::= <valor>

#=================================================

#=================================================
#INSTRUCCIONES DE DROP

<dropear>	::= DATABASE IF EXISTS ID PTCOMA
			| DATABASE ID PTCOMA
			| TABLE ID PTCOMA

#=================================================
```

#### Gramática BNF Ascendente
```sh
<init>	::= <instrucciones>

<instrucciones>	::= <instruccion> <instrucciones1>

<instrucciones1>	::= <instruccion> <instrucciones1>
					|

<instruccion>	::= CREATE <creaccion> PTCOMA
				| SHOW <show_db> PTCOMA
				| ALTER DATABASE <alter_database> PTCOMA
				| USE <cambio_bd> PTCOMA
				| SELECT <selects> PTCOMA
				| DELETE <deletes> PTCOMA
				| ALTER TABLE <alter_table> PTCOMA
				| UPDATE <update_table> PTCOMA
				| INSERT <insercion> PTCOMA
				| DROP <dropear> PTCOMA
#=================================================
#ELEMENTOS BÁSICOS
<lista_id>	::= ID <lista_id1>

<lista_id1> ::= COMA ID <lista_id1>
			|

<tipos>	::= SMALLINT
		| INTEGER
		| BIGINT
		| R_DECIMAL
		| NUMERIC
		| REAL
		| DOBULE PRECISION
		| MONEY
		| TEXT
		| TIMESTAMP
		| DATE
		| TIME
		| BOOLEAN
		| INTERVAL
		| CHARACTER VARING PARIZQ ENTERO PARDER
		| VARCHAR PARIZQ ENTERO PARDER
		| CHARACTER PARIZQ ENTERO PARDER
		| CHAR PARIZQ ENTERO PARDER
		| TIMESTAMP <def_dt_types>
		| TIME <def_dt_types>
		| INTERVAL <def_interval>

<def_dt_types>	::= PARIZQ ENTERO PARDER <with_time_zone>
				| WITHOUT TIME ZONE
				| WITH TIME ZONE

<with_time_zone>	::= WITHOUT TIME ZONE
					| WITH TIME ZONE
					|

<def_interval>	::= <def_fld_to> <def_interval_param>
				| PARIZQ ENTERO PARDER

<def_interval_param>	::= PARIZQ ENTERO PARDER
						|

<def_fld_to>	::= <def_fields> <to_def_fields>

<to_def_fields>	::= TO <def_fields>
				|

<def_fields>	::= YEAR
				| MONTH
				| DAY
				| HOUR
				| MINUTE
				| SECOND

<relacional>	::= <aritmetica> <continuacion_relacional_aritmetica> <relacional1>
				| NOT <relacional> <relacional1>
				| EXISTS <state_subquery <relacional1>
				| IN <state_subquery> <relacional1>
				| NOT IN <state_subquery> <relacional1>
				| ANY <state_subquery> <relacional1>
				| ALL <state_subquery> <relacional1>
				| SOME <state_subquery> <relacional1>
				| <state_between> <relacional1>
				| <state_predicate_nulls> <relacional1>
				| <state_is_distinct> <relacional1>
				| <state_pattern_match> <relacional1>

<relacional1>	::= AND <relacional1>
				| OR <relacional1>
				|

<continuacion_relacional_aritmetica>	::= MENOR <aritmetica>
										| MAYOR <aritmetica>
										| IGUAL IGUAL <aritmetica>
										| MENORIGUAL <aritmetica>
										| MAYORIGUAL <aritmetica>
										| DIFERENTE <aritmetica>
										| NO_IGUAL <aritmetica>
										| IGUAL <aritmetica>
										|

<aritmetica>	::= <valor> <aritmetica1>
				| PARIZQ <aritmetica> PARDER <aritmetica1>
				| <funciones_math_esenciales> <aritmetica1>
				| <lista_funciones> <aritmetica1>
				| <fun_binario_select> <aritmetica1>
				| <fun_trigonometrica> <aritmetica1>

<aritmetica1>	::= MAS <aritmetica> <aritmetica1>
				| MENOS <aritmetica> <aritmetica1>
				| POR <aritmetica> <aritmetica1>
				| DIVISON <aritmetica> <aritmetica1>
				| MODULO <aritmetica> <aritmetica1>
				| EXP <aritmetica> <aritmetica1>
				|

<valor>	::= ID <punto_id>
		| ENTERO
		| DECIMAL
		| <date_functions>
		| CADENA
		| <lista_funciones_where>
		| <fun_binario_where>
		| <state_subquery>

<state_between>	::= <valor> <continuacion_state_between>

<continuacion_state_between> ::= BETWEEN <valor> AND <valor>
							 | NOT <between_in>

<between_in>	::= BETWEEN <valor> AND <valor>
				| IN <state_subquery>

<state_predicate_nulls>	::= <valor> <nules>

<nules>	::= ISNULL
		| NOTNULL
		| IS <unul>

<state_is_distinct>	::= <valor> IS <state_is_distinct_notis>

<state_is_distinct_notis>	::= DISTINCT FROM <valor> <state_aliases_table>
							| NOT DISTINCT FROM <valor> <state_aliases_table>

<state_aliases_table> ::= AS ID
						| ID
						|

<state_pattern_match>	::= <aritmetica> LIKE <cadenas>

<cadenas>	::= CADENA
			| CADENA_DOBLE

<funciones_math_esenciales>	::= COUNT PARIZQ <lista_funciones_math_esenciales> PARDER <o_parametro>
							| SUM PARIZQ <lista_funciones_math_esenciales> PARDER <o_parametro>
							| AVG PARIZQ <lista_funciones_math_esenciales> PARDER <o_parametro>

<o_paramtero>	::= <parametro>
				|

<lista_funciones_math_esenciales>	::= <aritmetica>
									| <lista_id>
									| POR

<parametro>	::= ID <punto_id>
			| <lista_funciones>
			| <funciones_math_esenciales>
			| <fun_binario_select>
			| <date_functions>
			| <state_subquery>
			| CADENA
			| DECIMAL
			| ENTERO

<lista_funciones>	::= ABS PARIZQ <funcion_math_parametro>	PARDER
					| CBRT PARIZQ <funcion_math_parametro> PARDER
					| CEIL PARIZQ <funcion_math_parametro> PARDER
					| CEILING PARIZQ <funcion_math_parametro> PARDER
					| DEGREES PARIZQ <funcion_math_parametro> PARDER
					| DIV PARIZQ <funcion_math_parametro> PARDER
					| EXP PARIZQ <funcion_math_parametro> PARDER
					| FACTORIAL PARIZQ <funcion_math_parametro> PARDER
					| FLOOR PARIZQ <funcion_math_parametro> PARDER
					| GCD PARIZQ <funcion_math_parametro> PARDER
					| LN PARIZQ <funcion_math_parametro> PARDER
					| LOG PARIZQ <funcion_math_parametro> PARDER
					| MOD PARIZQ <funcion_math_parametro> PARDER
					| PI PARIZQ PARDER
					| POWER PARIZQ <funcion_math_parametro> COMA ENTERO PARDER
					| RADIANS PARIZQ <funcion_math_parametro> PARDER
					| ROUND PARIZQ <funcion_math_parametro> PARDER
					| SIGN PARIZQ <funcion_math_parametro> PARDER
					| SQRT PARIZQ <funcion_math_parametro> PARDER
					| WIDTH_BUCKET PARIZQ <funcion_math_parametro> COMA <funcion_math_parametro> COMA <funcion_math_parametro> COMA <funcion_math_parametro> PARDER
					| TRUNC PARIZQ <funcion_math_parametro> PARDER
					| RANDOM PARIZQ PARDER

<lista_funciones_where>	::= ABS PARIZQ <funcion_math_parametro> PARDER
						| CBRT PARIZQ <funcion_math_parametro> PARDER
						| CEIL PARIZQ <funcion_math_parametro> PARDER
						| CEILING PARIZQ <funcion_math_parametro PARDER

<funcion_math_parametro>	::= ENTERO
							| ID
							| DECIMAL
							| <funcion_math_parametro_negativo>

<funcion_math_parametro_negativo>	::= MENOS <dec_o_ent>

<dec_o_ent>	::= DECIMAL
			| ENTERO

<fun_binario_select>	::= LENGTH PARIZQ <valor> PARDER
						| SUBSTRING PARIZQ <valor> COMA ENTERO COMA ENTERO PARDER
						| TRIM PARIZQ CADENA FROM <valor> PARDER
						| SHA256 PARIZQ <valor> PARDER
						| SUBSTR PARIZQ <valor> COMA ENTERO COMA ENTERO PARDER
						| GET_BYTE PARIZQ <valor> <bytea> DOS_PUNTOS DOS_PUNTOS BYTEA COMA ENTERO PARDER
						| GET_BYTE PARIZQ <valor> COMA ENTERO PARDER
						| SET_BYTE PARIZQ <valor> DOS_PUNTOS DOS_PUNTOS BYTEA COMA ENTERO COMA ENTERO PARDER
						| SET_BYTE PARIZQ <valor> COMA ENTERO COMA ENTERO PARDER
						| CONVERT PARIZQ <valor> AS <tipos> PARDER
						| ENCODE PARIZQ <valor> DOS_PUNTOS DOS_PUNTOS BYTEA COMA CADENA PARDER
						| ENCODE PARIZQ <valor> COMA CADENA PARDER
						| DECODE PARIZQ <valor> COMA CADENA PARDER

<bytea>	::= DOS_PUNTOS DOS_PUNTOS BYTEA
		|

<fun_trigonometrica>	::= ACOS PARIZQ <aritmetica> PARDER
						| ASIN PARIZQ <aritmetica> PARDER
						| ATAN PARIZQ <aritmetica> PARDER
						| ATAN2 PARIZQ <aritmetica> COMA <aritmetica> PARDER
						| COS PARIZQ <aritmetica> PARDER
						| COT PARIZQ <aritmetica> PARDER
						| SIN PARIZQ <aritmetica> PARDER
						| TAN PARIZQ <aritmetica> PARDER
						| ACOSD PARIZQ <aritmetica> PARDER
						| ASIND PARIZQ <aritmetica> PARDER
						| ATAND PARIZQ <aritmetica> PARDER
						| ATAN2D PARIZQ <aritmetica> COMA <aritmetica> PARDER
						| COSD PARIZQ <aritmetica> PARDER
						| COTD PARIZQ <aritmetica> PARDER
						| SIND PARIZQ <aritmetica> PARDER
						| TAND PARIZQ <aritmetica> PARDER
						| SINH PARIZQ <aritmetica> PARDER
						| COSH PARIZQ <aritmetica> PARDER
						| TANH PARIZQ <aritmetica> PARDER
						| ASINH PARIZQ <aritmetica> PARDER
						| ACOSH PARIZQ <aritmetica> PARDER
						| ATANH PARIZQ <aritmetica> PARDER

<date_functions>	::= EXTRACT PARIZQ <lista_date_functions>
					| <date_part> PARIZQ <lista_date_functions>
					| NOW PARIZQ <lista_date_functions>
					| <lista_date_functions>

<lista_date_functions>	::= <def_fields> FROM TIMESTAMP CADENA PARDER PTCMA
						| CADENA COMA INTERVAL CADENA PARDER
						| TIMESTAMP CADENA
						| CURRENT_TIME
						| CURRENT_DATE
						| PARDER

<state_subquery>	::= PARIZQ SELECT selects PARDER
#=================================================

#=================================================
#INSTRUCCIONES DE CREACIÓN

<creacion>	::= DATABASE <crear_bd>
			| OR REPLACE DATABASE <crear_bd>
			| TABLE <crear_tb>
			| TYPE <crear_type>

<crear_db>	::= ID <lista_parametros_bd>
			| IF NOT EXISTS <lista_parametros_bd>

<lista_parametros_bd>	::= <parametros_bd> <lista_parametros_bd1>
						|

<lista_parametros_bd1>	::= <parametros_bd> <lista_parametros_bd1>
						|

<parametros_bd>	::= OWNER <igual> ID
				| MODE <igual> ENTERO

<igual>	::= IGUAL
		|

<crear_tb>	::= ID PARZIQ <crear_tb_columnas> PARDER <tb_herencia>

<tb_herencia>	::= INHERITS PARIZQ ID PARDER
				|

<crear_tb_columnas>	::= <crear_tb_columna> <crear_tb_columnas1>

<crear_tb_columnas1>	::= COMA <crear_tb_columna> <crear_tb_columnas1>
						|

<crear_tb_columna>	::= ID <tipos> <parametros_columna>
					| PRIMARY KEY PARIZQ <lista_id> PARDER
					| FOREIGN KEY PARIZQ <lista_id> PARDER
					| <chequeo>
					| UNIQUE PARIZQ <lista_id> PARDER

<chequeo>	::= CONSTRAINT ID CHECK PARIZQ <relacional> PARDER
			| CHECK PARIZQ <relacional> PARDER

<parametros_columna>	::= <parametro_columna> <parametros_columna>
						|

<parametro_columna>	::= <unul>
					| <unic>
					| <chequeo>
					| PRIMARY KEY
					| DEFAULT <valor>
					| REFERENCES ID

<unul>	::= NULL
		| NOT NULL

<unic>	::= CONSTRAINT ID UNIQUE
		| UNIQUE

<crear_type>	::= ID AS ENUM PARIZQ <lista_objetos> PARDER

#=================================================

#=================================================
#INSTRUCCIONES DE SHOW DATABASE

<show_db>	::= DATABASES <like_cadena>

<like_cadena>	::= LIKE CADENA
				|

#=================================================

#=================================================
#INSTRUCCIONES DE ALTER DATABASE

<alter_database>	::= ID <rename_owner>

<rename_owner>	::= RENAME ID
				| OWNER TO <def_alter_db>

<def_alter_db>	::= ID
				| CURRENT_USER
				| SESION_USER
#=================================================

#=================================================
#INSTRUCCIONES DE USE DATABASE

<cambio_db>	::= ID

#=================================================

#=================================================
#INSTRUCCIONES DE SELECT
<selects>	::= POR FROM <select_o_state>
			| <lista_parametros> <from_o_coma>
			| GREATEST PARIZQ <lista_parametros> PARDER
			| LEAST PARIZQ <lista_parametros> PARDER
			| <fun_trigonometrica> <state_aliases_field> <from_ep>
			| DISTINCT <por_lista_parametros>

<select_o_state>	::= <select_all>
					| <state_subquery> <inicio_condicional>

<from_o_coma>	::= FROM <lista_parametros> <inicio_condicional>
				| COMA CASE <case_state> FROM <lista_parametros> <inicio_condicional>
				|

<from_ep>	::= FROM ID <state_aliases_table>
			|

<por_lista_parametros>	::= POR FROM <select_all>
						| <lista_parametros> <from_ep_distinct>

<from_ep_distinct>	::= FROM <lista_parametros> <inicio_condicional>
					| COMA CASE <case_state> FROM <lista_parametros> <inicio_condicional>
					|

<select_all>	::= ID <state_aliases_table> <inicio_condicional>

<inicio_condicional>	::= WHERE <relacional> <inicio_group_by>
						| <inicio_group_by>

<inicio_group_by>	::= GROUP BY <lista_parametros> <inicio_having>
					| <incio_order_by>

<inicio_having>	::= HAVING <relacional> <inicio_order_by>
				| <inicio_order_by>

<inicio_order_by>	::= ORDER BY <sorting_rows> <state_limit>
					| <state_limit>

<sorting_rows>	::= <sort> <sorting_rows1>

<sorting_rows1>	::= COMA <sort> <sorting_rows1>
				|

<sort>	::= ID <asc_desc>

<asc_desc>	::= ASC
			| DESC
			|

<state_limit>	::= LIMIT <all_entero>
				| <state_offset>

<all_entero>	::= ENTERO <state_offset>
				| ALL <state_offset>

<state_offset>	::= OFFSET ENTERO <state_offset_opciones>
				| <state_offset_opciones>
				| <state_subquery>

<state_offset_opciones>	::= <state_union>
						| <state_intersect>
						| <state_except>

<state_union>	::= UNION <state_opciones>
				|

<state_intersect>	::= INTERSECT <state_opciones>
					|

<state_except>	::= EXCEPT <state_opciones>
				|

<state_opciones>::= SELECT <selects>
				| ALL SELECT <selects>

<lista_parametros>	::= <parametro> <state_aliases_field> <lista_parametros1>

<lista_parametros1>	::= COMA <parametro> <state_aliases_field> <lista_parametros1>
					|

<state_aliases_field>	::= AS <cadena_o_id>
						|

<cadena_o_id>	::= ID
				| CADENA_DOBLE
				| CADENA

<case_state>	::= <auxcase_state> END <case_state1>

<case_state1>	::= <auxcase_state> END <case_state1>
				|

<auxcase_state>	::= WHEN <relacional> THEN CADENA
				| ELSE COMILLA_SIMPLE ID COMILLA_SIMPLE
#=================================================

#=================================================
#INSTRUCCIONES DE DELETE

<deletes> ::= ID <condicion_delete>

<condicion_delete>	::= WHERE <relacional>
					|
#=================================================

#=================================================
#INSTRUCCIONES DE ALTER TABLE

<alter_table>	::= ID <def_alter>

<def_alter>	::= ADD <def_alter_tb_add>
			| DROP <def_alter_tb_drop>
			| ALTER COLUMN ID SET NOT NULL
			| RENAME COLUMN ID TO ID

<def_alter_tb_add>	::= CHECK PARIZQ <relacional> PARDER
					| CONSTRAINT ID UNIQUE PARIZQ ID PARDER
					| FOREIGN KEY PARIZQ <lista_parametros>
					| COLUMN ID <tipos>

<def_alter_tb_drop>	::= COLUMN ID
					| CONSTRAINT ID PARDER REFERENCES PARIZQ <lista_parametros> PARDER 

#=================================================

#=================================================
#INSTRUCCIONES DE UPDATE

<update_table>	::= ID SET <def_update> <update_table_condicion>

<update_table_condicion>	::= WHERE <relacional>
							|

<def_update>	::= ID IGUAL <valor> <def_update1>

<def_update1>	::= COMA ID IGUAL <valor> <def_update1>
				|

#=================================================
#INSTRUCCIONES DE INSERT

<insercion>	::= INTO ID <insercion_params>

<insercion_params>	::= PARIZQ <lista_id> PARDER VALUES PARIZQ <lista_insercion> PARDER
					| VALUES PARIZQ <lista_insercion> PARDER

<lista_insercion>	::= <valor> <lista_insercion1>
					| PARIZQ SELECT <selects> PARDER <lista_insercion1>

<lista_insercion1>	::= COMA <valor> <lista_insercion1>
					| COMA PARIZQ SELECT <selects> PARDER <lista_insercion1>

#=================================================

#=================================================
#INSTRUCCIONES DE DROP

<dropear>	::= DATABASE <if_exist> ID
			| TABLE ID

<if_exist>	::= IF EXISTS
			|

#=================================================
```

#### Gramática Elegida.
La gramática que elegida fue la Ascendente.
Las razones por la que fue elegida, principalmente fue porque esta gramática puede ser leída más fácilmente por la herramienta en la que se va a trabajar el proyecto “ply”, también influye que la gramática ascendente tiene menor cantidad de producciones. 
El hecho de que la gramática descendente tenga más producciones contribuye a que tenga que pasar por más verificaciones para saber en que espacio decide entrar. Al hacer esto, tarda más en generar una lectura o un análisis del texto base que se le envíe.
Esto fue confirmado por medio de pruebas, con una entrada mas o menos pequeña, con 10 ordenes de SQL en el formato de la gramática BNF descrita con anterioridad.
>**Los tiempos en promedio fueron:**
Ascendente 0.002999 segundos
Descendente: 0.003997 segundos.

Con estos datos podemos decir que es más probable que la gramática descendente tarde más en analizar un texto y estas medidas fueron hechas antes de que se realizaran producciones de error y el chequeo semántico.
Por lo que la mejor opción a elegir es la ascendente.