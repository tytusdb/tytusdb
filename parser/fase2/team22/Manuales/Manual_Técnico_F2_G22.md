# Manual Técnico Fase 2.

A continuación se presentará el manual técnico para lo que fue trabajado en la fase 2.

La fase 2 del grupo 22, fue trabajado en base a la fase 1 del grupo 8, que era uno de los elegidos ya que tenían uno de los mejores punteos en la calificación.

## Análisis sintáctico.
El análisis sintáctico de la fase 2 se focalizó en nuevas instrucciones, entre ellas el reconocimiento de la creación de index, la creación de funciones y de procedimientos almacenados.
Es en estos 2 últimos que la gramática se extendió y se añadieron nuevas producciones.

#### Index
Los index en la fase 2 solamente serán reconocidos y almacenados en la tabla de símbolos. Y esta es la sintaxis.
```
instruccion  : CREATE INDEX ID ON ID PARIZQ l_expresiones PARDER params_crt_indx can_where
                    | CREATE INDEX ID ON ID USING HASH PARIZQ l_expresiones PARDER params_crt_indx can_where
instruccion  : CREATE UNIQUE INDEX ID ON ID PARIZQ l_expresiones PARDER params_crt_indx can_where
                    | CREATE UNIQUE INDEX ID ON ID USING HASH PARIZQ l_expresiones PARDER params_crt_indx can_where
can_where    : instructionWhere PUNTO_COMA
                    | PUNTO_COMA
l_expresiones    : l_expresiones COMA expre lista_options
l_expresiones    : expre lista_options
lista_options  : lista_options options
lista_options  : options
options      : ASC
                    | DESC
                    | NULLS FIRST
                    | NULLS LAST
                    | TXT_PTN_OPS
                    | VRCH_PTN_OPS
                    | BPCH_PTN_OPS
                    | COLLATE expre
                    | expre
params_crt_indx  : INCLUDE PARIZQ expre PARDER
                        | 
```

Para los index también pueden utilizarse la función Drop para eliminarlos del almacenamiento. Se usa la siguiente sintaxis.
```
instruccion  : DROP INDEX ID PUNTO_COMA
```

#### Function y Procedure
Las funciones y los procedimientos almacenados tienen una estructura similar, sin embargo aun tienen diferencias remarcables además de la reservada function y procedure. 
Las funciones y los procedimientos aceptan en su interior llamadas a querys, asignaciones, operaciones matemáticas y estructuras como if else y case else.
La diferencia entre Procedure y Function es que Function acepta el retorno de datos o información, mientras que procedure no los acepta, pero puede contener "COMMIT" y "ROLLBACK" que son acciones especiales en el ámbito sql.

La sintaxis para Function es la siguiente.
```
instruccion  : CREATE FUNCTION ID PARIZQ list_params_funct PARDER return_funct as_def PROC def_funct PROC LANGUAGE PLPGSQL PUNTO_COMA
                    | CREATE FUNCTION ID PARIZQ list_params_funct PARDER as_def PROC def_funct PROC LANGUAGE PLPGSQL PUNTO_COMA
                    | CREATE FUNCTION ID PARIZQ PARDER return_funct as_def PROC def_funct PROC LANGUAGE PLPGSQL PUNTO_COMA
                    | CREATE FUNCTION ID PARIZQ PARDER as_def PROC def_funct PROC LANGUAGE PLPGSQL PUNTO_COMA
return_funct     : RETURNS tipo
                        | RETURNS ID
                        | RETURNS TABLE PARIZQ list_params_funct PARDER
list_params_funct    : list_params_funct COMA ID tipo
                            | list_params_funct COMA OUT ID tipo
                            | list_params_funct COMA ID ID
                            | list_params_funct COMA OUT ID ID
list_params_funct    : ID tipo
                            | OUT ID tipo
                            | ID ID
                            | OUT ID ID
def_funct    : dec_def beg_def END PUNTO_COMA
dec_def  : DECLARE list_declare
                | 
list_declare : list_declare declare
list_declare : declare
declare  : ID constant def_tipos_declare list_params_declare symbol_declare expre PUNTO_COMA
                | ID constant def_tipos_declare symbol_declare expre PUNTO_COMA
declare  : ID constant def_tipos_declare list_params_declare PUNTO_COMA
                | ID constant def_tipos_declare PUNTO_COMA
declare  : ID ALIAS FOR expre PUNTO_COMA
def_tipos_declare    : tipo
                            | expre MODULO ID
content_begin    : IF condicion_if THEN list_begin elsif else_if END IF PUNTO_COMA
                        | IF condicion_if THEN list_begin else_if END IF PUNTO_COMA
                        | IF condicion_if THEN list_begin elsif END IF PUNTO_COMA
                        | IF condicion_if THEN list_begin END IF PUNTO_COMA
elsif       : ELSIF condicion_if THEN list_begin elsif
                   | ELSIF condicion_if THEN list_begin
else_if         : ELSE list_begin
condiciones_if   : condiciones_if AND condiciones_if
                        | condiciones_if OR condiciones_if
                        | condiciones_if
condiciones_if   : condicion_if
condicion_if : expre IGUAL expre
                    | expre DISTINTO expre
                    | expre MAYORQ expre
                    | expre MENORQ expre
                    | expre MAYOR_IGUALQ expre
                    | expre MENOR_IGUALQ expre
condicion_if : expre
constant : CONSTANT
                |
symbol_declare   : DEFAULT
                        | DOS_PUNTOS IGUAL
                        | IGUAL
list_params_declare  : list_params_declare params_declare
list_params_declare  : params_declare
params_declare   : COLLATE expre
                        | NOT NULL
beg_def  : BEGIN list_begin
list_begin : list_begin content_begin
list_begin : content_begin
content_begin    : RAISE NOTICE l_expresiones PUNTO_COMA
                        | RAISE EXCEPTION l_expresiones PUNTO_COMA
                        | asign PUNTO_COMA
                        | def_funct
                        | RETURN def_return PUNTO_COMA
                        | EXCEPTION list_exception
                        | query PUNTO_COMA
content_begin    : CASE lcase_begin END CASE PUNTO_COMA
lcase_begin  : lcase_begin case_begin
                    | case_begin
case_begin  : WHEN lista_expre_begin THEN list_begin
                | ELSE list_begin
lista_expre_begin    : lista_expre_begin COMA expre
                            | expre
asign    : expre DOS_PUNTOS IGUAL expre
list_exception   : list_exception except
                        | except
except   : WHEN expre THEN content_except
                | WHEN expre THEN
content_except   : RAISE EXCEPTION l_expresiones PUNTO_COMA
                        | NULL PUNTO_COMA
instruccion  : PERFORM function_call PUNTO_COMA
instruccion  : IF NOT FOUND THEN list_begin END IF PUNTO_COMA
```

