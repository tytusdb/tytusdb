# Manual Tecnico

### Introduccion

Un compilador es un tipo de traductor que transforma un programa entero de
un lenguaje de programacion. Usualmente un lenguaje objeto es codigo máquina.   
  
El proyecto TytusDB es un manejador de sistemas de bases de datos (DBMS) open source, escrito en Python y basado en sintaxis de PosgreSQL. 

## Software Usado

### Visual Studio Code

Visual Studio Code es un poderoso y ligero editor de codigo el cual corre en el escritorio y esta disponible para Windows, macOS y Linux. Viene con soporte para diferentes lenguajes de programación y con capacidad para poder agregar lenguajes adicionales, temas, debuggers, comandos y mas.

## Hardware
* **Sistema Operativo:** Windows 
* **Tipo de Sistema:** 64 bits, procesador x64
* **Capacidad de Memoria (RAM) instalada:** 8.00 GB
* **Procesador:** Intel(R) Core(TM) i7-7700HQ


## Librerias Utilizadas para la realizacion del proyecto

##### * PLY phyton

Es una implementacion de herramientas de analisis de lex y yacc para python.


 * Se implementa completamente en Python
 * Utiliza el análisis LR que es razonablemente eficiente
   y muy adecuado para    gramáticas más grandes.
 * Posee soporte para parseo de gramaticas LALR(1).
 * PLY proporciona la mayoría de las características
   estándar de lex/yacc,incluida la compatibilidad con
   producciones vacías, reglas de precedencia,recuperación
   de errores y compatibilidad con gramáticas ambiguas.
* PLY es fácil de usar y proporciona una comprobación 
  de errores muy extensa.
* PLY no intenta hacer nada más o menos que proporcionar
  la funcionalidad básica de lex/yacc. En otras palabras,
  no es un marco de análisis grande o un componente de
  algún sistema más grande.

##### * tkinter ( Realizacion de la interfaz )
Es un paquete estandar de interfaz para Python. Viene instalado en la mayoría de plataformas Unix y Windows. 

##### * Graphviz python 
Es un software de visualización de grafos open source. La visualización de grafos es una manera de representar información estructural como diagramas de grafos abstractos y networks. 

Graphviz posee muchas funciones útiles para diagramas en concreto, como las opciones para colores, fuentes, estilos de línea y nodos, hipervínculos y formas personalizadas.

#### * MpMath
Es una librería libre para Python
basado en licensia BSD para poder hacer operaciones aritméticas con números reales y de punto flotante. Ha sido desarrollada por Frederik Johansson desde el año 2007, con la ayuda de muchos contribuidores. 

##### * Enum
La enumeración es un conjunto de miembros simbólicos unidos a valores únicos y constantes. En una enumeración, los miembros pueden ser comparados por identidad, y la enumeración puede ser iterada continuamente. 

##### * Random
Éste módulo implementa la generación pseudo aleatorio para varias distribuciones.   
  
Para enteros, hay selecciones uniformes en un rango. Para secuencias, hay una seleccion uniforme de un elemento aleatorio.

##### * Math
Este módulo provee acceso a las funciones matemáticas definidas por el lenguaje estandard de C.   
  
Estas funciones no pueden ser usadas con numeros complejos; si se requiere usar dichos números se debe usar el módulo cmath.

##### * Hashlib
Este módulo implementa una interfaz común a muchos hash seguros y mensajes para transcribir algoritmos. Incluidos están SHA256 y MD5. 

##### * base64
Éste módulo provee las funciones para la codificación de datos binarios a código ASCII imprimible y decodificar dichas codificaciones a datos binarios. Provee funciones de codificación y decodificación especificado en RFC 3548, el cual define algoritmos de codificación de Base16, Base32 y Base64 
##### * binascii
Éste módulo contiene un número de métodos para convertir entre binario y varias representaciones de codificaciones basadas en codificación ASCII. Normalmente, no se usan estas funciones directamente.


## Código Python

### expresiones.py

Posee todos los enums que identifican a los tipos de dato o acción, palabras reservadas y tipos a usar

