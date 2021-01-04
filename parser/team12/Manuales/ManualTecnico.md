
### UNIVERSIDAD DE SAN CARLOS DE GUATEMALA
### FACULTAD DE INGENIERIA
### ORGANIZACIÓN DE LENGUAJES Y COMPILADORES 2
### ESCUELA DE VACIONES DICIEMBRE 2020
---
# MANUAL TÉCNICO
---
## INDICE
1. Introducción
2. Objetivos
3. Alcances del proyecto
4. Requerimientos
5. Justificación de la gramática
6. Diagramas
7. Estructura
8. Glosario
---
## INTRODUCCIÓN
El presente documento detalla una los elementos basicos de Tytus DBMS, el cual fue desarrollado por alumnos del curso de compiladores 2. Documentado de la mejor manera posible
---
## OBJETIVOS
### GENERAL
* Desarrollar una aplicación robusta y completa, que sea capaz de gestionar adecuadamente el control de los datos a un nivel funcional.
## ESPECIFICOS
* El entorno gráfico de la aplicación debe de ser una interfaz amigable con el usuario, permitiendole una manipulación de datos sin complicaciones.
* A través del lenguaje de programación de python, permitir un acceso rápido e integro a los datos.
---
## ALCANCE DEL PROYECTO
* El proyecto desarrollado por los alumnos del curso de Organización de Lenguajes y Compiladores 2, tiene como alcance el desarrollar una aplicación que pueda cumplicar con la función de un DBMS el cual intervenga a favor del usuario final. 
Permitiendo dirigir y ordenar la forma en que la base de datos organiza la información. Al mismo tiempo que gestiona cada una de las fuentes para que el usuario pueda acceder a los datos automatizadamente, sin tener que buscar manualmente exactamente en qué parte del sistema se encuentra el dato específico que necesita. Tendrá la seguridad de que estará en el lugar que le corresponde.
---

## REQUERIMIENTOS
* Debe de ser desarrollado con el lenguaje Python
* Debe ser capaz de ejecutar las instruciones DML Y DDL correspondientes a SQL.
* Debe ser capaz de llevar un control adecuado de los tipos de datos.
* Debe ser capaza de obtener información a traves de consultas SQL.
* Tener un control y manejo adecuado de los archivos en los que se almacenaran los datos.
* Reportar adecuadamente los errores encontrados en las sentencias SQL ingresadas.

## Justificación de la gramática
Para el proyecto, se opto por implementar una gramatica descendente. Las gramaticas descendentes, son autómatas a pila deterministas que reconocen las frases de un lenguaje por la estrategia de vaciado de pila. Por lo que la pila es de gran ayuda al momento de implementarla. Tomando en consideración el manejo de la pila, decimos implementas este tipo de gramatica. De igual forma tomando en consideración lo siguiente:
* Fácil de entender e interpretar
* Gramática explícitamente representada
* Cada función representa un no terminal
* Adecuado para gramáticas sencillas

## Diagramas