La sintaxis para llamar la ejecución de la función es.
```
function_call    : ID PARIZQ l_expresiones PARDER
```

La sintaxis para los procedimientos almacenados es la siguiente.
```
instruccion  : CREATE PROCEDURE ID PARIZQ list_params_funct PARDER LANGUAGE PLPGSQL as_def PROC def_procedure PROC PUNTO_COMA
                    | CREATE PROCEDURE ID PARIZQ PARDER LANGUAGE PLPGSQL as_def PROC def_procedure PROC PUNTO_COMA
def_procedure    : dec_def beg_def_procedure END PUNTO_COMA
                        | beg_def_procedure END PUNTO_COMA
beg_def_procedure    : BEGIN list_begin_procedure
list_begin_procedure : list_begin_procedure content_begin_procedure
list_begin_procedure : content_begin_procedure
content_begin_procedure  : RAISE NOTICE l_expresiones PUNTO_COMA
                                | RAISE EXCEPTION l_expresiones PUNTO_COMA
                                | asign PUNTO_COMA
                                | def_procedure
                                | EXCEPTION list_exception
                                | query PUNTO_COMA
                                | COMMIT PUNTO_COMA
                                | ROLLBACK PUNTO_COMA
content_begin_procedure  : IF condicion_if THEN list_begin_procedure elsif_procedure else_if_procedure END IF PUNTO_COMA
                                | IF condicion_if THEN list_begin_procedure else_if_procedure END IF PUNTO_COMA
                                | IF condicion_if THEN list_begin_procedure elsif_procedure END IF PUNTO_COMA
                                | IF condicion_if THEN list_begin_procedure END IF PUNTO_COMA
elsif_procedure  : ELSIF condicion_if THEN list_begin_procedure elsif_procedure
                        | ELSIF condicion_if THEN list_begin_procedure
else_if_procedure         : ELSE list_begin_procedure
content_begin_procedure    : CASE lcase_begin_procedure END CASE PUNTO_COMA
lcase_begin_procedure  : lcase_begin_procedure case_begin_procedure
                              | case_begin_procedure
case_begin_procedure  : WHEN lista_expre_begin_procedure THEN list_begin_procedure
                          | ELSE list_begin_procedure
lista_expre_begin_procedure    : lista_expre_begin_procedure COMA expre
                                      | expre
```

## Generación de Código 3 direcciones.
La generación de codigo 3 direcciones ocurre dentro de las clases abstractas propias de cada instrucción o elemento. 

Como ejemplo se usará el de insert table.
Se hará uso del heap para poder almacenar los parámetros los cuales serán enviados a las funciones que estarán declaradas al principio del archivo c3d.py.
```
def generar3DV2(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append('h = p')
        code.append('h = h + 1')
        t00 = c3d.getTemporal()
        code.append(t00 + ' = "' + arbol.bdUsar + '"')
        code.append('heap[h] = ' + t00)
        code.append('h = h + 1')
        t0 = c3d.getTemporal()
        code.append(t0 + ' = "' + self.valor + '"')
        code.append('heap[h] = ' + t0)
        code.append('h = h + 1')
        if self.lcol != None:
            code.append('heap[h] = []')
            for columna in self.lcol:
                t1 = c3d.getTemporal()
                code.append(t1 + ' = ["' + columna + '"]')
                code.append('heap[h] = heap[h] + ' + t1)
        else:
            code.append('heap[h] = None')
        code.append('h = h + 1')
        code.append('heap[h] = []')
        for valor in self.lexpre:
            t2 = c3d.getTemporal()
            code.append(t2 + ' = [' + str(valor.generar3D(tabla, arbol)) + ']')
            code.append('heap[h] = heap[h] + ' + t2)
        code.append('p = h')
        code.append('call_insert_table()')
        
        return code
```
El propósito es ir aumentando el índice del heap y se utilizará de esta manera a la hora de llamar call_insert_table()
```
def call_insert_table():
    arbolAux = arbol
    arbolAux.bdUsar = heap[p-3]
    tabla = insertTable.insertTable(heap[p-2], None, heap[p-1], heap[p], '', 0, 0)
    tabla.ejecutar(tablaGlobal, arbolAux)
```

## Paso previo a optimización
Para la optimización del código 3 direcciones se deben seguir ciertas reglas, para que sea más sencillo analizarlas se implementaron 2 cosas muy importantes:
### 1 Clases para cada caso del 3 direcciones
El codigo 3 direcciones es una forma básica de programación, y hay casos muy específicos en como se va a escribir para su ejecución, por ejemplo la asignación, las sentencias if, goto, la creación de etiquetas, etc.

Por lo que es sencillo poder crear contenedores para poder analizar más sencillo que viene y así poder optimizarlo de una manera más rápida y facil para el programador.