```python
  class OPCIONESCREATE_TABLE(Enum):
    PRIMARIA = 1
    FORANEA = 2
    REFERENCES = 3
    NOT_NULL = 4
    NULL = 5
    PRIMARIA_SOLA = 6
    CONSTRAINT = 7
    UNIQUE = 8

class OPCIONES_UNIONES(Enum):
    UNION = 1
    INTERSECT = 2
    EXCEPTS = 3

class OPERACION_TIEMPO(Enum):
    YEAR = 1
    DAY = 2
    MOUNTH = 3
    HOUR = 4
    MINUTE = 5
    SECOND = 6
```

### gramatica.py

##### Analizador Léxico
Maneja la gramatica descendente creada usando PLY el cual está basado en Flex para el análisis léxico y Yacc para el análisis sintáctico.

Para crear palabras reservadas se declaran de la siguiente manera: 

```python
reservadas = {
    'create' : 'CREATE',
    'table':'TABLE',
    'tables':'TABLES',
    'inherits': 'INHERITS',
    'integer': 'INTEGER',
    'show': 'SHOW',
    .....  
    }
```
Si son necesitados otros símbolos o se agregan palabras reservadas usando expresiones regulares se deben de crear y agregar a una lista para así ser concatenadas junto con las palabras reservadas simples.   
  
```python 
    tokens = [
    'PTCOMA',
    'ASTERISCO',
    'COMA',
    'PAR_A',
    'PAR_C',
    'FLOTANTE',
    'ESCAPE',
    'HEX',
    .....
    ]
# Palabras reservadas por medio de expresiones regulares  
  
t_D_DOSPTS      = r'::'
t_PTCOMA        = r';'
t_COMA          = r','
....  
  
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t  
    
```
Para poder aceptar e ignorar propiamente los comentarios y todo tipo de espacio en blanco, se usan las siguientes expresiones:

```python 
def t_COMMENTM(t):
    r'(?s)/*.?*/'
    pass

# Caracteres ignorados
t_ignore = " \t"
t_ignore_COMMENT = r'(?:(--)[^\n])'
```
Una vez terminado el analizador léxico, se importan las librerias de PLY
```python 
import ply.lex as lex
lexer = lex.lex()
```
#### Analizador Sintáctico
Para el analizador sintáctico es importante definir una precedencia de operadores, para ello se usa precedencia
```python   
precedence = (
    ('left','MAYQUE','MENQUE','MAYIGQUE','MENIGQUE'),
    ('left','IGUAL','NOIG','NOIGUAL'),
    ('left','AND','OR'),
    ('left','SUMA','RESTA'),
    ('left','ASTERISCO','DIVISION'),
    ('nonassoc', 'IS'),
    ('right','UMINUS'),
    )

```
Para la creación del analizador sintáctico PLY usa producciones definidas, en la construcción del analizador también se puede encontrar las maneras por las cuales se realizaron los diferentes reportes.

La manera de crear producciones en PLY es la siguiente
```python 

def p_init(t) :
```
**p_** indica que es una producción

```python 
    'init            : instrucciones'
```    
La produccion conformada de terminales y no terminales que indican como el analizador debe leer la gramática

```python
    reporte_bnf.append("<init> ::= <instrucciones>")
```
*reporte_bnf* refiere a la lista donde se van almacenando las producciones BNF conforme se lean desde la entrada.
```python
    t[0] = t[1]
```
Acción que toma el analizador al momento de entrar en la producción

```python 
def p_instruccion(t) :
    'instruccion      : createDB_insrt'
    reporte_bnf.append("<instruccion> ::= <createDB_insrt>")
    t[0] = t[1]

def p_instruccion1(t) :
    'instruccion      : create_Table_isnrt'
    reporte_bnf.append("<instruccion> ::= <create_Table_isnrt>")
    t[0] = t[1]

def p_instruccion2(t) :
    'instruccion      : show_databases_instr'
    reporte_bnf.append("<instruccion> ::= <show_databases_instr>")
    t[0] = t[1]

def p_instruccion3(t) :
    'instruccion      : show_tables_instr'
    reporte_bnf.append("<instruccion> ::= <show_tables_instr>")
    t[0] = t[1]   
    
def p_instruccion4(t) :
    'instruccion      : drop_database_instr'
    reporte_bnf.append("<instruccion> ::= <drop_database_instr>")
    t[0] = t[1]
.....
```

