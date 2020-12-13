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