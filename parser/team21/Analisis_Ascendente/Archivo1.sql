--Manipulacion de datos
CREATE DATABASE IF NOT EXISTS test
    OWNER = 'root'
    MODE = 1;

CREATE DATABASE IF NOT EXISTS califica
    OWNER = 'root'
    MODE = 2;

CREATE DATABASE IF NOT EXISTS califica2
    OWNER = 'root'
    MODE = 3;
USE database test; -- agregar database

SELECT 'VALIDA CREATE DATABASE' as'VALIDA CREATE DATABASE';

create table tbcalifica
( iditem integer not null primary key,
  item   varchar(150) not null,
  puntos decimal(8,2) not null
);

CREATE TABLE tbusuario (
    idusuario integer NOT NULL primary key,
	nombre varchar(50),
	apellido varchar(50),
	usuario varchar(15)  UNIQUE NOT NULL,
	password varchar(15) NOT NULL,
	fechacreacion date 
);
CREATE TABLE tbroles (
    idrol integer NOT NULL primary key,
	rol varchar(15)
);

SELECT 'VALIDA TIPO DE DATOS' AS 'VALIDA TIPO DE DATOS';


SELECT EXTRACT(YEAR FROM TIMESTAMP '2001-02-16 20:38:40');
SELECT date_part('hour', INTERVAL '4 hours 3 minutes');
SELECT now();
SELECT EXTRACT(HOUR FROM TIMESTAMP '2001-02-16 20:38:40');
SELECT EXTRACT(MINUTE FROM TIMESTAMP '2001-02-16 20:38:40');
SELECT EXTRACT(SECOND FROM TIMESTAMP '2001-02-16 20:38:40');
SELECT EXTRACT(YEAR FROM TIMESTAMP '2001-02-16 20:38:40');
SELECT EXTRACT(MONTH FROM TIMESTAMP '2001-02-16 20:38:40'); -- eliminar i
SELECT EXTRACT(DAY FROM TIMESTAMP '2001-02-16 20:38:40');
SELECT date_part('minutes', INTERVAL '4 hours 3 minutes');
SELECT date_part('seconds', INTERVAL '4 hours 3 minutes 15 seconds');
SELECT CURRENT_DATE;
SELECT CURRENT_TIME;
SELECT TIMESTAMP 'now';

SELECT 'VALIDA Funciones Date-Extract' AS 'VALIDA Funciones Date-Extract';

/*Type*/
CREATE TYPE area AS ENUM ('CONTABILIDAD','ADMINISTRACION','VENTAS','TECNOLOGIA','FABRICA');
SELECT 'VALIDA TYPE' AS 'VALIDA TYPE';

create table tbempleado 
( idempleado integer not null UNIQUE PRIMARY KEY,
  primernombre varchar(50) not null,
 segundonombre varchar(50),
 primerapellido varchar(50) not null,
 segundoapellido varchar(50),
 fechadenacimiento DATE CONSTRAINT birth_data CHECK (fechadenacimiento > '1900-01-01'),
 fechacontratacion DATE CHECK (fechacontratacion > '1900-01-01'),  --unicamente cadenas o datos primitivos
 idestado integer
);

CREATE TABLE tbempleadopuesto
(
	idempleado integer not null PRIMARY key, -- debe existir llave primaria
	idpuesto   integer not null,
	departamento area
);

 alter table tbempleadopuesto
 add constraint FK_empleado
 foreign key (idempleado)
 references tbempleado(idempleado);
  
 alter table tbempleadopuesto
 add constraint FK_empleado
 foreign key (idempleado)
 references tbempleado(idempleado);


insert into tbempleadopuesto values(1,1,'ADMINISTRACION');
insert into tbempleadopuesto values(2,1,'CONTABILIDAD');
insert into tbempleadopuesto values(3,3,'CONTABILIDAD');
insert into tbempleadopuesto values(4,6,'VENTAS');
insert into tbempleadopuesto values(5,6,'VENTAS');

SHOW DATABASES; 
SELECT 'VALIDA SHOW DATBASE' as 'VALIDA SHOW DATBASE';


