# MANUAL USUARIO

### EXPLICACIÓN DEL PROYECTO
---
Se realizó en conjunto con 3 cursos del área de ingenieria en sistemas, un sistema de bases de datos, de la cuál este manual es sobre el parser. Dicho proyecto tiene por nombre TYTUS, desarrollado en python y basado en POSTGRESQL.

### REQUISITOS DEL SISTEMA
---
Los requisitos del sistema son basados en el hardware y software sobre el cual fueron programados.

#### HARDWARE
---
* Core I3 3220 or AMD Ryzen 5
* 8 GB RAM
* 200 MB Espacio almacenamiento

#### SOFTWARE
---
* Windows 10 
* Python 3.6
* Python 3.9

### LIBRERIAS UTILIZADAS PARA EL DESARROLLO

```sh
ply
Enum
tkinter
prettytable
datetime
random
decimal
math
goto
```

### INSTRUCTIVO DE USO
---

Dicha aplicación se encuentra en desarrollo actualemente, así que no se dispone de un ejecutable, pero si deseas realizar pruebas de TYTUS, debes descargar el repositorio en tu computadora, para poder ejecutar este programa debes disponer de [python](https://www.python.org/downloads/) en tu computadora, también debes realizar la instalación de ciertas librerias, mostradas anteriormente. 

Después de tener todas las herramientas instaladas, puedes utilizar la consola de windows o un editor de texto como VSCode, y ejecutar el siguiente comando:

```sh
& [RUTA DEL EJECUTABLE DE PYTHON] "[RUTA DONDE SE ENCUENTRA EL ARCHIVO INTERFACE]"

# Ejemplo:

 & C:/Python/python.exe "e:/CursosUSAC/COMPI 2/OLC2-FASE1/expresion/interface.py"
 ```

 Y listo puedes probar las funcionalidades de Python.

### FLUJO DE LA APLICACIÓN
---
Es una aplicación de escritorio, con las funciones principales de un editor de texto, dicha aplicación incluye las funciones como Guardar, Guardar Como, Abrir, Buscar, Reemplazar; puedes editar el código entre diferentes tabs, y ejecutar dicho código SQL y Pl/SQL, mostrando el resultado de cada instrucción en su consola. Por ende la interfaz de la aplicación es muy intuitiva y fácil de usar.

La aplicación también tiene la opción de mostrar los reportes Gramaticales de la entrada, los errores léxicos, sintácticos y semánticos que surgen en tiempo de ejecución, la tabla de simbolos, el AST, el codigo en 3 direcciones y la optimizacion como tal, en formato PDF.

Se pueden ejecutar diferente tipos de operaciones en dicha aplicación tales como:

```sh
# MANEJO DE BASES DE DATOS

	CREATE DATABASE DBFase2;

	USE DBFase2;

# MANEJO DE TABLAS

CREATE TABLE tbProducto (idproducto integer not null primary key,
							 producto varchar(150) not null,
							 fechacreacion date not null,
							 estado integer);
        
INSERT INTO tbProducto values(1,'Laptop Lenovo',now(),1);
	INSERT INTO tbProducto values(2,'Bateria para Laptop Lenovo T420',now(),1);
	INSERT INTO tbProducto values(3,'Teclado Inalambrico',now(),1);
	INSERT INTO tbProducto values(4,'Mouse Inalambrico',now(),1);
	INSERT INTO tbProducto values(5,'WIFI USB',now(),1);
	INSERT INTO tbProducto values(6,'Laptop HP',now(),1);
	INSERT INTO tbProducto values(7,'Teclado Flexible USB',now(),1);
	INSERT INTO tbProducto values(8,'Laptop Samsung','2021-01-02',1);

# FUNCTIONS

	CREATE FUNCTION myFuncion(texto text) RETURNS text AS $$
	BEGIN
		RETURN texto;
	END;
	$$ LANGUAGE plpgsql;

	select myFuncion('INICIO CALIFICACION FASE 2');


```

Como se mencionó anteriormente, la aplicación es de escritorio para el sistema operativo Windows, así también la aplicación posee una consola de salida, para mostrar todos los valores retornados, en esta fase, el codigo 3 direcciones, de las funciones explicadas anteriormente en esta fase y la fase 1. Para más información de las funciones disponibles en TYTUS puedes consultar la documentación de [SQL](https://www.postgresql.org/docs/13/sql.html).


```sh
-----------Codigo 3 Direcciones----------
from goto import with_goto 
import C3D 

@with_goto  # Decorador necesario
def myfuncion():
	# SEGMENTO BEGIN
	# RETURN
	t1 = 
	# SEGMENTO END

def main():
 C3D.pila = 0
 C3D.ejecutar() #Crear Base de datos

 C3D.pila = 1
 C3D.ejecutar() #Usar Base de datos

 C3D.pila = 2
 C3D.ejecutar() #Llamada

 C3D.pila = 3
 C3D.ejecutar() #Creando select con parametros

 C3D.pila = 4
 C3D.ejecutar() #Crear Tabla

 C3D.pila = 5
 C3D.ejecutar() #Index

 C3D.pila = 6
 C3D.ejecutar() #Crear Tabla

 C3D.pila = 7
 C3D.ejecutar() #Index

 C3D.pila = 8
 C3D.ejecutar() #Insertado

 C3D.pila = 9
 C3D.ejecutar() #Insertado

 C3D.pila = 10
 C3D.ejecutar() #Insertado

 C3D.pila = 11
 C3D.ejecutar() #Insertado

 C3D.pila = 12
 C3D.ejecutar() #Insertado

 C3D.pila = 13
 C3D.ejecutar() #Insertado

 C3D.pila = 14
 C3D.ejecutar() #Insertado

 C3D.pila = 15
 C3D.ejecutar() #Insertado

main()
```
### GRAMÁTICA SQL REALIZADA
---

La gramática desarrollada la puede consultar en: [Gramática SQL](https://github.com/tytusdb/tytus/blob/main/parser/fase2/team23/docs/Gramatica_Ascendente_BNF)

### DOCUMENTACIÓN CONSULTADA
---

* [Índice Documentación POSTGRESQL](https://www.postgresql.org/docs/13/index.html)
* [Errores POSTGRESQL](https://www.postgresql.org/docs/10/errcodes-appendix.html)
* [PLY](https://www.dabeaz.com/ply/ply.html)
* [Prettytable](https://pypi.org/project/prettytable/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)

### DESARROLLADO POR:
---
| NOMBRE                              | CARNET        |
|                                 --- |           --- |
| Pedro Rolando Ordoñez Carrillo      |   201701187   |
| Steven Aaron Sis Hernandez          |   201706357   |
| Davis Francisco Edward Enriquez     |   201700972   |
| Luis Fernando Arana Arias           |   201700988   |
