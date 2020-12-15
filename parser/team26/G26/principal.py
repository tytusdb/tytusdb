import gramatica as g
import Utils.TablaSimbolos as table
import Utils.Lista as l

datos = l.Lista([], '')

ruta = '../G26/entrada.txt'
f = open(ruta, "r")
input = f.read()

instrucciones = g.parse(input)

#for instr in instrucciones :
#    instr.execute(datos)

#print (datos)
