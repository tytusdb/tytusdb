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
