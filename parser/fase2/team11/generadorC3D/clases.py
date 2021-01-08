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