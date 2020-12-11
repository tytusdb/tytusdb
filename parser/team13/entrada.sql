-- ARCHIVO DE ENTRADA PARA PRUEBAS
--CREAR DATABASE
CREATE DATABASE hola;
CREATE DATABASE nueva OWNER = heidy;
CREATE DATABASE nueva2 MODE = 1;
CREATE DATABASE nueva3 OWNER= heidy MODE=2;

CREATE OR REPLACE DATABASE hola;
CREATE OR REPLACE DATABASE nueva OWNER = heidy;
CREATE OR REPLACE DATABASE nueva2 MODE = 1;
CREATE OR REPLACE DATABASE nueva3 OWNER= heidy MODE=2;

CREATE DATABASE IF NOT EXISTS hola;
CREATE DATABASE IF NOT EXISTS nueva OWNER = heidy;
CREATE DATABASE IF NOT EXISTS nueva2 MODE = 1;
CREATE DATABASE IF NOT EXISTS nueva3 OWNER= heidy MODE=2;

--SHOW DATABASE
SHOW DATABASES;
SHOW DATABASES LIKE "%nuevo%";

--ALTER DATABASE
ALTER DATABASE hola RENAME TO base;
ALTER DATABASE nueva OWNER TO base2;
ALTER DATABASE nueva2 OWNER TO CURRENT_USER;
ALTER DATABASE nueva3 OWNER TO SESSION_USER;

--DROP DATABASE
DROP DATABASE base;
DROP DATABASE IF EXISTS base;

--ENUM TYPE
CREATE TYPE mood AS ENUM ('sad', 'ok', 'happy');

--UPDATE TABLE
UPDATE weather SET temp_lo = temp_lo+1, temp_hi = temp_lo+15, prcp = cadenita
WHERE city = 'San Francisco' AND date_ = '2003-07-03';

--DELETE TABLE
DELETE FROM products WHERE price = 10;
DELETE FROM products;

--TRUNCATE TABLE
TRUNCATE bigtable, fattable;
TRUNCATE othertable;

--INSERT TABLE
insert into producto values ( 1,'juan',"0",1.5);
insert into producto values ( 2,'pedro',"3",1.5);
insert into producto values ( 3,'sks',"4",1.5);
insert into producto values ( 5,'s',"9",1.5);
INSERT into producto values ( 6,'N',"5",1.5);

--SHOW TABLE
SHOW TABLES ;

--DROP TABLE
DROP TABLE c1;

--ALTER TABLE
ALTER TABLE tablita rename column c1 TO c2;
ALTER TABLE products ADD COLUMN nombre_columna text;
ALTER TABLE products ADD CHECK (10 <> 5);
ALTER TABLE products ADD CONSTRAINT some_name UNIQUE (c1);
ALTER TABLE products ADD FOREIGN KEY (column_group_id) REFERENCES column_groups;
ALTER TABLE products ALTER COLUMN c1 SET NOT NULL;
ALTER TABLE products DROP COLUMN description;
ALTER TABLE carro DROP CONSTRAINT some_name;
CREATE TABLE table1(col1 varchar(3), col2 char(3), col5 text, col3 character varying(3), col4 character(3));
CREATE TABLE tab1(col1 date, col2 timestamp, col3 time, col4 interval);
CREATE TABLE table1(col1 smallint, col2 integer, col3 bigint, col4 decimal, col5 numeric,
col6 real, col7 double precision, col8 money,col9 varchar(3), col10 char(3), col11 text, col12 character varying(3),
col13 character(3), col14 date, col15 timestamp, col16 time, col17 interval,col18 true,col19 false);
CREATE TABLE mitabla(c1 integer DEFAULT 1 NOT NULL, c2 text NOT NULL);
CREATE TABLE mitabla(c1 integer DEFAULT 1 NOT NULL, c2 text NULL,UNIQUE (c1, c2),c3 date CONSTRAINT c_c4 UNIQUE, UNIQUE (c4));
CREATE TABLE mitabla(c1 integer NOT NULL PRIMARY KEY, c2 text NOT NULL,UNIQUE (c1, c2), book_id date, available BOOLEAN NOT NULL DEFAULT TRUE,UNIQUE (c4),FOREIGN KEY (col1,col2) REFERENCES table3(co1,co2));
CREATE TABLE table1(column1 integer DEFAULT 1 NOT NULL CONSTRAINT const_name UNIQUE );
CREATE TABLE capitals (stat char(2)) INHERITS (cities);