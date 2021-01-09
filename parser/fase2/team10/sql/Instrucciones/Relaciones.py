from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
import numpy as np

class Relaciones(Instruccion):
    def __init__(self, query, opcion, query2,strGram ,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.query = query
        self.query2 = query2
        self.opcion = opcion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("entro a relaciones")
        arbol.setRelaciones(True)

        tablaA = []
        tablaB = []
        if(self.query != None):
            tablaA = self.query.ejecutar(tabla,arbol)
        if(self.query2 != None):
            tablaB = self.query2.ejecutar(tabla,arbol)
        
        print(tablaA.data)
        print(tablaB.data)

        #aqui se  unen las 2 tablas

        if(self.opcion == "UNION"):
            #union remove  duplicates
            res = np.concatenate((tablaA.data, tablaB.data), axis=0)
            unique_rows = np.unique(res, axis=0)
            print(unique_rows)
            columnas = self.devolverColumnas(unique_rows)
            arbol.getMensajeTabla(tablaA.lista_de_campos,columnas)
            #aqui falta devolver la tabla hecha :D
            return unique_rows
        elif(self.opcion == "UNIONALL"):
            # esto es la union
            res = np.concatenate((tablaA, tablaB), axis=0)
            columnas = self.devolverColumnas(res)
            arbol.getMensajeTabla(tablaA.lista_de_campos,columnas)
            #aqui falta devolver la tabla hecha :D
            return res 
        elif(self.opcion == "INTERSECT"):
            #El número de columnas y su orden en las cláusulas SELECT deben ser iguales. 
            #Los tipos de datos de las columnas deben ser compatibles.
            res = self.compararIntersect(tablaA,tablaB)
            #columnas = self.devolverColumnas(res)
            print(res)
            #print(columnas)
            arbol.getMensajeTabla(tablaA.lista_de_campos,res)
            return res 
        elif(self.opcion == "INTERSECTALL"):
            res = self.compararIntersect(tablaA,tablaB)
            columnas = self.devolverColumnas(res)
            print(res)
            arbol.getMensajeTabla(tablaA.lista_de_campos,res)
            return res 
        elif(self.opcion == "EXCEPT"):
            res = self.compararExcept(tablaA,tablaB)
            columnas = self.devolverColumnas(res)
            arbol.getMensajeTabla(tablaA.lista_de_campos,columnas)
            return res 
        elif(self.opcion == "EXCEPTALL"):
            res = self.compararExceptAll(tablaA,tablaB)
            columnas = self.devolverColumnas(res)
            arbol.getMensajeTabla(tablaA.lista_de_campos,columnas)
            return res 
        
        arbol.setRelaciones(False)

    def compararIntersect(self, tablaA, tablaB):
        tabla1 = tablaB
        tabla2 = tablaA
        if(len(tablaA.data)>=len(tablaB.data)):
            tabla1 = tablaA.data
            tabla2 = tablaB.data
        
        res = []
        nodo = []
        for j in range(0,len(tabla1)):
            for k in range(0,len(tabla2)): 
                if(tabla1[j] == tabla2[k]):
                    nodo.append(tabla1[j])
            res.append(nodo)
        
        return res[0]

    def devolverColumnas(self, tabla):
        res = []
        for x in range(0, len(tabla)):
            print(tabla[x])
            tabla2 = tabla[x]
            nodo = []
            for y in range(0, len(tabla2)):
                nodo.append(tabla2[y])
            res.append(nodo)

        return res

    def compararExceptAll(self, tablaA,tablaB):
        tabla1 = tablaB
        tabla2 = tablaA
        if(len(tablaA.data)>=len(tablaB.data)):
            tabla1 = tablaA.data
            tabla2 = tablaB.data
                        
        #EXCEPT ALL
        res = []
        nodo = []
        for j in range(0,len(tabla1)):
            encontrado = 0
            for k in range(0,len(tabla2)): 
                if(tabla1[j] == tabla2[k]):
                    encontrado = 1

            if(encontrado == 0):
                nodo.append(tabla1[j])
        res.append(nodo)

        return res[0]



    def compararExcept(self, tablaA,tablaB):
        tabla1 = tablaB
        tabla2 = tablaA
        if(len(tablaA.data)>=len(tablaB.data)):
            tabla1 = tablaA.data
            tabla2 = tablaB.data
                        
        #EXCEPT ALL
        res = []
        nodo = []
        for j in range(0,len(tabla1)):
            encontrado = 0
            for k in range(0,len(tabla2)): 
                if(tabla1[j] == tabla2[k]):
                    encontrado = 1

            if(encontrado == 0):
                nodo.append(tabla1[j])
        res.append(nodo)
        tabla = res[0]
        #EXCEPT
        tabla = np.unique(res[0], axis=0)
        resul = []
        for fila in tabla:
            nodo2 = []
            for elemento in fila:
                nodo2.append(elemento)
            resul.append(nodo2)
        return resul


'''
    a = np.array([[1, 4, 3], [2, 3, 6]])
    b = np.array([[2, 4, 6], [3, 6, 9]])        
'''