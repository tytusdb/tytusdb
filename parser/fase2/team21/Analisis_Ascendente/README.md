## GRAMATICA ASCENDENTE

* S 									   ::= instrucciones

* instrucciones 					::= instrucciones instruccion

  ​						  				|instruccion

* instruccion 			::= 		**'CREATE' 'TABLE' 'ID' 'PARIZQ'** campos **'PARDR' 'PTCOMA'**

  ​											| **'CREATE' 'TABLE' 'ID' 'PARIZQ'** campos **'PARDR' 'INHERITS' 'PARIZQ' 'ID' 'PARDR' 'PTCOMA'**
  ​											| **'INSERT' 'INTO' 'ID' 'PARIZQ'** listaID **'PARDR' 'VALUES'** value **'PTCOMA'**

  ​											| **'INSERT' 'INTO' 'ID' 'VALUES'** value **'PTCOMA'**

  ​											| **'UPDATE' 'ID' 'SET'** asignaciones **'PTCOMA'**

  ​											| **'UPDATE' 'ID' 'SET'** asignaciones **'WHERE'** andOr **'PTCOMA'**

  ​											| **'DELETE' 'FROM' 'ID' 'WHERE'** andOr **'PTCOMA'**

  ​											| **'DELETE' 'FROM' 'ID' 'PTCOMA'**

  ​											| **'DROP' 'DATABASE' 'ID' 'PTCOMA'**

  ​                							| **'DROP' 'DATABASE' 'IF' 'EXISTS' 'ID' 'PTCOMA'**

  ​               							 | **'DROP' 'TABLE' 'ID' 'PTCOMA'**

  ​											| opcionCR **'ID' 'PTCOMA'**

  ​               							 | opcionCR **'IF' 'NOT' 'EXISTS' 'ID' 'PTCOMA'**

  ​											| opcionCR **'ID'** complemento **'PTCOMA'**

  ​                							| opcionCR **'IF' 'NOT' 'EXISTS' 'ID'** complemento **'PTCOMA'**

  ​											| **'SHOW' 'DATABASES' 'PTCOMA'**

  ​											| **'SHOW' 'DATABASES' 'LIKE' 'CADENA' 'PTCOMA'**

  ​											| **'ALTER' 'DATABASE' 'ID' 'RENAME' 'TO' 'ID' 'PTCOMA'**

  ​                							| **'ALTER' 'DATABASE' 'ID' 'OWNER' 'TO' 'ID' 'PTCOMA'**

  ​											| **'ALTER' 'TABLE' 'ID'**  lalterprima **'PTCOMA'**

  ​											| **'SELECT'** Time **'PTCOMA'**

  ​											| **'PARIZQ'** select2 **'PARDR'** inst_union

  ​											| select2 **'PTCOMA'**

  ​											|  **'CREATE' 'TYPE' 'ID' 'AS' 'ENUM' 'PARIZQ'** listaExpresiones **'PARDR' 'PTCOMA'**

  ​											|  **'USE' 'DATABASE' 'ID' 'PTCOMA'**

  ​											| **'PARIZQ'** select2 **'PARDR' 'UNION' 'ALL' 'PARIZQ'** select2 **'PARDR' 'PTCOMA'**

  ​											| **'PARIZQ'** select2 **'PARDR' 'INTERSECT' 'ALL' 'PARIZQ'** select2 **'PARDR' 'PTCOMA'**

  ​											| **'PARIZQ'** select2 **'PARDR' 'EXCEPT' 'ALL' 'PARIZQ'** select2 **'PARDR' 'PTCOMA'**

  ​											| **'PARIZQ'** select2 **'PARDR' 'UNION' 'PARIZQ'** select2 **'PARDR' 'PTCOMA'**

  ​											| **'PARIZQ'** select2 **'PARDR' 'INTERSECT' 'PARIZQ'** select2 **'PARDR' 'PTCOMA'**

  ​											| **'PARIZQ'** select2 **'PARDR' 'EXCEPT' 'PARIZQ'** select2 **'PARDR' 'PTCOMA'**

  ​											| **'CREATE' 'INDEX' 'ID' 'ON' 'ID' 'PARIZQ'** listaID **'PARDR' PTCOMA'**

  ​												| **'CREATE' 'INDEX' 'ID' 'ON' 'ID' 'USING' 'HASH' 'PARIZQ'** listaID  **'PARDR' 'PTCOMA'**

  ​												| **'CREATE' 'UNIQUE' 'INDEX' 'ID' 'ON' 'ID' 'PARIZQ'** listaID **'PARDR' 'PTCOMA'**

  ​												| **'ID' 'DOSPUNTOS' 'IGUAL' 'E' 'PTCOMA'**

  ​												| **'ID' 'IGUAL' 'E' 'PTCOMA'**

  ​												| **'RETURN' 'E' 'PTCOMA'**

  ​												| **'ID'** constant tipo colate notnull asignacionvariable **'PTCOMA'**

  ​												| **'CREATE'** orreplace **'FUNCTION' 'ID' 'PARIZQ'** parametros **'PARDR' 'RETURNS'** tipo **'AS' 'E' 'DECLARE'** instrucciones **'BEGIN'** instrucciones **'END''PTCOMA'**

  ​											| **'CREATE'** orreplace **'FUNCTION' 'ID' 'PARIZQ'** parametros **'PARDR'** **'RETURNS'** tipo **'AS' 'E' 'BEGIN' intrucciones 'END' 'PTCOMA'** 

  ​												| **'EXECUTE' 'ID' 'PARIZQ'** listaExpresiones **'PARDR' 'PTCOMA'**

  ​												| **'EXECUTE' 'ID' 'PARIZQ' 'PARDR' 'PTCOMA'**

  ​												| **'IF' 'E' 'THEN'** instrucciones **'END' 'IF' 'PTCOMA'**

  ​												| **'IF' 'E' 'THEN'** instrucciones listaElseIf **'ELSE'** instrucciones **'END' 'IF' 'PTCOMA'** 

  ​												| **'CASE' 'E'** listaWhen elsecase **'END' 'CASE' 'PTCOMA'**

  ​												| **'CREATE'** orreplace **'PROCEDURE' 'ID' 'PARIZQ'** parametros **'PARDR' 'LANGUAGE' 'E' 'AS' 'E' instrucciones 'ID' 'PTCOMA'**

  ​												| **'CREATE'** orreplace **'PROCEDURE' 'ID' 'PARIZQ'** parametros **'PARDR'** **'LANGUAGE' 'E' 'AS' 'E' 'DECLARE'** instrucciones **'BEGIN'** instrucciones **'END' 'PTCOMA'**

  ​												| **'CALL' 'ID' 'PARIZQ' 'PARDR' 'PTCOMA'**

  ​												| **'CREATE'** orreplace **'PROCEDURE' 'ID' 'PARIZQ'** parametros **'PARDR' 'LANGUAGE' 'E' 'AS' 'E 'BEGIN'** instrucciones **'END' 'PTCOMA'**

  ​												| **'DO' 'E' 'DECLARE'** instrucciones **'BEGIN'** instrucciones **'END' 'PTCOMA'**

  ​												| **'DO' 'E' 'BEGIN'** instrucciones **'END' 'PTCOMA'**

  

  

  * campos 					::= 	campos **'COMA'** campo
    	   		 	  					 											| campo

  * campo 						::=	   **'ID'** tipo
        													| **'ID'** tipo acompaniamiento
               	 	 							 | **'CONSTRAINT' 'ID' 'FOREIGN' 'KEY' 'PARIZQ'** listaID **'PARDR' 'REFERENCES' 'ID' 'PARIZQ'** listaID **'PARDR'**
               	  			   				  | **'FOREIGN' 'KEY' 'PARIZQ'** listaID **'PARDR' 'REFERENCES' 'ID' 'PARIZQ'** listaID **'PARDR'**
               									   | **'PRIMARY' 'KEY' 'PARIZQ'** 'listaID' **'PARDR'**
               					 				  | **'CADENA'**

       ​												

       ​										

       ​											

