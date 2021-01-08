## GRUPO #11 
# *REPORTE GRAMATICAL DE LA EJECUCION PL*

### Instruccion #1 
```bnf
<plsql_instr> : CREATE <procedfunct> ID PARIZQ <parametrosfunc> PARDER <tiporetorno> <cuerpofuncion>
<procedfunct>  : PROCEDURE
<parfunc>    : ID <type_column1>
<tiporetorno>  : RETURNS <type_column1> AS
<cuerpofuncion>  : CADDOLAR <declaraciones> <cuerpo> CADDOLAR LANGUAGE PLPGSQL PTCOMA
<cuerpo>     : BEGIN <instrlistabloque> END PTCOMA
<returnbloque> : RETURN <condicion> PTCOMA
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "texto"
```

### Instruccion #2 
```bnf
<plsql_instr> : CREATE <procedfunct> ID PARIZQ <parametrosfunc> PARDER <tiporetorno> <cuerpofuncion>
<procedfunct>  : PROCEDURE
<parfunc>    : ID <type_column1>
<parfunc>    : ID <type_column1>
<tiporetorno>  : RETURNS <type_column1> AS
<cuerpofuncion>  : CADDOLAR <declaraciones> <cuerpo> CADDOLAR LANGUAGE PLPGSQL PTCOMA
<declaraciones>   : DECLARE <listadeclaraciones>
<declaracion> : ID <constantintr> type_column1 <notnullinst> <asignavalor> PTCOMA
<declaracion> : ID <constantintr> type_column1 <notnullinst> <asignavalor> PTCOMA
<cuerpo>     : BEGIN <instrlistabloque> END PTCOMA
<instrif>   : IF <condiciones> THEN <instrlistabloque> END IF PTCOMA
<condiciones> ::= <condicion>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "tabla"
<expresionaritmetica> ::= <cualquiernumero>

<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<select_instr>     : SELECT CADENADOBLE
<instrif>   : IF <condiciones> THEN <instrlistabloque> ELSE <instrlistabloque> END IF PTCOMA
<condiciones> ::= <condicion>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "cantidad"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "resultado"
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0"
<instrif>   : IF <condiciones> THEN <instrlistabloque> END IF PTCOMA
<condiciones> ::= <condicion>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "tabla"
<expresionaritmetica> ::= <cualquiernumero>

<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<select_instr>     : SELECT CADENADOBLE
<instrif>   : IF <condiciones> THEN <instrlistabloque> ELSE <instrlistabloque> END IF PTCOMA
<condiciones> ::= <condicion>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "cantidad"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "resultado"
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0"
<instrif>   : IF <condiciones> THEN <instrlistabloque> END IF PTCOMA
<condiciones> ::= <condicion>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "tabla"
<expresionaritmetica> ::= <cualquiernumero>

<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<select_instr>     : SELECT CADENADOBLE
<instrif>   : IF <condiciones> THEN <instrlistabloque> ELSE <instrlistabloque> END IF PTCOMA
<condiciones> ::= <condicion>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "cantidad"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "resultado"
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0"
<returnbloque> : RETURN <condicion> PTCOMA
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "retorna"
```

