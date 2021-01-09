CREATE DATABASE DBFase2;

USE DBFase2;


create table tbbodega (idbodega integer not null primary key,
					   bodega varchar(100) not null,
					   estado integer);
								  
CREATE INDEX idexbodega ON tbbodega (bodega);

create procedure sp_validainsert()
language plpgsql
as $$
begin
	insert into tbbodega values(1,'BODEGA CENTRAL', 1);
	insert into tbbodega values(2,'BODEGA ZONA 12', 1);
	insert into tbbodega values(3,'BODEGA ZONA 11', 1);
	insert into tbbodega values(4,'BODEGA ZONA 1', 1);
	insert into tbbodega values(5,'BODEGA ZONA 10', 1);
	
end; $$
								 
EXECUTE sp_validainsert();

create procedure sp_validaupdate()
language plpgsql
as $$
begin
	update tbbodega set bodega = 'bodega zona 9' where idbodega = 4; 
end; $$

EXECUTE sp_validaupdate();

							 

CREATE FUNCTION myFuncion(texto text) RETURNS text AS $$
BEGIN
	RETURN texto;
END;
$$ LANGUAGE plpgsql;

select myFuncion('INICIO CALIFICACION FASE 2');

CREATE TABLE tbProducto (idproducto integer not null primary key,
  						 producto varchar(150) not null,
  						 fechacreacion date not null,
						 estado integer);

CREATE UNIQUE INDEX idx_producto ON tbProducto (idproducto);

CREATE TABLE tbCalificacion (idcalifica integer not null primary key,
							 item varchar(100) not null,
							 punteo integer not null);

CREATE UNIQUE INDEX idx_califica ON tbCalificacion (idcalifica);
						 
INSERT INTO tbProducto values(1,'Laptop Lenovo',NOW(),1);
INSERT INTO tbProducto values(2,'Bateria para Laptop Lenovo T420',NOW(),1);
INSERT INTO tbProducto values(3,'Teclado Inalambrico',NOW(),1);
INSERT INTO tbProducto values(4,'Mouse Inalambrico',NOW(),1);
INSERT INTO tbProducto values(5,'WIFI USB',NOW(),1);
INSERT INTO tbProducto values(6,'Laptop HP',NOW(),1);
INSERT INTO tbProducto values(7,'Teclado Flexible USB',NOW(),1);
INSERT INTO tbProducto values(8,'Laptop Samsung','2021-01-02',1);

select myFuncion('Crea Funcion');


CREATE FUNCTION ValidaRegistros(tabla varchar(50),cantidad integer) RETURNS integer AS $$
DECLARE 
resultado INTEGER = 0; 
retorna   INTEGER = 0;
BEGIN

	if tabla = 'tbProducto' then
	    resultado := 8;
    	if cantidad = resultado then
			retorna = 1;
		else 
			retorna = 0;
		end if;
	end if;
	if tabla = 'tbProductoUp' then
	    resultado := 0;
    	if cantidad = resultado then
			retorna = 1;
		else 
			retorna = 0;
		end if;
	end if;
	if tabla = 'tbbodega' then
	    resultado := 5;
    	if cantidad = resultado then
			retorna = 1;
		else 
			retorna = 0;
		end if;
	end if;
RETURN retorna;
END;
$$ LANGUAGE plpgsql;

insert into tbCalificacion values(1,'Create Table and Insert',ValidaRegistros('tbProducto',8));

update tbProducto set estado = 2 where estado = 1;

insert into tbCalificacion values(2,'Update',ValidaRegistros('tbProductoUp',8));

CREATE FUNCTION CALCULOS() RETURNS integer AS $$
DECLARE 
hora integer = 0;
SENO DECIMAL = 0;
VALOR INTEGER = 0;
ABSOLUTO DECIMAL = 0;
BEGIN
	hora := (SELECT EXTRACT(HOUR FROM TIMESTAMP '2001-02-16 20:38:40'));	
	SENO := (SELECT SIN(1));
	VALOR := TRUNC(SENO*hora, 0);	
	VALOR := VALOR + LENGTH(SUBSTRING('FASE2',1,4));					
	ABSOLUTO := ABS(SINH(-1));	
	ABSOLUTO := (ABSOLUTO*SQRT(225));
	VALOR := (VALOR + ABSOLUTO)/ACOSD(0.5);
	IF VALOR > 1 THEN
		VALOR = 20;
	ELSE
		VALOR = 10;
	END IF;
