from storageManager import jsonMode as EDD
import json
import copy

#variables
listaSalida=[]
listaMemoria=[]
listaoptimizaciones=[]
memoriTrue=0
contT=-1;
contOP=-1

#Funciones para generear codigo de 3 direcciones
def numT():
    global contT
    global contOP
    contT+=1
    contOP+=1
    return contOP

def reinicar_contOP():
    global contOP
    global listaoptimizaciones
    if contOP != -1 or contT != -1:
        regla = "Regla 1"
        msg = "Se reutilizo la t"+str(contOP)+" en lugar del t"+str(contT)  
        listaoptimizaciones.append([regla,msg])
    contOP=-1


def agregarInstr(datoMemoria,instruccion):
    #agregar a la lista de parametros
    global listaMemoria
    if datoMemoria != '':
        listaMemoria.append(datoMemoria)
    #agregar a la lista de salida
    global listaSalida
    if(instruccion!=''):
        listaSalida.append(instruccion)

def PCreateDatabase(nombreBase,result):
    reinicar_contOP()
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
    reinicar_contOP()
    txt="\t#Drop DataBase\n"
    txt+="\tt"+str(numT())+"='"+nombreBase+"'\n"
    txt+="\tCD3.EDropDatabase()\n"
    agregarInstr(nombreBase,txt)

def PSelectFunciones(alias,resultado):
    reinicar_contOP()
    txt="\t#Select funcion\n"
    varT="t"+str(numT())
    txt+="\t"+varT+"='"+alias+"'\n"
    varR="t"+str(numT())
    txt+="\t"+varR+"='"+str(resultado)+"'\n"
    

    txt+='\tprint("Cabecera:  " + '+ varT  + ' + " Resultado: "+ str('+ varR +'))\n'
    agregarInstr("",txt)
       
def PUseDatabase(nombreBase):
    reinicar_contOP()
    txt="\t#Use Database\n"
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
    reinicar_contOP()
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

def PCreateTable(nombreBase,nombreTabla,cantidadcol,llaves,nombresC):
    reinicar_contOP()
    txt="\t#Create Table\n"
    txt+="\tt"+str(numT())+"='"+nombreTabla+"'\n"
    txt+="\tt"+str(numT())+"="+str(nombresC)+"\n"
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
    reinicar_contOP()
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

def PUpdate(nombreBase,nombreTabla,indice,valor,nvalores):
    reinicar_contOP()
    update_data=[nombreBase,nombreTabla,indice,valor,nvalores]
    busqueda_tb=[nombreBase,nombreTabla]
    txt="\t#Update Registro\n"
    txt+="\tt"+str(numT())+"='"+nombreTabla+"'\n"
    var="t"+str(numT())
    txt+="\t"+var+"=CD3.EObtenerTabla()\n"
    txt+="\tif("+var+"):\n"
    txt+="\t\tgoto .tbencontrada"+str(contT)+"\n"
    txt+="\t\tlabel.tbencontrada"+str(contT)
    agregarInstr(busqueda_tb,txt)
    txt="\t\tt"+str(numT())+"='"+str(valor)+"'\n"
    txt+="\t\tCD3.EUpdate()\n"
    agregarInstr(update_data,txt)

def PDelete(nombreBase,nombreTabla,cols):
    reinicar_contOP()
    delete_data=[nombreBase,nombreTabla,cols]
    busqueda_tb=[nombreBase,nombreTabla]
    txt="\t#Delete Registro\n"
    txt+="\tt"+str(numT())+"='"+nombreTabla+"'\n"
    var="t"+str(numT())
    txt+="\t"+var+"=CD3.EObtenerTabla()\n"
    txt+="\tif("+var+"):\n"
    txt+="\t\tgoto .tbencontrada"+str(contT)+"\n"
    txt+="\t\tlabel.tbencontrada"+str(contT)
    agregarInstr(busqueda_tb,txt)
    txt="\t\tt"+str(numT())+"="+str(cols)+"\n"
    txt+="\t\tCD3.EDelete()\n"
    agregarInstr(delete_data,txt)

def PShowDatabases(dataBases):
    reinicar_contOP()
    txt="\t#Show Databases\n"
    txt+="\tt"+str(numT())+"="+str(dataBases)+"\n"
    txt+="\tCD3.EShowDatabases()\n"
    agregarInstr(dataBases,txt)

def PDropTable(nombreBase,nombreTabla):
    reinicar_contOP()
    drop_tb=[nombreBase,nombreTabla]
    txt="\t#Drop Table\n"
    txt+="\tt"+str(numT())+"='"+nombreTabla+"'\n"
    txt+="\tCD3.EDropTable()\n"
    agregarInstr(drop_tb,txt)

