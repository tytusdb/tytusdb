# Proyecto (FASE I)

### Descripcion del Programa

TytusDB es un proyecto Open Source para desarrollar un administrador de bases de datos, el administrador encargado de gestionar el almacenamiento de las bases de datos, este administrador se divide en 3 módulos que se describirán más adelante los cuales son:
- Módulo de las Bases de Datos
- Módulo de Tablas
- Módulo de Tuplas

### Módulo de bases de datos

##### Arranque del programa

Al momento de iniciar la aplicación se le mostrara la siguiente ventana, dicha ventana le permitara interactuar con el modulo de las base de datos

<p align="center">
  <img src="img/img1.png" width="700" alt="img1">
</p>

##### Creación de una Base de datos

1.	Deberá ingresar en el campo que se muestra a continuacion un nombre para su base de dato dicho nombre no debe repetirse, posterior a ello debera dar click en el botón Guardar

<p align="center">
  <img src="img/img2.png" width="700" alt="img1">
</p>

2.	Si el nombre ingresado no estaba siendo utilizado se le notificará que se agregó existosamente

<p align="center">
  <img src="img/img3.png" width="700" alt="img1">
</p>

##### Ver bases de datos existentes

1.	Deberá dar click en el botón Show Database y a continuación se le mostrarán todas las bases de datos registradas

<p align="center">
  <img src="img/img4.png" width="700" alt="img1">
</p>

##### Editar nombre de las bases de datos

1.	Deberá dar click en el botón en Alter Database , y se le mostrará la siguiente ventana

<p align="center">
  <img src="img/img5.png" width="700" alt="img1">
</p>

2.	Deberá ingresar en el primer campo el nombre de la base de datos a la cual desea realizar el cambio, en el segundo campo deberá ingresar el nuevo nombre que se quisiera tener

3.	Podrá dirigirse a la pestaña Show Data base para observar claramente el cambio solicitado

<p align="center">
  <img src="img/img6.png" width="700" alt="img1">
</p>

##### Eliminar un base de datos

1.	Deberá dar click en el botón en Drop database , y se le mostrará la siguiente ventana

<p align="center">
  <img src="img/img7.png" width="700" alt="img1">
</p>

2.	Deberá ingresar en el campo el nombre de la base de datos que desea eliminar

3.	Podrá dirigirse a la pestaña Show Data base para observar claramente que se ha eliminado la base de datos

<p align="center">
  <img src="img/img8.png" width="700" alt="img1">
</p>

### Módulo Tablas

##### Creación de una tabla

1. Deberá ingresar en el campo que se muestra a continuacion un nombre para su tabla dicho nombre no debe repetirse, posterior a ello debera dar click en el botón Guardar

<p align="center">
  <img src="img/img9.png" width="700" alt="img1">
</p>

##### Mostrar tablas existentes

1.	Deberá dar click en el botón Show Table y a continuación se le mostrarán todas las tablas registradas

<p align="center">
  <img src="img/img10.png" width="700" alt="img1">
</p>

##### Editar nombre de una tabla

1. Deberá dar click en el botón en Alter Table , y se le mostrará la siguiente ventana

<p align="center">
  <img src="img/img11.png" width="700" alt="img1">
</p>

2.	Deberá ingresar en el primer campo el nombre de la tabla a la cual desea realizar el cambio, en el segundo campo deberá ingresar el nuevo nombre que se quisiera tener

3.	Podrá dirigirse a la pestaña Show Table para observar claramente el cambio solicitado

<p align="center">
  <img src="img/img12.png" width="700" alt="img1">
</p>

##### Eliminar una tabla existente

1.	Deberá dar click en el botón en Drop Table , y se le mostrará la siguiente ventana

<p align="center">
  <img src="img/img13.png" width="700" alt="img1">
</p>

2.	Deberá ingresar en el campo el nombre de la tabla que desea eliminar

3.	Podrá dirigirse a la pestaña Show Table para observar claramente que se ha eliminado la tabla

<p align="center">
  <img src="img/img14.png" width="700" alt="img1">
</p>

##### Agregar llave primaria

1.	Deberá dar click en el botón en Alter add pk, y se le mostrará la siguiente ventana

<p align="center">
  <img src="img/img15.png" width="700" alt="img1">
</p>

2.	En el primer campo deberá ingresar el nombre de la tabla a la cual desea agregar la pk, en el segundo campo el numero de columna que tendrá la pk

##### Alter add columna

1.	Deberá dar click en el botón en Alter add columna, y se le mostrará la siguiente ventana

<p align="center">
  <img src="img/img16.png" width="700" alt="img1">
</p>

2.	En el primer campo deberá ingresar el nombre de la tabla a la cual desea agregar las columnas, en el segundo campo el número de columnas que se le agregaran a la tabla

##### Alter drop columna

1.	Deberá dar click en el botón en Alter drop columna, y se le mostrará la siguiente ventana

<p align="center">
  <img src="img/img17.png" width="700" alt="img1">
</p>

2.	En el primer campo deberá ingresar el nombre de la tabla a la cual desea eliminar la columna, en el segundo campo el número de columna que se desea eliminar

##### Eliminar pk

1.	Deberá dar click en el botón en Alter drop pk, y se le mostrará la siguiente ventana

<p align="center">
  <img src="img/img18.png" width="700" alt="img1">
</p>

2.	En el primer campo deberá ingresar el nombre de la tabla a la cual desea eliminar la pk, en el segundo campo el número de columna tiene la pk

### Módulo Tuplas

<p align="center">
  <img src="img/img19.PNG" width="700" alt="img1">
</p>

##### Insert

Deberá ingresar en el campo que se muestra a continuacion.

<p align="center">
  <img src="img/img20.PNG" width="700" alt="img1">
</p>

##### Load CSV

Este nos permite cargar archivos excel para cargar la base con datos

##### Extract Row
Extrae y devuelve un registro especificado por su llave primaria, es por esto que se debe de ingresar el campo que se solicita
<p align="center">
  <img src="img/img21.PNG" width="700" alt="img1">
</p>

##### Update
Inserta un registro en la estructura de datos asociada a la tabla y la base de datos, para esto es que se solicita dos campos, el register y el columnas.
<p align="center">
  <img src="img/img22.PNG" width="700" alt="img1">
</p>

##### Delete
Elimina un registro de una tabla y base de datos especificados por la llave primaria, es por esto que se solicita la llave primaria
<p align="center">
  <img src="img/img23.PNG" width="700" alt="img1">
</p>

##### Truncate
Elimina todos los registros de una tabla y base de datos, solamente debe de presionarse el boton Truncate en la interfaz del frmTabla