DROP DATABASE  IF EXISTS  califica2;
SELECT 'VALIDA DROP DATABASE' AS 'VALIDA DROP DATABASE';


DROP TABLE tbroles;
SELECT 'VALIDA DROP TABLES' AS 'VALIDA DROP TABLES';

CREATE TABLE tbrol (
    idrol integer NOT NULL primary key,
	rol varchar(15)
);


insert into tbcalifica values (1,'Funcionalidades básicas',2.0);
insert into tbcalifica values (2,'Funciones Date-Extract',2.0);

select * from tbcalifica;

CREATE TABLE tbrolxusuario (
    idrol integer NOT NULL primary key,  -- primary key
	idusuario integer NOT NULL 
);

SELECT 'VALIDA CREATE TABLES' as 'VALIDA CREATE TABLES';

 alter table tbrolxusuario
 add constraint FK_rol
  foreign key (idrol)
  references tbrol(idrol);
  
   alter table tbrolxusuario
 add constraint FK_usuario
  foreign key (idusuario)
  references tbusuario(idusuario);

SELECT 'VALIDA ALTER TABLES' as 'VALIDA ALTER TABLES';

--insert into tbrolxusaurio values(1,1);
--Error 23503


insert into tbrol values (1,'Administrador');
insert into tbrol values (2,'Admin');
insert into tbrol values (3,'Ventas');
--insert into tbrole values (1,'root');
--Error 23505


select * from tbrol;

insert into tbcalifica values (3,'Type',2.0);
insert into tbcalifica values (4,'Create Database-replace',3.0);
insert into tbcalifica values (5,'Show Database',2.0);

alter table tbcalifica add column seccion integer;
update tbcalifica set seccion = 2;




insert into tbcalifica values (6,'Database-Alter,drop',4.0,3);
insert into tbcalifica values (7,'Create Table- Variantes',4.0,3);

insert into tbusuario values(1,'Luis Fernando','Salazar Rodriguez','lsalazar',MD5('paswword'),now());
--Error 22001

ALTER TABLE tbusuario
    ALTER COLUMN password TYPE varchar(80);


create table tbcalifica2
( iditem integer not null primary key,
  item   varchar(150) not null,
  puntos decimal(8,2) not null
);
DROP TABLE tbcalifica2;

insert into tbcalifica values (8,'Drop table',2.0,3);
insert into tbcalifica values (9,'Alter table',4.0,3);
	
insert into tbusuario values(1,'Luis Fernando','Salazar Rodriguez','lsalazar',MD5('paswword'),now());
insert into tbusuario values(1,'Maria Cristina','Lopez Ramirez','mlopez',MD5('Diciembre'),now());
insert into tbusuario values(1,'Hugo Alberto','Huard Ordoñez','hhuard',MD5('Rafael'),now());
--Error 23505
insert into tbusuario values(1,'Luis Fernando','Salazar Rodriguez','lsalazar',MD5('paswword'),now());
insert into tbusuario values(2,'Maria Cristina','Lopez Ramirez','mlopez',MD5('Diciembre'),now());
insert into tbusuario values(3,'Hugo Alberto','Huard Ordoñez','hhuard',MD5('Rafael'),now());
insert into tbusuario values(3,'Hugo Alberto','Huard Ordoñez','hhuard',MD5('Rafael'),now());
insert into tbusuario values(4,'Pedro Peter','Parker','ppeter',MD5('Donatelo'),now());
insert into tbusuario values(5,'Mariana Elizabeth','Zahabedra Lopez','melizabeth',MD5('Miguel123'),now());
insert into tbusuario values(6,'Lisa Maria','Guzman','lmaria',MD5('Diciembre$$2020'),now());
insert into tbusuario values(7,'Aurelio','Baldor','abaldor',MD5('Algebra$*'),now());
insert into tbusuario values(8,'Elizabeth Taylor','Juarez','etaylor',MD5('hilbilly'),now());
insert into tbusuario values(9,'Lois','Lane','llane',MD5('smallville'),now());
							 
select * from tbusuario;
							 
