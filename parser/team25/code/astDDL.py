from enum import Enum
import entorno as env
import storageManager.jsonMode as DBMS
import typeChecker.typeReference as TRef
import typeChecker.typeEnum as TEnum
import sqlErrors
from reporteErrores.errorReport import ErrorReport
from useDB.instanciaDB import DB_ACTUAL

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
    MULTI_FOREIGN_KEY = 3
    CHECKS = 4

class CONSTRAINT_FIELD(Enum):
    UNIQUE = 1
    PRIMARY_KEY = 2
    NULL = 3

class TYPE_COLUMN(Enum):
    SMALLINT = 'SMALLINT'
    BIGINT = 'BIGINT'
    INTEGER = 'INTEGER'
    DECIMAL = 'DECIMAL'
    NUMERIC = 'NUMERIC'
    REAL = 'REAL'
    DOUBLE_PRECISION = 'DOUBLE_PRECISION'
    MONEY = 'MONEY'
    CHAR = 'CHAR'
    VARCHAR = 'VARCHAR'
    TEXT = 'TEXT'
    BOOLEAN = 'BOOLEAN'
    # No implementadas
    TIME = 'TIME'
    TIMESTAMP = 'TIMESTAMP'
    DATE = 'DATE'
    INTERVAL = 'INTERVAL'

# ------------------------ DDL ----------------------------
# Instruccion (Abstracta)
class Instruccion:
    def ejecutar(self,ts):
        pass

    def dibujar(self):
        return 'Sin implementar'

class CreateType(Instruccion):
    def __init__(self, nombre, lista):
        self.nombre = nombre
        self.lista = lista

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"CREATE " + self.nombre + " TYPE as ENUM\" ];"
        for item in self.lista:
            nodo += "\n" + identificador + "-> " + str(hash(item))
            nodo += '\n' +  str(hash(item)) + "[ label = \" " + item + " \" ];"

        return nodo

    def ejecutar(self, ts):
        lista = list()
        for item in self.lista:
            if not item in lista:
                lista.append(item)
        if not TEnum.insertEnum(self.nombre, lista):
            return ErrorReport('Semantico', 'Invalid Enum Declaration', 0)
        return 'Enum \'' + self.nombre + '\' succesful created'

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

        nodo = "\n" + identificador

        if self.reemplazo:
            nodo += "[ label = \" CREATE OR REPLACE DATABASE " + self.nombre + " \" ];"
        else:
            nodo += "[ label = \"CREATE DATABASE " + self.nombre + "\" ];"

        if self.existencia:
            nodo += "\nEXISTS" + identificador + "[ label = \"IF EXISTS\" ];"
            nodo += "\n" + identificador + " -> EXISTS" + identificador + ";"

        if self.duenio:
            nodo += "\n" + identificador + " -> " + str(hash(self.duenio)) + ";"
            nodo += "\n" + str(hash(self.duenio)) + "[ label = \"OWNER: " + self.duenio + "\" ];"

        if self.modo > 0:
            nodo += "\n" + str(hash(self.modo)) + "[ label = \"MODE: " + str(self.modo) + "\" ];"
            nodo += "\n" + identificador + " -> " + str(hash(self.modo)) + ";"

        return nodo

    def ejecutar(self,ts):
        if TRef.databaseExist(self.nombre):
            if not self.existencia:
                return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.duplicate_database), 0)

        exito = 0
        databases = DBMS.showDatabases()

        if self.reemplazo:
            if self.nombre in databases: #Eliminamos si existe 
                DBMS.dropDatabase(self.nombre)
                TRef.dropDatabase(self.nombre)
            exito = DBMS.createDatabase(self.nombre)
        elif self.existencia:
            if not self.nombre in databases:
                exito = DBMS.createDatabase(self.nombre)
        else:
            exito = DBMS.createDatabase(self.nombre)

        #Si tenemos exito se crea en el type reference
        if exito == 1:
            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.invalid_schema_definition), 0)
        elif exito == 2:
            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.duplicate_database), 0)
            
        TRef.createDatabase(self.nombre, self.modo)
        return "Database '" + self.nombre + "' succesful created"

