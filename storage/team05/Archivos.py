#Archivo para manejar la carga de archivos 
import csv #Necesaria para importar
from NameStructure import ne as d
from NameStructure import ht as h

class archivoCsv:
    def __init__(self):
        super().__init__()
    

    def leerCSV(self, file: str, database: str, table: str):
        listaValores = []
        try: 
            
            if d.searchDatabase(database) == True:
                if d.buscarTablaDatabase(database,table) == True:
                    with open(file) as f:
                        reader = csv.reader(f, delimiter=",")

                        valorError = True
                        numeroColumnas = int(d.numeroDeColumnas(database,table))
                        for x in reader: #[2,3,4,5]
                            if numeroColumnas == len(x): #Comprobamos que el numero de columnas sea igual al de csc
                                #aqui se ingresa la funcion insertar de la tabla hash 
                                valorRetorno = h.insert(database, table, x)
                                listaValores.append(valorRetorno)
                                
                            else:
                                valorError = False
                    
                    #Si hay error en la lectura la variable valorError devuelve True
                    if valorError == True:
                        return listaValores
                    else:
                        listaValores = []
                        return listaValores
                                
            else:
                return listaValores
        except:
            return listaValores
    

archivo = archivoCsv()
