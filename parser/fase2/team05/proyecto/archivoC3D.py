def crearArchivo(input):
    archivo = ''
    f = open("codigo3D.txt", "w")

    archivo += 'def main(): \n'
    for a in input:
        archivo += a + '\n'
        print(a)
    print('**************************************************')



    f.write(archivo)
    f.close()


