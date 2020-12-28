import json
import sys, os.path
import os

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\storageManager')
sys.path.append(storage)

error_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\ERROR')
sys.path.append(error_path)

response_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\Response')
sys.path.append(response_path)

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\typeChecker\\')
sys.path.append(storage)


from jsonMode import * 

from typeChecker.typeChecker import *
from Error import Error
from Response.Response import Response

tc = TypeChecker()

class Reference():
    def __init__(self, columnTable, tableReference, columnReference, nameConstraint):
        self.columnTable = columnTable
        self.tableReference = tableReference
        self.columnReference = columnReference
        self.nameConstraint = nameConstraint

class Column():
    def __init__(self):
        self.name = None
        self.type = None
        self.specificType = None
        self.default = None
        self.isNull = None
        self.isUnique = None
        self.uniqueName = None
        self.size = None
        self.isPrimary = None
        self.referencesTable = None
        self.isCheck = None
        self.referenceColumn = None

    def buscarColumnaValida(self, nombreColumna, tipoColumna, tablaReferencia):
        with open('src/Config/Config.json') as file:
            config = json.load(file)
        if config['databaseIndex'] == None:
            return False
        useDB = config['databaseIndex'].upper()
        listaColumnas = tc.return_columnsJSON(useDB,tablaReferencia.upper())
        for columna in listaColumnas:
            if columna['name'].upper() == nombreColumna.upper(): 
                if columna['specificType'] == tipoColumna:
                    return True
        return False

    def asignarTipoCol(self,entrada):
        tiposDato = {
            "SMALLINT":1,
            "INTEGER":1,
            "BIGINT":1,
            "DECIMAL":1,
            "NUMERIC":1,
            "REAL":1,
            "DOUBLE PRECISION":1,
            "MONEY":1,
            "CHARACTER VARYING": 2,
            "VARCHAR":2,
            "CHARACTER":2,
            "CHAR":2,
            "TEXT":2,
            "TIME":3,
            "DATE":3,
            "TIME WITH TIME ZONE" : 3,
            "TIME WITHOUT TIME ZONE" : 3,
            "BOOLEAN": 4
        }
        try:
            return tiposDato[entrada]
        except ValueError:
            return 3
    
    def tipo_declaracion(self, parent):
        # Pasos para validar
        # Siempre se va a recibir el nodo TIPO_DECLARACION, este puede tener más de un nodo
        # 1. Se deben de recorrer los hijos en caso de que tenga un tipo de dato que concatene
        #   dos o más palabras
        # 2. Si el nodo tiene nombre ENTERO significa que es el tamaño de la columna
        # 3. Si el nodo tiene nombre TIME_OPCINALES significa que entra a zona horaria o no.
        # 3.1 Se debe de recorrer el nodo TIME_OPCIONALES para validar si se tiene un timeZone o 
        #     un tamaño como entero
        tipoDato = ""
        for hijo in parent.hijos:
            if hijo.nombreNodo == "ENTERO":
                self.size = hijo.valor
            elif hijo.nombreNodo =="TIME_OPCIONALES":
                for hijoOpcional in hijo.hijos:
                    if hijoOpcional.nombreNodo == "ENTERO":
                        self.size = hijoOpcional.valor
                    else:
                        if tipoDato != "":
                            tipoDato = tipoDato + " " + hijoOpcional.nombreNodo
                        else:
                            tipoDato = hijoOpcional.nombreNodo
            else:
                if tipoDato!= "":
                    tipoDato = tipoDato + " " + hijo.nombreNodo
                else:
                    tipoDato = hijo.nombreNodo
        self.type = self.asignarTipoCol(tipoDato.upper())
        
    def ejec_atributo_check(self, parent, listaChecker, listaids):
        # Siempre se recibirá un nodo OPCIONALES_ATRIBUTO_CHECK
        # 1. Recorrer cada uno de los hijos buscando el nombre de la constraint.
        # 2. Si se encuentra el nodo OPCIONAL_CONSTRAINT tiene un alias en el hijo 0
        # 3. Si se encuentra el nodo E, se tiene que construir la expresion JSON.
        nuevoCheck = Check()
        for hijo in parent.hijos:
            if hijo.nombreNodo == "OPCIONAL_CONSTRAINT":
                nuevoCheck.name = hijo.hijos[0].valor.upper()
            elif hijo.nombreNodo == "E":
                nuevoCheck.checkExp = self.construirExpresionJSON(hijo, listaids)
        listaChecker.append(nuevoCheck)
        resp = Response("00000","Se agrego la constraint exitosamente")
        return resp
            
    def ejec_atributo_primary(self):
        # Verifica que no sea una primary key ya, en caso de que haya una, va a retornar un error
        if self.isPrimary == None:
            self.isPrimary = True
            resp = Response("00000","Se agrego la PK exitosamente")
            return resp
        respError = Error(3,"Ya se declaro esta columna como llave primaria "+self.name,-1)
        responseMessage = Response("20000", respError)
        return responseMessage
    
    def ejec_atributo_references(self, parent):
        # Siempre se va a recibir un nodo con el nombre OPCIONALES_ATRIBUTO_REFERENCES
        # Solo tendrá un hijo y es el nombre de la tabla.
        # Se debe de buscar que la columna tenga el mismo nombre y se debe de verificar
        # que tenga el mismo tipo de dato
        if self.buscarColumnaValida(self.name, self.specificType, parent.hijos[0].nombreNodo):
            self.referencesTable = parent.hijos[0].nombreNodo
            self.referenceColumn = self.name.upper()
            responseMessage = Response("00000", "Se agrego la referencia correctamente")
            return responseMessage
        respError = Error(3,"No existe una columna o tabla relacionada para la referencia "+self.name+" en " +parent.hijos[0].nombreNodo ,-1)
        responseMessage = Response("20000", respError)
        return responseMessage

    def ejec_atributo_unique(self, parent):
        # Siempre se recibirá un nodo
        if self.isUnique != None:
            respError = Error(3,"Ya se declaro esta columna como unique "+self.name,-1)
            responseMessage = Response("20000", respError)
            return responseMessage
        self.isUnique = True
        for hijo in parent.hijos:
            if hijo.nombreNodo == "OPCIONAL_CONSTRAINT":
                self.uniqueName = hijo.valor.upper()
        responseMessage = Response("00000", "Se agrego unique correctamente")
        return responseMessage

    def crearColumna(self, parent, checkers, listaids):
        # Pasos para crear una columna.
        # Siempre se va a recibir el nodo que contenga el nombre ATRIBUTO_COLUMNA
        # 1. Verificar cada uno de los nodos.
        # 1.1 El nodo que tenga como nombre IDENTIFICADOR, será el nombre de la columna,
        # 1.2 El nodo que tenga como nombre TIPO_DECLARACION, será el tipo de la columna
        # 1.3 El nodo que tenga como nombre OPCIONALES_ATRIBUTO_PRIMARY, será el que indique que es una llave primaria
        # 1.4 El nodo que tenga como nombre OPCIONALES_ATRIBUTO_UNIQUE, será el que indique que es un campo unique
        # 1.5 El nodo que tenga como nombre OPCIONALES_ATRIBUTO_REFERENCES, será el que indique que es una referencia.
        # 1.6 El nodo que tenga como nombre OPCIONALES_ATRIBUTO_CHECK, será el que indique que es una check.

        # Ejecuta 1.1
        self.name = parent.hijos[0].valor.upper()
        # Ejecuta 1.2
        self.tipo_declaracion(parent.hijos[1])
        # Ejecuta 1.3 -> 1.6
        for hijo in parent.hijos:
            if hijo.nombreNodo == "OPCIONALES_ATRIBUTO_PRIMARY":
                response = self.ejec_atributo_primary()
                if response.code != "00000":
                    return response
            elif hijo.nombreNodo == "OPCIONALES_ATRIBUTO_UNIQUE":
                response = self.ejec_atributo_unique(hijo)
                if response.code != "00000":
                    return response
            elif hijo.nombreNodo == "OPCIONALES_ATRIBUTO_REFERENCES":
                response = self.ejec_atributo_references(hijo)
                if response.code != "00000":
                    return response
            elif hijo.nombreNodo == "OPCIONALES_ATRIBUTO_CHECK":
                response = self.ejec_atributo_check(hijo, checkers, listaids)
                if response.code != "00000":
                    return response
        resp = Response("00000","Se creo la columna exitosamente")
        return resp

    def construirExpresionJSON(self, parent, listaids):
        if len(parent.hijos) == 3 :
            obj1 = self.construirExpresionJSON(parent.hijos[0], listaids)
            obj2 = self.construirExpresionJSON(parent.hijos[2], listaids)
            jsonExpresion = {
                'E0' : obj1,
                'operador' : parent.hijos[1].nombreNodo,
                'E1' : obj2
            }
            return jsonExpresion
        elif len(parent.hijos) == 2:
            jsonExpresion = {
                'nodo0' : self.construirExpresionJSON(parent.hijos[0], listaids),
                'nodo1' : self.construirExpresionJSON(parent.hijos[1], listaids)
            }
            return jsonExpresion
        elif len(parent.hijos) == 1:
            jsonExpresion = {
                'nombre' : parent.hijos[0].nombreNodo,
                'valor' : parent.hijos[0].valor
            }
            if parent.hijos[0].nombreNodo.upper() == "IDENTIFICADOR":
                listaids.append(parent.hijos[0].valor)
            return jsonExpresion

