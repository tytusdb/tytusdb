from analizadorFase2.Instrucciones.EliminarFuncion import EliminarFuncion
from analizadorFase2.Instrucciones.Llamada import Llamada
from analizadorFase2.Instrucciones.Else import Else_inst
from analizadorFase2.Instrucciones.If import If_inst
from analizadorFase2.Operaciones.TiposOperacionesLR import TiposOperacionesLR
from analizadorFase2.Operaciones.Operaciones_LogicasRelacionales import OperacionesLogicasRelacionales
from analizadorFase2.Abstractas.RetornoOp import RetornoOp
from analizadorFase2.Abstractas.Expresion import Tipos
from analizadorFase2.Abstractas.Primitivo import Primitivo
from analizadorFase2.Instrucciones.Funcion import Funcion
from analizadorFase2.Function.FuncionNativa import FuncionNativa
from analizadorFase2.Function.TipoFunNativa import TipoFunNativa
from analizadorFase2.Instrucciones.Asignacion import Asignacion
from analizadorFase2.Operaciones.Operaciones_Aritmeticcas import Operaciones_Aritmeticas
from analizadorFase2.Operaciones.TiposOperacionesA import TiposOperaciones
from analizadorFase2.Operaciones.OperacionesUnarias import OperacionesUnarias
from analizadorFase2.Instrucciones.Return import Return_inst


