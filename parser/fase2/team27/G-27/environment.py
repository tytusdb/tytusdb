tempCount = 0 #Contador de temporales para su generación
labelCount = 0 #Contador de etiquetas para su generación
entorno = 0 #Contador de entorno
temporales ={} #Diccionario en el que se almacena [id:temporal] 
funciones = []#Diccionario para metadata de las funciones
arregloFunciones = [] #Arreglo en donde se guardaran las funciones traducidas.
arregloInstrucciones = []#Arreglo de instrucciones generales traducidas.

def buscarFuncion(id):
    for v in funciones:
        if v['id'] == id:
            return v

def getT():
    return '\t'*entorno

def aumentarEntorno():
    global entorno
    entorno += 1

def disminuirEntorno():
    global entorno
    entorno +=1