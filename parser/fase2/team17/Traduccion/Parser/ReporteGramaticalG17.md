
#### Organizacion de lenguajes y compiladores 2
#### Proyecto 1 FASE 2
#### Pablo Rodrigo Barillas       201602503
#### Christopher Jhoanis Soto  201602569
#### Edgar Jonathan Arrecis     201602633
#### Nery Eduardo Herrera       201602870

## Reporte Gramatical Grupo 17

 ## Criterios de seleccion 
     Se "reduce" una cadena al símbolo inicial de la gramática.
     
     En cada paso de reducción, se sustituye una subcadena determinada que concuerda con el lado derecho de una producción por 
     el símbolo del lado izquierdo de dicha producción (básicamente se busca el lado derecho que corresponde y se reemplaza 
     por el lado izquierdo y se intenta de esa manera llegar a la raíz)Se traza una derivación por la derecha en sentido inverso.

 
    "En el análisis sintáctico ascendente: se construye el árbol sintáctico de abajo hacia arriba, lo cual disminuye 
    el número de reglas mal aplicadas con respecto al caso descendente."
    
    debido al corto tiempo que tenemos en escuela de vacaciones para la realizacion del proyecto de laboratorio
    se decidio utilizar la gramatica ascendente ya que esta tendria menos producciones y seria mucho mas sencillo
    sintetizar los elementos que implementar herencias.
    
    Al tener mas facilidad de manipulacion de los datos con estas gramaticas todo el equipo opto por trabajar de la manera
    ascendente, es decir la construccion de una gramatica ascendente la cual mostraremos a continuacion.
   






