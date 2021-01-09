#se copian las tablas de las bases aqui


class Tabla(object):
    def __init__(self, basedatos,nombre,columna,modo):
        self.base=basedatos #nombre base
        self.tabla = nombre   #nombre tabla
        self.columnas = columna  #numero de columnas
        self.modo=modo   #modo en que se guardo la tabla b 
        self.pk=None  # pk de la tabla
        self.fk=None  # fk de la tabla
        self.datos=[] #las tablas que se guardan  abajo se muestra como se guardo
        self.codificado=[]  # datos de tuplas codificadas
        self.compreso = False

    def __str__(self) -> str:
        return f" MODOTABLA {self.modo} nombreBase {self.base} NOmbreTabla {self.tabla} Ncol {self.columnas}  PK {self.pk}  FK {self.fk} tuplas {self.datos} "


class Base(object):
    def __init__(self, basedatos,modo,encoding):
       self.base=basedatos
       self.modo=modo
       self.encoding=encoding
       self.index=[]
       self.compreso = False

    def __str__(self) -> str:
        return f" Base {self.base}  modo {self.modo}  encoding {self.encoding}  {self.index}"


class indices(object):
    def __init__(self, basedatos,modo):
       self.base=basedatos
       self.modo=modo

    def __str__(self) -> str:
        return f" Base {self.base}  modo {self.modo}  "