def PDropFuncion(nombres):
    reinicar_contOP()
    drop_funcion=[nombres]
    txt="\t#Drop Funcion\n"
    txt+="\tt"+str(numT())+"="+str(nombres)+"\n"
    txt+="\tCD3.EDropFuncion()\n"
    agregarInstr(drop_funcion,txt)

#EMPIEZA MIO *****************

    TTv=""
#^^^
def PAlterRenameDatabase(nombreBaseOld,nombreBaseNew):
    global TTv
    reinicar_contOP()
    valores=[nombreBaseOld,nombreBaseNew]
    TTv=""
    addLine("#ALTER Rename Database")
    addLine("t"+str(numT())+"=\'"+nombreBaseOld+"\'")
    addLine("t"+str(numT())+"=\'"+nombreBaseNew+"\'")
    addLine("CD3.EAltRenameDatabase()")
    txt=copy.deepcopy(TTv)
    agregarInstr(valores,txt)


def PAlterTbRenameConst(NombreTabla,ID1,ID2):
    global TTv
    reinicar_contOP()
    valores=[NombreTabla,ID1,ID2]
    TTv=""
    addLine("#ALTER TABLE RENAME Constraint")
    addLine("t"+str(numT())+"=\'"+NombreTabla+"\'")
    addLine("#Old Name")
    addLine("t"+str(numT())+"=\'"+ID1+"\'")
    addLine("#New Name")
    addLine("t"+str(numT())+"=\'"+ID2+"\'")
    #addLine("    CD3.EAltRenameDatabase()")
    txt=copy.deepcopy(TTv)
    agregarInstr("",txt)

#^^^
def PAlterTbRenameTable(baseActiva, NombreTabla,ID1):
    global TTv
    reinicar_contOP()
    valores=[baseActiva, NombreTabla,ID1]
    TTv=""
    addLine("#ALTER TABLE RENAME Table")
    addLine("#Old Table Name")
    addLine("t"+str(numT())+"=\'"+NombreTabla+"\'")
    addLine("#New Table Name")
    addLine("t"+str(numT())+"=\'"+ID1+"\'")
    addLine("CD3.EAltTbRenameTable()")
    txt=copy.deepcopy(TTv)
    agregarInstr(valores,txt)



def PAlterTbRenameColum(baseActiva,NombreTabla,ID1,ID2):
    global TTv
    reinicar_contOP()
    valores=[baseActiva,NombreTabla,ID1,ID2]
    TTv=""
    addLine("#ALTER TABLE RENAME Column")
    addLine("#Table Name")
    addLine("t"+str(numT())+"=\'"+NombreTabla+"\'")
    addLine("#Old Name")
    addLine("t"+str(numT())+"=\'"+ID1+"\'")
    addLine("#New Name")
    addLine("t"+str(numT())+"=\'"+ID2+"\'")
    #addLine("    CD3.EAltRenameDatabase()")
    txt=copy.deepcopy(TTv)
    agregarInstr("",txt)


def PAlterTbAlterSNN(baseActiva,NombreTabla,ID):
    global TTv
    reinicar_contOP()
    valores=[baseActiva,NombreTabla,ID]
    TTv=""
    addLine("#ALTER TABLE ALTER COLUMN set not null")
    addLine("#Table Name")
    addLine("t"+str(numT())+"=\'"+NombreTabla+"\'")
    addLine("#Columna:"+ID+" SET NOT NULL")
    addLine("t"+str(numT())+"=\'"+ID+"\'")
    #addLine("    CD3.EAltRenameDatabase()")
    txt=copy.deepcopy(TTv)
    agregarInstr("",txt)



def PAlterTbAlterSDT(baseActiva,NombreTabla,ID,OPEE1):
    global TTv
    reinicar_contOP()
    valores=[baseActiva,NombreTabla,ID,OPEE1]
    TTv=""
    addLine("#ALTER TABLE ALTER COLUMN set data type")
    addLine("#Table Name")
    addLine("t"+str(numT())+"=\'"+NombreTabla+"\'")
    addLine("#Columna:"+ID+" SET DATA TYPE")
    addLine("t"+str(numT())+"=\'"+ID+"\'")
    addLine("#New Type")
    addLine("t"+str(numT())+"=\'"+OPEE1+"\'")
    #addLine("    CD3.EAltRenameDatabase()")
    txt=copy.deepcopy(TTv)
    agregarInstr("",txt)

