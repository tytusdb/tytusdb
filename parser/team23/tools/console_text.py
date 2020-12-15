contenido_consola = "PS C:\\Users\\Grupo 23> "

def limpiar_consola():    
    global contenido_consola
    contenido_consola = "PS C:\\Users\\Grupo 23> "

def add_text(text):
    global contenido_consola
    contenido_consola = contenido_consola + str(text)
    

def get_contenido():
    global contenido_consola
    return contenido_consola