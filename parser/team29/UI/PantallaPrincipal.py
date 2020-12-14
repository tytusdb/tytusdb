from tkinter import ttk
import tkinter as tk
from tkinter import *
from Pantalla_TS import *
from Pantalla_AST import *
from Pantalla_Error import *

class Pantalla():
    def __init__(self):
        #inicializacion de la pantalla
        self.window = Tk()
        self.window.geometry('700x600')
        self.window.resizable(0,0)
        self.window.title('Query Tool')
        self.txtEntrada = tk.Text(self.window,height=15,width=80)
        self.txtEntrada.pack(side=TOP)
        #Definicion del menu de items        
        navMenu = Menu(self.window)
        navMenu.add_command(label='               Tabla de Simbolos             ',command=self.open_ST)
        navMenu.add_command(label='                    AST                      ',command=self.open_AST)
        navMenu.add_command(label='              Reporte de errores              ',command=self.open_Reporte)
        self.window.config(menu=navMenu)
        btn = Button(self.window, text="Consultar", command=self.analize)
        btn.pack(side=TOP, anchor=E, padx=25, pady=20)
        self.window.mainloop()

    def analize(self): 
        entrada = self.txtEntrada.get("1.0",END) #variable de almacenamiento de la entrada
        print(entrada)
    
    def fill_table(self,tabla): #funcion que muestra la salida de la/s consulta/s
       """  tree = ttk.Treeview(self.pw)
        tree["columns"]=("one","two","three")
        tree.column("#0", width=270, minwidth=270, stretch=NO)
        tree.column("one", width=150, minwidth=150, stretch=NO)
        tree.column("two", width=400, minwidth=200)
        tree.column("three", width=80, minwidth=50, stretch=NO)
        tree.heading("#0",text="Name",anchor=W)
        tree.heading("one", text="Date modified",anchor=W)
        tree.heading("two", text="Type",anchor=W)
        tree.heading("three", text="Size",anchor=W)
        tree.pack(side=TOP,fill=X) """
    
    def open_ST(self): #Abre la pantalla de la tabla de simbolos
        windowTableS = Pantalla_TS(self.window)
    
    def open_AST(self): #Abre la pantalla del AST
        windowTableS = Pantalla_AST(self.window)
    
    def open_Reporte(self): #Abre la pantalla de los reportes de errores
        windowTableS = Pantalla_Error(self.window)
        


def main(): #Funcion main
    queryTool = Pantalla()
    return 0

if __name__ == '__main__':
   main()