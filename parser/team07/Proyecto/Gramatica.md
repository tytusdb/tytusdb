# Gramatica TytusDB
## Gramatica LL

<p>&ltinit&gt ::= &ltinstrucciones&gt</p><br>

<p>&ltintrucciones &gt ::= &ltintrucciones&gt &ltinstruccion&gt</p>
<p style="text-indent: 8em;">
 | &ltinstruccion&gt </p><br>

<h4>&ltinstruccion&gt ::= &ltcrear_instr&gt</h4>
<h4 style="text-indent: 8em;">
 | &ltinsert_table&gt <br></h4>
 <h4 style="text-indent: 8em;">
 | &ltdelete_table&gt <br></h4>
 <h4 style="text-indent: 8em;">
 | &ltupdate_table&gt <br></h4>
 <h4 style="text-indent: 8em;">
 | &ltcrear_instr&gt <br></h4>
 <h4 style="text-indent: 8em;">
 | &ltalter_instr&gt <br></h4>
 <h4 style="text-indent: 8em;">
 | &ltdrop_instr&gt <br></h4><br>

 <h4>&ltcrear_instr&gt ::= CREATE TABLE id '(' &ltcolumnas&gt ')' &ltherencia&gt ';'</h4>
 <h4 style="text-indent: 7em;">
 | CREATE &ltopReplace&gt DATABASE &ltopExists&gt id &ltopDatabase&gt ';' <br></h4>
 <h4 style="text-indent: 7em;">
 | CREATE TYPE id AS ENUM '(' id ')' ';' </h4><br>

<h4>&ltinsert_table&gt ::= INSERT INTO id VALUES &ltlista_valores&gt ';'</h4>
<h4 style="text-indent: 8em;">
| INSERT INTO id '('  &ltlista_columnas&gt ')' VALUES &ltlista_valores&gt ';' </h4>
<h4 style="text-indent: 8em;">
| INSERT INTO id DEFAULT VALUES ';' </h4>
<h4 style="text-indent: 8em;">
| INSERT INTO id '(' &ltlista_columnas&gt ')' DEFAULT VALUES ';' </h4><br>

<h4>&ltlista_columnas&gt ::= &ltlista_columnas&gt ',' id</h4>
<h4 style="text-indent: 9em;">
| id </h4><br>

<h4>&ltlista_valores&gt ::= &ltlista_valores&gt ',' &lttupla&gt</h4>
<h4 style="text-indent: 8em;">
| &lttupla&gt </h4><br>

<h4>&lttupla&gt ::= '(' &ltlista_expresiones&gt ')'</h4><br>

<h4>&ltlista_expresiones&gt ::= &ltlista_expresiones&gt ',' &ltexpresion&gt</h4>
<h4 style="text-indent: 10em;">
| &ltexpresion&gt </h4><br>

<h4>&ltexpresion&gt ::= cadena</h4>
<h4 style="text-indent: 7em;">
| entero </h4>
<h4 style="text-indent: 7em;">
| decimal_ </h4><br>

<h4>&ltdelete_table&gt ::= DELETE FROM id ';'</h4>
<h4 style="text-indent: 8em;">
| DELETE FROM id WHERE &ltexp_operacion&gt ';' </h4><br>

<h4>&ltexp_operacion&gt ::= &ltexp_logica&gt </h4><br>

<h4>&ltexp_logica&gt ::= &ltexp_logica&gt OR &ltexp_logica&gt</h4>
<h4 style="text-indent: 7em;">
| &ltexp_logica&gt AND &ltexp_logica&gt </h4>
<h4 style="text-indent: 7em;">
| NOT &ltexp_logica&gt </h4>
<h4 style="text-indent: 7em;">
| &ltexp_relacional&gt </h4><br>

