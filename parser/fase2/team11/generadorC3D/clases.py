from enum import Enum
from datetime import date
from datetime import datetime
#from .Retorno import *

from generadorC3D.Retorno import Retorno

class Nodo:
    '''Clase que define la estructura de los nodos del AST.'''
    
    def __init__(self, etiqueta, valor = '', hijos = [], linea = -1, columna = -1, gramatica = '', codigo3d = ''):
        self.etiqueta = etiqueta
        self.valor = valor
        self.hijos = hijos
        self.linea = linea
        self.columna = columna
        self.gramatica = gramatica
        self.codigo3d = codigo3d

    def toString(self):
        cadena = self.etiqueta + ',' + self.valor + ' L: ' + str(self.linea) + ' C: ' + str(self.columna)+'\n'
        for n in self.hijos:
            cadena = cadena + ' --- ' + n.toString()
        return cadena

#---------------------------------------------------------------------------------------------------------------
class EType(Enum):
    LEXICO      = 1
    SINTACTICO  = 2
    SEMANTICO   = 3

class Error:
    '''
    Clase utilizada para el manero de errores
    Atributos:
        code        - codigo de error (según errores definidos pos SQL)
        error_type  - tipo de error (EType)
        description - descripción del error
        line        - linea en la cual ocurrió
        column      - columna en la cual ocurrió
    '''
    def __init__(self,code,error_type,description = '',line = -1,column = -1):
        self.code = code
        self.error_type = error_type
        self.description = description
        self.line = line
        self.column = column
    
    def toString(self):
        return str(self.code)+'\t'+str(self.error_type.name)+'\t'+str(self.description)+'\tL: '+str(self.line)


class TBProcedimientos:
    def __init__(self, nombre, tipo, retorna = '', parametros = [], declaraciones = [], estado = 'Activo'):
        self.nombre = nombre
        self.tipo = tipo
        self.retorna = retorna
        self.parametros = parametros
        self.declaraciones = declaraciones
        self.estado = estado
    
    def toString(self):
        param = ''
        for par in self.parametros:
            param += par + ', '
        return '\tNombre: '+str(self.nombre)+'\tTipo: '+str(self.tipo)+'\tRetorna: '+str(self.retorna)+'\tParametros: '+param

    def toStringParams(self):
        param = ''
        for par in self.parametros:
            param += par + '<br>'
        return param

    def toStringDeclaraciones(self):
        decla = ''
        for d in self.declaraciones:
            decla += d + '<br>'
        return decla
    
