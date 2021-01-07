from tkinter import*  
from PIL import ImageTk, Image

ventana = Tk()
ventana.title('TYTUS DB II FASE')
imagen = ImageTk.PhotoImage(Image.open(r'C:\Users\rospo\Documents\GitHub\tytus\storage\fase2\team02\fondo.jpg').resize((500, 500)))
labelimagen = Label(image=imagen)


labelimagen.pack()
ventana.mainloop()
