from ArbolAVL import *
from tkinter import *
from tkinter import filedialog
import interfaz as variable

def runinterfaz():
    G=variable.MenuPrincipal()
    
raiz=Tk()
menubar = Menu(raiz)

cadena = "vacio"
nombreArchivo = ""
ficheroactual=""

teeexto=""

#se asigna el menu completo
raiz.config(menu = menubar)

yscroll = Scrollbar(raiz)
yscroll.pack(side=RIGHT, fill=Y)

#cajas de texto
caja1=Text(raiz,width=65,height=30)
caja1.place(x=60,y=100)

caja2=Text(raiz,width=30,height=10)
caja2.place(x=600,y=300)


#Metodos para la interfaz
def Abrir(): #abrir archivo
    try:
        caja1.delete(1.0,END)
        global ficheroactual
        file = filedialog.askopenfilename(filetypes =[('Archivo CSV', '*.csV')])
        caja2.insert(END,file)
        fichero = open(file)
        ficheroactual=file
        global cadena
        global teeexto
        global nombreArchivo
        nombreArchivo = file.split("/")[-1]

        muchoTexto = fichero.read()
        cadena=muchoTexto
        teeexto=muchoTexto
        caja1.delete(1.0,END)
        caja1.insert("insert",muchoTexto)
        fichero.close()
    except:
        print("Ruta no encontrada")

def nuevoA(): #Nuevo archivo
    caja1.delete(1.0,END)

def Datos(): #analiza
    #prueba para mostrar el arbol 
    mWindow= Toplevel()
    mWindow.geometry('300x200')
    mWindow.title('Miembros del grupo')
    mWindow.config(bg="black")
    Dato1 = Label(mWindow, text="GRUPO #6", font=("Impact",10))
    Dato1.place(x=10,y=10)
    Dato2 = Label(mWindow, text="Alex", font=("Impact",10))
    Dato2.place(x=10,y=50)
    Dato3 = Label(mWindow, text="Sohany", font=("Impact",10))
    Dato3.place(x=10,y=90)
    Dato4 = Label(mWindow, text="Jorge", font=("Impact",10))
    Dato4.place(x=10,y=130)
    Dato5 = Label(mWindow, text="Diego", font=("Impact",10))
    Dato5.place(x=10,y=130)
    print("Datos del grupo")

def guardarU():
    global nombreArchivo
    global ficheroactual
    global teeexto
    textt=caja1.get(1.0,END)
    abrirHtml = open(ficheroactual,"w")
    abrirHtml.write(textt)
    abrirHtml.close()
    print("guardar")

def Guardarcomo():
    global teeexto
    global ficheroactual
    textt=caja1.get(1.0,END)
    guardar = filedialog.asksaveasfile(title="Guardar Archivo",initialdir="C:",filetypes = (("Archivo de HTML","*.html*"),("Archivo de CSV","*.csV*")))
    yguardar = open(guardar,"w+",encoding="UTF-8")
    yguardar.write(textt)
    yguardar.close()
    teeexto = guardar
    print("guardar como")


#Aqui empiezan las funciones del db

#"FINALIZADO"
def CreateDB():
    if caja2.get("1.0",END) != "\n":
        caja1.delete("1.0", END)
        nombre = caja2.get("1.0",END)
        nombre = nombre[0:len(nombre)-1]
        respuesta = str(t.createDatabase(nombre))
        caja2.delete("1.0",END)
        caja1.insert(END,respuesta)
        commit(t,"ult")

#"FINALIZADO"
def CreateTable():
    if caja2.get("1.0",END) != "\n":
        caja1.delete("1.0", END)
        nombre = caja2.get("1.0", END)
        nombre = nombre[0:len(nombre) - 1]
        separacion = nombre.split(",")
        db = separacion[0]
        dbNueva = separacion[1]
        numColumnas = separacion[2]
        respuesta = str(t.createTable(db, dbNueva, numColumnas))
        caja2.delete("1.0", END)
        caja1.insert(END, respuesta)
        commit(t, "ult")

#"FINALIZADO"
def AlterDataBase():
    if caja2.get("1.0",END) != "\n":
        caja1.delete("1.0", END)
        nombre = caja2.get("1.0", END)
        nombre = nombre[0:len(nombre) - 1]
        separacion =nombre.split(",")
        dbAntigua = separacion[0]
        dbNueva = separacion[1]
        respuesta = str(t.alterDatabase(dbAntigua,dbNueva))
        caja2.delete("1.0", END)
        caja1.insert(END,respuesta)
        commit(t, "ult")

