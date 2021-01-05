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

        #Etiquetas e instrucciones ELSIF
        contador2 = 0
        for e in instancia.listaElsif:
            # condicion, inst
            cadenaIf += "\tlabel ." + str(listaEtiquetas[contador2]) + " \n"
            if e.inst != 0:
                cadenaIf += "\tprint(\"elsif\")"
                cadenaIf += self.Traducir2(e.inst)
            cadenaIf += "\tgoto ." + salto+ "\n" + "\n"
            contador2 += 1

        #Etiqueta e instrucciones ELSE
        cadenaIf += "\tlabel ." + falso + "\n"
        # Si el if trae instruciones en ELSE
        if instancia.instElse != None:
            if instancia.instElse != 0:
                cadenaIf += "\tprint(\"falso\")"+"\n"
                cadenaIf += self.Traducir2(instancia.instElse)
        cadenaIf += "\tlabel ."+salto+"\n"

        if isinstance(instancia.condicion.exp1, ExpresionValor) and instancia(instancia.condicion.exp2, ExpresionValor):
            original = "if " + str(condicion) + ": goto ."+verdadero+" else: goto."+falso
            # OPTIMIZACION REGLA 4 y 5
            if instancia.condicion.operador == OPERACION_RELACIONAL.IGUALQUE:
                if instancia.condicion.exp1.val == instancia.condicion.exp2.val:
                    co = "\tgoto ."+verdadero + "- Regla: 4"
                    o = Optimizacion(original, co)
                    listaOpt.append(o)

            original2 = "if " + str(condicion) + ": goto ."+verdadero+" else: goto."+falso
            if instancia.condicion.operador == OPERACION_RELACIONAL.IGUALQUE:
                if instancia.condicion.exp1.val != instancia.condicion.exp2.val:
                    co = "goto ."+falso + "- Regla: 5"
                    o = Optimizacion(original2, co)
                    listaOpt.append(o)

        return cadenaIf

    def t_Funciones_(self, instancia):
        global t_global, cadenaFuncion, ambitoFuncion, cadenaExpresion
        # temporal, nombre, tipo, tam, pos, rol ,ambito
        cadenaF = "\n"
        fun = t_global.varFuncion()
        metodo = tipoSimbolo(str(fun),instancia.Nombre, 'Integer', 0, 0, 'Metodo','')
        t_global.agregarSimbolo(metodo)
        cadenaF += "\tlabel ."+fun+"\n"
        ambitoFuncion = str(instancia.Nombre)
        cadenaF += "\t#**** Funcion *****\n"
        cadenaF +="\n\t# Parametros \n"
        for param in instancia.Parametros:
            #print(str(param.Nombre)+"---"+str(param.Tipo))

            tempoP = t_global.varParametro()
            cadenaF +="\t"+str(tempoP)+ "\n"

            p = tipoSimbolo(str(tempoP), param.Nombre, param.Tipo, 1, 1, 'parametro', instancia.Nombre)
            t_global.agregarSimbolo(p)

        # Temporal de retorno
        cadenaF +="\n\t# Retorno \n"
        tempoP = t_global.varRetorno()
        cadenaF +="\tglobal "+str(tempoP) + "\n"
        p = tipoSimbolo(str(tempoP), "return", "return", 1, 1, 'local', instancia.Nombre)
        t_global.agregarSimbolo(p)

        cadenaF += "\n\t# Declaraciones \n"
        for decla in instancia.Declaraciones:
            if decla != None:
                cadenaexp = ""
                r,cadenaexp = self.procesar_expresion(decla.expresion, t_global)
                cadenaExpresion = ""
                cadenaF += cadenaexp
                tempo = t_global.varTemporal()
                cadenaF +="\t"+str(tempo) + " = " + str(r) + "\n"
                v = tipoSimbolo(str(tempo), decla.id, decla.tipo, 1, 1, 'local', instancia.Nombre)
                t_global.agregarSimbolo(v)
        cadenaF += "\t#Fin declaraciones\n\n"
        #instrucciones
        codigo: Code_Funciones = instancia.Codigo
        cadenaF += self.Traducir2(codigo.Codigo)

        #llamamos al Recorrido del cuerpo
        #cadenaF += self.RecorrerCuerpoCodigo(codigo.Codigo,instancia.Nombre)

        anterior = "R"
        cadenaF += "\n\tgoto ."+anterior
        cadenaF += "\n\n"

        return cadenaF

    def t_Procedimientos_(self, instancia):
        global t_global, cadenaFuncion, ambitoFuncion, cadenaExpresion
        # temporal, nombre, tipo, tam, pos, rol ,ambito
        cadenaF = "\n"
        fun = t_global.varFuncion()
        metodo = tipoSimbolo(str(fun),instancia.Nombre, 'Integer', 0, 0, 'Metodo','')
        t_global.agregarSimbolo(metodo)
        cadenaF += "\tlabel ."+fun+"\n"
        ambitoFuncion = str(instancia.Nombre)
        cadenaF += "\t#**** Procedimiento *****\n"
        cadenaF +="\n\t# Parametros \n"
        for param in instancia.Parametros:
            #print(str(param.Nombre)+"---"+str(param.Tipo))

            tempoP = t_global.varParametro()
            cadenaF +="\t"+str(tempoP)+ "\n"

            p = tipoSimbolo(str(tempoP), param.Nombre, param.Tipo, 1, 1, 'parametro', instancia.Nombre)
            t_global.agregarSimbolo(p)

        # Temporal de retorno
        cadenaF +="\n\t# Retorno \n"
        tempoP = t_global.varRetorno()
        cadenaF +="\tglobal "+str(tempoP) + "\n"
        p = tipoSimbolo(str(tempoP), "return", "return", 1, 1, 'local', instancia.Nombre)
        t_global.agregarSimbolo(p)

        cadenaF += "\n\t# Declaraciones \n"
        for decla in instancia.Declaraciones:
            if decla != None:
                cadenaexp = ""
                r,cadenaexp = self.procesar_expresion(decla.expresion, t_global)
                cadenaExpresion = ""
                cadenaF += cadenaexp
                tempo = t_global.varTemporal()
                cadenaF +="\t"+str(tempo) + " = " + str(r) + "\n"
                v = tipoSimbolo(str(tempo), decla.id, decla.tipo, 1, 1, 'local', instancia.Nombre)
                t_global.agregarSimbolo(v)
        cadenaF += "\t#Fin declaraciones\n\n"
        #instrucciones
        codigo: Code_Funciones = instancia.Codigo
        cadenaF += self.Traducir2(codigo.Codigo)

        #llamamos al Recorrido del cuerpo
        #cadenaF += self.RecorrerCuerpoCodigo(codigo.Codigo,instancia.Nombre)
        #self.Traducir2(instancia.Instrucciones)


        anterior = "R"
        cadenaF += "\n\tgoto ."+anterior
        cadenaF += "\n\n"

        return cadenaF

    def t_asignacion(self, asignacion):
        # id, expresion, llamarFuncion
        global t_global, cadena, cadenaFuncion, ambitoFuncion, cadenaExpresion, listaAsignaciones, listaOpt
        cadenaAsi = ""
        if isinstance(asignacion.expresion,EjecucionFuncion):
            local = ambitoFuncion
            ambitoFuncion = asignacion.expresion.Id

            etiR = "-"
            for fun in t_global.tablaSimbolos:
                f: tipoSimbolo = t_global.obtenerSimbolo(fun)
                if f.ambito == asignacion.expresion.Id and f.rol == "local" and f.nombre == "return":
                    etiR = f.temporal


            ambitoFuncion = local
            # buscamos temporal de la variable.
            temp = "-"
            for var in t_global.tablaSimbolos:
                t: tipoSimbolo = t_global.obtenerSimbolo(var)
                if t.nombre == asignacion.id and t.ambito == ambitoFuncion:
                    temp = t.temporal

            cadenaAsi += self.t_llamadaFuncion(asignacion.expresion)

            cadenaAsi += "\n\t" + str(temp) + " = " + str(etiR) + "\n"
            return cadenaAsi
        else:
            etiR = ""
            for sim in t_global.tablaSimbolos:
                s: tipoSimbolo = t_global.obtenerSimbolo(sim)
                if s.nombre == asignacion.id and s.ambito == ambitoFuncion:
                    etiR = s.temporal

            exp,cadenaexp = self.procesar_expresion(asignacion.expresion, t_global)
            cadenaAsi += cadenaexp
            cadenaAsi += "\t" + str(etiR) + " = " + str(exp) + "\n\n"

            #insertando asignaciones
            objeto = OAs.OptAsignacion(str(etiR), str(exp))
            listaAsignaciones.append(objeto)

            cadenaExpresion = ""
            return cadenaAsi

    def t_llamadaFuncion(self, llamada):
        # Id, Lista-Parametros
        global t_global, cadena, ambitoFuncion, stack, cadenaExpresion
        cadenallamada  = ""
        cadenallamada += "\n\t#Llamada a funcion o procedimiento."
        temp = ambitoFuncion
        ambitoFuncion = llamada.Id
        listaParametros = []
        if llamada.Parametros != None:
            for param in llamada.Parametros:
                c = ""
                exp,c = self.procesar_expresion(param, t_global)
                cadenaExpresion = ""
                listaParametros.append(str(exp))
        #print("lista")
        #print(listaParametros)


        cont = 0
        for sim in t_global.tablaSimbolos:
            s: tipoSimbolo = t_global.obtenerSimbolo(sim)
            if s.ambito == ambitoFuncion and str(s.rol) == "parametro":
                #print("cccccccccccccccccccccccccccccccccccccccccccccccccc"+str(cont))
                cadenallamada += "\n\t"+str(s.temporal) +"="+ str(listaParametros[cont])
                cont += 1

        salto = t_global.varFuncion()
        cadenallamada += "\n\tstack.append(\""+salto+"\")"
        # llamada goto a la funcion
        for met in t_global.tablaSimbolos:
            m: tipoSimbolo = t_global.obtenerSimbolo(met)
            if m.nombre == llamada.Id and m.rol == "Metodo":
                cadenallamada += "\n\tgoto ."+str(m.temporal)
        cadenallamada += "\n\tlabel ."+salto

        ambitoFuncion = temp
        del listaParametros[:]
        return cadenallamada

    def t_retornoFuncion(self, instancia):
        global ambitoFuncion, t_global, cadenaExpresion
        cadenaRetorno = "\n\n\t# Return"
        for item in t_global.tablaSimbolos:
            v: tipoSimbolo = t_global.obtenerSimbolo(item)
            if v.nombre == "return" and v.ambito == ambitoFuncion:
                r = str(v.temporal)

        exp, c = self.procesar_expresion(instancia.Expresion, t_global)
        cadenaExpresion = ""
        cadenaRetorno += c
        cadenaRetorno += "\n\t"+str(r)+" = "+str(exp)+"\n"

        anterior = "R"
        cadenaRetorno += "\tgoto ."+anterior
        cadenaRetorno += "\n\n"

        return cadenaRetorno

