import os
from importlib import util

a = os.path.abspath("./parser/team29/analizer/interpreter.py")
name = os.path.splitext(os.path.basename(a))[0]
spec = util.spec_from_file_location(name, a)
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)


statement  = """ 

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
 insert into tbcalifica values (3,'esto es un prueba moi x',2.0,0);

use test;
SELECT * FROM tbcalifica;
    
    """

result = mod.execution(statement)

print(result)