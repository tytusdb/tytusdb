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
    def __init__(self, nombre, columnas, valores=[]) :
        self.nombre = nombre
        self.columnas = columnas
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

class Limite_Select(Instruccion):
    '''
        Esta clase representa el limit del select
    '''
    def __init__(self, select, limit, offset):
        self.select=select
        self.limit=limit
        self.offset=offset

class SELECT(Instruccion):
    '''
        Esta clase representa a una select
    '''
    def __init__(self, cantidad, parametros, cuerpo, funcion_alias):
        self.cantida=cantidad
        self.parametros=parametros
        self.cuerpo=cuerpo
        self.funcion_alias=funcion_alias

class Funcion_Alias(Instruccion):
    '''
        Esta clase representa un funcion junto a su alias
    '''
    def __init__(self, nombre, alias):
        self.nombre=nombre
        self.alias=alias

class CUERPO_SELECT(Instruccion):
    '''
        Esta clase representa el cuerpo de un select
    '''
    def __init__(self, b_from, b_join, b_where, b_group, b_having, b_order):
        self.b_from=b_from
        self.b_join=b_join
        self.b_where=b_where
        self.b_group=b_group
        self.b_having=b_having
        self.b_order=b_order

class Orden_Atributo(Instruccion):
    '''
        Esta clase representa el orden que tendra el atributo
    '''
    def __init__(self, nombre, direccion, rango):
        self.nombre=nombre
        self.direccion=direccion
        self.rango=rango

class SubQuery(Instruccion):
    '''
        Esta clase representa a una subquery y su comparacion con la query principal
    '''
    def __init__(self, condicion, subquery, alias):
        self.condicion=condicion
        self.subquery=subquery
        self.alias=alias

class Valor_From(Instruccion):
    '''
        Esta clase representa el contenido del from de una consulta
    '''
    def __init__(self, nombre, subquery, alias):
        self.nombre=nombre
        self.subquery=subquery
        self.alias=alias

class SubQuery_IN(Instruccion):
    '''
        Esta clase representa el si se declara un in o not in en subquery
    '''
    def __init__(self, exp, tipo):
        self.exp=exp
        self.tipo=tipo

class Valor_Select(Instruccion):
    '''
        Esta clase representa los valores para un select
    '''
    def __init__(self, nombre, tipo, alias, fun_exp):
        self.nombre=nombre
        self.tipo=tipo
        self.alias=alias
        self.fun_exp=fun_exp

class Condicion_WHEN_THEN(Instruccion):
    ''' 
        Esta clase representa la condicion when then 
    '''
    def __init__(self, exp, resultado):
        self.exp=exp
        self.resultado=resultado

class Case(Instruccion):
    '''
        Esta clase representa la un case
    '''
    def __init__(self, condicion, sino, alias):
        self.condicion=condicion
        self.sino=sino
        self.alias=alias
