import sys, os.path

nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..')) + '\\EXPRESION\\')
sys.path.append(nodo_dir)

nodo_ast = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..','..')) + '\\ENTORNO\\')
sys.path.append(nodo_ast)

nodo_select = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..','..')) + '\\DML\\Select\\')
sys.path.append(nodo_select)
print(nodo_select)

from Expresion import Expresion
from Tipo import Data_Type
from Tipo_Expresion import Type_Expresion
from Select import Info_Tabla
from Select import Info_Column

class Access_Expresion(Expresion):
    
    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)
        self.tipo = Data_Type.numeric

    def execute(self, environment):
        
        infoNameTable = self.hijos[0]
        infoIdTable = self.hijos[1]

        if environment == None :

            self.tipo = Type_Expresion(Data_Type.error)
            self.valorExpresion = None
            return self.valorExpresion
        
        else :

            nameAliasTable = infoNameTable.valor 
            nameAliasTable = nameAliasTable.upper()
            nameIdTable = infoIdTable.nombreNodo

            # Datos Columna
            contadorColumn = 0
            valorColumn = None
            typeColumn = 7

            if nameIdTable == 'Id Column' :

                nameIdTable = infoIdTable.valor
                nameIdTable = nameIdTable.upper()

                for tabla in environment :
                    #print(environment[tabla].nameTable)
                    #print(environment[tabla].aliasTabla)
                    if environment[tabla].aliasTabla == nameAliasTable :

                        #print("Se encontró la tabla :D")
                        #print(len(environment[tabla].lista))

                        for col in environment[tabla].lista :

                            #print("Columna Buscar: ",nameIdTable)
                            #print("Columna Actual: ",environment[tabla].lista[col].nameColumn)

                            if nameIdTable == environment[tabla].lista[col].nameColumn :

                                contadorColumn = contadorColumn + 1
                                typeColumn = environment[tabla].lista[col].typeColumn
                                valorColumn = environment[tabla].lista[col].valueColumn

                if contadorColumn == 0 :

                    print("No se encontró el identificador")
                    self.tipo = Type_Expresion(Data_Type.error)
                    self.valorExpresion = None 
                    return self.valorExpresion
                
                elif contadorColumn == 1 :

                    if typeColumn == 1 :

                        self.tipo = Type_Expresion(Data_Type.numeric)
                        self.valorExpresion = valorColumn
                        return self.valorExpresion
                
                    elif typeColumn == 2 :

                        self.tipo = Type_Expresion(Data_Type.character)
                        self.valorExpresion = valorColumn
                        return self.valorExpresion

                    elif typeColumn == 3 :

                        self.tipo = Type_Expresion(Data_Type.data_time)
                        self.valorExpresion = valorColumn
                        return self.valorExpresion
                
                    elif typeColumn == 4:

                        self.tipo = Type_Expresion(Data_Type.boolean)
                        self.valorExpresion = valorColumn
                        return self.valorExpresion
            
                    else :

                        self.tipo = Type_Expresion(Data_Type.error)
                        self.valorExpresion = None
                        return self.valorExpresion
            
            else :

                #print("Devolver todas las columnas")                
                tableResult = Info_Tabla('TABLERESULT')
                cantidadTablas = 0

                for tabla in environment :
                    #print(environment[tabla].nameTable)
                    #print(environment[tabla].aliasTabla)
                    if environment[tabla].aliasTabla == nameAliasTable :
                        #print("obtener datos de la tabla")
                        cantidadTablas = cantidadTablas + 1

                if cantidadTablas == 0 :

                    self.tipo = Type_Expresion(Data_Type.error)
                    self.valorExpresion = None
                    return self.valorExpresion

                elif cantidadTablas == 1 :

                    self.tipo = Type_Expresion(Data_Type.listaDatos)
                    self.valorExpresion = tableResult
                    return self.valorExpresion
                
                else : 

                    self.tipo = Type_Expresion(Data_Type.error)
                    self.valorExpresion = None
                    return self.valorExpresion

    def compile(self, enviroment):
        print("compile")
    
    def getText(self):

        infoNameTable = self.hijos[0]
        infoIdTable = self.hijos[1]

        if infoIdTable.nombreNodo == '*':
            textoAccess = infoNameTable.valor + '.*'
            return textoAccess
        else:
            textoAccess = infoNameTable.valor + '.'+infoIdTable.valor
            return textoAccess