def PAlterTbAlterSDef(baseActiva,NombreTabla,ID,valCOL):
    global TTv
    reinicar_contOP()
    valores=[baseActiva,NombreTabla,ID,valCOL]
    TTv=""
    addLine("#ALTER TABLE ALTER COLUMN set default")
    addLine("#Table Name")
    addLine("t"+str(numT())+"=\'"+NombreTabla+"\'")
    addLine("#Columna:"+ID+" SET DEFAULT")
    addLine("t"+str(numT())+"=\'"+ID+"\'")
    addLine("#New Default")
    addLine("t"+str(numT())+"=\'"+str(valCOL)+"\'")
    #addLine("    CD3.EAltRenameDatabase()")
    txt=copy.deepcopy(TTv)
    agregarInstr("",txt)


def PAlterTbAlterDNN(baseActiva,NombreTabla,ID):
    global TTv
    reinicar_contOP()
    valores=[baseActiva,NombreTabla,ID]
    TTv=""
    addLine("#ALTER TABLE ALTER COLUMN drop not null")
    addLine("#Table Name")
    addLine("t"+str(numT())+"=\'"+NombreTabla+"\'")
    addLine("#Columna:"+ID+" DROP NOT NULL")
    addLine("t"+str(numT())+"=\'"+ID+"\'")
    #addLine("    CD3.EAltRenameDatabase()")
    txt=copy.deepcopy(TTv)
    agregarInstr("",txt)


def PAlterTbAlterDDef(baseActiva,NombreTabla,ID):
    global TTv
    reinicar_contOP()
    valores=[baseActiva,NombreTabla,ID]
    TTv=""
    addLine("#ALTER TABLE ALTER COLUMN drop default")
    addLine("#Table Name")
    addLine("t"+str(numT())+"=\'"+NombreTabla+"\'")
    addLine("#Columna:"+ID+" DROP DEFAULT")
    addLine("t"+str(numT())+"=\'"+ID+"\'")
    #addLine("    CD3.EAltRenameDatabase()")
    txt=copy.deepcopy(TTv)
    agregarInstr("",txt)


#^^^
def PAlterTbAlterDropCol(baseActiva,NombreTabla,ID,No_col):
    global TTv
    reinicar_contOP()
    valores=[baseActiva,NombreTabla,ID,No_col]
    TTv=""
    addLine("#ALTER TABLE ALTER COLUMN drop column")
    addLine("#Table Name")
    addLine("t"+str(numT())+"=\'"+NombreTabla+"\'")
    addLine("#Columna:"+ID+" DROP COLUMN")
    addLine("t"+str(numT())+"=\'"+ID+"\'")
    addLine("CD3.EAltTbAlterDropCol()")
    txt=copy.deepcopy(TTv)
    agregarInstr(valores,txt)


def PAlterTbAlterDropConst(baseActiva,NombreTabla,ID):
    global TTv
    reinicar_contOP()
    valores=[baseActiva,NombreTabla,ID]
    TTv=""
    addLine("#ALTER TABLE ALTER COLUMN drop constraint")
    addLine("#Table Name")
    addLine("t"+str(numT())+"=\'"+NombreTabla+"\'")
    addLine("#Constraint:"+ID+" DROP constraint")
    txt=copy.deepcopy(TTv)
    agregarInstr("",txt)



def PAlterTbAlterAddConstUni(baseActiva,NombreTabla,ColN,ID):
    global TTv
    reinicar_contOP()
    valores=[baseActiva,NombreTabla,ID]
    TTv=""
    addLine("#ALTER TABLE ALTER COLUMN add constraint unique")
    addLine("#Table Name")
    addLine("t"+str(numT())+"=\'"+NombreTabla+"\'")
    addLine("#Column Name")
    addLine("t"+str(numT())+"=\'"+ColN+"\'")
    addLine("#Constraint:"+ID+" ADD constraint unique")
    txt=copy.deepcopy(TTv)
    agregarInstr("",txt)  

#^^^
def PAlterTbAlterAddConstPrim(baseActiva,NombreTabla,ColN,ID):
    global TTv
    reinicar_contOP()
    valores=[baseActiva,NombreTabla,ID]
    TTv=""
    addLine("#ALTER TABLE ALTER COLUMN add constraint primary")
    addLine("#Table Name")
    addLine("t"+str(numT())+"=\'"+NombreTabla+"\'")
    addLine("#Column Name")
    addLine("t"+str(numT())+"=\'"+ColN+"\'")
    addLine("#Constraint:"+ID+" ADD constraint primary")
    addLine("CD3.EAltTbAlterAddConstPrim()")
    txt=copy.deepcopy(TTv)
    agregarInstr(valores,txt)  



