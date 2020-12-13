# Gramatica Recursiva Por La Izquierda
```sh
<INICIO> ::= <SENTENCIAS>

<SENTENCIAS> ::= <SENTENCIAS> ";" <SENTENCIA>
    | <SENTENCIA>
    | ";" 

<SENTENCIA> ::= <SENTENCIAS_DDL> 
    | <SENTENCIAS DML> 

<SENTENCIAS_DDL> ::= <CREATE>
    | <ALTER>
    | <DROP>
    | <TRUNCATE>
    
<SENTENCIAS_DML> ::= <SELECT>
    | <INSERT>
    | <UPDATE>    
    | <DELETE>
    | <SHOW> 
```
### Sentencias DDL
```sh
<CREAR> ::= <CREARBASE> | <CREARTABLA> | <CREARTYPE>

<CREARBASE> ::= "CREATE" <att1> "DATABASE" <att2> <string> <att3> <att4>

<att1> ::= "or replace" | ""

<att2> ::= "if not exists" | ""

<att3> ::= "OWNER" <string> |"OWNER" "=" <string> | ""

<att4> ::= "MODE" <int> | "MODE" "=" <int> |""

<CREARTYPE> ::= "CREATE" <TYPE> <string>  "AS" "ENUM" "(" <Lstring> ")"

<CREARTABLA> ::= "CREATE TABLE" <string> "(" <COLUMNAS> ")" <HERENCIA>

<HERENCIA> ::=  "INHERITS" "(" <string> ")" | ""

<COLUMNAS> ::= <COLUMNAS> "," <COLUMNA>
    | <COLUMNA> <COLUMNA2> 
    | <COLUMNA> 

<COLUMNA> ::= <string> <TIPODATO> <ATRIBUTOCOLUM>

<COLUMNA2> ::= <COLUMNA2> ","  "CONSTRAINT" <string> <COLUMNA3>
    | <COLUMNA2> "," <COLUMNA3>
    | ","  "CONSTRAINT" <string> <COLUMNA3>
          | "," <COLUMNA3>

<COLUMNA3> ::= "CHECK" "(" <ConditionMultiColum> ")"
    | "UNIQUE" "("  <Lstrings>  ")"
    | "PRIMARY KEY" "(" <Lstrings> ")"
    | "FOREIGN  KEY" "(" <Lstrings> ")" "REFERENCES" <string> "(" <Lstring> ")"

<ConditionMultiColum> ::= <ConditionMultiColum> <ConditionColumn>
                 | <ConditionColumn>

<ATRIBUTOCOLUM> ::= <ATRIBUTOCOLUM> <ATRIBUTO>
    |<ATRIBUTO>

<ATRIBUTO> ::= "CONSTRAINT" <string>  <ATRIBUTO2>
    | <ATRIBUTO2>              

<ATRIBUTO2> ::=  "DEFAULT" <VALORES>
    | "NOT NULL"
    | "NULL" 
    | "UNIQUE"
    | "CHECK" "(" <ConditionColumn> ")"
    | "PRIMARY KEY"





```
### Sentencias DML
```sh
```
### DATOS
```sh
<TIPODATO> ::= "integer" | "char" | "date" |[...]
<VALORES> ::= <digito> | <decimal> | <string>
```
