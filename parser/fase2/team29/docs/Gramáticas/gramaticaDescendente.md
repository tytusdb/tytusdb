# Gramatica Descendente

<hr style="background-color:#0477c9">

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
<hr style="background-color:#0477c9">

## Inicio de la gramatica
    <stmtList> ::= <stmt> <stmtList_>
    <stmtList_>::= <stmt> <stmtList_>
                |/*epsilon*/ 


    <stmt> ::= <selectStmt> ';'
            | <createStmt> ';'
            | <showStmt> ';'
            | <alterStmt> ';'
            | <dropStmt> ';'
            | <insertStmt> ';'
            | <updateStmt> ';'
            | <deleteStmt> ';'


<hr style="background-color:#0477c9">

## Expresiones
        <expresion> ::= <datatype>
                | <expComp>
                | <expBool>

### Expresiones con tipos
    <datatype> ::=  <colName> <datatype_>
                    |<literal> <datatype_>
                    |<funcCall> <datatype_>
                    |'(' <datatype_> 

    <datatype_>::= '+' <datatype> <datatype_>
                |'-' <datatype> <datatype_>
                |'*' <datatype> <datatype_>
                |'/' <datatype> <datatype_>
                |'%' <datatype> <datatype_>
                |'^' <datatype> <datatype_>
                |'||' <datatype> <datatype_>
                |'&' <datatype> <datatype_>
                |'|' <datatype> <datatype_>
                |'#' <datatype> <datatype_>
                |'~' <datatype> <datatype_>
                |'>>' <datatype> <datatype_>
                |'<<' <datatype> <datatype_>
                | <datatype> ')' <datatype_>
                |

### Llamadas a funciones
        <funcCall> ::= funcMath '(' <paramList> ')'
                | funcBool '(' <paramList> ')'
                | funcTrig '(' <paramList> ')'

        <extract> ::= EXTRACT '(' <optsExtract> FROM TIMESTAMP stringLit ')'

        <optsExtract> ::= YEAR
                        | MONTH
                        | DAY
                        | HOUR 
                        | MINUTE
                        | SECOND

        <datePart> ::= DATE_PART '(' stringLit ',' INTERVAL stringLit ')'

### Literales
        <literal> ::= litBool
                | litString
                | litNum
                | litChar

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
                | <datatype> IS DISTINCT FFROM <datatype>
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

        <boolean> ::= <expComp>
                | litBool
                | EXISTS '(' <selectStmt> ')'
                | <datatype> IN '(' <selectStmt> ')'
                | <datatype> NOT IN '(' <selectStmt> ')'
                | <expSubq>

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

        <stringExp> ::= stringLit
                | <colName>

        <subqValues> ::= ALL
                | ANY
                | SOME

### Expresiones booleanas
        <boolean> ::= <expComp>
                | litBool
                | EXISTS '(' <selectStmt> ')'
                | <datatype> IN '(' <selectStmt> ')'
                | <datatype> NOT IN '(' <selectStmt> ')'
                | <expSubq>

        <expBool> ::= NOT <expBool> <expBool_>
                    |<boolean> <expBool_>

        <expBool_> ::=  AND <boolean> <expBool_>
                    |OR <boolean> <expBool_>
                    |

        <booleanCheck> ::= <expComp>
                | litBool

        <expBoolCheck> ::= NOT <expBoolCheck>
                        |<booleanCheck> <expBoolCheck_>

        <expBoolCheck_> ::= AND <booleanCheck> <expBoolCheck_>
                            |OR <booleanCheck> <expBoolCheck_>
                            |


### Llamada a funcion
        <funcCall> ::= funcMath '(' <paramList> ')'
                | funcBool '(' <paramList> ')'
                | funcTrig '(' <paramList> ')'

        <paramList> ::= <datatype> <paramList_>

        <paramList_> ::= ',' <datatype> <paramList_>
                        |

<hr style="background-color:#0477c9">

## DDL

