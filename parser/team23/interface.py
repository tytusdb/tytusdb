from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

import grammar.sql_grammar as gramatica
from graphviz import Source
from tools.console_text import *
from error.errores import *
from tools.tabla_simbolos import *

import os

class window:
    def __init__(self):
        #Variables 
        self.ventana = Tk() #Ventana
        self.color = "darkgray" #Color editor
        self.dir_os = os.path.dirname(__file__) #Dir 
        self.count_tabs = 1 #Conteo de tabs
        self.tabControl = ttk.Notebook(self.ventana,height=500) #Notebook contenedor tabs
        self.tab_salida = ttk.Notebook(self.ventana, height=100) #Notebook contenedor de salidas     
        self.my_status = StringVar()

        #Configuracion ventana
        self.ventana.title("Interfaz para compiladores")
        self.ventana.geometry("900x700")
        self.ventana.config(bg=self.color)

        #Creando widgets
        self.create_menu_bar()
        self.create_tool_bar()
        self.add_tab("Untitled-"+str(self.count_tabs))
        self.create_consola()
        self.create_status_bar()

        #Search and Replace vars
        self.search_text = ""
        self.replace_text = ""
       
    #Ejecución de la ventana
    def run(self):
        self.ventana.mainloop()
    
    #Widgets de la interfaz
    def create_menu_bar(self):
        my_menu = Menu(self.ventana)
        self.ventana.config(menu = my_menu)

        #Items del menu
        file_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="File", menu=file_menu)

        edit_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Edit", menu=edit_menu)

        tools_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Tools", menu=tools_menu)

        options_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Options", menu=options_menu)

        help_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Help", menu=help_menu)

        #Items de submenu
        file_menu.add_command(label="New File", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_separator()
        file_menu.add_command(label="Open File", command=self.open_file , accelerator="Ctrl+O")
        file_menu.add_separator()
        file_menu.add_command(label="Save File", command=self.save_file, accelerator="Ctrl+Shift-S")
        file_menu.add_command(label="Save As", command=self.save_as, accelerator="Ctrl+S")
        file_menu.add_separator()
        file_menu.add_command(label="Close Tab", command=self.delete_tab, accelerator="Ctrl+W")
        file_menu.add_command(label="Exit", command=self.ventana.quit)

        edit_menu.add_command(label="Copy", command=lambda:self.ventana.focus_get().event_generate('<<Copy>>'))
        edit_menu.add_command(label="Paste", command=lambda:self.ventana.focus_get().event_generate('<<Paste>>'))
        edit_menu.add_command(label="Cut", command=lambda:self.ventana.focus_get().event_generate('<<Cut>>'))
        edit_menu.add_separator()
        edit_menu.add_command(label="Search", command=self.find_popup, accelerator="Ctrl+F")
        edit_menu.add_command(label="Replace", command=self.replace_popup, accelerator="Ctrl+H")

        tools_menu.add_command(label="Ejecutar", command=self.ejecutar_codigo, accelerator="F5")
        tools_menu.add_separator()
        tools_menu.add_command(label="AST", command = self.compilar_AST_pdf)
        tools_menu.add_separator()
        tools_menu.add_command(label = "Errores Lexicos", command = self.compilar_lexico_pdf)
        tools_menu.add_command(label = "Errores Sintacticos", command = self.compilar_sintactico_pdf)
        tools_menu.add_command(label = "Errores Semanticos", command = self.compilar_semantico_pdf)
        tools_menu.add_command(label = "Todos los errores", command = self.compilar_Error_pdf)
        tools_menu.add_separator()
        tools_menu.add_command(label = "Reporte Gramatical", command = self.compilar_grammar_pdf)
        tools_menu.add_separator()
        tools_menu.add_command(label = "Tabla de Simbolos", command=self.compilar_ts_pdf)
        #tools_menu.add_command(label="Debug", command=self.open_file, accelerator="F5")

        theme_menu = Menu(options_menu, tearoff=0)
        options_menu.add_cascade(label="Theme", menu=theme_menu)
        #options_menu.add_command(label="Line Number", command=self.open_file)

        theme_menu.add_command(label="Default", command=self.default_theme)
        theme_menu.add_command(label="Light Gray", command=self.gray_theme)
        theme_menu.add_command(label="Dark Night", command=self.dark_night_theme)
        theme_menu.add_command(label="Light Blue", command=self.light_blue_theme)
        theme_menu.add_command(label="Dark", command=self.dark_theme)

        help_menu.add_command(label="Help")
        help_menu.add_command(label="About", command=self.popup_about)

    def popup_about(self):        
        popup = Tk()
        popup.wm_title("About")
        popup.geometry("330x190")
        popup.resizable(False, False)

        label = ttk.Label(popup, text="------------------ EDITOR COMPILADORES 2 ------------------", relief="sunken")
        label.pack(side="top", fill="x", pady=3)
        label = ttk.Label(popup, text="Versión: 1.51.1 (system setup)")
        label.pack(side="top", fill="x", pady=3)
        label = ttk.Label(popup, text="Confirmación: -----------------------------------")
        label.pack(side="top", fill="x", pady=3)
        label = ttk.Label(popup, text="Fecha: 2020-12-10T08:44:32")
        label.pack(side="top", fill="x", pady=3)
        label = ttk.Label(popup, text="Sistema Operativo: Windows_NT x64 10.0.18363")
        label.pack(side="top", fill="x", pady=3)
        label = ttk.Label(popup, text="Developer: Luis Fernando Arana Arias - 201700988\nPedro Rolando Ordoñez Carrillo - 201701187\nSteven Aaron Sis Hernandez - 201706357\nDavis Francisco Edward Enriquez - 201700972")
        label.pack(side="top", fill="x", pady=3)

        B1 = ttk.Button(popup, text="Close", command = popup.destroy)
        B1.pack()
        popup.mainloop()

    def pop_alert(self, msg):
        gui = Tk()
        gui.title("Alerta")
        gui.geometry("230x60") 
        gui.resizable(False,False)

        label = ttk.Label(gui, text=msg)
        label.pack(side="top", fill="x", pady=3)

        B1 = ttk.Button(gui, text="Close", command = gui.destroy)
        B1.pack()

        gui.mainloop()

    def find_popup(self):
        popup = Tk()
        popup.title("Buscar")
        popup.geometry("250x30")
        popup.resizable(False, False)
        
        Label(popup, text="> ").pack(side=LEFT)

        txtbox = Entry(popup)
        txtbox.pack(side = LEFT, fill = BOTH, expand = 1, pady=2)  
        txtbox.focus_set()  

        Find = Button(popup, text ='Buscar') 
        Find.pack(side = LEFT)          

        def find_func():
            tab_list = self.tabControl.winfo_children()
            current_tab = tab_list[self.tabControl.index(CURRENT)]

            txt_box = None                 
            for widget_item in current_tab.winfo_children():                
                if isinstance(widget_item, Text):
                    txt_box = widget_item

            text = txtbox.get()
            txt_box.tag_remove('found', '1.0', END) 

            if (text):  
                idx = '1.0'
                
                while 1:  
                    idx = txt_box.search(text, idx, nocase = 1, stopindex = END)               
                    if not idx: break
                    lastidx = '% s+% dc' % (idx, len(text)) 
                    txt_box.tag_add('found', idx, lastidx)
                    idx = lastidx  

                txt_box.tag_config('found', foreground='red', background ='#CACACA')  

        Find.config(command = find_func) 
            

    def replace_popup(self):
        popup = Tk()
        popup.title("Buscar y Remplazar")
        popup.geometry("350x30")
        popup.resizable(False, False)
        
        Label(popup, text="> ").pack(side=LEFT)

        txtbox = Entry(popup)
        txtbox.pack(side = LEFT, fill = BOTH, expand = 1, pady=2)  
        txtbox.focus_set()  

        Label(popup, text="> ").pack(side=LEFT)

        txtbox2 = Entry(popup)
        txtbox2.pack(side = LEFT, fill = BOTH, expand = 1, pady=2)  
        txtbox2.focus_set()  

        Replace = Button(popup, text ='Remplazar') 
        Replace.pack(side = LEFT)  

        def replace_func():     
            tab_list = self.tabControl.winfo_children()
            current_tab = tab_list[self.tabControl.index(CURRENT)]

            txt_box = None                 
            for widget_item in current_tab.winfo_children():                
                if isinstance(widget_item, Text):
                    txt_box = widget_item

            text_find = txtbox.get()
            text_replace = txtbox2.get()
            txt_box.tag_remove('found', '1.0', END)  
            
            if (text_find):  
                idx = '1.0'

                while 1:  
                    idx = txt_box.search(text_find, idx, nocase = 1, stopindex = END) 

                    if not idx: break 
                    lastidx = '% s+% dc' % (idx, len(text_find)) 
        
                    txt_box.delete(idx, lastidx) 
                    txt_box.insert(idx, text_replace) 
        
                    lastidx = '% s+% dc' % (idx, len(text_replace)) 
                    txt_box.tag_add('found', idx, lastidx)  
                    idx = lastidx  
        
                txt_box.tag_config('found', foreground ='green', background = 'yellow') 

        Replace.config(command = replace_func)

    def create_tool_bar(self):
        #Barra de herramientas
        myTool = Frame(self.ventana)

        #Botones de la barra de herramientas
        imgOpen = Image.open(self.dir_os +'/assets/open.png')
        imgOpen = imgOpen.resize((20,20), Image.ANTIALIAS)
        imgOpen = ImageTk.PhotoImage(imgOpen)
        OpenBtn = Button(myTool, image=imgOpen, command=self.open_file)
        OpenBtn.image = imgOpen
        OpenBtn.pack(side=LEFT, padx=2, pady=2)

        imgFile = Image.open(self.dir_os +'/assets/file.png')
        imgFile = imgFile.resize((20, 20), Image.ANTIALIAS)
        imgFile = ImageTk.PhotoImage(imgFile)
        FileBtn = Button(myTool, image=imgFile, command=self.new_file)
        FileBtn.image = imgFile
        FileBtn.pack(side=LEFT, padx=2, pady=2)

        imgSave = Image.open(self.dir_os +'/assets/save.png')
        imgSave = imgSave.resize((20, 20), Image.ANTIALIAS)
        imgSave = ImageTk.PhotoImage(imgSave)
        SaveBtn = Button(myTool, image=imgSave, command=self.save_as)
        SaveBtn.image = imgSave
        SaveBtn.pack(side=LEFT, padx=2, pady=2)

        imgSearch = Image.open(self.dir_os +'/assets/search.png')
        imgSearch = imgSearch.resize((20, 20), Image.ANTIALIAS)
        imgSearch = ImageTk.PhotoImage(imgSearch)
        SearchBtn = Button(myTool, image=imgSearch, command=self.find_popup)
        SearchBtn.image = imgSearch
        SearchBtn.pack(side=LEFT, padx=2, pady=2)

        imgDebug = Image.open(self.dir_os +'/assets/debug.png')
        imgDebug = imgDebug.resize((20, 20), Image.ANTIALIAS)
        imgDebug = ImageTk.PhotoImage(imgDebug)
        DebugBtn = Button(myTool, image=imgDebug, command=self.open_file)
        DebugBtn.image = imgDebug
        DebugBtn.pack(side=RIGHT, padx=2, pady=2)

        imgExecute = Image.open(self.dir_os +'/assets/execute.png')
        imgExecute = imgExecute.resize((20, 20), Image.ANTIALIAS)
        imgExecute = ImageTk.PhotoImage(imgExecute)
        ExecuteBtn = Button(myTool, image=imgExecute, command=self.ejecutar_codigo)
        ExecuteBtn.image = imgExecute
        ExecuteBtn.pack(side=RIGHT, padx=2, pady=2)

        imgAbout = Image.open(self.dir_os +'/assets/about.png')
        imgAbout = imgAbout.resize((20, 20), Image.ANTIALIAS)
        imgAbout = ImageTk.PhotoImage(imgAbout)
        AboutBtn = Button(myTool, image=imgAbout, command=self.popup_about)
        AboutBtn.image = imgAbout
        AboutBtn.pack(side=LEFT, padx=2, pady=2)

        imgClose = Image.open(self.dir_os +'/assets/close.png')
        imgClose = imgClose.resize((20, 20), Image.ANTIALIAS)
        imgClose = ImageTk.PhotoImage(imgClose)
        CloseBtn = Button(myTool, image=imgClose, command=self.delete_tab)
        CloseBtn.image = imgClose
        CloseBtn.pack(side=LEFT, padx=2, pady=2)

        imgClear = Image.open(self.dir_os +'/assets/clear.png')
        imgClear = imgClear.resize((20, 20), Image.ANTIALIAS)
        imgClear = ImageTk.PhotoImage(imgClear)
        ClearBtn = Button(myTool, image=imgClear, command=self.clear_consola)
        ClearBtn.image = imgClear
        ClearBtn.pack(side=LEFT, padx=2, pady=2)

        imgAst = Image.open(self.dir_os +'/assets/ast.png')
        imgAst = imgAst.resize((20, 20), Image.ANTIALIAS)
        imgAst = ImageTk.PhotoImage(imgAst)
        AstBtn = Button(myTool, image=imgAst, command=self.compilar_AST_pdf)
        AstBtn.image = imgAst
        AstBtn.pack(side=LEFT, padx=2, pady=2)

        imgErrores = Image.open(self.dir_os +'/assets/error.png')
        imgErrores = imgErrores.resize((20, 20), Image.ANTIALIAS)
        imgErrores = ImageTk.PhotoImage(imgErrores)
        ErroresBtn = Button(myTool, image=imgErrores, command=self.compilar_Error_pdf)
        ErroresBtn.image = imgErrores
        ErroresBtn.pack(side=LEFT, padx=2, pady=2)

        imgGrammar = Image.open(self.dir_os +'/assets/grammar.png')
        imgGrammar = imgGrammar.resize((20, 20), Image.ANTIALIAS)
        imgGrammar = ImageTk.PhotoImage(imgGrammar)
        GrammarBtn = Button(myTool, image=imgGrammar, command=self.compilar_grammar_pdf)
        GrammarBtn.image = imgGrammar
        GrammarBtn.pack(side=LEFT, padx=2, pady=2)

        imgSimbolo = Image.open(self.dir_os +'/assets/simbolos.png')
        imgSimbolo = imgSimbolo.resize((20, 20), Image.ANTIALIAS)
        imgSimbolo = ImageTk.PhotoImage(imgSimbolo)
        SimboloBtn = Button(myTool, image=imgSimbolo, command=self.compilar_ts_pdf)
        SimboloBtn.image = imgSimbolo
        SimboloBtn.pack(side=LEFT, padx=2, pady=2)

        myTool.pack(side=TOP, fill=X)

    def clear_consola(self):
        limpiar_consola()

        for tab_item in self.tab_salida.winfo_children():
            for widget_item in tab_item.winfo_children():                
                if isinstance(widget_item, Text):
                        widget_item.delete('1.0', END)            
                        widget_item.insert(INSERT, get_contenido())

    def create_consola(self):
        tab_consola = ttk.Frame(self.tab_salida)

        new_scroll = Scrollbar(tab_consola)

        font_spec = ("Consolas", 11)
        consola = Text(tab_consola, font=font_spec)
        consola.pack(side=LEFT, fill=BOTH, expand=TRUE)
        consola.config(yscrollcommand=new_scroll.set)
        
        consola.insert(INSERT, contenido_consola)
        
        new_scroll.pack(side=RIGHT, fill=Y)
        new_scroll.config(command=consola.yview)

        self.tab_salida.add(tab_consola, text="Consola")
        self.tab_salida.pack(side=TOP, fill=BOTH, expand=TRUE)

    def add_tab(self, title):         
        new_tab = ttk.Frame(self.tabControl)
        font_spec = ("Consolas", 11)  

        new_scroll = Scrollbar(new_tab)        
        txt_numbers = self.set_line_numbers(new_tab)  
        new_textarea = Text(new_tab, font=font_spec)        

        def double_scroll(self, *args):
            txt_numbers.yview_moveto(*args)
            new_textarea.yview_moveto(*args)
                
        new_scroll.config(command=double_scroll)  

        def update_scroll(first, last):  
            txt_numbers.yview_moveto(first)           

            new_scroll.set(first, last)
                                      
        txt_numbers.configure(yscrollcommand=update_scroll)                      
        new_textarea.configure(yscrollcommand=update_scroll)                      
        
        new_textarea.bind('<Return>', lambda event, txt_number=txt_numbers, txt_area=new_textarea: self.update_line_number(txt_number, new_textarea))        
        new_textarea.bind('<BackSpace>', lambda event, txt_number=txt_numbers, txt_area=new_textarea: self.update_line_number_back(txt_number, new_textarea))        
        new_textarea.bind('<Control-Return>', lambda event, txt_number=txt_numbers, txt_area=new_textarea: self.update_line_number_back(txt_number, new_textarea))        

        new_scroll.pack(side=RIGHT, fill=Y)
        new_textarea.pack(side=LEFT, fill=BOTH, expand=TRUE)

        self.update_line_number_back(txt_numbers, new_textarea)
        self.bind_shortcuts(new_textarea)                

        self.color_font_config(new_textarea)                      

        self.tabControl.add(new_tab, text=title)
        self.tabControl.select(self.count_tabs-1)
        self.tabControl.pack(side=TOP, fill=BOTH, expand=TRUE)

    def create_status_bar(self):        
        self.my_status.set("Editor - 0.1")
        font_spec = ("Consolas", 11)

        label = Label(self.ventana, textvariable=self.my_status, fg="black", bg="lightgrey", anchor="sw", font=font_spec)
        label.pack(side=BOTTOM, fill=BOTH)

    def set_line_numbers(self, tab_item):
        line_number = Text(tab_item, width=4)
        line_number.pack(side=LEFT, fill=Y)        
        
        font_spec = ("Consolas", 11)            
        line_number.config(font=font_spec)
        line_number.config(state=DISABLED)
        line_number.config(background="#BBBDCC")        

        return line_number

    #Funciones
    def open_file(self, *args):
        file_name = None
        file_name = filedialog.askopenfilename(
            defaultextension = ".txt",
            filetypes = [("All Files", "*.*"),
                        ("Text Files", "*.txt"),
                        ("Python Scripts", "*.py")])

        if file_name:
            index_tab = self.tab_libre()
            tab = None            

            if index_tab != -1:                
                self.tabControl.tab(index_tab, text=file_name)

                tabs_list = self.tabControl.winfo_children()
                tab = tabs_list[index_tab]  
                
                self.tabControl.select(index_tab)              
            else:                  
                self.count_tabs +=1               
                self.add_tab(file_name)
                
                tabs_list = self.tabControl.winfo_children()
                tab = tabs_list[self.count_tabs - 1]                

            txt_box = None                 
            widget_list = tab.winfo_children()
            for widget_item in widget_list:                
                if isinstance(widget_item, Text):
                    txt_box = widget_item

            with open(file_name, "r") as f:
                txt_box.insert("1.0", f.read())      

            self.update_line_number_back(widget_list[1], widget_list[2])
            self.color_font_config(widget_list[2])

    def new_file(self, *args):        
        self.count_tabs +=1     
        self.add_tab("Untitled-"+str(self.count_tabs))

    def tab_libre(self):      
        if self.count_tabs == 0:
            return -1

        tab_ideal = 0

        tabs_list = self.tabControl.winfo_children()
        for tab_item in tabs_list:            
            widget_list = tab_item.winfo_children()

            for widget_item in widget_list:
                if isinstance(widget_item, Text):
                    contenido_txt = widget_item.get("1.0",END)

                    if contenido_txt == "\n":                        
                        return tab_ideal

            tab_ideal += 1

        return -1

    def delete_tab(self, *args):   
        for item in self.tabControl.winfo_children():
            if str(item)==self.tabControl.select():
                item.destroy()       
                self.count_tabs -= 1
                return 

    def save_as(self, *args):
        try:           
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled-" + str(self.tabControl.index(CURRENT) + 1 ),
                defaultextension = ".txt",
                filetypes = [("All Files", "*.*"),
                            ("Text Files", "*.txt"),
                            ("Python Scripts", "*.py")])

            tab_list = self.tabControl.winfo_children()
            current_tab = tab_list[self.tabControl.index(CURRENT)]

            txt_box = None                 
            for widget_item in current_tab.winfo_children():                
                if isinstance(widget_item, Text):
                    txt_box = widget_item

            contenido = txt_box.get(1.0, END)
            with open(new_file, "w") as f:
                f.write(contenido)

            self.tabControl.tab(self.tabControl.index(CURRENT), text=new_file)
            self.update_status_bar(0)
        except Exception as er:
            print(er)   

    def save_file(self, *args):
        nombre_eval = "Untitled-" 
        actual_name = self.tabControl.tab(CURRENT, "text")
        nombre_aux = actual_name[:-1]

        if nombre_aux != nombre_eval:
            try:
                tab_list = self.tabControl.winfo_children()
                current_tab = tab_list[self.tabControl.index(CURRENT)]

                txt_box = None                 
                for widget_item in current_tab.winfo_children():                
                    if isinstance(widget_item, Text):
                        txt_box = widget_item

                contenido = txt_box.get(1.0, END)
                with open(actual_name, "w") as f:
                    f.write(contenido)

                self.update_status_bar(0)
            except Exception as er:
                print(er)
        else:
            self.save_as()        

    def update_status_bar(self, *args):           
        if args[0] == 0:
            self.my_status.set("Archivo Guardado con éxito")  
        else:
            self.my_status.set("Editor - 0.1")

    #Configuraciones
    def bind_shortcuts(self, text_edit):
        text_edit.bind('<Control-n>', self.new_file)
        text_edit.bind('<Control-o>', self.open_file)
        text_edit.bind('<Control-s>', self.save_file)
        text_edit.bind('<Control-S>', self.save_as)
        text_edit.bind('<Control-w>', self.delete_tab)
        text_edit.bind('<Key>', self.update_status_bar)                   
        text_edit.bind('<Key>', lambda event, txt_area=text_edit: self.color_font_config(text_edit)) 

    def update_line_number(self, txt_number, txt_area):
        txt_number.config(state=NORMAL)        
        txt_number.delete("1.0","end")
        lineas = int(txt_area.index('end').split('.')[0])        

        for i in range(1, lineas+1):
            line_print = str(i) + "\n"            
            txt_number.insert(INSERT, line_print)

        txt_number.config(state=DISABLED)

    def update_line_number_back(self, txt_number, txt_area):
        txt_number.config(state=NORMAL)        
        txt_number.delete("1.0","end")
        lineas = int(txt_area.index('end').split('.')[0]) -1        

        for i in range(1, lineas+1):
            line_print = str(i) + "\n"            
            txt_number.insert(INSERT, line_print)

        txt_number.config(state=DISABLED)
        
    def highlight_pattern(self, pattern, tag, txt_area, start="1.0", end="end", regexp=False, case_sensitive = 0):
        start = txt_area.index(start)
        end = txt_area.index(end)
        txt_area.mark_set("matchStart", start)
        txt_area.mark_set("matchEnd", start)
        txt_area.mark_set("searchLimit", end)

        count = IntVar()
        while True:
            index = txt_area.search(pattern, "matchEnd","searchLimit", count=count, regexp=regexp, nocase=case_sensitive)
            if index == "": break
            if count.get() == 0: break # degenerate pattern which matches zero-length strings
            txt_area.mark_set("matchStart", index)
            txt_area.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            txt_area.tag_add(tag, "matchStart", "matchEnd")

    def default_theme(self):
        for tab_item in self.tabControl.winfo_children():                
            conteo = 0
            for widget_item in tab_item.winfo_children():                
                if isinstance(widget_item, Text):
                    if conteo != 0:
                        widget_item.config(foreground="#000000")
                        widget_item.config(background="#FFFFFF")
                    conteo += 1
        
        for tab_item in self.tab_salida.winfo_children():
            for widget_item in tab_item.winfo_children():                
                if isinstance(widget_item, Text):
                        widget_item.config(foreground="#000000")
                        widget_item.config(background="#FFFFFF")

    def gray_theme(self):       
        for tab_item in self.tabControl.winfo_children():                
            conteo = 0
            for widget_item in tab_item.winfo_children():                
                if isinstance(widget_item, Text):
                    if conteo != 0:
                        widget_item.config(foreground="#000000")
                        widget_item.config(background="#BBBDCC")
                    conteo += 1

        for tab_item in self.tab_salida.winfo_children():
            for widget_item in tab_item.winfo_children():                
                if isinstance(widget_item, Text):
                        widget_item.config(foreground="#000000")
                        widget_item.config(background="#BBBDCC")

    def dark_night_theme(self):        
        for tab_item in self.tabControl.winfo_children():                
            conteo = 0
            for widget_item in tab_item.winfo_children():                
                if isinstance(widget_item, Text):
                    if conteo != 0:
                        widget_item.config(foreground="#FFFFFF")
                        widget_item.config(background="#252327")
                    conteo += 1

        for tab_item in self.tab_salida.winfo_children():
            for widget_item in tab_item.winfo_children():                
                if isinstance(widget_item, Text):
                        widget_item.config(foreground="#FFFFFF")
                        widget_item.config(background="#252327")

    def light_blue_theme(self):
        for tab_item in self.tabControl.winfo_children():
            conteo = 0                
            for widget_item in tab_item.winfo_children():
                if isinstance(widget_item, Text):
                    if conteo != 0:
                        widget_item.config(foreground="#000000")
                        widget_item.config(background="#4C57C8")
                    conteo += 1

        for tab_item in self.tab_salida.winfo_children():
            for widget_item in tab_item.winfo_children():                
                if isinstance(widget_item, Text):
                        widget_item.config(foreground="#000000")
                        widget_item.config(background="#4C57C8")

    def dark_theme(self):
        for tab_item in self.tabControl.winfo_children():    
            conteo = 0            
            for widget_item in tab_item.winfo_children():                
                if isinstance(widget_item, Text):
                    if conteo != 0:
                        widget_item.config(foreground="#FFFFFF")
                        widget_item.config(background="#2D163D")
                    conteo += 1

        for tab_item in self.tab_salida.winfo_children():
            for widget_item in tab_item.winfo_children():                
                if isinstance(widget_item, Text):
                        widget_item.config(foreground="#FFFFFF")
                        widget_item.config(background="#2D163D")

    def color_font_config(self, txt_area):
        #Colores 
        txt_area.tag_config("reservada", foreground="#A675B9")
        txt_area.tag_config("id", foreground="#759AF0")
        txt_area.tag_config("string", foreground="#7AC883")
        txt_area.tag_config("comentario", foreground="#9BA29C")
        txt_area.tag_config("item", foreground="#A675B9")
        txt_area.tag_config("important", foreground="#E7375C")
        txt_area.tag_config("function", foreground="#5182C9")
        txt_area.tag_config("boolean", foreground="#FA8C31")

        #Palabras
        self.highlight_pattern(r'/\*(.|\n)*?\*/', "comentario", txt_area, regexp=True)
        self.highlight_pattern(r'--.*\n', "comentario", txt_area, regexp=True)

        self.highlight_pattern("SELECT", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("UPDATE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("WHERE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("JOIN", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("CREATE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("DELETE", "reservada", txt_area, case_sensitive=1)        
        self.highlight_pattern("COUNT", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("SUM", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("FROM", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("CASE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("THEN", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("ELSE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("SMALLINT", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("INTEGER", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("BIGINT", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("DECIMAL", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("NUMERIC", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("REAL", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("MONEY", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("CHAR", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("CHARACTER", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("VARYING", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("TIMESTAMP", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("WITHOUT", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("WITH", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("TIME", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("ZONE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("DATE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("INTERVAL", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("FIELDS", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("YEAR", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("MONTH", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("DAY", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("HOUR", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("MINUTE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("SECOND", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("TO", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("BOOLEAN", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("AS", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("ENUM", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("TYPE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("IS", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("ISNULL", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("NOTNULL", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("NOT", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("AND", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("OR", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("BETWEEN", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("LIKE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("IN", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("INLIKE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("SIMILAR", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("REPLACE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("MODE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("OWNER", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("IF", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("EXISTS", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("ALTER", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("DATABASE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("RENAME", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("DROP", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("TABLE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("PRIMARY", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("FOREIGN", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("KEY", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("REFERENCES", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("CONSTRAINT", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("CHECK", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("SET", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("INSERT", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("BY", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("GROUP", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("HAVING", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("ORDER", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("WHEN", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("UNION", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("END", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("VALUES", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("INTERSECT", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("LIMIT", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("INNER", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("LEFT", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("RIGHT", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("OUTER", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("ASC", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("DESC", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("GREATEST", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("LEAST", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("OFFSET", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("FIRST", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("LAST", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("FULL", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("ALL", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("TRUE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("FALSE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("INHERITS", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("NULL", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("SHOW", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("DATABASES", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("USE", "reservada", txt_area, case_sensitive=1)
        self.highlight_pattern("VARCHAR", "reservada", txt_area, case_sensitive=1)

        self.highlight_pattern("==", "item", txt_area)
        self.highlight_pattern("!=", "item", txt_area)
        self.highlight_pattern(">=", "item", txt_area)
        self.highlight_pattern("<=", "item", txt_area)
        self.highlight_pattern(">", "item", txt_area)
        self.highlight_pattern("<", "item", txt_area)
        self.highlight_pattern("=", "item", txt_area)
        self.highlight_pattern("+", "item", txt_area)
        self.highlight_pattern("-", "item", txt_area)
        self.highlight_pattern("*", "item", txt_area)
        self.highlight_pattern("/", "item", txt_area)
        
        self.highlight_pattern("self", "important", txt_area)
        
        self.highlight_pattern("print", "function", txt_area)

        self.highlight_pattern("true", "boolean", txt_area)
        self.highlight_pattern("false", "boolean", txt_area)
        
        self.highlight_pattern(r'(\".*?\")|(\'.*?\')', "string", txt_area, regexp=True)

    def graficar_AST(self, ast_):
        if len(ast_) != 0:
            ast_str = 'digraph AST { \n node [shape=record];\n'

            count_nodos = 0
            for instruccion_ in ast_:
                if count_nodos != 0:                    
                    ast_str += 'node' + str(count_nodos + 1000000) + '[label =\" Instruccion \"];\n'
                    ast_str += 'node' + str(count_nodos + 10000) + '[label =\" Instrucciones \"];\n'

                    ast_str += 'node' + str(count_nodos + 10000 - 1) + ' -> node' + str(count_nodos + 1000000) + ';\n'
                    ast_str += 'node' + str(count_nodos + 10000 - 1) + ' -> node' + str(count_nodos + 10000) + ';\n'

                    ast_str += 'node' + str(count_nodos + 1000000) + ' -> node' + instruccion_.nodo.num + ';\n'
                    ast_str += 'node' + instruccion_.nodo.num + '[label =\"'+ instruccion_.nodo.valor +"\"];\n"
                    ast_str += self.graficar_AST_hijos(instruccion_.nodo)
                else:
                    ast_str += 'node' + instruccion_.nodo.num + '[label =\"'+ instruccion_.nodo.valor +"\"];\n"
                    ast_str += 'node' + str(count_nodos + 1000000) + '[label =\" Instruccion \"];\n'
                    ast_str += 'node' + str(count_nodos + 10000) + '[label =\" Instrucciones \"];\n'
                    ast_str += 'start_ast -> node' + str(count_nodos + 10000) + ';\n'
                    ast_str += 'start_ast -> node' + str(count_nodos + 1000000) + ';\n'
                    ast_str += 'node' + str(count_nodos + 1000000) + ' -> node' + instruccion_.nodo.num + ';\n'
                    ast_str += self.graficar_AST_hijos(instruccion_.nodo)
                count_nodos += 1
                
            ast_str += '\n}'

            with open('ast_reporte.dot', 'w', encoding='utf8') as f:
                f.write(ast_str)

    def graficar_AST_hijos(self, instr_):
        t = ''

        for instruc in instr_.hijos:
            t += 'node'+instruc.num+'[label=\"'+instruc.valor+'\"];\n'
            t += 'node'+instr_.num + ' -> node' + instruc.num+';\n'
            t += self.graficar_AST_hijos(instruc)

        return t

    def graficar_Gramatical(self, ast_):
        if len(ast_) != 0:
            grammar_str = 'digraph test {\ngraph [ratio=fill];\nnode [label=\"\\N\", fontsize=15, shape=plaintext];\ngraph [bb=\"0,0,352,154\"];\n'
            grammar_str += 'arset [label=<\n<TABLE ALIGN=\"LEFT\">\n<TR>\n<TD>PRODUCCIÓN</TD><TD>ACCIONES</TD></TR>\n'

            grammar_str += '<TR><TD>INSTRUCCIONES ::= INSTRUCCION INSTRUCCIONES1</TD><TD>INSTRUCCIONES = INSTRUCCIONES1; INSTRUCCIONES.append(INSTRUCCION); </TD></TR>\n'
            grammar_str += '<TR><TD>INSTRUCCIONES ::= </TD><TD>INSTRUCCIONES = [];</TD></TR>\n'

            for instr in ast_:
                grammar_str += instr.grammar_ + '\n'

            grammar_str += '</TABLE>\n>, ];\n}'

            with open('grammar_reporte.dot', 'w', encoding='utf8') as f:
                f.write(grammar_str)

    def graficar_Errores(self):        
        if len(errores) != 0:
            reporte_errores = "digraph test {\ngraph [ratio=fill];\nnode [label=\"\\N\", fontsize=15, shape=plaintext];\ngraph [bb=\"0,0,352,154\"];\n"
            reporte_errores += "arset [label=<\n<TABLE ALIGN=\"LEFT\">\n<TR>\n<TD>Tipo Error</TD>\n<TD>Descripcion</TD>\n<TD>Linea</TD>\n<TD>Columna</TD>\n</TR>\n"

            for error_ in errores:
                reporte_errores += '<TR>'
                reporte_errores += '<TD>' + error_.descripcion + '</TD>'
                reporte_errores += '<TD>' + error_.valor +'</TD>'
                reporte_errores += '<TD>' + error_.line +'</TD>'
                reporte_errores += '<TD>' + error_.column +'</TD>'
                reporte_errores += '</TR>\n'

            reporte_errores += '</TABLE>\n>, ];\n}'

            with open('errores_reporte.dot', 'w', encoding='utf8') as f:
                f.write(reporte_errores)

    def graficar_errores_lexicos(self):
        if len(errores) != 0:
            reporte_errores = "digraph test {\ngraph [ratio=fill];\nnode [label=\"\\N\", fontsize=15, shape=plaintext];\ngraph [bb=\"0,0,352,154\"];\n"
            reporte_errores += "arset [label=<\n<TABLE ALIGN=\"LEFT\">\n<TR>\n<TD>Tipo Error</TD>\n<TD>Descripcion</TD>\n<TD>Linea</TD>\n<TD>Columna</TD>\n</TR>\n"

            for error_ in errores:
                if error_.descripcion.lower() == "léxico":
                    reporte_errores += '<TR>'
                    reporte_errores += '<TD>' + error_.descripcion + '</TD>'
                    reporte_errores += '<TD>' + error_.valor +'</TD>'
                    reporte_errores += '<TD>' + error_.line +'</TD>'
                    reporte_errores += '<TD>' + error_.column +'</TD>'
                    reporte_errores += '</TR>'

            reporte_errores += '</TABLE>\n>, ];\n}'

            with open('lexico_reporte.dot', 'w', encoding='utf8') as f:
                f.write(reporte_errores)

    def graficar_errores_sintacticos(self):
        if len(errores) != 0:
            reporte_errores = "digraph test {\ngraph [ratio=fill];\nnode [label=\"\\N\", fontsize=15, shape=plaintext];\ngraph [bb=\"0,0,352,154\"];\n"
            reporte_errores += "arset [label=<\n<TABLE ALIGN=\"LEFT\">\n<TR>\n<TD>Tipo Error</TD>\n<TD>Descripcion</TD>\n<TD>Linea</TD>\n<TD>Columna</TD>\n</TR>\n"

            for error_ in errores:
                if error_.descripcion.lower() == "sintáctico":
                    reporte_errores += '<TR>'
                    reporte_errores += '<TD>' + error_.descripcion + '</TD>'
                    reporte_errores += '<TD>' + error_.valor +'</TD>'
                    reporte_errores += '<TD>' + error_.line +'</TD>'
                    reporte_errores += '<TD>' + error_.column +'</TD>'
                    reporte_errores += '</TR>'

            reporte_errores += '</TABLE>\n>, ];\n}'

            with open('sintactico_reporte.dot', 'w', encoding='utf8') as f:
                f.write(reporte_errores)

    def graficar_errores_semanticos(self):
        if len(errores) != 0:
            reporte_errores = "digraph test {\ngraph [ratio=fill];\nnode [label=\"\\N\", fontsize=15, shape=plaintext];\ngraph [bb=\"0,0,352,154\"];\n"
            reporte_errores += "arset [label=<\n<TABLE ALIGN=\"LEFT\">\n<TR>\n<TD>Tipo Error</TD>\n<TD>Descripcion</TD>\n<TD>Linea</TD>\n<TD>Columna</TD>\n</TR>\n"

            for error_ in errores:
                if error_.descripcion.lower() == "semántico":
                    reporte_errores += '<TR>'
                    reporte_errores += '<TD>' + error_.descripcion + '</TD>'
                    reporte_errores += '<TD>' + error_.valor +'</TD>'
                    reporte_errores += '<TD>' + error_.line +'</TD>'
                    reporte_errores += '<TD>' + error_.column +'</TD>'
                    reporte_errores += '</TR>'

            reporte_errores += '</TABLE>\n>, ];\n}'

            with open('semantico_reporte.dot', 'w', encoding='utf8') as f:
                f.write(reporte_errores)

    def graficar_TS(self):
        reporte_ts = ts.reporte_ts()

        with open('ts_reporte.dot', 'w', encoding='utf8') as f:
            f.write(reporte_ts)

    def compilar_ts_png(self):
        img = Source.from_file("ts_reporte.dot", format = "png", encoding="utf8")
        img.render()
        entrada = self.popup_reporte_png(self.ventana, "ts_reporte.dot.png")

    def compilar_ts_pdf(self):
        file_pdf = Source.from_file("ts_reporte.dot", format = "pdf", encoding="utf8")
        file_pdf.view()

    def compilar_grammar_png(self):
        img = Source.from_file("grammar_reporte.dot", format = "png", encoding="utf8")
        img.render()
        entrada = self.popup_reporte_png(self.ventana, "grammar_reporte.dot.png")

    def compilar_grammar_pdf(self):
        file_pdf = Source.from_file("grammar_reporte.dot", format = "pdf", encoding="utf8")
        file_pdf.view()

    def compilar_semantico_png(self):
        img = Source.from_file("semantico_reporte.dot", format = "png", encoding='utf8')
        img.render()
        entrada = self.popup_reporte_png(self.ventana, "semantico_reporte.dot.png")

    def compilar_semantico_pdf(self):
        file_pdf = Source.from_file("semantico_reporte.dot", format = "pdf", encoding='utf8')
        file_pdf.view()

    def compilar_sintactico_png(self):
        img = Source.from_file("sintactico_reporte.dot", format = "png", encoding='utf8')
        img.render()
        entrada = self.popup_reporte_png(self.ventana, "sintactico_reporte.dot.png")

    def compilar_sintactico_pdf(self):
        file_pdf = Source.from_file("sintactico_reporte.dot", format = "pdf", encoding='utf8')
        file_pdf.view()

    def compilar_lexico_png(self):
        img = Source.from_file("lexico_reporte.dot", format = "png", encoding='utf8')
        img.render()
        entrada = self.popup_reporte_png(self.ventana, "lexico_reporte.dot.png")
    
    def compilar_lexico_pdf(self):
        file_pdf = Source.from_file("lexico_reporte.dot", format = "pdf", encoding='utf8')
        file_pdf.view()

    def compilar_Error_png(self):
        img = Source.from_file("errores_reporte.dot", format="png", encoding='utf8')
        img.render()
        entrada = self.popup_reporte_png(self.ventana, "errores_reporte.dot.png")

    def compilar_Error_pdf(self):
        file_pdf = Source.from_file("errores_reporte.dot", format="pdf", encoding='utf8')
        file_pdf.view()

    def compilar_AST_png(self):
        img = Source.from_file("ast_reporte.dot", format="png", encoding='utf8')
        img.render()
        entrada = self.popup_reporte_png(self.ventana, "ast_reporte.dot.png")

    def compilar_AST_pdf(self):
        file_pdf = Source.from_file("ast_reporte.dot", format="pdf", encoding='utf8')
        file_pdf.view()

    def popup_reporte_png(self, master, path):
        top = self.top = Toplevel(master) 
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(top, image = img)
        panel.image = img
        panel.pack(side = "bottom", fill = "both", expand = "yes")

    def ejecutar_codigo(self):
        errores = []
        
        tab_list = self.tabControl.winfo_children()
        current_tab = tab_list[self.tabControl.index(CURRENT)]

        txt_box = None                 
        for widget_item in current_tab.winfo_children():                
            if isinstance(widget_item, Text):
                txt_box = widget_item

        contenido = txt_box.get(1.0, END)

        instruccions = []

        try:
            instruccions = gramatica.parse(contenido)
            self.ejecutar_resultado(instruccions)
        except:
            if len(contenido) == 1:
                add_text("No hay código para ejecutar")
            else:
                add_text("Error al ejecutar el código")

        #Imprimir consola
        for tab_item in self.tab_salida.winfo_children():
            for widget_item in tab_item.winfo_children():                
                if isinstance(widget_item, Text):
                        widget_item.delete('1.0', END)                                                   
                        add_text("\nPS C:\\Users\\Grupo 23> ")
                        widget_item.insert(INSERT, get_contenido())                             


        self.graficar_AST(instruccions)  
        self.graficar_Errores()
        self.graficar_errores_lexicos()
        self.graficar_errores_sintacticos()
        self.graficar_errores_semanticos()
        self.graficar_Gramatical(instruccions)
        self.graficar_TS()
    
    def ejecutar_resultado(self,instrucciones_):
        for instruccion_ in instrucciones_:
            instruccion_.ejecutar()

if __name__ == "__main__":
    index = window()
    index.run()

    