#FINALIZADO
def ShowDataBase():
    caja1.delete("1.0", END)
    resultado = t.showDatabases()
    if t.raiz != None:
        t.graficar()
        caja1.insert(END,resultado)
        try:
            #prueba para mostrar el arbol
            VBase= Toplevel()
            canvas1=Canvas(VBase, width=600,height=600,background="black")
            canvas1.grid(column=0,row=0)

            scroll_x = Scrollbar(VBase, orient="horizontal", command=canvas1.xview)
            scroll_x.grid(row=1, column=0, sticky="ew")

            scroll_y = Scrollbar(VBase, orient="vertical", command=canvas1.yview)
            scroll_y.grid(row=0, column=1, sticky="ns")

            canvas1.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)


            Grafico=PhotoImage(file="tab.png")
            canvas1.create_image(30, 50, image=Grafico, anchor="nw")

            canvas1.configure(scrollregion=canvas1.bbox("all"))


            VBase.wait_window()
        except:
            print("No se encontró la imagen")
    else:
        caja1.insert(END,"NO SE ENCUENTRAN BASES DE DATOS CREADAS")

#"FINALIZADO"
def DropDatabase():
    if caja2.get("1.0", END) != "\n":
        caja1.delete("1.0", END)
        nombre = caja2.get("1.0", END)
        nombre = nombre[0:len(nombre) - 1]
        respuesta = str(t.dropDatabase(nombre))
        caja2.delete("1.0", END)
        caja1.insert(END, respuesta)
        commit(t, "ult")

#FINALIZADO
def showTables():
    caja1.delete("1.0", END)
    if caja2.get("1.0", END) != "\n":
        db = caja2.get("1.0", END)
        db = db[0:len(db) - 1]
        arbolito = t.buscar(db)
        arbolito.lista.graficar()
        respuesta = str(t.showTables(db))
        caja2.delete("1.0", END)
        caja1.insert(END, respuesta)
        try:
            VBase= Toplevel()
            canvas1=Canvas(VBase, width=600,height=600,background="black")
            canvas1.grid(column=0,row=0)

            scroll_x = Scrollbar(VBase, orient="horizontal", command=canvas1.xview)
            scroll_x.grid(row=1, column=0, sticky="ew")

            scroll_y = Scrollbar(VBase, orient="vertical", command=canvas1.yview)
            scroll_y.grid(row=0, column=1, sticky="ns")

            canvas1.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)


            Grafico=PhotoImage(file="tab.png")
            canvas1.create_image(30, 50, image=Grafico, anchor="nw")

            canvas1.configure(scrollregion=canvas1.bbox("all"))
            VBase.wait_window()
        except:
            print("No se encontró la imagen")
        commit(t, "ult")

#"FINALIZADO"
def extractTable():
    if caja2.get("1.0", END) != "\n":
        caja1.delete("1.0", END)
        nombre = caja2.get("1.0", END)
        nombre = nombre[0:len(nombre) - 1]
        separacion = nombre.split(",")
        db = separacion[0]
        table = separacion[1]
        arbolito = t.buscartabla(db,table)
        try:
            arbolito.lista.graficar()
            respuesta = str(t.extractTable(db, table))
            caja2.delete("1.0", END)
            caja1.insert(END, respuesta)
            try:
                VBase= Toplevel()
                canvas1=Canvas(VBase, width=600,height=600,background="black")
                canvas1.grid(column=0,row=0)

                scroll_x = Scrollbar(VBase, orient="horizontal", command=canvas1.xview)
                scroll_x.grid(row=1, column=0, sticky="ew")

                scroll_y = Scrollbar(VBase, orient="vertical", command=canvas1.yview)
                scroll_y.grid(row=0, column=1, sticky="ns")

                canvas1.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)


                Grafico=PhotoImage(file="tab.png")
                canvas1.create_image(30, 50, image=Grafico, anchor="nw")

                canvas1.configure(scrollregion=canvas1.bbox("all"))
                VBase.wait_window()
            except:
                print("No se encontró la imagen")
        except:
            print("No se encontraron datos en la tabla seleccionada")
        commit(t, "ult")

