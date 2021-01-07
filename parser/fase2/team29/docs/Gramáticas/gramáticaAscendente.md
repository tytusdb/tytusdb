# Gramatica Ascendente

<hr style="background-color::=#0477c9">    
    
## Contenido
  - [Inicio de la gramatica](#inicio-de-la-gramatica)
  - [Expresiones](#expresiones)
    - [Expresiones con tipos](#expresiones-con-tipos)
    - [Llamadas a funciones](#llamadas-a-funciones)
    - [Literales](#literales)
    - [Expresiones de comparacion](#expresiones-de-comparacion)
    - [Expresiones de subqueries](#expresiones-de-subqueries)
    - [Expresiones booleanas](#expresiones-booleanas)
    - [Llamada a funcion](#llamada-a-funcion)
  - [DDL](#ddl)
    - [Create](#create)
      - [Create Table](#create-table)
      - [Create Database](#create-database)
      - [Create Index](#create-index)
    - [Alter](#alter)
      - [Alter Database](#alter-database)
      - [Alter Table](#alter-table)
    - [Drop](#drop)
  - [DML](#dml)
    - [Select](#select)
      - [From](#from)
      - [Joins](#joins)
      - [Where](#where)
      - [Group By](#group-by)
      - [Order By](#order-by)
      - [Limit](#limit)
    - [Insert](#insert)
    - [Update](#update)
    - [Delete](#delete)
  - [Otros](#otros)
    - [Show](#show)
    - [Use](#use)
- [PL/SQL](#PL/SQL)
    - [datatype2](#datatype2)
    - [block stmt](#block-stmt)
    - [Control Structures](#Control-Structures)
    - [local variable declaration](#local-variable-declaration)
    - [return](#return)
    - [CONDITIONALS IF, CASE](#CONDITIONALS-IF,-CASE)
        - [IF](#IF)
        - [CASE](#CASE)
    - [EXECUTE QUERY SINGLE ROW](#EXECUTE-QUERY-SINGLE-ROW)
    - [insert](#insert2)
    - [update](#update2)
    - [delete](#delete2)
    - [select](#select2)
    - [strict](#strict)
    - [returnParams](#returnParams)
    - [PERFORM](#PERFORM)
    - [EXECUTE](#EXECUTE)
    - [GET](#GET)
    - [EXCEPTION](#EXCEPTION)


<hr style="background-color::=#0477c9">

## Inicio de la gramatica



    <stmtList> ::= <stmtList> <stmt>
            | <stmt>


    <stmt> ::= <selectStmt> ';'
            | <createStmt> ';'
            | <showStmt> ';'
            | <alterStmt> ';'
            | <dropStmt> ';'
            | <insertStmt> ';'
            | <updateStmt> ';'
            | <deleteStmt> ';'
            | <truncateStmt> ';'
            | <useStmt> ';'
## Expresiones
    idOrString ::= ID
        | STRING
        | CHARACTER

    <expresion> ::= <datatype>
                | <expBool>
                | '(' <selectStmt> ')'
### Expresiones con tipos
    <datatype> ::=  <colName>
                | <literal>
                | <funcCall>
                | <extract>
                | <datePart>
                | <current>
                | <datatype> '+' <datatype>
                | <datatype> '-' <datatype>
                | <datatype> '/' <datatype>
                | <datatype> '*' <datatype> 
                | <datatype> '%' <datatype>
                | <datatype> '^' <datatype>
                | <datatype> '||' <datatype>
                | '(' <datatype> ')'
                |'-' datatype
                |'+' datatype 
### Llamadas a funciones
    <funcCall> ::= ID '(' <paramList> ')'

    <funcCall> ::= ID '(' ')'
                | R_NOW '(' ')'


    <funcCall> ::= R_COUNT '(' <paramsList> ')'
                | R_COUNT '(' O_PRODUCTO ')'
                | R_SUM   '(' <paramsList> ')'
                | R_SUM   '(' O_PRODUCTO ')'
                | R_PROM  '(' <paramsList> ')'
                | R_PROM  '(' O_PRODUCTO ')'

    <paramsList> ::= <paramList> ',' <datatype>
                | <datatype>

    <extract> ::= EXTRACT '(' <optsExtract> FROM <timeStamp> ')'
                | EXTRACT '(' <optsExtract> FROM <colName> ')'

    <timeStamp> ::= TIMESTAMP stringLit
            | INTERVAL stringLit

    <optsExtract> ::= YEAR
                    | MONTH
                    | DAY
                    | HOUR 
                    | MINUTE
                    | SECOND

    <datePart> ::= DATE_PART '(' stringLit ',' <dateSource> ')'

    <dateSource> ::= TIMESTAMP STRING
            | DATE STRING
            | TIME STRING
            | INTERVAL <intervalFields> STRING
            | NOW '(' ')'

    <current> ::= CURRENT_DATE
            | CURRENT_TIME
            | <timeStamp>
### Expresiones de comparacion
    <expComp> ::= <datatype> '<' <datatype>
                | <datatype> '>' <datatype>
                | <datatype> '>=' <datatype>
                | <datatype> '<=' <datatype>
                | <datatype> '=' <datatype>
                | <datatype> '!=' <datatype>
                | <datatype> '<>' <datatype>
                | <datatype> BETWEEN <datatype> AND <datatype>
                | <datatype> NOT BETWEEN <datatype> AND <datatype>
                | <datatype> BETWEEN SYMMETRIC <datatype> AND <datatype>
                | <datatype> IS DISTINCT FROM <datatype>
                | <datatype> IS NOT DISTINCT FROM <datatype>
                | <datatype> IS NULL
                | <datatype> IS NOT NULL
                | <datatype> ISNULL
                | <datatype> NOTNULL
                | <datatype> IS TRUE
                | <datatype> IS NOT TRUE
                | <datatype> IS FALSE
                | <datatype> IS NOT FALSE
                | <datatype> IS UNKNOWN
                | <datatype> IS NOT UNKNOWN
### Expresiones de subqueries
    <expSubq> ::= <datatype> '<'  <subqValues> '(' <selectStmt> ')'
                | <datatype> '>'  <subqValues> '(' <selectStmt> ')'
                | <datatype> '>=' <subqValues> '(' <selectStmt> ')'
                | <datatype> '<=' <subqValues> '(' <selectStmt> ')'
                | <datatype> '='  <subqValues> '(' <selectStmt> ')'
                | <datatype> '!=' <subqValues> '(' <selectStmt> ')'
                | <datatype> '<>' <subqValues> '(' <selectStmt> ')'
                | <datatype> BETWEEN <datatype> AND <datatype> <subqValues> '(' <selectStmt> ')'
                | <datatype> NOT BETWEEN <datatype> AND <datatype> <subqValues> '(' <selectStmt> ')'
                | <datatype> BETWEEN SYMMETRIC <datatype> AND <datatype> <subqValues> '(' <selectStmt> ')'
                | <datatype> IS DISTINCT FFROM <datatype> <subqValues> '(' <selectStmt> ')'
                | <datatype> IS NOT DISTINCT FROM <datatype> <subqValues> '(' <selectStmt> ')'
                | <datatype> IS NULL <subqValues> '(' <selectStmt> ')'
                | <datatype> IS NOT NULL <subqValues> '(' <selectStmt> ')'
                | <datatype> ISNULL <subqValues> '(' <selectStmt> ')'
                | <datatype> NOTNULL <subqValues> '(' <selectStmt> ')'
                | <datatype> IS TRUE <subqValues> '(' <selectStmt> ')'
                | <datatype> IS NOT TRUE <subqValues> '(' <selectStmt> ')'
                | <datatype> IS FALSE <subqValues> '(' <selectStmt> ')'
                | <datatype> IS NOT FALSE <subqValues> '(' <selectStmt> ')'
                | <datatype> IS UNKNOWN <subqValues> '(' <selectStmt> ')'
                | <datatype> IS NOT UNKNOWN <subqValues> '(' <selectStmt> ')'
                | <stringExp> LIKE pattern 

    <stringExp> ::= STRING
            | <colName>

    <subqValues> ::= ALL
                    | ANY
                    | SOME
### Expresiones booleanas
    <boolean> ::= <expComp>
                | EXISTS '(' <selectStmt> ')'
                | <datatype> IN '(' <selectStmt> ')'
                | <datatype> NOT IN '(' <selectStmt> ')'
                | <expSubq>

    <expBool> ::= <expBool> AND <expBool>
                | <expBool> OR <expBool>
                | NOT <expBool>
                |'(' <expBool>')'
                | <boolean>
                | <expBool> <optBoolPredicate>

    <optBoolPredicate> ::= IS TRUE
        | IS FALSE
        | IS UNKNOWN
        | IS NOT TRUE 
        | IS NOT FALSE
        | IS NOT UNKNOWN


    <booleanCheck> ::= <idOrLiteral> '<' <idOrLiteral>
        | <idOrLiteral> '>' <idOrLiteral>
        | <idOrLiteral> '>=' <idOrLiteral>
        | <idOrLiteral> '<=' <idOrLiteral>
        | <idOrLiteral> '=' <idOrLiteral>
        | <idOrLiteral> '!=' <idOrLiteral>
        | <idOrLiteral> IS DISTINCT FROM <idOrLiteral>
        | <idOrLiteral> IS NOT DISTINCT FROM <idOrLiteral>


    <idOrLiteral> ::= ID
        | INTEGER
        | STRING
        | DECIMAL
        | CHARACTER
        | TRUE
        | FALSE

    <expBoolCheck> ::= <expBoolCheck> AND <expBoolCheck>
                | <expBoolCheck> OR <expBoolCheck>
                | NOT <expBoolCheck>
                | <booleanCheck>

    <literal> ::= INTEGER
                | STRING
                | DECIMAL
                | CHARACTER
                | TRUE
                | FALSE
                | NULL

## DDL

### Create
    <createStmt> ::= CREATE <createBody>

    <createBody> ::=  <createOpts>
                

    <createOpts> ::= TABLE <ifNotExists> <idOrString> '(' <createTableList> ')' <inheritsOpt>
                |<orReplace> DATABASE <ifNotExists> <idOrString> <createOwner> <createMode>
                | TYPE <ifNotExists> id AS ENUM '(' <paramList> ')'

    <createOpts> ::= <indexUnique> R_INDEX ID R_ON ID <usingHash> '(' <indexList> ')' whereCl

    <orReplace> ::= R_OR R_REPLACE
                |

    <inheritsOpt> ::= INHERITS '(' id ')'
                    |

    <ifNotExists> ::= IF NOT EXISTS
                    | 

#### Create Table
    <createTableList> ::= <createTableList> ',' <createTable>
                        | <createTable>

    <createTable> ::= id <type> <createColumns>
                    | <createConstraint>
                    | <createUnique>
                    | <createPrimary>
                    | <createForeign>

    <createColumns> ::= colOptionsList
                    |


    <type> ::= id
            | SMALLINIT
            | INTEGER
            | BIGINIT 
            | DECIMAL<optParams>
            | NUMERIC <optParams>
            | REAL
            | DOUBLE PRECISION
            | MONEY
            | CHARACTER VARYING <optParams>
            | VARCHAR <optParams>
            | CHARACTER <optParams>
            | CHAR <optParams>
            | TEXT
            |TIMESTAMP <optParams>
            | DATE
            | TIME <optParams>
            | INTERVAL <intervalFields> 

    <intervalFields> ::= YEAR
                    | MONTH
                    | DAY
                    | HOUR
                    | MINUTE
                    | SECOND
                    |

    <optParams> ::= '(' <literalList> ')'
                |

    <literalList> ::= <literalList> ',' <literal>
                    | <literal>

    <createOpts> ::= <colOptionsList>
                | 

    <createConstraint> ::= <constrName> CHECK '(' <expBoolCheck> ')'

    <createUnique> ::= UNIQUE '(' <idList> ')'

    <idList> ::= <idList> ',' id
            | id

    <createPrimary> ::= PRIMARY KEY '(' <idList> ')'

    <createForeign> ::= FOREIGN KEY '(' <idList> ')' REFERENCES id '(' <idList> ')'

    <constrName> ::= CONSTRAINT id 
                |

    <colOptionsList> ::= <colOptionsList> <colOptions>
                    | <colOptions>

    <colOptions> ::= <defaultVal>
                | <nullOpt>
                | <constraintOpt>
                | <primaryOpt>
                | <referencesOpt>

    <defaultVal> ::= DEFAULT <datatype>

    <nullOpt> ::= NOT NULL
                | NULL

    <constraintOpt> ::= <constrName> UNIQUE
                    | <constrName> CHECK '(' <booleanCheck> ')'

    <primaryOpt> ::= PRIMARY KEY

    <referencesOpt> ::= REFERENCES id

#### Create Database
    <createOwner> ::= OWNER id
                    | OWNER '=' id
                    |OWNER string
                    |OWNER '=' string 
                    |

    <createMode> ::= MODE number
                | MODE '=' number
                |

### Create Index

    <indexList> ::= <indexList> ',' ID <indexOrder> <indexNull> <firstLast>
                |ID <indexOrder> <indexNull> <firstLast>

    <usingHash> ::= R_USING R_HASH  

    <indexOrder> ::= R_DESC
        | R_ASC
        |

    <indexNull> ::= R_NULL
    |

    <firstLast> ::= R_FIRST
        | R_LAST
        |

    <indexUnique> ::= R_UNIQUE
    |
### Alter
    <alterStmt> ::= ALTER DATABASE <idOrString> 
#### Alter Database
    <alterDb>
                | ALTER TABLE <idOrString> <alterTableList>

    <alterDb> ::= RENAME TO <idOrString>
                | OWNER TO <ownerOPts>

    <ownerOPts> ::= <idOrString>
                | CURRENT_USER
                | SESSION_USER
#### Alter Table
    <alterTableList> ::= <alterTableList> ',' <alterTable>
                    | <alterTable>

    <alterTable> ::= ADD <alterConstraint>
                | <alterCol>
                | DROP CONSTRAINT id
                | DROP COLUMN id
                | RENAME COLUMN id TO id

    <alterConstraint> ::= CHECK '(' <booleanCheck> ')'
                        | CONSTRAINT id UNIQUE '(' id ')'
                        | <createForeign>
                        | COLUMN id <type>

    <alterCol> ::= ALTER COLUMN id SET NOT NULL
                | ALTER COLUMN id SET NULL
                | ALTER COLUMN id TYPE <type>
### Drop
    <dropStmt> ::= DROP TABLE <ifExists> <idOrString>
                | DROP DATABASE <ifExists> <idOrString>

    <ifExists> ::= IF EXISTS 
                |

<hr style="background-color::=#0477c9">

## DML
### Select
    <selectStmt> ::= SELECT <selectParams> <fromCl> <whereCl> 
                | SELECT DISTINCT <selectParams> FROM <tableExp> <whereCl> <groupByCl> <limitCl>
                | <selectStmt> UNION <allOpt> <selectStmt>
                | <selectStmt> INTERSECT <allOpt> <selectStmt>
                | <selectStmt> EXCEPT <allOpt> <selectStmt>
                | '(' <selectStmt> ')'
                |SELECT <selectParams>

    <fromCl> ::= R_FROM tableExp

    <allOpt> ::= ALL
                |

    <selectParams> ::= '*'
                    | <selectList>

    <selectList> ::= <selectList> ',' <expresion> <optAlias>
                | <selectListParams> <optAlias>
            
    <selectListParams> ::= <expresion>
                    |ID '.' '*'

    <optAlias> ::= AS <idOrString>
                | <idOrString>
                |
#### From
    <tableExp> ::= <tableExp> ',' <fromBody> 
                | <fromBody> 

    <colName> ::= id
                | id.id

    <fromBody> ::= ID <optAlias>
                | '(' <selectStmt> ')' AS <idOrString>
#### Joins
    <joinList> ::= <joinList2>
            |

    <joinList2> ::= <joinList2> <joinCl>
                | <joinCl>

    <joinCl> ::= <joinOpt> JOIN <colName> ON <expBool>
            | <joinOpt> JOIN <colName> USING '(' <nameList> ')'
            | NATURAL <joinOpt> JOIN <colName>
            |

    <nameList> ::= <nameList> ',' <colName>
                | <colName>

    <joinOpt> ::= INNER
                | LEFT 
                | LEFT OUTER
                | RIGHT
                | RIGHT OUTER
                | FULL
                | FULL OUTER
#### Where
    <whereCl> ::= WHERE <expBool>
                | /*epsilon*/

#### Group By

    <groupByCl> ::= GROUP BY <groupList> <havingCl>
                | 

    <groupList> ::=  <groupList> ',' <colName>
                | <colName>

    <havingCl> ::= HAVING <expBool>
                |
#### Order By
    <orderByCl> ::= ORDER BY <orderList>

    <orderList> ::= <orderList> ',' <orderByElem>
                | <orderByElem>

    <orderByElem> ::= <colName> <orderOpts> <orderNull>

    <orderOpts> ::= ASC
                | DESC
                |

    <orderNull> ::= NULL FIRST
                | NULL LAST
                |
#### Limit
    <limitCl> ::= LIMIT INTEGER <offsetLimit>
                | LIMIT ALL <offsetLimit>
                |

    <offsetLimit> ::= OFFSET INTEGER
                    |
### Insert
    <insertStmt> ::= INSERT INTO ID <paramsColumn> VALUES '(' <paramList> ')'

    <paramsColumn< ::= '(' <idList> ')'
                    |
### Update
    <updateStmt> ::= UPDATE <fromBody> SET <updateCols> <whereCl>

    <updateCols> ::=  <updateCols> ',' <updateVals>
                    | <updateVals>

    <updateVals> ::= ID '=' <updateExp>
        

    <updateExp> ::= <datatype>
                    | DEFAULT
### Delete
    <deleteStmt> ::= DELETE <fromCl> <whereCl>

    <truncateStmt> ::= TRUNCATE <tableOpt> ID

    <tableOpt> ::= TABLE
            | 

<hr style="background-color::=#0477c9">

## Otros
### Show
    <showStmt> ::= SHOW DATABASES <likeOpt>

    <likeOpt> ::= LIKE STRING
                |
### Use
    <useStmt> ::= USE DATABSE ID








## PL/SQL
    <block> ::=  <declaration_stmt> R_BEGIN <block_stmts> <exception> R_END <label> ';'

    <declaration_stmt> ::= <label_stmt> R_DECLARE <global_variable_declaration>
        | 


    <global_variable_declaration> ::= <declaration> 
                                | <global_variable_declaration> <declaration>

    <declaration> ::= ID <constant> <types_d><assignment> ';'
        | ID R_ALIAS R_FOR S_DOLAR INTEGER ';'
        | ID R_RECORD ';
        | ID R_ALIAS R_FOR ID ';'
            
    <constant> ::= R_CONSTANT
        |

    <assignment> ::= <assignment_operator_D> <datatype_d>
        |

    <assignment_operator_D> ::= R_DEFAULT
        | O_ASIGNACION
        | OL_ESIGUAL

    <label_stmt> ::= OC_SHIFTL ID OC_SHIFTR
                |

    <label> ::= ID

    <types_d> ::=  ID

    <types_d> ::= T_SMALLINT
        | T_INTEGER
        | T_BIGINT
        | T_REAL
        | T_DOUBLE T_PRECISION
        | T_MONEY
        | T_TEXT
        | T_BOOLEAN
        | R_TIMESTAMP
        | T_DATE
        | T_TIME

    <types_d> ::= T_DECIMAL <optParams>
        | T_NUMERIC <optParams>
        | T_VARCHAR <optParams>
        | T_CHARACTER <optParams>
        | T_CHAR <optParams>

    <types_d> ::= T_CHARACTER T_VARYING <optParams>

    <types_d> ::= R_INTERVAL <intervalFields>

    <types_d> ::=  ID '%' R_TYPE

    <types_d> ::=  ID '.' ID '%' R_TYPE

    <types_d> ::=  ID '%' R_ROWTYPE



### datatype2
 

    <datatype_d> ::= <datatype_d> '+' <datatype_d>
    | <datatype_d> '-' <datatype_d>
    | <datatype_d> '*' <datatype_d>
    | <datatype_d> '/' <datatype_d>
    | <datatype_d> '^' <datatype_d>
    | <datatype_d> '%' <datatype_d>

  
    <datatype_d> ::= <datatype_d> OC_CONCATENAR <datatype>
    


    <datatype_d> ::= '-' <datatype_d> '-'
    | <datatype_d> '+'



    <datatype_d> ::= <literal_d>
    | <funcCall>
    | <extract>
    | <datePart>
    | <current>
    | <parameter>
  


    <datatype_d> ::= '(' <datatype_d> ')'
    


    <literal_d> ::=  INTEGER
    | STRING
    | DECIMAL
    | CHARACTER
    | R_TRUE
    | R_FALSE
    | ID
    

### block stmts

    <block_stmts> ::= <block_stmts> <block_stmt> """

    
    <block_stmt> ::= <local_variable_declaration>
                | <statement>
                | <stmt>

### Control Structures

    <statement> ::= <if_stmt>
        | <loop_stmt>
        | <while_stmt>
        | <for_stmt_int>
        | <for_stmt_query>
        | <case_stmt>
        | <stmt_without_substmt>

    <stmt_without_substmt> ::= R_NULL ';'
        | R_RETURN <return_stmt>
        | R_EXIT <exit_stmt>
        | R_CONTINUE <continue_stmt>
        | <query_single_row>
        



### local variable declaration

    <local_variable_declaration> ::= ID <assignment_operator> <datatype> ';'

    <assignment_operator> ::= O_ASIGNACION
        | '='

### return

    <return_stmt> ::= <expresion> ';'
                | R_NEXT <expresion> ';'
                | R_QUERY  <selectStmt> ';'
                | ';'
                | R_QUERY <execute_return> ';'"""



### CONDITIONALS IF, CASE
#### IF

    <if_stmt> ::= R_IF <expBool> R_THEN <block_stmts> <elseif_stmts> <else_stmt_opt> R_END R_IF ';'

    <elseif_stmts> ::= <elseif_stmts> <elseif_stmt>

    <elseif_stmt> ::=  R_ELSEIF <expBool> R_THEN <block_stmts>

    <else_stmt_opt> ::= R_ELSE <block_stmts>



#### CASE
    <case_stmt ::= <case_stmt_n>
        | <case_stmt_bool>

    <case_stmt_n> ::= R_CASE ID R_WHEN <list_expression> R_THEN <block_stmts> <else_case_stmt_n> <else_stmt_opt> R_END R_CASE ';'

    <else_case_stmt_n> ::= <else_case_stmt_n> R_WHEN <list_expression> R_THEN <block_stmts> 
    | R_WHEN <list_expression> R_THEN <block_stmts>  
    |

    <case_stmt_bool> ::= R_CASE R_WHEN <expBool> R_THEN <block_stmts> <else_case_stmt_bool><else_stmt_opt> R_END R_CASE ';'

    <else_case_stmt_bool> ::= <else_case_stmt_bool>  R_WHEN <expBool> R_THEN <block_stmts>  
                |  R_WHEN <expBool> R_THEN <block_stmts> 
                |

    <list_expression> ::= <exp1>
        | <list_expression> ',' <exp1>

    <exp1> ::= INTEGER
    | STRING
    | DECIMAL
    | CHARACTER
    | R_TRUE
    | R_FALSE



### EXECUTE QUERY SINGLE ROW

    <query_single_row> ::= <insertStmt_SR> ';'
        | <updateStmt_SR> ';'
        | <deleteStmt_SR> ';'
        | <selectStmt_SR> ';'
        | <perform> ';'
        | <execute> ';'
        | <get> ';'

### insert2

    <insertStmt_SR> ::= R_INSERT R_INTO ID <paramsColumn> R_VALUES '(' <paramsList> ')' R_RETURNING <returnParams>  R_INTO <strict> ID 


### update2

    <updateStmt_SR> ::= R_UPDATE <fromBody> R_SET <updateCols> <whereCl> R_RETURNING <returnParams> R_INTO <strict> ID 

   

### delete2

    <deleteStmt_SR> ::= R_DELETE <fromCl> <whereCl> R_RETURNING <returnParams> R_INTO <strict> ID 

### select2
    <selectStmt_SR> ::= R_SELECT R_DISTINCT <selectParams> R_INTO <strict> ID <fromCl> <whereCl> <groupByCl> <limitCl>



    <selectStmt_SR> ::= R_SELECT <selectParams> R_INTO <strict> ID <fromCl> <whereCl> <groupByCl> <limitCl>


    <selectStmt_SR> ::= R_SELECT <selectParams> R_INTO <strict> ID <fromCl> <joinList> <whereCl> <groupByCl> <orderByCl> <limitCl>
   


    <selectStmt_SR> ::= R_SELECT <selectParams> R_INTO <strict> ID <fromCl> <whereCl> <groupByCl> <orderByCl> <limitCl>
   


    <selectStmt_SR> ::= R_SELECT <selectParams> R_INTO <strict> ID <fromCl> <joinList> <whereCl> <groupByCl> <limitCl>
    


    <selectStmt_SR> ::= <selectStmt_SR> R_UNION <allOpt> <selectStmt_SR>
    


    <selectStmt_SR> ::= <selectStmt_SR> R_INTERSECT <allOpt> <selectStmt_SR>
    


    <selectStmt_SR> ::= <selectStmt_SR> R_EXCEPT <allOpt> <selectStmt_SR>
    


    <selectStmt_SR> ::= S_PARIZQ <selectStmt_SR> S_PARDER
    

    <selectStmt_SR> ::= R_SELECT <selectParams> R_INTO <strict> ID
   

### strict

    <strict> ::= R_STRICT
    |

### returnParams
    <returnParams> ::= '*'


    <returnParams> ::= <returnlist>


    <returnlist> ::= <returnlist> ',' <returnlistParams> <optAlias>


    <returnlist> ::= <returnlistParams><optAlias>


    <returnlistParams> ::= <expresion>
   

    <returnlistParams> ::= ID '*' '.'
    



### PERFORM

    <perform> ::= R_PERFORM STRING 

### EXECUTE

    <execute_return> ::= R_EXECUTE <exp_string>  <using>

    <execute> ::= R_EXECUTE <exp_string> <into_strict> <using> 

    <into_strict> ::= R_INTO <strict> ID
    |

    <using> ::= R_USING <list_expression_2>
    |

    <list_expression_2> ::= ID
                        | <list_expression_2> ',' ID

    <exp_string> ::= <id_or_string> 
                | <exp_string> OC_CONCATENAR <id_or_string>

    <id_or_string> ::= STRING
    | ID 
    | <funcCall>

### GET 

    <get> ::= R_GET <current> R_DIAGNOSTIC ID <assignment_operator> <item>

    <current> ::= R_CURRENT
    |

    <item> ::= R_ROW_COUNT

### EXCEPTION

    <exception> ::= R_EXCEPTION <when_stmt> R_END ';'

    <when_stmt> ::= R_WHEN <expBoolOR> R_THEN <handler_statements>
    | <when_stmt> R_WHEN <expBoolOR> R_THEN <handler_statements>

    <expBoolOR> ::= ID
                | <expBoolOR> OC_OR ID 

    <handler_statements> ::= <handler_statements> <handler_statement>
                        |
    

    <handler_statement> ::= R_RAISE R_NOTICE STRING ';'
        | R_RETURN <return_stmt>  
        | R_NULL ';'