class Check():
    def __init__(self):
        self.name = None
        self.checkExp = None

class Constraint():
    def __init__(self):
        self.nombre = None
        self.listaColumnas = []

    def crearConstraintPrimary(self, parent, columns):
        # Pasos para construir la llave Primaria
        # 1. Siempre se va a recibir un nodo ATRIBUTO_PRIMARY_KEY
        # 2. Se debe de recorrer cada uno de los nodos de este para asociar cada columna a
        #    un identificador. 
        # 3. Se inserta cada uno de los ids en la listaColumnas.
        # 4. Se busca cada uno de los id's de listaColumnas en columns para colocar
        #    las llaves primarias que sean necesarias.
        for hijo in parent.hijos:
            if hijo.nombreNodo == "IDENTIFICADOR":
                self.listaColumnas.append(hijo.valor)
        
        for col in self.listaColumnas:

            if not self.buscarColumna(columns,col):
                respError = Error(3,"No se encuentra la columna " +col,-1)
                responseMessage = Response("20000", respError)
                return responseMessage
        responseMessage = Response("00000", "Se creo la llave primaria")
        return responseMessage

    def crearConstraintReferences(self, parent, columns):
        #Pasos para crear una Referencia
        # 1. Siempre se va a encontrar un nodo con nombre ATRIBUTO_REFERENCES
        # 2. Se debe de recorrer cada uno de los nodos.
        # 3. Se crea la lista colOrigen para insertar las columnas de la tabla original ATRIBUTO_FOREIGN_KEY
        # 4. Se crea la lista colDestino para insertar las columnas de referencia LISTA_IDS
        # 5. Se busca la tabla a la que se hace referencia y se extraen las columnas
        # 6. Se buscan las columnas de colOrigen en las columnas ya hechas en la misma tabla
        # 7. Se buscan las columnas de colDestino en las columnas de la tabla de referencia
        # 8. Si colOrigen y colDestino tienen la misma longitud, se puede realizar
        # 9. Si colOrigen es vacío, se puede asignar
        # 10. Si no coinciden las longitudes, no se puede realizar la referencia.

        # Paso 1 - 4
        colOrigen = []
        colDestino = []
        tablaDestino = ""
        for hijo in parent.hijos:
            if hijo.nombreNodo == "ATRIBUTO_FOREIGN_KEY":
                for col in hijo.hijos[0].hijos:
                    colOrigen.append(col.valor.upper())
            elif hijo.nombreNodo == "IDENTIFICADOR":
                tablaDestino = hijo.valor
            elif hijo.nombreNodo == "LISTA_IDS":
                for col in hijo.hijos:
                    colDestino.append(col.valor.upper())
        
        # Paso 5 
        if not self.buscarTablaEnDB(tablaDestino):
            respError = Error(3,"No se encuentra la tabla "+ tablaDestino,-1)
            responseMessage = Response("20000", respError)
            return responseMessage
        listaColumnas = self.extraerColumnasDeTabla(tablaDestino)

        # Paso 6 Esto es opcional, no siempre va a venir
        for col in colOrigen:
            if not self.buscarColumna(columns,col):
                respError = Error(3,"No se encuentra la columna referida "+ col,-1)
                responseMessage = Response("20000", respError)
                return responseMessage

        # Paso 7 Esto si es obligatorio.
        for col in colDestino:
            if not self.buscarColumna(listaColumnas,col):
                respError = Error(3,"No se encuentra la columna referida "+ col,-1)
                responseMessage = Response("20000", respError)
                return responseMessage
            
        # Paso 8 - 10
        if len(colOrigen) == 0:
            colOrigen = colDestino
        elif len(colOrigen) != len(colDestino):
            respError = Error(3,"El numero de columnas referenciadas no coinciden",-1)
            responseMessage = Response("20000", respError)
            return responseMessage
        
        for col in columns:
            if col.name.upper() in colOrigen :
                col.referenceColumn = colOrigen.index(col.name.upper())
                col.referenceTable = tablaDestino.upper()
        responseMessage = Response("00000", "Se crearon las referencias")
        return responseMessage

    def crearConstraintCheck(self, parent, listaids, columns, checkers):
        # Pasos para crear un Check
        # Siempre se recibe un nodo OPCIONALES_ATRIBUTO_CHECK
        # 1. Recorrer los nodos hijos.
        # 2. Si hay un nodo OPCIONAL_CONSTRAINT se encuentra el nombre de la constraint check (opcional)
        # 3. Si hay un nodo LISTA_EXP se encontrarán los id's que serán los ids que hay que buscar.
        # 4. Dentro de la lista de ID's verificar que todos vengan en la lista de columnas
        # 5. Si todas están, insertar.
        nombreCheck = ""
        for hijo in parent.hijos:

            if hijo.nombreNodo == "OPCIONAL_CONSTRAINT":
                nombreCheck = hijo.hijos[0].valor.upper()
            elif hijo.nombreNodo == "LISTA_EXP":
                for exp in hijo.hijos:
                    nuevaConstraint = Check()
                    nuevaConstraint.name = nombreCheck.upper()
                    nuevaConstraint.checkExp = self.construirExpresionJSON(exp, listaids)
                    checkers.append(nuevaConstraint)
        for ident in listaids:
            if not self.buscarColumna(columns,ident):
                respError = Error(3,"No se encuentra la columna  "+ident+" en la tabla",-1)
                responseMessage = Response("20000", respError)
                return responseMessage
        responseMessage = Response("00000", "Se creo la constraint correctamente")
        return responseMessage
        
    def buscarTablaEnDB(self, nombreTabla):
        with open('src/Config/Config.json') as file:
            config = json.load(file)
        if config['databaseIndex'] == None:
            return False
        useDB = config['databaseIndex'].upper()
        listaDB = showTables(useDB)
        return nombreTabla.upper() in listaDB
    
    def extraerColumnasDeTabla(self, nombreTabla):
        with open('src/Config/Config.json') as file:
            config = json.load(file)
        if config['databaseIndex'] == None:
            return []
        useDB = config['databaseIndex'].upper()
        listaCol = tc.return_columnsJSON(useDB, nombreTabla.upper())
        listaTemp = []
        for col in listaCol:
            listaCol.append(col['name'])
        return listaTemp
        
    def buscarColumna(self, columns, nombreBusqueda):
        for col in columns:
            if col.name.upper() == nombreBusqueda.upper():
                return True
        return False

    def buscarColumnaP(self, columns, nombreBusqueda):
        for col in columns:
            if col.upper() == nombreBusqueda.upper():
                return True
        return False

    def construirExpresionJSON(self, parent, listaids):
        if len(parent.hijos) == 3 :
            obj1 = self.construirExpresionJSON(parent.hijos[0], listaids)
            obj2 = self.construirExpresionJSON(parent.hijos[2], listaids)
            jsonExpresion = {
                'E0' : obj1,
                'operador' : parent.hijos[1].nombreNodo,
                'E1' : obj2
            }
            return jsonExpresion
        elif len(parent.hijos) == 2:
            jsonExpresion = {
                'nodo0' : self.construirExpresionJSON(parent.hijos[0], listaids),
                'nodo1' : self.construirExpresionJSON(parent.hijos[1], listaids)
            }
            return jsonExpresion
        elif len(parent.hijos) == 1:
            jsonExpresion = {
                'nombre' : parent.hijos[0].nombreNodo,
                'valor' : parent.hijos[0].valor
            }
            if parent.hijos[0].nombreNodo.upper() == "IDENTIFICADOR":
                listaids.append(parent.hijos[0].valor)
            return jsonExpresion