#"FINALIZADO"
def extractRangeTable():
    if caja2.get("1.0", END) != "\n":
        caja1.delete("1.0", END)
        nombre = caja2.get("1.0", END)
        nombre = nombre[0:len(nombre) - 1]
        separacion = nombre.split(",")
        db = separacion[0]
        table = separacion[1]
        columnNumber = separacion[2]
        lower = separacion[3]
        upper = separacion[4]
        respuesta = str(t.extractRangeTable(db, table,columnNumber, lower, upper))
        caja2.delete("1.0", END)
        caja1.insert(END, respuesta)
        commit(t, "ult")

#FINALIZADO
def alterAddPK():
    if caja2.get("1.0", END) != "\n":
        caja1.delete("1.0", END)
        ingresado = caja2.get("1.0", END)
        ingresado = ingresado[0:len(ingresado) - 1]
        division1 = ingresado.split("[")
        primeraP = division1[0]
        llaves = division1[1]
        llaves = llaves[0:len(llaves)-1]
        donde = primeraP.split(",")
        columns = llaves.split(",")
        db = donde[0]
        table = donde[1]
        respuesta = str(t.alterAddPK(db, table, columns))
        caja2.delete("1.0", END)
        caja1.insert(END, respuesta)
        commit(t, "ult")

#FINALIZADO
def alterDropPK():
    if caja2.get("1.0", END) != "\n":
        caja1.delete("1.0", END)
        nombre = caja2.get("1.0", END)
        nombre = nombre[0:len(nombre) - 1]
        separacion = nombre.split(",")
        db = separacion[0]
        table = separacion[1]
        respuesta = str(t.alterDropPK(db, table))
        caja2.delete("1.0", END)
        caja1.insert(END, respuesta)
        commit(t, "ult")

#PARA LA FASE 2
def alterAddFK():
    print("AlterAddFK")

#PARA LA FASE 2
def alterAddIndex():
    print("alterAddIndex")    

#"FINALIZADO"
def alterTable():
    if caja2.get("1.0", END) != "\n":
        caja1.delete("1.0", END)
        ingresado = caja2.get("1.0", END)
        ingresado = ingresado[0:len(ingresado) - 1]
        separacion = ingresado.split(",")
        db = separacion[0]
        tableOld = separacion[1]
        tableNew = separacion[2]
        respuesta = str(t.alterTable(db, tableOld,tableNew))
        caja2.delete("1.0", END)
        caja1.insert(END, respuesta)
        commit(t, "ult")

#"FINALIZADO"
def alterAddColumn():
    if caja2.get("1.0", END) != "\n":
        caja1.delete("1.0", END)
        ingresado = caja2.get("1.0", END)
        ingresado = ingresado[0:len(ingresado) - 1]
        separacion = ingresado.split(",")
        db = separacion[0]
        table = separacion[1]
        default = separacion[2]
        respuesta = str(t.alterAddColumn(db, table, default))
        caja2.delete("1.0", END)
        caja1.insert(END, respuesta)
        commit(t, "ult")

#"FINALIZADO"
def alterDropColumn():
    if caja2.get("1.0", END) != "\n":
        caja1.delete("1.0", END)
        ingresado = caja2.get("1.0", END)
        ingresado = ingresado[0:len(ingresado) - 1]
        separacion = ingresado.split(",")
        db = separacion[0]
        table = separacion[1]
        columnNumber = separacion[2]
        respuesta = str(t.alterDropColumn(db, table, columnNumber))
        caja2.delete("1.0", END)
        caja1.insert(END, respuesta)
        commit(t, "ult")

#"FINALIZADO"
def dropTable():
    if caja2.get("1.0", END) != "\n":
        caja1.delete("1.0", END)
        ingresado = caja2.get("1.0", END)
        ingresado = ingresado[0:len(ingresado) - 1]
        separacion = ingresado.split(",")
        db = separacion[0]
        table = separacion[1]
        respuesta = str(t.dropTable(db, table))
        caja2.delete("1.0", END)
        caja1.insert(END, respuesta)
        commit(t, "ult")

#"FINALIZADO"
def insert():
    if caja2.get("1.0", END) != "\n":
        caja1.delete("1.0", END)
        ingresado = caja2.get("1.0", END)
        ingresado = ingresado[0:len(ingresado) - 2]
        division1 = ingresado.split("[")
        primeraP = division1[0]
        campos = division1[1]
        campos = campos[0:len(campos)]
        donde = primeraP.split(",")
        register = campos.split(",")
        db = donde[0]
        table = donde[1]
        respuesta = str(t.insert(db, table, register))
        caja2.delete("1.0", END)
        caja1.insert(END, respuesta)
        commit(t, "ult")

