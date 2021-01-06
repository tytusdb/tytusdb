import hashlib
import json as js
import os
import subprocess


def GenerarHash(cadena):
    return hashlib.sha256(cadena.encode()).hexdigest()


def DeleteSafeTable(nombreTabla, ruta):
    ruta = ruta + "\\SafeTables\\" + str(nombreTabla) + ".json"
    os.remove(ruta)


def CreateBlockChain(nombreTabla, ruta):

    ruta = ruta + "\\SafeTables\\" + str(nombreTabla) + ".json"
    file = open(ruta, "w+")
    file.write(js.dumps(['inicio']))
    file.close()


def EsUnaTablaSegura(nombreTabla, ruta):
    ruta = ruta + "\\SafeTables\\" + str(nombreTabla) + ".json"
    return os.path.isfile(ruta)


def updateSafeTable(nombreTabla, datos, datosmodificados, ruta):
    cadena = ''
    cadenaModificcada = ''
    contador = 0
    ruta = ruta + "\\SafeTables\\" + str(nombreTabla) + ".json"

    for dato in datos:
        if contador == len(datos) - 1:
            cadena += str(dato)
        else:
            cadena += (str(dato) + ',')
        contador += 1
    contador = 0

    for dato in datosmodificados:
        if contador == len(datos) - 1:
            cadenaModificcada += str(dato)
        else:
            cadenaModificcada += (str(dato) + ',')
        contador += 1

    file = open(ruta, "r")
    lista = js.loads(file.read())
    file.close()

    for bloque in lista:
        if cadena == bloque[1]:
            bloque[1] = cadenaModificcada
            bloque[3] = GenerarHash(cadenaModificcada)
            file = open(ruta, "w+")
            file.write(js.dumps(lista))
            file.close()
            return True


def insertCSV(nombretabla, rutaArchivo, ruta, retornos):
    contador = 0
    ruta = ruta + "\\SafeTables\\" + str(nombretabla) + ".json"

    file = open(ruta, "r")
    lista = js.loads(file.read())
    file.close()
    id = len(lista) - 1

    anterior = '000000000000000000'
    if not id == 0:
        lista.pop()
        anterior = lista[id-1][3]

    f = open(rutaArchivo, "r")
    for linea in f:
        linea = linea.rstrip('\n')
        if retornos[contador] == 0:
            h = GenerarHash(linea)
            if id == 0:
                DatosBloque = [0, linea, anterior, h]
                lista.pop()
            else:
                DatosBloque = [id, linea, anterior, h]
            anterior = h
            lista.append(DatosBloque)
            id += 1
        contador += 1

    lista.append([45612, 'datofinalParaComprobacionFinal', h, h])
    f.close()
    file = open(ruta, "w+")
    file.write(js.dumps(lista))
    file.close()


def insertSafeTable(nombreTabla, datos, ruta):
    cadena = ''
    contador = 0
    ruta = ruta + "\\SafeTables\\" + str(nombreTabla) + ".json"

    for dato in datos:
        if contador == len(datos) - 1:
            cadena += str(dato)
        else:
            cadena += (str(dato) + ',')
        contador += 1

    file = open(ruta, "r")
    lista = js.loads(file.read())
    file.close()

    id = len(lista)
    h = GenerarHash(cadena)
    if id == 1 and lista[0] == 'inicio':
        DatosBloque = [0, cadena, '000000000000000000', h]
        lista.pop()
    else:
        id -= 1
        DatosBloque = [id, cadena, lista[id-1][3], h]
        lista.pop()
    lista.append(DatosBloque)
    lista.append([45612, 'datofinalParaComprobacionFinal', h, h])
    file = open(ruta, "w+")
    file.write(js.dumps(lista))
    file.close()


def GraphSafeTable(nombreTabla, ruta):
    ruta = ruta + "\\SafeTables\\" + str(nombreTabla) + ".json"
    file = open(ruta, "r")
    lista = js.loads(file.read())
    file.close()

    file = open('BlockChain.dot', "w")
    file.write("graph grafica{" + os.linesep)
    file.write("rankdir=LR;" + os.linesep)
    contador = 0
    correcta = True
    for bloque in lista:
        if correcta:
            if contador == len(lista)-1:
                pass
            elif bloque[3] == lista[contador + 1][2]:
                file.write('bloque' + str(
                    contador) + ' [shape=record, style=bold,style=filled,fillcolor=lightblue,label="ID:\\n' + str(
                    bloque[0]) + ' | DATOS:\\n' + str(bloque[1]) + ' | ANTERIOR:\\n' + str(
                    bloque[2]) + ' | HASH:\\n' + str(bloque[3]) + '"];' + os.linesep)
            else:
                file.write('bloque' + str(
                    contador) + ' [shape=record, style=bold,style=filled,fillcolor=pink,label="ID:\\n' + str(
                    bloque[0]) + ' | DATOS:\\n' + str(bloque[1]) + ' | ANTERIOR:\\n' + str(
                    bloque[2]) + ' | HASH:\\n' + str(bloque[3]) + '"];' + os.linesep)
                correcta = False
        else:
            if not contador == len(lista)-1:
                file.write('bloque' + str(
                   contador) + ' [shape=record, style=bold,style=filled,fillcolor=pink,label="ID:\\n' + str(
                   bloque[0]) + ' | DATOS:\\n' + str(bloque[1]) + ' | ANTERIOR:\\n' + str(
                   bloque[2]) + ' | HASH:\\n' + str(bloque[3]) + '"];' + os.linesep)

        contador += 1

    for i in range(len(lista) - 2):
        if not i == len(lista)-1:
            file.write('bloque' + str(i) + ' -- bloque' + str(i + 1) + os.linesep)

    file.write('}')
    file.close()
    subprocess.call('dot -Tpng BlockChain.dot -o BlockChain.png')
    os.system('BlockChain.png')


listadedatos = [[1, 'pedro', '201901522'], [2, 'pedro1', '201901523'], [3, 'pedro2', '201901524'],
                [4, 'pedro3', '201901525'], [5, 'pedro4', '201901526'], [6, 'pedro5', '201901527'],
                [7, 'pedro6', '201901528']]

rutita = 'C:\\Users\\welma\\OneDrive\\Escritorio\\Cursos actuales\\EDD'
CreateBlockChain('prueba', rutita)


'''
GraphSafeTable('prueba', rutita)

if EsUnaTablaSegura('animales', rutita):
    updateSafeTable('animales', [sdf,fsfsd,sdfa], [fs,gaf,fsf], rutita)
else:
    print('No es una tabla segura')

input('stop')

if EsUnaTablaSegura('prueba', rutita):
    updateSafeTable('prueba', [5, 'pedro4', '201901526'], [6, 'JuanMecanico', 'TodoBien'], rutita)
else:
    print('No es una tabla segura')

GraphSafeTable('prueba', rutita)

if EsUnaTablaSegura('prueba', rutita):
    insertSafeTable('prueba', [89, 'este', 'DatoNuevo'], rutita)
else:
    print('No es una tabla segura')
'''