## GRUPO #11 
# *REPORTE GRAMATICAL DE LA EJECUCION*

### Instruccion #1 
```bnf
<createDB_instr> ::= CREATE DATABASE  <existencia>
<existencia> ::= IF NOT EXISTS "test"  <state_owner>
<state_owner> ::= OWNER IGUAL " root"  <state_mode>
<state_mode> ::= MODE IGUAL "1"  PTCOMA
```

### Instruccion #2 
```bnf
<createDB_instr> ::= CREATE DATABASE  <existencia>
<existencia> ::= IF NOT EXISTS "califica"  <state_owner>
<state_owner> ::= OWNER IGUAL " root"  <state_mode>
<state_mode> ::= MODE IGUAL "2"  PTCOMA
```

### Instruccion #3 
```bnf
<createDB_instr> ::= CREATE DATABASE  <existencia>
<existencia> ::= IF NOT EXISTS "califica2"  <state_owner>
<state_owner> ::= OWNER IGUAL " root"  <state_mode>
<state_mode> ::= MODE IGUAL "3"  PTCOMA
```

### Instruccion #4 
```bnf
<use_instr> ::= USE "test"  PTCOMA
```

### Instruccion #5 
```bnf
<create_table> : "CREATE" "TABLE" ID "PARIZQ" <list_columns_x> "PARDER" <end_create_table>
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<primary_key> ::= "PRIMARY" "KEY"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

```

### Instruccion #6 
```bnf
<create_table> : "CREATE" "TABLE" ID "PARIZQ" <list_columns_x> "PARDER" <end_create_table>
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<primary_key> ::= "PRIMARY" "KEY"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<constraint_field> ::= "UNIQUE"
<constraint_field> ::= "CONSTRAINT" ID <check_unique>
<constraint_field> ::= "CHECK" "PARIZQ" <condiciones> "PARDER"
<constraint_field> ::= <empty>

<null_field> ::= "NOT" "NULL"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

```

### Instruccion #7 
```bnf
<create_table> : "CREATE" "TABLE" ID "PARIZQ" <list_columns_x> "PARDER" <end_create_table>
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<primary_key> ::= "PRIMARY" "KEY"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

```

### Instruccion #8 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
```

### Instruccion #9 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
```

### Instruccion #10 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
```

### Instruccion #11 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
```

### Instruccion #12 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
```

### Instruccion #13 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
```

### Instruccion #14 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
```

### Instruccion #15 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
```

### Instruccion #16 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
```

### Instruccion #17 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
```

### Instruccion #18 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
```

### Instruccion #19 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
```

### Instruccion #20 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
```

### Instruccion #21 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
```

### Instruccion #22 
```bnf
<create_enum> ::= "CREATE" "TYPE" ID "AS" "ENUM" "PARIZQ" <list_string> "PARDER" "PTCOMA"
<list_string> ::= <cualquiercadena>
<list_string> ::= <list_string> "COMA" <cualquiercadena>

<list_string> ::= <list_string> "COMA" <cualquiercadena>

<list_string> ::= <list_string> "COMA" <cualquiercadena>

<list_string> ::= <list_string> "COMA" <cualquiercadena>

```

### Instruccion #23 
```bnf
<showDB_instr> ::= SHOW DATABASES PTCOMA
```

### Instruccion #24 
```bnf
<dropDB_instr> ::= DROP DATABASE IF EXISTS "califica2" PTCOMA
```

### Instruccion #25 
```bnf
<drop_table> ::= "DROP" "TABLE" ID "PTCOMA"

```

### Instruccion #26 
```bnf
<create_table> : "CREATE" "TABLE" ID "PARIZQ" <list_columns_x> "PARDER" <end_create_table>
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<primary_key> ::= "PRIMARY" "KEY"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

```

### Instruccion #27 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Funcionalidades basicas"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2.0"
```

### Instruccion #28 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Funciones Date-Extract"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2.0"
```