# Gramática ascendente
#### Ventajas:
- Parten de la sentencia de entrada.
- Van aplicando reglas de producción
hacia atrás (desde el consecuente hasta el antecedente).
- Proveen una menor cantidad de producciones.
#### Desventajas:
- Su excesiva generalidad no permite
que los reconocedores estén muy
optimizados.
#### Producciones:

        definitions   ::= definitions definition
                    | definition
    
        definition   ::= instruction PTCOMA
    
        instruction     ::= DataManipulationLenguage
                        |  plpgsql PTCOMA DOLAR DOLAR LANGUAGE exp
                        |  plpgsql
                        |  statements
                        
        plpgsql ::= <functions_or_procedures> <label> <declare> BEGIN <stmts> <plpgsql_ending>
                | <functions_or_procedures> <declare> BEGIN <stmts> <plpgsql_ending>
                | <functions_or_procedures> BEGIN <stmts> <plpgsql_ending>
                | <label> BEGIN <stmts> <plpgsql_ending>
                | <declare> BEGIN stmts <plpgsql_ending>
                | BEGIN <stmts> <plpgsql_ending>
                
        functions_or_procedures ::= <functions_or_procedures> <function_or_procedure>
                                | <function_or_procedure>
                                
        function_or_procedure ::= <function>
                              | <procedure>      
                              
        procedure ::= CREATE PROCEDURE ID PARIZQ <arguments> PARDER LANGUAGE ID AS DOLAR DOLAR
                  | CREATE OR REPLACE PROCEDURE ID PARIZQ <arguments> PARDER LANGUAGE ID AS DOLAR DOLAR
                  | CREATE PROCEDURE ID PARIZQ PARDER LANGUAGE ID AS DOLAR DOLAR
                  | CREATE OR REPLACE PROCEDURE ID PARIZQ PARDER LANGUAGE ID AS DOLAR DOLAR   
        
        plpgsql_ending ::= <exception> <end>
                       | <end>    
        
        exception ::= EXCEPTION <exception_whens>
        
        end ::= END ID
            | END      
            
        exception_whens ::= <exception_whens> <exception_when>
                        | <exception_when>  
        
        exception_when ::= WHEN <exp> THEN <stmts>
        
        function ::= CREATE FUNCTION ID PARIZQ <arguments> <function_ending>
                 | CREATE OR REPLACE FUNCTION ID PARIZQ <arguments> <function_ending>
                 | CREATE FUNCTION ID PARIZQ <function_ending>
                 | CREATE OR REPLACE FUNCTION ID PARIZQ <function_ending> 
        
        function_ending ::= PARDER RETURNS <types>
                        | PARDER RETURNS <types> AS DOLAR DOLAR
                        | PARDER                                                                
        
        arguments ::= <arguments> COMA <argument>
                  | <argument>
                  
        argument ::= ID <types>
        
        label ::= SHIFTIZQ ID SHIFTDER
        
        stmts ::= <stmts> <stmt>
              | <stmt>
              
        stmt ::= <DataManipulationLenguage> PTCOMA
             | <statements> PTCOMA
             
        statements ::= <conditionals>
                   | <return>
                   | <execute_procedure>
                   | <PRAISE>
                   | <callfunction>
                   | <exit>
                   | <asignacionvar>
                   | <declarer> 
                   
        exit ::= EXIT
             | EXIT ID
             | EXIT WHEN <exp>
             | EXIT ID WHEN <exp>
        
        execute_procedure ::= EXECUTE ID PARIZQ <exp_list> PARDER
                          | EXECUTE ID PARIZQ PARDER   
        
        return ::= RETURN <exp>
               | RETURN NEXT <exp>
               | RETURN QUERY <select>
               | RETURN QUERY EXECUTE <exp>
               | RETURN QUERY EXECUTE <exp> USING <exp_list>                               
                              
        DataManipulationLenguage  ::= select
    
        DataManipulationLenguage  ::= use_database
    
        DataManipulationLenguage  ::= SHOW DATABASES   
    
        use_database ::= USE ID
    
        DataManipulationLenguage  ::= createTB
    
        DataManipulationLenguage  ::= insert
    
        DataManipulationLenguage  ::= update
    
        DataManipulationLenguage  ::= deletetable
    
        DataManipulationLenguage  ::= drop_table

    
        DataManipulationLenguage  ::= create_db
    
    
        DataManipulationLenguage  ::= alter_table
    
    
        DataManipulationLenguage  ::= create_type
    
    
        DataManipulationLenguage  ::= alter_database
    

        DataManipulationLenguage  ::= drop_database
    
    
        DataManipulationLenguage  ::= select UNION select
    
    
        DataManipulationLenguage  ::= select INTERSECT select
    

        DataManipulationLenguage  ::= select EXCEPT select
    
    
        select  ::= SELECT exp_list FROM exp_list conditions
    
        select ::= SELECT exp_list FROM exp_list
    
        select ::= SELECT exp_list
    
    
        time ::= YEAR
             | HOUR
             | SECOND
             | MINUTE
             | MONTH
             | DAY
    
    
        conditions  ::= conditions condition
                    | condition
    

    
        condition  ::= WHERE exp
                        | ORDER BY exp setOrder
                        | GROUP BY exp_list
                        | LIMIT exp
                        | HAVING exp
    
    
        condition ::= subquery
    
    
    
        setOrder   ::= ASC
                       | DESC
    
    
        exp_list   ::= exp_list COMA exp
                       | exp
    
    
    
        exp   ::= COUNT PARIZQ exp PARDER
              | COUNT PARIZQ MULTI PARDER
    
    
    
        exp   ::= SUM PARIZQ exp PARDER
    
    
    
        exp   ::= AVG PARIZQ exp PARDER
    
    
        exp   ::= GREATEST PARIZQ exp_list PARDER
    
    
    
        exp   ::= LEAST PARIZQ exp_list PARDER
    
   
    
        exp   ::= MAX PARIZQ exp PARDER
    

        exp   ::= MIN PARIZQ exp PARDER
    
    
        exp   ::= ABS PARIZQ exp PARDER
    
    
        exp   ::= CBRT PARIZQ exp PARDER
    
    
    
        exp   ::= CEIL PARIZQ exp PARDER
    
    
        exp   ::= CEILING PARIZQ exp PARDER

    
        exp   ::= DEGREES PARIZQ exp PARDER

    
        exp   ::= DIV PARIZQ exp_list PARDER

    
        exp   ::= TKEXP PARIZQ exp PARDER

    
        exp   ::= FACTORIAL PARIZQ exp PARDER
    
 
        exp   ::= FLOOR PARIZQ exp PARDER
    
  
    
        exp   ::= GCD PARIZQ exp_list PARDER

        exp   ::= LN PARIZQ exp PARDER
    
    
        exp   ::= LOG PARIZQ exp PARDER
    
    
        exp   ::= MOD PARIZQ exp_list PARDER
   
    
        exp   ::= PI PARIZQ PARDER
    

    
        exp   ::= POWER PARIZQ exp_list PARDER

    
        exp   ::= RADIANS PARIZQ exp PARDER
   
    
        exp   ::= ROUND PARIZQ exp PARDER
  
    
        exp   ::= SIGN PARIZQ exp PARDER

    
        exp   ::= SQRT PARIZQ exp PARDER
    
    
        exp   ::= WIDTH_BUCKET PARIZQ exp COMA exp COMA exp COMA exp PARDER
    
    
        exp   ::= TRUNC PARIZQ exp PARDER
    
    
        exp   ::= RANDOM PARIZQ PARDER
    
    
        exp   ::= ACOS PARIZQ exp PARDER
    
    
        exp   ::= ACOSD PARIZQ exp PARDER
    
    
        exp   ::= ASIN PARIZQ exp PARDER

    
        exp   ::= ASIND PARIZQ exp PARDER
    
    
        exp   ::= ATAN PARIZQ exp PARDER

    
        exp   ::= ATAND PARIZQ exp PARDER
    
    
        exp   ::= ATAN2 PARIZQ exp COMA exp PARDER

    
        exp   ::= ATAN2D PARIZQ exp COMA exp PARDER
    
    
        exp   ::= COS PARIZQ exp PARDER
    
    
        exp   ::= SIN PARIZQ exp PARDER
    
    
        exp   ::= SIND PARIZQ exp PARDER

    
        exp   ::= TAN PARIZQ exp PARDER
    
        exp   ::= TAND PARIZQ exp PARDER
 
    
        exp   ::= SINH PARIZQ exp PARDER

    
        exp   ::= COSH PARIZQ exp PARDER
    
  
    
        exp   ::= TANH PARIZQ exp PARDER

    
        exp   ::= ASINH PARIZQ exp PARDER
    
    
        exp   ::= ACOSH PARIZQ exp PARDER

    
        exp   ::= ATANH PARIZQ exp PARDER

    
        exp   ::= SUBSTR PARIZQ exp COMA exp COMA exp PARDER

    
        exp   ::= GET_BYTE PARIZQ exp COMA exp PARDER
 
    
        exp   ::= SET_BYTE PARIZQ exp COMA exp COMA exp PARDER

    
        exp   ::= CONVERT PARIZQ exp AS types PARDER

    
        exp   ::= ENCODE PARIZQ exp COMA exp PARDER

    
        exp   ::= DECODE PARIZQ exp COMA exp PARDER

    
        exp   ::= ORBB exp
              | ORBBDOBLE exp
              | NOTBB exp
              | MAS exp
              | MENOS exp
              | NOT exp
              | IS exp
              | EXISTS exp
   
    
        exp ::= case

    
        exp ::= exp BETWEEN exp

         exp  ::= exp IS DISTINCT FROM exp
    

    
        exp   ::= exp ANDBB       exp
              | exp ORBB        exp
              | exp NUMERAL     exp
              | exp SHIFTIZQ    exp
              | exp SHIFTDER    exp
              | exp TKEXP       exp
              | exp MULTI       exp
              | exp DIVISION    exp
              | exp MODULO      exp
              | exp MAS         exp
              | exp MENOS       exp
              | exp LIKE        exp
              | exp ILIKE       exp
              | exp SIMILAR     exp
              | exp NOT         exp
              | exp IN          exp
              | exp IGUAL       exp
              | exp MAYORQUE    exp
              | exp MENORQUE    exp
              | exp MAYORIG     exp
              | exp MENORIG     exp
              | exp IS          exp
              | exp ISNULL      exp
              | exp NOTNULL     exp
              | exp AND         exp
              | exp OR          exp
              | expSimple
              | dateFunction
              | exp NOT IN exp
   
    
        expSimple   ::= NULL
                    | subquery
                    | DISTINCT exp
        dateFunction ::= EXTRACT PARIZQ time FROM TIMESTAMP exp PARDER
                     | DATE_PART PARIZQ CADENA COMA INTERVAL exp PARDER
                     | NOW PARIZQ PARDER
                     | CURRENT_DATE
                     | CURRENT_TIME
                     | TIMESTAMP CADENA
    
       expSimple ::= ID CORIZQ exp CORDER

        expSimple ::= MULTI
    
    
        expSimple ::= ID PT ID

    
        expSimple ::= ID AS ID
                  | exp AS CADENA
                  | exp AS ID
                  | exp AS CADENADOBLE
   


    
        subquery ::= PARIZQ select PARDER
                 | PARIZQ select PARDER ID
                 | PARIZQ select PARDER AS ID
    

    
     case ::= CASE WHEN exp THEN exp groupwhens ELSE exp END
          | CASE WHEN exp THEN exp groupwhens END
          | CASE WHEN exp THEN exp ELSE exp END
          | CASE WHEN exp THEN exp END
    
  
    


    
        expSimple   ::=   CADENADOBLE
    


