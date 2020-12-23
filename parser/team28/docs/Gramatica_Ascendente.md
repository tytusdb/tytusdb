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

<optioncol> ::= DEFAULT <SQLSIMPLEEXPRESSION>                
              | NOT NULL
              | NULL
              | CONSTRAINT ID UNIQUE
              | UNIQUE
              | CONSTRAINT ID CHECK LEFT_PARENTHESIS <conditionColumn> RIGHT_PARENTHESIS
              | CHECK LEFT_PARENTHESIS <conditionColumn> RIGHT_PARENTHESIS
              | PRIMARY KEY
              | REFERENCES ID

<conditionColumn> ::= <conditioncheck>

<conditioncheck> ::= <SQLRELATIONALEXPRESSION>

<showstatement> ::= SHOW DATABASES SEMICOLON
                  | SHOW DATABASES LIKE <SQLNAME> SEMICOLON

<alterstatement> ::= ALTER <optionsalter> SEMICOLON

<optionsalter> ::= DATABASE <alterdatabase>
				 | TABLE <altertable>

<alterdatabase> ::= ID RENAME TO ID
				  | ID OWNER TO <typeowner>

<typeowner> ::= ID
              | CURRENT_USER
              | SESSION_USER

<altertable> ::= ID <alterlist>

<alterlist> ::= <alterlist> COMMA <typealter>
			  | <typealter>

<typealter> ::= ADD <addalter>
              | ALTER <alteralter>
              | DROP <dropalter>
              | RENAME  <renamealter>

<addalter> ::= COLUMN ID <typecol>
              | CHECK LEFT_PARENTHESIS <conditionColumn> RIGHT_PARENTHESIS
              | CONSTRAINT ID UNIQUE LEFT_PARENTHESIS ID RIGHT_PARENTHESIS
              | FOREIGN KEY LEFT_PARENTHESIS ID RIGHT_PARENTHESIS REFERENCES ID

<alteralter> ::= COLUMN ID SET NOT NULL
               | COLUMN ID TYPE <typecol>

<dropalter> ::= COLUMN ID
              | CONSTRAINT ID

<renamealter> ::= COLUMN ID TO ID

<dropstatement> ::= DROP <optionsdrop> SEMICOLON

<optionsdrop> ::= DATABASE <dropdatabase>
                | TABLE <droptable>

<dropdatabase> ::= IF EXISTS ID
                 | ID

<droptable> ::= ID

<DML> ::= <QUERYSTATEMENT>
        | <INSERTSTATEMENT>
        | <DELETESTATEMENT>
        | <UPDATESTATEMENT>

<UPDATESTATEMENT> ::= UPDATE ID <OPTIONS1> SET <SETLIST> <OPTIONSLIST2> SEMICOLON
                       | UPDATE ID SET <SETLIST> <OPTIONSLIST2> SEMICOLON
                       | UPDATE ID SET <SETLIST>  SEMICOLON 

<SETLIST> ::= <SETLIST> COMMA <COLUMNVALUES>
            | <COLUMNVALUES>

<COLUMNVALUES> ::= <OBJECTREFERENCE> EQUALS <SQLEXPRESSION2>

<SQLEXPRESSION2> ::= <SQLEXPRESSION2> PLUS <SQLEXPRESSION2> 
                   | <SQLEXPRESSION2> REST <SQLEXPRESSION2> 
                   | <SQLEXPRESSION2> DIVISION <SQLEXPRESSION2> 
                   | <SQLEXPRESSION2> ASTERISK <SQLEXPRESSION2> 
                   | <SQLEXPRESSION2> MODULAR <SQLEXPRESSION2>
                   | <SQLEXPRESSION2> EXPONENT <SQLEXPRESSION2> 
                   | REST <SQLEXPRESSION2> %prec UREST
                   | PLUS <SQLEXPRESSION2> %prec UPLUS
                   | LEFT_PARENTHESIS <SQLEXPRESSION2> RIGHT_PARENTHESIS
                   | ACOSD LEFT_PARENTHESIS <SQLEXPRESSION2> RIGHT_PARENTHESIS
                   | ASIND LEFT_PARENTHESIS <SQLEXPRESSION2> RIGHT_PARENTHESIS
                   | SUBSTRING LEFT_PARENTHESIS ID COMMA <SQLINTEGER> COMMA <SQLINTEGER> RIGHT_PARENTHESIS
                   | <SQLNAME>
                   | <SQLINTEGER>

<OPTIONSLIST2> ::= <WHERECLAUSE> <OPTIONS4>
                 | <WHERECLAUSE>
                 | <OPTIONS4>

<DELETESTATEMENT> ::= DELETE FROM ID <OPTIONSLIST> SEMICOLON
                    | DELETE FROM ID SEMICOLON

<OPTIONSLIST> ::= <OPTIONS1> <OPTIONS2> <WHERECLAUSE> <OPTIONS4>
                | <OPTIONS1> <OPTIONS2> <WHERECLAUSE>
                | <OPTIONS1> <WHERECLAUSE> <OPTIONS4>
                | <OPTIONS1> <OPTIONS2> <OPTIONS4>
                | <OPTIONS2> <WHERECLAUSE> <OPTIONS4>
                | <OPTIONS1> <OPTIONS2>
                | <OPTIONS1> <WHERECLAUSE>
                | <OPTIONS1> <OPTIONS4>
                | <OPTIONS2> <WHERECLAUSE>
                | <OPTIONS2> <OPTIONS4>
                | <WHERECLAUSE> <OPTIONS4>
                | <OPTIONS1>
                | <OPTIONS2>
                | <WHERECLAUSE>
                | <OPTIONS4>

<OPTIONS1> ::= ASTERISK <SQLALIAS>
             | ASTERISK
             | <SQLALIAS>

