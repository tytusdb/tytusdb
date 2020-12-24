from enum import Enum


class IAT(Enum):
    GLOBAL = 0
    TABLA = 1
    SUBQUERY = 2
    ACCESO = 3
    ACCESO_SIN_ALIAS = 4
    TODO = 5
    TODO_CON_ALIAS = 6
    ACCESO_TYPE = 7


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
        elif tipo_ == 4:
            return IAT.ACCESO_SIN_ALIAS
        elif tipo_ == 7:
            return IAT.ACCESO_TYPE
        else:
            return IAT.SUBQUERY

    def get_origen(self):
        return self.origen
    
    def get_referencia(self):
        return self.referencia

    def get_tipo(self):
        return self.tipo