# Create Table
class CreateTable(Instruccion):
    def __init__(self, nombre, columnas, herencia = None):
        self.nombre = nombre
        self.columnas = columnas
        self.herencia = herencia

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"CREATE TABLE " + self.nombre + "\" ];"
        nodo += "\n//COLUMNAS DE LA TABLA" + identificador + "\n"

        for col in self.columnas:
            nodo += "\n" + identificador + " -> " + str(hash(col)) + ";"
            nodo += col.dibujar()

        if self.herencia:
            nodo += "\n" + identificador + " -> " + str(hash(self.herencia)) + ";"
            nodo += "\n" + str(hash(self.herencia)) + "[ label = \"" + self.herencia + "\" ];"

        return nodo

    def ejecutar(self, ts):
        if DB_ACTUAL.getName() == None:
            return ErrorReport('Semantico', 'Not defined database to used', 0)
        elif not TRef.databaseExist(DB_ACTUAL.getName()):
            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_invalid_schema_name.invalid_schema_name), 0)
        elif TRef.tableExist(DB_ACTUAL.getName(), self.nombre):
            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.duplicate_table), 0)

        # Aux de comprobacion y almacenamiento
        columns = dict()
        auxFK = list()
        auxPK = list()
        auxUnique = list()
        auxCheck = list()

        #Aux check field
        auxCheckF = list()

        # Proceso de las distintas columnas recibidas en la consulta
        for col in self.columnas:
            if isinstance(col, CreateField): #Columna nueva
                #Obtenemos cada columna y corroboramos que tengan nombres distintos
                if col.nombre in columns:
                    return 1
                else: 
                    colSint = col.ejecutar(ts)
                    if isinstance(colSint, ErrorReport):
                        return colSint

                    if isinstance(colSint, tuple):
                        columns[col.nombre] = colSint[0]
                        auxCheckF.append(colSint[1])
                    else:
                        columns[col.nombre] = colSint
            elif isinstance(col, ConstraintMultipleFields): #Multiples Constraints
                if col.tipo == CONSTRAINT_FIELD.UNIQUE:
                    auxUnique.extend(col.ejecutar(ts))
                else:
                    auxPK.extend(col.ejecutar(ts))
            elif isinstance(col, ForeignKeyMultipleFields): #Multiples Llaves Foraneas
                colSint = col.ejecutar(ts)
                if isinstance(colSint, ErrorReport):
                    return colSint
                auxFK.extend(colSint)
            elif isinstance(col, CheckMultipleFields): #Multiple chequeos
                auxCheck.extend(col.ejecutar(ts))
            else:
                return col

        if len(auxCheckF) != 0:
            tsLocal = env.Entorno()
            tsLocal = env.toEnviroment(columns, tsLocal)
            
            for chequeoS in auxCheckF:
                if chequeoS[0].evaluacionCheck(tsLocal) != 0:
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_integrity_constraint_violation.integrity_constraint_violation), 0)
                columns[chequeoS[2]]['Check'] = chequeoS[0].getExpresionToString()
                columns[chequeoS[2]]['CheckConst'] = chequeoS[1]
        
        #Modificamos los valores dependiendo de las columnas multiples
        # Primary Key
        for pk in auxPK:
            # Se verifica que cada constraint haga referencia a un campo, de lo contrario será invalido
            if not pk in columns:
                return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.invalid_column_reference), 0)
            columns[pk]['PK'] = True

        # Foreign Key
        for fk  in auxFK:
            # Se verifica que cada constraint haga referencia a un campo, de lo contrario será invalido
            if not fk[0] in columns:
                return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.invalid_column_reference), 0)
            columns[fk[0]]['FK'] = True
            columns[fk[0]]['References'] = {'Table':fk[1],'Field':fk[0]}

        #Check
        if len(auxCheck) != 0:
            tsLocal = env.Entorno()
            tsLocal = env.toEnviroment(columns, tsLocal)

            for chequeo in auxCheck:
                # Se verifica que cada constraint haga referencia a un campo, de lo contrario será invalido
                if not chequeo[0] in columns:
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.invalid_column_reference), 0)
                if chequeo[1].evaluacionCheck(tsLocal) != 0:
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_integrity_constraint_violation.integrity_constraint_violation), 0)
                columns[chequeo[0]]['Check'] = chequeo[1].getExpresionToString()
        # Unique
        for unico in auxUnique:
            # Se verifica que cada constraint haga referencia a un campo, de lo contrario será invalido
            if not unico in columns:
                return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.invalid_column_reference), 0)
            columns[unico]['Unique'] = True
            
        #--------- Herencia
        if self.herencia:
            if not TRef.tableExist(DB_ACTUAL.getName(), self.herencia):
                return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_fdw_error.fdw_table_not_found), 0)
            else:
                colsPadre = TRef.getColumns(DB_ACTUAL.getName(), self.herencia)
                for col in colsPadre:
                    # Verificamos que no existan columnas repetidas con el padre, ya que no existe el polimorfismo de campos
                    if col in columns:
                        return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.duplicate_column), 0)
                # De no existir columnas duplicadas, se agregan las columnas a la tabla
                columns.update(colsPadre)

        auxIndexPK = list()
        contador = 0
        for col in columns:
            if columns[col]['PK']:
                auxIndexPK.append(contador)
            contador += 1

        # Ahora procedemos a crear
        result = DBMS.createTable(DB_ACTUAL.getName(), self.nombre, len(columns))

        if result == 0:
            if len(auxIndexPK) > 0:
                DBMS.alterAddPK(DB_ACTUAL.getName(),self.nombre, auxIndexPK)
            TRef.createTable(DB_ACTUAL.getName(), self.nombre, columns, self.herencia)
            return result

        return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.duplicate_table), 0)
        
