from optimizacion.Instrucciones.TablaSimbolos.InstruccionC3D import InstruccionC3D

class ExpresionesOpti(InstruccionC3D):

    def __init__(self, id, op1, op2, linea, columna):
        InstruccionC3D.__init__(self,linea,columna)
        self.id = id
        self.op1 = op1
        self.op2 = op2
        print("ENTRO A expresion opti")
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("linea" + str(self.linea) + " columna: " + str(self.columna))
        cadena1 = ""
        cadena2 = ""

        if isinstance(self.id, ExpresionesOpti):
            cadena1 = self.id.ejecutar(tabla, arbol)
        else:
            ca = str(self.id)
            cadena1 = ca.replace("\\n", '\"\\n\"')

        if isinstance(self.op2, ExpresionesOpti):
            cadena2 = self.op2.ejecutar(tabla, arbol)
        else:
            cadena2 = str(self.op2)

        if self.op1 == "[":
            return cadena1 + " ["+ cadena2 + "]"
        elif self.op1 == "(":
            
            return cadena1 + "(" + cadena2 + ")"
        elif self.id == "[":
            if self.op1 == None:
                return "[]"
            else:
                if isinstance(self.op1, ExpresionesOpti):
                    cadena = self.op1.ejecutar(tabla,arbol)
                    return "[" + cadena + "]"  
                else :
                    return "[" + self.op1 + "]"

        elif self.id == "(":

            return "( " + self.op1 + ")"
        else:
            return cadena1 + " " + self.op1 + " " + cadena2
             

'''
    def getEstructuraString(self):
        if (self.operador == None and self.op2 == None ) or (self.operador == "" and self.op2 == ""):
            return self.op1
        
        return f"{self.op1} {self.operador} {self.op2}"

    def getC3D(self):
        if (self.operador == None and self.op2 == None ) or (self.operador == "" and self.op2 == ""):
            return f"{self.id} = {self.op1}"
        
        return f"{self.id} = {self.op1} {self.operador} {self.op2}"

    def getExpresion(self):
        if (self.operador == None and self.op2 == None ) or (self.operador == "" and self.op2 == ""):
            return self.op1
        
        return f"{self.op1} {self.operador} {self.op2}"

    def getOp1(self):
        if self.op1 == None or self.op1 == "":
            return ""

        return self.op1

    def getOp2(self):
        if self.op2 == None or self.op2 == "":
            return ""

        return self.op2
'''