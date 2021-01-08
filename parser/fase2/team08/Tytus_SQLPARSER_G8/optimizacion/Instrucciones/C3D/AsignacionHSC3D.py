from optimizacion.Instrucciones.TablaSimbolos.InstruccionC3D import InstruccionC3D

class AsignacionHSC3D(InstruccionC3D):
    

    def _init_(self, id, op1, op2, operador, linea, columna):
        InstruccionC3D.__init__(self, linea, columna)
        self.id = id
        self.op1 = op1
        self.op2 = op2
        self.operador = operador

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

        