* acompaniamiento    	:: =    acompaniamiento acom
  									  		| acom

* acom 						:: =  **'NOT NULL'**
  	  									| **'NULL'**
                        								| **'UNIQUE' 'PARIZQ'** listaID **'PARDR'**
                        								| **'DEFAULT'** valores
                        								| **'PRIMARY' 'KEY'**
                	  									| **'UNIQUE'**
                	  									| **'UNIQUE ID'**
                				 						 | **'CONSTRAINT' 'ID'**
                				  						| **'REFERENCES' 'ID'**
                				  						| **'CHECK' 'PARIZQ'** checkprima **'PARDR'**

* tipo  					::=           **'SMALLINT'**

  ​                       					 | **'INTEGER'**

  ​                        					| **'BIGINT'**

  ​                       					 | **'DECIMAL'**

  ​                        					| **'NUMERIC'**

  ​                       					 | **'REAL'**

  ​                       					 | **'DOUBLE'**

  ​                       					 | **'MONEY'**

  ​                       					 | **'TEXT'**

  ​                       					 | **'TIMESTAMP'**

  ​                       					 | **'DATE'**

  ​                        					| **'TIME'**

  ​                        					| **'INTERVAL'**

  ​                        					| **'BOOLEAN'**

  ​											| **'SERIAL'**

  ​											| **'CHARACTER' 'PARIZQ' 'ENTERO' 'PARDR'**

  ​                       					 | **'VARCHAR' 'PARIZQ' 'ENTERO' 'PARDR'**

  ​                       					 | **'CHAR' 'PARIZQ' 'ENTERO' 'PARDR'**

  ​                       					 | **'CHARACTER' 'VARYING' 'PARIZQ' 'ENTERO' 'PARDR'**

  ​											| **'DECIMAL' 'PARIZQ' 'ENTERO' 'COMA' 'ENTERO' 'PARDR'**