### Create
        <createStmt> ::= CREATE <createBody>

        <createBody> ::= OR REPLACE <createOpts>
                | <createOpts>

        <createOpts> ::= TABLE <ifNotExists> id '(' <createTableList> ')' <inheritsOpt>
                | DATABASE <ifNotExists> id <createOwner> <createMode>
                | TYPE <ifNotExists> id AS ENUM '(' <paramList> ')'

        <inheritsOpt> ::= INHERITS '(' id ')'
                        |

        <ifNotExists> ::= IF NOT EXISTS
                        | 

#### Create Table
        <createTableList> ::= <createTable> <createTableList_>
        <createTableList_> ::= ',' <createTable> <createTableList_>
                            |

        <createTable> ::= id id <createOpts>
                        | <createConstraint>
                        | <createUnique>
                        | <createPrimary>
                        | <createForeign>

        <createOpts> ::= <colOptionsList>
                | 

        <createConstraint> ::= <constrName> CHECK '(' <expBoolCheck> ')'

        <createUnique> ::= UNIQUE '(' <idList> ')'

        <idList>::= id <idList_>
        <idList_>::= ',' id <idList_>
             |/*epsilon*/

        <createPrimary> ::= PRIMARY KEY '(' <idList> ')'

        <createForeign> ::= FOREIGN KEY '(' <idList> ')' REFERENCES id '(' <idList> ')'

        <constrName> ::= CONSTRAINT id 
                |

        <colOptionsList>::= <colOptions> <colOptionsList_>
        <colOptionsList_>::= <colOptions><colOptionsList_>
                        |/*epsilon*/

        <colOptions> ::= <defaultVal>
                | <nullOpt>
                | <constraintOpt>
                | <primaryOpt>
                | <referencesOpt>

        <defaultVal> ::= DEFAULT <datatype>

        <nullOpt> ::= NOT NULL
                | NULL

        <constraintOpt> ::= <constrName> UNIQUE
                        | <constrName> CHECK '(' <expBoolCheck> ')'

        <primaryOpt> ::= PRIMARY KEY

        <referencesOpt> ::= REFERENCES id

#### Create Database
        <createOwner> ::= OWNER id
                        | OWNER '=' id
                        |

        <createMode> ::= MODE number
                | MODE '=' number
                |

### Alter
        <alterStmt> ::= ALTER DATABASE id <alterDb>
                | ALTER TABLE id <alterTable>

#### Alter Database
        <alterDb> ::= RENAME TO id
                | OWNER TO <ownerOPts>

        <ownerOPts> ::= id
                | CURRENT_USER
                | SESSION_USER

#### Alter Table
        <alterTable> ::= ADD <alterConstraint>
                | <alterCol>
                | DROP CONSTRAINT id
                | DROP COLUMN id
                | RENAME COLUMN id TO id

        <alterConstraint> ::= CHECK '(' <expBoolCheck> ')'
                        | CONSTRAINT id UNIQUE '(' id ')'
                        | <createForeign>
                        | COLUMN id id

        <alterCol> ::= ALTER COLUMN id SET NOT NULL
                | ALTER COLUMN id SET NULL

### Drop
        <dropStmt> ::= DROP TABLE id
                | DROP DATABASE <ifExists> id

        <ifExists> ::= IF EXISTS 
                |

<hr style="background-color:#0477c9">

## DML
### Select
        <selectStmt>::= SELECT <selectParams> FROM <tableExp> <joinList> <whereCl> <groupByCl> <orderByCl> <limitCl><selectStmt_>
                    | SELECT DISTINCT <selectParams> FROM <tableExp> <whereCl> <groupByCl> <selectStmt_>
                    | '('<selectStmt_>

        <selectStmt_>::= UNION <allOpt> <selectStmt> <selectList_>
                    | INTERSECT <allOpt> <selectStmt> <selectList_>
                    | EXCEPT <allOpt> <selectStmt> <selectList_>
                    | <selectStmt>')' <selectStmt_>
                    |

        <allOpt> ::= ALL
                |

        <selectParams> ::= '*'
                        | <selectList>

       <selectList> ::= <expresion> <selectList_>

        <selectList_> ::= ',' <selectList_>
                        |/*epsilon*/

        <optAlias> ::= AS id
                | id
                |

