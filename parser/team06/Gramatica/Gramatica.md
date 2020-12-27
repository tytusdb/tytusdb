![Help Builder Web Site](./Logo.png)
# Reporte Gramatical
## Gramática

```
inicio               ::= queries 

queries               ::= queries query
                       |  query 
    
query               ::= mostrarBD
                    |   crearBD
                    |   alterBD
                    |   dropBD
                    |   useBD
                    |   operacion
                    |   insertinBD
                    |   updateinBD
                    |   deleteinBD
                    |   createTable
                    |   inheritsBD
                    |   dropTable
                    |   alterTable
                    |   variantesAt
                    |   contAdd
                    |   contDrop
                    |   contAlter                    
                    |   selectData
 

crearBD     ::= CREATE DATABASE ID PUNTOYCOMA'
            |   CREATE OR REPLACE DATABASE ID PUNTOYCOMA'
            |   CREATE OR REPLACE DATABASE ID parametrosCrearBD PUNTOYCOMA'
            |   CREATE  DATABASE ID parametrosCrearBD PUNTOYCOMA'


parametrosCrearBD   ::= parametrosCrearBD parametroCrearBD
                    |   parametroCrearBD

parametroCrearBD    ::= OWNER IGUAL final
                    |   MODE IGUAL final


mostrarBD  ::= SHOW DATABASES PUNTOYCOMA

useBD    ::= USE ID PUNTOYCOMA


alterBD    ::= ALTER DATABASE ID RENAME TO ID PUNTOYCOMA'
           |   ALTER DATABASE ID OWNER TO parametroAlterUser PUNTOYCOMA'

parametroAlterUser ::= CURRENT_USER
                   |   SESSION_USER
                   |   final



dropTable  ::= DROP TABLE ID PUNTOYCOMA

alterTable  ::= ALTER TABLE ID variantesAt PUNTOYCOMA

variantesAt ::= ADD contAdd
            |   ALTER contAlter
            |   DROP contDrop

listaContAlter  ::= listaContAlter COMA contAlter 
                |   contAlter

contAlter   ::= COLUMN ID SET NOT NULL 
            |   COLUMN ID TYPE tipo

contAdd     ::= COLUMN ID tipo 
            |   CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA
            |   FOREIGN KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA REFERENCES ID 
            |   PRIMARY KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA
            |   CONSTRAINT ID FOREIGN KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA REFERENCES ID PARENTESISIZQUIERDA ID PARENTESISDERECHA
            |   CONSTRAINT ID PRIMARY KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA
            |   CONSTRAINT ID UNIQUE PARENTESISIZQUIERDA ID PARENTESISDERECHA

contDrop    ::= COLUMN ID 
            |   CONSTRAINT ID
            |   PRIMARY KEY

listaid     ::= listaid COMA ID
            |   ID


dropBD      ::= DROP DATABASE ID PUNTOYCOMA'
            |   DROP DATABASE IF EXISTS ID PUNTOYCOMA'

operacion   ::=      operacion MAS operacion
            |        operacion MENOS operacion
            |        operacion POR operacion
            |        operacion DIV operacion
            |        operacion RESIDUO operacion
            |        operacion POTENCIA operacion
            |        operacion AND operacion
            |        operacion OR operacion
            |        operacion SIMBOLOOR2 operacion
            |        operacion SIMBOLOOR operacion
            |        operacion SIMBOLOAND2 operacion
            |        operacion DESPLAZAMIENTOIZQUIERDA operacion
            |        operacion DESPLAZAMIENTODERECHA operacion
            |        operacion IGUAL operacion
            |        operacion IGUALIGUAL operacion
            |        operacion NOTEQUAL operacion
            |        operacion MAYORIGUAL operacion
            |        operacion MENORIGUAL operacion
            |        operacion MAYOR operacion
            |        operacion MENOR operacion
            |        operacion DIFERENTE operacion
            |        PARENTESISIZQUIERDA operacion PARENTESISDERECHA
            |        MENOS ENTERO
            |        MENOS DECIMAL
            |        operacion : NOT operacion
            |        funcionBasica
            |        final



funcionBasica    ::=      ABS PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | CBRT PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | CEIL PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | CEILING PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | DEGREES PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | DIV PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | EXP PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | FACTORIAL PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | FLOOR PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | GCD PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | LCM PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | LN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | LOG PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | MOD PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | PI PARENTESISIZQUIERDA  PARENTESISDERECHA
                        | POWER PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | RADIANS PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA                      
                        | SIGN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SQRT PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TRIM_SCALE PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TRUNC  PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | WIDTH_BUCKET PARENTESISIZQUIERDA operacion COMA operacion COMA operacion COMA operacion PARENTESISDERECHA
                        | RANDOM PARENTESISIZQUIERDA PARENTESISDERECHA
                        | ACOS  PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ACOSD PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ASIN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ASIND PARENTESISIZQUIERDA operacion PARENTESISDERECHA                
                        | ATAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ATAND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ATAN2 PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | ATAN2D PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | COS PARENTESISIZQUIERDA operacion PARENTESISDERECHA
			| COSD  PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | COT PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | COTD PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SIN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SIND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TAND  PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SINH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | GREATEST PARENTESISIZQUIERDA select_list PARENTESISDERECHA
                        | LEAST PARENTESISIZQUIERDA select_list PARENTESISDERECHA
                        | NOW PARENTESISIZQUIERDA  PARENTESISDERECHA
                        | COSH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TANH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ASINH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ACOSH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ATANH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | LENGTH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TRIM PARENTESISIZQUIERDA opcionTrim operacion FROM operacion PARENTESISDERECHA
                        | GET_BYTE PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | MD5 PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SET_BYTE PARENTESISIZQUIERDA operacion COMA operacion COMA operacion PARENTESISDERECHA
                        | SHA256 PARENTESISIZQUIERDA operacion PARENTESISDERECHA                       
                        | SUBSTR PARENTESISIZQUIERDA operacion  COMA operacion COMA operacion PARENTESISDERECHA
                        | CONVERT PARENTESISIZQUIERDA operacion  COMA operacion COMA operacion PARENTESISDERECHA
                        | ENCODE PARENTESISIZQUIERDA operacion  COMA operacion  PARENTESISDERECHA
                        | DECODE PARENTESISIZQUIERDA operacion  COMA operacion  PARENTESISDERECHA
                        | AVG PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SUM PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SUBSTRING PARENTESISIZQUIERDA operacion FROM operacion FOR operacion PARENTESISDERECHA
                        | SUBSTRING PARENTESISIZQUIERDA operacion FROM operacion PARENTESISDERECHA
                        | SUBSTRING PARENTESISIZQUIERDA operacion FOR operacion PARENTESISDERECHA
                        | operacion BETWEEN operacion 
                        | operacion LIKE CADENA
                        | operacion  IN PARENTESISIZQUIERDA select_list PARENTESISDERECHA 
                        | operacion NOT BETWEEN operacion
                        | operacion  BETWEEN SYMMETRIC operacion
                        | operacion NOT BETWEEN SYMMETRIC operacion
                        | operacion IS DISTINCT FROM operacion
                        | operacion IS NOT DISTINCT  FROM operacion



opcionTrim  ::= LEADING
            |   TRAILING
            |   BOTH


final       ::= DECIMAL
            |   ENTERO
            |   ID
            |   ID PUNTO ID
            |   CADENA


insertinBD     ::= INSERT INTO ID VALUES PARENTESISIZQUIERDA listaParam PARENTESISDERECHA PUNTOYCOMA
               |   INSERT INTO ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA VALUES PARENTESISIZQUIERDA listaParam PARENTESISDERECHA PUNTOYCOMA
 


listaParam      ::= listaParam COMA final
                |   final



updateinBD      ::= UPDATE ID SET asignaciones WHERE asignaciones PUNTOYCOMA



asignaciones      ::=    asignaciones COMA asigna
                  | asigna



asigna            ::=   ID IGUAL operacion




deleteinBD         ::=   DELETE FROM ID PUNTOYCOMA
                   |     DELETE FROM ID WHERE asignaciones PUNTOYCOMA


inheritsBD         ::= CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA  INHERITS PARENTESISIZQUIERDA ID PARENTESISDERECHA PUNTOYCOMA


createTable        ::= CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA PUNTOYCOMA


creaColumnas       ::= creaColumnas COMA Columna 
                   |   Columna 



Columna            ::= ID tipo
                   |   ID tipo paramOpcional
                   |   UNIQUE PARENTESISIZQUIERDA listaParam PARENTESISDERECHA
                   |   constraintcheck
                   |   checkinColumn
                   |   primaryKey
                   |   foreignKey


paramOpcional    ::= paramOpcional paramopc
                 |   paramopc



paramopc        ::= DEFAULT final
                |   NULL
                |   NOT NULL
                |   UNIQUE
                |   PRIMARY KEY
                |   constraintcheck
                |   checkinColumn
                |   CONSTRAINT ID UNIQUE


checkinColumn      ::=  CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA

constraintcheck    ::=  CONSTRAINT ID CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA

primaryKey         ::=  PRIMARY KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA

foreignKey         ::=  FOREIGN KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA REFERENCES ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA


tipo               ::=    SMALLINT
                        | INTEGER
                        | BIGINT
                        | DECIMAL
                        | NUMERIC
                        | REAL
                        | DOUBLE PRECISION
                        | MONEY
                        | VARCHAR PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA
                        | CHARACTER VARYING PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA
                        | CHARACTER PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA
                        | CHAR PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA
                        | TEXT
                        | BOOLEAN
                        | TIMESTAMP
                        | TIME
                        | INTERVAL
                        | DATE
                        | YEAR
                        | MONTH 
                        | DAY
                        | HOUR 
                        | MINUTE
                        | SECOND

selectData      ::= SELECT select_list FROM select_list WHERE search_condition opcionesSelect PUNTOYCOMA
                |   SELECT POR FROM select_list WHERE search_condition opcionesSelect PUNTOYCOMA
                |   SELECT select_list FROM select_list WHERE search_condition  PUNTOYCOMA
                |   SELECT POR FROM select_list WHERE search_condition  PUNTOYCOMA
                |   SELECT select_list FROM select_list  PUNTOYCOMA
                |   SELECT POR FROM select_list  PUNTOYCOMA
                |   SELECT select_list   PUNTOYCOMA

opcionesSelect   ::=     opcionesSelect opcionSelect
                 |       opcionSelect


opcionSelect     ::= LIMIT operacion
                 |   GROUP BY select_list
                 |   HAVING select_list
                 |   ORDER BY select_list
                 |   LIMIT operacion OFFSET operacion
                 |   ORDER BY select_list ordenamiento 

ordenamiento     ::= ASC
                 |   DESC


search_condition ::= NOT search_condition
                 |   operacion
                 |   PARENTESISIZQUIERDA search_condition PARENTESISDERECHA


select_list   ::= select_list COMA operacion
              |   select_list COMA asignacion
              |   asignacion
              |   operacion



asignacion    ::= operacion AS  operacion    
              |   final final'
```



