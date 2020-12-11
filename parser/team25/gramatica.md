## Gramatica
>Estructura general del archivo

    <inicial> ::= <init>
    <init> ::= <intrucciones> <instruccion> 
            | <instruccion>

    <instruccion> ::= <select> ';'
                  | <insert> ';'
                  | <update> ';'
                  | <delete> ';'
                  | <DEFINICION> ';'
>Definiciones

    <DEFINICION> ::= 'create' 'type' 'as' 'enum' '(' <LISTA_ENUM> ')'
                  | <CREATE_OR_REPLACE> 'database' <COMBINACIONES1>
                  | 'show' 'databases' 'like' regex
                  | 'show' 'databases'
                  | 'alter' 'database' id <ALTER>
                  | 'drop' 'database' 'if' 'exists' id
                  | 'drop' 'database' id
                  | 'create' 'table' id (<COLUMNAS>)

    <COLUMNAS> ::= <COLUMNA> 
                | <COLUMNAS>, <COLUMNA> 

    <COLUMNA> ::= id <TIPO> <DEFAULT> <NULLABLE> <CONSTRAINTS> <CHECKS> 
                | id <TIPO> <DEFAULT> <NULLABLE> <CONSTRAINTS>
                | id <TIPO> <DEFAULT> <NULLABLE> <CHECKS>
                | id <TIPO> <DEFAULT> <NULLABLE>
                | id <TIPO> <DEFAULT> <CONSTRAINTS> <CHECKS>
                | id <TIPO> <DEFAULT> <CONSTRAINTS>
                | id <TIPO> <DEFAULT> <CHECKS>
                | id <TIPO> <DEFAULT>
                | id <TIPO> <NULLABLE> <CONSTRAINTS> <CHECKS>
                | id <TIPO> <NULLABLE> <CONSTRAINTS>
                | id <TIPO> <NULLABLE> <CHECKS>
                | id <TIPO> <NULLABLE>
                | id <TIPO> <CONSTRAINTS> <CHECKS>
                | id <TIPO> <CONSTRAINTS>
                | id <TIPO> <CHECKS>
                | id <TIPO>
                | id <TIPO> 'primary' 'key'
                | id <TIPO> 'references' id
                | 'constraint' id 'check' (<LISTA_CONDICIONES>)
                | 'unique' (<LISTA_IDS>)
                | 'primary' 'key' (<LISTA_IDS>)
                | 'foreign' 'key' (<LISTA_IDS>) 'references' id (<LISTA_IDS>)


    <DEFAULT> ::= 'default' <VALOR>

    <NULLABLE> ::= 'not' 'null'
                | 'null'

    <CONSTRAINTS> ::= 'constraint' id 'unique'
                    | 'unique'

    <CHECKS> ::= 'constraint' id 'check' (<CONDICION>)
                |'check' (<CONDICION>) 

    <CONDICION> ::= <EXPRESION>
                 |  <CONDICION>, <EXPRESION>             

    <LISTA_CONDICIONES> ::= <CONDICIONES>
                        |   <LISTA_CONDICIONES>, <CONDICIONES>            

    <TIPO> ::= 'smallint'
            |  'integer'
            |  'bigint'
            |  'decimal'
            |  'numeric'
            |  'real'
            |  'double' 'precision'
            |  'money'
            |  'character' 'varying' ('numero')
            |  'varchar' ('numero')
            |  'character' ('numero')
            |  'char' ('numero')
            |  'text'
            |  <TIMESTAMP>
            |  'date'
            |  <TIME>
            |  <INTERVAL>
            |  'boolean'

    <TIMESTAMP> ::= 'timestamp' ('numero') 'tmstamp'
                |   'timestamp' 'tmstamp'
                |   'timestamp' ('numero') 
                |   'timestamp' 

    <TIME_ZONES>::=            

    <TIME> ::= 'time' ('numero') 'tmstamp'
            |  'time' 'tmstamp'
            |  'time' ('numero') 
            |  'time' 

    <INTERVAL> ::= 'interval' <FIELDS> ('numero')
                |  'interval' <FIELDS>
                |  'interval' ('numero')
                |  'interval'
                
    <FIELDS> ::= 'year'
              |  'month'
              |  'day'
              |  'hour'
              |  'minute'
              |  'second'

    <ALTER> ::= 'rename to' id
             | 'owner to' <NEW_OWNER>

    <NEW_OWNER> ::= id
                 | 'current_user'
                 | 'session_user'

    <COMBINACIONES1> ::= 'if' 'not' 'exists' id <COMBINACIONES2>
                      | id <COMBINACIONES2>
                      | id

    <COMBINACIONES2> ::= <OWNER>
                      |<MODE>
                      |<OWNER><MODE>
    <OWNER> ::= 'owner' id
             | 'owner' '=' id

    <MODE> ::= 'mode' entero
            | 'mode' '=' entero

    <CREATE_OR_REPLACE> ::= 'create'
                         | 'create or replace'
                  

    <LISTA_ENUM> ::= <ITEM>
                  | <LISTA_ENUM> ',' <ITEM>
    <ITEM> ::= cadena
    
>Select

    <select> ::= 'select' <lista_campos> 'from' <LISTA_IDS> 'where' <EXPRESION>
             | 'select' <lista_campos> 'from' <LISTA_IDS>


    <insert> ::= 'insert' 'into'  'id' <PARAMETROS> 'values' <PARAMETROS>


    <PARAMETROS> ::= '(' LISTA_IDS ')'

    <LISTA_IDS> ::= LISTA_IDS ',' 'ID'  
             | 'ID'

    <lista_campos>  ::=  lista_campos ',' <CAMPOS>
                 | <CAMPOS>

    <CAMPOS> ::= <CAMPO> 'as'  'ID' 
              | <CAMPO>
              | '*'

    <CAMPO>  ::= ID '.' ID
             | ID '.' '*'
             | ID


    <EXPRESION> ::= 'not' <EXPRESION>
                | '-'   <EXPRESION>
                | '<>'  <EXPRESION>
                | <EXPRESION> and   <EXPRESION>
                | <EXPRESION> or   <EXPRESION>
                | <EXPRESION> '='  <EXPRESION>
                | <EXPRESION> '!='  <EXPRESION>
                | <EXPRESION> '>='  <EXPRESION>
                | <EXPRESION> '<='  <EXPRESION> 
                | <EXPRESION>  '>'  <EXPRESION>
                | <EXPRESION>  '<'  <EXPRESION>
                | <EXPRESION>  '+'  <EXPRESION>
                | <EXPRESION>  '-'  <EXPRESION>
                | <EXPRESION>  '*'  <EXPRESION>
                | <EXPRESION>  '/'  <EXPRESION>
                | 'cadena'
                | 'numero'
                | 'decimal'
                | 'id' '.' 'id'
                | 'id'
                | '(' <EXPRESION> ')'


    <delete> ::= 'delete' 'from' id 'where' <EXPRESION>
              | 'delete' 'from' id
         

    <update> ::= 'id' 'set' <lista_asiganaciones> 'where' <EXPRESION>
              | 'id' 'set' <lista_asiganaciones>
 
    <lista_asiganaciones> ::=  <lista_asiganaciones> ',' 'id' '=' <EXPRESION>
                          |  'id' '=' <EXPRESION>