PLY posee su propia manera de reconocer e informar sobre los errores tanto léxicos como sintácticos. Para ambos se usan los métodos de *t_error* y *p_error* respectivamente

```python 

def t_error(t):
    #print("Illegal character '%s'" % t.value[0], t.lineno, t.lexpos)
    errorLexico = Error(str(t.value[0]),int(t.lineno),int(t.lexpos), "Error Lexico")
    listaErrores.append(errorLexico)
    t.lexer.skip(1)
    
def p_error(t):
    #print("Error sintáctico en '%s'" % t.value, str(t.lineno),find_column(str(entradaa), t))
    global reporte_sintactico
    reporte_sintactico += "<tr> <td> Sintactico </td> <td>" + t.value + "</td>" + "<td>" + str(t.lineno) + "</td> <td> "+ str(find_column(str(input),t))+"</td></th>"
    errorSintactico = Error(str(t.value),int(t.lineno),int(find_column(str(entradaa),t)), "Error Sintactico")
    listaErrores.append(errorSintactico)     
    
```
Es usado para poder reportar la columna del error sintáctico.
```python 
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

```

Lee la entrada y la parsea
```python 
def parse(input) :
    global entradaa
    entradaa = input
    return parser.parse(input)

```

### instrucciones.py

Crea objetos dependiendo la instrucción, tipo de dato o lista que se desee almacenar


```python 

class Crear_altertable(Instruccion):
    def __init__(self,etiqueta,identificador,columnid,tocolumnid,expresionlogica,lista_campos = [],lista_ref = []):
        self.etiqueta = etiqueta
        self.identificador = identificador
        self.columnid = columnid
        self.tocolumnid = tocolumnid
        self.lista_campos = lista_campos
        self.expresionlogica = expresionlogica
        self.lista_ref = lista_ref

class Crear_tipodato(Instruccion):
    def __init__(self,identificador,tipo,par1,par2):
        self.identificador = identificador
        self.tipo = tipo
        self.par1 = par1
        self.par2 = par2

class Definicion_Insert(Instruccion):
    def __init__(self, val, etiqueta ,lista_parametros = [], lista_datos = []):
        self.val = val
        self.etiqueta = etiqueta
        self.lista_parametros = lista_parametros
        self.lista_datos = lista_datos

class Create_type(Instruccion):
    def __init__(self,identificador,lista_datos = []):
        self.identificador = identificador
        self.lista_datos = lista_datos

class Definicion_delete(Instruccion):
    def __init__(self, val, etiqueta, expresion, id_using, returning = []):
        self.val = val
        self.etiqueta = etiqueta
        self.expresion = expresion
        self.id_using = id_using
        self.returning = returning


```

### main.py

Se crea la interfaz de usuario, y se unen las funcionalidades con dicha interfaz, además de tener funciones especiales de análisis y generación de reportes

```python 
def analizar(txt):

    global instrucciones_Global,tc_global1,ts_global1,listaErrores
    instrucciones = g.parse(txt)
    if  erroressss.getList()== []:
        instrucciones_Global = instrucciones
        ts_global = TS.TablaDeSimbolos()
        tc_global = TC.TablaDeTipos()
        tc_global1 = tc_global
        ts_global1 = ts_global
        salida = procesar_instrucciones(instrucciones, ts_global,tc_global)

        if type(salida) == list:
            salida_table(1,salida)
        else:
            salida_table(2,salida)
    else:
        salida_table(2,"PARSER ERROR")
    #parse(txt)

def analizar_select(e):
    global selected
    if my_text.selection_get():

        global instrucciones_Global,tc_global1,ts_global1,listaErrores
        selected = my_text.selection_get()
        #print(selected)
        instrucciones = g.parse(selected)
        
        if erroressss.getList() == []:
            instrucciones_Global = instrucciones
            ts_global = TS.TablaDeSimbolos()
            tc_global = TC.TablaDeTipos()
            tc_global1 = tc_global
            ts_global1 = ts_global
            salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
            if type(salida) == list:
                salida_table(1,salida)
            else:
                salida_table(2,salida)
        else:
            salida_table(2,"PARSER ERROR")
...
```

