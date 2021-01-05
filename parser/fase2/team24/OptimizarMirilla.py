from graphviz import Graph
import OptimizarObjetos as obj #Objetos utilizados en el optimizador mirilla

CodigoOptimizado = [] #Se guarda el codigo optimizado resultante para el reporte
ResultadoFinal = [] #Se guarda el resultado final de la optimizacion

class Optimizador:
    def __init__(self, Asignaciones = []):
        #Asignaciones = Pila de instrucciones del codigo de tres direcciones
        self.Asignaciones = Asignaciones

    #Metodos para realizar la optimizacion segun la regla.
    #Retornan False si no se cumple la regla de optimizacion y True si se cumple y se optimiza
    def Regla_1(self):
        "Regla 1"
        return False
       
    def Regla_2(self):
        "Regla 2"
        return False

    def Regla_3(self):
        "Regla 3"
        return False

    def Regla_4(self):
        "Regla 4"
        return False

    def Regla_5(self):
        "Regla 5"
        return False

    def Regla_6(self):
        "Regla 6"
        return False

    def Regla_7(self):
        "Regla 7"
        return False

    def Regla_8_9(self, asignacion):
        "(+)Regla 8 y (-)Regla 9 - Eliminacion de codigo"
        global CodigoOptimizado
        indice = asignacion.indice
        op1 = asignacion.operador2
        op2 = asignacion.operador2
        signo = asignacion.signo
        if (indice == op1 and op2 == '0' and (signo == '+' or signo == '-')) or (indice == op2 and op1 == '0' and (signo == '+' or signo == '-')):
            if signo == '+':
                NuevoObjeto = obj.Optimizado("Regla 8", indice + " = " + op1 + " " + signo + " " + op2, "Se elimino la instruccion")
                CodigoOptimizado.append(NuevoObjeto)
                return True
            elif signo == "-":
                NuevoObjeto = obj.Optimizado("Regla 9", indice + " = " + op1 + " " + signo + " " + op2, "Se elimino la instruccion")
                CodigoOptimizado.append(NuevoObjeto)
                return True
        else:
            return False

    def Regla_10_11(self):
        "(*)Regla 10 y (/)Regla 11"
        return False
        
    def Regla_12_13(self):
        "(+)Regla 12 y (-)Regla 13"
        return False

    def Regla_14_15(self):
        "(*)Regla 14 y (/)Regla 15"
        return False

    def Regla_16(self):
        "Regla 16"
        return False

    def Regla_17_18(self):
        "(*)Regla 17 y (/)Regla18"
        return False

    def GenerarReporte(self):
        "Generar el reporte en graphviz"
