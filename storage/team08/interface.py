import tkinter as tk
import pickle
import Tablas as ta
import Bases as ba
import GeneralesAVL as gA
import Tuplas as tu
import os
from tkinter import messagebox as MessageBox
from tkinter import filedialog
from tkinter import ttk
from tkinter.constants import ANCHOR

raiz = tk.Tk()

class MenuPrincipal:
    os.system('cls')
    def __init__(self,root):
        
        root.title("Grupo 8 Estructuras de Datos")
        root.geometry("600x600")
        barraMenu = tk.Menu(root)
        root.config(menu = barraMenu)
        fileMenu = tk.Menu(barraMenu, tearoff=0)
        fileMenu.add_command(label="Cargar Archivo...", command = self.cargarArchivo)
        fileMenu.add_command(label = "Load", command = self.load)
        fileMenu.add_separator()
        fileMenu.add_command(label = "Salir", command = root.quit) 
        ayuda = tk.Menu(barraMenu, tearoff=0)
        ayuda.add_command(label = "Licencia", command = self.Licencia)
        ayuda.add_separator()
        ayuda.add_command(label = "Acerca de...", command = self.integrantes)
        barraMenu.add_cascade(label="Opciones", menu = fileMenu)
        barraMenu.add_cascade(label="Ayuda", menu = ayuda)

        #MultiPanel
        self.pestanias = ttk.Notebook(root)
        # Agregar Pestañas
        self.basesDatos = ttk.Frame(self.pestanias)
        self.tablas = ttk.Frame(self.pestanias)
        self.tuplas = ttk.Frame(self.pestanias)

        self.pestanias.add(self.basesDatos, text = "Bases de Datos")
        self.pestanias.add(self.tablas, text = "Tablas")
        self.pestanias.add(self.tuplas, text = "Tuplas")

        #-----------------------Contenido Base Datos----------------------------------
        self.lblingresarbase = ttk.Label(self.basesDatos, text = "CreateDatabase")
        self.lblingresarbase.place(x=90,y=100)

        self.txtBase = ttk.Entry(self.basesDatos, width=25)
        self.txtBase.place(x=250, y= 100)

        self.lblSelect = ttk.Label(self.basesDatos, text = "Select DataBase")
        self.lblSelect.place(x=90, y=140)

        self.txtSelect = ttk.Entry(self.basesDatos, width=25)
        self.txtSelect.place(x=250, y=140)

        self.lblupdate = ttk.Label(self.basesDatos, text = "AlterDataBase")
        self.lblupdate.place(x=90, y=180)

        self.txtupdate = ttk.Entry(self.basesDatos, width =25)
        self.txtupdate.place(x=250, y=180)

        self.lbldropDT = ttk.Label(self.basesDatos, text="DropDataBase")
        self.lbldropDT.place(x=90, y=220)

        self.txtdropDT = ttk.Entry(self.basesDatos,width=25)
        self.txtdropDT.place(x=250, y= 220)

        self.txtcheckB = ttk.Entry(self.basesDatos,width=5)
        self.txtcheckB.place(x=230, y= 380)

        #----------------------------------Botones DataBase-----------------------------------------------
        self.btnagg = ttk.Button(self.basesDatos, text = "Crear", command = self.dbcreate)
        self.btnagg.place(x=420, y = 99)

        self.btnupadate = ttk.Button(self.basesDatos, text = "Actualizar", command = self.alterDB)
        self.btnupadate.place(x=420, y=179)

        self.btndrop = ttk.Button(self.basesDatos, text = "Borrar", command = self.dropDB)
        self.btndrop.place(x=420, y=220)

        self.btnmostrarbases = ttk.Button(self.basesDatos, text = "ShowDataBase", command=self.muestraDataBaseG)
        self.btnmostrarbases.place(x = 250 , y = 280, width = 150, height = 30)

        self.btnmostrarbases = ttk.Button(self.basesDatos, text = "Guardar", command=self.guardarBases)
        self.btnmostrarbases.place(x = 275 , y = 330, width = 100, height = 30)

        self.btnmostrarbases = ttk.Button(self.basesDatos, text = "Graphviz", command=self.generarGrapBases)
        self.btnmostrarbases.place(x = 275 , y = 380, width = 100, height = 30)

        # ------------------------Contenido Pestaña Tablas-------------------------------------

        self.lblselecionbase = ttk.Label(self.tablas, text = "Seleccionar DB")
        self.lblselecionbase.place(x=90,y=30)

        self.txtBaseSelec = ttk.Entry(self.tablas, width=25)
        self.txtBaseSelec.place(x=250, y= 30)

        self.lbltable = ttk.Label(self.tablas, text = "Table")
        self.lbltable.place(x=90, y=70)

        self.txttable = ttk.Entry(self.tablas, width =25)
        self.txttable.place(x=250, y=70)

        self.lblnumcol = ttk.Label(self.tablas, text="NumberColumns")
        self.lblnumcol.place(x=90, y=110)

        self.txtnumcol = ttk.Entry(self.tablas,width=25)
        self.txtnumcol.place(x=250, y= 110)

        self.lblcolums = ttk.Label(self.tablas, text = "Columns")
        self.lblcolums.place(x=90, y = 150)

        self.txtcolums = ttk.Entry(self.tablas, width = 25)
        self.txtcolums.place(x=250, y = 150)

        self.lbllow = ttk.Label(self.tablas, text = "Low")
        self.lbllow.place(x=90, y=190)

        self.txtlow = ttk.Entry(self.tablas, width = 25)
        self.txtlow.place(x=250, y = 190)

        self.lblupper = ttk.Label(self.tablas, text = "Upper")
        self.lblupper.place(x=90, y = 230)

        self.txtupper = ttk.Entry(self.tablas, width = 25)
        self.txtupper.place(x=250,y=230)

        self.lblreference = ttk.Label(self.tablas, text = "References",)
        self.lblreference.place(x=90, y= 270)

        self.txtreference = ttk.Entry(self.tablas, width = 25)
        self.txtreference.place(x=250, y = 270)

        self.lbltablenew = ttk.Label(self.tablas, text = "TableNew")
        self.lbltablenew.place(x=90, y= 310)

        self.txttablenew = ttk.Entry(self.tablas, width = 25)
        self.txttablenew.place(x=250, y = 310)

        self.lbldefault = ttk.Label(self.tablas, text = "Default")
        self.lbldefault.place(x= 90, y = 350)

        self.txtdefault = ttk.Entry(self.tablas, width=25)
        self.txtdefault.place(x=250,y = 350)

        self.txtguardarTabla = ttk.Entry(self.tablas, width=5)
        self.txtguardarTabla.place(x=170,y = 510)

        #-------------------------Botones Tablas-------------------------------------------
        self.btnaggtable = ttk.Button(self.tablas, text = "Create",command=self.dbCreateTable)
        self.btnaggtable.place(x=90, y = 400)

        self.btndrop = ttk.Button(self.tablas, text = "AlterTable", command = self.alterTable)
        self.btndrop.place(x=210, y=400)

        self.btndroptable = ttk.Button(self.tablas, text = "Drop", command = self.dropTable)
        self.btndroptable.place(x=330, y= 400)

        self.btnalterPK = ttk.Button(self.tablas, text = "AlterPK", command = self.alterAddPKT)
        self.btnalterPK.place(x=450, y=400)

        self.btnalterdropPk = ttk.Button(self.tablas, text = "AlterDropPK", command = self.alterDropPKT)
        self.btnalterdropPk.place(x=90,y=450)

        self.btnalterColumn = ttk.Button(self.tablas, text = "AlterAddColumn", command = self.alterAddColumn)
        self.btnalterColumn.place(x= 210, y=450)
        
        self.btnalterColumn = ttk.Button(self.tablas, text = "Guardar", command = self.guardarTablas)
        self.btnalterColumn.place(x= 210, y=510)

        self.btnalterColumn = ttk.Button(self.tablas, text = "Graphviz", command = self.generarGrapTablas)
        self.btnalterColumn.place(x= 330, y=510)

        self.btnalterDropColum = ttk.Button(self.tablas, text = "AlterDropColumn", command = self.alterAddColumn)
        self.btnalterDropColum.place(x=330,y=450)

        self.btnrangetable = ttk.Button(self.tablas, text= "ExtractRangeTable", command = self.extractRangeT)
        self.btnrangetable.place(x=450, y= 450)

        self.btnextracttable = ttk.Button(self.tablas, text = "Extract Table", command = self.extractTb)
        self.btnextracttable.place(x= 420, y= 70)

        self.btnmostrartablas = ttk.Button(self.tablas, text = "ShowTables", command=self.muestraTablas)
        self.btnmostrartablas.place(x = 420 , y = 30)

        #-----------------------------Contenido Pestaña Tuplas-------------------------------------
        self.txtcheckTPL = ttk.Entry(self.tuplas, width = 5)
        self.txtcheckTPL.place(x=80, y = 430)
        
        self.lblselectDatabase = ttk.Label(self.tuplas, text = "Select Database")
        self.lblselectDatabase.place(x = 110, y = 50)

        self.txtselectDatabase = ttk.Entry(self.tuplas, width = 25 )
        self.txtselectDatabase.place(x=270, y = 50)

        self.lblselectTablet = ttk.Label(self.tuplas, text = "Select Table")
        self.lblselectTablet.place(x=110, y = 90)

        self.txtselectTablet = ttk.Entry(self.tuplas, width = 25)
        self.txtselectTablet.place(x=270, y = 90)

        self.lblselectcolumn = ttk.Label(self.tuplas, text= "Select Columns")
        self.lblselectcolumn.place(x=110, y = 130)

        self.txtinsert = ttk.Entry(self.tuplas, width = 25)
        self.txtinsert.place(x = 270, y = 130)

        self.lblregister = ttk.Label(self.tuplas, text = "Select Register")
        self.lblregister.place(x=110, y = 170)

        self.txtregister = ttk.Entry(self.tuplas, width = 25)
        self.txtregister.place(x= 270, y = 170)

        self.lblfile = ttk.Label(self.tuplas, text = "File")
        self.lblfile.place(x=110, y = 210)

        self.txtfile = ttk.Entry(self.tuplas, width = 25)
        self.txtfile.place(x=270, y = 210)


        #------------------------------------Botones Tuplas--------------------------------------------------
        self.btninsert = ttk.Button(self.tuplas, text = "Insert", command = self.insertTupla)
        self.btninsert.place(x=120, y = 290,width = 130, height = 30)

        self.btnload = ttk.Button(self.tuplas, text = "LoadCSV", command = self.cargarArchivo)
        self.btnload.place(x=300, y = 290,width = 130, height = 30)

        self.btnextractRow = ttk.Button(self.tuplas, text = "ExtractRow", command = self.motrarRow)
        self.btnextractRow.place(x=120, y= 340,width = 130, height = 30)

        self.btnupdatetupla = ttk.Button(self.tuplas, text = "Update")
        self.btnupdatetupla.place(x=300, y= 340, width = 130, height = 30)

        self.btndelate = ttk.Button(self.tuplas, text = "Delete")
        self.btndelate.place (x=120, y = 380, width = 130, height = 30)

        self.btntruncate = ttk.Button(self.tuplas, text = "Truncate")
        self.btntruncate.place(x=300, y= 380, width = 130, height = 30)

        self.btngraphviz = ttk.Button(self.tuplas, text = "Graphviz", command = self.generarGrapTuplas)
        self.btngraphviz.place(x=120, y = 430, width = 130, height = 30)
        
        self.btngraphviz = ttk.Button(self.tuplas, text = "Guardar", command = self.guardarTuplas)
        self.btngraphviz.place(x=300, y = 430, width = 130, height = 30)

        self.pestanias.pack(expand = 1, fill = "both")

    #-------------------------------Metodos Bases de Datos---------------------------------

    def dbcreate(self):
        if self.txtBase.get() != '':
            #-----------------------------Metodo Create DB------------------------
            temp = ba.b.createBase(self.txtBase.get())
            if temp == 0:
                MessageBox.showinfo("Exito","Base Creada Exitosamente")
            elif temp == 1:
                MessageBox.showinfo("Error","Error en la Operacion")
            elif temp == 2:
                MessageBox.showinfo("Error","Base de Datos ya Existe")
        else:
            MessageBox.showinfo("Vacio","Ingresar Nombre BD")

    def alterDB(self):
        if self.txtSelect.get() != '': #Verificar si esta lleno texbox select
            if self.txtupdate.get() !='': #Verficaar si esta lleno texbox alter
                #-------------------Metodo AlterDATABASE---------------------------------------
                temp = ba.b.alterDatabase(self.txtBase.get(), self.txtupdate.get())
                if temp == 0:
                    MessageBox.showinfo("Exito","Alter completado")
                elif temp ==1:
                    MessageBox.showinfo("Error","Error en la operacion")
                elif temp == 2:
                    MessageBox.showinfo("Error","Base de datos no existe")
                elif temp == 3:
                    MessageBox.showinfo("Error","Base de datos ya existe")
                ba.b.guardar()
            else:
                MessageBox.showinfo("Error","Ingresar nuevo nombre ")
        else:
            MessageBox.showinfo("Error","Ingresar Select Database")

    def dropDB(self):
        if self.txtdropDT.get()!='':
            #------------------------Metodo Drop Database-----------------------------
            temp = ba.b.dropDatabase(self.txtdropDT.get())
            if temp == 0:
                MessageBox.showinfo("Exito","Drop completado")
            elif temp ==1:
                MessageBox.showinfo("Error","Error en la operacion")
            elif temp == 2:
                MessageBox.showinfo("Error","Base de datos no existe")
            ba.b.guardar()
        else:
            MessageBox.showinfo("Error","Ingresar una Base.")

    #---------------------------------METODOS TABLAS-----------------------------------------
    def dbCreateTable(self):
        if self.txtBaseSelec.get() != '': #Verificar Seleccion DB
            if self.txttable.get() != '': #Verificar textbox nombre tabla(Table)
                if self.txtnumcol.get() !='':#Verificar textbox NumColmns
                    #-----------------Metodo para Crear Tablas-----------------------------------
                    temp = ta.t.createTable(self.txtBaseSelec.get(),self.txttable.get(),self.txtnumcol.get())  
                    if temp == 0:
                        MessageBox.showinfo("Exito","Operacion Exitosa")
                    elif temp == 1:
                        MessageBox.showinfo("Error","Error en la operacion")
                    elif temp ==2:
                        MessageBox.showinfo("Error","Base de datos inexistente")
                    elif temp ==3:
                        MessageBox.showinfo("Error","Tabla existente") 
                else:
                    MessageBox.showinfo("Vacio","Ingresar Numero de Columnas")
            else:
                MessageBox.showinfo("Vacio","Ingresar Nombre Tabla")
        else:
            MessageBox.showinfo("Vacio","Ingresar Base de Datos") 

    def extractRangeT(self):
        if self.txtBaseSelec.get() != '': #Verificar Seleccion DB
            if self.txttable.get() != '': #Verificar textbox nombre tabla(Table)
                if self.txtlow.get() !='':#Verificar textbox Low
                    if self.txtupper.get() != '':
                        #-----------------------Ventana con ExtracRangeTable ------------------------
                        nuevar = tk.Toplevel(raiz)
                        nuevar.geometry("500x500")
                        nuevar.title("ExtractRangeTable")
                        listadbr = ta.t.extractRangeTable(self.txtBaseSelec.get(),self.txttable.get(),int(self.txtcolums.get()),int(self.txtlow.get()),int(self.txtupper.get()))
                        tabladbr =ttk.Treeview(nuevar, columns=1)
                        tabladbr['columns'] = ("Elementos")
                        tabladbr.column("#0",width =50)
                        tabladbr.heading("0",text="Elementos")
                        index = 0
                        for f in listadbr:
                            tabladbr.insert("",index, values=f)
                            index  = index+1
                        tabladbr.pack(pady=20) 
                    else:
                        MessageBox.showinfo("Vacio","Ingresar Upper")
                else:
                    MessageBox.showinfo("Vacio","Ingresar Low")
            else:
                MessageBox.showinfo("Vacio","Ingresar Nombre Tabla")
        else:
            MessageBox.showinfo("Vacio","Ingresar Base de Datos") 

    def muestraDataBaseG(self):
        nueva = tk.Toplevel(raiz)
        nueva.geometry("400x300")
        nueva.title("ShowDataBase")
        listadb = ba.b.showDataBases()
        tabladb =ttk.Treeview(nueva, columns=1)
        tabladb['columns'] = ("Bases de Datos")
        tabladb.column("#0",width =50)
        tabladb.heading("0",text="Bases de Datos")
        index = 0
        for f in listadb:
            tabladb.insert("",index, values=f)
            index  = index+1
        tabladb.pack(pady=20)

    def muestraTablas(self):
        if self.txtBaseSelec.get() != '':
            mostrartablas = tk.Toplevel(raiz)
            mostrartablas.geometry("500x500")
            mostrartablas.title("ShowTable")
            listatable = ta.t.showTables(self.txtBaseSelec.get())
            tablatable =ttk.Treeview(mostrartablas, columns=1)
            tablatable['columns'] = ("Tablas")
            tablatable.column("#0",width =50)
            tablatable.heading("0",text="Tablas")
            index = 0
            for f in listatable:
                tablatable.insert("",index, values=f)
                index  = index+1
            tablatable.pack(pady=20)
        else:
            MessageBox.showinfo("Error","Seleccione DB")

    def extractTb(self):
        if self.txtBaseSelec.get() != '':
            if self.txttable.get() !='':
                listatabler = ta.t.extractTable(self.txtBaseSelec.get(),self.txttable.get())
                mostrartablerange = tk.Toplevel(raiz)
                mostrartablerange.geometry("500x500")
                mostrartablerange.title("Extract Table")
                tablatabler =ttk.Treeview(mostrartablerange, columns=1)
                tablatabler['columns'] = ("ExtractTable")
                tablatabler.column("#0",width =50)
                tablatabler.heading("0",text="Elementos")
                index = 0
                for f in range(0,len(listatabler)):
                    g = listatabler[f]
                    for h in g:
                        tablatabler.insert("",index, values=h)
                        index  = index+1
                tablatabler.pack(pady=20)
            else:
                MessageBox.showinfo("Error","Seleccione Tabla")
        else:
            MessageBox.showinfo("Error","Seleccione DB")

    def alterAddPKT(self):
        if self.txtBaseSelec.get() != '':
            if self.txttable.get() !='':
                if self.txtcolums.get() !='':
                    #----------------------------------------Metodo para alterADD PKT
                    temp = 0 # <---Metodo(sustituir en el lugar de 0) textbox a ingresar --> self.txtBaseSelect.get(), self.txttable.get(),self.txtcolums.get()
                    if temp == 0:
                        MessageBox.showinfo("Exito","Operacion Exitosa")
                    elif temp ==1:
                        MessageBox.showinfo("Error","Error en la Operacion")
                    elif temp == 2:
                        MessageBox.showinfo("Error","Database No existe")
                    elif temp == 3:
                        MessageBox.showinfo("Error", "Table No existe")
                    elif temp ==4:
                        MessageBox.showinfo("Error","Llave Primaria Existente")
                    elif temp ==5:
                        MessageBox.showinfo("Error","Columnas fuera de los limites")
                else:
                    MessageBox.showinfo("Error","Ingrese list Colums")
            else:
                MessageBox.showinfo("Error","Seleccione Tabla")
        else:
            MessageBox.showinfo("Error","Seleccione DB")

    def alterDropPKT(self):
        if self.txtBaseSelec.get() !='':
            if self.txttable.get() !='':
                #-----------------------Metodo Drop APK------------------------------
                temp = 0 #<---Metodo(sustituir en el lugar de 0)  Textbox a ingresaar ->self.txtBaseSelect.get(), self.txttable.get()
                if temp == 0:
                    MessageBox.showinfo("Exito","Operacion Exitosa")
                elif temp ==1:
                    MessageBox.showinfo("Error","Error en la Operacion")
                elif temp == 2:
                    MessageBox.showinfo("Error","Database No existe")
                elif temp == 3:
                    MessageBox.showinfo("Error", "Table No existe")
                elif temp ==4:
                    MessageBox.showinfo("Error","Llave Primaria Existente")
            else:
                MessageBox.showinfo("Error","Seleccione Tabla")
        else:
            MessageBox.showinfo("Error","Seleccione DB")

    def alterTable(self):
        if self.txtBaseSelec.get() !='':
            if self.txttable.get() !='':
                if self.txttablenew.get() != '':

                    #-----------------------------METODO ALTERTABLE
                    temp = ta.t.alterTable(self.txtBaseSelec,self.txttable,self.txttablenew)
                    if temp == 0:
                        MessageBox.showinfo("Exito","Operacion Exitosa")
                    elif temp ==1:
                        MessageBox.showinfo("Error","Error en la Operacion")
                    elif temp == 2:
                        MessageBox.showinfo("Error","Database No existe")
                    elif temp == 3:
                        MessageBox.showinfo("Error", "TableOld No existe")
                    elif temp == 4:
                        MessageBox.showinfo("Error","TableNew Existe")
                else:
                    MessageBox.showinfo("Error", "TableNew Vacio")
            else:
                MessageBox.showinfo("Error", "Select Table Vacio (Old Table)")
        else:
            MessageBox.showinfo("Error","Seleccione DB ")

    def alterAddColumn(self):
        if self.txtBaseSelec.get() !='':
            if self.txttable.get() !='':
                if self.txtdefault.get() != '':
                    temp = 0#<---Metodo(sustituir en el lugar de 0) textbox a ingresar --> txtBaseSelect.get(), txttable.get(), txtdefault.get()
                    if temp == 0:
                        MessageBox.showinfo("Exito","Operacion Exitosa")
                    elif temp ==1:
                        MessageBox.showinfo("Error","Error en la Operacion")
                    elif temp == 2:
                        MessageBox.showinfo("Error","Database No existe")
                    elif temp == 3:
                        MessageBox.showinfo("Error", "Table No existe")
                else:
                    MessageBox.showinfo("Error","Ingrese Default")
            else:
                MessageBox.showinfo("Error", "Seleccione Table ")
        else:
            MessageBox.showinfo("Error","Seleccione DB ")

    def alterDropColumn(self):
        if self.txtBaseSelec.get() !='':
            if self.txttable.get() !='':
                if self.txtnumcol.get() != '':
                    #----------------------------------METODO ALTER DROP COLUMN------------------------------------------------------------
                    temp = 0 #<---Metodo(sustituir en el lugar de 0) textbox a ingresar --> txtBaseSelect.get(), txttable.get(),txtnumcol
                    if temp == 0:
                        MessageBox.showinfo("Exito","Operacion Exitosa")
                    elif temp ==1:
                        MessageBox.showinfo("Error","Error en la Operacion")
                    elif temp == 2:
                        MessageBox.showinfo("Error","Database No existe")
                    elif temp == 3:
                        MessageBox.showinfo("Error", "Table No existe")
                    elif temp ==4:
                        MessageBox.showinfo("Error","Llave no puede eliminarso o tabla quedarse sin columnas")
                    elif temp == 5:
                        MessageBox.showinfo("Error","Columna fuera de limites")
                else:
                    MessageBox.showinfo("Error","Seleccione numColums")
            else:
                MessageBox.showinfo("Error", "Seleccione Table ")
        else:
            MessageBox.showinfo("Error","Seleccione DB ")

    def dropTable(self):
        if self.txtBaseSelec.get() !='':
            if self.txttable.get() !='':
                temp = ta.t.dropTable(self.txtBaseSelec.get(),self.txttable.get())
                if temp == 0:
                    MessageBox.showinfo("Exito","Operacion Exitosa")
                elif temp ==1:
                    MessageBox.showinfo("Error","Error en la Operacion")
                elif temp == 2:
                    MessageBox.showinfo("Error","Database No existe")
                elif temp == 3:
                    MessageBox.showerror("Error","Table no existe")
            else:
                MessageBox.showinfo("Error", "Seleccione Table ")
        else:
            MessageBox.showinfo("Error","Seleccione DB ")

    def motrarRow(self):
        muestraTuplas = tk.Toplevel(raiz)
        muestraTuplas.geometry("500x500")
        muestraTuplas.title("ShowTuplas")