Para ello se crearon clases especiales, que se describen a continuación.
```
from enum import Enum
class OP_ARITMETICO(Enum) :
    SUMA = 1
    RESTA = 2
    MULTIPLICACION = 3
    DIVISION = 4
    MODULO = 5
    POTENCIA = 6

class OP_RELACIONAL(Enum) :
    MAYOR_QUE = 1
    MAYOR_IGUAL_QUE = 2
    MENOR_QUE = 3
    MENOR_IGUAL_QUE = 4
    IGUAL = 5
    DIFERENTE = 6

aritmetico = {'SUMA': '+', 'RESTA': '-', 'MULTIPLICACION': '*', 'DIVISION': '/', 'MODULO': '%', 'POTENCIA': '^'}

class Identificador:
    def __init__(self, nombre):
        self.Id = nombre #Si hay variables o temporales, se utiizará esto para almacenarla.
        '''
        Ejemplo:
        t1 = a + 'texto'
        Identificador('t1')
        Identificaodr('a')
        Solo t1 y a serán guardados en esta clase, para poder identificar si se usan variables
        o si se están usando valores numéricos o incluso texto.
        Ya que el texto no se guardará con comillas, sino solo el texto base
        (esto solo es una sugerencia, si es necesario cambiarlo, o eliminarlo es factible.)
        '''

    def __str__(self):
        return self.Id

class Valor:
    def __init__(self, valor, tipo):
        self.Valor = valor #Valor contenido 
        self.Tipo = tipo #Tipo del valor contenido, puede ser número (entero o decimal) o caracter ('a')
        '''
        Ejemplo:
        t1 = 6 * 1.5
        Valor (6, ENTERO)
        Valor(1.5, DECIMAL)
        Para 6 -> Valor = 6, Tipo = ENTERO
        Para 1.5 -> Valor = 1.5, Tipo = DECIMAL
        '''

    def __str__(self):
        return str(self.Valor)

class ValorLista:
    def __init__(self, valor):
        self.Valor = valor
        '''
        Ejemplo:
        t1 = [var]
        ValorLista(Identificador('var'))
        '''
    
    def __str__(self):
        return str('[' + str(self.Valor) + ']')

class ListaPosicion:
    def __init__(self, id, posicion):
        self.Id = id
        self.Posicion = posicion
        '''
        Ejemplo:
        heap[t1] = 'esto'
        ListaPosicion(Identificador('heap'), Identificador('t1'))
        '''
    def __str__(self):
        return str(str(self.Id) + '[' + str(self.Posicion) + ']')

class LlamFuncion:
    def __init__(self, id):
        self.Id = id
        '''
        Ejemplo:
        call_insert_table()
        LlamFuncion(Identificador('call_insert_table'))
        '''
    
    def __str__(self):
        return str(str(self.Id) + '()')

class Operacion:
    def __init__(self, op1, op2, operador):
        self.Op1 = op1 #Op1 será el id o valor que estará a la izquierda del operador
        self.Op2 = op2 #Op2 será el id o valor que estará a la derecha del operador
        self.Operador = operador #Esto es un OP_ARTIRMETICO (tipo Enum) -> Está definido en la parte de arriba
        '''
        Ejemplo:
        t0 = 1 + 5
        Operacion(Valor(1, int), Valor(5, int), OP_ARITMETICO.SUMA)
        1 es op1, 5 es op2 y OP_ARITMETICO.SUMA es el operador
        t1 = m + 2
        Operacion(Identificador('m'), Valor(2, int))
        t2 = 2 - t1
        t3 = t2 * t1
        t4 = t3 / t1
        '''

    def __str__(self):
        return str(self.Op1) + " " + aritmetico[self.Operador.name] + " " + str(self.Op2)

class Condicion:
    def __init__(self, op1, op2, operador):
        self.Op1 = op1 #esto puede ser un valor, o un id
        self.Op2 = op2 #esto puede ser un valor o un id
        self.Operador = operador #Esto es un OP_RELACIONAL (tipo Enum) -> Está definido en la parte de arriba
        '''
        Ejemplo:
        x >= 1
        Condicion(Identificador('x'), Valor(1, int), OP_RELACIONAL.MAYOR_IGUAL_QUE)
        x es el op1
        1 es el op2
        OP_RELACIONAL.MAYOR_IGUAL_QUE es el operador
        1 == 0
        Condicion(Valor(1, int), Valor(0, float), OP_RELACIONAL.IGUALs)
        2 != y
        '''

class Asignacion:
    def __init__(self, asignado, valor):
        self.Tx = asignado #Este será el temporal, variable o Arreglo que almacenará lo que valor contenga
        self.Valor = valor #Esto puede variar, puede ser un id, un valor, una operación o una condicion
        '''
        Ejemplo:
        t1 = 1
        Instruccion = Asignacion(Identificador('t1'), valor(1, int))
        En este caso t1 será asignado y 1 será valor
        t1 = a
        Instruccion = Asignacion(Identificador('t1'), Identificador('a'))
        Aquí t1 es asignado y a (Identificador) es valor
        t1 = t2 * 4
        Instruccion = Asignacion(Identificador('t1'), Operacion(Identificador('t2'), Valor(4, int), OP_ARITMETICO.MULTIPLICACION))
        En este caso Tx = t1 y Valor = Operacion(t2, 4, OP_ARITMETICA.MULTIPLICACION)
        t1 = 'valor'
        Instruccion = Asignacion(Identificador('t1'), Valor('valor', cadena))
        stack[p] = "Hola"
        Instruccion = Asignacion(Arreglo(Identificador("stack"), Identificador("p")), Valor("Hola", "STRING"))
        t1 = h[0]
        '''

    def __str__(self):
        return str(self.Tx) + " = " + str(self.Valor)

class Arreglo:
    def __init__(self, identificador, posicion):
        self.Identificador = identificador #Identificador del arreglo
        self.Posicion = posicion #Posicion que ocupa (puede ser un Identificador o Valor)
        '''
        Ejemplo:
        stack[p] = "Hola"
        Arreglo(Identificador("stack"), Identificador("p"))
        '''

    def __str__(self):
        return str(self.Identificador) + "[" + str(self.Posicion) + "]"

class Etiqueta:
    def __init__(self, etiqueta):
        self.Etiqueta = etiqueta #Esta será una etiqueta que servirá para poder hacer saltos con goto
        '''
        Ejemplo:
        if x > 1 goto L1
        L1:'''
        #Instruccion = Etiqueta(Identificador('L1'))
        '''
        L1 es la etiqueta a guardar
        <codigo>
        '''

class SentenciaIF:
    def __init__(self, condicion, EtiquetaTrue):
        self.Condicion = condicion #Contendrá la condición a evaluar, puede ser Condicion, Valor o Identificador
        self.EtiquetaTrue = EtiquetaTrue #Representa la etiqueta al cual se le hará salto si la condición es verdadera
        '''
        if x == 1 goto L1
        goto L2'''
        #instruccion = SetenciaIF(Condicion('x', valor(1, int), Op_RELACIONAL.IGUAL), Identificador('L1'))
        #instruccionElse = Goto(Identificador('L2'))
        '''
        x == 1 es la condición Esto puede ir en texto o en una clase llamada condición que sería mas sencillo analizarlo
        Etiqueta True es L1
        goto L2 sería una instrucción goto aparte
        '''

class Goto:
    def __init__(self, Etiqueta):
        self.Etiqueta = Etiqueta
        '''
        Ejemplo
        goto L1
        Si viene un goto, se guardará en esta clase para poder identificar esta operación
        Instruccion = Goto(Indentificador('L1'))
        L1: 
        <codigo>
        '''
```
El optmizador no recibirá cadenas de texto o un archivo para que lo analice y lo optimice, sino que se le dará ya ordenado para así poder optimizarlo según las reglas que se definirán más adelante.

