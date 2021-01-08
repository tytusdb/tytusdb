## FASE II - SQL PARSER



## Introducción

La fase dos del segundo proyecto fue elaborado por el grupo 1. En el período de vacaciones de diciembre 2020 para el curso de Organización de Lenguajes y Compiladores 2. Por parte de la universidad de San Carlos de Guatemala, de la Facultad de Ingeniería. 

Este proyecto toma de base el codigo de la fase uno del grupo 26. Utilizando para su construcción el lenguaje de programación PYTHON y la herramienta de análisis léxico y sintáctico PLY.

## Funcionalidades

Para la fase 2 el proyecto es ampliado con el reconocimiento de nuevas instrucciones, la generación de codigo en 3  direcciones y la optimización de código.

La ampliación de este proyecto sigue en base al lenguanje de gestión de  bases de datos de código abierto PostgresSQL, por lo tanto la sintaxis de las funciones ampliadas 

Entre las funciones de esta fase se encuentran:

* Creación de Índices
  * Create Index 
* Modificación de Índices
  * Alter Index
* Eliminación de Índices
  * Drop Index 
* Creación de Reporte de los Índices en la tabla de símbolos
* Generación de código en tres direcciones, este código es generado en un archivo.py 
* Ejecución del código generado en tres direcciones
* Creación de Funciones de lenguaje procedural SQL - PL/pgsSQL
* Creación de Procedimientos de lenguaje procedural SQL - PL/pgsSQL
* Eliminación de Funciones de lenguaje procedural SQL - PL/pgsSQL
* Eliminación de Procedimientos de lenguaje procedural SQL - PL/pgsSQL
* Utilizar por medio del comando execute las Funciones de lenguaje procedural SQL - PL/pgsSQL
* Utilizar por medio del comando execute los Procedimientos de lenguaje procedural SQL - PL/pgsSQL
* Generación de código intermedio de las funcionalidades agregadas

* Optimización de código a partir del archivo generado de codigo intermedio
  * Se aplican reglas de Optimización por Mirilla
* Reporte de reglas de optimización aplicadas
* Generar Reporte AST
* Generación de reporte gramatical con notación BNF realizado automáticamente.
* Consola de salida con información sobre operaciones realizadas.
* Ejecutar las nuevas funcionalidades agregadas



## Instrucciones reconocidas:



Instrucciones regulares para SQL

Ejemplos:

``` sql
CREATE DATABASE DBFase2;

USE DBFase2;

CREATE TABLE tbProducto (idproducto integer not null primary key,
  						 producto varchar(150) not null,
  						 fechacreacion date not null,
						 estado integer);
						 
INSERT INTO tbProducto values(1,'Laptop Lenovo',now(),1);
INSERT INTO tbProducto values(2,'Bateria para Laptop Lenovo T420',now(),1);
INSERT INTO tbProducto values(3,'Teclado Inalambrico',now(),1);

update tbProducto set estado = 2 where estado = 1;

select myFuncion('Crea funcion Nueva de Mensaje');
```



Instrucciones para Índices 

Ejemplos:

``` sql
CREATE UNIQUE INDEX idx_producto ON tbProducto (idproducto);
CREATE UNIQUE INDEX idx_califica ON tbCalificacion (idcalifica);
CREATE INDEX ON tbbodega (lower(bodega));
DROP INDEX idx_bodega
CREATE INDEX misind6 ON mitab6 USING HASH (casa);
CREATE INDEX mising4 ON tretab USING GIN (estosi);
```



Instrucciones SQL - PL/pgsSQL

Ejemplos:

``` sql
CREATE FUNCTION fn_Mensaje(texto text) RETURNS text AS $$
BEGIN
	RETURN texto;
END;
$$ LANGUAGE plpgsql;

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

DROP FUNCTION if exists myFuncion;

CREATE PROCEDURE sp_insertaproducto(llave integer,producto varchar(100),fecha date)
language plpgsql
as $$
begin
	insert into tbProducto values(llave,producto,fecha,1);
end; $$	
EXECUTE sp_insertaproducto(9,'Bocina Inalambrica','2021-01-06');
EXECUTE sp_insertaproducto(10,'Audifonos con Microfono USB','2021-01-06');
EXECUTE sp_insertaproducto(11,'Bocina Inalambrica','2021-01-06');
EXECUTE sp_insertaproducto(12,'Monitor de 17"','2021-01-06');

```



Fragmento de Generación de Código Intermedio

Ejemplos:

``` sql
from sentencias import *
from goto import with_goto
@with_goto  # Decorador necesario.

def main():
   t1='TEST'
   t2= createDB(t1)
   
   t3='TYTUS'
   t4= createDB(t3)
   
   t5='TEST'
   t6= useDatabase(t5)
   
   t7='TEST'
   t8='TBCALIFICA'
   t9=3
   t10= createTbl(t7,t8,t9)
   
   t11='TEST'
   t12='TBPRODUCTO'
   t13=4
   t14= createTbl(t11,t12,t13)
   
   t15='TEST'
   t16='TBPRODUCTO'
   t18=[]
   t18.append(1)
   t18.append('Laptop Lenovo')
   t18.append('2021-01-06 13:00:28')
   t18.append(1)
   t19=t18
   t20= existTableC3D(t15,t16)
   if t20 is False :
       goto .labelt21 
   else :
       goto .labelt20 
   label .labelt20
   t21= insertC3D(t15,t16,t19)
   label .labelt21
```



Optimización de código Intermedio 

Para esta optimización se utilizpo el método por mirilla , con 18 reglas disponibles para aplicar

Ejemplos de reglas:

``` sql
Regla 				Código					Optimización
No.8				X = X + 0				#Se elimina instrucción
No.9				X = X - 0				#Se elimina instrucción
No.10				X = X * 1				#Se elimina instrucción
No.11				X = X / 1				#Se elimina instrucción
No.12				X = Y + 0				X=Y
No.13				X = Y - 0				X=Y
No.14				X = Y * 1				X=Y
No.15				X = Y / 1				X=Y


```

