# Create Field
class CreateField(Instruccion):
    def __init__(self, nombre, tipo, atributos = None):
        self.nombre = nombre
        self.tipo = tipo
        self.atributos = atributos

    def dibujar(self):
        identificador = str(hash(self))

        aux = self.tipo
        if isinstance(self.tipo, tuple):
            aux = self.tipo[0].value
            if isinstance(self.tipo[1], tuple):
                aux += "(" + str(self.tipo[1][0]) + "," + str(self.tipo[1][1]) + ")"
            else:
                aux += "(" + str(self.tipo[1]) + ")"
        elif isinstance(self.tipo, str):
            pass
        else:
            aux = self.tipo.value
        nodo = "\n" + identificador + "[ label = \"NEW FIELD " + self.nombre + " " + aux + "\" ];"
        nodo += "\n//ATRIBUTOS DE CREAR UN CAMPO " + identificador + "\n"

        if self.atributos:
            for atributo in self.atributos:
                nodo += "\n" + identificador + " -> " + str(hash(atributo))
                nodo += atributo.dibujar()

        nodo += "\n//FIN DE ATRIBUTOS DE CREAR CAMPO " + identificador + "\n"

        return nodo

    def ejecutar(self, ts):
        #Guardamos el tipo y largo si es necesario
        tipo = None
        largo = None

        if isinstance(self.tipo, tuple):
            tipo = self.tipo[0].value
            if isinstance(self.tipo[1],tuple):
                largo = {'Precision': self.tipo[1][0],'Scale': self.tipo[1][1]}
            else:
                if self.tipo[1] < 1:
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_data_exception.numeric_value_out_of_range), 0)
                largo = self.tipo[1]
        elif isinstance(self.tipo, str):
            #Comprobamos que el type a elegir exista
            if not TEnum.enumExist(self.tipo):
                return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.indeterminate_datatype), 0)
            tipo = self.tipo
        else:
            tipo = self.tipo.value
            
        #Bajo la logica de que puede venir parametros repetidos, tomaremos el ultimo en venir como valido
        atributos = dict(
            {
                "Type": tipo,
                "Lenght": largo,
                "Default": None,
                "Null": True,
                "PK": False,
                "PKConst": None,
                "FK": False,
                "References": None,
                "FKConst": None,
                "Unique": False,
                "UniqueConst": None,
                "Check": None,
                "CheckConst": None
            }
            )

        checks = None
        if self.atributos:
            for atr in self.atributos:
                if isinstance(atr, ConstraintField):
                    if atr.tipo == CONSTRAINT_FIELD.PRIMARY_KEY:
                        atributos['PK'] = True

                    elif atr.tipo == CONSTRAINT_FIELD.UNIQUE:
                        atributos['Unique'] = True
                        atributos['UniqueConst'] = atr.ejecutar(ts)

                    elif atr.tipo == CONSTRAINT_FIELD.NULL:
                        atributos['Null'] = atr.ejecutar(ts)
                elif isinstance(atr, ForeignKeyField):
                    fk = atr.ejecutar(ts)
                    if isinstance(fk, ErrorReport):
                        return fk
                    else:
                        colFK = TRef.getColumns(DB_ACTUAL.getName(), fk['Table'])[fk['Field']]
                        if colFK['Type'] != tipo:
                            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_fdw_error.fdw_invalid_data_type), 0)
                        atributos['References'] = fk
                        atributos['FK'] = True
                elif isinstance(atr, DefaultField):
                    try:
                        dflt = atr.ejecutar(ts).val
                        #Chequeamos el default
                        if (tipo == 'SMALLINT'\
                        or tipo == 'BIGINT' \
                        or tipo == 'INTEGER') and not isinstance(dflt, int):
                            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch),0)
                        elif (tipo == 'DECIMAL' \
                        or tipo == 'NUMERIC' \
                        or tipo == 'REAL' \
                        or tipo == 'DOUBLE_PRECISION' \
                        or tipo == 'MONEY') and not (isinstance(dflt, float) or isinstance(dflt, int)):
                            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch),0)
                        elif (tipo == 'CHAR' \
                        or tipo == 'VARCHAR' \
                        or tipo == 'TEXT' \
                        or tipo == 'ENUM') and not isinstance(dflt, str):
                            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch),0)
                        elif tipo == 'BOOLEAN' and not isinstance(dflt, bool):
                            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch),0)
                        elif tipo == 'DATE' and not isinstance(dflt, str):
                            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch),0)
                        #Guardamos el default
                        atributos['Default'] = dflt
                    except:
                        return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.datatype_mismatch),0)
                elif isinstance(atr,CheckField):
                    cheq = atr.ejecutar(ts)
                    checks = (cheq[1],cheq[0],self.nombre)
                else:
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.invalid_table_definition), 0)


        if isinstance(checks, tuple):
            return (atributos, checks)

        return atributos