RETURN VALOR;
END;
$$ LANGUAGE plpgsql;


insert into tbCalificacion values(3,' Valida Funciones',CALCULOS());










CREATE INDEX idx_bodega ON tbbodega (bodega,estado);

DROP INDEX idx_bodega;

CREATE INDEX idx_bodega ON tbbodega (bodega, estado);																			  
/*No debe dar error el indice anterio ya no existe*/




insert into tbCalificacion values(4,'Valida Store Procedure',ValidaRegistros('tbbodega',5));
--aqui

delete from tbbodega where idbodega = 4;

insert into tbCalificacion values(5,'Valida Delete',ValidaRegistros('tbbodega',4));

select * from tbbodega;

CREATE INDEX idx_bodega ON tbbodega (estado);	
/*Debe devolver error el indice ya existe*/


CREATE PROCEDURE sp_insertaproducto(llave integer,producto varchar(100),fecha date)
language plpgsql
as $$
begin
	insert into tbProducto values(llave,producto,fecha,1);
end; $$	

EXECUTE sp_insertaproducto(9,'Bocina Inalambrica','2021-01-06');
EXECUTE sp_insertaproducto(10,'Audifonos con Microfono USB','2021-01-06');
EXECUTE sp_insertaproducto(11,'Bocina Inalambrica','2021-01-06');
EXECUTE sp_insertaproducto(12,'Monitor de 17in','2021-01-06');


CREATE FUNCTION fn_Mensaje(texto text) RETURNS text AS $$
BEGIN
	RETURN texto;
END;
$$ LANGUAGE plpgsql;



EXECUTE sp_insertaproducto(13,'Bocina Inalambrica Sony','2021-01-06');
EXECUTE sp_insertaproducto(14,'Audifonos con Microfono USB Lenovo','2021-01-06');
EXECUTE sp_insertaproducto(15,'Monitor de 21in','2021-01-06');
EXECUTE sp_insertaproducto(16,'Monitor de 17in Lenovo','2021-01-06');


create table tbinventario (
		idinventario integer not null primary key,
		idproducto   integer not null,
		idbodega     integer not null,
		cantidad     integer not null,
		fechacarga   date   not null,
		descripcion  text
);

CREATE FUNCTION fn_retornaproducto(Vproducto varchar(100)) RETURNS integer AS $$
declare idp integer = 0;
BEGIN
	idp := (select idproducto from tbProducto where tbProducto.producto = Vproducto);
	RETURN idp;
END;
$$ LANGUAGE plpgsql;

select fn_retornaproducto('Bocina Inalambrica');

CREATE FUNCTION fn_retornabodega(Vbodega varchar(100)) RETURNS integer AS $$
declare idb integer = 0;
BEGIN
	idb := (select idbodega from tbbodega where tbbodega.bodega = Vbodega);
	RETURN idb;
END;
$$ LANGUAGE plpgsql;

select fn_retornabodega('BODEGA CENTRAL');

insert into tbinventario values(-1,-1,-1,-1,NOW(),"");

create FUNCTION sp_insertainventario (ide integer,Vproducto varchar(100),Vbodega varchar(100),cantidad integer,descripcion varchar(200)) RETURNS integer AS $$
declare 
 idproducto integer = 0;
 idbodega integer = 0; 
 idev integer = 0;
BEGIN
	idev := (select count(*) from tbinventario where tbinventario.idinventario = ide);
	if idev = 0 then
		idproducto := (select fn_retornaproducto(Vproducto));
		idbodega   := (select fn_retornabodega(Vbodega));
		insert into tbinventario values(ide,idproducto,idbodega,cantidad,NOW(),descripcion);
	end if;
	RETURN ide;
END; 
$$ LANGUAGE plpgsql;	

select sp_insertainventario (1,'Laptop Lenovo','BODEGA CENTRAL',200,'Laptop Lenovo T420 i7 8GB');
select sp_insertainventario (2,'Teclado Inalambrico','BODEGA CENTRAL',100,'Teclado Inalambrico Lenovo');
select sp_insertainventario (3,'Mouse Inalambrico','BODEGA ZONA 12',50,'L');
select sp_insertainventario (4,'Laptop HP','bodega zona 9',20,'Laptop HP i5 4GB RAM');






