### Instruccion #29 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbcalifica"
```

### Instruccion #30 
```bnf
<create_table> : "CREATE" "TABLE" ID "PARIZQ" <list_columns_x> "PARDER" <end_create_table>
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

```

### Instruccion #31 
```bnf

<alter_instr> ::= ALTER TABLE ID "ADD" "FOREIGN" "KEY" "PARIZQ" ID "PARDER" "REFERENCES" ID

```

### Instruccion #32 
```bnf

<alter_instr> ::= ALTER TABLE ID "ADD" "FOREIGN" "KEY" "PARIZQ" ID "PARDER" "REFERENCES" ID

```

### Instruccion #33 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Administrador"
```

### Instruccion #34 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Admin"
```

### Instruccion #35 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Ventas"
```

### Instruccion #36 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbrol"
```

### Instruccion #37 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Type"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2.0"
```

### Instruccion #38 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "4"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Create Database-replace"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3.0"
```

### Instruccion #39 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Show Database"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2.0"
```

### Instruccion #40 
```bnf

<alter_instr> ::= ALTER TABLE ID add COLUMN <listtablas>

<list_columns> ::= ID <type_column>
```

### Instruccion #41 
```bnf
<update_instr> ::= "UPDATE" ID "SET" <asignaciones> "PTCOMA"

<asignaciones> ::= <asignacion>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
```

### Instruccion #42 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "6"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Database-Alter,drop"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "4.0"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
```

### Instruccion #43 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "7"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Create Table- Variantes"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "4.0"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
```

### Instruccion #44 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Luis Fernando"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Salazar Rodriguez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "lsalazar"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "paswword"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "now"
```

### Instruccion #45 
```bnf

<alter_instr> ::= ALTER TABLE ID <list_alter_column>

<list_alter_column> ::= "ALTER" "COLUMN" ID "TYPE" <type_column>

```

### Instruccion #46 
```bnf
<create_table> : "CREATE" "TABLE" ID "PARIZQ" <list_columns_x> "PARDER" <end_create_table>
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<primary_key> ::= "PRIMARY" "KEY"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

```

### Instruccion #47 
```bnf
<drop_table> ::= "DROP" "TABLE" ID "PTCOMA"

```

### Instruccion #48 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "8"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Drop table"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2.0"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
```

### Instruccion #49 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "9"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Alter table"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "4.0"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
```

### Instruccion #50 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Luis Fernando"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Salazar Rodriguez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "lsalazar"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "paswword"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #51 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Maria Cristina"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Lopez Ramirez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "mlopez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Diciembre"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #52 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Hugo Alberto"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Huard Ordoñez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hhuard"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Rafael"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #53 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Luis Fernando"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Salazar Rodriguez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "lsalazar"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "paswword"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #54 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Maria Cristina"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Lopez Ramirez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "mlopez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Diciembre"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #55 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Hugo Alberto"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Huard Ordoñez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hhuard"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Rafael"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #56 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Hugo Alberto"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Huard Ordoñez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hhuard"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Rafael"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #57 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "4"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Pedro Peter"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Parker"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "ppeter"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Donatelo"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #58 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Mariana Elizabeth"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Zahabedra Lopez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "melizabeth"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Miguel123"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #59 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "6"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Lisa Maria"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Guzman"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "lmaria"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Diciembre$$2020"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #60 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "7"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Aurelio"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Baldor"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "abaldor"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Algebra$*"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #61 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "8"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Elizabeth Taylor"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Juarez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "etaylor"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hilbilly"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #62 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "9"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Lois"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Lane"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "llane"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "smallville"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #63 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbusuario"
```

### Instruccion #64 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #65 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
```

### Instruccion #66 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
```

### Instruccion #67 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "4"
```

### Instruccion #68 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5"
```

### Instruccion #69 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "6"
```

### Instruccion #70 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "7"
```

### Instruccion #71 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "8"
```

### Instruccion #72 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "9"
```

### Instruccion #73 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbrolxusuario"
```

### Instruccion #74 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "4"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "IT"
```

