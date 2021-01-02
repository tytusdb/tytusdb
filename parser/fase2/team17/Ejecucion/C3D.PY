from Fase1.Sql import Sql
from goto import with_goto

heap = None

def inter():
    global  heap
    sql:Sql = Sql()
    sql.run(heap)


@with_goto
def principal():
    global heap

    heap  = """ 
--  Manipulacion de datos
 CREATE DATABASE IF NOT EXISTS test
     OWNER = 'root'
     MODE = 1;

 SHOW DATABASES;

 USE test;

 create table tbcalifica
 ( iditem integer primary key,
   item   varchar(150),
   puntos decimal(8,2),
   seccion integer
 );

 insert into tbcalifica values (1,'Funcionalidades básicas',2.0,0);
 insert into tbcalifica values (2,'Funciones Date-Extract',2.0,0);

use test;
SELECT * FROM tbcalifica;
    
    """

    t1 = 5
    t2 = 3

    if t1>t2:
        goto .L1

    goto .L2


    label .L1
    inter()

    label .L2
    print('es falso')


#if(a > b) goto L1;
#goto L2;
#L1:
#   //codigo si es verdadero
#L2:
#   //código si es falso




if __name__ == '__main__':
    principal()