### principal.ty  
Contiene la lógica principal del proyecto, se encarga de obtener los datos de la gramatica e ir haciendo las operaciones de a cuerdo a lo que se pide según las instrucciones dadas. Hace consultas a la tabla de símbolos y Type Checker para verificar que todo esté correcto  
  

```python 

            
def procesar_Definicion(instr,ts,tc,tabla) :
    tipo_dato = ""
    tamanio = ""
    if(isinstance(instr.tipo_datos,Etiqueta_tipo)):
        tipo_dato = instr.tipo_datos.etiqueta
        tamanio = ""
    elif(isinstance(instr.tipo_datos,ExpresionNumero)):
        tipo_dato = instr.tipo_datos.etiqueta
        tamanio = instr.tipo_datos.val
    elif(isinstance(instr.tipo_datos,Etiqueta_Interval)):
        tipo_dato = instr.tipo_datos.etiqueta
        tamanio = instr.tipo_datos.ext_time
    elif(isinstance(instr.tipo_datos,ExpresionTiempo)):
        tipo_dato = instr.tipo_datos.operador
        tamanio =  ""
    elif(isinstance(instr.tipo_datos,Expresion_Caracter)):
        tipo_dato = instr.tipo_datos.etiqueta
        tamanio =  instr.val
    
    if instr.opciones_constraint == None:
        buscar = tc.obtenerReturn(useCurrentDatabase,tabla,instr.val)
        if buscar == False:
            tipo = TC.Tipo(useCurrentDatabase,tabla,instr.val,tipo_dato,tamanio,"","",[])
            tc.agregar(tipo)
        else:
            print('No Encontrado')
            
    else:
        buscar = tc.obtenerReturn(useCurrentDatabase,tabla,instr.val)
        if buscar == False:
            tipo = TC.Tipo(useCurrentDatabase,tabla,instr.val,tipo_dato,tamanio,"","",[])
            tc.agregar(tipo)
        else:
            print('No Encontrado')
            
        for ins in instr.opciones_constraint:
            if isinstance(ins, definicion_constraint): 
                procesar_constraintDefinicion(ins,ts,tc,tabla,instr.val)

        

        ...
```

### report_ast.py, report_errores.py, report_tc.py, report_ts.py  

#### report_ast
Crea el AST de la gramatica por medio del uso de la librería Graphviz  
  
```python 
def crearNodoCreateTable(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CREATE TABLE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoNombreTabla(temp1,instruccion)
        if instruccion.instrucciones != []:
            for ins in instruccion.instrucciones:
                if isinstance(ins, Definicion_Columnas): 
                    self.crearNodoDefinicion(temp1, ins)
                elif isinstance(ins, LLave_Primaria): 
                    self.crearNodoConstraintLlavePrimaria(temp1, ins)
                elif isinstance(ins, Definicon_Foranea): 
                    self.crearNodoConstraintLlaveForanea(temp1, ins)
                elif isinstance(ins, Lista_Parametros): 
                    self.crearNodoConstraintUnique(temp1, ins)
                elif isinstance(ins, definicion_constraint): 
                    self.crearNodoConstraint(temp1, ins)
    
    def crearNodoNombreTabla(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'NOMBRE TABLA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoNombreTablaID(temp1,instruccion)

```
### report_BNF
Crea dinámicamente el reporte de la gramática en formato BNF, encontrado en el archivo gramatica.py