class Table():
    def __init__(self):
        self.name = None
        self.isNull = None
        self.columnas = []
        self.checkers = []
        self.listaids = [] #Solo es temporal, no hay que guardarla
        self.listaReferences = []
        
    def execute(self, parent, enviroment):
        # Siempre se va a recibir un CREATE_TABLE como nodo
        # 1. Recorrer y ejecutar cada uno de los nodos.
        # 2. Si llegó hasta el final, quiere decir que no hay ningun error
        # 3. Verificar que esté seleccionada una base de datos, si lo está crear la tabla.
        # 4. Verificar que no exista la tabla en la base de datos seleccionada
        for hijo in parent.hijos:
            if hijo.nombreNodo == "IDENTIFICADOR" :
                self.name = hijo.valor.upper()
            elif hijo.nombreNodo == "ATRIBUTO_COLUMNA" :
                nuevaColumna = Column()
                resp = nuevaColumna.crearColumna(hijo,self.checkers,self.listaids)
                if resp.code != "00000":
                    return resp
                self.columnas.append(nuevaColumna)
            elif hijo.nombreNodo == "ATRIBUTO_PRIMARY_KEY" :
                nuevaConstraint = Constraint()
                resp = nuevaConstraint.crearConstraintPrimary(hijo, self.columnas)
                if resp.code != "00000":
                    return resp
            elif hijo.nombreNodo == "ATRIBUTO_REFERENCES" :
                nuevaConstraint = Constraint()
                resp = nuevaConstraint.crearConstraintReferences(hijo,self.columnas)
                if resp.code != "00000":
                    return resp
                self.listaReferences.append(nuevaConstraint)
            elif hijo.nombreNodo == "OPCIONALES_ATRIBUTO_CHECK":
                nuevaConstraint = Constraint()
                resp = nuevaConstraint.crearConstraintCheck(hijo,self.listaids, self.columnas, self.checkers)
                if resp.code != "00000":
                    return resp
                

        
        with open('src/Config/Config.json') as file:
            config = json.load(file)
        
        if config['databaseIndex'] == None:
            err_resp = Error(3,"No se ha seleccionado ninguna base de datos.",-1)
            resp = Response("42P12",err_resp)
            return resp
        listTables = showTables(config['databaseIndex'].upper())
        if self.name.upper() in listTables :
            err_resp = Error(3,"Ya existe la tabla.",-1)
            resp = Response("42P12",err_resp)
            return resp
        createTable(config['databaseIndex'].upper(),self.name.upper(),len(self.columnas))
        tc.createTable(config['databaseIndex'].upper(),self.name.upper(),self.columnas)
        resp = Response("00000","Se creó la tabla")
        return resp

    def buscarColumna(self,nombre):
        for column in self.columnas:
            if column.name.upper() == nombre.upper():
                return True
        return False