# Default Field
class DefaultField(Instruccion):
    def __init__(self, valor):
        self.valor = valor

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"DEFAULT: " + str(self.valor.getExpresionToString()) + "\" ];"

        return nodo

    def ejecutar(self, ts):
        return self.valor.ejecutar(None)

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

        nodo += "\n" + identificador + " -> " + str(hash(self.condiciones)) + ";"
        nodo += "\n" + str(hash(self.condiciones)) + "[ label =\"" + self.condiciones.getExpresionToString() + "\" ];"

        return nodo

    def ejecutar(self, ts):
        return (self.nombre,self.condiciones)

# Constraint Field
class ConstraintField(Instruccion):
    def __init__(self, tipo, valor = None):
        self.tipo = tipo
        self.valor = valor

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador

        if self.tipo == CONSTRAINT_FIELD.UNIQUE:
            nodo += "[ label = \"UNIQUE\" ];"
        elif self.tipo == CONSTRAINT_FIELD.NULL:
            nodo += "[ label = \"NULLS\" ];"
        else:
            nodo += "[ label = \"PRIMARY KEY\" ];"

        if self.valor:
            nodo += "\nNAME" + identificador + "[ label = \"" + str(self.valor) + "\" ];"
            nodo += "\n" + identificador + " -> NAME" + identificador + ";"

        return nodo
    
    def ejecutar(self, ts):
        return self.valor

#ForeignKey Field
class ForeignKeyField(Instruccion):
    def __init__(self, tabla, campo):
        self.tabla = tabla
        self.campo = campo

    def dibujar(self):
        identificador = str(hash(self))
        nodo = "\n" + identificador + "[ label = \"FOREIGN KEY\" ];"

        nodo += "\n" + identificador + " -> " + str(hash(self.tabla)) + ";"
        nodo += "\n" + str(hash(self.tabla)) + "[ label = \"TABLE: " + self.tabla + "\" ];"

        nodo += "\n" + identificador + " -> " + str(hash(self.campo)) + ";"
        nodo += "\n" + str(hash(self.campo)) + "[ label = \"FIELD: " + self.campo + "\" ];"

        return nodo

    def ejecutar(self, ts):
        if TRef.columnExist(DB_ACTUAL.getName(), self.tabla, self.campo):
            return {'Table': self.tabla, 'Field': self.campo}
        else:
            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_fdw_error.fdw_column_name_not_found), 0)

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
            nodo += "\n" + str(hash(item)) + "[ label = \"" + item + "\" ];"

        return nodo

    def ejecutar(self, ts):
        return self.lista
        
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
            nodo += "\n" + str(hash(item)) + "[ label = \"" + item +" \" ];"

        nodo += "\nFOREIGN" + identificador + "[ label = \"" + self.otraTabla + " FIELDS\" ];"
        nodo += "\n" + identificador + " -> FOREIGN" + identificador + ";"

        for item in self.listaOtraTabla:
            nodo += "\nFOREIGN" + identificador + " -> " + str(hash(item)) + ";"
            nodo += "\n" + str(hash(item)) + "[ label = \"" + item +" \" ];"

        return nodo

    def ejecutar(self, ts):
        if not TRef.databaseExist(DB_ACTUAL.getName()):
            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_fdw_error.fdw_schema_not_found), 0)
        elif not TRef.tableExist(DB_ACTUAL.getName(),self.otraTabla):
            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_fdw_error.fdw_table_not_found), 0) 

        #Comparamos que la misma cantidad de ids propios sea igual a la foranea
        if len(self.lista) != len(self.listaOtraTabla):
            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_data_exception.data_exception), 0)

        for col in self.listaOtraTabla:
            if not TRef.columnExist(DB_ACTUAL.getName(), self.otraTabla, col):
                return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_fdw_error.fdw_invalid_column_number), 0)

        listaSin = list()
        for i in range(len(self.lista)):
            listaSin.append( (self.lista[i], self.otraTabla, self.listaOtraTabla[i]) )

        return listaSin

