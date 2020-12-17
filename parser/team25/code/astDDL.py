from enum import Enum

class IS(Enum):
    TRUE = 1
    FALSE = 2
    NULL = 3
    DISTINCT = 4
    UNKNOWN = 5
    
class ALTER_TABLE_DROP(Enum):
    COLUMN = 1
    CONSTRAINT = 2

class ALTER_TABLE_ADD(Enum):
    COLUMN = 1
    UNIQUE = 2
    FOREIGN_KEY = 3
    CHECKS = 4

class CONSTRAINT_FIELD(Enum):
    UNIQUE = 1
    PRIMARY_KEY = 2


# ------------------------ DDL ----------------------------
# Instruccion (Abstracta)
class Instruccion:
    def ejecutar(self):
        pass

    def dibujar(self):
        pass

# Create Database
class CreateDatabase(Instruccion):
    def __init__(self, nombre, reemplazo = False, existencia = False, duenio = None, modo = 0):
        self.nombre = nombre
        self.reemplazo = reemplazo
        self.existencia = existencia
        self.duenio = duenio
        self.modo = modo

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"CREATE DATABASE\" ];"

        if self.reemplazo:
            nodo += "\nREPLACE" + identificador + "[ label = \"OR REPLACE\" ];"
            nodo += "\n" + identificador + " -> REPLACE" + identificador + ";"

        nodo += "\nNAME" + identificador + "[ label = \"" + self.nombre + "\" ];"
        nodo += "\n" + identificador + " -> NAME" + identificador + ";"

        if self.existencia:
            nodo += "\nEXISTS" + identificador + "[ label = \"IF EXISTS\" ];"
            nodo += "\n" + identificador + " -> EXISTS" + identificador + ";"

        if self.duenio:
            nodo += "\nOWNER" + identificador + "[ label = \"OWNER\" ];"
            nodo += "\n" + identificador + " -> OWNER" + identificador + ";"
            nodo += "\nOWNERNAME" + identificador + "[ label = \""+ self.duenio + "\" ];"
            nodo += "\nOWNER" + identificador + " -> OWNERNAME" + identificador + ";"

        if self.modo > 0:
            nodo += "\nMODE" + identificador + "[ label = \"" + self.modo + "\" ];"
            nodo += "\n" + identificador + " -> MODE" + identificador + ";"

        return nodo

# Create Table
class CreateTable(Instruccion):
    def __init__(self, nombre, columnas, herencia = None):
        self.nombre = nombre
        self.columnas = columnas
        self.herencia = herencia

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"CREATE TABLE\" ];"
        nodo += "\n" + identificador + " -> NAME" + identificador +  "[ label=\"" + self.nombre + "\" ];\n//COLUMNAS DE LA TABLA" + identificador + "\n"

        for col in self.columnas:
            nodo += "\n" + identificador + " -> " + str(hash(col)) + ";"
            nodo += col.dibujar()

        if self.herencia:
            nodo += "\nINHERITS" + identificador +  "[ label=\"INHERITS\" ];"
            nodo += "\n" + identificador + " -> INHERITS" + identificador +  ";"
            nodo += "SUPER" + identificador +  "[ label=\"" + self.herencia + "\" ];"
            nodo += "\nINHERITS" + identificador + " -> SUPER" + identificador + ";"

        return nodo

# Alter Database
class AlterDatabase(Instruccion):
    def __init__(self, nombre, accion):
        self.nombre = nombre
        self.accion = accion

    def dibujar(self):
        identificador = str(hash(self))
        
        nodo = "\n" + identificador + "[ label = \"ALTER DATABASE\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.accion)) + ";"
        nodo += self.accion.dibujar()

        return nodo

# Alter Table
class AlterTable(Instruccion):
    def __init__(self, tabla, accion):
        self.tabla = tabla
        self.accion = accion

    def dibujar(self):
        identificador = str(hash(self))
        
        nodo = "\n" + identificador + "[ label = \"ALTER TABLE\" ];"

        nodo += "\nNAME" + identificador + "[ label = \"" + self.tabla + "\" ];"
        nodo += "\n" + identificador + " -> NAME" + identificador + ";"

        nodo += "\n" + identificador + " -> " + str(hash(self.accion)) + ";"
        nodo += self.accion.dibujar()

        return nodo

