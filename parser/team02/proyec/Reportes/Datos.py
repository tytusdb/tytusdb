class Datos():
    def __init__(self,tipo,descripcion,line,column):
        self.tipo = tipo
        self.error = descripcion
        self.line = str(line)
        self.column = str(column)
