#imports
import os
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import webbrowser
import Gramatica #importar el modulo de la gramatica 
import AST

archivo = None

# Configuración de Ventana
ventana = Tk()
ventana.geometry('800x600')
ventana.title("TytusDB_18")


# show pop-up menu

def abrirAST():
    AST.generarAST()

def abrirGramaticalASC():
    AST.generarGASC()

def abrirEstructuraTablas():
    #crear ventana
    win=Tk()
    win.title("Tabla de Simbolos")
    win.geometry('900x600')
    #crear Scrol
    scroll_Derecha=Scrollbar(win)
    scroll_Derecha.pack(side=RIGHT,fill=Y)
    Scroll_Abajo=Scrollbar(win,orient='horizontal')
    Scroll_Abajo.pack(side=BOTTOM, fill=X)
    #texbox
    tablasTxt=Text(win,width=100,height=40,yscrollcommand=scroll_Derecha.set,wrap="none",xscrollcommand=Scroll_Abajo.set)
    tablasTxt.pack()
    #configurar Scroll en texbox
    scroll_Derecha.config(command=tablasTxt.yview)
    Scroll_Abajo.config(command=tablasTxt.xview)
    gemts=AST.generarTSReporte()
    tablasTxt.insert('end',gemts)
    tablasTxt.insert('end','\n\n')
    #webbrowser.open_new_tab('reporte_TS.html')

def abrirErrores():
    webbrowser.open_new_tab('Reporte_Errores.html')
    webbrowser.open_new_tab('Reporte_Errores_Sem.html')

def abrirSimbolos():
    #crear ventana
    win=Tk()
    win.title("Estructura De Las Tablas")
    win.geometry('900x600')
    #crear Scrol
    scroll_Derecha=Scrollbar(win)
    scroll_Derecha.pack(side=RIGHT,fill=Y)
    Scroll_Abajo=Scrollbar(win,orient='horizontal')
    Scroll_Abajo.pack(side=BOTTOM, fill=X)
    #texbox
    tablasTxt=Text(win,width=100,height=40,yscrollcommand=scroll_Derecha.set,wrap="none",xscrollcommand=Scroll_Abajo.set)
    tablasTxt.pack()
    #configurar Scroll en texbox
    scroll_Derecha.config(command=tablasTxt.yview)
    Scroll_Abajo.config(command=tablasTxt.xview)
    for tab in AST.mostrarTablasTemp():
        tablasTxt.insert('end',tab)
        tablasTxt.insert('end','\n\n')
    #webbrowser.open_new_tab('reporte_TS.html')

def show_popup_menu(event):
    popup_menu.tk_popup(event.x_ventana, event.y_ventana)


def show_cursor_info_bar():
    show_cursor_info_checked = show_cursor_info.get()
    if show_cursor_info_checked:
        cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')
    else:
        cursor_info_bar.pack_forget()


def update_cursor_info_bar(event=None):
    row, col = content_text.index(INSERT).split('.')
    line_num, col_num = str(int(row)), str(int(col) + 1)  # col starts at 0
    infotext = "Fila: {0} | Columna: {1}".format(line_num, col_num)
    cursor_info_bar.config(text=infotext)


def change_theme(event=None):
    selected_theme = theme_choice.get()
    fg_bg_colors = color_schemes.get(selected_theme)
    foreground_color, background_color = fg_bg_colors.split('.')
    content_text.config(background=background_color, fg=foreground_color)


def update_line_numbers(event=None):
    line_numbers = get_line_numbers()
    line_number_bar.config(state='normal')
    line_number_bar.delete('1.0', 'end')
    line_number_bar.insert('1.0', line_numbers)
    line_number_bar.config(state='disabled')



def on_content_changed(event=None):
    update_line_numbers()
    update_cursor_info_bar()


def get_line_numbers():
    output = ''
    if show_line_number.get():
        row, col = content_text.index("end").split('.')
        for i in range(1, int(row)):
            output += str(i) + '\n'
    return output