def p_expSimples_true(t)::=

    
        createTB ::= CREATE TABLE ID PARIZQ atributesTable COMA especs inherits
                     | CREATE TABLE ID PARIZQ atributesTable inherits
                     | CREATE TABLE IF NOT EXISTS ID PARIZQ atributesTable COMA especs inherits
                     | CREATE TABLE IF NOT EXISTS ID PARIZQ atributesTable inherits

  
    
        inherits ::= PARDER INHERITS PARIZQ ID PARDER

    
        atributesTable  ::= atributesTable COMA atributeTable
                     | atributeTable

    
        nextespec ::= PRIMARY KEY PARIZQ idlist PARDER
                      | FOREIGN KEY PARIZQ idlist PARDER REFERENCES ID PARIZQ idlist PARDER
                      | CONSTRAINT ID CHECK PARIZQ exp PARDER
                      | CHECK PARIZQ exp PARDER
                      | UNIQUE PARIZQ idlist PARDER
    


    
        especificaciones ::= DEFAULT exp
                         | PRIMARY KEY
                         | REFERENCES ID
                         | CONSTRAINT ID UNIQUE
                         | CONSTRAINT ID CHECK PARIZQ exp PARDER
                         | CHECK PARIZQ exp PARDER
                         | UNIQUE
                         | NOT NULL
                         | NULL
    