class Generador:
    def __init__(self, numero_temp, numero_labl, inst):
        self.temp = numero_temp
        self.label = numero_labl
        self.inst = inst
        self.codigo3d = []
        self.numerotab = 0
        self.dentroetiqueta = False

    def generarTemporal(self):
        temp = "t" + str(self.temp)
        self.temp += 1
        return temp

    def generarTab(self):
        return "\t"

    def generarEtiqueta(self):
        label = ".L" + str(self.label)
        self.label += 1
        return label

    def generarNativaDelete(self):
        temp = self.generarTemporal()
        inst = "def nativa_borrarfuncion():\n\tglobal lista\n\t" + temp + "=lista.pop()\n\tglobals()[" + temp + "] = 0"
        self.codigo3d.append(inst)

    def agregarvariableglobal(self, id):
        inst = self.generarTab() + "global " + id
        self.codigo3d.append(inst)

    def generarGoto(self, etiqueta):
        inst = self.generarTab() + "goto " + etiqueta 
        self.codigo3d.append(inst)

    def generarLlamada(self, id):
        inst = self.generarTab() + id + "()"
        self.codigo3d.append(inst)

    def agregarEtiqueta(self, etiqueta):
        self.dentroetiqueta = False
        inst = self.generarTab() + "label " + etiqueta
        self.dentroetiqueta = True
        self.codigo3d.append(inst)

    def generarAsignacion(self, id, valor):
        if isinstance(valor, str):
            inst = self.generarTab() + id + " = " + valor
        else:
            inst = self.generarTab() + id + " = " + str(valor)
        self.codigo3d.append(inst)

    def agregarIf(self, condicion, etiqueta):
        inst = self.generarTab() + "if " + condicion + ": goto " + etiqueta
        self.codigo3d.append(inst)

    def agregarFuncion(self, id):
        inst = "def " + id + "():"
        self.codigo3d.append(inst)
        self.numerotab += 1

    def ejecutar(self):
        for instruccion in self.inst:
            if isinstance(instruccion, Funcion):
                self.compilarFuncion(instruccion)
            elif isinstance(instruccion, FuncionNativa): 
                self.compilarFuncionesNativas(instruccion)

        self.generarNativaDelete()
        for linea in self.codigo3d:
            print(linea)

    def compilarFuncion(self, instruccion):
        self.codigo3d.append("@with_goto")
        self.agregarFuncion("C3D_" + instruccion.id)
        self.agregarvariableglobal("lista")
        if instruccion.numparametros != 0:
            temporal = self.generarTemporal()
            self.generarAsignacion(temporal, "0")
            for param in instruccion.parametros :
                self.generarAsignacion(param.id, "simulador_pila[" + temporal + "]")
                self.generarAsignacion(temporal, temporal + " + 1")
        for instruccion1 in instruccion.cuerpo:
            if isinstance(instruccion1, Asignacion):
                self.compilarAsignacion(instruccion1)
            elif isinstance(instruccion1, If_inst):
                self.compilarIf(instruccion1)
            elif isinstance(instruccion1, Return_inst):
                self.compilarReturn(instruccion1)
            elif isinstance(instruccion1, Llamada):
                self.compilarLlamada(instruccion1)
            elif isinstance(instruccion1, Primitivo):
                self.compilarPrimitivo(instruccion1)
            elif isinstance(instruccion1, EliminarFuncion):
                self.compilarDropFunction(instruccion1)
        self.numerotab -= 1
    
    def compilarLlamada(self, instruccion):
        if instruccion.numparametros != 0:
            temporal = self.generarTemporal()
            self.generarAsignacion(temporal, "0")
            for param in instruccion.parametros:
                valor_param = self.compilarOperacionLogicaRelacional(param.valor)
                self.generarAsignacion("simulador_pila[" + temporal + "]", valor_param.valor)
                self.generarAsignacion(temporal, temporal + " + 1")
        self.generarLlamada("C3D_" + instruccion.id)
        temp = self.generarTemporal()
        self.generarAsignacion(temp, "0")
        temp1 = self.generarTemporal()
        self.generarAsignacion(temp1, "simulador_pila[" + temp + "]")
        return RetornoOp(temp1, None)

    def compilarLlamada1(self, instruccion):
        if instruccion.numparametros != 0:
            temporal = self.generarTemporal()
            self.generarAsignacion(temporal, "0")
            for param in instruccion.parametros:
                valor_param = self.compilarOperacionLogicaRelacional(param.valor)
                self.generarAsignacion("simulador_pila[" + temporal + "]", valor_param.valor)
                self.generarAsignacion(temporal, temporal + " + 1")
        self.generarLlamada("C3D_" + instruccion.id)
        temp = self.generarTemporal()
        self.generarAsignacion(temp, "0")
        temp1 = self.generarTemporal()
        self.generarAsignacion(temp1, "simulador_pila[" + temp + "]")
        return RetornoOp(temp1, None)

    def compilarReturn(self, instruccion):
        if not instruccion.valor is None:
            val = self.compilarOperacionLogicaRelacional(instruccion.valor)
            temporal = self.generarTemporal()
            self.generarAsignacion(temporal, "0")
            self.generarAsignacion("simulador_pila[" + temporal + "]", str(val.valor))

    def compilarcuerpoif(self, instruccion):
        for instruccion1 in instruccion:
            if isinstance(instruccion1, Asignacion):
                self.compilarAsignacion(instruccion1)
            elif isinstance(instruccion1, If_inst):
                self.compilarIf(instruccion1)
            elif isinstance(instruccion1, Return_inst):
                self.compilarReturn(instruccion1)
            elif isinstance(instruccion1, Llamada):
                self.compilarLlamada(instruccion1)
            elif isinstance(instruccion1, Primitivo):
                self.compilarPrimitivo(instruccion1)
            elif isinstance(instruccion1, EliminarFuncion):
                self.compilarDropFunction(instruccion1)

    def compilarIf(self, instruccion):
        if isinstance(instruccion, If_inst):
            condicion = self.compilarOperacionLogicaRelacional(instruccion.condicion)
            if instruccion.elsest is None:
                etiquetaverdadero = self.generarEtiqueta()
                etiquetafalso = self.generarEtiqueta()
                self.agregarIf(condicion.valor + " == " + str(True), etiquetaverdadero)
                self.generarGoto(etiquetafalso)
                self.agregarEtiqueta(etiquetaverdadero)
                self.compilarcuerpoif(instruccion.cuerpo)
                self.agregarEtiqueta(etiquetafalso)
            else:
                etiquetaverdadero = self.generarEtiqueta()
                etiquetafalso = self.generarEtiqueta()
                etiquetasalida = self.generarEtiqueta()
                self.agregarIf(condicion.valor + " == " + str(True), etiquetaverdadero)
                self.generarGoto(etiquetafalso)
                self.agregarEtiqueta(etiquetaverdadero)
                self.compilarcuerpoif(instruccion.cuerpo)
                self.generarGoto(etiquetasalida)
                self.agregarEtiqueta(etiquetafalso)
                self.compilarIf(instruccion.elsest)
                self.agregarEtiqueta(etiquetasalida)
        elif isinstance(instruccion, Else_inst):
            self.compilarcuerpoif(instruccion.cuerpoelse)

    def compilarAsignacion(self, instruccion):
        if isinstance(instruccion.valor, Primitivo):
            valp = self.compilarPrimitivo(instruccion.valor)
            if not valp is None:
                self.generarAsignacion(instruccion.id, valp.valor)
        elif isinstance(instruccion.valor, OperacionesLogicasRelacionales):
            ret = self.compilarOperacionLogicaRelacional(instruccion.valor)
            self.generarAsignacion(instruccion.id, ret.valor)
        elif isinstance(instruccion.valor, Operaciones_Aritmeticas):
            ret = self.compilarOperacionAritmetica(instruccion.valor)
            self.generarAsignacion(instruccion.id, ret.valor)
        elif isinstance(instruccion.valor, Llamada):
            ret = self.compilarLlamada(instruccion.valor)
            self.generarAsignacion(instruccion.id, ret.valor)
        elif isinstance(instruccion.valor, FuncionNativa):
            ret = self.compilarFuncionesNativas(instruccion.valor)
            self.generarAsignacion(instruccion.id, ret.valor)


    def compilarDropFunction(self, instruccion):
        if isinstance(instruccion, EliminarFuncion):
            self.codigo3d.append(instruccion.instruccion)

    def compilarOperacionLogicaRelacional(self, instruccion):
        if isinstance(instruccion, OperacionesLogicasRelacionales):
            if instruccion.tipo == TiposOperacionesLR.IGUAL:
                izquierdo = self.compilarOperacionLogicaRelacional(instruccion.izquierdo)
                derecho = self.compilarOperacionLogicaRelacional(instruccion.derecho)   
                temporal = self.generarTemporal()
                etiquetatrue = self.generarEtiqueta()
                etiquetafalse = self.generarEtiqueta()
                etiquetasalida = self.generarEtiqueta()
                self.agregarIf(str(izquierdo.valor) + "==" + str(derecho.valor), etiquetatrue)
                self.generarGoto(etiquetafalse)
                self.agregarEtiqueta(etiquetatrue)
                
                self.generarAsignacion(temporal, True)
                self.generarGoto(etiquetasalida)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetafalse)
                
                self.generarAsignacion(temporal, False)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetasalida)
                
                ret = RetornoOp(temporal, None)
                return ret
            elif instruccion.tipo == TiposOperacionesLR.DIFERENTE:
                izquierdo = self.compilarOperacionLogicaRelacional(instruccion.izquierdo)
                derecho = self.compilarOperacionLogicaRelacional(instruccion.derecho)
                temporal = self.generarTemporal()
                etiquetatrue = self.generarEtiqueta()
                etiquetafalse = self.generarEtiqueta()
                etiquetasalida = self.generarEtiqueta()
                self.agregarIf(str(izquierdo.valor) + "!=" + str(derecho.valor), etiquetatrue)
                self.generarGoto(etiquetafalse)
                self.agregarEtiqueta(etiquetatrue)
                
                self.generarAsignacion(temporal, True)
                self.generarGoto(etiquetasalida)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetafalse)
                
                self.generarAsignacion(temporal, False)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetasalida)
                
                ret = RetornoOp(temporal, None)
                return ret
            elif instruccion.tipo == TiposOperacionesLR.MENOR:
                izquierdo = self.compilarOperacionLogicaRelacional(instruccion.izquierdo)
                derecho = self.compilarOperacionLogicaRelacional(instruccion.derecho)
                temporal = self.generarTemporal()
                etiquetatrue = self.generarEtiqueta()
                etiquetafalse = self.generarEtiqueta()
                etiquetasalida = self.generarEtiqueta()
                self.agregarIf(str(izquierdo.valor) + "<" + str(derecho.valor), etiquetatrue)
                self.generarGoto(etiquetafalse)
                self.agregarEtiqueta(etiquetatrue)
                
                self.generarAsignacion(temporal, True)
                self.generarGoto(etiquetasalida)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetafalse)
                
                self.generarAsignacion(temporal, False)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetasalida)
                
                ret = RetornoOp(temporal, None)
                return ret
            elif instruccion.tipo == TiposOperacionesLR.MENORIGUAL:
                izquierdo = self.compilarOperacionLogicaRelacional(instruccion.izquierdo)
                derecho = self.compilarOperacionLogicaRelacional(instruccion.derecho)
                temporal = self.generarTemporal()
                etiquetatrue = self.generarEtiqueta()
                etiquetafalse = self.generarEtiqueta()
                etiquetasalida = self.generarEtiqueta()
                self.agregarIf(str(izquierdo.valor) + "<=" + str(derecho.valor), etiquetatrue)
                self.generarGoto(etiquetafalse)
                self.agregarEtiqueta(etiquetatrue)
                
                self.generarAsignacion(temporal, True)
                self.generarGoto(etiquetasalida)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetafalse)
                
                self.generarAsignacion(temporal, False)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetasalida)
                
                ret = RetornoOp(temporal, None)
                return ret
            elif instruccion.tipo == TiposOperacionesLR.MAYORIGUAL:
                izquierdo = self.compilarOperacionLogicaRelacional(instruccion.izquierdo)
                derecho = self.compilarOperacionLogicaRelacional(instruccion.derecho)
                temporal = self.generarTemporal()
                etiquetatrue = self.generarEtiqueta()
                etiquetafalse = self.generarEtiqueta()
                etiquetasalida = self.generarEtiqueta()
                self.agregarIf(str(izquierdo.valor) + ">=" + str(derecho.valor), etiquetatrue)
                self.generarGoto(etiquetafalse)
                self.agregarEtiqueta(etiquetatrue)
                
                self.generarAsignacion(temporal, True)
                self.generarGoto(etiquetasalida)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetafalse)
                
                self.generarAsignacion(temporal, False)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetasalida)
                
                ret = RetornoOp(temporal, None)
                return ret
            elif instruccion.tipo == TiposOperacionesLR.MAYOR:
                izquierdo = self.compilarOperacionLogicaRelacional(instruccion.izquierdo)
                derecho = self.compilarOperacionLogicaRelacional(instruccion.derecho)
                temporal = self.generarTemporal()
                etiquetatrue = self.generarEtiqueta()
                etiquetafalse = self.generarEtiqueta()
                etiquetasalida = self.generarEtiqueta()
                self.agregarIf(str(izquierdo.valor) + ">" + str(derecho.valor), etiquetatrue)
                self.generarGoto(etiquetafalse)
                self.agregarEtiqueta(etiquetatrue)
                
                self.generarAsignacion(temporal, True)
                self.generarGoto(etiquetasalida)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetafalse)
                
                self.generarAsignacion(temporal, False)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetasalida)
                
                ret = RetornoOp(temporal, None)
                return ret

            elif instruccion.tipo == TiposOperacionesLR.OR:
                izquierdo = self.compilarOperacionLogicaRelacional(instruccion.izquierdo)
                derecho = self.compilarOperacionLogicaRelacional(instruccion.derecho)
                temporal = self.generarTemporal()
                etiquetatrue = self.generarEtiqueta()
                etiquetafalse = self.generarEtiqueta()
                etiquetafalse1 = self.generarEtiqueta()
                etiquetasalida = self.generarEtiqueta()
                self.agregarIf(izquierdo.valor + " == " + str(True), etiquetatrue)
                self.generarGoto(etiquetafalse)
                self.agregarEtiqueta(etiquetafalse)
                
                self.agregarIf(derecho.valor + " == " + str(True), etiquetatrue)
                self.generarGoto(etiquetafalse1)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetatrue)
                
                self.generarAsignacion(temporal, True)
                self.generarGoto(etiquetasalida)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetafalse1)
                
                self.generarAsignacion(temporal, False)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetasalida)
                
                ret = RetornoOp(temporal, None)
                return ret
            elif instruccion.tipo == TiposOperacionesLR.AND:
                izquierdo = self.compilarOperacionLogicaRelacional(instruccion.izquierdo)
                derecho = self.compilarOperacionLogicaRelacional(instruccion.derecho)
                temporal = self.generarTemporal()
                etiquetatrue = self.generarEtiqueta()
                etiquetafalse = self.generarEtiqueta()
                etiquetatrue1 = self.generarEtiqueta()
                etiquetasalida = self.generarEtiqueta()
                self.agregarIf(izquierdo.valor + ' == ' + str(True), etiquetatrue)
                self.generarGoto(etiquetafalse)
                self.agregarEtiqueta(etiquetatrue)
                
                self.agregarIf(derecho.valor + ' == ' + str(True), etiquetatrue1)
                self.generarGoto(etiquetafalse)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetatrue1)
                
                self.generarAsignacion(temporal, True)
                self.generarGoto(etiquetasalida)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetafalse)
                
                self.generarAsignacion(temporal, False)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetasalida)
                
                ret = RetornoOp(temporal)
                return ret
            elif instruccion.tipo == TiposOperacionesLR.NOT:
                izquierdo = self.compilarOperacionLogicaRelacional(instruccion.izquierdo)
                temporal = self.generarTemporal()
                etiquetatrue = self.generarEtiqueta()
                etiquetafalse = self.generarEtiqueta()
                etiquetasalida = self.generarEtiqueta()
                self.agregarIf(izquierdo.valor + ' == ' + str(True), etiquetatrue)
                self.generarGoto(etiquetafalse)
                self.agregarEtiqueta(etiquetatrue)
                
                self.generarAsignacion(temporal, False)
                self.generarGoto(etiquetasalida)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetafalse)
                
                self.generarAsignacion(temporal, True)
                self.numerotab -= 1
                self.agregarEtiqueta(etiquetasalida)
                
                ret = RetornoOp(temporal, None)
                return ret                 
                
        elif isinstance(instruccion, Operaciones_Aritmeticas):
            return self.compilarOperacionAritmetica(instruccion)
        elif isinstance(instruccion, Primitivo) or isinstance(instruccion, Llamada):
            return self.compilarPrimitivo(instruccion)

    def compilarOperacionAritmetica(self, instruccion):
        if isinstance(instruccion, Operaciones_Aritmeticas):
            izquierdo = self.compilarOperacionAritmetica(instruccion.izquierdo)
            derecho = self.compilarOperacionAritmetica(instruccion.derecho)
            temporal = self.generarTemporal()
            if instruccion.tipo == TiposOperaciones.Suma:
                self.generarAsignacion(temporal, str(izquierdo.valor) + "+" + str(derecho.valor))
                ret = RetornoOp(temporal, None)
                return ret
            elif instruccion.tipo == TiposOperaciones.Resta:
                self.generarAsignacion(temporal, str(izquierdo.valor) + "-" + str(derecho.valor))
                ret = RetornoOp(temporal, None)
                return ret
            elif instruccion.tipo == TiposOperaciones.Mult:
                self.generarAsignacion(temporal, str(izquierdo.valor) + "*" + str(derecho.valor))
                ret = RetornoOp(temporal, None)
                return ret
            elif instruccion.tipo == TiposOperaciones.Div:
                self.generarAsignacion(temporal, str(izquierdo.valor) + "/" + str(derecho.valor))
                ret = RetornoOp(temporal, None)
                return ret
            elif instruccion.tipo == TiposOperaciones.Modulo:
                self.generarAsignacion(temporal, str(izquierdo.valor) + "%" + str(derecho.valor))
                ret = RetornoOp(temporal, None)
                return ret 
            elif instruccion.tipo == TiposOperaciones.Exp:
                self.generarAsignacion(temporal, str(izquierdo.valor) + "**" + str(derecho.valor))
                ret = RetornoOp(temporal, None)
                return ret
        elif isinstance(instruccion, OperacionesUnarias):
            izquierdo = self.compilarOperacionAritmetica(instruccion.valor)
            temporal = self.generarTemporal()
            if instruccion.tipoop == TiposOperaciones.RestaUnaria:
                self.generarAsignacion(temporal, "-" + str(izquierdo.valor))
                ret = RetornoOp(temporal,None)
                return ret
            else:
                self.generarAsignacion(temporal, str(izquierdo.valor)) 
                ret = RetornoOp(temporal, str(izquierdo.valo))
                return ret
        elif isinstance(instruccion, Primitivo):
            return self.compilarPrimitivo(instruccion)
        elif isinstance(instruccion, FuncionNativa):
            return  self.compilarFuncionesNativas(instruccion)

    def compilarPrimitivo(self, instruccion):
        if isinstance(instruccion, Primitivo):
            if instruccion.tipo == Tipos.Booleano:
                if instruccion.trueLabel == '':
                    instruccion.trueLabel = self.generarEtiqueta()
                
                if instruccion.falseLabel == '':
                    instruccion.falseLabel = self.generarEtiqueta()
                temporal = self.generarTemporal()
                if instruccion.valor is True:
                    self.generarGoto(instruccion.trueLabel)
                    self.agregarEtiqueta(instruccion.trueLabel)
                    self.generarAsignacion(temporal, True)
                else:
                    self.generarGoto(instruccion.falseLabel)
                    self.agregarEtiqueta(instruccion.falseLabel)
                    self.generarAsignacion(temporal, False)
                ret = RetornoOp(temporal, Tipos.Id)
                ret.trueLabel = instruccion.trueLabel
                ret.falseLabel = instruccion.falseLabel
                return ret
            elif instruccion.tipo == Tipos.Id:
                temporal = self.generarTemporal()
                self.generarAsignacion(temporal, instruccion.valor)
                return RetornoOp(temporal, instruccion.tipo)
            elif instruccion.tipo == Tipos.ISQL:
                valor = instruccion.valor
                if valor.find("C3D_") == -1:
                    auxvalor = valor.split("=", 1)
                    temporal = auxvalor[0].replace("\t", "")
                    inst = auxvalor[1]
                    self.generarAsignacion(temporal, inst)
                    self.generarAsignacion("lista", "[" + temporal + "]")
                    temp = self.generarTemporal()
                    self.generarAsignacion(temp, "funcionIntermedia()")
                    ret = RetornoOp(temp, None)
                    return ret
                else:
                    auxvalor = valor
                    auxvalor1 = auxvalor.split("\n")
                    temp = ""
                    for inst in auxvalor1:
                        if inst.find("funcionIntermedia()") == -1:
                            self.codigo3d.append(inst)
                        else:
                            temp = self.generarTemporal()
                            self.generarAsignacion(temp, "funcionIntermedia()")
                    ret = RetornoOp(temp, None)
                    return ret
            else:
                ret = RetornoOp(instruccion.valor, instruccion.tipo)
                return ret
        elif isinstance(instruccion, Llamada):
            return self.compilarLlamada(instruccion)

    def compilarFuncionesNativas(self, instruccion):
        '''Aqui se genera el C3D de las funciones nativas '''
        #PRIMERO DETECTAR QUE TIPO DE FUNCION ES 
        if instruccion.tipo == TipoFunNativa.avg: 
            #Verificar que trae como parametro (valor, variable, expresion)
            arregloDeValores =[]
            for param in instruccion.parametros :
                retorno = self.compilarOperacionAritmetica(instruccion.parametros)
                #agregamos el valor del retorno al arreglo de valores 
                arregloDeValores.append(retorno)
            indice = 0;
            for indice in len(arregloDeValores): 
                temporal=self.generarTemporal()
                if indice+1 < len(arregloDeValores):
                    lineaSuma=self.generarTab() + temporal + '=' + arregloDeValores[indice] + '+' + arregloDeValores[indice+1]
                    self.codigo3d.append(lineaSuma)
                    arregloDeValores[indice+1]=temporal
                else: 
                    lineaFinal=self.generarTab() + temporal + '=' + arregloDeValores[indice] + '/' + len(arregloDeValores)
                    self.codigo3d.append(lineaFinal)
                    ret = RetornoOp(temporal, None)
                    return ret
        elif instruccion.tipo == TipoFunNativa.sum:
            arregloDeValores =[]
            for param in instruccion.parametros :
                retorno = self.compilarOperacionAritmetica(instruccion.parametros)
                #agregamos el valor del retorno al arreglo de valores 
                arregloDeValores.append(retorno)
            indice = 0;
            for indice in len(arregloDeValores): 
                temporal=self.generarTemporal()
                if indice+1 < len(arregloDeValores):
                    lineaSuma=self.generarTab() + temporal + '=' + arregloDeValores[indice] + '+' + arregloDeValores[indice+1]
                    self.codigo3d.append(lineaSuma)
                    arregloDeValores[indice+1]=temporal
                else: 
                    #lineaFinal=self.generarTab() + temporal + '=' + arregloDeValores[indice] + '/' + len(arregloDeValores)
                    #self.codigo3d.append(lineaFinal)
                    ret = RetornoOp(arregloDeValores[indice], None)
                    return ret
        elif instruccion.tipo == TipoFunNativa.min: 
            arregloDeValores =[]
            for param in instruccion.parametros :
                retorno = self.compilarOperacionAritmetica(instruccion.parametros)
                #agregamos el valor del retorno al arreglo de valores 
                arregloDeValores.append(retorno)
            indice = 0;
            for indice in len(arregloDeValores): 
                #ciclo de comparaciones 
                #temporal=self.generarTemporal()
                #def agregarIf(self, condicion, etiqueta):
                etiquetaverdadero=self.generarEtiqueta()
                if indice+1 < len(arregloDeValores):
                    self.agregarIf(arregloDeValores[indice] + '<' + arregloDeValores[indice+1], etiquetaverdadero)
                    etiquetafalso=self.generarEtiqueta()
                    #acciones de falso
                    #self.generarGoto(etiquetafalso)
                    self.agregarEtiqueta(etiquetaverdadero)
                    #acciones de verdadero
                    arregloDeValores[indice+1]=arregloDeValores[indice]
                else: 
                    #lineaFinal=self.generarTab() + temporal + '=' + arregloDeValores[indice] + '/' + len(arregloDeValores)
                    #self.codigo3d.append(lineaFinal)
                    ret = RetornoOp(arregloDeValores[indice], None)
                    return ret
        elif instruccion.tipo == TipoFunNativa.max: 
            arregloDeValores =[]
            for param in instruccion.parametros :
                retorno = self.compilarOperacionAritmetica(instruccion.parametros)
                #agregamos el valor del retorno al arreglo de valores 
                arregloDeValores.append(retorno)
            indice = 0;
            for indice in len(arregloDeValores): 
                #ciclo de comparaciones 
                #temporal=self.generarTemporal()
                #def agregarIf(self, condicion, etiqueta):
                etiquetaverdadero=self.generarEtiqueta()
                if indice+1 < len(arregloDeValores):
                    self.agregarIf(arregloDeValores[indice] + '>' + arregloDeValores[indice+1], etiquetaverdadero)
                    etiquetafalso=self.generarEtiqueta()
                    #acciones de falso
                    #self.generarGoto(etiquetafalso)
                    self.agregarEtiqueta(etiquetaverdadero)
                    #acciones de verdadero
                    arregloDeValores[indice+1]=arregloDeValores[indice]
                else: 
                    #lineaFinal=self.generarTab() + temporal + '=' + arregloDeValores[indice] + '/' + len(arregloDeValores)
                    #self.codigo3d.append(lineaFinal)
                    ret = RetornoOp(arregloDeValores[indice], None)
                    return ret
        elif instruccion.tipo == TipoFunNativa.abs: 
            #FUNCION TIPO ABS 
            #Verificar que trae como parametro (valor, variable, expresion)
            #if isinstance(instruccion.parametros, Operaciones_Aritmeticas):
            retorno = self.compilarOperacionAritmetica(instruccion.parametros)
            #Linea del if 
            etiquetaverdadero=self.generarEtiqueta()
            self.agregarIf(retorno.valor + '>' + str(0), etiquetaverdadero)
            #self.codigo3d.append(inst)
            lineaAbs=self.generarTab() + retorno.valor + '=' + retorno.valor + '*-1'
            self.codigo3d.append(lineaAbs)
            self.agregarEtiqueta(etiquetaverdadero)
            ret = RetornoOp(retorno.valor, None)
            return ret
                #mandar a imprimir un if para validar si el valor del temporal que sale de operacion aritmetica es menor a 0
                #si entra al if hacer la conversion, sino entra seguir con l
            #elif isinstance(instruccion.parametros, Primitivo):
            #    retorno = self.compilarPrimitivo(instruccion.parametros)
            #    etiquetaverdadero=self.generarEtiqueta()
            #    self.agregarIf(retorno.valor + '>' + str(0), etiquetaverdadero)
            #    #AGREGAR UNA EXCEPCION PARA UN NUMERO NEGATIVO 
            #    lineaAbs=retorno.valor + '=' + retorno.valor + '*-1'
            #    self.codigo3d.append(lineaAbs)
            #    self.agregarEtiqueta(etiquetaverdadero)
            #    ret = RetornoOp(retorno.valor, None)
            #    return ret
            #elif isinstance(instruccion.parametros, FuncionNativa):
            #    retorno = self.compilarFuncionesNativas(instruccion.parametros)
            #    etiquetaverdadero = self.generarEtiqueta()
            #    self.agregarIf(retorno.valor + '>' + str(0), etiquetaverdadero)
            #    # AGREGAR UNA EXCEPCION PARA UN NUMERO NEGATIVO
            #    lineaAbs = self.generarTab() + retorno.valor + '=' + retorno.valor + '*-1'
            #    self.codigo3d.append(lineaAbs)
            #    self.agregarEtiqueta(etiquetaverdadero)
            #    ret = RetornoOp(retorno.valor, None)
            #    return ret
        elif instruccion.tipo == TipoFunNativa.cbrt:
            # Corresponde a función de CBRT
            #if isinstance(instruccion.parametros, Operaciones_Aritmeticas):
            retorno = self.compilarOperacionAritmetica(instruccion.parametros)
            tag = self.generarTemporal()
            lineaCubic = self.generarTab() + str(tag) + ' = ' + str(retorno.valor) + '** 1/3'
            self.codigo3d.append(lineaCubic)
            ret = RetornoOp(tag, None)
            return ret
            #elif isinstance(instruccion.parametros, Primitivo):
            #    retorno = self.compilarPrimitivo(instruccion.parametros)
            #    tag = self.generarTemporal()
            #    lineaCubic = self.generarTab() + str(tag) + ' = ' + str(retorno.valor) + '** 1/3'
            #    self.codigo3d.append(lineaCubic)
            #    ret = RetornoOp(tag, None)
            #    return ret
        elif instruccion.tipo == TipoFunNativa.ceil:
            # Corresponde a función de CEIL
            #if isinstance(instruccion.parametros, Operaciones_Aritmeticas):
            retorno = self.compilarOperacionAritmetica(instruccion.parametros)
            tag = self.generarTemporal()
            lineaCeil = self.generarTab() + str(tag) + ' = round(' + str(retorno.valor) + ')'
            self.codigo3d.append(lineaCeil)
            ret = RetornoOp(tag, None)
            return ret
            #elif isinstance(instruccion.parametros, Primitivo):
            #    retorno = self.compilarPrimitivo(instruccion.parametros)
            #    tag = self.generarTemporal()
            #    lineaCeil = self.generarTab() + str(tag) + ' = round(' + str(retorno.valor) + ')'
            #    self.codigo3d.append(lineaCeil)
            #    ret = RetornoOp(tag, None)
            #    return ret
        elif instruccion.tipo == TipoFunNativa.ceiling:
            # Corresponde a función de CEILING
            #if isinstance(instruccion.parametros, Operaciones_Aritmeticas):
            retorno = self.compilarOperacionAritmetica(instruccion.parametros)
            tag = self.generarTemporal()
            lineaCeil = self.generarTab() + str(tag) + ' = round(' + str(retorno.valor) + ')'
            self.codigo3d.append(lineaCeil)
            ret = RetornoOp(tag, None)
            return ret
            #elif isinstance(instruccion.parametros, Primitivo):
            #    retorno = self.compilarPrimitivo(instruccion.parametros)
            #    tag = self.generarTemporal()
            #    lineaCeil = self.generarTab() + str(tag) + ' = round(' + str(retorno.valor) + ')'
            #    self.codigo3d.append(lineaCeil)
            #    ret = RetornoOp(tag, None)
            #    return ret
        elif instruccion.tipo == TipoFunNativa.substring:
            # Corresponde a función de SUBSTRING
            pass
        elif instruccion.tipo == TipoFunNativa.sin:
            # Corresponde a función de SIN
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag = self.generarTemporal()
            linea = self.generarTab() + str(tag) + ' = math.sin(' + str(oper.valor) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.sinh:
            # Corresponde a función de SINH
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag = self.generarTemporal()
            linea = self.generarTab() + str(tag) + ' = math.sinh(' + str(oper.valor) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.sind:
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag1 = self.generarTemporal()
            linea = self.generarTab() + str(tag1) + ' = math.sin(' + str(oper.valor) + ')'
            tag2 = self.generarTemporal()
            linea += '\n'
            linea += self.generarTab() + str(tag2) + ' = math.degrees(' + str(tag1) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag2, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.asin:
            # Corresponde a función de ASIN
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag = self.generarTemporal()
            linea = self.generarTab() + str(tag) + ' = math.asin(' + str(oper.valor) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.asinh:
            # Corresponde a función de ASINH
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag = self.generarTemporal()
            linea = self.generarTab() + str(tag) + ' = math.asinh(' + str(oper.valor) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.asind:
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag1 = self.generarTemporal()
            linea = self.generarTab() + str(tag1) + ' = math.asin(' + str(oper.valor) + ')'
            tag2 = self.generarTemporal()
            linea += '\n'
            linea += self.generarTab() + str(tag2) + ' = math.degrees(' + str(tag1) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag2, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.cos:
            # Corresponde a función de COS
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag = self.generarTemporal()
            linea = self.generarTab() + str(tag) + ' = math.cos(' + str(oper.valor) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.cosh:
            # Corresponde a función de COSH
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag = self.generarTemporal()
            linea = self.generarTab() + str(tag) + ' = math.cosh(' + str(oper.valor) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.cosd:
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag1 = self.generarTemporal()
            linea = self.generarTab() + str(tag1) + ' = math.cos(' + str(oper.valor) + ')'
            tag2 = self.generarTemporal()
            linea += '\n'
            linea += self.generarTab() + str(tag2) + ' = math.degrees(' + str(tag1) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag2, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.acos:
            # Corresponde a función de ACOS
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag = self.generarTemporal()
            linea = self.generarTab() + str(tag) + ' = math.acos(' + str(oper.valor) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.acosh:
            # Corresponde a función de ACOSH
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag = self.generarTemporal()
            linea = self.generarTab() + str(tag) + ' = math.acosh(' + str(oper.valor) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.acosd:
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag1 = self.generarTemporal()
            linea = self.generarTab() + str(tag1) + ' = math.acos(' + str(oper.valor) + ')'
            tag2 = self.generarTemporal()
            linea += '\n'
            linea += self.generarTab() + str(tag2) + ' = math.degrees(' + str(tag1) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag2, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.tan:
            # Corresponde a función de TAN
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag = self.generarTemporal()
            linea = self.generarTab() + str(tag) + ' = math.tan(' + str(oper.valor) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.tanh:
            # Corresponde a función de TANH
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag = self.generarTemporal()
            linea = self.generarTab() + str(tag) + ' = math.tanh(' + str(oper.valor) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.tand:
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag1 = self.generarTemporal()
            linea = self.generarTab() + str(tag1) + ' = math.tan(' + str(oper.valor) + ')'
            tag2 = self.generarTemporal()
            linea += '\n'
            linea += self.generarTab() + str(tag2) + ' = math.degrees(' + str(tag1) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag2, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.atan:
            # Corresponde a función de ATAN
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag = self.generarTemporal()
            linea = self.generarTab() + str(tag) + ' = math.atan(' + str(oper.valor) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.atanh:
            # Corresponde a función de ATANH
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag = self.generarTemporal()
            linea = self.generarTab() + str(tag) + ' = math.atanh(' + str(oper.valor) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.atan2:
            # Corresponde a función de ATAN2
            if instruccion.numparametros == 2:
                oper1 = self.compilarOperacionAritmetica(instruccion.parametros[0])
                oper2 = self.compilarOperacionAritmetica(instruccion.parametros[1])
                tag = self.generarTemporal()
                linea = self.generarTab() + str(tag) + ' = math.atan2(' + str(oper1.valor) + ', ' + str(oper2.valor) + ')'
                self.codigo3d.append(linea)
                ret = RetornoOp(tag, None)
                return ret
        elif instruccion.tipo == TipoFunNativa.atand:
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag1 = self.generarTemporal()
            linea = self.generarTab() + str(tag1) + ' = math.atan(' + str(oper.valor) + ')'
            tag2 = self.generarTemporal()
            linea += '\n'
            linea += self.generarTab() + str(tag2) + ' = math.degrees(' + str(tag1) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag2, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.atan2d:
            # Corresponde a función de ATAN2
            if instruccion.numparametros == 2:
                oper1 = self.compilarOperacionAritmetica(instruccion.parametros[0])
                oper2 = self.compilarOperacionAritmetica(instruccion.parametros[1])
                tag1 = self.generarTemporal()
                linea = self.generarTab() + str(tag1) + ' = math.atan2(' + str(oper1.valor) + ', ' + str(oper2.valor) + ')'
                tag2 = self.generarTemporal()
                linea += '\n'
                linea += self.generarTab() + str(tag2) + ' = math.degrees(' + str(tag1) + ')'
                self.codigo3d.append(linea)
                ret = RetornoOp(tag2, None)
                return ret
        elif instruccion.tipo == TipoFunNativa.cot:
            # Corresponde a función de COT
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag1 = self.generarTemporal()
            linea = self.generarTab() + str(tag1) + ' = math.tan(' + str(oper.valor) + ')'
            tag2 = self.generarTemporal()
            linea += '\n'
            linea += self.generarTab() + str(tag2) + ' = 1 / ' + tag1
            self.codigo3d.append(linea)
            ret = RetornoOp(tag2, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.cotd:
            # Corresponde a función de COTD
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag1 = self.generarTemporal()
            linea = self.generarTab() + str(tag1) + ' = math.tan(' + str(oper.valor) + ')'
            tag2 = self.generarTemporal()
            linea += '\n'
            linea += self.generarTab() + str(tag2) + ' = 1 / ' + tag1
            tag3 = self.generarTemporal()
            linea += '\n'
            linea += self.generarTab() + str(tag3) + ' = math.degrees(' + str(tag2) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag2, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.degree:
            # Corresponde a función de DEGREES
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag = self.generarTemporal()
            linea = self.generarTab() + str(tag) + ' = math.degrees(' + str(oper.valor) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.factorial:
            # Corresponde a función de FACTORIAL
            oper = oper = self.compilarOperacionAritmetica(instruccion.parametros)
            etiquetaSalida = self.generarEtiqueta()
            etiquetaLoop = self.generarEtiqueta()
            factorial = self.generarTemporal()
            pivot = self.generarTemporal()
            self.codigo3d.append(self.generarTab() + factorial + ' = ' + str(oper.valor))
            self.codigo3d.append(self.generarTab() + pivot + ' = 1')

            # IF de salida (if entrada < 0)
            self.agregarIf(factorial + ' < 0' , etiquetaSalida)
            # IF de salida (if entrada == 0)
            self.agregarIf(factorial + ' == 0', etiquetaSalida)
            # IF de salida (if entrada == 1)
            self.agregarIf(factorial + ' == 1', etiquetaSalida)
            self.generarGoto(etiquetaLoop)
            self.agregarEtiqueta(etiquetaLoop)

            etiquetaTrue = self.generarEtiqueta()

            self.agregarIf(factorial + ' > 0', etiquetaTrue)
            self.generarGoto(etiquetaSalida)

            self.agregarEtiqueta(etiquetaTrue)
            self.codigo3d.append(self.generarTab() + pivot + ' = ' + pivot + ' * ' + factorial)
            self.codigo3d.append(self.generarTab() + factorial + ' = ' + factorial + ' - 1')
            self.generarGoto(etiquetaLoop)

            self.agregarEtiqueta(etiquetaSalida)
            ret = RetornoOp(pivot, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.div:
            # Corresponde a función de DIV
            if instruccion.numparametros == 2:
                oper1 = self.compilarOperacionAritmetica(instruccion.parametros[0])
                oper2 = self.compilarOperacionAritmetica(instruccion.parametros[1])
                tag = self.generarTemporal()
                linea = self.generarTab() + str(tag) + ' = ' + str(oper1.valor) + ' / ' + str(oper2.valor)
                self.codigo3d.append(linea)
                ret = RetornoOp(tag, None)
                return ret
        elif instruccion.tipo == TipoFunNativa.ln:
            # Corresponde a función de LN
            oper = self.compilarOperacionAritmetica(instruccion.parametros)
            tag = self.generarTemporal()
            linea = self.generarTab() + str(tag) + ' = math.ln(' + str(oper.valor) + ')'
            self.codigo3d.append(linea)
            ret = RetornoOp(tag, None)
            return ret
        elif instruccion.tipo == TipoFunNativa.log:
            if instruccion.numparametros == 1:
                oper = self.compilarOperacionAritmetica(instruccion.parametros[0])
                tag = self.generarTemporal()
                linea = self.generarTab() + str(tag) + ' = math.log(' + str(oper.valor) + ')'
                self.codigo3d.append(linea)
                ret = RetornoOp(tag, None)
                return ret
            elif instruccion.numparametros == 2:
                oper1 = self.compilarOperacionAritmetica(instruccion.parametros[0])
                oper2 = self.compilarOperacionAritmetica(instruccion.parametros[1])
                tag = self.generarTemporal()
                linea = self.generarTab() + str(tag) + ' = math.log(' + str(oper1.valor) + ', ' + str(oper2.valor) + ')'
                self.codigo3d.append(linea)
                ret = RetornoOp(tag, None)
                return ret
        elif instruccion.tipo == TipoFunNativa.mod:
            # Corresponde a función de MOD
            if instruccion.numparametros == 2:
                oper1 = self.compilarOperacionAritmetica(instruccion.parametros[0])
                oper2 = self.compilarOperacionAritmetica(instruccion.parametros[1])
                tag = self.generarTemporal()
                linea = self.generarTab() + str(tag) + ' = ' + str(oper1.valor) + ' % ' + str(oper2.valor)
                self.codigo3d.append(linea)
                ret = RetornoOp(tag, None)
                return ret