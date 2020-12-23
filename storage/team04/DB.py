# --------------------------- Desarrollo --------------------------- #
# -- Por: Erick Estrada                                           -- #
# -- Git: estrada-usac                                            -- #
# -- Para: USAC -> Ingeniería -> Estructuras De Datos -> Team04   -- #
# ------------------------------------------------------------------ #

from Nodo import *
d
class DB():

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def createDatabase(self,database):
        # Verifica Sí La Lista De BD Está Vacia
        if self.primero == None:
            # Insertar Primer BD
            nueva_BD = Nodo(database)
            self.primero = nueva_BD
            self.ultimo = nueva_BD

            return 0
        else: # Ya Existen Otras BD

            # Primero Verifica Que BD Aún No Exista
            if self.searchDB(database) == 1:
                # Base De Datos Ya Existe, No Es Posible Insertar
                return 2
            else:
                # Insertar DB
                nueva_BD = Nodo(database)
                self.ultimo.siguiente = nueva_BD
                self.ultimo.siguiente.anterior = self.ultimo
                self.ultimo = nueva_BD

                return 0

    # Buscar Base De Datos En La Lista
    def searchDB(self,database):
        # Pasa Como Parametro Nombre De BD
        # Retorna 1 Si La Encuentra, 0 Si No

        # Recorrer Lista De BD
        self.rec_BD = self.primero
        while self.rec_BD != None:

            # Verificar Si NodoBD Es El Buscado
            if self.rec_BD.nameDB == database:
                self.var_Return = 1

            self.rec_BD = self.rec_BD.siguiente

        return 0

    # Busca Base De Datos En La Lista Y Retorna El Nodo
    def searchDB2(self,database):
        # Pasa Como Parametro Nombre De BD
        # Retorna Nodo Si La Encuentra, 0 Si No

        # Recorrer Lista De BD
        self.rec_BD = self.primero
        while self.rec_BD != None:

            # Verificar Si NodoBD Es El Buscado
            if self.rec_BD.nameDB == database:
                return self.rec_BD

            self.rec_BD = self.rec_BD.siguiente

        return 0

    # Devolver Listado De Bases De Datos
    def showDatabases(self):
        # Lista Que Se Retornará
        BD_list = []

        # Recorrer Lista De BD Y Agregarlas A Lista De Retorno
        self.rec_BD = self.primero
        while self.rec_BD != None:
            BD_list.append(self.rec_BD.nameDB)
            self.rec_BD = self.rec_BD.siguiente

        # Retornar Lista De BD
        return BD_list

    # UPDATE
    def alterDatabase(self, databaseOld, databaseNew):

        # Buscar BD Para Obtener Nodo
        self.BD_old = self.searchDB2(databaseOld)
        if self.BD_old == 0: # No Encontro La BD
            return 1
        else: # Encuentra La BD
            # Buscar De Nuevo En Lista De BD Si El Nuevo Nombre No Está Ya Utilizado
            self.BD_new = self.searchDB(databaseNew)
            if self.BD_new == 1:
                return 3 # Nuevo Nombre Ya Existe
            else:
                # Actualizar
                self.BD_old.node_id = databaseNew
                return 0

    # DELETE
    def dropDatabase(self, database):
        self.DB_delete = self.searchDB2(database)
        if self.DB_delete == 0: # BD No Existe
            return 2
        else: # BD Existe
            self.DB_delete.anterior.siguiente = self.DB_delete.siguiente
            self.DB_delete.siguiente.anterior = self.DB_delete.anterior
            return 0
