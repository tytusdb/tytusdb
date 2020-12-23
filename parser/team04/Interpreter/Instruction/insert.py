
from Interpreter.Instruction.instruction import Instruction
from Statics.console import Console
from Scripts.jsonMode import *



class Insertinto(Instruction):
    def __init__(self, tabla, registros):
        self.tabla = tabla
        self.registros = registros
 
    def execute(self, env):
        print("Se ejecutó la instrucción 'INSERT'")
 
        values = []
        for exp in self.registros:
            values.append(exp.getValue(env))
      
       
        resultado = insert(env.currentDB, self.tabla.getValue(env), values )
        Console.add(resultado)
      

#Insert con especificación de columnas
class Insertinto2(Instruction):
    def __init__(self, tabla, columnas, registros):
        self.tabla = tabla
        self.columnas = columnas
        self.registros = registros
 
    def execute(self, env):
        print("Se ejecutó la instrucción 'INSERT2'")
        base =  env.dbs[env.currentDB]
        tablad = base[self.tabla.getValue(env)]
        print(tablad)
        
         #Lista 'tablac' de prueba, remplazarla por las columnas de la tabla
        tablac= [[{'idusuario':{'id':'idusuario','type':'integer','not_null':True,'pk':True}},
                    {'nombre':{'id':'nombre','type':'string','not_null':True,'pk':True}},
                    {'nombre2':{'id':'nombre','type':'string','not_null':True,'pk':True}},
                    {'nombre3':{'id':'nombre','type':'string','not_null':True,'pk':True}},
                    {'nombre4':{'id':'nombre','type':'string','not_null':True,'pk':True}},
                    {'nombre5':{'id':'nombre','type':'string','not_null':True,'pk':True}},
                    {'direccion':{'id':'direccion','type':'string','not_null':True,'pk':False}}],
                    [['2','Brayan','guate'],['1','Glendy','guate'],['3','otro','guate']]]

        listinsert = []                          #Listado final que se enviará a insertar
 
        listcolums = []                           #Listado de todas las columnas de la tabla
        for dicc1 in tablac[0]:                   #accedemos a la lista  
            for atributo,dicc2 in dicc1.items():  #acedemos a cada clave del diccionario: idusuario, nombre, dirección
                listcolums.append(atributo)    
                listinsert.append(" ")    
               
              
        values = []                               #Lista de Valores a insertar 
        for exp in self.registros:
            values.append(exp.getValue(env))      #Se analiza cada expresion y se guarda en la lista

        columns = []                              #Lista de columnas en donde se van a insertar datos
        for exp in self.columnas:
            columns.append(exp.getValue(env))     #Se analiza cada expresion y se guarda en la lista

        posiciones = []                           #Lista de posiciones
        for col in columns:                       #Devuelve la posición de columns en listacolumns
            indice = listcolums.index(col)
            posiciones.append(indice)
        
        cont = 0                                  #Cambia datos de listinsert
        for pos in posiciones:  
            print (pos)                             
            listinsert[pos] = values[cont]
            cont += 1
        print(listinsert)
        
        resultado = insert(env.currentDB, self.tabla.getValue(env), listinsert ) 
        Console.add(resultado)