### 2 Analizador de texto en 3D
Como se vió previamente, el código 3 direcciones se genera en cierto formato, pero se genera en cadenas de texto, que serán enviadas a un archivo .py para su posterior ejecución.
Para que este 3d generado pueda ser optimizado, debe pasarse a los contenedores explicados en el punto anterior, que serían las clases 3d.

Para poder llevar a cabo esto, se creó un analizador con ply similar al de la fase 1, que convertirá en objetos cada orden y valores enviados en el texto del archivo c3d.py.

Primero el archivo lexico.
```
Se reconocen pocas reservadas, las cuales son:
'GOTO', 'IF', 'TRUE', 'FALSE'

los tokens se conforman por las palabras reservadas y por valores o símbolos
tokens = reservadas + (
    'DOS_PUNTOS', 'IGUAL', 'SUMA', 'RESTA', 'POTENCIA', 'POR', 'DIVISION',
    'ID', 'CADENA', 'ENTERO', 'DECIMAL', 'CARACTER',
    #Relacional
    'DIFERENTE', 'MAYOR', 'MENOR','MAYORIGUAL', 'MENORIGUAL', 'ESIGUAL'
    #Simbolos de agrupacion
    'CORIZQ', 'CORDER', 'PARIZQ', 'PARDER', 'PUNTO'
)
```

Estos lexemas serán enviados al analizador sintáctico que está bajo el nombre de SintRecolector3D.py. El cual tendrá las siguientes producciones.
```
init   : instrucciones
instrucciones  : instrucciones instruccion
instrucciones  : instruccion
instruccion    : ID IGUAL valor
instruccion    : ID CORIZQ ID CORDER IGUAL valo
instruccion    : ID PARIZQ PARDER
instruccion    : IF condicion GOTO ID
instruccion    : GOTO ID
instruccion    : ID DOS_PUNTOS
valor  : valorOp SUMA valorOp
valor  : valorOp RESTA valorOp
valor  : valorOp POR valorOp
valor  : valorOp DIVISION valorOp
valor  : valorOp POTENCIA valorOp
valor  : condicion
valor  : valorOp
valor      : RESTA valorOp %prec UMENOS
valorOp    : CADENA
valorOp    : ENTERO
valorOp    : DECIMAL
valorOp    : CARACTER
valorOp    : ID
valorOp      : TRUE
                    | FALSE
valorOp  : CORIZQ valorOp CORDER
condicion  : valorOp MAYOR valorOp
condicion  : valorOp MENOR valorOp
condicion  : valorOp MAYORIGUAL valorOp
condicion  : valorOp MENORIGUAL valorOp
condicion  : valorOp ESIGUAL valorOp
condicion  : valorOp DIFERENTE valorOp
```

## Optimización de código 3 direcciones.
Para la optimización del código 3 direcciones, se utilizaron las reglas de optimización por mirilla. Esta optimización consta de 18 reglas.