### Instruccion #75 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Gerencia"
```

### Instruccion #76 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "10"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Duff"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Mackagan"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "dmackagan"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "sweetchild"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #77 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "10"
```

### Instruccion #78 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "11"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Carlos"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Mendez Chingui"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "cmendez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "niebla@@"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #79 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "12"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Diego"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Joachin"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "omendez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "raizanimal"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #80 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "13"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Carlos Mauricio"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Ordoñez Toto"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "cordonez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "radioviejo"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #81 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "14"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Fernando"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Gonzalez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "fgonzalez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "1245678$net"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #82 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "15"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Walter"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Reynoso Alvarado"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "wreynoso"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "corona*virus"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "hola"
```

### Instruccion #83 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "11"
```

### Instruccion #84 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "12"
```

### Instruccion #85 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "13"
```

### Instruccion #86 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbrolxusuario"
```

### Instruccion #87 
```bnf
<create_table> : "CREATE" "TABLE" ID "PARIZQ" <list_columns_x> "PARDER" <end_create_table>
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<primary_key> ::= "PRIMARY" "KEY"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

```

### Instruccion #88 
```bnf
<create_table> : "CREATE" "TABLE" ID "PARIZQ" <list_columns_x> "PARDER" <end_create_table>
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<constraint_field> ::= "UNIQUE"
<constraint_field> ::= "CONSTRAINT" ID <check_unique>
<constraint_field> ::= "CHECK" "PARIZQ" <condiciones> "PARDER"
<constraint_field> ::= <empty>

<primary_key> ::= "PRIMARY" "KEY"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<constraint_field> ::= "UNIQUE"
<constraint_field> ::= "CONSTRAINT" ID <check_unique>
<constraint_field> ::= "CHECK" "PARIZQ" <condiciones> "PARDER"
<constraint_field> ::= <empty>

<check_unique> ::= "UNIQUE"
<check_unique> ::= "CHECK" "PARIZQ" <condiciones> "PARDER"
<check_unique> ::= <empty>

<condiciones> ::= <condicion>
<condicion> ::= <expresion> ">" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "fechadenacimiento"
<cualquiercadena> ::= "1900-01-01"
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<constraint_field> ::= "UNIQUE"
<constraint_field> ::= "CONSTRAINT" ID <check_unique>
<constraint_field> ::= "CHECK" "PARIZQ" <condiciones> "PARDER"
<constraint_field> ::= <empty>

<condiciones> ::= <condicion>
<condicion> ::= <expresion> ">" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "fechacontratacion"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "fechadenacimiento"
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

```

### Instruccion #89 
```bnf

<alter_instr> ::= ALTER TABLE ID "ADD" "FOREIGN" "KEY" "PARIZQ" ID "PARDER" "REFERENCES" ID

```

### Instruccion #90 
```bnf
<create_table> : "CREATE" "TABLE" ID "PARIZQ" <list_columns_x> "PARDER" <end_create_table>
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

```

### Instruccion #91 
```bnf
<create_table> : "CREATE" "TABLE" ID "PARIZQ" <list_columns_x> "PARDER" <end_create_table>
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<end_create_table> ::= "INHERITS" "PARIZQ" ID "PARDER" "PTCOMA"

```

### Instruccion #92 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "capitals"
```

### Instruccion #93 
```bnf
<create_table> : "CREATE" "TABLE" ID "PARIZQ" <list_columns_x> "PARDER" <end_create_table>
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<primary_key> ::= "PRIMARY" "KEY"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

```

### Instruccion #94 
```bnf
<create_table> : "CREATE" "TABLE" ID "PARIZQ" <list_columns_x> "PARDER" <end_create_table>
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<primary_key> ::= "PRIMARY" "KEY"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

```

### Instruccion #95 
```bnf

<alter_instr> ::= ALTER TABLE ID "ADD" "FOREIGN" "KEY" "PARIZQ" ID "PARDER" "REFERENCES" ID

```

### Instruccion #96 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "DPI"
```

### Instruccion #97 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Nit"
```

