| sentencia_show              	| ::= 	| SHOW' 'DATABASES' like_options                                                                                         	|
|-----------------------------	|-----	|------------------------------------------------------------------------------------------------------------------------	|
| like_options                	| ::= 	| LIKE' CADENA                                                                                                           	|
| like_options                	| ::= 	| EPSILON                                                                                                                	|
| sentencia_drop              	| ::= 	| DROP' DROP_OPTIONS                                                                                                     	|
| drop_options                	| ::= 	| TABLE' IDENTIFICADOR                                                                                                   	|
| drop_options                	| ::= 	| DATABASE' if_exists IDENTIFICADOR                                                                                      	|
| if_exists                   	| ::= 	| IF' 'EXISTS'                                                                                                           	|
| if_exists                   	| ::= 	| EPSILON                                                                                                                	|
| instrucciones               	| ::= 	| instrucciones instruccion ';'                                                                                          	|
| instrucciones               	| ::= 	| instruccion ';'                                                                                                        	|
| instruccion                 	| ::= 	| sentencia_crear                                                                                                        	|
|                             	|     	| \| sentencia_case                                                                                                      	|
|                             	|     	| \| sentencia_use                                                                                                       	|
|                             	|     	| \| sent_insertar                                                                                                       	|
|                             	|     	| \| sent_update                                                                                                         	|
|                             	|     	| \| sent_delete                                                                                                         	|
|                             	|     	| \| sent_alter                                                                                                          	|
|                             	|     	| \| sentencia_show                                                                                                      	|
|                             	|     	| \| sentencia_drop                                                                                                      	|
|                             	|     	| \| sentencia_select                                                                                                    	|
|                             	|     	| \| Exp                                                                                                                 	|
|                             	|     	| \| error                                                                                                               	|
| sentencia_select            	| ::= 	| SELECT' lista_exp                                                                                                      	|
| sentencia_select            	| ::= 	| SELECT' campos 'FROM' tables_expresion                                                                                 	|
| sentencia_select            	| ::= 	| SELECT' campos 'FROM' tables_expresion sentencia_where                                                                 	|
| sentencia_select            	| ::= 	| SELECT' 'DISTINCT' lista_exp                                                                                           	|
| sentencia_select            	| ::= 	| SELECT' 'DISTINCT' campos 'FROM' tables_expresion                                                                      	|
| sentencia_select            	| ::= 	| SELECT DISTINCT campos FROM tables_expresion sentencia_where'                                                          	|
| sentencia_where             	| ::= 	| WHERE' Exp                                                                                                             	|
| campos                      	| ::= 	| lista_exp                                                                                                              	|
| campos                      	| ::= 	| *'                                                                                                                     	|
| lista_exp                   	| ::= 	| lista_exp ',' Exp                                                                                                      	|
| lista_exp                   	| ::= 	| lista_exp ',' Alias                                                                                                    	|
| lista_exp                   	| ::= 	| Exp                                                                                                                    	|
| lista_exp                   	| ::= 	| Alias                                                                                                                  	|
| Alias                       	| ::= 	| Exp AS part2                                                                                                           	|
| part2                       	| ::= 	| IDENTIFICADOR                                                                                                          	|
| part2                       	| ::= 	| CADENA                                                                                                                 	|
| tables_expresion            	| ::= 	| tables_expresion COMA elements                                                                                         	|
| tables_expresion            	| ::= 	| elements                                                                                                               	|
| elements                    	| ::= 	| IDENTIFICADOR                                                                                                          	|
| elements                    	| ::= 	| IDENTIFICADOR IDENTIFICADOR                                                                                            	|
| elements                    	| ::= 	| PARENTESISIZQ sentencia_select PARENTESISDER                                                                           	|
| funcion_fechas              	| ::= 	| EXTRACT PARENTESISIZQ time FROM TIMESTAMP CADENA PARENTESISDER                                                         	|
| funcion_fechas              	| ::= 	| DATE_PART PARENTESISIZQ CADENA COMA INTERVAL CADENA PARENTESISDER                                                      	|
| funcion_fechas              	| ::= 	| NOW PARENTESISIZQ PARENTESISDER                                                                                        	|
| funcion_fechas              	| ::= 	| CURRENT_DATE                                                                                                           	|
| funcion_fechas              	| ::= 	| CURRENT_TIME                                                                                                           	|
| funcion_fechas              	| ::= 	| TIMESTAMP CADENA                                                                                                       	|
| time                        	| ::= 	| YEAR                                                                                                                   	|
|                             	|     	| \| MONTH                                                                                                               	|
|                             	|     	| \| DAY                                                                                                                 	|
|                             	|     	| \| HOUR                                                                                                                	|
|                             	|     	| \| MINUTE                                                                                                              	|
|                             	|     	| \| SECOND                                                                                                              	|
| funcion_matematica          	| ::= 	| ABS PARENTESISIZQ Exp PARENTESISDER                                                                                    	|
| funcion_matematica          	| ::= 	| CBRT PARENTESISIZQ Exp PARENTESISDER                                                                                   	|
| funcion_matematica          	| ::= 	| CEIL PARENTESISIZQ Exp PARENTESISDER                                                                                   	|
| funcion_matematica          	| ::= 	| CEILING PARENTESISIZQ Exp PARENTESISDER                                                                                	|
| funcion_matematica          	| ::= 	| DEGREES PARENTESISIZQ Exp PARENTESISDER                                                                                	|
| funcion_matematica          	| ::= 	| DIV PARENTESISIZQ Exp COMA Exp PARENTESISDER                                                                           	|
| funcion_matematica          	| ::= 	| EXP PARENTESISIZQ Exp PARENTESISDER                                                                                    	|
| funcion_matematica          	| ::= 	| FACTORIAL PARENTESISIZQ Exp PARENTESISDER                                                                              	|
| funcion_matematica          	| ::= 	| FLOOR PARENTESISIZQ Exp PARENTESISDER                                                                                  	|
| funcion_matematica          	| ::= 	| GCD PARENTESISIZQ Exp COMA Exp PARENTESISDER                                                                           	|
| funcion_matematica          	| ::= 	| LN PARENTESISIZQ Exp PARENTESISDER                                                                                     	|
| funcion_matematica          	| ::= 	| LOG PARENTESISIZQ Exp PARENTESISDER                                                                                    	|
| funcion_matematica          	| ::= 	| MOD PARENTESISIZQ Exp COMA Exp PARENTESISDER                                                                           	|
| funcion_matematica          	| ::= 	| PI PARENTESISIZQ  PARENTESISDER                                                                                        	|
| funcion_matematica          	| ::= 	| POWER PARENTESISIZQ Exp COMA Exp PARENTESISDER                                                                         	|
| funcion_matematica          	| ::= 	| RADIANS PARENTESISIZQ Exp PARENTESISDER                                                                                	|
| funcion_matematica          	| ::= 	| ROUND PARENTESISIZQ Exp COMA Exp PARENTESISDER                                                                         	|
| funcion_matematica          	| ::= 	| SIGN PARENTESISIZQ Exp PARENTESISDER                                                                                   	|
| funcion_matematica          	| ::= 	| SQRT PARENTESISIZQ Exp PARENTESISDER                                                                                   	|
| funcion_matematica          	| ::= 	| WIDTH_BUCKET PARENTESISIZQ Exp COMA Exp COMA Exp COMA Exp PARENTESISDER                                                	|
| funcion_matematica          	| ::= 	| TRUNC PARENTESISIZQ Exp PARENTESISDER                                                                                  	|
| funcion_matematica          	| ::= 	| RANDOM PARENTESISIZQ PARENTESISDER                                                                                     	|
| funcion_trigonometrica      	| ::= 	| ACOS PARENTESISIZQ Exp PARENTESISDER                                                                                   	|
| funcion_trigonometrica      	| ::= 	| ACOSD PARENTESISIZQ Exp PARENTESISDER                                                                                  	|
| funcion_trigonometrica      	| ::= 	| ASIN PARENTESISIZQ Exp PARENTESISDER                                                                                   	|
| funcion_trigonometrica      	| ::= 	| ASIND PARENTESISIZQ Exp PARENTESISDER                                                                                  	|
| funcion_trigonometrica      	| ::= 	| ATAN PARENTESISIZQ Exp PARENTESISDER                                                                                   	|
| funcion_trigonometrica      	| ::= 	| ATAND PARENTESISIZQ Exp PARENTESISDER                                                                                  	|
| funcion_trigonometrica      	| ::= 	| ATAN2 PARENTESISIZQ Exp COMA Exp PARENTESISDER                                                                         	|
| funcion_trigonometrica      	| ::= 	| ATAN2D PARENTESISIZQ Exp COMA Exp PARENTESISDER                                                                        	|
| funcion_trigonometrica      	| ::= 	| COS PARENTESISIZQ Exp PARENTESISDER                                                                                    	|
| funcion_trigonometrica      	| ::= 	| COSD PARENTESISIZQ Exp PARENTESISDER                                                                                   	|
| funcion_trigonometrica      	| ::= 	| COT PARENTESISIZQ Exp PARENTESISDER                                                                                    	|
| funcion_trigonometrica      	| ::= 	| COTD PARENTESISIZQ Exp PARENTESISDER                                                                                   	|
| funcion_trigonometrica      	| ::= 	| SIN PARENTESISIZQ Exp PARENTESISDER                                                                                    	|
| funcion_trigonometrica      	| ::= 	| SIND PARENTESISIZQ Exp PARENTESISDER                                                                                   	|
| funcion_trigonometrica      	| ::= 	| TAN PARENTESISIZQ Exp PARENTESISDER                                                                                    	|
| funcion_trigonometrica      	| ::= 	| TAND PARENTESISIZQ Exp PARENTESISDER                                                                                   	|
| funcion_trigonometrica      	| ::= 	| SINH PARENTESISIZQ Exp PARENTESISDER                                                                                   	|
| funcion_trigonometrica      	| ::= 	| COSH PARENTESISIZQ Exp PARENTESISDER                                                                                   	|
| funcion_trigonometrica      	| ::= 	| TANH PARENTESISIZQ Exp PARENTESISDER                                                                                   	|
| funcion_trigonometrica      	| ::= 	| ASINH PARENTESISIZQ Exp PARENTESISDER                                                                                  	|
| funcion_trigonometrica      	| ::= 	| ACOSH PARENTESISIZQ Exp PARENTESISDER                                                                                  	|
| funcion_trigonometrica      	| ::= 	| ATANH PARENTESISIZQ Exp PARENTESISDER                                                                                  	|
| funcion_string              	| ::= 	| LENGTH PARENTESISIZQ Exp PARENTESISDER                                                                                 	|
| funcion_string              	| ::= 	| SUBSTRING PARENTESISIZQ Exp COMA Exp COMA Exp PARENTESISDER                                                            	|
| funcion_string              	| ::= 	| TRIM PARENTESISIZQ Exp FROM Exp PARENTESISDER                                                                          	|
| funcion_string              	| ::= 	| MD5 PARENTESISIZQ Exp PARENTESISDER                                                                                    	|
| funcion_string              	| ::= 	| SHA256 PARENTESISIZQ Exp PARENTESISDER                                                                                 	|
| funcion_string              	| ::= 	| SUBSTR PARENTESISIZQ Exp COMA Exp COMA Exp PARENTESISDER                                                               	|
| funcion_string              	| ::= 	| GET_BYTE PARENTESISIZQ Exp DOBLEDOSPUNTOS BYTEA COMA Exp PARENTESISDER                                                 	|
| funcion_string              	| ::= 	| SET_BYTE PARENTESISIZQ Exp DOBLEDOSPUNTOS BYTEA COMA Exp COMA Exp PARENTESISDER                                        	|
| funcion_string              	| ::= 	| CONVERT PARENTESISIZQ Exp AS tipo_declaracion PARENTESISDER                                                            	|
| funcion_string              	| ::= 	| ENCODE PARENTESISIZQ Exp DOBLEDOSPUNTOS BYTEA COMA Exp PARENTESISDER                                                   	|
| funcion_string              	| ::= 	| DECODE PARENTESISIZQ Exp COMA Exp PARENTESISDER                                                                        	|
| funcion_agregada            	| ::= 	| AVG PARENTESISIZQ Exp PARENTESISDER                                                                                    	|
| funcion_agregada            	| ::= 	| COUNT PARENTESISIZQ list_count PARENTESISDER                                                                           	|
| funcion_agregada            	| ::= 	| MAX PARENTESISIZQ Exp PARENTESISDER                                                                                    	|
| funcion_agregada            	| ::= 	| MIN PARENTESISIZQ Exp PARENTESISDER                                                                                    	|
| funcion_agregada            	| ::= 	| SUM PARENTESISIZQ Exp PARENTESISDER                                                                                    	|
| list_count                  	| ::= 	| Exp                                                                                                                    	|
| list_count                  	| ::= 	| ASTERISCO                                                                                                              	|
| tipo_declaracion            	| ::= 	| SMALLINT                                                                                                               	|
|                             	|     	| \| INTEGER                                                                                                             	|
|                             	|     	| \| BIGINT                                                                                                              	|
|                             	|     	| \| DECIMAL                                                                                                             	|
|                             	|     	| \| NUMERIC                                                                                                             	|
|                             	|     	| \| REAL                                                                                                                	|
|                             	|     	| \| MONEY                                                                                                               	|
|                             	|     	| \| TEXT                                                                                                                	|
|                             	|     	| \| DATE                                                                                                                	|
|                             	|     	| \| BOOLEAN                                                                                                             	|
| tipo_declaracion            	| ::= 	| DOUBLE PRECISION                                                                                                       	|
| tipo_declaracion            	| ::= 	| CHARACTER VARYING PARENTESISIZQ ENTERO PARENTESISDER                                                                   	|
| tipo_declaracion            	| ::= 	| VARCHAR PARENTESISIZQ ENTERO PARENTESISDER                                                                             	|
|                             	|     	| \| CHARACTER PARENTESISIZQ ENTERO PARENTESISDER                                                                        	|
|                             	|     	| \| CHAR PARENTESISIZQ ENTERO PARENTESISDER                                                                             	|
| tipo_declaracion            	| ::= 	| TIMESTAMP time_opcionales                                                                                              	|
|                             	|     	| \| TIME time_opcionales                                                                                                	|
|                             	|     	| \| INTERVAL interval_opcionales                                                                                        	|
| tipo_declaracion            	| ::= 	| PARENTESISIZQ ENTERO PARENTESISDER time_opcionales_p                                                                   	|
|                             	|     	| \| time_opcionales_p                                                                                                   	|
| time_opcionales             	| ::= 	| WITHOUT TIME ZONE                                                                                                      	|
|                             	|     	| \| WITH TIME ZONE                                                                                                      	|
|                             	|     	| \|                                                                                                                     	|
| time_opcionales_p           	| ::= 	| CADENA interval_opcionales_p                                                                                           	|
|                             	|     	| \| interval_opcionales_p                                                                                               	|
| interval_opcionales         	| ::= 	| PARENTESISIZQ ENTERO PARENTESISDER                                                                                     	|
|                             	|     	| \|                                                                                                                     	|
| sentencia_crear             	| ::= 	| CREATE TYPE IDENTIFICADOR AS ENUM PARENTESISIZQ lista_cadenas PARENTESISDER                                            	|
| sentencia_crear             	| ::= 	| CREATE sentencia_orreplace DATABASE sentencia_ifnotexists IDENTIFICADOR opcionales_crear_database                      	|
| sentencia_crear             	| ::= 	| CREATE TABLE IDENTIFICADOR PARENTESISIZQ cuerpo_creartabla PARENTESISDER                                               	|
| cuerpo_creartabla           	| ::= 	| cuerpo_creartabla COMA cuerpo_creartabla_p                                                                             	|
| cuerpo_creartabla           	| ::= 	| cuerpo_creartabla_p                                                                                                    	|
| cuerpo_creartabla_p         	| ::= 	| IDENTIFICADOR tipo_declaracion opcional_creartabla_columna                                                             	|
| cuerpo_creartabla_p         	| ::= 	| opcional_constraint  CHECK PARENTESISIZQ lista_exp PARENTESISDER                                                       	|
| cuerpo_creartabla_p         	| ::= 	| UNIQUE PARENTESISIZQ lista_ids  PARENTESISDER                                                                          	|
| cuerpo_creartabla_p         	| ::= 	| PRIMARY KEY PARENTESISIZQ lista_ids PARENTESISDER                                                                      	|
| cuerpo_creartabla_p         	| ::= 	| fk_references_p REFERENCES IDENTIFICADOR PARENTESISIZQ lista_ids PARENTESISDER                                         	|
| fk_references_p             	| ::= 	| FOREIGN KEY PARENTESISIZQ lista_ids PARENTESISDER \|                                                                   	|
| opcional_creartabla_columna 	| ::= 	| opcional_creartabla_columna NOT NULL                                                                                   	|
| opcional_creartabla_columna 	| ::= 	| opcional_creartabla_columna NULL                                                                                       	|
| opcional_creartabla_columna 	| ::= 	| opcional_creartabla_columna opcional_constraint UNIQUE                                                                 	|
| opcional_creartabla_columna 	| ::= 	| opcional_creartabla_columna opcional_constraint CHECK PARENTESISIZQ Exp PARENTESISDER                                  	|
| opcional_creartabla_columna 	| ::= 	| NOT NULL                                                                                                               	|
| opcional_creartabla_columna 	| ::= 	| NULL                                                                                                                   	|
| opcional_creartabla_columna 	| ::= 	| opcional_constraint UNIQUE                                                                                             	|
| opcional_creartabla_columna 	| ::= 	| PRIMARY KEY                                                                                                            	|
| opcional_creartabla_columna 	| ::= 	| opcional_creartabla_columna PRIMARY KEY                                                                                	|
| opcional_creartabla_columna 	| ::= 	| opcional_constraint CHECK PARENTESISIZQ PARENTESISDER \|                                                               	|
| opcional_creartabla_columna 	| ::= 	| opcional_creartabla_columna DEFAULT Exp                                                                                	|
| opcional_creartabla_columna 	| ::= 	| DEFAULT Exp                                                                                                            	|
| opcional_creartabla_columna 	| ::= 	| opcional_creartabla_columna REFERENCES IDENTIFICADOR                                                                   	|
| opcional_constraint         	| ::= 	| CONSTRAINT IDENTIFICADOR \|                                                                                            	|
| lista_cadenas               	| ::= 	| lista_cadenas COMA CADENA                                                                                              	|
|                             	|     	| \| CADENA                                                                                                              	|
| lista_ids                   	| ::= 	| lista_ids COMA IDENTIFICADOR                                                                                           	|
|                             	|     	| \| IDENTIFICADOR                                                                                                       	|
| sentencia_orreplace         	| ::= 	| OR REPLACE \|                                                                                                          	|
| sentencia_ifnotexists       	| ::= 	| IF NOT EXISTS \|                                                                                                       	|
| opcionales_crear_database   	| ::= 	| opcionales_crear_database OWNER opcional_comparar IDENTIFICADOR                                                        	|
|                             	|     	| \| opcionales_crear_database MODE opcional_comparar ENTERO                                                             	|
| opcionales_crear_database   	| ::= 	| OWNER opcional_comparar IDENTIFICADOR                                                                                  	|
|                             	|     	| \| MODE opcional_comparar ENTERO                                                                                       	|
|                             	|     	| \|                                                                                                                     	|
| opcional_comparar           	| ::= 	| IGUAL \|                                                                                                               	|
| sentencia_use               	| ::= 	| USE IDENTIFICADOR                                                                                                      	|
| sentencia_case              	| ::= 	| CASE listaExpCase caseElse END                                                                                         	|
| listaExpCase                	| ::= 	| listaExpCase WHEN Exp THEN Exp                                                                                         	|
|                             	|     	| \| WHEN Exp THEN Exp                                                                                                   	|
| caseElse                    	| ::= 	| ELSE Exp \|                                                                                                            	|
| sent_insertar               	| ::= 	| INSERT INTO IDENTIFICADOR VALUES PARENTESISIZQ l_param_insert PARENTESISDER                                            	|
| sent_insertar               	| ::= 	| INSERT INTO IDENTIFICADOR PARENTESISIZQ l_param_column PARENTESISDER VALUES PARENTESISIZQ l_param_insert PARENTESISDER 	|
| l_param_column              	| ::= 	| l_param_column COMA IDENTIFICADOR                                                                                      	|
| l_param_column              	| ::= 	| IDENTIFICADOR                                                                                                          	|
| l_param_insert              	| ::= 	| l_param_insert COMA  Exp                                                                                               	|
| l_param_insert              	| ::= 	| Exp                                                                                                                    	|
| sent_update                 	| ::= 	| UPDATE IDENTIFICADOR SET l_col_update                                                                                  	|
| l_col_update                	| ::= 	| l_col_update COMA col_update                                                                                           	|
| l_col_update                	| ::= 	| col_update                                                                                                             	|
| col_update                  	| ::= 	| IDENTIFICADOR IGUAL Exp                                                                                                	|
| sent_delete                 	| ::= 	| DELETE FROM IDENTIFICADOR                                                                                              	|
| sent_alter                  	| ::= 	| ALTER DATABASE IDENTIFICADOR accion_alter_db                                                                           	|
| sent_alter                  	| ::= 	| ALTER TABLE IDENTIFICADOR accion_alter_table                                                                           	|
| accion_alter_db             	| ::= 	| RENAME TO IDENTIFICADOR                                                                                                	|
| accion_alter_db             	| ::= 	| OWNER TO nuevo_prop                                                                                                    	|
| nuevo_prop                  	| ::= 	| CADENA                                                                                                                 	|
|                             	|     	| \| CURRENT_USER                                                                                                        	|
|                             	|     	| \| SESSION_USER                                                                                                        	|
| accion_alter_table          	| ::= 	| alter_add_col                                                                                                          	|
|                             	|     	| \| alter_drop_col                                                                                                      	|
|                             	|     	| \| l_alter_col                                                                                                         	|
| alter_add_col               	| ::= 	| ADD COLUMN IDENTIFICADOR tipo_declaracion                                                                              	|
| alter_add_col               	| ::= 	| ADD CHECK PARENTESISIZQ Exp PARENTESISDER                                                                              	|
| alter_add_col               	| ::= 	| ADD CONSTRAINT IDENTIFICADOR FOREIGN KEY IDENTIFICADOR REFERENCES IDENTIFICADOR                                        	|
| alter_add_col               	| ::= 	| ADD CONSTRAINT IDENTIFICADOR UNIQUE IDENTIFICADOR                                                                      	|
| alter_drop_col              	| ::= 	| DROP COLUMN IDENTIFICADOR                                                                                              	|
| alter_drop_col              	| ::= 	| DROP CONSTRAINT IDENTIFICADOR                                                                                          	|
| l_alter_col                 	| ::= 	| l_alter_col COMA alter_col                                                                                             	|
| l_alter_col                 	| ::= 	| alter_col                                                                                                              	|
| alter_col                   	| ::= 	| ALTER COLUMN IDENTIFICADOR SET NOT NULL                                                                                	|
| alter_col                   	| ::= 	| ALTER COLUMN IDENTIFICADOR TYPE tipo_declaracion                                                                       	|
| herencia                    	| ::= 	| INHERITS PARENTESISIZQ IDENTIFICADOR PARENTESISDER                                                                     	|
| Exp                         	| ::= 	| Exp AND Exp                                                                                                            	|
| Exp                         	| ::= 	| Exp OR Exp                                                                                                             	|
| Exp                         	| ::= 	| NOT Exp                                                                                                                	|
| Exp                         	| ::= 	| Exp IGUAL Exp                                                                                                          	|
| Exp                         	| ::= 	| Exp DIFERENTEQUE Exp                                                                                                   	|
| Exp                         	| ::= 	| Exp MAYORQUE Exp                                                                                                       	|
| Exp                         	| ::= 	| Exp MAYORIGUAL Exp                                                                                                     	|
| Exp                         	| ::= 	| Exp MENORQUE Exp                                                                                                       	|
| Exp                         	| ::= 	| Exp MENORIGUAL Exp                                                                                                     	|
| Exp                         	| ::= 	| Exp MAS Exp                                                                                                            	|
| Exp                         	| ::= 	| Exp MENOS Exp                                                                                                          	|
| Exp                         	| ::= 	| Exp ASTERISCO Exp                                                                                                      	|
| Exp                         	| ::= 	| Exp SLASH Exp                                                                                                          	|
| Exp                         	| ::= 	| Exp POTENCIA Exp                                                                                                       	|
| Exp                         	| ::= 	| Exp PORCENTAJE Exp                                                                                                     	|
| Exp                         	| ::= 	| MENOS Exp %prec UMINUS                                                                                                 	|
| Exp                         	| ::= 	| PARENTESISIZQ Exp PARENTESISDER                                                                                        	|
| Exp                         	| ::= 	| ENTERO                                                                                                                 	|
| Exp                         	| ::= 	| NUMDECIMAL                                                                                                             	|
| Exp                         	| ::= 	| CADENA                                                                                                                 	|
| Exp                         	| ::= 	| FALSE \| TRUE                                                                                                          	|
| Exp                         	| ::= 	| IDENTIFICADOR                                                                                                          	|
| Exp                         	| ::= 	| Acceso                                                                                                                 	|
| Exp                         	| ::= 	| funcion_fechas                                                                                                         	|
|                             	|     	| \| funcion_matematica                                                                                                  	|
|                             	|     	| \| funcion_trigonometrica                                                                                              	|
|                             	|     	| \| funcion_string                                                                                                      	|
|                             	|     	| \| funcion_agregada                                                                                                    	|
| Acceso                      	| ::= 	| IDENTIFICADOR PUNTO option_access                                                                                      	|
| option_access               	| ::= 	| IDENTIFICADOR                                                                                                          	|
| option_access               	| ::= 	| ASTERISCO                                                                                                              	|