from tkinter import *
from tkinter import Frame, ttk, messagebox
from os.path import isdir
from tkinter.constants import BOTH, HORIZONTAL, RAISED, VERTICAL
from team01 import avlMode as crud
import pathlib

class Application(Frame):
    
    def __init__(self, master=None):        
        super().__init__(master)
        master.title("TytusDB")
        self.master = master        
        self.create_tree()        
       
    def create_tree(self):              
        self.treeView = ttk.Treeview(self)
        self.treeView.grid(row=0, column=0, sticky="nsew")
        self.treeView.tag_bind(
            "fstag","<<TreeviewOpen>>",self.item_opened
        )
        for w in (self, self.master):
            w.rowconfigure(0,weight=1)
            w.columnconfigure(0,weight=1)
        self.grid(row=0,column=0,sticky="nsew")
        self.fsobjects={}
        #Seleccion de imagenes para el treeView          
        url=str(pathlib.Path().absolute())+"/team01/"        
        self.file_image = PhotoImage(file=url +"Imagenes/imagenesBaseDatos/file.png")
        self.folder_image = PhotoImage(file=url +"Imagenes/imagenesBaseDatos/database.png")
        self.table_image = PhotoImage(file=url +"Imagenes/imagenesBaseDatos/table.png") 
        self.load_tree(crud.showDatabases()) 

    def get_icon(self, tipo):
        if tipo == "base":
            return self.folder_image
        elif tipo =="table":
            return self.table_image
        else:
            return self.file_image        

    def insert_item(self, name, tipo, parent=""):        
        iid= self.treeView.insert(
            parent,END, text=name, tags=("fstag",),
            image=self.get_icon(tipo)
        )
        self.fsobjects[iid]=tipo
        return iid

    def load_tree(self, path, parent=""):        
        for database in path:            
            child = self.insert_item(database, "base", parent)            
            if crud.showTables(database):
                for tabla in crud.showTables(database):                                       
                    sub_child = self.insert_item(tabla,"table", child)
                    if crud.extractTable(database, tabla):
                        for  registos in crud.extractTable(database, tabla)[0]:                            
                            self.insert_item(registos,"", sub_child)

    def load_subitems(self, idd):
        for child_idd in self.treeView.get_children(idd):
            if isdir(self.fsobjects[child_idd]):
                self.load_tree(self.fsobjects[child_idd], parent=child_idd)
                
    def item_opened(self, event):
        iid= self.treeView.selection()[0]
        self.load_subitems(iid)
#Funciones para las acciones de los menubar Ayuda
def acerca():
    messagebox.showinfo(message="TytusDB Es un proyecto Open Source para desarrollar un administrador de bases de datos", title="Acerca de")

def version():
    messagebox.showinfo(message="Version: Betta", title="Version")

def creditos():
    messagebox.showinfo(message=" Edwin Mauricio Mazariegos -> 9213640 \n Edgar Enrique Patzan Yoc -> 200915715 \n Gabriel Orlando Ajsivinac Xicay -> 201213212 \n Walter Manono Martinez Mateo -> 201213212 \n Karen Elisa Lopez Pinto -> 201313996 ", title="Creditos")

#Configuracion de la ventan principal

ruta =str(pathlib.Path().absolute())+"/team01/"
root = Tk()
pw = ttk.PanedWindow(orient='horizontal')
root.geometry("1024x800")
menubar = Menu(root)
file_menu = Menu(menubar)
file_menu.add_command(label="Acerca de",command=acerca)
file_menu.add_command(label="Version",command=version)
file_menu.add_command(label="Creditos",command=creditos)
#funciones para la asignacion de nuevas ventanas con sus respectivas imagenes
def imagenDataBase():
    newWindow = Toplevel(root)
    newWindow.title("Arbol Avl Base de Datos")
    newWindow.geometry("800x800")   
    fondo = PhotoImage(file=ruta+"Imagenes/graficaArboles/BBDD.png")
    bot2 = Label(newWindow,image=fondo)
    bot2.pack(side=TOP)
    newWindow.add(bot2)