insert into tbrolxusuario values(1,1);
insert into tbrolxusuario values(2,2);
insert into tbrolxusuario values(2,3);
insert into tbrolxusuario values(3,4);
insert into tbrolxusuario values(3,5);
insert into tbrolxusuario values(3,6);
insert into tbrolxusuario values(2,7);
insert into tbrolxusuario values(3,8);
insert into tbrolxusuario values(2,9); 

select * from tbrolxusuario;
						 
insert into tbrol values (4,'IT');
insert into tbrol values (5,'Gerencia');
							 

insert into tbusuario values(10,'Duff','Mackagan','dmackagan',MD5('sweetchild'),now());
insert into tbrolxusuario values(1,10);
insert into tbusuario values(11,'Carlos','Mendez Chingui','cmendez',MD5('niebla@@'),now());			
insert into tbusuario values(12,'Diego','Joachin','omendez',MD5('raizanimal'),now());		
insert into tbusuario values(13,'Carlos Mauricio','Ordoñez Toto','cordonez',MD5('radioviejo'),now());		
insert into tbusuario values(14,'Fernando','Gonzalez','fgonzalez',MD5('1245678$net'),now());
insert into tbusuario values(15,'Walter','Reynoso Alvarado','wreynoso',MD5('corona*virus'),now());

insert into tbrolxusuario values(1,11);
insert into tbrolxusuario values(1,12);
insert into tbrolxusuario values(1,13);

SELECT 'VALIDA MANIPULAR DATOS' as 'VALIDA MANIPULAR DATOS';
							 
select * from tbrolxusuario;
					 
create table tbestado
( idestado integer not null PRIMARY KEY,
  estado varchar(30)
);


SELECT 'VALIDA CREATE TABLES - VARIANTES' as 'VALIDA CREATE TABLES - VARIANTES';
							 
 alter table tbempleado
 add constraint FK_estado
  foreign key (idestado)
  references tbestado(idestado);
  
CREATE TABLE cities (
    name            text primary key,  -- primary key
    population      decimal(8,2),
    elevation       integer     -- in feet
);

CREATE TABLE capitals (
    state           character(2)  -- problemas con character
) INHERITS (cities);

insert into capitals values ('GT','GUATEMALA',17000000,2500);

select * from capitals;
SELECT 'VALIDA HERENCIA' as 'VALIDA HERENCIA';
							 

select case when seccion = 1 then 'Caracteristicas'
			when seccion = 2 then 'Funcionalidades básicas'
			when seccion = 3 then 'Manipulacion de datos'
		end Seccion,item,puntos
from tbcalifica;

SELECT 'VALIDA CASE' as 'VALIDA CASE';


create table tbempleadoidentificacion(
	idempleado integer not null primary key,
	identificacion varchar(25) not null,
	ididentificaciontipo integer
);

create table tbidentificaciontipo(
	ididentificaciontipo integer not null primary key,
	tipoidentificacion varchar(20)
);

alter table tbempleadoidentificacion
add constraint FK_identificaciontipo
foreign key (ididentificaciontipo)
references tbidentificaciontipo(ididentificaciontipo);

insert into tbidentificaciontipo values(1,'DPI');
insert into tbidentificaciontipo values(2,'Nit');
insert into tbidentificaciontipo values(3,'Pasaporte');

select * from tbidentificaciontipo;

insert into tbestado values(1,'Activo');
insert into tbestado values(2,'Inactivo');

select * from tbestado;

insert into tbempleado (idempleado,primernombre,primerapellido,fechanacimiento,fechacontartacion,idestado) values(1,'Thelma','Esquit','1981-01-25','2014-07-06',1);

--Error 42703