def p_types(t)::=
    
         types ::= SMALLINT
              | INTEGER
              | BIGINT
              | DECIMAL
              | NUMERIC
              | REAL
              | MONEY
              | TEXT
              | TIME
              | DATE
              | TIMESTAMP
              | INTERVAL
              | BOOLEAN
              | DOUBLE PRECISION
              | CHARACTER VARYING PARIZQ exp PARDER
              | VARCHAR PARIZQ exp PARDER
              | CHAR PARIZQ exp PARDER
    

    
        insert ::= INSERT INTO ID  VALUES PARIZQ exp_list PARDER
               | INSERT INTO ID PARIZQ idlist PARDER VALUES PARIZQ exp_list PARDER
    
    
    
        update ::= UPDATE ID SET setcolumns WHERE exp
               | UPDATE ID SET setcolumns
    
   
 
    
        defAcces ::= defAcces PT newInstructions
               | defAcces  CORIZQ exp CORDER
               | ID

    
        newInstructions   ::= INSERT PARIZQ exp COMA exp PARDER
                            | INSERT PARIZQ exp PARDER
                            | SET PARIZQ exp COMA exp PARDER
                            | REMOVE PARIZQ exp PARDER
                            | SIZE PARIZQ PARDER
                            | CLEAR PARIZQ PARDER
                            | CONTAINS PARIZQ exp PARDER
                            | LENGTH PARIZQ PARDER
                            | SUBSTRING PARIZQ exp COMA exp PARDER



    
        deletetable ::= DELETE FROM ID WHERE exp
                    | DELETE FROM ID
                    | DELETE groupatributes FROM ID WHERE exp
                    | DELETE groupatributes FROM ID
    
    
        groupatributes ::= groupatributes COMA defAcces
                       | defAcces
    
   
    
        create_db ::= CREATE OR REPLACE DATABASE IF NOT EXISTS createdb_extra
                  | CREATE OR REPLACE DATABASE createdb_extra
                  | CREATE DATABASE IF NOT EXISTS createdb_extra
                  | CREATE DATABASE createdb_extra
    

    
        createdb_extra ::= ID OWNER IGUAL exp MODE IGUAL exp
                       | ID OWNER IGUAL exp MODE exp
                       | ID OWNER exp MODE IGUAL exp
                       | ID OWNER exp MODE exp
                       | ID OWNER IGUAL exp
                       | ID MODE IGUAL exp
                       | ID OWNER exp
                       | ID MODE exp
                       | ID
    
    
        drop_table ::= DROP TABLE IF EXISTS ID
                   | DROP TABLE ID
    
  
    
        alter_table ::= ALTER TABLE ID ADD listaespecificaciones
                    | ALTER TABLE ID DROP listaespecificaciones
                    | ALTER TABLE ID groupcolumns
   
    
        groupcolumns ::= groupcolumns COMA column
                    | column
    
    
        create_type ::= CREATE TYPE ID AS ENUM PARIZQ exp_list PARDER

    
        alter_database ::= ALTER DATABASE ID RENAME TO ID
                       | ALTER DATABASE ID OWNER TO CURRENT_USER
                       | ALTER DATABASE ID OWNER TO SESSION_USER
    

    
        drop_database ::= DROP DATABASE IF EXISTS ID
                      | DROP DATABASE ID
    
