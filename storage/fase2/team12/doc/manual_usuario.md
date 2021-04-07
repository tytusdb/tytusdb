### Tytus

Es un proyecto Open Source para desarrollar un administrador de bases de datos, el administrador de almacenamiento de la base de datos. El proyecto se dividió en dos fases, la primera dedicada a programar los distintos modos que poodrían ser utilizados, y la segunda en la que se unifican los modos creados en la primera fase del proyecto, en conjunto podremos manejar cualquier tipo de estructura de datos para cada base de datos específica.

La facilidad más importante para este tipo de manejo de las estructuras de datos, que es la de definirle una estructura de datos a un tipo de información en específico, es la de que sea mejor para el procesador dividir la información de una forma u otra.

### Estructuras de datos disponibles
* Árbol AVL
* Árbol B
* Árbol B+
* Tablas Hash
* Isam
* Json
* Diccionarios

### Reportes
Mediante el uso de imagenes generadas por graphviz podrá generar reportes específicos de una base de datos o de una tabla, mismos que le mostraran el tipo de relaciones que existen entre todas las tablas que posea una base de datos o bien toda la información de una única tabla.
### Funcionalidades elementales
* La serialización de los metadatos permite que se guarde y se pueda recuperar toda la información de cada base de datos y la información de las tablas.
* La compresión y des compresión de información permite que ciertas estructuras de datos mantengan su información de manera binaria con el fin de reducir el tamaño que produce a la memoria.
* La persistencia de la información permite que todos los registros que se hagan se almacenen en archivos externos para su uso posterior.
* La carga masiva de información permite que se pueda ingresar al sistema archivos externos de manera que se pueda cargar muchos registros de manera rápida y eficiente.

### Requerimientos del sistema
* Python 3.5 o superior.
* Instalar las librerías graphviz.
* Instalar las librerías cryptography.
* Instalar las librerías chardet.
* Conntar con los archivos de los modos de almacenamiento.