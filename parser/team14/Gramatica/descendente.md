> # Gramática Descendente

- [Precedencia de Operadores](#para-definir-la-producción-de-expresiones-aritméticas-lógicas-relacionales-se-utilizó-la-siguiente-precedencia-de-operadores)

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