# Gramática descendente
#### Ventajas:
- Parten del axioma inicial.
- Van efectuando derivaciones a izquierda hasta
obtener la secuencia de derivaciones que reconoce a la sentencia.
#### Desventajas:
- Recursividad a izquierdas.
- La recursividad a izquierdas da lugar a un bucle infinito de recursion.
- Problemas de indeterminismo cuando varias alternativas en una misma produccion comparten el mismo prefijo.
- Mayor cantidad de producciones.
#### Producciones:

        <sentences>   ::= <sentences> <setInstruccions>
                      | <setInstruccions>
    

    
        <setInstruccions>   ::= <sentence> <PTCOMA>
   
    
        <sentence>     ::= <ddl>

    
        <ddl>  ::= <select>
                | <table_create>
                | <insert>
                | <update>
                | <deletetable>
                | <create_db>
                | <drop_table>
                | <alter_table>
                | <create_type>
                | <alter_database>
                | <drop_database>
    
    
        <select>  ::=  SELECT <listavalores> FROM <listavalores> <listawhere>
                | SELECT <listavalores> FROM <listavalores>
                | SELECT EXTRACT PARIZQ <time> FROM TIMESTAMP <CADENA> PARDER
                | SELECT DATE_PART PARIZQ <CADENA> COMA INTERVAL <CADENA> PARDER
                | SELECT NOW PARIZQ PARDER
                | SELECT CURRENT_DATE
                | SELECT CURRENT_TIME
                | SELECT TIMESTAMP <CADENA>
    
    
        <time> ::= YEAR
             | HOUR
             | SECOND
             | MINUTE
             | MONTH
             | DAY
    
    
        <listawhere>  ::= <listawhere> <atributoselect>
                    | <atributoselect>
    
    
        <atributoselect>  ::= WHERE <<exp>>
                        | ORDER BY <listavalores> <ordenamiento>
                        | GROUP BY <listavalores>
                        | LIMIT <<exp>>
                        | HAVING <<exp>>
                        | <subquery>
    
        <ordenamiento>   ::= ASC
                       | DESC
    
        <listavalores>   ::= <listavalores> COMA <<exp>>
                       | <<exp>>
    
        <exp>   : <case>
              | COUNT PARIZQ <exp> PARDER
              | COUNT PARIZQ MULTI PARDER
              | SUM PARIZQ <exp> PARDER
              | AVG PARIZQ <exp> PARDER
              | GREATEST PARIZQ listavalores PARDER
              | LEAST PARIZQ listavalores PARDER
              | MAX PARIZQ <exp> PARDER
              | MIN PARIZQ <exp> PARDER
              | ABS PARIZQ <exp> PARDER
              | CBRT PARIZQ <exp> PARDER
              | CEIL PARIZQ <exp> PARDER
              | CEILING PARIZQ <exp> PARDER
              | DEGREES PARIZQ <exp> PARDER
              | DIV PARIZQ <exp> COMA <exp> PARDER
              | TK<exp> PARIZQ <exp> PARDER
              | FACTORIAL PARIZQ <exp> PARDER
              | FLOOR PARIZQ <exp> PARDER
              | GCD PARIZQ <exp> COMA <exp> PARDER
              | LN PARIZQ <exp> PARDER
              | LOG PARIZQ <exp> PARDER
              | MOD PARIZQ <exp> COMA <exp> PARDER
              | PI PARIZQ PARDER
              | NOW PARIZQ PARDER
              | POWER PARIZQ <exp> COMA <exp> PARDER
              | RADIANS PARIZQ <exp> PARDER
              | ROUND PARIZQ <exp> PARDER
              | SIGN PARIZQ <exp> PARDER
              | SQRT PARIZQ <exp> PARDER
              | WIDTH_BUCKET PARIZQ <exp> COMA <exp> COMA <exp> COMA <exp> PARDER
              | TRUNC PARIZQ <exp> PARDER
              | RANDOM PARIZQ PARDER
              | ACOS PARIZQ <exp> PARDER
              | ACOSD PARIZQ <exp> PARDER
              | ASIN PARIZQ <exp> PARDER
              | ASIND PARIZQ <exp> PARDER
              | ATAN PARIZQ <exp> PARDER
              | ATAND PARIZQ <exp> PARDER
              | ATAN2 PARIZQ <exp> COMA <exp> PARDER
              | ATAN2D PARIZQ <exp> COMA <exp> PARDER
              | COS PARIZQ <exp> PARDER
              | COSD PARIZQ <exp> PARDER
              | COT PARIZQ <exp> PARDER
              | COTD PARIZQ <exp> PARDER
              | SIN PARIZQ <exp> PARDER
              | SIND PARIZQ <exp> PARDER
              | TAN PARIZQ <exp> PARDER
              | TAND PARIZQ <exp> PARDER
              | SINH PARIZQ <exp> PARDER
              | COSH PARIZQ <exp> PARDER
              | TANH PARIZQ <exp> PARDER
              | ASINH PARIZQ <exp> PARDER
              | ACOSH PARIZQ <exp> PARDER
              | ATANH PARIZQ <exp> PARDER
              | LENGTH PARIZQ <exp> PARDER
              | SUBSTRING PARIZQ <exp> COMA <exp> COMA <exp> PARDER
              | TRIM PARIZQ <exp> PARDER
              | MD5 PARIZQ <exp> PARDER
              | SHA256 PARIZQ <exp> PARDER
              | SUBSTR PARIZQ <exp> COMA <exp> COMA <exp> PARDER
              | GET_BYTE PARIZQ <exp> COMA <exp> PARDER
              | SET_BYTE PARIZQ <exp> COMA <exp> COMA <exp> PARDER
              | CONVERT PARIZQ <exp> AS tipo PARDER
              | ENCODE PARIZQ <exp> COMA <exp> PARDER
              | DECODE PARIZQ <exp> COMA <exp> PARDER
              | ORBB <exp>
              | ORBBDOBLE <exp>
              | <exp> ANDBB <exp>
              | <exp> ORBB <exp>
              | <exp> NUMERAL <exp>
              | NOTBB <exp>
              | <exp> SHIFTIZQ <exp>
              | <exp> SHIFTDER <exp>
              | MAS <exp>
              | MENOS <exp>
              | <exp> TK<exp> <exp>
              | <exp> MULTI <exp>
              | <exp> DIVISION <exp>
              | <exp> MODULO <exp>
              | <exp> MAS <exp>
              | <exp> MENOS <exp>
              | <exp> BETWEEN <exp>
              | <exp> LIKE <exp>
              | <exp> ILIKE <exp>
              | <exp> SIMILAR <exp>
              | <exp> NOT <exp>
              | <exp> IN <exp>
              | <exp> NOT IN <exp>
              | <exp> IGUAL <exp>
              | <exp> MAYORQUE <exp>
              | <exp> MENORQUE <exp>
              | <exp> MAYORIG <exp>
              | <exp> MENORIG <exp>
              | <exp> IS <exp>
              | <exp> ISNULL <exp>
              | <exp> NOTNULL <exp>
              | NOT <exp>
              | IS <exp>
              | <exp> AND <exp>
              | <exp> OR <exp>
              | <expSimple>
    
 


        <expSimple>   ::=   <ID>
                    | NULL
                    | <ID> PT <ID>
                    | <ID> <ID>
                    | <subquery> <ID>
                    | <exp> AS ID
                    | <MULTI>
                    | <subquery>
    
        <subquery> : PARIZQ <select> PARDER
    

         <case> ::= CASE WHEN <exp> THEN <exp> <lista_when> ELSE <exp> END
              | CASE WHEN <exp> THEN <exp> <lista_when>END
              | CASE WHEN <exp> THEN <exp> ELSE <exp> END
              | CASE WHEN <exp> THEN <exp> END
        
        
        <lista_when> ::= <lista_when> <when_else>
                       | <when_else>
        
        
        <when_else> ::= WHEN <exp> THEN <exp>
            
        <expSimple>  ::=   ENTERO
                    |  TKDECIMAL
                    | CADENA
                    | CADENADOBLE
                    | TRUE
                    | FALSE
                    
        
        <table_create> ::= CREATE TABLE <ID> PARIZQ <lista_table> COMA <listadolprimary> <inherits>
                         | CREATE TABLE <ID> PARIZQ <lista_table> <inherits>
                         | CREATE TABLE IF NOT EXISTS <ID> PARIZQ <lista_table> COMA <listadolprimary> <inherits>
                         | CREATE TABLE IF NOT EXISTS <ID> PARIZQ <lista_table> <inherits>
        
        
        <inherits> ::= PARDER INHERITS PARIZQ <ID> PARDER
                     | PARDER
        
    
        <lista_table>  ::= <lista_table> COMA <atributo_table>
                         | <atributo_table>
        
        
        
        <listadolprimary>  ::= <listadolprimary> COMA <lista_primary>
                             | <lista_primary>
        
        
        <lista_primary> ::= PRIMARY KEY PARIZQ <listaids> PARDER
                          | FOREIGN KEY PARIZQ <listaids> PARDER REFERENCES <ID> PARIZQ <listaids> PARDER
                          | CONSTRAINT ID CHECK PARIZQ <exp> PARDER
                          | UNIQUE PARIZQ <listaids> PARDER
        
        <atributo_table> ::= <ID>  <tipocql> <listaespecificaciones>
                           | <ID> <tipocql>
    
        <listaespecificaciones>  ::= <listaespecificaciones> <especificaciones>
                                   | <especificaciones>
        
        
        <especificaciones> ::= UNIQUE
                             | <exp>
                             | DEFAULT
                             | PRIMARY KEY
                             | FOREIGN KEY PARIZQ <listaids> PARDER REFERENCES <listaids>
                             | REFERENCES <ID>
                             | CONSTRAINT <ID>
                             | SET
                             | CHECK PARIZQ <exp> PARDER
                             | TYPE <tipo>
                             | UNIQUE PARIZQ <listaids> PARDER
        
        <tipocql> ::= <ID>
                    | <tipo>
        
        
        <tipo> ::= SMALLINT
                  | INTEGER
                  | BIGINT
                  | DECIMAL
                  | NUMERIC
                  | REAL
                  | DOUBLE PRECISION
                  | MONEY
                  | CHARACTER VARYING PARIZQ <exp> PARDER
                  | VARCHAR PARIZQ <exp> PARDER
                  | TEXT
                  | CHARACTER PARIZQ <exp> PARDER
                  | CHAR PARIZQ <exp> PARDER
                  | TIME
                  | DATE
                  | TIMESTAMP
                  | INTERVAL
                  | BOOLEAN
        
        
       <insert> ::= INSERT INTO <ID> VALUES PARIZQ <listavalores> PARDER
                   | INSERT INTO <ID> PARIZQ <listaids> PARDER VALUES PARIZQ <listavalores> PARDER
        
        <listaids> ::= <listaids> COMA <ID>
                     | <ID>
        
        <update> ::= UPDATE <ID> SET <listaupdate> WHERE <exp>
                  | UPDATE <ID> SET <listaupdate>
        
        <listaupdate> ::= <listaupdate> COMA <asignacionupdate>
                       | <asignacionupdate>
        
    
        <asignacionupdate> ::= <acceso> IGUAL <exp>
        
        
        <acceso> ::= <acceso> PT <ID>
                   | <acceso> PT <funcioncollection>
                   | <acceso>  CORIZQ <exp> CORDER
                   | <ID>
        
        <funcioncollection> ::= INSERT PARIZQ <exp> COMA <exp> PARDER
                                | INSERT PARIZQ <exp> PARDER
                                | SET PARIZQ <exp> COMA <exp> PARDER
                                | REMOVE PARIZQ <exp> PARDER
                                | SIZE PARIZQ PARDER
                                | CLEAR PARIZQ PARDER
                                | CONTAINS PARIZQ <exp> PARDER
                                | LENGTH PARIZQ PARDER
                                | SUBSTRING PARIZQ <exp> COMA <exp> PARDER
        
        
        <deletetable> ::= DELETE FROM <ID> WHERE <exp>
                        | DELETE FROM <ID>
                        | DELETE <listaatributos> FROM <ID> WHERE <exp>
                        | DELETE <listaatributos> FROM <ID>
        
        <listaatributos> ::= <listaatributos> COMA <acceso>
                           | <acceso>
        
        
        <create_db> ::= CREATE OR REPLACE DATABASE IF NOT EXISTS <createdb_extra>
                      | CREATE OR REPLACE DATABASE <createdb_extra>
                      | CREATE DATABASE IF NOT EXISTS <createdb_extra>
                      | CREATE DATABASE <createdb_extra>
        
        
        <createdb_extra> ::= <ID> OWNER IGUAL <ID> MODE IGUAL <exp>
                           | <ID> OWNER IGUAL <ID>
                           | <ID>
        
        <drop_table> ::= DROP TABLE IF EXISTS <ID>
                       | DROP TABLE <ID>
        
        
        <alter_table> ::= ALTER TABLE <ID> ADD <listaespecificaciones>
                        | ALTER TABLE <ID> DROP <listaespecificaciones>
                        | ALTER TABLE <ID> <listacolumn>
        
        <listacolumn> ::= <listacolumn> COMA <column>
                        | <column>
        
        
        <column> ::= ALTER COLUMN <ID> <listaespecificaciones>
                   | ADD COLUMN <ID <tipo>
                   | DROP COLUMN <ID>
        
        <create_type> ::= CREATE TYPE <ID> AS <ID> PARIZQ <listavalores> PARDER
        
        
        <alter_database> ::= ALTER DATABASE <ID> RENAME TO <ID>
                           | ALTER DATABASE <ID> OWNER TO <ID>
        
        <drop_database> ::= DROP DATABASE IF EXISTS <ID>
                          | DROP DATABASE <ID>
    