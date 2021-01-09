# MANUAL TÉCNICO

#  SQL PARSER -- FASE II


---



---

## Introducción

SQL Parser fase II es la ampliación del proyecto  del curso de escuela de vacaciones año 2020 de la Facultad de Ingeniería de la Universidad de San Carlos de Guatemala. En esta fase se realizan ampliaciones a la gramática reconocida,  se genera código y se optimiza.

El proyecto realiza  análisis léxico, sintáctico, semántico, generación de código en tres dirección y optimización de códogp de base la gramática de PostgresSQL.



## Herramientas utilizadas:

- PLY: Generador de analizadores léxicos y sintácticos para python
- Graphviz : Generador de imagenes a base de codigo.
- Python : Es un lenguaje de programación interpretado de alto nivel.
- tkinter : Librería utilizada para la cracion de la interfaz
- prettytable : Libreria utilizada para tabular los datos de una forma mas entendible



PLY es una herramienta de análisis escrita exclusivamente en Python. Es, en esencia, una reimplementación de Lex y Yacc originalmente en lenguaje C. Fue escrito por David M. Beazley. PLY utiliza la misma técnica de análisis LALR que Lex y Yacc.



---

## Tokens:

Un **token** es un par que consiste en un nombre de token y un valor de atributo opcional. Un lexema es una secuencia de caracteres en el programa fuente, que coinciden con el patrón para un token y que el analizador léxico identifica como una instancia de este token. su declaración es como se muestra a continuación:

    ``` 
Lex.py
(Token Generator)

tokens = [
    'PTCOMA',
    'LLAVEIZQ',
    'LLAVEDER',
    'PARENIZQ',
    'PARENDER',
    'IGUAL',
    'MAS',
    'GUION',
    'BARRA',
    'ASTERISCO',
    'MAYORQUE',
    'MENORQUE',
    'MENORIGUALQUE',
    'MAYORIGUALQUE',
    'DIFERENTELL',
    'PUNTO',
    'COMA',
    'ENTERO',
    'CADENA',
    'ID',
    'FEED',
    'NEWLINE',
    'TAB',
    'FECHA',
    'PORCENTAJE',
    'POTENCIA',
    'DOSPUNTOS',
    'PLECA',
    'AMPERSON',
    'NUMERAL',
    'VIRGULILLA',
    'DOLAR',
] + list(reservadas.values())

#tokens
t_PLECA         = r'\|'
t_AMPERSON      = r'&'
t_VIRGULILLA    = r'~'
t_NUMERAL       = r'\#'
t_DOSPUNTOS     = r':'
t_PTCOMA        = r';'
t_LLAVEIZQ      = r'{'
t_LLAVEDER      = r'}'
t_PARENIZQ      = r'\('
t_PARENDER      = r'\)'
t_IGUAL         = r'='
t_MAS           = r'\+'
t_GUION         = r'-'
t_ASTERISCO     = r'\*'
t_BARRA         = r'/'
t_MAYORIGUALQUE = r'>='
t_MAYORQUE      = r'>'
t_MENORIGUALQUE = r'<='
t_MENORQUE      = r'<'
t_DIFERENTELL   = r'<>|!='
t_PUNTO         = r'.'
t_COMA          = r'\,'
t_FEED          = r'\\f'
t_NEWLINE       = r'\\n'
t_TAB           = r'\\r'
t_PORCENTAJE    = r'%'
t_POTENCIA      = r'\^'
t_DOLAR         = r'\$'
    ```

    tokens = [
    'PLECA',
    'AMPERSON',
    'NUMERAL',
    'VIRGULILLA'
    ]
    t_PLECA         = r'\|'
    t_AMPERSON      = r'&'
    t_VIRGULILLA    = r'~'
    t_NUMERAL       = r'\#'
    
    ```

---

## Palabras Reservadas

Las palabras reservadas son palabrsa que tienen un significado gramatical especial para ese lenguaje y no puede ser utilizada como un identificador de objetos en códigos del mismo, para esta fase se añadieron nuevas palabras al lenguaje, su declaración es como se muestra a continuación:

```
reservadas = {
     #Fase2:
    'perform': 'PERFORM',
    'strict': 'STRICT',
    'found': 'FOUND',
    'raise': 'RAISE',
    'exception': 'EXCEPTION',
    'no_data_found' : 'NO_DATA_FOUND',
    'too_many_rows' : 'TOO_MANY_ROWS',
    'exception1': 'EXCEPTION1',
    'print_strict_params': 'PRINT_STRICT_PARAMS',
    'return': 'RETURN',
    'execute': 'EXECUTE',    
    'using': 'USING',      
    'index':'INDEX',
    'hash':'HASH',
    'returns' : 'RETURNS',
    'next':'NEXT',
    'query': 'QUERY',
    'call': 'CALL',    
    'elsif': 'ELSIF',    
    'notice': 'NOTICE',        
    'function' : 'FUNCTION',
    'begin' : 'BEGIN',
    'language':'LANGUAGE' ,
    'plpgsql' :'PLPGSQL',
    'declare' :'DECLARE',
    'desc' :'DESC',
    'asc' :'ASC',
    'alias' : 'ALIAS',
    'for' :'FOR',
    'procedure' : 'PROCEDURE',    
    'lower':'LOWER',
    'gist': 'GIST',
    'gin': 'GIN',
    'brin':'BRIN',
    'sp': 'SP',
    'tree' :'TREE',
}
```

---

## Manejor de Errores Léxicos y Sintácticos

Los errores Lexicos y sintácticos son manejados por una funcion dentro de cada analizador.

```