#FINALIZADO
def loadCSV():
    parametros = caja2.get("1.0",END)
    parametros = parametros[0:len(parametros)-1]
    division = parametros.split(",")
    path = division[0]
    db = division[1]
    table = division[2]
    t.loadCSV(path,db,table)
    caja2.delete("1.0",END)

#"FINALIZADO"
def extractRow():
    if caja2.get("1.0", END) != "\n":
        caja1.delete("1.0", END)
        ingresado = caja2.get("1.0", END)
        ingresado = ingresado[0:len(ingresado) - 2]
        division1 = ingresado.split("[")
        primeraP = division1[0]
        campos = division1[1]
        campos = campos[0:len(campos)]
        donde = primeraP.split(",")
        columns = campos.split(",")
        db = donde[0]
        table = donde[1]
        respuesta = str(t.extractRow(db, table, columns))
        caja2.delete("1.0", END)
        caja1.insert(END, respuesta)
        commit(t, "ult")

#"FINALIZADO"
def update():
    if caja2.get("1.0", END) != "\n":
        caja1.delete("1.0", END)
        ingresado = caja2.get("1.0", END)
        ingresado = ingresado[0:len(ingresado) - 1]
        val = ingresado.split("{")
        val1 = val[1].split("}")
        val2 = val[0].split(",")
        db = val2[0]
        table = val2[1]
        dict = val1[0].split(",")
        register = {}
        for i in dict:
            f = i.split(":")
            register[f[0]] = f[1]
        cadena = val1[1][2:len(val1[1]) - 1]
        columns = cadena.split(",")
        respuesta = t.update(db, table,register,columns)
        caja2.delete("1.0", END)
        caja1.insert(END, respuesta)
        commit(t, "ult")

