import os
import sys
import webbrowser
import platform
import socket
import sys
from tkinter import *
import tkinter as tk
from tkinter import ttk, font, messagebox
from datetime import date
from datetime import datetime

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_add = ('localhost', 10000)
print('connection to port=>', serv_add)
serv.connect(serv_add)


class cliente():

    def __init__(self, img_carpeta, iconos):
        self.consoleMode = False
        # Prueba de conexion a base de datos
        message = 'data from client'
        print(message)
        serv.sendall(message.encode('utf-8'))

        recibido = 0
        esperado = len(message)

        while recibido < esperado:
            data = serv.recv(4096)
            recibido += len(data)
            print(data)

        # Creacion de la Ventana
        self.raiz = Tk()
        self.f_log()
        self.treeview = ttk.Treeview(self.raiz)

        '''
        iconos = (ruta_r + "pyremoto64x64.png",
              ruta_r + "conec16x16.png",
              ruta_r + "salir16x16.png",
              ruta_r + "star16x16.png",
              ruta_r + "conec32x32.png",
              ruta_r + "salir32x32.png",
              ruta_r + "grupo32x32.png", 
              ruta_r + "tytusdb.png",
              ruta_r + "open.png",
              ruta_r + "save.png",
              ruta_r + "serv.png") 
        '''

        # Definicion de Iconos
        self.img_carpeta = img_carpeta
        self.iconos = iconos
        self.PYREMOTO_ICON = PhotoImage(file=self.iconos[0])
        # icono2 = PhotoImage(file=self.iconos[1])
        # icono3 = PhotoImage(file=self.iconos[2])
        self.START_ICON = PhotoImage(file=self.iconos[3])
        self.CONNECT_ICON = PhotoImage(file=self.iconos[4])
        self.EXIT_ICON = PhotoImage(file=self.iconos[5])
        self.GRUPO_ICON = PhotoImage(file=self.iconos[6])
        self.TYTUS_ICON = PhotoImage(file=self.iconos[7])
        self.OPEN_ICON = PhotoImage(file=self.iconos[8])
        self.SAVE_ICON = PhotoImage(file=self.iconos[9])
        self.SERV_ICON = PhotoImage(file=self.iconos[10])
        self.BD_ICON = PhotoImage(file = self.iconos[11])
        self.TB_ICON = PhotoImage(file = self.iconos[12])
        self.COL_ICON = PhotoImage(file = self.iconos[13])
        self.CONSOLE_ICON = PhotoImage(file = self.iconos[14])


        self.TBASE_ICON = PhotoImage(file=self.iconos[15])
        self.TCARPETA_ICON = PhotoImage(file=self.iconos[16])
        self.TGUARDAR_ICON = PhotoImage(file=self.iconos[17])
        self.TBUSCAR_ICON = PhotoImage(file=self.iconos[18])
        self.TVACIAR_ICON = PhotoImage(file=self.iconos[19])
        self.TCOMPILAR_ICON = PhotoImage(file=self.iconos[20])
        self.TEXPLICAR_ICON = PhotoImage(file=self.iconos[21])
        self.TDESCARGAR_ICON = PhotoImage(file=self.iconos[22])
        self.TCERRAR_ICON = PhotoImage(file=self.iconos[23])
        

        # Preconfiguracion de la ventana

        self.raiz.title("TytusDB ")
        self.raiz.iconphoto(self.raiz, self.PYREMOTO_ICON)
        self.raiz.option_add("*Font", "Helvetica 12")
        self.raiz.option_add('*tearOff', True)
        self.raiz.attributes('-fullscreen', True)
        self.raiz.minsize(400, 300)
        self.fuente = font.Font(weight='normal')

        self.CFG_TIPOCONEX = IntVar()
        self.CFG_TIPOCONEX.set(1)
        self.CFG_TIPOEMUT = IntVar()
        self.CFG_TIPOEMUT.set(1)
        self.CFG_TIPOEXP = IntVar()
        self.CFG_TIPOEXP.set(1)

        self.estado = IntVar()
        self.estado.set(1)

        # Definicion del Menu
        barramenu = Menu(self.raiz)
        self.raiz['menu'] = barramenu
        self.fileMenu = Menu(barramenu)
        self.objectMenu = Menu(barramenu)
        self.toolsMenu = Menu(barramenu)
        self.aboutMenu = Menu(barramenu)
        barramenu.add_cascade(menu=self.fileMenu, label='FILE')
        barramenu.add_cascade(menu=self.objectMenu, label='OBJECT')
        barramenu.add_cascade(menu=self.toolsMenu, label='TOOLS')
        barramenu.add_cascade(menu=self.aboutMenu, label='ABOUT')

        # Programacion del Menu de Archivos
        self.fileMenu.add_command(label='   Abrir archivo *.sql', underline=0,command=self.f_cargar,
                                  image=self.OPEN_ICON, compound=LEFT)
        self.fileMenu.add_command(label='   Guardar archivo *.sql', underline=0,command = self.f_guardar,
                                  image=self.SAVE_ICON, compound=LEFT)

        # Programacion del Menu de Objetos

        # Programacion del Menu de Herramientas
        self.toolsMenu.add_command(
            label="Query Tool", command=self.f_query_tool, image=self.START_ICON, compound=LEFT)

        # Programacion del Menu de informacion
        self.aboutMenu.add_command(
            label="GRUPO 10", command=self.f_integrantes, image=self.GRUPO_ICON, compound=LEFT)
        self.aboutMenu.add_command(
            label="TytusDB", command=self.f_web, image=self.TYTUS_ICON, compound=LEFT)

        # Definicion de la Barra De Herramientas
        barraherr = Frame(self.raiz, relief=RAISED, bd=2, bg="#E5E5E5")
        barraherr.pack(side=TOP, fill=X)

        # Programacion del Boton de salida de la aplicacion
        bot2 = Button(barraherr, image=self.EXIT_ICON,  command=self.f_salir)
        bot2.pack(side=RIGHT, padx=1, pady=1)

        # Programacion del Boton de conexion a la base de datos
        bot1 = Button(barraherr, image=self.CONNECT_ICON,
                      command=self.f_conectar)
        bot1.pack(side=RIGHT, padx=2, pady=2)

        # Programacion de consola de PRUEBA, es unicamente para probar el switch de la consola
        botconsole = Button(barraherr, image = self.CONSOLE_ICON, command = self.f_switch_console_mode)
        botconsole.pack(side=RIGHT, padx=2, pady=2)

        # Barra Inferior
        now = datetime.now()
        format = now.strftime(
            'Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
        print(format)
        mensaje = " " + format
        self.barraest = Label(self.raiz, text=mensaje,
                              bd=1, relief=SUNKEN, anchor=W)
        self.barraest.pack(side=BOTTOM, fill=X)

        self.menucontext = Menu(self.raiz, tearoff=FALSE)
        self.menucontext.add_command(
            label="Salir", command=self.f_salir, compound=LEFT)

        # Definicion del Cuerpo de la Aplicacion
        # Cuerpo Principal
        cuerpo = Frame(self.raiz, relief=RAISED, bd=2, bg = 'white')
        cuerpo.pack(side=BOTTOM, fill=BOTH, expand=True)

        # Cuerpo del Treeview
        treeFrame = LabelFrame(cuerpo,bg="white")
        treeFrame.config(bg='steelblue', width="300")
        treeFrame.pack(side=LEFT, fill=Y)
        style = ttk.Style(treeFrame)
        style.configure('Treeview', rowheight=40)
        self.treeview = ttk.Treeview(treeFrame, selectmode="extended")
        self.treeview.column("#0", anchor=W, width=300)
        
        item = self.treeview.insert("", tk.END, text="Server", image=self.SERV_ICON)
        for x in range(1, 5):
            item2 = self.treeview.insert(item, tk.END,text="Databases"+str(x),image=self.BD_ICON)
            item3 = self.treeview.insert(item2, tk.END, text="Tables",image=self.TB_ICON)
            for x in range(1, 5):
                item4 = self.treeview.insert(item3, tk.END, text="Tabla"+str(x),image=self.TB_ICON)
                for x in range(1, 4):
                    self.treeview.insert(item4, tk.END, text="Columna"+str(x),image=self.COL_ICON)
        self.treeview.pack(fill=BOTH, expand=True)

        # SubCuerpo
        SubCuerpo = Frame(cuerpo)
        SubCuerpo.config(bg='white')
        SubCuerpo.pack(side=LEFT, fill=BOTH, expand=True)

        # QueryTool
        self.QueryTool = Frame(SubCuerpo)
        self.QueryTool.config(bg = 'white', height = "400")
        self.QueryTool.pack(side = TOP, fill = X)


        # QueryTool Edit Text
        self.QueryTool2 = Frame(SubCuerpo)
        self.QueryTool2.config(bg = 'green', height = "400")
        self.QueryTool2.pack(side = TOP, fill = X)

        self.QueryTool2.pack_forget()

        #botones
        toolbar3 = Label(self.QueryTool2, bg="Gainsboro")
        toolbar3.pack(side=TOP, fill = X)

        btnBase = Button(toolbar3, image=self.TBASE_ICON,command=self.f_cargar)
        # btnBase.grid(row=0,column=1, padx=8)
        btnBase.pack(side = LEFT, padx=2, pady=2)

        btnCarpeta = Button(toolbar3, image=self.TCARPETA_ICON)
        # btnCarpeta.grid(row=0,column=2, padx=8)
        btnCarpeta.pack(side = LEFT, padx=2, pady=2)

        btnGuardar = Button(toolbar3, image=self.TGUARDAR_ICON,command = self.f_guardar)
        # btnGuardar.grid(row=0,column=3, padx=8)
        btnGuardar.pack(side = LEFT, padx=2, pady=2)

        btnBuscar = Button(toolbar3, image=self.TBUSCAR_ICON,command = self.f_buscar)
        # btnBuscar.grid(row=0,column=4, padx=8)
        btnBuscar.pack(side = LEFT, padx=2, pady=2)

        btnVaciar = Button(toolbar3, image=self.TVACIAR_ICON)
        # btnVaciar.grid(row=0,column=5, padx=8)
        btnVaciar.pack(side = LEFT, padx=2, pady=2)

        btnCompilar = Button(toolbar3, image=self.TCOMPILAR_ICON,command = self.f_compilar)
        # btnCompilar.grid(row=0,column=6, padx=8)
        btnCompilar.pack(side = LEFT, padx=2, pady=2)

        btnExplicar = Button(toolbar3, image=self.TEXPLICAR_ICON)
        # btnExplicar.grid(row=0,column=7, padx=8)
        btnExplicar.pack(side = LEFT, padx=2, pady=2)

        btnDescargar = Button(toolbar3, image=self.TDESCARGAR_ICON)
        # btnDescargar.grid(row=0,column=8, padx=8)
        btnDescargar.pack(side = LEFT, padx=2, pady=2)

        btnCerrar = Button(toolbar3, image=self.TCERRAR_ICON, command=self.f_cerrar_query_tool)
        # btnCerrar.grid(row=0,column=9, padx=20)
        btnCerrar.pack(side = LEFT, padx=2, pady=2)


        #subtitulo
        toolbar2 = Label(self.QueryTool2, bg="LightSteelBlue")
        toolbar2.pack(side=TOP, fill = X)

        tituloQuery = StringVar()
        tituloQuery.set("Query Editor")
        barrita = Label(toolbar2, textvar=tituloQuery, justify = 'left', bg="LightSteelBlue", font=('arial',11))
        barrita.pack(side = "left")

        lista_numeros = Label(self.QueryTool2, bg = 'Silver', width = "3")
        lista_numeros.pack(side = LEFT, fill = Y)

        #text
        scroll = Scrollbar(self.QueryTool2)
        scroll.pack(side=RIGHT, fill = Y)
        texto = Text(self.QueryTool2)
        texto.pack(fill = BOTH, expand = True)
        texto.config(bd=0, padx=6, pady=4, bg="Beige", font=("Consolas", 12), yscrollcommand=scroll.set)
        scroll.config(command=texto.yview)


        # Consola
        self.ConsoleTool = LabelFrame(SubCuerpo, text='Consola')
        self.ConsoleTool.config(bg='white')
        self.ConsoleTool.pack(side=BOTTOM, fill=BOTH, expand = True)
        
        # Primera Configuracion de TextBox
        self.output = Text(self.ConsoleTool, pady = 1, padx = 1, state = 'normal', height = 12)
        self.output.pack(side=BOTTOM, fill=BOTH, expand = True)
        self.output.insert(INSERT, '''Error: Ha ocurrido un error
        > Este mensaje se mostrara cuando ocurra un error o cuando se deba mostrar el log
        > de alguna funcion de la base de datos o de la aplicacion     
        ''')
        self.output.tag_add('error', '1.0', '1.6')
        self.output.tag_config('error', foreground="red")
        self.output.config(state = 'disabled')
        
        
       

        # Ejecucion de la ventana
        self.raiz.mainloop()

    def f_switch_console_mode(self):
        self.consoleMode = not self.consoleMode

        if self.consoleMode:
            # De ser el valor True se mostrara la tabla con datos del query
            self.output.pack_forget()
            self.output = ttk.Treeview(self.ConsoleTool, columns = ('#1', '#2', '#3', '#4'))
            self.output.pack(side=BOTTOM, fill=BOTH, expand = True)
            self.output.heading('#1', text = 'Column1', anchor = CENTER)
            self.output.heading('#2', text = 'Column2', anchor = CENTER)
            self.output.heading('#3', text = 'Column3', anchor = CENTER)
            self.output.heading('#4', text = 'Column4', anchor = CENTER)
            self.output.insert('', 'end', text='index 1', values=("data 1", "data 2", "data 3", "data 4"))
        else:
            # de ser el valor False se mostrara un caja de texto con un mensaje
            self.output.pack_forget()
            self.output = Text(self.ConsoleTool, pady = 1, padx = 1, state = 'normal', height = 10)
            self.output.pack(side=BOTTOM, fill=BOTH, expand = True)
            self.output.insert(INSERT, '''Error: Ha ocurrido un error
            > Este mensaje se mostrara cuando ocurra un error o cuando se deba mostrar el log
            > de alguna funcion de la base de datos o de la aplicacion     
            ''')
            self.output.tag_add('error', '1.0', '1.6')
            self.output.tag_config('error', foreground="red")
            self.output.config(state = 'disabled')
        


    #abrir query tool
    def f_query_tool(self):
        self.QueryTool2.pack(side = TOP, fill = X)     
        self.QueryTool.pack_forget()
        """
        messagebox.showinfo(
            "Loading...", "DEBERA DEJAR EDITAR O MOSTRAR QUERY TOOL")
        """
    def f_guardar(self):
            messagebox.showinfo(
            "Loading...", "DEBERA GUARDAR LOS QUERYS")

    def f_log(self):
        self.log_screen = tk.Toplevel(self.raiz)
        self.log_screen.title("Login")
        self.log_screen.config(relief="sunken") 
        self.log_screen.config(bd=25)  
        ##self.log_screen.geometry("300x320")
        ancho_ventana = 900
        alto_ventana = 300

        x_ventana = self.log_screen.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.log_screen.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.log_screen.geometry(posicion)

        self.log_screen.resizable(0,0)
        Label(self.log_screen, text="Ingresar usuario y contraseña").pack()
        Label(self.log_screen, text="").pack()
        
        global usernameV
        global passwordV
    
        usernameV = StringVar()
        passwordV = StringVar()
    
    
        Label(self.log_screen, text="Username ").pack()
        self.username_entry = Entry(self.log_screen, textvariable=usernameV)
        self.username_entry.pack()
        Label(self.log_screen, text="").pack()
        Label(self.log_screen, text="Password ").pack()
        self.password_entry = Entry(self.log_screen, textvariable=passwordV, show= '*')
        self.password_entry.pack()
        Label(self.log_screen, text="").pack()
        Button(self.log_screen, text="Login", width=10, height=1, command=self.login_verification).pack()
        self.raiz.iconify()

    def login_verification(self):
        #print(usernameV.get())
        user = usernameV.get()
        password = passwordV.get()

        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

        if user == "admin" and password == "123":
            print("entro")
            messagebox.showinfo(
            "Loading...", "DATOS CORRECTOS ")
            self.log_screen.destroy()
            self.raiz.deiconify()
        else:
            messagebox.showinfo(
            "Loading...", "DATOS INCORRECTOS")

    def f_buscar(self):
    
        messagebox.showinfo(
            "Loading...", "DEBERA BUSCAR DENTRO DEL QUERY")

    def f_compilar(self):
        
        messagebox.showinfo(
            "Loading...", "DEBERA COMPILAR EL SCRIPT ACTUAL")

    def f_cargar(self):

        messagebox.showinfo(
            "Loading...", "DEBERA CARGAR QUERY")

    def f_eliminar(self):
    
        messagebox.showinfo(
            "Loading...", "DEBERA ELIMINAR QUERY ACTUAL")

    #cerrar query tool
    def f_cerrar_query_tool(self):
        self.QueryTool2.pack_forget()
        self.QueryTool.pack(side = TOP, fill = X) 

    def f_conectar(self):
        print("Conectando")

    def f_cambiaropc(self):
        self.objectMenu.entryconfig("Guardar", state="normal")

    def f_verestado(self):

        if self.estado.get() == 0:
            self.barraest.pack_forget()
        else:
            self.barraest.pack(side=BOTTOM, fill=X)

    def f_web(self):
        tytus = 'https://github.com/tytusdb/tytus'
        webbrowser.open_new_tab(tytus)

    def f_integrantes(self):
        messagebox.showinfo("INTEGRANTES", "BRANDON ALEXANDER VARGAS SARPEC     201709343\nALDO RIGOBERTO HERNÁNDEZ AVILA         201800585\nKEVIN ESTUARDO CARDONA LÓPEZ            201800596\nSERGIO FERNANDO MARTÍNEZ CABRERA   201801442\n")

    def f_acerca(self):
        acerca = Toplevel()
        acerca.geometry("320x200")
        acerca.resizable(width=False, height=False)
        acerca.title("Acerca de")
        marco1 = ttk.Frame(acerca, padding=(10, 10, 10, 10), relief=RAISED)
        marco1.pack(side=TOP, fill=BOTH, expand=True)
        etiq1 = Label(marco1, image=self.CONNECT_ICON, relief='raised')
        etiq1.pack(side=TOP, padx=10, pady=10, ipadx=10, ipady=10)
        etiq2 = Label(marco1, text="PyRemoto "+ __version__,
                      foreground='blue', font=self.fuente)
        etiq2.pack(side=TOP, padx=10)
        etiq3 = Label(marco1, text="Python para impacientes")
        etiq3.pack(side=TOP, padx=10)
        boton1 = Button(marco1, text="Salir", command=acerca.destroy)
        boton1.pack(side=TOP, padx=10, pady=10)
        boton1.focus_set()
        acerca.transient(self.raiz)
        self.raiz.wait_window(acerca)

    def f_salir(self):
        print("connection close")
        serv.close()
        self.raiz.destroy()


def f_verificar_iconos(iconos):
    for icono in iconos:
        if not os.path.exists(icono):
            print('Icono no encontrado:', icono)
            return(1)
    return(0)


def main():
    ruta_relativa = os.getcwd()
    ruta_r = ruta_relativa + os.sep + "imagen" + os.sep

    iconos = (ruta_r + "pyremoto64x64.png",
              ruta_r + "conec16x16.png",
              ruta_r + "salir16x16.png",
              ruta_r + "star16x16.png",
              ruta_r + "conec32x32.png",
              ruta_r + "salir32x32.png",
              ruta_r + "grupo32x32.png",
              ruta_r + "tytusdb.png",
              ruta_r + "open.png",
              ruta_r + "save.png",
              ruta_r + "serv.png",
              ruta_r + "bd.png",
              ruta_r + "tb.png",
              ruta_r + "col.png",
              ruta_r + "console.png",
              ruta_r + "Tbasedatos.png",
              ruta_r + "Tcarpeta.png",
              ruta_r + "Tguardar.png",
              ruta_r + "Tbuscar.png",
              ruta_r + "Tbasura.png",
              ruta_r + "Tcompilar.png",
              ruta_r + "Texplicar.png",
              ruta_r + "Tdescargar.png",
              ruta_r + "Tcerrar.png",
              ruta_r + "log.png"
              )

    error1 = f_verificar_iconos(iconos)

    if not error1:
        mi_app = cliente(ruta_r, iconos)
    return(0)


if __name__ == '__main__':
    main()
