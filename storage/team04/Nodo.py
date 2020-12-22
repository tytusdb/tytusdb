# --------------------------- Desarrollo --------------------------- #
# -- Por: Erick Estrada                                           -- #
# -- Git: estrada-usac                                            -- #
# -- Para: USAC -> Ingeniería -> Estructuras De Datos -> Team04   -- #
# ------------------------------------------------------------------ #

class Nodo():
    def __init__(self, nameDB):
        # Apuntadores
        self.siguiente = None
        self.anterior = None

        # Data
        self.nameDB = nameDB
        self.tablas = None