#### Regla 1
Si existe una asignación de valor de la forma a = b y posteriormente existe una asignación de forma b = a, se eliminará la segunda asignación siempre que a no haya cambiado su valor. Se deberá tener la seguridad de que no exista el cambio de valor y no existan etiquetas entre las 2 asignaciones:
```
Ejemplo: 
t2 = b;
b = t2
Optimizado
t2 = b;
```
En el código esta regla es así:
```
def regla1(self, pila, operacion, indice):
        if type(operacion.Valor) == C3D.Identificador:
            '''
            Entonces estamos agregando una variable
            Debemos recorrer la pila para revisar si esiste un caso como el siguiente
            a=b y luego más adelante b=a
            En caso de existir, debemos revisar si a no cambió de valor entre ambas operaciones
            O si es que no hay etiquetas entre ambas operaciones
            En caso de que ninguna de las 2 condiciones anteriores se cumpla, se debe borrar b=a de la pila            
            '''
            indiceAux = 0
            reporte = []
            for elemento in pila:
                #primero nos posicionamos sobre la operación asignación que nos mandaron para empezar a comparar
                if indiceAux > indice:
                    #ya aquí dentro podemos revisar
                    #primero confirmamos que sea una asignación ya que estamos buscando si a cambió de valor
                    if type(elemento) == C3D.Etiqueta:
                        #Si pasa esto, se romple la segunda condición, así que salimos
                        #antes de salir, debemos confirmar el guardado en nuestra lista optimizada
                        self.ListaOptimizada.append(operacion)
                        return
                    if type(elemento) == C3D.Asignacion:
                        if elemento.Tx.Id == operacion.Tx.Id:
                            '''
                            Si esto ocurre, quiere decir que se rompe la primera condición por lo que
                            devolvemos la operación tal cual se nos fue entregada.
                            '''
                            self.ListaOptimizada.append(operacion)
                            return
                        #Si la condición de arriba no se cumple, seguimos analizando
                        if type(elemento.Valor) == C3D.Identificador:
                            #Si esto se valida, quiere decir que encontramos una asiganción de variable a otra
                            if elemento.Valor.Id == operacion.Tx.Id:
                                #Si entramos aquí quiere decir que cumple las condiciones para ser optimizado
                                #Indicamos que esta línea de código es inutil, y seguimos nuestro análisis en busca de otros puntos similares
                                termino = elemento.Tx.Id + ' = ' + str(elemento.Valor.Id)
                                optimizado = 'Se elimina la instrucción'
                                self.reporteOptimizado.append(["Regla 1", termino, optimizado, str(indiceAux + 1)])
                                self.ElementosIgnorar.append(indiceAux)
                indiceAux += 1
            #Si llegamos a este punto quiere decir que ninguno de los puntos return se cumple y que terminamos la búsqueda.
            self.ListaOptimizada.append(operacion)
```

#### Regla 2.
Si existe un salto condicional de la forma Lx y exista una etiqueta Lx:, todo código contenido entre el goto Lx y la etiqueta Lx, podrá ser eliminado siempre y cuando no exista una etiqueta en dicho código:
```
Ejemplo:
goto L1;
<instrucciones>
L1:
Optimizado
L1:
```
En el código esta regla está hecha así:
```
def regla2(self, pila, operacion, indice):
        #Debemos recorrer la pila desde esta sentencia hasta encontrar una etiqueta.
        posiblesIgnorados = []
        indiceAux = 0
        reportado = []
        for elementos in pila:
            if indiceAux > indice:
                #Aquí ya estamos más adelante que nuestra orden anterior.
                if type(elementos) == C3D.Etiqueta:
                    #En este momento encontramos una etiqueta después del goto
                    #debemos revisar si es el mismo nombre de etiqueta Lx con el Goto Lx
                    if elementos.Etiqueta.Id == operacion.Etiqueta.Id:
                        #Entonces el goto Lx y la etiqueta Lx son las mismas, se puede simplificar
                        if len(posiblesIgnorados) > 0:
                            for ignorados in posiblesIgnorados:
                                self.ElementosIgnorar.append(ignorados)
                                #print(pila[posiblesIgnorados[len(posiblesIgnorados)-1]])
                                reportado.append(ignorados)
                        #self.ListaOptimizada.append(operacion)
                        termino = ''
                        for indizu in reportado:
                            termino = termino + self.Imprimir(pila[indizu]) + '\n'
                        optimizado = 'Se eliminan las instrucciones'
                        self.reporteOptimizado.append(["Regla 2", termino, optimizado, str(indiceAux + 1)])
                        return
                    else:
                        #Quiere decir que encontramos una etiqueta Ly, por lo que no puede ser reducido
                        self.ListaOptimizada.append(operacion)
                        return
                else:
                    #Si aun no hemos salido del método y encontramos código, este codigo debe ignorarse
                    posiblesIgnorados.append(indiceAux)
            indiceAux += 1
        self.ListaOptimizada.append(operacion)
        return
```

#### Regla 3.
Si existe un alto condicional de la forma if <cond> goto Lv; goto Lf; inmediatamente después de sus etiquetas Lv: <instrucciones> Lf: se podrá reducir el número de saltos negando la condición, cambiando el salto condicional hacia la etiqueta falsa Lf: y eliminando el salto condicional innecesario a goto Lf y quitando la etiqueta Lv:
```
Ejemplo:
if a == 10 goto L1;
goto L2;
L1:
<instrucciones>
L2:
Optimizado:
if a != 10 goto L2;
<instrucciones>
L2:
```
En codigo esta regla está hecha así:
```
def regla3(self, pila, operacion, indice):
        if len(pila)>indice+1 and type(pila[indice+1]) == C3D.Goto:
            #En este paso la primera condición de la regla3 existe (goto lf luego del if lx)
            if len(pila)>indice+2 and type(pila[indice+2]) == C3D.Etiqueta and pila[indice+2].Etiqueta.Id == operacion.EtiquetaTrue.Id:
                #Si entramos aquí se cumple la segunda condición que lx: <codigo> esté inmediatamente después del goto lf
                #Primero cambiamos la condición para aceptar lo que antes era falso
                NuevaCondicion = self.CambiarComparador(operacion.Condicion)
                #Ahora debemos primero almacenar el goto del if y luego cambiarlo por el de abajo
                termino = 'if ' + self.ImprimirCondicional(operacion.Condicion) + ' goto ' + operacion.EtiquetaTrue.Id + '\ngoto ' + pila[indice + 1].Etiqueta.Id
                operacion.EtiquetaTrue.Id = pila[indice+1].Etiqueta.Id
                operacion.Condicion = NuevaCondicion
                optimizado = 'if ' + self.ImprimirCondicional(NuevaCondicion) + ' goto ' + pila[indice + 1].Etiqueta.Id
                self.reporteOptimizado.append(["Regla 3", termino, optimizado, str(indice + 1)])
                self.ElementosIgnorar.append(indice+1)
                #Ahora agregamos la nueva sentencia if al codigo optimizado
                self.ListaOptimizada.append(operacion)
                #Y ahora debemos buscar y agregar el código de la etiqueta que se extrajo de la sentencia if anterior
                for indiceaux in range(indice+2, len(pila)):
                    if type(pila[indiceaux]) == C3D.Etiqueta or type(pila[indiceaux]) == C3D.SentenciaIF:
                        #Quiere decir que encontramos otra etiqueta, if o goto que hace que nuestro bloque termine
                        return
                    else:
                        self.ListaOptimizada.append(pila[indiceaux])
                        self.ElementosIgnorar.append(indiceaux)
            else:
                self.ListaOptimizada.append(operacion)
        else:
            self.ListaOptimizada.append(operacion)
```

