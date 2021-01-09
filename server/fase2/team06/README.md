# BD1 Diciembre 2020 Project1 TytusDB

## [](https://github.com/tytusdb/tytus/tree/main/server/team06#grupo-6)Grupo 6

#### [](https://github.com/tytusdb/tytus/tree/main/server/team06#201603198-cristian-estuardo-herrera-poncio)201603198 Cristian Estuardo Herrera Poncio

#### [](https://github.com/tytusdb/tytus/tree/main/server/team06#201612120-jackelin-sofia-montenegro-chamale)201612120 Jeackelin Sofia Montenegro Chamale

#### [](https://github.com/tytusdb/tytus/tree/main/server/team06#201612185-byron-antonio-alvarez-morales)201612185 Byron Antonio Alvarez Morales

#### [](https://github.com/tytusdb/tytus/tree/main/server/team06#201612190-marcos-sebastian-velasquez-cabrera)201612190 Marcos Sebastian Velasquez Cabrera

# [](https://github.com/tytusdb/tytus/tree/main/server/team06#tytusdb-manual-tecnico)  TytusDB Manual tecnico

## TytusDB

Es un proyecto Open Source para desarrollar un administrador de bases de datos. Está compuesto por tres componentes interrelacionados: el administrador de almacenamiento de la base de datos, el administrador de la base de datos, este administrador se compone a su vez de un servidor y de un cliente; y el SQL Parser.

![image](https://github.com/tytusdb/tytus/blob/main/client/fase2/team06/img/interfaz.png?raw=true)

## [](https://github.com/tytusdb/tytus/tree/main/server/team06#sistema-operativo-windows)Sistema operativo: Windows

## [](https://github.com/tytusdb/tytus/tree/main/server/team06#librerias)Librerias

### [](https://github.com/tytusdb/tytus/tree/main/server/team06#boostrap) ![image](https://github.com/tytusdb/tytus/blob/main/server/fase2/team06/img/bop.png?raw=true =50x) Boostrap    


Bootstrap es una biblioteca multiplataforma o conjunto de herramientas de código abierto para diseño de sitios y aplicaciones web. Se utilizó esta herramienta para realizar la interfaz gráfica de la aplicación.

### [](https://github.com/tytusdb/tytus/tree/main/server/team06#jquery) ![image](https://github.com/tytusdb/tytus/blob/main/server/fase2/team06/img/js.png?raw=true =50x) JQuery

jQuery es una biblioteca multiplataforma de JavaScript, que permite simplificar la manera de interactuar con los documentos HTML.

### [](https://github.com/tytusdb/tytus/tree/main/server/team06#jstree) ![image](https://github.com/tytusdb/tytus/blob/main/server/fase2/team06/img/jstre.png?raw=true =50x)  JStree

Sirve para desplegar estructuras de árbol totalmente personalizables, configurables e interactivas. Esta libreria se utilizó para agrupar el apartado del navegador bases de datos en la interfaz gráfica.

### [](https://github.com/tytusdb/tytus/tree/main/server/team06#jstree) ![image](https://github.com/tytusdb/tytus/blob/main/server/fase2/team06/img/toast.png?raw=true =50x)  Toastr

Toastr es una libreria javascript para mostrar notificaciones web visuales, interactivas y con muchas opciones. Es posible descargar el la libreria toastr desde el sitio web oficial

## Funciones Servidor
```
def  analize(texto):
```
Analiza las instrucciones escritas dentro del query seleccionado.
Parámetro texto: Es el texto a analizar.
Dentro del metodo se hace una llamada a la libreria G26, la cual devuelve la salida del query, ya sea un error, una tabla como solución a una instrucción Select o un estado en consola.

```
def  PYejecutarScript():
```
Recibe el contenido del script seleccionado y lo guarda en la variable x para luego ser analizada.

```
def  PYAbrirArchivo(x):
```
Abre un query o archivo SQL.
Parámetro x: Es el contenido del archivo.
Dentro del metodo se envia el contenido del archivo hacia uno de los querys para su uso.

```
def  PYguardarArchivo(x,y):
```
Abre un query o archivo SQL.
Parámetro x: Es la ruta del archivo.
Parámetro y: Es el contenido del archivo.
Dentro del metodo se recibe el contenido y la ruta del archivo para guardarlo o sobre escribirse, según sea el caso.

```
def  PYcrearBD():
```
Crear base de datos.
Dentro del metodo se genera una nueva base de datos la cual ejecuta automaticamente la sentencia para crearla en SQL y para agregarla al árbol de búsqueda.

```
def  PYcrearTabla():
```
Crear tabla.
Dentro del metodo se genera una nueva tabla dentro de la base de datos seleccionada la cual ejecuta automaticamente la sentencia para crearla en SQL y para agregarla al árbol de búsqueda.

## Funciones Cliente

```
function  resfreshJSTree()
```
Refresca el árbol de búsqueda.
Agrega la base de datos o tabla dentro del árbol de búsqueda.

```
function  customMenu(node)
```
Menu de árbol de búsqueda.
Al dar click derecho sobre una base de datos esta desplegara su menu para agregar tablas o bases de datos.

```
function  saveTextAsFile()
```
Guardar archivo.
Guarda el contenido del query seleccionado en un archivo .sql, a su vez muestra en consola la acción a realizar.

```
function  ejecutarScript()
```
Ejecutar script.
Selecciona el contenido del query seleccionado lo guarda en una variable y lo envia hacia el servidor para su análisis, a su vez muestra en consola la acción a realizar.

```
function  guardarArchivo()
```
Guardar archivo.
Selecciona el contenido del query seleccionado lo guarda en un archivo .sql

```
function  analize()
```
Analizar script.
Envia hacia el servidor las instrucciones a analizar.

Diciembre 2020