```

Para finalizar la creación del analizador léxico se declara de la siguiente manera:

```
import Librerias.ply.lex as lex
lexer = lex.lex()
```

---

## Analizador Sintáctico

El analizador sintactico o mas conocido como parser, que analiza una cadena de símbolos de acuerdo a las reglas de la gramática creada. 

Para finalizar la creacion del analizador sintactico se declara de la siguiente manera:

```
import Librerias.ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)
```

---

---

## Gramática creada para reconocer la Fase 2

Cada producción tiene asociadas reglas y acciones gramaticales para reconocer las distintas entradas del archivo de entrada.

**Producción para reconocer una función PL:**

```
def p_pl_funcion(t):
    '''pl_funcion : CREATE FUNCTION ID PARENIZQ parametrosf PARENDER RETURNS tipo AS DOLAR DOLAR pl_cuerpof  DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])+ ' ' +str(t[6])+ ' ' +str(t[7])+ ' ' +str(t[8]['visita'])+ ' ' +str(t[9])+ ' ' +str(t[10])+ ' ' +str(t[11])
    visitaarg1 = str(t[12]['visita'])
    visitaarg2 = str(t[13])+ ' ' +str(t[14])+ ' ' +str(t[15])+ ' ' +str(t[16])+ ' ' +str(t[17])

    grafo.newnode('pl_funcion')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    grafo.newchildrenF(grafo.index, t[8]['graph'])
    grafo.newchildrenF(grafo.index, t[12]['graph'])
    reporte = "<pl_funcion> ::= " + t[1].upper() + " FUNCTION ID <parametrosf>\n"+t[5]['reporte']+" RETURNS "+t[8]['reporte'] +" <cuerpof>\n" +t[12]['reporte']
    t[0] = {'ast' : pl_funciones.pl_Funcion('CREATE_FUNCTION',visita,visitaarg1,visitaarg2,t[3],t[5]['ast'],t[8]['ast'],t[12]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita, 'visitaarg1' : visitaarg1, 'visitaarg2': visitaarg2}
```

**Creación de indices, ejemplo:**

```
def p_createindex_lastnull(t):
    '''createindex : CREATE INDEX ID ON ID PARENIZQ ID NULLS LAST PARENDER PTCOMA
                   | CREATE INDEX ID ON ID PARENIZQ ID DESC NULLS LAST PARENDER PTCOMA    
                   | CREATE INDEX ID ON ID PARENIZQ ID ASC NULLS LAST PARENDER PTCOMA
    '''    
    if (len(t) == 12):
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]) + ' ' +str(t[9])+ ' ' +str(t[10])+ ' ' +str(t[11]) 
        grafo.newnode('CREATEINDEX NULLS LAST')
        grafo.newchildrenE(t[3])
        grafo.newchildrenE(t[5])
        grafo.newchildrenE(t[7])
        #grafo.newchildrenF(grafo.index, t[7]['graph'])
        #grafo.newchildrenE(t[7])#F(grafo.index, t[5])
        reporte = "<createindex> ::= CREATE INDEX " + t[3].upper() + " ON " + t[5].upper() + " PARENIZQ  " + t[7].upper() + " NULLS LAST PARENDER PTCOMA\n"
        #t[0] = {'ast': { "id": t[3], "id": t[5], "id": t[7],"id": t[8] }, 'graph' : grafo.index, 'reporte': reporte}          
        nombreind = "Nulls Last"
        t[0] = {'ast' : index_create.index_create('CREATEINDEX_NULLS_LAST',visita,t[1], t[3],t[5], None, t[7], None, nombreind, "B-tree"), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
```

---

**Manejo de querys **

```
ef p_querys(t):
    '''querys : select UNION allopcional select
              | select INTERSECT  allopcional select
              | select EXCEPT  allopcional select'''
    grafo.newnode('QUERYS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenE(t[2].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    if t[2].lower() == 'union' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4]['visita'])
        reporte = "<querys> ::= <select> UNION <allopcional> <select>"
        t[0] = {'ast': select.QuerysSelect('SELECT_UNION',visita,t[2].lower(),t[1]['ast'],t[3]['ast'],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2].lower() == 'intersect' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4]['visita'])
        reporte = "<querys> ::= <select> INTERSECT <allopcional> <select>"
        t[0] = {'ast': select.QuerysSelect('SELECT_INTERSECT',visita,t[2].lower(),t[1]['ast'],t[3]['ast'],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2].lower() == 'except' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4]['visita'])
        reporte = "<querys> ::= <select> EXCEPT <allopcional> <select>"
        t[0] = {'ast': select.QuerysSelect('SELECT_EXCEPT',visita,t[2].lower(),t[1]['ast'],t[3]['ast'],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
```

---

## Clases Abstractas

---

### Instrucciones

La creación de la clase instrucciones que va a ser la clase que hereda a las otras clases, esta clase contiene :

```
Asi como las instrucciones, expresion es una clase abstracta que hereda a cadauna de las funciones que se pueden utilizar al momento de hacer expresiones de los tipos:

- DDL - lenguaje de definición de datos
  - Alter
  - create
  - drop
  - show
  - use
- DML - 
  - Delete
  - Insert
  - Select
  - update
- INDEX
  - index_create
- PL
  - Asignación
  - Excepcion
  - Perform
  - Funciones
  - Procedimientos
  - Raise
```

---

### AST

Cada vez que se ejecuta una instrucción, se genera un AST el cual contiene los datos en cada nodo generado, este se recorre para interpretar dichas instrucciones.



### Tabla de símbolos para Indices

Para cada índice se genera un registro en la tabla de símbolos:

```
import sys
sys.path.append('../Grupo1/Instrucciones')
sys.path.append('../Grupo1/Utils')
sys.path.append('../Grupo1/Librerias/storageManager')

from instruccion import *
from Lista import *
from TablaSimbolos import *
from Primitivo import *
from Error import *
from jsonMode import *
import sys
sys.path.append('../Grupo1/Instrucciones')

class index_create(Instruccion):

    def __init__(self, arg0,arg1,namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice):
        self.namecom = namecom            #create. alter, drop 
        self.nombreindice =nombreindice
        self.tablaname = tablaname         
        self.unique = unique             #unique true false
        self.colname = colname
        self.tipoAscDes = tipoAscDes     # asc Desc   
        self.specs = specs               #not nulls last, not nulls first, lower
        self.tipoindice = tipoindice     #B-tree, Hash, GiST, SP-GiST, GIN and BRIN
        self.arg0 = arg0         
        self.arg1 = arg1         
        
    def execute(self, data):
        # if('IndicesTS' in data.tablaSimbolos) :
        #     nuevoindice = {self.namecom,self.nombreindice,self.tablaname,self.unique,self.colname,self.tipoAscDes,
        #     self.specs,self.tipoindice}

        #     data.tablaSimbolos['IndicesTS'].append(nuevoindice)
        # else:
        if 'IndicesTS' not in data.tablaSimbolos: 
            data.tablaSimbolos['IndicesTS'] = []


        cadcolname = self.colname
        # for i in self.colname:
        #     cadcolname += i.val + ","


        data.tablaSimbolos['IndicesTS'].append({
            'namecom' : self.namecom, 
            'nombreindice' : self.nombreindice, 
            'tablaname':self.tablaname,
            'unique' : self.unique, 
            'colname' : cadcolname,
            'tipoAscDes':self.tipoAscDes,
            'specs' : self.specs, 
            'tipoindice' : self.tipoindice
        })
        return 'tabla de simbolos de indices procesada.'

    def __repr__(self):
        return str(self.__dict__)
		
# class pl_CuerpoFuncion(Instruccion):
#     def __init__(self, declare,instrucciones):
#         self.declare = declare
#         self.instrucciones =instrucciones

#     def __repr__(self):
#         return str(self.__dict__)	
```

---

### 