def PAlterTbAlterAddConstFor(baseActiva,NombreTabla,ColN,ID):
    global TTv
    reinicar_contOP()
    valores=[baseActiva,NombreTabla,ID]
    TTv=""
    addLine("#ALTER TABLE ALTER COLUMN add constraint foreign")
    addLine("#Table Name")
    addLine("t"+str(numT())+"=\'"+NombreTabla+"\'")
    addLine("#Column Name")
    addLine("t"+str(numT())+"=\'"+ColN+"\'")
    addLine("#Constraint:"+ID+" ADD constraint foreign")
    txt=copy.deepcopy(TTv)
    agregarInstr("",txt) 


#^^^
def PAlterTbAlterAddCol(baseActiva,NombreTabla,ID,TIPO):
    global TTv
    reinicar_contOP()
    valores=[baseActiva,NombreTabla,ID]
    TTv=""
    addLine("#ALTER TABLE ALTER COLUMN add column")
    addLine("#Table Name")
    addLine("t"+str(numT())+"=\'"+NombreTabla+"\'")
    addLine("#Column Name")
    addLine("t"+str(numT())+"=\'"+ID+"\'")
    addLine("#Column Type:"+TIPO)
    addLine("CD3.EAltTbAlterAddCol()")

    txt=copy.deepcopy(TTv)
    agregarInstr(valores,txt)  


def addLine(cadena):
    global TTv
    TTv+=("\t"+cadena+"\n")

#FIN MIO *****************



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
    print("Optimizacion")
    for i in listaoptimizaciones:
        print(i)

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
        print("insert en tabla ",Data_insert[1]," \n\tvalores ",Data_insert[2])
        listaMemoria.pop(0)

def EObtenerTabla():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        get_tb=listaMemoria[0]
        result=EDD.showTables(get_tb[0])
        if get_tb[1] in result:
            listaMemoria.pop(0)
            return True
    return False

def EUpdate():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        update_registro=listaMemoria[0]
        indice=update_registro[2]
        valor=update_registro[3]
        col={}
        col[indice]=valor
        EDD.update(update_registro[0],update_registro[1],col,update_registro[4])
        print("update en tabla: ",update_registro[1])
        print("\tregistro actualizado: valor ",valor)
        listaMemoria.pop(0)

def EDelete():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        delete_registro=listaMemoria[0]
        EDD.delete(delete_registro[0],delete_registro[1],delete_registro[2])
        print("delete en tabla: ",delete_registro[1])
        print("\tregistro eliminado: llave primaria:",delete_registro[2])
        listaMemoria.pop(0)

def EShowDatabases():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        databases=listaMemoria[0]
        print("databases: ",str(databases))
        listaMemoria.pop(0)

def EDropTable():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        drop_tb=listaMemoria[0]
        EDD.dropTable(drop_tb[0],drop_tb[1])
        print("tabla eliminada: ",drop_tb[1])
        listaMemoria.pop(0)

def EDropFuncion():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        drop_fn=listaMemoria[0]
        for fn in drop_fn:
            print("funcion eliminada: ",fn.lower())
        listaMemoria.pop(0)

#2INICIO MIO *****************


def EAltRenameDatabase():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        EDD.alterDatabase(listaMemoria[0][0],listaMemoria[0][1])
        print("Base de datos Renombrada Exitosamente")
        listaMemoria.pop(0)

def EAltTbAlterAddCol():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        res=EDD.alterAddColumn(listaMemoria[0][0],listaMemoria[0][1],"")
        print("Resultado de la creacion de la columna:"+str(res))
        listaMemoria.pop(0)

def EAltTbAlterAddConstPrim():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        res=EDD.alterAddPK(listaMemoria[0][0],listaMemoria[0][1],[listaMemoria[0][2]])
        print("Resultado de la creacion de primary key:"+str(res))
        listaMemoria.pop(0)

def EAltTbAlterDropCol():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        res=EDD.alterDropColumn(listaMemoria[0][0],listaMemoria[0][1],[listaMemoria[0][3]])
        print("Resultado de la eliminacion de la columna:"+str(res))
        listaMemoria.pop(0)

def EAltTbRenameTable():
    cargarMemoria()
    #llamar la funcion de EDD
    if(len(listaMemoria)>0):
        res=EDD.alterTable(listaMemoria[0][0],listaMemoria[0][1],[listaMemoria[0][2]])
        print("Resultado de renombrar tabla:"+str(res))
        listaMemoria.pop(0)



#2FIN MIO *****************