Obtiene la lista dada por repo_BNF y va escribiendo cada elemento de forma inversa para así obtener el reporte dinámico de la gramática en formato BNF.
```python 
def get_array(lista):
    lista_repo = lista
    reverse_list = lista_repo[::-1]
    w_jumps = '\n \n'.join(reverse_list)
    f = open("reportes/reportebnf.bnf", "w")
    
    for items in w_jumps:
        f.write(items)

    f.close()

```

#### report_errores
Reporta los errores sintácticos y semanticos de la gramática

```python 
 def getList(self):
        global listaErrores
        return listaErrores

    def clearList(self):
        
        global listaErrores
        listaErrores = []

    def crearReporte(self):
              
        f = open("reportes/errores.html", "w")
        f.write("<!DOCTYPE html>")
        f.write("<html lang=\"en\" class=\"no-js\">")
        f.write("")
        f.write("<head>")
        f.write("    <meta charset=\"UTF-8\" />")
...
```
#### report_tc
Genera un reporte del Type Checker
```python 
 def crearReporte(self,tc_global):
        f = open("reportes/tc.html", "w")
        f.write("<!DOCTYPE html>")
        f.write("<html lang=\"en\" class=\"no-js\">")
        f.write("")
        f.write("<head>")
        f.write("    <meta charset=\"UTF-8\" />")
        f.write("    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">")
        f.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
        f.write("    <title>Type Checker </title>")
        f.write("    <meta name=\"description\"")
        f.write("        content=\"Sticky Table Headers Revisited: Creating functional and flexible sticky table headers\" />")
        f.write("    <meta name=\"keywords\" content=\"Sticky Table Headers Revisited\" />")
        f.write("    <meta name=\"author\" content=\"Codrops\" />")
        f.write("    <link rel=\"shortcut icon\" href=\"../favicon.ico\">")
        f.write("    <link rel=\"stylesheet\" type=\"text/css\" href=\"css/normalize.css\" />")
   ...
```
Genera un reporte de la tabla de símbolos

```python 

    def crearReporte(self,ts_global):
        f = open("reportes/ts.html", "w")
        f.write("<!DOCTYPE html>")
        f.write("<html lang=\"en\" class=\"no-js\">")
        f.write("")
        f.write("<head>")
        f.write("    <meta charset=\"UTF-8\" />")
        f.write("    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">")
        f.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
        f.write("    <title>Tabla de Simbolos</title>")
        f.write("    <meta name=\"description\"")
        f.write("        content=\"Sticky Table Headers Revisited: Creating functional and flexible sticky table headers\" />")
        f.write("    <meta name=\"keywords\" content=\"Sticky Table Headers Revisited\" />")
...
```
### tc.py
Agrega, obtiene  y verifica la tabla del Type Checker

```python 
class TablaDeTipos() :
    'Esta clase representa la tabla de tipos'

    def __init__(self, tipos = []) :
        self.tipos = tipos

    def agregar(self, tipo) :
        self.tipos.append(tipo)
    
    def obtener(self, id) :
        if not id in self.tipos :
            print('Error: variable ', id, ' no definida.')

        return self.tipos[id]

    def obtenerReturn(self,database,tabla,column) :
        i = 0
        while i < len(self.tipos):
            if self.tipos[i].database == database and self.tipos[i].tabla == tabla and self.tipos[i].val == column:
                return self.tipos[i]
            i += 1
        return False

...
```

### ts.py
Crea la tabla de símbolos
```python 
 def actualizarDBTable(self, tabla, newTable) :
        i = 0
        while i < len(self.simbolos):
            if self.simbolos[i].ambito == tabla:
                self.simbolos[i].ambito = newTable
            i += 1

    def actualizarValorIdTable(self, simbolo, tabla, ambito) :
        i = 0
        while i < len(self.simbolos):
            if self.simbolos[i].ambito == ambito and self.simbolos[i].val == tabla:
                self.simbolos[i] = simbolo
            i += 1

    def obtener(self, tabla, ambito) :
        i = 0
        while i < len(self.simbolos):
            if self.simbolos[i].ambito == ambito and self.simbolos[i].val == tabla:
                return self.simbolos[i]
            i += 1
```