<h4>&ltexp_relacional&gt ::= &ltexp_relacional&gt '<' &ltexp_relacional&gt</h4>
<h4 style="text-indent: 9em;">
| &ltexp_relacional&gt '<=' &ltexp_relacional&gt </h4>
<h4 style="text-indent: 9em;">
| &ltexp_relacional&gt '>' &ltexp_relacional&gt </h4>
<h4 style="text-indent: 9em;">
| &ltexp_relacional&gt '>=' &ltexp_relacional&gt </h4>
<h4 style="text-indent: 9em;">
| &ltexp_relacional&gt '<>' &ltexp_relacional&gt </h4>
<h4 style="text-indent: 9em;">
| &ltexp_relacional&gt '!=' &ltexp_relacional&gt </h4>
<h4 style="text-indent: 9em;">
| &ltexp_relacional&gt '=' &ltexp_relacional&gt </h4>
<h4 style="text-indent: 9em;">
| &ltexp_aritmetica&gt </h4><br>

<h4>&ltexp_aritmetica&gt ::= &ltexp_aritmetica&gt '+' &ltexp_aritmetica&gt</h4>
<h4 style="text-indent: 9em;">
| &ltexp_aritmetica&gt '-' &ltexp_aritmetica&gt </h4>
<h4 style="text-indent: 9em;">
| &ltexp_aritmetica&gt '*' &ltexp_aritmetica&gt </h4>
<h4 style="text-indent: 9em;">
| &ltexp_aritmetica&gt '/' &ltexp_aritmetica&gt </h4>
<h4 style="text-indent: 9em;">
| &ltexp_aritmetica&gt '%' &ltexp_aritmetica&gt </h4>
<h4 style="text-indent: 9em;">
| &ltexp_aritmetica&gt '^' &ltexp_aritmetica&gt </h4>
<h4 style="text-indent: 9em;">
| &ltexp_aritmetica&gt BETWEEN &ltexp_aritmetica&gt AND &ltexp_aritmetica&gt </h4>
<h4 style="text-indent: 9em;">
| &ltexp_aritmetica&gt NOT BETWEEN &ltexp_aritmetica&gt AND &ltexp_aritmetica&gt </h4>
<h4 style="text-indent: 9em;">
| &ltexp_aritmetica&gt IN '(' &ltlista_expresiones&gt ')' </h4>
<h4 style="text-indent: 9em;">
| &ltexp_aritmetica&gt NOT IN '(' &ltlista_expresiones&gt ')' </h4>
<h4 style="text-indent: 9em;">
| LIKE &ltexp_aritmetica&gt </h4>
<h4 style="text-indent: 9em;">
| NOT LIKE &ltexp_aritmetica&gt </h4>
<h4 style="text-indent: 9em;">
| ILIKE &ltexp_aritmetica&gt </h4>
<h4 style="text-indent: 9em;">
| NOT ILIKE &ltexp_aritmetica&gt </h4>
<h4 style="text-indent: 9em;">
| &ltexp_aritmetica&gt SIMILAR TO &ltexp_aritmetica&gt </h4>
<h4 style="text-indent: 9em;">
| &ltexp_aritmetica&gt IS NULL </h4>
<h4 style="text-indent: 9em;">
| &ltexp_aritmetica&gt IS NOT NULL </h4>
<h4 style="text-indent: 9em;">
| &ltprimitivo&gt </h4><br>

<h4>&ltprimitivo&gt ::= id</h4>
<h4 style="text-indent: 7em;">
| '+' &ltprimitivo&gt </h4>
<h4 style="text-indent: 7em;">
| '-' &ltprimitivo&gt </h4>
<h4 style="text-indent: 7em;">
| '(' &ltexp_operacion&gt ')' </h4><br>

<h4>&ltprimitivo&gt ::= entero</h4>
<h4 style="text-indent: 7em;">
| decimal_ </h4>
<h4 style="text-indent: 7em;">
| cadena </h4>
<h4 style="text-indent: 7em;">
| TRUE </h4>
<h4 style="text-indent: 7em;">
| FALSE </h4><br>