insert into tbempleado (idempleado,primernombre,primerapellido,fechadenacimiento,fechacontratacion,idestado) 
values(1,'Thelma','Esquit','1981-01-25','2014-07-06',1);
insert into tbempleado (idempleado,primernombre,primerapellido,fechadenacimiento,fechacontratacion,idestado) 
values(2,'Maria','Lopez','1990-12-01','2016-09-21',1);
insert into tbempleado (idempleado,primernombre,segundonombre,primerapellido,fechadenacimiento,fechacontratacion,idestado) 
values(3,'Julio','Roberto','Rodriguez','1985-06-05','2012-01-22',1);
insert into tbempleado (idempleado,primernombre,segundonombre,primerapellido,fechadenacimiento,fechacontratacion,idestado) 
values(4,'Roberto','Benjamin','Duque','1996-04-09','2018-10-03',1);
insert into tbempleado (idempleado,primernombre,segundonombre,primerapellido,segundoapellido,fechadenacimiento,fechacontratacion,idestado) 
values(5,'Francisco','','Juarez','Perez','1997-10-05','2010-03-01',1);

--Error 42601

insert into tbempleado (idempleado,primernombre,segundonombre,primerapellido,segundoapellido,fechadenacimiento,fechacontratacion,idestado) 
values(5,'Francisco','','Juarez','Perez','1997-10-05','2010-03-01',1);

insert into tbempleado (idempleado,primernombre,segundonombre,primerapellido,segundoapellido,fechadenacimiento,fechacontratacion,idestado) 
values(6,'Bryan','Jose','Rodriguez','Santos','1900-01-01','2010-03-01',1);
--Error 23514
insert into tbempleado (idempleado,primernombre,segundonombre,primerapellido,segundoapellido,fechadenacimiento,fechacontratacion,idestado) 
values(6,'Bryan','Jose','Rodriguez','Santos','1990-02-28','2012-09-01',1);		
							 
insert into tbempleado (idempleado,primernombre,segundonombre,primerapellido,segundoapellido,fechadenacimiento,fechacontratacion,idestado) 
values(7,'Estefania','Alejandra','Soto','Mazariegos','2000-08-03','1999-09-01',1);		
--Error 23514						 
insert into tbempleado (idempleado,primernombre,segundonombre,primerapellido,segundoapellido,fechadenacimiento,fechacontratacion,idestado) 
values(7,'Estefania','Alejandra','Soto','Mazariegos','2000-08-03','2019-09-01',1);
							 
insert into tbempleado (idempleado,primernombre,segundonombre,primerapellido,segundoapellido,fechadenacimiento,fechacontratacion,idestado) 
values(8,'Katherin','','Gonzalez','Lopez','1997-10-09','2018-06-09',1);

select * from tbempleado;
							 
insert into tbempleadoidentificacion values(1,'4578-784525-6562',1);
insert into tbempleadoidentificacion values(1,'8874585-5',2);
insert into tbempleadoidentificacion values(2,'1245-488454-7854',1);
insert into tbempleadoidentificacion values(3,'2610-417055-0101',1);
insert into tbempleadoidentificacion (idempleado,ididentificaciontipo,identficacion) values(8,2,'454878-7');
--Error 42703
	 
--la linea 2 da error porque no hay llave primaria compuesta

drop table tbempleadoidentificacion;


 create table tbempleadoidentificacion(
	idempleado integer not null primary key, -- primary key
	ididentificaciontipo integer not null,
	identificacion varchar(25) not null,
	primary key(idempleado,ididentificaciontipo)
);


insert into tbempleadoidentificacion values(1,1,'4578-784525-6562');
insert into tbempleadoidentificacion values(1,2,'8874585-5');
insert into tbempleadoidentificacion values(2,1,'1245-488454-7854');
insert into tbempleadoidentificacion values(3,1,'2610-417055-0101');
insert into tbempleadoidentificacion (idempleado,ididentificaciontipo,identificacion) values(8,2,'454878-7');
insert into tbempleadoidentificacion (idempleado,identificacion,ididentificaciontipo)  values(8,'12456-1997-0101',1);		


select * from tbempleadoidentificacion;

create table tbpuesto 
( idpuesto integer not null,
  puesto character(25),
  salariobase money,
 primary key (idpuesto)
);

insert into tbpuesto values (1,'Recepcionista',4000);
-- se recupera mas no continua con el semantico ;
alter table tbpuesto
add column tinecomision boolean;

