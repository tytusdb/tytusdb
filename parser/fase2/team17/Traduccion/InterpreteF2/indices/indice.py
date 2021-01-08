from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Reporteria.ReporteTS_Indice import ReportIndice
from InterpreteF2.Reporteria.ErroresSemanticos import ErroresSemanticos
from typing import List



class Option:
    def __init__(self,option:str):
        self.option:str = option

class Index_Param:
    def __init__(self,column:str, options:List[Option]):
        self.column:str =  column
        self.options:List[Option] = options
        pass


class Id_Indice:
    def __init__(self,indexname:str,tablename:str):
        self.indexname:str = indexname
        self.tablename:str = tablename
        pass

class indice(NodoArbol):

    def __init__(self, idx:Id_Indice,index_params:List[Index_Param],tipo:str ,linea:int, columna:int):
        super().__init__(linea, columna)
        self.linea = linea
        self.columna = columna

        self.identificador = idx.indexname

        if idx.indexname =='':
            self.identificador = idx.tablename+'_idx'

        self.tablename:str = idx.tablename
        self.index_params:List[Index_Param] = index_params
        self.tipo = tipo


    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):


        for temp in arbol.ReporteTS_Indice:
            if temp.nombre == self.identificador:
                error:ErroresSemanticos = ErroresSemanticos('Ya existe el index \''+temp.nombre+'\'', self.linea, self.columna, 'Indice')
                arbol.ErroresSemanticos.append(error)
                return

        columnas:List[str]= []
        for i in self.index_params:
            columnas.append(i.column)


        consideraciones= ''
        options:List[Option] = self.index_params[0].options
        for i in options:
            consideraciones+=i.option+' '


        nodo = ReportIndice(self.identificador,self.identificador,self.tipo,columnas,consideraciones, self.columna, self.columna)

        arbol.ReporteTS_Indice.append(nodo)
        return

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass



