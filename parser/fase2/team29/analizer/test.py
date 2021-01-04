from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

import analizer.grammarFP as grammar2

s = """ 
CREATE DATABASE DBFase2;

USE DBFase2;

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
						 
INSERT INTO tbProducto values(1,'Laptop Lenovo',now(),1);
INSERT INTO tbProducto values(2,'Bateria para Laptop Lenovo T420',now(),1);
INSERT INTO tbProducto values(3,'Teclado Inalambrico',now(),1);
INSERT INTO tbProducto values(4,'Mouse Inalambrico',now(),1);
INSERT INTO tbProducto values(5,'WIFI USB',now(),1);

CREATE FUNCTION ValidaRegistros(tabla varchar(50),cantidad integer) RETURNS int AS $$
DECLARE resultado INTEGER; 
		retorna   INTEGER;
BEGIN
	if tabla = 'tbProducto' then
	    resultado := (SELECT COUNT(*) FROM tbProducto);
    	if cantidad = resultado then
			retorna = 1;
		else 
			retorna = 0;
		end if;
	end if;
RETURN retorna;
END;
$$ LANGUAGE plpgsql;


insert into tbCalificacion values(1,'Create Table and Insert',ValidaRegistros('tbProducto',2));
																			  
select * from tbCalificacion;
"""
result = grammar2.parse(s)
print(result)