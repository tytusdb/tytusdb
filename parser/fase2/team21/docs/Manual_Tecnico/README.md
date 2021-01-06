# **MANUAL TÉCNICO**

## Introducción

TytusDB es un administrador de bases de datos, se divide en tres componentes para su funcionalidad, al curso de compiladores 2 le corresponde el análisis léxico, sintáctico y semántico de la entrada.

Para ello se realizó la construcción de un intérprete que acepta las instrucciones de un subconjunto del lenguaje SQL, definido previamente, utilizando la herramienta PLY para la construcción del parser.

A su vez se tienen tres componentes, siendo estos: SQL parser, en donde pasa por todo un proceso de validaciones hasta llegar a la ejecución de las instrucciones, en la cual se programó verificando y validando las reglas semánticas, se hizo uso del Storage Manager para almacenar la información de las bases de datos creadas y de sus tablas correspondientes; Type Checker, donde se validan los tipos de datos que fueron aceptados en el parser; Query Tool, se cuenta con un editor de texto, capaz de resaltar palabras reservadas y tipos de datos, en dicha área se ingresan las consultas, contiene una consola, donde se muestran los resultados de las consultas, mensajes de éxito o advertencias.

___

## Marco Téorico

* **Interprete** es un patrón de diseño que, dado un lenguaje, define una representación para su gramática junto con un intérprete del lenguaje. Se usa para definir un lenguaje para construir expresiones regulares que representen cadenas a buscar dentro de otras cadenas.

* **Patrón de diseño** son unas técnicas para resolver problemas comunes en el desarrollo de software y otros ámbitos referentes al diseño de interacción o interfaces.

* **Clase abstracta** Es una clase en la que se pueden definir tanto métodos como propiedades, pero que no pueden ser instancias directamente. Solamente se pueden usar para construir subclases. 

* **Parser** programa que analiza una porción de texto para determinar su estructura lógica.

* **PLY** es una herramienta de análisis escrita exclusivamente en Python. Tiene casi todas las características proporcionadas por Lex y Yacc. Incluye soporte para producciones vacías, reglas de precedencia, recuperación de errores y gramáticas ambiguas . Es compatible con Python 3

* **Análisis léxico** agrupa los carácteres que va leyendo uno a uno del programa fuente y formar los tokens. Aumenta la portabilidad del compilador, pudiendo tenerse
versiones diferentes para distintos formatos del texto de
código fuente (ASCII, EBCDIC, etc.). Se simplifica el diseño, puesto que hay una herramienta
especializada en el tratamiento del fichero que contiene el
código fuente.

* **Análisis semántico** utiliza el árbol sintáctico y la información en la tabla de símbolos para comprobar la consistencia semántica del programa fuente con la definición del lenguaje.

* **Árbol de sintáxis abstracta** es una representación de árbol de la estructura sintáctica abstracta del código fuente escrito en un lenguaje de programación . Cada nodo del árbol denota una construcción que ocurre en el código fuente. Árbol de sintaxis abstracta.

* **Tabla de símbolos** es una estructura de datos que usa el proceso de traducción de un lenguaje de programación, por un compilador o un intérprete, donde cada símbolo en el código fuente de un programa está asociado con información tal como la ubicación, el tipo de datos y el ámbito de cada variable.
___

## Objetivos

* General

    *  Crear un intérprete para un subconjunto del lenguaje SQL.

* Especificos

    * Diseñar una interfaz amigable para el usuario.

    * Construir el árbol de sintaxis abstracta para verificar el funcionamiento del parser.

    * Realizar validaciones semánticas de manera adecuada.

    * Almacenar de manera correcta los datos proporcionados para obtener las consultas que se realicen.

---

## Arquitectura

![imagen](Estados1.png)

![imagen](Estados.png)

## Patrón de diseño

Se utilizó el patrón interprete, usando dos clases abstractas principales, las cuales son Instruccion y Exp.

Para cada instrucción relevante se creó una clase que contenga lo necesario para su análisis semántico.

Las clases de mayor importancia son: 


```python
class CreateReplace(Instruccion):
    '''#1 create
       #2 create or replace'''
    def __init__(self, caso, exists, id, complemento,fila,columna):
        self.caso = caso
        self.exists = exists
        self.id = id
        self.complemento = complemento
        self.fila = fila
        self.columna = columna
```

Utilizada para almacenar los datos referentes a la creación de una base de datos.


```python
class CreateTable(Instruccion):
    def __init__(self, id, campos, idInherits,fila,columna):
        self.id = id
        self.campos = campos
        self.idInherits = idInherits
        self.fila = fila
        self.columna = columna

```
Para la creación de las tablas dentro de la base de datos, esta clase llega a contener otra de gran importancia, ya que da los parámetros que le corresponden a cada campo de la tabla.