### Instruccion #98 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Pasaporte"
```

### Instruccion #99 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbidentificaciontipo"
```

### Instruccion #100 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Activo"
```

### Instruccion #101 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Inactivo"
```

### Instruccion #102 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbestado"
```

### Instruccion #103 
```bnf
<insert_instr> ::= "INSERT" "INTO" ID "PARIZQ" <columnas> "PARDER" "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Thelma"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Esquit"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "1981-01-25"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2014-07-06"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #104 
```bnf
<insert_instr> ::= "INSERT" "INTO" ID "PARIZQ" <columnas> "PARDER" "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Maria"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Lopez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "1990-12-01"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2016-09-21"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #105 
```bnf
<insert_instr> ::= "INSERT" "INTO" ID "PARIZQ" <columnas> "PARDER" "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Julio"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Roberto"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Rodriguez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "1985-06-05"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2012-01-22"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #106 
```bnf
<insert_instr> ::= "INSERT" "INTO" ID "PARIZQ" <columnas> "PARDER" "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "4"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Roberto"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Benjamin"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Duque"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "1996-04-09"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2018-10-03"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #107 
```bnf
<insert_instr> ::= "INSERT" "INTO" ID "PARIZQ" <columnas> "PARDER" "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Francisco"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= ""
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Juarez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Perez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "1997-10-05"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2010-03-01"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #108 
```bnf
<insert_instr> ::= "INSERT" "INTO" ID "PARIZQ" <columnas> "PARDER" "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Francisco"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= ""
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Juarez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Perez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "1997-10-05"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2010-03-01"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #109 
```bnf
<insert_instr> ::= "INSERT" "INTO" ID "PARIZQ" <columnas> "PARDER" "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "6"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Bryan"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Jose"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Rodriguez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Santos"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "1900-01-01"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2010-03-01"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #110 
```bnf
<insert_instr> ::= "INSERT" "INTO" ID "PARIZQ" <columnas> "PARDER" "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "6"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Bryan"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Jose"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Rodriguez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Santos"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "1990-02-28"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2012-09-01"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #111 
```bnf
<insert_instr> ::= "INSERT" "INTO" ID "PARIZQ" <columnas> "PARDER" "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "7"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Estefania"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Alejandra"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Soto"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Mazariegos"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2000-08-03"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "1999-09-01"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #112 
```bnf
<insert_instr> ::= "INSERT" "INTO" ID "PARIZQ" <columnas> "PARDER" "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "7"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Estefania"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Alejandra"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Soto"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Mazariegos"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2000-08-03"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2019-09-01"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #113 
```bnf
<insert_instr> ::= "INSERT" "INTO" ID "PARIZQ" <columnas> "PARDER" "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "8"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Katherin"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= ""
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Gonzalez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Lopez"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "1997-10-09"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2018-06-09"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #114 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbempleado"
```

### Instruccion #115 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "4578-784525-6562"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #116 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "8874585-5"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
```

### Instruccion #117 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "1245-488454-7854"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #118 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2610-417055-0101"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #119 
```bnf
<insert_instr> ::= "INSERT" "INTO" ID "PARIZQ" <columnas> "PARDER" "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "8"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "454878-7"
```

### Instruccion #120 
```bnf
<drop_table> ::= "DROP" "TABLE" ID "PTCOMA"

```

### Instruccion #121 
```bnf
<create_table> : "CREATE" "TABLE" ID "PARIZQ" <list_columns_x> "PARDER" <end_create_table>
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<listtablas> ::= ID

<listtablas> ::= <listtablas> "COMA" ID

```

### Instruccion #122 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "4578-784525-6562"
```

### Instruccion #123 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "8874585-5"
```

### Instruccion #124 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "1245-488454-7854"
```

### Instruccion #125 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2610-417055-0101"
```

### Instruccion #126 
```bnf
<insert_instr> ::= "INSERT" "INTO" ID "PARIZQ" <columnas> "PARDER" "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "8"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "454878-7"
```