#### Regla 4.
Si se utilizan valores constantes dentro de las condiciones de la forma if <cond> goto Lv; goto Lf; y el resultado de la condición es una constante verdadera, se podrá transformar en un salto incondicional y eliminarse el salto hacia la etiqueta falsa Lf:
```
Ejemplo:
if 1 == 1 goto L1;
goto L2;
Optimizado:
goto L1;
```

#### Regla 5.
Si se utilizan valores constantes dentro de las condiciones de la forma if <cond> goto Lv; goto Lf; y el resultado de la condición es una constante falsa, se podrá transformar en un salto incondicional y eliminarse el salto hacia la etiqueta verdadera Lv.
```
Ejemplo:
if 1 == 0 goto L1;
goto L2;
Optimizado:
goto L2;
```
En el código, la regla 4 y 5 están de hechos en el mismo módulo de esta manera.
```
def regla4y5(self, pila, operacion, indice):
        if type(operacion.Condicion.Op1) == C3D.Valor and type(operacion.Condicion.Op2) == C3D.Valor:
            #Significa que ambos elementos a comparar son constantes. por lo que se cumple parte de la regla 4
            if self.ejecutarComparacion(operacion.Condicion.Op1.Valor, operacion.Condicion.Operador, operacion.Condicion.Op2.Valor):
                print('regla 4')
                termino = 'if ' + self.ImprimirCondicional(operacion.Condicion) + ' goto ' + operacion.EtiquetaTrue.Id
                self.ElementosIgnorar.append(indice)
                if len(pila) > indice+1 and type(pila[indice+1]) == C3D.Goto:
                    termino = termino + 'goto ' +pila[indice+1].Etiqueta.Id
                    self.ElementosIgnorar.append(indice+1)
                nuevaOrden = C3D.Goto(C3D.Identificador(operacion.EtiquetaTrue.Id))
                optimizado = 'goto ' + nuevaOrden.Etiqueta.Id
                self.reporteOptimizado.append(["Regla 4", termino, optimizado, str(indice + 1)])
                self.ListaOptimizada.append(nuevaOrden)
                return
            else:
                print('regla 5')
                self.ElementosIgnorar.append(indice)
                if len(pila)>indice+1 and type(pila[indice+1]) == C3D.Goto:
                    termino = 'if ' + self.ImprimirCondicional(operacion.Condicion) + ' goto ' + operacion.EtiquetaTrue.Id
                    termino = termino + 'goto ' + pila[indice +1].Etiqueta.Id
                    self.ElementosIgnorar.append(indice+1)
                    nuevaOrden = C3D.Goto(C3D.Identificador(pila[indice+1].Etiqueta.Id))
                    self.ListaOptimizada.append(nuevaOrden)
                    optimizado = 'goto ' + nuevaOrden.Etiqueta.Id
                    self.reporteOptimizado.append(["Regla 5", termino, optimizado, str(indice + 1)])
```

#### Regla 6.
Si existe un salto incondicional de la forma goto Lx donde existe la etiqueta Lx: y la primera instrucción, luego de la etiqueta, es otro salto, de la forma goto Ly; se podrá realizar la modificación al primer salto para que sea dirigido hacia la etiqueta Ly: , para omitir el salto condicional hacia Lx.
```
Ejemplo:
goto L1;
<instrucciones>
L1:
goto L2;
Optimizado:
goto L2:
<instrucciones>
L1:
goto L2;
```
En el código, la regla está hecha así:
```
def regla6(self, pila, operacion, indice):
        #En esta versión de la regla, debemos averiguar si la etiqueta Lx del goto tiene un salto inmediato
        EtiquetaGoto = operacion.Etiqueta.Id
        #Buscamos la etiqueta Lx
        for indiceAux in range(0, len(pila)):
            if type(pila[indiceAux]) == C3D.Etiqueta and pila[indiceAux].Etiqueta.Id == EtiquetaGoto:
                #Encontramos la etiqueta ahora debemos verifiar si tiene un salto goto Ly
                if len(pila) > indiceAux + 1 and type(pila[indiceAux + 1]) == C3D.Goto:
                    #si esto ocurre ya tenemos un salto de goto Ly, por lo que hay que cambiar la etiqueta Lx del goto anterior
                    termino = 'goto ' + EtiquetaGoto
                    optimizado = '\ngoto ' + pila[indiceAux+1].Etiqueta.Id
                    self.reporteOptimizado.append(["Regla 6", termino, optimizado, str(indice + 1)])
                    NuevaEtiqueta = pila[indiceAux+1].Etiqueta.Id
                    return NuevaEtiqueta
                else:
                    #Si no es así, entonces no hay necesidad de cambiar nada, y la etiqueta del goto es la misma
                    return EtiquetaGoto
        #Si llegamos a este punto, quiere decir que no encontramos ninguna etiqueta con el valor del goto, por lo que no cambiamos nada
        return EtiquetaGoto
```

