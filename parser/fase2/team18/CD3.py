from storageManager import jsonMode as EDD
import json


#variables
listaSalida=[]
listaMemoria=[]
memoriTrue=0
contT=-1;

#Funciones para generear codigo de 3 direcciones
def numT():
    global contT
    contT+=1
    return contT

def agregarInstr(datoMemoria,instruccion):
    #agregar a la lista de parametros
    global listaMemoria
    listaMemoria.append(datoMemoria)
    #agregar a la lista de salida
    global listaSalida
    if(instruccion!=''):
        listaSalida.append(instruccion)

def PCreateDatabase(nombreBase,result):
    txt="\t#Create DataBase\n"
    txt+="\tt"+str(numT())+"='"+nombreBase+"'\n"
    varT="t"+str(numT())
    txt+="\t"+varT+"=CD3.EReplace()\n"
    txt+="\tif("+varT+"):\n"
    txt+="\t\tgoto .dropDB"+str(contT)+"\n"
    txt+="\t\tlabel.dropDB"+str(contT)+"\n"
    txt+="\t\tCD3.EDropDatabase()"
    
    replac=False
    
    if(result==1):
        #'eliminar, luego crear'
        replac=True
        agregarInstr(replac,txt)#agregar replace
        agregarInstr(nombreBase,'')#agregar Drop
    else:
        agregarInstr(replac,txt)#agregar replace
    #crear tabla
    txt3="\tCD3.ECreateDatabase()\n"
    agregarInstr(nombreBase,txt3)#agregar create

def PDropDatabase(nombreBase):
    txt="\t#Drop DataBase\n"
    txt+="\tt"+str(numT())+"='"+nombreBase+"'\n"
    txt+="\tCD3.EDropDatabase()\n"
    agregarInstr(nombreBase,txt)

def PSelectFunciones(alias,resultado):
    agregarInstr("",'print("Alias:  '+ alias + '  Resultado: "+ str('+ str(resultado) +'))')
       
def PUseDatabase(nombreBase):
    txt="\t#usar base\n"
    txt+="\tt"+str(numT())+"='"+nombreBase+"'\n"
    txt+="\tCD3.EUseDatabase()\n"
    agregarInstr(nombreBase,txt)

def PCreateType(nombreBase,nombreTabla,cantidadcol,valores):
    '''
    var=nombreTipo #cargar en memoria el nombre
    t3=CD3.EcrearTipo()
    if(t3) goto Error1:
    insertD1:
        var=[1,1,1,1,1] #cargar en memoria la lista
        CD3.EInsert()
    '''
    txt="\t#Create Type\n"
    txt+="\tt"+str(numT())+"='"+nombreTabla+"'\n"
    var="t"+str(numT())
    txt+="\t"+var+"= CD3.ECreateTable()"+"\n"
    txt+="\tif("+var+"):"+"\n"
    txt+="\t\tgoto .Insertar"+str(contT)+"\n"
    txt+="\t\tlabel.Insertar"+str(contT)+"\n"
    var="t"+str(numT())
    txt+="\t\t"+var+"="+str(valores)+""
    
    crearT=[nombreBase,nombreTabla,cantidadcol]
    agregarInstr(crearT,txt)
    txt="\t\t"+"CD3.EInsert()"+"\n"
    inserT=[nombreBase,nombreTabla,valores]
    agregarInstr(inserT,txt)

def PCreateTable(nombreBase,nombreTabla,cantidadcol,llaves):
    txt="\t#Create Table\n"
    txt+="\tt"+str(numT())+"='"+nombreTabla+"'\n"
    var="t"+str(numT())
    txt+="\t"+var+"=CD3.ECreateTable()"+"\n"
    txt+="\tif("+var+"):"+"\n"
    txt+="\t\tgoto .insPK"+str(contT)+"\n"
    txt+="\t\tlabel.insPK"+str(contT)+"\n"
    var="t"+str(numT())
    txt+="\t\t"+var+"="+str(llaves)+""

    crearT=[nombreBase,nombreTabla,cantidadcol]
    agregarInstr(crearT,txt)
    txt="\t\t"+"CD3.EAddPK()"+"\n"
    pkT=[nombreBase,nombreTabla,llaves]
    agregarInstr(pkT,txt)

def PInsert(nombreBase,nombreTabla,valores):
    Data_insert=[nombreBase,nombreTabla,valores]
    txt="\t#Insert\n"
    txt+="\tt"+str(numT())+"='"+nombreTabla+"'\n"
    varT="t"+str(numT())
    txt+="\t"+varT+"=CD3.EExistT()\n"
    txt+="\tif("+varT+"):\n"
    txt+="\t\tgoto .insert"+str(contT)+"\n"
    txt+="\t\tlabel.insert"+str(contT)+"\n"
    agregarInstr(True,'')#agregar que si existe
    varT="t"+str(numT())
    txt+="\t\t"+varT+"="+str(valores)+"\n"
    txt+="\t\tCD3.EInsert()\n"

    agregarInstr(Data_insert,txt)

#escribir archivo
def CrearArchivo():
    #crear salida
    nombre="SalidaCD3.py"
    f=open(nombre,"w")
    f.write("#importar modulos")
    f.write("\n")
    f.write("import CD3  as CD3  #modulo codigo 3 direcciones")
    f.write("\n")
    f.write("from goto import with_goto  #modulo goto")
    f.write("\n")
    f.write("\n")
    f.write("@with_goto  # Decorador necesario \ndef main():\n")
    f.write("#Codigo Resultante")
    f.write("\n")
    for x in listaSalida:
        f.write(x)
        f.write("\n")
    
    f.write("main()")
    f.close()

    #crear memoria
    with open('memoria.json','w') as file:
        json.dump(listaMemoria,file,indent=4)
    
    #reiniciar lista temp
    listaMemoria.clear()
    listaSalida.clear()
    memoriTrue=0
    contT=-1




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
        listaMemoria.pop(0)
        return True
    return False

def EAddPK():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        crear_tabla=listaMemoria[0]
        if(len(crear_tabla[2])>0):
            EDD.alterAddPK(crear_tabla[0],crear_tabla[1],crear_tabla[2])
            print("\tllave primaria:",crear_tabla[2])
        listaMemoria.pop(0)

def EReplace():
    cargarMemoria()
    #llamar la funcion de EDD
    result=False
    if(len(listaMemoria)>0):
        result=listaMemoria[0]
        listaMemoria.pop(0)
    return result

def EExistT():
    cargarMemoria()
    #llamar la funcion de EDD
    result=False
    if(len(listaMemoria)>0):
        result=listaMemoria[0]
        listaMemoria.pop(0)
    return result

def ESelectFuncion():
    print("Select funcion")
        

def EInsert():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        Data_insert=listaMemoria[0]
        EDD.insert(Data_insert[0],Data_insert[1],Data_insert[2]) 
        print("Insert en tabla ",Data_insert[1]," \n\tvalores ",Data_insert[2])
        listaMemoria.pop(0)