<h4>&ltupdate_table&gt ::= UPDATE id SET &ltlista_seteos&gt ';'</h4>
<h4 style="text-indent: 8em;">
| UPDATE id SET &ltlista_seteos&gt WHERE &ltexp_operacion&gt ';' </h4><br>

<h4>&ltlista_seteos&gt ::= &ltlista_seteos&gt ',' &ltset_columna&gt</h4>
<h4 style="text-indent: 8em;">
| &ltset_columna&gt </h4><br>

<h4>&ltset_columna&gt ::= id '=' &ltexp_operacion&gt</h4><br>

<h4>&ltcolumnas&gt ::= &ltcolumnas&gt ',' &ltcolumna&gt</h4>
<h4 style="text-indent: 7em;">
| &ltcolumna&gt </h4><br>

<h4>&ltcolumna&gt ::= id &lttipos&gt &ltopcional&gt</h4>
<h4 style="text-indent: 7em;">
| PRIMARY KEY '(' &ltidentificadores&gt ')' </h4>
<h4 style="text-indent: 7em;">
| FOREIGN KEY '(' &ltidentificadores&gt ')' REFERENCES id '(' &ltidentificadores&gt ')' </h4>
<h4 style="text-indent: 7em;">
| UNIQUE '(' &ltidentificadores&gt ')' </h4><br>

<h4>&ltopcional&gt ::= DEFAULT &ltopcionNull&gt</h4>
<h4 style="text-indent: 7em;">
| &ltopcionNull&gt </h4><br>

<h4>&ltopcionNull&gt ::= NULL &ltopConstraint&gt</h4>
<h4 style="text-indent: 7em;">
| NOT NULL &ltopConstraint&gt </h4>
<h4 style="text-indent: 7em;">
| &ltopConstraint&gt </h4><br>

<h4>&ltopConstraint&gt ::= CONSTRAINT id &ltopUniqueCheck&gt</h4>
<h4 style="text-indent: 8em;">
| &ltopUniqueCheck&gt </h4><br>

<h4>&ltopUniqueCheck&gt ::= UNIQUE</h4>
<h4 style="text-indent: 10em;">
| CHECK '(' &ltcondicion_check&gt ')' </h4>
<h4 style="text-indent: 10em;">
| λ </h4><br>

<h4>&ltcondicion_check&gt ::= id '<' &ltexpresion&gt</h4>
<h4 style="text-indent: 10em;">
| id '<=' &ltexpresion&gt </h4>
<h4 style="text-indent: 10em;">
| id '>' &ltexpresion&gt </h4>
<h4 style="text-indent: 10em;">
| id '>=' &ltexpresion&gt </h4>
<h4 style="text-indent: 10em;">
| id '<>' &ltexpresion&gt </h4>
<h4 style="text-indent: 10em;">
| id '!=' &ltexpresion&gt </h4>
<h4 style="text-indent: 10em;">
| id '=' &ltexpresion&gt </h4><br>

<h4>&ltherencia&gt ::= INHERITS '(' id ')'</h4>
<h4 style="text-indent: 7em;">
| λ </h4><br>

<h4>&ltidentificadores&gt ::= &ltidentificadores&gt ',' id</h4>
<h4 style="text-indent: 9em;">
| id </h4><br>

<h4>&ltcadenas&gt ::= &ltcadenas&gt ',' cadena</h4>
<h4 style="text-indent: 7em;">
| cadena </h4><br>

<h4>&ltioReplace&gt ::= OR REPLACE</h4>
<h4 style="text-indent: 7em;">
| λ </h4><br>

<h4>&ltopExists&gt ::= IF NOT EXISTS</h4>
<h4 style="text-indent: 7em;">
| λ </h4><br>

<h4>&ltopDatabase&gt ::= OWNER &ltopIgual&gt id &ltmode&gt</h4>
<h4 style="text-indent: 8em;">
| &ltmode&gt </h4><br>

<h4>&ltopIgual&gt ::= '='</h4>
<h4 style="text-indent: 6em;">
| λ </h4><br>

