## GRUPO #11 
# *REPORTE GRAMATICAL DE LA EJECUCION*

### Instruccion #1 
```bnf
<createDB_instr> ::= CREATE DATABASE "DBFase2"  <state_owner>
<state_owner> ::= <state_mode>
<state_mode> ::= PTCOMA
```

### Instruccion #2 
```bnf
<use_instr> ::= USE "DBFase2"  PTCOMA
```

### Instruccion #3 
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

<key_column> ::= "PRIMARY" "KEY" "PARIZQ" <listtablas> "PARDER"
<key_column> ::= ID <type_column> <attributes>

<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>

```

### Instruccion #4 
```bnf

<columnas> ::= ID

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

<columnas> ::= ID

```

### Instruccion #7 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Laptop Lenovo"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #8 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Bateria para Laptop Lenovo T420"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #9 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Teclado Inalambrico"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #10 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "4"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Mouse Inalambrico"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #11 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "5"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "WIFI USB"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #12 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "6"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Laptop HP"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #13 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "7"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Teclado Flexible USB"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #14 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "8"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Laptop Samsung"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "2021-01-02"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #15 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
<valselect> ::=  "COUNT" "PARIZQ" "ASTERISCO" "PARDER"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbProducto"
```

### Instruccion #16 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Create Table and Insert"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0"
```

### Instruccion #17 
```bnf
<update_instr> ::= "UPDATE" ID "SET" <asignaciones> "WHERE" <condiciones> "PTCOMA"

<asignaciones> ::= <asignacion>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
```

### Instruccion #18 
```bnf
<select_instr> ::= "SELECT" <select_list> "FROM" <listatablasselect> <whereselect> "PTCOMA" 
<selectlist> ::= <listaselect> 
<listaselect> ::= <listaselect> "COMA" <valselect> 
<listaselect> ::= <valselect>
<valselect> ::=  "COUNT" "PARIZQ" "ASTERISCO" "PARDER"
<listatablasselect> ::=  <tablaselect>
<tablaselect> ::= "tbProducto"
<whereselect> ::= "WHERE" <condicioneswhere>
<condicioneswhere> ::= <condicionwhere>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "estado"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
```

### Instruccion #19 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "2"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= "Update"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0"
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
<valselect> ::= <funcion_trigonometrica> <alias>
<funcion_trigonometrica> ::= "SIN" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
```

### Instruccion #22 
```bnf
<insert_instr> ::=  "INSERT" "INTO" ID "VALUES" "PARIZQ" <parametros> "PARDER" "PTCOMA"

<parametros> ::= <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "3"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<cualquiercadena> ::= " Valida Funciones"
<parametros> ::= <parametros> "COMA" <parametroinsert>

<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "20"
```

### Instruccion #23 
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

