import numpy as np
from  storageManager import jsonMode as condb #cambio de conexion
from ReporteTS import *
import funcionesTS as fun


tabla_result = []


class DevolverTabla():

    def __init__(self, tabla):
        self.tabla = tabla

    def devolverCampos(self ,base, tabla):
        campos = []
        #print("Entrando a devolver posicion ", tsgen)

        for i in tsgen:
            if str(tsgen[i]['ambito']) == str(base) or str(tsgen[i]['declarada_en']) == str(base):
                if str(tsgen[i]['declarada_en']) == str(tabla):
                    #print("Encontrado campo " + str(tsgen[i]['nombre']))
                    campos.append(str(tsgen[i]['nombre']))
        return campos


    def devolverPosicionCampos(self, base, tabla, campo):
        campos = self.devolverCampos(base, tabla)
        #print(len(campos))
        validacion = 0

        contador = 0
        for i in campos:
            if str(i) == str(campo):
                return contador
            else:
                contador += 1
                validacion = 1

        if validacion == 1:
            return -1


    def unaTabla(self, nombreBase, nombreTabla, where, listaCampos):
        tabla_result = []
        tabla_result.append(self.devolverCampos(nombreBase, nombreTabla))

        resultados = condb.extractTable(nombreBase,nombreTabla) 
        arr = np.array(resultados)

        if where == -1: # no viene where, guarda todo lo que viene
            for i in range(0, len(resultados), 1):
                tabla_result.append(arr[i])
        
        elif listaCampos == -1:
            for i in range(0, len(resultados), 1):
                tabla_result.append(arr[i])

        else: # si viene where
            for i in range(0, len(resultados), 1):

                nuevoWhere = where
                for j in listaCampos:
                    print(len(listaCampos) , "tam de la lista de campos")

                    if nuevoWhere.__contains__(str(j)):
                        posicion = self.devolverPosicionCampos(nombreBase, nombreTabla, j)
                        print("entre al if con " , j, "  posicion " , posicion)
                        nuevoWhere = nuevoWhere.replace(str(j), "\"" + arr[i][posicion] + "\"")
                        print("reemplazando " , j , " con " , "\"" + arr[i][posicion] + "\"", "-- resultado " , nuevoWhere)

                #val = where.replace("col0", "\"" + arr[i][0] + "\"").replace("col2", "\"" + arr[i][2]+ "\"")

                print(nuevoWhere, "<----")

                respuesta = eval(nuevoWhere)

                if(respuesta == True):
                    tabla_result.append(arr[i])
        
        return tabla_result



    def ejecutarNumpy(self):    
        self.tabla.agregaraTS('0', 'nuevadb5', 'base', 'global', '', '')
        self.tabla.agregaraTS('1', 'tabla', 'tabla', 'nuevadb5', '', '')
        self.tabla.agregaraTS('2', 'col0', 'varchar(10)', 'tabla', 'nuevadb5', '')
        self.tabla.agregaraTS('3', 'col1', 'char(2)', 'tabla', 'nuevadb5', '')
        self.tabla.agregaraTS('4', 'col2', 'text',  'tabla', 'nuevadb5', '')

        #print("Tabla resultante: " , self.unaTabla("nuevadb5","tabla", "col0 < \"3\" and col2 == \"direccion1\"", ["col0","col2"])) 
        #return self.unaTabla("nuevadb5","tabla", "col0 < \"3\" and col2 == \"direccion1\"", ["col0","col2"])
        return self.unaTabla("nuevadb5","tabla", -1, -1)


#ts = fun.objTabla()
#ob = DevolverTabla(ts)
#ob.ejecutarNumpy()