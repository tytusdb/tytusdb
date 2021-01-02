# Manual de Usuario *TytusDB*
<p align="center">
  <img src="/parser/team14/img/logotytus.png" width="100" alt="Presentación">
</p>

### Universidad de San Carlos de Guatemala
### Organización de Lenguajes y Compiladores 2 
### Facultad de Ingeniería
### Interprete TytusDB

# Introducción
### 1. Objetivo
Este manual tiene como finalidad dar a conocer a los usuarios finales las caracteristicas
y formas de funcionamiento básicas de **tytusDB**
### 2. Requerimientos tecnicos para el uso del sistema
- Sistema operativo [Windows 7/8/10 o Linux]
- Python 3
- Graphviz 	[2.40.1 o superior]
- PLY [4.0]
- Configuración de pantalla con resolución 1245x600 pixeles o superior

## Descripcion de TytusDB
El sistema es un proyecto Open Source bajo una licencia MIT que tiene diferentes caracteristicas de un administrador de base de datos. Este sistema para su correcta
funcionalidad depende de la interración del usuario final, la interfaz y el interprete de tytusDB para obtener el resultado esperado
analizando las entradas SQL de PostgreSQL y dando como resultado las consultas esperadas.

### Flujo del programa
<p align="center">
  <img src="/parser/team14/img/FlujoI.png" width="700" alt="Presentación">
</p>

## ¿Como funciona el programa?
### Paso 1: *Ejecutar la aplicación TytusDB*
<p align="center">
  <img src="/parser/team14/img/Interfaz.png" width="700" alt="Presentación">
</p>

Como se puede observar la interfaz de usuario es muy amigable y entendible ya que solo cuenta con:
- Dos consolas, 1 para el ingreso de instrucciones SQL y la otra para
visualizar los resultados obtenidos por el interprete de tytusDB.
- Una opción de ejecutar para empezar el proceso de interpretación de codigo SQL ingresado
- Una opción de reportes para poder generar y visualizar los reportes lexicos, sintactis y el arbol AST generado despues de la interpretación del código.

### Paso 2: *Ingresar las instrucciones SQL.*
<p align="center">
  <img src="/parser/team14/img/Consola.jpeg" width="700" alt="Presentación">
</p>

Para obtener el resultado de la imagen anterior debe seguir los siguientes pasos:
1. Debe ingresar las instrucciones SQL en la primera consola
2. Presionar el boton **Ejecutar** para ejecutar las instrucciones SQL ingresadas
3. Luego en la segunda consola se podrá visualizar los resultados obtenidos de cada instrucción SQL ingresada
4. Por ultimo si desea puede presionar el boton reportes y elegir el reporte a visualizar.

<p align="center">
  <img src="/parser/team14/img/ReportesI.png" width="700" alt="Presentación">
</p>

Como se puede observar el apartado de reportes cuenta con diferentes opciones que se describen a continuación:

#### Reporte de errores lexicos y sintacticos
<p align="center">
  <img src="/parser/team14/img/ReporteE.png" width="700" alt="Presentación">
</p>
Este reporte se genera durante la interpretación del codigo SQL ingresado, analizando linea por linea e instrucción por instrucción para verificar que se haya
ingresado la sintaxis correcta, si hubo algun error en alguna linea el mismo continua el proceso pero el error queda almacenado ya sea lexico o sintactico 
para ser visualizado despues en este apartado.

#### Reporte del arbol AST
<p align="center">
  <img src="/parser/team14/img/ReporteAST.png" width="700" alt="Presentación">
</p>
Este reporte se genera durante la ejecución y tiene como finalidad grafica mediante un arbol el flujo de la gramatica de la entrada SQL ingresada.

#### Reporte de la gramatica
<p align="center">
  <img src="/parser/team14/img/Gramatica.png" width="700" alt="Presentación">
</p>
Este reporte tambien se genera durante la ejecución y tiene como finalidad mostrar en formato BNF la gramatica obtenida del flujo realizado por la entrada SQL ingresada.

#### Reporte de la tabla de simbolos
<p align="center">
  <img src="/parser/team14/img/TablaS.png" width="700" alt="Presentación">
</p>
Este reporte se genera durante la ejecución y tiene como finalidad mostrar en una tabla los simbolos que interactuan en el sistema como lo son los nombres de bases de datos,
tablas, los atributos de las tablas, entre otros para lograr identificar de forma gráfica el almacenamiento y funcionamiento del sistema.


## Autores
### Grupo 14
* **Walter Josue Paredes Sol** - *201504326*
* **Asunción Mariana Sic Sor** - *201504051*
* **Wendy Aracely Chamalé Boch** - *201504284*
* **Carlos Eduardo Torres Caal** - *201504240*
