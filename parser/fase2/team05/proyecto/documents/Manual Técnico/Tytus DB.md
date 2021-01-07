[TOC]

# Tytus DB

## Introducción

El siguiente manual muestra una descripción de las herramientas utilizadas para el desarrollo del proyecto de Tytus DB. Es un proyecto *open source* que es capaz de analizar instrucciones de SQL para la ejecución de la misma, así como la detección de errores en su sintaxis, errores léxicos, sintácticos y semánticos. 



## Objetivos

### Generales

- Dar a conocer el proyecto a interesados en el mantenimiento del mismo, o en conocer su funcionalidad. 

### Específicos

- Dar a conocer las herramientas de programación utilizadas en el desarrollo de Tytus DB. 
- Explicar el proyecto y los componentes que posee. 



## Usuarios

- A cualquier persona que se muestre interesada en el mantenimiento del programa. 

- A cualquier persona que quiera investigar el funcionamiento del proyecto Tytus DB.



## Descripción de Proyecto

Es un proyecto Open Source para desarrollar un administrador de bases de datos. Está compuesto por 3 componentes interrelacionados:

- El administrador del almacenamiento de la base de datos. 
- El administrador de la base de datos
  - Servidor
  - Cliente
- SQL Parser

#### Componentes

SQL Parser está compuesto por 3 sub componentes:

- **SQL Parser**. Es el intérprete de sentencias de SQL, que proporcionará una función para invocar al parser, al recibir una consulta el parser luego del proceso interno y de la planificación de la consulta debe invocar las diferentes funciones proporcionadas por el componente de administrador de almacenamiento.
- **Type Checker**. Es un sub componente que ayudará al parser a la comprobación de tipos. Al crear un objeto cualquiera se debe crear una estructura que almacenará los tipos de datos y cualquier información necesaria para este fin.
- **Query Tool**. Es un sub componente que consiste en una ventana gráfica similar al Query Tool de pgadmin de PostgreSQL, para ingresar consultas y mostrar los resultados, incluyendo el resalto de la sintaxis. La ejecución se realizará de todo el contenido del área de texto.



## Herramientas de Desarrollo

#### Python

Python es un lenguaje de programación interpretado, de alto nivel y de propósito general. La filosofía de diseño de Python enfatiza la legibilidad del código con su notable uso de espacios en blanco significativos.

A continuación se muestra información de la versión utilizada:

```
Python version 3.8.3
```

#### JetBrains PyCharm

PyCharm es un IDE de python que proporciona distintas herramientas para la edición de código, como la completación de metodos, inspección de código, relatar errores sobre la marcha y correcciones rápidas. 

A continuación se muestra información de la versión utilizada:

```
PyCharm 2020.3.2 (Professional Edition)
Build #PY-203.6682.179, built on December 30, 2020
Runtime version: 11.0.9.1+11-b1145.63 amd64
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
Windows 10 10.0
GC: ParNew, ConcurrentMarkSweep
Non-Bundled Plugins: com.jetbrains.intellij.datalore
```

#### PLY

PLY es una implementación de las herramientas de parseo de lex y yacc para Python. 

- Está implementado puramente en Python
- Utiliza parseo-LR
- PLY provee de las características básicas de lex/yaac, incluyendo el soporte hacia producciones vacias, recuperación de errores y el soporte de gramáticas ambiguas. 

A continuación se muestra información de la versión utilizada:

```
Python Lex-Yacc
Version 3.11
https://www.dabeaz.com/ply/
```



## Gramática

PLY es una herramienta de análisis de lenguajes gramaticales basado en Python, que tiene implementado las herramientas de parseo de **lex** y **yacc**. PLY provee a los usuarios de las características básicas de lex/yacc, siendo estas las producciones vacías, precedencia de reglas, recuperación de errores y suporte a gramáticas ambiguas. 

 De acuerdo con investigaciones hechas por el grupo, revisamos que la herramienta PLY usa un parseo LR, y que esta ayuda a que el análisis sea más eficiente y adecuada para grandes programas, o gramáticas de gran tamaño. [PLY (Python Lex-Yacc) (dabeaz.com)](https://www.dabeaz.com/ply/). Es por eso que, como grupo, hemos elegido usar una gramática ascendente. El objetivo de este consiste en construir el árbol sintáctico desde abajo hacia arriba, lo cual disminuye el número de reglas mal aplicadas con respecto al análisis descendente. 