De la funcionalidad de estas dos primeras dependerá el resto. A continuación el constructor de las instrucciones DML.

```python
class InsertInto(Instruccion):
    def __init__(self,caso, id, listaId, values,fila,columna):
        self.caso=caso
        self.id = id
        self.listaId = listaId
        self.values = values
        self.fila = fila
        self.columna = columna
```

```python
class Delete(Instruccion):
    def __init__(self,caso, id, where,fila,columna):
        self.caso = caso
        self.id = id
        self.where = where
        self.fila = fila
        self.columna = columna
```

```python
class Update(Instruccion):
    def __init__(self, id, asignaciones, where,fila,columna):
        self.id = id
        self.asignaciones = asignaciones
        self.where = where
        self.fila = fila
        self.columna = columna
```

```python
class Select(Instruccion):
    '''#1 time
       #2 p_instselect
       #3 p_instselect2
       #4 p_instselect3
       #5 p_instselect4
       #6 p_instselect7'''

    def __init__(self, caso, distinct, time, columnas, subquery, inner, orderby, limit, complementS,fila,columna):
        self.caso = caso
        self.distinct = distinct
        self.time = time
        self.columnas = columnas 
        self.subquery = subquery
        self.inner = inner 
        self.orderby = orderby
        self.limit = limit
        self.complementS = complementS
        self.fila = fila
        self.columna = columna
```
La clase de mayor relevancia que hereda de Exp es Expresión, en ella se contendrán las operaciones aritméticas, relacionales, booleanas.

```python
class Expresion(Exp):
    def __init__(self, iz, dr, operador,fila,columna):
        self.iz = iz
        self.dr = dr
        self.operador = operador
        self.fila = fila
        self.columna = columna
```


## Gramática utilizada

>Se optó por utilizar la [gramática ascendente](https://github.com/MarcosAlberto21/tytus/blob/main/parser/fase2/team21/Analisis_Ascendente/ascendente.py)

___

El uso de clases para cada tipo de instrucción facilitó el envió a ejecución así como la realización del árbol de sintáxis abstracta.

```python
    def TiposInstruccion(self, inst, padre):
        if inst != None:
            for i in inst:
                if isinstance(i, CreateTable):
                    self.CreateTable(i, padre)
                elif isinstance(i, InsertInto):
                    self.InsertInto(i, padre)
                elif isinstance(i, CreateReplace):
                    self.CreateReplace(i, padre)
                elif isinstance(i, Show):
                    self.Show(padre)
                elif isinstance(i, AlterDatabase):
                    self.AlterDatabase(i, padre)
                elif isinstance(i, AlterTable):
                    self.AlterTable(i, padre)
                elif isinstance(i, Update):
                    self.Update(i, padre)
                elif isinstance(i, Delete):
                    self.Delete(i, padre)
                elif isinstance(i, Select):
                    self.Select(i, padre)
                elif isinstance(i, Union):
                    self.Union(i, padre)
                elif isinstance(i, Use):
                    self.Use(i, padre)
                elif isinstance(i, Drop):
                    self.Drop(i, padre)
                elif isinstance(i, CreateType):
                    self.CreateType(i, padre)
```

De manera similar se envió cada instrucción a ejecución, dentro de cada clase se encuentra el método ejecutar o resolver según sea el caso.

---
## Bibliografía

* [Instalación PLY](https://pypi.org/project/ply/)

* [Descargable PLY](https://www.dabeaz.com/ply/)

* [Documentación PLY](https://www.dabeaz.com/ply/ply.html)

* [Documentación Graphviz](https://graphviz.org/documentation/)

* [Graphs with dot](https://graphviz.org/pdf/dotguide.pdf)

* [Documentación HTML](https://devdocs.io/html/)

* [Documentación PDF](https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdfs/pdf_reference_archives/PDFReference.pdf)

* [PrettyTable](https://pypi.org/project/prettytable/)

* [Documentación pip install](https://pip.pypa.io/en/stable/reference/pip_install/)

* [Documentación python](https://docs.python.org/es/3/)

---
## Licencias

Se está utilizando la licencia MIT, que se originó en el Instituto Tecnológico de Massachusetts, es una licencia de software libre permisiva, da muy pocas limitaciones, permitiendo reutilizar software dentro del software propietario. La licencia no posee copyrigth esto permite su modificación. Es usada muy a menudo en el software libre.

Licencia de PLY: 

Copyright (C) 2001-2011,
David M. Beazley (Dabeaz LLC)
All rights reserved.