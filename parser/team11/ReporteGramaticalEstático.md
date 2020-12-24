# Reporte Gramatical TytusDB.
<p align="center">
  <img src="img/tytus.png" width="100" alt="Presentación">
</p>

        Universidad de San Carlos de Guatemala
        Facultad de ingeniería
        Escuela de Ciencias y Sistemas 
        781 Organización de lenguajes y compiladores 2
        Reporte gramatical proyecto 1

                                                   Perteneciente a: Grupo 11
                                                                

***
## Índice
- [Elementos léxicos](#elementos-lexicos)
    - [Palabras reservadas](#Palabras-reservadas)
    - [Tokens](#Tokens)
- [Analizador Sintáctico](#analizador-sintáctico)
    - [Precedencia de operadores](#Precedencia-de-operadores)
    - [Grámatica Ascendente](#Grámatica-Ascendente)
        - [Definiciones](#Definiciones)
        - [Queries](#Queries)
    - [Grámatica Descendente](#Grámatica-Descendente)

***
### Elementos léxicos
Un elemento léxico (o unidad léxica ) es una sola palabra, una parte de una palabra o una cadena de palabras que forma los elementos básicos del léxico de un idioma Elemento léxico 

[Regresar a Índice](#Índice)
#### *Palabras reservadas*
En los lenguajes informáticos, una palabra reservada es una palabra que tiene un significado gramatical especial para ese lenguaje y no puede ser utilizada como un identificador de objetos en códigos del mismo, como pueden ser las variables.

Por ejemplo, en SQL, un usuario no puede ser llamado "group", porque la palabra group es usada para indicar que un identificador se refiere a un grupo, no a un usuario. Al tratarse de una palabra clave su uso queda restringido.

    <palabras reservadas> ::= 
                SMALLINT
                |INTEGER
                |BIGINT
                |NUMERIC 
                |REAL
                |DOUBLE
                |PRECISION
                |MONEY
                |CHARACTER
                |VARYING
                |VARCHAR
                |CHAR
                |TEXT
                |DATE
                |TIME
                |TIMESTRAMP
                |FLOAT
                |INT
                |INHERITS
                |BOOLEAN
                |CREATE
                |OR
                |REPLACE
                |DATABASE
                |IF
                |NOT
                |EXISTS
                |OWNER
                |SHOW
                |LIKE
                |REGEX
                |ALTER
                |RENAME
                |TO
                |CURRENT_USER
                |SESSION_USER
                |DROP
                |TABLE
                |DEFAULT
                |NULL
                |UNIQUE
                |AND
                |CONSTRAINT
                |CHECK
                |PRIMARY
                |KEY
                |REFERENCES
                |FOREIGN
                |ADD
                |COLUMN
                |INSERT
                |INTO
                |VALUES
                |UPDATE
                |SET
                |WHERE
                |DELETE
                |FROM
                |TRUNCATE
                |CASCADE
                |YEAR
                |MONTH
                |DAY
                |MINUTE
                |SECOND
                |ENUM
                |TYPE
                |INTERVAL
                |ZONE
                |DATABASES
                |WITHOUT
                |WITH
                |HOUR
                |SELECT
                |AS
                |DISTINCT
                |COUNT
                |SUM
                |AVG
                |MAX
                |MIN
                |IN
                |GROUP
                |BY
                |ORDER
                |HAVING
                |ASC
                |DESC
                |NULLS
                |FIRST
                |LAST
                |LIMIT
                |ALL
                |OFFSET
                |ABS
                |CBRT
                |CEIL
                |CEILING
                |DEGREES
                |DIV
                |EXP
                |FACTORIAL
                |FLOOR
                |GCD
                |LN
                |LOG
                |PI
                |MOD
                |POWER
                |RADIANS
                |ROUND
                |ACOS
                |ACOSD
                |ASIN
                |ASIND
                |ATAN
                |ATAND
                |ATAN2
                |ATAN2D
                |COS
                |COSD
                |COT
                |COTD
                |SIN
                |SIND
                |TAN
                |TAND
                |SINH
                |COSH
                |TANH
                |ASINH
                |ACOSH
                |ATANH
                |LENGTH
                |SUBSTRING
                |TRIM
                |GET_BYTE
                |MD5
                |SET_BYTE
                |SHA256
                |SUBSTR
                |CONVERT
                |ENCODE
                |DECODE
                |FOR
                |BETWEEN
                |ISNULL
                |NOTNULL
                |CASE
                |END
                |WHEN
                |ELSE
                |THEN
                |IS
                |SIGN
                |SQRT
                |WBUCKET
                |TRUNC
                |RANDOM
                |TRUE
                |FALSE
                |USE
[Regresar a Índice](#Índice)

#### *Tokens*
El token también llamado componente léxico es una cadena de caracteres que tiene un significado coherente en cierto lenguaje de programación.

    <tokens> ::=  <punto>
                | <dos puntos>
                | <coma>
                | <punto y coma>
                | <llave izquierda>
                | <llave derecha>
                | <parentesis izquierdo>
                | <parentesis derecho>
                | <corchete izquierdo>
                | <corchete derecho>
                | <signo igual>
                | <signo mas>
                | <signo menos>
                | <asterisco>
                | <sigo de division>
                | <signo de exponente>
                | <mayor que>
                | <menor que>
                | <mayor igual que>
                | <menor igual que>
                | <diferente> 
                | <modulo>
                | <comilla simple>
                | <barra vertical>
                | <decimal>
                | <entero>
                | <id>
                | <cadena doble>
                | <cadena like>
                | <cadena simple>
                | <comentario multilinea>
                | <comentario simple>
                | <nueva linea>

    <punto> ::= .

    <dos puntos> ::= :

    <coma> ::= ,

    <punto y coma> ::= ;

    <llave izquierda> ::= {

    <llave derecha> ::= }

    <parentesis izquierdo> ::= (

    <parentesis derecho> ::= )

    <corchete izquierdo> ::= [
    
    <corchete derecho> ::= ]
    
    <signo igual> ::= =
    
    <signo mas> ::= +
    
    <signo menos> ::= -
    
    <asterisco> ::= *
    
    <sigo de division> ::= /
    
    <signo de exponente> ::= ^
    
    <mayor que> ::= >
    
    <menor que> ::= <

    <mayor igual que> ::= >=
    
    <menor igual que> ::= <=
    
    <diferente> ::= <>
    
    <modulo> ::= %

    <comilla simple> ::= '
    
    <barra vertical> ::= |

    <decimal> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | .

    <entero> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

    <id> ::=
		 A | B | C | D | E | F | G | H | I | J | K | L | M | 
         N | O | P | Q | R | S | T | U | V | W | X | Y | Z | 
         a | b | c | d | e | f | g | h | i | j | k | l | m |
         n | o | p | q | r | s | t | u | v | w | x | y | z | 
         0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | _


    <cadena doble> ::= 
         A | B | C | D | E | F | G | H | I | J | K | L | M | 
         N | O | P | Q | R | S | T | U | V | W | X | Y | Z | 
         a | b | c | d | e | f | g | h | i | j | k | l | m |
         n | o | p | q | r | s | t | u | v | w | x | y | z |
         0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | _ | "

    <cadena like>::= 
         A | B | C | D | E | F | G | H | I | J | K | L | M | 
         N | O | P | Q | R | S | T | U | V | W | X | Y | Z | 
         a | b | c | d | e | f | g | h | i | j | k | l | m |
         n | o | p | q | r | s | t | u | v | w | x | y | z |
         0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | _ | " | % 

    <cadena simple>::= 
         A | B | C | D | E | F | G | H | I | J | K | L | M | 
         N | O | P | Q | R | S | T | U | V | W | X | Y | Z | 
         a | b | c | d | e | f | g | h | i | j | k | l | m |
         n | o | p | q | r | s | t | u | v | w | x | y | z |
         0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | _ | '
    
    <comentario multilinea> ::= 
         A | B | C | D | E | F | G | H | I | J | K | L | M | 
         N | O | P | Q | R | S | T | U | V | W | X | Y | Z | 
         a | b | c | d | e | f | g | h | i | j | k | l | m |
         n | o | p | q | r | s | t | u | v | w | x | y | z |
         0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | _ | / | *

    <comentario simple>::= 
         A | B | C | D | E | F | G | H | I | J | K | L | M | 
         N | O | P | Q | R | S | T | U | V | W | X | Y | Z | 
         a | b | c | d | e | f | g | h | i | j | k | l | m |
         n | o | p | q | r | s | t | u | v | w | x | y | z |
         0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | _ | -

[Regresar a Índice](#Índice)
***
### Analizador Sintáctico 
El parser (analizador sintáctico) utiliza los primeros componentes de los tokens producidos por el analizador de léxico para crear una representación intermedia en forma de árbol que describa la estructura gramatical
del flujo de tokens.

[Regresar a Índice](#Índice)

***

#### Precedencia de operadores
Considere la expresión 9 + 5 * 2. Hay dos posibles interpretaciones de esta expresión: (9 + 5) * 2 o 9 + ( 5 * 2). Las reglas de asociatividad para + y * se aplican a las ocurrencias del mismo operador, por lo que no resuelven esta ambigüedad. Las reglas que definen la precedencia relativa de
los operadores son necesarias cuando hay más de un tipo de operador presente.

Decimos que * tiene mayor precedencia que +, si * recibe sus operandos antes que +. En la aritmética ordinaria, la multiplicación y la división tienen mayor precedencia que la suma y la resta. Por lo tanto, * recibe el 5 tanto en 9 + 5 * 2 como en 9 * 5 + 2; es decir, las expresiones son
equivalentes a 9+(5 * 2) y (9 * 5)+2, respectivamente.
<table>
    <thead>
        <tr>
            <th>Nivel</th>
            <th>Asociativa por la</th>
            <th>Palabra reservada</th>
            <th>Símbolo</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>11</td>
            <td>Izquierda</td>
            <td>DIVIDIDO</td>
            <td>/</td>  
        </tr>
        <tr>
            <td>1</td>
            <td>Izquierda</td>
            <td>CONCAT</td>
            <td>||</td>                
        </tr>
        <tr>
            <td>2</td>
            <td>Izquierda</td>
            <td>MENQUE</td>
            <td><</td>  
        </tr>
        <tr>
            <td>3</td>
            <td>Izquierda</td>
            <td>MAYQUE</td>
            <td>></td>  
        </tr>
        <tr>
            <td>4</td>
            <td>Izquierda</td>
            <td>MENIGUAL</td>
            <td><=</td>  
        </tr>
        <tr>
            <td>5</td>
            <td>Izquierda</td>
            <td>MAYIGUAL</td>
            <td>>=</td>  
        </tr>
        <tr>
            <td>6</td>
            <td>Izquierda</td>
            <td>IGUAL</td>
            <td>=</td>  
        </tr>
        <tr>
            <td>7</td>
            <td>Izquierda</td>
            <td>MAYQUE</td>
            <td><></td>  
        </tr>
        <tr>
            <td>8</td>
            <td>Izquierda</td>
            <td>MAS</td>
            <td>+</td>  
        </tr>
        <tr>
            <td>9</td>
            <td>Izquierda</td>
            <td>MENOS</td>
            <td>-</td>  
        </tr>
        <tr>
            <td>10</td>
            <td>Izquierda</td>
            <td>ASTERISCO</td>
            <td>*</td>  
        </tr>
        <tr>
            <td>11</td>
            <td>Izquierda</td>
            <td>DIVIDIDO</td>
            <td>/</td>  
        </tr>
        <tr>
            <td>12</td>
            <td>Izquierda</td>
            <td>MODULO</td>
            <td>%</td>  
        </tr>
        <tr>
            <td>13</td>
            <td>Izquierda</td>
            <td>EXPONENTE</td>
            <td>^</td>  
        </tr>
        <tr>
            <td>14</td>
            <td>Izquierda</td>
            <td>UMENOS</td>
            <td>-</td>  
        </tr>
    </tbody>
</table>

[Regresar a Índice](#Índice)


#### Grámatica Ascendente
El objetivo de un análisis ascendente consiste en construir el árbol sintáctico desde abajo hacia arriba, esto es, desde los tokens hacia el axioma inicial, lo cual disminuye el número de reglas mal aplicadas con respecto al caso descendente (si hablamos del caso con retroceso) o amplía el número de gramáticas susceptibles de ser analizadas (si hablamos del caso LL(1)).
##### Definiciones
###### *Inicio*
    <init> ::= <instrucciones>

    <instrucciones> ::= <instrucciones> <instruccion>
                    | <instruccion>

    <instruccion>   ::= <createDB_instr>
                    | <replaceDB_instr>
                    | <alterDB_instr>
                    | <dropDB_instr>
                    | <showDB_instr>
                    | <insert_instr>
                    | <update_instr>
                    | <alter_instr> PTCOMA
                    | <delete_instr>
                    | <truncate_instr>
                    | <create_instr>
                    | <select_instr>
                    | <use_instr>

###### *Database*
Una base de datos es un conjunto de datos pertenecientes a un mismo contexto y almacenados sistemáticamente para su posterior uso. En este sentido; una biblioteca puede considerarse una base de datos compuesta en su mayoría por documentos y textos impresos en papel e indexados para su consulta. Actualmente, y debido al desarrollo tecnológico de campos como la informática y la electrónica, la mayoría de las bases de datos están en formato digital, siendo este un componente electrónico, por tanto se ha desarrollado y se ofrece un amplio rango de soluciones al problema del almacenamiento de datos.

    <createDB_instr>    ::= CREATE DATABASE <existencia>
                        | CREATE DATABASE ID <state_owner>

    <replaceDB_instr>   ::= REPLACE DATABASE <existencia>
                        | REPLACE DATABASE ID <state_owner>
    
    <existencia>        ::= IF NOT EXISTS ID <state_owner>

    <state_owner>       ::= OWNER IGUAL ID <state_mode>
                        | OWNER IGUAL CADENASIMPLE <state_mode>
                        | OWNER ID <state_mode>
                        | OWNER CADENASIMPLE <state_mode>
                        | <state_mode>
    
    <state_mode>        ::= MODE IGUAL ENTERO PTCOMA
                        | MODE ENTERO PTCOMA
                        | PTCOMA

    <alterDB_instr>     ::= ALTER DATABASE ID RENAME TO ID PTCOMA
                        | ALTER DATABASE ID OWNER TO <owner_users> PTCOMA

    <owner_users>       ::= ID
                        | CURRENT_USER
                        | SESSION_USER

    <dropDB_instr>      ::= DROP DATABASE ID PTCOMA
                        | DROP DATABASE IF EXISTS ID PTCOMA
    
    <showDB_instr>      ::= SHOW DATABASES PTCOMA
                        | SHOW DATABASES LIKE regexpr PTCOMA
    
    <regexpr>           ::=  MODULO ID
                        | MODULO ID MODULO
                        | MODULO ENTERO
                        | MODULO ENTERO MODULO
                        | ID MODULO
                        | ENTERO MODULO

    <use_instr>         ::=  USE DATABASE ID PTCOMA

###### *Insert*
Esta instrucción es utilizada para insertar nuevos datos en una tabla.

    <insert_instr>      ::= INSERT INTO ID VALUES PARIZQ <parametros> PARDER PTCOMA
                        | INSERT INTO ID PARIZQ <columnas> PARDER VALUES PARIZQ <parametros> PARDER PTCOMA

    <parametros>        ::=  <parametros> COMA <parametroinsert>
                        | <parametroinsert>

    <parametroinsert>   ::= DEFAULT
                        | <expresion>

    <columnas>          ::= <columnas> COMA ID
                        | ID
    
###### *Update*
Esta instrucción es utilizada para modificar los datos ya existentes en una tabla.

    <update_instr>      ::= UPDATE ID SET <asignaciones> PTCOMA
                        | UPDATE ID SET <asignaciones> WHERE <condiciones> PTCOMA

    <asignaciones>      ::= <asignaciones> COMA <asignacion>
                        | <asignacion>

    <asignacion>        ::= ID IGUAL <expresion>

###### *Delete*
Esta instruccion es usada para eliminar los datos ya existentes en una tabla.

    <delete_instr>      ::= DELETE FROM ID PTCOMA
                        | DELETE FROM ID WHERE <condiciones> PTCOMA

###### *Truncate*
    <truncate_instr>    ::= TRUNCATE <listtablas> PTCOMA
                        | TRUNCATE <listtablas> CASCADE PTCOMA
                        | TRUNCATE TABLE <listtablas> PTCOMA  
                        | TRUNCATE TABLE <listtablas> CASCADE PTCOMA

    <listtablas>        ::= <listtablas> COMA ID
                        | ID
###### *Alter*
Esta instruccion es usada para agregar, eliminar o modificar columnas en una tabla existente.

    <alter_instr>       ::= ALTER TABLE ID ADD COLUMN <list_columns>
                        | ALTER TABLE ID ADD CHECK PARIZQ <condicion> PARDER
                        | ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ ID PARDER
                        | ALTER TABLE ID ADD FOREIGN KEY PARIZQ ID PARDER REFERENCES ID
                        | ALTER TABLE ID ALTER COLUMN ID SET NOT NULL
                        | ALTER TABLE ID DROP CONSTRAINT ID
                        | ALTER TABLE ID RENAME COLUMN ID TO ID
                        | ALTER TABLE ID DROP COLUMN <listtablas>
                        | ALTER TABLE ID <list_alter_column>

    <list_alter_column> ::= <list_alter_column> COMA ALTER COLUMN ID TYPE <type_column>
                        | ALTER COLUMN ID TYPE <type_column>

    <list_columns>      ::= <list_columns> COMA ID <type_column>
                        | ID <type_column>

    <type_column>       ::= SMALLINT
                        | INTEGER
                        | BIGINT
                        | <decimal>
                        | NUMERIC
                        | REAL
                        | FLOAT
                        | INT
                        | DOUBLE
                        | MONEY
                        | VARCHAR PARIZQ ENTERO PARDER
                        | CHARACTER VARYING PARIZQ ENTERO PARDER
                        | CHARACTER PARIZQ ENTERO PARDER
                        | CHAR PARIZQ ENTERO PARDER
                        | TEXT
                        | TIMESTAMP 
                        | TIMESTAMP PARIZQ ENTERO PARDER
                        | DATE
                        | TIME
                        | TIME PARIZQ ENTERO PARDER
                        | INTERVAL <field>

    <field>             ::= YEAR
                        | MONTH
                        | DAY
                        | HOUR
                        | MINUTE
                        | SECOND
###### *Create*
Esta instrucción es usada para crear una nueva tabla en la base de datos.   

    <create_instr>      ::= CREATE <lista_crear> <create_final>

    <create_final>      ::= PTCOMA
                        | INHERITS PARIZQ ID PARDER PTCOMA

    <lista_crear>       ::= DATABASE <lista_owner>
                        | OR REPLACE DATABASE <lista_owner>
                        | TABLE ID PARIZQ <lista_campos> PARDER 

    <lista_campos>      ::= <lista_campos> COMA <campo>
                        | <campo>
                    
    <campo>             ::=  ID <type_column>
                        | ID <type_column> PRIMARY KEY
                        | PRIMARY KEY PARIZQ <columnas> PARDER 
                        | FOREIGN KEY PARIZQ <columnas> PARDER REFERENCES ID PARIZQ <columnas> PARDER

    <lista_owner>       ::= IF NOT EXISTS ID
                        | ID

***
##### Queries
Una consulta o query de una base de datos, es un lenguaje estándar que permite traer datos de una o más tablas, actualizar contenido o eliminarlos, de una manera rápida y poderosa; conocido generalmente como lenguaje SQL. 

###### Select

    <select_instr>      ::= <select_instr1> PTCOMA

    <select_instr1>     ::= SELECT <termdistinct> <selectlist> <selectfrom>

    <selectfrom>        ::= FROM <listatablasselect> <whereselect> <groupby> <orderby>
                        | <empty>

    <termdistinct>      ::= DISTINCT
                        | <empty>

    <selectlist>        ::= ASTERISCO
                        | <listaselect>

    <listaselect>       ::= listaselect COMA valselect
                        | valselect

    <valselect>         ::= ID <alias>
                        | ID PUNTO ASTERISCO
                        | ID PUNTO ID <alias>
                        | <funcion_matematica_ws> <alias>
                        | <funcion_matematica_s> <alias>
                        | <funcion_trigonometrica> <alias>
                        | PARIZQ <select_instr1> PARDER <alias>
                        | <agregacion> PARIZQ <cualquieridentificador> PARDER <alias>
                        | COUNT PARIZQ ASTERISCO PARDER <alias>
                        | COUNT PARIZQ <cualquieridentificador> PARDER <alias>
                        | <func_bin_strings_1> <alias>
                        | <func_bin_strings_2> <alias>
                        | <func_bin_strings_4> <alias>

    <agregacion>        ::= SUM
                        | AVG
                        | MAX
                        | MIN

    <listatablasselect> ::= <listatablasselect> COMA <tablaselect>
                        | <tablaselect>
    
    <tablaselect>       ::= ID <alias>
                        | PARIZQ <select_instr1> PARDER <alias>

    <alias>             ::= ID
                        | CADENASIMPLE
                        | CADENADOBLE
                        | AS ID
                        | AS CADENASIMPLE
                        | AS CADENADOBLE
                        | <empty>

***
###### *Condiciones where*

    <whereselect>       ::= WHERE condicioneswhere
                        | <empty>

    <condicioneswhere>  ::= condicioneswhere OR  condicionwhere
                        | condicioneswhere AND condicionwhere
                        | condicionwhere
    
    <condicionwhere>    ::= <whereexists>
                        | <notwhereexists>
                        | <wherenotin>
                        | <wherein>
                        | <wherenotlike>
                        | <wherelike>
                        | <wheresubstring>
                        | <between_state>
                        | <not_between_state>
                        | <predicates_state>
                        | <is_distinct_state>
                        | <condicion>

    <whereexists>       ::= EXISTS PARIZQ <select_instr1> PARDER

    <notwhereexists>    ::= NOT EXISTS PARIZQ <select_instr1> PARDER

    <wherein>           ::= <cualquiernumero> IN PARIZQ <select_instr1> PARDER
                        | <cadenastodas> IN PARIZQ <select_instr1> PARDER
    
    <wherenotin>        ::= <cualquiernumero> NOT IN PARIZQ <select_instr1> PARDER
                        | <cadenastodas> NOT IN PARIZQ <select_instr1> PARDER

    <wherenotlike>      ::= <cadenastodas> NOT LIKE CADENALIKE

    <wherelike>         ::= <cadenastodas> LIKE CADENALIKE

    <wheresubstring>    ::= SUBSTRING PARIZQ <cadenastodas> COMA ENTERO COMA ENTERO PARDER IGUAL CADENASIMPLE

    <cadenastodas>      ::= cualquiercadena
                        | cualquieridentificador

###### Condiciones Group by, having, order by, limit....

    <groupby>           ::= GROUP BY <listagroupby>
                        | GROUP BY <listagroupby> HAVING <condicioneshaving>
                        | empty

    <listagroupby>      ::= <listagroupby> COMA <valgroupby>
                        | <valgroupby>

    <valgroupby>        ::= <cualquieridentificador>
                        | <cualquiernumero>
    
    <condicioneshaving> ::= <condicioneshaving> OR <condicionhaving>
                        | <condicioneshaving> AND <condicionhaving>
                        | <condicionhaving>

    <condicionhaving>   ::= <expresionhaving> MENQUE <expresionhaving>
                        | <expresionhaving> MAYQUE <expresionhaving>
                        | <expresionhaving> MENIGUAL <expresionhaving>
                        | <expresionhaving> MAYIGUAL <expresionhaving>
                        | <expresionhaving> IGUAL <expresionhaving>
                        | <expresionhaving> DIFERENTE <expresionhaving>

    <expresionhaving>   ::= <cualquiercadena>
                        | <expresionaritmetica>
                        | <condicionhavingagregacion>
                        | <funcion_matematica_ws>

    <condicionhavingagregacion>     ::= <agregacion> PARIZQ <cualquieridentificador> PARDER

    <orderby>           ::= ORDER BY <listarorderby>
                        | ORDER BY <listarorderby> <instrlimit>
                        | <empty>

    <listarorderby>     ::= <listarorderby> COMA <valororderby>
                        | <valororderby>

    <valororderby>      ::= <cualquieridentificador> <ascdesc> <anular>
                        | <cualquiernumero> <ascdesc> <anular>

    <ascdesc>           ::= DESC
                        | ASC
                        | <empty>

    <anular>            ::= NULLS LAST
                        | NULLS FIRST
                        | <empty>

    <instrlimit>        ::= LIMIT ENTERO instroffset
                        | LIMIT ALL instroffset

    <instroffset>       ::= OFFSET ENTERO
                        | empty

    <condiciones>       ::= condiciones AND condicion
                        | condiciones OR condicion
                        | condicion
    
    <condicion>         ::= <expresion> MENQUE <expresion>
                        | <expresion> MAYQUE <expresion>
                        | <expresion> MENIGUAL <expresion>
                        | <expresion> MAYIGUAL <expresion>
                        | <expresion> IGUAL <expresion> 
                        | <expresion> DIFERENTE <expresion>

    <expresion>         ::= <cualquiercadena>
                        | <funcion_matematica_ws>
                        | <expresionaritmetica>
                        | <func_bin_strings_1>
                        | <func_bin_strings_2>
                        | <vallogico>
                        | PARIZQ <select_instr1> PARDER

    <expresionaritmetica>   ::= <expresionaritmetica> MAS <expresionaritmetica> 
                            | <expresionaritmetica> MENOS <expresionaritmetica> 
                            | <expresionaritmetica> ASTERISCO <expresionaritmetica>
                            | <expresionaritmetica> DIVIDIDO <expresionaritmetica> 
                            | <expresionaritmetica> MODULO <expresionaritmetica> 
                            | <expresionaritmetica> EXPONENTE <expresionaritmetica>
                            | MENOS <expresionaritmetica> %prec UMENOS
                            | cualquiernumero
                            | cualquieridentificador
                            | PARIZQ <expresionaritmetica> PARDER

    <cualquiernumero>   ::= ENTERO
                        | DECIMAL

    <cualquiercadena>   ::= CADENASIMPLE
                        | CADENADOBLE

    <cualquieridentificador> ::= ID
                             | ID PUNTO ID
    
    <vallogico>         ::= FALSE
                        | TRUE

    <funcion_matematica_ws> ::= ABS PARIZQ <expresionaritmetica> PARDER
                            | CBRT PARIZQ <expresionaritmetica> PARDER
                            | CEIL PARIZQ <expresionaritmetica> PARDER
                            | CEILING PARIZQ <expresionaritmetica> PARDER

    <funcion_matematica_s>  ::= DEGREES PARIZQ <expresionaritmetica> PARDER
                            | DIV PARIZQ <expresionaritmetica> COMA <expresionaritmetica> PARDER
                            | EXP PARIZQ <expresionaritmetica> PARDER
                            | FACTORIAL PARIZQ <expresionaritmetica> PARDER
                            | FLOOR PARIZQ <expresionaritmetica> PARDER
                            | GCD PARIZQ <expresionaritmetica> COMA <expresionaritmetica> PARDER
                            | LN PARIZQ <expresionaritmetica> PARDER
                            | LOG PARIZQ <expresionaritmetica> PARDER
                            | MOD PARIZQ <expresionaritmetica> COMA <expresionaritmetica> PARDER
                            | PI PARIZQ PARDER
                            | POWER PARIZQ <expresionaritmetica> COMA <expresionaritmetica> PARDER
                            | RADIANS PARIZQ <expresionaritmetica> PARDER
                            | ROUND PARIZQ <expresionaritmetica> PARDER
                            | SIGN PARIZQ <expresionaritmetica> PARDER
                            | SQRT PARIZQ <expresionaritmetica> PARDER
                            | WBUCKET PARIZQ <explist> PARDER
                            | TRUNC PARIZQ <expresionaritmetica> PARDER
                            | RANDOM PARIZQ <expresionaritmetica> PARDER

    <explist>           ::= <expresionaritmetica> COMA <expresionaritmetica> COMA <expresionaritmetica> COMA <expresionaritmetica>

    <funcion_trigonometrica>    ::= ACOS PARIZQ <expresionaritmetica> PARDER
                                | ACOSD PARIZQ <expresionaritmetica> PARDER
                                | ASIN PARIZQ <expresionaritmetica> PARDER
                                | ASIND PARIZQ <expresionaritmetica> PARDER
                                | ATAN PARIZQ <expresionaritmetica> PARDER
                                | ATAND PARIZQ <expresionaritmetica> PARDER
                                | ATAN2 PARIZQ <expresionaritmetica> PARDER
                                | ATAN2D PARIZQ <expresionaritmetica> PARDER
                                | COS PARIZQ <expresionaritmetica> PARDER
                                | COSD PARIZQ <expresionaritmetica> PARDER
                                | COT PARIZQ <expresionaritmetica> PARDER
                                | COTD PARIZQ <expresionaritmetica> PARDER
                                | SIN PARIZQ <expresionaritmetica> PARDER
                                | SIND PARIZQ <expresionaritmetica> PARDER
                                | TAN PARIZQ <expresionaritmetica> PARDER
                                | TAND PARIZQ <expresionaritmetica> PARDER
                                | SINH PARIZQ <expresionaritmetica> PARDER
                                | COSH PARIZQ <expresionaritmetica> PARDER
                                | TANH PARIZQ <expresionaritmetica> PARDER
                                | ASINH PARIZQ <expresionaritmetica> PARDER
                                | ACOSH PARIZQ <expresionaritmetica> PARDER
                                | ATANH PARIZQ <expresionaritmetica> PARDER

    <func_bin_strings_1>    ::=  LENGTH PARIZQ <cadena> PARDER

    <func_bin_strings_2>    ::= SUBSTRING PARIZQ <cadena> COMA <cualquiernumero> COMA cualquiernumero PARDER 
                            | SUBSTR PARIZQ <cadena> COMA <cualquiernumero> COMA <cualquiernumero> PARDER
                            | TRIM PARIZQ <cadena> PARDER

    <func_bin_strings_3>    ::= MD5 PARIZQ <cadena> PARDER

    <func_bin_strings_4>    ::=  GET_BYTE PARIZQ <cadena> COMA ENTERO PARDER
                            | SET_BYTE PARIZQ <cadena> COMA ENTERO COMA ENTERO PARDER
                            | SHA256 PARIZQ <cadena> PARDER
                            | CONVERT PARIZQ alias PARDER
                            | ENCODE PARIZQ <cadena> COMA <cadena> PARDER
                            | DECODE PARIZQ <cadena> COMA <cadena> PARDER

    <op_bin_strings>        ::= <op_bin_strings> CONCAT <op_bin_strings>
                            | <op_bin_strings> BITWAND <op_bin_strings>
                            | <op_bin_strings> BITWOR <op_bin_strings>
                            | <op_bin_strings> BITWXOR <op_bin_strings>
                            | <op_bin_strings> BITWNOT <op_bin_strings>
                            | <op_bin_strings> BITWSHIFTL <op_bin_strings>
                            | <op_bin_strings> BITWSHIFTR <op_bin_strings> 
                            | <cadena>

    <cadena>                ::= <cualquiercadena>
                            | <cualquieridentificador>

    <between_state>         ::= <cualquiernumero> BETWEEN <valores> AND <valores>
                            | <cadenastodas> BETWEEN <valores> AND <valores>

    <not_between_state>     ::= <cualquiernumero> NOT BETWEEN <valores> AND <valores>
                            | <cadenastodas> NOT BETWEEN <valores> AND <valores>

    <predicates_state>      ::= <valores> IS NULL
                            | <valores> IS NOT NULL
                            | <valores> ISNULL
                            | <valores> NOTNULL

    <is_distinct_state>     ::=  <valores> IS DISTINCT FROM <valores>
                            | <valores> IS NOT DISTINCT FROM <valores>

    <valores>               ::= <cualquiernumero>
                            | <cualquiercadena>
                            | <cualquieridentificador>

    <empty>                 ::= 
    
#### Grámatica Descendente
El análisis sintáctico descendente (ASD) intenta encontrar entre las producciones de la gramática la derivación por la izquierda del símbolo inicial para una cadena de entrada. Dicho análisis se desarrolla desde la raíz y de izquierda a derecha.
##### Definiciones
###### *Inicio*

    ```
    INIT ::= INSTRUCCIONES

    INSTRUCCIONES ::= INSTRUCCION INSTRUCCIONES'

    INSTRUCCIONES' ::= INSTRUCCION INSTRUCCIONES'
                | Ɛ

    INSTRUCCION ::= createDB_instr
                | replaceDB_instr
                | alterDB_instr
                | dropDB_instr
                | create_table
                | showDB_instr
                | insert_instr
                | update_instr
                | alter_instr PTCOMA
                | CREATEDB ptcoma
                | create_enum  
            | drop_table
            | delete_instr
            | truncate_instr
            | select_instr
            | use_instr

    <createDB_instr>    ::= <createDB_instr> <createDB_instr'>

    <createDB_instr'>    ::= <createDB_instr> <createDB_instr'>
                        | Ɛ
            
    <createDB_instr>    ::= CREATE DATABASE <existencia>
                            | CREATE DATABASE ID <state_owner>

    <replaceDB_instr>    ::= <replaceDB_instr> <replaceDB_instr'>

    <replaceDB_instr'>    ::= <replaceDB_instr> <replaceDB_instr'>
                        | Ɛ
                
        <replaceDB_instr>   ::= REPLACE DATABASE <existencia>
                            | REPLACE DATABASE ID <state_owner>
                

    <existencia>    ::= <existencia> <existencia'>

    <existencia'>    ::= <existencia> <existencia'>
                        | Ɛ
        <existencia>        ::= IF NOT EXISTS ID <state_owner>
        
        
    <state_owner>    ::= <state_owner> <state_owner'>

    <state_owner'>    ::= <state_owner> <state_owner'>
                        | Ɛ
                
        <state_owner>       ::= OWNER IGUAL ID <state_mode>
                            | OWNER IGUAL CADENASIMPLE <state_mode>
                            | OWNER ID <state_mode>
                            | OWNER CADENASIMPLE <state_mode>
                            | <state_mode>
        
        <state_mode>    ::= <state_mode> <state_mode'>

    <state_mode'>    ::= <state_mode> <state_mode'>
                        | Ɛ
                
        <state_mode>        ::= MODE IGUAL ENTERO PTCOMA
                            | MODE ENTERO PTCOMA
                            | PTCOMA

    <alterDB_instr>    ::= <alterDB_instr> <alterDB_instr'>

    <alterDB_instr'>    ::= <alterDB_instr> <alterDB_instr'>
                        | Ɛ
        <alterDB_instr>     ::= ALTER DATABASE ID RENAME TO ID PTCOMA
                            | ALTER DATABASE ID OWNER TO <owner_users> PTCOMA

    <owner_users>    ::= <owner_users> <owner_users'>

    <owner_users'>    ::= <owner_users> <owner_users'>
                        | Ɛ
        <owner_users>       ::= ID
                            | CURRENT_USER
                            | SESSION_USER
                
    <dropDB_instr>    ::= <dropDB_instr> <dropDB_instr'>

    <dropDB_instr'>    ::= <dropDB_instr> <dropDB_instr'>
                        | Ɛ

        <dropDB_instr>      ::= DROP DATABASE ID PTCOMA
                            | DROP DATABASE IF EXISTS ID PTCOMA
                
    <showDB_instr>    ::= <showDB_instr> <showDB_instr'>

    <showDB_instr'>    ::= <showDB_instr> <showDB_instr'>
                        | Ɛ
        
        <showDB_instr>      ::= SHOW DATABASES PTCOMA
                            | SHOW DATABASES LIKE regexpr PTCOMA
                
    <regexpr>    ::= <regexpr> <regexpr'>

    <regexpr'>    ::= <regexpr> <regexpr'>
                        | Ɛ		
        
        <regexpr>           ::=  MODULO ID
                            | MODULO ID MODULO
                            | MODULO ENTERO
                            | MODULO ENTERO MODULO
                            | ID MODULO
                            | ENTERO MODULO

    <use_instr>    ::= <use_instr> <use_instr'>

    <use_instr'>    ::= <use_instr> <use_instr'>
                        | Ɛ	
        <use_instr>         ::=  USE DATABASE ID PTCOMA

###### *Insert*
Esta instrucción es utilizada para insertar nuevos datos en una tabla.

    <insert_instr>    ::= <insert_instr> <insert_instr'>

    <insert_instr'>    ::= <insert_instr> <insert_instr'>
                        | Ɛ	
                
        <insert_instr>      ::= INSERT INTO ID VALUES PARIZQ <parametros> PARDER PTCOMA
                            | INSERT INTO ID PARIZQ <columnas> PARDER VALUES PARIZQ <parametros> PARDER PTCOMA
                

        <parametros>        ::=  <parametros> <parametros'>
        
        <parametros'>        ::=   COMA <parametros> <parametroinsert>
                            | <parametroinsert>
                | Ɛ

        <parametroinsert>   ::= DEFAULT
                            | <expresion>
        
        <columnas>          ::= <columnas> <columnas'>
        <columnas'>          ::=  COMA <columnas><columnas'>
                            | ID
                | Ɛ
        
###### *Update*
Esta instrucción es utilizada para modificar los datos ya existentes en una tabla.

    <update_instr>    ::= <update_instr> <update_instr'>

    <update_instr'>    ::= <update_instr> <update_instr'>
                        | Ɛ

        <update_instr>      ::= UPDATE ID SET <asignaciones> PTCOMA
                            | UPDATE ID SET <asignaciones> WHERE <condiciones> PTCOMA

        <asignaciones>      ::= <asignacion> <asignaciones'>
        <asignaciones'>      ::=  COMA <asignacion><asignaciones'>
                | Ɛ

        <asignacion>        ::= ID IGUAL <expresion>

    ###### *Delete*
    Esta instruccion es usada para eliminar los datos ya existentes en una tabla.

    <delete_instr>    ::= <delete_instr> <delete_instr'>

    <delete_instr'>    ::= <delete_instr> <delete_instr'>
                        | Ɛ

        <delete_instr>      ::= DELETE FROM ID PTCOMA
                            | DELETE FROM ID WHERE <condiciones> PTCOMA
###### *Truncate*
    <truncate_instr>    ::= <truncate_instr> <truncate_instr'>

    <truncate_instr'>    ::= <truncate_instr> <truncate_instr'>
                        | Ɛ
        <truncate_instr>    ::= TRUNCATE <listtablas> PTCOMA
                            | TRUNCATE <listtablas> CASCADE PTCOMA
                            | TRUNCATE TABLE <listtablas> PTCOMA  
                            | TRUNCATE TABLE <listtablas> CASCADE PTCOMA
        
    <listtablas>        ::= <listtab> <listtablas'>
                            
        <listtablas'>        ::=  COMA <listtab> <listtablas'>
                    | Ɛ
        listtablas>        ::=  ID
    ###### *Alter*
    Esta instruccion es usada para agregar, eliminar o modificar columnas en una tabla existente.

    <alter_instr>    ::= <alter_instr> <alter_instr'>

    <alter_instr'>    ::= <alter_instr> <alter_instr'>
                        | Ɛ
        <alter_instr>       ::= ALTER TABLE ID ADD COLUMN <list_columns>
                            | ALTER TABLE ID ADD CHECK PARIZQ <condicion> PARDER
                            | ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ ID PARDER
                            | ALTER TABLE ID ADD FOREIGN KEY PARIZQ ID PARDER REFERENCES ID
                            | ALTER TABLE ID ALTER COLUMN ID SET NOT NULL
                            | ALTER TABLE ID DROP CONSTRAINT ID
                            | ALTER TABLE ID RENAME COLUMN ID TO ID
                            | ALTER TABLE ID DROP COLUMN <listtablas>
                            | ALTER TABLE ID <list_alter_column>

        <list_alter_column> ::= <list_alter_column> COMA ALTER COLUMN ID TYPE <type_column>
                            | ALTER COLUMN ID TYPE <type_column>

        <list_columns>      ::= <list_columns> COMA ID <type_column>
                            | ID <type_column>

        <type_column>       ::= SMALLINT
                            | INTEGER
                            | BIGINT
                            | <decimal>
                            | NUMERIC
                            | REAL
                            | FLOAT
                            | INT
                            | DOUBLE
                            | MONEY
                            | VARCHAR PARIZQ ENTERO PARDER
                            | CHARACTER VARYING PARIZQ ENTERO PARDER
                            | CHARACTER PARIZQ ENTERO PARDER
                            | CHAR PARIZQ ENTERO PARDER
                            | TEXT
                            | TIMESTAMP 
                            | TIMESTAMP PARIZQ ENTERO PARDER
                            | DATE
                            | TIME
                            | TIME PARIZQ ENTERO PARDER
                            | INTERVAL <field>

        <field>             ::= YEAR
                            | MONTH
                            | DAY
                            | HOUR
                            | MINUTE
                            | SECOND
###### *Create*
Esta instrucción es usada para crear una nueva tabla en la base de datos.  

    <create_instr>    ::= <create_instr> <create_instr'>

    <create_instr'>    ::= <create_instr> <create_instr'>
                        | Ɛ

        <create_instr>      ::= CREATE <lista_crear> <create_final>
        
        <create_final>    ::= <create_final> <create_final'>

        <create_final'>    ::= <create_final> <create_final'>
                        | Ɛ

        <create_final>      ::= PTCOMA
                            | INHERITS PARIZQ ID PARDER PTCOMA

        <lista_crear>       ::= DATABASE <lista_owner>
                            | OR REPLACE DATABASE <lista_owner>
                            | TABLE ID PARIZQ <lista_campos> PARDER 

        <lista_campos>      ::= <lista_campos> COMA <campo>
                            | <campo>
                        
        <campo>             ::=  ID <type_column>
                            | ID <type_column> PRIMARY KEY
                            | PRIMARY KEY PARIZQ <columnas> PARDER 
                            | FOREIGN KEY PARIZQ <columnas> PARDER REFERENCES ID PARIZQ <columnas> PARDER

        <lista_owner>       ::= IF NOT EXISTS ID
                            | ID

***
##### Queries

Una consulta o query de una base de datos, es un lenguaje estándar que permite traer datos de una o más tablas, actualizar contenido o eliminarlos, de una manera rápida y poderosa; conocido generalmente como lenguaje SQL.

###### Select

    <select_instr>    ::= <select_instr> <select_instr'>

        <select_instr'>    ::= <select_instr> <select_instr'>
                        | Ɛ
        <select_instr>      ::= <select_instr1> PTCOMA

        <select_instr1>     ::= SELECT <termdistinct> <selectlist> <selectfrom>

        <selectfrom>        ::= FROM <listatablasselect> <whereselect> <groupby> <orderby>
                            | <empty>

        <termdistinct>      ::= DISTINCT
                            | <empty>

        <selectlist>        ::= ASTERISCO
                            | <listaselect>

        <listaselect>       ::= listaselect COMA valselect
                            | valselect

        <valselect>         ::= ID <alias>
                            | ID PUNTO ASTERISCO
                            | ID PUNTO ID <alias>
                            | <funcion_matematica_ws> <alias>
                            | <funcion_matematica_s> <alias>
                            | <funcion_trigonometrica> <alias>
                            | PARIZQ <select_instr1> PARDER <alias>
                            | <agregacion> PARIZQ <cualquieridentificador> PARDER <alias>
                            | COUNT PARIZQ ASTERISCO PARDER <alias>
                            | COUNT PARIZQ <cualquieridentificador> PARDER <alias>
                            | <func_bin_strings_1> <alias>
                            | <func_bin_strings_2> <alias>
                            | <func_bin_strings_4> <alias>

        <agregacion>        ::= SUM
                            | AVG
                            | MAX
                            | MIN

        <listatablasselect> ::= <listatablasselect> COMA <tablaselect>
                            | <tablaselect>
        
        <tablaselect>       ::= ID <alias>
                            | PARIZQ <select_instr1> PARDER <alias>

        <alias>             ::= ID
                            | CADENASIMPLE
                            | CADENADOBLE
                            | AS ID
                            | AS CADENASIMPLE
                            | AS CADENADOBLE
                            | <empty>

    ***
###### *Condiciones where*

        <whereselect>       ::= WHERE condicioneswhere
                            | <empty>

        <condicioneswhere>  ::= condicioneswhere OR  condicionwhere
                            | condicioneswhere AND condicionwhere
                            | condicionwhere
        
        <condicionwhere>    ::= <whereexists>
                            | <notwhereexists>
                            | <wherenotin>
                            | <wherein>
                            | <wherenotlike>
                            | <wherelike>
                            | <wheresubstring>
                            | <between_state>
                            | <not_between_state>
                            | <predicates_state>
                            | <is_distinct_state>
                            | <condicion>

        <whereexists>       ::= EXISTS PARIZQ <select_instr1> PARDER

        <notwhereexists>    ::= NOT EXISTS PARIZQ <select_instr1> PARDER

        <wherein>           ::= <cualquiernumero> IN PARIZQ <select_instr1> PARDER
                            | <cadenastodas> IN PARIZQ <select_instr1> PARDER
        
        <wherenotin>        ::= <cualquiernumero> NOT IN PARIZQ <select_instr1> PARDER
                            | <cadenastodas> NOT IN PARIZQ <select_instr1> PARDER

        <wherenotlike>      ::= <cadenastodas> NOT LIKE CADENALIKE

        <wherelike>         ::= <cadenastodas> LIKE CADENALIKE

        <wheresubstring>    ::= SUBSTRING PARIZQ <cadenastodas> COMA ENTERO COMA ENTERO PARDER IGUAL CADENASIMPLE

        <cadenastodas>      ::= cualquiercadena
                            | cualquieridentificador

###### Condiciones Group by, having, order by, limit....

        <groupby>           ::= GROUP BY <listagroupby>
                            | GROUP BY <listagroupby> HAVING <condicioneshaving>
                            | empty

        <listagroupby>      ::= <listagroupby> COMA <valgroupby>
                            | <valgroupby>

        <valgroupby>        ::= <cualquieridentificador>
                            | <cualquiernumero>
        
        <condicioneshaving> ::= <condicioneshaving> OR <condicionhaving>
                            | <condicioneshaving> AND <condicionhaving>
                            | <condicionhaving>

        <condicionhaving>   ::= <expresionhaving> MENQUE <expresionhaving>
                            | <expresionhaving> MAYQUE <expresionhaving>
                            | <expresionhaving> MENIGUAL <expresionhaving>
                            | <expresionhaving> MAYIGUAL <expresionhaving>
                            | <expresionhaving> IGUAL <expresionhaving>
                            | <expresionhaving> DIFERENTE <expresionhaving>

        <expresionhaving>   ::= <cualquiercadena>
                            | <expresionaritmetica>
                            | <condicionhavingagregacion>
                            | <funcion_matematica_ws>

        <condicionhavingagregacion>     ::= <agregacion> PARIZQ <cualquieridentificador> PARDER

        <orderby>           ::= ORDER BY <listarorderby>
                            | ORDER BY <listarorderby> <instrlimit>
                            | <empty>

        <listarorderby>     ::= <listarorderby> COMA <valororderby>
                            | <valororderby>

        <valororderby>      ::= <cualquieridentificador> <ascdesc> <anular>
                            | <cualquiernumero> <ascdesc> <anular>

        <ascdesc>           ::= DESC
                            | ASC
                            | <empty>

        <anular>            ::= NULLS LAST
                            | NULLS FIRST
                            | <empty>

        <instrlimit>        ::= LIMIT ENTERO instroffset
                            | LIMIT ALL instroffset

        <instroffset>       ::= OFFSET ENTERO
                            | empty

        <condiciones>       ::= condiciones AND condicion
                            | condiciones OR condicion
                            | condicion
        
        <condicion>         ::= <expresion> MENQUE <expresion>
                            | <expresion> MAYQUE <expresion>
                            | <expresion> MENIGUAL <expresion>
                            | <expresion> MAYIGUAL <expresion>
                            | <expresion> IGUAL <expresion> 
                            | <expresion> DIFERENTE <expresion>

        <expresion>         ::= <cualquiercadena>
                            | <funcion_matematica_ws>
                            | <expresionaritmetica>
                            | <func_bin_strings_1>
                            | <func_bin_strings_2>
                            | <vallogico>
                            | PARIZQ <select_instr1> PARDER

        <expresionaritmetica>   ::= <expresionaritmetica> MAS <expresionaritmetica> 
                                | <expresionaritmetica> MENOS <expresionaritmetica> 
                                | <expresionaritmetica> ASTERISCO <expresionaritmetica>
                                | <expresionaritmetica> DIVIDIDO <expresionaritmetica> 
                                | <expresionaritmetica> MODULO <expresionaritmetica> 
                                | <expresionaritmetica> EXPONENTE <expresionaritmetica>
                                | MENOS <expresionaritmetica> %prec UMENOS
                                | cualquiernumero
                                | cualquieridentificador
                                | PARIZQ <expresionaritmetica> PARDER

        <cualquiernumero>   ::= ENTERO
                            | DECIMAL

        <cualquiercadena>   ::= CADENASIMPLE
                            | CADENADOBLE

        <cualquieridentificador> ::= ID
                                | ID PUNTO ID
        
        <vallogico>         ::= FALSE
                            | TRUE

        <funcion_matematica_ws> ::= ABS PARIZQ <expresionaritmetica> PARDER
                                | CBRT PARIZQ <expresionaritmetica> PARDER
                                | CEIL PARIZQ <expresionaritmetica> PARDER
                                | CEILING PARIZQ <expresionaritmetica> PARDER

        <funcion_matematica_s>  ::= DEGREES PARIZQ <expresionaritmetica> PARDER
                                | DIV PARIZQ <expresionaritmetica> COMA <expresionaritmetica> PARDER
                                | EXP PARIZQ <expresionaritmetica> PARDER
                                | FACTORIAL PARIZQ <expresionaritmetica> PARDER
                                | FLOOR PARIZQ <expresionaritmetica> PARDER
                                | GCD PARIZQ <expresionaritmetica> COMA <expresionaritmetica> PARDER
                                | LN PARIZQ <expresionaritmetica> PARDER
                                | LOG PARIZQ <expresionaritmetica> PARDER
                                | MOD PARIZQ <expresionaritmetica> COMA <expresionaritmetica> PARDER
                                | PI PARIZQ PARDER
                                | POWER PARIZQ <expresionaritmetica> COMA <expresionaritmetica> PARDER
                                | RADIANS PARIZQ <expresionaritmetica> PARDER
                                | ROUND PARIZQ <expresionaritmetica> PARDER
                                | SIGN PARIZQ <expresionaritmetica> PARDER
                                | SQRT PARIZQ <expresionaritmetica> PARDER
                                | WBUCKET PARIZQ <explist> PARDER
                                | TRUNC PARIZQ <expresionaritmetica> PARDER
                                | RANDOM PARIZQ <expresionaritmetica> PARDER

        <explist>           ::= <expresionaritmetica> COMA <expresionaritmetica> COMA <expresionaritmetica> COMA <expresionaritmetica>

        <funcion_trigonometrica>    ::= ACOS PARIZQ <expresionaritmetica> PARDER
                                    | ACOSD PARIZQ <expresionaritmetica> PARDER
                                    | ASIN PARIZQ <expresionaritmetica> PARDER
                                    | ASIND PARIZQ <expresionaritmetica> PARDER
                                    | ATAN PARIZQ <expresionaritmetica> PARDER
                                    | ATAND PARIZQ <expresionaritmetica> PARDER
                                    | ATAN2 PARIZQ <expresionaritmetica> PARDER
                                    | ATAN2D PARIZQ <expresionaritmetica> PARDER
                                    | COS PARIZQ <expresionaritmetica> PARDER
                                    | COSD PARIZQ <expresionaritmetica> PARDER
                                    | COT PARIZQ <expresionaritmetica> PARDER
                                    | COTD PARIZQ <expresionaritmetica> PARDER
                                    | SIN PARIZQ <expresionaritmetica> PARDER
                                    | SIND PARIZQ <expresionaritmetica> PARDER
                                    | TAN PARIZQ <expresionaritmetica> PARDER
                                    | TAND PARIZQ <expresionaritmetica> PARDER
                                    | SINH PARIZQ <expresionaritmetica> PARDER
                                    | COSH PARIZQ <expresionaritmetica> PARDER
                                    | TANH PARIZQ <expresionaritmetica> PARDER
                                    | ASINH PARIZQ <expresionaritmetica> PARDER
                                    | ACOSH PARIZQ <expresionaritmetica> PARDER
                                    | ATANH PARIZQ <expresionaritmetica> PARDER

        <func_bin_strings_1>    ::=  LENGTH PARIZQ <cadena> PARDER

        <func_bin_strings_2>    ::= SUBSTRING PARIZQ <cadena> COMA <cualquiernumero> COMA cualquiernumero PARDER 
                                | SUBSTR PARIZQ <cadena> COMA <cualquiernumero> COMA <cualquiernumero> PARDER
                                | TRIM PARIZQ <cadena> PARDER

        <func_bin_strings_3>    ::= MD5 PARIZQ <cadena> PARDER

        <func_bin_strings_4>    ::=  GET_BYTE PARIZQ <cadena> COMA ENTERO PARDER
                                | SET_BYTE PARIZQ <cadena> COMA ENTERO COMA ENTERO PARDER
                                | SHA256 PARIZQ <cadena> PARDER
                                | CONVERT PARIZQ alias PARDER
                                | ENCODE PARIZQ <cadena> COMA <cadena> PARDER
                                | DECODE PARIZQ <cadena> COMA <cadena> PARDER

        <op_bin_strings>        ::= <op_bin_strings> CONCAT <op_bin_strings>
                                | <op_bin_strings> BITWAND <op_bin_strings>
                                | <op_bin_strings> BITWOR <op_bin_strings>
                                | <op_bin_strings> BITWXOR <op_bin_strings>
                                | <op_bin_strings> BITWNOT <op_bin_strings>
                                | <op_bin_strings> BITWSHIFTL <op_bin_strings>
                                | <op_bin_strings> BITWSHIFTR <op_bin_strings> 
                                | <cadena>

        <cadena>                ::= <cualquiercadena>
                                | <cualquieridentificador>

        <between_state>         ::= <cualquiernumero> BETWEEN <valores> AND <valores>
                                | <cadenastodas> BETWEEN <valores> AND <valores>

        <not_between_state>     ::= <cualquiernumero> NOT BETWEEN <valores> AND <valores>
                                | <cadenastodas> NOT BETWEEN <valores> AND <valores>

        <predicates_state>      ::= <valores> IS NULL
                                | <valores> IS NOT NULL
                                | <valores> ISNULL
                                | <valores> NOTNULL

        <is_distinct_state>     ::=  <valores> IS DISTINCT FROM <valores>
                                | <valores> IS NOT DISTINCT FROM <valores>

        <valores>               ::= <cualquiernumero>
                                | <cualquiercadena>
                                | <cualquieridentificador>
    ```

### Para definir la producción de Expresiones (aritméticas, lógicas, relacionales) se utilizó la siguiente precedencia de operadores

    |Asociatividad|Símbolo|Descripción|
    |:----------:|:-------------:|:---------:|
    |Izquierda|```lsel```|Precedencia utilizada para los alias en la instrucción SELECT|
    |Izquierda|```.```|Operador para separar atributos de una tabla|
    |Derecha|```-,+```|Operador unario para números negativos y positivos|
    |Izquierda|```^```|Potencia|
    |Izquierda|```*,/,%```|Multiplicación, división y modular|
    |Izquierda|```-,+```|Suma y Resta|
    |Izquierda|```>,<,>=,<=,=,!=,<>```|Operaciones relacionales|
    |Izquierda|```predicates```|Precedencia para predicados en consultas|
    |Derecha|```NOT```|Negación lógica|
    |Izquierda|```AND```|Operador AND lógico|
    |Izquierda|```OR```| Operador OR lógico|

    ```
    EXP ::= EXP mas EXP
        | EXP menos EXP
        | EXP multiplicacion  EXP
        | EXP division EXP
        | EXP modulo EXP
        | EXP elevado EXP
        | EXP and EXP
        | EXP or EXP
        | EXP mayor EXP
        | EXP menor EXP
        | EXP mayor_igual EXP
        | EXP menor_igual EXP
        | EXP igual EXP
        | EXP diferente1 EXP
        | EXP diferente2 EXP
        | EXP punto EXP
        | mas EXP %prec umas
        | menos EXP %prec umenos
        | EXP between EXP %prec predicates
        | EXP in para LEXP parc %prec predicates
        | EXP not in para LEXP parc %prec predicates
        | EXP not between EXP %prec predicates
        | EXP  between symetric EXP %prec predicates
        | EXP not between symetric EXP %prec predicates
        | EXP is distinct r_from EXP %prec predicates
        | EXP is not distinct r_from EXP %prec predicates
        | EXP is not null %prec predicates
        | EXP is null %prec predicates
        | EXP isnull %prec predicates
        | EXP notnull %prec predicates
        | EXP  is true %prec predicates
        | EXP is not true %prec predicates
        | EXP is false %prec predicates
        | EXP is not false %prec predicates
        | EXP is unknown %prec predicates
        | EXP is not unknown %prec predicates
        | EXP as cadenaString %prec lsel
        | EXP cadenaString %prec lsel
        | EXP as id %prec lsel
        | EXP id  %prec lsel
        | EXP as cadena %prec lsel
        | EXP cadena %prec lsel
        | multiplicacion %prec lsel
        | not EXP
        | para EXP parc
        | int
        | decimales
        | cadena
        | cadenaString
        | true
        | false
        | id
        | null
        | SELECT
        | id para parc
        | id para LEXP parc
        | extract para FIELDS r_from timestamp cadena parc
        | current_time
        | current_date
        | timestamp cadena 
        | interval cadena
        | CASE
        | cadena like cadena
        | cadena not like cadena
        | any para LEXP parc
        | all para LEXP parc
        | some para LEXP parc
        | default
    ```


[Regresar a Índice](#Índice)
