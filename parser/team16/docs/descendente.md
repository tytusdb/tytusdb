# Gramatica
```
<INICIO> ::= <INSTRUCCIONES\>
<INSTRUCCIONES> ::= <INSTRUCCION> <INSTRUCCIONES>'
<INSTRUCCIONES>' ::= <INSTRUCCION> <INSTRUCCIONES>'
              | ϵ
<INSTRUCCION> ::= <DML_COMANDOS>
              | <DQL_COMANDOS>
<DQL_COMANDOS> ::= SELECT <LISTA_CAMPOS> FROM <NOMBRES_TABLAS> <CUERPO> <UNIONS>
              | SELECT TIMESTAMP CADENASIMPLE PUNTOCOMA
              | SELECT NOW PARIZQ PARDER PUNTOCOMA
              | CREATE TYPE MOOD AS ENUM PARIZQ <LISTAS_CS> PARDER PUNTOCOMA
              | SELECT EXTRACT PARIZQ <TIPO_TIEMPO> FROM TIMESTAMP CADENASIMPLE PARDER PUNTOCOMA
              | SELECT DATE_PART PARIZQ CADENASIMPLE COMA INTERVAL CADENASIMPLE PARDER PUNTOCOMA
              | SELECT <TIPO_CURRENT> PUNTOCOMA
              | SELECT <DISTINCTNT> <LISTA_CAMPOS> FROM <NOMBRES_TABLAS> <CUERPO> <UNIONS>
              | SELECT <DISTINCTNT> <LISTA_CAMPOS> FROM <NOMBRES_TABLAS> <UNIONS>
              | SELECT <LISTA_CAMPOS> FROM <NOMBRES_TABLAS> <UNIONS>
<LISTA_CAMPOS> ::= <LISTAA> <LISTA_CAMPOS>'
<LISTA_CAMPOS>' ::= <LISTAA> <LISTA_CAMPOS>'
              | ϵ
<LISTAA> ::= <NOMBRE_T> PUNTO <CAMPOS> <S>
              | <NOMBRE_T> PUNTO <CAMPOS>
              | <CAMPOS> <S>
              | <CAMPOS>
              | <EXPRESIONES_C>
              | <SUBQUERYS>
<CAMPOS> ::= ID
              | ASTERISCO
<NOMBRE_T> ::= ID
<ALIAS> ::= ID
<S> ::= COMA <LISTAA>
              | AS <ALIAS>
              | AS <ALIAS> COMA <LISTA_CAMPOS>
              | ID COMA <LISTA_CAMPOS>
              | ID
<DISTINCTNT> ::= DISTINCT
<NOMBRES_TABLAS> ::= <TABLA> <NOMBRES_TABLAS>'
<NOMBRES_TABLAS>' ::= <TABLA> <NOMBRES_TABLAS>'
              | ϵ
<TABLA> ::= ID
              | ID <S1>
              | <SUBQUERYS>
<S1> ::= COMA <NOMBRES_TABLAS>
              | AS <ALIAS>
              | AS <ALIAS> COMA <TABLA>
              | ID COMA <TABLA>
              | ID
<CUERPOS> ::= <CUERPO> <CUERPOS>'
<CUERPOS>' ::= <CUERPO> <CUERPOS>'
              | ϵ
<CUERPO> ::= <MOREE>
              | WHEN <CONDICIONES> <EXPRESIONNE> END
              | WHEN <CONDICIONES> <EXPRESIONNE> ELSE <EXPRESIONNE> END
              | END
              | END ID
<MOREE> ::= <INNERS>
              | <GROUPS>
              | <LIMITS>
              | <CONDICIONS>
<CONDICIONS> ::= <CONDI> <CONDICIONS>'
<CONDICIONS>' ::= <CONDI> <CONDICIONS>'
              | ϵ
<CONDI> ::= WHERE <expresion>
<CONDICIONES> ::= <CONDICION> <CONDICIONES>'
<CONDICIONES>' ::= <CONDICION> <CONDICIONES>'
              | ϵ
<CONDICION> ::= <CONDICION_REL> <SIMBOLO_LOGICO> <CONDICION_REL> <OTRO_LOGICO>
              | <CONDICION_REL> <SIMBOLO_LOGICO> <CONDICION_REL>
              | <CONDICION_REL>
<CONDICION_REL> ::= <EXPRESIONNE> <OPERADOR> <EXPRESIONNE>
              | <SIMBOLO_NEG> <EXPRESIONNE>
              | <EXPRESIONNE>
<OTRO_LOGICO> ::= <SIMBOLO_LOGICO> <CONDICIONES>
<EXPRESIONNE> ::= <NOMBRE_C> PUNTO <CAMPOSC>
              | <expresion>
              | <SUBQUERYS>
<SIMBOLO_LOGICO> ::= AND
              | OR
<SIMBOLO_NEG> ::= NOT
<NOMBRE_C> ::= ID
<CAMPOSC> ::= ID
              | ENTERO
              | FLOTANTE
              | CADENASIMPLE
              | CADENADOBLE
<OPERADOR> ::= IGUAL
              | DIFERENTE
              | MAYOR
              | MENOR
              | MENORIGUAL
              | MAYORIGUAL
<INNERS> ::= <INNERR> <INNERS>'
<INNERS>' ::= <INNERR> <INNERS>'
              | ϵ
<INNERR> ::= <TIPOS_INNER> JOIN <TABLA_REF> ON <CONDICIONES>
              | JOIN <TABLA_REF> ON <CONDICIONES>
              | <TIPOS_INNER> JOIN <TABLA_REF> USING PARIZQ <SUB_COLUMN> PARDER
              | JOIN <TABLA_REF> USING PARIZQ <SUB_COLUMN> PARDER
              | WHERE <expresion>
<SUB_COLUMN> ::= JOIN <EXPRESIONNE>
              | ID PUNTO <CAMPOSC>
              | <expresion>
              | <SUBQUERYS>
<TIPOS_INNER> ::= INNER OUTER
              | INNER
              | LEFT OUTER
              | LEFT
              | RIGHT OUTER
              | RIGHT
              | FULL OUTER
              | FULL
<TABLA_REF> ::= ID
              | ID AS ID
              | ID ID
<GROUPS> ::= <GROUPP> <GROUPS>'
<GROUPS>' ::= <GROUPP> <GROUPS>'
              | ϵ
<GROUPP> ::= GROUP BY <EXPRE_LIST> HAVING <expresion>
              | GROUP BY <EXPRE_LIST>
<EXPRE_LIST> ::= <EXPRES> <EXPRE_LIST>'
<EXPRE_LIST>' ::= <EXPRES> <EXPRE_LIST>'
              | ϵ
<EXPRES> ::= ID PUNTO <CAMPOS> <S2>
              | ID PUNTO <CAMPOS>
              | ID <S2>
              | ASTERISCO <S2>
              | ID
              | ASTERISCO
              | ID PUNTO <CAMPOS> <S2> <STATE>
              | ID PUNTO <CAMPOS> <STATE>
              | ID <S2> <STATE>
              | ASTERISCO <S2> <STATE>
              | ID <STATE>
              | ASTERISCO <STATE>
<S2> ::= COMA <EXPRES>
              | AS <ALIAS>
              | AS <ALIAS> COMA <EXPRES>
              | ID
              | ID COMA <EXPRES>
<STATE> ::= ASC
              | ASC NULLS FIRST
              | ASC NULLS LAST
              | DESC
              | DESC NULLS FIRST
              | DESC NULLS LAST
<LIMITS> ::= <LIMITT> <LIMITS>'
<LIMITS>' ::= <LIMITT> <LIMITS>'
              | ϵ
<LIMITT> ::= LIMIT <EXPRE_NUM>
              | OFFSET <EXPRE_NUM>
<EXPRE_NUM> ::= ENTERO
              | ALL
<SUBQUERYS> ::= <QUERY> <SUBQUERYS>'
<QUERY> ::= <ATE_QUE> PARIZQ <QUE> PARDER
              | <ATE_QUE> PARIZQ <QUE> PARDER <AS_NO>
              | PARIZQ <QUE> PARDER
              | PARIZQ <QUE> PARDER <AS_NO>
<AS_NO> ::= COMA <QUERY>
              | AS <NO_N>
              | AS <NO_N> COMA <QUERY>
              | <NO_N>
              | <NO_N> COMA <QUERY>
<NO_N> ::= ID
<ATE_QUE> ::= EXISTS <ATE_QUE>'
              | ID PUNTO <CAMPOSC> <OPCIONALESS> <ATE_QUE>'
              | <expresion> <OPCIONALESS> <ATE_QUE>'
              | PARIZQ <QUE> PARDER <SUBQUERYS>' <OPCIONALESS> <ATE_QUE>'
              | PARIZQ <QUE> PARDER <AS_NO> <SUBQUERYS>' <OPCIONALESS> <ATE_QUE>'
              | ID PUNTO <CAMPOSC> <OPERADOR> <OPCIONALESS2> <ATE_QUE>'
              | <expresion> <OPERADOR> <OPCIONALESS2> <ATE_QUE>'
              | PARIZQ <QUE> PARDER <SUBQUERYS>' <OPERADOR> <OPCIONALESS2> <ATE_QUE>'
              | PARIZQ <QUE> PARDER <AS_NO> <SUBQUERYS>' <OPERADOR> <OPCIONALESS2> <ATE_QUE>'
              | ID <ATE_QUE>'
<ATE_QUE>' ::= PARIZQ <QUE> PARDER <SUBQUERYS>' <OPCIONALESS> <ATE_QUE>'
              | PARIZQ <QUE> PARDER <AS_NO> <SUBQUERYS>' <OPCIONALESS> <ATE_QUE>'
              | PARIZQ <QUE> PARDER <SUBQUERYS>' <OPERADOR> <OPCIONALESS2> <ATE_QUE>'
              | PARIZQ <QUE> PARDER <AS_NO> <SUBQUERYS>' <OPERADOR> <OPCIONALESS2> <ATE_QUE>'
              | ϵ
<SUBQUERYS>' ::= <QUERY> <SUBQUERYS>'
              | ϵ
<OPCIONALESS> ::= IN
              | NOT IN
<OPCIONALESS2> ::= ANY
              | ALL
              | SOME
<QUE> ::= <QUE_SUBS>
<QUE_SUBS> ::= SELECT <LISTA_CAMPOS> FROM <NOMBRES_TABLAS> <CUERPO>
              | SELECT <LISTA_CAMPOS> FROM <NOMBRES_TABLAS>
              | SELECT <DISTINCTNT> <LISTA_CAMPOS> FROM <NOMBRES_TABLAS> <CUERPO>
              | SELECT <DISTINCTNT> <LISTA_CAMPOS> FROM <NOMBRES_TABLAS>
<UNIONS> ::= <UNIONN> <UNIONS>'
<UNIONS>' ::= <UNIONN> <UNIONS>'
              | ϵ
<UNIONN> ::= <COMPORTAMIENTO> ALL <DQL_COMANDOS>
              | <COMPORTAMIENTO> <DQL_COMANDOS>
              | PUNTOCOMA
<COMPORTAMIENTO> ::= UNION
              | INTERSECT
              | EXCEPT
<EXPRESIONES_C> ::= CASE <WHEN_LIST> <CUERPO>
              | GREATEST PARIZQ <EXPRESIONNE> PARDER
              | LEAST PARIZQ <EXPRESIONNE> PARDER
<WHEN_LIST> ::= <WHEN_UNI> <WHEN_LIST>'
<WHEN_LIST>' ::= <WHEN_UNI> <WHEN_LIST>'
              | ϵ
<WHEN_UNI> ::= WHEN <CONDICIONES> THEN <EXPRESIONNE>
              | WHEN <CONDICIONES> <EXPRESIONNE> THEN <EXPRESIONNE>
              | WHEN <CONDICIONES> <EXPRESIONNE> ELSE <EXPRESIONNE> THEN <EXPRESIONNE>
<DML_COMANDOS> ::= CREATE TABLE ID PARIZQ <CUERPO>_CREATE_TABLE PARDER PUNTOCOMA
              | CREATE TABLE ID PARIZQ <CUERPO>_CREATE_TABLE PARDER <INHER> PUNTOCOMA
              | INSERT INTO <LISTA_DE_IDS> <DATOS> PUNTOCOMA
              | INSERT INTO <NOMBRES_TABLAS> DEFAULT VALUES PUNTOCOMA
              | UPDATE <LISTA_DE_IDS> SET <CAMPOSN> WHERE <expresion> PUNTOCOMA
              | UPDATE <LISTA_DE_IDS> SET <CAMPOSN> PUNTOCOMA
              | DELETE FROM <LISTA_DE_IDS> WHERE <expresion> PUNTOCOMA
              | DELETE FROM <LISTA_DE_IDS> PUNTOCOMA
              | DROP TABLE <LISTA_DE_IDS> PUNTOCOMA
              | ALTER TABLE ID ADD COLUMN <LISTA_ALTER_EM> PUNTOCOMA
              | ALTER TABLE ID DROP COLUMN <LISTA_DE_IDS> PUNTOCOMA
              | ALTER TABLE ID RENAME COLUMN ID TO ID PUNTOCOMA
              | ALTER TABLE ID DROP CONSTRAINT ID PUNTOCOMA
              | ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PUNTOCOMA
              | ALTER TABLE ID ADD FOREIGN KEY PARIZQ ID PARDER REFERENCES ID PUNTOCOMA
              | ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ ID PARDER PUNTOCOMA
              | ALTER COLUMN ID TYPE <TIPO_CAMPO> COMA
              | ALTER COLUMN ID TYPE <TIPO_CAMPO> PUNTOCOMA
<INHER> ::= INHERITS PARIZQ ID PARDER
<CUERPO_CREATE_TABLE ::= <LISTA_DE_COLUMNAS>
<LISTA_DE_COLUMNAS> ::= <LISTA2> <LISTA_DE_COLUMNAS>'
<LISTA_DE_COLUMNAS>' ::= <LISTA2> <LISTA_DE_COLUMNAS>'
              | ϵ
<LISTA2> ::= ID <TIPO_CAMPO> <VALIDACIONES_CREATE_TABLE> COMA
              | ID <TIPO_CAMPO> <VALIDACIONES_CREATE_TABLE>
              | CONSTRAINT ID UNIQUE
              | CONSTRAINT ID UNIQUE COMA
              | CONSTRAINT ID CHECK PARIZQ <VALORES> PARDER
              | CONSTRAINT ID CHECK PARIZQ <VALORES> PARDER COMA
              | UNIQUE PARIZQ <LISTA_DE_IDS> PARDER COMA
              | UNIQUE PARIZQ <LISTA_DE_IDS> PARDER
              | CONSTRAINT ID PRIMARY KEY PARIZQ <LISTA_DE_IDS> PARDER
              | CONSTRAINT ID PRIMARY KEY PARIZQ <LISTA_DE_IDS> PARDER COMA
              | PRIMARY KEY PARIZQ <LISTA_DE_IDS> PARDER COMA
              | FOREIGN KEY PARIZQ <LISTA_DE_IDS> PARDER REFERENCES ID PARIZQ <LISTA_DE_IDS> PARDER COMA
              | PRIMARY KEY PARIZQ <LISTA_DE_IDS> PARDER
              | FOREIGN KEY PARIZQ <LISTA_DE_IDS> PARDER REFERENCES ID PARIZQ <LISTA_DE_IDS> PARDER
<LISTA_DE_IDS> ::= <LISTA_ID_> <LISTA_DE_IDS>'
<LISTA_ID_> ::= ID COMA
              | ID
<TIPO_CAMPO> ::= SMALLINT
              | INTEGER
              | INT
              | BIGINT
              | DECIMAL
              | REAL
              | MONEY
              | FLOAT
              | TEXT
              | BOOLEAN
              | DOUBLE PRECISION
              | CHARACTER VARYING PARIZQ <expresion_aritmetica> PARDER
              | VARCHAR PARIZQ <expresion_aritmetica> PARDER
              | CHARACTER PARIZQ <expresion_aritmetica> PARDER
              | CHAR PARIZQ <expresion_aritmetica> PARDER
<VALIDACIONES_CREATE_TABLE> ::= <LISTA3>
<LISTA3> ::= <VALIDACION_CAMPO_CREATE> <LISTA3>'
              | <VALIDACION_CAMPO_CREATE_VACIO> <LISTA3>'
<LISTA3>' ::= <VALIDACION_CAMPO_CREATE> <LISTA3>'
              | ϵ
<VALIDACION_CAMPO_CREATE> ::= NOT NULL
              | PRIMARY KEY
              | DEFAULT CADENASIMPLE
              | DEFAULT CADENADOBLE
              | DEFAULT DECIMAL
              | DEFAULT ENTERO
              | DEFAULT ID
              | NULL
              | CONSTRAINT ID UNIQUE
              | CONSTRAINT ID CHECK PARIZQ <CONDICIONES> PARDER
<VALIDACION_CAMPO_CREATE_VACIO> ::= <empty>
<DATOS> ::= PARIZQ <COLUMNAS> PARDER VALUES PARIZQ <VALORES> PARDER
              | VALUES PARIZQ <VALORES> PARDER
<COLUMNAS> ::= <COLUMNA> <COLUMNAS>'
<COLUMNAS>' ::= <COLUMNA> <COLUMNAS>'
              | ϵ
<COLUMNA> ::= ID COMA
              | ID
<VALORES> ::= <VALOR> <VALORES>'
<VALORES>' ::= <VALOR> <VALORES>'
              | ϵ
<VALOR> ::= <expresion> COMA
              | <expresion>
<CAMPOSN> ::= <CAMPO> <CAMPOSN>'
<CAMPOSN>' ::= <CAMPO> <CAMPOSN>'
              | ϵ
<CAMPO> ::= <expresion>
              | <expresion> COMA
              | ID COMA <LISTA_DE_IDS>' PUNTO ID IGUAL <expresion>
              | ID <LISTA_DE_IDS>' PUNTO ID IGUAL <expresion>
              | ID COMA <LISTA_DE_IDS>' PUNTO ID IGUAL <expresion> COMA
              | ID <LISTA_DE_IDS>' PUNTO ID IGUAL <expresion> COMA
<LISTA_DE_IDS>' ::= <LISTA_ID_> <LISTA_DE_IDS>'
              | ϵ
<LISTA_ALTER_EM> ::= <LISTA_ALTER_EM_> <LISTA_ALTER_EM>'
<LISTA_ALTER_EM>' ::= <LISTA_ALTER_EM_> <LISTA_ALTER_EM>'
              | ϵ
<LISTA_ALTER_EM_> ::= ID <TIPO_CAMPO> COMA
              | ID <TIPO_CAMPO>
<DDL_COMANDOS> ::= <CREATE_DATABASE>
              | <SHOW_DATABASES>
              | <ALTER_DATABASE>
              | <DROP_DATABASE>
<CREATE_DATABASE> ::= CREATE <REPLACE_OP> DATABASE <IF_NOT_EXISTIS> ID <OWNER_DATABASE> <MODE_DATABASE> PUNTOCOMA
<REPLACE_OP> ::= OR REPLACE
              | <empty>
<IF_NOT_EXISTIS> ::= IF NOT EXISTS
              | <empty>
<OWNER_DATABASE> ::= OWNER IGUAL ID
              | <empty>
<MODE_DATABASE> ::= MODE IGUAL ENTERO
              | <empty>
<SHOW_DATABASES> ::= SHOW DATABASES <SHOW_DATABASES_LIKE> PUNTOCOMA
<SHOW_DATABASES_LIKE> ::= LIKE CADENADOBLE
              | <empty>
<ALTER_DATABASE> ::= ALTER DATABASE ID <ALTER_DATABASE_OP> PUNTOCOMA
<ALTER_DATABASE_OP> ::= RENAME TO ID
              | OWNER TO <ALTER_TABLE_OP_OW>
              | <empty>
<ALTER_TABLE_OP_OW> ::= ID
              | CURRENT_USER
              | SESSION_USER
<DROP_DATABASE> ::= DROP DATABASE <IF_EXISTS_DATABASE> ID PUNTOCOMA
<IF_EXISTS_DATABASE> ::= IF EXISTS
              | <empty>
<TIPO_TIEMPO> ::= YEAR
              | HOUR
              | MINUTE
              | SECOND
<TIPO_CURRENT> ::= CURRENT_DATE
              | CURRENT_TIME
<LISTAS_CS> ::= <LISTA_CS>
<LISTA_CS> ::= CADENASIMPLE
              | CADENASIMPLE <CS>
<CS> ::= COMA <LISTA_CS>
<expresion> ::= <expresion_aritmetica>
              | <expresion_logica>
              | <expresion_unaria>
<expresion_relacional> ::= <expresion_aritmetica> IGUAL <expresion_aritmetica>
              | <expresion_aritmetica> DIFERENTE <expresion_aritmetica>
              | <expresion_aritmetica> MAYORIGUAL <expresion_aritmetica>
              | <expresion_aritmetica> MENORIGUAL <expresion_aritmetica>
              | <expresion_aritmetica> MAYOR <expresion_aritmetica>
              | <expresion_aritmetica> MENOR <expresion_aritmetica>
              | PARIZQ <expresion_relacional> PARDER
<expresion_logica> ::= NOT <expresion_logica> <expresion_logica>'
              | PARIZQ <expresion_logica> PARDER <expresion_logica>'
              | <expresion_aritmetica> IGUAL <expresion_aritmetica> <expresion_logica>'
              | <expresion_aritmetica> DIFERENTE <expresion_aritmetica> <expresion_logica>'
              | <expresion_aritmetica> MAYORIGUAL <expresion_aritmetica> <expresion_logica>'
              | <expresion_aritmetica> MENORIGUAL <expresion_aritmetica> <expresion_logica>'
              | <expresion_aritmetica> MAYOR <expresion_aritmetica> <expresion_logica>'
              | <expresion_aritmetica> MENOR <expresion_aritmetica> <expresion_logica>'
              | PARIZQ <expresion_relacional> PARDER <expresion_logica>'
              | EXISTS <QUE> <expresion_logica>'
              | <expresion_aritmetica> IN <QUE> <expresion_logica>'
              | <expresion_aritmetica> NOT IN <QUE> <expresion_logica>'
              | <expresion_aritmetica> NOT BETWEEN <expresion_aritmetica> AND <expresion_aritmetica> <expresion_logica>'
              | <expresion_aritmetica> IS NOT DISTINCT FROM <expresion_aritmetica> <expresion_logica>'
              | <expresion_aritmetica> BETWEEN <expresion_aritmetica> AND <expresion_aritmetica> <expresion_logica>'
              | <expresion_aritmetica> IS DISTINCT FROM <expresion_aritmetica> <expresion_logica>'
              | <expresion_aritmetica> IS NOT NULL <expresion_logica>'
              | <expresion_aritmetica> IS NOT TRUE <expresion_logica>'
              | <expresion_aritmetica> IS NOT FALSE <expresion_logica>'
              | <expresion_aritmetica> IS NOT UNKNOWN <expresion_logica>'
              | <expresion_aritmetica> IS NULL <expresion_logica>'
              | <expresion_aritmetica> IS TRUE <expresion_logica>'
              | <expresion_aritmetica> IS FALSE <expresion_logica>'
              | <expresion_aritmetica> IS UNKNOWN <expresion_logica>'
<expresion_logica>' ::= AND <expresion_logica> <expresion_logica>'
              | OR <expresion_logica> <expresion_logica>'
              | ϵ
<expresion_aritmetica> ::= MENOS <expresion_aritmetica> <expresion_aritmetica>'
              | ID <expresion_aritmetica>'
              | ENTERO <expresion_aritmetica>'
              | FLOTANTE <expresion_aritmetica>'
              | DEFAULT <expresion_aritmetica>'
              | CADENASIMPLE <expresion_aritmetica>'
              | CADENADOBLE <expresion_aritmetica>'
              | CADENABINARIA <expresion_aritmetica>'
              | TRUE <expresion_aritmetica>'
              | FALSE <expresion_aritmetica>'
              | PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | ABS PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | CBRT PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | CEIL PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | CEILING PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | DEGREES PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | DIV PARIZQ <expresion_aritmetica> COMA <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | EXP PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | FACTORIAL PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | FLOOR PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | GCD PARIZQ <expresion_aritmetica> COMA <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | LN PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | LOG PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | MOD PARIZQ <expresion_aritmetica> COMA <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | PI PARIZQ PARDER <expresion_aritmetica>'
              | POWER PARIZQ <expresion_aritmetica> COMA <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | RADIANS PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | ROUND PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | SIGN PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | SQRT PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | WIDTH_BUCKET PARIZQ <expresion_aritmetica> COMA <expresion_aritmetica> COMA <expresion_aritmetica> COMA <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | TRUNC PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | RANDOM PARIZQ PARDER <expresion_aritmetica>'
              | ACOS PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | ACOSD PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | ASIN PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | ASIND PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | ATAN PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | ATAND PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | ATAN2 PARIZQ <expresion_aritmetica> COMA <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | ATAN2D PARIZQ <expresion_aritmetica> COMA <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | COS PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | COSD PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | COT PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | COTD PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | SIN PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | SIND PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | TAN PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | TAND PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | SINH PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | COSH PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | TANH PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | ASINH PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | ACOSH PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | ATANH PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | LENGTH PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | SUBSTRING PARIZQ <expresion_aritmetica> COMA <expresion_aritmetica> COMA <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | TRIM PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | MD5 PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | SHA256 PARIZQ <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | SUBSTR PARIZQ <expresion_aritmetica> COMA <expresion_aritmetica> COMA <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | GET_BYTE PARIZQ <expresion_aritmetica> COMA <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | SET_BYTE PARIZQ <expresion_aritmetica> COMA <expresion_aritmetica> COMA <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | CONVERT PARIZQ <expresion_aritmetica> AS <TIPO_CAMPO> PARDER <expresion_aritmetica>'
              | ENCODE PARIZQ <expresion_aritmetica> COMA <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | DECODE PARIZQ <expresion_aritmetica> COMA <expresion_aritmetica> PARDER <expresion_aritmetica>'
              | VIRGULILLA <expresion_aritmetica> <expresion_aritmetica>'
<expresion_aritmetica>' ::= MAS <expresion_aritmetica> <expresion_aritmetica>'
              | MENOS <expresion_aritmetica> <expresion_aritmetica>'
              | ASTERISCO <expresion_aritmetica> <expresion_aritmetica>'
              | DIVISION <expresion_aritmetica> <expresion_aritmetica>'
              | PORCENTAJE <expresion_aritmetica> <expresion_aritmetica>'
              | DOBLEPLECA <expresion_aritmetica> <expresion_aritmetica>'
              | AMPERSAND <expresion_aritmetica> <expresion_aritmetica>'
              | PLECA <expresion_aritmetica> <expresion_aritmetica>'
              | NUMERAL <expresion_aritmetica> <expresion_aritmetica>'
              | LEFTSHIFT <expresion_aritmetica> <expresion_aritmetica>'
              | RIGHTSHIFT <expresion_aritmetica> <expresion_aritmetica>'
              | ϵ
```