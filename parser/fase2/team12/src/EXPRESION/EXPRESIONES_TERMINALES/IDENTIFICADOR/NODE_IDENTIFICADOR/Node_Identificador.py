import sys, os

nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..')) + '\\EXPRESION\\')
sys.path.append(nodo_dir)

nodo_ast = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..','..')) + '\\ENTORNO\\')
sys.path.append(nodo_ast)

from Expresion import Expresion
from Tipo import Data_Type
from Tipo_Expresion import Type_Expresion


class Identificator_Expresion(Expresion):
    
    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)
        self.tipo = Data_Type.non
    
    def execute(self, eviroment):

        #print("Nodo identificador")
        nombreId = self.valor
        nombreId = nombreId.upper()

        
        if eviroment == None :

            self.tipo = Type_Expresion(Data_Type.error)
            self.valorExpresion = None
            return self.valorExpresion

        else :                

            # Verificar que la columna venga solamente 1 vez
            contadorColumn = 0

            # Variables para almacenar el tipo de dato y su valor
            valorColumn = None
            typeColumn = 7

            for tabla in eviroment:

                #print("Tabla: "+eviroment[tabla].nameTable)

                for col in eviroment[tabla].lista:

                    #print("\tColumna: "+eviroment[tabla].lista[col].nameColumn)
                    #print("\tColumna Buscar: "+nombreId)

                    if nombreId == eviroment[tabla].lista[col].nameColumn :
                        contadorColumn = contadorColumn + 1
                        typeColumn = eviroment[tabla].lista[col].typeColumn
                        valorColumn = eviroment[tabla].lista[col].valueColumn

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
                
                else :

                    self.tipo = Type_Expresion(Data_Type.boolean)
                    self.valorExpresion = valorColumn
                    return self.valorExpresion
            
            else :
                
                print("Existen varias Columnas con el mismo identificador")
                self.tipo = Type_Expresion(Data_Type.error)
                self.valorExpresion = None 
                return self.valorExpresion
            
    def compile(self, eviroment):
        print("text")

    def getText(self):
        return self.valor