# Alter Field: Cambia al tipo varchar o cambia ser nulo
class AlterField(Instruccion):
    def __init__(self, campo, cantidad = None):
        self.campo = campo
        self.cantidad = cantidad

    def dibujar(self):
        identificador = str(hash(self))
        
        nodo = "\nNAME" + identificador + "[ label = \"" + self.campo + "\" ];"
        nodo += "\n" + identificador + " -> NAME" + identificador + ";"

        nodo += "\n" + identificador 

        if self.cantidad:
            nodo += "[ label = \"ALTER COLUMN TYPE\" ];"

            nodo += "\nTYPE" + identificador + "[ label = \"VARCHAR(" + self.cantidad + ")\" ];"
            nodo += "\n" + identificador + " -> TYPE" + identificador + ";\n"
        else:
            nodo += "[ label = \"ALTER COLUMN SET\" ];"

            nodo += "\nVALUE" + identificador + "[ label = \"NOT NULL\" ];"
            nodo += "\n" + identificador + " -> VALUE" + identificador + ";\n"

        return nodo


# Alter Tbale Drop: Encapsula tanto constraints como columna
class AlterTableDrop(Instruccion):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador

        if self.tipo == ALTER_TABLE_DROP.CONSTRAINT:
            nodo += "[ label = \"DROP CONSTRAINT\" ];"
        else:
            nodo += "[ label = \"DROP COLUMN\" ];"

        nodo += "\nNAME" + identificador + "[ label = \"" + self.nombre + "\" ];"
        nodo += "\n" + identificador + " -> NAME" + identificador + ";\n"

        return nodo        

# Alter add 
class AlterTableAdd(Instruccion):
    def __init__(self, nombre, tipo, accion = None):
        self.nombre = nombre
        self.tipo = tipo
        self.accion = accion

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador 

        if self.tipo == ALTER_TABLE_ADD.UNIQUE:
            nodo += "[ label = \"ADD UNIQUE\" ];"
            nodo += "\nNAME" + identificador + "[ label = \"" + self.nombre + "\" ];"
            nodo += "\n" + identificador + " -> NAME" + identificador + ";"
            nodo += "\nID" + identificador + "[ label = \"" + self.accion + "\" ];"
            nodo += "\n" + identificador + " -> ID" + identificador + ";\n"
        elif self.tipo == ALTER_TABLE_ADD.FOREIGN_KEY:
            nodo += "[ label = \"ADD FOREIGN KEY\" ];"
            for identificador in self.nombre:
                nodo += "\n" + identificador + " -> " + str(hash(identificador)) + ";"
                nodo += identificador.dibujar()            
            for identificador in self.accion:
                nodo += "\n" + identificador + " -> " + str(hash(identificador)) + ";"
                nodo += identificador.dibujar()
        elif self.tipo == ALTER_TABLE_ADD.CHECKS:
            nodo += "[ label = \"ADD CHECKS\" ]"
            nodo += "\nNAME" + identificador + "[ label = \"" + self.nombre + "\" ];"
            nodo += "\n" + identificador + " -> NAME" + identificador + ";"
            nodo += "\nACTION" + identificador + "[ label = \"" + self.accion + "\" ];"
            nodo += "\n" + identificador + " -> ACTION" + identificador + ";\n"
        else:
            nodo += "[ label = \"ADD COLUMN\" ];"
            nodo += "\nNAME" + identificador + "[ label = \"" + self.nombre + "\" ];"
            nodo += "\n" + identificador + " -> NAME" + identificador + ";"
            nodo += "\nTYPE" + identificador + "[ label = \"" + self.accion + "\" ];"
            nodo += "\n" + identificador + " -> TYPE" + identificador + ";\n"
        return nodo

# Show Database
class ShowDatabase(Instruccion):
    def __init__(self, db, like = None):
        self.db = db
        self.like = like

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"SHOW DATABASE\" ];"
        nodo += "\nNAME" + identificador + "[ label = \"" + self.db + "\" ];"
        nodo += "\n" + identificador + " -> NAME" + identificador + ";"
        if self.like:
            nodo += "\nLIKE" + identificador + "[ label = \"" + self.like + "\" ];"
            nodo += "\n" + identificador + " -> LIKE" + identificador + ";"
        return nodo

# Drop Database
class DropDatabase(Instruccion):
    def __init__(self, db, existencia = False):
        self.db = db
        self.existencia = existencia

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"DROP DATABASE\" ];"
        nodo += "\nNAME" + identificador + "[ label = \"" + self.db + "\" ];"
        nodo += "\n" + identificador + " -> NAME" + identificador + ";"
        if self.existencia:
            nodo += "\nLIKE" + identificador + "[ label = \"IF EXISTS\" ];"
            nodo += "\n" + identificador + " -> LIKE" + identificador + ";"
        return nodo

