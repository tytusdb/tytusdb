from ast.Sentencia import Sentencia
from ast.Declarevar import Declarevar
from ast.Symbol import TIPOVAR as Tipo
from Valor.Valor import Valor
from Valor.Asignacion import Asignacion
from Reportes.Datos import Datos
import Reportes.Errores as Reporte


class Leer(Sentencia):
    def __init__(self,id,line,column):
        self.id = id
        self.line = line
        self.column = column
        self.declared = None

    def setAmbito(self,ambito):
        self.declared = ambito

    def isfloat(self,a}):
        try:
            v = float(a)
        except ValueError:
            return False
        else:
            return True

    def esentero(self,a):
        try:
            v = float(a)
            b = int(v)
        except ValueError:
            return False
        else:
            return v == b
