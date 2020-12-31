from enum import Enum
from ast.Expresion import Expresion
from Reportes.Datos import Datos
import Reportes.Errores as Reporte
from ast.Symbol import TIPOVAR as Tipo


class TIPO(Enum) :
    SUM = 1
    REST= 2
    MULT= 3
    DIV= 4
    NORMAL= 10
    ID = 20
class Operacion(Expresion):
    def __init__(self):
        self.tipo     = None
        self.value    = None
        self.line     = 0
        self.column   = 0

    def Value(self,value):
        self.tipo = TIPO.NORMAL
        self.value = value



    def getvalue(self,value):
        decimal = False
        valor = ""
        for letra in value:
            if(letra.isdigit()):
                valor +=letra


        if(valor==""):
            return 0

        return int(valor)

    def getValor(self,entorno,tree):
        if(self.tipo == TIPO.NORMAL):
            return self.valor.getValor(entorno,tree)


        elif(self.tipo == TIPO.ID):
            symbolic = entorno.get(str(self.value))
            if(symbolic == None):
                valueaagregar = Datos("SEMANTICO","No es existe la Variable "+self.value,self.line,self.column)
                Reporte.agregar(valueaagregar)
                return None

            value = symbolic.getValor(entorno,tree)

            return value




    def getTypeofvar(self,entorno,tree):
        value = self.getValor(entorno,tree)
        if isinstance(value, str):
            return Tipo.STRING
        elif isinstance(value, int):
            return Tipo.ENTERO
        elif isinstance(value, float):
            return Tipo.DOBLE
        elif (value == True or value == False):
            return Tipo.BOOL
        else:
            return Tipo.NULL
