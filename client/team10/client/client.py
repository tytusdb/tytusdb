import os, sys, webbrowser, platform
import socket
import sys
from tkinter import *
from tkinter import ttk, font, messagebox
from datetime import date
from datetime import datetime
 
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_add = ('localhost', 10000)
print ('connection to port=>', serv_add)
serv.connect(serv_add)

class cliente(): 
        
    def __init__(self, img_carpeta, iconos):
        message = 'data from client'
        print(message)
        serv.sendall(message.encode('utf-8'))

    
        recibido = 0
        esperado = len(message)
    
        while recibido < esperado:
            data = serv.recv(4096)
            recibido += len(data)
            print(data)

        self.img_carpeta = img_carpeta
        self.iconos = iconos 
        self.raiz = Tk() 
        self.raiz.title("TytusDB ")
        self.icono1= PhotoImage(file=self.iconos[0])   
        self.raiz.iconphoto(self.raiz, self.icono1)  
        self.raiz.option_add("*Font", "Helvetica 12")       
        self.raiz.option_add('*tearOff', True)  
        self.raiz.attributes('-fullscreen', True)        
        self.raiz.minsize(400,300)   
        self.fuente = font.Font(weight='normal')  
 
        
        self.CFG_TIPOCONEX = IntVar()
        self.CFG_TIPOCONEX.set(1)  
        self.CFG_TIPOEMUT = IntVar()
        self.CFG_TIPOEMUT.set(1)  
        self.CFG_TIPOEXP = IntVar()
        self.CFG_TIPOEXP.set(1)  
         
        
        self.estado = IntVar()
        self.estado.set(1)   
                          
        
        barramenu = Menu(self.raiz)
        self.raiz['menu'] = barramenu
 

        menu1 = Menu(barramenu)
        self.menu2 = Menu(barramenu)
        menu3 = Menu(barramenu)
        menu4 = Menu(barramenu)
        barramenu.add_cascade(menu=menu1, label='FILE')
        barramenu.add_cascade(menu=self.menu2, label='OBJECT')
        barramenu.add_cascade(menu=menu3, label='TOOLS')
        barramenu.add_cascade(menu=menu4, label='ABOUT')
 

        icono2 = PhotoImage(file=self.iconos[1])
        icono3 = PhotoImage(file=self.iconos[2])
        icono8 = PhotoImage(file=self.iconos[8])
        icono9 = PhotoImage(file=self.iconos[9])
        menu1.add_command(label='   Abrir archivo *.sql', underline=0,image=icono8, compound=LEFT,state="disabled") 
        menu1.add_command(label='   Guardar archivo *.sql', underline=0,image=icono9, compound=LEFT,state="disabled") 
      
        icono4 = PhotoImage(file=self.iconos[3])
        menu3.add_command(label="Query Tool", command=self.f_query_tool, image=icono4, compound=LEFT)

        icono5 = PhotoImage(file=self.iconos[6])
        icono7 = PhotoImage(file=self.iconos[7])
        menu4.add_command(label="GRUPO 10", command=self.f_integrantes, image=icono5, compound=LEFT)
        menu4.add_command(label="TytusDB", command=self.f_web, image=icono7, compound=LEFT)
 

        self.icono5 = PhotoImage(file=self.iconos[4])
        icono6 = PhotoImage(file=self.iconos[5])

        barraherr = Frame(self.raiz, relief=RAISED, bd=2, bg="#E5E5E5")
        bot1 = Button(barraherr, image=icono7 ,  command=self.f_conectar)
        bot1.pack(side=LEFT, padx=2, pady=2)
        bot2 = Button(barraherr, image=icono6,  command=self.f_salir)
        bot2.pack(side=RIGHT, padx=1, pady=1)
        barraherr.pack(side=TOP, fill=X)
                 
        now = datetime.now()
        format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
        print(format)
        mensaje = " " + format
        self.barraest = Label(self.raiz, text=mensaje,bd=1, relief=SUNKEN, anchor=W)
        self.barraest.pack(side=BOTTOM, fill=X)
 

        self.menucontext = Menu(self.raiz, tearoff=FALSE) 
        self.menucontext.add_command(label="Salir",command=self.f_salir, compound=LEFT)

        
        self.raiz.mainloop() 

    def f_query_tool(self):
        messagebox.showinfo("Loading...", "DEBERA DEJAR EDITAR O MOSTRAR QUERY TOOL")
 
                                                    
    def f_conectar(self): 
        print("Conectando")
          
    def f_cambiaropc(self):        
        self.menu2.entryconfig("Guardar", state="normal")
                    
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
        marco1 = ttk.Frame(acerca, padding=(10, 10, 10, 10),relief=RAISED)
        marco1.pack(side=TOP, fill=BOTH, expand=True)
        etiq1 = Label(marco1, image=self.icono5,relief='raised')
        etiq1.pack(side=TOP, padx=10, pady=10, ipadx=10, ipady=10)
        etiq2 = Label(marco1, text="PyRemoto "+__version__,foreground='blue', font=self.fuente)
        etiq2.pack(side=TOP, padx=10)
        etiq3 = Label(marco1, text="Python para impacientes")
        etiq3.pack(side=TOP, padx=10)
        boton1 = Button(marco1, text="Salir",command=acerca.destroy)
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
              ruta_r + "save.png")                  
    error1 = f_verificar_iconos(iconos)
       
    if not error1:
        mi_app = cliente(ruta_r, iconos)
    return(0)

if __name__ == '__main__':
    main()