* listaID            			::=    listaID **'COMA'** var

  ​		       							| var

* values            			 ::=   values **'COMA'** value

  ​		       			  			 |value

* value 			 			 :: =  **'PARIZQ'** listaExpresiones **'PARDR'**

* listaExpresiones          :: = listaExpresiones **'COMA' 'E'**

  ​											| E

* listaValores 				::=  listaValores **'COMA'** valores

  ​		 					 			| valores

* valores 						::= 	**'ENTERO'**

  ​	   										 |  **'NUMDECIMAL'**

  ​	   			 							|  **'CADENA'**

  ​												| Time

* asignaciones 	 		 ::=   asignaciones **'COMA'** asignacion

  ​		 								 |  asignacion

* where 						::=     asignacion

  ​	    									| boolean

  ​	    									| **'NOT'** boolean

  ​            								| columna **'IN' 'PARIZQ'** listaValores **'PARDR'** 

  ​											| columna **'IN' 'PARIZQ'** select2 **'PARDR'**

  ​            								| columna **'BETWEEN'** valores **'AND'** valores

  ​	    									| var **'ILIKE'** valores

  ​            								| var **'LIKE'** valores

  ​            								| valores  comparisonP2

  ​	    									| prim comparisonP2

  ​	    									| boolean  comparisonP2

  ​							    			| var **'IS' 'NOT' 'DISTINCT' 'FROM'** valores

  ​							    			| var **'IS' 'DISTINCT' 'FROM'** valores

  ​											| columna **'ILIKE'** valores

  ​											| columna **'LIKE'** valores

  ​											| columna **'NOT' 'IN' 'PARIZQ'** select2 **'PARDR'**

  ​											| columna **'NOT' 'IN' 'PARIZQ'** listaValores **'PARDR'**

  ​											| **'NOT' 'EXISTS' 'PARIZQ'** select2 **'PARDR'**

  ​											| **'NOT' 'EXISTS' 'PARIZQ'** listaValores **'PARDR'**

  ​											| **'EXISTS' 'PARIZQ'** select2 **'PARDR'**

  ​											| **'EXISTS' 'PARIZQ'** listaValores **'PARDR'**

  ​											

  

* comparisonP2    			 ::=   **'IS' 'TRUE'**

  ​                        					| **'IS' 'FALSE'**

  ​                       	 				| **'IS' 'UNKNOWN'**

  ​											| **'IS' 'NULL'**

  ​                        					| **'IS' 'NOT 'NULL'**

  ​                        					| **'NOTNULL'**

  ​		    					 		   | **'ISNULL'**

  ​											| **'IS' 'NOT' 'TRUE'**

  ​											| **'IS' 'NOT' 'FALSE'**

  ​											| **'IS' 'NOT' 'UNKNOWN'**
  ​		    								

* andOr            			::=       andOr **'AND'** andOr

  ​                       	 				| andOr **'OR'** andOr

  ​											| where

* asignacion      		    ::=    E **'IGUAL'** E

