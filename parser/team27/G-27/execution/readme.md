# EXECUTION

## Funcionalidad:
Creación de las clases para los nodos del AST, este se generará utilizando herencia de clases abstractas para poder recibir entornos padres y a su vez estos sean compatibles entre distintas clases, además se generarán las clases concretas en las cuales se tengan las verificaciones semánticas pertinentes a cada situación específica.

Los métodos abstractos optimizarán un recorrido utilizando unicamente la función execute del nodo raiz, el cual llamará a los operadores hijos de tal manera que resulte en lo necesario para devolver el resultado deseado.

### Tipos de clases concretas:

* Expresiones
* Funciones
* Queries
* Tabla de simbolos

### Caracteristicas de las clases abstractas
Generalización del método execute, generación de reporte gráfico del AST y atributos esenciales como fila y columna.

