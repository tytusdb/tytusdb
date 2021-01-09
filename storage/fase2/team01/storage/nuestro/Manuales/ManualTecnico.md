# MANUAL TÉCNICO 

UNIVERSIDAD DE SAN CARLOS DE GUATEMALA  
FACULTAD DE INGENIERÍA  
ESCUELA DE CIENCIAS Y SISTEMAS  
CURSO: ESTRUCTURA DE DATOS
___

<p align="center">
  <img src="imagenes/LOGO.png" width="800" alt="USAC">
</p>

## GRUPO 01 
* 9213640		Edwin Mauricio Mazariegos 
* 200915715		Edgar Enrique Patzan Yoc 
* 201213010		Gabriel Orlando Ajsivinac Xicay 
* 201213212		Walter Manolo Martinez Mateo 
* 201313996 	Karen Elisa López Pinto
___

- Enuncido del proyecto [enunciado]( https://github.com/tytusdb/tytus/blob/main/docs/README.md)
___

## Introducción

El presente documento detalla los elementos técnicos utilizados para la funcionalidad de este proyecto. 
También expone las tecnologías que fueron utilizadas durante la realización del proyecto.
___

## Objetivos
### General
Proporcionar una herramienta eficaz y completa que permita la gestión y control de datos a un nivel eficiente y funcional. 
Basada en una estructura específica que maximiza el tiempo de búsqueda, siendo el objetivo principal ser óptima.
### Específico
-	Implementar de manera eficiente un arbol ALV, para conciderarlo como base principal del proyecto.
-	Brindar una retroalimentación adecuada de cada proceso respecto al enunciado del proyecto 
-	Manejar adecuadamente los datos para brindar una eficiencia de alto nivel.
-	Permitir al usuario observar de manera gráfica los datos manejados y sus respectivas estructuras.
___

## Desarrollo de la Interfáz
- Software utilizado: Visual Studio Code
- Lenguaje utilizado: Python
	- Visual studio Code:  es un editor de código fuente desarrollado por Microsoft para Windows, Linux y macOS. Incluye soporte para la depuración, control integrado de Git, resaltado de sintaxis, finalización inteligente de código, fragmentos y refactorización de código. También es personalizable, por lo que los usuarios pueden cambiar el tema del editor, los atajos de teclado y las preferencias. Es gratuito y de código abierto, aunque la descarga oficial está bajo software privativo e incluye características personalizadas por Microsoft.
	- Python: es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, dinámico y multiplataforma.

## Descripción de estructura
Un árbol AVL es un tipo especial de árbol binario ideado por los matemáticos rusos Adelson-Velskii y Landis. Fue el primer árbol de búsqueda binario auto-balanceable que se ideó.
Los árboles AVL están siempre equilibrados de tal modo que, para todos los nodos, la altura de la rama izquierda no difiere en más de una unidad de la altura de la rama derecha o viceversa. Gracias a esta forma de equilibrio (o balanceo), la complejidad de una búsqueda en uno de estos árboles se mantiene siempre en orden de complejidad O(log n). El factor de equilibrio puede ser almacenado directamente en cada nodo o ser computado a partir de las alturas de los subárboles.
Para garantizar la eficiencia de lo procesos, nos basamos en las búsquedas optimizadas de la estructura y para garantizar la integridad/seguridad de los datos se manejó de manera binaria. 

## Requerimientos funcionales
-	Importar AVLMode o utilizar directamente la interfaz gráfica.
-	Utilizar correctamente los métodos de entrada.
-	Brindar los parámetros requeridos, para evitar que el proceso sea rechazado.
-	Considerar las reglas en los nombres de objetos para que el proceso culmine exitosamente. 
-	Contar con las librerías necesarias para la ejecución del proyecto.[Graphviz & Tkinter]


## Atributos del sistema
-	Todos los datos ingresados serán convertidos a estructuras internas y posteriormente serán guardadas de manera binaria.
-	Todo proceso cuenta con una retroalimentación, la cual indicará el estado del proceso culminado.
-	La interfaz gráfica es otra manera de interactuar con las funcionalidades.
-	Existe una funcionalidad que genera reportes, esta es accesible por medio de la interfaz.

## Métodos de funcionalidad general
|Nombre de la función |Descripción|
| ------------ | ------------ |
| `createDatabase(self, database: str)` | Crea una base de datos y la concatena al archivo raíz. |
| `showDatabases(self)` | Retorna todas las bases de datos existentes. |
| `alterDatabase(self, databaseOld: str, databaseNew: str)` | Cambia el valor de una base da datos, actualiza la raíz y todos los archivos dependientes. |
| `dropDatabase(self, database: str)` | Elimina la base de datos del archivo raíz y todas las tablas relacionadas. |
| `dropAll(self)` | Limpia por completo los datos del proyecto. |
| `insert(self, database: str, table: str, register: list)` | Ingresa y administra el orden de los nodos dentro de una tabla. |
| `extractRow(self, database: str, table: str, columns: list)` | Retorna los valores de una tupla específica. |
| `update(self, database: str, table: str, register: dict, columns: list)` | Actualiza el contenido de una tupla, recorriendo y validando por medio del índice. |
| `delete(self, database: str, table: str, columns: list)` | Elimina una tupla por completo. |
| `truncate(self, database: str, table: str)` | Elimina todos los valores dentro de una tabla. |

## Metodos utilizados para la funcionalidad de las Tablas
|Nombre de la función |Descripción|
| ------------ | ------------ |
| `createTable(self, database: str, table: str, numberColumns: int)` | Crea una tabla y genera el archivo propio. |
| `showTables(self, database: str)` | Retorna el nombre de todas las tablas relacionadas a la base de datos. |
| `extractTable(self, database: str, table: str)` | Retorna todos las tuplas contenidas en una tabla específica. |
| `extractRangeTable(self, database: str, table: str, columnNumber: int, lower: any, upper: any)` | Retorna valores de una tabla contenidos en un rango especificado.  |
| `alterAddPK(self, database: str, table: str, columns: list)` | Crea una PK dentro una tabla que determinará directamente el ingreso de valores. |
| `alterDropPK(self, database: str, table: str)` | Elimina la PK pero se mantiene la estructura hasta agregar una nuevamente. |
| `alterTable(self, database: str, tableOld: str, tableNew: str)` | Cambia el nombre de una tabla. |
| `alterAddColumn(self, database: str, table: str, default: any)` | Ingresa un valor por defecto en una nueva columna en cada registro.|
| `alterDropColumn(self, database: str, table: str, columnNumber: int)` | Elimina una columna específica dentro de todos los registros de una tabla.   |
| `dropTable(self, database: str, table: str)` | Elimina un tabla, su contenido y la relación con la base de datos. |

## Valores de Retorno
|Nombre de la función | Retorno | Interpretación |
| ------------ | ------------ | ------------ |
| Database |
| `createDatabase(database: str)` | 0 | Operación exitosa |
| `createDatabase(database: str)` | 1 | Error en la operación |
| `createDatabase(database: str)` | 2 | Base de datos existente |
| `showDatabase()` | list | Proceso exitoso |
| `showDatabase()` | [ ] | Error en la operación |
| `alterDatabase(databaseOld, databaseNew)` | 0 | Operación exitosa |
| `alterDatabase(databaseOld, databaseNew)` | 1 | Error en la operación |
| `alterDatabase(databaseOld, databaseNew)` | 2 | DatabaseOld no existente |
| `alterDatabase(databaseOld, databaseNew)` | 3 | DatabaseNew existente |
| `dropDatabase(database: str)` | 0 | Operación exitosa |
| `dropDatabase(database: str)` | 1 | Error en la operación |
| `dropDatabase(database: str)` | 2 | Base de datos no existente |
| Table |
| `createTable(database: str, table: str, numberColumns: int)` | 0 | Operación exitosa |
| `createTable(database: str, table: str, numberColumns: int)` | 1 | Error en la operación |
| `createTable(database: str, table: str, numberColumns: int)` | 2 | Base de datos inexistente |
| `createTable(database: str, table: str, numberColumns: int)` | 3 | Tabla existente |
| `showTables(database: str)` | list | Proceso exitoso |
| `showTables(database: str)` | [ ] | No hay tablas |
| `showTables(database: str)` | None | Error en la operación |
| `extractTable(database: str, table: str)` | list | Proceso exitoso |
| `extractTable(database: str, table: str)` | [ ] | No hay datos |
| `extractTable(database: str, table: str)` | None | Error en la operación |
| `extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any)` | list | Proceso exitoso |
| `extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any)` | [ ] | No hay datos |
| `extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any)` | None | Error en la operación |
| `alterAddPK(database: str, table: str, columns: list)` | 0 | Operación exitosa |
| `alterAddPK(database: str, table: str, columns: list)` | 1 | Error en la operación |
| `alterAddPK(database: str, table: str, columns: list)` | 2 | Base de datos inexistente |
| `alterAddPK(database: str, table: str, columns: list)` | 3 | Tabla inexistente |
| `alterAddPK(database: str, table: str, columns: list)` | 4 | PK existente |
| `alterAddPK(database: str, table: str, columns: list)` | 5 | Columna fuera de límites |
| `alterDropPK(database: str, table: str)` | 0 | Operación exitosa |
| `alterDropPK(database: str, table: str)` | 1 | Error en la operación |
| `alterDropPK(database: str, table: str)` | 2 | Base de datos inexistente |
| `alterDropPK(database: str, table: str)` | 3 | Tabla inexistente |
| `alterDropPK(database: str, table: str)` | 4 | PK inexistente |
| `alterTable(database: str, tableOld: str, tableNew: str)` | 0 | Operación exitosa |
| `alterTable(database: str, tableOld: str, tableNew: str)` | 1 | Error en la operación |
| `alterTable(database: str, tableOld: str, tableNew: str)` | 2 | Base de datos inexistente |
| `alterTable(database: str, tableOld: str, tableNew: str)` | 3 | TableOld inexistente |
| `alterTable(database: str, tableOld: str, tableNew: str)` | 4 | TableNew existente |
| `alterAddColumn(database: str, table: str, default: any) ` | 0 | Operación exitosa |
| `alterAddColumn(database: str, table: str, default: any) ` | 1 | Error en la operación |
| `alterAddColumn(database: str, table: str, default: any) ` | 2 | Base de datos inexistente |
| `alterAddColumn(database: str, table: str, default: any) ` | 3 | Tabla inexistente |
| `alterDropColumn(database: str, table: str, columnNumber: int)` | 0 | Operación exitosa |
| `alterDropColumn(database: str, table: str, columnNumber: int)` | 1 | Error en la operación |
| `alterDropColumn(database: str, table: str, columnNumber: int)` | 2 | Base de datos inexistente |
| `alterDropColumn(database: str, table: str, columnNumber: int)` | 3 | Tabla inexistente |
| `dropTable(database: str, table: str)` | 0 | Operación exitosa |
| `dropTable(database: str, table: str)` | 1 | Error en la operación |
| `dropTable(database: str, table: str)` | 2 | Base de datos inexistente |
| `dropTable(database: str, table: str)` | 3 | Tabla inexistente |
| Tupla |
| `insert(database: str, table: str, register: list)` | 0 | Operación exitosa |
| `insert(database: str, table: str, register: list)` | 1 | Error en la operación |
| `insert(database: str, table: str, register: list)` | 2 | Base de datos inexistente |
| `insert(database: str, table: str, register: list)` | 3 | Tabla inexistente |
| `insert(database: str, table: str, register: list)` | 4 | PK duplicada |
| `insert(database: str, table: str, register: list)` | 5 | Columna fuera de límites |
| `loadCSV(file: str, database: str, table: str)` | list | Proceso exitoso |
| `loadCSV(file: str, database: str, table: str)` | [ ] | No hay datos |
| `extractRow(database: str, table: str, columns: list)` | list | Proceso exitoso |
| `extractRow(database: str, table: str, columns: list)` | [ ] | No hay datos |
| `update(database: str, table: str, register: dict, columns: list)` | 0 | Operación exitosa |
| `update(database: str, table: str, register: dict, columns: list)` | 1 | Error en la operación |
| `update(database: str, table: str, register: dict, columns: list)` | 2 | Base de datos inexistente |
| `update(database: str, table: str, register: dict, columns: list)` | 3 | Tabla inexistente |
| `update(database: str, table: str, register: dict, columns: list)` | 4 | PK inexistente |
| `delete(database: str, table: str, columns: list)` | 0 | Operación exitosa |
| `delete(database: str, table: str, columns: list)` | 1 | Error en la operación |
| `delete(database: str, table: str, columns: list)` | 2 | Base de datos inexistente |
| `delete(database: str, table: str, columns: list)` | 3 | Tabla inexistente |
| `delete(database: str, table: str, columns: list)` | 4 | PK inexistente |
| `truncate(database: str, table: str)` | 0 | Operación exitosa |
| `truncate(database: str, table: str)` | 1 | Error en la operación |
| `truncate(database: str, table: str)` | 2 | Base de datos inexistente |
| `truncate(database: str, table: str)` | 3 | Tabla inexistente |

## Diagrama de clases
<p align="center">
  <img src="imagenes/Diagramadeclases.png" width="900" alt="Diagrama">
</p>


