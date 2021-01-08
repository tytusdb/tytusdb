CREATE DATABASE IF NOT EXISTS test
    OWNER = root
    MODE = 1;

USE test;

create table tbempleado 
( idempleado integer not null UNIQUE PRIMARY KEY,
  primernombre varchar(50) not null,
 segundonombre varchar(50),
 primerapellido varchar(50) not null,
 segundoapellido varchar(50),
 fechadenacimiento DATE ,
 fechacontratacion DATE ,
 idestado integer, 
 tiempo varchar(250)
);


create table tbestado
( idestado integer not null PRIMARY KEY,
  estado varchar(30)
);


 create table tbempleadoidentificacion(
	idempleado integer not null primary key,
	identificacion integer not null,
	ididentificaciontipo integer
);


create table tbidentificaciontipo(
	ididentificaciontipo integer not null primary key,
	tipoidentificacion varchar(20)
);


insert into tbempleado values(1,'Thelma','Esquit','Thelma','Esquit','1981-01-25','2014-07-06',1, '1 years 2 months 3 days');
insert into tbempleado values(2,'Maria','Lopez','Maria','Lopez','1990-12-01','2016-09-21',1, '2 years 2 months 3 days');
insert into tbempleado values(3,'Julio','Roberto','Rodriguez','Rodriguez','1985-06-05','2012-01-22',1, '4 years 2 months 3 days');
insert into tbempleado values(4,'Roberto','Benjamin','Duque','Rodriguez','1996-04-09','2018-10-03',1, '5 years 2 months 3 days');
insert into tbempleado values(5,'Francisco','Alejandro','Juarez','Perez','1997-10-05','2010-03-01',1, '6 years 2 months 3 days');

insert into tbestado values(1,'Activo');
insert into tbestado values(2,'Inactivo');
insert into tbestado values(3,'Limbo');
insert into tbestado values(4,'Inactivo2');
insert into tbestado values(5,'Activo1');


select LENGTH(primernombre), SUBSTRING(primernombre, 1, 3), SUBSTR(primernombre, 1, 4) from tbempleado;

--select * from tbempleado where DATE_PART('years', INTERVAL tbempleado.tiempo) > 1;


