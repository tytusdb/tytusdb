from Instruccion_pl import *
import ts as TS
import Instruccion_pl as OAs
from Temporales import *
from expresiones import *
from sentencias import *
from graphviz import Graph
from graphviz import escape
ts_global = TS.TablaDeSimbolos()

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
            if isinstance(i, Funciones_):
                cadenaFuncion += self.t_Funciones_(i)
            elif isinstance(i, ss.EjecucionFuncion):
                cadena += self.t_llamadaFuncion(i)
            elif isinstance(i, Drop_fun_proc):  # eliminar funcion o procedimiento.
                self.t_dropFuncProc(i)
            elif isinstance(i, Procedimientos_):
                cadenaFuncion += self.t_Procedimientos_(i)
            elif isinstance(i, CrearIndice):
                cadena += self.t_CrearIndice(i)
            elif isinstance(i, Insert_Datos):
                cadena += self.t_Insert(i)
            elif isinstance(i, SelectExpresion):
                if isinstance(i.listaCampos[0].Columna, ss.EjecucionFuncion):
                    v, cad = self.procesar_ejecucion_funcion(i.listaCampos[0].Columna, None)
                    cadena += cad + "\n"
                    aux = '"SELECT \'" + str(' + v + ') + "\';"\n'
                    cadena += "\t" + str(v) + " = " + aux
                    cadena += "\theap.append(" + str(v) + ")\n"
                    cadena += "\tF3D.ejecutarSQL()\n"

                else:
                    aux = SQL(i)
                    aux.generarCadenaSQL()
                    if aux.CadenaSQL is not None:
                        print("PRODUCE SENTENCIA SQL-----------------------------------===")
                        # print(str(aux.CadenaSQL))
                        cadena += "\n" + self.t_sentenciaSQL(aux)
                    else:
                        print("NO TRADUCE....")
            else:
                aux = SQL(i, ts_global, t_global, ambitoFuncion)
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
            elif isinstance(i, Insert_Datos):
                cadenaT += self.t_Insert(i)
            else:
                aux = SQL(i, ts_global, t_global, ambitoFuncion)
                aux.generarCadenaSQL()
                if aux.CadenaSQL is not None:
                    print("PRODUCE SENTENCIA SQL-----------------------------------===2")
                    #print(str(aux.CadenaSQL))
                    cadenaT += "\n" + self.t_sentenciaSQL(aux)
                else:
                    print("NO TRADUCE....")

            contador += 1
        return cadenaT

    def t_dropFuncProc(self, instancia):
        global ts_global
        eliminar = ""
        for ob in ts_global.FuncProc:
            o = ts_global.obtenerFuncProc(ob)
            if str(o.Nombre) == str(instancia.id):
                eliminar = o.Nombre

        ts_global.eliminarFuncProc(eliminar)

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
        global t_global, cadenaFuncion, ambitoFuncion, cadenaExpresion, ts_global
        ts_global.agregarFuncProc(instancia)
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
        cadenaF +="\t"+str(tempoP) + "= 0\n"
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
        global t_global, cadenaFuncion, ambitoFuncion, cadenaExpresion, ts_global
        ts_global.agregarFuncProc(instancia)
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
        cadenaF +="\t"+str(tempoP) + " = 0\n"
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

        baderaC = False

        for recorrets in t_global.tablaSimbolos:
                tsTemporal = t_global.obtenerSimbolo(recorrets)
                if str(tsTemporal.nombre) == str(llamada.Id) :
                    baderaC = True

        if baderaC:
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
        else:
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



#--------------------------------  TRADUCCION CUERPO DE LA FUNCION
    def RecorrerCuerpoCodigo(self,Instrucciones,Ambito):
        #Objetos para diferenciar
        if(isinstance(Instrucciones,list)):
            print("Viene una lista de codigo..")
            #Recorremos la lista
            #Miramos las instancias que trae
            for elemento in Instrucciones:
                if(isinstance(elemento,CaseSimple)):
                    #Nos bamos a la Generacion del codigo del case
                    print("Encontre el Case Simple")
                    self.t_TraduccionCaseSimple(elemento,Ambito)
                elif(isinstance(elemento,CaseBuscado)):
                    print("Encontre el Case Buscado")
        else:
            print("Viene epsilon en la produccion")


