## Universidad San Carlos de Guatemala
## Organización de Lenguajes y Compiladores 2
## Escuela de Vacaciones Diciembre    
  
    GRUPO 10:
    Elba María Alvarez Domínguez 201408549
    Andrea María Lopez Flores 201404134
    Ocsael Neftalí Ramirez Castillo 201404341
    Jurgen Andoni Ramirez Ramirez 201404179   

# **Selección entre gramáticas**


<p style="text-align: justify;"> Para seleccionar entre las dos gramáticas realizadas, una para un analizador ascendente y otra para un analizador descendente, en equipo se consideraron los siguientes factores: </p>


* Extensión de la gramática:

    <p style="text-align: justify;"> La gramática para el analizador descendente es de longitud mayor que la gramática para el analizador ascendente debido a que se debe de tomar en cuenta el remover la recursividad por la izquierda para que logre funcionar correctamente con atributos heredados y luego de esto, considerar las producciones que deben llevar incluido las producciones vacías que nos permitan recuperar toda la información resultante de las operaciones de atributos heredados para llegar, por medio de atributos sintetizados, al resultado esperado. Mientras que la gramática ascendente omite todo el proceso de descender con atributos heredados y al comenzar directamente desde los valores básicos para luego ascender con atributos sintetizando las operaciones y resultados finales resulta ser menos extensa. </p>

* Tiempo de realización del proyecto: 

    <p style="text-align: justify;"> Debido a la cantidad de tiempo disponible para la realización del proyecto en total consideramos elegir la gramática menos extensa y más comprendida por todos los integrantes del equipo de trabajo. </p>

* Velocidad de generación de árboles AST:

    <p style="text-align: justify;"> El descendente es más lento debido al tipo de herramienta utilizada, PLY, ya que se encuentra adaptada especialmente para análisis ascendentes y al realizar el recorrido simulando un análisis descendente se debe de manejar una pila temporal con el recorrido del árbol creado. Experimentalmente también comprobamos que el tiempo era mayor en el ascendente, el cual fue, en promedio, de **12.25** segundos. Mientras que el tiempo en el análisis descendente fue, en promedio, de **14.68**. </p>
