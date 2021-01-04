# --------------------------- Desarrollo --------------------------- #
# -- Por: Erick Estrada                                           -- #
# -- Git: estrada-usac                                            -- #
# -- Para: USAC -> Ingeniería -> Estructuras De Datos -> Team04   -- #
# ------------------------------------------------------------------ #

from Nodo import *
from Lista import *
from binario import *

class DB():

    # Constructor De Administrador
    def __init__(self):
        self.list_ = Lista()

    # ----------- Administrador De Bases De Datos ----------- #

    # ------------- Método Crear Base De Datos ------------- #
    # Parametros:   database -> Nombre De BD A Crear
    # Retorno:      [0] Operación Exitosa
    #               [1] Error
    #               [2] BD Ya Existe
    def createDatabase(self, database):

        # Verificar Si BD(database) Ya Existe
        if self.list_.Search(database) == 0: # BD No Existe

            # Insertar Nueva BD
            self.list_.Insert(database)

            # Binario
            binario.commit(self.showDatabases(), "bases")

            return 0 # Operación Exitosa

        else: # BD Ya Existe

            return 2 # BD Ya Existe

    # ------------- Método Mostrar Base De Datos ------------- #
    # Parametros:   Ninguno
    # Retorno:      [] Lista Vaacia (No Existen BD)
    #               [Llena] Lista De Bases De Datos
    def showDatabases(self):

        # Lista Que Retonranrá
        self.BD_list = []

        # Recorrer Lista De BD Y Agregarlas A Lista De Retorno
        self.rec_BD = self.list_.primero
        while self.rec_BD != None:

            self.BD_list.append(self.rec_BD.node_id) # Aqui Puede Ser Solo Pasar ID Y No El Nodo Depende El Buscado
            self.rec_BD = self.rec_BD.siguiente

        # Retornar Lista De BD
        return self.BD_list

    # Método Para Interfaz (Obtener Lista De BD)
    def get_all(self):

        # Lista Retorno
        self.BD_list = []
        self.BD_list = self.showDatabases()


    # ------------- Método Update Base De Datos ------------- #
    # Parametros:   databaseOld -> Nombre De BD A Modificar
    #               databaseNew -> Nuevo Nombre De BD
    # Retorno:      [0] Operación Exitosa
    #               [1] Error
    #               [2] databaseOld No Existe
    #               [3] databaseNew Ya Existe
    def alterDatabase(self, databaseOld, databaseNew):

        # Buscar BD Para Obtener Nodo
        self.BD_old = self.list_.Search(databaseOld)
        if self.BD_old == 0: # No Encontro La BD

            return 2 #databaseOld No Existe

        else: # Encuentra La BD

            # Buscar De Nuevo En Lista De BD Si El Nuevo Nodo Ya Está En Uso
            self.BD_new = self.list_.Search(databaseNew)
            if self.BD_new == 0: # No Existe La BD

                # Actualizar
                #self.BD_old.data.Update(parametros) Otra Opción
                self.BD_old.node_id = databaseNew

                # Binario
                binario.commit(self.list_.showDatabases(), "bases")

                return 0 # Operación Exitosa

            else: # Nuevo Nombre Ya Existe

                return 3 # databaseNew Ya Existe


    # ------------- Método Delete Base De Datos ------------- #
    # Parametros:   database -> Nombre De BD A Eliminar
    # Retorno:      [0] Operación Exitosa
    #               [1] Error
    #               [2] BD No Existe
    def dropDatabase(self, database):

        # Verificar Si BD Existe
        self.DB_delete = self.list_.Search(database)
        if self.DB_delete == 0: # BD No Existe

            return 2 # BD No Existe

        else: # BD Existe

            # Eliminar
            self.list_.Delete(database)

            # Binario
            binario.commit(self.showDatabases(), "bases")

            return 0 # Operación Exitosa

    # ------------ Administrador De Tablas De BD ------------ #

    # ------------- Método Crear Tabla En BD ------------- #
    # Parametros:   database -> Nombre De BD A Eliminar
    #               table -> Nombre De Tabla A Crear
    #               numberColumns -> Numero De Columnas De Los Registros
    # Retorno:      [0] Operación Exitosa
    #               [1] Error
    #               [2] BD No Existe
    #               [3] Tabla Ya Existe
    def createTable(self, database, table, numberColumns):

        # Obtener Nodo BD
        self.DB = self.list_.Search(database)

        # Verificar Si BD No Existe
        if self.DB == 0:

            return 2 # BD No Existe

        else: # BD Existe

            # Intentar Insertar Tabla
            self.insert_Table = self.DB.data.Search(table)

            # Verificar Si Tabla No Existe
            if self.insert_Table == 0:

                # Tabla No Existe, Insertar Tabla
                self.DB.data.InsertIsam(table)

                # Binario
                binario.commit(self.DB.data.Search(table).data, self.DB.node_id + "_" + table)

                return 0 # Operación Exitosa

            else: # Tabla Ya Existe

                return 3 # Tabla Ya Existe

    # ------------- Método Mostrar Tablas De BD ------------- #
    # Parametros:   database -> Nombre De BD A Eliminar
    # Retorno:      [] Lista Vacia
    #               [Llena] Lista De Tablas
    def showTables(self, database):
        # Lista De Retorno
        self.tables_List = []

        # Obtener Nodo De La Base De Datos
        self.DB = self.list_.Search(database)

        # Recorrer Lista De Tablas Y Agregarlas A Lista De Retorno
        self.rec_T = self.DB.data.primero
        while self.rec_T != None:
            self.tables_List.append(self.rec_T.node_id)
            self.rec_T = self.rec_T.siguiente

        # Retornar Lista De Tablas
        return self.tables_List


    # Método Para Interfaz (Obtener Lista De Tablas)
    def get_all2(self ):

        # Lista Retorno
        self.T_list = []
        self.T_list = self.showTables()






#
