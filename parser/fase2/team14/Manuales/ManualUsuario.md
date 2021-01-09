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
- Python Goto
- Configuración de pantalla con resolución 1245x600 pixeles o superior

## Descripcion de TytusDB
El sistema es un proyecto Open Source bajo una licencia MIT que tiene diferentes caracteristicas de un administrador de base de datos. Este sistema para su correcta
funcionalidad depende de la interración del usuario final, la interfaz y el interprete de tytusDB para obtener el resultado esperado
analizando las entradas SQL de PostgreSQL y dando como resultado las consultas esperadas.

### Flujo del programa
<p align="center">
  <img src="/parser/team14/img/FlujoI.png" width="700" alt="Presentación">
</p>

### Diagrama interno del programa
<p align="center">
  <img src="/parser/fase2/team14/Manuales/img/DiagramaPrograma.png" width="700" alt="Presentación">
</p>

## ¿Como funciona el programa?
### Paso 1: *Ejecutar la aplicación TytusDB*
<p align="center">
  <img src="/parser/team14/img/Interfaz.png" width="700" alt="Presentación">
</p>

Como se puede observar la interfaz de usuario es muy amigable y entendible ya que solo cuenta con:
- Dos consolas, 1 para el ingreso de instrucciones SQL y la otra para
visualizar los resultados obtenidos por el interprete de tytusDB.
- Una opción de ejecutar para empezar el proceso de interpretación, traducción a codigo intermedio y optimización del codigo SQL ingresado
- Una opción de reportes para poder generar y visualizar los reportes lexicos, sintacticos, el arbol AST, la tabla de simbolos, gramatica BNF dinamico y el reporte de la optimización del código generado despues de la interpretación, traducción y optimización del código.

### Paso 2: *Ingresar las instrucciones SQL.*
<p align="center">
  <img src="/parser/fase2/team14/Manuales/img/Interfaz.png" width="700" alt="Presentación">
</p>

Como se puede observar primero se deben ingresar las instrucciones SQL en la consola de entrada y luego ubicarnos en la opción de "Ejecutar" para poder seleccionar una de las opciones descritas a continuación:

## 1. Ejecutar "Analizar Entrada"
**En esta opción se realiza el analisis y ejecución de las instrucciones SQL ingresadas**
<p align="center">
  <img src="/parser/team14/img/Consola.jpeg" width="700" alt="Presentación">
</p>

Al momento de ingresar las instrucciones SQL y haber seleccionado la opcion de **Analizar Entrada** en la consola de salida de podrá visualizar los resultados del analisis realizado a las instrucciones obteniendo como resultado las consultas esperadas por cada instrucción SQL ingresada.
Como se puede observar en la imagen anterior, se ingresaron a la consola de entrada los.

## 2. Ejecutar "Traducir a 3D"
**En esta opción se realiza la traducción a código 3D las instrucciones SQL ingresadas**
<p align="center">
  <img src="/parser/fase2/team14/Manuales/img/Traducir3D.png" width="700" alt="Presentación">
</p>

Como se puede observar en las imagen anterior se debe ingresar las instrucciones SQL, luego seleccinar la opción **Traducir a 3D** lo cual dará como resultado un mensaje en la consola de salida indicando que la traducción de las instrucciones se realizó, lo cual se puede validar en el archivo llamado prueba que contiene el codigo traducido a 3D de las instrucciones SQL ingresadas el cual queda como el de la siguiente imagen:

<p align="center">
  <img src="/parser/fase2/team14/Manuales/img/ArcTraducido3D.png" width="700" alt="Presentación">
</p>

## 3. Ejecutar "Ejecutar Codigo Traducido"
**En esta opción se realiza la ejecución de las instrucciones SQL ingresadas pero traducidas en código 3D**

Para poder validar esta opción primero tuvo que haberse realizado el paso anterior de traducir a 3D las instrucciones SQL ingresadas, si no se ha realizado la traducción no podrá ejecutar con exito esta opción; luego de haber realizado la traducción solo se debe seleccionar la opcion **Ejecutar Codigo Traducido** lo que devolvera los resultados esperados por las instrucciones SQL ingresadas pero que fueron traducidas anteriormente, dando como resultado lo siguiente:

<p align="center">
  <img src="/parser/fase2/team14/Manuales/img/EjecutarTraduccion.png" width="700" alt="Presentación">
</p>

**Nota:** Como se puede observar no hay necesidad de ingresar nada en la consola de entrada debido a que anteriormente ya se ingresaron las instrucciones y se tradujeron, pero para que sea exitosa la ejecución despues de traducir a 3D el programa debe cerrarse y volverse a abrir y ejecutar el codigo, esto debido a las modificaciones en tiempo de ejecución con python.

## 4. Ejecutar "Optimización"
**En esta opción se realiza la optimización de la traducción del código traducido a 3D de las instrucciones SQL ingresadas**
Para poder validar esta opción primero tuvo que haberse realizado el paso anterior de traducir a 3D las instrucciones SQL ingresadas, si no se ha realizado la traducción no podrá ejecutar con exito esta opción; luego de haber realizado la traducción solo se debe seleccionar la opcion **Optimizacion** lo que devolvera un archivo llamado **optimizacion.py** con el codigo 3D optimizado para luego ser ejecutado.

<p align="center">
  <img src="/parser/fase2/team14/Manuales/img/Optimizacion.png" width="700" alt="Presentación">
</p>

### Paso 3: *Generación de Reportes*
**En esta opción se realiza la generación de reportes según la opción seleccionada como se muestra en la imagen:**
<p align="center">
  <img src="/parser/fase2/team14/Manuales/img/OpReportes.png" width="700" alt="Presentación">
</p>

Las cuales se describen a continuación:

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

#### Reporte de la optimización
<p align="center">
  <img src="/parser/fase2/team14/Manuales/img/RepoOptimizacion.png" width="700" alt="Presentación">
</p>
Este reporte se genera luego de la ejecución del opción **Ejecutar Optimización** y tiene como finalidad mostrar en una tabla las reglas aplicada a cada optimización realizada al codigo 3D que fue traducido anteriormente, mostrando detalladamente la regla aplicada a cada porción del codigo 3D.

## Autores
### Grupo 14
* **Walter Josue Paredes Sol** - *201504326*
* **Asunción Mariana Sic Sor** - *201504051*
* **Wendy Aracely Chamalé Boch** - *201504284*
* **Carlos Eduardo Torres Caal** - *201504240*
