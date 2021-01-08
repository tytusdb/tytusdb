# **MANUAL DE USUARIO**

## TytusDB 

Es un administrador de bases de datos, que acepta un subconjunto del lenguaje SQL.

El editor de texto cuenta con resaltado de sintáxis, funcionalidades básicas como abrir y guardar archivo, copiar, cortar, pegar, crear nueva pestaña, numeración de filas y cerrar.

Desde aquí también es posible abrir los reportes:

* Errores léxicos
* Errores sintácticos
* Errores semánticos
* AST
* Gramatical
* Tabla de símbolos

![imagen1](c.PNG)

 El resaltado de sintáxis ayuda a diferenciar las palabras reservadas, id y cadenas.

 Al ser un subconjunto de lenguaje SQL aplican las mismas reglas, acepta palabras reservadas tanto en minúscula, mayúscula o una mezcla de ellas. Se recomienda usar las palabras reservadas en mayúsculas

 ![imagen2](c1.PNG) 

---
* #### Abrir archivo

Es posible desde el icono

![imagen11](a1.PNG)

O desde la barra

![imagen12](a2.PNG)

En cualquiera de los casos se abrirá una ventana como la siguiente, donde se deberá escoger el archivo que se desea abrir.

![imagen10](abrir.PNG)

* #### Cerrar

Para cerrar una pestaña es posible desde el icono

![imagen13](cerrar1.PNG)

o desde la barra

![imagen14](cerrar2.PNG)

Si no se han guardado los cambio aparecerá lo siguiente 

![imagen15](cerrar.PNG)

Al seleccionar la opción si, cerrará la pestaña y se perderán los cambios, al seleccionar no, nos llevará a la siguiente ventana

![imagen16](guardarComo.PNG)

Será necesario escribir el nombre y tipo del archivo, ademas de seleccionar la ubicación.

Al aceptar aparecerá el siguiente mensaje.

![imagen17](ge.PNG)

* #### Guardar 

Este icono llevará a la ventana descrita con aterioridad

![imagen18](g1.PNG)

De igual manera se puede acceder desde la barra

![imagen19](g2.PNG)

* #### Pestaña nueva

Para crear una nueva pestaña solo hace falta presionar el icono

![imagen20](pes.PNG)

O desde la barra

![imagen21](pes2.PNG)

* #### Ejecutar

Para realizar la ejecución de una entrada solo hace falta colocarla en el área del texto, ya sea abriendo un archivo o pegandola directamente.

Luego presionar el icono de ejecución

![imagen22](correr.PNG)

O desde la barra

![imagen23](correr2.PNG)

Luego se verán los resultados en consola

* #### Copiar, cortar y pegar

![imagen24](xcv.PNG)

* #### Reportes

Para acceder a ellos deberá presionar en el icono correspondiente

![imagen25](reportes.PNG)

---

Cuenta con una consola, para muestra de errores, confirmación de acciones, resultado de consultas realizadas.

![imagen4](c3.PNG)

De esa manera se verán las consultas realizadas.

---

#### Los reportes se verán de la siguiente manera:

* Errores léxicos

![imagen5](c4.PNG)

* Errores sintácticos

![imagen6](c5.PNG)

* AST
![imagen7](c6.PNG)

* Gramatical

![imagen9](c8.PNG)

* Tabla de símbolos

![imagen8](c7.PNG)

## FASE 2

Se agrego un nuevo botón y nuevas funcionalidades.

![imagen1](NewQuerytool.PNG)

* #### Nueva Funcionalidades

  Se agregó la funcion de poder seleccionar la parte del codigo que se quiera ejecutar como se muestra en la imagen, en este caso solo  se ejecuto el CREATE DATABASE DBFase2; y USE DATABASE DBFase2; 

  ![imagen19](nuevaFunci.PNG)

* #### Nueva salida

  ![imagen19](salidaConsola.PNG)

  La consola ahora muestra la traduccion del codigo en tres direcciones de cada instrucción que se deseo ejecutar con anterioridad.

* #### Reporte de Optimización

  ![imagen19](botonOptim.PNG)

Este icono genera el reporte de Optimizacion.

![imagen19](reportOptim.PNG)

Al presionar el botón este generara el siguiente reporte.

Este contendra la regla que se utilizo el parte sin optimizar como la que ya esta optimizada.

![imagen19](reporOptim2.PNG)