#FINALIZADO
def EjecutarBD():
    if caja1.get("1.0", END) != "\n":
        cmd = caja1.get("1.0", END)
        cmd = cmd[0:len(cmd) - 1]
        try:
            opciones = cmd.split('(')
            datos = opciones[1]
            datos = datos[0:len(datos)-1]
            atributos = datos.split(',')
            if opciones[0] == "createDatabase":
                respuesta = str(t.createDatabase(atributos[0]))
                caja1.delete("1.0", END)
                caja1.insert(END, respuesta)
                commit(t, "ult")
            elif opciones[0] == "showDatabases":
                caja1.delete("1.0", END)
                resultado = t.showDatabases()
                t.graficar()
                caja1.insert(END, resultado)
                try:
                    #prueba para mostrar el arbol
                    VBase= Toplevel()
                    canvas1=Canvas(VBase, width=600,height=600,background="black")
                    canvas1.grid(column=0,row=0)

                    scroll_x = Scrollbar(VBase, orient="horizontal", command=canvas1.xview)
                    scroll_x.grid(row=1, column=0, sticky="ew")

                    scroll_y = Scrollbar(VBase, orient="vertical", command=canvas1.yview)
                    scroll_y.grid(row=0, column=1, sticky="ns")

                    canvas1.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)


                    Grafico=PhotoImage(file="tab.png")
                    canvas1.create_image(30, 50, image=Grafico, anchor="nw")

                    canvas1.configure(scrollregion=canvas1.bbox("all"))
                    VBase.wait_window()
                except:
                    print("No se encontró la imagen")
            elif opciones[0] == "alterDatabase":
                dbAntigua = atributos[0]
                dbNueva = atributos[1]
                respuesta = str(t.alterDatabase(dbAntigua, dbNueva))
                caja1.delete("1.0", END)
                caja1.insert(END, respuesta)
                commit(t, "ult")
            elif opciones[0] == "dropDatabase":
                respuesta = str(t.dropDatabase(atributos[0]))
                caja1.delete("1.0", END)
                caja1.insert(END, respuesta)
                commit(t, "ult")
            elif opciones[0] == "createTable":
                db = atributos[0]
                dbNueva = atributos[1]
                numColumnas = atributos[2]
                respuesta = str(t.createTable(db, dbNueva, numColumnas))
                caja1.delete("1.0", END)
                caja1.insert(END, respuesta)
                commit(t, "ult")
            elif opciones[0] == "showTables":
                arbolito = t.buscar(atributos[0])
                arbolito.lista.graficar()
                respuesta = str(t.showTables(atributos[0]))
                caja1.delete("1.0", END)
                caja1.insert(END, respuesta)
                try:
                    VBase= Toplevel()
                    canvas1=Canvas(VBase, width=600,height=600,background="black")
                    canvas1.grid(column=0,row=0)

                    scroll_x = Scrollbar(VBase, orient="horizontal", command=canvas1.xview)
                    scroll_x.grid(row=1, column=0, sticky="ew")

                    scroll_y = Scrollbar(VBase, orient="vertical", command=canvas1.yview)
                    scroll_y.grid(row=0, column=1, sticky="ns")

                    canvas1.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)


                    Grafico=PhotoImage(file="tab.png")
                    canvas1.create_image(30, 50, image=Grafico, anchor="nw")

                    canvas1.configure(scrollregion=canvas1.bbox("all"))
                    VBase.wait_window()
                except:
                    print("No se encontró la imagen")
                commit(t, "ult")
            elif opciones[0] == "extractTable":
                db = atributos[0]
                table = atributos[1]
                arbolito = t.buscartabla(db, table)
                try:
                    arbolito.lista.graficar()
                    respuesta = str(t.extractTable(db, table))
                    caja2.delete("1.0", END)
                    caja1.insert(END, respuesta)
                    try:
                        VBase= Toplevel()
                        canvas1=Canvas(VBase, width=600,height=600,background="black")
                        canvas1.grid(column=0,row=0)

                        scroll_x = Scrollbar(VBase, orient="horizontal", command=canvas1.xview)
                        scroll_x.grid(row=1, column=0, sticky="ew")

                        scroll_y = Scrollbar(VBase, orient="vertical", command=canvas1.yview)
                        scroll_y.grid(row=0, column=1, sticky="ns")

                        canvas1.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)


                        Grafico=PhotoImage(file="tab.png")
                        canvas1.create_image(30, 50, image=Grafico, anchor="nw")

                        canvas1.configure(scrollregion=canvas1.bbox("all"))
                        VBase.wait_window()
                    except:
                        print("No se encontró la imagen")
                except:
                    print("No se encontraron datos en la tabla seleccionada")
                commit(t, "ult")
            elif opciones[0] == "extractRangeTable":
                db = atributos[0]
                table = atributos[1]
                columnNumber = atributos[2]
                lower = atributos[3]
                upper = atributos[4]
                respuesta = str(t.extractRangeTable(db, table, columnNumber, lower, upper))
                caja1.delete("1.0", END)
                caja1.insert(END, respuesta)
                commit(t, "ult")
            elif opciones[0] == "alterAddPK":
                division1 = datos.split("[")
                primeraP = division1[0]
                llaves = division1[1]
                llaves = llaves[0:len(llaves) - 1]
                donde = primeraP.split(",")
                columns = llaves.split(",")
                db = donde[0]
                table = donde[1]
                respuesta = str(t.alterAddPK(db, table, columns))
                caja1.delete("1.0", END)
                caja1.insert(END, respuesta)
                commit(t, "ult")
            elif opciones[0] == "alterDropPK":
                db = atributos[0]
                table = atributos[1]
                respuesta = str(t.alterDropPK(db, table))
                caja1.delete("1.0", END)
                caja1.insert(END, respuesta)
                commit(t, "ult")
            elif opciones[0] == "alterTable":
                db = atributos[0]
                tableOld = atributos[1]
                tableNew = atributos[2]
                respuesta = str(t.alterTable(db, tableOld, tableNew))
                caja1.delete("1.0", END)
                caja1.insert(END, respuesta)
                commit(t, "ult")
            elif opciones[0] == "alterAddColumn":
                db = atributos[0]
                table = atributos[1]
                default = atributos[2]
                respuesta = str(t.alterAddColumn(db, table, default))
                caja1.delete("1.0", END)
                caja1.insert(END, respuesta)
                commit(t, "ult")
            elif opciones[0] == "alterDropColumn":
                db = atributos[0]
                table = atributos[1]
                columnNumber = atributos[2]
                respuesta = str(t.alterDropColumn(db, table, columnNumber))
                caja1.delete("1.0", END)
                caja1.insert(END, respuesta)
                commit(t, "ult")
            elif opciones[0] == "dropTable":
                db = atributos[0]
                table = atributos[1]
                respuesta = str(t.dropTable(db, table))
                caja1.delete("1.0", END)
                caja1.insert(END, respuesta)
                commit(t, "ult")
            elif opciones[0] == "insert":
                division1 = datos.split("[")
                primeraP = division1[0]
                campos = division1[1]
                campos = campos[0:len(campos)]
                donde = primeraP.split(",")
                register = campos.split(",")
                db = donde[0]
                table = donde[1]
                respuesta = str(t.insert(db, table, register))
                caja2.delete("1.0", END)
                caja1.insert(END, respuesta)
                commit(t, "ult")
            elif opciones[0] == "loadCSV":
                path = atributos[0]
                db = atributos[1]
                table = atributos[2]
                t.loadCSV(path, db, table)
            elif opciones[0] == "extractRow":
                division1 = datos.split("[")
                primeraP = division1[0]
                campos = division1[1]
                campos = campos[0:len(campos)]
                donde = primeraP.split(",")
                columns = campos.split(",")
                db = donde[0]
                table = donde[1]
                respuesta = str(t.extractRow(db, table, columns))
                caja2.delete("1.0", END)
                caja1.insert(END, respuesta)
                commit(t, "ult")
            elif opciones[0] == "update":
                val = datos.split("{")
                val1 = val[1].split("}")
                val2 = val[0].split(",")
                db = val2[0]
                table = val2[1]
                dict = val1[0].split(",")
                register = {}
                for i in dict:
                    f = i.split(":")
                    register[f[0]] = f[1]
                cadena = val1[1][2:len(val1[1]) - 1]
                columns = cadena.split(",")
                respuesta = t.update(db, table, register, columns)
                caja2.delete("1.0", END)
                caja1.insert(END, respuesta)
                commit(t, "ult")
            elif opciones[0] == "delete":
                division1 = datos.split("[")
                primeraP = division1[0]
                llaves = division1[1]
                llaves = llaves[0:len(llaves) - 1]
                donde = primeraP.split(",")
                columns = llaves.split(",")
                db = donde[0]
                table = donde[1]
                respuesta = str(t.deletet(db, table, columns))
                caja2.delete("1.0", END)
                caja1.insert(END, respuesta)
                commit(t, "ult")
            elif opciones[0] == "truncate":
                db = atributos[0]
                dbNueva = atributos[1]
                respuesta = str(t.truncate(db, dbNueva))
                caja2.delete("1.0", END)
                caja1.insert(END, respuesta)
                commit(t, "ult")
            else:
                caja1.delete("1.0", END)
                caja1.insert(END, "VERIFIQUE LOS DATOS INGRESADOS")
        except:
            caja1.delete("1.0",END)
            caja1.insert(END,"INGRESE UN COMANDO VALIDO")

