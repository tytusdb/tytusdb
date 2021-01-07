# TEAM 04
## INTEGRANTES
### 201025406 GLENDY MARILUCY CONTRERAS GONZALEZ
### 201114496 AUGUSTO GERMAN MAZARIEGOS SALGUERO
### 201114566	BRAYAN EZEQUIEL SANTIAGO BRITO		
### 201122864	LUIS CARLOS VALIENTE SALAZAR	

#

## GRAMATICAS
#
**Índice**   

1. [Expresiones regulares](#id1)
2. [Precedencia Utilizada](#id2)
3. [Simbolos terminales y no terminales](#id3)
4. [Gramática Funcional](#id4)

#

## Expresiones regulares<a name="id1"></a>

| Reconoce              | Expesión Regular       |
|-----------------------|:----------------------:|
| ID                    | [a-zA-Z_][a-zA-Z_0-9]* |
| CADENA                | (\".*?\"|\'.*?\')      |
| DISTINTO              | (!=|<>)                |
| DECIMAL               | \d+\.\d+               |
| ENTERO                | \d+                    |
| COMENTARIO MULTILINEA | /\*(.\n)*?\*/          |
| COMENTARIO SIMPLE     | --(.)+(\n)+            |

#

## Precedencia Utilizada<a name="id2"></a>

| Operador  | Asociatividad  |
|-----------|:--------------:|
| left      | CONTAT         |
| left      | OR             |
| left      | AND            |
| left      | BOR            |
| left      | NUMERAL        |
| right     | UNOT,UBNOT     |
| left      | MENORQ, MAYORQ        |
| left      | MENORIGUAL,MAYORIGUAL |  
| left      | DISTINTO              |
| left      | MOV,MOVI              |
| left      | SUMA,RESTA            |
| left      | MULT,DIVISION,MODULO  |
| left      | POTENCIA              |
| rigth     | UMINUS, UPLUS         |

#
## Simbolos terminales y no terminales<a name="id3"></a>


| No.  | Símbolo terminal |
|------|:----------------:|
|   1  |       +           |  
|   2  |       -           |  
|   3  |       *           |  
|   4  |       /           |  
|   5  |       %           |  
|   6  |        (          |  
|   7  |        )          |  
|   8  |        .          |  
|   9  |        ;          |  
|   10 |        ,          |  
|   11 |        [          |  
|   12 |        ]          |  
|   13 |        =          |  
|   14 |        <          |
|   15 |        >          |  
|   16 |        &          |  
|   17 |       '|'         |  
|   18 |        <<         |  
|   19 |        >>         |  
|   20 |        #          |  
|   21 |        ~          | 
|   22 |     smallint      | 
|   23 |     integer       | 
|   24 |     bigint        | 
|   25 |     decimal       | 
|   26 |     numeric       | 
|   27 |     real          | 
|   28 |     double        | 
|   29 |     precition     | 
|   30 |     money         | 
|   31 |     float         | 
|   32 |     boolean     | 
|   33 |     true        | 
|   34 |     false       | 
|   35 |     yes         | 
|   36 |     no          | 
|   37 |     off         | 
|   38 |     character   | 
|   40 |     varying     | 
|   41 |     varchar     | 
|   42 |     char        | 
|   43 |     text        | 
|   44 |     timestamp   | 
|   45 |     date        | 
|   46 |     time        | 
|   47 |     interval    | 
|   48 |     year        | 
|   49 |     month       | 
|   50 |     day         | 
|   51 |     hour        | 
|   52 |     minute      | 
|   52 |     second      | 
|   54 |     extract     | 
|   55 |     date_part   | 
|   56 |     now         | 
|   57 |     current_date | 
|   58 |     current_time | 
|   59 |     enum         | 
|   60 |     between      | 
|   61 |     in           | 
|   62 |     like         | 
|   63 |     ilike        | 
|   64 |     similar      | 
|   65 |     is           | 
|   66 |     not          | 
|   68 |     null         | 
|   68 |     or           | 
|   69 |     if           | 
|   70 |     else          | 
|   71 |     use           | 
|   72 |     database      | 
|   73 |     databases     | 
|   74 |     create        | 
|   75 |     insert         | 
|   76 |     into           | 
|   77 |     alter          | 
|   78 |     table          | 
|   79 |     show           | 
|   80 |     drop           | 
|   81 |     delete         | 
|   82 |     primary        | 
|   83 |     foreign        | 
|   84 |     key            | 
|   85 |     add            | 
|   86 |     column         | 
|   87 |     set            | 
|   88 |     type           | 
|   89 |     constraint     | 
|   90 |     unique         | 
|   91 |     references     | 
|   92 |     exists         | 
|   93 |     replace        |
|   94 |     owner          | 
|   95 |     new_owner      | 
|   96 |     current_user   | 
|   97 |     session_user   | 
|   98 |     mode      | 
|   99 |     rename    | 
|   100|     inherits  |  
|   101|     values    | 
|   102|     update    | 
|   103|     where     | 
|   104|     from      | 
|   105|     select    | 
|   106|     distinct  | 
|   107|     group     | 
|   108|     order     | 
|   109|     by        | 
|   110|     as        |  
|   111|     left      | 
|   112|     righ      |
|   113|     full      |
|   114|     outer     |
|   115|     inner     |
|   116|     join      |
|   117|     on        |
|   118|     asc       |
|   119|     desc      |
|   120|     first     |
|   121|     case      |
|   122|     when      |
|   123|     then      |
|   124|     end       |
|   125|     greatest  |
|   126|     least     |
|   127|     limit     |
|   128|     offset    |
|   129|     intersect |
|   130|     expect    |
|   131|     to        |

## Gramática Funcional<a name="id4"></a>
#
### Nodo raiz donde se guardan las instrucciones

```
s : INSTS 
```

### Lista inicial de instrucciones
```
 INSTS : INSTS INST PCOMA
       | INST PCOMA
```

### Tipos de Instrucciones

### Aquí se encuentran las  sentencias  principales. 
```
   INST : CREATE_TYPE
            | SELECT
            | CREATE_DB
            | SHOW_DB
            | DROP_DB
            | ALTER_DB
            | USE_DB
            | CREATE_TB
            | UNION
            | UNIONALL
            | INTERSECT
            | INTERSECTALL
            | EXCEPT
            | EXCEPTALL
            | DROPTABLE
            | DELETE
            | INSERT
```

### Producción de  opciones para la creación de una base de datos.

```
    OPDB : OWNER
         | MODE       
```

### Producción donde se reconocen la sintaxis para crear una base de datos.

```
CREATE_DB : CREATE DATABASE IF NOT EXISTS E OPDB IGUAL E OPDB IGUAL E
          | CREATE DATABASE IF NOT EXISTS E OPDB IGUAL E
          | CREATE DATABASE E OPDB IGUAL E
          | CREATE OR REMPLACE DATABASE E
          | CREATE DATABASE E
```

### Producción donde se reconoce la sintaxis para eliminar una base de datos.

```
DROP_DB : RDROP DATABASE E 
        | RDROP DATABASE IF EXISTS E
```
### Producción donde se reconoce la  sintaxis para renombra una base de datos.

```
ALTER_DB : ALTER DATABASE E RENAME TO E
         | ALTER DATABASE E OWNER  TO E
            
```

### Producción donde se reconoce la sintaxis para mostrar las bases de datos.

```
SHOW_DB : SHOW DATABASE 
```

### Producción que reconoce la sintaxis para la selección de una base de datos y trabajar sobre ella.

```
USE_DB : USE DATABASE ID
```


### Producción donde se reconoce la sintaxis para la creación de una nueva tabla.

```
 CREATE_TB : CREATE TABLE ID PARI ATRIBUTOS PARD 
```

### Producción recursiva para reconocer los atributos que estan separados por coma. 

```
ATRIBUTOS : ATRIBUTOS COMA ATRIBUTO
          | ATRIBUTO 
                  
```

### Producción atributo donde se encuentra la sintaxis de de una tablas de base de datos.

```
ATRIBUTO : ID TIPO CONSTRAINT E CHECK PARI E PARD 
         | ID TIPO NOT NULL PRIMARY KEY 
         | ID TIPO CHECK PARI E PARD    
         | ID TIPO NOT NULL UNIQUE
         | ID TIPO UNIQUE NOT NULL
         | ID TIPO NOT NULL
         | ID TIPO UNIQUE
         | ID TIPO            
```
### Producción de tipos de datos que reconoce el lenguaje.

```
TIPO : INTEGER  
     | VARCHAR PARI E PARD
     | REAL
     | DATE
     | BOOLEAN      
```

### Producción que reconoce la sinstaxis para la eliminación de un tabla.

```
DROPTABLE : RDROP TABLE ID
```

### Esta producción eliminta un data especifico de una tabla.
```
 DELETE : RDELETE FROM ID
```

### Esta produccion reconoce la sintaxis de insert, incerta filas en una tabla.
```
INSERT : RINSERT INTO ID VALUES PARI LE PARD
```

### Esta produccion reconoce la sintaxis  de registro de un nuevo tipo de  dato para usar en la base de datos.
```
'CREATE_TYPE : CREATE TYPE ID AS ENUM PARI LE PARD'
```

### Esta produccion es una declaracción compleja  tiene muchas cláusulas que puede tilizar para forma una consulta flexible.

```
 SELECT : RSELECT E
 ```

### Esta producción es un operador de conjutos de resultados de mas de la sentencia select.
```
UNION : SELECT RUNION UNION
      | SELECT RUNION SELECT
 ```

### Esta producción que reconoce el operador union all se utiliza para combinar los conjutos de resultados de 2 o mas sentencias select.
```
 UNIONALL : SELECT RUNION ALL UNIONALL
          | SELECT RUNION ALL SELECT
 ```


### Esta producción reconoce el operador insersect y devuelve las filas que estan disponibles en ambos conhutos de resultado.

```
INTERSECT : SELECT RINTERSECT INTERSECT
          | SELECT RINTERSECT SELECT

 ```

### Esta produdcción reconoce el operador intersect all elimina las filas duplicadas.  

```
INTERSECTALL : SELECT RINTERSECT ALL INTERSECTALL
             | SELECT RINTERSECT ALL SELECT

```
### Esta producción reconoce la estructura de except devulve filas distintas de la primer consulta  (izquierda) que no estan en la salida.

```
EXCEPT : SELECT REXCEPT EXCEPT
              | SELECT REXCEPT SELECT'

```
### Esta producción reconoce la estructura de except devulve filas distintas de la primer consulta.
```
EXCEPTALL : SELECT REXCEPT ALL EXCEPT
          | SELECT REXCEPT ALL SELECT

```

### Esta producción reconoce tipos de datos y los combierte en cadena para su uso posterior.
```
LITERAL : INT
        | DECIMAL
        | ID
        | CADENA
        | TRUE
        | FALSE
        | MULT

```
### Esta produccion contiene y reconoce los elementos logicos, relacionales, operadores artméticos y estructura de texto como literales.

```
E : E AND E
         | E OR E
         | NOT E %prec UNOT
         | E MENORQ E
         | E MAYORQ E
         | E MAYORIGUAL E
         | E MENORIGUAL E
         | E IGUALQ E
         | E DISTINTO E
         | E SUMA E
         | E RESTA E
         | E MULT E
         | E DIVISION E
         | E POTENCIA E
         | E MODULO E
         | E CONCAT E
         | E BAND E
         | E BOR E
         | E MOVD E
         | E MOVI E
         | E NUMERAL E
         | E AS E
         | E PUNTO E
         | E IGUAL E
         | VIRGULILLA E %prec UBNOT
         | RESTA E %prec UMINUS
         | SUMA E %prec UPLUS
         | PARI E PARD
         | CALL
         | LITERAL
```