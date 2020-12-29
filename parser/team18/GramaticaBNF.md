# Gramatica Ascendente
```sh
<init> ::= <l_sentencias>

<l_sentencias> ::= <l_sentencias sentencias>
    | <sentencias>

<sentencias> ::= <sentencia> ";"

<sentencia> ::= <sentencia_ddl>
    | <sentencia_dml>

<sentencia_ddl> ::= <crear>
    | <liberar>

<sentencia_dml> ::= <insertar>
    | <actualizar>
    | <eliminar>
    | <seleccionH>
    | <mostrar>
    | <altert>

<seleccionH>  ::= <seleccionH> "UNION" <seleccionar>
    | <seleccionH> "INTERSECT" <seleccionar>
    | <seleccionH> "EXCEPT"  <seleccionar>
    | <seleccionH> "UNION" "ALL"  <seleccionar>
    | <seleccionH> "INTERSECT" "ALL" <seleccionar>
    | <seleccionH> "EXCEPT" "ALL" <seleccionar>
    | "(" <seleccionH> ")"
    | <seleccionar>

<altert> ::= <alterdb>
    | <altertb>

<alterdb> ::= "ALTER" "DATABASE" <ID> <alterdb1>

<alterdb1 ::= "RENAME" "TO" <ID> 
    | "OWNER" "TO" <alterdb2>

<alterdb2> ::= <ID> 
               | "CURRENT_USER"
               | "SESSION_USER"

<altertb> ::= "ALTER" "TABLE" <ID> <altertb1>

<altertb1> ::= <alttbadd> 
    | <alttbdrop>
    | <alttbalterv>
    | <alttbname>

<alttbname> ::= "RENAME" <alttbrename1>

<alttbrename1> ::= "COLUMN" <ID> "TO" <ID> 
    | <ID> "TO" <ID> 
    | "CONSTRAINT" <ID> "TO" <ID>
    | "TO" <ID>

<alttbalterv> ::= <alttbalterv> "," <alttbalter>
    | <alttbalter>

<alttbalter> ::= "ALTER" "COLUMN" <ID> <alttbalter1>
    | "CONSTRAINT" <ID>

<alttbalter1> ::= "SET" "NOT" "NULL"
    | "DROP" "NOT" "NULL"
    | "SET" "DATA" "TYPE" <tipo> <valortipo>
    | "TYPE" <tipo> <valortipo>
    | "SET" "DEFAULT" <CADENA1>
    | "DROP" "DEFAULT"

<alttbdrop> ::= "DROP" <alttbdrop1>

<alttbdrop1> ::= "COLUMN" <ID> 
    |  <ID> 
    | "CONSTRAINT" <ID>

<alttbadd> ::= "ADD" <ID> <tipo> <valortipo>
    | "ADD" "COLUMN" <ID> <tipo> <valortipo>
    | "ADD" "CONSTRAINT" <ID> alttbadd2>
    | "ADD" <alttbadd2>

<alttbadd2> ::= <alttbadd2> <alttbadd3>
    | <alttbadd3>

<alttbadd3> ::= "CHECK" "(" <exp> ")"
    | "UNIQUE" "(" <CADENA1> ")"
    | "PRIMARY" "KEY" "(" <CADENA1> ")"
    | "FOREIGN" "KEY" "(" <CADENA1> ")" "REFERENCES"  <ID> "(" <CADENA1> ")"

<insertar> ::= "INSERT" "INTO" <ID> "VALUES" "(" <lista_exp> ")"

<actualizar> ::= "UPDATE" <ID> "SET" <exp> "WHERE" <exp>

<eliminar> ::= "DELETE" "FROM" <ID> "WHERE" <exp>

<seleccionar> ::= <seleccionar1> "LIMIT" <ENTERO> <offsetop>
    | <seleccionar1> "LIMIT" "ALL" <offsetop>
    | <seleccionar1> <offsetop>
    | <seleccionar1> "LIMIT" "ENTERO"
    | <seleccionar1> "LIMIT" "ALL"
    | <seleccionar1>

<extract> ::= "EXTRACT" "(" <extract1>  "FROM" <timestamp>  <valoresdefault>  ")"
    | "DATE_PART" "(" <valoresdefault> "," <interval> <valoresdefault>  ")"
    | <nowf>
    | "CURRENT_DATE"
    | "CURRENT_TIME"
    | <timestamp> <valoresdefault>

<nowf> ::= "NOW" "(" ")"

<extract1> ::= "YEAR"
    | "MONTH"
    | "DAY"
    | "HOUR"
    | "MINUTE"
    | "SECOND"
    | <CADENA1>
    | <CADENA2>

<offsetop> ::= "OFFSET" <ENTERO>

<seleccionar1> ::= "SELECT" <cantidad_select> <parametros_select> <cuerpo_select> 
    | "SELECT" <funcion_math> <alias_name>
    | "SELECT" <funcion_date>
    | "SELECT" <funcionGREALEAST>
    | "SELECT" <extract>

<funcionGREALEAST> : "GREATEST" "(" <exp> ")"
    | "LEAST" "(" <exp> ")"

<cantidad_select> ::= "DISTINCT"
    | ""

<parametros_select> ::= "*"
    | <lista_select>

<lista_select> ::= <lista_select> "," <value_select>
    | value_select

<value_select> ::= <columna_name> <alias_name>
    | <ID> "." "*" <alias_name>
    | <funcion_math> <alias_name>
    | "(" <seleccionar> ")" <alias_name>
    | <case>

<case> ::= "CASE" <loop_condition>  "END" 
    | "CASE" <loop_condition>  "END" "AS" <ID>
    | "CASE" <loop_condition>  <else>  "END" 
    | "CASE" <loop_condition>  <else> "END" "AS" <ID>
    | "(" <case> ")"

<loop_condition> ::= <loop_condition> "WHEN" <exp> "THEN" <resultV>
    | "WHEN" <exp> "THEN" <resultV>

<else> ::= "ELSE" <resultV>

<resultV> ::= <ENTERO>
    | <DECIMAL>
    | <CADENA1>
    | <CADENA2>
    | <ID>
    | "(" <resultV> ")"

<columna_name> : <ID>
    | <ID> "." <ID>

<list_colum> ::= <list_colum> "," <columna_name>
                    | <columna_name>  

<sub_query> ::= "EXISTS"
    | <exp>
    | <exp> "NOT" "IN"
    | <exp> "IN"

<cuerpo_select> ::= <bloque_from> <bloque_join> <bloque_where> <bloque_group> <bloque_having> <bloque_order>

<bloque_from> ::= "FROM" <lista_tablas>

<lista_tablas> ::= <lista_tablas> "," <value_from>
    | <value_from>

<value_from> ::= <tabla_name>
    | "(" <seleccionar> ")" <ID>
    | "(" <seleccionar> ")" "AS" <ID>

<tabla_name> ::= <ID>
    | <ID> <ID>

<bloque_join> ::= <bloque_join> <lista_joins>
    | <lista_joins>
    | ""

<lista_joins> ::= "NATURAL" <tipo_joins> <tabla_name> "ID"
    | <tipo_joins> "JOIN" <tabla_name> "ON" <condicion_boleana>
    | <tipo_joins> "JOIN" <tabla_name> "USING" "(" <list_colum> ")"

<tipo_joins> ::= "INNER"
    | <value_join>
    | <value_join> "OUTER"

<value_join> ::= "LEFT"
    | "RIGHT"
    | "FULL"

<bloque_where> ::= "WHERE" <cuerpo_where>
    | ""

cuerpo_where ::= <condicion_boleana>
    | <sub_query> "(" <seleccionar> ")" <alias_name>

<bloque_group> ::= "GROUP" "BY" <list_colum>
    | ""

<bloque_having ::= "HAVING" <condicion_boleana>
    | ""

<bloque_order> ::= "ORDER" "BY" <lista_order>
    | ""

<lista_order> ::= <lista_order> "," <value_order>
    | <value_order>
    | <case>

<value_order> ::= <ID> <value_direction> <value_rang>

<value_direction> ::= "ASC"
    | "DESC"
    | ""

<value_rang> ::= "NULLS" "FIRST"
    | "NULLS" "LAST"
    | "NULLS" "FIRST" "NULLS" "LAST"
    | "NULLS" "LAST" "NULLS" "FIRST"
    | ""

<alias_name> ::= <valoralias>
    | "AS" <valoralias>
    | ""

<valoralias> ::= <ID>
    | <CADENA1>
    | <CADENA2>

<condicion_boleana> ::= <exp>

<funcion_math> ::= "ABS" "(" <exp> ")"
    | "CBRT" "(" <exp> ")"
    | "CEIL" "(" <exp> ")"
    | "CEILING" "(" <exp> ")"
    | "DEGREES" "(" <exp> ")"
    | "DIV" "(" <lista_exp> ")"
    | "EXP" "(" <exp> ")"
    | "factorial" "(" <exp> ")"
    | "FLOOR" "(" <exp> ")"
    | "GCD" "(" <lista_exp> ")"
    | "LN" "(" <exp> ")"
    | "LOG" "(" <exp> ")"
    | "MOD" "(" <lista_exp> ")"
    | "PI" "(" ")"
    | "POWER" "(" <lista_exp> ")"
    | "RADIANS" "(" <exp> ")"
    | "ROUND" "(" <exp> ")"
    | "min_scale" "(" <exp> ")"
    | "scale" "(" <exp> ")"
    | "sign" "(" <exp> ")"
    | "sqrt" "(" <exp> ")"
    | "trim_scale" "(" <exp> ")"
    | "TRUNC" "(" <lista_exp> ")" 
    | "random" "(" ")"
    | "setseed" "(" <exp> ")"
    | "ACOS" "(" <exp> ")"
    | "ACOSD" "(" <exp> ")"
    | "ASIN" "(" <exp> ")"
    | "ASIND" "(" <exp> ")"
    | "ATAN" "(" <exp> ")"
    | "ATAND" "(" <exp> ")"
    | "ATAN2" "(" <lista_exp> ")"
    | "ATAN2D" "(" <lista_exp> ")"
    | "COS" "(" <exp> ")"
    | "COSD" "(" <exp> ")"
    | "COT" "(" <exp> ")"
    | "COTD" "(" <exp> ")"
    | "SIN" "(" <exp> ")"
    | "SIND" "(" <exp> ")"
    | "TAN" "(" <exp> ")"
    | "TAND" "(" <exp> ")"
    | "SINH" "(" <exp> ")"
    | "COSH" "(" <exp> ")"
    | "TANH" "(" <exp> ")"
    | "ASINH" "(" <exp> ")"
    | "ACOSH" "(" <exp> ")"
    | "ATANH" "(" <exp> ")"
    | "length" "(" <exp> ")"
    | "substring" "(" <lista_exp> ")"
    | "trim" "(" <valorestrim> exp FROM exp ")"
    | "MD5" "(" <exp> ")"
    | "sha256" "(" <exp> ")"
    | "decode" "(" <exp> <byteaop> "," <lista_exp> ")"
    | "encode" "(" <exp> <byteaop> "," <lista_exp> ")"
    | "get_byte" "(" <exp> ":" <bytea> "," <lista_exp> ")"
    | "set_byte" "(" <exp> ":" <bytea> "," <lista_exp> ")"
    | "substr" "(" <lista_exp> ")"
    | "CONVERT" "(" <exp> "AS" <tipo> ")" 
    | "width_bucket" "(" <lista_exp> ")"
    | ""

<funcion_date> ::= ""

<mostrar> ::= "SHOW" "DATABASES"

<valorestrim> ::= "leading"
    | "trailing"
    | "both"

<byteaop> ::= ":" <bytea>
    | ""

<lista_exp> ::= <lista_exp> "," <exp>  
    | <exp>

<exp> ::= <exp_log>
    | <exp_rel>
    | <exp_ar>
    | <exp_select>
    | <expresion_patron>
    | <E>

<exp_log> ::= "NOT" <exp>
    | <exp> "AND" <exp>  
    | <exp> "OR" <exp>

<expresion_patron> ::= <exp> "BETWEEN" <exp>
    | <exp> "IN" <exp>
    | <exp> "NOT" "IN" <exp>
    | <exp> "LIKE" <exp>
    | <exp> "NOT" "LIKE"  <exp>
    | <exp> "ILIKE" <exp>
    | <exp> "NOT" "ILIKE"  <exp>
    | <exp> "SIMILAR" "TO" <exp>
    | <exp> "NOT" "SIMILAR" "TO" <exp>
    | <exp> "," <exp>

<exp_rel> ::= <exp> <toperador> <exp>

<toperador> ::= <IGUAL>
    | <DESIGUAL>
    | <DESIGUAL2>
    | <MAYORIGUAL>
    | <MENORIGUAL>
    | <MAYOR>
    | <MENOR>

<exp_ar> ::= <exp> <SUMA> <exp>
    | <exp> <RESTA> <exp>
    | <exp> <ASTERISCO> <exp>
    | <exp> <DIVISION> <exp>
    | <exp> <POTENCIA> <exp>
    | <exp> <MODULO> <exp>

<exp_select> ::= <SQRT2> <exp>
    | <CBRT2> <exp>
    | <exp> <AND2> <exp>
    | <exp> <SQRT2> <exp>
    | <NOT2> <exp>
    | <exp> <XOR> <exp>
    | <exp> <SH_LEFT> <exp>
    | <exp> <SH_RIGHT> <exp>

<E> ::= <ENTERO>
    | <DECIMAL>
    | <CADENA1>
    | <CADENA2>
    | <ID>
    | <ID> "." <ID>
    | "(" <exp> ")"
    | "ANY"
    | "ALL"
    | "SOME"
    | "IN"
    | <seleccionar>
    | <funcion_math>
    | "NULL"
    | <lvaloresdefault>
    | "NOT" "IN"

<crear> ::= "CREATE" <reemplazar> "DATABASE" <verificacion> <ID> <propietario> <modo>
    | "CREATE" "TABLE" <ID> "(" <columnas> ")" <herencia>
    | "CREATE" "TYPE" <ID> "AS" "ENUM" ""(""<lista_exp> "")""

<reemplazar> ::= "OR" "REPLACE"
    | ""

<verificacion> ::= "IF" "NOT" "EXISTS"
    | ""

<propietario> ::= "OWNER" <valorowner>
    | ""

<valorowner> ::= <ID>
    | <IGUAL> <ID>

<modo> ::= "MODE" <valormodo>
    | ""

<valormodo> ::= <ENTERO>
    | <IGUAL> <ENTERO>

<herencia> ::= "INHERITS" "(" <ID> ")"
    | ""

<columnas> ::= <columnas> "," <columna>
    | <columna>

<columna> ::= <ID> <tipo> <valortipo> <zonahoraria> <atributocolumn>
    | "PRIMARY" "KEY" "(" <lnombres> ")"
    | "FOREIGN" "KEY" "(" <lnombres> ")" "REFERENCES" <ID> "(" <lnombres> ")"

<tipo> ::= "smallint"
    | "integer"
    | "bigint"
    | "decimal"
    | "numeric"
    | "real"
    | "double" "precision"
    | "money"
    | "character" "varying"
    | "character"
    | "char"
    | "varchar"
    | "text"
    | "date"
    | "timestamp"
    | "time"
    | "interval"
    | "boolean"

<valortipo> ::= "(" <lvaloresdefault> ")"
    | <lvaloresdefault>
    | ""

<zonahoraria> ::= "with" "time" "zone"
    | ""

<atributocolumn> ::= <atributocolumn> <atributo>
    | <atributo>

<atributo> ::= "DEFAULT" <valoresdefault>
    | "CONSTRAINT" <ID>
    | "NULL" 
    | "NOT" "NULL"
    | "UNIQUE"
    | "PRIMARY" "KEY"
    | "CHECK" "(" <lista_exp> ")"
    | ""

<lvaloresdefault> ::= <lvaloresdefault> "," <valoresdefault>
    | <valoresdefault>

<valoresdefault> ::= <CADENA1>
    | <CADENA2>
    | <DECIMAL>
    | <ENTERO>
    | <BOOLEAN>
    | "YEAR"
    | "MONTH"
    | "DAY"
    | "SECOND"
    | "MINUTE"
    | "HOURS"

<lnombres> ::= <lnombres> "," <ID>
    | <ID>

<liberar> ::= "DROP" "TABLE" <existencia> <ID>
    | "DROP" "DATABASE" <existencia> <ID>

<existencia> ::= "IF" "EXISTS"
                  | ""

```
# Gramatica Descendente 

