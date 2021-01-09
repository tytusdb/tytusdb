import tkinter as Tk

import tkinter.ttk as Ttk
from tkinter import messagebox
from tkinter import filedialog

import storageManager as u

ventana=Tk.Tk()
ventana.geometry('300x200')
ventana.title('REPORTES | Tytus DB | EDD A | G5 | FASE 2')
ventana.resizable(0,0)

label_DB=Tk.Label(ventana,text='Database')
label_DB.place(x=25,y=25)
entry_db=Tk.Entry(ventana)
entry_db.place(x=25,y=50)

label_TB=Tk.Label(ventana,text='Table')
label_TB.place(x=25,y=75)
entry_tb=Tk.Entry(ventana)
entry_tb.place(x=25,y=100)

b_DSD=Tk.Button(ventana,text='Reporte DSD', command=lambda:[u.graphDSD(entry_tb.get())])
b_DSD.place(x=225,y=75)

b_DF=Tk.Button(ventana,text='Reporte DF', command=lambda:[u.graphDF(entry_db.get(),entry_tb.get())])
b_DF.place(x=225,y=100)


ventana.mainloop()
