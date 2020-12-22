import tkinter as Tk

import tkinter.ttk as Ttk
from NameStructure import ne as newData
from NameStructure import ht as newHash
from Archivos import archivo as newLoad

from tkinter import messagebox
from tkinter import filedialog
from tkinter import StringVar


#newData es quien importa el paquete de NameStructures
ventana = Tk.Tk()
ventana.geometry("400x200")
ventana.title("TytusDB | EDD A | G5")
ventana.resizable(0,0)

#vars
tablas=[]
#db_name=Tk.StringVar()
#global img

#icon
ventana.iconbitmap('images/icon.ico')

#metodos
def show_acercade():
    messagebox.showinfo("Acerca De...","GRUPO 5:\n\nCARLOS EMILIO CAMPOS MORÁN\nJOSÉ RAFAEL SOLIS FRANCO\nMÁDELYN ZUSETH PÉREZ ROSALES\nJOSÉ FRANCISCO DE JESÚS SANTOS SALAZAR")

def saveDatabaseFile():
    newData.serialize("data/database",newData.database)
def reloadTablas():
    #print("CB_DB_CHANGE")
    #lb_databases_tables.delete(0,'end')
    cb_databases_tables.set("")
    db_name=cb_databases.get()
    tablas=newData.showTables(db_name)
    #for data in tablas:
    #    counter=0
    #    lb_databases_tables.insert(counter,str(data))
    #    counter=counter+1

    cb_databases_tables['values']=tablas
    if tablas is not None:
        if len(tablas)==0:
            messagebox.showerror("ERROR","No hay tablas en "+str(db_name))
        else:
            cb_databases_tables.set("")

def showContenido(db,tabla):
    print('DB:'+str(db),'TB:'+str(tabla))
    newHash.graficar(str(db),str(tabla))


#metodos bar pendientes
#metodos
#ventanas de DATABASE
def ventana_createDatabase():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
    def newDataCrearDB(nombre):
        print("nombre nuevo: ",nombre)
        retorno=newData.createDatabase(nombre)
        if retorno ==0:
            messagebox.showinfo("Exito","Base Creada con exito")
            #saveDatabaseFile()
            cb_databases.set("")
            cb_databases['values']=newData.showDatabases() #actualiza bases de datos en el sistema
        else:
            mostrarError(retorno)
    
    ventanaCreateDB=Tk.Tk()
    ventanaCreateDB.geometry("400x200")
    ventanaCreateDB.title("Create Database")
    ventanaCreateDB.iconbitmap('images/icon.ico')
    
    label_nombre=Tk.Label(ventanaCreateDB,text="Nombre",font=("Arial",14))
    label_nombre.place(x=50,y=50)

    entry_nombre=Tk.Entry(ventanaCreateDB)
    entry_nombre.place(x=50,y=100)
    
    b_crear=Tk.Button(ventanaCreateDB,text="Crear Base de Datos",command=lambda: [newDataCrearDB(entry_nombre.get()),ventanaCreateDB.destroy()])
    b_crear.place(x=225,y=100)

def ventana_alterDatabase():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database OLD no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Database NEW existente")
    def newDataAlterDB(old,new):
        retorno=newData.alterDatabase(old,new)
        if retorno==0:
            messagebox.showinfo("Exito","Base de Datos Actualizada \n"+str(old)+"->"+str(new))
            #saveDatabaseFile()
            cb_databases['values']=newData.showDatabases()
        else:
            mostrarError(retorno)
    ventanaAlterDB=Tk.Tk()
    ventanaAlterDB.geometry("400x200")
    ventanaAlterDB.title("Alter Database")
    ventanaAlterDB.iconbitmap('images/icon.ico')

    label_nombreOld=Tk.Label(ventanaAlterDB,text="Nombre Actual",font=("Arial",14))
    label_nombreOld.place(x=50,y=50)
    label_nombreNew=Tk.Label(ventanaAlterDB,text="Nombre Nuevo",font=("Arial",14))
    label_nombreNew.place(x=225,y=50)

    cb_nombreOld=Ttk.Combobox(ventanaAlterDB,state="readonly")
    cb_nombreOld['values']=newData.showDatabases()
    cb_nombreOld.place(x=50, y=100)
    entry_nombreNew=Tk.Entry(ventanaAlterDB)
    entry_nombreNew.place(x=225,y=100)
    b_alter=Tk.Button(ventanaAlterDB,text="Modificar Base de Datos",command=lambda :[newDataAlterDB(cb_nombreOld.get(),entry_nombreNew.get()),ventanaAlterDB.destroy()])
    b_alter.place(x=125,y=150)

