CREATE DATABASE compiladores2;

USE compiladores2;

CREATE TABLE tbUSUARIO(
	id_ususario		INTEGER PRIMARY KEY,
	usuario		INTEGER,
	password		INTEGER
);

CREATE TABLE tbCURSO(
	id_curso		INTEGER PRIMARY KEY,
	descripcion		VARCHAR(50)
);

CREATE TABLE tbASIGNACION(
    id_asignacion   INTEGER PRIMARY KEY,
    id_ususario     INTEGER NOT NULL,
    id_curso        INTEGER NOT NULL,
    CONSTRAINT userr FOREIGN KEY (id_ususario) REFERENCES tbUSUARIO(id_ususario),
    CONSTRAINT cursoo FOREIGN KEY (id_curso) REFERENCES tbCURSO(id_curso)
);

SHOW TABLES;

ALTER TABLE tbUSUARIO ADD COLUMN telefono VARCHAR(50), direccion VARCHAR(50);

SHOW TABLES;

--OTROS
CREATE DATABASE compiladores2;

USE compiladores2;

CREATE TABLE tbUSUARIO(
	id_ususario		INTEGER PRIMARY KEY,
	usuario		    VARCHAR(50),
	password		VARCHAR(50),
    telefono        INTEGER,
    direccion       VARCHAR(50),
    edad            INTEGER
);

CREATE TABLE tbUSAURIO_ADD(
    edad2   INTEGER
)INHERITS(tbUSUARIO);

INSERT INTO tbUSUARIO VALUES (1,'Juliocotzo','password',12345678,'Guatemala',20);
INSERT INTO tbUSUARIO (id_ususario,usuario,telefono) VALUES (2,'Manuel',12345678);
INSERT INTO tbUSAURIO_ADD VALUES (1,'Juliocotzo','password',12345678,'Guatemala',20);
INSERT INTO tbUSAURIO_ADD VALUES (1,'Juliocotzo','password',12345678,'Guatemala',20,23);
INSERT INTO tbUSAURIO_ADD VALUES (1,'Juliocotzo','password',12345678,'Guatemala',20,24);




CREATE DATABASE compiladores2;

USE compiladores2;

CREATE TABLE tbUSUARIO(
	id_ususario		INTEGER PRIMARY KEY,
	usuario		    VARCHAR(50),
	password		VARCHAR(50),
    telefono        VARCHAR(50),
    direccion       VARCHAR(50),
    edad            INTEGER
);

INSERT INTO tbUSUARIO VALUES (1,'Juliocotzo','password','236388481','Pingyin',20); 
INSERT INTO tbUSUARIO VALUES (2,'LopDlMa','passwordLop','653497674','Monamon',25);
INSERT INTO tbUSUARIO VALUES (3,'azurdiajonatan','passwordAzu','305539638','Smach Mean Chey',25);
INSERT INTO tbUSUARIO VALUES (4,'mdmata20','passwordMd','512175902','El Puente',20);
INSERT INTO tbUSUARIO VALUES (5,'franciscolezana','Fpassword','232979832','Luobuqiongzi',21);
INSERT INTO tbUSUARIO VALUES (6,'gl3ncal3l','Gpassword','297163535','Houk',19);





CREATE DATABASE compiladores2;

USE compiladores2;

CREATE TABLE tbUSUARIO(
	id_ususario		INTEGER PRIMARY KEY,
	usuario		    VARCHAR(50),
	password		VARCHAR(50),
    telefono        VARCHAR(50),
    direccion       VARCHAR(50),
    edad            INTEGER
);

INSERT INTO tbUSUARIO VALUES (1,'Juliocotzo','password','236388481','Pingyin',20);
INSERT INTO tbUSUARIO VALUES (2,'LopDlMa','passwordLop','653497674','Monamon',25);
INSERT INTO tbUSUARIO VALUES (3,'azurdiajonatan','passwordAzu','305539638','Smach Mean Chey',25);
INSERT INTO tbUSUARIO VALUES (4,'mdmata20','passwordMd','512175902','El Puente',20);
INSERT INTO tbUSUARIO VALUES (5,'franciscolezana','Fpassword','232979832','Luobuqiongzi',21);
INSERT INTO tbUSUARIO VALUES (6,'gl3ncal3l','Gpassword','297163535','Houk',19);







SELECT usuario,usuario FROM tbUSUARIO;

CREATE DATABASE compiladores2;

USE compiladores2;


CREATE TABLE tbUSUARIO(
	id_ususario		INTEGER,
	usuario		VARCHAR(50),
	password		VARCHAR(50)
);

CREATE TABLE tbCURSO(
	id_curso		INTEGER,
	descripcion		VARCHAR(50)
);

CREATE TABLE tbASIGNACION(
    id_asignacion   INTEGER,
    id_ususario     INTEGER,
    id_curso        INTEGER
);


INSERT INTO tbCURSO VALUES (2,'Compi2');
INSERT INTO tbCURSO VALUES (1,'Compi1');

INSERT INTO tbUSUARIO VALUES(1,'Juliocotzo','passJ');
INSERT INTO tbUSUARIO VALUES(2,'Diego','passD');
INSERT INTO tbUSUARIO VALUES(3,'Fraaans','passF');

INSERT INTO tbASIGNACION VALUES(1,1,1);
INSERT INTO tbASIGNACION VALUES(2,1,2);
INSERT INTO tbASIGNACION VALUES(3,2,1);
INSERT INTO tbASIGNACION VALUES(4,2,2);

SELECT * FROM tbCURSO tC, tbASIGNACION tA WHERE tC.id_curso == tA.id_curso;