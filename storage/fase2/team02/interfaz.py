from tkinter import*  
from PIL import ImageTk, Image

ventana = Tk()
ventana.title('TYTUS DB II FASE')
imagen = ImageTk.PhotoImage(Image.open(r'C:\Users\rospo\Documents\GitHub\tytus\storage\fase2\team02\fondo.jpg').resize((500, 500)))
labelimagen = Label(image=imagen)

botonGrafo1 = Button(labelimagen , text = "   Grafo 1   ")
botonGrafo1.place(x=325, y = 110)
botonGrafo1.config(background = "#70af85",  relief = "raised", borderwidth=6, fg="white", font=("Helvetica", 12 , "bold") )



labelimagen.pack()
ventana.mainloop()
