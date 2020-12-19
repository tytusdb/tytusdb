
from .simboloColumna import TiposDatos

class Simbolo():

    def __init__(self):
        self.nombreColumna = None   #Guarda el nombre de una columna, cuando viene dentro de expresion, este tipo de dato esta en la clase simboloColumna TiposDatos
        self.tipoDatoRetorno = None  #Guarda el tipo de dato de retorno, columna, int, varchar, date, datetime, etc.
        self.valorRetorno = None     #Guarda el valor como tal que se va a retornar



    def crearSimboloPrimitivo(self,tipoDatoRetorno,valorRetorno):
        self.tipoDatoRetorno = tipoDatoRetorno
        self.valorRetorno = valorRetorno
    
    def crearSimboloColumna(self,nombreColumna):
        self.tipoDatoRetorno = TiposDatos.columna
        self.nombreColumna = nombreColumna

