# Manual de Usuario **ISAM Mode**

## Índice
- [Descripción General del Programa](#Descripción-General-del-Programa)
- [Requerimientos del Sistema](#Requerimientos-del-Sistema)
- [Glosario](Glosario)
- [Opciones de Bases de Datos](#Opciones-de-Bases-de-Datos)
- [Opciones de Tablas](#Opciones-de-Tablas)
- [Opciones de Tuplas](#Opciones-de-Tuplas)

## Requerimientos del Sistema
- Python 2.7, 3.5 o superior.
- Microsoft Windows XP o superior de 64 bits.
- Instalar graphviz
- contar con el paquete ISAMMode.py

## Descripción General del Programa

Este Programa consiste en una interfaz gráfica que permite la interacción del usuario con las funciones contenidas en el paquete [ISAMMode.py](storage/team14/ISAMMode.py). Este permite que el usuario desarrolle las funciones CRUD de una base de datos, que están en el archivo anteriormente mencionado, de forma gráfica.

## Glosario
1. Base de Datos: Una base de datos es un conjunto de datos pertenecientes a un mismo contexto y almacenados sistemáticamente para su posterior uso.

2. CSV: tipo de documento en formato abierto sencillo para representar datos en forma de tabla, en las que las columnas se separan por comas y las filas por saltos de línea.

3. Tabla: tipo de modelado de datos donde se guardan los datos recogidos por un programa.

4. Cuadro de diálogo: es un tipo de ventana que permite comunicación simple entre el usuario y el sistema informático.

5. Tupla: representa un objeto único de datos implícitamente estructurados en una tabla.

6. Llave Primaria: es un campo o a una combinación de campos que identifica de forma única a cada fila de una tabla. Una clave primaria comprende de esta manera una columna o conjunto de columnas.

7. Graphviz: campo o a una combinación de campos que identifica de forma única a cada fila de una tabla. Una clave primaria comprende de esta manera una columna o conjunto de columnas.



## Opciones de Bases de Datos

<p align="center"><img src="img/bases_de_datos.png" width="800" alt="Opciones de bases de Datos"></p>

1. Lista de Bases de Datos disponibles: al iniciar el programa, las bases de datos que ya se encuentren creadas se desplegarán en este panel. Así mismo si se crean o se eliminan bases de datos, estás se irán agregando o desapareciendo del panel.

2. Crear Base de Datos: este botón permite crear una base de datos y la agrega al panel Lista de Bases de Datos disponibles. Para esto se debe ingresar el nombre de la base de datos a crear. Mediante un cuadro de diálogo.

3. Eliminar Base de Datos: con este botón se puede eliminar cualquiera de las bases de datos que se muestran en el panel Lista de Bases de Datos disponibles. Para eliminar una de las bases de datos, se debe seleccionar en la lista dando click sobre ella y posteriormente dar click en el botón Eliminar Base de Datos, esto desplegará un cuadro de dialogo en el que se pregunta si deseamos eliminar la base de datos.

4. Editar nombre de BD: este botón sirve para cambiar el nombre de cualquiera de las bases de datos que se encuentran creadas. Para editar el nombre una de las bases de datos, se debe seleccionar en la lista dando click sobre ella y posteriormente dar click en el botón Editar nombre de BD, esto desplegará un cuadro de dialogo en el que se pide ingresar el nuevo nombre de la Base de datos.

5. Ver Tablas: esta opción sirve para ver las tablas que pertenecen a una base de datos en particular. Para ver las tablas de una base de datos, se debe seleccionar en la lista dando click sobre ella y posteriormente dar click en el botón Ver Tablas.



## Opciones de Tablas


<p align="center"><img src="img/tablas.png" width="800" alt="Opciones de bases de Datos"></p>


6. Lista de tablas almacenadas: Al acceder a la ventana de tablas, se podrá visualizar todas las tablas que se encuentran disponibles dentro de la base de datos elegida con anterioridad.

7. Crear Tabla de Datos: Si se desea agregar una nueva tabla, se presiona el botón y mediante un cuadro de texto se debe ingresar el nombre que se desea que lleve, posteriormente aparecerá en la nueva tabla en el listado.

8. Borrar Tabla: Si se desea eliminar una tabla, solamente es necesario seleccionarla en el listado y presionar el botón, al hacerlo la tabla se eliminará tanto del listado como del registro.

9. Cambiar nombre: Si se desea editar el nombre de una tabla, se selecciona la tabla a la cual se desea renombrar, y presionar el botón, se solicitará el nuevo nombre mediante un cuadro de diálogo, se actualizará el nombre de la tabla dentro del listado y dentro del registro.

10. Agregar Columna:  Si se desea que una tabla posea una nueva columna, se presiona el botón, se mostrará un cuadro de diálogo donde se deberá ingresar el valor por default que se desea que lleve la nueva columna en todos los registros

11. Eliminar Columna:  Si se desea eliminar una columna, se presiona el botón, posteriormente se solicitará el número de la columna que se desea eliminar, se verificará que la columna seleccionada no forme parte de la primary key, si no forma parte se eliminará la columna, en caso contrario no se podrá eliminar la columna.

12. Agregar PK: Si se desea vincular una PK a la tabla, se presiona el botón, se solicitará un listado, donde se deberá ingresar el número de columnas que se desean convertir en la nueva PK. Se podrá vincular una PK si y solo si no existe una primary key ya vinculada.

13. Eliminar PK:  Si se desea eliminar la PK vinculada a la tabla, se debe seleccionar la tabla a la cual se desea eliminar la PK y se presiona el botón, se verificará que la tabla posea PK.

14. Ver Tabla: Si se desea visualizar todos los registros dentro de una tabla en específico, se debe seleccionar la tabla de la cual se desean ver los registros y presionar el botón, posteriormente se mostrará una nueva ventana donde se visualizará las opciones que se pueden ejecutar con los registros junto con los registros ya ingresados.

15. Graficar:  Si se desea visualizar todos los registros gráficamente dentro de la estructura almacenados, se debe seleccionar la tabla de la cual se desea graficar, se podrá visualizar una nueva ventana con la imagen gráfica de todos los registros.

16. Regresar: Si se desea regresar a la ventana anterior solamente es necesario presionar el botón para poder visualizar nuevamente la ventana con las bases de datos.



## Opciones de Tuplas


<p align="center"><img src="img/tuplas.png" width="800" alt="Opciones de bases de Datos"></p>


17. Tuplas de la Tabla: en este panel se encuentran listadas todas las tuplas pertenecientes a la tabla que se seleccionó anteriormente.

18. Extraer Tabla completa: esta opción muestra todas las tuplas pertenecientes a la tabla seleccionada anteriormente en el panel de Tuplas de la Tabla.

19. Extraer por Rangos: esta opción permite al usuario extraer tuplas que se encuentren en un rango específico. Para esto se solicita el valor y número de columna que se desea evaluar mediante un cuadro de texto.

20. Extraer Row: mediante esta opción es posible traer al panel una sola tupla, llamándola mediante su llave primaria. Para esto se debe presionar este botón lo que desplegará un cuadro de diálogo que solicita la llave o lista de llaves primarias.

21. Insertar Registro: esta opción permite ingresar una nueva tupla a la tabla. Para esto se debe presionar este botón lo que desplegará un cuadro de diálogo que solicita la lista de elementos que conforman la tupla.

22. Actualizar Registro: este botón sirve para hacer cambios a la información dentro de una tupla en específico. Para esto se debe presionar este botón lo que desplegará un cuadro de diálogo que solicita la lista de elementos que se desean cambiar con un formato de tipo llave1:valor1,llave2valor2… y posteriormente en otro cuadro de diálogo se solicita la llave o listas de llaves primarias de la tupla que se quiere actualizar.

23. Eliminar Registro: esta opción permite eliminar una tupla específica, indicando su llave primaria en un cuadro de diálogo.

24. Eliminar Todo: esta opción permite eliminar todas las tuplas correspondientes a una base de datos.

25. Cargar CSV: esta opción permite la carga masiva de tuplas mediante un archivo CSV.

26. Regresar: permite volver a la pantalla de opciones de Tablas.