### Instruccion #127 
```bnf
<insert_instr> ::= "INSERT" "INTO" ID "PARIZQ" <columnas> "PARDER" "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "8"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "12456-1997-0101"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #128 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbempleadoidentificacion"
```

### Instruccion #129 
```bnf
<create_table> : "CREATE" "TABLE" ID "PARIZQ" <list_columns_x> "PARDER" <end_create_table>
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<listtablas> ::= ID

```

### Instruccion #130 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Recepcionista"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "4,000"
```

### Instruccion #131 
```bnf

<alter_instr> ::= ALTER TABLE ID add COLUMN <listtablas>

<list_columns> ::= ID <type_column>
```

### Instruccion #132 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Asistente Contable"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "4,500"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<vallogico> ::= "false"
```

### Instruccion #133 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Contador General"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "9000"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<vallogico> ::= "false"
```

### Instruccion #134 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "4"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Asistente de RRHH"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "4000"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<vallogico> ::= "false"
```

### Instruccion #135 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Recepcionista Gerencia"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "5000"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<vallogico> ::= "false"
```

### Instruccion #136 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "6"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Vendedor 1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2500"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<vallogico> ::= "true"
```

### Instruccion #137 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "7"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Vendedor 2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2750"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<vallogico> ::= "true"
```

### Instruccion #138 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "8"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Vendedor 3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "3000"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<vallogico> ::= "true"
```

### Instruccion #139 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "9"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Jefe de Ventas"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "4000"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<vallogico> ::= "true"
```

### Instruccion #140 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "10"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Jefe de Ventas Regional"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2500"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<vallogico> ::= "true"
```

### Instruccion #141 
```bnf
<create_table> : "CREATE" "TABLE" ID "PARIZQ" <list_columns_x> "PARDER" <end_create_table>
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

```

### Instruccion #142 
```bnf

<alter_instr> ::= ALTER TABLE ID "ADD" "FOREIGN" "KEY" "PARIZQ" ID "PARDER" "REFERENCES" ID

```

### Instruccion #143 
```bnf

<alter_instr> ::= ALTER TABLE ID "ADD" "FOREIGN" "KEY" "PARIZQ" ID "PARDER" "REFERENCES" ID

```

### Instruccion #144 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "ADMINISTRACION"
```

### Instruccion #145 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "CONTABILIDAD"
```

### Instruccion #146 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "CONTABILIDAD"
```

### Instruccion #147 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "4"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "6"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "VENTAS"
```

### Instruccion #148 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "6"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "VENTAS"
```

### Instruccion #149 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> <whereselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbusuario" <alias>
<alias> ::= "US"
<whereselect> ::= "WHERE" <condicioneswhere>
<condicioneswhere> ::= <condicionwhere>
<condicionwhere> ::= <notwhereexists>
<notwhereexists> ::= "NOT" "EXISTS" "PARIZQ" <select_instr1> "PARDER"
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> <whereselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbrolxusuario" <alias>
<alias> ::= "RU"
<whereselect> ::= "WHERE" <condicioneswhere>
<condicioneswhere> ::= <condicionwhere>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "RU" "PUNTO" "idusuario"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "US" "PUNTO" "idusuario"
```

### Instruccion #150 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbrolxusuario"
```

### Instruccion #151 
```bnf
<delete_instr> ::= "DELETE" "FROM" ID "WHERE" <condiciones> "PTCOMA"

<condiciones> ::= <condiciones> "and" <condicion>
<condiciones> ::= <condicion>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "idrol"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "idusuario"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "9"
```

### Instruccion #152 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "9"
```

### Instruccion #153 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbrolxusaurio"
```

### Instruccion #154 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> <whereselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbrol" <alias>
<alias> ::= "R"
<whereselect> ::= "WHERE" <condicioneswhere>
<condicioneswhere> ::= <condicionwhere>
<condicionwhere> ::= <wherenotin>
<wherenotin> ::= <cualquiernumero> "NOT" "IN" "PARIZQ" <select_instr1> "PARDER"
<cualquieridentificador> ::= "idrol"
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
<valselect> ::= "idrol" 
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbrolxusuario"
```

