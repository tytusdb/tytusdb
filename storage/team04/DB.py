# --------------------------- Desarrollo --------------------------- #
# -- Por: Erick Estrada                                           -- #
# -- Git: estrada-usac                                            -- #
# -- Para: USAC -> Ingeniería -> Estructuras De Datos -> Team04   -- #
# ------------------------------------------------------------------ #

from Nodo import *

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