#"FINALIZADO"
def Truncate():
    if caja2.get("1.0", END) != "\n":
        caja1.delete("1.0", END)
        nombre = caja2.get("1.0", END)
        nombre = nombre[0:len(nombre) - 1]
        separacion = nombre.split(",")
        db = separacion[0]
        dbNueva = separacion[1]
        respuesta = str(t.truncate(db, dbNueva))
        caja2.delete("1.0", END)
        caja1.insert(END, respuesta)
        commit(t, "ult")

#"FINALIZADO"
def Delete():
    if caja2.get("1.0", END) != "\n":
        caja1.delete("1.0", END)
        ingresado = caja2.get("1.0", END)
        ingresado = ingresado[0:len(ingresado) - 1]
        division1 = ingresado.split("[")
        primeraP = division1[0]
        llaves = division1[1]
        llaves = llaves[0:len(llaves)-1]
        donde = primeraP.split(",")
        columns = llaves.split(",")
        db = donde[0]
        table = donde[1]
        respuesta = str(t.deletet(db, table, columns))
        caja2.delete("1.0", END)
        caja1.insert(END, respuesta)
        commit(t, "ult")
    


##Configuracion de la parte visual
raiz.title("Base de datos con AVL")
raiz.geometry("1150x600")
raiz.config(bg="black")


#titulo
Titulo = Label(raiz, text="BASE DE DATOS GRUPO 6", font=("Impact",30))
Titulo.place(x=400,y=25)

