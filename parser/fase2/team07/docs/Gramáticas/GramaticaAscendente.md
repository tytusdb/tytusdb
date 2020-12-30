# Gramatica Ascendente

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

<hr style="background-color:#0477c9">
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
    idOrString : ID
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

    <createColumns> : colOptionsList
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

<hr style="background-color:#0477c9">

## DML
### Select
    <selectStmt> ::= SELECT <selectParams> <fromCl> <whereCl> 
                | SELECT DISTINCT <selectParams> FROM <tableExp> <whereCl> <groupByCl> <limitCl>
                | <selectStmt> UNION <allOpt> <selectStmt>
                | <selectStmt> INTERSECT <allOpt> <selectStmt>
                | <selectStmt> EXCEPT <allOpt> <selectStmt>
                | '(' <selectStmt> ')'
                |SELECT <selectParams>

    <fromCl> : R_FROM tableExp

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

<hr style="background-color:#0477c9">

## Otros
### Show
    <showStmt> ::= SHOW DATABASES <likeOpt>

    <likeOpt> ::= LIKE STRING
                |
### Use
    <useStmt> ::= USE DATABSE ID