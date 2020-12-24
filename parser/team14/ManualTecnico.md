#### Universidad de San Carlos de Guatemala
#### Organización de Lenguajes y Compiladores 2 
#### Facultad de Ingeniería
#### Interprete TytusDB

## Introducción
El siguiente manual guiara a los usuarios que harán soporte al sistema, el cual les dará a
conocer los requerimientos y la estructura realizada para la construcción del sistema, en el desarrollo
de programa de escritorio, el cual muestra las herramientas necesarias para la construcción y la funcionalidad
del sistema.

## Objetivo
Informar y especificar al usuario la estructura y conformación del sistema con el fin de que
puedan hacer soporte y modificaciones o actualizaciones al sistema en general.

## Procesos
### Procesos de entrada
- Ingresar al programa de escritorio (acceso)
- Ingresar datos al programa para ejecutar el interprete
- Ingresar datos para para generación de reportes
- Ingresar o modificar información de la base de datos mediante los metodos INSERT, UPDATE, ALTER, DROP, CREATE y DELETE
- Ingresar al programa funciones matematicas, trigonometricas y binarias

### Procesos de salida
- Resultado de consultas a traves del SELECT
- Resultado de funciones matematicas, trigonometricas y binarias
- Reporte de arbol sintactico AST
- Reporte de errores lexicos
- Reporte de errores sintacticos
- Reporte de tabla de simbolos

## Requerimientos del sistema
### Requerimientos de hardware
- Equipo de computo; CPU, Teclado, Mouse y Monitor
- Memoria RAM 2GB o superior
- Procesador 1.4 GHz o superior
### Requerimientos de software
- Sistemas operativos (Windows 7/8/10 o Linux)
- Python 3
- Graphviz
- PLY

## Herramientas utilizadas para el desarrollo
### Python
Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.​ 
Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y,
en menor medida, programación funcional.

### Visual Studio Code
Visual Studio Code es un editor de código fuente desarrollado por Microsoft para Windows, Linux y macOS. 
Incluye soporte para la depuración, control integrado de Git, resaltado de sintaxis, finalización inteligente de código, fragmentos y refactorización de código.

## Analisis Lexico y Sintactico utilizando PLY
### Analisis Lexico
En el interprete tytusDB se implemento un analisis lexico utilizando la herramienta de PLY con las siguientes
consideraciones:
- **Expresiones regulares**
Una expresión regular, o expresión racional, ​​ también son conocidas como regex o regexp, ​ 
por su contracción de las palabras inglesas regular expression, es una secuencia de caracteres que conforma un patrón de búsqueda
```
int ::= digito+
decimales ::= digito+ "." digito+ (["e"] ["+"|"-""] digito+)?
id ::= [a-zA-Z_][a-zA-Z_0-9]*
cadena ::= """ "."*? """
cadenaString ::= "".*?""
```

- **Palabras Reservadas:**
Las palabras reservadas son aquellas que son propias del lenguaje y no pueden ser usadas para
nombrar etiquetas o variables.

| show   | database  | databases | like | select |
| ------ |---------| ---------| ---------| ------:|
| distinct | from  | alter  | rename | to |
| owner  | table    | add   | column | set |
| not | null | check   | constraint | unique |
| foreign | key | or   | replace | if |
| exists | mode | inherits   | primary | references |
| default | type | enum   | drop | update |
| where | smallint | integer   | bigint | decimal |
| double | precision | money   | character | varying |
| char | timestamp | without   | zone | date |
| time | interval | boolean   | true | false |
| year | month | day   | hour | minute |
| second | in | and   | between | symetric |
| isnull | notnull | unknown   | insert | into |
| values | group | by   | having | as |
| create | varchar | text   | is | delete |
| order | asc | desc   | when | case |
| else | then | end   | extract | current_time |
| current_date | any | all   | some | limit |
| offset | union | except   | intersect | with |
| use | int | tables   | collection |  |


- **Tokens:**
Son los caracteres que están permitidos dentro de nuestro lenguaje

| mas | menos   | elevado |
| ------ |---------| ------:|
| multiplicacion  | division   | modulo    |
| menor_igual  | mayor_igual    | diferente1   |
| diferente2 | ptcoma | para   |
| coma | int | decimales   |
| cadena | cadenastring | parc   |
| id | idpunto |    |

