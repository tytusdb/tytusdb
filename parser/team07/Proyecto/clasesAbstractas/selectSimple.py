import jsonMode
from prettytable import PrettyTable
from .instruccionAbstracta import InstruccionAbstracta

class selectSimple(InstruccionAbstracta):

    '''Clase que representa un select simple el cual lleva como atributos'''

    def __init__(self, selectColumnas, selectTablas, selectCondiciones, Distinct):
        self.selectColumnas = selectColumnas
        self.selectTablas = selectTablas
        self.selectCondiciones = selectCondiciones
        self.Distinct = Distinct


    def ejecutar(self, tabalSimbolos, listaErrores):  

        if self.selectTablas is None: #Select sin tablas en el FROM y se asume que viene una funcion matematica
            
            
            for elemento in self.selectColumnas.hijos:
                Res = elemento.hijos[0].ejecutar(tabalSimbolos, listaErrores)
                print(Res.valorRetorno)   
            

        else: #Se tinene tablas e el FROM

            ListaTablasFrom = {"Tabla":[],"ID": []}
            ListaSubquerysFrom = {"Subquery": [], "ID": []}

            '''
            Paso1:
                Se extraen los nombres de las tablas correspondientes al FROM con sus ID si es que los tienen
            '''
            
            for Tabla in self.selectTablas.hijos: #Recorrido de todos los elementos de FROM
                
                if str.lower(Tabla.hijos[0].nombreNodo) == "dec_id_from": #Es una declaracion simple de una tabla
                    
                    if len(Tabla.hijos[0].hijos) == 1:
                        ListaTablasFrom["Tabla"].append(Tabla.hijos[0].hijos[0].valor)
                        ListaTablasFrom["ID"].append(Tabla.hijos[0].hijos[0].valor)
                    elif len(Tabla.hijos[0].hijos) == 2:
                        ListaTablasFrom["Tabla"].append(Tabla.hijos[0].hijos[0].valor)
                        ListaTablasFrom["ID"].append(Tabla.hijos[0].hijos[1].valor)

                else: #Es un subquery
                    if len(Tabla.hijos) == 1:
                        ListaSubquerysFrom["Subquery"].append(Tabla.hijos[0])
                        ListaSubquerysFrom["ID"].append(None)
                    if len(Tabla.hijos) == 2:
                        ListaSubquerysFrom["Subquery"].append(Tabla.hijos[0])
                        ListaSubquerysFrom["ID"].append(Tabla.hijos[0].valor)

            '''
            Paso2:
                Se obtine de la base de datos la informacion de las tablas
            '''
            DatosTablas = {"ID": [], "Datos": []}

            for tabla in ListaTablasFrom["Tabla"]:
                DatosTablas["ID"].append(tabla)
                DatosTablas["Datos"].append(jsonMode.extractTable("BD", tabla))


            '''
            Paso3:
                Se revisan que campos se piden
            '''
            Tablas = []
            if self.selectColumnas.valor == "*": #Se buscan todas las columnas de las tablas
                
                for T in DatosTablas["Datos"]:
                    TablaPrint = PrettyTable()
                    TablaPrint.add_rows(T)
                    Tablas.append(TablaPrint)
                
                for T in Tablas:
                    print(T)

            else: #Se revisan las columnas que se piden
                print("Se piden campos especificos")

        pass 