<h4>&ltmode&gt ::= MODE &ltopIgual&gt entero</h4>
<h4 style="text-indent: 5em;">
| λ </h4><br>

<h4>&ltalter_instr&gt ::= ALTER DATABASE id &ltopAlterDatabase&gt ';'</h4>
<h4 style="text-indent: 7em;">
| ALTER TABLE id &ltalter_table_instr&gt ';' </h4><br>

<h4>&ltopAlterDatabase&gt ::= RENAME TO id</h4>
<h4 style="text-indent: 10em;">
| OWNER TO &ltownerList&gt</h4><br>

<h4>&ltownerList&gt ::= id</h4>
<h4 style="text-indent: 7em;">
| CURRENT_USER</h4>
<h4 style="text-indent: 7em;">
| SESSION_USER</h4><br>

<h4>&ltalter_table_instr&gt ::= ADD &ltadd_instr&gt</h4>
<h4 style="text-indent: 10em;">
| &ltalter_columnas&gt</h4>
<h4 style="text-indent: 10em;">
| &ltdrop_columnas&gt</h4>
<h4 style="text-indent: 10em;">
| DROP CONSTRAINT id</h4><br>

<h4>&ltalter_columnas&gt ::= &ltalter_columnas&gt ',' &ltalter_columna&gt</h4>
<h4 style="text-indent: 9em;">
| &ltalter_columna&gt </h4><br>

<h4>&ltalter_columna&gt ::= ALTER COLUMN id &ltalter_column_instr&gt</h4><br>

<h4>&ltdrop_columnas&gt ::= &ltdrop_columnas&gt ',' &ltdrop_columna&gt</h4>
<h4 style="text-indent: 9em;">
| &ltdrop_columna&gt </h4><br>

<h4>&ltdrop_columna&gt ::= DROP COLUMN id </h4><br>

<h4>&ltalter_table_instr&gt ::= DROP COLUMN id </h4><br>

<h4>&ltadd_instr&gt ::= CHECK '(' &ltcondicion_check&gt ')'</h4>
<h4 style="text-indent: 7em;">
| CONSTRAINT id UNIQUE '(' id ')' </h4><br>

<h4>&ltalter_column_instr&gt ::= SET NOT NULL</h4>
<h4 style="text-indent: 11em;">
| SET NULL</h4>
<h4 style="text-indent: 11em;">
| TYPE &lttipos&gt</h4><br>

<h4>&ltdrop_instr&gt ::= DROP DATABASE &ltsi_existe&gt id ';'</h4>
<h4 style="text-indent: 7em;">
| DROP TABLE id ';' </h4><br>

<h4>&ltsi_existe&gt ::= IF EXISTS</h4>
<h4 style="text-indent: 7em;">
| λ </h4><br>

<h4>&lttipos&gt ::= SMALLINT</h4>
<h4 style="text-indent: 5em;">
| SERIAL </h4>
<h4 style="text-indent: 5em;">
| INTEGER </h4>
<h4 style="text-indent: 5em;">
| BIGINIT </h4>
<h4 style="text-indent: 5em;">
| DECIMAL </h4>
<h4 style="text-indent: 5em;">
| NUMERIC </h4>
<h4 style="text-indent: 5em;">
| REAL </h4>
<h4 style="text-indent: 5em;">
| DOUBLE </h4>
<h4 style="text-indent: 5em;">
| MONEY </h4>
<h4 style="text-indent: 5em;">
| VARCHAR </h4>
<h4 style="text-indent: 5em;">
| CHARACTER </h4>
<h4 style="text-indent: 5em;">
| TEXT </h4>
<h4 style="text-indent: 5em;">
| TIMESTAMP </h4>
<h4 style="text-indent: 5em;">
| TIME </h4>
<h4 style="text-indent: 5em;">
| DATE </h4>
<h4 style="text-indent: 5em;">
| INTERVAL </h4>
<h4 style="text-indent: 5em;">
| BOOLEAN </h4><br>
