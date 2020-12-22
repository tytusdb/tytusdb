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