#### Regla 7.
Si existe un salto incondicional de la forma if <cond> goto Lx; y existe la etiqueta Lx: y la primera instrucciones luego de la etiqueta es otro salto, de la forma goto Ly; se podrá realizar la modificación al primer salto para que sea dirigido hacia la etiqueta Ly: , para omitir el salto condicional hacia Lx:
```
Ejemplo:
if t9 >= t10 goto L1;
<instrucciones>
L1:
goto L2;
Optimizado:
if t9 >= t10 goto L2;
<instruciones>
L1:
goto L2;
```
En el código, esta regla está hecha así:
```
def regla7(self, pila, operacion, indice):
        #En esta versión de la regla, debemos averiguar si el goto Lx del if lleva a algúna etiqueta con Lx: con salto inmediato goto Ly
        EtiquetaGoto = operacion.EtiquetaTrue.Id
        #Buscamos le etiqueta Lx
        for indiceAux in range (0, len(pila)):
            if type(pila[indiceAux]) == C3D.Etiqueta and pila[indiceAux].Etiqueta.Id == EtiquetaGoto:
                #Encontramos la etiqueta ahora debemos verificar si tiene un salto goto Ly
                if len(pila) > indiceAux + 1 and type(pila[indiceAux + 1]) == C3D.Goto:
                    #si esto ocurre, ya tenemos un salto de goto Ly, por lo que hay que cambiar la etiqueta Ly del if
                    termino = 'if ' + self.ImprimirCondicional(operacion.Condicion) + ' goto ' + operacion.EtiquetaTrue.Id
                    optimizado = 'if ' + self.ImprimirCondicional(operacion.Condicion) + ' goto ' + pila[indiceAux + 1].Etiqueta.Id
                    self.reporteOptimizado.append(["Regla 7", termino, optimizado, str(indice + 1)])
                    NuevaEtiqueta = pila[indiceAux+1].Etiqueta.Id
                    return NuevaEtiqueta
                else:
                    #Si no es así, entonces no hay necesidad de cambiar nada, y la etiqueta del if goto es la misma
                    return EtiquetaGoto
        #Si llegamos a este punto, no encontramos ninguna etiqueta con el valor del goto, por lo que no cambiamos nada.
        return EtiquetaGoto
```

#### Regla 8 a la 11.
Estas reglas son simplificaciones algebráicas. Donde si las operaciones presentan una suma con cero, resta con cero, división o multiplicación con 1, se eliminan, ya que no cambia el resultado.
```
Ejemplo:
x = x - 0
x = x + 0
x = x * 1
x = x / 1
Optimizado
se eliminan esas instrucciones.
```
En el código estas reglas se presentan así:
```
def regla8_9(self,operacion,indice):
        if type(operacion.Valor) == C3D.Operacion:
            asignado = self.verificaValor(operacion.Tx)
            op1 = self.verificaValor(operacion.Valor.Op1)
            op2 = self.verificaValor(operacion.Valor.Op2)
            operador = operacion.Valor.Operador
            if (asignado == op1) and (operador == C3D.OP_ARITMETICO.SUMA) and (op2 == '0'):
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " + " + op2
                optimizado = "Se elimina la instruccion"
                self.reporteOptimizado.append(["Regla 8", termino, optimizado, str(indice + 1)])
                return True
            elif (asignado == op2) and (operador == C3D.OP_ARITMETICO.SUMA) and (op1 == '0'):
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " + " + op2
                optimizado = "Se elimina la instruccion"
                self.reporteOptimizado.append(["Regla 8", termino, optimizado, str(indice + 1)])
                return True
            elif (asignado == op1) and (operador == C3D.OP_ARITMETICO.RESTA) and (op2  == '0'):
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " - " + op2
                optimizado = "Se elimina la instruccion"
                self.reporteOptimizado.append(["Regla 9", termino, optimizado, str(indice + 1)])
                return True
            else:
                return False
        else:
            return False

    #Reglas 10 y 11, eliminacion de instruccion; multiplicando o dividiendo con 1
    def regla10_11(self,operacion,indice):
        if type(operacion.Valor) == C3D.Operacion:
            asignado = self.verificaValor(operacion.Tx)
            op1 = self.verificaValor(operacion.Valor.Op1)
            op2 = self.verificaValor(operacion.Valor.Op2)
            operador = operacion.Valor.Operador
            if (asignado == op1) and (operador == C3D.OP_ARITMETICO.MULTIPLICACION) and (op2  == '1'):
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " * " + op2
                optimizado = "Se elimina la instruccion"
                self.reporteOptimizado.append(["Regla 10", termino, optimizado, str(indice + 1)])
                return True
            elif (asignado == op2) and (operador == C3D.OP_ARITMETICO.MULTIPLICACION) and (op1 == '1'):
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " * " + op2
                optimizado = "Se elimina la instruccion"
                self.reporteOptimizado.append(["Regla 10", termino, optimizado, str(indice + 1)])
                return True
            elif (asignado == op1) and (operador == C3D.OP_ARITMETICO.DIVISION) and (op2  == '1'):
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " / " + op2
                optimizado = "Se elimina la instruccion"
                self.reporteOptimizado.append(["Regla 11", termino, optimizado, str(indice + 1)])
                return True
            else:
                return False
        else:
            return False
```

