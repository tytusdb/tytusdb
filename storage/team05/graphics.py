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
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)
    def alterAddCol(db,table,any_one):
        retorno=newData.alterAddColumn(db,table,any_one)
        if retorno==0:
            messagebox.showinfo("Exito","Se ha agregado columna \'"+str(any_one)+"\' en tabla "+str(table)+" de DB: "+str(db))
            #saveDatabaseFile()
            reloadTablas()
        else:
            mostrarError(retorno)
    
    ventanaAlterAddCol=Tk.Tk()
    ventanaAlterAddCol.geometry("600x200")
    ventanaAlterAddCol.title("Alter Add Column")
    ventanaAlterAddCol.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaAlterAddCol,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaAlterAddCol,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaAlterAddCol,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaAlterAddCol,text="Tabla a Modificar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaAlterAddCol,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    label_column=Tk.Label(ventanaAlterAddCol,text="Default Columna",font=("Arial",14))
    label_column.place(x=50,y=150)

    entry_col=Tk.Entry(ventanaAlterAddCol)
    entry_col.place(x=225,y=150)

    b_addcol=Tk.Button(ventanaAlterAddCol,text="Agregar Columna",command=lambda:[alterAddCol(cb_showdb.get(),cb_showtable.get(),entry_col.get()),ventanaAlterAddCol.destroy()])
    b_addcol.place(x=400,y=150)

def ventana_AlterDropColumn():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
        if value==4:
            messagebox.showerror("Error: "+str(value),"Llave no puede eliminarse o tabla quedarse sin columnas")
        if value==5:
            messagebox.showerror("Error: "+str(value),"Columna fuera de limites")
    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def alterDropCol(db,table,col):
        retorno=newData.alterDropColumn(db,table,col)
        if retorno==0:
            messagebox.showinfo("Exito","Se ha Eliminado la columna: \'"+str(col)+"\' de tabla "+str(table)+" en DB: "+str(db))
            #saveDatabaseFile()
            reloadTablas()
        else:
            mostrarError(retorno)
    ventanaAlterDropCol=Tk.Tk()
    ventanaAlterDropCol.geometry("600x200")
    ventanaAlterDropCol.title("Alter Drop Column")
    ventanaAlterDropCol.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaAlterDropCol,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaAlterDropCol,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaAlterDropCol,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaAlterDropCol,text="Tabla a Modificar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaAlterDropCol,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    label_col=Tk.Label(ventanaAlterDropCol,text="# Columna",font=("Arial",14))
    label_col.place(x=50,y=150)

    entry_col=Tk.Entry(ventanaAlterDropCol)
    entry_col.place(x=225,y=150)

    b_dropcol=Tk.Button(ventanaAlterDropCol,text="Eliminar Columna",command=lambda:[alterDropCol(cb_showdb.get(),cb_showtable.get(),entry_col.get()),ventanaAlterDropCol.destroy()])
    b_dropcol.place(x=400,y=150)
 
def ventana_AlterAddPK():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
        if value==4:
            messagebox.showerror("Error: "+str(value),"Llave primaria existente")
        if value==5:
            messagebox.showerror("Error: "+str(value),"Columna fuera de limites")
        else:
            messagebox.showerror("Error:", "Error desconocido")

    def showColNumber(db,table):
        messagebox.showinfo("Cantidad de Columnas","La tabla contiene: "+str(newData.numeroDeColumnas(db,table))+" columnas")

    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def addPk(db,table,colist):
        colList=colist.split(",")
        retorno=newData.alterAddPK(db,table,colList)
        print("RetornoPK",retorno)
        if retorno==0:
            messagebox.showinfo("Exito","Operacion Exitosa")
        else:
            mostrarError(retorno)

    ventanaAlterAddPk=Tk.Tk()
    ventanaAlterAddPk.geometry("600x200")
    ventanaAlterAddPk.title("Alter Add Primary Key")
    ventanaAlterAddPk.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaAlterAddPk,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaAlterAddPk,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaAlterAddPk,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaAlterAddPk,text="Tabla a Modificar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaAlterAddPk,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    b_showcolnum=Tk.Button(ventanaAlterAddPk,text="Mostrar Cantidad de Columnas",command=lambda : [showColNumber(cb_showdb.get(),cb_showtable.get())])
    b_showcolnum.place(x=400,y=100)


    label_columnas=Tk.Label(ventanaAlterAddPk,text="Columnas \nEj: 0,1,2",font=("Arial",14))
    label_columnas.place(x=50,y=135)

    entry_columnas=Tk.Entry(ventanaAlterAddPk)
    entry_columnas.place_configure(x=225,y=150)

    b_AddPk=Tk.Button(ventanaAlterAddPk,text="Agregar PK",command=lambda:[addPk(cb_showdb.get(),cb_showtable.get(),entry_columnas.get()),ventanaAlterAddPk.destroy()])
    b_AddPk.place(x=400,y=150)

