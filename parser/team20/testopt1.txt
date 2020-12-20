CREATE DATABASE db1;
CREATE DATABASE db1 OWNER diego MODE = 1;
CREATE OR REPLACE DATABASE db1;
CREATE DATABASE IF NOT EXISTS db1;
CREATE OR REPLACE DATABASE IF NOT EXISTS db1;
create table tbpuesto 
( idpuesto smallint not null,
  puesto character(25),
  salariobase money,
 primary key (idpuesto)
);

insert into tbpuesto values (1,'Recepcionista','4,000');