# funcion que nos permite elegir el archivo a analizar.
def buscarFichero(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print (str(cont)+". "+file)
        cont = cont+1

    while respuesta == False:
        numArchivo = input('\nNumero del test: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break

    print ("Has escogido \"%s\" \n" %files [int(numArchivo) - 1])
    return files[int(numArchivo)-1]  


# proceso para abrir la ruta seteada y poder leer cualquiera de los archivos contenidos
# en esa carperta.

def analizar():    
    directorio = 'C:/Users/A8/Desktop/proyecto/test/'
    archivo = buscarFichero(directorio)
    test = directorio + archivo
    fp = codecs.open(test,"r","utf-8")
    cadena = fp.read()
    fp.close()
    analizador = lex.lex()
    analizador.input(cadena)# el parametro cadena, es la cadena de texto que va a analizar.

    #ciclo para la lectura caracter por caracter de la cadena de entrada.
    while True:
        tok = analizador.token()
        if not tok : break
        print(tok)