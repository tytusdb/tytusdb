# Gramaticas Parser TytusDB
Las gramaticas utilizadas para la elaboración del SQL parser en el presente proyecto se presentan a continuación:
## Gramática Descendente
La gramática descendente creada para el presente proyecto es la siguiente:
```
//Like Regex,,ALTERTABLE,DROPTABLE
//Preguntas:  \n concatena luego del select

<init>  ::=  <start>

<start> ::= 
            <listadesentencias>
        | ε

<listadesentencias> ::= 
                        <sentencias> <listadesentencias>
                    | <sentencias>

<sentencias> ::= 
                <create> 
            |  <show>
            |  <alter>
            |  <drop>
            |  <delete>
            |  <insert>
            |  <update>
            |  <select>

<create> ::= 
                CREATE <createopciones> 


<createopciones>  ::= OR REPLACE DATABASE <creaciondb>
                 | DATABASE <creaciondb>
                 | TABLE   <creaciontable>


<creaciondb> ::= 
                IF NOT EXISTS ID <owner> <mode>
            | ID <owner> <mode>


<owner> ::=  
            OWNER <igualopcional> ID
        | ε


<mode> ::=  
            MODE <igualopcional> NUMERO
        | ε                             


<igualopcional> ::= 
                    =
                | ε


<show> ::= SHOW DATABASE <opcionlike>


<opcionlike>::= 
                LIKE CADENA                                                   
            | ε


<alter> ::= ALTER <altertipo>


<altertipo> ::= 
                DATABASE ID <alterdb>
             | TABLE  <altertable>


<alterdb> ::= 
            RENAME TO ID
          | OWNER TO <tipodeowner>


<tipodeowner> ::=
                 ID
              | CURRENT_USER
              | SESSION_USER


<drop>::= 
        DROP <droptipo>


<droptipo> ::= 
            DATABASE <dropdb>
           | TABLE   <droptable>


<dropdb>::= 
             IF EXISTS ID
            | ID

<creaciontable> ::= 
                    ID (  <tuplas> <tcheck> <tunique> ) <inheritsopcional> ;


<inheritsopcional> ::= 
                    INHERIT ( ID )
                   | ε


<tuplas> ::= 
            <tupla> <tuplasp>


<tuplasp> ::= 
                 , <tupla> <tuplasp>
                | ε


<tupla> ::= 
            ID <tipo> <ordentuplas>


<ordentuplas> ::= 
                    <ordentuplasp> <ordentuplas>


<ordentuplasp> ::= 
                    <ordentuplas> <ordentuplasp> 
                    | ε


<tcheck>::= 
            , <tcheckprima>
            | ε

<TCONSTRAINTCHECK> ::= 
                        CONSTRAINT ID CHECK ( ID <verificaciones> ID )
                        | CHECK ( ID <verificaciones> ID )


<tunique>::= 
            , UNIQUE ( <listaids> )
            | ε


<listaids> ::= 
                ID <listaidsp>


<listaidsp> ::=     
                , ID <listaidsp>
                | ε

<ordentupla> ::=
                 <tpf>
                | <tdefault>
                | <tnull>
                | <tconstraintunique>
                | <tconstraintcheck>
                | ε


<tpf> ::=
         PRIMARY KEY
        | REFERENCES ID


<tconstraintunique> ::= 
                        CONSTRAINT ID UNIQUE
                        | UNIQUE


<tconstraintcheck>::= 
                        CONSTRAINT ID CHECK (  ID <verificaciones> <valor> )
                        | CHECK ( ID <verificaciones> <valor> )


<valor> ::= 
            NUMERO
            | BOLEANO
            | CADENA
            | FECHA


<verificaciones>::=
                    <
                    | >
                    | =
                    | >=
                    | <=
                    | <>
                    | !=


<tnull> ::= 
            NOT NULL
            | NULL


<tdefault>::= 
            DEFAULT <tipodefault>


<tipodefault>::=
                 ID
             | NUMERO
             | <boleano>
             | CADENA


<boleano>::= 
            TRUE
            | FALSE


<tipo> ::= 
            SMALLINT
            | INTEGER
            | BIGINT
            | DECIMAL
            | NUMERIC
            | REAL
            | DOUBLE <precision>
            | MONEY
            | CHARACTER VARYING ( NUMERO )
            | VARCHAR ( NUMERO )
            | CHARACTER ( NUMERO )
            | CHAR ( NUMERO )
            | TEXT
            | TIMESTAMP <precision>
            | TIMESTAMP <precision>
            | DATE
            | TIME <precision>
            | TIME <precision>
            | INTERVAL <fields> <precision>

<precision> ::= 
                ( NUMERO )
                | ε

<fields> ::= 
        YEAR <to>
        | MONTH <to>
        | DAY <to>
        | HOUR <to>
        | MINUTE <to>
        | SECOND
        | ε

<to> ::=  
        TO <fieldspr> 
        | ε

<fieldspr> ::=
            MONTH
            | HOUR
            | MINUTE
            | SECOND

<alter> ::= 
            ALTER TABLE ID <opcionalter>


<opcionalter> ::= 
                ADD <opcionadd>
              | <opconalter>
              | <opcion> <drop>
              | <opcionrename>


<opcionadd> ::= 
                CHEK ( ID <> ALGO )
            | CONSTRAINT ID UNIQUE ( ID )
            | FOREIGN KEY ( ID ) REFERENCES ID


<opconalter> ::= 
                ALTER COLUMN ID SET NOT NULL


<opciondrop> ::=
                 DROP CONSTRAINT


<delete> ::= 
            DELETE FROM <onlyopcional> ID <allopcional> <aliasopcional> <usingopcional> <whereopcional> <returnopcional>


<onlyopcional> ::= 
                ONLY
                | ε


<allopcional> ::= 
                *
              | ε


<aliasopcional> ::=
                 AS ID
                | ID
                | ε


<usingopcional> ::= USING ID <usingopcional>



<usingopcional> ::= 
                    , USING ID <usingopcional>
                 | ε


<whereopcional> ::= 
                WHERE <condition>
                | WHERE CURRENT OF ID
                | ε


<returnopcional> ::= 
                    RETURNING *
                 | RETURNING id <aliasopcional> <returnopcional>
                 | ε


<returnopcional> ::= 
                    , ID <returnopcional>
                  | ε


<insert> ::=
             INSERT INTO ID VALUES ( <valoresinsert> )


<valoresinsert> ::= 
                    <valor> <valoresinsert>


<valoresinsert> ::= 
                    , <valor> <valoresinsert>
                 |  ε


<update> ::= 
                UPDATE ID SET ID = <valor> <whereopcional>


<select> ::= 
                SELECT <selectstructure> <combination>

<selectstructure> ::=
                     * <from>
                   |<distinct> <columnnames> <from> 
                   | row <columnnames> <from>
                   
<from> ::= 
            FROM <tablesname> <where> <orderby> <limit> ;
        |FROM <subquerie>

<subquerie> ::= 
                tk_parentesis_izq SELECT tk_parentesis_der AS

<distinct> ::= 
            rsv_distinct 
        | epsilon

<columnnames> ::= 
                 <sanemes>  <as> <columnnames>
                | <srepeatednames> <as> <columnnames>
                | <funcitons> ( <names> )

<as> ::= 
           AS ID
        | ε

<snames> ::= 
            ID <nameslist>

<nameslist> ::= 
                , <names>
            | ε
    
<srepeatednames> ::=
                 ID . ID <repeatednameslist>

<repeatednameslist> ::= 
                , <srepeatednames>
                | ε

<tablesname> ::= 
                ID <nameslist>

<nameslist> ::= 
                , <tablesname>
            | ε 

<where> ::=
             WHERE <condition> <groupby>
        | ε

<conditionlist> ::= 
                    <logicaloperator> <condition>
                | ε

<logicaloperator> ::= 
                    AND
                | OR

<condition> ::= 
                <nombre> <operator> <expretion> <condition>
            | <nombre> ID <operator> <expretion> 
            | <nombre> <like>
            | <nombre> NOT <like
            | ( <nombre> <operator> <expretion> ) <condition>
            | ( <nombre> <operator> <expretion> <condition> )
            | <nombre> BETWEEN <expretion> AND <expretion>
            | <nombre> NOT BETWEEN <expretion> AND <expretion>
            | <nombre> NOT BETWEEN SYMMETRIC <expretion> AND <expretion>
            | <nombre> BETWEEN SYMMETRIC <expretion> AND <expretion>
            | <nombre> IS DISTINCT FROM <expretion>
            | <nombre> IS NOT DISTINCT FROM <expretion>
            | <nombre> IS NULL
            | <nombre> IS NOT NULL
            | <nombre> ISNULL
            | <nombre> NOTNULL
            | <nombre> IN  <subquerie>
            | <nombre> NOT IN <subquerie>
            | <nombre> <operator> ALL <subquerie>


<nombre> ::= 
            ID
          | ID . ID

<operator> ::= 
                =
            | >
            | >
            | >=
            | <=
            | ==
            | !=

<expretion> ::= 
                DIGITO
            | ID
            | CHARACTER
            | STRING
            | DATE
            | ID . ID

<like> ::= 
            LIKE % STRING %

<groupby> ::= 
            <names> <having>

<NAMES> ::= 
            ID <listnames>
            | ID . ID <listnames>

<listnames> ::= 
            , <names>
            | ε

<having> ::=
             HAVING <condition>

<orderby> ::=
             ORDER BY <nombre> <order> 

<order> ::= 
            ASC
        | DESC
        | ε

<funcitons> ::=  
                ABS
             | CBRT
             | CEIL
             | DEGREES
             | DIV
             | EXP
             | FACTORIAL
             | FLOOR
             | GCD
             | LCM
             | LN
             | LOG
             | LOG10
             | MIN_SCALE
             | MOD
             | PI
             | POWER
             | RADIANS
             | ROUND
             | SCALE
             | SIGN
             | SQRT
             | TRIM_SCALE
             | TRUC
             | WIDTH_BUCKET
             | RANDOM
             | SETSEED
             | ACOS
             | ACOSD
             | ASIN
             | ASIND
             | ATAN
             | ATAN2
             | ATAN2D
             | COS
             | COSD
             | COT
             | COTD
             | SIN
             | SIND
             | TAN
             | TAND
             | SINH
             | COSH
             | TANH
             | ASINH
             | ACOSH
             | ATANH
             | LENGTH
             | SUBSTRING
             | TRIM
             | GET_BYTE
             | MD5
             | SET_BYTE
             | SHA256
             | SUBSTR
             | CONVERT
             | ENCODE
             | DECODE
             | ε

<like> ::= 
            LIMIT DIGITO <offset>
        | LIMIT ALL <offset>
        | ε

<offset> ::= 
            OFFSET DIGITO

<combination> ::=
                 UNION <select>
                | INTERSECT <select>
                | EXCEPT <select>
                | ε
```

