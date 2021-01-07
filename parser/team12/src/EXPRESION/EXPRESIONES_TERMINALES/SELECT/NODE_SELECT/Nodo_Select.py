import sys, os

nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..')) + '\\EXPRESION\\')
sys.path.append(nodo_dir)

nodo_ast = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..','..')) + '\\ENTORNO\\')
sys.path.append(nodo_ast)

nodo_select = (os.path.abspath(os.path.dirname(__file__)))
sys.path.append(nodo_select)

nodo_function_select = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..','..')) + '\\DML\\Select\\')
sys.path.append(nodo_function_select)

from Expresion import Expresion
from Tipo import Data_Type
from Tipo_Expresion import Type_Expresion
from Response_Exp import Response
from Select import Select

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
            for exp in lista_Exp.hijos :

                value = exp.execute(None)

                if exp.tipo.data_type == Data_Type.error :
                    print("Error: ")

                else :

                    if exp.nombreNodo == 'ALIAS':
                        dataSelect.encabezados.append(exp.alias)
                    else :
                        dataSelect.encabezados.append('?column?')
                    
                    l.append(value)
            dataSelect.data.append(l)    
            return dataSelect
                
        else :
            #SENTENCIA_SELECT_DISTINCT
            functionSelect = Select()
            result = functionSelect.execute(nodoSelect)
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
            return responseSelect

