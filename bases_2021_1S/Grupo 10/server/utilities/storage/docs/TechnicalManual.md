# MANUAL TÉCNICO

## Indice

- [Introducción](#introducción)
- [Objetivos](#objetivos)
- [Alcances del proyecto](#alcances-del-proyecto)
- [Descripción de estructura](#descripcin-de-estructura)
- [Requerimientos funcionales](#requerimientos-funcionales)
- [Atributos del sistema](#atributos-del-sistema)
- [Método de trabajo](#mtodo-de-trabajo)
- [Valores de retorno](#valores-de-retorno)
- [Recursos externos](#recursos-externos)
- [Diagrama de clases](#diagrama-de-clases)

## Introducción

En el presente documento se detallan los elementos técnicos detrás de la funcionalidad de AVLMode, realizado por los 
estudiantes del [grupo 16](https://github.com/tytusdb/tytus/tree/main/storage/team16) de Estructuras de Datos. Así mismo 
se justifica las decisiones tomadas a lo largo de la elaboración de la fase en busca de una implementación completa y 
robusta sin poner en riesgo la eficiencia que caracteriza a la estructura AVLTree, es decir, la utilización apropiada de 
análisis de algoritmos. 

## Objetivos

### General

Brindar una herramienta robusta y completa que permita la gestión y control de datos a un nivel eficiente y funcional. 
Basada en una estructura específica que maximiza el tiempo de búsqueda, siendo el objetivo principal ser óptima para un 
DataBase Management System (DBMS).

### Específicos

- Implementar de manera eficiente un AVLTree, para ser utilizado como la base funcional del proyecto.
- Manejar adecuadamente cualquier tipo de error humano que genere conflicto dentro de la ejecución.
- Brindar una retroalimentación adecuada de cada proceso tal y como se presenta en el [enunciado]( https://github.com/tytusdb/tytus/blob/main/docs/README.md)
- Manejar adecuadamente los datos para no perder eficiencia a pesar de la cantidad y holgura de estos.
- Permitir al usuario observar de manera gráfica los datos manejados y sus respectivas estructuras. 

## Alcances del proyecto

El alcance real del proyecto es muy amplio ya que al ser de tipo 
[open-source](https://github.com/tytusdb/tytus/blob/main/LICENSE.md) permite la implementación de AVLMode de distintas maneras. 

Pero en un principio el proyecto está pensado para la gestión y control de datos por medio de una 
estructura definida para ser complementado con otros dos módulos desarrollados en paralelo. Es decir, ser un submódulo 
funcional dentro un proyecto completo que busca implementar en su totalidad un DataBase Management System (DBMS) 
nombrado Tytus, que en un inicio es desarrollado por estudiantes de la Escuela de Ciencias y Sistemas de la Facultad de 
Ingeniería de la Universidad de San Carlos de Guatemala. 

El submódulo está orientado al manejo de los datos, por lo cual lo esperado es poder manejar correctamente estos. 
Velando principalmente por la eficiencia de procesos y la integridad/seguridad de los datos.

## Descripción de estructura

Un árbol AVL es un tipo especial de árbol binario ideado por los matemáticos rusos Adelson-Velskii y Landis. Fue el primer árbol de búsqueda binario auto-balanceable que se ideó.

Los árboles AVL están siempre equilibrados de tal modo que, para todos los nodos, la altura de la rama izquierda no difiere en más de una unidad de la altura de la rama derecha o viceversa. Gracias a esta forma de equilibrio (o balanceo), la complejidad de una búsqueda en uno de estos árboles se mantiene siempre en orden de complejidad O(log n). El factor de equilibrio puede ser almacenado directamente en cada nodo o ser computado a partir de las alturas de los subárboles.

Para garantizar la eficiencia de lo procesos, nos basamos en las búsquedas optimizadas de la estructura y para garantizar la integridad/seguridad de los datos se manejó de manera binaria. 

## Requerimientos funcionales

- Importar AVLMode o utilizar directamente la interfaz gráfica.
- Utilizar correctamente los métodos de entrada.
- Brindar los parámetros requeridos, para evitar que el proceso sea rechazado.
- Considerar las reglas en los nombres de objetos para que el proceso culmine exitosamente. 
- Contar con las librerías necesarias para la ejecución del proyecto. Por el momento solo utiliza [graphviz](https://graphviz.org/download/)
- Conocer el código de retroalimentación que retornarán los procesos.

## Atributos del sistema

- Todos los datos ingresados serán convertidos a estructuras internas y posteriormente serán guardadas de manera binaria.
- Todo proceso cuenta con una retroalimentación, la cual indicará el estado del proceso culminado.
- La interfaz gráfica es otra manera de interactuar con las funcionalidades.
- Existe una funcionalidad que genera reportes, esta es accesible por medio de la interfaz.
- La mayor parte de la funcionalidad real es implementada desde 0 por lo cual no debería existir incompatibilidad. 

## Método de trabajo

El proyecto está distribuido en módulos, para optimizar el trabajo en equipo, los módulos son los siguientes:

- BusinessLayer
- DataAccessLayer
- Models 
- View    

Toda la metodología está ligeramente inspirada en MVC donde se busca mantener separado cada uno de sus componentes para un mejor orden y control de errores. El proyecto es multiparadigma pero predomina el OOP, representado por cada clase e instancia que se maneja a lo largo de la implementación. 

### [DataAccessLayer](https://github.com/tytusdb/tytus/tree/main/storage/team16/DataAccessLayer)

Módulo que contiene la funcionalidad de guardado a archivo y reportería.

#### [Handler](https://github.com/tytusdb/tytus/blob/main/storage/team16/DataAccessLayer/handler.py)

| Nombre de la función                           | Descripción                                                            |
| ---------------------------------------------- | ---------------------------------------------------------------------- |
| `rootinstance()`                               | Valida la existencia de la raíz y la retorna.                          |
| `rootupdate(databases)`                        | Actualiza el archivo raíz, contiene las bases de datos.                |
| `tableinstance(database: str, tableName: str)` | Lee el archivo específico de la tabla y retorna la estructura.         |
| `tableupdate(table)`                           | Actualiza el contenido del archivo de la tabla específica.             |
| `exists(database: str, tableName: str)`        | Valida la existencia del archivo, es decir, busca y retorna el estado. |
| `delete(filename)`                             | Elimina el archivo especificado, desaparece el registro.               |
| `rename(oldName, newName)`                     | Utilizado en función Alter, cambia el nombre de un documento.          |
| `findCoincidences(database, tablesName)`       | Busca todos los archivos de tablas relacionadas a una base de datos.   |
| `readcsv(file)`                                | Función que retorna un archivo csv leído y cargado a memoria.          |
| `invalid(name: str)`                           | Invalida un nombre si no cumple las reglas especificadas.              |
| `reset()`                                      | Borra la carpeta de datos, permitiendo así hacer pruebas desde 0.      |
| `init_DirReports()`                            | Se encarga de crear y validar la carpeta de recursos de reportes.      |

#### [Reports](https://github.com/tytusdb/tytus/blob/main/storage/team16/DataAccessLayer/reports.py)

| Nombre de la función                           | Descripción                                                                   |
| ---------------------------------------------- | ----------------------------------------------------------------------------- |
| `graphicTables(database: str)`                 | Genera y ejecuta el archivo .dot que contiene la representación de tablas.    |
| `graphicDatabases()`                           | Genera y ejecuta el archivo .dot que contiene la representación de bases.     |
| `graphAVL(database: str, table: str)`          | Genera y ejecuta el archivo .dot que contiene la representación de un AVL.    |
| `graphTuple(database: str, table: str, index)` | Genera y ejecuta el archivo .dot que contiene la representación de una tupla. |

#### [Tree Graph](https://github.com/tytusdb/tytus/blob/main/storage/team16/DataAccessLayer/tree_graph.py)

| Nombre de la función | Descripción                                  |
| -------------------- | -------------------------------------------- |
| `export()`           | Genera el .dot del AVL y lo convierte a png. |

### [BusinessLayer](https://github.com/tytusdb/tytus/tree/main/storage/team16/BusinessLayer)

Módulo que contiene la funcionalidad real del proyecto, aquí ocurren todos los métodos indicados.

#### [Database Module](https://github.com/tytusdb/tytus/blob/main/storage/team16/BusinessLayer/database_module.py)

| Nombre de la función                                      | Descripción                                                                                |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `createDatabase(self, database: str)`                     | Crea una base de datos y la concatena al archivo raíz.                                     |
| `showDatabases(self)`                                     | Retorna todas las bases de datos existentes.                                               |
| `alterDatabase(self, databaseOld: str, databaseNew: str)` | Cambia el valor de una base da datos, actualiza la raíz y todos los archivos dependientes. |
| `dropDatabase(self, database: str)`                       | Elimina la base de datos del archivo raíz y todas las tablas relacionadas.                 |
| `dropAll(self)`                                           | Limpia por completo los datos del proyecto.                                                |

#### [Table Module](https://github.com/tytusdb/tytus/blob/main/storage/team16/BusinessLayer/table_module.py)

| Nombre de la función                                                                            | Descripción                                                                      |
| ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `createTable(self, database: str, table: str, numberColumns: int)`                              | Crea una tabla y genera el archivo propio.                                       |
| `showTables(self, database: str)`                                                               | Retorna el nombre de todas las tablas relacionadas a la base de datos.           |
| `extractTable(self, database: str, table: str)`                                                 | Retorna todos las tuplas contenidas en una tabla específica.                     |
| `extractRangeTable(self, database: str, table: str, columnNumber: int, lower: any, upper: any)` | Retorna valores de una tabla contenidos en un rango especificado.                |
| `alterAddPK(self, database: str, table: str, columns: list)`                                    | Crea una PK dentro una tabla que determinará directamente el ingreso de valores. |
| `alterDropPK(self, database: str, table: str)`                                                  | Elimina la PK pero se mantiene la estructura hasta agregar una nuevamente.       |
| `alterTable(self, database: str, tableOld: str, tableNew: str)`                                 | Cambia el nombre de una tabla.                                                   |
| `alterAddColumn(self, database: str, table: str, default: any)`                                 | Ingresa un valor por defecto en una nueva columna en cada registro.              |
| `alterDropColumn(self, database: str, table: str, columnNumber: int)`                           | Elimina una columna específica dentro de todos los registros de una tabla.       |
| `dropTable(self, database: str, table: str)`                                                    | Elimina un tabla, su contenido y la relación con la base de datos.               |

#### [Tuple Module](https://github.com/tytusdb/tytus/blob/main/storage/team16/BusinessLayer/tuple_module.py)

| Nombre de la función                                                     | Descripción                                                                        |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| `insert(self, database: str, table: str, register: list)`                | Ingresa y administra el orden de los nodos dentro de una tabla.                    |
| `loadCSV(self, file: str, database: str, table: str)`                    | Carga el archivo y administra el insert masivo.                                    |
| `extractRow(self, database: str, table: str, columns: list)`             | Retorna los valores de una tupla específica.                                       |
| `update(self, database: str, table: str, register: dict, columns: list)` | Actualiza el contenido de una tupla, recorriendo y validando por medio del índice. |
| `delete(self, database: str, table: str, columns: list)`                 | Elimina una tupla por completo.                                                    |
| `truncate(self, database: str, table: str)`                              | Elimina todos los valores dentro de una tabla.                                     |

### [Models](https://github.com/tytusdb/tytus/tree/main/storage/team16/Models)

Módulo que contiene la estructura y sus métodos relacionados.

#### [AVL Tree](https://github.com/tytusdb/tytus/blob/main/storage/team16/Models/avl_tree.py)

| Nombre de la función                                     | Descripción                                                   |
| -------------------------------------------------------- | ------------------------------------------------------------- |
| `add(self, index, content)`                              | Ingresa un nodo dentro del árbol, respetando las condiciones. |
| `search(self, index)`                                    | Busca un el contenido de una tupla, basado en su índice.      |
| `update(self, index, content)`                           | Actualiza el contenido de una tupla.                          |
| `tolist(self)`                                           | Retorna una lista con todos los registros de la tabla.        |
| `indexes(self)`                                          | Retorna una lista con todos los índices de la tabla.          |
| `massiveupdate(self, action: str, arg)`                  | Actualiza masivamente todos los registros (agrega o elimina)  |
| `delete(self, index)`                                    | Elimina un nodo basado en el índice.                          |
| `range(self, columnNumber: int, lower: any, upper: any)` | Retorna los registros dentro del rango indicado.              |
| `preorder(self)`                                         | Imprime el contenido en un recorrido preorden(antes)          |
| `inorder(self)`                                          | Imprime el contenido en un recorrido enorden(en medio)        |
| `postorder(self)`                                        | Imprime el contenido en un recorrido postorden(después)       |

#### [Node](https://github.com/tytusdb/tytus/blob/main/storage/team16/Models/node.py)

| Nombre de la función | Descripción                                  |
| -------------------- | -------------------------------------------- |
| `get()`              | Función generalizada, retorna el contenido   |
| `set()`              | Función generalizada, configura el contenido |

### [View](https://github.com/tytusdb/tytus/tree/main/storage/team16/View)

Módulo que contiene la funcionalidad de la interfaz. 

#### [Interfaz](https://github.com/tytusdb/tytus/blob/main/storage/team16/View/Interfaz.py)

| Nombre de la función                   | Descripción                                                            |
| -------------------------------------- | ---------------------------------------------------------------------- |
| `initComp(self)`                       | Inicializa la interfaz.                                                |
| `centrar(self)`                        | Genera el cálculo necesario para mantener siempre centrada la ventana. |
| `ventanaFunciones(self)`               | Genera la ventana de funciones.                                        |
| `ventanaReporte(self)`                 | Genera la ventana de reportes.                                         |
| `main(self)`                           | Carga todos los elementos de la ventana principal.                     |
| `funciones(self)`                      | Carga todos los elementos de la ventana de funcionalidad.              |
| `reportes(self)`                       | Carga todos los elementos de la ventana de reportes                    |
| `displayDBData(self, event)`           | Muestra las bases de datos en el sistema.                              |
| `displayTableData(self, event)`        | Muestra las tablas en el sistema.                                      |
| `displayTupleData(self, event)`        | Muestra las tuplas en el sistema.                                      |
| `simpleDialog(self, args, action)`     | Genera el popup de ingreso de datos.                                   |
| `cargarArchivo(self, btn)`             | Permite la carga de un csv.                                            |
| `ejecutar(self, dialog, args, action)` | Ejecuta todas las funciones del proyecto.                              |
| `run()`                                | Corre la interfaz.                                                     |

#### [Controller](https://github.com/tytusdb/tytus/blob/main/storage/team16/View/Icontroller.py)

Contiene la conexión entre la interfaz y el AVLMode.

| Nombre de la función                          | Descripción                          |
| --------------------------------------------- | ------------------------------------ |
| `execute(self, args, action)`                 | Ejecuta la instrucción indicada.     |
| `reportDB()`                                  | Genera el reporte de bases de datos. |
| `reportTBL(database: str)`                    | Genera el reporte de tablas.         |
| `reportAVL(database: str, table: str)`        | Genera el reporte de AVL.            |
| `reportTPL(database: str, table: str, llave)` | Genera el reporte de tupla.          |
| `getIndexes(database: str, table: str)`       | Devuelve los índices de un AVL.      |

> `Controller` Básicamente es un puente entra la interfaz y la funcionalidad. 

### [AVLMode](https://github.com/tytusdb/tytus/blob/main/storage/team16/avlMode.py)

 Archivo que contiene todas las funciones del proyecto, este mismo es el que debe ser importado.

> `AVLMode` No contiene implementación de funcionalidad, solo la reúne. 

## Valores de retorno

| Nombre de la función                                                                      | Retorno | Interpretación             |
| ----------------------------------------------------------------------------------------- | ------- | -------------------------- |
| Database                                                                                  |         |                            |
| `createDatabase(database: str)`                                                           | 0       | Operación exitosa          |
|                                                                                           | 1       | Error en la operación      |
|                                                                                           | 2       | Base de datos existente    |
| `showDatabase()`                                                                          | list    | Proceso exitoso            |
|                                                                                           | [ ]     | Error en la operación      |
| `alterDatabase(databaseOld, databaseNew)`                                                 | 0       | Operación exitosa          |
|                                                                                           | 1       | Error en la operación      |
|                                                                                           | 2       | DatabaseOld no existente   |
|                                                                                           | 3       | DatabaseNew existente      |
| `dropDatabase(database: str)`                                                             | 0       | Operación exitosa          |
|                                                                                           | 1       | Error en la operación      |
|                                                                                           | 2       | Base de datos no existente |
| Table                                                                                     |         |                            |
| `createTable(database: str, table: str, numberColumns: int)`                              | 0       | Operación exitosa          |
|                                                                                           | 1       | Error en la operación      |
|                                                                                           | 2       | Base de datos inexistente  |
|                                                                                           | 3       | Tabla existente            |
| `showTables(database: str)`                                                               | list    | Proceso exitoso            |
|                                                                                           | [ ]     | No hay tablas              |
|                                                                                           | None    | Error en la operación      |
| `extractTable(database: str, table: str)`                                                 | list    | Proceso exitoso            |
|                                                                                           | [ ]     | No hay datos               |
|                                                                                           | None    | Error en la operación      |
| `extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any)` | list    | Proceso exitoso            |
|                                                                                           | [ ]     | No hay datos               |
|                                                                                           | None    | Error en la operación      |
| `alterAddPK(database: str, table: str, columns: list)`                                    | 0       | Operación exitosa          |
|                                                                                           | 1       | Error en la operación      |
|                                                                                           | 2       | Base de datos inexistente  |
|                                                                                           | 3       | Tabla inexistente          |
|                                                                                           | 4       | PK existente               |
|                                                                                           | 5       | Columna fuera de límites   |
| `alterDropPK(database: str, table: str)`                                                  | 0       | Operación exitosa          |
|                                                                                           | 1       | Error en la operación      |
|                                                                                           | 2       | Base de datos inexistente  |
|                                                                                           | 3       | Tabla inexistente          |
|                                                                                           | 4       | PK inexistente             |
| `alterTable(database: str, tableOld: str, tableNew: str)`                                 | 0       | Operación exitosa          |
|                                                                                           | 1       | Error en la operación      |
|                                                                                           | 2       | Base de datos inexistente  |
|                                                                                           | 3       | TableOld inexistente       |
|                                                                                           | 4       | TableNew existente         |
| `alterAddColumn(database: str, table: str, default: any) `                                | 0       | Operación exitosa          |
|                                                                                           | 1       | Error en la operación      |
|                                                                                           | 2       | Base de datos inexistente  |
|                                                                                           | 3       | Tabla inexistente          |
| `alterDropColumn(database: str, table: str, columnNumber: int)`                           | 0       | Operación exitosa          |
|                                                                                           | 1       | Error en la operación      |
|                                                                                           | 2       | Base de datos inexistente  |
|                                                                                           | 3       | Tabla inexistente          |
| `dropTable(database: str, table: str)`                                                    | 0       | Operación exitosa          |
|                                                                                           | 1       | Error en la operación      |
|                                                                                           | 2       | Base de datos inexistente  |
|                                                                                           | 3       | Tabla inexistente          |
| Tupla                                                                                     |         |                            |
| `insert(database: str, table: str, register: list)`                                       | 0       | Operación exitosa          |
|                                                                                           | 1       | Error en la operación      |
|                                                                                           | 2       | Base de datos inexistente  |
|                                                                                           | 3       | Tabla inexistente          |
|                                                                                           | 4       | PK duplicada               |
|                                                                                           | 5       | Columna fuera de límites   |
| `loadCSV(file: str, database: str, table: str)`                                           | list    | Proceso exitoso            |
|                                                                                           | [ ]     | No hay datos               |
| `extractRow(database: str, table: str, columns: list)`                                    | list    | Proceso exitoso            |
|                                                                                           | [ ]     | No hay datos               |
| `update(database: str, table: str, register: dict, columns: list)`                        | 0       | Operación exitosa          |
|                                                                                           | 1       | Error en la operación      |
|                                                                                           | 2       | Base de datos inexistente  |
|                                                                                           | 3       | Tabla inexistente          |
|                                                                                           | 4       | PK inexistente             |
| `delete(database: str, table: str, columns: list)`                                        | 0       | Operación exitosa          |
|                                                                                           | 1       | Error en la operación      |
|                                                                                           | 2       | Base de datos inexistente  |
|                                                                                           | 3       | Tabla inexistente          |
|                                                                                           | 4       | PK inexistente             |
| `truncate(database: str, table: str)`                                                     | 0       | Operación exitosa          |
|                                                                                           | 1       | Error en la operación      |
|                                                                                           | 2       | Base de datos inexistente  |
|                                                                                           | 3       | Tabla inexistente          |

## Recursos externos

- [csv](https://docs.python.org/3/library/csv.html)

- [graphviz](https://graphviz.org/download/)

- [PIL](https://pypi.org/project/Pillow/)

- [pickle](https://docs.python.org/3/library/pickle.html)

- [re](https://docs.python.org/3/library/re.html)

- [tkinter](https://docs.python.org/3/library/tkinter.html)

- [shutil](https://docs.python.org/3/library/shutil.html)
  
  > `graphviz` Única librería externa, con licencia autorizada.

## Diagrama de clases

<div align="center" alt="Diagrama">
  <img src="img/class.png" />
</div>