def exit_editor(event=None):
    if tkinter.messagebox.askokcancel("Exit", "Seguro que desea salir?"):
        ventana.destroy()


def new_file(event=None):
    ventana.title("Untitled")
    global archivo
    archivo = None
    content_text.delete(1.0, END)
    on_content_changed()


def open_file(event=None):
    input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if input_file_name:
        global archivo
        archivo = input_file_name
        ventana.title('{} - {}'.format(os.path.basename(archivo), "TytusDB_18"))
        content_text.delete(1.0, END)
        with open(archivo) as _file:
            content_text.insert(1.0, _file.read())
        on_content_changed()


def select_all(event=None):
    content_text.tag_add('sel', '1.0', 'end')
    return "break"


def find_text(event=None):
    search_toplevel = Toplevel(ventana)
    search_toplevel.title('Find Text')
    search_toplevel.transient(ventana)

    Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')

    search_entry_widget = Entry(search_toplevel, width=25)
    search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
    search_entry_widget.focus_set()
    ignore_case_value = IntVar()
    Checkbutton(search_toplevel, text='Ignore Case', variable=ignore_case_value).grid(row=1, column=1, sticky='e', padx=2, pady=2)
    Button(search_toplevel, text="Find All", underline=0,
           command=lambda: search_output(
               search_entry_widget.get(), ignore_case_value.get(),
               content_text, search_toplevel, search_entry_widget)
           ).grid(row=0, column=2, sticky='e' + 'w', padx=2, pady=2)

    def close_search_window():
        content_text.tag_remove('match', '1.0', END)
        search_toplevel.destroy()
    search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)
    return "break"


def search_output(needle, if_ignore_case, content_text,search_toplevel, search_box):
    content_text.tag_remove('match', '1.0', END)
    matches_found = 0
    if needle:
        start_pos = '1.0'
        while True:
            start_pos = content_text.search(needle, start_pos,nocase=if_ignore_case, stopindex=END)
            if not start_pos:
                break
            end_pos = '{}+{}c'.format(start_pos, len(needle))
            content_text.tag_add('match', start_pos, end_pos)
            matches_found += 1
            start_pos = end_pos
        content_text.tag_config(
            'match', foreground='red', background='yellow')
    search_box.focus_set()
    search_toplevel.title('{} matches found'.format(matches_found))


def cut():
    content_text.event_generate("<<Cut>>")
    on_content_changed()
    return "break"


def copy():
    content_text.event_generate("<<Copy>>")
    return "break"


def paste():
    content_text.event_generate("<<Paste>>")
    on_content_changed()
    return "break"


def undo():
    content_text.event_generate("<<Undo>>")
    on_content_changed()
    return "break"


def redo(event=None):
    content_text.event_generate("<<Redo>>")
    on_content_changed()
    return 'break'


#Metodo para analizar la entrada

def analizar():
    input = content_text.get(1.0,"end-1c")
    #print(input)
    #print(".........Analizando....")
    #Gramatica.AnalizarInput(input)
    AST.Analisar(input)
    #AST.generarAST()

#Metodo para generar el reporte del arbol ast


menu_bar = Menu(ventana)
archivo = Menu(menu_bar, tearoff=0)
archivo.add_command(label='Nuevo Archivo',  compound='left', underline=0, command=new_file)
archivo.add_command(label='Abrir',  compound='left', underline=0, command=open_file)
archivo.add_separator()
archivo.add_command(label='Salir', accelerator='Alt+F4', command=exit_editor)
menu_bar.add_cascade(label='Archivo', menu=archivo)

editar = Menu(menu_bar, tearoff=0)
editar.add_command(label='Cortar', accelerator='Ctrl+X',compound='left', command=cut)
editar.add_command(label='Copiar', accelerator='Ctrl+C',compound='left', command=copy)
editar.add_command(label='Pegar', accelerator='Ctrl+V',compound='left',  command=paste)
editar.add_separator()
editar.add_command(label='Buscar', underline=0,accelerator='Ctrl+F', command=find_text)
editar.add_separator()
editar.add_command(label='Seleccionar Todo', underline=7,accelerator='Ctrl+A', command=select_all)
menu_bar.add_cascade(label='Editar', menu=editar)