# Check Multiple Fields
class CheckMultipleFields(Instruccion):
    def __init__(self, campo, condiciones):
        self.campo = campo
        self.condiciones = condiciones

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"CHECK " + self.campo + "\" ];"

        nodo += "\n" + identificador + " -> " + str(hash(self.condiciones)) + ";"
        nodo += "\n" + str(hash(self.condiciones)) + "[ label = \"" + self.condiciones.getExpresionToString() + "\" ];"

        return nodo

    def ejecutar(self, ts):
        return (self.campo, self.condiciones)

# Alter Database
class AlterDatabase(Instruccion):
    def __init__(self, nombre, accion):
        self.nombre = nombre
        self.accion = accion

    def dibujar(self):
        identificador = str(hash(self))
        
        nodo = "\n" + identificador + "[ label = \"ALTER DATABASE\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.accion)) + ";"
        
        if self.accion[0] == 'OWNER':
            nodo += "\n" + str(hash(self.accion)) + "[ label = \"OWNER: " + self.accion + "\" ];"
        else:
            nodo += "\n" + str(hash(self.accion)) + "[ label = \"NAME: " + self.accion + "\" ];"

        return nodo
    
    def ejecutar(self, ts):
        if not TRef.databaseExist(self.nombre):
            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_invalid_schema_name.invalid_schema_name), 0)

        if self.accion[0] == 'OWNER':
            pass
        else:
            #Comprobamos que no exista una base de datos con ese nombre
            if TRef.databaseExist(self.accion[1]):
                return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.duplicate_database), 0)
            DBMS.alterDatabase(self.nombre, self.accion[1])
            TRef.alterDatabase(self.nombre, self.accion[1])
        return 'Successful alter database ' + self.nombre

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

        if isinstance(self.accion, list):
            for item in self.accion:
                nodo += "\n" + identificador + " -> " + str(hash(item)) + ";"
                nodo += item.dibujar()
        else:
            nodo += "\n" + identificador + " -> " + str(hash(self.accion)) + ";"
            nodo += self.accion.dibujar()

        return nodo
        
    def ejecutar(self, ts):
        if DB_ACTUAL.getName() == None:
            return ErrorReport('Semantico', 'Not defined database to used', 0)
        elif not TRef.databaseExist(DB_ACTUAL.getName()):
            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_invalid_schema_name.invalid_schema_name), 0)
        elif not TRef.tableExist(DB_ACTUAL.getName(), self.tabla):
            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.undefined_table), 0)

        if isinstance(self.accion, list):
            for subaccion in self.accion:
                sint = subaccion.ejecutar(ts)
                #Si es un error, solo se retorna
                if isinstance(sint, ErrorReport):
                    return sint

                if not TRef.columnExist(DB_ACTUAL.getName(),self.tabla, subaccion.campo):
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.undefined_column), 0)
                
                if subaccion.cantidad:
                    sint = subaccion.ejecutar(ts)
                    if isinstance(sint, int):
                        TRef.alterField(DB_ACTUAL.getName(), self.tabla, subaccion.campo, 'Type', TYPE_COLUMN.VARCHAR.value)
                        TRef.alterField(DB_ACTUAL.getName(), self.tabla, subaccion.campo, 'Lenght', sint)
                    elif isinstance(sint, tuple):
                        TRef.alterField(DB_ACTUAL.getName(), self.tabla, subaccion.campo, 'Type', sint[0].value)
                        TRef.alterField(DB_ACTUAL.getName(), self.tabla, subaccion.campo, 'Lenght', sint[1])
                    else:
                        TRef.alterField(DB_ACTUAL.getName(), self.tabla, subaccion.campo, 'Type', sint)
                        TRef.alterField(DB_ACTUAL.getName(), self.tabla, subaccion.campo, 'Lenght', None)
                else:
                    TRef.alterField(DB_ACTUAL.getName(), self.tabla, subaccion.campo, 'Null', False)
        elif isinstance(self.accion, AlterTableDrop):
            if self.accion.tipo == ALTER_TABLE_DROP.COLUMN:
                sint = self.accion.ejecutar(ts)
                #Comprobamos la existencia del campo
                if not TRef.columnExist(DB_ACTUAL.getName(),self.tabla,self.accion.nombre):
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.undefined_column), 0)
                dropField = TRef.alterDropColumn(DB_ACTUAL.getName(), self.tabla, sint)
                if dropField == 1:
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_data_exception.data_exception), 0)
                elif dropField == 4:
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_integrity_constraint_violation.integrity_constraint_violation), 0)
                elif dropField == 6:
                    return ErrorReport('Semantico', 'Error: A table cannot be empty', 0)
            else:
                if not TRef.constraintExist(DB_ACTUAL.getName(),self.accion.nombre):
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_integrity_constraint_violation.integrity_constraint_violation), 0)
                colPres = TRef.getConstraint(DB_ACTUAL.getName(),self.tabla, self.accion.nombre)
                if not isinstance(colPres, tuple):
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_data_exception.data_exception), 0)

                TRef.alterField(DB_ACTUAL.getName(), self.tabla, colPres[0], colPres[1], None)
                if colPres[1] == 'PKConst':
                    TRef.alterField(DB_ACTUAL.getName(), self.tabla, colPres[0], 'PK', False)
                    DBMS.alterDropPK(DB_ACTUAL.getName(), self.tabla)
                    DBMS.alterAddPK(DB_ACTUAL.getName(), self.tabla, TRef.getIndexPK(DB_ACTUAL.getName(), self.tabla))
                elif colPres[1] == 'PKConst':
                    TRef.alterField(DB_ACTUAL.getName(), self.tabla, colPres[0], 'FK', False)
                    TRef.alterField(DB_ACTUAL.getName(), self.tabla, colPres[0], 'References', None)
                elif colPres[1] == 'UniqueConst':
                    TRef.alterField(DB_ACTUAL.getName(), self.tabla, colPres[0], 'Unique', False)
                else:
                    TRef.alterField(DB_ACTUAL.getName(), self.tabla, colPres[0], 'Check', None)
        elif isinstance(self.accion, AlterTableAdd):
            colSint = self.accion.ejecutar(ts)
            if isinstance(colSint, ErrorReport):
                return colSint

            if self.accion.tipo == ALTER_TABLE_ADD.COLUMN:
                if TRef.columnExist(DB_ACTUAL.getName(), self.tabla, self.accion.nombre):
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.duplicate_column), 0)
                tipo = None
                largo = None

                if isinstance(self.accion.accion, tuple):
                    tipo = self.accion.accion[0].value
                    if isinstance(self.tipo[1],tuple):
                        largo = {'Precision': self.accion.accion[1][0],'Scale': self.accion.accion[1][1]}
                    else:
                        largo = self.accion.accion[1]
                elif isinstance(self.accion.accion, str):
                    tipo = self.accion.accion
                else:
                    tipo = self.accion.accion.value

                atributos = dict(
                    {
                        "Type": tipo,
                        "Lenght": largo,
                        "Default": None,
                        "Null": True,
                        "PK": False,
                        "PKConst": None,
                        "FK": False,
                        "References": None,
                        "FKConst": None,
                        "Unique": False,
                        "UniqueConst": None,
                        "Check": None,
                        "CheckConst": None
                    }
                    )

                TRef.alterAddColumn(DB_ACTUAL.getName(), self.tabla, self.accion.nombre, atributos)
                DBMS.alterAddColumn(DB_ACTUAL.getName(), self.tabla, None)
            elif self.accion.tipo == ALTER_TABLE_ADD.FOREIGN_KEY:
                

                if not TRef.columnExist(DB_ACTUAL.getName(),self.tabla,colSint[0]):
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.invalid_column_reference),0)
                elif TRef.getColumns(DB_ACTUAL.getName(),self.tabla)[colSint[0]]['Type'] != TRef.getColumns(DB_ACTUAL.getName(),colSint[1])[colSint[2]]['Type']:
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_fdw_error.fdw_invalid_data_type), 0)
                TRef.alterAddFK(DB_ACTUAL.getName(),self.tabla,colSint[0],{'Table':colSint[1],'Field':colSint[2]})
                TRef.alterField(DB_ACTUAL.getName(),self.tabla,colSint[0],'FKConst',colSint[3])
            elif self.accion.tipo == ALTER_TABLE_ADD.MULTI_FOREIGN_KEY:
                # Procesamos por columna
                for i in range(len(colSint)):
                    if not TRef.columnExist(DB_ACTUAL.getName(),self.tabla,colSint[i][0]):
                        return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.invalid_column_reference),0)
                    elif TRef.getColumns(DB_ACTUAL.getName(),self.tabla)[colSint[i][0]]['Type'] != TRef.getColumns(DB_ACTUAL.getName(),colSint[i][1])[colSint[i][2]]['Type']:
                        return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_fdw_error.fdw_invalid_data_type), 0)
                    TRef.alterAddFK(DB_ACTUAL.getName(),self.tabla,colSint[i][0],{'Table':colSint[i][1],'Field':colSint[i][2]})
            elif self.accion.tipo == ALTER_TABLE_ADD.CHECKS:
                auxCols = TRef.getColumns(DB_ACTUAL.getName(),self.tabla)
                if not colSint[0] in auxCols:
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.invalid_column_reference), 0)
                auxCols[colSint[0]]['Check'] = colSint[0] + ' != ' + colSint[1]
            else:
                if not TRef.columnExist(DB_ACTUAL.getName(),self.tabla,self.accion.nombre):
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.invalid_column_reference), 0)
                elif TRef.constraintExist(DB_ACTUAL.getName(),self.accion.accion):
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_integrity_constraint_violation.integrity_constraint_violation), 0)
                elif TRef.getAttribute(DB_ACTUAL.getName(),self.tabla,self.accion.nombre, 'UniqueConst') != None:
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_integrity_constraint_violation.integrity_constraint_violation), 0)
                TRef.alterField(DB_ACTUAL.getName(), self.tabla, self.accion.nombre, 'UniqueConst', self.accion.accion)
                TRef.alterField(DB_ACTUAL.getName(), self.tabla, self.accion.nombre, 'Unique', True)

        return 'Alter table complete'          