def imagenTable():
    newWindow = Toplevel(root)
    newWindow.title("Arbol Avl Tablas")
    newWindow.geometry("800x800")      
    fondo = PhotoImage(file=ruta+"Imagenes/graficaArboles/Tablas.png")
    bot2 = Label(newWindow,image=fondo)
    bot2.pack(side=TOP)
    newWindow.add(bot2)
def imagenFile():
    newWindow = Toplevel(root)
    newWindow.title("Arbol Avl Registros")
    newWindow.geometry("800x800")   
    fondo = PhotoImage(file=ruta+"Imagenes/graficaArboles/Registros.png")
    bot2 = Label(newWindow,image=fondo)
    bot2.pack(side=TOP)
    newWindow.add(bot2) 
#funcion para los reportes

def  reportes():
    valores =[]
    newWindowReportes = Toplevel(root)
    newWindowReportes.title("Generador de Reportes")
    newWindowReportes.geometry("800x800")
    menu_reportes=Menu(root)
    newWindowReportes.config(menu=menu_reportes)
    label_select = Label(newWindowReportes, text = "Seleccione la base de datos :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 15, padx = 10, pady = 25) 
   
    n=StringVar()
    for dataBase in crud.showDatabases():
        valores.append(dataBase)
    mi_listBox = ttk.Combobox(newWindowReportes, width = 27, textvariable = n, state="readonly") 
    mi_listBox['values'] = valores    
    mi_listBox.grid(column=1,row=15)
    
    def comando():
        correcto_bases=crud.graficaBD()
        #imagenDataBase()       
        label_select_2 = Label(newWindowReportes, text = "Seleccione la Tabla :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 20, padx = 10, pady = 25) 
        valores_tabla =[]
        for dataTable in crud.showTables(n.get()):
            valores_tabla.append(dataTable)
        p=StringVar()
        mi_listBox_tablas = ttk.Combobox(newWindowReportes, width = 27, textvariable = p, state="readonly") 
        mi_listBox_tablas['values']=valores_tabla
        mi_listBox_tablas.grid(column=1,row=20)
        def tuplas():
            correcto_tablas=crud.graficaTBL(n.get())           
            correcto_registro=crud.graficaREG(n.get(),p.get())          
            if(correcto_registro + correcto_tablas + correcto_bases)==0:
                messagebox.showinfo(message=" Graficas generadas correctamente ", title="Graficas",parent=newWindowReportes)
        Button(newWindowReportes,text="Generar registros", command=tuplas, width=20).grid(column=2,row=20)
    Button(newWindowReportes,text="Generar tablas", command=comando, width=20).grid(column=2,row=15)
    mi_listBox.current(0)
    imagen_menu_reporte = Menu(menu_reportes)   
    imagen_menu_reporte.add_command(label="Bases Datos", command=imagenDataBase)
    imagen_menu_reporte.add_command(label="Tablas",command=imagenTable)
    imagen_menu_reporte.add_command(label="Registros",command=imagenFile)
    menu_reportes.add_cascade(label="Reportes",menu=imagen_menu_reporte)
root.config(menu=menubar)
imagen_menu = Menu(menubar)
imagen_menu.add_command(label="Reportes", command=reportes)
imagen_menu.add_command(label="Bases Datos", command=imagenDataBase)
imagen_menu.add_command(label="Tablas",command=imagenTable)
imagen_menu.add_command(label="Registros",command=imagenFile)
menubar.add_cascade(label="Reportes",menu=imagen_menu)
menubar.add_cascade(label="Ayuda", menu=file_menu)
app = Application(master=root)
pw.add(app)
#Imagen de inicio
fondo = PhotoImage(file=ruta+"usac_logo.png")
bot = Label(pw,image=fondo)
bot.pack(side = TOP)
pw.add(bot) 
pw.pack(fill=BOTH, expand=True)
app.mainloop()
