class Instruccion:
    '''This is an abstract class'''

class Crear_BD(Instruccion):
    '''
        Esta clase representa la instruccion de creacion de una BD.
        La instruccion Crear_BD unicamente tiene como parametro un identificador.
    '''
    def __init__(self, id, line, replace = False) :
        self.id = id
        self.replace = replace
        self.line = line

class Show_BD(Instruccion):
    '''
        Esta clase representa la instruccion de mostrar las BD.
    '''
    def __init__(self, line, like = '') :
        self.line = line
        self.like = like

class Alter_BD(Instruccion):
    '''
        Esta clase representa la instruccion de cambiar nombre de BD.
    '''
    def __init__(self, databaseOld, databaseNew, line) :
        self.databaseOld = databaseOld
        self.databaseNew = databaseNew
        self.line = line

class Drop_BD(Instruccion):
    '''
        Esta clase representa la instruccion de eliminar  BD.
    '''
    def __init__(self, database, line) :
        self.database = database
        self.line = line


class Cambio_BD(Instruccion):
    '''
        Esta clase representa la instruccion del Cambio de una BD.
        La instruccion Cambio_BD unicamente tiene como parametro un identificador.
    '''
    def __init__(self,  id, line) :
        self.id = id
        self.line = line

class Select(Instruccion):
    '''
        Esta clase representa la instruccion de select 
        El objeto es un diccionario con 'objeto' y 'alias'.
    '''
    def __init__(self, objeto, line) :
        self.objeto = objeto
        self.line = line


class Select_All(Instruccion):
    '''
        Esta clase representa la instruccion de Consulta general para tabla.
        La instruccion Select_All unicamente tiene como parametro un identificador.
    '''
    def __init__(self,  id) :
        self.id = id


class Delete_incondicional(Instruccion):
    '''
        Esta clase representa la instruccion de Delete general para tabla.
        La instruccion Delete_incondicional unicamente tiene como parametro un identificador.
    '''
    def __init__(self,  id) :
        self.id = id

class Delete_condicional(Instruccion) :
    '''
        Esta clase representa la instrucción Delete_incondicional.
    '''

    def __init__(self, expLogica, id) :
        self.expLogica = expLogica
        self.id = id

class FuncionTrigonometrica1(Instruccion) :
    '''
        Esta clase representa las funciones trigonométricas con 1 parámetro.
    '''

    def __init__(self, funcion, valor, line) :
        self.funcion = funcion
        self.valor = valor
        self.line = line

class FuncionTrigonometrica2(Instruccion) :
    '''
        Esta clase representa las funciones trigonométricas con 1 parámetro.
    '''

    def __init__(self, funcion, valor1, valor2, line) :
        self.funcion = funcion
        self.valor1 = valor1
        self.valor2 = valor2
        self.line = line

class FuncionAritmetica(Instruccion) :
    '''
        Esta clase representa las funciones aritmetica con 2 parámetros.
    '''

    def __init__(self, operacion, valor1, valor2, line) :
        self.operacion = operacion
        self.valor1 = valor1
        self.valor2 = valor2
        self.line = line

class FuncionMatematica1(Instruccion) :
    '''
        Esta clase representa las funciones matemáticas con 1 parámetro.
    '''

    def __init__(self, funcion, valor, line) :
        self.funcion = funcion
        self.valor = valor
        self.line = line

class Crear_TB_Herencia(Instruccion) :
    '''
        Esta clase representa la instrucción de Crear tabla con herencia.
        La instrucción Crear_TB_Herencia tiene 3 parámetros:
        id = identificador, nombre de la tabla.
        columnas = columnas que contendrá la tabla.
        idHerencia = identificador de la tabla que hereda parámetros y valores a esta.
    '''
    
    def __init__(self, id, columnas, idHerencia):
        self.id = id
        self.columnas = columnas
        self.idHerencia = idHerencia

class Crear_TB(Instruccion):
    '''
        Esta clase representa la instrucción de Crear tabla sin herencia
        La instrucción Crear_TB tiene 2 parámetros:
        id = identificador, nombre de la tabla.
        columnas = columnas que contendrá la tabla.
    '''

    def __init__(self, id, columnas, line):
        self.id = id
        self.columnas = columnas
        self.line = line

class Drop_TB(Instruccion):
    '''
        Esta clase representa la instruccion de eliminar TB.
    '''
    def __init__(self, table, line) :
        self.table = table
        self.line = line