# Manual de Usuario **Storage**

## Índice
- [Descripción General del Programa](#Descripción-General-del-Programa)
- [Requerimientos del Sistema](#Requerimientos-del-Sistema)
- [Glosario](Glosario)
- [Opciones de Bases de Datos](#Opciones-de-Bases-de-Datos)
- [Opciones de Tablas](#Opciones-de-Tablas)
- [Pantalla de Reporte gráfico](#Pantalla-de-Reporte-gráfico)

## Requerimientos del Sistema
- Python 2.7, 3.5 o superior.
- Microsoft Windows XP o superior de 64 bits.
- Instalar graphviz
- Instalar Cryptography
- contar con el paquete Storage.py

## Descripción General del Programa

Este Programa consiste en una interfaz gráfica que permite la interacción del usuario con las funciones contenidas en el paquete [storage.py](storage/fase2/team14/storage/storage.py). Este permite que el usuario visualice gráficamente el almacenamiento de las bases de datos entre otras funciones, que están en el archivo anteriormente mencionado.

## Glosario
1. Base de Datos: Una base de datos es un conjunto de datos pertenecientes a un mismo contexto y almacenados sistemáticamente para su posterior uso.

2. CSV: tipo de documento en formato abierto sencillo para representar datos en forma de tabla, en las que las columnas se separan por comas y las filas por saltos de línea.

3. Tabla: tipo de modelado de datos donde se guardan los datos recogidos por un programa.

4. Cuadro de diálogo: es un tipo de ventana que permite comunicación simple entre el usuario y el sistema informático.

5. Tupla: representa un objeto único de datos implícitamente estructurados en una tabla.

6. Llave Primaria: es un campo o a una combinación de campos que identifica de forma única a cada fila de una tabla. Una clave primaria comprende de esta manera una columna o conjunto de columnas.

7. Graphviz: campo o a una combinación de campos que identifica de forma única a cada fila de una tabla. Una clave primaria comprende de esta manera una columna o conjunto de columnas.



## Opciones de Bases de Datos

<p align="center"><img src="/storage/fase2/team14/img/bases.png" width="800" alt="Opciones de bases de Datos"></p>

1. Lista de Bases de Datos disponibles: al iniciar el programa, las bases de datos que ya se encuentren creadas se desplegarán en este panel.

2. Ver Tablas: esta opción sirve para ver las tablas que pertenecen a una base de datos en particular. Para ver las tablas de una base de datos, se debe seleccionar en la lista dando click sobre ella y posteriormente dar click en el botón Ver Tablas.

3. Graficar DSD: esta opción permite visualizar un diagrama de dependencias de la base de datos seleccionada.


## Opciones de Tablas


<p align="center"><img src="/storage/fase2/team14/img/tablas.png" width="800" alt="Opciones de bases de Datos"></p>


4. Lista de tablas almacenadas: Al acceder a la ventana de tablas, se podrá visualizar todas las tablas que se encuentran disponibles dentro de la base de datos elegida con anterioridad.

5. Ver Tabla: Si se desea visualizar todos los registros dentro de una tabla en específico, se debe seleccionar la tabla de la cual se desean ver los registros y presionar el botón, posteriormente se mostrará una nueva ventana donde se visualizará las opciones que se pueden ejecutar con los registros junto con los registros ya ingresados.

6. Graficar:  Si se desea visualizar todos los registros gráficamente dentro de la estructura almacenados, se debe seleccionar la tabla de la cual se desea graficar, se podrá visualizar una nueva ventana con la imagen gráfica de todos los registros.

7. Ver Blockchain: Esta opción despliega un grafico de una cadena de bloques si la tabla seleccionada tiene activo el modo seguro, si esta no la tiene activo se muestra una imagen que lo especifica.

8. Graficar DF: esta opción permite visualizar un diagrama de dependencias de la tabla seleccionada.

9. Regresar: Si se desea regresar a la ventana anterior solamente es necesario presionar el botón para poder visualizar nuevamente la ventana con las bases de datos.



## Pantalla de Reporte gráfico


<p align="center"><img src="/storage/fase2/team14/img/grafico.png" width="800" alt="Opciones de bases de Datos"></p>


10. Salir: Si se desea regresar a la ventana anterior solamente es necesario presionar el botón para poder visualizar nuevamente la ventana con las bases de datos.

11. Gráfico: en este apartado se presenta un grafico segun la opción seleccionada en la ventana anterior.