```sh

<init> ::= <l_sentencias>

<l_sentencias> ::= <l_sentencias sentencias>
    | <sentencias>

<sentencias> ::= <sentencia> ";"

<sentencia> ::= <sentencia_ddl>
    | <sentencia_dml>

<sentencia_ddl> ::= <crear>
    | <liberar>

<sentencia_dml> ::= <insertar>
    | <actualizar>
    | <eliminar>
    | <seleccionH>
    | <mostrar>
    | <altert>

<seleccionH>  ::= <selecccionHP> "UNION" <seleccionar>

<seleccionHP> ::="UNION" <seleccionar> <seleccionHP>
    | "INTERSECT" <seleccionar> <selecccionHP>
    | "EXCEPT"  <seleccionar> <selecccionHP>
    | "UNION" "ALL"  <seleccionar> <selecccionHP>
    | "INTERSECT" "ALL" <seleccionar> <selecccionHP>
    | "EXCEPT" "ALL" <seleccionar> <selecccionHP>
    | "(" <selecccionHP> ")"
    | ""

<altert> ::= <alterdb>
    | <altertb>

<alterdb> ::= "ALTER" "DATABASE" <ID> <alterdb1>

<alterdb1 ::= "RENAME" "TO" <ID> 
    | "OWNER" "TO" <alterdb2>

<alterdb2> ::= <ID> 
               | "CURRENT_USER"
               | "SESSION_USER"

<altertb> ::= "ALTER" "TABLE" <ID> <altertb1>

<altertb1> ::= <alttbadd> 
    | <alttbdrop>
    | <alttbalterv>
    | <alttbname>

<alttbname> ::= "RENAME" <alttbrename1>

<alttbrename1> ::= "COLUMN" <ID> "TO" <ID> 
    | <ID> "TO" <ID> 
    | "CONSTRAINT" <ID> "TO" <ID>
    | "TO" <ID>

<alttbadd2> ::= <alttbadd3> <alttbadd2P>

<alttbadd2P> ::= <alttbadd3> <alttbadd2P>
    | ""

<alttbadd3> ::= "CHECK" "(" <exp> ")"
    | "UNIQUE" "(" <CADENA1> ")"
    | "PRIMARY" "KEY" "(" <CADENA1> ")"
    | "FOREIGN" "KEY" "(" <CADENA1> ")" "REFERENCES"  <ID> "(" <CADENA1> ")"

<insertar> ::= "INSERT" "INTO" <ID> "VALUES" "(" <lista_exp> ")"

<actualizar> ::= "UPDATE" <ID> "SET" <exp> "WHERE" <exp>

<eliminar> ::= "DELETE" "FROM" <ID> "WHERE" <exp>

<seleccionar> ::= <seleccionar1> "LIMIT" <ENTERO> <offsetop>
    | <seleccionar1> "LIMIT" "ALL" <offsetop>
    | <seleccionar1> <offsetop>
    | <seleccionar1> "LIMIT" "ENTERO"
    | <seleccionar1> "LIMIT" "ALL"
    | <seleccionar1>

<extract> ::= "EXTRACT" "(" <extract1>  "FROM" <timestamp>  <valoresdefault>  ")"
    | "DATE_PART" "(" <valoresdefault> "," <interval> <valoresdefault>  ")"
    | <nowf>
    | "CURRENT_DATE"
    | "CURRENT_TIME"
    | <timestamp> <valoresdefault>

<nowf> ::= "NOW" "(" ")"

<extract1> ::= "YEAR"
    | "MONTH"
    | "DAY"
    | "HOUR"
    | "MINUTE"
    | "SECOND"
    | <CADENA1>
    | <CADENA2>

<offsetop> ::= "OFFSET" <ENTERO>

<seleccionar1> ::= "SELECT" <cantidad_select> <parametros_select> <cuerpo_select> 
    | "SELECT" <funcion_math> <alias_name>
    | "SELECT" <funcion_date>
    | "SELECT" <funcionGREALEAST>
    | "SELECT" <extract>

<funcionGREALEAST> : "GREATEST" "(" <exp> ")"
    | "LEAST" "(" <exp> ")"

<cantidad_select> ::= "DISTINCT"
    | ""

<parametros_select> ::= "*"
    | <lista_select>

<lista_select> ::= <value_select> <lista_selectP>

<lista_selectP> ::= "," <value_select> <lista_selectP>
    | ""

<value_select> ::= <columna_name> <alias_name>
    | <ID> "." "*" <alias_name>
    | <funcion_math> <alias_name>
    | "(" <seleccionar> ")" <alias_name>
    | <case>

<case> ::= "CASE" <loop_condition>  "END" 
    | "CASE" <loop_condition>  "END" "AS" <ID>
    | "CASE" <loop_condition>  <else>  "END" 
    | "CASE" <loop_condition>  <else> "END" "AS" <ID>
    | "(" <case> ")"

<loop_condition> ::= "WHEN" <exp> "THEN" <resultV> <loop_conditionP>

<loop_conditionP> ::= "WHEN" <exp> "THEN" <resultV> <loop_conditionP>
    | ""

<else> ::= "ELSE" <resultV>

<resultV> ::= <ENTERO>
    | <DECIMAL>
    | <CADENA1>
    | <CADENA2>
    | <ID>
    | "(" <resultV> ")"

<columna_name> : <ID>
    | <ID> "." <ID>

<list_colum> ::= <columna_name> <list_columP>

<list_columP> ::= "," <columna_name> <list_columP>
    | ""  

<sub_query> ::= "EXISTS"
    | <exp>
    | <exp> "NOT" "IN"
    | <exp> "IN"

<cuerpo_select> ::= <bloque_from> <bloque_join> <bloque_where> <bloque_group> <bloque_having> <bloque_order>

<bloque_from> ::= "FROM" <lista_tablas>

<lista_tablas> ::= <value_from> <lista_tablasP>

<lista_tablasP> ::= "," <value_from> <lista_tablasP>
    | ""

<value_from> ::= <tabla_name>
    | "(" <seleccionar> ")" <ID>
    | "(" <seleccionar> ")" "AS" <ID>

<tabla_name> ::= <ID>
    | <ID> <ID>

<bloque_join> ::= <lista_joins> <bloque_joinP>

<bloque_joinP> ::= <lista_joins> <bloque_joinP>
    | ""

<lista_joins> ::= "NATURAL" <tipo_joins> <tabla_name> "ID"
    | <tipo_joins> "JOIN" <tabla_name> "ON" <condicion_boleana>
    | <tipo_joins> "JOIN" <tabla_name> "USING" "(" <list_colum> ")"

<tipo_joins> ::= "INNER"
    | <value_join>
    | <value_join> "OUTER"

<value_join> ::= "LEFT"
    | "RIGHT"
    | "FULL"

<bloque_where> ::= "WHERE" <cuerpo_where>
    | ""

cuerpo_where ::= <condicion_boleana>
    | <sub_query> "(" <seleccionar> ")" <alias_name>

<bloque_group> ::= "GROUP" "BY" <list_colum>
    | ""

<bloque_having ::= "HAVING" <condicion_boleana>
    | ""

<bloque_order> ::= "ORDER" "BY" <lista_order>
    | ""

<lista_order> ::= <value_order> <lista_orderP>

<lista_orderP> ::= "," <value_order> <lista_orderP>

<lista_orderP> ::= "," <case> <lista_orderP>
    | ""

<value_order> ::= <ID> <value_direction> <value_rang>

<value_direction> ::= "ASC"
    | "DESC"
    | ""

<value_rang> ::= "NULLS" "FIRST"
    | "NULLS" "LAST"
    | "NULLS" "FIRST" "NULLS" "LAST"
    | "NULLS" "LAST" "NULLS" "FIRST"
    | ""

<alias_name> ::= <valoralias>
    | "AS" <valoralias>
    | ""

<valoralias> ::= <ID>
    | <CADENA1>
    | <CADENA2>

<condicion_boleana> ::= <exp>

<funcion_math> ::= "ABS" "(" <exp> ")"
    | "CBRT" "(" <exp> ")"
    | "CEIL" "(" <exp> ")"
    | "CEILING" "(" <exp> ")"
    | "DEGREES" "(" <exp> ")"
    | "DIV" "(" <lista_exp> ")"
    | "EXP" "(" <exp> ")"
    | "factorial" "(" <exp> ")"
    | "FLOOR" "(" <exp> ")"
    | "GCD" "(" <lista_exp> ")"
    | "LN" "(" <exp> ")"
    | "LOG" "(" <exp> ")"
    | "MOD" "(" <lista_exp> ")"
    | "PI" "(" ")"
    | "POWER" "(" <lista_exp> ")"
    | "RADIANS" "(" <exp> ")"
    | "ROUND" "(" <exp> ")"
    | "min_scale" "(" <exp> ")"
    | "scale" "(" <exp> ")"
    | "sign" "(" <exp> ")"
    | "sqrt" "(" <exp> ")"
    | "trim_scale" "(" <exp> ")"
    | "TRUNC" "(" <lista_exp> ")" 
    | "random" "(" ")"
    | "setseed" "(" <exp> ")"
    | "ACOS" "(" <exp> ")"
    | "ACOSD" "(" <exp> ")"
    | "ASIN" "(" <exp> ")"
    | "ASIND" "(" <exp> ")"
    | "ATAN" "(" <exp> ")"
    | "ATAND" "(" <exp> ")"
    | "ATAN2" "(" <lista_exp> ")"
    | "ATAN2D" "(" <lista_exp> ")"
    | "COS" "(" <exp> ")"
    | "COSD" "(" <exp> ")"
    | "COT" "(" <exp> ")"
    | "COTD" "(" <exp> ")"
    | "SIN" "(" <exp> ")"
    | "SIND" "(" <exp> ")"
    | "TAN" "(" <exp> ")"
    | "TAND" "(" <exp> ")"
    | "SINH" "(" <exp> ")"
    | "COSH" "(" <exp> ")"
    | "TANH" "(" <exp> ")"
    | "ASINH" "(" <exp> ")"
    | "ACOSH" "(" <exp> ")"
    | "ATANH" "(" <exp> ")"
    | "length" "(" <exp> ")"
    | "substring" "(" <lista_exp> ")"
    | "trim" "(" <valorestrim> exp FROM exp ")"
    | "MD5" "(" <exp> ")"
    | "sha256" "(" <exp> ")"
    | "decode" "(" <exp> <byteaop> "," <lista_exp> ")"
    | "encode" "(" <exp> <byteaop> "," <lista_exp> ")"
    | "get_byte" "(" <exp> ":" <bytea> "," <lista_exp> ")"
    | "set_byte" "(" <exp> ":" <bytea> "," <lista_exp> ")"
    | "substr" "(" <lista_exp> ")"
    | "CONVERT" "(" <exp> "AS" <tipo> ")" 
    | "width_bucket" "(" <lista_exp> ")"
    | ""

<funcion_date> ::= ""

<mostrar> ::= "SHOW" "DATABASES"

<valorestrim> ::= "leading"
    | "trailing"
    | "both"

<byteaop> ::= ":" <bytea>
    | ""

<lista_exp> ::= <exp> <lista_expP>

<lista_expP> ::= "," <exp> <lista_expP>
    | ""

<exp> ::= <exp_log>
    | <exp_rel>
    | <exp_ar>
    | <exp_select>
    | <expresion_patron>
    | <E>

<exp_log> ::= "NOT" <exp>
    | <exp> "AND" <exp>  
    | <exp> "OR" <exp>

<expresion_patron> ::= <exp> "BETWEEN" <exp>
    | <exp> "IN" <exp>
    | <exp> "NOT" "IN" <exp>
    | <exp> "LIKE" <exp>
    | <exp> "NOT" "LIKE"  <exp>
    | <exp> "ILIKE" <exp>
    | <exp> "NOT" "ILIKE"  <exp>
    | <exp> "SIMILAR" "TO" <exp>
    | <exp> "NOT" "SIMILAR" "TO" <exp>
    | <exp> "," <exp>

<exp_rel> ::= <exp> <toperador> <exp>

<toperador> ::= <IGUAL>
    | <DESIGUAL>
    | <DESIGUAL2>
    | <MAYORIGUAL>
    | <MENORIGUAL>
    | <MAYOR>
    | <MENOR>

<exp_ar> ::= <exp> <SUMA> <exp>
    | <exp> <RESTA> <exp>
    | <exp> <ASTERISCO> <exp>
    | <exp> <DIVISION> <exp>
    | <exp> <POTENCIA> <exp>
    | <exp> <MODULO> <exp>

<exp_select> ::= <SQRT2> <exp>
    | <CBRT2> <exp>
    | <exp> <AND2> <exp>
    | <exp> <SQRT2> <exp>
    | <NOT2> <exp>
    | <exp> <XOR> <exp>
    | <exp> <SH_LEFT> <exp>
    | <exp> <SH_RIGHT> <exp>

<E> ::= <ENTERO>
    | <DECIMAL>
    | <CADENA1>
    | <CADENA2>
    | <ID>
    | <ID> "." <ID>
    | "(" <exp> ")"
    | "ANY"
    | "ALL"
    | "SOME"
    | "IN"
    | <seleccionar>
    | <funcion_math>
    | "NULL"
    | <lvaloresdefault>
    | "NOT" "IN"

<crear> ::= "CREATE" <reemplazar> "DATABASE" <verificacion> <ID> <propietario> <modo>
    | "CREATE" "TABLE" <ID> "(" <columnas> ")" <herencia>
    | "CREATE" "TYPE" <ID> "AS" "ENUM" ""(""<lista_exp> "")""

<reemplazar> ::= "OR" "REPLACE"
    | ""

<verificacion> ::= "IF" "NOT" "EXISTS"
    | ""

<propietario> ::= "OWNER" <valorowner>
    | ""

<valorowner> ::= <ID>
    | <IGUAL> <ID>

<modo> ::= "MODE" <valormodo>
    | ""

<valormodo> ::= <ENTERO>
    | <IGUAL> <ENTERO>

<herencia> ::= "INHERITS" "(" <ID> ")"
    | ""

<columnas> ::= <columna> <columnasP>

<columnasP> ::= "," <columna> <columnasP>
    | ""

<columna> ::= <ID> <tipo> <valortipo> <zonahoraria> <atributocolumn>
    | "PRIMARY" "KEY" "(" <lnombres> ")"
    | "FOREIGN" "KEY" "(" <lnombres> ")" "REFERENCES" <ID> "(" <lnombres> ")"

<tipo> ::= "smallint"
    | "integer"
    | "bigint"
    | "decimal"
    | "numeric"
    | "real"
    | "double" "precision"
    | "money"
    | "character" "varying"
    | "character"
    | "char"
    | "varchar"
    | "text"
    | "date"
    | "timestamp"
    | "time"
    | "interval"
    | "boolean"

<valortipo> ::= "(" <lvaloresdefault> ")"
    | <lvaloresdefault>
    | ""

<zonahoraria> ::= "with" "time" "zone"
    | ""

<atributocolumn> ::= <atributo> <atributocolumnP>

<atributocolumnP> ::= <atributo> <atributocolumnP>
    | ""

<atributo> ::= "DEFAULT" <valoresdefault>
    | "CONSTRAINT" <ID>
    | "NULL" 
    | "NOT" "NULL"
    | "UNIQUE"
    | "PRIMARY" "KEY"
    | "CHECK" "(" <lista_exp> ")"
    | ""

<lvaloresdefault> ::= <valoresdefault> <lvaloresdefaultP>

<lvaloresdefaultP> ::= "," <valoresdefault> <lvaloresdefaultP>
    | ""

<valoresdefault> ::= <CADENA1>
    | <CADENA2>
    | <DECIMAL>
    | <ENTERO>
    | <BOOLEAN>
    | "YEAR"
    | "MONTH"
    | "DAY"
    | "SECOND"
    | "MINUTE"
    | "HOURS"

<lnombres> ::= <ID> <lnombresP>

<lnombresP> ::= "," <ID> <lnombresP>
    | ""

<liberar> ::= "DROP" "TABLE" <existencia> <ID>
    | "DROP" "DATABASE" <existencia> <ID>

<existencia> ::= "IF" "EXISTS"
                  | ""
```