import storageManager
from tkinter import *
from os import path
from tkinter import filedialog

from tkinter import Menu
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
import os
#from sintactico import ejecutar_analisis
import reportes.RealizarReportes
import reportes.reportesimbolos as rs
import reportes.RealizarGramatica

from sql.Instrucciones.TablaSimbolos.Tabla import Tabla
from sql.Instrucciones.TablaSimbolos.Arbol import Arbol
from sql.Instrucciones.Excepcion import Excepcion
from sql.Instrucciones.Sql_create.CreateDatabase import CreateDatabase

from sql.storageManager.jsonMode import *

import sintactico

global arbol
arbol = None
'''
instruccion = CreateDatabase("bd1",None,"TRUE",None,None,None,None, 1,2)
instruccion.ejecutar(None,None)

# ---------------------------- PRUEBA DE UNA SUMA  ----------------------------
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from sql.Instrucciones.Expresiones import Primitivo, Logica

p1 = Primitivo.Primitivo(True,Tipo(Tipo_Dato.BOOLEAN),1,1)
p2 = Primitivo.Primitivo(True,Tipo(Tipo_Dato.BOOLEAN),1,1)
a = Arbol([])
op = Logica.Logica(p1,p2,'AND',1,2)
print('Resultado logica: ' + str(suma.ejecutar(None,a)))

# ---------------------------- PRUEBA DE UNA SUMA CON ERROR DE TIPO ----------------------------
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from sql.Instrucciones.Expresiones import Primitivo, Aritmetica

p1 = Primitivo.Primitivo(1,Tipo(Tipo_Dato.BOOLEAN),1,1)
p2 = Primitivo.Primitivo(2,Tipo(Tipo_Dato.INTEGER),1,1)
a = Arbol([])
suma = Aritmetica.Aritmetica(p1,p2,'+',1,2)
suma.ejecutar(None,a)
reportes.RealizarReportes.RealizarReportes.generar_reporte_lexicos(a.excepciones)
'''

