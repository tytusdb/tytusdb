# Reporte de Gramatical

A continuación se presentan dos gramáticas creadas para el lenguaje, una gramática descendente y otra ascendente donde más adelante por medio de un análisis se llegó a la conclusión que la gramática que quedaba más acorde para el presente proyecto era la gramática ascendente.

## **Gramática descendente**

	E ::= INSTRUCCION 

	INSTRUCCION ::= CREATE_TABLE INSTRUCCION_p 
			  | CREATE_DB INSTRUCCION_p
			  | SHOW_DB INSTRUCCION_p
			  | ALTER_DB INSTRUCCION_p
			  | DROP_DB INSTRUCCION_p
			  | CREATE_TABLE INSTRUCCION_p
			  | DROP_TABLE INSTRUCCION_p
			  | ALTER_TABLE INSTRUCCION_p
			  | S_DELETE INSTRUCCION_p
			  | S_INSERT INSTRUCCION_p
			  | S_UPDATE INSTRUCCION_p
			  | SELECT INSTRUCCION_p

	INSTRUCCION_p ::= CREATE_TABLE INSTRUCCION_p 
				| CREATE_DB INSTRUCCION_p
				| SHOW_DB INSTRUCCION_p
				| ALTER_DB INSTRUCCION_p
				| DROP_DB INSTRUCCION_p
				| CREATE_TABLE INSTRUCCION_p
				| DROP_TABLE INSTRUCCION_p
				| ALTER_TABLE INSTRUCCION_p
				| S_DELETE INSTRUCCION_p
				| S_INSERT INSTRUCCION_p
				| S_UPDATE INSTRUCCION_p
				| SELECT INSTRUCCION_p
				| epsilon 

	CREATE_TYPE ::= create type id as C_TYPE ";"

	C_TYPE ::= enum "(" LISTA
	     	| "(" LISTA

	LISTA ::= ID_CADENA LISTA1

	LISTA1 ::= "," ID_CADENA LISTA1_p
		 | ")" LISTA1_p

	LISTA1_p ::= "," ID_CADENA LISTA1_p
		   | ")" LISTA1_p
		   | epsilon

	ID_CADENA ::= id DATA_TYPE
			| cadena

	CREATE_DB ::= create C_DB 

	C_DB ::= [ or replace ] database C_DB1

	C_DB1 ::= [ if not exists ] id OWNER_MODE

	OWNER_MODE ::= owner IGUAL_ID OWNER_MODE_p
		     | mode IGUAL_ID OWNER_MODE_p
		     | ";" OWNER_MODE_p 

	OWNER_MODE_p ::= owner IGUAL_ID OWNER_MODE_p
			   | mode IGUAL_ID OWNER_MODE_p
			   | ";" OWNER_MODE_p
			   | epsilon

	IGUAL_ID ::= "=" id
		   | id

	SHOW_DB ::= show databases LIKE_ID

	LIKE_ID ::= like id ";"
		  | ";"

	ALTER_DB ::= alter database id AL_DB ";

	AL_DB ::= rename to id
		| owner to OWNER_DB

	OWNER_DB ::= id
		   | current_user
		   | session_user

	DROP_DB ::= drop database [ if exist ] id ";"

	C_TABLE ::= create table id "(" VALUES ")" ";"

	VALUES ::= COLUM_LIST VALUES_F

	VALUES_F ::= "," CONST_KEY
		   | epsilon
			
	COLUM_LIST ::= id DATA_TYPE COLUM_LIST_F

	COLUM_LIST_F ::= COLUM_LIST_P
               | "," CONST COLUM_LIST_P

	COLUM_LIST_P ::= "," id DATA_TYPE COLUM_LIST_F
               | epsilon

	CONST_KEYS ::= primary key "(" LISTA_ID ")" CONST_KEYS_p
             	| foreign key "(" LISTA_ID ")" reference "(" LISTA_ID ")" CONST_KEYS_p

	CONST_KEYS_p ::= "," primary key "(" LISTA_ID ")" CONST_KEYS_p_F
               	| epsilon

	CONST_KEYS_p_F ::= CONST_KEYS_p
                 | reference "(" LISTA_ID ")"

	CONST ::= default VAL
   	    | [ [ not ] null ]
		| constraint id unique
		| unique
		| constraint id check "(" EXP ")"
		| check "(" EXP ")"
		| primary key
  	    	| reference id "(" id ")"

	DATA_TYPE ::= smallint
			| integer
			| bigint
			| decimal
			| numeric
			| real
			| double precision
			| money
			| text
			| character varying "(" entero ")"
			| varchar "(" entero ")"
			| character "(" entero ")"
			| char "(" entero ")"
			| data	
			| TEMP_EXP


	DROP_TABLE ::= drop table id ";"

	A_TABLE ::= alter table id ACCIONES ";"

	ACCIONES ::= add ACC
		   | alter column id type TYPE
		   | drop constraint id
		   | rename column id to id

	ACC ::= CONST
	  | CONST_KEYS

	S_DELETE ::= delete from id S_DELETE_F

	S_DELETE_F ::= ";"
			 | where id 2=" EXP ";"

	S_INSERT ::= insert into id "(" LISTA_ID ")" S_INSERT_F

	S_INSERT_F ::= values LISTA_VALUES ";"
			 | SELECT ";"

	LISTA_ID ::= id LISTA_ID_p

	LISTA_ID_p ::= "," id LISTA_ID_p
             | epsilon

	LISTA_VALUES ::= "(" LISTA_VALORES ")" LISTA_VALUES_p

	LISTA_VALUES_p  ::= "," "(" LISTA_VALORES ")" [ LISTA_VALUES_p ]
               		 | epsilon

	LISTA_VALORES ::= VALORES LISTA_VALORES_p

	LISTA_VALORES_p ::= "," VALORES LISTA_VALORES_p
                		| epsilon

	VALORES ::= cadena   
		  | entero
		  | decimal

	S_UPDATE ::= update id set LISTA_ASIG S_UPDATE_F

	S_UPDATE_F ::= ";"
            | where id "=" expresion ";"
			
	LISTA_ASIG ::= id "=" VALORES LISTA_ASIG_p

	LISTA_ASIG_p ::= "," id "=" VALORES LISTA_ASIG_p
             	   | epsilon

	EXP ::= not EXP EXP_p
		  | "(" EXP ")" EXP_p
		  | val EXP_p
		  | id  EXP_p
		  | sum "(" exp ")" EXP_p
		  | avg "(" exp ")" EXP_p
		  | max "(" exp ")" EXP_p
		  | MATH_SELECT EXP_p
		  | MATH_SW EXP_p
		  | "|/" EXP EXP_p
		  | "||/" EXP EXP_p
		  | "&" EXP EXP_p
		  | "|" EXP EXP_p
		  | "#" EXP EXP_p
		  | "~" EXP EXP_p
		  | "<<" EXP EXP_p
		  | ">>" EXP EXP_p

	EXP_p ::= and EXP EXP_p
		| or EXP EXP_p
		| "<" EXP EXP_p
		| ">" EXP EXP_p
		| "<=" EXP EXP_p
		| ">=" EXP EXP_p
		| "==" EXP EXP_p
		| "<>" EXP EXP_p
		| "*" EXP EXP_p 
		| "^" EXP EXP_p
		| "/" EXP EXP_p
		| "+" EXP EXP_p
		| "-" EXP EXP_p
		| epsilon

	SELECT ::= select SELECT_LIST from LISTA_FROM LISTA_ORDER ";"

	SELECT_LIST ::= "*" 
              | LISTA_ID1

	LISTA_ID1 ::= EXP LISTA_ID1_p
			| identificador "." identificador LISTA_ID1_p
			| identificador LISTA_ID1_p
			| EXTRACT LISTA_ID1_p
			| now "(" ")" LISTA_ID1_p
			| DATE_PART LISTA_ID1_p

	LISTA_ID1_p ::= "," LISTA_ID1_p_F LISTA_ID1_p
			  | epsilon

	LISTA_ID1_p_F ::= EXP 
				| identificador "." identificador 
				| identificador 
				| EXTRACT 
				| now "(" ")" 
				| DATE_PART 

	TIME_TYPE ::= year
			| month
			| day
			| hour
			| minute
			| second

	LISTA_FROM ::= identificador LISTA_FROM_p
			 | JOINS LISTA_FROM_p
			 | "(" SELECT ")" LISTA_FROM_F

	LISTA_FROM_F ::= as identificador LISTA_FROM_p
			   | LISTA_FROM_p

	LISTA_FROM_p ::= "," identificador LISTA_FROM_p_F LISTA_FROM_p

	LISTA_FROM_p_F ::= as identificador 
                	         | epsilon

	JOINS ::= identificador JOIN_TIPO join identificador JOIN_F

	JOIN_F ::= on EXP
     	 	| epsilon
		 
	JOIN_TIPO::= inner
		   | left
		   | right
		   | full
		   | outer

	LISTA_ORDER ::= order by identificador OPCION_ORDERBY LISTA_ORDER
			  | CONDICION_CONT
			  | limit EXP LISTA_ORDER
			  | offset EXP LISTA_ORDER

	CONDICION_CONT ::= where EXP CONDICION_CONT_F1
				| group by identificador CONDICION_CONT_F2
				| FIN_SELECT

	CONDICION_CONT_F1 ::= FIN_SELECT
					| group by identificador FIN_SELECT

	CONDICION_CONT_F1 ::= FIN_SELECT
					| having EXP FIN_SELECT

	FIN_SELECT::= LISTA_ORDER identificador OPCION_ORDERBY ";"
			| ";"
			| union SELECT_LIST
			| intersect SELECT_LIST
			| except SELECT_LIST

	OPCION_ORDERBY ::= asc
                		| desc

	MATH_SW ::= abs "(" EXP ")" 
		  | cbrt "(" EXP ")"
		  | ceil "(" EXP ")"
	      | ceiling "(" EXP ")"

	MATH_SELECT ::= degrees "(" EXP ")"
			  | div "(" EXP "," EXP ")"
			  | exp "(" EXP ")"
			  | factorial "(" EXP ")"
			  | floor "(" EXP ")"
			  | gcd "(" LISTA_EXP ")"
			  | ln "(" EXP ")"
			  | log "(" EXP ")"
			  | mod "(" EXP "," EXP ")"
			  | pi "(" ")"
			  | power "(" EXP "," EXP ")"
			  | radians  "(" EXP ")"
			  | round "(" EXP ")"
			  | sign"(" EXP ")"
			  | sqrt "(" EXP ")"
			  | width_bucket "(" LISTA_EXP ")"
			  | trunc "(" EXP TRUNC
			  | random "(" ")"

	LISTA_EXP ::= EXP LISTA_EXP_p

	LISTA_EXP_p ::= "," EXP LISTA_EXP_p
			  | epsilon

	TRUNC ::= "," num ")"
		| ")"

	TRIGONOMETRIC ::= acos "(" EXP ")"
				| acosd (" EXP ")"
				| asin "(" EXP ")"
				| asind "(" EXP ")"
				| atan "(" EXP ")"
				| atand "(" EXP ")"
				| atan2 "(" EXP "," EXP ")"
				| atan2d "(" EXP "," EXP ")"
				| cos "(" EXP ")"
				| cosd "(" EXP ")"
				| cot "(" EXP ")"
				| cotd "(" EXP ")"
				| sin "(" EXP ")"
				| sind "(" EXP ")"
				| tan "(" EXP ")"
				| tand "(" EXP ")"
				| sinh "(" EXP ")"
				| cosh "(" EXP ")"
				| asinh "(" EXP ")"
				| acosh "(" EXP ")"
				| atanh "(" EXP ")"

	EXTRACT ::= extract "(" TIME_TYPE from TEMP_EXP cadena ")"

	TIME_TYPE ::= year
			| month
			| day
			| hour
			| minute
			| second

	DATE_PART ::= date_part "(" cadena "," TEMP_EXP cadena ")"

	TEMP_EXP ::= timestamp
		   | time
		   | interval

	BINARY_STRING ::= sha256 "(" cadena ")"   
				| substr "(" id "," num "," num ")"
				| get_byte "(" cadena "," num")"
				| set_byte "(" cadena "," num "," num ")"
				| convert "(" cadena as DATA_TYPE ")"
				| encode "(" cadena "," escape")" 
				| decode "(" cadena "," escape")" 
				| BS_SW
				| BS_I_U 
				| BS_S_I_U_W 


	BS_SW ::= length "(" id ")" 

	BS_I_U ::= md5 "(" cadena ")" 

	BS_S_I_U_W ::= substring "(" id "," num "," num ")" 
			 | trim "(" TRIM ")"    

	TRIM ::= TRIM1 from cadena
	   | cadena

	TRIM1 ::= leading
		| trailing 
		| both