def ventana_AlterDropPK():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
        if value==4:
            messagebox.showerror("Error: "+str(value),"Llave primaria no existente")
        else:
            messagebox.showerror("Error:", "Error desconocido")

    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def dropPK(db,tabla):
        retorno=newData.alterDropPK(str(db),str(tabla))
        if retorno==0:
            messagebox.showinfo("Exito","Operacion Exitosa")
        else:
            mostrarError(retorno)

    ventanaAlterDropPk=Tk.Tk()
    ventanaAlterDropPk.geometry("600x200")
    ventanaAlterDropPk.title("Alter Drop Primary Key")
    ventanaAlterDropPk.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaAlterDropPk,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaAlterDropPk,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaAlterDropPk,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaAlterDropPk,text="Tabla a Modificar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaAlterDropPk,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    b_dropPK=Tk.Button(ventanaAlterDropPk,text="Drop Primary Key",command=lambda:[dropPK(cb_showdb.get(),cb_showtable.get()),ventanaAlterDropPk.destroy()])
    b_dropPK.place(x=400,y=100)

def ventana_ExtractTable():
    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def loadTable(db,tabla):
        retorno=newHash.extractTable(db,tabla)
        lb_tabla.delete('0',Tk.END)
        if retorno==None:
            messagebox.showerror("Error","Ha ocurrido un error")
        elif retorno is not None:
            if len(retorno)!=0:
                for r in retorno:
                    contador=1
                    lb_tabla.insert(contador,str(r))
                    contador=contador+1
            else:
                messagebox.showerror("Error","Lista Vacia")

    ventanaExtractTable=Tk.Tk()
    ventanaExtractTable.geometry("600x400")
    ventanaExtractTable.title("Extract Table")
    ventanaExtractTable.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaExtractTable,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaExtractTable,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaExtractTable,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaExtractTable,text="Tabla a Extraer",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaExtractTable,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    b_extract=Tk.Button(ventanaExtractTable,text="Extract Table",command=lambda:[loadTable(cb_showdb.get(),cb_showtable.get())])
    b_extract.place(x=400,y=100)

    sb=Tk.Scrollbar(ventanaExtractTable)
    sb.pack(side=Tk.RIGHT,fill=Tk.Y)

    lb_tabla=Tk.Listbox(ventanaExtractTable,width=82,yscrollcommand=sb.set)
    lb_tabla.place(x=50,y=150)
    sb.config(command=lb_tabla.yview)

