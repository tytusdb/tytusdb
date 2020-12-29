from storageManager import jsonMode as EDD
import json


#variables
listaSalida=[]
listaMemoria=[]
memoriTrue=0;

#Funciones para generear codigo de 3 direcciones
def agregarInstr(datoMemoria,instruccion):
    #agregar a la lista de parametros
    global listaMemoria
    listaMemoria.append(datoMemoria)
    #agregar a la lista de salida
    global listaSalida
    listaSalida.append(instruccion)

def PCreateDatabase(nombreBase,result):
    if(result==1):
        'eliminar, luego crear'
        PDropDatabase(nombreBase)
    #crear
    agregarInstr(nombreBase,"CD3.ECreateDatabase()")

def PDropDatabase(nombreBase):
    agregarInstr(nombreBase,"CD3.EDropDatabase()")


def PSelectFunciones(alias,resultado):
    agregarInstr("",'print("Alias:  '+ alias + '  Resultado: "+ str('+ str(resultado) +'))')
    
    
    

#escribir archivo
def CrearArchivo():
    #crear salida
    nombre="SalidaCD3.py"
    f=open(nombre,"w")
    f.write("#importar modulos")
    f.write("\n")
    f.write("import CD3  as CD3  #modulo codigo 3 direcciones")
    f.write("\n")
    f.write("\n")
    f.write("#Codigo Resultante")
    f.write("\n")
    for x in listaSalida:
        f.write(x)
        f.write("\n")
    f.close()

    #crear memoria
    with open('memoria.json','w') as file:
        json.dump(listaMemoria,file,indent=4)
    
    #reiniciar lista temp
    listaMemoria.clear()
    memoriTrue=0




#Funciones para ejecutar codigo de 3 direcciones
def cargarMemoria():
    #lectura memoria temp
    global memoriTrue
    global listaMemoria
    if(memoriTrue==0):
        print("----------Verificando Heap-------")
        memoriTrue=1
        with open('memoria.json') as file:
            data = json.load(file)
        listaMemoria=data

def ECreateDatabase():
    cargarMemoria()
    if(len(listaMemoria)>0):
        print("base de datos creada:",listaMemoria[0])
        EDD.createDatabase(listaMemoria[0])
        listaMemoria.pop(0)

def EDropDatabase():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        print("base de datos eliminada:",listaMemoria[0])
        EDD.dropDatabase(listaMemoria[0])
        listaMemoria.pop(0)
        

def ESelectFuncion():
    print("Select funcion")