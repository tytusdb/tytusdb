## GRAMATICA ASCENDENTE

	S 				::= instrucciones
	instrucciones 			::= instrucciones instruccion
					|instruccion
	instruccion 			::= 	**'CREATE' 'TABLE' 'ID' 'PARIZQ'** campos **'PARDR' 'PTCOMA'**
					| **'CREATE' 'TABLE' 'ID' 'PARIZQ'** campos **'PARDR' 'INHERITS' 'PARIZQ' 'ID' 'PARDR' 'PTCOMA'**
					| **'INSERT' 'INTO' 'ID' 'PARIZQ'** listaID **'PARDR' 'VALUES'** values **'PTCOMA'**
					| **'INSERT' 'INTO' 'ID' 'VALUES'** values **'PTCOMA'**
					| **'UPDATE' 'ID' 'SET'** asignaciones **'PTCOMA'**
					| **'UPDATE' 'ID' 'SET'** asignaciones **'WHERE'** andOr **'PTCOMA'**
					| **'DELETE' 'FROM' 'ID' 'WHERE'** andOr **'PTCOMA'**
					| **'DELETE' 'FROM' 'ID' 'PTCOMA'**
					| **'DROP' 'DATABASE' 'ID' 'PTCOMA'**
					| **'DROP' 'DATABASE' 'IF' 'EXISTS' 'ID' 'PTCOMA'**
					| **'DROP' 'TABLE' 'ID' 'PTCOMA'**
					| opcionCR **'ID' 'PTCOMA'**
					| opcionCR **'IF' 'NOT' 'EXISTS' 'ID' 'PTCOMA'**
					| opcionCR **'ID'** complemento **'PTCOMA'**
					| opcionCR **'IF' 'NOT' 'EXISTS' 'ID'** complemento **'PTCOMA'**
					| **'SHOW' 'DATABASES' 'PTCOMA'**
					| **'SHOW' 'DATABASES' 'LIKE' 'CADENA' 'PTCOMA'**
					| **'ALTER' 'DATABASE' 'ID' 'RENAME' 'TO' 'ID' 'PTCOMA'**
					| **'ALTER' 'DATABASE' 'ID' 'OWNER' 'TO' 'ID' 'PTCOMA'**
					| **'ALTER' 'TABLE' 'ID'**  lalterprima **'PTCOMA'**
					| **'SELECT'** Time **'PTCOMA'**
					| **'PARIZQ'** select2 **'PARDR'** inst_union
					| select2 **'PTCOMA'**
					|  **'CREATE' 'TYPE' 'ID' 'AS' 'ENUM' 'PARIZQ'** campos **'PARDR' 'PTCOMA'**

	campos 				::= 	campos **'COMA'** campo
						|campo
	campo 				::=	  **'ID'** tipo
						| **'ID'** tipo acompaniamiento
						| **'CONSTRAINT' 'ID' 'FOREIGN' 'KEY' 'PARIZQ'** listaID **'PARDR' 'REFERENCES' 'ID' 'PARIZQ'** listaID **'PARDR'**
						| **'FOREIGN' 'KEY' 'PARIZQ'** listaID **'PARDR' 'REFERENCES' 'ID' 'PARIZQ'** listaID **'PARDR'**
						| **'PRIMARY' 'KEY' 'PARIZQ'** 'listaID' **'PARDR'**
						| **'CADENA'**

	acompaniamiento    	:: =    acompaniamiento acom
					| acom

	acom 			:: =  **'NOT NULL'**
					| **'NULL'**
					| **'UNIQUE' 'PARIZQ'** listaID **'PARDR'**
					| **'DEFAULT'** valores
					| **'PRIMARY' 'KEY'**
					| **'UNIQUE'**
					| **'UNIQUE ID'**
					| **'CONSTRAINT' 'ID'**
					| **'REFERENCES' 'ID'**
					| **'CHECK' 'PARIZQ'** checkprima **'PARDR'**

	tipo  			::=           **'SMALLINT'**
					     | **'INTEGER'**
					     | **'BIGINT'**
					     | **'DECIMAL'**
					     | **'NUMERIC'**
					     | **'REAL'**
					     | **'DOUBLE'**
					     | **'MONEY'**
					     | **'TEXT'**
					     | **'TIMESTAMP'**
					     | **'DATE'**
					     | **'TIME'**
					     | **'INTERVAL'**
					     | **'BOOLEAN'**
					     | **'CHARACTER' 'PARIZQ' 'ENTERO' 'PARDR'**
					     | **'VARCHAR' 'PARIZQ' 'ENTERO' 'PARDR'**
					     | **'CHAR' 'PARIZQ' 'ENTERO' 'PARDR'**
					     | **'CHARACTER' 'VARYING' 'PARIZQ' 'ENTERO' 'PARDR'**

	listaID            	  ::=    listaID **'COMA'** var
					 | var

	values            	  ::=   values **'COMA'** value
					|value

	value 			  :: =  **'PARIZQ'** listaValores **'PARDR'**

	listaValores 			::=  listaValores **'COMA'** valores
					     | valores

	valores 		  ::= 	**'ENTERO'**
					|  **'NUMDECIMAL'**
					|  **'CADENA'**
					| **'NOW' 'PARIZQ' 'PARDR'**
					| columna

	asignaciones 	 	    ::=   asignaciones **'COMA'** asignacion
					  |  asignacion

	where 		    	::=     asignacion
					| boolean
					| **'NOT'** boolean
					| columna **'IN' 'PARIZQ'** listaValores **'PARDR'** 
					| columna **'BETWEEN'** valores **'AND'** valores
					| var **'ILIKE'** valores
					| var **'LIKE'** valores
					| valores  comparisonP2
					| var comparisonP2
					| boolean  comparisonP
					| var **'IS' 'NOT' 'DISTINCT' 'FROM'** valores
					| var **'IS' 'DISTINCT' 'FROM'** valores
					| var **'NOT' 'IN' 'PARIZQ'** select2 **'PARDR'**

	comparisonP    			 ::=   **'IS' 'TRUE'**
					| **'IS' 'FALSE'**
					| **'IS' 'UNKNOWN'**
					| **'IS' 'NOT TRUE'**
					| **'IS' 'NOT FALSE'**
					| **'IS' 'NOT UNKNOWN'**

	comparisonP2    		::=    **'IS' 'NULL'**
					 	| **'IS' 'NOT' 'NULL'**
						| **'NOTNULL'**
						| **'ISNULL'**

	andOr            			::=       andOr **'AND'** andOr
							| andOr **'OR'** andOr
							| where

	asignacion      		    ::=    E **'IGUAL'** E

	E               	   	::=     operando
						| boolean
						| unario
						| valores
						| var
						| pnum
						| math
						| **'PARIZQ'** E **'PARDR'**

	boolean          			::=  	**'FALSE'**
							| 	**'TRUE'**
							| E **'IGUALIGUAL'** E
							| E **'NOIGUAL'** E
							| E **'MENMAY'** E
							| E **'MENOR'** E
							| E **'MAYOR'** E
							| E **'MENORIGUAL'** E
							| E **'MAYORIGUAL'** E

	operando         		::=     E **'MAS'** E
						| E **'MENOS'** E
						| E **'MULT'** E
						| E **'DIVI'** E
						| E **'MODU'** E
						| E **'EXPO'** E
						| E **'MENMEN'** E
						| E **'MAYMAY'** E
						| E **'ANDO'** E
						| E **'ORO'** E

	unario           		::= 		 **'NOTO'** E
							| **'MENOS'** E
							| **'GNOT'** E
							| **'MAS'** E

	var                		::=    	**'ID'**
						| **'ID' 'PUNTO' 'ID'**

	pnum 				   ::= 		**'PUNTO'** E



	opcionCR         	::=        **'CREATE' 'DATABASE'**
						| **'CREATE' 'OR' 'REPLACE' 'DATABASE'**

	complemento        ::=  	    **'OWNER' 'IGUAL' 'ID'**
						| **'OWNER' 'ID'**
						| **'OWNER' 'IGUAL' 'ID' 'MODE' 'IGUAL' 'ENTERO'**
						| **'OWNER' 'ID' 'MODE' 'IGUAL' 'ENTERO'**
						| **'OWNER' 'IGUAL' 'ID' 'MODE' 'ENTERO'**
						| **'OWNER' 'ID' 'MODE' 'ENTERO'**		

	lalterprima         ::=  			lalterprima **'COMA'** alterprima
							| alterprima

	alterprima         ::=  	 **'ADD' 'COLUMN' 'ID'** tipo
					| **'DROP' 'COLUMN' 'ID'**
					| **'ADD' 'CHECK'** checkprima
					| **'DROP' 'CONSTRAINT' 'ID'**
					| **'ADD' 'CONSTRAINT' 'ID' 'UNIQUE' 'PARIZQ' 'ID' 'PARDR'**
					| **'ADD' 'FOREIGN' 'KEY' 'PARIZQ'** listaID **'PARDR' 'REFERENCES'** listaID
					| **'ALTER' 'COLUMN' 'ID' 'TYPE'** tipo
					| **'ALTER' 'COLUMN' 'ID' 'SET' 'NOT' 'NULL'**



	Time         ::=		 **'EXTRACT' 'PARIZQ'** momento **'FROM' 'TIMESTAMP'  'CADENA' 'PARDR'**
					| date_part **'PARIZQ' 'CADENA' 'COMA' 'INTERVAL' 'CADENA' 'PARDR'**
					| **'NOW' 'PARIZQ' 'PARDR'**
					| **'TIMESTAMP' 'CADENA'**
					| **'CURRENT_TIME'**
					| **'CURRENT_DATE'**

	momento         ::=			 **'YEAR'**
						| **'MONTH'**
						| **'DAY'**
						| **'HOUR'**
						| **'MINUTE'**
						| **'SECOND'**

	inst_union 		::= 			 **'UNION' 'ALL' PARIZQ** select2 **'PARDR' 'PTCOMA'**
							| **'INTERSECT' 'ALL'  'PARIZQ'** select2 **'PARDR' 'PTCOMA'**
							| **'EXCEPT' 'ALL' 'PARIZQ'** select2 **'PARDR' 'PTCOMA'**
							| **'UNION' 'PARIZQ'** select2 **'PARDR' 'PTCOMA'**
							| **'INTERSECT' 'PARIZQ'** select2 **'PARDR' 'PTCOMA'**
							| **'EXCEPT' 'PARIZQ'** select2 **'PARDR' 'PTCOMA'**

	compSelect   	 ::= 			table_expr
						| table_expr **'GROUP' 'BY'**  compGroup

	compGroup        ::= 			list
						| list **'HAVING'** andOr

	select2  			::=  	 **'SELECT' 'DISTINCT'** select_list **'FROM'** inner compSelect
						| **'SELECT'** select_list **'FROM'** subquery inner orderby limit
						| **'SELECT'** select_list
						| **'SELECT'** select_list **'FROM'** subquery inner **'WHERE'** complemSelect orderby limit
						| **'SELECT' 'DISTINCT'** select_list **'FROM'** subquery inner **'WHERE'** complemSelect orderby limit

	orderby 				:: =  **'ORDER' 'BY'** listaID


	limit 					::=  **'LIMIT' 'ENTERO'**
						| **'LIMIT' 'ALL'**
						| **'LIMIT' 'ENTERO' 'OFFSET' 'ENTERO'**
						| 
	subquery 			:: = **'PARIZQ'** select2 **'PARDR'**

	inner    				::=   table_expr
							| compSelect
							| table_expr **'INNER' 'JOIN'** columna **'ON'** asignacion
							| table_expr **'INNER' 'JOIN'** columna **'ON'** asignacion complemSelect

	complemSelect 		::= 		andOr
						| andOr **'GROUP' 'BY'**  compGroup

	select_list 				::=  		 **'MULT'**
								| list

	list 							::= 	 list **'COMA'** columna
									| columna

	columna 					::=    		**'CASE'** cases **'END' 'ID'**
									| **'PARIZQ'** select2 **'PARDR'**
									| Time
									| Time **'AS' 'ID'**
									| Time **'ID'**
									| Time **'AS' 'CADENA'**  
									| Time **'CADENA'*
									| **'ID'** opcionID
									| **'ID' 'AS' 'ID'**
									| **'ID'**
									| **'ID' 'ID'**
									| ** 'ID' CADENA'**
									| **'ID' 'AS' 'CADENA'**
									| math **'AS' 'ID'**
									| math **'AS' 'CADENA'**
									| math **'CADENA'**
									| math **'ID'**
									| math
									| trig **'AS' 'CADENA'**
									| trig
									| trig **'AS' 'ID'**
									| bina **'AS' 'CADENA'**
									| bina
									| bina **'AS' 'ID'**

	cases 					::= 		cases case
								|case

	case 					::= 		**'WHEN'** asignacion **'THEN'** valores

	opcionID 				::=		    **'PUNTO'** ascolumnaux
									| **'ID'**

	ascolumnaux 			::= 	**'ID' 'AS' 'ID'**
						| **'ID' 'CADENA'**
						| **'ID' 'ID'**
						| **'ID'**
						| **'ID' 'AS' 'CADENA'**

	math  						::= 		**'ABS' 'PARIZQ'** E **'PARDR'**
									| **'CBRT' 'PARIZQ'** E **'PARDR'**
									| **'CEIL' 'PARIZQ'** E **'PARDR'**
									| **'CEILING' 'PARIZQ'** E **'PARDR'**
									| **'DEGREES' 'PARIZQ'** E **'PARDR'**
									| **'EXP' 'PARIZQ'** E **'PARDR'**
									| **'FACTORIAL' 'PARIZQ'** E **'PARDR'**
									| **'FLOOR' 'PARIZQ'** E **'PARDR'**
									| **'LCM' 'PARIZQ'** E **'PARDR'**
									| **'LN' 'PARIZQ'** E **'PARDR'**
									| **'LOG' 'PARIZQ'** E **'PARDR'**
									| **'LOG10' 'PARIZQ'** E **'PARDR'**
									| **'RADIANS' 'PARIZQ'** E **'PARDR'**
									| **'ROUND' 'PARIZQ'** E **'PARDR'**
									| **'SIGN' 'PARIZQ'** E **'PARDR'**
									| **'SQRT' 'PARIZQ'** E **'PARDR'**
									| **'TRUC' 'PARIZQ'** E **'PARDR'**
									| **'WIDTH_BUCKET' 'PARIZQ'** E **'PARDR'**
									| **'SETSEED' 'PARIZQ'** E **'PARDR'**
									| **'SUM' 'PARIZQ'** E **'PARDR'**
									| **'AVG' 'PARIZQ'** E **'PARDR'**
									| **'COUNT' 'PARIZQ'** E **'PARDR'**
									| **'MIN' 'PARIZQ'** E **'PARDR'**
									| **'MAX' 'PARIZQ'** E **'PARDR'**
											| **'DIV' 'PARIZQ'** E **'COMA'** E **'PARDR'**
									| **'GCD' 'PARIZQ'** E **'COMA'** E **'PARDR'**
									| **'MOD' 'PARIZQ'** E **'COMA'** E **'PARDR'**
									| **'POWER' 'PARIZQ'** E **'COMA'** E **'PARDR'**
											| **'PI' 'PARIZQ' 'PARDR'**
									| **'RANDOM' 'PARIZQ' 'PARDR'**
											| **'MIN_SCALE'**
									| **'SCALE'**
									| **'TRIM_SCALE'**

	bina 			::=    	 **'LENGTH' 'PARIZQ'** E **'PARDR'**
					| **'SHA256' 'PARIZQ'** E **'PARDR'**
					| **'ENCODE' 'PARIZQ'** E **'PARDR'**
					| **'DECODE' 'PARIZQ' E 'PARDR'**
					| **SUBSTRING' 'PARIZQ'** var **'COMA' **'ENTERO' 'COMA' 'ENTERO' 'PARDR'**
					| **'SUBSTR' 'PARIZQ'** var **'COMA' 'ENTERO' 'COMA' 'ENTERO' 'PARDR'**
					 | **'TRIM' 'PARIZQ' 'CADENA' 'FROM'** columna **'PARDR'**
					 | **'GET_BYTE' 'PARIZQ' 'CADENA' 'COMA' 'ENTERO' 'PARDR'**
					 | **'SET_BYTE' 'PARIZQ' 'CADENA' 'COMA' 'ENTERO' 'COMA' 'ENTERO' 'PARDR'**
					| **'CONVERT' 'PARIZQ' 'CADENA' 'AS'** tipo **'PARDR'**
					 | **'GREATEST' 'PARIZQ'** listaValores **'PARDR'**
					| **'LEAST' 'PARIZQ'** listaValores **'PARDR'**

	trig 					::= 			**'ACOS' 'PARIZQ'** E **'PARDR'**
									      | **'ACOSD' 'PARIZQ'** E **'PARDR'**
									      | **'ASIN' 'PARIZQ'** E **'PARDR'**
									      | **'ASIND' 'PARIZQ'** E **'PARDR'**
									      | **'ATAN' 'PARIZQ'** E **'PARDR'**
									      | **'ATAND' 'PARIZQ'** E **'PARDR'**
									      | **'ATAN2' 'PARIZQ'** E **'PARDR'**
									      | **'ATAN2D'** **'PARIZQ'** E **'PARDR'**
									      | **'COS'** **'PARIZQ'** E **'PARDR'**
									      | **'COSD' 'PARIZQ'** E **'PARDR'**
									      | **'COT' 'PARIZQ'** E **'PARDR'**
									      | **'COTD' 'PARIZQ'** E **'PARDR'**
									      | **'SIN' 'PARIZQ'** E **'PARDR'**
									      | **'SIND' 'PARIZQ'** E **'PARDR'**
									      | **'TAN' 'PARIZQ'** E **'PARDR'**
									      | **'TAND' 'PARIZQ'** E **'PARDR'**
									      | **'SINH' 'PARIZQ'** E **'PARDR'**
									      | **'COSH' 'PARIZQ'** E **'PARDR'**
									      | **'TANH' 'PARIZQ'** E **'PARDR'**
									      | **'ASINH' 'PARIZQ'** E **'PARDR'**
									      | **'ACOSH' 'PARIZQ'** E **'PARDR'**
									      | **'ATANH' 'PARIZQ'** E **'PARDR'**

	table_expr 				::=  			table_expr **'COMA'** tablaR
									| tablaR

	tablaR					 ::=  			**'ID' 'ID'**
									| **'ID' 'AS' 'ID'**
									| **'ID'**

	checkprima 			::=      listaValores
						| E 					
