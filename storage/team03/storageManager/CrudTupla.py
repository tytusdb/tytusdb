# Package:      Python
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Maynor Piló Tuy

import os
import time
from storageManager.ArbolBmas import ArbolBmas

#  CLASE PARA INSTANCIAR CADA UNA DE LAS FUNCIONES :
class CrudTuplas:

    def __init__(self, columas):
        self.pk = [] #Lista de llaves primarias que recibe de la tabla
        #self.fk = fk #Lista de llaves foraneas que recibe de la tabla
        self.auto = 0 #autoincremental cuando no existan llaves 
        self.tamCol = columas # contiene el tamaño de la columan que se definio en la tabla
        self.pkactuales= []   # lista para corroborar las llaves primarias
        self.tabla = ArbolBmas()
    ##########################################################################################################
    ############                                FUNCIONES CRUD  TUPLAS                            ############ 
    ##########################################################################################################
    
    # FUNCTION 1 - INSERT(LIST) - RECIBE COMO PARAMETRO UNA LISTA Y RETORNA INT 
    # 0 OPERACION EXITOSA
    # 4 LLAVE PRIMARIA DUPLICADA
    # 5 COLUMNAS FUERA DE LIMITES 
    def insert(self, tupla):
        #comprobar si el rango de columnas es la correcta
        try: 
            if len(tupla) != self.tamCol:
                #print("Error 5")
                return 5
            else:
                if len(self.pk) != 0:                                  # CUANDO EXISTEN LLAVES PRIMARIAS
                    pkey = ""
                    for k in self.pk:
                        pkey +=str(tupla[k])+"_"
                    
                    pkey=pkey[:-1]
                    if pkey in self.pkactuales:
                        #print("Error 4")
                        return 4
                    else: 
                        self.tabla.insertar(str(pkey),tupla)
                        self.pkactuales.append(pkey)
                        #print("Error 0")
                        return 0
                else:
                    self.tabla.insertar(str(self.auto), tupla)
                    self.pkactuales.append(str(self.auto))
                    self.auto += 1
                    return 0
        except ( IndexError):
            #print("Error 1")
            return 1
        
    # FUNCION 2 - LOAD CSV () RECIBE COMO PARAMETRO  FILE:STR RETORNA UNA LISTA CON LAS LINEAS EXITOSAS
    # 1 ERROR EN OPERACION
    # 4 LLAVE PRIMARIA DUPLICADA
    # COLUMNA FUERA DE LIMITES 
    def loadCSV(self, file):
        lista_retorno = []  # lista que contendra los valores de retorno
        try:
            
            archivo = open(file,'r',encoding='UTF-8')   #,encoding='UTF-8'
            # procesar el archivo
            data = archivo.readlines()
            archivo.close() 
            # se procede a recorrer las lineas de la lista y se insertan en los nodos del arbol
            # variable ret  es la encargada de recibir el numero de retorno de la funcion insertar
            for d in data:
                d=d.rstrip('\r\n\t')
                de=d.split(",")
                ret=self.insert(de)
                lista_retorno.append(ret)
                
            return  lista_retorno  # retorno de  la lista con los valores ingresados
        except IOError:
            #print ("Error de entrada")
            lista_retorno = []
            return []

    #FUNCION 3 - EXCTRACROW RECIBE COMO PARAMETRO UNA LISTA DE COLUMNAS  Y RETORNA  UNA LISTA   
    def extractRow(self, columns):
        pkey = ""
        for k in columns:
            pkey +=str(k)+"_"            
        pkey=pkey[:-1]
        resultado = self.tabla.Busqueda(pkey)
        return resultado
         
    #FUNCION 4 - UPDATE RECIBE COMO PARAMETRO UN DICCIONARIO DE LOS DATOS PARA ACTUALIZAR Y UNA COLUMNA CON LAS LLAVES PRIMARIAS
    # 0 OPREACION EXITOSA
    # 1 ERROR EN LA OPERACION 
    # 4 LLAVE PRIMARIA NO EXISTE
    def update(self, register, columns):
        pkey = ""
        for k in columns:
            pkey +=str(k)+"_"            
        pkey=pkey[:-1]
        resultado = self.tabla.Update(register, pkey)
        return resultado
        
    # FUNCION 5 - DELETE : RECIBE COMO PARAMETROS LA COLUMNA CON  LA LLAVE PRIMARIA
    # 0 FUNCION EXITOSA
    # 1 ERROR EN LA OPERACION
    # 4 LLAVE PRIMARIA NO EXISTE
    def delete(self,columns):
        try:
            pkey = ""
            for k in columns:
                pkey +=str(k)+"_"            
            pkey=pkey[:-1]
            resultado = self.tabla.eliminar(pkey)

            if resultado :
                return  0
            else:
                return 4
        except (TypeError):
            return 1

    # FUNCION 6 -  
    def truncateRaiz(self):
        self.tabla.truncateRoot()
    
