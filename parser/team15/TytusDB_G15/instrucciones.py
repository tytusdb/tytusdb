class Instruccion:
    ''' Esta sera la clase de Instrucciones '''

class Definicion(Instruccion):
    def __init__(self, tipo, id):
        self.tipo = tipo
        self.id = id

class CreateDatabase(Instruccion):
    def __init__(self, nombre, usuario, modo = 1):
        self.nombre = nombre
        self.usuario = usuario
        self.modo = modo

class LLave_Primaria(Instruccion):
    def __init__(self, id):
        self.id  = id

class Definicon_Foranea(Instruccion):
    def __init__(self, nombre_tabla, referencia_tabla , campo_referencia):
        self.nombre_tabla = nombre_tabla
        self.referencia_tabla = referencia_tabla
        self.campo_referencia = campo_referencia

class Definicion_check(Instruccion):
    def __init__(self, exp_logica = []):
        self.exp_logica = exp_logica

class Etiqueta_tipo(Instruccion):
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta

class Etiqueta_Interval(Instruccion):
    def __init__(self,ext_time, ext_time1,etiqueta):
        self.ext_time = ext_time
        self.ext_time1 = ext_time1
        self.etiqueta = etiqueta

class Create_Table(Instruccion):
    def __init__(self, id, herencia, instrucciones = []):
        self.id  = id
        self.herencia = herencia
        self.instrucciones = instrucciones

class Definicion_Columnas(Instruccion):
    def __init__(self, id, tipo_datos, etiqueta, id_referencia, opciones_constraint = []):
        self.id = id
        self.tipo_datos = tipo_datos
        self.etiqueta = etiqueta
        self.id_referencia = id_referencia
        self.opciones_constraint = opciones_constraint

class Lista_Parametros(Instruccion):
    def __init__(self ,identificadores = []):
        self.identificadores = identificadores

class definicion_constraint(Instruccion):
    def __init__(self, id, tipo , referencia,columna,opciones_contraint = []):
        self.id = id
        self.tipo = tipo
        self.referencia = referencia
        self.columna = columna
        self.opciones_constraint = opciones_contraint