<OPTIONS2> ::= USING <USINGLIST>

<USINGLIST> ::= <USINGLIST> COMMA <SQLNAME>
              | <SQLNAME>

<OPTIONS4> : RETURNING <RETURNINGLIST>  

<EXPRESSIONRETURNING> ::= <EXPRESSIONRETURNING> COMMA <SQLEXPRESSION> <SQLALIAS>
                        | <SQLEXPRESSION> <SQLALIAS>

<INSERTSTATEMENT> ::= INSERT INTO <SQLNAME> LEFT_PARENTHESIS <LISTPARAMSINSERT> RIGHT_PARENTHESIS VALUES LEFT_PARENTHESIS <LISTVALUESINSERT> RIGHT_PARENTHESIS SEMICOLON
                    | INSERT INTO <SQLNAME> VALUES LEFT_PARENTHESIS <LISTVALUESINSERT> RIGHT_PARENTHESIS SEMICOLON

<LISTPARAMSINSERT> ::= <LISTPARAMSINSERT> COMMA <SQLNAME>
                     | <SQLNAME> 

<QUERYSTATEMENT> ::= <SELECTSTATEMENT> SEMICOLON

<SELECTSTATEMENT> ::= <SELECTWITHOUTORDER> <ORDERBYCLAUSE> <LIMITCLAUSE>
                    | <SELECTWITHOUTORDER> <ORDERBYCLAUSE> 
                    | <SELECTWITHOUTORDER> <LIMITCLAUSE> 
                    | <SELECTWITHOUTORDER>

<SELECTWITHOUTORDER> ::= <SELECTSET>
                       | <SELECTWITHOUTORDER> <TYPECOMBINEQUERY> ALL <SELECTSET>
                       | <SELECTWITHOUTORDER> <TYPECOMBINEQUERY> <SELECTSET>

<SELECTSET> ::= <SELECTQ> 
              | LEFT_PARENTHESIS <SUBQUERY> RIGHT_PARENTHESIS

<SELECTQ> ::= SELECT <SELECTLIST> <FROMCLAUSE>
            | SELECT <SELECTLIST> <FROMCLAUSE> <SELECTWHEREAGGREGATE>
            | SELECT <TYPESELECT> <SELECTLIST> <FROMCLAUSE>
            | SELECT <TYPESELECT> <SELECTLIST> <FROMCLAUSE> <SELECTWHEREAGGREGATE>
            | SELECT <SELECTLIST>

<SELECTLIST> ::= ASTERISK
               | <LISTITEM>

<LISTITEM> ::= <LISTITEM> COMMA <SELECTITEM>
             | <SELECTITEM>

<SELECTITEM> ::= <SQLEXPRESSION> <SQLALIAS>
               | <SQLEXPRESSION>
               | LEFT_PARENTHESIS <SUBQUERY> RIGHT_PARENTHESIS

<FROMCLAUSE> ::= FROM <FROMCLAUSELIST>

<FROMCLAUSELIST> ::= <FROMCLAUSELIST> COMMA <TABLEREFERENCE>
                   | <FROMCLAUSELIST> LEFT_PARENTHESIS <SUBQUERY> RIGHT_PARENTHESIS <SQLALIAS>
                   | <FROMCLAUSELIST> LEFT_PARENTHESIS <SUBQUERY> RIGHT_PARENTHESIS
                   | LEFT_PARENTHESIS <SUBQUERY> RIGHT_PARENTHESIS
                   | LEFT_PARENTHESIS <SUBQUERY> RIGHT_PARENTHESIS <SQLALIAS>
                   | <TABLEREFERENCE>

<SELECTWHEREAGGREGATE> ::= <WHERECLAUSE> <SELECTGROUPHAVING>
                         | <SELECTGROUPHAVING>
                         | <WHERECLAUSE>

<SELECTGROUPHAVING> ::= <GROUPBYCLAUSE>
                      | <HAVINGCLAUSE> <GROUPBYCLAUSE>
                      | <GROUPBYCLAUSE> <HAVINGCLAUSE>

<TABLEREFERENCE> ::= <SQLNAME> <SQLALIAS>
                   | <SQLNAME> <SQLALIAS> <JOINLIST>
                   | <SQLNAME> <JOINLIST>
                   | <SQLNAME>

<ORDERBYCLAUSE> ::= ORDER BY <ORDERBYEXPRESSION>

<ORDERBYEXPRESSION> ::= <LISTPARAMSINSERT> ASC
                      | <LISTPARAMSINSERT> DESC
                      | <LISTPARAMSINSERT>

<LIMITCLAUSE> ::= LIMIT <LIMITTYPES> OFFSET INT_NUMBER
                | LIMIT <LIMITTYPES>

<LIMITTYPES> ::= INT_NUMBER
               | ALL

<WHERECLAUSE> ::= WHERE <SQLEXPRESSION>

<GROUPBYCLAUSE> ::= GROUP BY <SQLEXPRESSIONLIST>

<HAVINGCLAUSE> ::= HAVING <SQLEXPRESSION>

<JOINLIST> ::= <JOINLIST> <JOINP>
             | <JOINP>

<JOINP> ::= <JOINTYPE> JOIN <TABLEREFERENCE> ON <SQLEXPRESSION>

<JOINTYPE> ::= INNER
             | LEFT OUTER
             | RIGHT OUTER
             | FULL OUTER

<SQLEXPRESSION> ::= <SQLEXPRESSION> OR <SQLEXPRESSION>
                  | <SQLEXPRESSION> AND <SQLEXPRESSION>
                  | NOT <EXISTSORSQLRELATIONALCLAUSE>
                  | <EXISTSORSQLRELATIONALCLAUSE>
```
