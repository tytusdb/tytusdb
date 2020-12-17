from ast.Expresion import Expresion
from Valor.Asignacion import Asignacion


class Label(Expresion) :
    def __init__(self, id, ins,linea,columna) :
        self.id = id
        self.sentencias = ins
        self.line = line
        self.column = column

    def ejecutar(self,entorno,tree):
        salir = False

        for Expres in self.ins:
            try:
                if(Expres.ejecutar(entorno,tree) == True):
                    return True
            except:
                pass

            sig = tree.nextlabel(self.id)
            if(sig!=None):
                if(sig.ejecutar(entorno,tree) == True):
                    return True

        return False


def getTipo(self):
        return "LABEL"