### Instruccion #3 
```bnf
<plsql_instr> : CREATE <procedfunct> ID PARIZQ <parametrosfunc> PARDER <tiporetorno> <cuerpofuncion>
<procedfunct>  : PROCEDURE
<tiporetorno>  : RETURNS <type_column1> AS
<cuerpofuncion>  : CADDOLAR <declaraciones> <cuerpo> CADDOLAR LANGUAGE PLPGSQL PTCOMA
<declaraciones>   : DECLARE <listadeclaraciones>
<declaracion> : ID <constantintr> type_column1 <notnullinst> <asignavalor> PTCOMA
<declaracion> : ID <constantintr> type_column1 <notnullinst> <asignavalor> PTCOMA
<declaracion> : ID <constantintr> type_column1 <notnullinst> <asignavalor> PTCOMA
<declaracion> : ID <constantintr> type_column1 <notnullinst> <asignavalor> PTCOMA
<cuerpo>     : BEGIN <instrlistabloque> END PTCOMA
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<select_instr>     : SELECT CADENADOBLE
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<select_instr>     : SELECT CADENADOBLE
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<funcion_matematica_s> ::= "TRUNC" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <expresionaritmetica> "*" <expresionaritmetica>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "SENO"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "hora"
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<expresionaritmetica> ::= <expresionaritmetica> "+" <expresionaritmetica>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "VALOR"
<expresionaritmetica> ::= <cualquiernumero>

<cualquiernumero> ::= "1"
<cualquiernumero> ::= "4"
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<expresionaritmetica> ::= "MENOS" <expresionaritmetica> %prec "UMENOS"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<expresionaritmetica> ::= "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <expresionaritmetica> "*" <expresionaritmetica>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "ABSOLUTO"
<funcion_matematica_s> ::= "SQRT" "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "225"
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<expresionaritmetica> ::= <expresionaritmetica> "/" <expresionaritmetica>
<expresionaritmetica> ::= "PARIZQ" <expresionaritmetica> "PARDER"
<expresionaritmetica> ::= <expresionaritmetica> "+" <expresionaritmetica>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "VALOR"
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "ABSOLUTO"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0.5"
<instrif>   : IF <condiciones> THEN <instrlistabloque> ELSE <instrlistabloque> END IF PTCOMA
<condiciones> ::= <condicion>
<condicion> ::= <expresion> ">" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "VALOR"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "1"
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "20"
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "10"
<returnbloque> : RETURN <condicion> PTCOMA
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "VALOR"
```

### Instruccion #4 
```bnf
<plsql_instr> : CREATE <procedfunct> ID PARIZQ <parametrosfunc> PARDER <tiporetorno> <cuerpofuncion>
<procedfunct>  : PROCEDURE
<cuerpofuncion>  : CADDOLAR <declaraciones> <cuerpo> CADDOLAR LANGUAGE PLPGSQL PTCOMA
<cuerpo>     : BEGIN <instrlistabloque> END PTCOMA
<insert_instr>     : INSERT CADENADOBLE PTCOMA
<insert_instr>     : INSERT CADENADOBLE PTCOMA
<insert_instr>     : INSERT CADENADOBLE PTCOMA
<insert_instr>     : INSERT CADENADOBLE PTCOMA
<insert_instr>     : INSERT CADENADOBLE PTCOMA
```

### Instruccion #5 
```bnf
<plsql_instr> : CREATE <procedfunct> ID PARIZQ <parametrosfunc> PARDER <tiporetorno> <cuerpofuncion>
<procedfunct>  : PROCEDURE
<cuerpofuncion>  : CADDOLAR <declaraciones> <cuerpo> CADDOLAR LANGUAGE PLPGSQL PTCOMA
<cuerpo>     : BEGIN <instrlistabloque> END PTCOMA
<update_instr>     : UPDATE CADENADOBLE PTCOMA
```

### Instruccion #6 
```bnf
<plsql_instr> : CREATE <procedfunct> ID PARIZQ <parametrosfunc> PARDER <tiporetorno> <cuerpofuncion>
<procedfunct>  : PROCEDURE
<parfunc>    : ID <type_column1>
<parfunc>    : ID <type_column1>
<parfunc>    : ID <type_column1>
<cuerpofuncion>  : CADDOLAR <declaraciones> <cuerpo> CADDOLAR LANGUAGE PLPGSQL PTCOMA
<cuerpo>     : BEGIN <instrlistabloque> END PTCOMA
<insert_instr>     : INSERT CADENADOBLE PTCOMA
```

### Instruccion #7 
```bnf
<dropfunction>    :   DROP FUNCTION IF EXISTS ID PTCOMA
```

