
### UNIVERSIDAD DE SAN CARLOS DE GUATEMALA
### FACULTAD DE INGENIERIA
### ORGANIZACIÓN DE LENGUAJES Y COMPILADORES 2
### ESCUELA DE VACIONES DICIEMBRE 2020
---
# MANUAL USUARIO

El presente documento detalla el funcionamiento básico de Tytus DBMS, el cual fue desarrollado por alumnos del curso de compiladores 2. Se cuenta con una gran variedad de funcionalidades las cuales se pueden encontrar para mayor información en el siguiente enlace: [Documentacion](https://github.com/tytusdb/tytus)


## PANTALLA PRINCIPAL

![Interfaz](https://github.com/tytusdb/tytus/blob/main/parser/team12/Manuales/Interfaz.png "Interfaz")

La interfaz de usuario esta compuesta por lo siguiente:

* TAB Archivo
   * Abrir Archivo: Opción que nos permite cargar un archivo en el editor  del dbms Tytus.
   * Analizar: Opción que nos permite analizar el texto cargado en el editor del dbms Tytus
   * Compilar: Opción utilizado para la ejecución del codigo generado.
   ![AST](https://github.com/tytusdb/tytus/blob/main/parser/team12/Manuales/compilar.png "AST")
* TAB Reportes
   * AST: Genera una imagen con el AST generado de la gramatica.
   ![AST](https://github.com/tytusdb/tytus/blob/main/parser/team12/Manuales/ast.png "AST")
   * Gramatica: Genera un archivo txt con la gramatica dinamica del archivo de entrada, en formato BNF.
   ![Gramatica](https://github.com/tytusdb/tytus/blob/main/parser/team12/Manuales/gd.png "Gramatica")
   * Tabla de Simbolos: Genera un archivo txt con la tabla de simbolos respectiva al archivo analizado
   ![Tabla de Simbolos](https://github.com/tytusdb/tytus/blob/main/parser/team12/Manuales/ts.png "Tabla de Simbolos")
* Consola Salida
    * Se muestra un cuadro de texto en el cual se mostraran las salidas de las consultas realizadas.
    ![Salida](https://github.com/tytusdb/tytus/blob/main/parser/team12/Manuales/salida.png "Salida")
* Consola de Errores
    * Se muestra un cuadro de texto en el cual se mostraran los errores encontrados en el archivo analizado.
    ![Error](https://github.com/tytusdb/tytus/blob/main/parser/team12/Manuales/error.png "Error")
* CD3
Tytus dbms es capaz de generar codigo de tres direcciones correspondientes a las entradas ingresadas.
El codigo generado por Tytus dbms se puede compilar para comprobar su funcionalidad.

## FUNCIONES
El lenguaje SQL aceptado, puede cumplir con lo siguiente:
* Crear bases de datos
* Crear tablas
* Insertar valores en la tabla
* Realizar consultas
* Manejo de expresiones
* Manejo de tipos
* Entre otras
![Ejemplo](https://github.com/tytusdb/tytus/blob/main/parser/team12/Manuales/ej.png "Ejemplo")