def ventana_ExtractRT():
    def showColNumber(db,table):
        cantidad=newData.numeroDeColumnas(db,table)
        messagebox.showinfo("Cantidad de Columnas","La tabla contiene: "+str(cantidad)+" columnas")
        valores=[]
        contador=0
        while contador<int(cantidad):
            valores.append(contador)
            contador=contador+1
        sb_colnumber['values']=valores
        sb_colnumber.update()
    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def extractRT(db,tabla,colnum,low,up):
        retorno=newHash.extractRangeTable(db,tabla,int(colnum),int(low),int(up))
        lb_tabla.delete('0',Tk.END)
        if retorno==None:
            messagebox.showerror("Error","Ha ocurrido un error")
        elif retorno is not None:
            if len(retorno)!=0:
                for r in retorno:
                    contador=1
                    lb_tabla.insert(contador,str(r))
                    contador=contador+1
            else:
                messagebox.showerror("Error","Lista Vacia")
    
    ventanaExtractRTable=Tk.Tk()
    ventanaExtractRTable.geometry("600x800")
    ventanaExtractRTable.title("Extract Range Table")
    ventanaExtractRTable.iconbitmap("images/icon.ico")
    
    label_db=Tk.Label(ventanaExtractRTable,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaExtractRTable,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaExtractRTable,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaExtractRTable,text="Tabla a Modificar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaExtractRTable,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    b_showcolnum=Tk.Button(ventanaExtractRTable,text="Mostrar Cantidad de Columnas",command=lambda : [showColNumber(cb_showdb.get(),cb_showtable.get())])
    b_showcolnum.place(x=400,y=100)

    label_colNum=Tk.Label(ventanaExtractRTable,text="Columna #: ",font=("Arial",14))
    label_colNum.place(x=50,y=150)
    
    sb_colnumber=Tk.Spinbox(ventanaExtractRTable)
    sb_colnumber.place(x=225,y=150)
    
    label_lower=Tk.Label(ventanaExtractRTable,text="Lower",font=("Arial",14))
    label_lower.place(x=50,y=200)

    entry_lower=Tk.Entry(ventanaExtractRTable)
    entry_lower.place(x=225,y=200)

    label_upper=Tk.Label(ventanaExtractRTable,text="Upper",font=("Arial",14))
    label_upper.place(x=50,y=250)

    entry_upper=Tk.Entry(ventanaExtractRTable)
    entry_upper.place(x=225,y=250)

    b_extract=Tk.Button(ventanaExtractRTable,text="Extract Range Table",command=lambda:[extractRT(cb_showdb.get(),cb_showtable.get(),sb_colnumber.get(),entry_lower.get(),entry_upper.get())])
    b_extract.place(x=400,y=250)

    sb=Tk.Scrollbar(ventanaExtractRTable)
    sb.pack(side=Tk.RIGHT,fill=Tk.Y)

    lb_tabla=Tk.Listbox(ventanaExtractRTable,width=82,yscrollcommand=sb.set)
    lb_tabla.place(x=50,y=300)
    sb.config(command=lb_tabla.yview)

#Ventana Tuples
def ventana_Insert():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
        if value==4:
            messagebox.showerror("Error: "+str(value),"Llave primaria duplicada")
        if value==5:
            messagebox.showerror("Error: "+str(value),"Columna fuera de limites")
        else:
            messagebox.showerror("Error:", "Error desconocido")
    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def insertRegister(db,tabla,registro):
        print("db"+str(db),"table:"+str(tabla),"reg: "+str(registro))
        retorno=newHash.insert(db,tabla,registro.split(","))
        if retorno==0:
            messagebox.showinfo("Exito","Se ha ingresado el registro a la tabla")
        else:
            mostrarError(retorno)
    ventanaInsert=Tk.Tk()
    ventanaInsert.geometry("600x400")
    ventanaInsert.title("Insert")
    ventanaInsert.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaInsert,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaInsert,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaInsert,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaInsert,text="Tabla a Insertar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaInsert,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    l_registro=Tk.Label(ventanaInsert,text="Registro",font=("Arial",14))
    l_registro.place(x=50,y=150)

    entry_registro=Tk.Entry(ventanaInsert,width=50)
    entry_registro.place(x=225,y=150)

    b_cargar=Tk.Button(ventanaInsert,text="Insert",command=lambda: [insertRegister(cb_showdb.get(),cb_showtable.get(),entry_registro.get()),ventanaInsert.destroy()])
    b_cargar.place(x=50,y=200)

def ventana_ExtraerRow():

    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def extractRow(db,table,columns):
        retorno=newHash.extractRow(db,table,columns.split(","))
        lb_tabla.delete('0',Tk.END)
        if retorno==None:
            messagebox.showerror("Error","Ha ocurrido un error")
        elif retorno is not None:
            if len(retorno)!=0:
                for r in retorno:
                    contador=1
                    lb_tabla.insert(contador,str(r))
                    contador=contador+1
            else:
                messagebox.showerror("Error","Lista Vacia")


    ventanaExtractRow=Tk.Tk()
    ventanaExtractRow.geometry("600x500")
    ventanaExtractRow.title("Extract Row")
    ventanaExtractRow.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaExtractRow,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaExtractRow,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaExtractRow,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaExtractRow,text="Tabla a Extraer",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaExtractRow,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)
    
    label_columns=Tk.Label(ventanaExtractRow,text="Columnas",font=("Arial",14))
    label_columns.place(x=50,y=150)

    entry_columns=Tk.Entry(ventanaExtractRow,width=50)
    entry_columns.place(x=225,y=150)

    b_extract=Tk.Button(ventanaExtractRow,text="Extract Row",command=lambda:[extractRow(cb_showdb.get(),cb_showtable.get(),entry_columns.get())])
    b_extract.place(x=50,y=200)

    sb=Tk.Scrollbar(ventanaExtractRow)
    sb.pack(side=Tk.RIGHT,fill=Tk.Y)

    lb_tabla=Tk.Listbox(ventanaExtractRow,width=82,yscrollcommand=sb.set)
    lb_tabla.place(x=50,y=250)
    sb.config(command=lb_tabla.yview)

