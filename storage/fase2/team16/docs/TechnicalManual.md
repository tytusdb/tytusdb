# MANUAL TÉCNICO (FASE 2)

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
En el presente documento se detallan los elementos técnicos detrás de la funcionalidad de Storage Manager, realizado por los 
estudiantes del [grupo 16](https://github.com/tytusdb/tytus/tree/main/storage/fase2/team16) de Estructuras de Datos. Así mismo 
se justifica las decisiones tomadas a lo largo de la elaboración de la fase 2 en busca de una implementación completa y 
robusta sin poner en riesgo la eficiencia que caracteriza a las estructuras de datos, es decir, la utilización apropiada de 
análisis de algoritmos. 

## Objetivos
### General 
Brindar una herramienta robusta y completa que permita la gestión y control de datos a un nivel eficiente y funcional. 
Basada en varias estructuras específicas que minimicen el tiempo de búsqueda, siendo el objetivo principal ser óptima para un 
DataBase Management System (DBMS).
### Específicos
-	Implementar de manera eficiente una estructura de carpetas, para ser utilizado como la base funcional del proyecto con todos los modos de almacenamiento.
-	Brindar un manejo adecuado de los índices dentro de cada estructura de datos que se utillice.
-	Manejar de manera completa la codificación de los elementos dentro de las estructuras de datos con tres codificaciones diferentes a elección del usuario.
-	Generar para el usuario una función para realizar el checksum de una base de datos a través de dos algoritmos seleccionables.
-	Permitir la compresión de datos para la otimización del almacenamiento en el equipo cuando se manejan grandes cantidades de registros.
-	Ofrecer seguridad para las estructuras de datos que se almacenan a través de criptografía, o verificar la fidelidad de los datos a través de blockchain.
-	Mostrar al usuario la estructura interna de las llaves e índices creados a través de gráficas en graphviz.

## Alcances del proyecto
El alcance real del proyecto es muy amplio ya que al ser de tipo 
[open-source](https://github.com/tytusdb/tytus/tree/main/LICENSE.md) permite la implementación de los modos de almacenamiento de distintas maneras. 

Pero en un principio el proyecto está pensado para la gestión y control de datos por medio de varias
estructuras definidas para ser complementado con otros dos módulos desarrollados en paralelo, además de funcionalidades adicionales agregadas. 
Es decir, ser parte de un submódulo funcional dentro un proyecto completo que busca implementar en su totalidad un DataBase Management System (DBMS) 
nombrado Tytus, que en un inicio es desarrollado por estudiantes de la Escuela de Ciencias y Sistemas de la Facultad de 
Ingeniería de la Universidad de San Carlos de Guatemala. 

El submódulo está orientado al manejo de los datos, por lo cual lo esperado es poder manejar correctamente estos. 
Velando principalmente por la eficiencia de procesos y la integridad/seguridad de los datos.

## Descripción de estructura de los modos
Los modos dentro del paquete están distribuidos de tal manera que cada estructura tiene su propio subpaquete, de manera que se pueden importar de manera fácil y rápida, sin embargo, también se deben considerar los submódulos que otorgan funcionalidades adicionales a los modos de almacenamiento previamente mencionados.

Dentro de estas funcionalidade adicionales se pueden encontrar archivos y subpaquetes destinados a cada una de las necesidades de la fase 2 de este proyecto, entre ellos, la codificación, encriptación, graficación, y compresión de datos, entre otras funcionalidades, sin embargo, los modos como tal se pueden encontrar cada uno en un paquete por separado.

Para garantizar la eficiencia de lo procesos, se manejó con la mejor gestión posible los paquetes y subpaquetes para la reutilización de código y de esta manera aumentar la eficiencia tanto en ciclos realizados (la menor cantidad de líneas de código posible), como en espacio de memoria empleado (debido a la reutilización de código realizada).

## Requerimientos funcionales
-	Importar storagemanager o utilizar directamente la interfaz gráfica.
-	Utilizar correctamente los métodos de entrada.
-	Brindar los parámetros requeridos, para evitar que el proceso sea rechazado.
-	Considerar las reglas en los nombres de objetos para que el proceso culmine exitosamente. 
-	Contar con las librerías necesarias para la ejecución del proyecto. Por el momento se utilizan solo [graphviz](https://graphviz.org/download/) y [cryptography](https://pypi.org/project/cryptography/)
-	Conocer el código de retroalimentación que retornarán los procesos.

## Atributos del sistema
-	Todos los datos ingresados serán convertidos a estructuras internas y posteriormente serán guardadas de manera binaria.
-	Todo proceso cuenta con una retroalimentación, la cual indicará el estado del proceso culminado.
-	La interfaz gráfica es otra manera de interactuar con las funcionalidades.
-	Existe una funcionalidad que genera reportes, esta es accesible por medio de la interfaz.
-	La mayor parte de la funcionalidad real es implementada desde 0 por lo cual no debería existir incompatibilidad. 

## Método de trabajo
El proyecto está distribuido en módulos, para optimizar el trabajo en equipo, los módulos son los siguientes:
- Modules
- View
Además de archivos adicionales dentro del mismo directorio.

Toda la metodología está ligeramente inspirada en MVC donde se busca mantener separado cada uno de sus componentes para un mejor orden y control de errores. El proyecto es multiparadigma pero predomina el OOP, representado por cada clase e instancia que se maneja a lo largo de la implementación. 

### [Modules](https://github.com/tytusdb/tytus/tree/main/storage/fase2/team16/storage/Modules)
Módulo que contiene la funcionalidad de guardado a archivo, reportes, y todos los módulos de almacenamiento necesarios.
#### [Handler](https://github.com/tytusdb/tytus/tree/main/storage/fase2/team16/storage/Modules/handler.py)
|Nombre de la función |Descripción|
| ------------ | ------------ |
| `rootinstance()` | Valida la existencia de la raíz y la retorna. |
| `rootupdate(databases)` | Actualiza el archivo raíz, contiene las bases de datos. |
| `writer(name: str, tuples: list)` | Escribe o reescribe un archivo con formato CSV una tabla de datos determinada. |
| `tableinstance(database: str, tableName: str)` | Lee el archivo específico de la tabla y retorna la estructura. |
| `tableupdate(table)` | Actualiza el contenido del archivo de la tabla específica. |
| `exists(database: str, tableName: str)`| Valida la existencia del archivo, es decir, busca y retorna el estado. |
| `delete(filename)` | Elimina el archivo especificado, desaparece el registro. |
| `modeinstance(mode:str)` | verifica que dentro de la carpeta data exista el modo parámetro recibido, si este no existe, lo crea. |
| `rename(oldName, newName)` | Utilizado en función Alter, cambia el nombre de un documento. |
| `findCoincidences(database, tablesName)` | Busca todos los archivos de tablas relacionadas a una base de datos. |
| `readcsv(file)` | Función que retorna un archivo csv leído y cargado a memoria.  |
| `invalid(name: str)` | Invalida un nombre si no cumple las reglas especificadas. |
| `reset()` | Borra la carpeta de datos, permitiendo así hacer pruebas desde 0. |
| `clean(mode: str)` | Elimina el arbol de directorios entero de un modo en específico recibido. |
| `readJSON(database: str, table: str)` | Lee un archivo json de una tabla dentro de una base determinada. |
| `writeJSON(database: str, table: str, blocks: list)` | Escribe un archivo con formato JSON de registros enviados como parámetros. |

#### [Database Module](https://github.com/tytusdb/tytus/tree/main/storage/fase2/team16/storage/Modules/database_module.py)
|Nombre de la función |Descripción|
| ------------ | ------------ |
| `createDatabase(self, database: str, mode: str, encoding: str)` | Crea una base de datos con un modo y codificación concreta y la concatena al archivo raíz. |
| `showDatabases(self)` | Retorna todas las bases de datos existentes. |
| `alterDatabase(self, databaseOld: str, databaseNew: str)` | Cambia el valor de una base da datos, actualiza la raíz y todos los archivos dependientes. |
| `dropDatabase(self, database: str)` | Elimina la base de datos del archivo raíz y todas las tablas relacionadas. |
| `dropAll(self)` | Limpia por completo los datos del proyecto. |

#### [Table Module](https://github.com/tytusdb/tytus/tree/main/storage/fase2/team16/storage/Modules/table_module.py)
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

#### [Tuple Module](https://github.com/tytusdb/tytus/tree/main/storage/fase2/team16/storage/Modules/tuple_module.py)
|Nombre de la función |Descripción|
| ------------ | ------------ |
| `insert(self, database: str, table: str, register: list)` | Ingresa y administra el orden de los nodos dentro de una tabla. |
| `loadCSV(self, file: str, database: str, table: str)` | Carga el archivo y administra el insert masivo. |
| `extractRow(self, database: str, table: str, columns: list)` | Retorna los valores de una tupla específica. |
| `update(self, database: str, table: str, register: dict, columns: list)` | Actualiza el contenido de una tupla, recorriendo y validando por medio del índice. |
| `delete(self, database: str, table: str, columns: list)` | Elimina una tupla por completo. |
| `truncate(self, database: str, table: str)` | Elimina todos los valores dentro de una tabla. |


Además se cuenta con una interfaz gráfica para trabajar con las funciones de manera más dinámica e intuitiva.
#### [Interfaz](https://github.com/tytusdb/tytus/tree/main/storage/fase2/team16/storage/View/interface.py)
|Nombre de la función |Descripción|
| ------------ | ------------ |
| `initComp(self)` | Inicializa la interfaz.|
| `centrar(self)` | Genera el cálculo necesario para mantener siempre centrada la ventana. |
| `ventanaFunciones(self)` | Genera la ventana de funciones. |
| `ventanaReporte(self)` | Genera la ventana de reportes. |
| `main(self)` | Carga todos los elementos de la ventana principal. |
| `funciones(self)` | Carga todos los elementos de la ventana de funcionalidad. |
| `reportes(self)` | Carga todos los elementos de la ventana de reportes |
| `displayDBData(self, event)` | Muestra las bases de datos en el sistema. |
| `displayTableData(self, event)` | Muestra las tablas en el sistema. |
| `displayTupleData(self, event)` | Muestra las tuplas en el sistema. |
| `simpleDialog(self, args, action)` | Genera el popup de ingreso de datos. |
| `cargarArchivo(self, btn)` | Permite la carga de un csv. |
| `ejecutar(self, dialog, args, action)` | Ejecuta todas las funciones del proyecto. |
| `run()` | Corre la interfaz. |

#### [Controller](https://github.com/tytusdb/tytus/tree/main/storage/fase2/team16/storage/View/controller.py)
Contiene la conexión entre la interfaz y el AVLMode.

|Nombre de la función |Descripción|
| ------------ | ------------ |
| `execute(self, args, action)` | Ejecuta la instrucción indicada.|
| `reportDB()` | Genera el reporte de bases de datos. |
| `reportTBL(database: str)` | Genera el reporte de tablas. |
| `reportAVL(database: str, table: str)` | Genera el reporte de AVL. |
| `reportTPL(database: str, table: str, llave)` | Genera el reporte de tupla. |
| `getIndexes(database: str, table: str)` | Devuelve los índices de un AVL. |
 > `Controller` Básicamente es un puente entra la interfaz gráfica y la funcionalidad de los módulos. 
 

## Valores de retorno para cada uno de los modelos

|Nombre de la función | Retorno | Interpretación |
| ------------ | ------------ | ------------ |
| Database |
| `createDatabase(database: str, mode: str, encoding: str)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos existente |
| | 3 | Modo incorrecto |
| | 4 | Codificación incorrecta |
| `showDatabase()` | list | Proceso exitoso |
| | [ ] | Error en la operación |
| `alterDatabase(databaseOld, databaseNew)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | DatabaseOld no existente |
| | 3 | DatabaseNew existente |
| `dropDatabase(database: str)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos no existente |
| Table |
| `createTable(database: str, table: str, numberColumns: int)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos inexistente |
| | 3 | Tabla existente |
| `showTables(database: str)` | list | Proceso exitoso |
| | [ ] | No hay tablas |
| | None | Error en la operación |
| `extractTable(database: str, table: str)` | list | Proceso exitoso |
| | [ ] | No hay datos |
| | None | Error en la operación |
| `extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any)` | list | Proceso exitoso |
| | [ ] | No hay datos |
| | None | Error en la operación |
| `alterAddPK(database: str, table: str, columns: list)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos inexistente |
| | 3 | Tabla inexistente |
| | 4 | PK existente |
| | 5 | Columna fuera de límites |
| `alterDropPK(database: str, table: str)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos inexistente |
| | 3 | Tabla inexistente |
| | 4 | PK inexistente |
| `alterTable(database: str, tableOld: str, tableNew: str)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos inexistente |
| | 3 | TableOld inexistente |
| | 4 | TableNew existente |
| `alterAddColumn(database: str, table: str, default: any) ` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos inexistente |
| | 3 | Tabla inexistente |
| `alterDropColumn(database: str, table: str, columnNumber: int)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos inexistente |
| | 3 | Tabla inexistente |
| `dropTable(database: str, table: str)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos inexistente |
| | 3 | Tabla inexistente |
| Tupla |
| `insert(database: str, table: str, register: list)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos inexistente |
| | 3 | Tabla inexistente |
| | 4 | PK duplicada |
| | 5 | Columna fuera de límites |
| `loadCSV(file: str, database: str, table: str)` | list | Proceso exitoso |
| | [ ] | No hay datos |
| `extractRow(database: str, table: str, columns: list)` | list | Proceso exitoso |
| | [ ] | No hay datos |
| `update(database: str, table: str, register: dict, columns: list)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos inexistente |
| | 3 | Tabla inexistente |
| | 4 | PK inexistente |
| `delete(database: str, table: str, columns: list)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos inexistente |
| | 3 | Tabla inexistente |
| | 4 | PK inexistente |
| `truncate(database: str, table: str)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos inexistente |
| | 3 | Tabla inexistente |


## Valores de retorno para las funcionalidades adicionales
Como complemento a las funcionalidades de todos los modos mencionadas anteriormente, se tienen diferentes funciones complementarias las cuales
ayudan a la correcta gestión, codificación, integridad y seguridad de los datos para ello se dividieron en los módulos siguientes.

|Nombre de la función | Retorno | Interpretación |
| ------------ | ------------ | ------------ |
| Modos |
| `alterTableMode(database: str, table: str, mode: str)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos existente |
| | 3 | Tabla no existente |
| | 4 | Modo incorrecto |
| Índices |
| `alterTableAddFK(database: str, table: str, indexName: str, columns: list,  tableRef: str, columnsRef: list)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos existente |
| | 3 | Tabla o referencia inexistente |
| | 4 | Cantidad entre columnas o referencias inexacta |
| | 5 | Incumplimiento de integridad referencial |
| `alterTableDropFK(database: str, table: str, indexName: str)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos existente |
| | 3 | Tabla inexistente |
| | 4 | Nombre del índice inexistente |
| `alterTableAddUnique(database: str, table: str, indexName: str, columns: list)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos no existente |
| | 3 | Tabla o referencia inexistente |
| | 4 | Cantidad entre columnas o referencias inexacta |
| | 5 | Incumplimiento de integridad de unicidad |
| `alterTableDropUnique(database: str, table: str, indexName: str)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos existente |
| | 3 | Tabla inexistente |
| | 4 | Nombre del índice inexistente |
| `alterTableAddIndex(database: str, table: str, indexName: str, columns: list)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos no existente |
| | 3 | Tabla o referencia inexistente |
| | 4 | Cantidad entre columnas o referencias inexacta |
| `alterTableDropIndex(database: str, table: str, indexName: str)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos existente |
| | 3 | Tabla inexistente |
| | 4 | Nombre del índice inexistente |
| Codificación |
| `alterDatabaseEncoding(database: str, encoding: str)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos existente |
| | 3 | Codificación inexistente |
| CheckSum |
| `checksumDatabase(database: str, mode: str)` | string | Cadena de retorno |
| | None | Error en la operación |
| `checksumTable(database: str, table:str, mode: str)` | string | Cadena de retorno |
| | None | Error en la operación |
| Compresión |
| `alterDatabaseCompress(database: str, level: int)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos existente |
| | 4 | Nivel incorrecto |
| `alterDatabaseDecompress(database: str)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos existente |
| | 4 | Compresión inexistente |
| `alterTableCompress(database: str, table: str, level: int)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos existente |
| | 4 | Nivel incorrecto |
| `alterTableDecompress(database: str, table: str)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos existente |
| | 4 | Compresión inexistente |
| Seguridad |
| `encrypt(backup: str, password: str)` | string | Criptograma resultante |
| | None | Error en la operación |
| `decrypt(cipherBackup: str, password: str)` | string | Texto plano resultante |
| | None | Error en la operación |
| `safeModeOn(database: str, table: str)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos inhexistente |
| | 3 | Tabla inexistente |
| | 4 | Modo seguro existente |
| `safeModeOff(database: str, table: str)` | 0 | Operación exitosa |
| | 1 | Error en la operación |
| | 2 | Base de datos inhexistente |
| | 3 | Tabla inexistente |
| | 4 | Modo seguro no existente |
| Grafos |
| `graphDSD(database: str)` | str | Grafo en formato graphviz |
| | None | Error en la operación |
| `graphDF(database: str, table: str)` | str | Grafo en formato graphviz |
| | None | Error en la operación |


## Recursos externos
- [csv](https://docs.python.org/3/library/csv.html)
- [graphviz](https://graphviz.org/download/)
- [cryptography](https://pypi.org/project/cryptography/)
- [PIL](https://pypi.org/project/Pillow/)
- [pickle](https://docs.python.org/3/library/pickle.html)
- [re](https://docs.python.org/3/library/re.html)
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [shutil](https://docs.python.org/3/library/shutil.html)
> `graphviz` y `cryptography` Únicas librerías externas, con licencias autorizadas.

## Diagrama de clases 
 El siguente diagrama es un diagrama de clases de uno de los módulos implementados en el almacenamiento

<div align="center" alt="Diagrama">
  <img src="img/class.png" />
</div>








