from optimizacion.Instrucciones.TablaSimbolos.InstruccionC3D import InstruccionC3D
from optimizacion.Instrucciones.C3D.ExpresionesOpti import ExpresionesOpti
class AsignacionC3D(InstruccionC3D):

    def __init__(self, id, op1, op2, valor, linea, columna):
        InstruccionC3D.__init__(self,linea,columna)
        self.id = id
        self.valor = valor
        self.op1 = op1
        self.op2 = op2
        print("ENTRO A Asignacion")
        
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(" linea: " + str(self.linea) + " columna: " + str(self.columna))
        if self.op2 == None:
            if isinstance(self.op1, ExpresionesOpti) :
                cadena = ""
                if(self.op1.id == "instruccion.ejecutar"):
                    return "\t"+".".join(self.id) + " = " + self.op1.ejecutar(tabla, arbol)
                cadena += self.op1.ejecutar(tabla, arbol)
                return ".".join(self.id) + " = " + cadena
            else :
                return ".".join(self.id) + " = " + str(self.op1)

        elif self.op1 == None :
            return self.id +".ejecutar(" + self.op2 + ","+self.valor+")"
        else :
            expresion1 = ""
            expresion2 = ""
            if isinstance(self.op1, ExpresionesOpti):
                expresion1 = self.op1.ejecutar(tabla, arbol)
            else :
                expresion1 = str(self.op1)

            if isinstance(self.op2, ExpresionesOpti):
                expresion2 = self.op2.ejecutar(tabla, arbol)
            else:
                expresion2 = str(self.op2)

            if(self.id == "rs" and self.op1 == "crear_tabla"):
                return "\t" + self.id + "." + self.op1 + "(" +self.valor + ")"
            elif self.op2 == "]":
                return self.id + "." + self.op1 + " = []"
            elif self.op2 == ")":
                return self.id + "." + self.op1 + "("+self.valor+")"
            elif self.op2 == "True" or self.op2 == "False":
                return self.id + "." + expresion1 +" = " + expresion2
            else:
                return self.id + "[" + expresion1 +"] = " + expresion2
         
    def getOp1(self):
        return self.op1

    def getOp2(self):
        return self.op2

    def getC3D(self):
        cadena = ""
        if(self.op1):
            res = self.op1
            if(isinstance(res, (float, int, str))):
                cadena += str(self.id) + " = " +  res
            else:    
                op1 = res.id
                op2 = res.op2
                operador = res.op1
                cadena += str(self.id) + " = " + str(op1) + " " + str(operador) + " " + str(op2) 
        return cadena
            