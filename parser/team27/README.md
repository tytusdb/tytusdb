# Gramática SQL :page_facing_up:

## Integrantes
201800634	ANTHONY FERNANDO SON MUX

201801181	CÉSAR EMANUEL GARCIA PÉREZ

201801195	JOSE CARLOS JIMENEZ

201801237	JOSÉ RAFAEL MORENTE GONZÁLEZ

## Gramática Ascendente
```sh
<INICIO> ::= <INSTRUCCIONES>

<INSTRUCCIONES> ::= <INSTRUCCIONES> <INSTRUCCION>
			| <INSTRUCCION>

<INSTRUCCION> ::= <USE>
			| <SHOW>
			| <CREATE>
			| <ALTER>
			| <DROP>

<USE> ::= USE identificador;

<SHOW> ::= SHOW DATABASES;

<CREATE> ::= create <TIPO_CREATE> 

<TIPO_CREATE> ::= <REPLACE> DATABASE <IF_EXIST> identificador <CREATE_OPCIONES> ;
			| TABLE identificador ( <DEFINICION_COLUMNA> );
			| TYPE identificador AS ENUM ( <LIST_VLS> );

<REPLACE> ::= OR REPLACE 
			| épsilon

<CREATE_OPCIONES> ::= OWNER = identificador <CREATE_OPCIONES>
			| MODE = numero <CREATE_OPCIONES>
			| épsilon

<DEFINICION_COLUMNA> ::= <DEFINICION_COLUMNA>, <COLUMNA>
			| <COLUMNA>

<COLUMNA> ::= identificador <TIPO_DATO> <DEFINICION_VALOR_DEFECTO> <CONSTRAINT> 
            | <PRIMARY_KEY>
            | <FOREIGN_KEY>

<DEFINICION_VALOR_DEFECTO> ::= DEFAULT <TIPO_DEFAULT>
			| épsilon

<CONSTRAINT>::= CONSTRAINT identificador <RESTRICCION_COLUMNA>
			| <RESTRICCION_COLUMNA>
			| épsilon

<RESTRICCION_COLUMNA> ::= NOT NULL
			| NULL
			| PRIMARY KEY
			| UNIQUE

<PRIMARY_KEY> ::= PRIMARY KEY ( <NOMBRE_COLUMNAS> )

<FOREIGN_KEY> ::= FOREING KEY ( <NOMBRE_COLUMNAS> ) REFERENCES ID ( <NOMBRE_COLUMNAS> )

<NOMBRE_COLUMNAS> ::= <NOMBRE_COLUMNAS> , ID
            | ID

<DROP> ::= DROP <TIPO_DROP>

<ALTER> ::= ALTER <TIPO_ALTER>

<TIPO_ALTER> ::= DATABASE identificador <ALTER_DATABASE> ;
			| TABLE identificador <ALTERACION_TABLA> ;

<ALTER_DATABASE> ::= RENAME TO identificador
			| OWNER TO identificador

<ALTERACION_TABLA> ::= <ALTERACION_TABLA>,<ALTERAR_TABLA>
			| <ALTERAR_TABLA>

<ALTERAR_TABLA> ::= add column <COLUMNA>
			| alter column <COLUMNA>
			| drop column identificador 
			| drop constraint identificador 

<TIPO_DROP> ::= DATABASE <IF_EXIST> identificador;
			| TABLE identificador;

<IF_EXIST> ::= IF EXIST
			| épsilon

```
