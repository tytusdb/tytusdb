from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from StoreManager import jsonMode as dbms
from Interprete.CREATE_TABLE import clases_auxiliares
from Interprete.Meta import HEAD
from Interprete.Manejo_errores.ErroresSemanticos import ErroresSemanticos

from Interprete.Manejo_errores.ErroresSintacticos import ErroresSintacticos


##################################
# Patrón intérprete: CREATE TABLE#
##################################

# CREATE TABLE: crear una tabla


class CreateTable(NodoArbol):

    def __init__(self, line, column, id_, columnas_, especificaciones_=None, herencia_=None):
        super().__init__(line, column)
        self.id = id_
        self.columnas = columnas_
        self.especificaciones = especificaciones_
        self.herencia = herencia_
        self.bd_actual = ""
        self.inh = []
        self.ifinh = False

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        # Se obtiene la base de datos actual, la tabla a crear y el numero de colúmnas
        bdactual = entorno.getBD()
        self.bd_actual = bdactual
        nuevatabla = self.id
        nocolumnas = len(self.columnas)
        if self.herencia is not None:
            self.inh = self.definir_inherits(self.herencia.tabla)
            if self.inh is not None:
                self.ifinh = True
                nocolumnas = nocolumnas + len(self.inh)
            else:
                '''
                                            			  ______ _____  _____   ____  _____  
                                            			 |  ____|  __ \|  __ \ / __ \|  __ \ 
                                            			 | |__  | |__) | |__) | |  | | |__) |
                                            			 |  __| |  _  /|  _  /| |  | |  _  / 
                                            			 | |____| | \ \| | \ \| |__| | | \ \ 
                                            			 |______|_|  \_\_|  \_\\____/|_|  \_\

                                            			Descripcion: ocurrio un error o no existe la base de datos
                                            			'''
                Error: ErroresSemanticos = ErroresSemanticos("XX00: internal_error db is not exist", self.linea, self.columna,
                                                             'Create Table')
                arbol.ErroresSemanticos.append(Error)

                print("error")
                #return
        # Se utiliza el paquete de almacenamiento para enviar a crear una nueva tabla y se obtiene un retorno
        retorno = dbms.createTable(bdactual, nuevatabla, nocolumnas)
        if retorno == 0:  # Si la operacion exitosa
            primarykeys = self.crear_pks()  # Se verifican si existen llaves primarias
            if len(primarykeys) != 0:
                pks = self.obtenerindice(primarykeys)
                dbms.alterAddPK(bdactual, nuevatabla, pks)  # Se crean las llaves primarias
                cadena = "tytus> La tabla '" + self.id + "' fue creada exitosamente"
                print("tytus> La tabla '" + self.id + "' fue creada exitosamente")
                arbol.console.append(cadena)
            else:
                pks = self.obtenerindice(primarykeys)
                if len(pks) != 0:
                    dbms.alterAddPK(bdactual, nuevatabla, pks)  # Se crean las llaves primarias
            self.crear_encabezados(bdactual, entorno, arbol)  # Se crean los encabezados de las columnas
        elif retorno == 1:  # Error en la operacion
            '''
                                        			  ______ _____  _____   ____  _____  
                                        			 |  ____|  __ \|  __ \ / __ \|  __ \ 
                                        			 | |__  | |__) | |__) | |  | | |__) |
                                        			 |  __| |  _  /|  _  /| |  | |  _  / 
                                        			 | |____| | \ \| | \ \| |__| | | \ \ 
                                        			 |______|_|  \_\_|  \_\\____/|_|  \_\

                                        			Descripcion: error en la operacion
                                        			'''
            Error: ErroresSemanticos = ErroresSemanticos("XX00: internal_error error en la operacion", self.linea,
                                                         self.columna,
                                                         'Create Table')
            arbol.ErroresSemanticos.append(Error)
            print("Nel error")
        elif retorno == 2:  # La base de datos no existe
            '''
                                        			  ______ _____  _____   ____  _____  
                                        			 |  ____|  __ \|  __ \ / __ \|  __ \ 
                                        			 | |__  | |__) | |__) | |  | | |__) |
                                        			 |  __| |  _  /|  _  /| |  | |  _  / 
                                        			 | |____| | \ \| | \ \| |__| | | \ \ 
                                        			 |______|_|  \_\_|  \_\\____/|_|  \_\

                                        			Descripcion: no existe la base de datos
                                        			'''
            Error: ErroresSemanticos = ErroresSemanticos("XX00: internal_error db is not exist", self.linea,
                                                         self.columna,
                                                         'Create Table')
            arbol.ErroresSemanticos.append(Error)
            print("Nel no existe la bd")

        elif retorno == 3:  # La tabla ya existe
            '''
                                        			  ______ _____  _____   ____  _____  
                                        			 |  ____|  __ \|  __ \ / __ \|  __ \ 
                                        			 | |__  | |__) | |__) | |  | | |__) |
                                        			 |  __| |  _  /|  _  /| |  | |  _  / 
                                        			 | |____| | \ \| | \ \| |__| | | \ \ 
                                        			 |______|_|  \_\_|  \_\\____/|_|  \_\

                                        			Descripcion: la tabla 'self.id' ya existe
                                        			'''
            Error: ErroresSemanticos = ErroresSemanticos("XX01: internal_error id ya existe", self.linea,
                                                         self.columna,
                                                         'Create Table')
            arbol.ErroresSemanticos.append(Error)
            print("Nel ya existe la tabla")

    def crear_encabezados(self, bdactual, entorno, arbol):
        encabezados = []
        if self.ifinh is True:
            for item in self.inh:
                encabezados.append(item)
        for columna in self.columnas:
            encabezados.append(self.setear_atributos(columna, entorno, arbol))
        dbms.insert(bdactual, self.id, encabezados)

    def setear_atributos(self, columna, entorno, arbol):
        cadena = columna.nombre + ',' + columna.tipo + ','
        if columna.atributos is not None:
            cadena += self.isDefault(columna, entorno, arbol)
            cadena += self.isNotNull(columna)
            cadena += self.isNull(columna)
            cadena += self.isUnique(columna)
            cadena += self.isForeignKey(columna)
            cadena += self.isPrimaryKey(columna)
            cadena += self.isCheck(columna, entorno, arbol)
        elif self.especificaciones is not None:
            cadena += ',0,0,'
            cadena += self.isUniqueEspec(columna)
            cadena += self.isForeignKey(columna)
            cadena += self.isPrimaryKeyEspec(columna)
            cadena += ','
        else:
            cadena += ',0,0,,,0,,'
        return cadena

    def isDefault(self, columna, entorno, arbol):
        for atributo in columna.atributos:
            if isinstance(atributo, clases_auxiliares.Default):
                nuevovalor = atributo.valor.execute(entorno, arbol)
                return str(nuevovalor.data) + ','
        return ','

    def isNotNull(self, columna):
        for atributo in columna.atributos:
            if isinstance(atributo, clases_auxiliares.NotNull):
                return '1,'
        return '0,'

    def isNull(self, columna):
        for atributo in columna.atributos:
            if isinstance(atributo, clases_auxiliares.Null):
                return '1,'
        return '0,'

    def isUnique(self, columna):
        for atributo in columna.atributos:
            if isinstance(atributo, clases_auxiliares.Unique):
                if atributo.constraint is not None:
                    return str(atributo.constraint.nombre) + ':' + str(columna.nombre) + ','
                else:
                    return str(self.bd_actual) + '_' + str(self.id) + '_' + str(columna.nombre) + '_unique,'
        if self.especificaciones is not None:
            for espec in self.especificaciones:
                if isinstance(espec, clases_auxiliares.UniqueC):
                    for col in espec.columnas:
                        if col == columna.nombre:
                            return str(self.bd_actual) + '_' + str(self.id) + '_' + str(columna.nombre) + '_unique,'
        return ','

    def isUniqueEspec(self, columna):
        if self.especificaciones is not None:
            for espec in self.especificaciones:
                if isinstance(espec, clases_auxiliares.UniqueC):
                    for col in espec.columnas:
                        if col == columna.nombre:
                            return str(self.bd_actual) + '_' + str(self.id) + '_' + str(columna.nombre) + '_unique,'
        return ','

    def isForeignKey(self, columna):
        if self.especificaciones is not None:
            for espec in self.especificaciones:
                if isinstance(espec, clases_auxiliares.ForeignKeyC):
                    for col in espec.keys:
                        if col == columna.nombre:
                            return str(columna.nombre) + ':' + str(espec.references.table) + ':' + str(espec.references.columnas[0]) + ','
        return ','

    def isPrimaryKey(self, columna):
        for atributo in columna.atributos:
            if isinstance(atributo, clases_auxiliares.PrimaryKey):
                return '1,'
        if self.especificaciones is not None:
            for espec in self.especificaciones:
                if isinstance(espec, clases_auxiliares.PrimaryKeyC):
                    for key in espec.keys:
                        if key == columna.nombre:
                            return '1,'
        return '0,'

    def isPrimaryKeyEspec(self, columna):
        if self.especificaciones is not None:
            for espec in self.especificaciones:
                if isinstance(espec, clases_auxiliares.PrimaryKeyC):
                    for key in espec.keys:
                        if key == columna.nombre:
                            return '1,'
        return '0,'

    # TODO: Falta resolver las expresiones, por ahora solo recibe numeros y no resuelve si Check viene sin constraint.
    def isCheck(self, columna, entorno, arbol):
        for atributo in columna.atributos:
            if isinstance(atributo, clases_auxiliares.Check):
                opizq = str(atributo.exp.getIzq().origen)
                operador = str(atributo.exp.getTipoOperaRelacional())
                opder = str(atributo.exp.getDer().execute(entorno, arbol).data)
                condicion = opizq + ',' + operador + ',' + opder
                if atributo.constraint is not None:
                    nombre = str(atributo.constraint.nombre)
                    return nombre + ',' + condicion + ','
                else:
                    return str(self.bd_actual) + '_' + str(self.id) + '_' + str(columna.nombre) + '_check,' + str(condicion) + ','
        return ',,,'

    def crear_pks(self):
        pks = []
        for columna in self.columnas:
            if columna.atributos is not None:
                for atributo in columna.atributos:
                    if isinstance(atributo, clases_auxiliares.PrimaryKey):
                        pks.append(columna.nombre)
        if self.especificaciones is not None:
            for especificacion in self.especificaciones:
                if isinstance(especificacion, clases_auxiliares.PrimaryKeyC):
                    for key in especificacion.keys:
                        pks.append(key)
        return pks

    def obtenerindice(self, lista):
        pks = []
        if self.ifinh is False:
            for item in lista:
                pks.append(lista.index(item))
        else:
            cont = 0
            for elemento in self.inh:
                x = elemento.split(',')
                if x[7] == '1':
                    pks.append(cont)
                cont += 1
            total = len(self.inh)
            for item in lista:
                pks.append(lista.index(item) + total)
        return pks

# INHERITS
    def definir_inherits(self, nombre):
        return dbms.extractTable(self.bd_actual, nombre)[0]
