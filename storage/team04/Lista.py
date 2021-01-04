# --------------------------- Desarrollo --------------------------- #
# -- Por: Erick Estrada                                           -- #
# -- Git: estrada-usac                                            -- #
# -- Para: USAC -> Ingeniería -> Estructuras De Datos -> Team04   -- #
# ------------------------------------------------------------------ #

from Nodo import *
from isam import *

class Lista():

    # Constructor De Lista
    def __init__(self):

        # Apuntadores
        self.primero = None
        self.ultimo = None

    # ------------- Método Insertar Nodo En Lista ------------- #
    # Parametros:   node_id -> Nombre De BD o De Tabla
    # Retorno:      [0] Operación Exitosa
    def Insert(self, node_id):

        # Verificar Si La Lista Está Vacia
        if self.primero == None: # Lista Vacia

            # Insertar Primer Nodo De La Lista
            nuevo_Nodo = Nodo(node_id)
            self.primero = nuevo_Nodo
            self.ultimo = nuevo_Nodo

            # Inicializar Lista De Tablas
            nuevo_Nodo.data = Lista()

            return 0 # Operación Exítosa

        else: # Ya Existen Otros Nodos (BD o Tablas)

            # Inserta Nuevo Nodo Al Final De La Lista
            nuevo_Nodo = Nodo(node_id)
            self.ultimo.siguiente = nuevo_Nodo
            self.ultimo.siguiente.anterior = self.ultimo
            self.ultimo = nuevo_Nodo

            # Inicializar Lista De Tablas
            nuevo_Nodo.data = Lista()

            return 0 # Operación Exitosa

    def InsertIsam(self, node_id):

            # Verificar Si La Lista Está Vacia
            if self.primero == None: # Lista Vacia

                # Insertar Primer Nodo De La Lista
                nuevo_Nodo = Nodo(node_id)
                self.primero = nuevo_Nodo
                self.ultimo = nuevo_Nodo

                # Inicializar Lista De Tablas
                nuevo_Nodo.data = Isam()

                return 0 # Operación Exítosa

            else: # Ya Existen Otros Nodos (BD o Tablas)

                # Inserta Nuevo Nodo Al Final De La Lista
                nuevo_Nodo = Nodo(node_id)
                self.ultimo.siguiente = nuevo_Nodo
                self.ultimo.siguiente.anterior = self.ultimo
                self.ultimo = nuevo_Nodo

                # Inicializar Lista De Tablas
                nuevo_Nodo.data = Lista()

                return 0 # Operación Exitosa

    # ------------- Método Buscar Nodo En Lista ------------- #
    # Parametros:   node_id -> Nombre De BD o De Tabla
    # Retorno:      [Nodo] Devuelve Nodo Buscado
    #               [0] Nodo No Existe (BD o Tabla No Existe)
    def Search(self, node_id):

        # Recorrer Lista (De BD o De Tablas)
        self.rec_Nodo = self.primero
        while self.rec_Nodo != None:

            # Verificar Si Nodo Es El Buscado
            if self.rec_Nodo.node_id == node_id:

                return self.rec_Nodo # Nodo Encontrado

            self.rec_Nodo = self.rec_Nodo.siguiente

        return 0 # Nodo No Existe (BD o Tabla No Existe)

    # ------------- Método Update Nodo En Lista ------------- #
    # Parametros:   id_Old -> ID(Nombre) De Nodo Antiguo
    #               id_New -> ID(Nombre) De Nodo Nuevo
    # Retorno:      [0] Operación Exitosa
    def Update(self, id_Old, id_New):

        # Obtener Nodo A Actualizar
        self.node_Old = self.Search(id_Old)

        # Actualizar Nodo
        self.node_Old.node_id = id_New

    # ------------- Método Delete Nodo En Lista ------------- #
    # Parametros:   node_id -> ID De Nodo A Eliminar
    # Retorno:      [0] Operación Exitosa
    def Delete(self, node_id):

        # Obtener Nodo A Eliminar
        self.node_Delete = self.Search(node_id)

        # Eliminar Nodo De Lista
        # Caso 1: Solo Hay Un Nodo En La Lista
        if self.primero == self.ultimo:

            self.primero = None
            self.ultimo = None

            return 0 # Operación Exitosa

        # Caso 2: Es El Ultimo Nodo De La Lista
        elif self.node_Delete.siguiente == None:

            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None

            return 0 # Operación Exitosa

        # Caso 3: Es El Primero
        elif self.primero == self.node_Delete:

            self.primero = self.primero.siguiente

            return 0 # Operación Exitosa

        # Caso 4: Está En Medio
        else:
            self.node_Delete.anterior.siguiente = self.node_Delete.siguiente
            self.node_Delete.siguiente.anterior = self.node_Delete.anterior

            return 0 # Operación Exitosa