## Gramática Ascendente
La gramática descendente creada para el presente proyecto es la siguiente:
```
<init> ::= <instrucciones>

<problem> ::=  error PTCOMA

<instrucciones> ::= <instrucciones> <instruccion>
                | <instruccion>

<instruccion> ::=
                 CREATE <create>
                | USE <use>
                | SHOW <show>
                | DROP <drop>
                | DELETE <delete>
                | INSERT <insert>
                | UPDATE <update>
                | <alter>
                | <select>
                | <querys>

<querys>   ::=
                <select> UNION <allopcional> <select>
              | <select> INTERSECT  <allopcional> <select>
              | <select> EXCEPT  <allopcional> <select>

<allopcional>  ::= 
                ALL
                |ε

<select> ::= SELECT <parametrosselect> <fromopcional>

<fromopcional>    ::= 
                     FROM <parametrosfrom>  <whereopcional>
                    | FROM <parametrosfrom>  <groupbyopcional>
                    | ε

<whereopcional> ::=  
                    WHERE <condiciones> <groupbyopcional>
                    | ε 

<groupbyopcional>  ::= 
                        GROUP BY <listaids> <havings>
                      | GROUP BY <listanumeros> <havings>
                      | ε

<havings>   ::=
                 HAVING <condiciones>
                | ε

<listanumeros> ::= 
                  <listanumeros> COMA ENTERO
                  | ENTERO

<parametrosfrom> ::=
                   <parametrosfrom> COMA <parametrosfromr> <asopcional>
                  | <parametrosfromr> <asopcional>

<parametrosfromr>   ::= 
                      ID
                    | PARENIZQ <select> PARENDER'''

<parametrosselect> ::= 
                      DISTINCT <listadeseleccion>
                      | <listadeseleccion>

<listadeseleccion> ::= 
                        <listadeseleccion> COMA <listadeseleccionados>  <asopcional>
                      | <listadeseleccionados> <asopcional>

<listadeseleccionados> ::= 
                            PARENIZQ <select> PARENDER
                            | ASTERISCO
                            | GREATEST PARENIZQ <listadeargumentos>  PARENDER
                            | LEAST PARENIZQ <listadeargumentos>  PARENDER
                            | CASE <cases>  END ID 
                            | <funcionesmatematicassimples>
                            | <funcionestrigonometricas>
                            | <funcionesmatematicas>
                            | <funcionesdefechas>
                            | <funcionesbinarias>
                            | <operadoresselect>
                  
<listadeargumentos> ::= 
                        <listadeargumentos> COMA <argument>
                        | argument

<cases>    ::= 
              <cases> <case> <elsecase>
              | <case> <elsecase>

<case> ::= WHEN <condiciones>  THEN  <argument>

<elsecase>  ::= ELSE <argument>
                | ε

<operadoresselect> ::= 
                          PLECA <argumentodeoperadores>
                        | VIRGULILLA <argumentodeoperadores>

<operadoresselect>  ::=   PLECA <argumentodeoperadores>
                        | VIRGULILLA <argumentodeoperadores>
                        | PLECA PLECA <argumentodeoperadores>
                        | <argumentodeoperadores> AMPERSON <argumentodeoperadores>
                        | <argumentodeoperadores> PLECA <argumentodeoperadores>
                        | <argumentodeoperadores> NUMERAL          
                        | <argumentodeoperadores> MENORQUE MENORQUE <argumentodeoperadores>
                        | <argumentodeoperadores> MAYORQUE MAYORQUE <argumentodeoperadores>

<argumentodeoperadores>    ::= <argumentodeoperadores> MAS <argumentodeoperadores>
                                | <argumentodeoperadores> GUION <argumentodeoperadores>
                                | <argumentodeoperadores> BARRA <argumentodeoperadores>
                                | <argumentodeoperadores> ASTERISCO <argumentodeoperadores>
                                | <argumentodeoperadores> PORCENTAJE <argumentodeoperadores>
                                | <argumentodeoperadores> POTENCIA <argumentodeoperadores>
                                | DECIMAL
                                | ENTERO

<funcionesmatematicassimples>  ::= COUNT PARENIZQ <argument>  PARENDER
                                    | MAX PARENIZQ <argument>  PARENDER
                                    | SUM PARENIZQ <argument>  PARENDER
                                    | AVG PARENIZQ <argument>  PARENDER
                                    | MIN PARENIZQ <argument>  PARENDER

<funcionesbinarias>    : LENGTH PARENIZQ  <argument>   PARENDER
                            | SUBSTRING PARENIZQ  <argument>  COMA  ENTERO  COMA  ENTERO  PARENDER
                            | TRIM PARENIZQ  <argument>   PARENDER
                            | MD5 PARENIZQ  <argument>   PARENDER
                            | SHA PARENIZQ  <argument>   PARENDER
                            | SUBSTR PARENIZQ  <argument>  COMA  ENTERO  COMA  ENTERO  PARENDER
                            | GETBYTE PARENIZQ <argument> DOSPUNTOS DOSPUNTOS BYTEA COMA argument PARENDER
                            | SETBYTE PARENIZQ <argument> DOSPUNTOS DOSPUNTOS BYTEA COMA argument COMA argument PARENDER
                            | CONVERT PARENIZQ <argument> AS tipo
                            | ENCODE PARENIZQ <argument> DOSPUNTOS DOSPUNTOS BYTEA COMA CADENA PARENDER
                            | DECODE PARENIZQ <argument> COMA CADENA PARENDER

<funcionesmatematicas> ::=
                             PI PARENIZQ PARENDER
                            | RANDOM PARENIZQ PARENDER
                            | ABS PARENIZQ  <argument>  PARENDER
                            | CBRT PARENIZQ  <argument>   PARENDER
                            | CEIL PARENIZQ  <argument>   PARENDER
                            | CEILING PARENIZQ  <argument>   PARENDER
                            | DEGREES PARENIZQ  <argument>   PARENDER
                            | EXP PARENIZQ  <argument>   PARENDER
                            | FLOOR PARENIZQ  <argument>   PARENDER
                            | LN PARENIZQ  <argument>   PARENDER
                            | LOG PARENIZQ  <argument>   PARENDER
                            | RADIANS PARENIZQ  <argument>   PARENDER
                            | SCALE PARENIZQ  <argument>   PARENDER
                            | SIGN PARENIZQ  <argument>   PARENDER
                            | SQRT PARENIZQ  <argument>   PARENDER
                            | TRUNC PARENIZQ  <argument>   PARENDER
                            | DIV PARENIZQ  <argument>  COMA  <argument>  PARENDER
                            | GCD PARENIZQ  <argument>  COMA  <argument>  PARENDER
                            | MOD PARENIZQ  <argument>  COMA  <argument>   PARENDER
                            | POWER PARENIZQ  <argument>  COMA  <argument>   PARENDER
                            | ROUND PARENIZQ  <argument>   <tipoderound>  PARENDER
                            | BUCKET PARENIZQ  <argument> COMA <argument> COMA <argument> COMA <argument> PARENDER
                  
<tipoderound>  ::= 
                  COMA  <argument>
                  | ε

<funcionestrigonometricas> ::=  ACOS PARENIZQ <argument>  PARENDER
                                | ASIN PARENIZQ <argument>  PARENDER
                                | ACOSD PARENIZQ <argument>  PARENDER
                                | ASIND PARENIZQ <argument>  PARENDER
                                | ATAN PARENIZQ <argument>  PARENDER
                                | ATAND PARENIZQ <argument>  PARENDER
                                | ATANDOS PARENIZQ <argument> COMA <argument> PARENDER
                                | ATANDOSD PARENIZQ <argument> COMA <argument> PARENDER
                                | COS PARENIZQ <argument>  PARENDER
                                | COSD PARENIZQ <argument>  PARENDER
                                | COT PARENIZQ <argument>  PARENDER
                                | COTD PARENIZQ <argument>  PARENDER
                                | SIN PARENIZQ <argument>  PARENDER
                                | SIND PARENIZQ <argument>  PARENDER
                                | TAN PARENIZQ <argument>  PARENDER
                                | TAND PARENIZQ <argument>  PARENDER
                                | SINH PARENIZQ <argument>  PARENDER
                                | COSH PARENIZQ <argument>  PARENDER
                                | TANH PARENIZQ <argument>  PARENDER
                                | ASINH PARENIZQ <argument>  PARENDER
                                | ACOSH PARENIZQ <argument>  PARENDER
                                | ATANH PARENIZQ <argument>  PARENDER

<funcionesdefechas>    ::=
                           EXTRACT PARENIZQ  <partedelafecha>  FROM TIMESTAMP <argument> PARENDER
                            | DATEPART PARENIZQ <argument> COMA INTERVAL <argument> PARENDER
                            | NOW PARENIZQ PARENDER
                            | CURRENTDATE
                            | CURRENTTIME
                            | TIMESTAMP <argument>

<partedelafecha>   ::= 
                        YEAR
                        | MONTH
                        | DAY
                        | HOUR
                        | MINUTE
                        | SECOND

<listadeseleccionados> ::=
                          ID
                         | ID PUNTO ID

<asopcional>  ::=
                   AS ID
                  | ID
                  | AS CADENA
                  | CADENA
                  | ε

<argument> ::=
                 <funcionesmatematicassimples>
                | <funcionestrigonometricas>
                | <funcionesmatematicas>
                | <funcionesdefechas>
                | <funcionesbinarias>

<create> ::=
               TYPE <createenum>
              | TABLE <createtable>
              | OR REPLACE DATABASE <createdatabase>
              | DATABASE <createdatabase>
              | <problem>

<createenum> ::=
               ID AS ENUM PARENIZQ <listacadenas> PARENDER PTCOMA

<listacadenas> ::=
                   <listacadenas> COMA CADENA
                  | CADENA

<createdatabase> ::=
                       IF NOT EXISTS ID <databaseowner>
                      | ID <databaseowner>

<databaseowner> ::=
                     OWNER IGUAL <tipoowner> <databasemode>
                     | OWNER <tipoowner> <databasemode>
                     | <databasemode>
  
<tipoowner> ::=
                 ID
                | CADENA

<databasemode> ::=
                     MODE IGUAL ENTERO PTCOMA
                    | MODE ENTERO PTCOMA
                    | PTCOMA

<createtable> ::= 
                  ID PARENIZQ <tabledescriptions> PARENDER <tableherencia>

<tableherencia> ::=
                     INHERITS PARENIZQ ID PARENDER PTCOMA
                     | PTCOMA

<tabledescriptions> ::=
                       <tabledescriptions> COMA <tabledescription>
                       | tabledescription

<tabledescription> ::=
                         ID <tipo> <tablekey>
                        | PRIMARY KEY PARENIZQ <listaids> PARENDER
                        | FOREIGN KEY PARENIZQ <listaids> PARENDER REFERENCES ID PARENIZQ <listaids> PARENDER
                        | CONSTRAINT ID CHECK finalconstraintcheck
                        | CHECK <finalconstraintcheck>
                        | UNIQUE <finalunique>

<tablekey> ::=
                   PRIMARY KEY <tabledefault>
                | REFERENCES ID PARENIZQ <columnreferences> PARENDER <tabledefault>
                | REFERENCES ID <tabledefault>
                | tabledefault

<columnreferences> ::=
                       <columnreferences> COMA ID
                      | ID

<tabledefault> ::=
                | DEFAULT >value> <tablenull>
                | tablenull

<tablenull> ::=
                   NOT NULL <tableconstraintunique>
                 | NULL <tableconstraintunique>
                 | tableconstraintunique

<tableconstraintunique> ::=
                             CONSTRAINT ID UNIQUE <tableconstraintcheck>
                             | UNIQUE <tableconstraintcheck>
                             | <tableconstraintcheck>


<tableconstraintcheck> ::= CONSTRAINT ID CHECK PARENIZQ <condiciones> PARENDER
                            | CHECK PARENIZQ <condiciones> PARENDER
                            | ε

<finalconstraintcheck> ::=
                           PARENIZQ <condiciones> PARENDER

<finalunique> ::=
                   PARENIZQ <listaids> PARENDER

<listaids> ::= 
              <listaids> COMA ID
              | ID

<listaidcts> ::=
                 <listaidcts> COMA ID PUNTO ID
                 | <listaidcts> COMA ID
                 | ID PUNTO ID
                 | ID

<tipo> ::=
             SMALLINT
            | INTEGER
            | BIGINT
            | DECIMAL
            | NUMERIC
            | REAL
            | DOUBLE PRECISION
            | MONEY
            | CHARACTER <tipochar>
            | VARCHAR PARENIZQ ENTERO PARENDER
            | CHAR PARENIZQ ENTERO PARENDER
            | TEXT
            | TIMESTAMP <precision>
            | TIME <precision>
            | DATE
            | INTERVAL <fields> <precision>
            | BOLEANO
            | ID

<tipochar> ::=
                 VARYING PARENIZQ ENTERO PARENDER
                | PARENIZQ ENTERO PARENDER

<precision> ::=
               PARENIZQ ENTERO PARENDER
               | ε

<fields> ::=
               MONTH
              | HOUR
              | MINUTE
              | SECOND
              | YEAR 
              | ε

<use>    ::= 
              DATABASE ID PTCOMA

<show>   ::=
            DATABASES <likeopcional>
   
<likeopcional>   ::=   LIKE CADENA PTCOMA
                    | PTCOMA 

<drop> ::=
             DATABASE <dropdb> PTCOMA
            |   TABLE ID PTCOMA

<dropdb>   ::=
               IF EXISTS ID
              | ID

<alter>    ::=
                 DATABASE ID <alterdbs> PTCOMA
                | TABLE ID <altertables> PTCOMA

<alterdbs>   ::=
                 <alterdbs> COMA <alterdb>
                 | alterdb

<alterdb>  ::=
                   RENAME TO ID
                |  OWNER TO <tipodeowner>

<tipodeowner>  ::=
                   ID
                  | CURRENT_USER
                  | SESSION_USER

<altertables>   ::=
                 <altertables> COMA <altertable>
                 | <altertable>

<altertable>   ::=
                     ADD <alteradd>
                    | ALTER COLUMN ID SET <opcionesalterset>
                    | DROP <tipodedrop>
                    | RENAME COLUMN ID TO ID
                    | ALTER COLUMN ID TYPE <tipo>
  
<alteradd>     ::=
                      COLUMN ID <tipo>
                    |  CHECK PARENIZQ <condiciones> PARENDER
                    |  CONSTRAINT ID UNIQUE PARENIZQ ID PARENDER
                    |  FOREIGN KEY PARENIZQ <listaids> PARENDER REFERENCES PARENIZQ <listaidcts> PARENDER

<opcionesalterset> ::=
                       NOT NULL
                      | NULL 

<tipodedrop>   ::=
                     COLUMN ID
                    | CONSTRAINT  ID

<delete>    ::=  
                FROM ID <condicionesops> PTCOMA

<insert>    ::=
                 INTO ID VALUES PARENIZQ <values> PARENDER PTCOMA

<values>   ::= 
                <values> COMA <value>
                | <value>

<value>   ::= ENTERO
            | DECIMAL
            | CADENA
            | boleano
  
<update>    ::=
                 ID SET <asignaciones> condicionesops PTCOMA

<asignaciones> ::= <asignaciones> COMA ID IGUAL <argument>
                  | ID IGUAL <argument>
      
<condicionesops>  ::=
                       WHERE <condiciones>
                       | ε

<condiciones>    ::=
                     <condiciones> <comparacionlogica> <condicion>
                     | <condicion>

<comparacionlogica>    ::= AND
                          | OR

<condicion>    ::=
                   NOT <condicion>
                 | <condicions>

<condicions> ::=
                   <argument> MENORQUE <argument>
                  | <argument> MAYORQUE <argument>
                  | <argument> IGUAL <argument>
                  | <argument> MENORIGUALQUE <argument>
                  | <argument> MAYORIGUALQUE <argument>
                  | <argument> DIFERENTELL <argument>
                  | <argument> BETWEEN <betweenopcion>
                  | <argument> ISNULL
                  | <argument> NOTNULL
                  | <argument> IS isopcion
                  | <argument> IN PARENIZQ <select> PARENDER
                  | <argument> NOT BETWEEN <betweenopcion>
                  | <argument> NOT IN  PARENIZQ <select> PARENDER
                  | <argument> ANY  PARENIZQ <select> PARENDER
                  | <argument> ALL PARENIZQ <select> PARENDER
                  | <argument> SOME PARENIZQ <select> PARENDER
                  | EXISTS PARENIZQ <select> PARENDER

<betweenopcion>   ::= 
                      <symm> <argument> AND <argument>
                      | <argument> AND <argument>

<symm>   ::=
           SYMMETRIC

<isopcion> ::=
                 DISTINCT FROM <argument>
                | NULL
                | TRUE
                | FALSE
                | UNKNOWN
                | NOT <isnotoptions>

<isnotoptions> ::=
                     FALSE
                    | UNKNOWN
                    | TRUE
                    | NULL
                    | DISTINCT FROM <argument>

<argument> ::= <argument> MAS <argument>
                | <argument> GUION <argument>
                | <argument> BARRA <argument>
                | <argument> ASTERISCO <argument>
                | <argument> PORCENTAJE <argument>
                | <argument> POTENCIA <argument>
                | <boleano>
                | MAS <argument> <%prec> UMAS
                | GUION <argument> <%prec> UMENOS
                | PARENIZQ <argument> PARENDER
                | ENTERO
                | DECIMAL
                | CADENA
                | ID
                | ID PUNTO ID

<boleano>  ::=
               TRUE
             | FALSE


                
```