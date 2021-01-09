from graphviz import Graph
import os
import re
import OptimizarObjetos as obj #Objetos utilizados en el optimizador mirilla
import reportOptimizacion as reporteopt

CodigoOptimizado = [] #Se guarda el codigo optimizado resultante para el reporte
ResultadoFinal = [] #Se guarda el resultado final de la optimizacion

class Optimizador:
    def __init__(self, Asignaciones = []):
        #Asignaciones = Pila de instrucciones del codigo de tres direcciones
        self.Asignaciones = Asignaciones

    def ejecutar(self):
        global CodigoOptimizado
        global ResultadoFinal
        CodigoOptimizado = []
        ResultadoFinal = []
        for objeto in self.Asignaciones:
            if isinstance(objeto, obj.Asignacion):
                if self.Regla_8_9(objeto) or self.Regla_10_11(objeto):
                    "NO SE AGREGA LA INSTRUCCION AL RESULTADO"
                elif self.Regla_12_13(objeto) or self.Regla_14_15(objeto) or self.Regla_16(objeto) or self.Regla_17_18(objeto):
                    "SE AGREGA LA OPTIMIZACION AL RESULTADO"
                    ResultadoFinal.append(CodigoOptimizado[-1].resultado)
                else:
                    "SE AGREGA LA INSTRUCCION ORIGINAL AL RESULTADO"
                    if objeto.signo == None or objeto.operador2 == None:
                        if objeto.cadena == True:
                            instruccion = str(objeto.indice) + " = " + "\'" +  str(objeto.operador1) + "\'"
                        else:
                            instruccion = str(objeto.indice) + " = " + str(objeto.operador1)
                    else:
                        instruccion = str(objeto.indice) + " = " + str(objeto.operador1) + " " + str(objeto.signo) + " " + str(objeto.operador2)
                    ResultadoFinal.append(instruccion)
            else:
                "NO ES OBJETO ASIGNACION ASI QUE SOLO SE AGREGA AL RESULTADO"
                if isinstance(objeto, obj.Temporal):
                    if objeto.cadena == True:
                        Nobjeto = str(objeto.indice) + " = \'" + str(objeto.valor) + "\'"
                        ResultadoFinal.append(Nobjeto)
                    else:
                        Nobjeto = str(objeto.indice) + " = " + str(objeto.valor)
                        ResultadoFinal.append(Nobjeto)
                else:  
                    ResultadoFinal.append(objeto)
        self.GenerarReporte()

    def BuscarTemporal(self, Nombre):
        for elemento in self.Asignaciones:
            if isinstance(elemento, obj.Temporal):
                if elemento.indice == Nombre:
                    return elemento

    #Metodos para realizar la optimizacion segun la regla.
    #Retornan False si no se cumple la regla de optimizacion y True si se cumple y se optimiza
    def Regla_1(self, asignacion, listaasignaciones):
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
        op1 = asignacion.operador1
        op2 = asignacion.operador2
        signo = asignacion.signo
        if self.BuscarTemporal(op1):
            op1 = str(self.BuscarTemporal(op1).valor)
        if self.BuscarTemporal(op2):
            op2 = str(self.BuscarTemporal(op2).valor)
        if (indice == op1 and op2 == '0' and signo == '+') or (indice == op2 and op1 == '0' and signo == '+'):
            NuevoObjeto = obj.Optimizado("Regla 8", indice + " = " + op1 + " " + signo + " " + op2, "Se elimina la instruccion")
            CodigoOptimizado.append(NuevoObjeto)
            return True
        elif indice == op1 and op2 == '0' and signo == '-':
            NuevoObjeto = obj.Optimizado("Regla 9", indice + " = " + op1 + " " + signo + " " + op2, "Se elimina la instruccion")
            CodigoOptimizado.append(NuevoObjeto)
            return True
        else:
            return False

    def Regla_10_11(self, asignacion):
        "(*)Regla 10 y (/)Regla 11"
        global CodigoOptimizado
        indice = asignacion.indice
        op1 = asignacion.operador1
        op2 = asignacion.operador2
        signo = asignacion.signo
        if self.BuscarTemporal(op1):
            op1 = str(self.BuscarTemporal(op1).valor)
        if self.BuscarTemporal(op2):
            op2 = str(self.BuscarTemporal(op2).valor)
        if (indice == op1 and op2 == '1' and signo == '*') or (indice == op2 and op1 == '1' and signo == '*'):
            NuevoObjeto = obj.Optimizado("Regla 10", indice + " = " + op1 + " " + signo + " " + op2, "Se elimina la instruccion")
            CodigoOptimizado.append(NuevoObjeto)
            return True
        elif indice == op1 and op2 == '1' and signo == '/':
            NuevoObjeto = obj.Optimizado("Regla 11", indice + " = " + op1 + " " + signo + " " + op2, "Se elimina la instruccion")
            CodigoOptimizado.append(NuevoObjeto)
            return True
        else:
            return False
        
    def Regla_12_13(self, asignacion):
        "(+)Regla 12 y (-)Regla 13"
        global CodigoOptimizado
        indice = asignacion.indice
        op1 = asignacion.operador1
        op2 = asignacion.operador2
        signo = asignacion.signo
        if self.BuscarTemporal(op1):
            op1 = str(self.BuscarTemporal(op1).valor)
        if self.BuscarTemporal(op2):
            op2 = str(self.BuscarTemporal(op2).valor)
        if op1 == '0' and op2 != '0' and signo == '+' and op2 != indice:
            NuevoObjeto = obj.Optimizado("Regla 12", indice + " = " + op1 + " " + signo + " " + op2, indice + " = " + op2)
            CodigoOptimizado.append(NuevoObjeto)
            return True
        elif op2 == '0' and op1 != '0' and signo == '+' and op1 != indice:
            NuevoObjeto = obj.Optimizado("Regla 12", indice + " = " + op1 + " " + signo + " " + op2, indice + " = " + op1)
            CodigoOptimizado.append(NuevoObjeto)
            return True
        elif op1 != '0' and op2 == '0' and signo == '-' and op1 != indice:
            NuevoObjeto = obj.Optimizado("Regla 13", indice + " = " + op1 + " " + signo + " " + op2, indice + " = " + op1)
            CodigoOptimizado.append(NuevoObjeto)
            return True
        else:
            return False

    def Regla_14_15(self, asignacion):
        "(*)Regla 14 y (/)Regla 15"
        global CodigoOptimizado
        indice = asignacion.indice
        op1 = asignacion.operador1
        op2 = asignacion.operador2
        signo = asignacion.signo
        if self.BuscarTemporal(op1):
            op1 = str(self.BuscarTemporal(op1).valor)
        if self.BuscarTemporal(op2):
            op2 = str(self.BuscarTemporal(op2).valor)
        if op1 == '1' and op2 != '1' and signo == '*' and op2 != indice:
            NuevoObjeto = obj.Optimizado("Regla 14", indice + " = " + op1 + " " + signo + " " + op2, indice + " = " + op2)
            CodigoOptimizado.append(NuevoObjeto)
            return True
        elif op2 == '1' and op1 != '1' and signo == '*' and op1 != indice:
            NuevoObjeto = obj.Optimizado("Regla 14", indice + " = " + op1 + " " + signo + " " + op2, indice + " = " + op1)
            CodigoOptimizado.append(NuevoObjeto)
            return True
        elif op1 != '1' and op2 == '1' and signo == '/' and op1 != indice:
            NuevoObjeto = obj.Optimizado("Regla 15", indice + " = " + op1 + " " + signo + " " + op2, indice + " = " + op1)
            CodigoOptimizado.append(NuevoObjeto)
            return True
        else:
            return False

    def Regla_16(self, asignacion):
        "Regla 16"
        global CodigoOptimizado
        indice = asignacion.indice
        op1 = asignacion.operador1
        op2 = asignacion.operador2
        signo = asignacion.signo
        if self.BuscarTemporal(op1):
            op1 = str(self.BuscarTemporal(op1).valor)
        if self.BuscarTemporal(op2):
            op2 = str(self.BuscarTemporal(op2).valor)
        if op1 == '2' and not isinstance(op2, int) and signo == '*' and op2 != indice:
            NuevoObjeto = obj.Optimizado("Regla 16", indice + " = " + op1 + " " + signo + " " + op2, indice + " = " + op2 + " " + "+" + " " + op2)
            CodigoOptimizado.append(NuevoObjeto)
            return True
        elif op2 == '2' and not isinstance(op1, int) and signo == '*' and op1 != indice:
            NuevoObjeto = obj.Optimizado("Regla 16", indice + " = " + op1 + " " + signo + " " + op2, indice + " = " + op1 + " " + "+" + " " + op1)
            CodigoOptimizado.append(NuevoObjeto)
            return True
        else:
            return False

    def Regla_17_18(self, asignacion):
        "(*)Regla 17 y (/)Regla18"
        global CodigoOptimizado
        indice = asignacion.indice
        op1 = asignacion.operador1
        op2 = asignacion.operador2
        signo = asignacion.signo
        if self.BuscarTemporal(op1):
            op1 = str(self.BuscarTemporal(op1).valor)
        if self.BuscarTemporal(op2):
            op2 = str(self.BuscarTemporal(op2).valor)
        if op1 == '0' and signo == '*' and op2 != indice:
            NuevoObjeto = obj.Optimizado("Regla 17", indice + " = " + op1 + " " + signo + " " + op2, indice + " = 0")
            CodigoOptimizado.append(NuevoObjeto)
            return True
        elif op2 == '0' and signo == '*' and op1 != indice:
            NuevoObjeto = obj.Optimizado("Regla 17", indice + " = " + op1 + " " + signo + " " + op2, indice + " = 0")
            CodigoOptimizado.append(NuevoObjeto)
            return True
        elif op1 == '0' and signo == '/' and op2 != indice:
            NuevoObjeto = obj.Optimizado("Regla 18", indice + " = " + op1 + " " + signo + " " + op2, indice + " = 0")
            CodigoOptimizado.append(NuevoObjeto)
            return True
        else:
            return False

    def GenerarReporte(self):
        global CodigoOptimizado
        "Generar el reporte en graphviz y el archivo de optimizacion"
        #PARA EL ARCHIVO
        Nombre = "Salidas/CodigoOptimizado.py"
        texto = ""
        for elem in ResultadoFinal:
            if isinstance(elem, obj.Temporal):
                texto += str(elem.indice) + " = " + str(elem.valor) + "\n"
            else:
                texto += elem + "\n"
        try:
            os.makedirs(os.path.dirname(Nombre), exist_ok=True)
            with open(Nombre, "w") as f:
                f.write('''
from datetime import date
from variables import tabla as ts
from variables import NombreDB 
from variables import cont 
import tablaDGA as TAS
import sql as sql 
import mathtrig as mt
from reportTable import *
    
    
pila = []
for i in range(100):
    pila.append(i)
    
def ejecutar():
\tglobal cont
\tglobal ts
\tNombreDB = ts.nameDB
\n''')
                f.write(texto)
                f.write('''ejecutar()''')
                f.close()
        except:
            print("No se pudo generar el archivo del codigo generado")
        #PARA REPORTE
        reporteopt.graphTable(CodigoOptimizado)
