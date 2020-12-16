
class Errores():
    def __init__(self, id,error,fila,columna,lexema):
        self.id = id
        self.error = error
        self.fila = fila
        self.columna = columna
        self.lexema = lexema

    def __init__(self,id,error):
        self.id = id
        self.error = error
        self.fila = -1
        self.columna = -1
        self.lexema =''

    def set_columna(self,col):
        self.columna = col
    
    def set_fila(self,fil):
        self.fila = fil

    def set_lexema(self,lex):
        self.lexema = lex