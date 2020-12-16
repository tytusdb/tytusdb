import AVLtablas as ta
import AVLbase as ba
import os

class Main():
    os.system('cls')

    print(ba.b.createBase('Base 1')) #460
    print(ba.b.createBase('Base 2')) #461
    print(ba.b.createBase('Base 3')) #462
    print(ba.b.createBase('Base 2')) #461
    print(ba.b.createBase('Base 4')) #463
    print(ba.b.createBase('Base 7')) #466
    print(ba.b.createBase('Base 11')) #509
    print(ba.b.createBase('Base 12')) #510
    print('------------------------------')
    print(ta.t.createTable('Base 1', 'Nombre 1', 25)) #692   1
    print(ta.t.createTable('Base 4', 'Tabla 2', 15)) #566  2
    print(ta.t.createTable('Base 1', 'Tabla 1', 50)) #565   3
    print(ta.t.createTable('Base 2', 'Nombre', 8)) #611   4
    print(ta.t.createTable('Base 7', 'ya no', 15)) #471    5
    print(ta.t.createTable('Base 3', 'ya', 5)) #218    6
    print(ta.t.createTable('Base 1', 'ya', 45)) #922    7
    print('---------------------------------')
    #print(ba.b.alterDatabase('Base 1','Base 7777'))
    #print(ta.t.dropTable('Base 1', 'Yucas'))
    print('---------------------------------')
    print(ba.b.dropDatabase('Base 2'))

    ba.b.mostrarBasesConsola()
    ta.t.mostrarTablasConsola()
    #print(ba.b.showDataBases())