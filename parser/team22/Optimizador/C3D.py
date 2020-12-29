#ESTA CLASE SERVIRÁ ÚNICAMENTE PARA HACER PRUEBAS PARA LA OPTIMIZACIÓN
#PERO ES UNA MUESTRA DE COMO SE ESTRUCTURARÁN LAS CLASES PARA ALMACENAR EL CÓDIGO 3D
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
        self.Tx = asignado #Este será el temporal o variable que almacenará lo que valor contenga
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
        t1 = h[0]
        '''

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