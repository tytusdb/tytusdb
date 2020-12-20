import tkinter as tk
from tkinter import Tk, Text, BOTH, W, N, E, S, Menu,ttk,messagebox
from tkinter import filedialog
from tkinter.ttk import Frame, Button, Label, Style, Treeview
import os


class Example(Frame):
    contadorQuerysTabs = 1
    def __init__(self):

        super().__init__()
        #self contador numero tab querys

        #Creacion de ventana
        self.master.title("TytusDB")
        self.pack(fill=BOTH, expand=True)


        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        self.lbl = Label(self, text="TytusDB")
        self.lbl.grid(sticky=W, pady=4, padx=5)


        self.nb = CustomNotebook(self)
        self.fm = Frame(self.nb)
        self.fm.pack(fill=BOTH, expand=True)
        self.fm.columnconfigure(1, weight=1)
        self.fm.columnconfigure(3, pad=7)
        self.fm.rowconfigure(3, weight=1)
        self.fm.rowconfigure(5, pad=7)
        self.nb.add(self.fm, text='Query '+str(self.contadorQuerysTabs))
        self.nb.grid(row=1, column=1, columnspan=2, rowspan=4,
                       padx=5, sticky=E + W + S + N)
        self.area = Text(self.fm)
        self.area.grid(row=1, column=1, columnspan=2, rowspan=4,
                       padx=5, sticky=E + W + S + N)

        # *************************** BARRA DE MENÚ ***************************
        menubar = Menu(self.master)
        self.master.filemenu = Menu(menubar, tearoff=0)
        self.master.filemenu.add_command(label="Nuevo")
        self.master.filemenu.add_command(label="Abrir",command=self.openFile)
        self.master.filemenu.add_command(label="Guardar", command=self.saveFile)
        self.master.filemenu.add_command(label="Salir", command=self.master.quit)
        self.master.helpmenu = Menu(menubar, tearoff=0)
        self.master.helpmenu.add_command(label="Documentación")
        self.master.helpmenu.add_command(label="Acerca de...")
        self.master.servermenu = Menu(menubar, tearoff=0)
        self.master.servermenu.add_command(label="Nueva conexión")
        self.master.servermenu.add_command(label="Quitar conexión")
        self.master.herramientasMenu = Menu(menubar, tearoff=0)
        self.master.herramientasMenu.add_command(label="Query Tool", command=self.addQueryTool)
        self.master.herramientasMenu.add_command(label="run", command=self.run)
        menubar.add_cascade(label="Archivo", menu=self.master.filemenu)
        menubar.add_cascade(label="Servidor", menu=self.master.servermenu)
        menubar.add_cascade(label="Herramientas", menu=self.master.herramientasMenu)
        menubar.add_cascade(label="Ayuda", menu=self.master.helpmenu)
        self.master.config(menu=menubar);
        # *********************************************************************
        
        # ******************************* ÁRBOL *******************************
        self.treeview = Treeview(self)    
        self.treeview.grid(row=1, column=0, rowspan=4, sticky=E + W + S + N);                       
        servers = self.treeview.insert("", tk.END, text="Servidores")
        srvr1 = self.treeview.insert(servers, tk.END, text="server_vd2020")
        dbs = self.treeview.insert(srvr1, tk.END, text="Databases")
        dvdrental = self.treeview.insert(dbs, tk.END, text="dvdrental")
        funcdvdrental = self.treeview.insert(dvdrental, tk.END, text="Functions")
        tabldvdrental = self.treeview.insert(dvdrental, tk.END, text="Tables")
        triggersdvdrental = self.treeview.insert(dvdrental, tk.END, text="Trigger Functions")
        viewsdvdrental = self.treeview.insert(dvdrental, tk.END, text="Views")
        sports = self.treeview.insert(dbs, tk.END, text="sports")
        funcsports = self.treeview.insert(sports, tk.END, text="Functions")
        tablsport = self.treeview.insert(sports, tk.END, text="Tables")
        triggersport = self.treeview.insert(sports, tk.END, text="Trigger Functions")
        viewsport = self.treeview.insert(sports, tk.END, text="Views")
        logingrp = self.treeview.insert(srvr1, tk.END, text="Login/Group Roles")
        usr1 = self.treeview.insert(logingrp, tk.END, text="user1")
        usr2 = self.treeview.insert(logingrp, tk.END, text="user2")
        usr3 = self.treeview.insert(logingrp, tk.END, text="user3")
        usr4 = self.treeview.insert(logingrp, tk.END, text="user4")
        # *********************************************************************



        # *********************************************************************

    #Metodo agregar QueryTool
    def addQueryTool( self ):
        self.contadorQuerysTabs = self.contadorQuerysTabs+1
        self.nb.fm = Frame(self.nb)
        self.nb.fm.pack(fill=BOTH, expand=True)
        self.nb.fm.columnconfigure(1, weight=1)
        self.nb.fm.columnconfigure(3, pad=7)
        self.nb.fm.rowconfigure(3, weight=1)
        self.nb.fm.rowconfigure(5, pad=7)
        self.nb.add(self.nb.fm, text='Query '+str(self.contadorQuerysTabs))
        self.nb.grid(row=1, column=0, columnspan=2, rowspan=4,
                     padx=5, sticky=E + W + S + N)
        self.nb.fm.area = Text(self.nb.fm)
        self.nb.fm.area.grid(row=1, column=0, columnspan=2, rowspan=4,
                       padx=5, sticky=E + W + S + N)
        #self.lbl.configure(text="Cambia")

    def run(self):
        active_object = self.nb.nametowidget(self.nb.select())
        messagebox.showinfo("Info",active_object.area.get("1.0",'end-1c'))
        #print(self.nb.index(self.nb.select()))
        #print(self.nb.tab(self.nb.select(), "text"))

    def saveFile( self ):

        f = filedialog.asksaveasfile(initialdir="/", title="Select file",
                                     mode='w', defaultextension=".sql")
        if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        active_object = self.nb.nametowidget(self.nb.select())
        text2save = str(active_object.area.get("1.0", 'end-1c'))  # starts from `1.0`, not `0.0`
        self.nb.tab(self.nb.select(), text=os.path.basename(f.name))
        f.write(text2save)
        f.close()

    def openFile( self ):
        filename = filedialog.askopenfilename(initialdir="/", title="Select a File")
        with open(filename, "r") as f:
            self.contadorQuerysTabs = self.contadorQuerysTabs + 1
            self.nb.fm = Frame(self.nb)
            self.nb.fm.pack(fill=BOTH, expand=True)
            self.nb.fm.columnconfigure(1, weight=1)
            self.nb.fm.columnconfigure(3, pad=7)
            self.nb.fm.rowconfigure(3, weight=1)
            self.nb.fm.rowconfigure(5, pad=7)
            self.nb.add(self.nb.fm, text=os.path.basename(filename))
            self.nb.grid(row=1, column=0, columnspan=2, rowspan=4,
                         padx=5, sticky=E + W + S + N)
            self.nb.fm.area = Text(self.nb.fm)
            self.nb.fm.area.insert(1.0, f.read())
            self.nb.fm.area.grid(row=1, column=0, columnspan=2, rowspan=4,
                                 padx=5, sticky=E + W + S + N)