* E               	   			::=     operando
  	                    				| boolean

  ​                        				| unario

  ​                        				| valores

  ​                        				| var

  ​                        				| pnum

  ​                        				| math

  ​										| asignacion

  ​										| trig

  ​										| bina

  ​										| **'PARIZQ'** E **'PARDR'**

  	                    			* boolean          			::=  	**'FALSE'**
  	                    			                          															| 	**'TRUE'**
  	                    			                										| E **'IGUALIGUAL'** E
  	                    			                	                    				| E **'NOIGUAL'** E
  	                    			                                                    							| E **'MENMAY'** E
  	                    			                	                    				| E **'MENOR'** E
  	                    			                	                    				| E **'MAYOR'** E
  	                    			                	                    				| E **'MENORIGUAL'** E
  	                    			                	                    				| E **'MAYORIGUAL'** E
  	                    			
  	                    			* operando         		::=     E **'MAS'** E
  	                    			     												| E **'MENOS'** E
  	                    			             	                    				| E **'MULT'** E
  	                    			     												| E **'DIVI'** E
  	                    			
  	                    			     ​                   							| E **'MODU'** E
  	                    			
  	                    			     ​                   							| E **'EXPO'** E
  	                    			     ​    	                   			 		| E **'MENMEN'** E
  	                    			     ​    	                    					| E **'MAYMAY'** E
  	                    			       	                    			    	   | E **'ANDO'** E
  	                    			       	                    			    	    | E **'ORO'** E
  	                    			
  	                    			     * unario           		::= 		 **'NOTO'** E %prec **'NEG'**   	
  	                    			
  	                    			       ​	 										| **'MENOS'** E %prec **'UMENOS'**		
  	                    			
  	                    			       ​       	                    			 | **'GNOT'** E %prec **'NB'**
  	                    			
  	                    			       ​											 | **'MAS'** E %prec **'UMAS'**
  	                    			
  	                    			       * var                		::=    	**'ID'**
  	                    			
  	                    			         ​										| **'ID' 'PUNTO' 'ID'**
  	                    			
  	                    			         ​										| **'ID' 'PUNTO' 'MULT'**       			     
  	                    			
* pnum 				   ::= 		**'PUNTO'** E



* opcionCR         	::=        **'CREATE' 'DATABASE'**
                          														| **'CREATE' 'OR' 'REPLACE' 'DATABASE'**

* complemento        ::=  	    **'OWNER' 'IGUAL' 'ID'**

  ​                          				| **'OWNER' 'ID'**

  ​										  | **'OWNER' 'IGUAL' 'CADENA' **

  ​										  | **'OWNER' 'IGUAL' 'ID' 'MODE' 'IGUAL' 'ENTERO'**

  ​                        				  | **'OWNER' 'ID' 'MODE' 'IGUAL' 'ENTERO'**

  ​                        				  | **'OWNER' 'IGUAL' 'ID' 'MODE' 'ENTERO'**

  ​                        				  | **'OWNER' 'ID' 'MODE' 'ENTERO'**		

  ​										  | **'OWNER' 'IGUAL' 'CADENA' 'MODE' 'IGUAL' 'ENTERO'**

  * lalterprima         ::=  			lalterprima **'COMA'** alterprima
    																					| alterprima

* alterprima         ::=  	 **'ADD' 'COLUMN'** listaID tipo

  ​									| **'DROP' 'COLUMN' ** listaID

  ​									| **'ADD' 'CHECK'** checkprima

  ​									| **'DROP' 'CONSTRAINT' 'ID'**

  ​									| **'ADD' 'CONSTRAINT' 'ID'**

  ​									| **'ADD' 'FOREIGN' 'KEY' 'PARIZQ'** listaID **'PARDR' 'REFERENCES' 'ID' 'PARIZQ'** listaID **'PARDR'**

  ​									| **'ADD' 'PRIMARY' 'KEY' 'PARIZQ'** listaID **'PARDR'**

  ​									| **'ADD' 'CONSTRAINT' 'ID' 'FOREIGN' 'KEY' 'PARIZQ'** listaID **'PARDR'** **'REFERENCES' 'ID' 'PARIZQ'** listaID **'PARDR'**

  ​									| **'ALTER' 'COLUMN' 'ID' 'TYPE'** tipo

  ​									| **'ALTER' 'COLUMN' 'ID' 'SET' 'NOT' 'NULL'**

  



* Time         ::=					  | **'EXTRACT' 'PARIZQ'** momento **'FROM' 'TIMESTAMP'  'CADENA' 'PARDR'**

  ​											| date_part **'PARIZQ' 'CADENA' 'COMA' 'INTERVAL' 'CADENA' 'PARDR'**

  ​											| **'NOW' 'PARIZQ' 'PARDR'**

  ​											| **'TIMESTAMP' 'CADENA'**

  ​											| **'CURRENT_TIME'**

  ​											| **'CURRENT_DATE'**

