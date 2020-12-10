## Gramatica Ascendente, formato BNF

\<**init**\>  := \<**instruccione**s\>

\<**instrucciones**\>    := \<**instrucciones**\>  \<**instruccion**\>

\<instrucciones\>    := \<instruccion\> 

\<instruccion\> := \<crear\>  t_PUNTOCOMA
	      | SHOW DATABASE \<like_regex\> t_PUNTOCOMA
                   | \<alter_db\> t_PUNTOCOMA
      | \<drop_db\> t_PUNTOCOMA
      | DELET FROM [ONLY] ID delet_op t_PUNTOCOMA
      | \<seleccionar\> t_PUNTOCOMA


\<crear\> := CREATE TABLE  ID t_PAR_ABRE \<contenido_tabla\> t_PAR_CIERRA 
        | CREATE [\<or_replace\>] DATABASE [\<if_not_exists\>] ID [\<owner_mode\>]

\<owner_mode\> := OWNER = ID
         | MODE = ENTERO
        
\<alter_db\> := ALTER DATABASE ID \<rename_owner\>
 |ALTER TABLE ID \<alter_op\>

\<alter_op\> :=  ADD \<op_add\>
	 | DROP \<op_drop\>
	 | ALTER COLUMN ID SET NOT NULL 
	 | RENAME COLUMN ID TO ID

\<op_add\> := CHECK t_PAR_ABRE ID t_DIFERENTE t_CADENA t_PAR_CIERRA
|CONSTRAINT ID UNIQUE t_PAR_ABRE t_PAR_CIERRA
|\<key_table\> REFERENCES ID t_PAR_ABRE list_id t_PAR_CIERRA

\<or_replace\> := OR REPLACE
    
   
 \<if_not_exists\> := IF NOT EXISTS 
	         

\<like_regex\> := LIKE cadena
                | epsilon

\<rename_owner\> := RENAME TO ID
	           | OWNER TO t_LLAVE_ABRE ID t_BARRA CURRENT_USER t_BARRA SESSION USER t_LLAVE_CIERRA

\<drop_db\> := DROP DATABASE [\<if_exists\>] ID 

\<if_exists\>: IF EXISTS
            

\<contenido_tabla\> := \<contenido_tabla\> t_COMA \<manejo_tabla\>
	             | \<manejo_tabla\>

\<manejo_tabla\> := \<declaracion_columna\>
	          | \<condition_column\>

\<declaracion_columna\> := ID \<type_column\> \<condition_column_row\>
		        | ID \<type_column\>

\<condition_column_row\> := \<condition_row\> \<condition_column\>
	                       | \<condition_column\>

\<condition_column\> := CONSTRAINT ID CHECK \<condition_columns\>
                            | CHECK \<condition_columns\>
	               | CONSTRAINT ID UNIQUE
                            | CONSTRAINT ID UNIQUE t_PAR_ABRE \<list_id\> t_PAR_CIERRA
		  | UNIQUE t_PAR_ABRE \<list_id\> t_PAR_CIERRA

\<condition_columns\>:= \<condition_columns\> , \<condition_columna\>
	                 | \<condition_columna\>

condition_columna: 

\<key_table\> := PRIMARY KEY [\<list_key\>]
	    | FOREIGN KEY t_PAR_ABRE \<list_id\> t_PAR_CIERRA REFERENCES ID t_PAR_ABRE 
\<list_id\> t_PAR_CIERRA

\<list_key\> := t_PAR_ABRE list_id t_PAR_CIERRA
	

\<list_id\>:= \<list_id\> , ID \<alias\>
         | ID \<alias\>

\<type_column\> := SMALLINT
	         | INTEGER
	         | BIGINT
	         | DECIMAL
	         | NUMERIC
	         | REAL
	         | DOUBLE PRECISION
	         | MONEY
	         | INTEGER

queries
------
\<seleccionar\> := SELECT [\<distinto\>]  \<select_list\> FROM table_expression \<fin_select\>

\<fin_select\> := \<group_by\>  
	| \<donde\>
	| \<order_by\>
	| \<group_having\>
	| \<limite\>
	|\<epsilon\>

\<distinto\> := DISTINCT

\<select_list\> := ASTERISCO
	| \<list_id\>

\<table_expression\> := \<list_id\>
	

\<donde\> := WHERE \<expression\>

\<group_by\> := GROUP BY \<list_id\>
	

\<order_by\> := ORDER BY \<list_id asc_desc\> [\<nulls_f_l\>]
	

\<group_having\>:= HAVING \<list_id\>
	

\<asc_desc\> := ASC
	| DESC

\<nulls_f_l\>:= NULLS LAST
	| NULLS FIRST
	

\<limite\> := LIMIT ENTERO
	| LIMIT ALL
	| OFFSET ENTERO

