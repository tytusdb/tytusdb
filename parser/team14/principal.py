import gramatica2 as g
from tkinter import *




ventana= Tk()
ventana.geometry("1000x900")
ventana.resizable(False,False)
ventana.config(background = "gray25")

def send_data():
    print("Analizando Entrada:")
    print("==============================================")
    contenido = Tentrada.get(1.0, 'end')
    Tsalida.delete("1.0", "end")
    Tsalida.configure(state='normal')
    Tsalida.insert(INSERT, "Salida de consultas")
    Tsalida.configure(state='disabled')
    print(contenido)

    instrucciones = g.parse(contenido)


entrada = StringVar()
Tentrada = Text(ventana)
Tentrada.config(width=120, height=35)
Tentrada.config(background="gray18")
Tentrada.config(foreground="white")
Tentrada.config(insertbackground="white")
Tentrada.place(x = 10, y = 10)

Tsalida = Text(ventana)
Tsalida.config(width=120, height=19)
Tsalida.config(background="gray10")
Tsalida.config(foreground="white")
Tsalida.config(insertbackground="white")
Tsalida.place(x = 10, y = 580)
Tsalida.configure(state='disabled')
menu_bar = Menu(ventana)

ventana.config(menu=menu_bar)
# Menu Ejecutar
ej_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Ejecutar",menu=ej_menu)
ej_menu.add_command(label="Analizar Entrada", command=send_data)

# Menu Reportes

reps_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Reportes",menu=reps_menu)
reps_menu.add_command(label="Errores Lexicos", command=send_data)
reps_menu.add_command(label="Errores Sintacticos", command=send_data)
reps_menu.add_command(label="Errores Semanticos", command=send_data)
reps_menu.add_command(label="Tabla de Simbolos", command=send_data)
reps_menu.add_command(label="AST", command=send_data)
reps_menu.add_command(label="Gramatica", command=send_data)



ventana.mainloop()



