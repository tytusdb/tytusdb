import hashlib
import json as js
import os

##############
# BLOCKCHAIN #
##############

def existeSeguridad(nombreTabla):
    ruta = "storageSafeTables/" + nombreTabla + ".json"
    return os.path.isfile(ruta)

def crearBlockchain(nombreTabla):
    ruta = "storageSafeTables/" + nombreTabla + ".json"
    
    file = open(ruta, "w+")
    file.write(js.dumps(['start']))
    file.close()

def insertarCSV(nombretabla, filepath, arregloDeInserciones):
    contador = 0
    ruta = "storageSafeTables/" + nombretabla + ".json"

    file = open(ruta, "r")
    listaBloques = js.loads(file.read())
    file.close()
    id = len(listaBloques) - 1

    anterior = '000000000000inicial0000000000000'
    if not id == 0:
        listaBloques.pop()
        anterior = listaBloques[id-1][3]

    archivoCSV = open(filepath, "r")
    for linea in archivoCSV:
        linea = linea.rstrip('\n')
        if arregloDeInserciones[contador] == 0:
            hashRegistroActual = __getHash(linea)
            if id == 0:
                DatosBloque = [0, linea, anterior, hashRegistroActual]
                listaBloques.pop()
            else:
                DatosBloque = [id, linea, anterior, hashRegistroActual]
            anterior = hashRegistroActual
            listaBloques.append(DatosBloque)
            id += 1
        contador += 1

    listaBloques.append([1000000, 'final', hashRegistroActual, hashRegistroActual])
    archivoCSV.close()
    file = open(ruta, "w+")
    file.write(js.dumps(listaBloques))
    file.close()

def insertarRegistrosSeguros(nombreTabla, registros):
    cadenaRegistros = ''
    contador = 0
    ruta = "storageSafeTables/" + nombreTabla + ".json"

    for dato in registros:
        if contador == len(registros) - 1:
            cadenaRegistros += str(dato)
        else:
            cadenaRegistros += (str(dato) + ',')
        contador += 1

    file = open(ruta, "r")
    listaBloques = js.loads(file.read())
    file.close()

    id = len(listaBloques)
    hashRegistroActual = __getHash(cadenaRegistros)
    if id == 1 and listaBloques[0] == 'start':
        DatosBloque = [0, cadenaRegistros, '000000000000inicial0000000000000', hashRegistroActual]
        listaBloques.pop()
    else:
        id -= 1
        DatosBloque = [id, cadenaRegistros, listaBloques[id-1][3], hashRegistroActual]
        listaBloques.pop()
    listaBloques.append(DatosBloque)
    listaBloques.append([1000000, 'final', hashRegistroActual, hashRegistroActual])
    file = open(ruta, "w+")
    file.write(js.dumps(listaBloques))
    file.close()

def eliminarTablaSegura(nombreTabla):
    ruta = "storageSafeTables/" + nombreTabla + ".json"
    os.remove(ruta)

def actualizarTablaSegura(nombreTabla, tuplaParaActualizar, tuplaActualizada):
    cadena = ''
    cadenaModificada = ''
    contador = 0
    ruta = "storageSafeTables/" + nombreTabla + ".json"

    for dato in tuplaParaActualizar:
        if contador == len(tuplaParaActualizar) - 1:
            cadena += str(dato)
        else:
            cadena += (str(dato) + ',')
        contador += 1
    contador = 0

    for dato in tuplaActualizada:
        if contador == len(tuplaParaActualizar) - 1:
            cadenaModificada += str(dato)
        else:
            cadenaModificada += (str(dato) + ',')
        contador += 1

    file = open(ruta, "r")
    listaBloques = js.loads(file.read())
    file.close()

    for bloque in listaBloques:
        if cadena == bloque[1]:
            bloque[1] = cadenaModificada
            bloque[3] = __getHash(cadenaModificada)
            file = open(ruta, "w+")
            file.write(js.dumps(listaBloques))
            file.close()
            break
    
def reporteBlockchain(database, table):
    try:
        if not database.isidentifier() \
        or not table.isidentifier():
            raise Exception()
        
        nombreTabla = database + '_' + table

        ruta = "storageSafeTables/" + nombreTabla + ".json"

        if os.path.exists(ruta):
            file = open(ruta, "r")
            listaBloques = js.loads(file.read())
            file.close()

            file = open('Bc.dot', "w")
            file.write("digraph g{\n")
            file.write("rankdir=LR\n")

            file.write(__getDot(listaBloques))

            file.write('}')
            file.close()

            os.system('dot -Tpng Bc.dot -o Bc.png')
            os.system('Bc.png')
        else:
            return 1

        return 0
    except:
        return 1

def __getDot(listaBloques):
    listaBloques = listaBloques

    dot = ""
    contador = 0
    hash_Correcto = True

    def replaceComillas(cadenaDatos):
        sinComillas = cadenaDatos.replace('"', "'")
        return sinComillas
    
    for bloque in listaBloques:
        if hash_Correcto:
            if contador == len(listaBloques)-1:
                pass
            elif bloque[3] == listaBloques[contador + 1][2]:
                dot += 'bloque' + str(contador) + ' [shape=record, style=filled, fillcolor=green, label="Block #:\\n' + str(bloque[0]) + ' | Data:\\n' + replaceComillas(str(bloque[1])) + ' | Prev:\\n' + str(bloque[2]) + ' | Hash:\\n' + str(bloque[3]) + '"];\n'
            else:
                dot += 'bloque' + str(contador) + ' [shape=record, style=filled, fillcolor=red, label="Block #:\\n' + str(bloque[0]) + ' | Data:\\n' + replaceComillas(str(bloque[1])) + ' | Prev:\\n' + str(bloque[2]) + ' | Hash:\\n' + str(bloque[3]) + '"];\n'
                hash_Correcto = False
        else:
            if not contador == len(listaBloques)-1:
                dot += 'bloque' + str(contador) + ' [shape=record, style=filled,fillcolor=red, label="Block #:\\n' + str(bloque[0]) + ' | Data:\\n' + replaceComillas(str(bloque[1])) + ' | Prev:\\n' + str(bloque[2]) + ' | Hash:\\n' + str(bloque[3]) + '"];\n'

        contador += 1

    for i in range(len(listaBloques) - 2):
        if not i == len(listaBloques)-1:
            dot += 'bloque' + str(i) + ' -> bloque' + str(i + 1) + "\n"

    return dot

#############
# Utilities #
#############

def __getHash(cadena):
    return hashlib.sha256(cadena.encode()).hexdigest()