#### Regla 12 a la 15.
En el caso de estas reglas, son similares a las anteriores pero con la diferencia que esta vez se está igualando otra variable a la que se está operando.
```
Ejemplo:
x = y + 0
x = y - 0
x = y / 1
x = y * 1
Optimizado:
x = y
x = y
x = y
x = y
```
Em el código, estas reglas se presentan así
```
#Reglas 12 y 13, optimizacion de instruccion; sumando o restando con 0
    def regla12_13(self,operacion,indice):
        if type(operacion.Valor) == C3D.Operacion:
            asignado = self.verificaValor(operacion.Tx)
            op1 = self.verificaValor(operacion.Valor.Op1)
            op2 = self.verificaValor(operacion.Valor.Op2)
            operador = operacion.Valor.Operador
            if (asignado != op1) and (operador == C3D.OP_ARITMETICO.SUMA) and (op2  == '0'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),operacion.Valor.Op1)
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " + " + op2
                optimizado = asignado + " = " + op1
                self.reporteOptimizado.append(["Regla 12", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            elif (asignado != op2) and (operador == C3D.OP_ARITMETICO.SUMA) and (op1 == '0'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),operacion.Valor.Op2)
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " + " + op2
                optimizado = asignado + " = " + op2
                self.reporteOptimizado.append(["Regla 12", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            elif (asignado != op1) and (operador == C3D.OP_ARITMETICO.RESTA) and (op2  == '0'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),operacion.Valor.Op1)
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " - " + op2
                optimizado = asignado + " = " + op1
                self.reporteOptimizado.append(["Regla 13", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            else:
                return False
        else:
            return False

    #Reglas 14 y 15, optimizacion de instruccion; multiplicando o dividiendo con 1
    def regla14_15(self,operacion,indice):
        if type(operacion.Valor) == C3D.Operacion:
            asignado = self.verificaValor(operacion.Tx)
            op1 = self.verificaValor(operacion.Valor.Op1)
            op2 = self.verificaValor(operacion.Valor.Op2)
            operador = operacion.Valor.Operador
            if (asignado != op1) and (operador == C3D.OP_ARITMETICO.MULTIPLICACION) and (op2  == '1'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),operacion.Valor.Op1)
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " * " + op2
                optimizado = asignado + " = " + op1
                self.reporteOptimizado.append(["Regla 14", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            elif (asignado != op2) and (operador == C3D.OP_ARITMETICO.MULTIPLICACION) and (op1 == '1'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),operacion.Valor.Op2)
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " * " + op2
                optimizado = asignado + " = " + op2
                self.reporteOptimizado.append(["Regla 14", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            elif (asignado != op1) and (operador == C3D.OP_ARITMETICO.DIVISION) and (op2  == '1'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),operacion.Valor.Op1)
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " / " + op2
                optimizado = asignado + " = " + op1
                self.reporteOptimizado.append(["Regla 15", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            else:
                return False
        else:
            return False
```

#### Regla 16 a la 18
Estas 3 reglas son solo optimización en el costo de ejecución en algunos casos específicos de operaciones, solo haciendo más sencilla la ejecución de estos para la computadora.
```
Ejemplo:
x = y * 2
Optimizado:
x = y + y
Ejemplo:
x = y * 0
Optimizado:
x = 0
Ejemplo:
x = 0 / y
Optimizado:
x = 0
```
En el código estas reglas están hechas así:
```
#Regla 16, optimizacion de instruccion; convirtiendo multiplicacion * 2 a suma
    def regla16(self,operacion,indice):
        if type(operacion.Valor) == C3D.Operacion:
            asignado = self.verificaValor(operacion.Tx)
            op1 = self.verificaValor(operacion.Valor.Op1)
            op2 = self.verificaValor(operacion.Valor.Op2)
            operador = operacion.Valor.Operador
            if (operador == C3D.OP_ARITMETICO.MULTIPLICACION) and (op2  == '2' or op1 == '2'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),C3D.Operacion(operacion.Tx,operacion.Tx,C3D.OP_ARITMETICO.SUMA))
                #Generamos los datos para realizar el reporte de optimizacion
                termino = ""
                optimizado = ""
                if op1 == '2':
                    termino = asignado + " = " + op1 + " * " + op2
                    optimizado = asignado + " = " + op2 + " + " + op2
                elif op2 == '2':
                    termino = asignado + " = " + op1 + " * " + op2
                    optimizado = asignado + " = " + op1 + " + " + op1
                
                self.reporteOptimizado.append(["Regla 16", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            else:
                return False
        else:
            return False

    #Regla 17 y 18, optimizacion de instruccion; multiplicando o dividiendo con 0
    def regla17_18(self,operacion,indice):
        if type(operacion.Valor) == C3D.Operacion:
            asignado = self.verificaValor(operacion.Tx)
            op1 = self.verificaValor(operacion.Valor.Op1)
            op2 = self.verificaValor(operacion.Valor.Op2)
            operador = operacion.Valor.Operador
            if (operador == C3D.OP_ARITMETICO.MULTIPLICACION) and (op2  == '0' or op1 == '0'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),C3D.Valor(0, 'ENTERO'))
                #Generamos los datos para realizar el reporte de optimizacion
                termino = ""
                optimizado = ""
                if op1 == '0':
                    termino = asignado + " = " + op1 + " * " + op2
                    optimizado = asignado + " = " + op2
                elif op2 == '0':
                    termino = asignado + " = " + op1 + " * " + op2
                    optimizado = asignado + " = " + op1

                self.reporteOptimizado.append(["Regla 17", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            elif (operador == C3D.OP_ARITMETICO.DIVISION) and (op1 == '0'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),operador.Valor.Op1)
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " / " + op2
                optimizado = asignado + " = " + op1
                self.reporteOptimizado.append(["Regla 18", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            else:
                return False
        else:
            return False
```