#--------------------------------   TRADUCCION CASE SIMPLE
    def t_TraduccionCaseSimple(self,Objeto:CaseSimple, Ambito):
        #Objetos globales para la traduccion
        global t_global
        cadena = "\t#----- CASE SIMPLE --------- \n"
#-------#Viene Expresion_Busqueda  => ExpresionValor(ID)
        #Creamor un temporal con el valor que va a tener
        Variable:ExpresionValor = Objeto.busqueda
# -------#viene CElse(CodigoEpsilon) =>
        #Objetemos el else
        vari1: CElse = Objeto.caseelse
        #busqueda, listawhen, caseelse
#-------#viene Lista_When =>Lista => CSWhen(Cs_Expresion, CodigoCuerpoEpsilon) => Cs_Expresion=> Lista => Lista de expresines
        cadena += self.RecorrerListaWhensCS(Objeto.listawhen,Ambito,Variable,vari1)
        return cadena

    # Recorremos la lista de Whens Case Simple
    def RecorrerListaWhensCS(self, lista,Ambito,Variable,Else):
        cadena = ""
        contador = len(lista)
        ifaux = None
        while contador > 0:
            element = lista[contador - 1]
            ele: CSWhen = element
            print(ele)
            if contador == len(lista):
                explogica = self.Recorrido_InstruccionesCS(ele.expresiones, Ambito, Variable)
                elseaux = None
                if Else is not None:
                    elseaux = Else.sentencias
                ifaux = If_inst(explogica, element.sentencias, elseaux)
            else:
                explogica = self.Recorrido_InstruccionesCS(ele.expresiones, Ambito, Variable)
                ifaux = If_inst(explogica, element.sentencias, [ifaux])
            contador = contador - 1
        if ifaux is not None:
            cadena += self.t_If(ifaux)

        return cadena

    #Recorremos la lista de instrucciones
    def Recorrido_InstruccionesCS(self, listaIns, Ambito, Variable):

        contador=0
        exp1 = None
        exp2 = None
        explogica = None
        for ele in listaIns:

            #Recorremos los tipos de instruccines
            if isinstance(ele,ExpresionAritmetica) or isinstance(ele, ExpresionValor):
                print("Viene un alista de instrucciones aritmeticas.. ")
                if contador == 0:
                    exp1 = ExpresionRelacional(Variable, ele, OPERACION_RELACIONAL.IGUALQUE)
                else:
                    exp2 = ExpresionRelacional(Variable, ele, OPERACION_RELACIONAL.IGUALQUE)
                    explogica = ExpresionLogica(exp1, exp2, OPERACION_LOGICA.OR)
                    exp1 = explogica

            contador+=1

        return exp1



#--------------------------------   TRADUCCION CASE BUSCADO
    def t_TraduccionCaseBuscado(self,Objeto:CaseBuscado, Ambito):
        #Objetos globales para la traduccion
        global t_global
        cadena = "#--------- CASE BUSCADO --------------- \n"
# -------#viene CElse(CodigoEpsilon) =>
        #Obtenemos el else si este existe
        #Objetemos el else
        vari1:CElse = Objeto.caseelse