* momento         ::=			 **'YEAR'**
                          				| **'MONTH'**
                                                    				| **'DAY'**
                                                  				 | **'HOUR'**
                                                    				| **'MINUTE'**
                                                    				| **'SECOND'**

                          			* inst_union 		::= 			 **'UNION' 'ALL' PARIZQ** select2 **'PARDR' 'PTCOMA'**
                          			  																							| **'INTERSECT' 'ALL'  'PARIZQ'** select2 **'PARDR' 'PTCOMA'**
                          			                											| **'EXCEPT' 'ALL' 'PARIZQ'** select2 **'PARDR' 'PTCOMA'**
                          			                											| **'UNION' 'PARIZQ'** select2 **'PARDR' 'PTCOMA'**
                          			                											| **'INTERSECT' 'PARIZQ'** select2 **'PARDR' 'PTCOMA'**
                          			                											| **'EXCEPT' 'PARIZQ'** select2 **'PARDR' 'PTCOMA'**
                          			
                          			  										* compSelect   	 ::= 			table_expr
                          			  										  																					| table_expr **'GROUP' 'BY'**  compGroup
                          			
* compGroup        ::= 			list

  ​											| list **'GROUP' 'BY'**  compGroup

  ​											| **'GROUP' 'BY'**  compGroup 

  ​											| list ordenar

  ​											| list ordenar **'HAVING'** andOr

* select2  			::=  			  **'SELECT' 'DISTINCT'** select_list **'FROM'** inner compSelec
  ​												| **'SELECT'** select_list **'FROM'** subquery inner orderby limit
    ​    											| **'SELECT'** select_list
    ​    											| **'SELECT'** select_list **'FROM'** subquery inner **'WHERE'** complemSelect orderby limit
    ​    											| **'SELECT' 'DISTINCT'** select_list **'FROM'** subquery inner **'WHERE'** complemSelect orderby limit

* orderby 				:: =  **'ORDER' 'BY'** listaID

​									| 	

* ordenar				 ::=  **'DESC'**

​								   | **'ASC'** 	

​								   | 

* limit 					::=  **'LIMIT' 'ENTERO'**
  	   																	| **'LIMIT' 'ALL'**
                	   							| **'LIMIT' 'ENTERO' 'OFFSET' 'ENTERO'**
                	   							| 
* subquery 			:: = **'PARIZQ'** select2 **'PARDR'**

​									| 

* inner    				::=   	list

     ​										| compSelect
     ​    									| table_expr **'INNER' 'JOIN'** columna **'ON'** asignacion
     ​    									| table_expr **'INNER' 'JOIN'** columna **'ON'** asignacion complemSelect

* complemSelect 		::= 		andOr
  		  								

​												| andOr **'GROUP' 'BY'**  compGroup
  		  								
* select_list 				::=  			 **'MULT'**

     ​													| list

* list 							::= 	 list **'COMA'** columna

     ​											| columna

* columna 					::=    		**'CASE'** cases **'END' 'ID'**
  												

​													| prim **'AS'** seg

​													| prim seg

​													| prim 
  												
* cases 					::= 		cases case
  	   								

​											|case
  	   								
* case 					::= 		**'WHEN'** asignacion **'THEN'** valores

* opcionID 				::=		    **'PUNTO'** ascolumnaux

     ​												| **'ID'**

* prim                         :: = var

​										| math

​										| trig

​										| bina

​										| Time

​										|  **'PARIZQ'** select2 **'PARDR'**

* seg							:: = ID

​										| CADENA

* math  						::= 		**'ABS' 'PARIZQ'** E **'PARDR'**

​                								| **'CBRT' 'PARIZQ'** E **'PARDR'**

​                								| **'CEIL' 'PARIZQ'** E **'PARDR'**

​								                | **'CEILING' 'PARIZQ'** E **'PARDR'**

​								                | **'DEGREES' 'PARIZQ'** E **'PARDR'**

​								                | **'EXP' 'PARIZQ'** E **'PARDR'**

​								                | **'FACTORIAL' 'PARIZQ'** E **'PARDR'**

​								                | **'FLOOR' 'PARIZQ'** E **'PARDR'**

​								                | **'LCM' 'PARIZQ'** E **'PARDR'**

​								                | **'LN' 'PARIZQ'** E **'PARDR'**

​								                | **'LOG' 'PARIZQ'** E **'PARDR'**

​								                | **'LOG10' 'PARIZQ'** E **'PARDR'**

​								                | **'RADIANS' 'PARIZQ'** E **'PARDR'**