#### From
       <tableExp> ::= <fromBody> <tableExp_>

        <tableExp_> ::= ','<fromBody> <tableExp_>
                    |/*epsilon*/

        <colName> ::= id
                | id.id

        <fromBody> ::= <colName>
                | '(' <selectStmt> ')'

#### Joins
        <joinList> ::= <joinCl> <joinList_>

        <joinList_> ::= <joinCl> <joinList_>
                        |

        <joinCl> ::= <joinOpt> JOIN <colName> ON <expBool>
                | <joinOpt> JOIN <colName> USING '(' <nameList> ')'
                | NATURAL <joinOpt> JOIN <colName>
                |

        <nameList> ::= <colName> <nameList_>
        <nameList_> ::= ',' <colName> <nameList_>
                        |

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

        <groupList> ::= <groupElem> <groupList_>
        <groupList_> ::= ',' <colName>
                    |

        <havingCl> ::= HAVING <expBool>
                |

#### Order By
        <orderByCl> ::= ORDER BY <orderList>

        <orderList> ::= <orderByElem> <orderList_>
        <orderList_>:: ',' <orderByElem> <orderList_>
                |/*epsilon*/

        <orderByElem> ::= <colName> <orderOpts> <orderNull>

        <orderOpts> ::= ASC
                | DESC
                |

        <orderNull> ::= NULL FIRST
                | NULL LAST
                |

#### Limit
        <limitCl> ::= LIMIT number <offsetLimit>
                | LIMIT ALL <offsetLimit>
                |

        <offsetLimit> ::= OFFSET number
                        |

### Insert
        <insertStmt> ::= INSERT INTO id VALUES '(' <paramList> ')'

### Update
        <updateStmt> ::= UPDATE id <optAlias> SET <updateCols> '=' <updateVals> <whereCl>

        <updateCols> ::= id
                        | '(' <idList> ')'

        <updateVals> ::= <updateExp>
                        | '(' <updateList> ')'

        <updateList> ::= <updateExp> <updateList_>
        <updateList_>::= ',' <updateExp> <updateList_>
                        |

        <updateExp> ::= <datatype>
                        | DEFAULT

### Delete
        <deleteStmt> ::= DELETE FROM id <optAlias> <whereCl>

<hr style="background-color:#0477c9">

## Otros
### Show
        <showStmt> ::= SHOW DATABASES <likeOpt>

        <likeOpt> ::= LIKE regex
                |

### Use
        <useStmt> ::= USE DATABSE id


## PL/SQL

    <block> ::=  <declaration_stmt> R_BEGIN <block_stmts> <exception> R_END <label> ';'

    <declaration_stmt> ::= <label_stmt> R_DECLARE <global_variable_declaration>
        | 


    <global_variable_declaration> ::= <declaration><global_variable_delcaration_> 
                               
    <global_variable_declaration_> ::=<declaration><global_variable_declaration_> 

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
     <datatype_d> ::=  <colName> <datatype_d_>
                    |<literal> <datatype_d_>
                    |<funcCall> <datatype_d_>
                    |<extract>  <datatype_d_>
                    |<datePart> <datatype_d_>
                    |<current> <datatype_d_>
                    |'(' <datatype_d_> 

    <datatype_d_>::= '+' <datatype_d> <datatype_>
                |'-' <datatype_d> <datatype_d_>
                |'*' <datatype_d> <datatype_d_>
                |'/' <datatype_d> <datatype_d_>
                |'%' <datatype_d> <datatype_d_>
                |'^' <datatype_d> <datatype_d_>
                |'||'<datatype_d> <datatype_d_>
                |  <datatype> ')' <datatype_d_>
                |

        <datatype_d> ::= <literal_d>
                | <funcCall>
                | <extract>
                | <datePart>
                | <current>
                | <parameter>
  
    


        <literal_d> ::=  INTEGER
                | STRING
                | DECIMAL
                | CHARACTER
                | R_TRUE
                | R_FALSE
                | ID
        