#-------#viene Lista_When =>Lista => CBWhen(expresion->una sola, sentencias->CodigoCuerpoEpsilon)
        cadena += self.RecorrerListaWhensCB(Objeto.listawhen,Ambito,vari1)

        return cadena

    #Recorremos la lista de whens CB
    def RecorrerListaWhensCB(self, lista, Ambito, Else):
        cadena = ""
        contador = len(lista)
        ifaux = None
        while contador > 0:
            element = lista[contador - 1]
            ele: CBWhen = element
            print(ele)
            if contador == len(lista):
                elseaux = None
                if Else is not None:
                    elseaux = Else.sentencias
                ifaux = If_inst(ele.expresion, element.sentencias, elseaux)
            else:
                ifaux = If_inst(ele.expresion, element.sentencias, [ifaux])
            contador = contador - 1
        if ifaux is not None:
            cadena += self.t_If(ifaux)
        return cadena



    def t_CrearIndice(self, objeto):
        global t_global
        cadena = ""
        crearindice: CrearIndice = objeto
        # Generando Sentencia SQL

        sentencia = "CREATE "

        if crearindice.unique:
            sentencia += "UNIQUE "

        sentencia += "INDEX " + str(crearindice.id_indice)

        sentencia += " ON " + str(crearindice.id_tabla) + " ("

        for c in crearindice.columnas:
            col: ColumnaIndice = c
            sentencia += str(col.id_columna)
            if col.orden is not None:
                sentencia += " " + str(col.orden)
            if col.nulls is not None:
                sentencia += " " + str(col.nulls)
            sentencia += ", "

        sentencia = sentencia[0: len(sentencia) - 2 ]
        sentencia += ");"

        # Generando codigo de tres direcciones
        v = t_global.varTemporal()
        cadena += "\n\t"+str(v) + " = \"" + sentencia + "\"\n"
        cadena += "\theap.append(" + str(v) + ")\n"
        cadena += "\tF3D.ejecutarSQL()\n"

        return cadena


    def t_sentenciaSQL(self, sentencia: SQL):
        global t_global
        cadena = ""
        v = t_global.varTemporal()
        cadena += "\t"+str(v) + " = \"\"\"" + sentencia.CadenaSQL + "\"\"\"\n"
        cadena += "\theap.append(" + str(v) + ")\n"
        cadena += "\tF3D.ejecutarSQL()\n"

        return cadena

    def t_Insert(self, insert: Insert_Datos):
        global cadenaExpresion
        print(insert)
        cadena = ""
        cadaux = ""
        for valor in insert.valores:
            v, c = self.procesar_expresion(valor, None)
            cadenaExpresion = ""
            cadena += c + "\n"
            cadaux = "\theap.append(" + str(v) + ")" + "\n" + cadaux

        cadaux = cadaux + "\theap.append(" + str(len(insert.valores)) + ")" + "\n"
        cadaux = cadaux + "\theap.append('" + str(insert.id_table[0].val) + "')" + "\n"
        cadena += cadaux
        cadena += "\tF3D.insert()"

        return cadena