​								                | **'ROUND' 'PARIZQ'** E **'PARDR'**

​								                | **'SIGN' 'PARIZQ'** E **'PARDR'**

​								                | **'SQRT' 'PARIZQ'** E **'PARDR'**

​								                | **'TRUC' 'PARIZQ'** E **'PARDR'**

​								                | **'WIDTH_BUCKET' 'PARIZQ'** E **'PARDR'**

​								                | **'SETSEED' 'PARIZQ'** E **'PARDR'**

​								                | **'SUM' 'PARIZQ'** E **'PARDR'**

​												| **'MD5' 'PARIZQ' **E **'PARDR'**

​												| **'SING' 'PARIZQ'** E **'PARDR'**

​												| **'WIDTH_BUCKET' 'PARIZQ'** listaValores **'PARDR'**

​								                | **'AVG' 'PARIZQ'** E **'PARDR'**

​								                | **'COUNT' 'PARIZQ'** E **'PARDR'**

​												| **'COUNT' 'PARIZQ' 'MULT' 'PARDR'**

​								                | **'MIN' 'PARIZQ'** E **'PARDR'**

​								                | **'MAX' 'PARIZQ'** E **'PARDR'**

​												| **'DIV' 'PARIZQ'** E **'COMA'** E **'PARDR'**

​												| **'TRUNC' 'PARIZQ'** E **'PARDR'**

​								                | **'GCD' 'PARIZQ'** E **'COMA'** E **'PARDR'**

​								                | **'MOD' 'PARIZQ'** E **'COMA'** E **'PARDR'**

​								                | **'POWER' 'PARIZQ'** E **'COMA'** E **'PARDR'**

​												| **'PI' 'PARIZQ' 'PARDR'**

​                								| **'RANDOM' 'PARIZQ' 'PARDR'**

​												| **'MIN_SCALE'**

​								                | **'SCALE'**

​								                | **'TRIM_SCALE'**

* bina 			::=    	    **'LENGTH' 'PARIZQ'** E **'PARDR'**

     ​										| **'SHA256' 'PARIZQ'** E **'PARDR'**

     ​              						| **'ENCODE' 'PARIZQ'** E **'PARDR'**

     ​              						| **'DECODE' 'PARIZQ' E 'PARDR'**

     ​										| **SUBSTRING' 'PARIZQ'** var **'COMA' **'ENTERO' 'COMA' 'ENTERO' 'PARDR'**

     ​										| **'SUBSTR' 'PARIZQ'** var **'COMA' 'ENTERO' 'COMA' 'ENTERO' 'PARDR'**

     ​										| **'TRIM' 'PARIZQ' 'CADENA' 'FROM'** columna **'PARDR'**

     ​										| **'GET_BYTE' 'PARIZQ' 'CADENA' 'COMA' 'ENTERO' 'PARDR'**

     ​										| **'SET_BYTE' 'PARIZQ' 'CADENA' 'COMA' 'ENTERO' 'COMA' 'ENTERO' 'PARDR'**

     ​										| **'CONVERT' 'PARIZQ' 'CADENA' 'AS'** tipo **'PARDR'**

     ​										| **'GREATEST' 'PARIZQ'** listaValores **'PARDR'**

     ​										| **'LEAST' 'PARIZQ'** listaValores **'PARDR'**

     ​    							

* trig 					::= 			**'ACOS' 'PARIZQ'** E **'PARDR'**
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

  							             * parametro  	:: = **ID** tipo
  							               							             
  							                 ​						 | 
  							             
*  parametros ::= parametros **COMA** parametro

     ​						| paramaetro

* constant :: = **'CONSTANT'**

     ​					| 

* colate ::= **'COLLATE' 'ID'**

     ​				| 

* notnull ::= **'NOTNULL'**

     ​					|

* asignacionvariable  ::= **'DEFAULT' 'E'**

     ​									| **'IGUAL' 'E'**

     ​									| **'DOSPUNTOS' 'IGUAL'**

     ​									| 

* orreplace ::= **'OR' 'REPLACE'**

     ​				|

* listaElseIf ::= listaElseIf elseif

     ​						| elseif

* elseif ::= **'ELSIF' 'E' 'THEN'** instrucciones

     ​				| 

* listaWhen ::= listaWhen when

     ​					| when

* when : **'WHEN'** listaExpresiones **'THEN'** instrucciones

* elsecase ::= **'ELSE'** instrucciones

     ​				|

* checkprima 			::=      listaValores
                      						| E 					