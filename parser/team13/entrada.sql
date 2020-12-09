-- ARCHIVO DE ENTRADA PARA PRUEBAS
CREATE DATABASE hola;

-- ACTUALIZACIÓN DE TABLA
UPDATE weather SET temp_lo = temp_lo+1, temp_hi = temp_lo+15, prcp = cadenita
WHERE city = 'San Francisco' AND date_ = '2003-07-03';


-- ELIMINACIÓN DE CAMPOS DENTRO DE UNA TABLA
DELETE FROM products WHERE price = 10;

DELETE FROM products;


-- TRUNCAR UNA TABLA
TRUNCATE bigtable, fattable;

TRUNCATE othertable; 


-- CREATE TABLE
CREATE TABLE table1(
    col1 smallint,
    col2 integer,
    col3 bigint,
    col4 decimal,
    col5 numeric,
    col6 real,
    col7 double precision,
    col8 money);

CREATE TABLE table1(col1 varchar(3), col2 char(3), col5 text, col3 character varying(3), col4 character(3));

CREATE TABLE tab1(col1 date, col2 timestamp, col3 time, col4 interval);
CREATE TABLE table1(col1 smallint, col2 integer, col3 bigint, col4 decimal, col5 numeric, col6 real, col7 double precision, col8 money,col9 varchar(3), col10 char(3), col11 text, col12 character varying(3), col13 character(3), col14 date, col5 timestamp, col6 time, col7 interval, col18 true,col19 false);
CREATE TABLE mitabla(c1 integer DEFAULT 1 NOT NULL, c2 text NOT NULL);
CREATE TABLE mitabla(c1 integer DEFAULT 1 NOT NULL, c2 text NULL,UNIQUE (c1, c2),c3 date CONSTRAINT c_c4 UNIQUE, UNIQUE (c4));
CREATE TABLE mitabla(c1 integer NOT NULL PRIMARY KEY, c2 text NOT NULL,UNIQUE (c1, c2), book_id date, available BOOLEAN NOT NULL DEFAULT TRUE,UNIQUE (c4),FOREIGN KEY (col1,col2) REFERENCES table3(co1,co2));
CREATE TABLE table1(column1 integer DEFAULT 1 NOT NULL CONSTRAINT const_name UNIQUE );
CREATE TABLE capitals (stat char(2)) INHERITS (cities);

-- SHOW TABLES
SHOW TABLES ;

-- DROP TABLE
DROP TABLE c1;

-- ALTER TABLE
ALTER TABLE tablita ALTER COLUMN c1 SET NOT NULL;

ALTER TABLE tablita rename column c1 TO c2;

alter table tablita rename column c1 to c2;

--- Modificacado-----------INSERT-----
insert into producto values ( 1,'juan',"0",1.5);
insert into producto values ( 2,'pedro',"3",1.5);
insert into producto values ( 3,'sks',"4",1.5);
insert into producto values ( 5,'s',"9",1.5);
INSERT into producto values ( 6,'N',"5",1.5);
--- Modificacado-----------ALTER-----
ALTER TABLE products ADD COLUMN nombre_columna text;
ALTER TABLE products ADD CHECK (10 <> 5);
ALTER TABLE products ADD FOREIGN KEY (column_group_id) REFERENCES column_groups;
ALTER TABLE products DROP COLUMN description;
ALTER TABLE carro DROP CONSTRAINT some_name;








