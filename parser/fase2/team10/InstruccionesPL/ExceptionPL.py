class ExceptionPL():
    'Esta clase se utiliza para guardar errores de tipo léxico, sintáctico y semántico.'

    def __init__(self,cod_error, tipo, descripcion, linea, columna):
        self.cod_error = cod_error
        self.tipo = tipo
        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna

    def toString(self):
        return "ERROR:  "+self.descripcion+"\nLINEA "+str(self.linea)+":\n\n"+"SQL state: "+str(self.cod_error)+'\n'