# --------------------------------  TRADUCCION CUERPO DE LA FUNCION
    # EXPRESIONES
    def procesar_expresion(self, expresiones, ts):
        global cadenaExpresion
        if isinstance(expresiones, ExpresionAritmetica):
            v,c = self.procesar_aritmetica(expresiones, ts)
            cadenaExpresion += c
            return v,cadenaExpresion
        elif isinstance(expresiones, ExpresionRelacional):
            v,c = self.procesar_relacional(expresiones, ts)
            cadenaExpresion += c
            return v, cadenaExpresion
        elif isinstance(expresiones, ExpresionLogica):
            v,c = self.procesar_logica(expresiones, ts)
            cadenaExpresion += c
            return v, cadenaExpresion
        elif isinstance(expresiones, UnitariaNegAritmetica):
            v, c = self.procesar_expresion(expresiones.exp, ts)
            cadenaExpresion += c
            if isinstance(v, int) or isinstance(v, float):
                v = v * -1
            else:
                if v.isnumeric() or v.isdecimal:
                    v = "- " + str(v)
                else:
                    cadenaExpresion += str(v) + " = " + str(v) + " * -1"

            return v, cadenaExpresion
        elif isinstance(expresiones, ExpresionValor):
            # c = str(expresiones.val)
            if isinstance(expresiones.val, int) or isinstance(expresiones.val, float):
                return expresiones.val, ""
            # if c.isdigit():
            #     return expresiones.val, ""
            else:
                q = "\""+str(expresiones.val)+"\""
                return q, ""
        elif isinstance(expresiones, Variable):
            return self.procesar_variable(expresiones, ts)
        elif isinstance(expresiones, UnitariaAritmetica):
            return procesar_unitaria_aritmetica(expresiones, ts)
        elif isinstance(expresiones, ExpresionFuncion):
            v, c =  self.procesar_funcion(expresiones, ts)
            cadenaExpresion += c
            return v, cadenaExpresion
        elif isinstance(expresiones, ExpresionTiempo):
            return '"' + expresiones.nombre + '"', ""
        elif isinstance(expresiones, ExpresionConstante):
            return procesar_constante(expresiones, ts)
        elif isinstance(expresiones, SelectExpresion):
            return self.procesar_select_expresion(expresiones, ts)
        elif isinstance(expresiones, SubSelect2):
            v, c = self.procesar_select2(expresiones, ts)
            cadenaExpresion += c
            return v, cadenaExpresion
        elif isinstance(expresiones, AccesoSubConsultas):
            return self.procesar_expresion(expresiones.Query, ts)
        elif isinstance(expresiones, EjecucionFuncion):
            v, c =  self.procesar_ejecucion_funcion(expresiones, ts)
            cadenaExpresion += c
            return v, cadenaExpresion
        elif isinstance(expresiones, Absoluto):
            try:
                return self.procesar_expresion(expresiones.variable, ts)
                # return abs(procesar_expresion(expresiones.variable,ts))
            except:
                print('Error no se puede aplicar abs() por el tipo de dato')
                # consola.insert('end','>>Error: No se puede aplicar abs() al tipo de dato\n>>')
                # newErr=ErrorRep('Semantico','No se puede aplicar abs() al tipo de dato ',indice)
                # LisErr.agregar(newErr)
                return None
        else:
            print(expresiones)
            print('Error:Expresion no reconocida')


    def procesar_aritmetica(self, expresion, ts):
        global listaOpt
        val, cad1 = self.procesar_expresion(expresion.exp1, ts)
        val2, cad2 = self.procesar_expresion(expresion.exp2, ts)

        sval1 = str(val2)
        sval2 = str(val)

        if expresion.operador == OPERACION_ARITMETICA.MAS:
            v = t_global.varTemporal()
            cadena ="\t" + v + " = "+str(val)+" + "+str(val2) + "\n"

            op = ""
            if sval1 == "0" or sval2 == "0":
                if v == sval1 or v == sval2:
                    op = "# Se elimina la instruccion." + "- Regla: 8"
                else:
                    if sval1 == "0":
                        op = v + "= "+sval2 + "- Regla: 12"
                    else:
                        op = v + "= " + sval1 + "- Regla: 12"
            o = Optimizacion(cadena, op)
            listaOpt.append(o)
            return v, cadena

        elif expresion.operador == OPERACION_ARITMETICA.MENOS:
            v = t_global.varTemporal()
            cadena ="\t" +  v + " = " + str(val) + " - " + str(val2) + "\n"

            op = ""
            if sval1 == "0" or sval2 == "0":
                if v == sval1 or v == sval2:
                    op = "# Se elimina la instruccion." + "- Regla: 9"
                else:
                    if sval1 == "0":
                        op = v + " = "+sval2 + "- Regla: 13"
                    else:
                        op = v + " = " + sval1 + "- Regla: 13"
            o = Optimizacion(cadena, op)
            listaOpt.append(o)
            return v, cadena


        elif expresion.operador == OPERACION_ARITMETICA.MULTI:
            v = t_global.varTemporal()
            cadena ="\t" +  v + " = " + str(val) + " * " + str(val2) + "\n"

            op = ""
            if sval1 == "1" or sval2 == "1":
                if v == sval1 or v == sval2:
                    op = "# Se elimina la instruccion." + "- Regla: 10"
                else:
                    if sval1 == "1":
                        op = v + " = "+sval2 + "- Regla: 14"
                    else:
                        op = v + " = " + sval1
            elif sval1 == "0" or sval2 == "0":
                op = v + "= 0" + "- Regla: 17"
            elif sval1 == "2" or sval2 == "2":
                if sval1 == "2":
                    op = v + " = " + sval2 + "+" + sval2 + "- Regla: 16"
                else:
                    op = v + " = " + sval1 + "+" + sval1 + "- Regla: 16"
            o = Optimizacion(cadena, op)
            listaOpt.append(o)
            return v, cadena


        elif expresion.operador == OPERACION_ARITMETICA.DIVIDIDO:
            v = t_global.varTemporal()
            cadena ="\t" +  v + " = " + str(val) + " / " + str(val2) + "\n"

            op = ""
            if sval1 == "1" or sval2 == "1":
                if v == sval1 or v == sval2:
                    op = "# Se elimina la instruccion." + "- Regla: 11"
                else:
                    if sval1 == "1":
                        op = v + " = "+sval2 + "- Regla: 15"
                    else:
                        op = v + " = " + sval2
            elif sval2 == "0":
                op = v + "= 0" + "- Regla: 18"
            o = Optimizacion(cadena, op)
            listaOpt.append(o)

            return v, cadena


        elif expresion.operador == OPERACION_ARITMETICA.RESIDUO:
            v = t_global.varTemporal()
            cadena ="\t" +  v + " = " + str(val) + " / " + str(val2) + "\n"
            return v, cadena

        elif expresion.operador == OPERACION_ARITMETICA.POTENCIA:
            v = t_global.varTemporal()
            cadena ="\t" +  v + "= " + str(val) + " ** " + str(val2) + "\n"
            return v, cadena


    def procesar_relacional(self, expresion, ts):
        # OPTIMIZACION - AHORRO DE 2 LINEAS........................................................
        val, cad1 = self.procesar_expresion(expresion.exp1, ts)
        val2, cad2 = self.procesar_expresion(expresion.exp2, ts)
        #print("valores"+str(val)+str(val2))
        if expresion.operador == OPERACION_RELACIONAL.IGUALQUE:
            v = t_global.varTemporal()
            cadena ="\t" +  v + " = " + str(val) + " == " + str(val2) + "\n"
            return v, cadena
        elif expresion.operador == OPERACION_RELACIONAL.DISTINTO:
            v = t_global.varTemporal()
            cadena ="\t" +  v + " = " + str(val) + " != " + str(val2) + "\n"
            return v, cadena
        elif expresion.operador == OPERACION_RELACIONAL.MAYORIGUAL:
            v = t_global.varTemporal()
            cadena ="\t" +  v + " = " + str(val) + " >= " + str(val2) + "\n"
            return v, cadena
        elif expresion.operador == OPERACION_RELACIONAL.MENORIGUAL:
            v = t_global.varTemporal()
            cadena ="\t" +  v + " = " + str(val) + " <= " + str(val2) + "\n"
            return v, cadena
        elif expresion.operador == OPERACION_RELACIONAL.MAYORQUE:
            v = t_global.varTemporal()
            cadena ="\t" +  v + " = " + str(val) + " > " + str(val2) + "\n"
            return v, cadena
        elif expresion.operador == OPERACION_RELACIONAL.MENORQUE:
            v = t_global.varTemporal()
            cadena ="\t" +  v + " = " + str(val) + " < " + str(val2) + "\n"
            return v, cadena
        else:
            return 1

    def procesar_logica(self, expresion, ts):
        val, cad1 = self.procesar_expresion(expresion.exp1, ts)
        val2, cad2 = self.procesar_expresion(expresion.exp2, ts)

        if expresion.operador == OPERACION_LOGICA.AND:
            v = t_global.varTemporal()
            cadena ="\t" + v + " = " + str(val) + " and " + str(val2) + "\n"
            return v, cadena
        elif expresion.operador == OPERACION_LOGICA.OR:
            v = t_global.varTemporal()
            cadena ="\t" + v + " = " + str(val) + " or " + str(val2) + "\n"
            return v, cadena

    def procesar_variable(self, tV, ts):
        global t_global, ambitoFuncion
        r = ""
        for item in t_global.tablaSimbolos:
            v: tipoSimbolo = t_global.obtenerSimbolo(item)
            #print(str(v.nombre)+"<>"+str(tV.id)+"-"+str(v.ambito)+"<>"+ambitoFuncion)
            if v.nombre == tV.id and v.ambito == ambitoFuncion:
                #print(str(v.temporal))
                r = str(v.temporal)
                return r,""
        return r,""

    def procesar_funcion(self, expresion:ExpresionFuncion, ts):
        aux = ""
        cadena = ""
        if expresion.exp1 is not None:
            v, cad = self.procesar_expresion(expresion.exp1, ts)
            cadena += cad + "\n"
            aux = "\theap.append(" + str(v) + ")" + "\n" + aux
        if expresion.exp2 is not None:
            v, cad = self.procesar_expresion(expresion.exp2, ts)
            cadena += cad + "\n"
            aux = "\theap.append(" + str(v) + ")" + "\n" + aux
        if expresion.exp3 is not None:
            v, cad = self.procesar_expresion(expresion.exp3, ts)
            cadena += cad + "\n"
            aux = "\theap.append(" + str(v) + ")" + "\n" + aux

        v = t_global.varTemporal()
        cadena += aux + "\n" + "\theap.append(" + str(expresion.id_funcion.value) + ")" + "\n\t" + str(v) + " = F3D.funcionNativa()" + "\n"

        return v, cadena

    def procesar_select_expresion(self, expresion: SelectExpresion, ts):
        print(expresion)
        exp = expresion.listaCampos[0].Columna
        return self.procesar_expresion(exp, ts)

    def procesar_select2(self, expresion: SubSelect2, ts):
        global ts_global, t_global, ambitoFuncion
        cadena = ""
        aux = SQL(expresion, ts_global, t_global, ambitoFuncion)
        aux.CadenaSQL = aux.GrafoSubSelect2(expresion.Lista_Campos, expresion.Nombres_Tablas, expresion.Cuerpo)
        if aux.CadenaSQL is not None:
            print("PRODUCE SENTENCIA SQL-----------------------------------===")
            # print(str(aux.CadenaSQL))
            cadena += "\n" + self.t_sentenciaSQL(aux)
            return "heap[-1]", cadena
        else:
            print("NO TRADUCE....")
        return "", ""

    def procesar_ejecucion_funcion(self, expresion: EjecucionFuncion, ts):
        global t_global, cadena, cadenaFuncion, ambitoFuncion, cadenaExpresion, listaAsignaciones, listaOpt
        cadenaAsi = ""

        local = ambitoFuncion
        ambitoFuncion = expresion.Id

        etiR = "-"
        for fun in t_global.tablaSimbolos:
            f: tipoSimbolo = t_global.obtenerSimbolo(fun)
            if f.ambito == expresion.Id and f.rol == "local" and f.nombre == "return":
                etiR = f.temporal

        ambitoFuncion = local

        v = t_global.varTemporal()
        temp = v
        cadenaAsi += self.t_llamadaFuncion(expresion)

        cadenaAsi += "\n\t" + str(temp) + " = " + str(etiR) + "\n"
        return temp, cadenaAsi

    def generar(self):
        global cadena
        f = open('./intermedio.py', 'w')
        f.write(cadena)
        f.close()