### FuncionesInter.py


```
class Intermedio():
	instrucciones_Global = []
	tc_global1 = []
	ts_global1 = []

	def __init__(self):
		''' Funcion Intermedia '''


	def procesar_funcion0(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
		instrucciones = g.parse('CREATE DATABASE prueba1;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
			return salida
		else:
			return 'Parser Error'


	def procesar_funcion1(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
		instrucciones = g.parse('USE prueba1;')
		erroressss = ErrorHTML()
		if  erroressss.getList()== []:
			instrucciones_Global = instrucciones
			ts_global = TS.TablaDeSimbolos()
			tc_global = TC.TablaDeTipos()
			tc_global1 = tc_global
			ts_global1 = ts_global
			salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
			return salida
		else:
			return 'Parser Error'
```

# Codigo tres direcciones
El ćodigo de tres direccioneses una secuencia de proposicionesde la forma general "x = y op z" donde op representa cualquier operador; x,y,z representan variables definidas por el programador o variables temporales generadas por el compilador. "y,z" tambi ́en pueden representar constantes o literales. "op" representa cualquier operador: un operador aritḿetico de punto fijo o flotante, o un operador logico sobredatos booleanos.
## Reglas de optimizacion
#### Optimizacion por mirilla
El  método  de  mirilla  consiste  en  utilizar  una  ventana  que  se  mueve  a  través  del  código  de  3 direcciones, la cual se le conoce como mirilla, en donde se toman las instrucciones dentro de la mirilla y se sustituyen en una secuencia equivalente que sea de menor longitud y lo más rápido posible que el bloque original. El proceso de mirilla permite que por cada optimización realizada con este método se puedan obtener mejoresbeneficios.


### traduccionPLSQL.py

Traducción de funciones a codigo tres direcciones.

