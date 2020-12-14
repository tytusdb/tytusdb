import Gramatica.Gramatica as g
import graphviz
import sys
import threading
import Errores.Nodo_Error as error
import Errores.ListaErrores as lista_err
from Reportes.ReporteError import ReporteError
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font
from tkinter import ttk

#------------------------------------ Interfaz ----------------------------------------------------------
root = Tk()
root.title('TytusDB - Team 19')
root.geometry("1000x750")
errores = None

def ejecutar():
    reporteg=[]
    global errores
    errores=lista_err.ListaErrores()
    entrada = my_text.get("1.0",END)
    SQLparser = g.parse(entrada, errores)
    print(SQLparser)
    Output.delete(1.0,"end")
    respuestaConsola = str(SQLparser) if errores.principio is None else "Hubieron errores ve a Reporte->Errores"
    Output.insert("1.0", respuestaConsola)


def open_File():
    try:
        text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Text File", filetypes=(("Text Files", "*.txt"), ))
        text_file = open(text_file, 'r')
        stuff = text_file.read()

        my_text.insert(END, stuff)
        update_line_numbers()
        text_file.close()
    except FileNotFoundError:
        messagebox.showinfo("Informacion","No se seleccionó un archivo")

def mostrar_reporte_errores():
    global errores #El global indica que no creo una nueva var sino que uso la variable global
    reporte_error = ReporteError(errores)
    reporte_error.open_file_on_my_computer()

def get_line_numbers():
    output = ''
    if show_line_number.get():
        row, col = my_text.index("end").split('.')
        for i in range(1, int(row)):
            output += str(i) + '\n'
    return output

def on_content_changed(event=None):
    update_line_numbers()

def update_line_numbers(event=None):
    line_numbers = get_line_numbers()
    line_number_bar.config(state='normal')
    line_number_bar.delete('1.0', 'end')
    line_number_bar.insert('1.0', line_numbers)
    line_number_bar.config(state='disabled')

menu_bar = Menu(root) 
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', compound='left', underline=0, command=open_File)
file_menu.add_command(label='Ejecutar', compound='left', underline=0, command=ejecutar)
menu_bar.add_cascade(label='File', menu=file_menu)
reportes_menu = Menu(menu_bar, tearoff=0)
reportes_menu.add_command(label='Errores', compound='left',  underline=0, command=mostrar_reporte_errores)
reportes_menu.add_separator()
reportes_menu.add_command(label='Gramaticas',compound='left',  underline=0)
reportes_menu.add_separator()
reportes_menu.add_command(label='AST', compound='left',  underline=0) 
reportes_menu.add_separator()
reportes_menu.add_command(label='TS',compound='left',  underline=0)
menu_bar.add_cascade(label='Reportes', menu=reportes_menu)
show_line_number=IntVar()
show_line_number.set(1)
root.config(menu=menu_bar)

my_frame = Frame(root)
my_frame.pack(pady=10)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

line_number_bar = Text(my_frame, width=4, padx=3, takefocus=0, fg='white', border=0, background='#282828',state='disabled',  wrap='none')
line_number_bar.pack(side='left', fill='y')

my_text = Text(my_frame, width=110, height=30, selectforeground="black", yscrollcommand=text_scroll.set)
text_scroll.config(command=my_text.yview)

separator = ttk.Separator(root, orient='horizontal') 
separator.place(relx=0, rely=0.47, relwidth=1, relheight=1) 

Output = Text(root, height = 10,width = 115,bg = "light cyan") 
my_text.bind('<Any-KeyPress>', on_content_changed)

entrada = my_text.get("1.0",END)

my_text.pack()
separator.pack()
Output.pack() 

root.mainloop()



