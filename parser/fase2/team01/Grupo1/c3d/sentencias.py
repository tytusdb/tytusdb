#import sys
#sys.path.append('../Grupo1/Librerias/storageManager')


from enum import Enum
import math
import random
import hashlib 
#from jsonMode import *
from storageManager import jsonMode as manager
           
  
def createDB(database: str) :
        
        
    #*********************** CREATE DB ****************************
    resultado = manager.createDatabase(database)
    if resultado==0:
        print('Base de datos ' + database + ' creada correctamente')
    elif resultado==2:
        print('Error al crear la base de datos ' + database + '. El nombre ya existe')
    elif resultado==1:
        print('Ha ocurrido un error al crear la base de datos ' + database + '.')
    else:
        print('Error desconocido')


# READ and show databases by constructing a list
def showDB(database: str) :
    
    resultado = manager.showDatabases()
    print(resultado)

# CREATE a table checking their existence
def createTbl(database: str, table: str, numberColumns: int):
    
    resultado = manager.createTable(database, table, numberColumns)
    if resultado == 1:
        print('Error(42P16): invalid_table_definition.')
    elif resultado == 2:
        print('Error(???): No existe la base de datos.')
    elif resultado == 3:
        print('Error(42P07): duplicate_table.')
    elif resultado == 0:
        print('Tabla ' + table + ' creada correctamente')