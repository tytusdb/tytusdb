# GRAMÁTICA DESCENDENTE

- s ::=                           instrucciones

- instrucciones ::=        instruccion instrucciones'

  ​							      | epsilon

- instrucciones' ::=       instruccion instrucciones

  ​							      | epsilon

- instruccion  ::=           **'CREATE'** createp **';'**

  ​         		             	| **'ALTER'** factorizar_alter **';'**

  ​          		                | **'DROP'** droptp **';'**

  ​          		                | **'SELECT'** selectp **';'**

  ​          		                | **'INSERT' 'INTO' 'IDENTIFICADOR' 'VALUES' '('** expresion **')' ';'**

  ​				                  | **'UPDATE' 'IDENTIFICADOR' 'SET'** expresion **'WHERE'** expresion **';'**

  ​       			               | **'DELETE' 'FROM' 'IDENTIFICADOR' 'WHERE'** expresion **';'**

- instruccion ::=            **'SHOW' 'DATABASES'** opcional3 **';'**

- factorizar_alter ::= 	**'DATABASE'** alterp

  ​             					  | **'TABLE'** l_campo

- selectp ::=                   **'EXTRACT' '('** l_campo **')'**

  ​                                   | **'DATE_PART' '('** expresion l_campo **')'**

  ​                                   | **'NOW' '(' ')'**

  ​                                   | **'GREATEST' '('** expresion **')'**

  ​                                   | **'LEAST' '('** expresion **')'**

  ​                                   | expresion **'FROM'**

- droptp ::=                    **'DATABASE'** dropp **'IDENTIFICADOR'**

  ​                                   | **'TABLE' 'IDENTIFICADOR'**

- dropp ::=                     **'IF' 'EXISTS'**

  ​									| epsilon

- alterp ::=                     **'IDENTIFICADOR'** alterpp

- alterpp ::=                    **'RENAME' 'TO'** alterppp

  ​                                    | **'OWNER' 'TO'** alterppp

* alterppp ::=                  **'IDENTIFICADOR'**

  ​                                    | **'CURRENT_USER'**

  ​                                    | **'SESSION_USER'**

* createp ::=                   **'OR' 'REPLACE' 'DATABASE'** opcional **'IDENTIFICADOR'** opcional

  ​                                    | **'TYPE'** createpp

  ​                                    | **'DATABASE'** createpp

  ​                                    | **'TABLE'** createpp

* createpp ::=                 **'IDENTIFICADOR'** createtp

* createtp ::=                   **'AS' 'ENUM' '('** l_cadenas **')'**

  ​                                     | opcional

  ​                                     | **'('** l_campos **')'** createqp

* createqp ::=                  **'INHERITS' '(' 'IDENTIFICADOR' ')'**

  ​									 | epsilon

  

* l_campos ::=                **'IDENTIFICADOR'** l_campo l_campos

  ​									| **',' 'IDENTIFICADOR'** l_campo l_campos

  ​									| **','** l_campo l_campos

  ​									| epsilon

* l_campo ::=                 tipo l_campo

  ​									| epsilon

* l_altercolumn ::=         **'IDENTIFICADOR' 'TYPE'** l_campo l_altercolumn

  ​									| **'IDENTIFICADOR' 'SET' 'NOT' 'NULL'**

  ​									| **',' 'ALTER' 'COLUMN' 'IDENTIFICADOR' 'TYPE'** l_campo l_altercolumn

  ​									| **',' 'ALTER' 'COLUMN' 'IDENTIFICADOR' 'SET' 'NOT' NULL**