#Metodo para crear Tabs con la x para cerrar
class CustomNotebook(ttk.Notebook):
    """A ttk Notebook with close buttons on each tab"""

    __initialized = False
    def __init__(self, *args, **kwargs):
        if not self.__initialized:
            self.__initialize_custom_style()
            self.__inititialized = True

        kwargs["style"] = "CustomNotebook"
        ttk.Notebook.__init__(self, *args, **kwargs)

        self._active = None

        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)

    def on_close_press(self, event):
        """Called when the button is pressed over the close button"""

        element = self.identify(event.x, event.y)

        if "close" in element:
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
            self._active = index


    def on_close_release(self, event):
        """Called when the button is released over the close button"""
        if not self.instate(['pressed']):
            return

        element =  self.identify(event.x, event.y)
        index = self.index("@%d,%d" % (event.x, event.y))

        if "close" in element and self._active == index:
            self.forget(index)
            self.event_generate("<<NotebookTabClosed>>")

        self.state(["!pressed"])
        self._active = None

    def __initialize_custom_style(self):
        style = ttk.Style()
        self.images = (
            tk.PhotoImage("img_close", data='''
                R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
                '''),
            tk.PhotoImage("img_closeactive", data='''
                R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                '''),
            tk.PhotoImage("img_closepressed", data='''
                R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
            ''')
        )

        style.element_create("close", "image", "img_close",
                            ("active", "pressed", "!disabled", "img_closepressed"),
                            ("active", "!disabled", "img_closeactive"), border=8, sticky='')
        style.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})])
        style.layout("CustomNotebook.Tab", [
            ("CustomNotebook.tab", {
                "sticky": "nswe",
                "children": [
                    ("CustomNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("CustomNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                                    ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                                ]
                        })
                    ]
                })
            ]
        })
    ])

def main():
    root = Tk()
    app = Example()
    root.geometry("350x300+300+300")
    root.mainloop()

    # *************************** BARRA DE MENÚ ***************************    
    '''menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Nuevo")
    filemenu.add_command(label="Abrir")
    filemenu.add_command(label="Salir", command=root.quit)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Documentación")
    helpmenu.add_command(label="Acerca de...")
    servermenu = Menu(menubar, tearoff=0)
    servermenu.add_command(label="Nueva conexión")
    servermenu.add_command(label="Quitar conexión")
    menubar.add_cascade(label="Archivo", menu=filemenu)
    menubar.add_cascade(label="Servidor", menu=servermenu)
    menubar.add_cascade(label="Ayuda", menu=helpmenu)
    root.config(menu=menubar)'''
    # *********************************************************************



if __name__ == '__main__':
    main()