## **Gramática asendente**

	CREATE_TYPE ::= create type id as C_TYPE ";"

	C_TYPE ::= [ enum ] "(" LISTA

	LISTA ::= ID_CADENA LISTA1

	LISTA1 ::= [ LISTA1 ] "," ID_CADENA
			 | [ LISTA1 ] ")"

	ID_CADENA ::= id DATA_TYPE
				| cadena

	CREATE_DB ::= create C_DB

	C_DB ::= [ or replace ] database C_DB1

	C_DB1 ::= [ if  not exists ]  id  OWNER_MODE

	OWNER_MODE ::= [ OWNER_MODE ] owner IGUAL_ID
				 | [ OWNER_MODE ] mode IGUAL_ID
				 | [ OWNER_MODE ] ";"

	IGUAL_ID ::= [ "=" ] id

	SHOW_DB ::= show databases like_id

	LIKE_ID ::= [ like id ] ";"

	ALTER_DB ::= alter  database id AL_DB ";"

	AL_DB ::= rename to id
			| owner to OWNER_DB	

	OWNER_DB ::= id
			   | current_user
			   | session_user

	DROP_DB ::= drop database [ if exist ] id ";"

	C_TABLE ::= create table id "(" CAMPOS ")" ";"

	CAMPOS ::= COLUMN_LIST [ "," CONST_KEYS ]

	COLUMN_LIST ::= [ COLUMN_LIST "," ] id DATA_TYPE [ "," CONST ]

	CONST_KEYS ::= [ CONST_KEYS "," ] primary key "(" LISTA_ID ")"
				 | [ CONST_KEYS ","] foreign key "(" LISTA_ID ")" reference "(" LISTA_ID ")"

	CONST ::= default val
			| [ [ not ] null ]
			| constraint id unique
			| unique
			| constraint id check "(" EXP ")"
			| check "(" EXP ")"
			| primary key
			| reference id "(" id ")"

	DATA_TYPE ::= smallint
				| integer
				| bigint
				| decimal
				| numeric
				| real
				| double precision
				| money
				| text
				| character varying "(" entero ")"
				| varchar( entero )
				| character( entero )
				| char( entero )
				| data	
				| TEMP_EXP


	DROP_TABLE ::= drop table id ";"

	A_TABLE ::= alter table id ACCIONES ";"

	ACCIONES ::= add ACC
			   | alter column id type DATA_TYPE
			   | drop constraint id
			   | rename column id to id

	ACC ::= CONST
		  | CONST_KEYS


	S_DELETE ::= delete from id [ where id "=" EXP ] ";"

	S_INSERT ::= insert into id [ "(" LISTA_ID ")" ] values LISTA_VAL ";"
			   | insert into id ["(" LISTA_ID ")"] S_SELECT

	LISTA_ID  ::= [ LISTA_ID ] "," id
				| id

	LISTA_VAL ::= [ LISTA_VAL ] "," "(" LISTA_VA ")"
				| "(" LISTA_VA ")"

	LISTA_VA ::= LISTA_VA "," VAL
			   | VAL

	val ::= entero
		  | decimal
		  | cadena
		  | booleano

	S_UPDATE ::= update id set LISTA_ASI [ where id "=" EXP ] ";"

	LISTA_ASI ::= [ LISTA_ASI ] "," id "=" VAL
		    | id "=" VAL

	EXP ::= EXP and EXP
		  | EXP or EXP
		  | not EXP
		  | EXP "" EXP
		  | EXP "" EXP
		  | EXP "=" EXP
		  | EXP "=" EXP
		  | EXP "==" EXP
		  | EXP "" EXP
		  | EXP "*" EXP
		  | EXP "^" EXP
		  | EXP "/" EXP
		  | EXP "+" EXP
		  | EXP "-" EXP
		  | "(" EXP ")"
		  | val
		  | id 
		  | sum "(" EXP ")"
		  | avg "(" EXP ")"
		  | max "(" EXP ")"
		  | MATH_SELECT
		  | MATH_SW
		  | "|/" EXP
		  | "||/" EXP
		  | "&" EXP
		  | "|" EXP
		  | "#" EXP
		  | "~" EXP
		  | "<<" EXP
		  | ">>" EXP

	SELECT ::= select SELECT_LIST from LISTA_FROM LISTA_ORDER ";"

	SELECT_LIST ::= "*" 
				  | LISTA_ID1

	LISTA_ID1 ::= [ LISTA_ID1 ] "," EXP
				| [ LISTA_ID1 ] "," identificador "." identificador
				| [ LISTA_ID1 ] "," identificador
				| identificador "." identificador
				| EXP
				| identificador
				| EXTRACT 
				| now "(" ")"
				| DATE_PART

	LISTA_FROM ::= [ LISTA_FROM ] "," identificador as identificador
				 | [ LISTA_FROM ] "," identificador
				 | identificador
				 | JOINS
				 | "(" SELECT ")" as identificador
				 | "(" SELECT ")"

	JOINS ::= identificador JOIN_TIPO join identificador on EXP 
			| identificador JOIN_TIPO join identificador

	JOIN_TIPO::= inner
			   | left
			   | right
			   | full
			   | outer

	LISTA_ORDER ::= order by identificador OPCION_ORDERBY [ LISTA_ORDER ]
				  | CONDICION_CONT
				  | limit EXP [ LISTA_ORDER ]
				  | offset EXP [ LISTA_ORDER ]

	CONDICION_CONT ::= where EXP FIN_SELECT
					 | where EXP group by identificador FIN_SELECT
					 | group by identificador FIN_SELECT
					 | group by identificador having EXP FIN_SELECT
					 | FIN_SELECT

	FIN_SELECT ::= LISTA_ORDER identificador OPCION_ORDERBY ";"
				 | ";"
				 | union SELECT_LIST
				 | intersect SELECT_LIST
				 | except SELECT_LIST

	OPCION_ORDERBY ::= asc
					 | desc


	MATH_SW ::= abs "(" EXP ")" 
			  | cbrt "(" EXP ")"
			  | ceil "(" EXP ")"
			  | ceiling "(" EXP ")"

	MATH_SELECT ::= degrees "(" EXP ")"
				  | div "(" EXP "," EXP ")"
				  | exp "(" EXP ")"
				  | factorial "(" EXP ")"
				  | floor "(" EXP ")"
				  | gcd "(" EXP LISTA _EXP ")"
				  | ln "(" EXP ")"
				  | log "(" EXP ")"
				  | mod "(" EXP "," EXP ")"
				  | pi "(" ")"
				  | power "(" EXP "," EXP ")"
				  | radians  "(" EXP ")"
				  | round "(" EXP ")"
				  | sign"(" EXP ")"
				  | sqrt "(" EXP ")"
				  | width_bucket "(" EXP LISTA_EXP ")"
				  | trunc "(" EXP TRUNC
				  | random "(" ")"

	LISTA_EXP ::= lista_EXP "," EXP
				| "," EXP


	TRIGONOMETRIC ::= acos "(" EXP ")"
					| acosd (" EXP ")"
					| asin "(" EXP ")"
					| asind "(" EXP ")"
					| atan "(" EXP ")"
					| atand "(" EXP ")"
					| atan2 "(" EXP "," EXP ")"
					| atan2d "(" EXP "," EXP ")"
					| cos "(" EXP ")"
					| cosd "(" EXP ")"
					| cot "(" EXP ")"
					| cotd "(" EXP ")"
					| sin "(" EXP ")"
					| sind "(" EXP ")"
					| tan "(" EXP ")"
					| tand "(" EXP ")"
					| sinh "(" EXP ")"
					| cosh "(" EXP ")"
					| asinh "(" EXP ")"
					| acosh "(" EXP ")"
					| atanh "(" EXP ")"

	EXTRACT ::= extract "(" TIME_TYPE from TEMP_EXP cadena ")"

	TIME_TYPE ::= year
				| month
				| day
				| hour
				| minute
				| second

	DATE_PART ::= date_part "(" cadena "," TEMP_EXP cadena ")"

	TEMP_EXP ::=  timestamp
				| time
				| interval

	BINARY_STRING ::= length "(" id ")"
					| substring "(" id "," num "," num ")"
					| trim "(" trim ")"
					| md5 "(" cadena ")"
					| sha256 "(" cadena ")"
					| substr "(" id"," num "," num ")"
					| get_byte "(" cadena "," num")"
					| set_byte "(" cadena "," num "," num ")"
					| convert "(" cadena as DATA_TYPE ")"
					| encode "(" cadena "," "escape" ")" 
					| decode "(" cadena "," "escape ")" 

	TRIM ::=  TRIM1 from cadena
			| cadena

	TRIM1 ::= leading
			| trailing 
			| both


