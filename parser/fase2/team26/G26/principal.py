import gramaticaF2 as g
import Utils.TablaSimbolos as table
import Utils.Lista as l
import Librerias.storageManager.jsonMode as storage
import Utils.Error as error
import Instrucciones.DML.select as select

storage.dropAll()
datos = l.Lista({}, '')
 

ruta = '../G26/entrada.txt'
f = open(ruta, "r")
input = f.read()

instrucciones = g.parse(input)
print(instrucciones['text'])

err = g.getMistakes()
for e in err:
    print(e.toString())