# Alter Field: Cambia al tipo varchar o cambia ser nulo
class AlterField(Instruccion):
    def __init__(self, campo, cantidad = None):
        self.campo = campo
        self.cantidad = cantidad

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador 

        if self.cantidad:
            nodo += "[ label = \"ALTER COLUMN " + self.campo + " TYPE\" ];"

            nodo += "\nTYPE" + identificador + "[ label = \"VARCHAR(" + str(self.cantidad) + ")\" ];"
            nodo += "\n" + identificador + " -> TYPE" + identificador + ";\n"
        else:
            nodo += "[ label = \"ALTER COLUMN " + self.campo + " SET\" ];"

            nodo += "\nVALUE" + identificador + "[ label = \"NOT NULL\" ];"
            nodo += "\n" + identificador + " -> VALUE" + identificador + ";\n"

        return nodo
    
    def ejecutar(self, ts):
        # Verificar si existe la columna
        if self.cantidad:
            if isinstance(self.cantidad, int):
                if self.cantidad < 0:
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_data_exception.numeric_value_out_of_range),0)
                return self.cantidad
            elif isinstance(self.cantidad, tuple):
                return self.cantidad
            elif isinstance(self.cantidad, str):
                return self.cantidad
            else:
                return self.cantidad.value
                
        else:
            return False