def ventana_dropDatabase():
   def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
    def newDataDropDB(nombre):
        retorno=newData.dropDatabase(nombre)
        if retorno==0:
            messagebox.showinfo("Exito","Base de Datos Eliminada con exito")
            #saveDatabaseFile()
            cb_databases.set("")
            cb_databases['values']=newData.showDatabases()
            reloadTablas()
        else:
            mostrarError(retorno)

    ventanaDropDB=Tk.Tk()
    ventanaDropDB.geometry("400x200")
    ventanaDropDB.title("Drop Database")
    ventanaDropDB.iconbitmap('images/icon.ico')

    label_nombre=Tk.Label(ventanaDropDB,text="Nombre",font=("Arial",14))
    label_nombre.place(x=50,y=50)

    cb_dropDatabase=Ttk.Combobox(ventanaDropDB,state="readonly")
    cb_dropDatabase['values']=newData.showDatabases()
    cb_dropDatabase.place(x=50,y=100)

    
    b_drop=Tk.Button(ventanaDropDB,text="Eliminar Base de Datos",command=lambda: [newDataDropDB(cb_dropDatabase.get()),ventanaDropDB.destroy()])
    b_drop.place(x=225,y=100)

#ventanas de TABLAS
def ventana_createTable():
       def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table existe")
    def newDataCreateT(db,nombre,columna):
        print("db: "+str(db),"nombre: "+str(nombre),"col: "+str(columna))
        retorno=newData.createTable(db,nombre,columna)

        if retorno==0:
            messagebox.showinfo("Exito","Tabla "+str(nombre)+"\ncreada con exito en: "+str(db)+"\nColumna: "+str(columna))
            #saveDatabaseFile()
            reloadTablas()
        else:
            mostrarError(retorno)

    ventanaCreateTable=Tk.Tk()
    ventanaCreateTable.geometry("400x300")
    ventanaCreateTable.title("Create Table")
    ventanaCreateTable.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaCreateTable,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_createTable=Ttk.Combobox(ventanaCreateTable,state="readonly")
    cb_createTable['values']=newData.showDatabases()
    cb_createTable.place(x=225,y=50)

    label_nombre=Tk.Label(ventanaCreateTable,text="Nombre de Tabla",font=("Arial",14))
    label_nombre.place(x=50,y=100)

    entry_nombre=Tk.Entry(ventanaCreateTable)
    entry_nombre.place(x=225,y=100)

    label_columna=Tk.Label(ventanaCreateTable,text="# Columna",font=("Arial",14))
    label_columna.place(x=50,y=150)

    entry_columna=Tk.Entry(ventanaCreateTable)
    entry_columna.place(x=225,y=150)

    b_createTable=Tk.Button(ventanaCreateTable,text="Crear Tabla",command=lambda : [newDataCreateT(cb_createTable.get(),entry_nombre.get(),entry_columna.get()),ventanaCreateTable.destroy()])
    b_createTable.place(x=50,y=200)   
    pass

