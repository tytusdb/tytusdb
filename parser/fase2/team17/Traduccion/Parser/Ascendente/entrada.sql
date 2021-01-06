begin

    tax := subtotal * 0.06;
    my_recoser_id := 20;
    SELECT table1.column1 INTO STRICT lol FROM table1;
    insert into tblibrosalario values(4,2020,10,2500,6885) RETURNING col1,col2 into var1;
    insert into tblibrosalario values(4,2020,10,2500,6885) RETURNING col1,col2 into var1;
    insert into tblibrosalario values(4,2020,10,2500,6885) RETURNING col1,col2 into  strict var1;
    update tbventa set ventaregistrada = true where idempleado = 4 and fechaventa between '2020-10-01' and '2020-10-31'RETURNING col1,col2 into var1;
    update tbventa set ventaregistrada = true where idempleado = 4 and fechaventa between '2020-10-01' and '2020-10-31'RETURNING col1,col2 into strict var1;
    delete from tbfuncionesmath where idfuncion = 1 RETURNING col1,col2 into var1;

end;

CREATE FUNCTION Fun2 (n integer, m integer)
declare ide1 integer = 'primer ide';
BEGIN
if 'uno' == 'dos' then
raise notice 'hola';
end if;
    update tbventa set ventaregistrada = true where idempleado = 4 and fechaventa between '2020-10-01' and '2020-10-31'RETURNING col1,col2 into var1;
    update tbventa set ventaregistrada = true where idempleado = 4 and fechaventa between '2020-10-01' and '2020-10-31'RETURNING col1,col2 into strict var1;
    delete from tbfuncionesmath where idfuncion = 1 RETURNING col1,col2 into var1;

END;



SELECT ValidaRegistros('lol exd',456 );


CREATE INDEX mytable_cat_1 ON mytable (data) WHERE category = 1;
CREATE INDEX test3_desc_index 	ON test3 (id DESC NULLS LAST, id DESC NULLS LAST);
CREATE UNIQUE INDEX idx_califica ON tbCalificacion (idcalifica);
CREATE UNIQUE INDEX index2 ON tbCalificacion (idcalifica);
CREATE UNIQUE INDEX index3 ON tbCalificacion (idcalifica);
CREATE UNIQUE INDEX index4 ON tbCalificacion (idcalifica);

drop INDEX            index4,test3_desc_index, index4;
drop INDEX if exists  index2 cascade;


ALTER INDEX mytable_cat_1 RENAME TO index1;

ALTER INDEX distributors SET (fillfactor = 75);
ALTER INDEX coord_idx ALTER COLUMN 3 SET STATISTICS 1000;
ALTER INDEX distributors RENAME TO suppliers;


CREATE UNIQUE INDEX idx_producto ON tbProducto (idproducto);
CREATE INDEX ON tbbodega ( ( lower(bodega) ) );
CREATE UNIQUE INDEX idx_califica ON tbCalificacion (idcalifica);


-- =================== ARCHIVO ENTRADA MAEDA ====================
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
INSERT INTO tbProducto values(6,'Laptop HP',now(),1);
INSERT INTO tbProducto values(7,'Teclado Flexible USB',now(),1);
INSERT INTO tbProducto values(8,'Laptop Samsung','2021-01-02',1);



CREATE FUNCTION ValidaRegistros(tabla varchar(50),cantidad integer) RETURNS integer AS $$
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
	if tabla = 'tbProductoUp' then
	    resultado := (SELECT COUNT(*) FROM tbProducto where estado = 2);
    	if cantidad = resultado then
			retorna = 1;
		else
			retorna = 0;
		end if;
	end if;
	if tabla = 'tbbodega' then
	    resultado := (SELECT COUNT(*) FROM tbbodega);
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
DECLARE hora integer;
DECLARE SENO DECIMAL(10,2);
DECLARE VALOR INTEGER;
DECLARE ABSOLUTO DECIMAL(10,2);
BEGIN
	hora := (SELECT EXTRACT(HOUR FROM TIMESTAMP '2001-02-16 20:38:40'));
	SENO := (SELECT SIN(1));
	VALOR := TRUNC(SENO*hora);
	VALOR := VALOR + LENGTH(SUBSTRING('FASE2',1,4));
	ABSOLUTO := ABS(SINH(-1));
	ABSOLUTO := (ABSOLUTO*SQRT(225));
	VALOR := (VALOR + ABSOLUTO)/acosd(0.5);
	IF VALOR > 1 THEN
		VALOR = 20;
	ELSE
		VALOR = 10;
	END IF;
RETURN VALOR;
END;
$$ LANGUAGE plpgsql;


insert into tbCalificacion values(3,' Valida Funciones',CALCULOS());

create table tbbodega (idbodega integer not null primary key,
					   bodega varchar(100) not null,
					   estado integer);

CREATE INDEX ON tbbodega ( ( lower(bodega) ) );



create procedure sp_validainsert()
language plpgsql
as $$
begin
	insert into tbbodega values(1,'BODEGA CENTRAL',1);
	insert into tbbodega (idbodega,bodega) values(2,'BODEGA ZONA 12');
	insert into tbbodega (idbodega,bodega,estado) values(3,'BODEGA ZONA 11',1);
	insert into tbbodega (idbodega,bodega,estado) values(4,'BODEGA ZONA 1',1);
	insert into tbbodega (idbodega,bodega,estado) values(5,'BODEGA ZONA 10',1);
end; $$

EXECUTE sp_validainsert();

insert into tbCalificacion values(4,'Valida Store Procedure',ValidaRegistros('tbbodega',5));


create procedure sp_validaupdate()
language plpgsql
as $$
begin
	update tbbodega set bodega = 'bodega zona 9' where idbodega = 4;
end; $$