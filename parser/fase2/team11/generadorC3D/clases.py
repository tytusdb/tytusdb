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