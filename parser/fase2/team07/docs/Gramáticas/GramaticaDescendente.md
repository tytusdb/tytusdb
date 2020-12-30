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