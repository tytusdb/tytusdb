# PROYECTO DE CLASE BASES DE DATOS.

El proyecto de clase consiste en utilizar el proyecto de [Tytus](https://github.com/tytusdb/tytus) y recolectar cada parte para unirlas y crear un DBMS lo más funcional posible.

### Participantes:
200113057   -   Mario Augusto Pineda Morales
200413657   -   Juan Pablo Renato Montúfar Chávez
201314826   -   Rafael Angel Chocoj Xinico
201700857   -   Daniel Arturo Alfaro Gaitan
201731087   -   Jose Fernando Guerra Muñoz

## Partes del DBMS.
El programa está dividido en 2 partes un cliente y servidor. El cliente es el que el usuario final utilizará directamente, este hace uso de angular para trabajar en el navegador.
El lado del cliente no tiene más que la parte visual e interactuable del proyecto, las partes funcionales están en el servidor.

El servidor está constituido por 3 partes:
* Proveedor de los microservicios y que funciona como el enlace para las otras partes que lo llamaremos SERVER.
* Analizador lexico, sintactico, semántico y el que proporciona la posibilidad de la ejecución de las instrucciones. Lo llamaremos ANALIZADOR.
* Estructura Árbol AVL, donde se almacenarán las bases de datos, tablas y tuplas que el usuario vaya creando. Lo llamaremos AVL MODE.

### Server.
Esta parte está hecha para poder comunicarse con el cliente y poder hacer de enlace central para el avl mode y el analizador. Esta parte del proyecto se obtuvo del trabajo realizado por el curso de bases en vacaciones de diciembre 2020. El [Grupo 5](https://github.com/tytusdb/tytus/tree/main/server/fase2/team05) es el responsable de la creación de esta parte al igual que la parte del [cliente](https://github.com/tytusdb/tytus/tree/main/client/fase2/team05)
Esta parte se puede decir que no cuenta con deficiencias, ya que funciona bastante bien como enlace entre el cliente y los servicios de analisis y creación o modificación de bases de datos en la estructura AVL.

### Analizador.
El analizador es la parte que se encarga de recibir y analizar léxica, sintáctica y semánticamente las instrucciones o comandos enviados desde el área de edición de texto del cliente. En el caso de que se encuentren errores léxicos, sintácticos o semánticos, este manda respuesta al server que mande respuesta al cliente que encontró una falla, para que sea corregida y pueda proceder a la ejecución.
El analizador fue hecho por el [grupo 29](https://github.com/tytusdb/tytus/tree/main/parser/team29) del curso de compiladores en el curso de vacaciones de diciembre de 2020.
Si el analizador da visto bueno a los comandos enviados desde el cliente, procede a la ejecución haciendo uso del avl mode. Donde se crearán o se modificarán las bases de datos, tablas o tuplas.

### AVL Mode.
El avl mode, es el nombre con el que se le conoce a las acciones programadas para un arbol AVL. Este árbol avl está encargado de almacenar toda la información que el usuario solicite crear o modificar. Esta estructura fue creada por el [grupo 16](https://github.com/tytusdb/tytus/tree/main/storage/team16) del curso de Estructuras de Datos en el periódo de vacaciones de diciembre de 2020.

#### Partes funcionales y no funcionales.
Las partes funcionales, son aquellas ordenes que funcionan de manera normal y sin problema alguno. Son las siguientes:
* Funciona la creación de base de datos.
* Funciona use database.
* Funciona insert.
* Funciona select con where.
* Funciona create table con primary y foreign key.
* Funciona hacer un select buscando valores de una tabla que estén en otra.
* Funciona Truncate.

Las partes que presentan algúna falla son los siguientes:
* Update no funciona correctamente. No actualiza la información en las tuplas.
* AlterTable no funciona correctamente, si cambia la información en el typechecker pero no en la estructura.
* Alterdatabase rename funciona, sin embargo luego al querer usar la base de datos no encuentra la base.
* Delete si elimina, pero no elimina correctamente lo que uno le solicita, sino elimina otra tupla.
