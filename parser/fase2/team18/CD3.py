from storageManager import jsonMode as EDD
import json


#variables
listaSalida=[]
listaMemoria=[]
memoriTrue=0

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

def PUseDatabase(nombreBase):
    agregarInstr(nombreBase,"CD3.EUseDatabase()")

def PCreateType(nombreBase,nombreTabla,cantidadcol,valores):
    crear_type=[nombreBase,nombreTabla,cantidadcol,valores]
    agregarInstr(crear_type,"CD3.ECreateType()")

def PCreateTable(nombreBase,nombreTabla,cantidadcol,llaves):
    crear_Tabla=[nombreBase,nombreTabla,cantidadcol,llaves]
    agregarInstr(crear_Tabla,"CD3.ECreateTable()")

def PInsert(nombreBase,nombreTabla,valores):
    Data_insert=[nombreBase,nombreTabla,valores]
    agregarInstr(Data_insert,"CD3.EInsert()")

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
    listaSalida.clear()
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
       
def EUseDatabase():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        print("selecionada base de datos:",listaMemoria[0])
        listaMemoria.pop(0)

def ECreateType():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        crear_type=listaMemoria[0]
        EDD.createTable(crear_type[0],crear_type[1],crear_type[2])
        EDD.insert(crear_type[0],crear_type[1],crear_type[3]) 
        print("creado type ",crear_type[1]," con valores ",crear_type[3])
        listaMemoria.pop(0)

def ECreateTable():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        crear_tabla=listaMemoria[0]
        EDD.createTable(crear_tabla[0],crear_tabla[1],crear_tabla[2])
        print("creando Tabla ",crear_tabla[1])
        if(len(crear_tabla[3])>0):
            EDD.alterAddPK(crear_tabla[0],crear_tabla[1],crear_tabla[3])
            print("\tllave primaria:",crear_tabla[3])

        listaMemoria.pop(0)

def EInsert():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        Data_insert=listaMemoria[0]
        EDD.insert(Data_insert[0],Data_insert[1],Data_insert[2]) 
        print("Insert en tabla ",Data_insert[1]," \n\tvalores ",Data_insert[2])
        listaMemoria.pop(0)