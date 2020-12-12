from tkinter  import *


root=Tk()
root.title('Editor SQL TytusDB')

root.geometry("1080x660")

#Create Main Frame
my_frame= Frame(root)
my_frame.pack(pady=5)

#Create our Scrollbar For the text Box
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)

#Create Text Box
my_text= Text(my_frame,width=97,height=25,font=("Helvetica", 16),selectbackground="yellow",selectforeground="black",undo=True,yscrollcommand=text_scroll.set)
my_text.pack()

#configure our Scrollbar
text_scroll.config(command=my_text.yview)

#create Menu
my_menu= Menu(root)
root.config(menu=my_menu)

#Add File Menu
file_menu= Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#Definicion de Comandos
def analizar(entrada):
    print("iniciando analisis")
    #analizador(entrada)<-------INVOCAR A PARSER ACA
    print(entrada)


        


run_menu= Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Run",menu=run_menu)
run_menu.add_command(label="Run", command=lambda:analizar(my_text.get("1.0",'end-1c')))



root.mainloop()