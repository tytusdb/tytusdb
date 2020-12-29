# REPORTE DE SELECCIÓN DE GRAMATICA

Para empezar con el reporte del porque utilizamos cierta gramática, es necesario conocer dicho concepto. Se define a continuación:

### GRAMÁTICA
---
Podemos definir que la gramática es al conjunto de reglas que se deben seguir al escribir código, como es este caso enfoque computacional, o ya sea algún idioma que posee su propia gramática. Existen 2 tipos de gramáticas, de las cuales nosostros debimos decidir cuál utilizaremos en nuestro proyecto.

* Gramática Ascendente
* Gramática Descendente

Dichas gramáticas, nos sirven para realizar el análisis sintáctico de los tokens reconocidos en el análisis léxico. Para conocer un poco a fondo las diferencias entre ambas gramáticas se realizará una explicación a continuación.

### GRAMÁTICA ASCENDENTE
---
* También conocido como analizador bottom - up.
*Se construye un árbol sintáctico para una cadena de entrada que comienza con las hojas y avanza hacia la raíz.
* Una cadena se "reduce" al símbolo inicial de la gramática.
* En cada paso de reducción, una subcadena específica que coincide con el lado derecho de una producción se reemplaza por el símbolo en el lado izquierdo de esa producción (básicamente se busca el lado derecho correspondiente y se reemplaza por el lado izquierdo y se intenta hacerlo). manera de llegar a la raíz)
* Un bypass se dibuja desde la derecha en dirección contraria

### GRAMÁTICA DESCENDENTE
---
* También conocido como analizador top - down. 
* Busque una derivación a la izquierda para una cadena de entrada l árbol de análisis. 
* Se construye partiendo de la raíz y creando los nodos en el orden anterior.
* No hay muchos analizadores de arriba hacia abajo con retroceso; el retroceso casi nunca es necesario para analizar construcciones de lenguaje de programación. El retroceso tampoco es muy eficiente.
* Una gramática recursiva izquierda puede hacer que el analizador entre en un bucle infinito (porque no consume ningún símbolo de entrada).
* Al eliminar la recursividad y la factorización, puede obtener una gramática analizable mediante un analizador predictivo de descenso que no necesita retroceso.

### CONCLUSIÓN
---
Después de un poco de teoría sobre la gramática ascendente y descendente, se hizo un analisis sobre que gramatica nos beneficiaría en la producción de dicho proyecto:

* PLY reconoce las gramáticas ascendentes.
* Los integrantes tienen más experiencia desarrollando gramáticas ascendentes.
* El tiempo de ejecución para una gramática ascendente en PLY es menor que el de una gramática descendente.
* La cantidad de producciones en una gramática ascendente es menor.

Por dichas razones elegimos realizar una gramatica ascendente. Si desea consultar nuestra [gramática](https://github.com/tytusdb/tytus/blob/main/parser/team23/grammar/Gramatica_Ascendente_BNF.md) en formato BNF.