## se genera codigo en 3d de los procedimientos y funciones
class TraducirProcedimientos:
    def __init__(self, raiz, codigo3d, conTemp, TSprocedimientos = [], label = 0):
        self.raiz = raiz
        self.codigo3d = codigo3d
        self.conTemp = conTemp
        self.TSprocedimientos = TSprocedimientos
        self.label = label

    def asignarEn3d(self, id, temval):
        if isinstance(temval, str):
            cd3 = '\t'+ id + " = " + temval
        else:
            cd3 = '\t'+ id + " = " + str(temval)
        self.codigo3d.append(cd3)

    def crearTemp(self):
        t = "t" + str(self.conTemp)
        self.conTemp += 1
        return t

    def crearEtiqueta(self):
        lb = ".L" + str(self.label)
        self.label += 1
        return lb

    def addEtiqueta(self, etiqueta):
        c3d = "\tlabel " + etiqueta
        self.codigo3d.append(c3d)

    def addGoto(self, etiqueta):
        c3d = "\tgoto " + etiqueta 
        self.codigo3d.append(c3d)

    def addIF(self, cond, etiqueta):
        c3d = "\tif " + cond + ": goto " + etiqueta
        self.codigo3d.append(c3d)

    def traducir(self):

        for nodo in self.raiz.hijos:
            if nodo.etiqueta.lower() != 'drop':
                self.generarCodigo3d(nodo)
            else:
                self.eliminarFuncion(nodo)

    def eliminarFuncion(self, nodo):
        for tb in self.TSprocedimientos:
            if nodo.valor == tb.nombre:
                tb.estado = 'ELIMINADO'
                break

    def generarCodigo3d(self, nodo):
        nombre = nodo.valor
        tipo = nodo.etiqueta
        retorno = 'None'
        parametros = []
        declaraciones = []

        cd3 = '\n\n@with_goto'
        self.codigo3d.append(cd3)
        cd3 = 'def '+ nombre +'():'  

        for nd in nodo.hijos:
            if nd.etiqueta.lower() == 'parametros':
                self.agregarParametros(nd, parametros, cd3)
            elif nd.etiqueta.lower() == 'returns':
                retorno = self.agregarTipoRetorno(nd)
            elif nd.etiqueta.lower() == 'cuerpo':
                if len(parametros) == 0:
                    self.codigo3d.append(cd3)
                    self.codigo3d.append('\tglobal pila')
                self.agregarCuerpo(nd, declaraciones)

        ts = TBProcedimientos(nombre, tipo, retorno, parametros, declaraciones)
        self.TSprocedimientos.append(ts)

    def agregarParametros( self, nodo, parametros, cd3):
        params = ''
        for nd in nodo.hijos:
            if nd.etiqueta == 'ID':    
                params += ' '+nd.valor+','
                parametros.append(nd.valor)

        if params != '':
            params = params[:-1]
            cd3 = cd3.replace('():', '(' + params+'):')
            self.codigo3d.append(cd3)
            self.codigo3d.append('\tglobal pila')

    def agregarTipoRetorno(self, nodo):
        nd = nodo.hijos[0]
        if nd.etiqueta == "TYPE COLUMN":
            return nd.valor

    def agregarCuerpo(self, nodo, declaraciones):
        for nd in nodo.hijos:
            if nd.etiqueta.lower() == 'declare':
                self.agregarDeclaraciones(nd, declaraciones)
            elif nd.etiqueta.lower() == 'begin':
                listainstr = nd.hijos[0]
                self.agregarBloques(listainstr)

    def agregarDeclaraciones(self, nodo, declaraciones):
        for nd in nodo.hijos:
            if len(nd.hijos) == 3:
                name = nd.hijos[0].valor
                nodoexp = nd.hijos[2].hijos[0]
                exp = self.agregarOperacionLogica(nodoexp)
                self.asignarEn3d(name, exp.valor)
                declaraciones.append(name +':'+ nd.hijos[1].valor)
            if len(nd.hijos) == 2:
                name = nd.hijos[0].valor
                self.asignarEn3d(name, 0)
                declaraciones.append(nd.hijos[0].valor +':'+ nd.hijos[1].valor)

    def agregarBloques(self, nodo):
        for nd in nodo.hijos:
            if nd.etiqueta.lower() == 'if':
                self.agregarIF(nd)
            elif nd.etiqueta.lower() == 'asignacion':
                self.agregarAsignacion(nd)
            elif nd.etiqueta.lower() == 'return':
                self.agregarReturn(nd)
            elif nd.etiqueta.lower() == 'execute':
                pass
            elif nd.etiqueta.lower() == 'insert into':
                self.agregarSQL(nd)
            elif nd.etiqueta.lower() == 'update':
                self.agregarSQL(nd)
            elif nd.etiqueta.lower() == 'delete':
                self.agregarSQL(nd)
            elif nd.etiqueta.lower() == 'truncate':
                self.agregarSQL(nd)
            elif nd.etiqueta.lower() == 'drop':
                self.agregarSQL(nd)
            elif nd.etiqueta.lower() == 'alter':
                self.agregarSQL(nd)
            elif nd.etiqueta.lower() == 'create index':
                self.agregarSQL(nd)
            
    def agregarSQL(self, nodo):
        nodo.valor = nodo.valor.replace('\n', ' ')
        nodo.valor = nodo.valor.replace('\'', '\\\'')
        nodo.valor = nodo.valor.replace('\t', ' ')
        temp = self.crearTemp()
        self.asignarEn3d(temp, '\''+nodo.valor+'\'')
        self.asignarEn3d('pila', '[' + temp+']')
        cd3 = '\tfuncionIntermedia()'
        self.codigo3d.append(cd3)

    def agregarAsignacion(self, nodo):
        id = nodo.hijos[0].valor
        exp = self.agregarOperacionLogica(nodo.hijos[1])
        self.asignarEn3d(id, exp.valor)

    def agregarReturn(self, nodo):
        if len(nodo.hijos) > 0:   #retorna algun valor
            exp = self.agregarOperacionLogica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, exp.valor)
            c3d = '\treturn '+ temp
            self.codigo3d.append(c3d)
        else:                      #return de procedimientos
            c3d = '\treturn'
            self.codigo3d.append(c3d)

    def agregarIF(self, nodo):
        if nodo.etiqueta.lower() == 'if':
            nodoCondicion = nodo.hijos[0]
            condicion = self.agregarOperacionLogica(nodoCondicion.hijos[0])
            etiquetaverdadero = self.crearEtiqueta()
            etiquetafalso = self.crearEtiqueta()
            if len(nodo.hijos) == 3:        # es solo un if
                self.addIF(condicion.valor + " == " + str(True), etiquetaverdadero)
                self.addGoto(etiquetafalso)
                self.addEtiqueta(etiquetaverdadero)
                self.agregarCuerpoIF(nodo.hijos[1])
                self.addEtiqueta(etiquetafalso)
            elif len(nodo.hijos) == 4:      # es un if con else
                etiquetasalida = self.crearEtiqueta()
                self.addIF(condicion.valor + " == " + str(True), etiquetaverdadero)
                self.addGoto(etiquetafalso)
                self.addEtiqueta(etiquetaverdadero)
                self.agregarCuerpoIF(nodo.hijos[1])
                self.addGoto(etiquetasalida)
                self.addEtiqueta(etiquetafalso)
                self.agregarCuerpoIF(nodo.hijos[2])
                self.addEtiqueta(etiquetasalida)
        elif nodo.etiqueta.lower() == 'else':
            pass

    def agregarCuerpoIF(self, nodo):
        for nd in nodo.hijos:
            if nd.etiqueta.lower() == 'if':
                self.agregarIF(nd)
            elif nd.etiqueta.lower() == 'asignacion':
                self.agregarAsignacion(nd)
            elif nd.etiqueta.lower() == 'return':
                self.agregarReturn(nd)
            elif nd.etiqueta.lower() == 'insert into':
                self.agregarSQL(nd)
            elif nd.etiqueta.lower() == 'update':
                self.agregarSQL(nd)
            elif nd.etiqueta.lower() == 'delete':
                self.agregarSQL(nd)
            elif nd.etiqueta.lower() == 'truncate':
                self.agregarSQL(nd)
            elif nd.etiqueta.lower() == 'drop':
                self.agregarSQL(nd)
            elif nd.etiqueta.lower() == 'alter':
                self.agregarSQL(nd)
            elif nd.etiqueta.lower() == 'create index':
                self.agregarSQL(nd)

    def agregarOperacionLogica(self, nodo):
        if nodo.etiqueta.lower() == 'oplog':
            if nodo.valor.lower() == 'or':
                izquierdo = self.agregarOperacionLogica(nodo.hijos[0])
                derecho = self.agregarOperacionLogica(nodo.hijos[1])
                temporal = self.crearTemp()
                etiquetatrue = self.crearEtiqueta()
                etiquetafalse = self.crearEtiqueta()
                etiquetafalse1 = self.crearEtiqueta()
                etiquetasalida = self.crearEtiqueta()
                self.addIF(izquierdo.valor + " == " + str(True), etiquetatrue)
                self.addGoto(etiquetafalse)
                self.addEtiqueta(etiquetafalse)

                self.addIF(derecho.valor + " == " + str(True), etiquetatrue)
                self.addGoto(etiquetafalse1)
                self.addEtiqueta(etiquetatrue)
                
                self.asignarEn3d(temporal, True)
                self.addGoto(etiquetasalida)
                self.addEtiqueta(etiquetafalse1)
                
                self.asignarEn3d(temporal, False)
                self.addEtiqueta(etiquetasalida)
                r = Retorno(temporal, None)
                return r
            elif nodo.valor.lower() == 'and':
                izquierdo = self.agregarOperacionLogica(nodo.hijos[0])
                derecho = self.agregarOperacionLogica(nodo.hijos[1])
                temporal = self.crearTemp()
                etiquetatrue = self.crearEtiqueta()
                etiquetafalse = self.crearEtiqueta()
                etiquetatrue1 = self.crearEtiqueta()
                etiquetasalida = self.crearEtiqueta()
                self.addIF(izquierdo.valor + ' == ' + str(True), etiquetatrue)
                self.addGoto(etiquetafalse)
                self.addEtiqueta(etiquetatrue)
                
                self.addIF(derecho.valor + ' == ' + str(True), etiquetatrue1)
                self.addGoto(etiquetafalse)
                self.addEtiqueta(etiquetatrue1)
                
                self.asignarEn3d(temporal, True)
                self.addGoto(etiquetasalida)
                self.addEtiqueta(etiquetafalse)
                
                self.asignarEn3d(temporal, False)
                self.addEtiqueta(etiquetasalida)  
                r = Retorno(temporal, None)
                return r
            elif nodo.valor.lower() == 'not':
                izquierdo = self.agregarOperacionLogica(nodo.hijos[0])
                temporal = self.crearTemp()
                etiquetatrue = self.crearEtiqueta()
                etiquetafalse = self.crearEtiqueta()
                etiquetasalida = self.crearEtiqueta()
                self.addIF(izquierdo.valor + ' == ' + str(True), etiquetatrue)
                self.addGoto(etiquetafalse)
                self.addEtiqueta(etiquetatrue)
                
                self.asignarEn3d(temporal, False)
                self.addGoto(etiquetasalida)
                self.addEtiqueta(etiquetafalse)
                
                self.asignarEn3d(temporal, True)
                self.addEtiqueta(etiquetasalida)
                r = Retorno(temporal, None)
                return r 
        elif nodo.etiqueta.lower() == 'oprel':
            return self.agregarOperacionRelacional(nodo)
        else:
            return self.agregarOperacionAritmetica(nodo)

    def agregarOperacionRelacional(self, nodo):
        if nodo.etiqueta.lower() == 'oprel':
            izquierdo = self.agregarOperacionRelacional(nodo.hijos[0])
            derecho = self.agregarOperacionRelacional(nodo.hijos[1])   
            temporal = self.crearTemp()
            etiquetatrue = self.crearEtiqueta()
            etiquetafalse = self.crearEtiqueta()
            etiquetasalida = self.crearEtiqueta()

            nodo.valor = nodo.valor.replace('\\', '')
            if nodo.valor.lower() == '=':
                self.addIF(str(izquierdo.valor) + "==" + str(derecho.valor), etiquetatrue)
                self.addGoto(etiquetafalse)
                self.addEtiqueta(etiquetatrue)

                self.asignarEn3d(temporal, True)
                self.addGoto(etiquetasalida)
                self.addEtiqueta(etiquetafalse)

                self.asignarEn3d(temporal, False)
                self.addEtiqueta(etiquetasalida)
                t = Retorno(temporal, None)
                return t
            elif nodo.valor.lower() == '<':
                self.addIF(str(izquierdo.valor) + "<" + str(derecho.valor), etiquetatrue)
                self.addGoto(etiquetafalse)
                self.addEtiqueta(etiquetatrue)
                
                self.asignarEn3d(temporal, True)
                self.addGoto(etiquetasalida)
                self.addEtiqueta(etiquetafalse)
                
                self.asignarEn3d(temporal, False)
                self.addEtiqueta(etiquetasalida)
                r = Retorno(temporal, None)
                return r
            elif nodo.valor.lower() == '>':
                self.addIF(str(izquierdo.valor) + ">" + str(derecho.valor), etiquetatrue)
                self.addGoto(etiquetafalse)
                self.addEtiqueta(etiquetatrue)
                
                self.asignarEn3d(temporal, True)
                self.addGoto(etiquetasalida)
                self.addEtiqueta(etiquetafalse)
                
                self.asignarEn3d(temporal, False)
                self.addEtiqueta(etiquetasalida)
                t = Retorno(temporal, None)
                return t
            elif nodo.valor.lower() == '<=':
                self.addIF(str(izquierdo.valor) + "<=" + str(derecho.valor), etiquetatrue)
                self.addGoto(etiquetafalse)
                self.addEtiqueta(etiquetatrue)
                
                self.asignarEn3d(temporal, True)
                self.addGoto(etiquetasalida)
                self.addEtiqueta(etiquetafalse)
                
                self.asignarEn3d(temporal, False)
                self.addEtiqueta(etiquetasalida)
                t = Retorno(temporal, None)
                return t
            elif nodo.valor.lower() == '>=':
                self.addIF(str(izquierdo.valor) + ">=" + str(derecho.valor), etiquetatrue)
                self.addGoto(etiquetafalse)
                self.addEtiqueta(etiquetatrue)
                
                self.asignarEn3d(temporal, True)
                self.addGoto(etiquetasalida)
                self.addEtiqueta(etiquetafalse)
                
                self.asignarEn3d(temporal, False)
                self.addEtiqueta(etiquetasalida)
                t = Retorno(temporal, None)
                return t
            elif nodo.valor.lower() == '<>':
                self.addIF(str(izquierdo.valor) + "!=" + str(derecho.valor), etiquetatrue)
                self.addGoto(etiquetafalse)
                self.addEtiqueta(etiquetatrue)
                
                self.asignarEn3d(temporal, True)
                self.addGoto(etiquetasalida)
                self.addEtiqueta(etiquetafalse)
                
                self.asignarEn3d(temporal, False)
                self.addEtiqueta(etiquetasalida)  
                t = Retorno(temporal, None)
                return t
        else:
            return self.agregarOperacionAritmetica(nodo)

    def agregarOperacionAritmetica(self, nodo):
        if nodo.etiqueta.lower() == 'oparit':
            izquierdo = self.agregarOperacionAritmetica(nodo.hijos[0])
            derecho = self.agregarOperacionAritmetica(nodo.hijos[1])
            temporal = self.crearTemp()
            if nodo.valor.lower() == '+':
                self.asignarEn3d(temporal, str(izquierdo.valor) + "+" + str(derecho.valor))
                t = Retorno(temporal, None)
                return t
            elif nodo.valor.lower() == '-':
                self.asignarEn3d(temporal, str(izquierdo.valor) + "-" + str(derecho.valor))
                t = Retorno(temporal, None)
                return t
            elif nodo.valor.lower() == '*':
                self.asignarEn3d(temporal, str(izquierdo.valor) + "*" + str(derecho.valor))
                t = Retorno(temporal, None)
                return t
            elif nodo.valor.lower() == '/':
                self.asignarEn3d(temporal, str(izquierdo.valor) + "/" + str(derecho.valor))
                t = Retorno(temporal, None)
                return t
            elif nodo.valor.lower() == '%':
                self.asignarEn3d(temporal, str(izquierdo.valor) + "%" + str(derecho.valor))
                t = Retorno(temporal, None)
                return t 
            elif nodo.valor.lower() == '^':
                self.asignarEn3d(temporal, str(izquierdo.valor) + "**" + str(derecho.valor))
                t = Retorno(temporal, None)
                return t
        elif nodo.etiqueta.lower() == 'entero':
            t = Retorno(nodo.valor, 'int')
            return t
        elif nodo.etiqueta.lower() == 'decimal':
            t = Retorno(nodo.valor, 'float')
            return t
        elif nodo.etiqueta.lower() == 'cadena':
            t = Retorno('\''+nodo.valor+'\'', 'string')
            return t
        elif nodo.etiqueta.lower() == 'logico':
            t = Retorno(nodo.valor, 'boolean')
            return t
        elif nodo.etiqueta.lower() == 'negativo':
            izquierdo = self.agregarOperacionAritmetica(nodo.hijos[0])
            temporal = self.crearTemp()
            self.asignarEn3d(temporal, "-" + str(izquierdo.valor))
            ret = Retorno(temporal, 'int')
            return ret
        elif nodo.etiqueta.lower() == 'id':
            t = Retorno(nodo.valor, 'id')
            return t
        elif nodo.etiqueta.lower() == 'matematica':
            return self.agregarFuncionMatematica(nodo)
        elif nodo.etiqueta.lower() == 'trigonometrica':
            return self.agregarFuncionTrigonometrica(nodo)
        elif nodo.etiqueta.lower() == 'binaria':
            return self.agregarFuncionBinaria(nodo)
        elif nodo.etiqueta.lower() == 'select':
            temporal1 = self.crearTemp()
            temporal2 = self.crearTemp()
            nodo.valor = nodo.valor.replace('\'', '\\\'')
            nodo.valor = nodo.valor.replace('\"', '\\\"')
            self.asignarEn3d(temporal1, '\''+nodo.valor+'\'')
            self.asignarEn3d('pila', '['+temporal1+']')
            cd3 = '\tfuncionIntermedia()'
            self.codigo3d.append(cd3)
            self.asignarEn3d(temporal2, 'pila[0]')
            t = Retorno(temporal2, 'select')
            return t
        

    def agregarFuncionMatematica(self, nodo):
        if nodo.valor.lower() == 'abs': 
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.fabs(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'cbrt':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'np.cbrt(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'ceil':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.ceil(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'ceiling':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.ceil(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'div':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            exp1 = self.agregarOperacionAritmetica(nodo.hijos[1])
            temp = self.crearTemp()
            self.asignarEn3d(temp, str(exp.valor) +'/'+ str(exp1.valor))
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'degrees':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.degrees(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'exp':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.exp('+str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'factorial':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.factorial('+str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'floor':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.floor('+str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'gcd':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            exp1 = self.agregarOperacionAritmetica(nodo.hijos[1])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.gcd('+str(exp.valor)+','+str(exp1.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'ln':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.log('+str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'log':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.log10('+str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'mod':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            exp1 = self.agregarOperacionAritmetica(nodo.hijos[1])
            temp = self.crearTemp()
            self.asignarEn3d(temp, str(exp.valor)+'%'+str(exp1.valor))
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'pi':
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.pi')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'power':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            exp1 = self.agregarOperacionAritmetica(nodo.hijos[1])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.pow('+str(exp.valor)+','+str(exp1.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'radians':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.radians('+str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'round':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'round('+str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'sign':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'np.sign('+str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'sqrt':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.sqrt('+str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'trunc':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.trunc('+str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'random':
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'rd.random()')
            ret = Retorno(temp, None)
            return ret

    def agregarFuncionTrigonometrica(self, nodo):
        if nodo.valor.lower() == 'acos': 
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.acos(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'acosd':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.acos(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'asin': 
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.asin(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'asind': 
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.asin(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'atan': 
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.atan(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'atand': 
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.atan(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'cos': 
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.cos(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'cosd': 
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.cos(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'sin': 
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.sin(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'sind':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.sin(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'tan': 
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.tan(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'tand':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.tan(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'sinh': 
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.sinh(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'cosh':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.cosh(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'tanh': 
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.tanh(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'asinh':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.asinh(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'acosh': 
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.acosh(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'atanh':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'math.atanh(' + str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret

    def agregarFuncionBinaria(self, nodo):
        if nodo.valor.lower() == 'length':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, 'len('+str(exp.valor)+')')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'substring':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            exp1 = self.agregarOperacionAritmetica(nodo.hijos[1])
            exp2 = self.agregarOperacionAritmetica(nodo.hijos[2])
            temp = self.crearTemp()
            self.asignarEn3d(temp, str(exp.valor)+'['+str(exp1.valor)+':'+str(exp2.valor)+']')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'substr':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            exp1 = self.agregarOperacionAritmetica(nodo.hijos[1])
            exp2 = self.agregarOperacionAritmetica(nodo.hijos[2])
            temp = self.crearTemp()
            self.asignarEn3d(temp, str(exp.valor)+'['+str(exp1.valor)+':'+str(exp2.valor)+']')
            ret = Retorno(temp, None)
            return ret
        elif nodo.valor.lower() == 'trim':
            exp = self.agregarOperacionAritmetica(nodo.hijos[0])
            temp = self.crearTemp()
            self.asignarEn3d(temp, str(exp.valor)+'.strip()')
            ret = Retorno(temp, None)
            return ret



    def imprimirTS(self):
        print('\n ------------- TABLA DE SIMBOLOS PROCEDIMIENTOS Y FUNCIONES -------------\n')
        for tb in self.TSprocedimientos:
            print(tb.toString())

    def generateProYFunc(self):
        now = datetime.now()
        fecha = 'Fecha: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)
        hora = 'Hora: '+str(now.hour)+':'+str(now.minute)
        header = '<html><head><br><title>REPORTE DE PROCEDIMIENTOS Y FUNCIONES</title></head><body>\n<H1 ALIGN=CENTER><b><font face="Roboto" color="#1f253d">REPORTE DE PROCEDIMIENTOS Y FUNCIONES</font></b></H1>\n<H4 ALIGN=CENTER><b><font face="Roboto" color="#1f253d">'+fecha+' | '+hora+'</font></b></H4>\n'
        tbhead = '<table align="center" cellpadding="20" cellspacing="0"  style="border:2px solid #1f253d">\n'
        tbhead += '<tr>\n'
        tbhead += '<td bgcolor="#2d48b5" width="150" style="text-align:center"><font face="Roboto" color="white" size="4">NOMBRE</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="150" style="text-align:center"><font face="Roboto" color="white" size="4">TIPO</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="100" style="text-align:center"><font face="Roboto" color="white" size="4">RETORNA</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="50" style="text-align:center"><font face="Roboto" color="white" size="4">PARAMETROS</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="50" style="text-align:center"><font face="Roboto" color="white" size="4">DECLARACIONES</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="50" style="text-align:center"><font face="Roboto" color="white" size="4">ESTADO</font></td>\n'
        tbhead += '</tr>\n'
        cont = ''
        template = open("ReporteProYFunc.html", "w")

        # Iteración sobre las tablas de la DB
        
        for comp in self.TSprocedimientos:
            cont += '<tr>\n'
            cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+comp.nombre.upper()+'</font></td>\n'
            cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+comp.tipo.upper()+'</font></td>\n'
            cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+comp.retorna.upper()+'</font></td>\n'
            cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+comp.toStringParams()+'</font></td>\n'
            cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+comp.toStringDeclaraciones()+'</font></td>\n'
            cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+comp.estado.upper()+'</font></td>\n'
            cont += '</tr>\n'
        template.write(header)
        template.write(tbhead)
        template.write(cont)
        template.write("</table> \n</body> \n</html>")
        template.close()

    ## ---------------------- REPORTE EN EJECUCION --------------------------------------

    def crearReporte(self) :
        file = open("ReporteEjecucionPL.md", "w")
        file.write('## GRUPO #11 \n'
                + '# *REPORTE GRAMATICAL DE LA EJECUCION PL*\n\n')
        file.write(self.recorrerAST(self.raiz))
        file.close()

    def recorrerAST(self, nodo):
        bnf = ""
        contador = 1
        for hijo in nodo.hijos: 
            bnf += '### Instruccion #'+str(contador)+' \n'
            bnf += '```bnf\n'
            bnf += hijo.gramatica + '\n'
            bnf += self.recorrerHijo(hijo)
            bnf += '```\n\n'
            contador += 1
        return bnf

    def recorrerHijo(self, nodo):
        bnf = ""
        for hijo in nodo.hijos: 
            if hijo.gramatica != '':
                bnf += hijo.gramatica + '\n'
            bnf += self.recorrerHijo(hijo)
        return bnf