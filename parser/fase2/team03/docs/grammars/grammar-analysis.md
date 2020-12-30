# Análisis de la gramática ascendente vs la gramática descendente

## Grupo 3
---

Se desarrollaron dos gramáticas para el Tutys a nivel sintáctico:
 * [Gramática ascendente (Bottom-Up)](https://github.com/tytusdb/tytus/blob/main/parser/team03/docs/grammars/gramatica-ascendente.md)
 * [Gramática descendente (Top-Down)](https://github.com/tytusdb/tytus/blob/main/parser/team03/docs/grammars/gramatica-descendente.md)

Se desarrolló un análisis para implementar la gramática más adecuada para el parser, para ello se tuvieron en cuenta los siguientes criterios:

* Tipo de analizador. [PLY (Python Lex-Yacc)](https://www.dabeaz.com/ply/) es un analizador LR, lo cual nos da la pauta que con la gramática ascendente el código a ejecutarse es más limpio.

* Ambigüedad: La ambigüedad no es un problema para la escritura de la gramática ascendente, ya que el mismo [PLY](https://www.dabeaz.com/ply/) maneja las reglas de precedencia.

* Tiempo. Al elegirse una gramática descendente hace que el tiempo de ejecución sea mayor, ya que se realizan dos recorridos, una lectura descendente y una ejecución ascendente.

* Cantidad de memoria dinámica en uso.Mayor uso del recurso de memoria con el uso de la gramática descendente, se tiene que hacer uso de otras estructuras de datos en memoria para la ejecución, por ejemplo el uso de la pila.

* Entrada. En un análisis top-down un parser hacer corresponder cadenas de entrada con sus correspondientes derivaciones izquierdas. En un análisis bottom-up un parser hace corresponder cadenas de entrada con las inversas de las correspondientes derivaciones derechas.

* Análisis de gramática. La gramática descendente necesita que se elimine la ambigüedad y que se elimine la recursividad por la izquierda; esto nos lleva a tener mayor cuidado y hacer las transformaciones pertinentes.

* Detección de errores. Los errores pueden detectarse tan pronto como sea posible hacerlo, en un examen de la entrada de izquierda a derecha.