insert into tbpuesto values (2,'Asistente Contable',4500,false);
insert into tbpuesto values(3,'Contador General',9000,false);
insert into tbpuesto values(4,'Asistente de RRHH',4000,false);
insert into tbpuesto values(5,'Recepcionista Gerencia',5000,false);
insert into tbpuesto values(6,'Vendedor 1',2500,true);
insert into tbpuesto values(7,'Vendedor 2',2750,true);
insert into tbpuesto values(8,'Vendedor 3','3000',true);
insert into tbpuesto values(9,'Jefe de Ventas',4000,true);
insert into tbpuesto values(10,'Jefe de Ventas Regional',2500,true);



UPDATE tbempleadopuesto SET idpuesto = 2 where idempleado = 2;
SELECT 'VALIDA UPDATE' as 'VALIDA UPDATE';

SELECT 'VALIDA SUB QUERY' as 'VALIDA SUB QUERY';
--QUerys  solo agregué el campo a comparar en el resultado de la subquery y la otra tabla  a la subquery
select * from tbusuario US
where idusuario not exists (Select RU.*, US.* from tbrolxusuario RU, tbusuario US where RU.idusuario = US.idusuario );
/*select *
from tbusuario US
where not exists (Select * from tbrolxusuario RU where RU.idusuario = US.idusuario );*/

select * from tbrolxusuario;
SELECT 'VALIDA QUERY SIMPLE' as'VALIDA QUERY SIMPLE' ;							 
delete from tbrolxusuario where idrol = 2 and idusuario = 9;
SELECT 'VALIDA DELETE' as 'VALIDA DELETE';
insert into tbrolxusuario values(2,9); 
select * from tbrolxusaurio;							 
							 
select *
from tbrol R
where idrol not in (select idrol from tbrolxusuario);
--QUerys  solo agregué el campo a comparar en el resultado de la subquery y la otra tabla  a la subquery
select *
from tbrol R
where idrol not exists (select RU.*, R.* from tbrolxusuario RU, tbrol R where RU.idrol = R.idrol);
SELECT 'VALIDA SUB QUERY' as 'VALIDA SUB QUERY';

-- solo se agregan los campos a la consulta y el igual igual por el and
select E.*,estado,I.identificacion,tipoidentificacion, ES.idestado, I.idempleado, IT.ididentificaciontipo, I.ididentificaciontipo
from tbempleado E, tbestado ES,tbempleadoidentificacion I,tbidentificaciontipo IT
where ES.idestado == E.idestado
and I.idempleado == E.idempleado
and IT.ididentificaciontipo == I.ididentificaciontipo;
-- solo se agregan los campos a la consulta y el igual igual por el and
select E.*,estado,I.identificacion,tipoidentificacion, ES.idestado, I.idempleado, IT.ididentificaciontipo,I.ididentificaciontipo
from tbempleado E, bestado ES ,tbempleadoidentificacion I,tbidentificaciontipo IT
where ES.idestado == E.idestado
and  I.idempleado == E.idempleado
and  IT.ididentificaciontipo == I.ididentificaciontipo;
--Error 42P01
-- solo se agregan los campos a la consulta y el igual igual por el and
select E.*,estado,I.identificacion,tipoidentificacion, ES.idestado, I.idempleado, IT.ididentificaciontipo, I.ididentificaciontipo
from tbempleado E, tbestado ES ,tbempleadoidentificacion I,tbidentificaciontipo IT
where ES.idestado == E.idestado
and  I.idempleado == E.idempleado
and  IT.ididentificaciontipo == I.ididentificaciontipo;

select distinct  E.primernombre,primerapellido,fechadenacimiento,estado
from tbempleado E, tbestado ES ,tbempleadoidentificacion I,tbidentificaciontipo IT
where ES.idestado == E.idestado
and  I.idempleado == E.idempleado
and  IT.ididentificaciontipo == I.ididentificaciontipo;

