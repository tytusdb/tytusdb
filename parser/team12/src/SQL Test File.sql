CREATE OR REPLACE DATABASE PRUEBA;
USE PRUEBA;
CREATE TABLE EMPLEADO(
    idEmpleado INTEGER,
    nombreEmpelado VARCHAR (2)
);
CREATE TABLE PUESTO(
    idPuesto INTEGER,
    nombrePuesto VARCHAR (2)
);

CREATE TABLE EMPLEADO_PUESTO(
    idEmpleado INTEGER,
    idPuesto INTEGER
);
SELECT idpuesto FROM empleado,  puesto;