# Alter Table Drop: Encapsula tanto constraints como columna
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

    def ejecutar(self, ts):
            return self.nombre

# Alter add 
class AlterTableAdd(Instruccion):
    def __init__(self, nombre, tipo, accion):
        self.nombre = nombre
        self.tipo = tipo
        self.accion = accion

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador 

        if self.tipo == ALTER_TABLE_ADD.UNIQUE:
            nodo += "[ label = \"ADD UNIQUE " + self.nombre + "\" ];"
            nodo += "\nNAME" + identificador + "[ label = \"" + self.nombre + "\" ];"
            nodo += "\n" + identificador + " -> NAME" + identificador + ";"
            nodo += "\nID" + identificador + "[ label = \"" + self.accion + "\" ];"
            nodo += "\n" + identificador + " -> ID" + identificador + ";\n"
        elif self.tipo == ALTER_TABLE_ADD.FOREIGN_KEY:
            nodo += "[ label = \"ADD CONSTRAINT " + self.nombre + " FOREIGN KEY\" ];"
            nodo += "\n" + identificador + " -> " + str(hash(self.accion[0])) +"\n"
            nodo += "\n" + str(hash(self.accion[0])) + "[ label = \"" + self.accion[0] + "." + self.accion[1] + "\" ]"
            nodo += "\n" + identificador + " -> " + str(hash(self.accion[2])) +"\n"
            nodo += "\n" + str(hash(self.accion[2])) + "[ label = \"CONSTRAINT: " + self.accion[2] + "\" ]"
        elif self.tipo == ALTER_TABLE_ADD.MULTI_FOREIGN_KEY:
            nodo += "[ label = \"ADD FOREIGN KEY\" ];"
            for local in self.nombre:
                nodo += "\n" + str(hash(local)) + "[ label =\"" + local + "\" ];"
                nodo += "\n" + identificador + " -> " + str(hash(local)) + ";"
            nodo += "\nTABLA" + identificador + "[ label = \"" + self.accion[0] + "\" ];"
            nodo += "\n" + identificador + " -> TABLA" + identificador + ";"
            for foraneo in self.accion[1]:
                nodo += "\n" + str(hash(foraneo)) + "[ label =\"" + foraneo + "\" ];"
                nodo += "\nTABLA" + identificador + " -> " + str(hash(foraneo)) + ";"
        elif self.tipo == ALTER_TABLE_ADD.CHECKS:
            nodo += "[ label = \"ADD CHECKS\" ]"
            nodo += "\nNAME" + identificador + "[ label = \"" + self.nombre + "\" ];"
            nodo += "\n" + identificador + " -> NAME" + identificador + ";"
            nodo += "\nACTION" + identificador + "[ label = \"" + self.accion + "\" ];"
            nodo += "\n" + identificador + " -> ACTION" + identificador + ";\n"
        else:
            aux = self.accion
            if isinstance(self.accion, tuple):
                aux = self.accion[0].value
                if isinstance(self.accion[1], tuple):
                    aux += "(" + str(self.accion[1][0]) + "," + str(self.accion[1][1]) + ")"
                else:
                    aux += "(" + str(self.accion[1]) + ")"
            elif isinstance(self.accion, str):
                pass
            else:
                aux = self.accion.value
            nodo += "[ label = \"ADD COLUMN " + self.nombre + " " + aux + "\" ];"
        return nodo

    def ejecutar(self, ts):
        if self.tipo == ALTER_TABLE_ADD.FOREIGN_KEY:
            if TRef.constraintExist(DB_ACTUAL.getName(),self.accion[2]):
                return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_integrity_constraint_violation.integrity_constraint_violation), 0) 
            if not TRef.tableExist(DB_ACTUAL.getName(),self.accion[0]):
                return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_fdw_error.fdw_table_not_found), 0) 
            if not TRef.columnExist(DB_ACTUAL.getName(), self.accion[0], self.accion[1]):
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_fdw_error.fdw_invalid_column_number), 0)
            return (self.nombre,self.accion[0],self.accion[1],self.accion[2])
        elif self.tipo == ALTER_TABLE_ADD.MULTI_FOREIGN_KEY:
            if not TRef.tableExist(DB_ACTUAL.getName(),self.accion[0]):
                return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_fdw_error.fdw_table_not_found), 0) 

            #Comparamos que la misma cantidad de ids propios sea igual a la foranea
            if len(self.nombre) != len(self.accion[1]):
                return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_data_exception.data_exception), 0)

            for col in self.accion[1]:
                if not TRef.columnExist(DB_ACTUAL.getName(), self.accion[0], col):
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_fdw_error.fdw_invalid_column_number), 0)

            listaSin = list()
            for i in range(len(self.nombre)):
                listaSin.append( (self.nombre[i], self.accion[0], self.accion[1][i]) )

            return listaSin
        elif self.tipo == ALTER_TABLE_ADD.COLUMN:
            if isinstance(self.accion, tuple):
                if self.accion[1] < 1:
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_data_exception.numeric_value_out_of_range), 0)
            elif isinstance(self.accion, str):
                #Comprobamos que el type a elegir exista
                if not TEnum.enumExist(self.accion):
                    return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.indeterminate_datatype), 0)
        return (self.nombre, self.accion)
