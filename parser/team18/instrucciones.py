class Instruccion:
    '''This is an abstract class'''

class Imprimir(Instruccion) :
    '''
        Esta clase representa la instrucción imprimir.
        La instrucción imprimir únicamente tiene como parámetro una cadena
    '''

    def __init__(self,  cad) :
        self.cad = cad


class CrearBD(Instruccion) :
    '''
        Esta clase representa la funcion para crear una base de datos solo recibe el nombre de la BD
    '''
    def __init__(self,reemplazar,verificacion,nombre, propietario, modo) :
        self.reemplazar = reemplazar
        self.verificacion = verificacion
        self.nombre = nombre 
        self.propietario = propietario
        self.modo = modo


class CrearTabla(Instruccion) :
    '''
        Esta clase representa la instrucción crear tabla.
        La instrucción crear tabla recibe como parámetro nombre de tabla, lista de columnas y una tabla padre
    '''

    def __init__(self, nombre, padre, columnas = []) :
        self.nombre = nombre
        self.columnas = columnas
        self.padre = padre

class CrearType(Instruccion) :
    '''
        Esta clase representa la instrucción crear tipo.
        La instrucción crear tipo recibe como parámetro nombre del tipo, lista de valores
    '''

    def __init__(self, nombre, valores = []) :
        self.nombre = nombre
        self.valores = valores


class EliminarTabla(Instruccion) :
    '''
        Esta clase representa la instrucción drope table.
        La instrucción drope table recibe como parámetro la existencia y el nombre
    '''

    def __init__(self, existencia, nombre) :
        self.nombre = nombre
        self.existencia = existencia        

class EliminarDB(Instruccion) :
    '''
        Esta clase representa la instrucción drope database.
        La instrucción drope database recibe como parámetro la existencia y el nombre
    '''

    def __init__(self, existencia, nombre) :
        self.nombre = nombre
        self.existencia = existencia    

class columnaTabla(Instruccion) :
    '''
        Esta clase las columnas de una tabla
    '''

    def __init__(self, id, tipo, valor,zonahoraria, atributos = []) :
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.zonahoraria = zonahoraria
        self.atributos = atributos   


class llaveTabla(Instruccion) :
    '''
        Esta clase representa las llaves de una tabla ya sean foraneas o primarias
        Tipo= Primaria=True
        Tipo= Foreing=False
    '''
    def __init__(self, tipo,referencia,columnas = [],columnasRef = []) :
        self.tipo = tipo
        self.referencia = referencia
        self.columnas = columnas
        self.columnasRef = columnasRef

class atributoColumna(Instruccion) :
    '''
        Esta clase representa los atributos de una columna
    '''
    def __init__(self, default,constraint,null,unique,primary,check) :
        self.default = default
        self.constraint = constraint
        self.null = null
        self.unique = unique
        self.primary = primary
        self.check = check

class Insertar(Instruccion):
    '''
        Estan clase representa los valores a insertar en una tabla
    '''
    def __init__(self, nombre, valores=[]) :
        self.nombre = nombre
        self.valores = valores

class Actualizar(Instruccion):
    '''
        Esta clase representa los valores a actualizar de la tabla
    '''
    def __init__(self, nombre, condicion, valores=[]) :
        self.nombre = nombre
        self.condicion = condicion
        self.valores = valores

class columna_actualizar(Instruccion):
    '''
        Esta clase representa las columnas a actualizar
    '''
    def __init__(self, nombre, valor) :
        self.nombre = nombre
        self.valor = valor

class Eliminar(Instruccion): 
    '''
        Esta clase representa la eliminacion de una tabla 
    '''
    def __init__(self, nombre, condicion):
        self.nombre = nombre
        self.condicion = condicion

class DBElegida(Instruccion):
    '''
        Esta clase representa la base de datos elegida
    '''
    def __init__(self,nombre):
        self.nombre = nombre

class MostrarDB(Instruccion):
    '''
        Esta clase representa las base de datos creadas
    '''
