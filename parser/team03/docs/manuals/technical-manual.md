# MANUAL TECNICO

## Requerimientos para el desarrollo
* [PLY (Python Lex-Yacc)](https://www.dabeaz.com/ply/) Included.
* [Python 3](https://www.python.org/downloads/) This has to be installed by you.

## Requerimientos del entorno
### Librerías, paquetes y modulos
 - [jsonMode.py](https://github.com/tytusdb/tytus/blob/main/storage/storageManager/jsonMode.py)
- [numpy](https://pypi.org/project/numpy/)
- [tabulate](https://pypi.org/project/tabulate/)
 ### Software para graficar
 - [Graphviz](https://graphviz.org/)

## Clases
- [query_tool.py](https://github.com/tytusdb/tytus/blob/main/parser/team03/query_tool.py) : 
    Intefaz del usuario

- [grammarReview.py](https://github.com/tytusdb/tytus/blob/main/parser/team03/grammarReview.py): Analizador léxico y sintáctico basado en [PLY](https://www.dabeaz.com/ply/)
- [Carpeta parse](https://github.com/tytusdb/tytus/tree/main/parser/team03/parse): Proporciona las clases necesarias para el análisis sintáctico
    * [expressions](https://github.com/tytusdb/tytus/tree/main/parser/team03/parse/expressions): Conjunto de clases para la ejecución de las expresiones enums, basicas de la gramática, funciones matemáticas y funciones trigonométricas

    * [functions](https://github.com/tytusdb/tytus/tree/main/parser/team03/parse/functions): Conjunto de clases para la ejecución de funciones agregadas, funciones de control y funciones para strings

    * [sql_common](https://github.com/tytusdb/tytus/blob/main/parser/team03/parse/sql_common/sql_general.py): Conjunto de clases para la ejecución de consultas básicas para SQL.
    
    * [sql_ddl](https://github.com/tytusdb/tytus/tree/main/parser/team03/parse/sql_ddl) : Conjunto de clases para la ejecución de sentencias DDL de SQL

    * [sql_dml](https://github.com/tytusdb/tytus/tree/main/parser/team03/parse/sql_dml):  Conjunto de clases para la ejecución de sentencias DML de SQL

    * [ast_node.py](https://github.com/tytusdb/tytus/blob/main/parser/team03/parse/ast_node.py): Clase abstracta de la que extienden la mayoria de las clases que permiten la ejecución del análisis semántico. Es la base del AST.

    * [errors.py](https://github.com/tytusdb/tytus/blob/main/parser/team03/parse/errors.py) : Clase que permite instanciar errores de tipo lexico, sintáctico y semántico durante el análisis.

    * [symbol_table.py](https://github.com/tytusdb/tytus/blob/main/parser/team03/parse/symbol_table.py): Define los tipos de Simbolos en la tablas de símbolos, así como diferentes métodos para su manejo


## Métodos