![alt text](https://github.com/tytusdb/tytus/blob/main/parser/team12/Manuales/d.png "EncenderR")


## ESTRUCTURA
#### Carpeta ARBOL_AST
* En esta carpeta se encuentra ubicado todo lo referente a la generación del arbol AST

#### Carpeta AST
* En esta carpeta se encuentra el nodo, el cual es la base del arbol.

### Carpeta  DDL
* En esta carpeta se encuentran todos las instrucciones referente a la instrucciones de DDL:
   * CREATE table y database
   * DROP table y database
   * SHOW table y database
   * USE database

### Carpeta DML
* En esta carpeta se encuentran todos las instrucciones referente a la instrucciones de DML:
   * Sentencia Alter
   * Sentencia Delete
   * Sentencia Insert
   * Sentencia Update
   * Sentencia Select

### Carpeta DML
* En esta carpeta se encuentra la clase que maneja el entorno de la gramatica, esto para poder llevar un contexto de donde se encuentran las variables definida, etc.

### Carpeta Error
* En esta carpeta se encuentral a clase que sirve de apoyo para llevar el control de los errores.

### Carpeta Expresión
* En esta carpeta se encuentra el manejo de las expresiones logicas, aritmeticas y relacionales.

### Carpeta Funciones Nativas
* En esta carpeta se encuentra los archivos correspondientes al manejo de las funciones nativas definidase para Tytus.

### Carpeta Start
* En esta carpeta se encuentra el archivo que recorre el arbol para su respectiva ejecución

### Carpeta typeChecker
* En esta carpeta se encuentran los archivos que llevan el control local de las tabals y base de datos creadas, asi como el tipo de las columnas.

### Archivo gramatica.py
* En este archivo se encuentra definido lo que es la gramatica a implementar para el proyecto

### Archivo main.py
* en este archivo se hace uso del parser para implementarlo con la interfaz grafica.



## GLOSARIO
1. COMPILADOR: Es un Software que traduce un programa escrito en un lenguaje de programación de alto nivel (C / C ++, COBOL, etc.) en lenguaje de máquina. Un compilador generalmente genera lenguaje ensamblador primero y luego traduce el lenguaje ensamblador al lenguaje máquina.
2. ANALIZADOR: es un programa informático que analiza una cadena de símbolos de acuerdo a las reglas de una gramática formal. 
3. SQL: es un lenguaje de dominio específico utilizado en programación, diseñado para administrar, y recuperar información de sistemas de gestión de bases de datos relacionales.
4. DML: El lenguaje de manipulación de datos más popular hoy en día es SQL, usado para recuperar y manipular datos en una base de datos relacional. Otros ejemplos de DML son los usados por bases de datos IMS/DL1, CODASYL u otras.
5. DDL:Un lenguaje de base de datos o lenguaje de definición de datos (Data Definition Language, DDL por sus siglas en inglés) es un lenguaje proporcionado por el sistema de gestión de base de datos que permite a los programadores de la misma llevar a cabo las tareas de definición de las estructuras que almacenarán los datos ...
6. GRAMATICA:Es una forma de describir un lenguaje formal. La gramática permite generar cadenas a partir de un simbolo inicial y aplicando reglas que indican como ciertas combinaciones de símbolos pueden ser reemplazadas usando otras combinaciones de símbolos
7. FUNCION: En programación, una función es una sección de un programa que calcula un valor de manera independiente al resto del programa. los parámetros, que son los valores que recibe la función como entrada; ... el código de la función, que son las operaciones que hace la función; y.
8. NODO:De forma muy general, un nodo es un punto de intersección, conexión o unión de varios elementos que confluyen en el mismo lugar. En estructuras de datos dinámicas un nodo es un registro que contiene un dato de interés y al menos un puntero para referenciar (apuntar) a otro nodo.
9. DBMS:Un sistema manejador de bases de datos (SGBD, por sus siglas en inglés) o DataBase Management System (DBMS) es una colección de software muy específico, orientado al manejo de base de datos, cuya función es servir de interfaz entre la base de datos, el usuario y las distintas aplicaciones utilizadas.
10. AST: es una representación de árbol de la estructura sintáctica simplificada del código fuente escrito en cierto lenguaje de programación.
11. INTERFAZ: Se conoce como la interfaz de usuario al medio que permite a una persona comunicarse con una máquina.
12. LICENCIA MIT: Esta licencia es una Licencia de software libre permisiva lo que significa que impone muy pocas limitaciones en la reutilización y por tanto posee una excelente Compatibilidad de licencia. La licencia MIT permite reutilizar software dentro de Software propietario.
13. LLAVE FORANEA: Es llamada clave Externa, es uno o más campos de un tabla que hacen referencia al campo o campos de clave principal de otra tabla, una clave externa indica como esta relacionadas las tablas. Los datos en los campos de clave externa y clave principal deben coincidir, aunque los nombres de los campos no sean los mismos.
14. LLAVE PRIMARIA: Es un conjunto de uno o más atributos de una tabla, que tomados colectivamente nos permiten identificar un registro como único, es decir, en una tabla podemos saber cuál es un registro en específico sólo con conocer la llave primaria.
15. REGISTRO: También llamado fila o tupla, representa un objeto único de datos implícitamente estructurados en una tabla.
16. TUPLA: Conjuto de registros.