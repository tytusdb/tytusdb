from optimizacion.Instrucciones.TablaSimbolos.InstruccionC3D import InstruccionC3D

class ImportFrom(InstruccionC3D):

    def __init__(self, fro, imp, importas ,linea, columna):
        InstruccionC3D.__init__(self,linea,columna)
        self.fro = fro
        self.imp = imp
        self.importas = importas
        print("ENTRO A import")
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if self.fro == None :
            if(len(self.imp) > 0):
                return "import "+ ".".join(self.imp) + " " + self.importas
            else:
                return "import "+ "."+str(self.imp) + " " + self.importas
        else:
            if(isinstance(self.fro,str)):
                return "from "+"."+ str(self.fro)+" import "+self.imp + " " + self.importas
            else:
                return "from "+"." .join(self.fro)+" import "+self.imp + " " + self.importas

        print(" linea: " + str(self.linea) + " columna: " + str(self.columna))