compil = Menu(menu_bar, tearoff=0)
compil.add_command(label="Compilar Ascendente", compound="left", command=analizar)
#compil.add_command(label="Compilar Descendente", accelerator='Ctrl+8', compound="left", command=compilar)
menu_bar.add_cascade(label='Compilar', menu=compil)

report = Menu(menu_bar, tearoff=0)
report.add_command(label="Gramatical Ascendente", compound="left", command=abrirGramaticalASC)
report.add_command(label="Tabla de Simbolos", compound="left", command=abrirEstructuraTablas)
report.add_command(label="AST", compound="left", command=abrirAST)
report.add_command(label="Estructura Tablas", compound="left", command=abrirSimbolos)
report.add_command(label="Errores", compound="left", command=abrirErrores)
menu_bar.add_cascade(label='Reportes', menu=report)

view_menu = Menu(menu_bar, tearoff=0)
show_line_number = IntVar()
show_line_number.set(1)
view_menu.add_checkbutton(label='Mostrar Linea', variable=show_line_number,command=update_line_numbers)
show_cursor_info = IntVar()
show_cursor_info.set(1)
view_menu.add_checkbutton(label='Posición del Cursos', variable=show_cursor_info, command=show_cursor_info_bar)
to_highlight_line = BooleanVar()
themes_menu = Menu(menu_bar, tearoff=0)
view_menu.add_cascade(label='Temas', menu=themes_menu)

color_schemes = {
    'Light': '#000000.#FFFFFF',
    'Dark': '#FFFFFF.#000000'
}

theme_choice = StringVar()
theme_choice.set('Light')
for k in sorted(color_schemes):
    themes_menu.add_radiobutton(label=k, variable=theme_choice, command=change_theme)
menu_bar.add_cascade(label='Vista', menu=view_menu)

about_menu = Menu(menu_bar, tearoff=0)
ventana.config(menu=menu_bar)

line_number_bar = Text(ventana, width=4, padx=3, takefocus=0, border=0,background='#D1D4D1', state='disabled',  wrap='none')
line_number_bar.pack(side='left',  fill='y')

content_text = Text(ventana, wrap='word', undo=1)
content_text.pack(expand='yes', fill='both')
scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')
cursor_info_bar = Label(content_text, text='Fila: 1 | Columna: 1')
cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')


content_text.bind('<Control-N>', new_file)
content_text.bind('<Control-n>', new_file)
content_text.bind('<Control-O>', open_file)
content_text.bind('<Control-o>', open_file)
content_text.bind('<Control-f>', find_text)
content_text.bind('<Control-F>', find_text)
content_text.bind('<Control-A>', select_all)
content_text.bind('<Control-a>', select_all)
content_text.bind('<Control-y>', redo)
content_text.bind('<Control-Y>', redo)
content_text.bind('<Any-KeyPress>', on_content_changed)
content_text.tag_configure('active_line', background='ivory')

# set up the pop-up menu
popup_menu = Menu(content_text)
for i in ('cut', 'copy', 'paste', 'undo', 'redo'):
    cmd = eval(i)
    popup_menu.add_command(label=i, compound='left', command=cmd)
popup_menu.add_separator()
popup_menu.add_command(label='Select All', underline=7, command=select_all)
content_text.bind('<Button-3>', show_popup_menu)


# bind right mouse click to show pop up and set focus to text widget on launch
content_text.bind('<Button-3>', show_popup_menu)
content_text.focus_set()


#Consola de salida
'''consola_text = Text(ventana, wrap='word', undo=1)
consola_text.pack(expand='yes', fill='both')
scroll_bar2 = Scrollbar(consola_text)
consola_text.configure(yscrollcommand=scroll_bar2.set)
scroll_bar2.config(command=consola_text.yview)
scroll_bar2.pack(side='right', fill='y')'''

ventana.protocol('WM_DELETE_WINDOW', exit_editor)
ventana.mainloop()
