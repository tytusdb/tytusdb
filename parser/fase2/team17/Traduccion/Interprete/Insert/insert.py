from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Mode import MODE


#############################
# Patrón intérprete: INSERT #
#############################

class Insert(NodoArbol):

    def __init__(self, tablename, listcolumn, listvalues , line, column ):
        super().__init__(line, column)
        self.tableName: str = tablename
        self.listColumn: list = listcolumn
        self.listValues: list = listvalues
        self.arbol:Arbol

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):

        mode = entorno.mode

        if entorno.mode == MODE.STRING:
            self.executeString(entorno,arbol)

        elif entorno.mode == MODE.C3D:
            self.executeC3d(entorno,arbol)

    # ================================================================================================


    def executeC3d(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass
    # ================================================================================================



    def executeString(self, entorno: Tabla_de_simbolos, arbol: Arbol):

        listvalues = self.getValues(self.listValues,entorno,arbol)

        if not self.listColumn:
            # insert : INSERT INTO ID VALUES PARIZQ exp_list PARDER
            result = 'insert into '+self.tableName+' values ('
            result+= self.listToStr(listvalues)
            result+=');'

        else:
            # insert : INSERT INTO ID PARIZQ idlist PARDER VALUES PARIZQ exp_list PARDER
            result = 'insert into '+self.tableName+' ('
            result+= self.listToStr(self.listColumn)
            result+=') values ('
            result+= self.listToStr(listvalues)
            result+=');'
    # ================================================================================================


    def listToStr(self,array:list) -> str:
        result =''
        for item in array: result-=str(item)
        return result
    # ================================================================================================


    def getValues(self, listValues, entorno, arbol) -> list:
        result: list = []
        for v in listValues:
            try:
                value = v.execute(entorno, arbol).data
                result.append(value)
            except:
                pass
        return result
    # ================================================================================================