```
def generarC3D(instrucciones, ts_global):
    global contadorLlamadas, tablaSimbolos, ts
    global cadenaTraduccion, tf, cadenaManejador
    global cadenaFuncionIntermedia,numFuncionSQL
    cadenaTraduccion = ""
    cadenaFuncionIntermedia = ""
    contadorLlamadas = 0
    numFuncionSQL = 0
    cadenaManejador = ""
    resetTemporalA()
    resetTemporalT()
    resetTemporalEtiqueta()
    tf = TF.TablaDeFunciones()

    cadenaFuncionIntermedia += "\nfrom gramatica import parse"
    cadenaFuncionIntermedia += "\nfrom principal import * "
    cadenaFuncionIntermedia += "\nimport ts as TS"
    cadenaFuncionIntermedia += "\nfrom expresiones import *"
    cadenaFuncionIntermedia += "\nfrom instrucciones import *"
    cadenaFuncionIntermedia += "\nfrom report_ast import *"
    cadenaFuncionIntermedia += "\nfrom report_tc import *"
    cadenaFuncionIntermedia += "\nfrom report_ts import *"
    cadenaFuncionIntermedia += "\nfrom report_errores import *\n\n"
    cadenaFuncionIntermedia += "\nclass Intermedio():"
    cadenaFuncionIntermedia += "\n\tinstrucciones_Global = []"
    cadenaFuncionIntermedia += "\n\ttc_global1 = []"
    cadenaFuncionIntermedia += "\n\tts_global1 = []\n"
    cadenaFuncionIntermedia += "\n\tdef __init__(self):"
    cadenaFuncionIntermedia += "\n\t\t''' Funcion Intermedia '''\n\n"

    cadenaTraduccion += "from FuncionInter import * " + "\n"
    cadenaTraduccion += "from goto import with_goto" + "\n\n"
    cadenaTraduccion += "inter = Intermedio()" + "\n\n"
    cadenaTraduccion += "@with_goto  # Decorador necesario." + "\n"
    cadenaTraduccion += "def main():" + "\n"
    cadenaTraduccion += "\tSra = -1" + "\n"
    cadenaTraduccion += "\tSs0 = [0] * 10000" + "\n"
    indice = 0
    ts = ts_global
    while indice < len(instrucciones):
        instruccion = instrucciones[indice]
        if isinstance(instruccion, ListaDeclaraciones):
            generarListaDeclaraciones(instruccion, ts)
        elif isinstance(instruccion, LlamadaFuncion):
            generarLlamadaFuncion(instruccion, ts)
        elif isinstance(instruccion, Principal):
            generarPrincipal(instruccion, ts)
            cadenaTraduccion += '\t\n'
            cadenaTraduccion += '\tgoto. end'
        elif isinstance(instruccion, Funcion):
            guardarFuncion(instruccion, ts)
        elif isinstance(instruccion, CreateDatabase):
            cadenaTraduccion += "\n\tprint(inter.procesar_funcion"+str(numFuncionSQL)+"())"
            cadenaFuncionIntermedia += createDatabaseFuncion(instruccion, ts)
        elif isinstance(instruccion, ShowDatabases):
            cadenaTraduccion += "\n\tprint(inter.procesar_funcion"+str(numFuncionSQL)+"())"
            cadenaFuncionIntermedia += createShowDatabasesFuncion(instruccion, ts)
        elif isinstance(instruccion, UseDatabase):
            cadenaTraduccion += "\n\tprint(inter.procesar_funcion"+str(numFuncionSQL)+"())"
            cadenaFuncionIntermedia += createUseDatabaseFuncion(instruccion, ts)
        elif isinstance(instruccion, ShowTables):
            cadenaTraduccion += "\n\tprint(inter.procesar_funcion"+str(numFuncionSQL)+"())"
            cadenaFuncionIntermedia += createShowTablesFuncion(instruccion, ts)
        elif isinstance(instruccion, DropDatabase):
            cadenaTraduccion += "\n\tprint(inter.procesar_funcion"+str(numFuncionSQL)+"())"
            cadenaFuncionIntermedia += createDropDatabaseFuncion(instruccion, ts)
        elif isinstance(instruccion, CreateTable):
            cadenaTraduccion += "\n\tprint(inter.procesar_funcion"+str(numFuncionSQL)+"())"
            cadenaFuncionIntermedia += createCreateTableFuncion(instruccion, ts)
        elif isinstance(instruccion, DropTable):
            cadenaTraduccion += "\n\tprint(inter.procesar_funcion"+str(numFuncionSQL)+"())"
            cadenaFuncionIntermedia += createDropTablesFuncion(instruccion, ts)
        elif isinstance(instruccion, AlterDatabase):
            cadenaTraduccion += "\n\tprint(inter.procesar_funcion"+str(numFuncionSQL)+"())"
            cadenaFuncionIntermedia += createAlterDatabaseFuncion(instruccion, ts)
        elif isinstance(instruccion, AlterTable):
            cadenaTraduccion += "\n\tprint(inter.procesar_funcion"+str(numFuncionSQL)+"())"
            cadenaFuncionIntermedia += createAlterTableFuncion(instruccion, ts)
        elif isinstance(instruccion, InsertTable):
            cadenaTraduccion += "\n\tprint(inter.procesar_funcion"+str(numFuncionSQL)+"())"
            cadenaFuncionIntermedia += createInsertTableFuncion(instruccion, ts)
            
        indice = indice + 1
    tablaSimbolos = ts
    
    cadenaTraduccion += "\n\tprint(inter.Reportes())"

    cadenaTraduccion += '\t\n'
    cadenaTraduccion += '\tgoto. end'
    agregarFunciones()
    agregarRetorno()
    cadenaTraduccion += "\n\n\tlabel .end" + "\n"
    cadenaTraduccion += "\treturn" + "\n"
    cadenaTraduccion += "\nmain()" + "\n"

    #REPORTES FASE 1
    
    cadenaFuncionIntermedia += generarFuncionesSQLREPORTES()

    salidaFuncionIntermedia = open("./FuncionInter.py", "w")
    salidaFuncionIntermedia.write(cadenaFuncionIntermedia)
    salidaFuncionIntermedia.close()

    return cadenaTraduccion
```