# ========== REPORTE OPTIMIZACION =================== #
def reporte_optimizacion():
    global listaOpt, listaAsignaciones
    cadena = ""
    print("------------REPORTE OPTIMIZACION---------------")
    SymbolT2 = Graph('g', filename='reporteOptimizacion.gv', format='png',
                     node_attr={'shape': 'plaintext', 'height': '.1'})

    print("ASIGNACIONES -- ")
    for i in listaAsignaciones:
        print(str(i.izq)+" = "+str(i.der))


    for item in listaAsignaciones:
        for asi in listaAsignaciones:
            if str(item.der) == str(asi.izq) and str(item.izq) == str(asi.der):
                print("optimiza 1")
                op = str(item.der) + "=" + str(asi.der) + "-"
                op += str(item.izq) + "=" + str(asi.izq)
                opt = str(item.der) + "=" + str(asi.der) + "- Regla: 1"
                o = Optimizacion(op, opt)
                listaOpt.append(o)
                break;


    ope  = "goto .R" + "-"+ "Label .R"
    opet = "Label .R" + "- Regla: 2"
    regla2 = Optimizacion(ope, opet)

    listaOpt.append(regla2)

    for o in listaOpt:
        cadena += '\n <TR><TD>'+o.original+'</TD><TD>'+o.optimizado+'</TD></TR>'

    SymbolT2.node('table', '<<TABLE><TR><TD>CODIGO</TD><TD>OPTIMIZACION</TD></TR>' + cadena + '</TABLE>>')
    SymbolT2.render('g', format='png', view=True)
