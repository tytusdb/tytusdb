# Reporte de Gramaticas utilizadas

Para el lenguaje Tytus se implementó la gramática ascendente recursiva por la izquieda y generada por la herramienta PLY de Python.  
  
A continuación se encuentra la gramática usada en formato BNF:


```
<init> ::= <instrucciones>

<instrucciones> ::= <instrucciones> <instruccion>
                    | <instruccion>

<instruccion> ::= <alterDB_insrt>
                | <alterTable_insrt>
                | <drop_insrt>
                | USE ID DATABASE PTCOMA
                | <TIPO_ENUM_INSRT>
                | <dropDB>
                | <create_Table_insrt>
                | <select_insrt> PTCOMA
                | <select_uniones>
                | <insert_insrt> 
                | <delete_insrt>
                | <update_insrt>
                | <createDB_insrt>
                | <useDB_insrt>

<useDB_insrt> ::= USE ID PTCOMA

<dropDB> ::= DROP DATABASE ID PTCOMA
           | DROP DATABASE IF EXISTS ID PTCOMA

<createDB_insrt> ::= CREATE DATABASE ID PTCOMA  
                   | CREATE OR REPLACE DATABASE ID PTCOMA
                   | CREATE DATABASE IF NOT EXISTS ID PTCOMA
                   | CREATE OR REPLACE DATABASE IF NOT EXISTS ID PTCOMA
                   | CREATE DATABASE ID <createDB_unParam> PTCOMA
                   | CREATE OR REPLACE DATABASE ID <createDB_unParam> PTCOMA 
                   | CREATE DATABASE IF NOT EXISTS ID <createDB_unParam> PTCOMA 
                   | CREATE OR REPLACE DATABASE IF NOT EXISTS ID                 | <createDB_unParam> PTCOMA    

<createDB_unParam> ::= OWNER ID
                     | MODE ENTERO
                     | OWNER IGUAL ID
                     | MODE IGUAL ENTERO
                    
<createDB_insrt> ::= CREATE DATABASE ID <createDB_dosParam> PTCOMA
                   | CREATE OR REPLACE DATABASE ID <createDB_dosParam> PTCOMA
                   | CREATE DATABASE IF NOT EXISTS ID <createDB_dosParam> PTCOMA
                   | CREATE OR REPLACE DATABASE IF NOT EXISTS ID                 | <createDB_dosParam> PTCOMA

<createDB_dosParam> ::= OWNER string_type MODE ENTERO
                      | OWNER string_type MODE IGUAL ENTERO
                      | MODE ENTERO OWNER string_type
                      | MODE ENTERO OWNER IGUAL string_type
                      | OWNER IGUAL string_type MODE ENTERO
                      | OWNER IGUAL string_type MODE IGUAL ENTERO
                      | MODE IGUAL ENTERO OWNER string_type
                      | MODE IGUAL ENTERO OWNER IGUAL string_type
                      
                      
                      

<TIPO_ENUM_INSRT> ::= CREATE TYPE ID AS ENUM PAR_A <lista_datos> PAR_C PTCOMA

<drop_insrt> ::= DROP TABLE <lista_drop_id> PTCOMA

<lista_drop_id> ::= <lista_drop_id> COMA ID
                  | ID

<alterDB_insrt> ::= ALTER DATABASE ID RENAME TO ID PTCOMA
                  | ALTER DATABASE ID OWNER TO <usuariosDB> PTCOMA

<usuariosDB> ::= ID
              | CURRENT_USER
              | SESSION_USER
              | CADENA

<alterTable_insrt> ::= ALTER TABLE ID <alterTable_type> PTCOMA

<alterTable_type> ::= ADD <alterTable_add>
                    | <alterTable_alter>
                    | DROP CONSTRAINT <campos_c>
                    | RENAME COLUMN ID TO ID
                    | DROP COLUMN <campos_c>

<alterTable_add> ::= COLUMN <campos_add_Column>
                   | CHECK PAR_A <expresion_logica> PAR_C
                   | CONSTRAINT ID <constraint_esp>
                   | FOREIGN KEY PAR_A <campos_c> PAR_C REFERENCES <campos_c>
                    

<campos_add_Column> ::= <campos_add_Column> COMA ID TIPO_DATO
                      | ID TIPO_DATO

<constraint_esp> ::= CHECK PAR_A <expresion_logica> PAR_C
                    | UNIQUE PAR_A <campos_c> PAR_C
                    | FOREIGN KEY PAR_A <campos_c> PAR_C REFERENCES <campos_c>

<alterTable_alter> ::= <alterTable_alter> COMA <Table_alter>
                    | <Table_alter>
                    
<Table_alter> ::= ALTER COLUMN <campos_c> <alter_type>

<alter_type> ::= TYPE TIPO_DATO
                | SET NOT NULL

<campos_c> ::= <campos_c> COMA ID
            | ID

<create_Table_isnrt> ::= CREATE TABLE ID PAR_A <cuerpo_createTable_lista> PAR_C <opcion_herencia>
                        
<opcion_herencia> ::= INHERITS PAR_A ID PAR_C PTCOMA
                    | PTCOMA

<cuerpo_createTable_lista> ::= <cuerpo_createTable_lista> COMA <cuerpo_createTable>
                                | <cuerpo_createTable>

<cuerpo_createTable> ::= ID <TIPO_DATO>
                        | ID <TIPO_DATO> <createTable_options>
                        | PRIMARY KEY PAR_A <campos_c> PAR_C
                        | FOREING KEY PAR_A <campos_c> PAR_C REFERENCES ID PAR_A <campos_c> PAR_C
                        | UNIQUE PAR_A <campos_c> PAR_C
                        | CONSTRAINT ID <constraint_esp>
                        
<createTable_options> ::= <createTable_options> <cT_options>
                        | <cT_options>

<cT_options> ::=  <defecto>
                | <N_null>
                | <C_unique>
                | <C_check>
                | <llave>                        
                        
<defecto> ::= DEFAULT <expresion_dato>

<N_null> ::= NULL
           | NOT NULL

<C_unique> ::= UNIQUE
             | CONSTRAINT <string_type> UNIQUE
             
<C_check> ::= CHECK PAR_A <expresion_logica> PAR_C
            | CONSTRAINT <string_type> CHECK PAR_A <expresion_logica> PAR_C

<llave> : PRIMARY KEY 
        | FOREIGN KEY                    

<TIPO_DATO> ::= TEXT
            | FLOAT
            | INTEGER
            | SMALLINT
            | MONEY
            | DECIMAL PAR_A ENTERO COMA ENTERO PAR_C 
            | NUMERIC PAR_A ENTERO COMA ENTERO PAR_C
            | NUMERIC PAR_A ENTERO PAR_C
            | NUMERIC
            | BIGINT
            | REAL
            | DOUBLE PRECISION
            | INTERVAL <extract_time> TO <extract_time>
            | INTERVAL
            | TIME
            | TIMESTAMP
            | DATE 
            | CHARACTER VARYING PAR_A ENTERO PAR_C
            | VARCHAR PAR_A ENTERO PAR_C
            | CHAR PAR_A ENTERO PAR_C
            | CHARACTER PAR_A ENTERO PAR_C
            | CHAR PAR_A PAR_C
            | CHARACTER PAR_A PAR_C

<update_insrt> ::= UPDATE ID SET <lista_update> WHERE ID IGUAL <expresion> PTCOMA
                
                
<lista_update> ::= <lista_update> COMA <parametro_update>
                | <parametro_update>

<parametro_update> ::= ID IGUAL <expresion_update>
                    
<expresion_update> ::= <expresion>
                    | <exclusivas_update>


<exclusivas_update> ::=  ACOSD PAR_A <expresion> PAR_C
                    | ASIN PAR_A <expresion> PAR_C
                    | SUBSTRING PAR_A <string_type> COMA <expresion> COMA <expresion> PAR_C
                    | MD5 PAR_A <string_type> PAR_C 
                    | TRIM PAR_A <string_type> D_DOSPTS BYTEA FROM <string_type> D_DOSPTS BYTEA PAR_C
                    | SUBSTR PAR_A <string_type> COMA ENTERO COMA ENTERO PAR_C

<delete_insrt> ::= DELETE FROM ONLY ID PTCOMA
                | DELETE FROM ONLY ID RETURNING <returning_exp> PTCOMA
                | DELETE FROM ID WHERE EXISTS <expresion_logica> PTCOMA
                | DELETE FROM ID WHERE EXISTS <expresion_logica> RETURNING <returning_exp> PTCOMA
                | DELETE FROM ID WHERE <expresion_logica> PTCOMA
                | DELETE FROM ID WHERE <expresion_logica RETURNING <returning_exp> PTCOMA
                | DELETE FROM ID RETURNING <returning_exp PTCOMA
                | DELETE FROM ID USING ID WHERE EXISTS <expresion_logica> PTCOMA
                | DELETE FROM ID USING ID WHERE EXISTS <expresion_logica> RETURNING <returning_exp> PTCOMA
                | DELETE FROM ID USING ID WHERE <expresion_logica> PTCOMA
                | DELETE FROM ID USING ID WHERE <expresion_logica> RETURNING <returning_exp> PTCOMA

<returning_exp> ::= ASTERISCO
                | <campos_c>

<as_ID> ::= ID
        | CADENA    

<select_insrt> ::= SELECT <opcion_select_tm>
                
<select_uniones> ::= <select_uniones> <tipo_union> <select_insrt> PTCOMA
                   | <select_insrt> 

<tipo_union> ::= UNION
               | INTERSECT 
               | EXCEPT

<from_s> ::= ID
           | PAR_A  

<otro_from> ::= <from_s> 
              | <from_s> <opcion_from> 

<opcion_sobrenombre> ::= ID <seguir_sobrenombre>
                       | ID

<seguir_sobrenombre> ::= AS <as_ID>
                       | ID 
                       | PUNTO ID            

<opcion_select_tm> ::=  <greatest_insrt> 
                | <funciones_select> AS <as_ID>
                | <opcion_select_lista>  FROM <opciones_sobrenombres>
                | <opcion_select_lista> <seguir_sobrenombre> FROM <otros_froms>
                | <opcion_select_lista>  FROM <from_s> <opcion_from>
                | EXTRACT PAR_A <extract_time> FROM TIMESTAMP CADENA  PAR_C PTCOMA
                | DATE_PART PAR_A CADENA COMA INTERVAL CADENA PAR_C PTCOMA
                | NOW PAR_A PAR_C PTCOMA
                | CURRENT_DATE PTCOMA
                | TIMESTAMP CADENA PTCOMA

<opciones_sobrenombres> ::= <opciones_sobrenombres> COMA <opcion_sobrenombre>
                        | <opcion_sobrenombre>

<otros_froms> ::= <otros_froms> COMA <otro_from>
              | <otro_from>

<opcion_select_lista> ::= DISTINCT <campos_c>
                       | <opciones_select_lista>    

<opciones_select_lista> ::= <opciones_select_lista> COMA <opcion_select>
                         | <opcion_select>   

<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_ob> <orden> <cond_limit> <cond_offset>
                | <cond_gb> <cond_having> <cond_ob> <orden <cond_limit> <cond_offset>
                | <cond_where> <cond_having> <cond_ob> <orden <cond_limit> <cond_offset>
                | <cond_having> <cond_ob> <orden <cond_limit> <cond_offset>
                | <cond_where> <cond_gb> <cond_ob> <orden <cond_limit> <cond_offset>
                | <cond_gb> <cond_ob> <orden <cond_limit> <cond_offset>
                | <cond_where> <cond_ob> <orden <cond_limit> <cond_offset>
                | <cond_ob> <orden <cond_limit> <cond_offset>
                | <cond_where> <cond_gb> <cond_having> <cond_ob> <cond_limit> <cond_offset>
                | <cond_gb> <cond_having> <cond_ob> <cond_limit> <cond_offset>
                | <cond_where> <cond_having> <cond_ob> <cond_limit> <cond_offset>
                | <cond_having> <cond_ob> <cond_limit> <cond_offset>
                | <cond_where> <cond_gb>  <cond_ob> <cond_limit> <cond_offset>
                | <cond_gb> <cond_ob> <cond_limit> <cond_offset>
                | <cond_where> <cond_ob> <cond_limit> <cond_offset>
                | <cond_ob> <cond_limit> <cond_offset>
                | <cond_where> <cond_gb> <cond_having> <cond_limit> <cond_offset>
                | <cond_gb> <cond_having> <cond_limit> <cond_offset>
                | <cond_where> <cond_having> <cond_limit> <cond_offset>
                | <cond_having> <cond_limit> <cond_offset>
                | <cond_where> <cond_gb> <cond_limit> <cond_offset>
                | <cond_gb> <cond_limit> <cond_offset>
                | <cond_where> <cond_limit> <cond_offset>
                | <cond_limit> <cond_offset>
                | <cond_where> <cond_gb> <cond_having> <cond_ob> <orden <cond_limit>
                | <cond_gb> <cond_having> <cond_ob> <orden <cond_limit>
                | <cond_where> <cond_having> <cond_ob> <orden <cond_limit>
                | <cond_having> <cond_ob> <orden <cond_limit>
                | <cond_where> <cond_gb> <cond_ob> <orden <cond_limit>
                | <cond_gb> <cond_ob> <orden <cond_limit>
                | <cond_where> <cond_ob> <orden <cond_limit>
                | <cond_ob> <orden <cond_limit>
                | <cond_where> <cond_gb> <cond_having> <cond_ob> <cond_limit> 
                | <cond_gb> <cond_having> <cond_ob> <cond_limit>
                | <cond_where> <cond_having> <cond_ob> <cond_limit>
                | <cond_having> <cond_ob> <cond_limit>
                | <cond_where> <cond_gb> <cond_ob> <cond_limit>
                | <cond_gb> <cond_ob> <cond_limit>
                | <cond_where> <cond_ob> <cond_limit>
                | <cond_ob> <cond_limit>
                | <cond_where> <cond_gb> <cond_having> <cond_limit>
                | <cond_gb> <cond_having> <cond_limit>
                | <cond_where> <cond_having> <cond_limit>
                | <cond_having> <cond_limit>
                | <cond_where> <cond_gb> <cond_limit>
                | <cond_gb>  <cond_limit>
                | <cond_where> <cond_limit>
                | <cond_limit>
                | <cond_where> <cond_gb> <cond_having> <cond_ob> <orden
                | <cond_gb> <cond_having> <cond_ob> <orden
                | <cond_where> <cond_having> <cond_ob> <orden
                | <cond_having> <cond_ob> <orden
                | <cond_where> <cond_gb> <cond_ob> <orden
                | <cond_gb>  <cond_ob> <orden
                | <cond_where> <cond_ob> <orden
                | <cond_ob>
                | <cond_where> <cond_gb> <cond_having> <cond_ob>
                | <cond_gb> <cond_having> <cond_ob>
                | <cond_where> <cond_having> <cond_ob>
                | <cond_having> <cond_ob>
                | <cond_where> <cond_gb> <cond_ob>
                | <cond_gb> <cond_ob>
                | <cond_where> <cond_ob>
                | <cond_where> <cond_gb> <cond_having>
                | <cond_gb> <cond_having>
                | <cond_where> <cond_having>
                | <cond_having>
                | <cond_where> <cond_gb> 
                | <cond_gb> 
                | <cond_where>
                | <select_insrt> PAR_C ID 
                | <select_insrt> PAR_C

<cond_where> ::= WHERE <expresion_where>

<cond_gb> ::= GROUP BY <campos_c>

<cond_having> ::= HAVING <expresion_logica>

<cond_ob> ::= ORDER BY <campos_c>

<cond_limit> ::= LIMIT <opc_lim>

<cond_offset> ::= OFFSET ENTERO

<extract_time> ::=    YEAR
                    | DAY
                    | MONTH
                    | HOUR
                    | MINUTE
                    | SECOND

<opc_lim> ::= ENTERO
            | ASTERISCO

<orden> ::= DESC
          | ASC

<case_insrt> ::= CASE <estructura_when_lista> ELSE <expresion> END

<estructura_when_lista> ::= <estructura_when_lista> <estructura_when>

<estructura_when_lista> ::= <estructura_when>

<estructura_when> ::= WHEN <expresion_logica> THEN <expresion>
<sum_insrt> ::= SUM <agrupacion_expresion>

<count_insrt> ::= COUNT <agrupacion_expresion>

<insert_insrt> ::= INSERT INTO ID PAR_A <lista_parametros_lista> PAR_C VALUES PAR_A <lista_datos> PAR_C PTCOMA
                | INSERT INTO ID PAR_A  PAR_C  VALUES PAR_A <lista_datos> PAR_C PTCOMA

<lista_parametros_lista> ::= <lista_parametros_lista> COMA <lista_parametros>
                          | <lista_parametros>

<lista_parametros> ::= ID
                     
<lista_datos> ::= <lista_datos> COMA <exclusiva_insert>
                | <exclusiva_insert> 

<exclusiva_insert> ::= <expresion_relacional>
                    | SUBSTRING PAR_A <string_type> COMA <expresion> COMA <expresion> PAR_C
                    | MD5 PAR_A <string_type> PAR_C
                    | TRIM PAR_A <string_type> D_DOSPTS BYTEA FROM <string_type> D_DOSPTS BYTEA PAR_C
                    | SUBSTR PAR_A <string_type> COMA ENTERO COMA ENTERO PAR_C
                    | NOW PAR_A PAR_C

<agrupacion_expresion> ::= PAR_A <expresion> PAR_C

<expresion_dato> ::= <string_type>
                  | RESTA ENTERO
                  | ID PUNTO ID
                  | <expresion_numero>

<expresion_numero> ::=  ENTERO
                    | FLOTANTE

<expresion> ::=  <expresion_dato>
                | <select_insrt>
                | NOW PAR_A PAR_C
                | PAR_A <expresion_logica> PAR_C
                | <expresion> SUMA <expresion>
                | <expresion> RESTA <expresion>
                | <expresion> ASTERISCO <expresion>
                | <expresion> DIVISION <expresion>
                | <expresion> MODULO <expresion>
                | <expresion> MAYMAY <expresion>
                | <expresion> MENMEN <expresion>
                | CEJILLA <expresion>
                | <expresion> HASHTAG <expresion>
                | S_OR <expresion>
                | D_OR <expresion>
                | <expresion> Y <expresion>                
                | AVG PAR_A <expresion> PAR_C 
                | MAX PAR_A <expresion> PAR_C
                | MIN PAR_A <expresion> PAR_C                 
                | ALL PAR_A <select_insrt> PAR_C
                | SOME PAR_A <select_insrt> PAR_C
                | <sum_insrt> 
                | <count_insrt>
                | TRUE
                | FALSE
                | SOME
                | ANY

<string_type> ::= CADENA
                | ID

<expresion_relacional> ::= <expresion> MAYQUE <expresion>
                        | <expresion> MENQUE <expresion>
                        | <expresion> MAYIGQUE <expresion>
                        | <expresion> MENIGQUE <expresion>
                        | <expresion> DOBLEIG <expresion>
                        | <expresion> IGUAL <expresion>
                        | <expresion> NOIG <expresion>
                        | <expresion> NOIGUAL <expresion>

<expresion_relacional> ::= <expresion>

<expresion_logica> ::= <expresion_relacional> AND <expresion_logica>
                    | <expresion_relacional> OR <expresion_logica>
                    | NOT expresion_logica>
                    | <expresion_relacional>

<opcion_select> ::= <case_insrt>
                  | PAR_A <select_insrt> PAR_C
                  | <expresion>
                  | <funciones_select>
                  | ASTERISCO
                  | ID PUNTO ASTERISCO

<greatest_insrt> ::= GREATEST PAR_A <greatest_val> PAR_C
                   | LEAST PAR_A <greatest_val> PAR_C

<greatest_val> ::= <greatest_val> COMA <expresion_dato>
                 | <expresion_dato>

<funciones_select> ::= ABS PAR_A <expresion> PAR_C
                     | CBRT PAR_A <expresion> PAR_C
                     | CEIL PAR_A <expresion> PAR_C 
                     | CEILING PAR_A <expresion> PAR_C 
                     | DEGREES PAR_A <expresion> PAR_C 
                     | DIV PAR_A <expresion> COMA <expresion> PAR_C 
                     | EXP PAR_A <expresion> PAR_C 
                     | FACTORIAL PAR_A <expresion> PAR_C 
                     | FLOOR PAR_A <expresion> PAR_C 
                     | GCD PAR_A <expresion> COMA <expresion> PAR_C
                     | LN PAR_A <expresion> PAR_C 
                     | LOG PAR_A <expresion> PAR_C 
                     | MOD PAR_A <expresion> COMA <expresion> PAR_C 
                     | PI PAR_A PAR_C 
                     | POWER PAR_A <expresion> COMA <expresion> PAR_C 
                     | RADIANS PAR_A <expresion> PAR_C 
                     | ROUND PAR_A <expresion> PAR_C 
                     | SIGN PAR_A <expresion> PAR_C 
                     | SQRT PAR_A <expresion> PAR_C
                     | WIDTH_BUCKET PAR_A <expresion> COMA <expresion> COMA expresion COMA expresion PAR_C 
                     | TRUNC PAR_A <expresion> COMA ENTERO PAR_C
                     | TRUNC PAR_A <expresion> PAR_C 
                     | RANDOM PAR_A PAR_C 
                     | ACOS PAR_A <expresion> PAR_C
                     | ASIND PAR_A <expresion> PAR_C
                     | ATAN PAR_A <expresion> COMA <expresion> PAR_C
                     | ATAND PAR_A <expresion> COMA <expresion> PAR_C
                     | ATAN2 PAR_A <expresion> PAR_C
                     | ATAN2D PAR_A <expresion> PAR_C
                     | COS PAR_A <expresion> PAR_C
                     | COT PAR_A <expresion> PAR_C 
                     | COTD PAR_A <expresion> PAR_C 
                     | SIN PAR_A <expresion> PAR_C 
                     | SIND PAR_A <expresion> PAR_C 
                     | TAN PAR_A <expresion> PAR_C 
                     | TAND PAR_A <expresion> PAR_C 
                     | SINH PAR_A <expresion> PAR_C 
                     | COSH PAR_A <expresion> PAR_C
                     | TANH PAR_A <expresion> PAR_C 
                     | ASINH PAR_A <expresion> PAR_C
                     | ATANH PAR_A <expresion> PAR_C
                     | COSD PAR_A <expresion> PAR_C
                     | ACOSH PAR_A <expresion> PAR_C  
                     | ASIN PAR_A <expresion> PAR_C
                     | ACOSD PAR_A <expresion> PAR_C
                     | LENGTH PAR_A <string_type> PAR_C
                     | SUBSTRING PAR_A <string_type> COMA <expresion> COMA <expresion> PAR_C
                     | TRIM PAR_A <string_type> D_DOSPTS BYTEA FROM <string_type> D_DOSPTS BYTEA PAR_C
                     | SUBSTR PAR_A <string_type> COMA ENTERO COMA ENTERO PAR_C
                     | GET_BYTE PAR_A <string_type> D_DOSPTS BYTEA COMA ENTERO PAR_C
                     | SET_BYTE PAR_A <string_type> D_DOSPTS BYTEA COMA ENTERO COMA ENTERO PAR_C
                     | SHA256 PAR_A <string_type> PAR_C
                     | ENCODE PAR_A <string_type> D_DOSPTS BYTEA COMA <formato_texto> PAR_C
                     | DECODE PAR_A <string_type> D_DOSPTS BYTEA COMA <formato_texto> PAR_C
                     | CONVERT PAR_A <string_type> AS TIPO_DATO PAR_C

<formato_texto> ::= ESCAPE
                 | BASE64
                 | HEX

<expresion_where> ::= <expresion_logica_w>
                   | <expresion_dato> IS DISTINCT FROM <expresion_dato>
                   | <expresion_dato> IS NOT DISTINCT FROM <expresion_dato> 
                   | <expresion_dato> LIKE CADENA
                   | <expresion_dato> NOT LIKE CADENA
                   | <expresion_dato> IS NOT DISTINCT FROM <expresion_dato> AND <expresion_dato>
                   | <expresion_dato> BETWEEN <expresion_dato> AND <expresion_dato>
                   | <expresion_dato> NOT BETWEEN <expresion_dato> AND <expresion_dato>
                   | <expresion_dato> BETWEEN SYMMETRIC <expresion_dato> AND <expresion_dato>
                   | <expresion_dato> NOT BETWEEN SYMMETRIC <expresion_dato> AND <expresion_dato>
                   | <expresion_whereb> IS NULL
                   | <expresion_whereb> IS NOT NULL
                   | <expresion_whereb> ISNULL
                   | <expresion_whereb> NOTNULL
                   | <expresion_whereb> IS TRUE
                   | <expresion_whereb> IS FALSE
                   | <expresion_whereb> IS NOT TRUE
                   | <expresion_whereb> IS NOT FALSE
                   | <expresion_whereb> IS UNKNOWN
                   | <expresion_whereb> IS NOT UNKNOWN 
                  
                                 
<expresion_wherea> ::=  ABS PAR_A <expresion> PAR_C
                    | LENGTH PAR_A <string_type> PAR_C
                    | CBRT PAR_A <expresion> PAR_C
                    | CEIL PAR_A <expresion> PAR_C 
                    | CEILING PAR_A <expresion> PAR_C 
                    | SUBSTRING PAR_A <string_type> COMA expresion COMA expresion PAR_C
                    | TRIM PAR_A <string_type> D_DOSPTS BYTEA FROM string_type D_DOSPTS BYTEA PAR_C
                    | SUBSTR PAR_A <string_type COMA ENTERO COMA ENTERO PAR_C
                    | <sin_some_any> PAR_A <select_insrt> PAR_C
                    | EXTRACT PAR_A <extract_time> FROM <string_type> PAR_C
                    | <expresion>                

<expresion_whereb> ::= <expresion_wherea> MAYQUE <expresion_wherea>
                    | <expresion_wherea> MENQUE <expresion_wherea>
                    | <expresion_wherea> MAYIGQUE <expresion_wherea>
                    | <expresion_wherea> MENIGQUE <expresion_wherea>
                    | <expresion_wherea> DOBLEIG <expresion_wherea>
                    | <expresion_wherea> IGUAL <expresion_wherea>
                    | <expresion_wherea> NOIG <expresion_wherea>
                    | <expresion_wherea> NOIGUAL <expresion_wherea>
                    | <expresion_wherea>

<expresion_logica_w> ::= <expresion_whereb> AND <expresion_logica_w>
                      | <expresion_whereb> OR <expresion_logica_w>
                      | NOT <expresion_logica_w>
                      | <expresion_whereb>
```


