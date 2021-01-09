
from .simboloColumna import TiposDatos

class Simbolo():

    def __init__(self):
        self.nombreColumnaIzquierdo = None   #Guarda el nombre de una columna, cuando viene dentro de expresion lado izquierdo, este tipo de dato esta en la clase simboloColumna TiposDatos
        self.nombreColumnaDerecho = None     #Guarda el nombre de la columna, cuando viende dentre de expresion lado derecho
        self.tipoDatoRetorno = None  #Guarda el tipo de dato de retorno, columna, int, varchar, date, datetime, etc.
        self.valorRetorno = None     #Guarda el valor como tal que se va a retornar
        self.descripcionError = None   #Guarda información de error cuando se esta operando expresion
        self.tipDatoCasteo = None      #Guarda el tipo de casteo que se debera realiar al operar Expresion
        self.tipoOperacion = None      #Guarda el tipo de operacion a realizar cuando viene una columna



    def crearSimboloPrimitivo(self,tipoDatoRetorno,valorRetorno):
        self.tipoDatoRetorno = tipoDatoRetorno
        self.valorRetorno = valorRetorno
    
    def crearSimboloColumna(self,nombreColumna):
        self.tipoDatoRetorno = TiposDatos.columna
        self.nombreColumnaIzquierdo = nombreColumna

    def setTipoDatoRetorno(self,tipoDato):
        self.tipoDatoRetorno = tipoDato

    def setDescripcionError(self,descripcion):
        self.descripcionError = descripcion
    
    def setTipoDatosCasteo(self, tipoDato):
        self.tipDatoCasteo = tipoDato

