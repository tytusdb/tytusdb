class CTable:
    'Esta clase representa un símbolo dentro de nuestra tabla de símbolos'

    def __init__(self, key, nombreAtr, tipo, tipo1, tipo2, null,llave):
        self.key = key
        self.nombreAtr = nombreAtr
        self.tipo = tipo
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.null = null
        self.llave = llave


class crearTabla:
    'Esta clase representa la tabla de símbolos'

    def __init__(self, simbolos={}):
        self.simbolos = simbolos

    def agregar(self, simbolo):
        self.simbolos[simbolo.id] = simbolo