Para demostrar la diferencia entre una gramatica recursiva por la izquierda como la usada en el proyecto con la gramatica recursiva por la derecha se tomará como ejemplo de la producción para crear tablas: 


```
<createTable_options> ::= <createTable_options> <cT_options>
                        | <cT_options>

<cT_options> ::=  <defecto>
                | <N_null>
                | <C_unique>
                | <C_check>
                | <llave>                        
                        
<defecto> ::= DEFAULT <expresion_dato>

<N_null> ::= NULL
           | NOT NULL

<C_unique> ::= UNIQUE
             | CONSTRAINT <string_type> UNIQUE
             
<C_check> ::= CHECK PAR_A <expresion_logica> PAR_C
            | CONSTRAINT <string_type> CHECK PAR_A <expresion_logica> PAR_C

<llave> ::= PRIMARY KEY 
        | FOREIGN KEY    
```
        
La cual se vuelve recursiva a la derecha usando la regla:

```
A-> Aa                 A  -> bA' 
A -> b                 A' -> aA'
                       A' -> epsilon
```
Por lo tanto la gramática antes expuesta al aplicar la regla quedaría:

##### Gramática Recursiva por la Derecha

```
<createTable_options> ::=  <cT_options> <createTable_options'>
                        
<createTable_options'> ::= <cT_options> <createTable_options'>
                         | epsilon 
<cT_options> ::=  <defecto>
                | <N_null>
                | <C_unique>
                | <C_check>
                | <llave>                        
                        
<defecto> ::= DEFAULT <expresion_dato>

<N_null> ::= NULL
           | NOT NULL

<C_unique> ::= UNIQUE
             | CONSTRAINT <string_type> UNIQUE
             
<C_check> ::= CHECK PAR_A <expresion_logica> PAR_C
            | CONSTRAINT <string_type> CHECK PAR_A <expresion_logica> PAR_C

<llave> ::= PRIMARY KEY 
        | FOREIGN KEY    
```


