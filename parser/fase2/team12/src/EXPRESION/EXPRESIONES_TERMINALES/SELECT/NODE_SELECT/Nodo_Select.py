import sys, os

nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..')) + '\\EXPRESION\\')
sys.path.append(nodo_dir)

nodo_ast = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..','..')) + '\\ENTORNO\\')
sys.path.append(nodo_ast)

nodo_select = (os.path.abspath(os.path.dirname(__file__)))
sys.path.append(nodo_select)

nodo_function_select = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..','..')) + '\\DML\\Select\\')
sys.path.append(nodo_function_select)

start_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..','..')) + '\\Start\\')
sys.path.append(start_dir)

c3d_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..','..')) + '\\C3D\\')
sys.path.append(c3d_dir)

from Expresion import Expresion
from Tipo import Data_Type
from Tipo_Expresion import Type_Expresion
from Response_Exp import Response
from Select import Select
from Traduccion import *
from Label import *
from Temporal import *

class Select_Expresion(Expresion):
    
    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)
        self.tipo = Type_Expresion(Data_Type.non)
    
    def execute(self, eviroment):
        
        dataSelect = Response()
        nodoSelect = Select_Expresion("SENTENCIA_SELECT",self.fila,self.columna,self.valor)
        nodoSelect.hijos = self.hijos

        # Solamente viene una lista de expresiones.
        if len(self.hijos) == 1 :

            lista_Exp = self.hijos[0]
            l = []
            tipoVariable = None
            for exp in lista_Exp.hijos :

                value = exp.execute(eviroment)

                if exp.tipo.data_type == Data_Type.error :
                    print("Error: ")
                else :

                    if exp.nombreNodo == 'ALIAS':
                        dataSelect.encabezados.append(exp.alias)
                    else :
                        dataSelect.encabezados.append('?column?')
                    
                    l.append(value)
                    self.tipo = exp.tipo
                    self.valorExpresion = value

            dataSelect.data.append(l)

            if len(l) == 1 :
                if self.tipo.data_type == Data_Type.error or self.tipo.data_type == Data_Type.non :

                    self.tipo = Type_Expresion(Data_Type.error)
                    self.valorExpresion = None
                    self.dataResult = dataSelect
                    return dataSelect

                else:

                    self.dataResult = dataSelect
                    return self.valorExpresion

            else:

                self.tipo = Type_Expresion(Data_Type.listaDatos)
                self.isLista = True
                    
            return dataSelect
                
        else :
            #SENTENCIA_SELECT_DISTINCT
            functionSelect = Select()
            result = functionSelect.execute(nodoSelect, eviroment)
            responseSelect = Response()



            if self.nombreNodo == "SENTENCIA_SELECT_DISTINCT":
                resultDistinct = {}
                for r in result:
                    resultDistinct[' '.join(map(str, r))] = r
                result =  []
                for res in resultDistinct:
                    result.append(resultDistinct[res])
            encabezados = []
            tipos = []
            for encabezado in functionSelect.encabezadoRetorno:
                encabezados.append(encabezado.nombre)
                tipos.append(encabezado.tipo)

            responseSelect.encabezados = encabezados 
            responseSelect.data = result.data
            responseSelect.tipos = tipos
            responseSelect.tipoUnico = result.tipoUnico
            responseSelect.valorUnico = result.valorUnico
            if responseSelect.tipoUnico == None:
                self.tipo = Type_Expresion(Data_Type.listaDatos)
                self.dataResult = responseSelect
                return responseSelect
            else:
                self.tipo = Type_Expresion(responseSelect.tipoUnico)
                self.dataResult = responseSelect
                self.valorExpresion = responseSelect.valorUnico
            return self.valorExpresion

    def compile(self, enviroment):
        temporalAsignado = instanceTemporal.getTemporal()
        retornoMatriz = []
        retornoMatriz.append(temporalAsignado + ' = \'' + traduccionSelect(self) + '\'')
        retornoMatriz.append('display[p] = ' + temporalAsignado)
        retornoMatriz.append('p = p + 1')
        return retornoMatriz

    def getText(self):
        return traduccionSelect(self)