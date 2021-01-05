def crearArchivo(input):
    archivo = ''
    f = open("team29/ui/codigo3D.py", "w")
    file1 = open("salida/header.txt", "r")

    archivo += file1.read()

    archivo += 'def funcionIntermedia(): \n'
    archivo += '\tglobal lista\n'
    archivo += '\tentrada = lista.pop()\n'
    archivo += '\tanalize(entrada)\n'

    archivo += '\n\n'
    archivo += 'def main3d(): \n'
    archivo += '\tglobal lista \n'
    for a in input:
        archivo += '\t'+ a + '\n'
        subA = a.split("=")
        archivo += '\tlista = [' + str(subA[0]) + '] \n'
        archivo += '\tfuncionIntermedia() \n'

    archivo += '\n\nif __name__ == "__main__": \n'
    archivo += '\t main()\n'

    print('**************************************************')




    f.write(archivo)
    f.close()


