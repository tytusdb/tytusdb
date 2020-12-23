# --------------------------- Desarrollo --------------------------- #
# -- Por: Erick Estrada                                           -- #
# -- Git: estrada-usac                                            -- #
# -- Para: USAC -> Ingeniería -> Estructuras De Datos -> Team04   -- #
# ------------------------------------------------------------------ #

class Nodo():

    # Nodo Para BD (Constructor De BD)
    def __init__(self, nameDB):

        # Apuntadores
        self.siguiente = None
        self.anterior = None

        # Data
        self.node_id = nameDB
        self.tablas = None # Apuntador A Lista De Tablas

    # Nodo Para Tabla (Constructor De Tabla)
    def __init__(self, tableName):

        # Apuntadores
        self.siguiente = None
        self.anterior = None

        # Data
        self.node_id = tableName
        self.tabla = None # Apuntador A Isam

# Los Nodos Se Pueden Fusionar Y Optimar En Código