##Botones para las funciones
boton1 = Button(raiz, text="createDatabase", activebackground="#F50743",command=CreateDB)
boton1.place(x=600,y=100)
boton1.config(width=13, height=1)
boton2 = Button(raiz, text="showDatabases", activebackground="#F50743",command=ShowDataBase)
boton2.place(x=700,y=100)
boton2.config(width=13, height=1)
boton3 = Button(raiz, text="alterDatabase", activebackground="#F50743",command=AlterDataBase)
boton3.place(x=800,y=100)
boton3.config(width=13, height=1)
boton4 = Button(raiz, text="dropDatabase", activebackground="#F50743",command=DropDatabase)
boton4.place(x=900,y=100)
boton4.config(width=13, height=1)
boton5 = Button(raiz, text="createTable", activebackground="#F50743",command=CreateTable)
boton5.place(x=1000,y=100)
boton5.config(width=13, height=1)
boton6 = Button(raiz, text="showTables", activebackground="#F50743",command=showTables)
boton6.place(x=600,y=150)
boton6.config(width=13, height=1)
boton7 = Button(raiz, text="extractTable", activebackground="#F50743",command=extractTable)
boton7.place(x=700,y=150)
boton7.config(width=13, height=1)
boton8 = Button(raiz, text="update", activebackground="#F50743",command=update)
boton8.place(x=800,y=150)
boton8.config(width=13, height=1)
boton9 = Button(raiz, text="alterAddPK", activebackground="#F50743",command=alterAddPK)
boton9.place(x=900,y=150)
boton9.config(width=13, height=1)
boton10 = Button(raiz, text="alterDropPK", activebackground="#F50743",command=alterDropPK)
boton10.place(x=1000,y=150)
boton10.config(width=13, height=1)
boton11 = Button(raiz, text="alterAddFK", activebackground="#F50743",command=alterAddFK)
boton11.place(x=600,y=200)
boton11.config(width=13, height=1)
boton12 = Button(raiz, text="alterAddIndex", activebackground="#F50743",command=alterAddIndex)
boton12.place(x=700,y=200)
boton12.config(width=13, height=1)
boton13 = Button(raiz, text="alterTable", activebackground="#F50743",command=alterTable)
boton13.place(x=800,y=200)
boton13.config(width=13, height=1)
boton14 = Button(raiz, text="alterAddColumn", activebackground="#F50743",command=alterAddColumn)
boton14.place(x=900,y=200)
boton14.config(width=13, height=1)
boton15 = Button(raiz, text="alterDropColumn", activebackground="#F50743",command=alterDropColumn)
boton15.place(x=1000,y=200)
boton15.config(width=13, height=1)
boton16 = Button(raiz, text="dropTable", activebackground="#F50743",command=dropTable)
boton16.place(x=600,y=250)
boton16.config(width=13, height=1)
boton17 = Button(raiz, text="insert", activebackground="#F50743",command=insert)
boton17.place(x=700,y=250)
boton17.config(width=13, height=1)
boton18 = Button(raiz, text="loadCSV", activebackground="#F50743",command=loadCSV)
boton18.place(x=800,y=250)
boton18.config(width=13, height=1)
boton19 = Button(raiz, text="extractRow", activebackground="#F50743",command=extractRow)
boton19.place(x=900,y=250)
boton19.config(width=13, height=1)
boton20 = Button(raiz, text="extractRangeTable", activebackground="#F50743",command=extractRangeTable)
boton20.place(x=1000,y=250)
boton20.config(width=13, height=1)
boton21 = Button(raiz, text="Truncate", activebackground="#F50743",command=Truncate)
boton21.place(x=900,y=300)
boton21.config(width=13, height=1)
boton22 = Button(raiz, text="Delete", activebackground="#F50743",command=Delete)
boton22.place(x=1000,y=300)
boton22.config(width=13, height=1)


BotonEjecutar = Button(raiz, text="Ejecutar Base de datos", activebackground="#F50743",command=EjecutarBD)
BotonEjecutar.place(x=600,y=500)

#BotonVer = Button(raiz, text="Ver Base de datos", activebackground="#F50743",command=VBD)
#BotonVer.place(x=750,y=500)


#Menu de acciones
menubar.add_command(label = "Nuevo", command = nuevoA)
menubar.add_command(label = "Abrir", command = Abrir)
menubar.add_command(label = "Guardar", command=guardarU)
menubar.add_command(label = "Guardar Como", command=Guardarcomo)
menubar.add_command(label = "Saber mas", command=Datos)
menubar.add_command(label = "Salir", command = raiz.quit)

#bucle de la aplicacion
t = ArbolAVL()
try:
    t = rollback("ult")
except:
    print("no se encontró")
raiz.mainloop()
commit(t, "ult")




