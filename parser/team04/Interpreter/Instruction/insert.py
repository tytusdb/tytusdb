
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
        tablac = base[self.tabla.getValue(env)]
        print(tablac)


        listinsert = []                           #Listado final que se enviará a insertar
 
        listcolums = []                           #Listado de todas las columnas de la tabla
        for col in tablac.keys():                 #Se recorre el diccionario y se almacena cada clave  
            listcolums.append(col)    
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