# Show Database
class ShowDatabase(Instruccion):
    def __init__(self, like = None):
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

    def ejecutar(self, ts):
        display = 'Databases\n---------------------\n'
        databases = TRef.showDatabases()

        for db in databases:
            display += db + '\n'

        return display

# Drop Database
class DropDatabase(Instruccion):
    def __init__(self, db, existencia = False):
        self.db = db
        self.existencia = existencia

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"DROP DATABASE " + self.db + "\" ];"
        if self.existencia:
            nodo += "\nLIKE" + identificador + "[ label = \"IF EXISTS\" ];"
            nodo += "\n" + identificador + " -> LIKE" + identificador + ";"
        return nodo

    def ejecutar(self, ts):
        if not TRef.databaseExist(self.db):
            if self.existencia:
                return "Drop Database: Database doesn't exist"
            else:
                return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_invalid_schema_name.invalid_schema_name), 0)

        DBMS.dropDatabase(self.db)
        TRef.dropDatabase(self.db)

        return 'Successful database dropped'

class DropTable(Instruccion):
    def __init__(self, tabla):
        self.tabla = tabla

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"DROP TABLE " + self.tabla + "\" ];"

        return nodo

    def ejecutar(self, ts):
        if DB_ACTUAL.getName() == None:
            return ErrorReport('Semantico', 'Not defined database to used', 0)
        elif not TRef.databaseExist(DB_ACTUAL.getName()):
            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_invalid_schema_name.invalid_schema_name), 0)
        elif not TRef.tableExist(DB_ACTUAL.getName(), self.tabla):
            return ErrorReport('Semantico', sqlErrors.sqlErrorToString(sqlErrors.sql_error_syntax_error_or_access_rule_violation.undefined_table), 0)

        DBMS.dropTable(DB_ACTUAL.getName(), self.tabla)
        TRef.dropTable(DB_ACTUAL.getName(), self.tabla)
        return 'Successful table dropped'        