-- NO RESUELVE LA COLUMNA DEL EXTRACT   CREO ESTO ENTRA A LA PRODUCCION DE FREDY  DEL SELECT DEL CASO 2 Y EL TIMESTAMP CON UNA FECHA VALIDA PORQUE NO ACEPTA NOMBRE DE CAMPO EL EXTRACT
select distinct  E.primernombre,primerapellido,EXTRACT(YEAR FROM TIMESTAMP '2001-02-16 20:38:40') AnioNacimiento,estado
from tbempleado E, tbestado ES 
where ES.idestado = E.idestado;

/*select primernombre,primerapellido,2020-Anionacimiento Edad,estado
from (select distinct  E.primernombre,primerapellido,EXTRACT(YEAR FROM fechadenacimiento) AnioNacimiento,estado
from tbempleado E, tbestado ES 
where ES.idestado = E.idestado) A*/
SELECT 'VALIDA QUERYS MULTIPLES' as 'VALIDA QUERYS MULTIPLES';

/*select primernombre,primerapellido,fechadenacimiento,'' identificacion 
from tbempleado
UNION 
select '' primernombre,'' primerapellido,now() fechadenacimiento,identificacion 
from tbempleadoidentificacion;*/

SELECT 'VALIDA UNION' as 'VALIDA UNION';

SELECT idempleado,abs(45),cbrt(13),DIV(325,5);

-- sin alias ya le puedes colocar alias pero de diferente nombre que cualquier funcion matematica o trigonometrica si no entre comillas
SELECT factorial(17) AS "factorial", 
EXP(2.0) as "Exponencial",
LN(5.0) as "Logaritmo Natural",
PI(),
POWER(5,2);


SELECT 
  width_bucket(3, 1, 12, 3),
  width_bucket(5, 1, 12, 3),
  width_bucket(9, 1, 12, 3);


create table tbfuncionesmath
(
	idfuncion integer not null primary key,
	seno decimal(10,2),
	coseno decimal(10,2)
);

insert into tbfuncionesmath values(1,0,0);
insert into tbfuncionesmath values(2,0,0);
insert into tbfuncionesmath values(3,0,0);
insert into tbfuncionesmath values(4,0,0);

update tbfuncionesmath set seno = SIN(1),coseno = COS(0) where idfuncion = 1;
update tbfuncionesmat set seno = SIND(1),coseno = TAN(0) where idfuncion = 1;
--Error 42P01
update tbfuncionesmath set seno = SIND(1),coseno = TAN(0) where idfuncion = 1;
update tbfuncionesmath set seno = TAND(0),coseno = COSD(0) where idfuncion = 2;

delete from tbfuncionesmath where idfuncion = 1;

select * from tbfuncionesmath;
-- quitar alias sis se puede con alias 
select SQRT(225) ,SIGN(14.321) ,PI(),TRUNC(67.456) , RANDOM() ,
RADIANS(15.0) , ROUND(67.456) , POWER(7.0,3), MOD(38,5), LOG(200.0) , LN(3.0) ,
FLOOR(53.6) , FACTORIAL(4),EXP(2.0),DIV(19,3);

-- SOLO AGREGAR A UN ASIN UN ALIAS PARA NO TENER ENCABEZADOS EN LA TABLA REPETIDOS
select ATAN(1),ASIN(1) "ASIN (1)",ATAND(0),ACOS(1),ACOSD(0),ASIN(1),ASIND(0),COS(0),TAN(0),SINH(2),ACOSH(2),ATANH(0),TANH(1);
SELECT length('primernombre'),substring('primerapellido',1,5),substr('primerapellido',1,5);
/*SELECT length(primernombre),substring(primerapellido,1,5),substr(primerapellido,1,5)
FROM tbempleado*/

SELECT
   CONVERT ('2015-01-01' AS DATE),
   CONVERT ('01-OCT-2015' AS DATE),
   CONVERT ('10' AS INTEGER);

/*select * 
from tbempleado
where primernombre like  '%Jul%';*/

/*select * 
from tbempleado
where primernombre NOT like  '%Jul%';*/

insert into tbcalifica values (15,'Funciones Matematicas',3.0,5);
insert into tbcalifica values (16,'Funciones Trigonometricas',3.0,5);
insert into tbcalifica values (17,'Funciones String',3.0,5);
insert into tbcalifica values (18,'Binarios',1.0,5);


