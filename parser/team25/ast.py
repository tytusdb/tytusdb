from enum import Enum

# Enumeraciones para identificar expresiones que comparten clase
class OPERACION_ARITMETICA(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDO = 4

class OPERACION_LOGICA(Enum):
    MAYORIGUAL = 1
    MENORIGUAL = 2
    MAYOR = 3
    MENOR = 4
    IGUAL = 5
    DESIGUAL = 6

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

class COMBINE_QUERYS(Enum):
    UNION = 1
    INTERSECT = 2
    EXCEPT = 3

class JOIN(Enum):
    INNER = 1
    LEFT = 2
    RIGHT = 3
    FULL = 4

# ------------------------ EXPRESIONES ----------------------------
# ------EXPRESIONES NUMERICAS

# Clase de expresion númerica (Abstracta)
class ExpresionNumerica:
    def dibujar(self):
        pass

# Clase de expresión aritmética
class ExpresionAritmetica(ExpresionNumerica):
    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"" + self.operador + "\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp1)) + ";"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp2)) + ";\n"

        nodo += self.exp1.dibujar()
        nodo += self.exp2.dibujar()

        return nodo
        
# Clase de expresión negativa
class ExpresionNegativa(ExpresionNumerica):
    def __init__(self, exp):
        self.exp = exp

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"-\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp)) + ";\n"

        nodo += self.exp.dibujar()

        return nodo

class ExpresionPositiva(ExpresionNumerica):
    def __init__(self, exp):
        self.exp = exp

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"+\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp)) + ";\n"

        nodo += self.exp.dibujar()

        return nodo

# Clase de expresión numero
class ExpresionNumero(ExpresionNumerica):
    def __init__(self, val):
        self.val = val

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"" + str(self.val) + "\" ];\n"

        return nodo

# ------FUNCIONES NUMERICAS (EXPRESIONES NUMERICAS)
class FuncionNumerica(ExpresionNumerica):
    def __init__(self, funcion, parametro1 = None, parametro2 = None):
        self.parametro1 = parametro1
        self.parametro2 = parametro2
        self.funcion = funcion

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"" + self.funcion + "\" ];"

        # Retorno
        if self.parametro1:
            nodo += "\n" + identificador + " -> " + str(hash(self.parametro1)) + ";"
            nodo += self.parametro1.dibujar()
        if self.parametro2:
            nodo += "\n" + identificador + " -> " + str(hash(self.parametro2)) + ";"
            nodo += self.parametro2.dibujar()

        return nodo

# ------EXPRESIONES LOGICAS

# Clase de expresión lógica (Abstracta)
class ExpresionLogica:
    def dibujar(self):
        pass

# Expresión binaria de comparacion
class ExpresionComparacion(ExpresionLogica):
    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"" + self.operador + "\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp1)) +";"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp2)) + ";\n"

        nodo += self.exp1.dibujar()
        nodo += self.exp2.dibujar()

        return nodo

# Expresion negada
class ExpresionNegada(ExpresionLogica):
    def __init__(self, exp):
        self.exp = exp

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"NOT\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp)) + ";\n"

        nodo += self.exp.dibujar()

        return nodo

# Expresión booleana (Valor puro)
class ExpresionBooleano(ExpresionLogica):
    def __init__(self, val):
        self.val = val

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"" + str(self.val) + "\" ];\n"

        return nodo

# Expresión Between: Contempla tanto al Between como al Between Symmetric, asi como las versiones negadas
class ExpresionBetween(ExpresionLogica):
    def __init__(self, evaluado, limiteInferior, limiteSuperior, invertido = False, simetria = False):
        self.evaluado = evaluado
        self.limiteInferior = limiteInferior
        self.limiteSuperior = limiteSuperior
        self.invertido = invertido
        self.simetria = simetria

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador

        if self.simetria:
            if self.invertido:
                nodo += "[ label = \"NOT BETWEEN SYMMETRIC\" ];"
            else:
                nodo += "[ label = \"BETWEEN SYMMETRIC\" ];"
        else:
            if self.invertido:
                nodo += "[ label = \"NOT BETWEEN\" ];"
            else:
                nodo += "[ label = \"BETWEEN\" ];"

        nodo += "\nAND" + identificador + "[ label = \"AND\" ];"
        nodo += "\n" + identificador + " -> AND" + identificador + ";"

        nodo += "\n" + identificador + " -> " + str(hash(self.evaluado)) + ";"
        nodo += self.evaluado.dibujar()
        
        nodo += "\nAND" + identificador + " -> " + str(hash(self.limiteInferior)) + ";"
        nodo += self.limiteInferior.dibujar()

        nodo += "\nAND" + identificador + " -> " + str(hash(self.limiteSuperior)) + ";"
        nodo += self.limiteSuperior.dibujar()

        return nodo

# Expresión is: Contempla todas su variaciones
class ExpresionIs(ExpresionLogica):
    def __init__(self, condicion, tipo, invertido = False, subcondicion = None):
        self.condicion = condicion
        self.invertido = invertido
        self.subcondicion = subcondicion

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador

        return nodo

# ------EXPRESIONES DE CADENAS
class ExpresionString:
    def dibujar(self):
        pass

class ExpresionCadena(ExpresionString):
    def __init__(self, valor):
        self.val = valor
    
    def dibujar(self):
        identificador = str(hash(self))
        temp = str(self.val)
        
        temp = temp.replace("\"", "")
        temp = temp.replace("\'", "")

        nodo = "\n" + identificador + "[ label =\"" + temp + "\" ];\n"

        return nodo

class FuncionCadena(ExpresionString):
    def __init__(self, funcion, parametro1, parametro2 = None, parametro3 = None):
        self.funcion = funcion
        self.parametro1 = parametro1
        self.parametro2 = parametro2
        self.parametro3 = parametro3

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"" + self.funcion + "\" ];"
        nodo += "\n" + identificador+ " -> " + str(hash(self.parametro1)) + ";"
        nodo += "\n" + str(hash(self.parametro1)) + "[label = \"" + self.parametro1 + "\"];"

        if self.parametro2:
            if isinstance(self.parametro2, str):
                nodo += "\n" + identificador+ " -> " + str(hash(self.parametro2)) + ";"
                nodo += "\n" + str(hash(self.parametro2)) + "[label = \"" + self.parametro2 + "\"];"
            else:
                nodo += "\n" + identificador+ " -> " + str(hash(self.parametro2)) + ";"
                nodo += "\n" + str(hash(self.parametro2)) + "[label = \"" + str(self.parametro2) + "\"];"
        

        return nodo

# ------------------------ DDL ----------------------------

# Consulta (Abstracta)
class Consulta:
    def ejecutar(self):
        pass

    def dibujar(self):
        pass

# Complemento (Abstracta)
class Complemento:
    def dibujar(self):
        pass

# Create Database
class CreateDatabase(Consulta):
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
class CreateTable(Consulta):
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
            node += col.dibujar()

        if self.herencia:
            nodo += "\nINHERITS" + identificador +  "[ label=\"INHERITS\" ];"
            nodo += "\n" + identificador + " -> INHERITS" + identificador +  ";"
            nodo += "SUPER" + identificador +  "[ label=\"" + self.herencia + "\" ];"
            nodo += "\nINHERITS" + identificador + " -> SUPER" + identificador + ";"

        return node

# Alter Database
class AlterDatabase(Consulta):
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
class AlterTable(Consulta):
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
class AlterField(Complemento):
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
class AlterTableDrop(Complemento):
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
class AlterTableAdd(Complemento):
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
class ShowDatabase(Consulta):
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
class DropDatabase(Consulta):
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
class CreateField(Complemento):
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
class DefaultField(Complemento):
    def __init__(self, valor):
        self.valor = valor

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"DEFAULT\" ];"
        nodo += "\nDEFAULT" + identificador + "[ label = \"" + self.valor + "\" ];"
        nodo += "\n" + identificador + " -> DEFAULT" + identificador + ";\n"

        return nodo

# Check Field
class CheckField(Complemento):
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
class ConstraintField(Complemento):
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
class ConstraintMultipleFields(Complemento):
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
class ForeignKeyMultipleFields(Complemento):
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
class CheckMultipleFields(Complemento):
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

# ------------------------ DML ----------------------------

# Insert into table
class InsertTable(Consulta):
    def __init__(self, tabla, valores):
        self.tabla = tabla
        self.valores = valores
    
    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"INSERT TABLE\" ];"

        nodo += "\nINTO" + identificador + "[ label = \"INTO\" ];"
        nodo += "\n" + identificador + " -> INTO" + identificador + ";"
        nodo += "\nNAME" + identificador + "[ label = \"" + self.tabla + "\" ];"
        nodo += "\nINTO" + identificador + " -> NAME" + identificador + ";"
        nodo += "\nVALUES" + identificador + "[ label = \"VALUES\" ];"
        nodo += "\n" + identificador + " -> VALUES" + identificador + ";"
        
        for valor in self.valores:
            nodo += "\nVALUES" + identificador + " -> " + str(hash(valor)) + ";"
            nodo += valor.dibujar()

        return nodo

# Delete from a table
class DeleteTabla(Consulta):
    def __init__(self, tabla, condiciones = None):
        self.tabla = tabla
        self.condiciones = condiciones

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"DELETE TABLE\" ];"

        nodo += "\nFROM" + identificador + "[ label = \"FROM\" ];"
        nodo += "\n" + identificador + " -> FROM" + identificador + ";"
        nodo += "\nNAME" + identificador + "[ label = \"" + self.tabla + "\" ];"
        nodo += "\nFROM" + identificador + " -> NAME" + identificador + ";"

        if self.condiciones:
            nodo += "\nWHERE" + identificador + "[ label = \"WHERE\" ];"
            nodo += "\n" + identificador + " -> WHERE" + identificador + ";"

            for condicion in self.condiciones:
                nodo += "\nWHERE" + identificador + " -> " + str(hash(condicion)) + ";"
                nodo += condicion.dibujar()

        return nodo

class UpdateTable(Consulta):
    def __init__(self, tabla, asignaciones, condiciones = None):
        self.tabla = tabla
        self.asignaciones = asignaciones
        self.condiciones = condiciones

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"DELETE TABLE\" ];"

        nodo += "\nNAME" + identificador + "[ label = \"" + self.tabla + "\" ];"
        nodo += "\n" + identificador + " -> NAME" + identificador + ";"

        nodo += "\nSET" + identificador + "[ label = \"SET\" ];"
        nodo += "\n" + identificador + " -> SET" + identificador + ";"

        for asignacion in self.asignaciones:
            nodo += "\nSET" + identificador + " -> " + str(hash(asignacion)) + ";"
            nodo += asignacion.dibujar()

        if self.condiciones:
            nodo += "\nWHERE" + identificador + "[ label = \"WHERE\" ];"
            nodo += "\n" + identificador + " -> WHERE" + identificador + ";"

            for condicion in self.condiciones:
                nodo += "\nWHERE" + identificador + " -> " + str(hash(condicion)) + ";"
                nodo += condicion.dibujar()

        return nodo

# ------------------------ Select ----------------------------
# Select Table
class SelectTable(Consulta):
    def __init__(self, campos, tablas = None, filtro = None, orden = None, limite = None, offset = None, join = None):
        self.campos = campos
        self.tablas = tablas
        self.filtro = filtro
        self.orden = orden
        self.limite = limite
        self.offset = offset
        self.join = join

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"SELECT TABLE\" ];" + "\nVALUES" + identificador + "[ label = \"FIELDS\" ];"
        nodo += "\n" + identificador + " -> VALUES" + identificador + ";"

        # Para los distintos campos que puedan ser objeto, una lista o un booleano
        if isinstance(self.campos, bool):
            nodo += "\nVALUES" + identificador + " -> " + str(hash(self.campos)) + ";"
            nodo += "\n" + str(hash(self.campos)) + "[ label = \"*\" ];"
        elif isinstance(self.campos, list):
            for campo in self.campos:
                nodo += "\nVALUES" + identificador + " -> " + str(hash(campo)) + ";"
                nodo += campo.dibujar()
        else:
            nodo += "\nVALUES" + identificador + " -> " + str(hash(self.campos)) + ";"
            nodo += self.campos.dibujar()

        # Para from
        if self.tablas:
            nodo += "\nFROM" + identificador + "[ label = \"FROM\" ];"
            nodo += "\n" + identificador + " -> FROM" + identificador + ";"
            for tabla in self.tablas:
                nodo += "\nFROM" + identificador + " -> " + str(hash(tabla)) + ";"
                nodo += tabla.dibujar()

        # Para filtro
        if self.filtro:
            nodo += "\n" + identificador + " -> " + str(hash(self.filtro)) + ";"
            nodo += self.filtro.dibujar()
        
        # Para orders
        if self.orden:
            nodo += "\n" + identificador + " -> " + str(hash(self.orden)) + ";"
            nodo += self.orden.dibujar()

        # Para limites
        if self.limite:
            nodo += "\n" + identificador + " -> " + str(hash(self.limite)) + ";"
            if isinstance(self.limite, int):
                nodo += "\n" + str(hash(self.limite)) + "[ label =  \"" + str(self.limite) + "\"];"
            else:            
                nodo += "\n" + str(hash(self.limite)) + "[ label =  \"ALL\"];"

        # Para offset
        if self.offset:
            nodo += "\n" + identificador + " -> " + str(hash(self.offset)) + ";"
            nodo += "\n" + str(hash(self.offset)) + "[ label =  \"" + str(self.offset) + "\"];"

        # Para join
        if self.join:
            nodo += "\n" + identificador + " -> " + str(hash(self.join)) + ";"
            nodo += self.join.dibujar()

        return nodo

# JOIN
class SelectJoin(Complemento):
    def __init__(self, tabla, tipo, coincidencia = None, natural = False, outer = False):
        self.tabla = tabla
        self.tipo = tipo
        self.coincidencia = coincidencia
        self.natural = natural
        self.outer = outer

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador

        if self.natural:
            if self.outer:
                if self.tipo == JOIN.RIGHT:
                    nodo += "[ label = \"NATURAL RIGHT OUTER\" ];"
                elif self.tipo == JOIN.LEFT:
                    nodo += "[ label = \"NATURAL LEFT OUTER\" ];"
                else:
                    nodo += "[ label = \"NATURAL FULL OUTER\" ];"
            else:
                if self.tipo == JOIN.INNER:
                    nodo += "[ label = \"NATURAL INNER\" ];"
                elif self.tipo == JOIN.RIGHT:
                    nodo += "[ label = \"NATURAL RIGHT\" ];"
                elif self.tipo == JOIN.LEFT:
                    nodo += "[ label = \"NATURAL LEFT\" ];"
                else:
                    nodo += "[ label = \"NATURAL FULL\" ];"
        else:
            if self.outer:
                if self.tipo == JOIN.RIGHT:
                    nodo += "[ label = \"RIGHT OUTER\" ];"
                elif self.tipo == JOIN.LEFT:
                    nodo += "[ label = \"LEFT OUTER\" ];"
                else:
                    nodo += "[ label = \"FULL OUTER\" ];"
            else:
                if self.tipo == JOIN.INNER:
                    nodo += "[ label = \"INNER\" ];"
                elif self.tipo == JOIN.RIGHT:
                    nodo += "[ label = \"RIGHT\" ];"
                elif self.tipo == JOIN.LEFT:
                    nodo += "[ label = \"LEFT\" ];"
                else:
                    nodo += "[ label = \"FULL\" ];"
        
        nodo += "\n" + str(hash(self.tabla)) + "[ label = \"" + self.tabla + "\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.tabla)) + ";"

        return nodo

# Select From
class SelectFrom(Complemento):
    def __init__(self, fuente, alias = None):
        self.fuente = fuente
        self.alias = alias
    
    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador
        if self.alias:
            nodo += "[ label = \"AS: " + self.alias + "\" ];"
            nodo += "\n" + identificador + " -> " + str(hash(self.fuente)) + ";"
            if isinstance(self.fuente, str):
                nodo += "\n" + str(hash(self.fuente)) + "[ label = \"" + self.fuente + "\" ];\n"
            else:
                nodo += self.fuente.dibujar()
        else:
            if isinstance(self.fuente, str):
                nodo += "[ label = \"" + self.fuente + "\" ];\n"
            else:
                nodo += "[ label = \"SUBQUERY\" ];"
                nodo += "\n" + identificador + " -> " + str(hash(self.fuente)) + ";"
                nodo += self.fuente.dibujar()
        return nodo

# Select filter
class SelectFilter(Complemento):
    def __init__(self, where, groupby = None, having = None):
        self.where = where
        self.groupby = groupby
        self.having = having

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"FILTER\" ];"

        # Para el where
        nodo += "\nWHERE" + identificador + "[ label = \"WHERE\" ];"
        nodo += "\n" + identificador + " -> WHERE" + identificador + ";"
        nodo += "\nWHERE" + identificador + " -> " + str(hash(self.where)) + ";"

        # Para el group by
        if self.groupby:
            nodo += "\nGROUPBY" + identificador + "[ label = \"GROUP BY\" ];"
            nodo += "\n" + identificador + " -> GROUPBY" + identificador + ";"
            nodo += "\nGROUPBY" + identificador + " -> " + str(hash(self.groupby)) + ";"

        if self.having:
            nodo += "\nHAVING" + identificador + "[ label = \"HAVING\" ];"
            nodo += "\n" + identificador + " -> HAVING" + identificador + ";"
            nodo += "\nHAVING" + identificador + " -> " + str(hash(self.having)) + ";"        

        return nodo

# Select orderby
class SelectOrderBy(Complemento):
    def __init__(self, exp, orden = None, nulo = None):
        self.exp = exp
        self.orden = orden
        self.nulo = nulo
    
    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"ORDER BY\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp)) + ";"
        nodo += self.exp.dibujar()

        if self.orden:
            nodo += "\n" + str(hash(self.orden)) + "[ label = \"" + self.orden + "\" ];"
            nodo += "\n" + identificador + " -> " + str(hash(self.orden)) + ";\n"

        if self.nulo:
            nodo += "\n" + str(hash(self.nulo)) + "[ label = \"" + self.nulo + "\" ];"
            nodo += "\n" + identificador + " -> " + str(hash(self.nulo)) + ";\n"

        return nodo

# Select Aggregate
class SelectAggregate(Complemento):
    def __init__(self, funcion, parametro):
        self.funcion = funcion
        self.parametro = parametro

# Combine Select
class CombineSelect(Consulta):
    def __init__(self, select1, select2, funcion, all = False):
        self.select1 = select1
        self.select2 = select2
        self.funcion = funcion
        self.all = all

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador 

        if self.all:
            if self.funcion == COMBINE_QUERYS.UNION:
                nodo += "[ label = \"UNION ALL\" ];"
            elif self.funcion == COMBINE_QUERYS.INTERSECT:
                nodo += "[ label = \"INTERSECT ALL\" ];"
            else:
                nodo += "[ label = \"EXCEPT ALL\" ];"
        else:
            if self.funcion == COMBINE_QUERYS.UNION:
                nodo += "[ label = \"UNION\" ];"
            elif self.funcion == COMBINE_QUERYS.INTERSECT:
                nodo += "[ label = \"INTERSECT\" ];"
            else:
                nodo += "[ label = \"EXCEPT\" ];"

        nodo += "\n" + identificador + " -> " + str(hash(self.select1)) + ";"
        nodo += self.select1.dibujar() + "\n"

        nodo += "\n" + identificador + " -> " + str(hash(self.select2)) + ";"
        nodo += self.select2.dibujar() + "\n"

        return nodo