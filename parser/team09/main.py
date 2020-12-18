import lex
from tkinter import *
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
import instrucciones as inst
import tabla_simbolos as TS 
import Errores as E

ts_global = TS.tabla_simbolos()


def abrir_btn():
    print('open file')
    try:
        read_file = filedialog.askopenfile(mode="r")
        editor_box.delete('1.0', END)
        editor_box.insert(INSERT, read_file.read())

        read_file.close()
        
    except FileNotFoundError:
        messagebox.showwarning("Abrir","Seleccione un archivo.")
    except UnicodeDecodeError:
        messagebox.showerror('Abrir','Archivo no valido.')

def analizar_btn():
    print('analizando')
    txt_entrada = editor_box.get(1.0, END+"-1c")
    parse_result = lex.parse(str(txt_entrada))
    console_box.delete('1.0', END)
    console_box.insert(INSERT, parse_result[1])
    #tabla = inst.create_table('mascotas', 'perro', 'nombre:string,edad:integer', ts_global)

def btnejecutar_click():
    print('ejecutando')

def tblerrores_click():
    print('tabla errores')

def tblsimbolos_click():
    print('tabla simbolos')

def ast_click():
    print('arbol AST')


#--- Main Window
window = Tk()

#self.window.configure(background="#")
window.title("Compiladores 2 SQLParser")

window.geometry("%dx%d+0+0" % (760, 600))
        

#--- Header Menu      
main_menu = Menu(window)
file_menu = Menu(main_menu,tearoff=0)
file_menu.add_command(label='Open', command=abrir_btn)

main_menu.add_cascade(label='File', menu=file_menu)

reportes_menu = Menu(main_menu,tearoff=0)
reportes_menu.add_command(label='Tabla de Errores', command=tblerrores_click)
reportes_menu.add_command(label='Tabla de Simbolos', command=tblsimbolos_click)
reportes_menu.add_command(label='AST', command=ast_click)

main_menu.add_cascade(label='Reportes', menu=reportes_menu)

window.config(menu=main_menu)

#--- Entrada / SQL Editor        
lblentrada= Label(window,text="Editor SQL",height=1, width=15)
lblentrada.place(x=5,y=5)

editor_box = scrolledtext.ScrolledText(window,width=90,height=17)
editor_box.place(x=5, y=30)

#---  Botones Analizar / Ejecutar
btnanalizar = Button(window,text="Analizar",height=2, width=8, command=analizar_btn)
btnanalizar.place(x=40,y=320)

btnejecutar = Button(window,text="Ejecutar",height=2, width=8, command=btnejecutar_click)
btnejecutar.place(x=130,y=320)


#btngraficar = Button(window, text="Graficar", height=2, width=8, command=graficar_ast)
#btngraficar.place(x= 220, y=320)

#--- Consola de Salida
lblsalida= Label(window,text="Consola salida",height=1, width=15)
lblsalida.place(x=5,y=370)

console_box = scrolledtext.ScrolledText(window,width=90,height=11)
console_box.place(x=5,y=395)

window.mainloop()




def create_table(db, nombre, columnas):
    global ts_global

    nueva_tabla = TS.Simbolo(nombre, TS.tipo_simbolo.TABLE, None, db, None, None, None, None)
    x = columnas.split(",")
    for i in x:
        c = x[i].split(":")
        print('El nombre es -> ' + c[0] + ' y el tipo es -> ' + c[1])
        #create_column(db, nombre, c[0], c[1], ts)
    ts_global.agregar_simbolo(nueva_tabla)
    return ts_global

def create_column(db, tabla, columna, tipo):
    nueva_columna = TS.Simbolo(columna,TS.tipo_simbolo.INTEGER,None,db,0,True,False,None)
    agregar = ts_global.agregar_columna(tabla, db, nueva_columna)