```
mas ::= "+"
menos ::= "-"
elevado ::= "^"
multiplicacion ::= "*"
division ::= "/"
modulo ::= "%"
menor ::= "<"
mayor ::= ">"
igual ::= "="
menor_igual ::= "<="
mayor_igual ::= ">="
diferente1 ::= "<>"
diferente2 ::= "!=""
para ::= "("
parc ::= ")"
ptcoma ::= ";"
coma ::= ","
punto ::= "."
```

- **Precedencia:**
Precedencia de operaciones para la producción de las expresiones

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

### Analisis Sintactico
En el interprete tytusDB se implemento un analisis sintactico utilizando la herramienta de PLY a traves de un analizador
ascendente utilizando la siguiente gramatica:
- Ascendente
```
    <init> ::=::== <instrucciones>

    <instrucciones> ::= <instrucciones> <instruccion>

    <instrucciones> ::= <instruccion>

    <instruccion> ::=  <SELECT> "ptcoma"
                    | <CREATETABLE>
                    | <UPDATE> "ptcoma"
                    | <DELETE>  "ptcoma"
                    | <ALTER>  "ptcoma"
                    | <DROP> "ptcoma"
                    | <INSERT> "ptcoma"
                    | <CREATETYPE> "ptcoma"
                    | <CASE> 
                    | <CREATEDB> "ptcoma"
                    | <SHOWDB> "ptcoma"

    <SELECT> ::= <select> "distinct" <LEXP> "r_from" <LEXP> <WHERE> <GROUP> <HAVING> <ORDER> <LIMIT> <COMBINING>
				|<select> <LEXP> "r_from" <LEXP> <WHERE> <GROUP> <HAVING> <ORDER> <LIMIT> <COMBINING>
				|<select> <LEXP> <LIMIT> <COMBINING> 

    <LIMIT> ::=  "limit" "int"
               | "limit" "all"
               | "offset" "int"
               | "limit" "int" "offset" "int"
               | "offset" "int" "limit" "int"
               | "limit" "all" "offset" "int"
               | "offset" "int" "limit" "all"
               | Ɛ

    <WHERE> ::=   "where" <LEXP>
                | "where" <EXIST>
                | "union" <LEXP>
                | "union" "all" <LEXP>
	            | Ɛ

    <COMBINING> ::=  "union" <LEXP>
                | "union" "all" <LEXP>
                | "intersect" <LEXP>
                | "intersect" "all" <LEXP>
                | "except" <LEXP>
                | "except" "all" <LEXP>
	            | Ɛ

    <GROUP> ::= "group" "by" <LEXP>
	            | Ɛ

    <HAVING> ::= "having" <LEXP>
				| Ɛ 

    <ORDER> ::= "order" "by" <LEXP> <ORD>
    			| "order" "by" <LEXP>
				| Ɛ  

    <ORD> ::= "asc"
				| "desc" 

    <CASE> ::= "case"  <LISTAWHEN> <ELSE> "end"
               | "case" <LISTAWHEN> "end"
    
    <LISTAWHEN> ::= <LISTAWHEN> <WHEN>
                    | <WHEN>
    
    <WHEN> ::= "when" <LEXP> "then" <LEXP>
    
    <ELSE> ::= "else" <LEXP>
    
    <CREATETABLE> ::= "create" "table" "id" "para" <L> "parc" "ptcoma"
                    | "create" "table" "id" "para" <L> "parc" <HERENCIA> "ptcoma"

    <L> ::= <L> "coma" <COL>
            | <COL>

    <COL> ::= <OPCONST>
            | "constraint" "id" <OPCONST>
            | "id" <TIPO>
            | "id" <TIPO> <LOPCOLUMN>

    <LOPCOLUMN> ::= <LOPCOLUMN> <OPCOLUMN>
            | <OPCOLUMN>

    <OPCOLUMN> ::= "constraint" "id" "unique"
            | "constraint" "id" "check" "para" <EXP> "parc"
            | "ault" <EXP>
            | <PNULL>
            | "primary" "key"
            | "references" "id"

    <PNULL> ::= "not" "null"
        | "null"

    <OPCONST> ::= "primary" "key" "para" <LEXP> "parc"
            | "foreign" "key" "para" <LEXP> "parc" "references" "table" "para" <LEXP> "parc"
            | "unique" "para" <LEXP> "parc"
            | "check" "para" <LEXP> "parc"

    <HERENCIA> ::= "inherits" "para" <LEXP> "parc"

	<UPDATE> ::= "update" "id" "set" <LCAMPOS> "where" <LEXP>

	<DELETE> ::= "delete" "r_from" "id" "where" <LEXP>
            | "delete" "r_from" "id"

    <LCAMPOS> ::=  <LCAMPOS> "id" "igual" <EXP>
		| "id" "igual" <EXP>
		| "id" "igual" "ault"

	<ALTERTABLE> ::= "alter" "table" "id" <OP>
    
    <OP> ::= "add" <ADD>
            | "drop" "column" <ALTERDROP>
            | "alter" "column" "id" "set" "not" "null"
            | "alter" "column" "id" "set" "null"
            | <LISTAALC>
            | "drop" <ALTERDROP>
            | "rename" "column" "id" "to" "id" 

    <LISTAALC> ::= <LISTAALC> "coma" <ALC>
            | <ALC>
    
    <ALC> ::= "alter" "column" "id" "type" <TIPO>
    
    <ALTERDROP> ::= "constraint" "id"
                   | "column" <LEXP>
                   | "check" "id"
    
    <ADD> ::= "column" "id" <TIPO>
            | "check" "para" <LEXP> "parc"
            | "constraint" "id" "unique" "para" "id" "parc"
            | "foreign" "key" "para" "id" "parc" "references" "id" "para" "id" "parc"

    <DROP> ::= "drop" "table" "id"
             | "drop" "databases" "if" "exist" "id"
             | "drop" "databases" "id" 

    <INSERT> ::= "insert" "into" "id" "values" "para" <LEXP> "parc"
    
    <CREATETYPE> ::= "create" "type" "id" "as" "enum" "para" <LEXP> "parc"

	<CREATEDB> ::= "create" <RD> "if" "not" "exist" "id"
        | "create" <RD> "if" "not" "exist" "id" <OPCCDB>
        | "create" <RD> "id"
        | "create" <RD> "id" <OPCCDB>
    
    <OPCCDB> ::= <PROPIETARIO>
        | <MODO>
        | <PROPIETARIO> <MODO>

    <RD> ::= "or" "replace" "databases"
        | "databases"
    
    <PROPIETARIO> ::= "owner" "igual" "id"
		| "owner" "id"
    
    <MODO> ::= "mode" "igual" "int"
	    | "mode" "int"
    	
    <EXIST> ::= "exist" "para" <SELECT> "parc"

    <SHOWDB> ::= "show" "databases"

    <ALTER> ::= "alter" "databases" "id" <RO>
              | <ALTERTABLE>

    <RO> ::= "rename" "to" "id"
           | "owner" "to" "id"
    
    <LEXP> ::= <LEXP> "coma" <EXP>
			| <EXP>

    <TIPO> ::= "smallint"
            | "integer"
            | "bigint"
            | "decimal" "para" <LEXP> "parc"
            | "numeric" "para" <LEXP> "parc"
            | "real"
            | "double" "precision"
            | "money"
            | "character" "varying" "para" "int" "parc"
            | "varchar" "para" "int" "parc"
            | "character" "para" "int" "parc"
            | "char" "para" "int" "parc"
            | "text"
            | "timestamp" 
            | "timestamp" "without" "time" "zone"
            | "timestamp" "para" "int" "parc" "without" "time" "zone"
            | "timestamp" "with" "time" "zone"
            | "timestamp" "para" "int" "parc" "with" "time" "zone"
            | "timestamp" "para" "int" "parc"
            | "date"
            | "time" 
            | "time" "without" "time" "zone"
            | "time" "para" "int" "parc" "without" "time" "zone"
            | "time" "with" "time" "zone"
            | "time" "para" "int" "parc" "with" "time" "zone"
            | "time" "para" "int" "parc"
            | "interval"
            | "interval" "para" "int" "parc"
            | "interval" "cadena"
            | "interval" "para" "int" "parc" "cadena"
            | "boolean"

    <FIELDS> ::= "year"
        | "month"
        | "day"
        | "hour"
        | "minute"
        | "second"

    <EXP> ::= <EXP> "mas" <EXP>
            | <EXP> "menos" <EXP>
            | <EXP> "multiplicacion" <EXP>
            | <EXP> "division" <EXP>
            | <EXP> "modulo" <EXP>
            | <EXP> "elevado" <EXP>
            | <EXP> "and" <EXP>
            | <EXP> "or" <EXP>
            | <EXP> "mayor" <EXP>
            | <EXP> "menor" <EXP>
            | <EXP> "mayor_igual" <EXP>
            | <EXP> "menor_igual" <EXP>
            | <EXP> "igual" <EXP>
            | <EXP> "diferente1" <EXP>
            | <EXP> "diferente2" <EXP>
            | <EXP> "punto" <EXP>
            | "mas" <EXP> %prec "umas"
            | "menos" <EXP> %prec "umenos"
            | "not" <EXP>
            | "para" <EXP> "parc"
            | "int"
            | "decimales"
            | "cadena"
            | "cadenaString"
            | "true"
            | "false"
            | "id"
            | <PNULL>
            | <SELECT>
            | <PREDICADOS>
            | "id" "para" "parc"
            | "id" "para" <LEXP> "parc"
            | "extract" "para" <FIELDS> "r_from" "timestamp" "cadena" "parc"
            | "current_time"
            | "current_date"
            | "timestamp" "cadena" 
            | "interval" "cadena"
            | <CASE>
            | "cadena" "like" "cadena"
            | "cadena" "not" "like" "cadena"
            | "any" "para" <LEXP> "parc"
            | "all" "para" <LEXP> "parc"
            | "some" "para" <LEXP> "parc"
            | <EXP> "as" "cadenaString" %prec "lsel"
            | <EXP> "cadenaString" %prec "lsel"
            | <EXP> "as" "id" %prec "lsel"
            | <EXP> "id" %prec "lsel"
            | <EXP> "as" "cadena" %prec "lsel"
            | <EXP> "cadena" %prec "lsel"
            | "multiplicacion" %prec "lsel"
    
    <PREDICADOS> ::= <EXP> "between" <EXP> %prec "predicates"
            | <EXP> "in" "para" <LEXP> "parc" %prec "predicates"
            | <EXP> "not" "in" "para" <LEXP> "parc" %prec "predicates"
            | <EXP> "not" "between" <EXP> %prec "predicates"
		    | <EXP> "between" "symetric" <EXP> %prec "predicates"
		    | <EXP> "not" "between" "symetric" <EXP> %prec "predicates"
		    | <EXP> "is" "distinct" "r_from" <EXP> %prec "predicates"
		    | <EXP> "is" "not" "distinct" "r_from" <EXP> %prec "predicates"
		    | <EXP> "is" <PNULL> %prec "predicates"
		    | <EXP> "isnull" %prec "predicates"
		    | <EXP> "notnull" %prec "predicates"
		    | <EXP> "is" "true" %prec "predicates"
		    | <EXP> "is" "not" "true" %prec "predicates"
		    | <EXP> "is" "false" %prec "predicates"
		    | <EXP> "is" "not" "false" %prec "predicates"
		    | <EXP> "is" "unknown" %prec "predicates"
		    | <EXP> "is" "not" "unknown" %prec "predicates"
```
- **Descendente:**
Esta tiene se diferencia de la ascendente porque, no tiene ambigüedad , no es recursiva por la
izquierda y esta factorizada; esta gramatica no se utilizó en el proyecto solo se realizo para comparar
la eficiencia de cada una.
```
INIT ::= INSTRUCCIONES

INSTRUCCIONES ::= INSTRUCCION INSTRUCCIONES'

INSTRUCCIONES' ::= INSTRUCCION INSTRUCCIONES'
            | Ɛ

INSTRUCCION ::= SELECT ptcoma
            | CREATETABLE
            | UPDATE ptcoma
            | DELETE ptcoma
            | ALTER ptcoma
            | DROP ptcoma
            | INSERT ptcoma
            | CREATETYPE ptcoma
            | CASE
            | CREATEDB ptcoma
            | SHOWDB ptcoma

CASE ::= case LISTAWHEN ELSE end
        | case LISTAWHEN end

LISTAWHEN ::= WHEN LISTAWHEN'

LISTAWHEN' ::= WHEN LISTAWHEN'
            | Ɛ

WHEN : when LEXP then LEXP

ELSE ::= else LEXP

INSERT ::= insert into id values para LEXP parc

DROP ::= drop table id
        | drop databases if exist id
        | drop databases id

ALTER ::= alter databases id RO
        | ALTERTABLE

RO ::= rename to id
        | owner to id

ALTERTABLE ::= alter table id OP

OP ::= add ADD
    | drop column ALTERDROP
    | alter column id set not null
    | alter column id set null
    | LISTAALC
    | drop ALTERDROP
    | rename column id to id

LISTAALC ::= ALC LISTAALC'

LISTAALC' ::= coma ALC LISTAALC'
            | Ɛ

ALC ::= alter column id type TIPO

ALTERDROP ::= constraint id
            | column LEXP
            | check id

ADD ::= column id TIPO
        | check para LEXP parc
        | constraint id unique para id parc
        | foreign key para LEXP parc references id para LEXP parc

SHOWDB ::= show databases

CREATEDB ::= create RD if not exist id
            | create RD if not exist id OPCCDB
            | create RD id
            | create RD id OPCCDB

OPCCDB ::= PROPIETARIO
        | MODO
        | PROPIETARIO MODO

RD ::= or replace databases
        | databases

PROPIETARIO ::= owner igual id
            | owner id

MODO ::= mode igual int
        | mode int

CREATETABLE ::= create table id para LDEF parc ptcoma
            | create table id para LDEF parc HERENCIA ptcoma

LDEF ::= COLDEF LDEF'

LDEF' ::= coma COLDEF LDEF'
        | Ɛ

COLDEF ::= OPCONST
        | constraint id OPCONST
        | id TIPO
        | id TIPO LOPCOLUMN

LOPCOLUMN ::= OPCOLUMN LOPCOLUMN'

LOPCOLUMN' ::= OPCOLUMN LOPCOLUMN'
            | Ɛ

OPCOLUMN ::= constraint id unique
            | constraint id check para EXP parc
            | default EXP
            | not null
            | null
            | primary key
            | references id

OPCONST ::= primary key para LEXP parc
        | foreign key para LEXP parc references id para LEXP parc
        | unique para LEXP parc
        | check para LEXP parc

HERENCIA ::= inherits para LEXP parc

CREATETYPE ::= create type id as enum para LEXP parc

SELECT ::= select distinct LEXP from LEXP WHERE GROUP HAVING ORDER LIMIT COMBINING
        | select LEXP from LEXP WHERE GROUP HAVING ORDER LIMIT COMBINING
        | select LEXP LIMIT COMBINING

LIMIT ::= limit int
        | limit all
        | offset int
        | limit int offset int
        | offset int limit int
        | limit all offset int
        | offset int limit all
        | Ɛ

WHERE ::= where LEXP
        | where EXIST
        | union LEXP 
        | union all LEXP
        | Ɛ

COMBINING ::= union LEXP
            | union all LEXP
            | intersect all LEXP
            | except LEXP
            | except all LEXP
            | Ɛ

GROUP ::= group by LEXP
        | Ɛ

HAVING ::= having LEXP
        | Ɛ

ORDER ::= order by LEXP ORD
        | order by LEXP
        | Ɛ

ORD ::= asc
    | desc

UPDATE ::= update id set LCAMPOS where LEXP

LCAMPOS ::= id igual EXP LCAMPOS'

LCAMPOS' ::= id igual EXP LCAMPOS'
            | Ɛ

DELETE ::= delete from id where LEXP
        | delete from id

EXIST ::= exist para SELECT parc

LEXP ::= EXP LEXP'

LEXP' ::= coma EXP LEXP'
        | Ɛ

TIPO ::= smallint
        | integer
        | bigint
        | decimal para LEXP parc
        | numeric para LEXP parc
        | real
        | double precision
        | money
        | character varying para int parc
        | varchar para int parc
        | character para int parc
        | char para int parc
        | text
        | timestamp 
        | timestamp without time zone
        | timestamp para int parc without time zone
        | timestamp with time zone
        | timestamp para int parc with time zone
        | timestamp para int parc
        | date
        | time 
        | time without time zone
        | time para int parc without time zone
        | time with time zone
        | time para int parc with time zone
        | time para int parc
        | interval
        | interval para int parc
        | interval cadena
        | interval para int parc cadena
        | boolean

FIELDS ::=  year
        | month
        | day
        | hour
        | minute
        | second
```
## Autores
### Grupo 14
* **Walter Josue Paredes Sol** - *201504326*
* **Asunción Mariana Sic Sor** - *201504051*
* **Wendy Aracely Chamalé Boch** - *201504284*
* **Carlos Eduardo Torres Caal** - *201504240*
