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
import optimizacion.reportes.RepOptimizacion as ro
import reportes.reportesimbolos as rs
import reportes.RealizarGramatica
import reportes.tablasimbolos as rts

from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.TablaSimbolos.Arbol import Arbol
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Sql_create.CreateDatabase import CreateDatabase
from Instrucciones.PL.Func import Func
from Instrucciones.PL.Proc import Proc
from optimizacion.reportes.Mirilla import Mirillas
from storageManager.jsonMode import *
from optimizacion.Instrucciones.C3D.MetodoC3D import MetodoC3D
from optimizacion.Instrucciones.C3D.SentenciaIf import SentenciaIf
from optimizacion.Instrucciones.C3D.Arroba import Arroba
import graficaAST

import sintactico
global arbol
arbol = None
global tabb
tabb = None
'''
instruccion = CreateDatabase("bd1",None,"TRUE",None,None,None,None, 1,2)
instruccion.ejecutar(None,None)
# ---------------------------- PRUEBA DE UNA SUMA  ----------------------------
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Expresiones import Primitivo, Logica
p1 = Primitivo.Primitivo(True,Tipo(Tipo_Dato.BOOLEAN),1,1)
p2 = Primitivo.Primitivo(True,Tipo(Tipo_Dato.BOOLEAN),1,1)
a = Arbol([])
op = Logica.Logica(p1,p2,'AND',1,2)
print('Resultado logica: ' + str(suma.ejecutar(None,a)))
# ---------------------------- PRUEBA DE UNA SUMA CON ERROR DE TIPO ----------------------------
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Expresiones import Primitivo, Aritmetica
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
        self.window.configure(background="#252850")
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
        btnanalizar = Button(self.window,image=img2 , bg="#cdcdcd",height=35, width=40, command=self.btnanalizar_click)
        btnanalizar.place(x=20,y=4)

        img3 = PhotoImage(file='img/icons/play32.png')
        btnejecutar = Button(self.window,image = img3 , bg="#cdcdcd",height=35, width=40,command=self.btnejecutar_click)
        btnejecutar.place(x=115,y=5)
        
        img4 = PhotoImage(file='img/icons/opt.png')
        btnejecutar = Button(self.window,image = img4 , bg="#cdcdcd",height=35, width=40,command=self.btnoptimizar_click)
        btnejecutar.place(x=210,y=5)

        ##############################################PESTAÑAS####################################
        self.tab = ttk.Notebook(self.window)
        self.tab.pack(fill='both',padx=20, pady=[50,20])
        self.tab_frame =[]
        self.txtentrada =[]
        self.txtsalida =[]
        self.txtoptimizacion = []
        self.crear_tab("","Nuevo.sql")
        
        lblentrada= Label(self.window,text="Archivo de Entrada:",height=1, width=15,bg='#CDCDCD')
        lblentrada.place(x=50,y=80)
        lblsalida= Label(self.window,text="Consola de Salida:",height=1, width=15,bg='#CDCDCD')
        lblsalida.place(x=700,y=80)
        lbloptimización= Label(self.window,text="Consola de Optimización:",height=1, width=20,bg='#CDCDCD')
        lbloptimización.place(x=50,y=350)

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
        global tabb
        if tabb != None:
            rts.crear_tabla(tabb)
        arbol = None         

    def ast_click(self):
        input=self.txtentrada[self.tab.index("current")].get(1.0,END)
        graficaAST.graficarAST(input)
    
    def repDin_click(self):
        global arbol
        reportes.RealizarGramatica.RealizarGramatica.generar_reporte_gamatical(arbol.lRepDin)
        arbol = None


    def btnoptimizar_click(self):
        import optimizacion.sintacticoC3D
        os.system ("cls")
        #Elimina el Contenido de txtsalida
        self.txtoptimizacion[self.tab.index("current")].delete(1.0,END)
        #aqui vamos a leer el archivo
        input=self.txtsalida[self.tab.index("current")].get(1.0,END)
        tablaGlobal = Tabla(None)
        inst = optimizacion.sintacticoC3D.ejecutar_analisis2(input)
        arbol = Arbol(inst)
        instru = arbol.instrucciones
        if(instru):
            m = Mirillas(instru)
            m.optimizarCodigo()
            val = m.getItemReporte()
            ro.crear_tabla(val)

        resultado = ""
        tabulador = ""
        for i in arbol.instrucciones:
            # La variable resultado nos permitirá saber si viene un return, break o continue fuera de sus entornos.
            if i :
                if(isinstance(i,MetodoC3D)):
                    tabulador = True

                if(tabulador == True and not(isinstance(i,MetodoC3D))):
                    resultado += "\t"

                if(isinstance(i,Arroba)):
                    resultado += "\r\r" 
                
                resultado += i.ejecutar(tablaGlobal, arbol)
                
                resultado += "\n"

                if(isinstance(i, SentenciaIf)):
                    resultado += "\t"
                 

        # Después de haber ejecutado todas las instrucciones se verifica que no hayan errores semánticos.
        if len(arbol.excepciones) != 0:
            reportes.RealizarReportes.RealizarReportes.generar_reporte_lexicos(arbol.excepciones)
        # Ciclo que imprimirá todos los mensajes guardados en la variable consola.
        mensaje = ''
        for m in arbol.consola:
            mensaje += m + '\n'

        archivo = open("pruebaOpti.py", "w",encoding='utf-8')
        archivo.write(resultado)
        archivo.close() 
        self.txtoptimizacion[self.tab.index("current")].insert(INSERT,resultado)
        
    ##############################################EVENTOS DE LOS BOTONES DEL FRAME####################################
    def btnanalizar_click(self):
        global arbol
        arbol = None
        global tabb
        tabb = None
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
        
        '''
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
        '''
        # Buscar funciones
        for i in arbol.instrucciones:
            if isinstance(i, Func) or isinstance(i, Proc):
                i.llenarTS(tablaGlobal,arbol)

        for i in arbol.instrucciones:
            # La variable resultado nos permitirá saber si viene un return, break o continue fuera de sus entornos.
            resultado = i.analizar(tablaGlobal,arbol)
        
        # Ciclo que imprimirá todos los mensajes guardados en la variable consola.
        mensaje = ''
        for m in arbol.consola:
            mensaje += m + '\n'
        self.txtsalida[self.tab.index("current")].insert(INSERT,mensaje)
        
        # Después de haber ejecutado todas las instrucciones se verifica que no hayan errores semánticos.
        if len(arbol.excepciones) != 0:
            reportes.RealizarReportes.RealizarReportes.generar_reporte_lexicos(arbol.excepciones)
        else:
            c3d = 'from goto import with_goto\n'
            c3d += 'import math\n'
            c3d += 'from sintactico import *\n'
            c3d += 'import reportes.reportesimbolos as rs\n'
            c3d += 'from Instrucciones.TablaSimbolos.Tabla import Tabla\n'
            c3d += 'from Instrucciones.TablaSimbolos.Arbol import Arbol\n'
            c3d += 'from storageManager.jsonMode import *\n'
            c3d += 'import sys\n'
            c3d += 'global P\n'
            c3d += 'global Pila\n'
            c3d += 'P = 0\n'
            c3d += 'Pila = [None] * 1000\n'

            c3d += 'tablaGlobal = Tabla(None)\n'
            c3d += 'global sql\n'
            c3d += 'global inst\n'
            c3d += 'arbol = Arbol(None)\n'

            c3d += self.funcionintermedia()
            #c3d += '@with_goto  # Decorador necesario.\n'
            

            # Agregamos las funciones al reporte
            for i in tablaGlobal.variables:
                tablaGlobal.agregarReporteSimbolo(i)
            
            # Se traducen las funciones
            for i in tablaGlobal.variables:
                if i.rol == "Metodo":
                    i.funcion.traducir(tablaGlobal,arbol)
            c3d += arbol.cadena

            c3d += 'def main():\n'
            c3d += '\tdropAll()\n'
            c3d += '\tglobal P\n'
            c3d += '\tglobal Pila\n'
        
            # Se traducen el resto de las demás sentencias
            arbol.cadena = ""
            for i in arbol.instrucciones:
                if not isinstance(i, Func) and not isinstance(i, Proc):
                    i.traducir(tablaGlobal,arbol)

            c3d += arbol.cadena
            c3d += 'if __name__ == \"__main__\":\n'
            c3d += '\tmain()\n'
            c3d += '\trs.crear_tabla(arbol)'
            archivo = open("prueba.py", "w",encoding='utf-8')
            archivo.write(c3d)
            archivo.close() 
            self.txtsalida[self.tab.index("current")].insert(INSERT,c3d)
            # Nuevo reporte tabla de símbolos 2
            tabb = tablaGlobal.reporte
            # rts.crear_tabla(tablaGlobal.reporte)
        
        
    def funcionintermedia(self):
        c3d = 'def funcionintermedia():\n'
        c3d += '\tglobal P\n'
        c3d += '\tglobal Pila\n'
        c3d += '\tt0 = P+0\n'
        c3d += '\tt1 = t0+1\n'
        c3d += '\tt2 = Pila[t1]\n'
        c3d += '\tprint(\"\\n\"+\'\\033[96m\'+t2+\'\\033[0m\')\n'

        c3d += '\tsql = Pila[t1]\n'
        c3d += '\tinstrucciones = ejecutar_analisis(sql)\n'
        c3d += '\tfor instruccion in instrucciones:\n'
        c3d += '\t\tt3 = instruccion.ejecutar(tablaGlobal,arbol)\n'
        c3d += '\tt4 = P+0\n'
        c3d += '\tt5 = t0+2\n'
        c3d += '\tPila[t5] = t3\n'
        c3d += '\tfor msj in arbol.consola:\n'
        c3d += '\t\tprint(f\"{msj}\")\n'
        c3d += '\tarbol.consola = []\n'

        return c3d


    def btnejecutar_click(self):
        print("se va ejecutar el archivo")
        
    ##############################################CREA PESTAÑAS EN EL TAB####################################
    def crear_tab(self,entrada,nombre):
        self.tab_frame.append(Frame(self.tab,width=200, height=700,background="#CDCDCD"))
        self.tab_frame[-1].pack(fill='both', expand=1)
        self.tab_frame[-1].config(bd=5)
        self.tab.add(self.tab_frame[-1],text=nombre)
        self.txtentrada.append(scrolledtext.ScrolledText(self.tab_frame[-1],width=78,height=15))
        self.txtentrada[-1].place(x=0,y=25)
        self.txtentrada[-1].insert(INSERT,entrada+"")
        #self.txtentrada[-1].bind("<MouseWheel>", self.OnMouseWheel)

        self.txtsalida.append(scrolledtext.ScrolledText(self.tab_frame[-1],width=80,height=15,background="#252440",foreground="#FEFDFD"))
        self.txtsalida[-1].place(x=655,y=25)
        #nombre del archivo
        #print(self.tab.tab(self.tab.select(),"text"))
        #self.txtsalida[-1].insert(INSERT,entrada+"")
        self.txtoptimizacion.append(scrolledtext.ScrolledText(self.tab_frame[-1],width=162,height=15,background="#070707",foreground="#FEFDFD"))
        self.txtoptimizacion[-1].place(x=0,y=300)
        self.tab.select(int(len(self.tab_frame)-1))

    
    #def OnMouseWheel(self,event):
    #    print("scrool mouse")

def main():
    mi_app = interfaz()
    return(0)

if __name__ == '__main__':
    main()