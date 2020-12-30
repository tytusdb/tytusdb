# Manual de Usuario

[![N|Solid](https://avatars0.githubusercontent.com/u/74935909?s=200&v=4)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Es un proyecto Open Source para desarrollar un administrador de bases de datos. Está compuesto por tres componentes interrelacionados: 

  - administrador de almacenamiento de la base de datos
  - administrador de la base de datos
  - SQL Parser

En este manual se describira como funciona el SQL parser es stand-alone 

## Propósito
El presente manual tiene como finalidad ser una guía basica de operación del sistema, permitiendo al lector de este manual adquirir las destrezas y conocimientos indispensables para una operación adecuada del sistema, y ser una herramienta de consulta de primera mano a la cual puede recurrir el usuario en cualquier momento.


## Interfaz de Usuario

<div align="center">
    <p align="center">
        Figura 1. Acciones semánticas en la gramática ascendente.
    </p>
    <img src="../assets/img/Interfaz.png" width="400">
</div>

### Partes de la Interfaz
    - Barra de Herramientas
    - Editor de Texto
    - Consola de Salida
    
#### Barra de Herramientas
En la barra de herramientas se encuentran todas las acciones que puede realizar el programa.

##### Archivo
Opciones disponibles:
| Opcion | Accion |
| ------ | ------ |
| Nuevo | Limpia el editor de texto |
| Abrir | Abre un archivo de texto y lo pega en el editor de texto |
| Guardar | Guarda los cambios realizados en el editor de texto |
| Guardar como | Crea un archivo con el texto del editor |
| Ejecutar | Ejecuta las instrucciones SQL del editor |
| Salir | Cierra el programa |

<div align="center">
    <p align="center">
        Figura 1. Acciones semánticas en la gramática ascendente.
    </p>
    <img src="../assets/img/Archivo.png" width="300">
</div>

##### Reportes
Opciones disponibles:
| Opcion | Accion |
| ------ | ------ |
| AST | Crea un arbol grafico del AST generado con la entrada en el editor |
| Type Checker | Muestra los datos almacenados en una estructura JSON de la base de datos |
| Tabla de Simbolos | Muestra los simbolos creados durante la ejecucion|
| Reporte de Errores | Errores encontrados durante la ejecucion |
| Reporte Gramatica BNF | Ejecuta las instrucciones SQL del editor |

<div align="center">
    <p align="center">
        Figura 1. Acciones semánticas en la gramática ascendente.
    </p>
    <img src="../assets/img/reportes.png" width="300">
</div>


### Tech

Tecnologias y librerias utilizadas para el desarrollo del SQL Parser

* [Python] - https://www.python.org/
* [Pandas] - https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html
* [markdown-it] - Markdown.


### Development

Desea contribuir o saber mas acerca del proyecto?
Repositorio: https://github.com/tytusdb/tytus