### Instruccion #155 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> <whereselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbrol" <alias>
<alias> ::= "R"
<whereselect> ::= "WHERE" <condicioneswhere>
<condicioneswhere> ::= <condicionwhere>
<condicionwhere> ::= <notwhereexists>
<notwhereexists> ::= "NOT" "EXISTS" "PARIZQ" <select_instr1> "PARDER"
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> <whereselect> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
<valselect> ::= "idrol" 
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbrolxusuario" <alias>
<alias> ::= "RU"
<whereselect> ::= "WHERE" <condicioneswhere>
<condicioneswhere> ::= <condicionwhere>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "RU" "PUNTO" "idrol"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "R" "PUNTO" "idrol"
```

### Instruccion #156 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> <whereselect> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
<valselect> ::= "E" "PUNTO" "ASTERISCO"
<valselect> ::= "estado" 
<valselect> ::= "I" "PUNTO" "identificacion" 
<valselect> ::= "tipoidentificacion" 
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbempleado" <alias>
<alias> ::= "E"
<tablaselect> ::= "tbestado" <alias>
<alias> ::= "ES"
<tablaselect> ::= "tbempleadoidentificacion" <alias>
<alias> ::= "I"
<tablaselect> ::= "tbidentificaciontipo" <alias>
<alias> ::= "IT"
<whereselect> ::= "WHERE" <condicioneswhere>
<condicioneswhere> ::= <condicioneswhere> "and" <condicionwhere>
<condicioneswhere> ::= <condicioneswhere> "and" <condicionwhere>
<condicioneswhere> ::= <condicionwhere>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "ES" "PUNTO" "idestado"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "E" "PUNTO" "idestado"
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "I" "PUNTO" "idempleado"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "E" "PUNTO" "idempleado"
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "IT" "PUNTO" "ididentificaciontipo"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "I" "PUNTO" "ididentificaciontipo"
```

### Instruccion #157 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> <whereselect> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
<valselect> ::= "E" "PUNTO" "ASTERISCO"
<valselect> ::= "estado" 
<valselect> ::= "I" "PUNTO" "identificacion" 
<valselect> ::= "tipoidentificacion" 
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbempleado" <alias>
<alias> ::= "E"
<tablaselect> ::= "tbestado" <alias>
<alias> ::= "ES"
<tablaselect> ::= "tbempleadoidentificacion" <alias>
<alias> ::= "I"
<tablaselect> ::= "tbidentificaciontipo" <alias>
<alias> ::= "IT"
<whereselect> ::= "WHERE" <condicioneswhere>
<condicioneswhere> ::= <condicioneswhere> "and" <condicionwhere>
<condicioneswhere> ::= <condicioneswhere> "and" <condicionwhere>
<condicioneswhere> ::= <condicionwhere>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "ES" "PUNTO" "idestado"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "E" "PUNTO" "idestado"
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "I" "PUNTO" "idempleado"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "E" "PUNTO" "idempleado"
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "IT" "PUNTO" "ididentificaciontipo"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "I" "PUNTO" "ididentificaciontipo"
```

### Instruccion #158 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> <whereselect> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
<valselect> ::= "E" "PUNTO" "ASTERISCO"
<valselect> ::= "estado" 
<valselect> ::= "I" "PUNTO" "identificacion" 
<valselect> ::= "tipoidentificacion" 
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbempleado" <alias>
<alias> ::= "E"
<tablaselect> ::= "tbestado" <alias>
<alias> ::= "ES"
<tablaselect> ::= "tbempleadoidentificacion" <alias>
<alias> ::= "I"
<tablaselect> ::= "tbidentificaciontipo" <alias>
<alias> ::= "IT"
<whereselect> ::= "WHERE" <condicioneswhere>
<condicioneswhere> ::= <condicioneswhere> "and" <condicionwhere>
<condicioneswhere> ::= <condicioneswhere> "and" <condicionwhere>
<condicioneswhere> ::= <condicionwhere>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "ES" "PUNTO" "idestado"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "E" "PUNTO" "idestado"
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "I" "PUNTO" "idempleado"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "E" "PUNTO" "idempleado"
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "IT" "PUNTO" "ididentificaciontipo"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "I" "PUNTO" "ididentificaciontipo"
```