### block stmts
        

        <block_stmts> ::= <block_stmt><block_stmts_>
        <block_stmts_>::=<block_stmt><block_stmts_>


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
                        | R_QUERY <execute_return> ';'



### CONDITIONALS IF, CASE
#### IF

        <if_stmt> ::= R_IF <expBool> R_THEN <block_stmts> <elseif_stmts> <else_stmt_opt> R_END R_IF ';'

        <elseif_stmts> ::= <elseif_stmt><elseif_stmts_>
        <elseif_stmts_>::= <elseif_stmt><elseif_stmts_>
                        |

        <elseif_stmt> ::=  R_ELSEIF <expBool> R_THEN <block_stmts>

        <else_stmt_opt> ::= R_ELSE <block_stmts>



#### CASE
        <case_stmt ::= <case_stmt_n>
                | <case_stmt_bool>

        <case_stmt_n> ::= R_CASE ID R_WHEN <list_expression> R_THEN <block_stmts> <else_case_stmt_n> <else_stmt_opt> R_END R_CASE ';'

        <else_case_stmt_n> ::= R_WHEN <list_expression> R_THEN <block_stmts> <else_case_stmt_n_>
        <else_case_stmt_n_> ::= R_WHEN <list_expression> R_THEN <block_stmts> <else_case_stmt_n_>
                        |

        <case_stmt_bool> ::= R_CASE R_WHEN <expBool> R_THEN <block_stmts> <else_case_stmt_bool><else_stmt_opt> R_END R_CASE ';'


        <else_case_stmt_bool> ::=  R_WHEN <expBool> R_THEN <block_stmts> <else_case_stmt_bool_>
        <else_case_stmt_bool_> ::= R_WHEN <expBool> R_THEN <block_stmts> <else_case_stmt_bool_>
                                |

        <list_expression>::= <exp1> <list_expression_>
        <list_expression_>::=',' <exp1><list_expression_>
                        |

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
   


         <selectStmt_SR> ::= R_SELECT <selectParams> R_INTO <strict> ID <fromCl> <joinList> <whereCl>        <groupByCl> <limitCl>
    


       
        <selectStmt_SR> ::= <selectStmt_SR_>
                        |S_PARIZQ <selectStmt_SR_>

        <selectStmt_SR_>::= R_UNION <allOpt> <selectStmt_SR> <selectStmt_SR_>
                        |R_INTERSECT <allOpt> <selectStmt_SR> <selectStmt_SR_>
                        |R_EXCEPT <allOpt> <selectStmt_SR> <selectStmt_SR_>
                        |<selectStmt_SR> S_PARDER <selectStmt_SR_>
                        |

        

        <selectStmt_SR> ::= R_SELECT <selectParams> R_INTO <strict> ID
        

### strict

    <strict> ::= R_STRICT
    |

### returnParams
        <returnParams> ::= '*'


        <returnParams> ::= <returnlist>

        <returnlist> ::= <returnlistParams><optAlias> <returnlist_>
        <returnlist_> ::= ',' <returnlistParams> <optAlias> <returnlist_>
                        |

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

        <list_expression_2> ::= ID <list_expression_2_>
        <list_expression_2_> ::= ',' ID <list_expression_2_>
                        |
        

        <exp_string> ::= <id_or_string> <exp_string_>
        <exp_string_> ::= OC_CONCATENAR <id_or_string> <exp_string_>
                        |

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

        <when_stmt> ::=R_WHEN <expBoolOR> R_THEN <handler_statements> <when_stmt_>
        <when_stmt_> ::= R_WHEN <expBoolOR> R_THEN <handler_statements><when_stmt_>
                        |


        <expBoolOR> ::= ID <expBoolOR_>
        <expBoolOR_> ::= OC_OR ID <expBoolOR_>
                        |

        
        <handler_statements> ::= <handler_statement> <handler_statements_>
        <handler_statements_> ::= <handler_statement> <handler_statements_>
                                |

        <handler_statement> ::= R_RAISE R_NOTICE STRING ';'
                | R_RETURN <return_stmt>  
                | R_NULL ';'
