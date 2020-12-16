import gramatica as g
import Utils.TablaSimbolos as table
import Utils.Lista as l

#datos = l.Lista([], '')
datos = l.Lista({}, '')

#dic1 = { 'nombreBase1' : {'tablas' : [{'NombreTabla1': ['1.', '2', '3'] }], 'enum' : [], 'owner' : 'prueba', 'mode' : '1'}, 'nombreBase2' : [{'NombreTabla1': ['1.', '2', '3'] }] }
#database1 = dic1
#print(dic1)
#dic1['nombreBaseNueva'] = dic1.pop('nombreBase1')
#print(dic1)

#mm = 'hola'
#rr = { 'nombreBase1' : {'tablas' : [{'NombreTabla1': ['1.', '2', '3'] }], 'enum' : [], 'owner' : 'prueba', 'mode' : '1'}, 'nombreBase2' : [{'NombreTabla1': ['1.', '2', '3'] }] }
#dic1[mm] = rr

#print(dic1)

ruta = 'C:/Users/alvar/Desktop/entrada.txt'
f = open(ruta, "r")
input = f.read()

instrucciones = g.parse(input)
print(instrucciones)
#for instr in instrucciones :
    #print(instr.execute(datos))
    #instr.execute(datos)

#print('\n\nTABLA DE SIMBOLOS')
#print (datos)

g.grafo.showtree()