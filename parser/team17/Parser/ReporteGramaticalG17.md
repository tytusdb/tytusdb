
#### Organizacion de lenguajes y compiladores 2
#### Proyecto 1
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
   






### Gramatica ascendente 

        definitions   ::= definitions definition
                    | definition
    
        definition   ::= instruction PTCOMA
    
        instruction     ::= DataManipulationLenguage
    
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
    
