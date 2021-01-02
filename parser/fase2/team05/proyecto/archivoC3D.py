def crearArchivo(input):
    archivo = ''
    archivo += 'lista = [] \n'
    f = open("codigo3D.txt", "w")

    archivo += 'def funcionIntermedia(): \n'
    archivo += '\tglobal lista\n'
    archivo += '\tprueba = lista.pop()\n'

    archivo += 'def main(): \n'
    archivo += '\tglobal lista \n'
    for a in input:
        archivo += '\t'+ a + '\n'
        subA = a.split("=")
        archivo += '\tlista = [' + str(subA[0]) + '] \n'
        archivo += '\tfuncionIntermedia() \n'

    archivo += 'if __name__ == "__main__": \n'
    archivo += '\t main()'

    print('**************************************************')




    f.write(archivo)
    f.close()


