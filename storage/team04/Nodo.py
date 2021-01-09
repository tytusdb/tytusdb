# --------------------------- Desarrollo --------------------------- #
# -- Por: Erick Estrada                                           -- #
# -- Git: estrada-usac                                            -- #
# -- Para: USAC -> Ingeniería -> Estructuras De Datos -> Team04   -- #
# ------------------------------------------------------------------ #

class Nodo():

    # Constructor De Nodo Para Lista De BD o Lista De Tablas
    # Como Parametro Se Pasa El Nombre BD o Nombre De Tabla
    def __init__(self, node_id):

        # Apuntadores
        self.siguiente = None
        self.anterior = None

        # Data
        self.node_id = node_id # Nombre De BD o Nombre De Tabla
        self.data = None # Apuntador A Lista De Tablas O Isam