### Instruccion #159 
```bnf
<select_instr> ::= "SELECT" <termdistinct> <select_list> "FROM" <listatablasselect> <whereselect> "PTCOMA" 
<termdistinct> ::= "DISTINCT" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
<valselect> ::= "E" "PUNTO" "primernombre" 
<valselect> ::= "primerapellido" 
<valselect> ::= "fechadenacimiento" 
<valselect> ::= "estado" 
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbempleado" <alias>
<alias> ::= "E"
<tablaselect> ::= "tbestado" <alias>
<alias> ::= "ES"
<tablaselect> ::= "tbempleadoidentificacion" <alias>
<alias> ::= "I"
<tablaselect> ::= "tbidentificaciontipo" <alias>
<alias> ::= "IT"
<whereselect> ::= "WHERE" <condicioneswhere>
<condicioneswhere> ::= <condicioneswhere> "and" <condicionwhere>
<condicioneswhere> ::= <condicioneswhere> "and" <condicionwhere>
<condicioneswhere> ::= <condicionwhere>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "ES" "PUNTO" "idestado"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "E" "PUNTO" "idestado"
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "I" "PUNTO" "idempleado"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "E" "PUNTO" "idempleado"
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "IT" "PUNTO" "ididentificaciontipo"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "I" "PUNTO" "ididentificaciontipo"
```

### Instruccion #160 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
<valselect> ::= "idempleado" 
<valselect> ::= <funcion_matematica_ws> <alias>
<funcion_matematica_ws > ::= "abs" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= "MENOS" <expresionaritmetica> %prec "UMENOS"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "45"
<valselect> ::= <funcion_matematica_ws> <alias>
<funcion_matematica_ws > ::= "cbrt" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "13"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "DIV" "PARIZQ" <expresionaritmetica> "COMA" <expresionaritmetica>"PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "325"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5"
```

### Instruccion #161 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "factorial" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "17"
<alias> ::= "AS" "factorial1"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "EXP" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2.0"
<alias> ::= "AS" "Exponencial"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "LN" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5.0"
<alias> ::= "Logaritmo Natural"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "PI" "PARIZQ" "PARDER"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "POWER" "PARIZQ" <expresionaritmetica> "COMA" <expresionaritmetica>"PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
```

### Instruccion #162 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "width_bucket" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "12"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<alias> ::= "AS" "uno"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "width_bucket" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "12"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<alias> ::= "AS" "dos"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "width_bucket" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "9"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "12"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<alias> ::= "AS" "tres"
```

### Instruccion #163 
```bnf
<create_table> : "CREATE" "TABLE" ID "PARIZQ" <list_columns_x> "PARDER" <end_create_table>
<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<null_field> ::= "NOT" "NULL"

<primary_key> ::= "PRIMARY" "KEY"

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

```

### Instruccion #164 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0"
```

### Instruccion #165 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0"
```

### Instruccion #166 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0"
```

### Instruccion #167 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "4"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0"
```

### Instruccion #168 
```bnf
<delete_instr> ::= "DELETE" "FROM" ID "WHERE" <condiciones> "PTCOMA"

