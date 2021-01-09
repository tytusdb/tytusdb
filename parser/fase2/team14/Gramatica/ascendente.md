> # Gramática para Analizador Ascendente

- [Expresiones Regulares](#expresiones-regulares)
- [Tokens](#tokens)
- [Reglas Sintácticas](#reglas-sintacticas)
- [Precedencia](#precedencia-de-operadores)


## Expresiones regulares
```
int ::= digito+
decimales ::= digito+ "." digito+ (["e"] ["+"|"-""] digito+)?
id ::= [a-zA-Z_][a-zA-Z_0-9]*
cadena ::= """ "."*? """
cadenaString ::= "".*?""
```

## Tokens
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

## Reglas Sintácticas
```
INIT ::= INSTRUCCIONES

INSTRUCCIONES ::= INSTRUCCIONES INSTRUCCION
            | INSTRUCCION

INSTRUCCION ::= SELECT ptcoma
            | CREATETABLE
            | UPDATE ptcoma
            | DELETE  ptcoma
            | ALTER  ptcoma
            | DROP ptcoma
            | INSERT ptcoma
            | CREATETYPE ptcoma
            | CASE ptcoma
            | CREATEDB ptcoma
            | SHOWDB ptcoma
            | SHOW ptcoma
            | use id ptcoma
            | CREATEINDEX  ptcoma
            | CREATEINDEX  WHERE ptcoma
            | ASIGNACION  ptcoma
            | CONDICIONIF  ptcoma
            | PROCEDIMIENTOS 
            | FUNCIONES
            | CALLPROCEDURE ptcoma
            | DROPFUNC ptcoma
            | DROPPROCEDURE ptcoma

RETURN ::= return EXP

FUNCIONES ::= create function id para LPARAM parc RETURNP LENGUAJE LCONTENIDOP
            | create function id para parc RETURNP LENGUAJE LCONTENIDOP
            | create function id para LPARAM parc RETURNP LCONTENIDOP LENGUAJE
            | create function id para  parc RETURNP LCONTENIDOP LENGUAJE
            
DROPFUNC ::= drop function id
        | drop function if exist id
        
DROPPROCEDURE ::= drop procedure id
            | drop procedure if exist id
            
RETURNP ::= returns  TIPO

CALLPROCEDURE ::= execute id para LEXP parc
                | execute id para  parc

PROCEDIMIENTOS ::= create procedure id para LPARAM parc LENGUAJE  LCONTENIDOP
                | create procedure id para  parc LENGUAJE  LCONTENIDOP
                | create procedure id para LPARAM parc LCONTENIDOP LENGUAJE
                | create procedure id para parc LCONTENIDOP LENGUAJE

LCONTENIDOP ::= LCONTENIDOP CONTENIDOP
                | CONTENIDOP

CONTENIDOP ::= as dolarn LISTACONTENIDO dolarn
            | do dolarn LISTACONTENIDO dolarn

LPARAM ::= LPARAM coma inout id TIPO
        | LPARAM coma  id TIPO
        | inout id TIPO
        | id TIPO

LENGUAJE ::= language plpgsql
            | language plpgsql ptcoma

BEGINEND ::=  begin LISTACONTENIDO end

CREATEINDEX ::= create index id on id para LEXP parc
            | create unique index id on id para LEXP parc
            | create index id on id using hash para LEXP parc
            | create index id on id  para id ORDEN parc
            | create  index id on id para id  id ORDEN parc
            | create  index id on id para id  id  parc '''

ORDEN ::= asc
        | desc
        | nulls first
        | nulls last 
        | asc nulls first
        | desc nulls last
        | desc nulls first
        | asc nulls last

LDEC ::= LDEC DECLARACIONES
        | DECLARACIONES

DECLARACIONES ::= id TIPO not null ASIG ptcoma
            | id TIPO ASIG ptcoma
            | id constant TIPO not null ASIG ptcoma
            | id constant TIPO ASIG ptcoma

ASIG : default EXP
    | dospuntos igual EXP
    | igual EXP
    | Ɛ
    
ASIGNACION ::= id dospuntos igual EXP
            | id igual EXP

CONDICIONIF ::= if EXP then LISTACONTENIDO ELSEF  end if
                | if EXP then LISTACONTENIDO LELIF   end if
                | if EXP then LISTACONTENIDO end if
                | if EXP then LISTACONTENIDO LELIF ELSEF end if

LELIF ::= LELIF elsif EXP then LISTACONTENIDO
        | elsif EXP then LISTACONTENIDO

ELSEF ::= else LISTACONTENIDO

CASE : case EXP  LISTAWHEN ELSEF  end case
    | case EXP  LISTAWHEN   end case
    | case  LISTAWHEN ELSEF end case
    | case LISTAWHEN end case

LISTACONTENIDO ::= LISTACONTENIDO CONTENIDO
                | CONTENIDO

CONTENIDO : ASIGNACION ptcoma
        | CONDICIONIF ptcoma
        | RAISE ptcoma
        | BEGINEND ptcoma
        | CALLPROCEDURE ptcoma
        | declare LDEC 
        | RETURN ptcoma
        | INSERT ptcoma 
        | SELECT ptcoma
        | UPDATE ptcoma
        | DELETE ptcoma 
        | CASE ptcoma

RAISE ::= raise LEVEL FORMAT
        | raise LEVEL EXP
        | raise LEVEL 
        | raise
        | raise LEVEL cadena coma id

LEVEL ::= info
        | debug
        | notice
        | warning
        | exception
        
FORMAT ::= format para EXP  coma LEXP parc

LISTAWHEN ::= LISTAWHEN WHEN
            | WHEN

WHEN ::= when EXP then LISTACONTENIDO
        | when EXP then LEXP'''

ELSE ::= else LEXP

INSERT ::= insert into id values para LEXP parc
        | insert into id para LEXP parc values para LEXP parc

DROP ::= drop all para parc
        | drop table id
        | drop index id
        | drop databases if exist id
        | drop databases id 

ALTER ::= alter databases id rename to id
        | alter databases id owner to id
        | alter table id LOP
        | alter index id alter EXP
        | alter index if exist id alter EXP
        | alter index id alter column EXP
        | alter index if exist id alter column EXP

LOP ::= LOP coma OP
        | OP

OP ::= add column id TIPO
    | add check para CONDCHECK parc
    | add constraint id check para CONDCHECK parc
    | add constraint id unique para LEXP parc
    | add unique para LEXP parc
    | add foreign key para LEXP parc references id para LEXP parc
    | add constraint id foreign key para LEXP parc references id para LEXP parc
    | alter column id set not null
    | alter column id set null
    | drop constraint id
    | drop column LEXP
    | drop check id
    | rename column id to id 
    | alter column id type TIPO

SHOWDB ::= show dbs
        | show tables para id parc
        | show collection para parc

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
            | owner igual cadena
            | owner igual cadenaString
            | owner id
            | owner cadena
            | owner cadenaString

MODO ::= mode  igual int
	    | mode int

CREATETABLE ::= create table id para LDEF parc ptcoma
            | create table id para LDEF parc HERENCIA ptcoma
            
LDEF ::= LDEF coma COLDEF
        | COLDEF

COLDEF ::= OPCONST
        | constraint id OPCONST
        | id TIPO
        | id TIPO LOPCOLUMN

LOPCOLUMN ::= LOPCOLUMN OPCOLUMN
            | OPCOLUMN

OPCOLUMN ::= constraint id unique
            | unique
            | constraint id check para CONDCHECK parc
            | check para CONDCHECK parc
            | default EXP
            | not null
            | null
            | primary key
            | references id

OPCONST ::= primary key para LEXP parc
        | foreign key para LEXP parc references id para LEXP parc
        | unique para LEXP parc
        | check para CONDCHECK parc

CONDCHECK ::= EXP mayor EXP
            | EXP menor EXP
            | EXP mayor_igual EXP
            | EXP menor_igual EXP
            | EXP igual EXP
            | EXP diferente1 EXP
            | EXP diferente2 EXP

HERENCIA ::= inherits para id parc

CREATETYPE ::= create type id as enum para LEXP parc

SELECT ::= select distinct  LEXP r_from LEXP  WHERE GROUP HAVING COMBINING ORDER LIMIT
	    | select  LEXP r_from LEXP WHERE  GROUP HAVING  COMBINING ORDER LIMIT
	    | select  LEXP WHERE  GROUP HAVING  COMBINING ORDER LIMIT

LIMIT ::= limit int
        | limit all
        | offset int
        | limit int offset int
        | offset int limit int
        | limit all offset int
        | offset int limit all
        | Ɛ

WHERE ::= where EXP 
        | where EXIST
	    | Ɛ

COMBINING ::=  union EXP
            | union all EXP
            | intersect EXP
            | except EXP
            | Ɛ

GROUP ::=  group by LEXP
        | Ɛ

HAVING ::= having EXP
	    | Ɛ

ORDER ::= order by LEXP ORD
        | order by LEXP
        | Ɛ 

ORD ::= asc
	| desc

UPDATE ::= update id set LCAMPOS WHERE

LCAMPOS ::= LCAMPOS coma id igual EXP
        | id igual EXP

DELETE ::= delete from id WHERE

EXIST ::= exist para SELECT parc
        | not exist para SELECT parc

LEXP ::= LEXP coma EXP
        | EXP

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

### Precedencia de operadores

|Asociatividad|Símbolo|Descripción|
|:----------:|:-------------:|:---------:|
|Izquierda|lsel|Precedencia utilizada para los alias en la instrucción SELECT|
|Izquierda|.|Operador para separar atributos de una tabla|
|Derecha|-,+|Operador unario para números negativos y positivos|
|Izquierda|^|Potencia|
|Izquierda|*,/,%|Multiplicación, división y modular|
|Izquierda|-,+|Suma y Resta|
|Izquierda|>,<,>=,<=,=,!=,<>|Operaciones relacionales|
|Izquierda|predicates|Precedencia para predicados en consultas|
|Derecha|NOT|Negación lógica|
|Izquierda|AND|Operador AND lógico|
|Izquierda|OR| Operador OR lógico|

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