class interfaz():
    def __init__(self):
        ##############################################VENTANA PRINCIPAL####################################
        self.window=Tk()
        #self.window.configure(background="#04DE5E")
        img = PhotoImage(file='img/icons/postgesql2.png')
        self.window.tk.call('wm', 'iconphoto', self.window._w, img)
        #img = PhotoImage(file='img/icons/Postgresql.ico')
        #self.window.tk.call('wm', 'iconphoto', self.window._w, img)
        self.window.configure(background="#6a8d92")
        self.window.title("Query Tool - Grupo 8")
        #w, h = self.window.winfo_screenwidth()/2, self.window.winfo_screenheight()/2
        w, h = 1370,670
        self.window.geometry("%dx%d+0+0" % (w, h))
        
        ##############################################MENU####################################
        menu = Menu(self.window)
        new_item = Menu(menu,tearoff=0)
        new_item.add_command(label='Abrir', command=self.abrir_click)
        new_item.add_command(label='Guardar', command=self.guardar_click)
        new_item.add_command(label='Guardar Como...', command=self.guardar_como_click)
        #new_item.add_separator()
        #new_item.add_command(label='Edit')
        menu.add_cascade(label='Archivo', menu=new_item)
        mnreportes = Menu(menu,tearoff=0)
        mnreportes.add_command(label='Tabla de Errores', command=self.tblerrores_click)
        mnreportes.add_command(label='Tabla de Simbolos', command=self.tblsimbolos_click)
        mnreportes.add_command(label='AST', command=self.ast_click)
        mnreportes.add_command(label='Reporte Gramatical', command=self.repDin_click)
        menu.add_cascade(label='Reportes', menu=mnreportes)
        self.window.config(menu=menu)

        ##############################################BOTONES####################################
        
        img2 = PhotoImage(file='img/icons/AnalyzeMP.png')
        btnanalizar = Button(self.window,image=img2 , bg="#6a8d92",height=35, width=40, command=self.btnanalizar_click)
        btnanalizar.place(x=20,y=4)

        img3 = PhotoImage(file='img/icons/play32.png')
        btnejecutar = Button(self.window,image = img3 , bg="#6a8d92",height=35, width=40,command=self.btnejecutar_click)
        btnejecutar.place(x=115,y=5)

        ##############################################PESTAÑAS####################################
        self.tab = ttk.Notebook(self.window)
        self.tab.pack(fill='both',padx=20, pady=[50,20])
        self.tab_frame =[]
        self.txtentrada =[]
        self.txtsalida =[]
        self.crear_tab("","Nuevo.sql")
        
        lblentrada= Label(self.window,text="Archivo de Entrada:",height=1, width=15,bg='#80b192')
        lblentrada.place(x=20,y=80)
        lblsalida= Label(self.window,text="Consola de Salida:",height=1, width=15,bg='#80b192')
        lblsalida.place(x=20,y=350)

        #redimensionar los elementos
        #self.window.bind('<Configure>',self.resizeEvent)

        #Objeto que almacena el Archivo
        self.file=""

        self.window.mainloop()


    def ejecutar(self):
        print("Hello World!")
        print("Estoy ejecutando el main")
        f = open("./entrada.txt", "r")
        input = f.read()
        #lista = "" : ""
        #insert(database: "world", table: "countries", register: lista) 
        #print(input)
        #parser.parse(input)
        #Inserta "Archivo Analizado" en txtsalida
        
        
    ##############################################EVENTO REDIMENSIONAR LA VENTANA####################################
    def resizeEvent(self, event):
        print(event.width,event.height)

    ##############################################EVENTOS DE LOS BOTONES DEL MENU####################################
    def abrir_click(self):
        try:
            self.file = filedialog.askopenfilename(initialdir= os.path.dirname(__file__))
            archivo=open(self.file,"r")
            entrada=archivo.read()
            archivo.close()
            self.crear_tab(entrada,self.file.split("/").pop())
        except FileNotFoundError:
            messagebox.showwarning("Abrir","No selecciono ningún Archivo.")
        except UnicodeDecodeError:
            messagebox.showerror('Abrir','El Archivo seleccionado no es admitido.')

    def guardar_click(self):
        try:
            archivo=open(self.file,"w")
            archivo.write(self.txtentrada[self.tab.index("current")].get(1.0,END))
            messagebox.showinfo('Aviso','Se Guardo el Archivo Correctamente!')
        except FileNotFoundError:
            messagebox.showerror('Guardar','No abrio ningun Archivo.')
        except:
            messagebox.showerror("Error","Contacte al Administrador del sistema.")
        
    def guardar_como_click(self):
        self.file = filedialog.askdirectory(initialdir= path.dirname(__file__))
        archivo=open(self.file+"/"+self.tab.tab(self.tab.select(),"text"),"w")
        archivo.write(self.txtentrada[self.tab.index("current")].get(1.0,END))
        print(self.file+"/"+self.tab.tab(self.tab.select(),"text"))
        print("guardar_como")

    def tblerrores_click(self):
        if len(sintactico.lista_lexicos)==0:
            messagebox.showinfo('Tabla de Errores','La Entrada no Contiene Errores!')
        else:
            reportes.RealizarReportes.RealizarReportes.generar_reporte_lexicos(sintactico.lista_lexicos)

    def tblsimbolos_click(self):
        # Función que crea el reporte de tabla de símbolos, recibe como parametro una tabla.
        global arbol
        rs.crear_tabla(arbol)  
        arbol = None         

    def ast_click(self):
        print("ast")   
    
    def repDin_click(self):
        global arbol
        reportes.RealizarGramatica.RealizarGramatica.generar_reporte_gamatical(arbol.lRepDin)
        arbol = None

    ##############################################EVENTOS DE LOS BOTONES DEL FRAME####################################
    def btnanalizar_click(self):
        global arbol
        arbol = None
        dropAll()
        os.system ("cls")
        #Elimina el Contenido de txtsalida
        self.txtsalida[self.tab.index("current")].delete(1.0,END)
        #Inserta "Archivo Analizado" en txtsalida
        #self.txtsalida[self.tab.index("current")].insert(INSERT,"Archivo Analizado")
        #Selecciona el contenido de txt entrada
        #print(self.txtentrada[self.tab.index("current")].get(1.0,END))
        input=self.txtentrada[self.tab.index("current")].get(1.0,END)
        tablaGlobal = Tabla(None)
        inst = sintactico.ejecutar_analisis(input)
        arbol = Arbol(inst)

        if len(sintactico.lista_lexicos)>0:
            messagebox.showerror('Tabla de Errores','La Entrada Contiene Errores!')
            reportes.RealizarReportes.RealizarReportes.generar_reporte_lexicos(sintactico.lista_lexicos)
        # Ciclo que recorrerá todas las instrucciones almacenadas por la gramática.
        arbol.lRepDin.append("<init> ::= <instrucciones>")
        arbol.lRepDin.append("<instrucciones>   ::=  <instrucciones> <instruccion>")
        arbol.lRepDin.append("<instrucciones> ::= <instruccion>")
        
        for i in arbol.instrucciones:
            # La variable resultado nos permitirá saber si viene un return, break o continue fuera de sus entornos.
            resultado = i.ejecutar(tablaGlobal,arbol)
        # Después de haber ejecutado todas las instrucciones se verifica que no hayan errores semánticos.
        if len(arbol.excepciones) != 0:
            reportes.RealizarReportes.RealizarReportes.generar_reporte_lexicos(arbol.excepciones)
        # Ciclo que imprimirá todos los mensajes guardados en la variable consola.
        mensaje = ''
        for m in arbol.consola:
            mensaje += m + '\n'
        self.txtsalida[self.tab.index("current")].insert(INSERT,mensaje)
        
        

        


    def btnejecutar_click(self):
        print("se va ejecutar el archivo")
        
    ##############################################CREA PESTAÑAS EN EL TAB####################################
    def crear_tab(self,entrada,nombre):
        self.tab_frame.append(Frame(self.tab,width=200, height=700,background="#80b192"))
        self.tab_frame[-1].pack(fill='both', expand=1)
        self.tab_frame[-1].config(bd=5)
        self.tab.add(self.tab_frame[-1],text=nombre)
        self.txtentrada.append(scrolledtext.ScrolledText(self.tab_frame[-1],width=162,height=15))
        self.txtentrada[-1].place(x=0,y=25)
        self.txtentrada[-1].insert(INSERT,entrada+"")
        #self.txtentrada[-1].bind("<MouseWheel>", self.OnMouseWheel)

        self.txtsalida.append(scrolledtext.ScrolledText(self.tab_frame[-1],width=162,height=15,background="#070707",foreground="#FEFDFD"))
        self.txtsalida[-1].place(x=0,y=298)
        #nombre del archivo
        #print(self.tab.tab(self.tab.select(),"text"))
        self.tab.select(int(len(self.tab_frame)-1))
        #self.txtsalida[-1].insert(INSERT,entrada+"")

    
    #def OnMouseWheel(self,event):
    #    print("scrool mouse")

def main():
    mi_app = interfaz()
    return(0)

if __name__ == '__main__':
    main()