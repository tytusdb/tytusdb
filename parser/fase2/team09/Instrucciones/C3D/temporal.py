from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo

class temporal():
    def __init__(self, temp, tipo):
        self.temp = temp
        self.tipo = tipo

    def get_temp(self):
        return 't'+ str(self.temp)