# Comparación de velocidad entre un analisador recursivo por la izquierda y un analizador recursivo por la derecha.

Se decidió implementar la gramática recursiva por la izquierda debido a su rapidez.

Un analizador descendente realizará 2 lecturas para poder sintentizar y heredar gramática. En una de las pasadas forma las producciones hacia abajo, de izquierda a derecha y las termina de analizar al reducir todas las producciones. Mientras que las gramaticas recursivas por la izquierda solo realizan una sola lectura. 

## Pruebas realizadas 

Ya que la libreria de analisis léxico y sintáctico PLY posee la capacidad de poder manipular la pila para realizar un análisis de acorde a las necesidades, se realizaron pruebas y se tomó el tiempo con ayuda de la librería de Python "timer" tomando una cadena simple y analizandola.   

Para esta prueba se tomó la expresión:

```
e ::= expresion
expresion ::= expreion * t
t ::= numero
```

#### Análisis Sintáctico Ascendente

El siguiente código fue el ejecutado para evaluar la entrada analizada por medio de gramática  ascendente: 
```
import time
import grammar as g

start_time = time.time()
g.entrada("5*5")
print("--- %s seconds ---" % (time.time() - start_time))
```

![Análisis Sintáctico Ascendente][image_ref_ah8dej8f]El cual dió como resultado que: 