def ventana_alterTable():
   def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table OLD no existe")
        if value==4:
            messagebox.showerror("Error: "+str(value),"Tabla NEW existente")
    def updateAlterCB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def alterTable(db,old,new):
        retorno=newData.alterTable(db,old,new)
        if retorno==0:
            print(db,old,new)
            messagebox.showinfo("Exito","Se ha renombrado la tabla:\n"+str(old)+"->"+str(new))
            #saveDatabaseFile()
            reloadTablas()
        else:
            mostrarError(retorno)
    ventanaAlterTable=Tk.Tk()
    ventanaAlterTable.geometry("600x300")
    ventanaAlterTable.title("Alter Table")
    ventanaAlterTable.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaAlterTable,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaAlterTable,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaAlterTable,text="Mostrar Tablas",command=lambda:[updateAlterCB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaAlterTable,text="Tabla a Modificar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaAlterTable,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)
    
    label_table=Tk.Label(ventanaAlterTable,text="Nuevo Nombre",font=("Arial",14))
    label_table.place(x=50,y=150)

    entry_newName=Tk.Entry(ventanaAlterTable)
    entry_newName.place(x=225,y=150)

    b_alter=Tk.Button(ventanaAlterTable,text="Modificar Tabla",command=lambda:[alterTable(cb_showdb.get(),cb_showtable.get(),entry_newName.get()),ventanaAlterTable.destroy()])
    b_alter.place(x=400,y=150)

def ventana_delTable():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table existe")
    def updateDropDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)
    def dropTable(db,name):
        retorno=newData.dropTable(db,name)
        if retorno==0:
            messagebox.showinfo("Exito","Se ha eliminado la tabla \'"+str(name)+"\' de "+str(db))
            #saveDatabaseFile()
            reloadTablas()
        else:
            mostrarError(retorno)
    
    ventanaDropTable=Tk.Tk()
    ventanaDropTable.geometry("600x200")
    ventanaDropTable.title("Drop Table")
    ventanaDropTable.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaDropTable,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaDropTable,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaDropTable,text="Mostrar Tablas",command=lambda:[updateDropDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaDropTable,text="Tabla a Eliminar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaDropTable,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)
    
    b_dropTable=Tk.Button(ventanaDropTable,text="Eliminar Tabla",command=lambda:[dropTable(cb_showdb.get(),cb_showtable.get()),ventanaDropTable.destroy()])
    b_dropTable.place(x=400,y=100)
    

def ventana_alterAddColumn():
	pass

def ventana_AlterDropColumn():
	pass

def ventana_AlterAddPK():
	pass

def ventana_AlterDropPK():
	pass

def ventana_ExtractTable():
	pass

def ventana_ExtractRT():
	pass

#ventanas Tuples
def ventana_Insert():
	pass

def ventana_ExtraerRow():
	pass

def ventana_Update():
	pass

def ventana_Delete():
	pass

def ventana_Truncate():
	pass

def ventana_Truncate():
	pass

def ventana_abrirCSV():
    def loadData(file_path,db,table):
        if file_path!="":
            if db !="":
                if table !="":
                    errorCode=newLoad.leerCSV(file_path,db,table)
                    contador_exitoso=0
                    contador_errorOP=0
                    contador_dbNE=0
                    contador_tNE=0
                    contador_llDup=0
                    contador_colOut=0
                    contador_desconocido=0
                    for e in errorCode:
                        if e==0:
                            contador_exitoso=contador_exitoso+1
                        if e==1:
                            contador_errorOP=contador_errorOP+1
                        if e==2:
                            contador_dbNE=contador_dbNE+1
                        if e==3:
                            contador_tNE=contador_tNE+1
                        if e==4:
                            contador_llDup=contador_llDup+1
                        if e==5:
                            contador_colOut=contador_colOut+1
                        else:
                            contador_desconocido=contador_desconocido+1
                    messagebox.showinfo("Archivo Cargado","Operaciones Exitosas: "+str(contador_exitoso)+"\nErrores en Operacion: "+str(contador_errorOP)+"\nDatabase no Existente: "+str(contador_dbNE)+"\nLlave Primaria Duplicada: "+str(contador_llDup)+"\nColumnas Fuera de Limites: "+str(contador_colOut))
            if db=="":
                messagebox.showerror("Error", "No ha seleccionado una Base de Datos")
            else:
                if table=="":
                    messagebox.showerror("Error","No ha seleccionado una Tabla")
        elif file_path=="":
            messagebox.showerror("Error","No se ha seleccionado un archivo")

    def updateCSVDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    archivo_csv =filedialog.askopenfilename(filetypes=[("Archivo de Carga","*.csv")])
    print("File",archivo_csv)
    ventanaCSV=Tk.Tk()
    ventanaCSV.geometry("600x400")
    ventanaCSV.title("Abrir CSV")
    ventanaCSV.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaCSV,text="Base de Datos",font=(("Arial",14)))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaCSV,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaCSV,text="Mostrar Tablas",command=lambda:[updateCSVDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaCSV,text="Tabla a Cargar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaCSV,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    label_path=Tk.Label(ventanaCSV,text="Path",font=("Arial",14))
    label_path.place(x=50,y=150)

    entry_path=Tk.Entry(ventanaCSV,width=44)
    entry_path.place(x=100,y=155)
    entry_path.insert(0,str(archivo_csv))
    entry_path.update()
    entry_path.config(state="readonly")

    b_loadData=Tk.Button(ventanaCSV,text="Carga Informacion",command=lambda:[loadData(archivo_csv,cb_showdb.get(),cb_showtable.get()),ventanaCSV.destroy()])
    b_loadData.place(x=400,y=150)
    
#finmetodos

#objetos de menu
bar_menu=Tk.Menu(ventana)

#cascada Archivo
archivo=Tk.Menu(bar_menu,tearoff=0)
archivo.add_command(label="Guardar",command=saveDatabaseFile)
archivo.add_separator()
archivo.add_command(label="Salir...",command=ventana.quit)

#Cascada ayuda
ayuda=Tk.Menu(bar_menu,tearoff=0)
ayuda.add_command(label="Ayuda")
ayuda.add_command(label="Acerca de...",command=show_acercade)

#cascada Database
database=Tk.Menu(bar_menu,tearoff=0)
database.add_command(label="Create Database",command=ventana_createDatabase)
database.add_command(label="Alter Database",command=ventana_alterDatabase)
database.add_command(label="Drop Database",command=ventana_dropDatabase)

#cascada Tablas
tables=Tk.Menu(bar_menu,tearoff=0)
tables.add_command(label="Create Table",command=ventana_createTable)
tables.add_command(label="Alter Table",command=ventana_alterTable)
tables.add_command(label="Drop Table",command=ventana_delTable)
tables.add_separator()
tables.add_command(label="Add Column",command=ventana_alterAddColumn)
tables.add_command(label="Drop Column",command=ventana_AlterDropColumn)
tables.add_separator()
tables.add_command(label="Alter Add Primary Key",command=ventana_AlterAddPK)
tables.add_command(label="Alter Drop Primary Key",command=ventana_AlterDropPK)
tables.add_command(label="Alter Add Foreign Key",state=Tk.DISABLED)
tables.add_command(label="Alter Add Index",state=Tk.DISABLED)
tables.add_separator()
tables.add_command(label="Extract Table",command=ventana_ExtractTable)
tables.add_command(label="Extract Range Table",command=ventana_ExtractRT)

#cascada Tuplas
tuplas=Tk.Menu(bar_menu,tearoff=0)
tuplas.add_command(label="Insert",command=ventana_Insert)
tuplas.add_command(label="Load CSV",command=ventana_abrirCSV)
tuplas.add_command(label="Extract Row",command=ventana_ExtraerRow)
tuplas.add_command(label="Update",command=ventana_Update)
tuplas.add_command(label="Delete",command=ventana_Delete)
tuplas.add_command(label="Truncate",command=ventana_Truncate)

#--Cargar al menu las cascadas
bar_menu.add_cascade(label="Archivo",menu=archivo)
bar_menu.add_cascade(label="Base De Datos",menu=database)
bar_menu.add_cascade(label="Tablas",menu=tables)
bar_menu.add_cascade(label="Tuplas",menu=tuplas)
bar_menu.add_cascade(label="Ayuda",menu=ayuda)
#fin metodos bar

#variables
tablas=[]

#objetos en la ventana
label_db = Tk.Label(ventana,text="Bases de Datos")
label_db_tables=Tk.Label(ventana,text="Tablas en\n Base de Datos")

cb_databases=Ttk.Combobox(ventana,state="readonly")
cb_databases['values']=newData.showDatabases()
#cb_databases.current(1)

cb_databases_tables=Ttk.Combobox(ventana,state="readonly")
cb_databases_tables['values']=newData.showTables(cb_databases.get())
#lb_databases_tables=Tk.Listbox(ventana)

#frames
b_mostrarTablas=Tk.Button(ventana,text="Mostrar Tablas",command=reloadTablas)
b_mostrarinfo=Tk.Button(ventana,text="Mostrar Contenido",command=lambda:[showContenido(cb_databases.get(),cb_databases_tables.get())])
#posicion de objetos
#labels
label_db.place(x=25,y=25)
label_db_tables.place(x=25,y=65)

#comboboxs
cb_databases.place(x=125,y=25)
cb_databases_tables.place(x=125,y=75)

#lb_databases_tables.grid(column=1,row=1)

#botones
b_mostrarTablas.place(x=275,y=25)
b_mostrarinfo.place(x=275,y=75)

#image_viewer=Tk.Canvas(ventana,height=475,width=750)
#image_viewer.place(x=25,y=100)
#img = Tk.PhotoImage(file="images/descarga.gif")
#image_viewer.create_image(20,20,anchor=Tk.NW,image=img)


#conditionals widgets
tmp_showDB=[]
tmp_showDB=newData.showDatabases()


#ejecucion en bucle
ventana.config(menu=bar_menu)
ventana.mainloop()
