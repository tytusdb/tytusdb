# Gramática Ascendente
```xml
<root> ::= <instructionlist>
       
<instructionlist> ::= <instructionlist> <sqlinstruction>
			        | <sqlinstruction>

<sqlinstruction> ::= <DDL>
				   | <DML>
                   | <usestatement>
                   | MULTI_LINE_COMMENT
                   | SINGLE_LINE_COMMENT

<usestatement> ::= USE ID SEMICOLON

<DDL> ::= <createstatement>
        | <showstatement>
        | <alterstatement>
        | <dropstatement>

<createstatement> ::= CREATE <optioncreate> SEMICOLON      

<optioncreate> ::= <TYPE> <SQLNAME> AS ENUM LEFT_PARENTHESIS <typelist> RIGHT_PARENTHESIS
               	 | DATABASE <createdb>
               	 | OR REPLACE DATABASE <createdb>
               	 | TABLE <SQLNAME> LEFT_PARENTHESIS <columnstable> RIGHT_PARENTHESIS
               	 | TABLE <SQLNAME> LEFT_PARENTHESIS <columnstable> RIGHT_PARENTHESIS INHERITS LEFT_PARENTHESIS ID RIGHT_PARENTHESIS

<typelist> ::= <typelist> COMMA <SQLNAME>
             | <SQLNAME> 

<createdb> ::= IF NOT EXISTS ID <listpermits>
             | IF NOT EXISTS ID
             | ID <listpermits>
             | ID    

<listpermits> ::= <listpermits> <permits>
                | <permits>

<permits> ::= OWNER EQUALS SQLNAME
            | OWNER SQLNAME
            | MODE EQUALS INT_NUMBER
            | MODE INT_NUMBER  

<columnstable> ::= <columnstable> COMMA <column>
                 | <column>

<column> ::= ID <typecol> <optionscollist>
           | ID <typecol>
           | UNIQUE LEFT_PARENTHESIS <columnlist> RIGHT_PARENTHESIS
           | PRIMARY KEY LEFT_PARENTHESIS <columnlist> RIGHT_PARENTHESIS
           | FOREIGN KEY LEFT_PARENTHESIS <columnlist> RIGHT_PARENTHESIS REFERENCES ID LEFT_PARENTHESIS <columnlist> RIGHT_PARENTHESIS
           | CONSTRAINT ID CHECK LEFT_PARENTHESIS <conditionColumn> RIGHT_PARENTHESIS
           | CHECK LEFT_PARENTHESIS <conditionColumn> RIGHT_PARENTHESIS

<typecol> ::= SMALLINT
            | INTEGER
            | BIGINT
            | DECIMAL LEFT_PARENTHESIS INT_NUMBER COMMA INT_NUMBER RIGHT_PARENTHESIS
            | DECIMAL LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
            | NUMERIC LEFT_PARENTHESIS INT_NUMBER COMMA INT_NUMBER RIGHT_PARENTHESIS
            | NUMERIC LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
            | REAL
            | DOUBLE PRECISION
            | MONEY
            | CHARACTER VARYING LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
            | CHARACTER VARYING
            | VARCHAR LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
            | VARCHAR
            | CHARACTER LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
            | CHARACTER
            | CHAR LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
            | CHAR
            | TEXT
            | TIMESTAMP LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
            | TIMESTAMP
            | DATE
            | TIME LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
            | TIME
            | INTERVAL <SQLNAME>
            | BOOLEAN               

<optionscollist> ::= <optionscollist> <optioncol>
                   | <optioncol>                     
```