def ventana_Update():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
        if value==4:
            messagebox.showerror("Error: "+str(value),"Llave primaria no existe")
        else:
            messagebox.showerror("Error:", "Error desconocido")
    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def updateRegister(db,table,register,col):
        #diccionario=dict(zip(range(len(register)),register))
        diccionario={}
        one_step=register.replace("\"","").split(",")
        for c in one_step:
            reg_temp=c.split(":")
            diccionario[reg_temp[0]]=reg_temp[1]

        retorno=newHash.update(db,table,diccionario,col.split(","))
        if retorno==0:
            messagebox.showinfo("Exito","Se ha realizado un Update a la tabla")
        else:
            mostrarError(retorno)



    ventanaUpdate=Tk.Tk()
    ventanaUpdate.geometry("600x400")
    ventanaUpdate.title("Update")
    ventanaUpdate.iconbitmap("images/icon.ico")
    
    label_db=Tk.Label(ventanaUpdate,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaUpdate,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaUpdate,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaUpdate,text="Tabla a Actualizar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaUpdate,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    l_register=Tk.Label(ventanaUpdate,text="Registro",font=("Arial",14))
    l_register.place(x=50,y=150)

    entry_register=Tk.Entry(ventanaUpdate,width=50)
    entry_register.place(x=225,y=150)

    l_columns=Tk.Label(ventanaUpdate,text="Columns",font=("Arial",14))
    l_columns.place(x=50,y=200)

    entry_columns=Tk.Entry(ventanaUpdate,width=50)
    entry_columns.place(x=225,y=200)

    b_update=Tk.Button(ventanaUpdate,text="Update",command=lambda:[updateRegister(cb_showdb.get(),cb_showtable.get(),entry_register.get(),entry_columns.get())])
    b_update.place(x=50,y=250)

def ventana_Delete():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
        if value==4:
            messagebox.showerror("Error: "+str(value),"Llave primaria no existe")
        else:
            messagebox.showerror("Error:", "Error desconocido")

    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def deleteEntry(db,table,columns):
        retorno=newHash.delete(db,table,columns.split(","))
        if retorno==0:
            messagebox.showinfo("Exito","Se ha eliminado el registro de la tabla")
        else:
            mostrarError(retorno)
    ventanaDelete=Tk.Tk()
    ventanaDelete.geometry("600x400")
    ventanaDelete.title("Delete")
    ventanaDelete.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaDelete,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaDelete,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaDelete,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaDelete,text="Tabla a Modificar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaDelete,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    l_columns=Tk.Label(ventanaDelete,text="Columns",font=("Arial",14))
    l_columns.place(x=50,y=150)

    entry_columns=Tk.Entry(ventanaDelete,width=50)
    entry_columns.place(x=225,y=150)

    b_delete=Tk.Button(ventanaDelete,text="Delete",command=lambda:[deleteEntry(cb_showdb.get(),cb_showtable.get(),entry_columns.get()),ventanaDelete.destroy()])
    b_delete.place(x=50,y=200)

def ventana_Truncate():
    def mostrarError(value):
        if value==1:
            messagebox.showerror("Error: "+str(value),"Error en la operacion")
        if value==2:
            messagebox.showerror("Error: "+str(value),"Database no existe")
        if value==3:
            messagebox.showerror("Error: "+str(value),"Table no existe")
        if value==4:
            messagebox.showerror("Error: "+str(value),"Llave primaria no existe")
        else:
            messagebox.showerror("Error:", "Error desconocido")
    def updateAlColDB(nombre):
        cb_showtable['values']=newData.showTables(nombre)

    def truncateDB(db,table):
        retorno=newHash.truncate(db,table)
        if retorno==0:
            messagebox.showinfo("Exito","Registros de tabla han sido eliminados")
        else:
            mostrarError(retorno)



    ventanaTruncate=Tk.Tk()
    ventanaTruncate.geometry("600x200")
    ventanaTruncate.title("Truncate")
    ventanaTruncate.iconbitmap("images/icon.ico")

    label_db=Tk.Label(ventanaTruncate,text="Base de Datos",font=("Arial",14))
    label_db.place(x=50,y=50)

    cb_showdb=Ttk.Combobox(ventanaTruncate,state="readonly")
    cb_showdb['values']=newData.showDatabases()
    cb_showdb.place(x=225,y=50)

    b_showTable=Tk.Button(ventanaTruncate,text="Mostrar Tablas",command=lambda:[updateAlColDB(cb_showdb.get())])
    b_showTable.place(x=400,y=50)

    label_table=Tk.Label(ventanaTruncate,text="Tabla a Truncar",font=("Arial",14))
    label_table.place(x=50,y=100)

    cb_showtable=Ttk.Combobox(ventanaTruncate,state="readonly")
    cb_showtable['values']=newData.showTables(cb_showdb.get())
    cb_showtable.place(x=225,y=100)

    b_truncate=Tk.Button(ventanaTruncate,text="Truncate",command=lambda:[truncateDB(cb_showdb.get(),cb_showtable.get()),ventanaTruncate.destroy()])
    b_truncate.place(x=400,y=100)

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
    

#objetos de menu
bar_menu=Tk.Menu(ventana)

#cascada Archivo
archivo=Tk.Menu(bar_menu,tearoff=0)
archivo.add_command(label="Guardar",command=saveDatabaseFile)
archivo.add_separator()
archivo.add_command(label="Salir...",command=ventana.quit)

def link(tipo):
    import webbrowser
    if tipo=="repo":
        webbrowser.open("https://github.com/tytusdb/tytus/tree/main/storage/team05")
    if tipo=="tecnico":
        webbrowser.open("https://github.com/tytusdb/tytus/tree/main/storage/team05/ManualTecnico.md")
    if tipo=="user":
        webbrowser.open("https://github.com/tytusdb/tytus/tree/main/storage/team05/ManualUsuario.md")
#Cascada ayuda
ayuda=Tk.Menu(bar_menu,tearoff=0)
ayuda.add_command(label="Repositorio", command=lambda:[link("repo")])
ayuda.add_command(label="Manual Tecnico",command=lambda:[link("tecnico")])
ayuda.add_command(label="Manual Usuario",command=lambda:[link("user")])
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

#reportes
reportes=Tk.Menu(bar_menu,tearoff=0)
reportes.add_command(label="Base de Datos",command=lambda:[newData.graficarBaseDato()])
reportes.add_command(label="Tablas",command=lambda:[newData.graficarTablaBaseDato()])

#--Cargar al menu las cascadas
bar_menu.add_cascade(label="Archivo",menu=archivo)
bar_menu.add_cascade(label="Base De Datos",menu=database)
bar_menu.add_cascade(label="Tablas",menu=tables)
bar_menu.add_cascade(label="Tuplas",menu=tuplas)
bar_menu.add_cascade(label="Reportes",menu=reportes)
bar_menu.add_cascade(label="Ayuda",menu=ayuda)

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
