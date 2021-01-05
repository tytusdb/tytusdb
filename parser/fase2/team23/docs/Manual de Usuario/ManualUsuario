Universidad de San Carlos de Guatemala


Ingeniería en Ciencias y Sistemas


Organización de Lenguajes y Compiladores 2


Ing. Luis Espino


Aux. Juan Carlos Maeda 

#Manual de Usuario SQL Parser

Grupo 29

Quetzaltenango diciembre 
2020

## Indice

- Presentación

	- Caracteristicas de SQL Parser
	
- Inicio del Programa

- Query Tool

	- Menú
	
	- Área de consultas
	
	- Área de resultados
	
	- Consulta
	
		- Tipo de Consultas
		
	- Pantalla Tabla de Símbolos
	
	- Pantalla AST
	
	- Pantalla Reporte de Errores

##Presentación

Tytus es un proyecto Open Source para desarrollar un administrador de bases de datos y está compuesto por tres componentes interrelacionados los cuales son:

- Administrador de bases de datos
- Administrador de almacenamiento de la base de datos
- SQL parser
 
SQL parser es el componente que proporciona al servidor una funcionalidad encargada de interpretar un subconjunto de sentencias del lenguaje SQL y este a su vez está conformado por tres subcomponentes:

- SQL parser
- Type Checker
- Query Tool

###Características de SQL parser

- Ejecución de Sentencias
- Visualización de Tabla de Símbolos
- Visualización de Errores (Léxicos, Sintacticos, Semánticos)
- Visualización de un Árbol de Sintaxis Abstracta


##Inicio del Programa

Diríjase a la carpeta donde se ubica el ejecutable del programa y de doble clic en el archivo seguidamente aparecerá la pantalla principal (Ver figura 1)

![Figura 1. Query Tool (Pantalla principal de SQL parser](./img/PantallaPrincipal.png)

Figura 1. Query Tool (Pantalla principal de SQL parser)

##Query Tool

Query Tool es una herramienta gráfica que tiene como propósito la facilidad de realizar consultas y visualizar el resultado de las mismas. Está conformada por tres componentes (Ver figura 2):

- Menú
- Área de consultas
- Área de resultados

![Figura 2. Localización de los componentes de Query Tool](./img/LocalizacionComponentesQT.png)

Figura 2. Localización de los componentes de Query Tool

###Menu

El menú cuenta con tres elementos (Ver figura 3) los cuales son:

- Tabla de Símbolos
- AST
- Reporte de errores

Cada uno de estos elementos redirige hacia la ventana en donde se visualizará la información debida.

![Figura 3. Barra de menú de Query Tool](./img/Menu.png)

Figura 3. Barra de menú de Query Tool


###Área de Consultas

El área de consultas está conformado por 2 elementos (Ver figura 4), el panel de entrada de texto y el botón Consultar.

 
En el panel de entrada de texto se ingresa la consulta a ejecutar y al presionar el botón Consultar se procederá a la ejecución de la misma.

![Figura 4. Área de consultas](./img/AreaConsultas.png)

Figura 4. Área de consultas

###Área de Resultados

El área de resultados mostrará la respuesta de la consulta o los errores que esta posea.

###Consulta

####Tipo de Consultas

En el programa se podrán realizar los siguientes tipos de consultas:

- SELECT
- INSERT
- UPDATE
- DELETE
- DROP
- CREATE
- ALTER
- SHOW
- USE

Para más información acerca de la forma de realizar consultas diríjase al siguiente [enlace][tytus]

[tytus]: https://github.com/tytusdb/tytus/tree/main/docs/sql_syntax


Cuando ya se haya ingresado la consulta en el panel de entrada de texto deberá presionar el botón Consultar.


Si la consulta no posee ningún error en el área de resultados aparecerá la consulta ya procesada (Ver figura 5), de lo contrario se mostrará un mensaje de error (Ver figura 6) si este es de tipo lexico, sintactico y semantico, además de proporcionar una breve descripción en el área de resultados (Ver figura 7).

__Nota: Si se realiza dos o más consultas estas aparecerán identificadas con un número correlativo, en el orden que fueron ingresadas, por medio de pestañas.__

![Figura 5. Visualizacion de Consultas](./img/VisualizacionConsultas.png)

Figura 5.  Visualización de Consultas

![Figura 6. Mensaje de error](./img/MensajeError.png)

Figura 6. Mensaje de error

![Figura 7. Visualizacion de error en el area de resultados](./img/VisualizacionErrorAreaResul.png)

Figura 7. Visualización de error en el área de resultados

##Pantalla Tabla de Símbolos

En esta pantalla se visualiza una tabla la cual muestra las variables, funciones y procedimientos y sus atributos como lo son el identificador, tipo, dimensión entre otros. (Ver figura 8)

__Nota: Para regresar a la pantalla principal se puede presionar el botón Regresar o el botón de Cerrar (X) ubicado en la esquina superior derecha de la pantalla.__

![Figura 8. Pantalla de la Tabla de Simbolos](./img/PantallaTablaSimbolos.png)

Figura 8. Pantalla de la Tabla de Símbolos

##Pantalla AST
En esta pantalla se visualizará la imagen del árbol de sintaxis abstracta (Ver figura 9)

__Nota: Para regresar a la pantalla principal se puede presionar el botón Regresar o el botón de Cerrar (X) ubicado en la esquina superior derecha de la pantalla.__

![Figura 9. Pantalla AST](./img/PantallaAST.png)

Figura 9. Pantalla AST

##Pantalla Reporte de Errores

En esta pantalla se visualizarán los errores de tipo léxico, sintácticos y semánticos, los cuales tendrán una breve descripción y el número de línea en donde fueron encontrados. (Ver figura 10)

__Nota: Para regresar a la pantalla principal se puede presionar el botón Regresar o el botón de Cerrar (X) ubicado en la esquina superior derecha de la pantalla.__

![Figura 10. Pantalla de Reporte de Errores](./img/PantallaReporteErrores.png)

Figura 10. Pantalla de Reporte de Errores




