class TablaValores:
    def __init__(self, temp = 0, et = 0):
        self.temp = temp
        self.et =et

    def Temp(self):
        '''Retorna la nueva variable temporal t# y la incremeta'''
        var = 't' + str(self.temp)
        self.temp = self.temp + 1
        return var

    def Et(self):
        '''Retorna la nueva etiqueta L# y la incrementa'''
        var = 'L' + str(self.et)
        self.et = self.et + 1
        return var

    def SiguienteEt(self):
        '''Retorna la siguiente equiqueta L# sin modificar el contador'''
        num = self.et
        var = 'L' + str(num)
        return var

    def SiguienteTemp(self):
        '''Retorna el siguiente temporal simbolicamente pues no aumenta el contador'''
        num = self.temp
        var = 't' + str(num)
        return var