#### Análisis Sintáctico Descendente 
Usando la misma gramática expuesta anteriormente, se realizó el análisis con análisis sintáctico descendente teniendo como resultado : 
![Analisis y resultado de gramática descendente][image_ref_gqdnia7f]



[image_ref_gqdnia7f]: data:image/png;base64,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AABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAAQIAIXQAAAAAQIEIXAAAAAASI0AUAAAAAASJ0AQAAAECACF0AAAAAECBCFwAAAAAEiNAFAAAAAAEidAEAAABAgAhdAAAAABAgQhcAAAAABIjQBQAAAAABInQBAAAA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



[image_ref_ah8dej8f]: data:image/jpeg;base64,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p/46KPtlx/z0/wDHRRoAzyJf+eT/APfJo8iX/nk//fJp/wBsuP8Anp/46KPtlx/z0/8AHRRoAzyJf+eT/wDfJo8iX/nk/wD3yaf9suP+en/joo+2XH/PT/x0UaAQUUUUgCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACitD+2br/nlY/8AgBB/8RR/bN1/zysf/ACD/wCIqrR7/wBfePQz6K0P7Zuv+eVj/wCAEH/xFH9s3X/PKx/8AIP/AIii0e/9feGhn0Vof2zdf88rH/wAg/8AiKP7Zuv+eVj/AOAEH/xFFo9/6+8NDPorQ/tm6/55WP8A4AQf/EUf2zdf88rH/wAAIP8A4ii0e/8AX3hoZ9FaH9s3X/PKx/8AACD/AOIo/tm6/wCeVj/4AQf/ABFFo9/6+8NDPorQ/tm6/wCeVj/4AQf/ABFH9s3X/PKx/wDACD/4ii0e/wDX3hoZ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IrzaHeeeR3UDOVUluA2cEY5FSt451FnNyLSxXVDB9nOpKj+ftxjP3tobHG7bnHeiihq41o7jNL8e+JdLvEuBq95chFZRDdXMjxnII+7uHTOR7gVUs/ELWbG4/syxuNQLM/2658yWTec/MQz7CRnOSp55oooESW3iq8jtry2vYLbUre7m+0SR3gc/vf74KMrA9jzgipYfGeoxeIhrfk2r3KRGGBGQiO3XGAEUEYwCcZz68miiiyHdlTQPEFx4f1gapFbWt3cqDtN2rOFY/wAQwQd3vmrH/CTp/asOpDQtM+0pN5zM7XEolbn7weU55OfqKKKBdGu47VPFk2qX76i2m2UGpNIsovIpJzIrAgjAaVlA4xjHA6Yp134zvLhL0w2NhZ3F+u27ubeNhJMO4O5iq5PJ2gZNFFKytYd3e5I3jnUDJ9qFnYLqhg8g6iI284rjGfvbN2ON23OO9cxRRTt1F0sa+m66mnJCG0fTbuSB98Us6SB1PHXY6hhx/EDVkeMNQmW9j1GG11KC8lE8kNyjBRIP41MZVlOBjg4xRRRYFoR2HiebTL24lstPsora5i8meyIkeGRffc5bPuGFOtvFM1je+dZadp9vA0LQS2ixu0cyN1DlmLnPH8XGOMUUUWQFi28b39jNZGxsrG1trN2kjtY0cxl2BBZizFycHH3qpab4n1DSbO5trTyk+0TxXBkKksjxnK45xjJ7g0UUDvpY0J/Hd9La6jbw6dplqmpA/avJibMjE53ZLHB68Djk8VWt/Fk1kkjWOl6ba3csPkvdxRvvK4wcKXKAkdSFHeiilyoPM5+iiimIKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD/2Q==


Por lo tanto es notable que la gramática ascendente es mucho más rápida que la descendente