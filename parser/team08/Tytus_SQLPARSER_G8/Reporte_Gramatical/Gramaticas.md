# Gramaticas BNF - PostgeSQL 13.1 

Universidad de San Carlos de Guatemala  
Facultad de Ingeniería  
Curso: 781 Organización de Lenguajes y Compiladores 2  
Diciembre 2020
Ing. Luis Espino | Aux. Juan Carlos Maeda
Grupo 8

## Índice
- [Descripcion](#descripcion)
- [Elementos Lexicos](#elementos-lexicos)
- [Gramatica Descendente](#gramatica-descendente) 
- [Gramatica Ascendente](#gramatica-ascendente)

## Descripcion
 

## Elementos Lexicos

### Palabras reservadas
~~~
<reservadas> ::= TABLE | INT | VARCHAR | DATE
 | CHAR | DOUBLE | DECIMAL | NULL | PRIMARY | KEY 
 | REFERENCES | FOREIGN 
 | FLOAT 
 | BETWEEN 
 | LIKE 
 | IN | TYPE | INHERITS 
 | ENUM | IS | SHOW | DATABASES 
 | USE | RENAME | TO | OWNER 
 | CURRENT_USER | SESSION_USER 
 | IF | EXISTS | MODE | REPLACE 
 | DEFAULT | UNIQUE | CONSTRAINT | CHECK | DISTINCT 
 | SMALLINT | INTEGER | BIGINT 
 | NUMERIC | REAL | PRECISION | MONEY 
 | CHARACTER | VARYING | TEXT 
 | TIMESTAMP | TIME | INTERVAL 
 | EXTRACT | YEAR | MONTH | DAY | HOUR 
 | MINUTE | SECOND 
 | NOW | DATE_PART |CURRENT_DATE 
 | CURRENT_TIME | BOOLEAN 
 | AND | OR | NOT 
 | SELECT | FROM | WHERE | AS 
 | INSERT | INTO | VALUES 
 | UPDATE | SET 
 | DELETE | CREATE | DROP 
 | ALTER | COLUMN 
 | ADD | TRUNCATE | DATABASE
 | SUM | MAX | MIN | AVG | COUNT | TOP
 | INNER | JOIN | LEFT | RIGHT | FULL | OUTER | ON 
 | GROUP  | HAVING 
 | ABS | CBRT | CEIL | CEILING | DEGREES | DIV 
 | EXP | FACTORIAL | FLOOR | GCD 
 | LCM | LN | LOG | LOG10 | MIN_SCALE 
 | MOD | PI | POWER | RADIANS
 | ROUND | SCALE | SIGN 
 | SQRT | TRIM_SCALE | TRUNC 
 | WIDTH_BUCKET | RANDOM | SETSEED 
 | LENGTH | SUBSTRING | TRIM 
 | GET_BYTE | MD5 | SET_BYTE 
 | SHA256 | SUBSTR | CONVERT | ENCODE | DECODE 
 | ACOS | ACOSD | ASIN | ASIND 
 | ATAN | ATAND | ATAN2 | ATAN2D 
 | COS | COSD | COT | COTD | SIN | SIND  
 | TAN | TAND | SINH 
 | COSH | TANH | ASINH | ACOSH | ATANH 
 | ORDER | BY | FIRST | LAST | ASC | DESC | NULLS 
 | CASE |WHEN |THEN |ELSE | LEAST | GREATEST 
 | LIMIT | OFFSET 
 | UNION | INTERSECT | EXCEPT | ALL 
 | FUNCTION | BEGIN | END | DECLARE
~~~

### Caracteres especiales

~~~
<caracter_especial> ::= <IGUAL> | <BLANCO> |
    <MAYORQ> |
    <MENORQ> |
    <MAYOR_IGUALQ> |
    <MENOR_IGUALQ> |
    <DISTINTO> |
    <PARIZQ> |
    <PARDER> |
    <CORIZQ> |
    <CORDER> |
    <MAS> |
    <LLAVEA> |
    <LLAVEC> |
    <MENOS> |
    <POR> |
    <DIVIDIDO> |
    <EXPONENCIACION> |
    <MODULO> |
    <ENTERO> |
    <PUNTO_COMA> |
    <PUNTO> |
    <FDECIMAL> |
    <COMA> |
    <ID> |
    <CADENA> |
    <CARACTER> |
    <COMENTARIO_MULTILINEA> |
    <COMENTARIO_SIMPLE> |
    <ARROBA>

<ARROBA> = @
<PARIZQ> = (
<PARDER> = )
<CORIZQ> = [
<CORDER> = ]
<PUNTO_COMA> = ;
<COMA> = ,
<PUNTO> = .
<MAS> = +
<MENOS> = -
<POR> = *
<DIVIDIDO> = /
<EXPONENCIACION> = ^
<MODULO> = %
<DISTINTO> = <>
<IGUAL> = =
<MAYORQ> = >
<MENORQ> = <
<MAYOR_IGUALQ> = >=
<MENOR_IGUALQ> = <=

~~~

## Gramatica Descendente 
    
~~~
<<instrucciones>> ::= <instruccion> { <instruccion> }
			

<instruccion> ::= CREATE TABLE ID PARIZQ <campos> PARDER PUNTO_COMA
			| TRUNCATE TABLE ID PUNTO_COMA
			| DROP TABLE ID PUNTO_COMA
			| DROP ID
			| UPDATE ID SET <l_columnas> WHERE <logicos> PUNTO_COMA
			| DELETE FROM ID WHERE <logicos> PUNTO_COMA
			| CREATE FUNCTION ID BEGIN <instrucciones> END PUNTO_COMA
			| CREATE FUNCTION ID PARIZQ <lcol> PARDER BEGIN <instrucciones> END PUNTO_COMA
			| CREATE FUNCTION ID PARIZQ <lcol> PARDER AS <expresion> BEGIN <instrucciones> END PUNTO_COMA
			| DECLARE <expresion> AS <expresion> PUNTO_COMA
			| DECLARE <expresion> <tipo> PUNTO_COMA
			| SET <expresion> IGUAL <logicos> PUNTO_COMA
			| ALTER TABLE ID ADD ID <tipo> PUNTO_COMA
			| ALTER TABLE ID DROP <lcol> ID PUNTO_COMA
			| INSERT INTO ID PARIZQ <lcol> PARDER VALUES PARIZQ <l_expresiones> PARDER PUNTO_COMA
			| INSERT INTO ID VALUES PARIZQ <l_expresiones> PARDER PUNTO_COMA
			| SELECT <lcol> FROM <lcol> <inners> PUNTO_COMA
			| SELECT POR FROM <lcol> <inners> PUNTO_COMA
			| SELECT <lcol> FROM <lcol> <inners> WHERE <logicos> PUNTO_COMA
			| SELECT POR FROM <lcol> <inners> WHERE <logicos> PUNTO_COMA


<l_columnas> ::= <logicos> COMA <l_columnas>
			| <logicos>
			
<inners> ::= [ FULL OUTER | INNER | LEFT | RIGHT ] JOIN <logicos> ON <logicos>
        
<logicos> ::= <lt> OR { <lt> } 

<lt> ::= <lf> AND { <lf> }
	
<lf> ::= <lfp> LIKE { <lfp> }
	| <lfp> BETWEEN { <lfp> }
	| <lfp> IN { <lfp> }
	| <lfp> NOT LIKE { <lfp> }
	| <lfp> NOT BETWEEN { <lfp> }

<lfp> ::= <relacional>
	| NOT <logicos> 
	| PARIZQ <logicos> PARDER

<relacional> ::= <rf> IGUAL { <rf> } 
			| <rf> MAYORQ { <rf> }
			| <rf> MENORQ { <rf> }
			| <rf> MAYOR_IGUALQ { <rf> }
			| <rf> MENOR_IGUALQ { <rf> }
			| <rf> DISTINTO { <rf> }

<rf> ::= <expre>
	| PARIZQ <logicos> PARDER
	
<expre> ::= <t> SUMA { <t> }
		| <t> RESTA { <t> }

<t> ::= <tp> MULTIPLICACION {<tp>}
	| <tp> DIVISION {<tp>}
	
<tp> ::= <tpp> MODULO {<tpp>}

<tpp> ::= <expresion> AS ID
	  | <expresion>

<expresion> ::= CADENA
            | CARACTER
            | ENTERO
            | FDECIMAL
            | DOUBLE
            | ID [ PUNTO ID | PARIZQ <lcol> PARDER ] 
            | ARROBA ID
            | ID 	
			
<campos> ::= ID <l_campo> COMA { ID <l_campo> }
			
<l_campo> ::= <tipo> { <tipo> }
			 
<l_expresiones> ::= <expresion> COMA { <expresion }			

<lcol> ::= <expre> COMA { <expre> }

<tipo> ::= INT
		| DATE
        | NOT
        | NULL
        | PRIMARY KEY
        | FOREIGN KEY REFERENCES
        | ID PARIZQ ID PARDER
		| VARCHAR PARIZQ ENTERO PARDER
        | CHAR PARIZQ ENTERO PARDER
		| DECIMAL [ PARIZQ ENTERO COMA ENTERO PARDER ]
        | DOUBLE
        | ENTERO
		| SMALLINT
		| BIGINT
		| NUMERIC [ PARIZQ ENTERO COMA ENTERO PARDER ]
		| REAL
        | FLOAT PARIZQ ENTERO COMA ENTERO PARDER



			
			
~~~


## Gramatica Ascendente
~~~

<instrucciones> ::= { < instruccion > } <instruccion>

<instruccion> ::= CREATE [ OR REPLACE ] DATABASE [ <if_not_exists> ] ID [ OWNER IGUAL ID ] [ MODE IGUAL ENTERO ]  PUNTO_COMA
        | CREATE TABLE ID PARIZQ <campos> PARDER [ INHERITS PARIZQ ID PARDER ] PUNTO_COMA
        | USE ID PUNTO_COMA
        | SHOW DATABASES [ LIKE CARACTER ] PUNTO_COMA
        | CREATE TYPE ID AS ENUM PARIZQ <l_expresiones> PARDER PUNTO_COMA
        | TRUNCATE TABLE ID PUNTO_COMA
        | DROP DATABASE [ IF EXISTS ] ID PUNTO_COMA
        | DROP TABLE ID PUNTO_COMA
        | DROP ID
        | UPDATE ID SET <l_columnas> <instructionWhere> PUNTO_COMA
        | DELETE FROM ID <instructionWhere> PUNTO_COMA
        | CREATE FUNCTION ID [ PARIZQ <lcol> PARDER [ AS <expresion> ] ] BEGIN <instrucciones> END PUNTO_COMA
        | DECLARE <expresion> AS <expresion> PUNTO_COMA
        | DECLARE <expresion> <tipo> PUNTO_COMA
        | SET <expresion> IGUAL <expre> PUNTO_COMA
        | ALTER TABLE ID ADD ID tipo PUNTO_COMA
        | ALTER DATABASE ID RENAME TO ID PUNTO_COMA
        | ALTER DATABASE ID OWNER TO <list_owner> PUNTO_COMA
        | ALTER TABLE ID ADD COLUMN ID <tipo> PUNTO_COMA
        | ALTER TABLE ID DROP COLUMN ID PUNTO_COMA
        | ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ <lista_id> PARDER PUNTO_COMA
        | ALTER TABLE ID ADD FOREIGN KEY PARIZQ <lista_id> PARDER REFERENCES ID PARIZQ <lista_id> PARDER PUNTO_COMA
        | ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PUNTO_COMA
        | ALTER TABLE ID DROP CONSTRAINT ID PUNTO_COMA
        | ALTER TABLE ID ADD CHECK <expre> PUNTO_COMA
        | ALTER TABLE ID ADD CONSTRAINT ID CHECK <expre> PUNTO_COMA
        | ALTER TABLE ID RENAME COLUMN ID TO ID PUNTO_COMA
        | INSERT INTO ID PARIZQ <lcol> PARDER VALUES PARIZQ <l_expresiones> PARDER PUNTO_COMA
        | INSERT INTO ID VALUES PARIZQ <l_expresiones> PARDER PUNTO_COMA
        | <lquery> PUNTO_COMA

<if_not_exists> ::= IF NOT EXISTS
            | 

<instructionWhere> ::=  WHERE <expre>

<l_columnas> ::= { <expre> } COMA <expre>

<list_owner> ::= ID
        | CURRENT_USER
        | SESSION_USER

<lquery> ::= {<query>} relaciones query

<relaciones> ::= UNION [ ALL ]
        | INTERSECT [ ALL ] 
        | EXCEPT [ ALL ] 

<query> ::= SELECT <dist> <lcol> [ FROM <lcol> [ <instructionWhere> [ <lrows> ] 
				| <linners>  [<instructionWhere> [ <lrows> ] ] 
				| <lrows> ] ]


<lcase> ::= { <case> } <case>

<case> ::= WHEN <expre> THEN <expre>
    | ELSE <expre>

<lrows> ::= { <rows> } <rows>

<rows> ::= ORDER BY <lista_order>
    | GROUP BY <l_expresiones>
    | HAVING <lcol>
    | LIMIT <l_expresiones> [OFFSET expre]
    

<dist> ::= DISTINCT
        | 

<lista_order> ::= { <order_op> } COMA <order_op>
        

<order_op> ::= <expre> [ DESC | ASC | NULLS FIRST | NULLS LAST ]
        

<linners> ::= {<inners>} <inners>

<inners> ::= [ INNER | LEFT | RIGHT | FULL OUTER ] JOIN expre ON expre

<expre> ::= <expre> OR <expre>
        | <expre> AND <expre>
        | NOT <expre>
        | <expre> IGUAL <expre>
        | <expre> MAYORQ <expre>
        | <expre> MENORQ <expre>
        | <expre> MAYOR_IGUALQ <expre>
        | <expre> MENOR_IGUALQ <expre>
        | <expre> DISTINTO <expre>
        | <expre> MAS <expre>
        | <expre> MENOS <expre>
        | <expre> POR <expre>
        | <expre> EXPONENCIACION <expre>
        | <expre> MODULO <expre>
        | <expre> LIKE <expre>
        | <expre> NOT LIKE <expre>
        | <expre> BETWEEN <expresion> AND <expresion>
        | <expre> NOT BETWEEN <expresion> AND <expresion>
        | <expre> IN PARIZQ <lcol> PARDER
        | <expre> IS NULL
        | <expre> IS NOT NULL
        | <expre> IS DISTINCT FROM <expre>
        | <expre> IS NOT DISTINCT FROM <expre>
        | MIN PARIZQ <expre> PARDER
        | MAX PARIZQ <expre> PARDER
        | SUM PARIZQ <expre> PARDER
        | AVG PARIZQ <expre> PARDER
        | COUNT PARIZQ <expre> PARDER
        | TOP PARIZQ <expre> PARDER
        | ABS PARIZQ <expre> PARDER 
        | CBRT PARIZQ <expre> PARDER 
        | CEIL PARIZQ <expre> PARDER 
        | CEILING PARIZQ <expre> PARDER 
        | DEGREES PARIZQ <expre> PARDER 
        | DIV PARIZQ <expre> PARDER
        | EXP PARIZQ <expre> PARDER 
        | FACTORIAL PARIZQ <expre> PARDER 
        | FLOOR PARIZQ <expre> PARDER 
        | GCD PARIZQ <expre> PARDER
        | LCM PARIZQ <expre> PARDER 
        | LN PARIZQ <expre> PARDER 
        | LOG PARIZQ <expre> PARDER 
        | LOG10 PARIZQ <expre> PARDER 
        | MIN_SCALE PARIZQ <expre> PARDER
        | MOD PARIZQ <expre> PARDER 
        | PI PARIZQ <expre> PARDER 
        | POWER PARIZQ <expre> PARDER 
        | RADIANS PARIZQ <expre> PARDER 
        | ROUND PARIZQ <expre> PARDER 
        | SCALE PARIZQ <expre> PARDER 
        | SIGN PARIZQ <expre> PARDER
        | SQRT PARIZQ <expre> PARDER 
        | TRIM_SCALE PARIZQ <expre> PARDER 
        | TRUNC PARIZQ <expre> PARDER 
        | WIDTH_BUCKET PARIZQ <expre> PARDER 
        | RANDOM PARIZQ <expre> PARDER 
        | SETSEED PARIZQ <expre> PARDER
        | LENGTH PARIZQ <expre> PARDER
        | SUBSTRING PARIZQ <lcol> PARDER
        | TRIM PARIZQ <expre> PARDER
        | GET_BYTE PARIZQ <lcol> PARDER
        | MD5 PARIZQ <lcol> PARDER
        | SET_BYTE PARIZQ <lcol> PARDER
        | SHA256 PARIZQ <lcol> PARDER
        | SUBSTR PARIZQ <lcol> PARDER
        | CONVERT PARIZQ <lcol> PARDER
        | ENCODE PARIZQ <expre> PARDER
        | DECODE PARIZQ <expre> PARDER
        | ACOS PARIZQ <expre> PARDER
        | ACOSD PARIZQ <expre> PARDER
        | ASIND PARIZQ <expre> PARDER
        | ATAN PARIZQ <expre> PARDER
        | ATAND PARIZQ <expre> PARDER
        | ATAN2 PARIZQ <expre> PARDER
        | ATAN2D PARIZQ <expre> PARDER
        | COS PARIZQ <expre> PARDER
        | COSD PARIZQ <expre> PARDER
        | COT PARIZQ <expre> PARDER
        | COTD PARIZQ <expre> PARDER
        | SIN PARIZQ <expre> PARDER
        | SIND PARIZQ <expre> PARDER
        | TAN PARIZQ <expre> PARDER
        | TAND PARIZQ <expre> PARDER
        | SINH PARIZQ <expre> PARDER
        | COSH PARIZQ <expre> PARDER
        | TANH PARIZQ <expre> PARDER
        | ASINH PARIZQ <expre> PARDER
        | ACOSH PARIZQ <expre> PARDER
        | ATANH PARIZQ <expre> PARDER
        | LEAST PARIZQ <lcol> PARDER
        | GREATEST PARIZQ <lcol> PARDER
        | EXTRACT PARIZQ <tiempo> FROM TIMESTAMP CARACTER PARDER
        | NOW PARIZQ PARDER
        | DATE_PART PARIZQ CARACTER COMA INTERVAL CARACTER PARDER
        | CURRENT_DATE
        | CURRENT_TIME
        | TIMESTAMP CARACTER
        | POR
        | CASE <lcase> END 
        | PARIZQ <expre> PARDER
        | PARIZQ <query> PARDER

<tiempo> ::=  YEAR
        | MONTH
        | DAY
        | HOUR
        | MINUTE
        | SECOND

<expre> ::=  <expresion>

<expresion> ::= CADENA
        | CARACTER
        | ENTERO
        | FDECIMAL
        | DOUBLE
        | ID [ PUNTO ID | PARIZQ <lcol> PARDER ]
        | ARROBA ID
        

<campos> ::= <campos> COMA ID <tipo> [<lista_op>]
        | <campos> COMA [ CONSTRAINT ID ] CHECK <expre>
        | <campos> COMA UNIQUE PARIZQ <lista_id> PARDER
        | <campos> COMA FOREIGN KEY PARIZQ <lista_id> PARDER REFERENCES ID PARIZQ <lista_id> PARDER
        | <campos> COMA PRIMARY KEY PARIZQ <lista_id> PARDER
        | ID tipo [ <lista_op> ]

<lista_id> ::= { ID } COMA ID

<lista_op> ::= { <opcion> } <opcion>

<opcion> ::= PRIMARY KEY
        | REFERENCES ID
        | DEFAULT <expresion>
        | [ NOT ] NULL
        | UNIQUE
        | CONSTRAINT ID UNIQUE
        | CONSTRAINT ID CHECK <expre>
        | CHECK <expre>

<l_expresiones> ::= { <expresion> } COMA <expresion>


<lcol> ::=  <lcol> COMA <expre> [ [AS] ID]
    | <expre> [ [ AS ] ID ]

<tipo> ::= INT
    | DATE
    | ID PARIZQ ID PARDER
    | VARCHAR PARIZQ ENTERO PARDER
    | CHAR PARIZQ ENTERO PARDER
    | CHARACTER VARYING PARIZQ ENTERO PARDER
    | CHARACTER PARIZQ ENTERO PARDER
    | TEXT
    | DECIMAL [ PARIZQ ENTERO COMA ENTERO PARDER ]
    | DOUBLE
    | ENTERO
    | FLOAT PARIZQ ENTERO COMA ENTERO PARDER
    | SMALLINT
    | INTEGER
    | BIGINT
    | NUMERIC
    | REAL
    | DOUBLE PRECISION
    | MONEY
    | BOOLEAN
    | TIMESTAMP
    | TIME
    | INTERVAL

~~~