# Create Field
class CreateField(Instruccion):
    def __init__(self, nombre, tipo, atributos):
        self.nombre = nombre
        self.tipo = tipo
        self.atributos = atributos

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"NEW FIELD\" ];"
        nodo += "\nNAME" + identificador + "[ label = \"" + self.nombre + "\" ];"
        nodo += "\n" + identificador + " -> NAME" + identificador + ";\n//ATRIBUTOS DE CREAR UN CAMPO " + identificador + "\n"

        for atributo in self.atributos:
            nodo += "\n" + identificador + " -> " + str(hash(atributo))
            nodo += atributo.dibujar()

        nodo += "\n//FIN DE ATRIBUTOS DE CREAR CAMPO " + identificador + "\n"

        return nodo

# Default Field
class DefaultField(Instruccion):
    def __init__(self, valor):
        self.valor = valor

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"DEFAULT\" ];"
        nodo += "\nDEFAULT" + identificador + "[ label = \"" + self.valor + "\" ];"
        nodo += "\n" + identificador + " -> DEFAULT" + identificador + ";\n"

        return nodo

# Check Field
class CheckField(Instruccion):
    def __init__(self, condiciones, nombre = None):
        self.condiciones = condiciones
        self.nombre = nombre
    
    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"CHECK\" ];"

        if self.nombre:
            nodo += "\nNAME" + identificador + "[ label = \"" + self.nombre + "\" ];"
            nodo += "\n" + identificador + " -> NAME" + identificador + ";"

        for condicion in self.condiciones:
            nodo += "\n" + identificador + " -> " + str(hash(condicion)) + ";"
            nodo += condicion.dibujar()

        return nodo

# Constraint Field
class ConstraintField(Instruccion):
    def __init__(self, tipo, nombre = None):
        self.tipo = tipo
        self.nombre = nombre

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador

        if self.tipo == CONSTRAINT_FIELD.UNIQUE:
            nodo += "[ label = \"UNIQUE\" ];"
        else:
            nodo += "[ label = \"PRIMARY KEY\" ];"

        if self.nombre:
            nodo += "\nNAME" + identificador + "[ label = \"" + self.nombre + "\" ];"
            nodo += "\n" + identificador + " -> NAME" + identificador + ";"

        return nodo


# Constraint Multiple Fields: Comprende tanto Unique como Primary Key
class ConstraintMultipleFields(Instruccion):
    def __init__(self, tipo, lista):
        self.tipo = tipo
        self.lista = lista

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador

        if self.tipo == CONSTRAINT_FIELD.UNIQUE:
            nodo += "[ label = \"UNIQUE MULTIPLE\" ];"
        else:
            nodo += "[ label = \"PRIMARY KEY MULTIPLE\" ];"

        for item in self.lista:
            nodo += "\n" + identificador + " -> " + str(hash(item)) + ";"
            nodo += item.dibujar()

        return nodo
            

# Foreign Key Multiple Fields
class ForeignKeyMultipleFields(Instruccion):
    def __init__(self, listaPropia, otraTabla, listaOtraTabla):
        self.lista = listaPropia
        self.otraTabla = otraTabla
        self.listaOtraTabla = listaOtraTabla

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"FOREIGN KEY MULTIPLE\" ];"

        nodo += "\nLOCAL" + identificador + "[ label = \"LOCAL FIELDS\" ];"
        nodo += "\n" + identificador + " -> LOCAL" + identificador + ";"

        for item in self.lista:
            nodo += "\nLOCAL" + identificador + " -> " + str(hash(item)) + ";"
            nodo += item.dibujar()

        nodo += "\nFOREIGN" + identificador + "[ label = \"" + self.otraTabla + " FIELDS\" ];"
        nodo += "\n" + identificador + " -> FOREIGN" + identificador + ";"

        for item in self.listaOtraTabla:
            nodo += "\nFOREIGN" + identificador + " -> " + str(hash(item)) + ";"
            nodo += item.dibujar()

        return nodo

# Check Multiple Fields
class CheckMultipleFields(Instruccion):
    def __init__(self, tipo, condiciones):
        self.tipo = tipo
        self.condiciones = condiciones

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"CHECK MULTIPLE\" ];"

        for condicion in self.condiciones:
            nodo += "\n" + identificador + " -> " + str(hash(condicion)) + ";"
            nodo += condicion.dibujar()

        return nodo