<condiciones> ::= <condicion>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "idfuncion"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #169 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbfuncionesmath"
```

### Instruccion #170 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "SQRT" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "225"
<alias> ::= "AS" "SQRT1"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "SIGN" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "14.321"
<alias> ::= "SING"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "PI" "PARIZQ" "PARDER"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "TRUNC" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "67.456"
<alias> ::= "TRUNC1"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "RANDOM" "PARIZQ" "PARDER"
<alias> ::= "AS" "RANDOM1"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "RADIANS" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "15.0"
<alias> ::= "AS" "RADIANS1"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "ROUND" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "67.456"
<alias> ::= "AS" "ROUND1"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "POWER" "PARIZQ" <expresionaritmetica> "COMA" <expresionaritmetica>"PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "7.0"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "MOD" "PARIZQ" <expresionaritmetica> "COMA" <expresionaritmetica>"PARDER"
<expresionaritmetica> ::= "MENOS" <expresionaritmetica> %prec "UMENOS"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "38"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "LOG" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "200.0"
<alias> ::= "AS" "LOGARITMO"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "LN" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3.0"
<alias> ::= "AS" "LOGARITMONATURAL"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "FLOOR" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "53.6"
<alias> ::= "AS" "FLOOR1"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "FACTORIAL" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "4"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "EXP" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2.0"
<alias> ::= "AS" "EXPONENCIAL"
<valselect> ::= <funcion_matematica_s> <alias>
<funcion_matematica_s> ::= "DIV" "PARIZQ" <expresionaritmetica> "COMA" <expresionaritmetica>"PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "19"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
```

### Instruccion #171 
```bnf
<select_instr> ::= "SELECT" <select_list> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
<valselect> ::= <funcion_trigonometrica> <alias>
<funcion_trigonometrica> ::= "ATAN" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<valselect> ::= <funcion_trigonometrica> <alias>
<funcion_trigonometrica> ::= "ASIN" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<valselect> ::= <funcion_trigonometrica> <alias>
<funcion_trigonometrica> ::= "ACOS" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<valselect> ::= <funcion_trigonometrica> <alias>
<funcion_trigonometrica> ::= "COS" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0"
<valselect> ::= <funcion_trigonometrica> <alias>
<funcion_trigonometrica> ::= "TAN" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0"
<valselect> ::= <funcion_trigonometrica> <alias>
<funcion_trigonometrica> ::= "SINH" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<valselect> ::= <funcion_trigonometrica> <alias>
<funcion_trigonometrica> ::= "ACOSH" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<valselect> ::= <funcion_trigonometrica> <alias>
<funcion_trigonometrica> ::= "ATANH" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0"
<valselect> ::= <funcion_trigonometrica> <alias>
<funcion_trigonometrica> ::= "TANH" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #172 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
<fun_bin_strings_1> ::= "LENGTH" "PARIZQ" <cadena> "PARDER"

<func_bin_strings_2> ::= "substring" "PARIZQ" <cadena> "COMA" <cualquiernumero> "COMA" <cualquiernumero> "PARDER"

<cualquieridentificador> ::= "primerapellido"
<cualquiernumero> ::= "1"
<cualquiernumero> ::= "5"
<func_bin_strings_2> ::= "substr" "PARIZQ" <cadena> "COMA" <cualquiernumero> "COMA" <cualquiernumero> "PARDER"

<cualquieridentificador> ::= "primerapellido"
<cualquiernumero> ::= "1"
<cualquiernumero> ::= "5"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbempleado"
```

### Instruccion #173 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> <whereselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbempleado"
<whereselect> ::= "WHERE" <condicioneswhere>
<condicioneswhere> ::= <condicionwhere>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "primernombre"
<cualquiercadena> ::= "Jul"
```

### Instruccion #174 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> <whereselect> "PTCOMA" 
<selectlist> ::= "ASTERISCO"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbempleado"
<whereselect> ::= "WHERE" <condicioneswhere>
<condicioneswhere> ::= <condicionwhere>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "primernombre"
<cualquiercadena> ::= "Jul"
```

### Instruccion #175 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "15"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Funciones Matematicas"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3.0"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5"
```

### Instruccion #176 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "16"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Funciones Trigonometricas"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3.0"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5"
```

### Instruccion #177 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "17"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Funciones String"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3.0"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5"
```

### Instruccion #178 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "18"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Binarios"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1.0"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5"
```