#---------------------Métodos Tuplas--------------------------
    def cargarArchivo(self):
        abrir = filedialog.askopenfilename(title ="Cargar ...")
        self.txtfile.insert(0,abrir)
    
    def leerCSV(self, ruta):
        f = open(ruta,'r')
        lst = []
        for linea in f:
            h = linea.replace('\n','')
            lst += [h.split(',')]
            if not linea:
                break
        f.close()
        return lst
    
    def insertTupla(self):
        if self.txtselectDatabase.get() != '':
            if self.txtselectTablet.get() != '':
                if self.txtfile.get() != '':
                    leDato = self.leerCSV(self.txtfile.get())
                    for n in range(0 , len(leDato)):
                        val = tu.u.insert(self.txtselectDatabase.get(),self.txtselectTablet.get(),leDato[n])
                        if val == 0:
                            MessageBox.showinfo("Todo bien Todo Correcto", "Se registro correctamente.")
                        elif val == 1:
                            MessageBox.showinfo("Fatality", "Error de ejecución.")
                        elif val == 2:
                            MessageBox.showinfo("Error", "Base de datos no existe.")
                        elif val == 3:
                            MessageBox.showinfo("Error", "Tabla no existe.")
                        elif val == 5:
                            MessageBox.showinfo("Error", "Columnas fuera de límite.")
                else:
                    MessageBox.showinfo("Error", "Ingrese una ruta válida.")
            else:
                MessageBox.showinfo("Error", "Seleccione Table.")
        else:
            MessageBox.showinfo("Error", "Seleccione DB")