### Instruccion #8 
```bnf
<plsql_instr> : CREATE <procedfunct> ID PARIZQ <parametrosfunc> PARDER <tiporetorno> <cuerpofuncion>
<procedfunct>  : PROCEDURE
<parfunc>    : ID <type_column1>
<tiporetorno>  : RETURNS <type_column1> AS
<cuerpofuncion>  : CADDOLAR <declaraciones> <cuerpo> CADDOLAR LANGUAGE PLPGSQL PTCOMA
<cuerpo>     : BEGIN <instrlistabloque> END PTCOMA
<returnbloque> : RETURN <condicion> PTCOMA
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "texto"
```

### Instruccion #9 
```bnf
<plsql_instr> : CREATE <procedfunct> ID PARIZQ <parametrosfunc> PARDER <tiporetorno> <cuerpofuncion>
<procedfunct>  : PROCEDURE
<parfunc>    : ID <type_column1>
<tiporetorno>  : RETURNS <type_column1> AS
<cuerpofuncion>  : CADDOLAR <declaraciones> <cuerpo> CADDOLAR LANGUAGE PLPGSQL PTCOMA
<declaraciones>   : DECLARE <listadeclaraciones>
<declaracion> : ID <constantintr> type_column1 <notnullinst> <asignavalor> PTCOMA
<cuerpo>     : BEGIN <instrlistabloque> END PTCOMA
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<select_instr>     : SELECT CADENADOBLE
<returnbloque> : RETURN <condicion> PTCOMA
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "idp"
```

### Instruccion #10 
```bnf
<plsql_instr> : CREATE <procedfunct> ID PARIZQ <parametrosfunc> PARDER <tiporetorno> <cuerpofuncion>
<procedfunct>  : PROCEDURE
<parfunc>    : ID <type_column1>
<tiporetorno>  : RETURNS <type_column1> AS
<cuerpofuncion>  : CADDOLAR <declaraciones> <cuerpo> CADDOLAR LANGUAGE PLPGSQL PTCOMA
<declaraciones>   : DECLARE <listadeclaraciones>
<declaracion> : ID <constantintr> type_column1 <notnullinst> <asignavalor> PTCOMA
<cuerpo>     : BEGIN <instrlistabloque> END PTCOMA
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<select_instr>     : SELECT CADENADOBLE
<returnbloque> : RETURN <condicion> PTCOMA
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "idb"
```

### Instruccion #11 
```bnf
<plsql_instr> : CREATE <procedfunct> ID PARIZQ <parametrosfunc> PARDER <tiporetorno> <cuerpofuncion>
<procedfunct>  : PROCEDURE
<parfunc>    : ID <type_column1>
<parfunc>    : ID <type_column1>
<parfunc>    : ID <type_column1>
<parfunc>    : ID <type_column1>
<parfunc>    : ID <type_column1>
<tiporetorno>  : RETURNS <type_column1> AS
<cuerpofuncion>  : CADDOLAR <declaraciones> <cuerpo> CADDOLAR LANGUAGE PLPGSQL PTCOMA
<declaraciones>   : DECLARE <listadeclaraciones>
<declaracion> : ID <constantintr> type_column1 <notnullinst> <asignavalor> PTCOMA
<declaracion> : ID <constantintr> type_column1 <notnullinst> <asignavalor> PTCOMA
<declaracion> : ID <constantintr> type_column1 <notnullinst> <asignavalor> PTCOMA
<cuerpo>     : BEGIN <instrlistabloque> END PTCOMA
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<select_instr>     : SELECT CADENADOBLE
<instrif>   : IF <condiciones> THEN <instrlistabloque> END IF PTCOMA
<condiciones> ::= <condicion>
<condicion> ::= <expresion> "=" <expresion>
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "idev"
<expresionaritmetica> ::= <cualquiernumero>
<cualquiernumero> ::= "0"
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<select_instr>     : SELECT CADENADOBLE
<asignacionbloque> : ID IGUAL <expresion> PTCOMA
<select_instr>     : SELECT CADENADOBLE
<insert_instr>     : INSERT CADENADOBLE PTCOMA
<returnbloque> : RETURN <condicion> PTCOMA
<expresionaritmetica> ::= <cualquiernumero>
<cualquieridentificador> ::= "ide"
```