* tipo ::=                         '**INTEGER**'

  ​     							   | '**ADD**'

  ​    							    | '**RENAME**'

  ​      							  | '**DATE**'

  ​      							  | **'SET'**

  ​      							  | **'NOT'**

  ​      							  | **'NULL'**

  ​      							  | **'PRIMARY'** **'KEY'**

  ​      							  | **'FOREIGN'** **'KEY'**

  ​      							  | **'CONSTRAINT'**

  ​      							  | **'UNIQUE'**

  ​      							  | **'IDENTIFICADOR'**

  ​      							  | **'REFERENCES'**

  ​      							  | **'ALTER'** **'COLUMN'** l_altercolumn

  ​       							 | **'DROP'**

  ​        							| **'('** l_cadenas **')'**

  ​        							| **'YEAR'**

  ​        							| **'FROM'**

  ​        							| **'TIMESTAMP'**

  ​        							| **'HOUR'**

  ​        							| **'SECOND'**

  ​        							| **'MINUTE'**

  ​        							| **'DAY'**

  ​      		  					| **'MONTH'**

* tipo ::=                         **'MONEY'**

  ​      							  | **'SMALLINT'**

  ​      							  | **'BIGINT'**

  ​        							| **'DECIMAL'**

  ​    							    | '**NUMERIC**'

  ​        							| **'REAL'**

  ​        							| **'CARACTER_O_CADENA'**

  ​									| **'DOUBLE'** **'PRECISION'**

  ​									| **'DOUBLE'**

  ​       							 | **'NOENTERO'**

  ​      							  | **'TEXT'**

  ​      							  | **'BOOLEAN'**

* tipo ::=                        **'VARCHAR'** **'('** **'NOENTERO'** **')'**

  ​       							| **'CHAR'** **'('** **'NOENTERO'** **')'**

  ​     							  | **'CHECK'** **'('** expresion **')'**

  ​     							  | **'CHARACTER'** **'('** **'NOENTERO'** **')'**

  ​								   | **'CHARACTER'** '**VARYING**' **'('** **'NOENTERO'** **')'**

  ​								   | **'DECIMAL'** **'('** **'NOENTERO'** **','** **'NOENTERO'** **')'**

* l_cadenas ::=              **'CARACTER_O_CADENA'** l_cadenasp

  ​         						  | **'IDENTIFICADOR'** l_cadenasp

* l_cadenasp ::=            **','** **'CARACTER_O_CADENA'** l_cadenasp

  ​          						 | **','** **'IDENTIFICADOR'** l_cadenasp

  ​								   | epsilon

* opcional ::=                 **'IF' 'NOT' 'EXISTS'**

  ​                                   | **'OWNER'** opcional1 **'IDENTIFICADOR'** opcional2

  ​								   | epsilon

* opcional1 ::=               **'='**

  ​                                   | epsilon

* opcional2 ::=               **'MODE'** opcional1 **'NOENTERO'**

  ​								   | epsilon

* opcional3 ::=               **'LIKE'** **'CARACTER_O_CADENA'**

  ​								   | epsilon

* expresion ::=               w

* w ::=                            x wp

* wp ::=                          **'='** x wp

  ​								    | epsilon

* x ::=                             y xp

* xp ::=                          **'OR'** y xp

  ​								   | epsilon

* y ::=                            z yp

* yp ::=                          **'AND'** z yp

  ​								   | epsilon

* z ::=                            a zp

* zp ::=                          **'<>'** a zp

  ​     							  | **'>'** a zp

     							    | **'>='** a zp

  ​    							   | **'<'** a zp

  ​    							   | **'<='** a zp

  ​								   | epsilon

* a ::=                            b ap

* ap ::=                         **'+'** b ap

  ​     							 | **'-'** b ap

  ​								  | epsilon

* b ::=                           c bp

* bp ::=                         **'*'** c bp

  ​    							  | **'/'** c bp

  ​								  | epsilon

* c ::=                           d dp

* dp ::=                         **','** d dp

  ​								  | epsilon

* d ::=                           **'('** a **')'**

  ​     							 | **IDENTIFICADOR**

  ​      							| **CADENA**

  ​    							  | **CARACTER_O_CADENA**

  ​      							| **NOENTERO**

  ​      							| **NODECIMAL**

  ​      							| **BOOLEAN**

  ​      							| **'INTERVAL'**

  ​      							| **'NOW'** **'('** **')'**

  ​      							| **'SUM'** **'('**

