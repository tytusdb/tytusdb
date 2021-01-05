from Instruccion_pl import *
import Instruccion_pl as OAs
from Temporales import *
from expresiones import *
from sentencias import *
from graphviz import Graph
from graphviz import escape

import os
import Temporales as T
import sentencias as ss
from SqlComandos import SqlComandos as SQL

c3d = []

t_global = T.Temporales()
cadena = ""


GotoList = []




cadenaFuncion = ""
cadenaExpresion = ""
ambitoFuncion = ""

# lista optimizacion
listaOpt = []
listaAsignaciones = []

class Codigo3d:

    def __init__(self):
        global cadena
        self.i = 0
        cadena += "from goto import with_goto\n"
        cadena += "import FuncionesIntermedias as F3D\n"
        cadena += "heap = F3D.heap\n"
        cadena += "stack = []\n\n"
        cadena += "@with_goto \n"
        cadena += "def main(): \n"
        cadena += "\tglobal heap\n"
        cadena += "\tglobal stack\n"

    def retorno(self):
        global cadena
        cadena += "\n\tlabel .R\n"
        cadena += "\tu = stack.pop()"
        cantidad = t_global.varFuncionAnterior()
        i = 1
        cadena += "\n"
        while i < cantidad:
            cadena += "\tif u == \"F"+str(i)+"\": \n"
            cadena += "\t\tgoto .F"+str(i)+"\n"
            i += 1

        cadena += "\n\tlabel .END\n"

    def imprimir(self):
        global cadena
        self.retorno()
        #cadena += "\n\nmain() \n"
        print(cadena)

        c3d.append(cadena)

        self.generar()

        print("----------------------------------SE LIMPIO ----------------------------------------------")
        t_global.limpiar()
        cadena = ""

    def Traducir(self, instrucciones):
        global ts_global, cadena, cadenaFuncion
        for i in instrucciones:
            if isinstance(i,Funciones_):
                cadenaFuncion += self.t_Funciones_(i)
            elif isinstance(i, ss.EjecucionFuncion):
                cadena += self.t_llamadaFuncion(i)
            elif isinstance(i, Procedimientos_):
                cadenaFuncion += self.t_Procedimientos_(i)
            elif isinstance(i, CrearIndice):
                cadena += self.t_CrearIndice(i)
            elif isinstance(i, Insert_Datos):
                cadena += self.t_Insert(i)
            else:
                aux = SQL(i)
                aux.generarCadenaSQL()
                if aux.CadenaSQL is not None:
                    print("PRODUCE SENTENCIA SQL-----------------------------------===")
                    #print(str(aux.CadenaSQL))
                    cadena += "\n" + self.t_sentenciaSQL(aux)
                else:
                    print("NO TRADUCE....")
        cadena += "\n\n\tgoto .END\n"
        cadena += cadenaFuncion

    def Traducir2(self, instrucciones):
        global ts_global, cadenaFuncion
        cadenaT = ""
        contador = 0
        for i in instrucciones:
            if isinstance(i, If_inst):
                cadenaT += self.t_If(i)
            elif isinstance(i, Elsif_inst):
                cadenaT += self.t_ELSIF(i)
            elif isinstance(i, ss.EjecucionFuncion):
                cadenaT += self.t_llamadaFuncion(i)
            elif isinstance(i, Asignacion):
                cadenaT += self.t_asignacion(i)
            elif isinstance(i, ForInstruccion):
                cadenaT += self.t_TraduccionFor(i)
            elif isinstance(i, CaseSimple):
                cadenaT += self.t_TraduccionCaseSimple(i, "")
            elif isinstance(i, RetornoFuncion):
                cadenaT += self.t_retornoFuncion(i)
            elif isinstance(i, CaseBuscado):
                cadenaT += self.t_TraduccionCaseBuscado(i, "")
            elif isinstance(i, Print_I):
                cadenaT += self.t_print(i)
            else:
                aux = SQL(i)
                aux.generarCadenaSQL()
                if aux.CadenaSQL is not None:
                    print("PRODUCE SENTENCIA SQL-----------------------------------===2")
                    #print(str(aux.CadenaSQL))
                    cadenaT += "\n" + self.t_sentenciaSQL(aux)
                else:
                    print("NO TRADUCE....")

            contador += 1
        return cadenaT

    def t_print(self, id):
        global  t_global
        resultado = ""
        cadena = ""
        for item in t_global.tablaSimbolos:
            v: tipoSimbolo = t_global.obtenerSimbolo(item)
            if v.nombre == id.id and v.ambito == ambitoFuncion:
                resultado = v.temporal

        cadena += "\n\tprint(\" |>> \" + str("+str(resultado)+")) \n"
        return cadena

    def t_If(self, instancia):
        global t_global, cadena, cadenaExpresion
        cadenaIf  =""
        cadenaIf += "\t# ------ If ------- \n"
        #print(instancia.condicion)
        condicion, cad = self.procesar_expresion(instancia.condicion, t_global)
        cadenaExpresion = ""
        cadenaIf += cad
        verdadero = str(t_global.etiquetaT())
        falso = str(t_global.etiquetaT())
        salto = str(t_global.etiquetaT())

        cadenaIf += "\tif " + str(condicion) + ": \n"
        cadenaIf += "\t\tgoto ."+verdadero+"\n"
        cadenaIf += "\telse: \n"
        cadenaIf += "\t\tgoto ."+falso+"\n"

        cadenaIf += "\tlabel ." + verdadero + "\n"
        cadenaIf += "\tprint(\"verdadero\")"+"\n"
        # Si el if trae instruciones en IF
        if instancia.instIf != 0:
            cadenaIf += self.Traducir2(instancia.instIf)
        cadenaIf += "\tgoto ."+salto+"\n"+"\n"
        cadenaIf += "\tlabel ." + falso + "\n"
        # Si el if trae instruciones en ELSE
        if instancia.instElse != None:
            if instancia.instElse != 0:
                cadenaIf += "\tprint(\"falso\")"+"\n"
                cadenaIf += self.Traducir2(instancia.instElse)
        cadenaIf += "\tlabel ."+salto+"\n"

        original = "if " + str(condicion) + ": goto ."+verdadero+" else: goto."+falso
        # OPTIMIZACION REGLA 4 y 5
        if isinstance(instancia.condicion.exp1, ExpresionValor) and instancia(instancia.condicion.exp2, ExpresionValor):
            if instancia.condicion.operador == OPERACION_RELACIONAL.IGUALQUE:
                if instancia.condicion.exp1.val == instancia.condicion.exp2.val:
                    co = "goto ."+verdadero + "- Regla: 4"
                    o = Optimizacion(original, co)
                    listaOpt.append(o)

            original2 = "if " + str(condicion) + ": goto ."+verdadero+" else: goto."+falso
            if instancia.condicion.operador == OPERACION_RELACIONAL.IGUALQUE:
                if instancia.condicion.exp1.val != instancia.condicion.exp2.val:
                    co = "goto ."+falso + "- Regla: 5"
                    o = Optimizacion(original2, co)
                    listaOpt.append(o)

        return cadenaIf

    def t_ELSIF(self, instancia):
        # condicion, instIf, listaElsif,instElse
        global t_global, cadena, cadenaExpresion
        cadenaIf  =""
        cadenaIf += "# ---- If-Elsif ----\n"

        # condicion if
        #print(instancia.condicion)
        condicion, cad = self.procesar_expresion(instancia.condicion, t_global)
        cadenaExpresion = ""
        cadenaIf += cad

        # condiciones elsif
        etiquetasCondiciones = []
        for c in instancia.listaElsif:
            # condicion, inst
            condi, ca = self.procesar_expresion(c.condicion, t_global)
            cadenaIf += ca
            etiquetasCondiciones.append(condi)

        # etiqueta verdadero, falso y salto
        verdadero = str(t_global.etiquetaT())
        falso = str(t_global.etiquetaT())
        salto = str(t_global.etiquetaT())

        cadenaIf += "\tif " + str(condicion) + ": \n"
        cadenaIf += "\t\tgoto ."+verdadero+"\n"

        # por cada elsif
        listaEtiquetas = []
        contador = 0
        for e in instancia.listaElsif:
            # condicion, inst
            v = str(t_global.etiquetaT())
            cadenaIf += "\telif " + str(etiquetasCondiciones[contador]) + ": \n"
            cadenaIf += "\t\tgoto ."+str(v)+"\n"
            listaEtiquetas.append(v)
            contador += 1

        cadenaIf += "\telse: \n"
        cadenaIf += "\t\tgoto ."+falso+"\n"

        #Etiqueta e instruccion IF
        cadenaIf += "\n\tlabel ." + verdadero + "\n"
        cadenaIf += "\tprint(\"verdadero\")"
        # Si el if trae instruciones en IF
        if instancia.instIf != 0:
            cadenaIf += self.Traducir2(instancia.instIf)
        cadenaIf += "\tgoto ."+salto+"\n"+"\n"
