import gramatica as g
import Utils.TablaSimbolos as table
import Utils.Lista as l

import Librerias.storageManager.jsonMode as storage
import Utils.Error as error
import Instrucciones.DML.select as select


storage.dropAll()
datos = l.Lista({}, '')


def parsear(input_x):
    res = []

    fx = open("entrada.txt", "w")
    fx.write(input_x)
    fx.close()

    ruta = 'entrada.txt'
    f = open(ruta, "r")
    input = f.read()

    instrucciones = g.parse(input)
    for instr in instrucciones['ast']:
        if instr == None:
            continue
        result = instr.execute(datos)
        if isinstance(result, error.Error):
            print(result)
        elif isinstance(instr, select.Select):
            res.append(instr.ImprimirTabla(result))
            #print(instr.ImprimirTabla(result))
        else:
            res.append(result)

    #print(input)
    return '\n '.join([(str(elem)) for elem in res])

    #print('\n\nTABLA DE SIMBOLOS')
    #print(datos)

def otro():
    ruta = '../G26/entrada.txt'
    f = open(ruta, "r")
    input = f.read()

    instrucciones = g.parse(input)

    for instr in instrucciones['ast']:
        if instr == None:
            continue
        result = instr.execute(datos)
        if isinstance(result, error.Error):
            print(result)
        elif isinstance(instr, select.Select):
            print(instr.ImprimirTabla(result))
        else:
            print(result)

'''
ruta = '../G26/entrada.txt'
f = open(ruta, "r")
input = f.read()

instrucciones = g.parse(input)


for instr in instrucciones['ast']:
    if instr == None:
        continue
    result = instr.execute(datos)
    if isinstance(result, error.Error):
        print(result)
    elif isinstance(instr, select.Select):
        print(instr.ImprimirTabla(result))
    else:
        print(result)

print('\n\nTABLA DE SIMBOLOS')
print(datos)
'''

