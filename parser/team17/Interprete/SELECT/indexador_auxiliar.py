from enum import Enum


class IAT(Enum):
    GLOBAL = 0
    TABLA = 1
    SUBQUERY = 2
    ACCESO = 3
    ACCESO_SIN_ALIAS = 4
    TODO = 5


class indexador_auxiliar:
    def __init__(self, origen_, ref_, tipo_):
        self.origen = origen_
        self.referencia = ref_
        self.tipo = self.get_iat(tipo_)

    def get_iat(self, tipo_):
        if tipo_ == 0:
            return IAT.GLOBAL
        elif tipo_ == 1:
            return IAT.TABLA
        else:
            return IAT.SUBQUERY

    def get_origen(self):
        return self.origen
    
    def get_referencia(self):
        return self.referencia

    def get_tipo(self):
        return self.tipo
