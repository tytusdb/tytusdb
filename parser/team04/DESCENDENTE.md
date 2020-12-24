


s: INSTS


INSTS  :  INST PCOMA INSTS'
INSTS' :  INST PCOMA INSTS'
       |  epsilon


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


 OPDB : OWNER
      | MODE          


CREATE_DB : CREATE DATABASE IF NOT EXISTS A OPDB IGUAL E OPDB IGUAL A
          | CREATE DATABASE IF NOT EXISTS A OPDB IGUAL A
          | CREATE DATABASE E OPDB IGUAL A
          | CREATE OR REMPLACE DATABASE A
          | CREATE DATABASE A




DROP_DB : RDROP DATABASE A 
        | RDROP DATABASE IF EXISTS A


ALTER_DB : ALTER DATABASE E RENAME TO A
         | ALTER DATABASE E OWNER  TO A


SHOW_DB : SHOW DATABASE


USE_DB : USE DATABASE ID


 CREATE_TB : CREATE TABLE ID PARI ATRIBUTOS PARD



ATRIBUTOS : ATRIBUTO ATRIBUTOS'
ATRIBUTOS' : COMA ATRIBUTO ATRIBUTOS'
           | EPSILON



ATRIBUTO : ID TIPO CONSTRAINT E CHECK PARI E PARD 
         | ID TIPO NOT NULL PRIMARY KEY 
         | ID TIPO CHECK PARI E PARD    
         | ID TIPO NOT NULL UNIQUE
         | ID TIPO UNIQUE NOT NULL
         | ID TIPO NOT NULL
         | ID TIPO UNIQUE
         | ID TIPO    


TIPO : INTEGER  
     | VARCHAR PARI E PARD
     | REAL
     | DATE
     | BOOLEAN   


DROPTABLE : RDROP TABLE ID


DELETE : RDELETE FROM ID


INSERT : RINSERT INTO ID VALUES PARI LE PARD

 LE  : A LE'
 LE' : COMA A LE'
     | EPSILON 


CREATE_TYPE : CREATE TYPE ID AS ENUM PARI LE PARD


SELECT : RSELECT A

UNION : SELECT RUNION UNION
      | SELECT RUNION SELECT

 
 UNIONALL : SELECT RUNION ALL UNIONALL
          | SELECT RUNION ALL SELECT


INTERSECT : SELECT RINTERSECT INTERSECT
          | SELECT RINTERSECT SELECT


INTERSECTALL : SELECT RINTERSECT ALL INTERSECTALL
             | SELECT RINTERSECT ALL SELECT



EXCEPT : SELECT REXCEPT EXCEPT
              | SELECT REXCEPT SELECT'


EXCEPTALL : SELECT REXCEPT ALL EXCEPT
          | SELECT REXCEPT ALL SELECT


LITERAL : INT
        | DECIMAL
        | ID
        | CADENA
        | TRUE
        | FALSE
        | MULT



A        : B  A'
A'       : AND B A' 
         | EPSILON

B        : C  B'
B'       : OR C B'
         | EPSILON

C        : E C'
C'       :  MENORQ C' 
         | EPSILON

F        : G F'
F'       : MAUORQ F' 
         | EPSILON 

H        : I H'
H'       : MAYOURIGUAL H'
         | EPSILON  

I        : K I'
I'       : MENORQUE I'
         | EPSILON
 
L        : M L'
L'       : MAYORQUE L'         
         | EPSILON

M        : N M'
M'       : MAYORIGUAL M' 
         | EPSILON

N        : O N'      
N'       : MENORIGUAL N'
         | EPSILON

O        : P O'
O'       : IGUALQ O' 
         | EPSILON

P        : Q P'
P'       : DISTINTO P' 
         | EPSILON

Q        : R Q'
Q'       : SUMA Q'
         | EPSILON

R        : S R'
R'       : RESTA R'
         | EPSILON
   
S        : T S'
S'       : MULT S'
         | EPSILON

T        : U T'
T'       : DIVISION T'        
         | EPSILON

U        : V U'
U'       : POTENCIA U'  
         | EPSILON



V        : X V'
V'       : MODULO V'
         | EPSILON
 
X        : Y X'
X'       : CONCAT X'
         | EPSILON

Y        : Z Y'
Y'       : BAND Y'
         | EPSILON

Z        : A1  Z'
Z'       : BAND Z'
         | EPSILON

A1       : A2  A1'
A1'      : BOR A1'
         | EPSILON

A2       : A3  A2'
A2'      : MOVI A2'
         | EPSILON

A3       : A4  A3'
A3'      : MOVD A3'
         | EPSILON

A4       : A5  A4'
A4'      : NUMERAL A4'
         | EPSILON

A5       : A6  A5'
A5'      : AS A5'
         | EPSILON

A6       : A7  A6'
A6'      : PUNTO A6'
         | EPSILON

A7       : A8  A7'
A7'      : IGUAL A7'
         | EPSILON
        
A8       : PARI A9 PARD         
          
A9       : CALL     
         | LITERAL

         
    