## **Análisis de gramáticas**

Para el analizador sintáctico del proyecto se presentaron dos gramáticas, una descendente y otra ascendente donde se evaluaron diferentes criterios para determinar cuál era la más conveniente a utilizar en el proyecto utilizando la herramienta de Ply. 
Primero se realizó la gramática ascendente para el lenguaje del programa, esta gramática es LR, es decir, que lee de izquierda a derecha sintetizando los atributos de las hojas a la raíz. 
Aplicando la siguiente fórmula se generó la gramática descendente.

![image](https://user-images.githubusercontent.com/53104989/103085335-07f0ab00-45a7-11eb-9b68-ef36e48e3e90.png)

Se dice que todas las gramáticas LL son gramáticas LR y es porque estas surgen de las gramáticas ascendentes. Es más sencillo convertir una gramática LR a LL, que en el caso contrario. Las gramáticas LL quitan la recursividad por la izquierda dejando que sus producciones deriven a la derecha. A continuación se presenta un caso dentro de las gramática donde se usó esta formula. 

Analisis ascendente 
LISTA_ID  ::= [ LISTA_ID ] "," id
			| id
Analisis descendente 
LISTA_ID ::= id LISTA_ID_p

LISTA_ID_p ::= "," id LISTA_ID_p
             | epsilon

Este es un pequeño ejemplo de cómo se derivan las listas de identificadores dentro del lenguaje en ambos analizadores. Se presenta la siguiente entrada para el lenguaje:

![image](https://user-images.githubusercontent.com/53104989/103085402-31113b80-45a7-11eb-83b0-84016650397c.png)

El árbol para la lista de identificadores quedaría de la siguiente manera utilizando un analizador ascendente. 

![image](https://user-images.githubusercontent.com/53104989/103085429-3f5f5780-45a7-11eb-9999-9795688d0ec6.png)

De esta manera podemos ver que el árbol deriva a la izquierda y que los atributos son sintetizados, podemos observar que los valores están en el nodo hoja y a través del analizador van a subir hacia su padre y así recursivamente sintetizando todos los valores del árbol para llegar a la salida del programa.
El árbol para la lista de identificadores quedaría de la siguiente manera utilizando un analizador descendente. 

![image](https://user-images.githubusercontent.com/53104989/103085440-4ab28300-45a7-11eb-8c5d-53677ec33300.png)

Podemos observar que el árbol deriva a la derecha y que los valores están en los nodos hoja, estos valores se sintetizan a los nodos padre y luego deben de ser heredados a sus hermanos o padres. Este tipo de analizador es más complejo de manipular, ya que a su vez podemos observar que estas utilizan el símbolo de epsilon indicando que ya no vienen más símbolos para esas producciones. 
La herramienta de Ply trabaja con gramáticas ascendentes por lo que la manipulación y acceso a los valores es más sencilla de utilizar, mientras que para trabajar con una gramática descendente es necesario que se simule, para ello se debería de implementar el uso de la pila de Ply, haciendo más complejo el uso y el control de los datos. Por lo que para este proyecto llegamos a la conclusión de utilizar la gramática ascendente LR, ya que la misma herramienta ayuda a que se pueda utilizar sin complicación. 




