# Gramática para analizador Ascendente

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

## Precedencia de operaciones para la producción de las expresiones.

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


## inicio de la gramática
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