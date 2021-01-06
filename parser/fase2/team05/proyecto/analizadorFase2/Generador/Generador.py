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
        temp = "T" + str(self.temp)
        self.temp += 1
        return temp

    def generarTab(self):
        return "\t"

    def generarEtiqueta(self):
        label = ".L" + str(self.label)
        self.label += 1
        return label

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
            inst = self.generarTab() + id + "=" + valor
        else:
            inst = self.generarTab() + id + "=" + str(valor)
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
        for linea in self.codigo3d:
            print(linea)

    def compilarFuncion(self, instruccion):
        self.agregarFuncion(instruccion.id)
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
                self.compilarPrimitivo
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
        self.generarLlamada(instruccion.id)
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
                self.compilarPrimitivo
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

    def compilarDropFunction(self, instruccion):
        inst = self.generarTab() + "del " + instruccion.id
        self.codigo3d.append(inst)

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
                temporal = self.generarTemporal()
                self.generarAsignacion(temporal, instruccion.valor)
                self.generarAsignacion("lista", "[" + temporal + "]")
                self.generarLlamada("funcionintermedia")
            else:
                ret = RetornoOp(instruccion.valor, instruccion.tipo)
                return ret
        elif isinstance(instruccion, Llamada):
            return self.compilarLlamada(instruccion)