#---------------------------Otros-----------------------------
    def load(self):
        if os.path.isfile('Base.bin') and os.path.isfile('Tabla.bin') and os.path.isfile('Tupla.bin'):
            ba.b, ba.nodoBase.index = gA.g.loadBase()
            ta.t, ta.nodoTabla.index = gA.g.loadTabla()
            tu.u, tu.nodoTupla.key = gA.g.loadTupla()
            MessageBox.showinfo("Load", "Datos cargados.")
        else:
            MessageBox.showinfo("Load", "No hay datos guardados.")

    def integrantes(self):
        MessageBox.showinfo("Integrantes","  201701160 Maria Zucely Hernandez Garcia \n  201708975 Douglas Josue Martinez Huit \n  201709003 Pablo Josue Ayapan Vargas \n  201709073 Walter Alexander Guerra Duque")

    def Licencia(self):
        MessageBox.showinfo("Lincencia","MIT")
    
    def guardarBases(self):
        if self.txtcheckB.get() != '':
            ba.b.guardar()

    def generarGrapBases(self):
        if self.txtcheckB.get() != '':
            ba.b.generarGraphvizBases()

    def guardarTablas(self):
        if self.txtguardarTabla.get() != '':
            ta.t.guardar()

    def generarGrapTablas(self):
        if self.txtguardarTabla.get() != '':
            ta.t.generarGraphvizTablas()
        
    def guardarTuplas(self):
        if self.txtcheckTPL.get() != '':
            tu.u.guardar()

    def generarGrapTuplas(self):
        if self.txtcheckTPL.get() != '':
            tu.u.generarGraphvizTuplas()

principal = MenuPrincipal(raiz)

raiz.mainloop()