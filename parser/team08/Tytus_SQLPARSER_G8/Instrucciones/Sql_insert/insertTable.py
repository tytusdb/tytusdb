from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Expresiones.Primitivo import Primitivo
from storageManager.jsonMode import *

class insertTable(Instruccion):
    def __init__(self, id, tipo, lcol, lexpre, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = id
        self.lcol = lcol
        self.lexpre = lexpre

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("INSERTAR EN TABLA")
        print("------COLUMNAS------")
        listaN = []
        orden = 0
        lista = []
        if(self.lcol != None):
            for x in range(0,len(self.lcol)):
                val = arbol.devolverOrdenDeColumna(self.valor,self.lcol[x])
                listaN.append(val)
                if(val != x):
                    orden = 1
            if orden == 1:
                listaOrd = []
                if(self.lexpre != None):
                    for x in range(0,len(self.lexpre)):
                        orden = listaN[x]
                        obj = [orden,self.lexpre[x]]
                        print(obj)
                        listaOrd.append(obj)
                #aqui se van a ordenar
                ordenados = sorted(listaOrd)
                print(ordenados)
                for x in range(0,len(ordenados)):
                    val = ordenados[x]
                    for y in range(0,len(val)):
                        if(y == 1):
                            valor = val[y]
                            #aqui el res me tira error :D
                            res = valor.ejecutar(tabla,arbol)
                            lista.append(res)
                            print("-->" + str(res))
                            
        res = insert(arbol.getBaseDatos(),self.valor,lista)
        if(res == 0):
            arbol.consola.append(f"el registro se inserto correctamente.")
        else:
            if(self.lexpre != None):
                print("------VALORES------")
                #DEVOLVER TABLA
                itabla=arbol.devolviendoTablaDeBase(self.valor)
                #print()
                for x in range(0,len(itabla.lista_de_campos)):
                    #volver tipo primitivo
                    if x< len(self.lexpre) and (type(self.lexpre[x]) is Primitivo):
                        valor = self.lexpre[x].ejecutar(tabla,arbol)
                        lista.append(valor)
                        #print(valor)

                    else:
                        lista.append(None)
                        #print(None)    
                
            print("esta es la insercion de lista, ya inserto estaticamente")
            res = insert(arbol.getBaseDatos(),self.valor,lista)
            if(res == 0):
                arbol.consola.append(f"el registro se inserto correctamente.")
'''
instruccion = insertTable("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''